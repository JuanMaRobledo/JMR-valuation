import math
from pathlib import Path

from jmr_valuation.io.inputs import load_company_inputs
from jmr_valuation.models.dcf import (
    GrowthAndMarginPath,
    TerminalAssumptions,
    equity_value_bridge,
    run_dcf,
)

EXAMPLE_CSV = Path(__file__).resolve().parent.parent / "data" / "example_adbe.csv"


def test_flat_scenario_terminal_value_matches_perpetuity_formula():
    """Si crecimiento, margen y WACC son planos desde el anio 1, el valor terminal
    debe coincidir exactamente con la formula de perpetuidad FCFF/(WACC-g)."""
    growth = GrowthAndMarginPath(
        year1_growth=0.05, years_2_to_5_growth=0.05,
        target_ebit_margin=0.30, year_of_margin_convergence=1,
    )
    terminal = TerminalAssumptions(riskfree_rate=0.05, terminal_growth_override=0.05,
                                    terminal_wacc_override=0.09, terminal_roic_override=0.09)
    result = run_dcf(
        base_revenue=1000, base_ebit=300, growth_path=growth,
        initial_ebit_margin=0.30, initial_cost_of_capital=0.09, terminal=terminal,
        initial_tax_rate=0.25, marginal_tax_rate=0.25, tax_rate_converges_to_marginal=False,
        sales_to_capital_years_1_5=2.0, sales_to_capital_years_6_10=2.0,
        invested_capital_base=1500,
    )
    expected_terminal_value = result.terminal_year.fcff / (0.09 - 0.05)
    assert math.isclose(result.terminal_value, expected_terminal_value, rel_tol=1e-9)
    # con margen y crecimiento planos desde el anio 1, todos los anios deben ser identicos
    growth_rates = {round(y.revenue_growth, 9) for y in result.years}
    assert growth_rates == {0.05}


def test_revenue_compounds_at_the_given_growth_rate():
    growth = GrowthAndMarginPath(year1_growth=0.10, years_2_to_5_growth=0.10, target_ebit_margin=0.20)
    terminal = TerminalAssumptions(riskfree_rate=0.04)
    result = run_dcf(
        base_revenue=100, base_ebit=20, growth_path=growth,
        initial_ebit_margin=0.20, initial_cost_of_capital=0.08, terminal=terminal,
        initial_tax_rate=0.25, marginal_tax_rate=0.25, tax_rate_converges_to_marginal=False,
        sales_to_capital_years_1_5=2.0, sales_to_capital_years_6_10=2.0,
        invested_capital_base=200,
    )
    assert math.isclose(result.years[0].revenue, 110, rel_tol=1e-9)
    assert math.isclose(result.years[4].revenue, 100 * 1.10 ** 5, rel_tol=1e-9)


def test_end_to_end_smoke_test_with_example_company(capsys):
    """No valida contra el Excel (no hay forma de recalcularlo en este entorno,
    ver conversacion) -- solo confirma que el pipeline completo corre sin
    excepciones y produce un valor por accion positivo y de orden de magnitud
    razonable para los inputs de ejemplo."""
    inputs = load_company_inputs(EXAMPLE_CSV)

    growth = GrowthAndMarginPath(
        year1_growth=inputs.revenue_growth_next_year,
        years_2_to_5_growth=inputs.revenue_growth_years_2_to_5,
        target_ebit_margin=inputs.target_ebit_margin,
        year_of_margin_convergence=inputs.year_of_margin_convergence,
    )
    terminal = TerminalAssumptions(riskfree_rate=inputs.riskfree_rate)
    initial_ebit_margin = inputs.ebit_ltm / inputs.revenue_ltm
    invested_capital_base = inputs.book_value_equity_ltm + inputs.book_value_debt_ltm - inputs.cash_ltm

    result = run_dcf(
        base_revenue=inputs.revenue_ltm, base_ebit=inputs.ebit_ltm, growth_path=growth,
        initial_ebit_margin=initial_ebit_margin, initial_cost_of_capital=inputs.initial_cost_of_capital,
        terminal=terminal, initial_tax_rate=inputs.effective_tax_rate,
        marginal_tax_rate=inputs.marginal_tax_rate, tax_rate_converges_to_marginal=True,
        sales_to_capital_years_1_5=inputs.sales_to_capital_years_1_5,
        sales_to_capital_years_6_10=inputs.sales_to_capital_years_6_10,
        invested_capital_base=invested_capital_base,
        nol_carryforward=inputs.nol_carryforward,
    )
    bridge = equity_value_bridge(
        result, book_value_debt=inputs.book_value_debt_ltm,
        minority_interests=inputs.minority_interests, cash=inputs.cash_ltm,
        non_operating_assets=inputs.cross_holdings_ltm, shares_outstanding=inputs.shares_outstanding,
        current_price=inputs.current_price,
    )

    assert result.value_of_operating_assets > 0
    assert bridge.value_per_share > 0
    # rango amplio a proposito: es un smoke test de que el pipeline corre, no una
    # validacion de precision contra el Excel.
    assert 10 < bridge.value_per_share < 5000
