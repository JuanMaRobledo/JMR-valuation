"""Escribe el resultado del pipeline a un Google Sheet: pestañas "Datos"
(historico crudo + comps), "Supuestos" (Motor de Supuestos v2 por escenario)
y "Resumen" (valor por accion por escenario). Cada corrida BORRA y reescribe
estas 3 pestañas -- no acumula versiones viejas (ver instrucciones del
pipeline)."""
from __future__ import annotations

from dataclasses import dataclass

import gspread

from jmr_valuation.io.comps_loader import CompsTable
from jmr_valuation.io.sec_edgar_loader import AnnualSeries
from jmr_valuation.io.yfinance_client import MarketSnapshot
from jmr_valuation.models.assumptions_engine import AssumptionsEngineResult
from jmr_valuation.models.dcf import DcfResult, EquityBridgeResult

_TAB_DATOS = "Datos"
_TAB_SUPUESTOS = "Supuestos"
_TAB_RESUMEN = "Resumen"


@dataclass(frozen=True)
class ScenarioOutput:
    scenario: str
    assumptions: AssumptionsEngineResult
    dcf: DcfResult
    bridge: EquityBridgeResult


def _get_or_create_worksheet(sh: gspread.Spreadsheet, title: str, rows: int = 200, cols: int = 20) -> gspread.Worksheet:
    try:
        ws = sh.worksheet(title)
        ws.clear()
        return ws
    except gspread.exceptions.WorksheetNotFound:
        return sh.add_worksheet(title=title, rows=rows, cols=cols)


def _pct(x: float | None) -> str:
    return "" if x is None else f"{x:.2%}"


def _num(x: float | None) -> str:
    return "" if x is None else f"{x:,.2f}"


def write_datos_tab(sh: gspread.Spreadsheet, series: AnnualSeries, comps: CompsTable | None) -> None:
    ws = _get_or_create_worksheet(sh, _TAB_DATOS)
    rows: list[list] = [
        [f"Datos historicos -- {series.company_name} ({series.ticker})"],
        ["Fuente: SEC EDGAR (XBRL company facts), hasta 10 años fiscales + LTM."],
        [],
        ["Concepto"] + series.fiscal_year_ends + ["LTM"],
        ["Revenue ($mm)"] + [v / 1e6 for v in series.revenue] + [series.ltm_revenue / 1e6],
        ["EBIT ($mm)"] + [v / 1e6 for v in series.ebit] + [series.ltm_ebit / 1e6],
        ["D&A ($mm)"] + [v / 1e6 for v in series.da] + [series.ltm_da / 1e6],
        ["Shares Outstanding (mm)"] + [v / 1e6 for v in series.shares_outstanding] + [""],
        ["Deuda LP ($mm)"] + [v / 1e6 for v in series.long_term_debt] + [""],
        ["Deuda corriente ($mm)"] + [v / 1e6 for v in series.current_debt] + [""],
        ["Caja ($mm)"] + [v / 1e6 for v in series.cash] + [""],
    ]

    if comps is not None:
        rows += [[], ["Comparables (peers)"],
                  ["Ticker", "Empresa", "Market Cap", "Gross Margin", "Fwd P/E", "P/E", "EV/FCF",
                   "P/FCF", "EV/EBITDA", "P/OCF", "Op. Margin", "Rev CAGR 3Y", "Rev CAGR 5Y", "Rev CAGR 10Y"]]
        for p in comps.peers:
            rows.append([
                p.ticker, p.company_name, _num(p.market_cap), _pct(p.gross_margin), _num(p.forward_pe),
                _num(p.pe), _num(p.ev_fcf), _num(p.p_fcf), _num(p.ev_ebitda), _num(p.p_ocf),
                _pct(p.operating_margin), _pct(p.revenue_cagr_3y), _pct(p.revenue_cagr_5y), _pct(p.revenue_cagr_10y),
            ])
        rows.append(["Promedio", ""] + [
            _num(comps.average.get(f)) if f not in ("gross_margin", "operating_margin",
                "revenue_cagr_3y", "revenue_cagr_5y", "revenue_cagr_10y") else _pct(comps.average.get(f))
            for f in ("market_cap", "gross_margin", "forward_pe", "pe", "ev_fcf", "p_fcf",
                      "ev_ebitda", "p_ocf", "operating_margin", "revenue_cagr_3y", "revenue_cagr_5y", "revenue_cagr_10y")
        ])

    ws.update(values=rows, range_name="A1")


