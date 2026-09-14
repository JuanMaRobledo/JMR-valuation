import statistics

import pytest

from jmr_valuation.io.sec_edgar_loader import AnnualSeries
from jmr_valuation.models.assumptions_engine import (
    BASE_BLEND_WEIGHTS,
    FundamentalGrowthInputs,
    PeerGrowthBenchmark,
    fundamental_growth_rate,
    resolve_sales_to_capital,
    run_assumptions_engine,
    run_growth_engine,
    run_margin_engine,
)

INDUSTRY = "Software (System & Application)"

REVENUE = [100, 115, 130, 150, 175, 205, 240, 280, 325, 375]
EBIT = [25, 30, 36, 42, 50, 60, 72, 85, 100, 118]


def _series(ltm_revenue=400, ltm_ebit=145) -> AnnualSeries:
    return AnnualSeries(
        ticker="TEST", company_name="Test Corp",
        fiscal_year_ends=[f"20{15+i}-12-31" for i in range(10)],
        revenue=[float(v) for v in REVENUE], ebit=[float(v) for v in EBIT],
        da=[0.0] * 10, shares_outstanding=[0.0] * 10,
        long_term_debt=[0.0] * 10, current_debt=[0.0] * 10, cash=[0.0] * 10,
        ltm_revenue=float(ltm_revenue), ltm_ebit=float(ltm_ebit), ltm_da=0.0,
    )


def _fundamental_inputs(**overrides) -> FundamentalGrowthInputs:
    defaults = dict(
        ebit_ltm=145.0, effective_tax_rate=0.25, revenue_ltm=400.0,
        book_value_equity_ltm=300.0, book_value_debt_ltm=100.0, cash_ltm=50.0,
        hist_capex_pct_of_revenue=0.08, hist_da_pct_of_revenue=0.03,
    )
    defaults.update(overrides)
    return FundamentalGrowthInputs(**defaults)


def test_growth_engine_matches_manual_cagr():
    series = _series()
    result = run_growth_engine(series, "Base", industry_us=INDUSTRY, industry_global=INDUSTRY)

    assert result.ltm_growth == pytest.approx(400 / 375 - 1)
    assert result.cagr_3y == pytest.approx((375 / 240) ** (1 / 3) - 1)
    assert result.cagr_5y == pytest.approx((375 / 175) ** (1 / 5) - 1)
    assert result.cagr_long == pytest.approx((375 / 100) ** (1 / 9) - 1)
    assert result.cagr_long_years == 9
    assert result.fundamental is None  # sin fundamental_inputs, no se inventa


def test_growth_engine_base_matches_manual_blend_without_fundamental():
    series = _series()
    result = run_growth_engine(series, "Base", industry_us=INDUSTRY, industry_global=INDUSTRY)
    w = BASE_BLEND_WEIGHTS

    combined = (
        result.ltm_growth * w.weight_ltm + result.cagr_3y * w.weight_cagr3
        + result.cagr_5y * w.weight_cagr5 + result.cagr_long * w.weight_cagr_long
    )
    assert result.combined_historical == pytest.approx(combined)

    industry_avg = (result.industry_growth_us + result.industry_growth_global) / 2
    total = 1 - w.fundamental_growth_weight
    hist_share = (1 - w.industry_growth_weight - w.fundamental_growth_weight) / total
    industry_share = w.industry_growth_weight / total
    expected_base = combined * hist_share + industry_avg * industry_share
    assert result.growth_year1 == pytest.approx(expected_base)


# --- Crecimiento fundamental de Damodaran (g = Reinvestment Rate x ROIC) ---

def test_fundamental_growth_rate_matches_damodaran_formula():
    inputs = _fundamental_inputs()
    result = fundamental_growth_rate(inputs)

    ebit_after_tax = 145.0 * (1 - 0.25)
    invested_capital = 300.0 + 100.0 - 50.0
    expected_roic = ebit_after_tax / invested_capital
    expected_reinvestment_rate = ((0.08 - 0.03) * 400.0) / ebit_after_tax

    assert result.roic == pytest.approx(expected_roic)
    assert result.reinvestment_rate == pytest.approx(expected_reinvestment_rate)
    assert result.fundamental_growth == pytest.approx(expected_reinvestment_rate * expected_roic)


def test_fundamental_growth_rate_returns_none_when_ebit_after_tax_not_positive():
    inputs = _fundamental_inputs(ebit_ltm=-10.0)
    assert fundamental_growth_rate(inputs) is None


