import pytest

from jmr_valuation.io.sec_edgar_client import SecEdgarError
from jmr_valuation.io.sec_edgar_loader import (
    _annual_rows,
    _ltm_value,
    load_annual_series_from_sec_edgar,
    load_company_inputs_from_sec_edgar,
)

M = 1_000_000  # los valores de SEC EDGAR vienen en USD/acciones crudos, no en millones


def _annual(end, val, start_year_offset=1):
    # start_year_offset=1 (el default) produce un periodo de ~1 anio (start =
    # 1 de enero del mismo anio que 'end'), consistente con el chequeo de
    # duracion (350-380 dias) que ahora exige _annual_rows -- un offset de 2
    # generaria ~2 anios de duracion y quedaria excluido a proposito.
    year = int(end[:4]) - start_year_offset + 1
    return {"start": f"{year}-01-01", "end": end, "val": val, "form": "10-K", "fp": "FY", "filed": f"{end[:4]}-02-01"}


def _quarter(start, end, val):
    return {"start": start, "end": end, "val": val, "form": "10-Q", "fp": "Q1", "filed": end}


def _instant(end, val, form="10-K", fp="FY"):
    return {"end": end, "val": val, "form": form, "fp": fp, "filed": end}


def _usd_node(rows):
    return {"units": {"USD": rows}}


def _shares_node(rows):
    return {"units": {"shares": rows}}


def _quarterly_shares(start, end, val):
    """Acciones diluidas promedio de UN trimestre -- a diferencia de
    ingresos/EBIT, este concepto NUNCA se reporta acumulado desde el inicio
    del ejercicio, asi que cada trimestre ya es discreto tal cual viene."""
    return {"start": start, "end": end, "val": val, "form": "10-Q", "fp": "Q1", "filed": end}


def _per_share_node(rows):
    return {"units": {"USD/shares": rows}}


def _build_facts() -> dict:
    revenue = [_annual("2023-12-31", 900 * M), _annual("2024-12-31", 1000 * M)]
    revenue_quarters = [
        _quarter("2025-01-01", "2025-03-31", 260 * M),
        _quarter("2025-04-01", "2025-06-30", 270 * M),
        _quarter("2025-07-01", "2025-09-30", 280 * M),
        _quarter("2025-10-01", "2025-12-30", 290 * M),
    ]
    ebit = [_annual("2023-12-31", 300 * M), _annual("2024-12-31", 360 * M)]
    ebit_quarters = [
        _quarter("2025-01-01", "2025-03-31", 90 * M),
        _quarter("2025-04-01", "2025-06-30", 95 * M),
        _quarter("2025-07-01", "2025-09-30", 100 * M),
        _quarter("2025-10-01", "2025-12-30", 105 * M),
    ]
    interest = [_annual("2023-12-31", 10 * M), _annual("2024-12-31", 12 * M)]

    gaap = {
        "Revenues": _usd_node(revenue + revenue_quarters),
        "OperatingIncomeLoss": _usd_node(ebit + ebit_quarters),
        "InterestExpense": _usd_node(interest),
        "StockholdersEquity": _usd_node([
            _instant("2023-12-31", 500 * M), _instant("2024-12-31", 600 * M),
            _instant("2025-09-30", 650 * M, form="10-Q", fp="Q3"),
        ]),
        "LongTermDebtNoncurrent": _usd_node([
            _instant("2023-12-31", 200 * M), _instant("2024-12-31", 220 * M),
            _instant("2025-09-30", 230 * M, form="10-Q", fp="Q3"),
        ]),
        "LongTermDebtCurrent": _usd_node([
            _instant("2023-12-31", 30 * M), _instant("2024-12-31", 35 * M),
            _instant("2025-09-30", 40 * M, form="10-Q", fp="Q3"),
        ]),
        "CashAndCashEquivalentsAtCarryingValue": _usd_node([
            _instant("2023-12-31", 100 * M), _instant("2024-12-31", 120 * M),
            _instant("2025-09-30", 150 * M, form="10-Q", fp="Q3"),
        ]),
        "MinorityInterest": _usd_node([_instant("2025-09-30", 20 * M, form="10-Q", fp="Q3")]),
        "CommonStockSharesOutstanding": _shares_node([
            _instant("2023-12-31", 100 * M), _instant("2024-12-31", 105 * M),
            _instant("2025-09-30", 108 * M, form="10-Q", fp="Q3"),
        ]),
        "IncomeTaxExpenseBenefit": _usd_node([_annual("2024-12-31", 60 * M)]),
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest": _usd_node(
            [_annual("2024-12-31", 300 * M)]
        ),
        "CommonStockDividendsPerShareDeclared": _per_share_node([
            _annual("2023-12-31", 0.5), _annual("2024-12-31", 0.6),
        ]),
        "DepreciationDepletionAndAmortization": _usd_node([
            _annual("2023-12-31", 40 * M), _annual("2024-12-31", 45 * M),
        ]),
        "PaymentsToAcquirePropertyPlantAndEquipment": _usd_node([
            _annual("2023-12-31", 20 * M), _annual("2024-12-31", 25 * M),
        ]),
        "ResearchAndDevelopmentExpense": _usd_node([
            _annual("2021-12-31", 150 * M), _annual("2022-12-31", 170 * M),
            _annual("2023-12-31", 190 * M), _annual("2024-12-31", 210 * M),
        ]),
        "ProceedsFromIssuanceOfLongTermDebt": _usd_node([
            _annual("2023-12-31", 50 * M), _annual("2024-12-31", 60 * M),
        ]),
        "RepaymentsOfLongTermDebt": _usd_node([
            _annual("2023-12-31", 10 * M), _annual("2024-12-31", 20 * M),
        ]),
        "DeferredTaxAssetsOperatingLossCarryforwards": _usd_node([_instant("2024-12-31", 30 * M)]),
        "NetIncomeLoss": _usd_node([_annual("2023-12-31", 240 * M), _annual("2024-12-31", 300 * M)]),
        "NetCashProvidedByUsedInOperatingActivities": _usd_node([
            _annual("2023-12-31", 350 * M), _annual("2024-12-31", 400 * M),
        ]),
        "PaymentsForRepurchaseOfCommonStock": _usd_node([
            _annual("2023-12-31", 30 * M), _annual("2024-12-31", 40 * M),
        ]),
        "PaymentsOfDividendsCommonStock": _usd_node([
            _annual("2023-12-31", 15 * M), _annual("2024-12-31", 18 * M),
        ]),
        "CostOfRevenue": _usd_node([_annual("2023-12-31", 300 * M), _annual("2024-12-31", 330 * M)]),
        "Assets": _usd_node([_instant("2023-12-31", 900 * M), _instant("2024-12-31", 1000 * M)]),
        "Liabilities": _usd_node([_instant("2023-12-31", 400 * M), _instant("2024-12-31", 430 * M)]),
        "ShareBasedCompensation": _usd_node([_annual("2023-12-31", 25 * M), _annual("2024-12-31", 28 * M)]),
        "NetCashProvidedByUsedInInvestingActivities": _usd_node([
            _annual("2023-12-31", -80 * M), _annual("2024-12-31", -90 * M),
        ]),
        "NetCashProvidedByUsedInFinancingActivities": _usd_node([
            _annual("2023-12-31", -60 * M), _annual("2024-12-31", -70 * M),
        ]),
        "AccountsReceivableNetCurrent": _usd_node([_instant("2023-12-31", 70 * M), _instant("2024-12-31", 80 * M)]),
        "PropertyPlantAndEquipmentNet": _usd_node([_instant("2023-12-31", 150 * M), _instant("2024-12-31", 170 * M)]),
        "Goodwill": _usd_node([_instant("2023-12-31", 200 * M), _instant("2024-12-31", 200 * M)]),
        "AccountsPayableCurrent": _usd_node([_instant("2023-12-31", 40 * M), _instant("2024-12-31", 45 * M)]),
        "AdditionalPaidInCapital": _usd_node([_instant("2023-12-31", 300 * M), _instant("2024-12-31", 320 * M)]),
        "RetainedEarningsAccumulatedDeficit": _usd_node([
            _instant("2023-12-31", 250 * M), _instant("2024-12-31", 290 * M),
        ]),
        "AccumulatedOtherComprehensiveIncomeLossNetOfTax": _usd_node([
            _instant("2023-12-31", -5 * M), _instant("2024-12-31", -4 * M),
        ]),
        "WeightedAverageNumberOfDilutedSharesOutstanding": _shares_node([
            _annual("2023-12-31", 98 * M), _annual("2024-12-31", 103 * M),
            _quarterly_shares("2025-01-01", "2025-03-31", 106 * M),
            _quarterly_shares("2025-04-01", "2025-06-30", 106.5 * M),
            _quarterly_shares("2025-07-01", "2025-09-30", 107 * M),
            _quarterly_shares("2025-10-01", "2025-12-30", 107.5 * M),
        ]),
    }
    return {"cik": 1, "entityName": "TEST CORP", "facts": {"us-gaap": gaap}}


