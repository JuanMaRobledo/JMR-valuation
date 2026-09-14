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
from jmr_valuation.models.relative import RelativeValuationResult

_TAB_DATOS = "Datos"
_TAB_SUPUESTOS = "Supuestos"
_TAB_MULTIPLOS = "Multiplos"
_TAB_RESUMEN = "Resumen"

# Orden de presentacion de los 5 metodos de valoracion relativa (mismos 5 que
# las hojas EV/FCFF, P/OCF, P/E, P/FCFE, EV/EBITDA del Excel original).
RELATIVE_METRIC_ORDER = ("EV/FCFF", "P/OCF", "P/E", "P/FCFE", "EV/EBITDA")


@dataclass(frozen=True)
class ScenarioOutput:
    scenario: str
    assumptions: AssumptionsEngineResult
    dcf: DcfResult
    bridge: EquityBridgeResult
    relative: dict[str, RelativeValuationResult] | None = None  # metrica -> resultado (None si no hay comps)


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
        ["Reinvestment Rate LTM (Damodaran)"] + [
            _pct(s.assumptions.growth.fundamental.reinvestment_rate) if s.assumptions.growth.fundamental else "n/d"
            for s in scenarios
        ],
        ["ROIC LTM (Damodaran)"] + [
            _pct(s.assumptions.growth.fundamental.roic) if s.assumptions.growth.fundamental else "n/d"
            for s in scenarios
        ],
        ["Crecimiento fundamental = RR x ROIC"] + [
            _pct(s.assumptions.growth.fundamental.fundamental_growth) if s.assumptions.growth.fundamental else "n/d"
            for s in scenarios
        ],
        ["  (I+D capitalizado en el calculo)"] + [
            ("Si" if s.assumptions.growth.fundamental.rd_adjusted else "No") if s.assumptions.growth.fundamental else "n/d"
            for s in scenarios
        ],
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
        # OJO: value_of_operating_assets esta en $ crudos, no en millones -- el
        # pipeline corre todo en $ (series.ltm_revenue/ltm_ebit de AnnualSeries
        # NO estan en millones, a diferencia de CompanyInputs). "Valor por
        # accion" da bien igual (EV $ / shares crudas = $/accion correcto).
        ["Enterprise Value ($)"] + [_num(s.dcf.value_of_operating_assets) for s in scenarios],
        ["Valor por acción"] + [_num(s.bridge.value_per_share) for s in scenarios],
    ]
    ws.update(values=rows, range_name="A1")


def write_multiplos_tab(
    sh: gspread.Spreadsheet, ticker: str, company_name: str, scenarios: list[ScenarioOutput],
) -> None:
    """Valoracion relativa por multiplos de comparables (equivalente a las 5
    hojas EV/FCFF, P/OCF, P/E, P/FCFE, EV/EBITDA del Excel): el multiplo ancla
    es la MEDIANA de los peers (no el propio historico de la empresa, que no
    tenemos con precios historicos reales) x el ajuste +/-10% por escenario
    que ya trae `models.relative` (Conservador=0.9x, Base=1.0x, Optimista=1.1x
    la mediana). Se omite si no se paso una lista de peers al pipeline."""
    ws = _get_or_create_worksheet(sh, _TAB_MULTIPLOS)
    if not any(s.relative for s in scenarios):
        ws.update(values=[
            [f"Valoración relativa por múltiplos -- {company_name} ({ticker})"],
            ["Sin datos: no se paso una lista de peers al pipeline (--peers)."],
        ], range_name="A1")
        return

    rows: list[list] = [
        [f"Valoración relativa por múltiplos -- {company_name} ({ticker})"],
        ["Múltiplo ancla = mediana de los peers, ajustado +/-10% por escenario. "
         "Precio objetivo FY+3 (mismo horizonte que el resto del pipeline)."],
        [],
    ]
    for metric in RELATIVE_METRIC_ORDER:
        if not scenarios[0].relative or metric not in scenarios[0].relative:
            continue
        rows.append([metric])
        rows.append(["Escenario", "Múltiplo ancla (peers, x escenario)", "Métrica FY+3", "Precio objetivo FY+3", "Retorno total FY+3"])
        for s in scenarios:
            result = s.relative[metric]
            fy3 = result.years[-1]
            rows.append([
                s.scenario, _num(result.multiple_fy1), _num(fy3.metric), _num(fy3.total_target_price), _pct(fy3.total_return),
            ])
        rows.append([])

    ws.update(values=rows, range_name="A1")


def _average_relative_price(scenario: ScenarioOutput) -> float | None:
    if not scenario.relative:
        return None
    fy3_prices = [result.years[-1].total_target_price for result in scenario.relative.values()]
    return sum(fy3_prices) / len(fy3_prices) if fy3_prices else None


def write_resumen_tab(
    sh: gspread.Spreadsheet, ticker: str, company_name: str, current_price: float, scenarios: list[ScenarioOutput],
) -> None:
    ws = _get_or_create_worksheet(sh, _TAB_RESUMEN)
    has_relative = any(s.relative for s in scenarios)
    header = ["Escenario", "Valor/acción (DCF)", "Upside DCF"]
    if has_relative:
        header += ["Precio objetivo (múltiplos, prom. 5 métodos)", "Upside múltiplos"]
    rows: list[list] = [
        [f"Resumen de Valoración -- {company_name} ({ticker})"],
        ["Precio actual (mercado)", _num(current_price)],
        [],
        header,
    ]
    for s in scenarios:
        upside_dcf = (s.bridge.value_per_share / current_price - 1) if current_price else None
        row = [s.scenario, _num(s.bridge.value_per_share), _pct(upside_dcf)]
        if has_relative:
            avg_relative = _average_relative_price(s)
            upside_relative = (avg_relative / current_price - 1) if (avg_relative and current_price) else None
            row += [_num(avg_relative), _pct(upside_relative)]
        rows.append(row)
    ws.update(values=rows, range_name="A1")


def write_full_valuation(
    sh: gspread.Spreadsheet, *, ticker: str, company_name: str, current_price: float,
    series: AnnualSeries, comps: CompsTable | None, scenarios: list[ScenarioOutput],
) -> None:
    write_datos_tab(sh, series, comps)
    write_supuestos_tab(sh, ticker, company_name, scenarios)
    write_multiplos_tab(sh, ticker, company_name, scenarios)
    write_resumen_tab(sh, ticker, company_name, current_price, scenarios)