def test_fundamental_growth_rate_returns_none_when_invested_capital_not_positive():
    inputs = _fundamental_inputs(book_value_equity_ltm=-200.0, book_value_debt_ltm=0.0, cash_ltm=50.0)
    assert fundamental_growth_rate(inputs) is None


def test_fundamental_growth_rate_ignores_rd_when_capitalize_rd_is_false():
    with_rd_off = _fundamental_inputs(capitalize_rd=False, rd_expense_current_year=50.0,
                                       rd_expense_past_years=(45.0, 40.0, 35.0))
    without_rd_data = _fundamental_inputs()
    assert fundamental_growth_rate(with_rd_off) == fundamental_growth_rate(without_rd_data)
    assert fundamental_growth_rate(with_rd_off).rd_adjusted is False


def test_fundamental_growth_rate_capitalizes_rd_and_can_turn_negative_net_capex_positive():
    """Caso real: una empresa de software con Net CapEx negativo (CapEx < D&A)
    da Reinvestment Rate negativo si se ignora el I+D -- pero si reinvierte
    fuerte via I+D (gasto contable, no CapEx), el crecimiento fundamental
    deberia ser positivo una vez que se capitaliza el I+D (Damodaran)."""
    no_rd = _fundamental_inputs(hist_capex_pct_of_revenue=0.02, hist_da_pct_of_revenue=0.03)  # Net CapEx negativo
    assert fundamental_growth_rate(no_rd).fundamental_growth < 0

    with_rd = _fundamental_inputs(
        hist_capex_pct_of_revenue=0.02, hist_da_pct_of_revenue=0.03,
        capitalize_rd=True, rd_amortization_years=3,
        rd_expense_current_year=120.0, rd_expense_past_years=(100.0, 80.0, 60.0),
    )
    result = fundamental_growth_rate(with_rd)
    assert result.rd_adjusted is True
    assert result.fundamental_growth > fundamental_growth_rate(no_rd).fundamental_growth

    from jmr_valuation.models.converters import capitalize_rd as _cap_rd
    rd = _cap_rd(amortization_years=3, current_year_rd_expense=120.0,
                 past_years_rd_expense=[100.0, 80.0, 60.0], tax_rate=0.25)
    ebit = 145.0 + rd.ebit_adjustment
    invested_capital = 300.0 + 100.0 - 50.0 + rd.research_asset_value
    ebit_after_tax = ebit * (1 - 0.25)
    net_capex = (0.02 - 0.03) * 400.0 + rd.ebit_adjustment
    assert result.roic == pytest.approx(ebit_after_tax / invested_capital)
    assert result.reinvestment_rate == pytest.approx(net_capex / ebit_after_tax)


def test_growth_engine_includes_fundamental_growth_as_a_third_candidate():
    series = _series()
    fundamental_inputs = _fundamental_inputs()
    result = run_growth_engine(
        series, "Base", industry_us=INDUSTRY, industry_global=INDUSTRY, fundamental_inputs=fundamental_inputs,
    )
    assert result.fundamental is not None
    expected = fundamental_growth_rate(fundamental_inputs)
    assert result.fundamental.fundamental_growth == pytest.approx(expected.fundamental_growth)

    w = BASE_BLEND_WEIGHTS
    industry_avg = (result.industry_growth_us + result.industry_growth_global) / 2
    expected_base = (
        result.combined_historical * (1 - w.industry_growth_weight - w.fundamental_growth_weight)
        + industry_avg * w.industry_growth_weight
        + result.fundamental.fundamental_growth * w.fundamental_growth_weight
    )
    assert result.growth_year1 == pytest.approx(expected_base)


def test_growth_engine_conservador_and_optimista_are_min_and_max_including_fundamental():
    series = _series()
    fundamental_inputs = _fundamental_inputs()
    conservador = run_growth_engine(
        series, "Conservador", industry_us=INDUSTRY, industry_global=INDUSTRY, fundamental_inputs=fundamental_inputs,
    )
    optimista = run_growth_engine(
        series, "Optimista", industry_us=INDUSTRY, industry_global=INDUSTRY, fundamental_inputs=fundamental_inputs,
    )
    industry_avg = (conservador.industry_growth_us + conservador.industry_growth_global) / 2
    candidates = [
        conservador.ltm_growth, conservador.cagr_3y, conservador.cagr_5y, conservador.cagr_long,
        industry_avg, conservador.fundamental.fundamental_growth,
    ]
    assert conservador.growth_year1 == pytest.approx(min(candidates))
    assert optimista.growth_year1 == pytest.approx(max(candidates))


