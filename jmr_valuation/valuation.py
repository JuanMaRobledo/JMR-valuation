"""Orquesta el pipeline completo: inputs de una empresa -> DCF (3 escenarios)
+ valoracion relativa (5 multiplos). Es el equivalente a abrir el Excel,
completar 'Input sheet' y mirar 'Resumen de Valoracion'.

Uso tipico:
    from jmr_valuation.io.inputs import load_company_inputs
    from jmr_valuation.valuation import run_valuation

    inputs = load_company_inputs("data/example_adbe.csv")
    report = run_valuation(inputs)
    print(report.summary())
"""
from __future__ import annotations

from dataclasses import dataclass

from jmr_valuation.io.inputs import CompanyInputs
from jmr_valuation.models import converters
from jmr_valuation.models.blend import BlendResult, MethodValues, run_blend
from jmr_valuation.models.dcf import (
    DcfResult,
    EquityBridgeResult,
    GrowthAndMarginPath,
    TerminalAssumptions,
    equity_value_bridge,
    run_dcf,
)
from jmr_valuation.models.financials_multiples import (
    HistoricalRatios,
    project_financials_multiples,
)
from jmr_valuation.models.options import dilution_adjusted_black_scholes
from jmr_valuation.models.relative import (
    ScenarioMultipleInputs,
    project_target_prices,
    resolve_anchor_multiple,
    sensitivity_matrix,
)

SCENARIOS = ("Conservador", "Base", "Optimista")
RELATIVE_METRICS = {
    # nombre -> (atributo de MultiplesYear a usar, prefijo de campos en CompanyInputs:
    # hist_multiple_<prefijo>_y1/y2/y3 + multiple_<prefijo> como override manual)
    "EV/FCFF": ("fcff", "ev_fcff"),
    "P/OCF": ("ocf", "p_ocf"),
    "P/E": ("net_income", "pe"),
    "P/FCFE": ("fcfe", "p_fcfe"),
    "EV/EBITDA": ("ebitda", "ev_ebitda"),
}


def _anchor_multiple(inputs: CompanyInputs, field_prefix: str) -> float:
    override_active = getattr(inputs, f"override_{field_prefix}")
    override_value = getattr(inputs, f"multiple_{field_prefix}") if override_active else None

    historical = [
        getattr(inputs, f"hist_multiple_{field_prefix}_y1"),
        getattr(inputs, f"hist_multiple_{field_prefix}_y2"),
        getattr(inputs, f"hist_multiple_{field_prefix}_y3"),
    ]
    if override_value is None and not any(historical):
        raise ValueError(
            f"Falta el multiplo para '{field_prefix}': completa hist_multiple_{field_prefix}_y1/y2/y3 "
            f"con los ultimos 3 anios del Excel (mediana), o activa override_{field_prefix} y "
            f"completa multiple_{field_prefix}."
        )
    return resolve_anchor_multiple(historical, override_value=override_value)


@dataclass(frozen=True)
class ScenarioResult:
    scenario: str
    dcf: DcfResult
    equity_bridge: EquityBridgeResult