def _build_submissions() -> dict:
    return {
        "name": "TEST CORP",
        "sicDescription": "Services-Prepackaged Software",
        "addresses": {"business": {"isForeignLocation": 0, "country": None, "stateOrCountryDescription": "CA"}},
    }


class _FakeClient:
    def __init__(self, facts, submissions):
        self._facts, self._submissions = facts, submissions

    def company_facts(self, ticker):
        return self._facts

    def company_submissions(self, ticker):
        return self._submissions


@pytest.fixture
def fake_client():
    return _FakeClient(_build_facts(), _build_submissions())


def test_loads_core_financials_from_ltm_and_last_10k(fake_client):
    inputs = load_company_inputs_from_sec_edgar(
        "TEST", current_price=50.0, riskfree_rate=0.04, initial_cost_of_capital=0.09, client=fake_client,
    )

    assert inputs.ticker == "TEST"
    assert inputs.company_name == "TEST CORP"
    assert inputs.country_of_incorporation == "United States"
    assert inputs.industry_us == "Services-Prepackaged Software"

    assert inputs.revenue_ltm == pytest.approx(1100.0)  # suma de los 4 trimestres
    assert inputs.revenue_prior_10k == pytest.approx(1000.0)  # ultimo 10-K cerrado
    assert inputs.ebit_ltm == pytest.approx(390.0)
    assert inputs.ebit_prior_10k == pytest.approx(360.0)
    assert inputs.interest_expense_ltm == pytest.approx(12.0)  # sin trimestres -> cae al ultimo 10-K

    assert inputs.book_value_equity_ltm == pytest.approx(650.0)
    assert inputs.book_value_equity_prior_10k == pytest.approx(600.0)
    assert inputs.book_value_debt_ltm == pytest.approx(270.0)  # 230 LT + 40 corriente
    assert inputs.book_value_debt_prior_10k == pytest.approx(255.0)  # 220 + 35
    assert inputs.cash_ltm == pytest.approx(150.0)
    assert inputs.cash_prior_10k == pytest.approx(120.0)
    assert inputs.minority_interests == pytest.approx(20.0)
    assert inputs.shares_outstanding == pytest.approx(108.0)  # instantaneo mas reciente (10-Q), no el promedio anual
    assert inputs.nol_carryforward == pytest.approx(30.0)

    assert inputs.effective_tax_rate == pytest.approx(0.2)
    assert inputs.dividend_per_share_ltm == pytest.approx(0.6)