def test_growth_ordering_is_guaranteed_even_when_industry_and_fundamental_beat_own_history():
    """Caso real que causaba la inversion: una empresa desacelerando (LTM bajo)
    cuyo CAGR historico largo, industria y crecimiento fundamental son mas
    altos. Con el criterio viejo (pesos distintos por escenario) esto daba
    Conservador > Optimista."""
    series = _series(ltm_revenue=381)  # LTM growth ~1.6%, mucho mas bajo que el resto
    fundamental_inputs = _fundamental_inputs()
    conservador = run_growth_engine(
        series, "Conservador", industry_us=INDUSTRY, industry_global=INDUSTRY, fundamental_inputs=fundamental_inputs,
    )
    base = run_growth_engine(
        series, "Base", industry_us=INDUSTRY, industry_global=INDUSTRY, fundamental_inputs=fundamental_inputs,
    )
    optimista = run_growth_engine(
        series, "Optimista", industry_us=INDUSTRY, industry_global=INDUSTRY, fundamental_inputs=fundamental_inputs,
    )
    assert conservador.growth_year1 <= base.growth_year1 <= optimista.growth_year1


# --- Formula de peers ("Modelo JMR - Motor de Supuestos v2"): Conservador =
# AVG(CAGR 3y, Q1 peers), Base = AVG(CAGR 5y, mediana peers), Optimista =
# AVG(CAGR largo, Q3 peers). ---

def test_growth_engine_with_peers_matches_paired_cagr_and_quartile_formula():
    series = _series()
    peers = PeerGrowthBenchmark(q1=0.08, median=0.12, q3=0.20)
    conservador = run_growth_engine(series, "Conservador", industry_us=INDUSTRY, industry_global=INDUSTRY, peer_growth=peers)
    base = run_growth_engine(series, "Base", industry_us=INDUSTRY, industry_global=INDUSTRY, peer_growth=peers)
    optimista = run_growth_engine(series, "Optimista", industry_us=INDUSTRY, industry_global=INDUSTRY, peer_growth=peers)

    assert conservador.growth_year1 == pytest.approx((conservador.cagr_3y + peers.q1) / 2)
    assert base.growth_year1 == pytest.approx((base.cagr_5y + peers.median) / 2)
    assert optimista.growth_year1 == pytest.approx((optimista.cagr_long + peers.q3) / 2)
    assert conservador.peer_growth == peers


def test_growth_engine_clamp_prevents_inversion_when_cagr_horizons_dont_increase():
    """Empresa que ACELERO recientemente (CAGR 3y > CAGR largo) -- rompe el
    supuesto implicito de la formula de peers. El clamp de seguridad debe
    evitar que Conservador > Base o Base > Optimista de todos modos."""
    accelerating_revenue = [375, 350, 325, 280, 240, 205, 175, 150, 130, 115]  # decrece hacia atras = acelero
    series = AnnualSeries(
        ticker="TEST", company_name="Test Corp", fiscal_year_ends=[f"20{15+i}-12-31" for i in range(10)],
        revenue=[float(v) for v in accelerating_revenue], ebit=[float(v) for v in EBIT],
        da=[0.0] * 10, shares_outstanding=[0.0] * 10, long_term_debt=[0.0] * 10,
        current_debt=[0.0] * 10, cash=[0.0] * 10, ltm_revenue=400.0, ltm_ebit=145.0, ltm_da=0.0,
    )
    # peers invertidos a proposito (Q1 alto, Q3 bajo) para forzar el peor caso
    peers = PeerGrowthBenchmark(q1=0.30, median=0.10, q3=0.02)
    conservador = run_growth_engine(series, "Conservador", industry_us=INDUSTRY, industry_global=INDUSTRY, peer_growth=peers)
    base = run_growth_engine(series, "Base", industry_us=INDUSTRY, industry_global=INDUSTRY, peer_growth=peers)
    optimista = run_growth_engine(series, "Optimista", industry_us=INDUSTRY, industry_global=INDUSTRY, peer_growth=peers)
    assert conservador.growth_year1 <= base.growth_year1 <= optimista.growth_year1


def test_margin_engine_uses_median_of_last_5_years():
    series = _series()
    result = run_margin_engine(series, "Base", industry_us=INDUSTRY, industry_global=INDUSTRY)
    assert result.ebit_margin_actual == pytest.approx(145 / 400)
    last5 = [e / r for e, r in zip(EBIT[-5:], REVENUE[-5:])]
    assert result.ebit_margin_median_5y == pytest.approx(statistics.median(last5))


