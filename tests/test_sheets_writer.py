import gspread
import pytest

from jmr_valuation.io.comps_loader import CompsTable
from jmr_valuation.io.sec_edgar_loader import AnnualSeries
from jmr_valuation.io.sheets_writer import ScenarioOutput, write_full_valuation
from jmr_valuation.io.yfinance_client import PeerMultiples
from jmr_valuation.models.assumptions_engine import (
    GrowthEngineResult, MarginEngineResult, SCENARIO_WEIGHTS, AssumptionsEngineResult,
)
from jmr_valuation.models.dcf import DcfResult, EquityBridgeResult, YearProjection
from jmr_valuation.models.relative import RelativeValuationResult, YearTarget


class _FakeWorksheet:
    def __init__(self, title):
        self.title = title
        self.cleared = False
        self.last_update = None

    def clear(self):
        self.cleared = True

    def update(self, values, range_name=None):
        self.last_update = values


class _FakeSpreadsheet:
    def __init__(self):
        self._sheets: dict[str, _FakeWorksheet] = {}

    def worksheet(self, title):
        if title not in self._sheets:
            raise gspread.exceptions.WorksheetNotFound(title)
        return self._sheets[title]

    def add_worksheet(self, title, rows, cols):
        ws = _FakeWorksheet(title)
        self._sheets[title] = ws
        return ws


def _series() -> AnnualSeries:
    return AnnualSeries(
        ticker="TEST", company_name="Test Corp", fiscal_year_ends=["2023-12-31", "2024-12-31"],
        revenue=[900e6, 1000e6], ebit=[300e6, 360e6], da=[40e6, 45e6],
        shares_outstanding=[100e6, 105e6], long_term_debt=[200e6, 220e6],
        current_debt=[30e6, 35e6], cash=[100e6, 120e6], ltm_revenue=1100e6, ltm_ebit=390e6, ltm_da=50e6,
    )


def _year(year=1) -> YearProjection:
    return YearProjection(
        year=year, revenue_growth=0.1, revenue=1100.0, ebit_margin=0.3, ebit=330.0, tax_rate=0.2,
        ebit_after_tax=264.0, reinvestment=50.0, fcff=214.0, cost_of_capital=0.09,
        cumulative_discount_factor=0.9, pv_fcff=192.6, sales_to_capital=1.5, invested_capital=1000.0, roic=0.26,
    )


def _relative_result(metric_name: str, scenario: str, target_price: float) -> RelativeValuationResult:
    year = YearTarget(
        year_label="FY+3", multiple=10.0, metric=1000.0, implied_target_price=target_price,
        cumulative_dividends=0.0, total_target_price=target_price, total_return=0.1, annualized_return=0.03,
    )
    return RelativeValuationResult(metric_name=metric_name, scenario=scenario, multiple_fy1=10.0, years=[year])


def _scenario(name: str, *, with_relative: bool = False) -> ScenarioOutput:
    growth = GrowthEngineResult(0.1, 0.11, 0.12, 0.13, 9, 0.15, 0.14, 0.115, None, 0.13)
    margin = MarginEngineResult(0.36, 0.34, 0.33, 0.27, 0.34)
    assumptions = AssumptionsEngineResult(
        scenario=name, weights=SCENARIO_WEIGHTS["Base"], growth=growth, margin=margin,
        sales_to_capital_1_5=1.5, sales_to_capital_6_10=1.5,
    )
    dcf = DcfResult(
        years=[_year()], terminal_year=_year(11), terminal_value=5000.0, pv_terminal_value=2000.0,
        pv_explicit_years=1500.0, value_of_operating_assets=3500.0,
    )
    bridge = EquityBridgeResult(
        value_of_operating_assets=3500.0, less_debt=250.0, less_minority_interests=0.0, plus_cash=120.0,
        plus_non_operating_assets=0.0, value_of_equity=3370.0, less_value_of_options=0.0,
        value_of_equity_in_common_stock=3370.0, value_per_share=32.1, price_as_pct_of_value=0.85,
    )
    relative = None
    if with_relative:
        relative = {
            "EV/EBITDA": _relative_result("EV/EBITDA", name, 35.0),
            "P/E": _relative_result("P/E", name, 33.0),
        }
    return ScenarioOutput(scenario=name, assumptions=assumptions, dcf=dcf, bridge=bridge, relative=relative)


