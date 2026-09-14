#!/usr/bin/env python
"""Corre el pipeline completo para un ticker: SEC EDGAR (historico 10y) +
yfinance (precio, comps) -> Motor de Supuestos v2 -> DCF (3 escenarios) ->
Google Sheets.

Uso minimo (risk-free rate y WACC se auto-derivan de datos de mercado reales
-- Treasury 10y y CAPM+synthetic rating, ver mas abajo):
    python scripts/run_pipeline.py ADBE \
        --industry-us "Software (System & Application)" \
        --industry-global "Software (System & Application)" \
        --peers INTU MSFT ORCL ADSK CRM SAP NOW

Lo unico que NO se auto-deriva (y no deberia, ver docstrings de
comps_loader.py y assumptions_engine.py): la industria Damodaran (--industry-us/
--industry-global, tiene que coincidir con un nombre exacto de
reference/industry_averages_*.csv) y el set de peers (--peers). Pasa
--riskfree-rate/--wacc para pisar el valor automatico.

El sheet destino se toma de GOOGLE_SHEET_ID en .env, salvo --sheet-id.
"""
from __future__ import annotations

import argparse
import sys

from jmr_valuation.io import reference_data as ref
from jmr_valuation.io.comps_loader import load_comps_table
from jmr_valuation.io.market_data import current_riskfree_rate
from jmr_valuation.io.sec_edgar_loader import (
    load_annual_series_from_sec_edgar,
    load_company_inputs_from_sec_edgar,
)
from jmr_valuation.io.sheets_auth import get_gspread_client, open_target_sheet
from jmr_valuation.io.sheets_writer import ScenarioOutput, write_full_valuation
from jmr_valuation.io.yfinance_client import YFinanceError, get_market_snapshot
from jmr_valuation.models.assumptions_engine import (
    SCENARIOS,
    FundamentalGrowthInputs,
    growth_and_margin_path,
    resolve_sales_to_capital,
    run_assumptions_engine,
    terminal_assumptions,
)
from jmr_valuation.models.cost_of_capital import cost_of_debt_synthetic_rating, cost_of_equity, wacc as compute_wacc
from jmr_valuation.models.dcf import equity_value_bridge, run_dcf
from jmr_valuation.models.financials_multiples import HistoricalRatios, project_financials_multiples
from jmr_valuation.models.relative import ScenarioMultipleInputs, project_target_prices

# metrica -> (atributo de MultiplesYear a usar, campo de PeerMultiples/CompsTable
# con el multiplo ancla). Mismos 5 metodos que las hojas EV/FCFF, P/OCF, P/E,
# P/FCFE, EV/EBITDA del Excel original -- el ancla ahora es la mediana de los
# PEERS (no el propio historico de precios de la empresa, que no tenemos).
RELATIVE_METRICS = {
    "EV/FCFF": ("fcff", "ev_fcf"),
    "P/OCF": ("ocf", "p_ocf"),
    "P/E": ("net_income", "pe"),
    "P/FCFE": ("fcfe", "p_fcf"),
    "EV/EBITDA": ("ebitda", "ev_ebitda"),
}