@dataclass(frozen=True)
class ValuationReport:
    inputs: CompanyInputs
    ebit_adjustment: float          # de leasing/I+D, ya sumado al EBIT base usado en el DCF
    invested_capital_adjustment: float
    value_of_options: float
    scenarios: dict[str, ScenarioResult]
    relative: dict[str, dict[str, object]]  # metrica -> {escenario -> RelativeValuationResult}
    anchor_multiples: dict[str, float]      # metrica -> multiplo ancla resuelto (mediana 3a u override)
    sensitivity: dict[str, list[list[float]]]  # metrica -> matriz 5x5 (filas=multiplo, cols=metrica), escenario Base FY+3
    blend: BlendResult

    def summary(self) -> str:
        lines = [
            f"Valoracion DCF -- {self.inputs.company_name} ({self.inputs.ticker})",
            f"Precio actual: {self.inputs.current_price:,.2f}",
            "",
        ]
        for scenario in SCENARIOS:
            b = self.scenarios[scenario].equity_bridge
            lines.append(
                f"  {scenario:<12} valor/accion = {b.value_per_share:>10,.2f}"
                f"   (precio/valor = {b.price_as_pct_of_value:.1%})"
                if b.price_as_pct_of_value is not None else
                f"  {scenario:<12} valor/accion = {b.value_per_share:>10,.2f}"
            )
        lines.append("")
        lines.append("Valoracion relativa (precio objetivo FY+3, escenario Base):")
        for metric_name, by_scenario in self.relative.items():
            result = by_scenario["Base"]
            fy3 = result.years[-1]
            lines.append(f"  {metric_name:<10} ancla(mediana 3a)={self.anchor_multiples[metric_name]:6.2f}x  "
                         f"multiplo usado={result.multiple_fy1:6.2f}x  "
                         f"target FY+3={fy3.total_target_price:>10,.2f}  "
                         f"retorno total={fy3.total_return:+.1%}")
        lines.append("")
        lines.append(f"Indicador exploratorio mixto DCF hoy + múltiplos FY+3 (tipo: {self.blend.company_type}):")
        for scenario in SCENARIOS:
            price = self.blend.weighted_price_by_scenario[scenario]
            cagr = self.blend.cagr_3y_by_scenario[scenario]
            lines.append(f"  {scenario:<12} promedio mixto = {price:>10,.2f}   CAGR ilustrativo = {cagr:+.1%}")
        lines.append(f"  Precio con margen de seguridad sobre DCF Base de hoy ({self.inputs.margin_of_safety:.0%}): "
                     f"{self.blend.mos_price:,.2f}")
        tiers = self.blend.buy_price_tiers
        lines.append(f"  Bandas de compra -- Value: {tiers.value_min:,.2f}-{tiers.value_max:,.2f}  "
                     f"Deep Value: {tiers.deep_value_min:,.2f}-{tiers.deep_value_max:,.2f}  "
                     f"Historica: {tiers.historical_valuation_min:,.2f}-{tiers.historical_valuation_max:,.2f}")
        return "\n".join(lines)


def _resolve_ebit_and_invested_capital(inputs: CompanyInputs):
    ebit_adjustment = 0.0
    invested_capital_adjustment = 0.0

    if inputs.has_operating_leases:
        lease = converters.capitalize_operating_leases(
            current_year_lease_expense=inputs.lease_expense_current_year,
            commitments_years_1_to_5=[
                inputs.lease_commitment_y1, inputs.lease_commitment_y2,
                inputs.lease_commitment_y3, inputs.lease_commitment_y4, inputs.lease_commitment_y5,
            ],
            commitment_year_6_plus=inputs.lease_commitment_y6_plus,
            pretax_cost_of_debt=inputs.initial_cost_of_capital,  # aproximacion si no se corrio cost_of_capital aparte
        )
        ebit_adjustment += lease.ebit_adjustment
        invested_capital_adjustment += lease.debt_adjustment

    if inputs.capitalize_rd:
        past_rd = [
            inputs.rd_expense_year_minus_1, inputs.rd_expense_year_minus_2, inputs.rd_expense_year_minus_3,
            inputs.rd_expense_year_minus_4, inputs.rd_expense_year_minus_5, inputs.rd_expense_year_minus_6,
            inputs.rd_expense_year_minus_7, inputs.rd_expense_year_minus_8, inputs.rd_expense_year_minus_9,
        ]
        rd = converters.capitalize_rd(
            amortization_years=inputs.rd_amortization_years,
            current_year_rd_expense=inputs.rd_expense_current_year,
            past_years_rd_expense=past_rd,
            tax_rate=inputs.marginal_tax_rate,
        )
        ebit_adjustment += rd.ebit_adjustment
        invested_capital_adjustment += rd.research_asset_value

    return ebit_adjustment, invested_capital_adjustment


def _value_of_options(inputs: CompanyInputs) -> float:
    if not inputs.has_employee_options or inputs.n_options_outstanding <= 0:
        return 0.0
    result = dilution_adjusted_black_scholes(
        stock_price=inputs.current_price, strike_price=inputs.avg_strike_price,
        expiration_years=inputs.avg_option_maturity, volatility=inputs.stdev_stock_price,
        dividend_yield=(inputs.dividend_per_share_ltm / inputs.current_price) if inputs.current_price else 0.0,
        riskfree_rate=inputs.riskfree_rate, n_options=inputs.n_options_outstanding,
        n_shares=inputs.shares_outstanding,
    )
    return result.total_value


