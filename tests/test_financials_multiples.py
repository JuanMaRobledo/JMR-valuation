import math

import pytest

from jmr_valuation.models.dcf import GrowthAndMarginPath, TerminalAssumptions, run_dcf
from jmr_valuation.models.financials_multiples import (
    historical_ratios_from_actuals,
    project_financials_multiples,
)


def test_historical_ratios_from_real_adbe_data():
    # Datos reales de 'Income Statement'/'Cash Flow Statement'/'Balance Sheet'
    # del Excel (columnas H..K), calculados a mano en la conversacion.
    ratios = historical_ratios_from_actuals(
        revenues=[19409, 21505, 23769], prior_year_revenue=17606,
        ebit=[6650, 6741, 8706], interest_other=[149, 190, 28],
        da=[872, 857, 818], capex=[360, 183, 179],
        nwc_change=[-295, -665, -954], net_borrowing=[-500, 1997, 497],
        shares_diluted=[459, 450, 427], prior_year_shares_diluted=470.9,
    )
    assert ratios.interest_pct_of_ebit == pytest.approx(0.01794, abs=1e-4)
    assert ratios.da_pct_of_revenue == pytest.approx(0.03973, abs=1e-4)
    assert ratios.capex_pct_of_revenue == pytest.approx(0.01153, abs=1e-4)
    assert ratios.nwc_change_pct_of_revenue_growth == pytest.approx(-0.30077, abs=1e-3)
    assert ratios.shares_growth_rate == pytest.approx(-0.02527, abs=1e-4)
    assert ratios.dividend_growth_rate == 0.0


def test_project_financials_multiples_fcff_matches_manual_formula():
    growth = GrowthAndMarginPath(year1_growth=0.10, years_2_to_5_growth=0.10, target_ebit_margin=0.30)
    terminal = TerminalAssumptions(riskfree_rate=0.04)
    dcf_result = run_dcf(
        base_revenue=1000, base_ebit=250, growth_path=growth, initial_ebit_margin=0.25,
        initial_cost_of_capital=0.08, terminal=terminal, initial_tax_rate=0.25,
        marginal_tax_rate=0.25, tax_rate_converges_to_marginal=False,
        sales_to_capital_years_1_5=2.0, sales_to_capital_years_6_10=2.0, invested_capital_base=1200,
    )
    ratios = historical_ratios_from_actuals(
        revenues=[900, 950, 1000], prior_year_revenue=850,
        ebit=[220, 235, 250], interest_other=[5, 5, 5],
        da=[40, 42, 45], capex=[50, 52, 55],
        nwc_change=[5, 5, 5], net_borrowing=[0, 0, 0],
        shares_diluted=[100, 100, 100], prior_year_shares_diluted=100,
    )
    years = project_financials_multiples(
        base_year_revenue=1000, base_year_shares_diluted=100, base_year_dividend_per_share=0.0,
        year_projections=dcf_result.years[:3], ratios=ratios,
    )
    y1 = dcf_result.years[0]
    fm1 = years[0]
    expected_revenue = 1000 * (1 + y1.revenue_growth)
    expected_ebit = expected_revenue * y1.ebit_margin
    expected_da = ratios.da_pct_of_revenue * expected_revenue
    expected_capex = ratios.capex_pct_of_revenue * expected_revenue
    expected_nwc = ratios.nwc_change_pct_of_revenue_growth * (expected_revenue - 1000)
    expected_fcff = expected_ebit * (1 - y1.tax_rate) + expected_da - expected_capex - expected_nwc

    assert fm1.revenue == pytest.approx(expected_revenue)
    assert fm1.fcff == pytest.approx(expected_fcff)
    assert fm1.fcff_per_share == pytest.approx(expected_fcff / fm1.shares_diluted)
    assert len(years) == 3


def test_project_financials_multiples_fcfe_subtracts_capex():
    """FCFE = NI + D&A - CapEx - deltaNWC + Endeudamiento neto (formula estandar,
    y la misma que 'Financials Multiples'!B68 en el Excel: capex resta, no suma --
    hubo un signo invertido aca que este test hubiera atrapado)."""
    growth = GrowthAndMarginPath(year1_growth=0.10, years_2_to_5_growth=0.10, target_ebit_margin=0.30)
    terminal = TerminalAssumptions(riskfree_rate=0.04)
    dcf_result = run_dcf(
        base_revenue=1000, base_ebit=250, growth_path=growth, initial_ebit_margin=0.25,
        initial_cost_of_capital=0.08, terminal=terminal, initial_tax_rate=0.25,
        marginal_tax_rate=0.25, tax_rate_converges_to_marginal=False,
        sales_to_capital_years_1_5=2.0, sales_to_capital_years_6_10=2.0, invested_capital_base=1200,
    )
    ratios = historical_ratios_from_actuals(
        revenues=[900, 950, 1000], prior_year_revenue=850,
        ebit=[220, 235, 250], interest_other=[5, 5, 5],
        da=[40, 42, 45], capex=[50, 52, 55],
        nwc_change=[5, 5, 5], net_borrowing=[10, 10, 10],
        shares_diluted=[100, 100, 100], prior_year_shares_diluted=100,
    )
    years = project_financials_multiples(
        base_year_revenue=1000, base_year_shares_diluted=100, base_year_dividend_per_share=0.0,
        year_projections=dcf_result.years[:3], ratios=ratios,
    )
    y1, fm1 = dcf_result.years[0], years[0]
    expected_revenue = 1000 * (1 + y1.revenue_growth)
    expected_ebit = expected_revenue * y1.ebit_margin
    expected_ebt = expected_ebit * (1 + ratios.interest_pct_of_ebit)
    expected_ni = expected_ebt * (1 - y1.tax_rate)
    expected_da = ratios.da_pct_of_revenue * expected_revenue
    expected_capex = ratios.capex_pct_of_revenue * expected_revenue
    expected_nwc = ratios.nwc_change_pct_of_revenue_growth * (expected_revenue - 1000)
    expected_net_borrowing = ratios.net_borrowing_pct_of_revenue * expected_revenue
    expected_fcfe = expected_ni + expected_da - expected_capex - expected_nwc + expected_net_borrowing

    assert fm1.fcfe == pytest.approx(expected_fcfe)
    # con capex y ratios positivos, restar capex tiene que dar un FCFE menor que sumarlo
    assert fm1.fcfe < fm1.net_income + expected_da - expected_nwc + expected_net_borrowing + expected_capex
