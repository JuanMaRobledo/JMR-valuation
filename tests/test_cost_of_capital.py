import math

from jmr_valuation.models.cost_of_capital import (
    cost_of_debt_actual_rating,
    cost_of_equity,
    industry_average_cost_of_capital,
    interest_coverage_ratio,
    synthetic_rating_spread,
    unlevered_to_levered_beta,
    wacc,
)


def test_interest_coverage_ratio_edge_cases():
    assert interest_coverage_ratio(ebit=100, interest_expense=0) == 1_000_000.0
    assert interest_coverage_ratio(ebit=-50, interest_expense=10) == -100_000.0
    assert interest_coverage_ratio(ebit=100, interest_expense=20) == 5.0


def test_synthetic_rating_spread_large_manufacturing():
    rating, spread = synthetic_rating_spread(3.2, small_firm=False)
    assert rating == "A3/A-"
    assert spread == 0.008872


def test_synthetic_rating_spread_below_lowest_bucket_uses_first_row():
    rating, spread = synthetic_rating_spread(-500, small_firm=False)
    assert rating == "D2/D"


def test_cost_of_debt_actual_rating():
    result = cost_of_debt_actual_rating(riskfree_rate=0.0462, rating="A1/A+")
    assert math.isclose(result, 0.0462 + 0.007003)


def test_unlevered_to_levered_beta_no_debt_equals_unlevered():
    beta_l = unlevered_to_levered_beta(unlevered_beta=1.1, tax_rate=0.25, debt_to_equity=0.0)
    assert beta_l == 1.1


def test_cost_of_equity_capm():
    ke = cost_of_equity(riskfree_rate=0.045, levered_beta=1.2, equity_risk_premium=0.05)
    assert math.isclose(ke, 0.045 + 1.2 * 0.05)


def test_wacc_all_equity_equals_cost_of_equity():
    result = wacc(
        market_value_equity=1000, market_value_debt=0,
        cost_of_equity_=0.09, cost_of_debt_pretax=0.04, tax_rate=0.25,
    )
    assert math.isclose(result.wacc, 0.09)
    assert result.weight_equity == 1.0


def test_wacc_weighted_blend():
    result = wacc(
        market_value_equity=800, market_value_debt=200,
        cost_of_equity_=0.10, cost_of_debt_pretax=0.05, tax_rate=0.25,
    )
    expected = 0.8 * 0.10 + 0.2 * (0.05 * 0.75)
    assert math.isclose(result.wacc, expected)


def test_industry_average_cost_of_capital_uses_real_reference_data():
    # Software (System & Application), US -- viene del CSV extraido del Excel real.
    result = industry_average_cost_of_capital("Software (System & Application)", riskfree_rate=0.0462)
    assert 0.05 < result < 0.15
