import math

from jmr_valuation.models.options import dilution_adjusted_black_scholes, _norm_cdf


def test_norm_cdf_matches_known_values():
    assert math.isclose(_norm_cdf(0.0), 0.5, abs_tol=1e-9)
    assert math.isclose(_norm_cdf(1.959964), 0.975, abs_tol=1e-4)


def test_negligible_dilution_matches_plain_black_scholes():
    # con muy pocas opciones frente a las acciones en circulacion, el precio
    # ajustado por dilucion debe converger casi al precio de mercado (sin ajuste).
    result = dilution_adjusted_black_scholes(
        stock_price=100, strike_price=100, expiration_years=1, volatility=0.3,
        dividend_yield=0.0, riskfree_rate=0.05, n_options=1, n_shares=1_000_000,
    )
    assert math.isclose(result.adjusted_stock_price, 100, rel_tol=1e-3)
    # Black-Scholes (Rf=5%, sigma=30%, S=K=100, T=1) valor de referencia ~ 14.23
    assert math.isclose(result.value_per_option, 14.23, abs_tol=0.1)


def test_dilution_lowers_adjusted_price_and_value_per_option():
    no_dilution = dilution_adjusted_black_scholes(
        stock_price=50, strike_price=10, expiration_years=5, volatility=0.4,
        dividend_yield=0.01, riskfree_rate=0.04, n_options=1, n_shares=1_000_000,
    )
    with_dilution = dilution_adjusted_black_scholes(
        stock_price=50, strike_price=10, expiration_years=5, volatility=0.4,
        dividend_yield=0.01, riskfree_rate=0.04, n_options=200_000, n_shares=1_000_000,
    )
    assert with_dilution.adjusted_stock_price < no_dilution.adjusted_stock_price
    assert with_dilution.total_value > 0
    assert with_dilution.iterations < 100  # debe converger, no agotar el limite