def run(
    ticker: str, *, industry_us: str, industry_global: str, peer_tickers: list[str] | None,
    riskfree_rate: float | None, wacc: float | None, tax_rate: float | None, sheet_id: str | None,
) -> None:
    print(f"[1/5] Descargando historico de 10y de {ticker} desde SEC EDGAR...")
    series = load_annual_series_from_sec_edgar(ticker)
    print(f"      {len(series.fiscal_year_ends)} años fiscales encontrados "
          f"({series.fiscal_year_ends[0]} a {series.fiscal_year_ends[-1]})")

    print(f"[2/5] Consultando precio/market cap de {ticker} en yfinance...")
    market = get_market_snapshot(ticker)
    print(f"      Precio actual: {market.current_price:,.2f}")

    if riskfree_rate is None:
        riskfree_rate = current_riskfree_rate()
        print(f"      Risk-free rate (10y Treasury, auto): {riskfree_rate:.2%}")

    # Tasa impositiva efectiva y minority interests reales (no se inventan):
    # mismo loader que ya calcula esto desde IncomeTaxExpenseBenefit/pretax
    # income de SEC EDGAR -- se reusa en vez de duplicar el parseo XBRL. El
    # placeholder de wacc aca abajo no se usa para nada mas que completar el
    # dataclass -- el WACC real (auto o manual) se resuelve despues, porque
    # el enfoque automatico necesita ebit_ltm/interest_expense_ltm que recien
    # entrega este mismo loader (dependencia circular resuelta con un valor
    # provisorio que nunca se lee).
    company_inputs = load_company_inputs_from_sec_edgar(
        ticker, current_price=market.current_price, riskfree_rate=riskfree_rate,
        initial_cost_of_capital=wacc if wacc is not None else riskfree_rate + 0.05,
    )
    effective_tax_rate = tax_rate if tax_rate is not None else company_inputs.effective_tax_rate
    minority_interests = company_inputs.minority_interests * 1_000_000  # esa funcion trabaja en millones

    if wacc is None:
        if market.beta is None:
            raise YFinanceError(
                f"yfinance no trae beta para {ticker!r} -- no se puede calcular el WACC "
                "automaticamente. Pasa --wacc manualmente."
            )
        cost_of_debt = cost_of_debt_synthetic_rating(
            ebit=company_inputs.ebit_ltm, interest_expense=company_inputs.interest_expense_ltm,
            riskfree_rate=riskfree_rate,
        )
        coe = cost_of_equity(riskfree_rate, market.beta, ref.mature_market_erp())
        debt_for_wacc = company_inputs.book_value_debt_ltm * 1_000_000  # a $ crudos, ver nota de unidades abajo
        wacc = compute_wacc(
            market_value_equity=market.market_cap, market_value_debt=debt_for_wacc,
            cost_of_equity_=coe, cost_of_debt_pretax=cost_of_debt, tax_rate=effective_tax_rate,
        ).wacc
        print(f"      WACC (auto: CAPM + synthetic rating): {wacc:.2%} "
              f"(beta={market.beta:.2f}, Ke={coe:.2%}, Kd={cost_of_debt:.2%})")

    # Crecimiento fundamental de Damodaran (g = Reinvestment Rate x ROIC),
    # usando los mismos numeros ya parseados de EDGAR -- ver assumptions_engine.
    fundamental_inputs = FundamentalGrowthInputs(
        ebit_ltm=company_inputs.ebit_ltm, effective_tax_rate=effective_tax_rate,
        revenue_ltm=company_inputs.revenue_ltm, book_value_equity_ltm=company_inputs.book_value_equity_ltm,
        book_value_debt_ltm=company_inputs.book_value_debt_ltm, cash_ltm=company_inputs.cash_ltm,
        hist_capex_pct_of_revenue=company_inputs.hist_capex_pct_of_revenue,
        hist_da_pct_of_revenue=company_inputs.hist_da_pct_of_revenue,
        capitalize_rd=company_inputs.capitalize_rd, rd_amortization_years=company_inputs.rd_amortization_years,
        rd_expense_current_year=company_inputs.rd_expense_current_year,
        rd_expense_past_years=(
            company_inputs.rd_expense_year_minus_1, company_inputs.rd_expense_year_minus_2,
            company_inputs.rd_expense_year_minus_3, company_inputs.rd_expense_year_minus_4,
            company_inputs.rd_expense_year_minus_5, company_inputs.rd_expense_year_minus_6,
            company_inputs.rd_expense_year_minus_7, company_inputs.rd_expense_year_minus_8,
            company_inputs.rd_expense_year_minus_9,
        ),
    )

    comps = None
    if peer_tickers:
        print(f"[3/5] Armando tabla de comparables ({', '.join(peer_tickers)})...")
        comps = load_comps_table(peer_tickers)
    else:
        print("[3/5] Sin peers -- se omite la tabla de comparables (pasa --peers para incluirla).")

    print("[4/5] Corriendo Motor de Supuestos v2 + DCF para Conservador/Base/Optimista...")
    stc = resolve_sales_to_capital(industry_global=industry_global)
    long_term_debt_ltm = series.long_term_debt[-1]
    current_debt_ltm = series.current_debt[-1]
    cash_ltm = series.cash[-1]
    debt_ltm = long_term_debt_ltm + current_debt_ltm
    # Invested capital = book value equity + deuda - caja. No tenemos equity book value
    # en AnnualSeries (no hace falta para el motor de supuestos), asi que usamos la
    # aproximacion Damodaran de "capital invertido = deuda + valor de mercado del equity
    # - caja" solo para el ROIC de referencia; el DCF en si usa invested_capital_base
    # como semilla de ROIC año 1, que es menos sensible que el resto de los supuestos.
    invested_capital_base = debt_ltm + market.market_cap - cash_ltm

    # Ratios historicos reales para proyectar FCFF/OCF/FCFE/EBITDA (mismo
    # loader que ya parseo esto de EDGAR -- ver load_company_inputs_from_sec_edgar).
    historical_ratios = HistoricalRatios(
        interest_pct_of_ebit=company_inputs.hist_interest_pct_of_ebit,
        da_pct_of_revenue=company_inputs.hist_da_pct_of_revenue,
        capex_pct_of_revenue=company_inputs.hist_capex_pct_of_revenue,
        nwc_change_pct_of_revenue_growth=company_inputs.hist_nwc_pct_of_revenue_growth,
        net_borrowing_pct_of_revenue=company_inputs.hist_net_borrowing_pct_of_revenue,
        shares_growth_rate=company_inputs.hist_shares_growth_rate,
        dividend_growth_rate=company_inputs.hist_dividend_growth_rate,
    )

    scenarios: list[ScenarioOutput] = []
    for scenario in SCENARIOS:
        assumptions = run_assumptions_engine(
            series, scenario, industry_us=industry_us, industry_global=industry_global, sales_to_capital=stc,
            fundamental_inputs=fundamental_inputs,
        )
        growth_path = growth_and_margin_path(assumptions)
        terminal = terminal_assumptions(assumptions, riskfree_rate=riskfree_rate, wacc_current=wacc)

        dcf_result = run_dcf(
            base_revenue=series.ltm_revenue, base_ebit=series.ltm_ebit, growth_path=growth_path,
            initial_ebit_margin=assumptions.margin.ebit_margin_actual, initial_cost_of_capital=wacc,
            terminal=terminal, initial_tax_rate=effective_tax_rate, marginal_tax_rate=0.25,
            tax_rate_converges_to_marginal=True, sales_to_capital_years_1_5=assumptions.sales_to_capital_1_5,
            sales_to_capital_years_6_10=assumptions.sales_to_capital_6_10, invested_capital_base=invested_capital_base,
            growth_convergence_years=assumptions.weights.growth_convergence_years,
        )
        bridge = equity_value_bridge(
            dcf_result, book_value_debt=debt_ltm, minority_interests=minority_interests, cash=cash_ltm,
            non_operating_assets=0.0, shares_outstanding=market.shares_outstanding, current_price=market.current_price,
        )

        relative = None
        if comps is not None:
            fm_years = project_financials_multiples(
                base_year_revenue=series.revenue[-1], base_year_shares_diluted=market.shares_outstanding,
                base_year_dividend_per_share=company_inputs.dividend_per_share_ltm,
                year_projections=dcf_result.years[:3], ratios=historical_ratios,
            )
            relative = {}
            for metric_name, (attr, comps_field) in RELATIVE_METRICS.items():
                anchor = comps.median.get(comps_field)
                if anchor is None:
                    continue  # peers no traen este multiplo (yfinance no lo devolvio) -- no se inventa
                scenario_inputs = ScenarioMultipleInputs(
                    scenario=scenario, historical_median_multiple=anchor,
                    metric_fy1=getattr(fm_years[0], attr), metric_fy2=getattr(fm_years[1], attr),
                    metric_fy3=getattr(fm_years[2], attr), shares_or_ev_divisor=market.shares_outstanding,
                    cumulative_dividends_fy1=fm_years[0].cumulative_dividends_per_share,
                    cumulative_dividends_fy2=fm_years[1].cumulative_dividends_per_share,
                    cumulative_dividends_fy3=fm_years[2].cumulative_dividends_per_share,
                )
                relative[metric_name] = project_target_prices(metric_name, market.current_price, scenario_inputs)

        scenarios.append(ScenarioOutput(scenario=scenario, assumptions=assumptions, dcf=dcf_result, bridge=bridge, relative=relative))
        print(f"      {scenario:<12} valor/accion (DCF) = {bridge.value_per_share:>10,.2f}")

    print("[5/5] Escribiendo a Google Sheets...")
    client = get_gspread_client()
    sh = open_target_sheet(client, sheet_id)
    write_full_valuation(
        sh, ticker=ticker, company_name=series.company_name, current_price=market.current_price,
        series=series, comps=comps, scenarios=scenarios,
    )
    print(f"      Listo: {sh.url}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ticker")
    parser.add_argument("--industry-us", required=True)
    parser.add_argument("--industry-global", required=True)
    parser.add_argument("--peers", nargs="*", default=None)
    parser.add_argument("--riskfree-rate", type=float, default=None,
                         help="Si se omite, se toma el rendimiento actual del Treasury 10y (yfinance ^TNX).")
    parser.add_argument("--wacc", type=float, default=None,
                         help="Si se omite, se calcula via CAPM (beta de yfinance) + costo de deuda por "
                              "synthetic rating -- ver models/cost_of_capital.py.")
    parser.add_argument("--tax-rate", type=float, default=None)
    parser.add_argument("--sheet-id", default=None)
    args = parser.parse_args(argv)

    run(
        args.ticker.upper(), industry_us=args.industry_us, industry_global=args.industry_global,
        peer_tickers=args.peers, riskfree_rate=args.riskfree_rate, wacc=args.wacc,
        tax_rate=args.tax_rate, sheet_id=args.sheet_id,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
