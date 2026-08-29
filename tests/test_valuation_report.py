from pathlib import Path

from jmr_valuation.io.inputs import load_company_inputs
from jmr_valuation.valuation import RELATIVE_METRICS, SCENARIOS, run_valuation

EXAMPLE_CSV = Path(__file__).resolve().parent.parent / "data" / "example_adbe.csv"


def test_report_includes_a_5x5_sensitivity_matrix_per_metric():
    inputs = load_company_inputs(EXAMPLE_CSV)
    report = run_valuation(inputs)

    assert set(report.sensitivity) == set(RELATIVE_METRICS)
    for metric_name, matrix in report.sensitivity.items():
        assert len(matrix) == 5
        assert all(len(row) == 5 for row in matrix)
        # el centro de la matriz (delta 1.0 x 1.0) debe coincidir con el target FY+3 real
        center = matrix[2][2]
        fy3 = report.relative[metric_name]["Base"].years[-1]
        assert abs(center - fy3.implied_target_price) < 1e-6


def test_report_has_all_scenarios_and_metrics():
    inputs = load_company_inputs(EXAMPLE_CSV)
    report = run_valuation(inputs)

    assert set(report.scenarios) == set(SCENARIOS)
    assert set(report.relative) == set(RELATIVE_METRICS)
    for metric_name in RELATIVE_METRICS:
        assert set(report.relative[metric_name]) == set(SCENARIOS)
        for scenario in SCENARIOS:
            assert len(report.relative[metric_name][scenario].years) == 3