def test_margin_ordering_is_guaranteed_without_peers():
    """Sin `peer_margin_median`, el benchmark cae al promedio de industria
    Damodaran (US+Global) -- min/max sobre (actual, mediana 5y, ese benchmark)."""
    series = _series()
    conservador = run_margin_engine(series, "Conservador", industry_us=INDUSTRY, industry_global=INDUSTRY)
    base = run_margin_engine(series, "Base", industry_us=INDUSTRY, industry_global=INDUSTRY)
    optimista = run_margin_engine(series, "Optimista", industry_us=INDUSTRY, industry_global=INDUSTRY)

    assert conservador.target_ebit_margin <= base.target_ebit_margin <= optimista.target_ebit_margin
    benchmark = (conservador.industry_margin_us + conservador.industry_margin_global) / 2
    candidates = [conservador.ebit_margin_actual, conservador.ebit_margin_median_5y, benchmark]
    assert conservador.target_ebit_margin == pytest.approx(min(candidates))
    assert optimista.target_ebit_margin == pytest.approx(max(candidates))
    assert base.target_ebit_margin == pytest.approx((conservador.ebit_margin_median_5y + benchmark) / 2)


def test_margin_ordering_is_guaranteed_with_peer_median():
    """Con `peer_margin_median` (mediana real de Operating Margin de los
    peers), ese numero reemplaza al promedio de industria Damodaran como
    benchmark -- mismo criterio que 'Crecimiento y Márgenes'!E14 en el Excel
    de referencia del usuario."""
    series = _series()
    peer_median = 0.50   # mas alto que el margen propio y que la industria Damodaran
    conservador = run_margin_engine(series, "Conservador", industry_us=INDUSTRY, industry_global=INDUSTRY,
                                     peer_margin_median=peer_median)
    optimista = run_margin_engine(series, "Optimista", industry_us=INDUSTRY, industry_global=INDUSTRY,
                                   peer_margin_median=peer_median)
    assert conservador.peer_margin_median == pytest.approx(peer_median)
    candidates = [conservador.ebit_margin_actual, conservador.ebit_margin_median_5y, peer_median]
    assert conservador.target_ebit_margin == pytest.approx(min(candidates))
    assert optimista.target_ebit_margin == pytest.approx(max(candidates))
    assert optimista.target_ebit_margin == pytest.approx(peer_median)  # peer median es el mayor de los 3


def test_resolve_sales_to_capital_defaults_all_scenarios_to_industry_global_average():
    stc = resolve_sales_to_capital(industry_global=INDUSTRY)
    from jmr_valuation.io import reference_data as ref
    expected = ref.get_industry_average(INDUSTRY, global_=True).sales_to_capital
    assert stc.base == pytest.approx(expected)
    assert stc.conservative == pytest.approx(expected)
    assert stc.optimistic == pytest.approx(expected)


def test_resolve_sales_to_capital_honors_explicit_overrides():
    stc = resolve_sales_to_capital(industry_global=INDUSTRY, overrides={"Conservador": 0.5, "Optimista": 3.0})
    assert stc.conservative == pytest.approx(0.5)
    assert stc.optimistic == pytest.approx(3.0)
    from jmr_valuation.io import reference_data as ref
    assert stc.base == pytest.approx(ref.get_industry_average(INDUSTRY, global_=True).sales_to_capital)


def test_run_assumptions_engine_end_to_end_guarantees_scenario_ordering():
    series = _series()
    stc = resolve_sales_to_capital(industry_global=INDUSTRY)
    fundamental_inputs = _fundamental_inputs()
    results = {
        scenario: run_assumptions_engine(
            series, scenario, industry_us=INDUSTRY, industry_global=INDUSTRY, sales_to_capital=stc,
            fundamental_inputs=fundamental_inputs,
        )
        for scenario in ("Conservador", "Base", "Optimista")
    }
    assert results["Conservador"].growth.growth_year1 <= results["Base"].growth.growth_year1 <= results["Optimista"].growth.growth_year1
    assert results["Conservador"].margin.target_ebit_margin <= results["Base"].margin.target_ebit_margin <= results["Optimista"].margin.target_ebit_margin
    for scenario, result in results.items():
        assert result.scenario == scenario
        assert result.sales_to_capital_1_5 == result.sales_to_capital_6_10 == pytest.approx(stc.base)


def test_run_assumptions_engine_rejects_unknown_scenario():
    series = _series()
    stc = resolve_sales_to_capital(industry_global=INDUSTRY)
    with pytest.raises(ValueError, match="Escenario desconocido"):
        run_assumptions_engine(series, "Bull", industry_us=INDUSTRY, industry_global=INDUSTRY, sales_to_capital=stc)
