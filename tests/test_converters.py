from jmr_valuation.models.converters import capitalize_operating_leases, capitalize_rd


def test_operating_lease_matches_excel_example():
    # Mismos numeros que 'Operating lease converter' en el Excel original:
    # gasto actual 295, compromisos 287/235/194/151/98, remanente 605, Kd pre-tax = B38.
    result = capitalize_operating_leases(
        current_year_lease_expense=295,
        commitments_years_1_to_5=[287, 235, 194, 151, 98],
        commitment_year_6_plus=605,
        pretax_cost_of_debt=0.04,  # 'Cost of capital worksheet'!B35 (direct input default)
    )
    # n_years_yr6 = round(605 / mean(287,235,194,151,98)) = round(605/193) = 3
    assert result.debt_value > 0
    assert result.debt_adjustment == result.debt_value
    assert result.depreciation == result.debt_value / (5 + 3)
    assert result.ebit_adjustment == 295 - result.depreciation


def test_operating_lease_zero_remaining_commitment():
    result = capitalize_operating_leases(
        current_year_lease_expense=100,
        commitments_years_1_to_5=[50, 40, 30, 20, 10],
        commitment_year_6_plus=0,
        pretax_cost_of_debt=0.05,
    )
    expected_pv_1_5 = sum(c / 1.05 ** (i + 1) for i, c in enumerate([50, 40, 30, 20, 10]))
    assert result.debt_value == expected_pv_1_5
    assert result.depreciation == result.debt_value / 5


def test_rd_capitalization_three_year_amortization():
    # amortiza a 3 anios: el gasto actual entra 100%, el del anio -1 al 66%, el del -2 al 33%.
    result = capitalize_rd(
        amortization_years=3,
        current_year_rd_expense=300,
        past_years_rd_expense=[270, 240, 210],  # solo se usan los primeros 2 (amort_years-1)
        tax_rate=0.25,
    )
    # amortizacion a 3 anios usa los 3 anios anteriores (-1,-2,-3), no solo 2 --
    # el ano -3 ya no aporta valor de activo remanente (fraccion 0) pero SI aporta
    # su cuota de amortizacion de este anio (confirmado contra 'R& D converter').
    expected_asset = 300 * 1.0 + 270 * (2 / 3) + 240 * (1 / 3) + 210 * 0
    expected_amort = 270 / 3 + 240 / 3 + 210 / 3
    assert result.research_asset_value == expected_asset
    assert result.amortization_current_year == expected_amort
    assert result.ebit_adjustment == 300 - expected_amort
    assert result.tax_effect == result.ebit_adjustment * 0.25


def test_rd_capitalization_one_year_amortization_still_amortizes_last_years_expense():
    # amortizacion a 1 anio: el gasto del anio -1 termina de amortizarse
    # justo este anio (fraccion remanente 0, pero amortizacion = 100% de ese gasto).
    result = capitalize_rd(
        amortization_years=1,
        current_year_rd_expense=100,
        past_years_rd_expense=[90, 80, 70],
        tax_rate=0.3,
    )
    assert result.research_asset_value == 100
    assert result.amortization_current_year == 90
    assert result.ebit_adjustment == 10
    assert result.tax_effect == 10 * 0.3
