import math

import pytest

from jmr_valuation.models.blend import (
    COMPANY_TYPES,
    METHODS,
    MethodValues,
    buy_price_tiers,
    cagr_3y,
    margin_of_safety_price,
    renormalize_weights,
    run_blend,
    weighted_target_price,
    weights_for_type,
)


@pytest.mark.parametrize("company_type", COMPANY_TYPES)
def test_weights_sum_to_one_for_every_company_type(company_type):
    weights = weights_for_type(company_type)
    assert set(weights) == set(METHODS)
    assert math.isclose(sum(weights.values()), 1.0, abs_tol=1e-9)


def test_unknown_company_type_raises():
    with pytest.raises(ValueError):
        weights_for_type("No existe")


def test_weighted_target_price_software_favors_dcf_and_ev_ebitda():
    values = MethodValues(dcf_damodaran=100, ev_ebitda=80, ev_fcff=90, pe=70, p_fcfe=60, p_ocf=50)
    price = weighted_target_price("Software", values)
    weights = weights_for_type("Software")
    expected = sum(weights[m] * v for m, v in zip(METHODS, [100, 80, 90, 70, 60, 50]))
    assert math.isclose(price, expected)


def test_weighted_target_price_all_methods_equal_returns_that_value():
    values = MethodValues(100, 100, 100, 100, 100, 100)
    for company_type in COMPANY_TYPES:
        assert math.isclose(weighted_target_price(company_type, values), 100.0)


def test_cagr_3y_matches_manual_formula():
    assert math.isclose(cagr_3y(target_price=133.1, current_price=100), 0.10, abs_tol=1e-6)


def test_buy_price_tiers_are_percentages_of_base():
    tiers = buy_price_tiers(200)
    assert tiers.value_max == pytest.approx(140) and tiers.value_min == pytest.approx(130)
    assert tiers.deep_value_max == pytest.approx(120) and tiers.deep_value_min == pytest.approx(110)
    assert tiers.historical_valuation_max == pytest.approx(100) and tiers.historical_valuation_min == pytest.approx(90)


def test_margin_of_safety_price_default_35_pct():
    assert math.isclose(margin_of_safety_price(200), 130.0)


def test_run_blend_end_to_end():
    values_by_scenario = {
        "Conservador": MethodValues(300, 280, 290, 270, 260, 250),
        "Base": MethodValues(360, 340, 350, 330, 320, 310),
        "Optimista": MethodValues(420, 400, 410, 390, 380, 370),
    }
    result = run_blend("Generico", current_price=276.27, values_by_scenario=values_by_scenario)
    assert result.weighted_price_by_scenario["Conservador"] < result.weighted_price_by_scenario["Base"]
    assert result.weighted_price_by_scenario["Base"] < result.weighted_price_by_scenario["Optimista"]
    assert result.mos_price == pytest.approx(result.weighted_price_by_scenario["Base"] * 0.65)
    assert result.buy_price_tiers.value_max == pytest.approx(result.weighted_price_by_scenario["Base"] * 0.70)


def test_renormalize_weights_none_returns_original():
    weights = weights_for_type("Software")
    assert renormalize_weights(weights, None) == weights


def test_renormalize_weights_excluded_method_gets_zero_and_rest_rescale_to_one():
    weights = weights_for_type("Generico")  # DCF=0.5, y el resto 0.1 cada uno
    included = {"P/OCF": False}
    result = renormalize_weights(weights, included)
    assert result["P/OCF"] == 0.0
    assert math.isclose(sum(result.values()), 1.0)
    # los pesos relativos entre los metodos que quedan no deberian cambiar entre si
    assert math.isclose(result["DCF Damodaran"] / result["P/E"], weights["DCF Damodaran"] / weights["P/E"])


def test_renormalize_weights_all_excluded_raises():
    weights = weights_for_type("Generico")
    included = {m: False for m in METHODS}
    with pytest.raises(ValueError):
        renormalize_weights(weights, included)


def test_weighted_target_price_excludes_method_from_the_average():
    # "Financiera": DCF=0.35, EV/EBITDA=0, EV/FCFF=0, P/E=0.35, P/FCFE=0.20, P/OCF=0.10
    values = MethodValues(dcf_damodaran=100, ev_ebitda=200, ev_fcff=200, pe=200, p_fcfe=200, p_ocf=999)
    price_with_pocf = weighted_target_price("Financiera", values)
    price_without_pocf = weighted_target_price("Financiera", values, included_methods={"P/OCF": False})

    # excluir P/OCF (un outlier de 999) tiene que alejar el resultado de ese
    # outlier, no acercarlo -- y el 0.10 de peso que tenia se reparte entre
    # DCF/P-E/P-FCFE en la misma proporcion relativa que ya tenian entre si (0.35:0.35:0.20).
    assert price_without_pocf < price_with_pocf
    expected = (100 * 0.35 + 200 * 0.35 + 200 * 0.20) / 0.90
    assert math.isclose(price_without_pocf, expected)


def test_run_blend_respects_included_methods_end_to_end():
    values_by_scenario = {
        "Conservador": MethodValues(300, 280, 290, 270, 260, 250),
        "Base": MethodValues(360, 340, 350, 330, 320, 310),
        "Optimista": MethodValues(420, 400, 410, 390, 380, 370),
    }
    included = {"EV/EBITDA": False, "P/OCF": False}
    result = run_blend("Generico", current_price=276.27, values_by_scenario=values_by_scenario,
                        included_methods=included)
    assert result.weights["EV/EBITDA"] == 0.0
    assert result.weights["P/OCF"] == 0.0
    assert math.isclose(sum(result.weights.values()), 1.0)