def test_annual_series_returns_full_history_and_ltm(fake_client):
    series = load_annual_series_from_sec_edgar("TEST", client=fake_client)

    assert series.ticker == "TEST"
    assert series.company_name == "TEST CORP"
    assert series.fiscal_year_ends == ["2023-12-31", "2024-12-31"]
    assert series.revenue == pytest.approx([900.0 * M, 1000.0 * M])
    assert series.ebit == pytest.approx([300.0 * M, 360.0 * M])
    assert series.long_term_debt == pytest.approx([200.0 * M, 220.0 * M])
    assert series.current_debt == pytest.approx([30.0 * M, 35.0 * M])
    assert series.cash == pytest.approx([100.0 * M, 120.0 * M])
    assert series.ltm_revenue == pytest.approx(1100.0 * M)  # suma de los 4 trimestres
    assert series.ltm_ebit == pytest.approx(390.0 * M)


def test_annual_series_includes_income_statement_and_cash_flow_extras(fake_client):
    """Regresion: estos campos alimentan Income Statement (taxes/net income/
    EPS/acciones diluidas), Cash Flow Statement (OCF/CapEx/buybacks/
    dividendos) y Trailing/Forward Valuation (multiplos historicos reales)
    en refresh_native_model.py -- ver docstring de AnnualSeries."""
    series = load_annual_series_from_sec_edgar("TEST", client=fake_client)

    assert series.net_income == pytest.approx([240.0 * M, 300.0 * M])
    assert series.tax_expense == pytest.approx([0.0, 60.0 * M])  # solo 2024 en el fixture
    assert series.operating_cash_flow == pytest.approx([350.0 * M, 400.0 * M])
    assert series.buybacks == pytest.approx([30.0 * M, 40.0 * M])
    assert series.dividends_paid == pytest.approx([15.0 * M, 18.0 * M])
    assert series.cogs == pytest.approx([300.0 * M, 330.0 * M])
    assert series.diluted_shares_avg == pytest.approx([98.0 * M, 103.0 * M])

    assert series.ltm_net_income == pytest.approx(300.0 * M)  # sin trimestres -> ultimo 10-K
    assert series.ltm_tax_expense == pytest.approx(60.0 * M)
    assert series.ltm_operating_cash_flow == pytest.approx(400.0 * M)
    assert series.ltm_capex == pytest.approx(25.0 * M)  # ya existia como campo "capex"
    assert series.ltm_buybacks == pytest.approx(40.0 * M)
    assert series.ltm_dividends_paid == pytest.approx(18.0 * M)
    assert series.ltm_cogs == pytest.approx(330.0 * M)

    # Acciones diluidas promedio LTM: PROMEDIA (no suma) los ultimos 4
    # trimestres discretos si son contiguos -- ver docstring de
    # _ltm_average_value (sumarlos daria ~4x el valor real).
    assert series.ltm_diluted_shares_avg == pytest.approx((106 + 106.5 + 107 + 107.5) / 4 * M)


def test_annual_series_includes_balance_sheet_and_cash_flow_detail(fake_client):
    """Regresion: estas filas (Income Statement COGS/SG&A/R&D/pretax,
    Balance Sheet Total Assets/Liabilities/Equity/Receivables/PP&E/Goodwill/
    AP/equity components, Cash Flow SBC/investing/financing) quedaban en
    blanco en la plantilla -- ver refresh_native_model.py."""
    series = load_annual_series_from_sec_edgar("TEST", client=fake_client)

    assert series.rd == pytest.approx([190.0 * M, 210.0 * M])
    assert series.total_assets == pytest.approx([900.0 * M, 1000.0 * M])
    assert series.total_liabilities == pytest.approx([400.0 * M, 430.0 * M])
    assert series.equity == pytest.approx([500.0 * M, 600.0 * M])  # StockholdersEquity, ya en el fixture base
    assert series.share_based_comp == pytest.approx([25.0 * M, 28.0 * M])
    assert series.investing_cash_flow == pytest.approx([-80.0 * M, -90.0 * M])
    assert series.financing_cash_flow == pytest.approx([-60.0 * M, -70.0 * M])
    assert series.receivables == pytest.approx([70.0 * M, 80.0 * M])
    assert series.ppe_net == pytest.approx([150.0 * M, 170.0 * M])
    assert series.goodwill == pytest.approx([200.0 * M, 200.0 * M])
    assert series.accounts_payable == pytest.approx([40.0 * M, 45.0 * M])
    assert series.apic == pytest.approx([300.0 * M, 320.0 * M])
    assert series.retained_earnings == pytest.approx([250.0 * M, 290.0 * M])
    assert series.aoci == pytest.approx([-5.0 * M, -4.0 * M])
    assert series.interest_expense == pytest.approx([10.0 * M, 12.0 * M])  # InterestExpense, ya en el fixture base

    assert series.ltm_share_based_comp == pytest.approx(28.0 * M)  # sin trimestres -> ultimo 10-K
    assert series.ltm_investing_cash_flow == pytest.approx(-90.0 * M)
    assert series.ltm_financing_cash_flow == pytest.approx(-70.0 * M)


