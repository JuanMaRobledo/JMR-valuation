import pytest

from jmr_valuation.io.sec_edgar_loader import AnnualSeries
from jmr_valuation.screener import scoring
from jmr_valuation.screener.metrics import compute_metrics, share_counts
from jmr_valuation.screener.valuation import value_snapshot

B = 1_000_000_000
M = 1_000_000


def _series(n=10, **overrides) -> AnnualSeries:
    """Negocio 'maravilloso' de manual: ventas +10%/anio, margen operativo
    30%, margen bruto 70%, FCF = 110% de la utilidad, sin deuda, recompras
    de 2%/anio."""
    ends = [f"{2016 + i}-12-31" for i in range(n)]
    revenue = [10 * B * 1.10 ** i for i in range(n)]
    ebit = [0.30 * r for r in revenue]
    pretax = ebit
    tax = [0.21 * p for p in pretax]
    ni = [p - t for p, t in zip(pretax, tax)]
    shares = [1000 * M * 0.98 ** i for i in range(n)]
    base = dict(
        ticker="WOND", company_name="Wonderful Co", fiscal_year_ends=ends,
        revenue=revenue, ebit=ebit, da=[0.03 * r for r in revenue],
        shares_outstanding=shares, long_term_debt=[0.0] * n, current_debt=[0.0] * n,
        cash=[2 * B] * n, ltm_revenue=revenue[-1], ltm_ebit=ebit[-1], ltm_da=0.03 * revenue[-1],
        tax_expense=tax, net_income=ni, pretax_income=pretax, diluted_shares_avg=shares,
        operating_cash_flow=[1.25 * x for x in ni], capex=[0.14 * x for x in ni],
        cogs=[0.30 * r for r in revenue], equity=[0.8 * r for r in revenue],
        total_assets=[1.5 * r for r in revenue], current_liabilities=[0.2 * r for r in revenue],
        ltm_net_income=ni[-1], ltm_operating_cash_flow=1.25 * ni[-1], ltm_capex=0.14 * ni[-1],
        ltm_diluted_shares_avg=shares[-1], ltm_share_based_comp=0.02 * revenue[-1],
    )
    base.update(overrides)
    return AnnualSeries(**base)


def test_metrics_of_textbook_wonderful_business():
    m = compute_metrics(_series())
    assert m.years == 10
    assert m.revenue_cagr_5y == pytest.approx(0.10)
    assert m.gross_margin_median_5y == pytest.approx(0.70)
    assert m.gross_margin_std_5y == pytest.approx(0.0, abs=1e-9)
    assert m.operating_margin_ltm == pytest.approx(0.30)
    assert m.fcf_positive_ratio == 1.0
    assert m.fcf_conversion_5y == pytest.approx(1.11)
    assert m.shares_cagr_5y == pytest.approx(-0.02)
    # FCF por accion crece por ventas (+10%) y recompras (1/0.98)
    assert m.fcf_per_share_cagr_5y == pytest.approx(1.10 / 0.98 - 1)
    assert m.net_debt_to_ebitda < 0  # caja neta
    # NOPAT = 30% x 79% de ventas sobre capital promedio (80% de ventas - caja)
    assert 0.30 < m.roic_median_5y < 0.40


def test_textbook_business_is_classified_wonderful():
    q = scoring.score_metrics(compute_metrics(_series()))
    assert q.passes_filters
    assert q.tier == "Maravillosa"
    assert q.score >= 90
    assert q.flags == []


def test_high_leverage_fails_hard_filter():
    n = 10
    s = _series(long_term_debt=[60 * B] * n)
    q = scoring.score_metrics(compute_metrics(s))
    assert not q.passes_filters
    assert q.tier == scoring.NOT_PASSING
    assert any("Deuda neta/EBITDA" in f for f in q.failed_filters)


def test_low_roic_fails_hard_filter():
    n = 10
    s = _series(equity=[5 * r for r in _series().revenue], total_assets=[6 * r for r in _series().revenue])
    q = scoring.score_metrics(compute_metrics(s))
    assert any("ROIC" in f for f in q.failed_filters)


def test_negative_equity_falls_back_to_capital_employed():
    n = 10
    rev = _series().revenue
    s = _series(equity=[-0.5 * r for r in rev], long_term_debt=[0.2 * r for r in rev])
    m = compute_metrics(s)
    assert m.negative_equity
    assert m.roic_median_5y is not None and m.roic_median_5y > 0
    assert "Patrimonio negativo (recompras acumuladas)" in scoring.score_metrics(m).flags


def test_missing_gross_margin_is_skipped_not_penalised():
    full = scoring.score_metrics(compute_metrics(_series()))
    no_cogs = scoring.score_metrics(compute_metrics(_series(cogs=[0.0] * 10)))
    assert no_cogs.coverage < full.coverage
    assert no_cogs.tier == "Maravillosa"


def test_stock_split_is_not_read_as_dilution():
    shares = [1000 * M] * 6 + [3000 * M] * 4  # split 3:1 en el FY7
    s = _series(diluted_shares_avg=shares, shares_outstanding=shares, ltm_diluted_shares_avg=3000 * M)
    hist, current = share_counts(s)
    assert current == 3000 * M
    assert hist[0] == pytest.approx(3000 * M)
    m = compute_metrics(s)
    assert m.shares_cagr_5y == pytest.approx(0.0)


def test_share_count_reported_in_thousands_is_rescaled():
    shares = [191_000.0, 191_500.0] + [192 * M] * 8  # GRMN: dos FY taggeados en miles
    s = _series(diluted_shares_avg=shares, shares_outstanding=shares, ltm_diluted_shares_avg=192 * M)
    hist, current = share_counts(s)
    assert hist[0] == pytest.approx(191 * M)
    assert current == 192 * M


def test_recent_years_in_thousands_do_not_rescale_real_history():
    shares = [861 * M, 815 * M, 785 * M, 765 * M, 750 * M, 752 * M, 741 * M, 732_300.0, 721_900.0, 716_400.0]
    s = _series(diluted_shares_avg=shares, shares_outstanding=shares, ltm_diluted_shares_avg=716_400.0)
    hist, current = share_counts(s)
    assert hist[0] == pytest.approx(861 * M)
    assert current == pytest.approx(716.4 * M)


def test_absurd_share_jump_is_dropped():
    shares = [1000 * M] * 9 + [70_000 * M]
    s = _series(diluted_shares_avg=shares, shares_outstanding=shares, ltm_diluted_shares_avg=1000 * M)
    hist, current = share_counts(s)
    assert hist[-1] is None
    assert hist[0] == 1000 * M


def test_split_after_last_10k_is_applied_to_market_cap():
    s = _series()
    prices = [(f"{2016 + i}-12-30", 100.0) for i in range(10)] + [("2026-09-20", 4.0)]
    plain = value_snapshot(s, prices)
    split = value_snapshot(s, prices, splits=[("2026-04-06", 25.0)])
    assert split.market_cap == pytest.approx(25 * plain.market_cap)


def test_valuation_vs_own_history():
    s = _series()
    # precio constante 100: el P/FCF de hoy es el mas bajo de su historia
    # porque el FCF crecio todos los anios.
    prices = [(f"{2016 + i}-12-30", 100.0) for i in range(10)] + [("2026-09-20", 100.0)]
    v = value_snapshot(s, prices)
    assert v is not None
    assert v.hist_years == 10
    assert v.p_fcf_vs_hist < -0.2
    assert v.label == "Barata vs su historia"
    assert v.fcf_yield == pytest.approx(1 / v.p_fcf)


def test_valuation_without_prices_is_none():
    assert value_snapshot(_series(), []) is None