def _target_ebit_margin(inputs: CompanyInputs, scenario: str, initial_ebit_margin: float) -> float:
    """Replica 'Valuation output'!C45/C46/C47: el margen objetivo NO es un delta
    fijo sobre el actual -- Base usa el margen LTM (sin ajustar) tal cual,
    Conservador el minimo entre LTM/promedio 3a/5a/10a, y Optimista el maximo
    entre esos 4 y el margen actual (ya ajustado por leasing/I+D si corresponde).
    """
    historical = [inputs.ebit_margin_ltm, inputs.ebit_margin_avg_3y,
                  inputs.ebit_margin_avg_5y, inputs.ebit_margin_avg_10y]
    if not any(historical):
        # no hay margenes historicos cargados (CSV manual, no vino del Excel) --
        # fallback: target_ebit_margin +/- el delta fijo del escenario.
        delta = {"Base": 0.0, "Conservador": inputs.conservative_margin_delta,
                  "Optimista": inputs.optimistic_margin_delta}[scenario]
        return inputs.target_ebit_margin + delta

    if scenario == "Base":
        return inputs.ebit_margin_ltm
    if scenario == "Conservador":
        return min(historical)
    if scenario == "Optimista":
        return max(historical + [initial_ebit_margin])
    raise ValueError(f"Escenario desconocido: {scenario!r}")


def _growth_path(inputs: CompanyInputs, scenario: str, initial_ebit_margin: float) -> GrowthAndMarginPath:
    if scenario == "Base":
        growth_delta = 0.0
    elif scenario == "Conservador":
        growth_delta = inputs.conservative_growth_delta
    elif scenario == "Optimista":
        growth_delta = inputs.optimistic_growth_delta
    else:
        raise ValueError(f"Escenario desconocido: {scenario!r}")

    return GrowthAndMarginPath(
        year1_growth=inputs.revenue_growth_next_year + growth_delta,
        years_2_to_5_growth=inputs.revenue_growth_years_2_to_5 + growth_delta,
        target_ebit_margin=_target_ebit_margin(inputs, scenario, initial_ebit_margin),
        year_of_margin_convergence=inputs.year_of_margin_convergence,
    )