def test_sga_sums_admin_and_selling_expense_when_company_reports_them_separately():
    """Regresion: MSFT (y varias empresas mas) NO reporta el tag combinado
    'SellingGeneralAndAdministrativeExpense' -- reporta
    'GeneralAndAdministrativeExpense' y 'SellingAndMarketingExpense' como
    DOS lineas separadas. Sin este fallback, la fila de SG&A quedaba en
    blanco (0.0) para esas empresas en vez de sumar ambas."""
    facts = _build_facts()
    facts["facts"]["us-gaap"]["GeneralAndAdministrativeExpense"] = _usd_node([
        _annual("2023-12-31", 80 * M), _annual("2024-12-31", 90 * M),
    ])
    facts["facts"]["us-gaap"]["SellingAndMarketingExpense"] = _usd_node([
        _annual("2023-12-31", 120 * M), _annual("2024-12-31", 130 * M),
    ])
    client = _FakeClient(facts, _build_submissions())

    series = load_annual_series_from_sec_edgar("TEST", client=client)

    assert series.sga == pytest.approx([200.0 * M, 220.0 * M])
    assert series.ltm_sga == pytest.approx(220.0 * M)


def test_sga_prefers_combined_tag_over_summing_parts_when_both_present():
    """Si la empresa SI reporta el tag combinado, se usa ese directo -- no
    se suma ademas con admin/selling (evitaria doble conteo si algunas
    empresas reportan ambos por transicion de un tag al otro)."""
    facts = _build_facts()
    facts["facts"]["us-gaap"]["SellingGeneralAndAdministrativeExpense"] = _usd_node([
        _annual("2023-12-31", 250 * M), _annual("2024-12-31", 275 * M),
    ])
    facts["facts"]["us-gaap"]["GeneralAndAdministrativeExpense"] = _usd_node([
        _annual("2023-12-31", 80 * M), _annual("2024-12-31", 90 * M),
    ])
    facts["facts"]["us-gaap"]["SellingAndMarketingExpense"] = _usd_node([
        _annual("2023-12-31", 120 * M), _annual("2024-12-31", 130 * M),
    ])
    client = _FakeClient(facts, _build_submissions())

    series = load_annual_series_from_sec_edgar("TEST", client=client)

    assert series.sga == pytest.approx([250.0 * M, 275.0 * M])


def test_da_sums_depreciation_and_amortization_when_company_reports_them_separately():
    """Regresion real: MSFT NO reporta NINGUNO de los tags combinados de D&A
    ('DepreciationDepletionAndAmortization', etc.) -- reporta 'Depreciation'
    y 'AmortizationOfIntangibleAssets' como dos lineas separadas. Sin este
    fallback, 'da' quedaba en 0.0 para MSFT: EBITDA terminaba IGUAL a EBIT
    en todo el modelo (Income Statement, Financials Multiples, EV/EBITDA), y
    sobre todo, FCFF/FCFE perdian el resello de D&A (~$39.000M/año para
    MSFT), lo que llevo el precio objetivo de 'EV/FCFF'/'P/FCFE' a numeros
    profundamente negativos en la hoja en vivo."""
    facts = _build_facts()
    del facts["facts"]["us-gaap"]["DepreciationDepletionAndAmortization"]
    facts["facts"]["us-gaap"]["Depreciation"] = _usd_node([
        _annual("2023-12-31", 30 * M), _annual("2024-12-31", 35 * M),
    ])
    facts["facts"]["us-gaap"]["AmortizationOfIntangibleAssets"] = _usd_node([
        _annual("2023-12-31", 10 * M), _annual("2024-12-31", 12 * M),
    ])
    client = _FakeClient(facts, _build_submissions())

    series = load_annual_series_from_sec_edgar("TEST", client=client)

    assert series.da == pytest.approx([40.0 * M, 47.0 * M])
    assert series.ltm_da == pytest.approx(47.0 * M)


def test_da_prefers_combined_tag_over_summing_parts_when_both_present(fake_client):
    """Si la empresa SI reporta un tag combinado de D&A (el fixture base usa
    'DepreciationDepletionAndAmortization'), se usa ese directo -- no se
    suma ademas con Depreciation/AmortizationOfIntangibleAssets."""
    series = load_annual_series_from_sec_edgar("TEST", client=fake_client)
    assert series.da == pytest.approx([40.0 * M, 45.0 * M])  # valores del fixture base, sin sumar nada mas


def test_annual_series_truncates_to_requested_years(fake_client):
    series = load_annual_series_from_sec_edgar("TEST", years=1, client=fake_client)
    assert series.fiscal_year_ends == ["2024-12-31"]
    assert series.revenue == pytest.approx([1000.0 * M])


def test_computes_historical_margins_and_ratios(fake_client):
    inputs = load_company_inputs_from_sec_edgar(
        "TEST", current_price=50.0, riskfree_rate=0.04, initial_cost_of_capital=0.09, client=fake_client,
    )

    assert inputs.ebit_margin_ltm == pytest.approx(390 / 1100)
    assert inputs.ebit_margin_avg_3y == pytest.approx((300 / 900 + 360 / 1000) / 2)
    assert inputs.hist_interest_pct_of_ebit == pytest.approx((10 / 300 + 12 / 360) / 2)
    assert inputs.hist_da_pct_of_revenue == pytest.approx((40 / 900 + 45 / 1000) / 2)
    assert inputs.hist_capex_pct_of_revenue == pytest.approx((20 / 900 + 25 / 1000) / 2)
    assert inputs.hist_net_borrowing_pct_of_revenue == pytest.approx(((50 - 10) / 900 + (60 - 20) / 1000) / 2)
    assert inputs.hist_shares_growth_rate == pytest.approx(105 / 100 - 1)
    assert inputs.hist_dividend_growth_rate == pytest.approx(0.6 / 0.5 - 1)
    assert inputs.revenue_growth_next_year == pytest.approx(1000 / 900 - 1)
    assert inputs.revenue_growth_years_2_to_5 == pytest.approx(1000 / 900 - 1)


