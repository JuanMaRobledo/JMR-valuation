import math

from jmr_valuation.io.inputs import CompanyInputs
from jmr_valuation.valuation import _target_ebit_margin

_BASE_KWARGS = dict(
    ticker="X", company_name="X", country_of_incorporation="US", industry_us="X", industry_global="X",
    revenue_ltm=1000, revenue_prior_10k=900, years_since_last_10k=1, ebit_ltm=300, ebit_prior_10k=280,
    interest_expense_ltm=0, interest_expense_prior_10k=0, book_value_equity_ltm=0,
    book_value_equity_prior_10k=0, book_value_debt_ltm=0, book_value_debt_prior_10k=0,
    cash_ltm=0, cash_prior_10k=0,
)


def test_base_uses_ltm_margin_directly():
    inputs = CompanyInputs(**_BASE_KWARGS, ebit_margin_ltm=0.30, ebit_margin_avg_3y=0.28,
                            ebit_margin_avg_5y=0.27, ebit_margin_avg_10y=0.25)
    assert _target_ebit_margin(inputs, "Base", initial_ebit_margin=0.40) == 0.30


def test_conservador_uses_minimum_of_the_four_historical_margins():
    inputs = CompanyInputs(**_BASE_KWARGS, ebit_margin_ltm=0.30, ebit_margin_avg_3y=0.28,
                            ebit_margin_avg_5y=0.27, ebit_margin_avg_10y=0.25)
    assert _target_ebit_margin(inputs, "Conservador", initial_ebit_margin=0.40) == 0.25


def test_optimista_uses_maximum_including_current_margin():
    inputs = CompanyInputs(**_BASE_KWARGS, ebit_margin_ltm=0.30, ebit_margin_avg_3y=0.28,
                            ebit_margin_avg_5y=0.27, ebit_margin_avg_10y=0.25)
    # el margen actual (0.40) es mayor que los 4 historicos -> deberia ganar
    assert _target_ebit_margin(inputs, "Optimista", initial_ebit_margin=0.40) == 0.40


def test_optimista_falls_back_to_historical_if_higher_than_current():
    inputs = CompanyInputs(**_BASE_KWARGS, ebit_margin_ltm=0.30, ebit_margin_avg_3y=0.45,
                            ebit_margin_avg_5y=0.27, ebit_margin_avg_10y=0.25)
    assert _target_ebit_margin(inputs, "Optimista", initial_ebit_margin=0.20) == 0.45


def test_falls_back_to_delta_when_no_historical_margins_loaded():
    inputs = CompanyInputs(**_BASE_KWARGS, target_ebit_margin=0.35,
                            conservative_margin_delta=-0.03, optimistic_margin_delta=0.03)
    assert math.isclose(_target_ebit_margin(inputs, "Base", initial_ebit_margin=0.40), 0.35)
    assert math.isclose(_target_ebit_margin(inputs, "Conservador", initial_ebit_margin=0.40), 0.32)
    assert math.isclose(_target_ebit_margin(inputs, "Optimista", initial_ebit_margin=0.40), 0.38)
