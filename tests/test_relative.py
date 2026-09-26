import math
import pytest

from jmr_valuation.models.relative import (
    ScenarioMultipleInputs,
    project_target_prices,
    sensitivity_matrix,
)


def test_base_scenario_uses_median_multiple_unadjusted():
    inputs = ScenarioMultipleInputs(
        scenario="Base", historical_median_multiple=20.0,
        metric_fy1=100, metric_fy2=110, metric_fy3=121,
        shares_or_ev_divisor=10,
    )
    result = project_target_prices("EV/FCFF", current_price=150, inputs=inputs)
    assert result.multiple_fy1 == 20.0
    assert math.isclose(result.years[0].implied_target_price, 20.0 * (100 / 10))


def test_conservador_and_optimista_adjust_multiple_by_10_pct():
    base = ScenarioMultipleInputs("Base", 20.0, 100, 110, 121, 10)
    conservador = ScenarioMultipleInputs("Conservador", 20.0, 100, 110, 121, 10)
    optimista = ScenarioMultipleInputs("Optimista", 20.0, 100, 110, 121, 10)

    r_base = project_target_prices("EV/FCFF", 150, base)
    r_cons = project_target_prices("EV/FCFF", 150, conservador)
    r_opt = project_target_prices("EV/FCFF", 150, optimista)

    assert math.isclose(r_cons.multiple_fy1, r_base.multiple_fy1 * 0.9)
    assert math.isclose(r_opt.multiple_fy1, r_base.multiple_fy1 * 1.1)


def test_manual_override_bypasses_scenario_adjustment():
    inputs = ScenarioMultipleInputs(
        "Conservador", historical_median_multiple=20.0, metric_fy1=100, metric_fy2=110,
        metric_fy3=121, shares_or_ev_divisor=10, manual_multiple_override=15.0,
    )
    result = project_target_prices("EV/FCFF", 150, inputs)
    assert result.multiple_fy1 == 15.0


def test_sensitivity_matrix_center_cell_equals_base_case():
    matrix = sensitivity_matrix(base_multiple_fy3=20.0, base_metric_fy3=100.0, shares_or_ev_divisor=10)
    assert len(matrix) == 5 and all(len(row) == 5 for row in matrix)
    center = matrix[2][2]  # delta 1.0 x delta 1.0
    assert math.isclose(center, 20.0 * (100.0 / 10))


def test_enterprise_multiple_converts_ev_to_equity_and_uses_projected_shares():
    inputs = ScenarioMultipleInputs(
        "Base", 20.0, 100, 110, 120, 10,
        projected_shares=(10, 11, 12), ev_to_equity_adjustment=250,
    )
    result = project_target_prices("EV/EBITDA", 100, inputs)
    assert result.years[0].implied_target_price == 175  # (2000 - 250) / 10
    assert result.years[2].implied_target_price == pytest.approx((2400 - 250) / 12)
    matrix = sensitivity_matrix(20, 120, 12, ev_to_equity_adjustment=250)
    assert matrix[2][2] == pytest.approx(result.years[2].implied_target_price)


def test_equity_multiple_does_not_subtract_debt():
    inputs = ScenarioMultipleInputs(
        "Base", 20.0, 100, 110, 120, 10,
        projected_shares=(10, 11, 12), ev_to_equity_adjustment=250,
    )
    assert project_target_prices("P/E", 100, inputs).years[2].implied_target_price == 200