def test_capitalizes_rd_with_up_to_nine_years_of_history(fake_client):
    inputs = load_company_inputs_from_sec_edgar(
        "TEST", current_price=50.0, riskfree_rate=0.04, initial_cost_of_capital=0.09, client=fake_client,
    )

    assert inputs.capitalize_rd is True
    assert inputs.rd_expense_current_year == pytest.approx(210.0)
    assert inputs.rd_expense_year_minus_1 == pytest.approx(190.0)
    assert inputs.rd_expense_year_minus_2 == pytest.approx(170.0)
    assert inputs.rd_expense_year_minus_3 == pytest.approx(150.0)
    assert inputs.rd_expense_year_minus_4 == 0.0


def test_market_inputs_are_required_not_guessed(fake_client):
    inputs = load_company_inputs_from_sec_edgar(
        "TEST", current_price=123.45, riskfree_rate=0.041, initial_cost_of_capital=0.088, client=fake_client,
    )
    assert inputs.current_price == 123.45
    assert inputs.riskfree_rate == 0.041
    assert inputs.initial_cost_of_capital == 0.088
    # nunca se adivinan desde EDGAR -- no hay precio de mercado en un 10-K.
    assert inputs.hist_multiple_pe_y1 == 0.0
    assert inputs.has_operating_leases is False
    assert inputs.has_employee_options is False


def test_overrides_replace_any_field(fake_client):
    inputs = load_company_inputs_from_sec_edgar(
        "TEST", current_price=50.0, riskfree_rate=0.04, initial_cost_of_capital=0.09, client=fake_client,
        company_type="Software", margin_of_safety=0.30,
    )
    assert inputs.company_type == "Software"
    assert inputs.margin_of_safety == 0.30


def test_shares_outstanding_falls_back_to_dei_when_more_recent():
    """Regresion: varias empresas (Boston Scientific incluida) dejaron de
    taggear 'CommonStockSharesOutstanding' en us-gaap alrededor de 2020 y
    desde entonces solo reportan el dato de portada como
    'dei:EntityCommonStockSharesOutstanding' -- un namespace XBRL distinto de
    'us-gaap'. Si el loader solo mira us-gaap, se queda con un numero de
    acciones viejo (o en 0 si la empresa nunca taggeo nada en us-gaap)."""
    facts = _build_facts()
    facts["facts"]["dei"] = {
        "EntityCommonStockSharesOutstanding": _shares_node([
            _instant("2026-01-15", 110 * M, form="10-Q", fp="Q1"),
        ]),
    }
    client = _FakeClient(facts, _build_submissions())

    inputs = load_company_inputs_from_sec_edgar(
        "TEST", current_price=50.0, riskfree_rate=0.04, initial_cost_of_capital=0.09, client=client,
    )

    # el dato de dei (2026-01-15) es mas reciente que el de us-gaap (2025-09-30,
    # 108M) -- debe ganar, no quedarse con el valor viejo de us-gaap.
    assert inputs.shares_outstanding == pytest.approx(110.0)


def test_concept_rows_breaks_recency_ties_by_choosing_more_history():
    """Regresion: Boston Scientific reporta 'StockholdersEquity' solo desde
    2021 (cuando empezo a tener interes minoritario) pero
    'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'
    desde 2008 -- ambos tags terminan el mismo dia (el ultimo 10-K), asi que
    antes de este fix el desempate 'tag mas reciente gana' se quedaba con el
    PRIMERO de la lista por orden de aparicion, perdiendo 13 anios de
    historia de patrimonio."""
    from jmr_valuation.io.sec_edgar_loader import _concept_rows

    short_history = [_instant("2024-12-31", 100 * M), _instant("2025-12-31", 110 * M)]
    long_history = [_instant(f"{y}-12-31", y * M) for y in range(2016, 2026)]
    gaap = {
        "StockholdersEquity": _usd_node(short_history),
        "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest": _usd_node(long_history),
    }

    result = _concept_rows(gaap, "equity")

    assert len(result) == len(long_history)
    assert {r["end"] for r in result} == {r["end"] for r in long_history}


def test_shares_outstanding_never_uses_shares_issued():
    """Regresion: 'CommonStockSharesIssued' mide acciones EMITIDAS (incluye
    las que estan en tesoreria), no acciones en CIRCULACION -- para una
    empresa sin tesoreria material son casi iguales, pero Boston Scientific
    (que si tiene tesoreria) reporta ~1746M emitidas vs. ~1484M en
    circulacion para el mismo cierre -- una diferencia de cientos de millones
    de acciones. _concept_rows combina TODOS los tags candidatos de una
    clave, asi que si 'CommonStockSharesIssued' quedara en la lista de
    candidatos de 'shares_outstanding', esa serie mas alta se colaria."""
    from jmr_valuation.io.sec_edgar_loader import _concept_rows

    gaap = {
        "CommonStockSharesOutstanding": _shares_node([_instant("2024-12-31", 1484 * M)]),
        "CommonStockSharesIssued": _shares_node([_instant("2024-12-31", 1746 * M)]),
    }

    result = _concept_rows(gaap, "shares_outstanding", units=("shares",))

    assert [r["val"] for r in result] == [1484 * M]


