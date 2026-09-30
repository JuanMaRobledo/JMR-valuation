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


def test_cagr_3y_negative_target_price_returns_real_negative_number():
    # target_price negativo (posible en escenarios extremos) no debe devolver un
    # numero complejo -- eso hacia crashear el dashboard al formatearlo como "%".
    result = cagr_3y(target_price=-50, current_price=100)
    assert isinstance(result, float)
    assert math.isclose(result, -(0.5 ** (1 / 3)) - 1, abs_tol=1e-9)
    assert f"{result:+.1%}"  # no debe lanzar ValueError al formatear


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
    assert result.method_base_values["DCF Damodaran"] == 360
    assert result.method_mos_price["P/E"] == pytest.approx(330 * 0.65)
    assert result.method_mos_vs_current["P/E"] == pytest.approx(1 - 276.27 / 330)
    assert result.method_mos_vs_current["DCF Damodaran"] == pytest.approx(1 - 276.27 / 360)


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


# --- Multiplos a valor presente (ADBE, escenario Base, hoja del 29-sep-2026) ---
from jmr_valuation.models.blend import (  # noqa: E402
    CONSOLIDATE_3Y,
    consolidate_horizons,
    discount_multiple,
    present_value_blend,
)

_ADBE_KE = 0.11202253349164944
_ADBE_BASE = {  # precio + dividendos acumulados, FY+1..FY+3
    "EV/EBITDA": (415.1537921453624, 465.9090426394286, 518.0078695372337),
    "EV/FCFF": (316.71876937878704, 358.63440816090474, 400.2617612595693),
    "P/E": (409.62004062157047, 462.2854744157724, 514.9509082099744),
    "P/FCFE": (290.7974617360271, 328.9207672480282, 366.7868016089501),
    "P/OCF": (322.88376143857886, 364.81991439297207, 406.60818307806375),
}


def test_discount_multiple_matches_sheet():
    assert math.isclose(discount_multiple(518.0078695372337, _ADBE_KE, 3), 376.6999777519675, rel_tol=1e-12)
    assert math.isclose(discount_multiple(415.1537921453624, _ADBE_KE, 1), 373.3321759603354, rel_tol=1e-12)


def test_consolidate_horizons_average_and_three_years():
    assert consolidate_horizons((1.0, 2.0, 3.0)) == 2.0
    assert consolidate_horizons((1.0, 2.0, 3.0), CONSOLIDATE_3Y) == 3.0
    with pytest.raises(ValueError):
        consolidate_horizons((1.0, 2.0, 3.0), "otro")


def test_present_value_blend_matches_adbe_sheet():
    r = present_value_blend("Madura", 377.93587266843457, _ADBE_BASE, _ADBE_KE)
    assert math.isclose(r.multiples_consolidated, 343.91616722118016, rel_tol=1e-12)
    assert math.isclose(r.weighted_present, 357.52404940008194, rel_tol=1e-12)
    assert math.isclose(r.method_consolidated["EV/EBITDA"], 375.6000380619109, rel_tol=1e-12)
    assert math.isclose(r.weight_dcf + r.weight_multiples, 1.0)


@pytest.mark.parametrize("ke", [0.01, 0.08, 0.15])
def test_three_year_present_value_is_below_undiscounted(ke):
    r = present_value_blend("Madura", 100.0, _ADBE_BASE, ke)
    for method, values in _ADBE_BASE.items():
        assert r.method_present_values[method][2] < values[2]