def write_supuestos_tab(
    sh: gspread.Spreadsheet, ticker: str, company_name: str, scenarios: list[ScenarioOutput],
) -> None:
    ws = _get_or_create_worksheet(sh, _TAB_SUPUESTOS)
    rows: list[list] = [
        [f"Motor de Supuestos v2 -- {company_name} ({ticker})"],
        [],
        ["Métrica"] + [s.scenario for s in scenarios],
        ["-- Crecimiento --"],
        ["Crecimiento LTM"] + [_pct(s.assumptions.growth.ltm_growth) for s in scenarios],
        ["CAGR 3 años"] + [_pct(s.assumptions.growth.cagr_3y) for s in scenarios],
        ["CAGR 5 años"] + [_pct(s.assumptions.growth.cagr_5y) for s in scenarios],
        [f"CAGR largo plazo"] + [_pct(s.assumptions.growth.cagr_long) for s in scenarios],
        ["Crecimiento industria (US)"] + [_pct(s.assumptions.growth.industry_growth_us) for s in scenarios],
        ["Crecimiento industria (Global)"] + [_pct(s.assumptions.growth.industry_growth_global) for s in scenarios],
        ["Crecimiento historico combinado"] + [_pct(s.assumptions.growth.combined_historical) for s in scenarios],
        ["Crecimiento Año 1 (usado en el DCF)"] + [_pct(s.assumptions.growth.growth_year1) for s in scenarios],
        ["Años convergencia crecimiento"] + [s.assumptions.weights.growth_convergence_years for s in scenarios],
        ["-- Margen EBIT --"],
        ["Margen EBIT actual (LTM)"] + [_pct(s.assumptions.margin.ebit_margin_actual) for s in scenarios],
        ["Mediana margen EBIT (5y)"] + [_pct(s.assumptions.margin.ebit_margin_median_5y) for s in scenarios],
        ["Margen industria (US)"] + [_pct(s.assumptions.margin.industry_margin_us) for s in scenarios],
        ["Margen industria (Global)"] + [_pct(s.assumptions.margin.industry_margin_global) for s in scenarios],
        ["Margen objetivo (usado en el DCF)"] + [_pct(s.assumptions.margin.target_ebit_margin) for s in scenarios],
        ["Años convergencia margen"] + [s.assumptions.weights.margin_convergence_years for s in scenarios],
        ["-- Reinversión --"],
        ["Sales-to-Capital años 1-5"] + [_num(s.assumptions.sales_to_capital_1_5) for s in scenarios],
        ["Sales-to-Capital años 6-10"] + [_num(s.assumptions.sales_to_capital_6_10) for s in scenarios],
        ["-- Resultado DCF --"],
        ["Enterprise Value ($mm)"] + [_num(s.dcf.value_of_operating_assets) for s in scenarios],
        ["Valor por acción"] + [_num(s.bridge.value_per_share) for s in scenarios],
    ]
    ws.update(values=rows, range_name="A1")


def write_resumen_tab(
    sh: gspread.Spreadsheet, ticker: str, company_name: str, current_price: float, scenarios: list[ScenarioOutput],
) -> None:
    ws = _get_or_create_worksheet(sh, _TAB_RESUMEN)
    rows: list[list] = [
        [f"Resumen de Valoración -- {company_name} ({ticker})"],
        ["Precio actual (mercado)", _num(current_price)],
        [],
        ["Escenario", "Valor por acción", "Precio / Valor", "Upside / (Downside)"],
    ]
    for s in scenarios:
        upside = (s.bridge.value_per_share / current_price - 1) if current_price else None
        rows.append([
            s.scenario, _num(s.bridge.value_per_share), _pct(s.bridge.price_as_pct_of_value), _pct(upside),
        ])
    ws.update(values=rows, range_name="A1")


def write_full_valuation(
    sh: gspread.Spreadsheet, *, ticker: str, company_name: str, current_price: float,
    series: AnnualSeries, comps: CompsTable | None, scenarios: list[ScenarioOutput],
) -> None:
    write_datos_tab(sh, series, comps)
    write_supuestos_tab(sh, ticker, company_name, scenarios)
    write_resumen_tab(sh, ticker, company_name, current_price, scenarios)