def test_raises_clear_error_when_no_revenue_data_available():
    empty_client = _FakeClient({"facts": {"us-gaap": {}}}, _build_submissions())
    with pytest.raises(SecEdgarError, match="No se encontraron ingresos anuales"):
        load_company_inputs_from_sec_edgar(
            "TEST", current_price=50.0, riskfree_rate=0.04, initial_cost_of_capital=0.09, client=empty_client,
        )


def test_annual_rows_excludes_quarterly_footnote_disclosures_mislabeled_as_fy():
    """Regresion: Intuit (y otras empresas) redivulgan cada trimestre fiscal
    en la nota de 'informacion financiera trimestral' del propio 10-K, usando
    el mismo tag XBRL (p.ej. Revenues) y el mismo form='10-K'/fp='FY' que el
    dato anual real -- solo la duracion propia del hecho (start/end) delata
    que es un trimestre (~90 dias) y no un ejercicio completo (~365 dias).
    Caso real observado en la API de EDGAR para INTU:
    {'start': '2016-08-01', 'end': '2016-10-31', 'val': 778000000,
     'accn': '0000896878-18-000171', 'fy': 2018, 'fp': 'FY', 'form': '10-K',
     'filed': '2018-08-31', 'frame': 'CY2016Q3'}
    """
    rows = [
        # Fiscal years reales de Intuit (cierran el 31 de julio) -- se
        # escriben a mano (en vez de usar _annual, pensado para cierres de
        # calendario en 31 de diciembre) para preservar una duracion real de
        # ~365 dias.
        {"start": "2022-08-01", "end": "2023-07-31", "val": 900 * M, "form": "10-K", "fp": "FY", "filed": "2023-09-01"},
        {"start": "2023-08-01", "end": "2024-07-31", "val": 1000 * M, "form": "10-K", "fp": "FY", "filed": "2024-08-31"},
        # Nota trimestral dentro del 10-K: mismo tag, mismo form/fp, pero
        # duracion real de ~90 dias -- NO debe colarse como anual.
        {
            "start": "2016-08-01", "end": "2016-10-31", "val": 778 * M,
            "accn": "0000896878-18-000171", "fy": 2018, "fp": "FY", "form": "10-K",
            "filed": "2018-08-31", "frame": "CY2016Q3",
        },
    ]

    annual = _annual_rows(rows)

    ends = [r["end"] for r in annual]
    assert "2016-10-31" not in ends
    assert ends == ["2023-07-31", "2024-07-31"]
    assert annual[-1]["val"] == pytest.approx(1000 * M)


def test_ltm_falls_back_to_annual_when_quarters_have_a_gap():
    """Regresion: Intuit (entre otras) nunca taggea su ultimo trimestre fiscal
    como hecho discreto -- se deriva como 'anio - Q1 - Q2 - Q3' y no aparece
    solo en la API. Con solo 3 trimestres reales disponibles mas uno de un
    periodo posterior no consecutivo, tomar 'los ultimos 4 por fecha' arma un
    LTM de ~15 meses con un hueco de por medio en vez de fallar de forma
    segura al ultimo anio cerrado. Caso real (INTU, ingresos): quedan
    2025-02-01/04-30, despues salta directo a 2025-08-01/10-31 (falta
    2025-05-01/07-31 por completo)."""
    rows = [
        {"start": "2023-08-01", "end": "2024-07-31", "val": 1000 * M, "form": "10-K", "fp": "FY", "filed": "2024-08-31"},
        {"start": "2024-08-01", "end": "2024-10-31", "val": 200 * M, "form": "10-Q", "fp": "Q1", "filed": "2024-11-20"},
        {"start": "2024-11-01", "end": "2025-01-31", "val": 210 * M, "form": "10-Q", "fp": "Q2", "filed": "2025-02-20"},
        {"start": "2025-02-01", "end": "2025-04-30", "val": 500 * M, "form": "10-Q", "fp": "Q3", "filed": "2025-05-20"},
        # falta el trimestre 2025-05-01/07-31 (Q4 fiscal, nunca taggeado solo)
        {"start": "2025-08-01", "end": "2025-10-31", "val": 220 * M, "form": "10-Q", "fp": "Q1", "filed": "2025-11-20"},
    ]

    assert _ltm_value(rows) == pytest.approx(1000 * M)  # cae al ultimo 10-K, no suma los 4 "mas recientes"


def test_ltm_sums_four_quarters_when_actually_contiguous():
    rows = [
        {"start": "2023-08-01", "end": "2024-07-31", "val": 1000 * M, "form": "10-K", "fp": "FY", "filed": "2024-08-31"},
        {"start": "2024-08-01", "end": "2024-10-31", "val": 200 * M, "form": "10-Q", "fp": "Q1", "filed": "2024-11-20"},
        {"start": "2024-11-01", "end": "2025-01-31", "val": 210 * M, "form": "10-Q", "fp": "Q2", "filed": "2025-02-20"},
        {"start": "2025-02-01", "end": "2025-04-30", "val": 500 * M, "form": "10-Q", "fp": "Q3", "filed": "2025-05-20"},
        {"start": "2025-05-01", "end": "2025-07-31", "val": 230 * M, "form": "10-Q", "fp": "Q4", "filed": "2025-08-20"},
    ]

    assert _ltm_value(rows) == pytest.approx(1140 * M)