def run_valuation(inputs: CompanyInputs) -> ValuationReport:
    ebit_adjustment, invested_capital_adjustment = _resolve_ebit_and_invested_capital(inputs)
    value_of_options = _value_of_options(inputs)

    base_ebit = inputs.ebit_ltm + ebit_adjustment
    invested_capital_base = (
        inputs.book_value_equity_ltm + inputs.book_value_debt_ltm - inputs.cash_ltm
        + invested_capital_adjustment
    )
    initial_ebit_margin = base_ebit / inputs.revenue_ltm

    ratios = HistoricalRatios(
        interest_pct_of_ebit=inputs.hist_interest_pct_of_ebit,
        da_pct_of_revenue=inputs.hist_da_pct_of_revenue,
        capex_pct_of_revenue=inputs.hist_capex_pct_of_revenue,
        nwc_change_pct_of_revenue_growth=inputs.hist_nwc_pct_of_revenue_growth,
        net_borrowing_pct_of_revenue=inputs.hist_net_borrowing_pct_of_revenue,
        shares_growth_rate=inputs.hist_shares_growth_rate,
        dividend_growth_rate=inputs.hist_dividend_growth_rate,
    )

    scenarios: dict[str, ScenarioResult] = {}
    multiples_by_scenario = {}

    for scenario in SCENARIOS:
        growth = _growth_path(inputs, scenario, initial_ebit_margin)
        terminal = TerminalAssumptions(riskfree_rate=inputs.riskfree_rate)

        dcf_result = run_dcf(
            base_revenue=inputs.revenue_ltm, base_ebit=base_ebit, growth_path=growth,
            initial_ebit_margin=initial_ebit_margin, initial_cost_of_capital=inputs.initial_cost_of_capital,
            terminal=terminal, initial_tax_rate=inputs.effective_tax_rate,
            marginal_tax_rate=inputs.marginal_tax_rate, tax_rate_converges_to_marginal=True,
            sales_to_capital_years_1_5=inputs.sales_to_capital_years_1_5,
            sales_to_capital_years_6_10=inputs.sales_to_capital_years_6_10,
            invested_capital_base=invested_capital_base, nol_carryforward=inputs.nol_carryforward,
        )
        bridge = equity_value_bridge(
            dcf_result, book_value_debt=inputs.book_value_debt_ltm,
            minority_interests=inputs.minority_interests, cash=inputs.cash_ltm,
            non_operating_assets=inputs.cross_holdings_ltm, shares_outstanding=inputs.shares_outstanding,
            value_of_options=value_of_options, current_price=inputs.current_price,
        )
        scenarios[scenario] = ScenarioResult(scenario=scenario, dcf=dcf_result, equity_bridge=bridge)

        # Los múltiplos y el DCF parten de la misma fecha y base LTM.
        # Proyectar desde el último FY cerrado daba ventas FY+1 distintas
        # para el mismo crecimiento y mezclaba horizontes al ponderarlos.
        multiples_by_scenario[scenario] = project_financials_multiples(
            base_year_revenue=inputs.revenue_ltm, base_year_shares_diluted=inputs.shares_outstanding,
            base_year_dividend_per_share=inputs.dividend_per_share_ltm,
            year_projections=dcf_result.years[:3], ratios=ratios,
        )

    relative: dict[str, dict[str, object]] = {}
    anchor_multiples: dict[str, float] = {}
    ev_bridge = (inputs.book_value_debt_ltm + inputs.minority_interests + value_of_options
                 - inputs.cash_ltm - inputs.cross_holdings_ltm)
    for metric_name, (attr, field_prefix) in RELATIVE_METRICS.items():
        anchor_multiple = _anchor_multiple(inputs, field_prefix)
        anchor_multiples[metric_name] = anchor_multiple
        by_scenario = {}
        for scenario in SCENARIOS:
            fm_years = multiples_by_scenario[scenario]
            scenario_inputs = ScenarioMultipleInputs(
                scenario=scenario, historical_median_multiple=anchor_multiple,
                metric_fy1=getattr(fm_years[0], attr), metric_fy2=getattr(fm_years[1], attr),
                metric_fy3=getattr(fm_years[2], attr), shares_or_ev_divisor=inputs.shares_outstanding,
                projected_shares=tuple(y.shares_diluted for y in fm_years),
                ev_to_equity_adjustment=ev_bridge if metric_name.startswith("EV/") else 0.0,
                cumulative_dividends_fy1=fm_years[0].cumulative_dividends_per_share,
                cumulative_dividends_fy2=fm_years[1].cumulative_dividends_per_share,
                cumulative_dividends_fy3=fm_years[2].cumulative_dividends_per_share,
            )
            by_scenario[scenario] = project_target_prices(metric_name, inputs.current_price, scenario_inputs)
        relative[metric_name] = by_scenario

    sensitivity: dict[str, list[list[float]]] = {}
    for metric_name, by_scenario in relative.items():
        fy3_base = by_scenario["Base"].years[-1]
        sensitivity[metric_name] = sensitivity_matrix(
            base_multiple_fy3=fy3_base.multiple, base_metric_fy3=fy3_base.metric,
            shares_or_ev_divisor=multiples_by_scenario["Base"][2].shares_diluted,
            ev_to_equity_adjustment=ev_bridge if metric_name.startswith("EV/") else 0.0,
        )

    values_by_scenario = {
        scenario: MethodValues(
            dcf_damodaran=scenarios[scenario].equity_bridge.value_per_share,
            ev_ebitda=relative["EV/EBITDA"][scenario].years[-1].total_target_price,
            ev_fcff=relative["EV/FCFF"][scenario].years[-1].total_target_price,
            pe=relative["P/E"][scenario].years[-1].total_target_price,
            p_fcfe=relative["P/FCFE"][scenario].years[-1].total_target_price,
            p_ocf=relative["P/OCF"][scenario].years[-1].total_target_price,
        )
        for scenario in SCENARIOS
    }
    included_methods = {
        "DCF Damodaran": inputs.include_dcf, "EV/EBITDA": inputs.include_ev_ebitda,
        "EV/FCFF": inputs.include_ev_fcff, "P/E": inputs.include_pe,
        "P/FCFE": inputs.include_p_fcfe, "P/OCF": inputs.include_p_ocf,
    }
    blend = run_blend(
        company_type=inputs.company_type, current_price=inputs.current_price,
        values_by_scenario=values_by_scenario, margin_of_safety=inputs.margin_of_safety,
        included_methods=included_methods,
    )

    return ValuationReport(
        inputs=inputs, ebit_adjustment=ebit_adjustment,
        invested_capital_adjustment=invested_capital_adjustment, value_of_options=value_of_options,
        scenarios=scenarios, relative=relative, anchor_multiples=anchor_multiples,
        sensitivity=sensitivity, blend=blend,
    )