def test_write_full_valuation_creates_all_three_tabs_and_clears_existing():
    sh = _FakeSpreadsheet()
    existing = sh.add_worksheet("Datos", rows=1, cols=1)
    series = _series()
    comps = CompsTable(
        peers=[PeerMultiples("PEER", "Peer Co", 100.0, 0.8, 10.0, 12.0, 8.0, 9.0, 11.0, 7.0, 0.3, 0.1, None, None)],
        average={"market_cap": 100.0, "gross_margin": 0.8, "forward_pe": 10.0, "pe": 12.0, "ev_fcf": 8.0,
                  "p_fcf": 9.0, "ev_ebitda": 11.0, "p_ocf": 7.0, "operating_margin": 0.3,
                  "revenue_cagr_3y": 0.1, "revenue_cagr_5y": None, "revenue_cagr_10y": None},
        median={"market_cap": 100.0, "gross_margin": 0.8, "forward_pe": 10.0, "pe": 12.0, "ev_fcf": 8.0,
                "p_fcf": 9.0, "ev_ebitda": 11.0, "p_ocf": 7.0, "operating_margin": 0.3,
                "revenue_cagr_3y": 0.1, "revenue_cagr_5y": None, "revenue_cagr_10y": None},
    )
    scenarios = [_scenario(s) for s in ("Conservador", "Base", "Optimista")]

    write_full_valuation(
        sh, ticker="TEST", company_name="Test Corp", current_price=30.0,
        series=series, comps=comps, scenarios=scenarios,
    )

    assert existing.cleared is True
    for title in ("Datos", "Supuestos", "Multiplos", "Resumen"):
        ws = sh.worksheet(title)
        assert ws.last_update is not None
        assert len(ws.last_update) > 1


def test_write_full_valuation_works_without_comps():
    sh = _FakeSpreadsheet()
    scenarios = [_scenario(s) for s in ("Conservador", "Base", "Optimista")]
    write_full_valuation(
        sh, ticker="TEST", company_name="Test Corp", current_price=30.0,
        series=_series(), comps=None, scenarios=scenarios,
    )
    datos = sh.worksheet("Datos").last_update
    assert not any("Comparables" in row for row in datos if row)

    multiplos = sh.worksheet("Multiplos").last_update
    assert any("Sin datos" in row[0] for row in multiplos if row)

    resumen = sh.worksheet("Resumen").last_update
    assert "múltiplos" not in resumen[3][-1].lower()  # sin relative, no agrega columnas de multiplos


def test_write_multiplos_tab_shows_target_price_per_metric_and_scenario():
    sh = _FakeSpreadsheet()
    scenarios = [_scenario(s, with_relative=True) for s in ("Conservador", "Base", "Optimista")]
    write_full_valuation(
        sh, ticker="TEST", company_name="Test Corp", current_price=30.0,
        series=_series(), comps=None, scenarios=scenarios,
    )
    multiplos = sh.worksheet("Multiplos").last_update
    flat = [cell for row in multiplos for cell in row]
    assert "EV/EBITDA" in flat
    assert "P/E" in flat
    assert "35.00" in flat  # precio objetivo FY+3 de EV/EBITDA


def test_write_resumen_tab_adds_multiples_columns_when_relative_data_present():
    sh = _FakeSpreadsheet()
    scenarios = [_scenario(s, with_relative=True) for s in ("Conservador", "Base", "Optimista")]
    write_full_valuation(
        sh, ticker="TEST", company_name="Test Corp", current_price=30.0,
        series=_series(), comps=None, scenarios=scenarios,
    )
    resumen = sh.worksheet("Resumen").last_update
    header = resumen[3]
    assert any("múltiplos" in cell.lower() for cell in header)
    base_row = next(row for row in resumen if row and row[0] == "Base")
    # promedio de 35.0 (EV/EBITDA) y 33.0 (P/E) = 34.0
    assert base_row[3] == "34.00"