def test_ltm_derives_discrete_quarters_from_ytd_cumulative_reporting():
    """Regresion: Boston Scientific (y muchas empresas mas) taggea Q1 como
    duracion propia (~90 dias) pero Q2 y Q3 como ACUMULADO desde el inicio
    del ejercicio ('1/1 al 30/6', no '1/4 al 30/6') -- _quarterly_rows()
    exigia una duracion de ~90 dias y nunca encontraba Q2/Q3 asi reportados,
    haciendo que _ltm_value() cayera siempre al ultimo 10-K aunque la
    empresa reportara con la cadencia trimestral normal. Caso real (BSX,
    ingresos, en millones): Q1=4663 (discreto), Q2 YTD=9724 (discreto=5061),
    Q3 YTD=14788 (discreto=5064), FY YTD=20074 (Q4 discreto=5286); anio
    siguiente Q1=5203 (discreto), Q2 YTD=10646 (discreto=5443)."""
    rows = [
        {"start": "2024-01-01", "end": "2024-12-31", "val": 16747 * M, "form": "10-K", "fp": "FY", "filed": "2025-02-14"},
        {"start": "2025-01-01", "end": "2025-03-31", "val": 4663 * M, "form": "10-Q", "fp": "Q1", "filed": "2025-04-20"},
        {"start": "2025-01-01", "end": "2025-06-30", "val": 9724 * M, "form": "10-Q", "fp": "Q2", "filed": "2025-07-20"},
        {"start": "2025-01-01", "end": "2025-09-30", "val": 14788 * M, "form": "10-Q", "fp": "Q3", "filed": "2025-10-20"},
        {"start": "2025-01-01", "end": "2025-12-31", "val": 20074 * M, "form": "10-K", "fp": "FY", "filed": "2026-02-17"},
        {"start": "2026-01-01", "end": "2026-03-31", "val": 5203 * M, "form": "10-Q", "fp": "Q1", "filed": "2026-04-20"},
        {"start": "2026-01-01", "end": "2026-06-30", "val": 10646 * M, "form": "10-Q", "fp": "Q2", "filed": "2026-07-20"},
    ]

    # Q3-2025 (5064) + Q4-2025 (5286) + Q1-2026 (5203) + Q2-2026 (5443) = 20996
    assert _ltm_value(rows) == pytest.approx(20996 * M)


def test_derive_discrete_quarters_matches_already_discrete_reporting():
    """Para una empresa que YA taggea cada trimestre como duracion discreta
    propia (Adobe, por ejemplo), _derive_discrete_quarters no debe cambiar
    nada -- cada trimestre queda solo en su propio grupo (arrancan en fechas
    distintas) y sale identico al dato tal cual estaba reportado."""
    from jmr_valuation.io.sec_edgar_loader import _derive_discrete_quarters

    rows = [
        {"start": "2025-01-01", "end": "2025-03-31", "val": 260 * M, "form": "10-Q", "fp": "Q1", "filed": "2025-04-20"},
        {"start": "2025-04-01", "end": "2025-06-30", "val": 270 * M, "form": "10-Q", "fp": "Q2", "filed": "2025-07-20"},
        {"start": "2025-07-01", "end": "2025-09-30", "val": 280 * M, "form": "10-Q", "fp": "Q3", "filed": "2025-10-20"},
    ]

    result = _derive_discrete_quarters(rows)

    assert [r["val"] for r in result] == [260 * M, 270 * M, 280 * M]


def test_loader_ignores_quarterly_footnote_when_computing_prior_10k_revenue(fake_client):
    """Version end-to-end del mismo bug: si la fila trimestral mal etiquetada
    se cuela en _annual_rows, revenue_prior_10k (y ebit_margin_avg_10y, que se
    deriva de la misma lista) terminan con un numero de ~1 trimestre en vez de
    un ejercicio completo."""
    facts = _build_facts()
    facts["facts"]["us-gaap"]["Revenues"]["units"]["USD"].append({
        "start": "2016-08-01", "end": "2016-10-31", "val": 778 * M,
        "accn": "0000896878-18-000171", "fy": 2018, "fp": "FY", "form": "10-K",
        "filed": "2018-08-31", "frame": "CY2016Q3",
    })
    client = _FakeClient(facts, _build_submissions())

    inputs = load_company_inputs_from_sec_edgar(
        "TEST", current_price=50.0, riskfree_rate=0.04, initial_cost_of_capital=0.09, client=client,
    )

    # revenue_prior_10k toma el ULTIMO 'end' de la serie anual, que sigue
    # siendo 2024-12-31 tanto con el bug como sin el -- por eso el chequeo que
    # realmente distingue el bug es revenue_growth_next_year (CAGR sobre
    # revenue_annual): si la nota trimestral de 2016 se cuela como un tercer
    # "anio" anual, el CAGR se calcula sobre 3 puntos en vez de 2 y usa 778M
    # (el trimestre) como base en vez de 900M (el anio real 2023).
    assert inputs.revenue_prior_10k == pytest.approx(1000.0)
    assert inputs.revenue_growth_next_year == pytest.approx(1000 / 900 - 1)


def test_ltm_when_10q_reports_both_discrete_quarter_and_ytd_with_same_end():
    """Regresion PYPL: cada 10-Q trae el trimestre (3M) Y el acumulado (6M/9M)
    con la MISMA fecha de cierre. Deduplicar solo por 'end' se quedaba con
    uno cualquiera; si sobrevivia el 3M de Q3, no habia 9M para derivar
    Q4 = anual - 9M y el LTM caia al ultimo 10-K."""
    from jmr_valuation.io.sec_edgar_loader import _concept_rows

    rows = [
        {"start": "2025-01-01", "end": "2025-03-31", "val": 731 * M, "form": "10-Q", "fp": "Q1", "filed": "2025-04-29"},
        {"start": "2025-04-01", "end": "2025-06-30", "val": 767 * M, "form": "10-Q", "fp": "Q2", "filed": "2025-07-29"},
        {"start": "2025-01-01", "end": "2025-06-30", "val": 1498 * M, "form": "10-Q", "fp": "Q2", "filed": "2025-07-29"},
        {"start": "2025-07-01", "end": "2025-09-30", "val": 801 * M, "form": "10-Q", "fp": "Q3", "filed": "2025-10-28"},
        {"start": "2025-01-01", "end": "2025-09-30", "val": 2299 * M, "form": "10-Q", "fp": "Q3", "filed": "2025-10-28"},
        {"start": "2025-01-01", "end": "2025-12-31", "val": 3103 * M, "form": "10-K", "fp": "FY", "filed": "2026-02-03"},
        {"start": "2026-01-01", "end": "2026-03-31", "val": 793 * M, "form": "10-Q", "fp": "Q1", "filed": "2026-05-05"},
        {"start": "2026-04-01", "end": "2026-06-30", "val": 849 * M, "form": "10-Q", "fp": "Q2", "filed": "2026-07-28"},
        {"start": "2026-01-01", "end": "2026-06-30", "val": 1642 * M, "form": "10-Q", "fp": "Q2", "filed": "2026-07-28"},
    ]
    merged = _concept_rows({"ResearchAndDevelopmentExpense": {"units": {"USD": rows}}}, "rd")

    # Q3-25 (801) + Q4-25 (3103-2299=804) + Q1-26 (793) + Q2-26 (849) = 3247
    assert _ltm_value(merged) == pytest.approx(3247 * M)


def test_pretax_income_synthesized_from_net_income_plus_tax_when_total_tag_missing():
    """Regresion PYPL: desde 2023 solo taggea el desglose Domestic/Foreign del
    resultado antes de impuestos. El tag Domestic (~US$1.000M) se usaba como
    total y la tasa efectiva daba >100%."""
    from jmr_valuation.io.sec_edgar_loader import _pretax_rows

    gaap = {
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic": {"units": {"USD": [_annual("2025-12-31", 1453 * M)]}},
        "NetIncomeLoss": {"units": {"USD": [{**_annual("2025-12-31", 5233 * M), "accn": "a"}]}},
        "IncomeTaxExpenseBenefit": {"units": {"USD": [{**_annual("2025-12-31", 1059 * M), "accn": "a"}]}},
    }

    annual = _annual_rows(_pretax_rows(gaap))

    assert annual[-1]["val"] == pytest.approx(6292 * M)


def test_pretax_income_prefers_reported_total_over_synthesized():
    from jmr_valuation.io.sec_edgar_loader import _pretax_rows

    gaap = {
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest": {
            "units": {"USD": [{**_annual("2022-12-31", 3366 * M), "accn": "a"}]}},
        "NetIncomeLoss": {"units": {"USD": [{**_annual("2022-12-31", 2419 * M), "accn": "a"}]}},
        "IncomeTaxExpenseBenefit": {"units": {"USD": [{**_annual("2022-12-31", 900 * M), "accn": "a"}]}},
    }

    assert _annual_rows(_pretax_rows(gaap))[-1]["val"] == pytest.approx(3366 * M)


def test_ebit_synthesized_from_gross_profit_minus_sga_when_operating_income_missing():
    """Regresion NKE: nunca taggea OperatingIncomeLoss; el EBIT quedaba en 0.
    FY2024: Gross Profit 22.887 - SG&A 16.576 = 6.311."""
    from jmr_valuation.io.sec_edgar_loader import _ebit_rows

    fy = {"start": "2023-06-01", "end": "2024-05-31", "form": "10-K", "fp": "FY", "filed": "2024-07-25", "accn": "a"}
    gaap = {
        "GrossProfit": {"units": {"USD": [{**fy, "val": 22887 * M}]}},
        "SellingGeneralAndAdministrativeExpense": {"units": {"USD": [{**fy, "val": 16576 * M}]}},
    }

    assert _annual_rows(_ebit_rows(gaap))[-1]["val"] == pytest.approx(6311 * M)


def test_ebit_fallback_subtracts_rd_and_prefers_reported_operating_income():
    from jmr_valuation.io.sec_edgar_loader import _ebit_rows

    gaap = {
        "GrossProfit": {"units": {"USD": [{**_annual("2023-12-31", 100 * M), "accn": "a"},
                                          {**_annual("2024-12-31", 120 * M), "accn": "b"}]}},
        "SellingGeneralAndAdministrativeExpense": {"units": {"USD": [{**_annual("2023-12-31", 40 * M), "accn": "a"},
                                                                     {**_annual("2024-12-31", 45 * M), "accn": "b"}]}},
        "ResearchAndDevelopmentExpense": {"units": {"USD": [{**_annual("2024-12-31", 25 * M), "accn": "b"}]}},
        "OperatingIncomeLoss": {"units": {"USD": [{**_annual("2023-12-31", 58 * M), "accn": "a"}]}},
    }

    annual = {r["end"]: r["val"] for r in _annual_rows(_ebit_rows(gaap))}

    assert annual == {"2023-12-31": pytest.approx(58 * M), "2024-12-31": pytest.approx(50 * M)}
