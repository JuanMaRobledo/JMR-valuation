from jmr_valuation.io import company_store
from jmr_valuation.io.company_store import list_saved_companies, load_saved_company, save_company
from jmr_valuation.io.inputs import load_company_inputs

_MINIMAL_CSV = """ticker,ADBE
company_name,Adobe Inc.
country_of_incorporation,United States
industry_us,Software
industry_global,Software
revenue_ltm,100
revenue_prior_10k,90
years_since_last_10k,1
ebit_ltm,20
ebit_prior_10k,18
interest_expense_ltm,1
interest_expense_prior_10k,1
book_value_equity_ltm,50
book_value_equity_prior_10k,45
book_value_debt_ltm,10
book_value_debt_prior_10k,10
cash_ltm,30
cash_prior_10k,28
"""


def _load_minimal_inputs(ticker="ADBE"):
    import io
    text = _MINIMAL_CSV.replace("ADBE", ticker, 1) if ticker != "ADBE" else _MINIMAL_CSV
    inputs = load_company_inputs(io.StringIO(text))
    return inputs


def test_save_company_writes_csv_named_after_ticker(tmp_path, monkeypatch):
    monkeypatch.setattr(company_store, "SAVED_COMPANIES_DIR", tmp_path / "saved_companies")
    inputs = _load_minimal_inputs()

    path = save_company(inputs)

    assert path.name == "ADBE.csv"
    assert path.exists()


def test_save_company_sanitizes_unsafe_characters_in_ticker(tmp_path, monkeypatch):
    monkeypatch.setattr(company_store, "SAVED_COMPANIES_DIR", tmp_path / "saved_companies")
    inputs = _load_minimal_inputs(ticker="BRK.B")

    path = save_company(inputs)

    assert path.name == "BRK_B.csv"


def test_list_saved_companies_empty_when_no_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(company_store, "SAVED_COMPANIES_DIR", tmp_path / "does_not_exist")
    assert list_saved_companies() == []


def test_save_and_reload_round_trip(tmp_path, monkeypatch):
    monkeypatch.setattr(company_store, "SAVED_COMPANIES_DIR", tmp_path / "saved_companies")
    inputs = _load_minimal_inputs()
    inputs.company_description = "Una empresa de software."

    save_company(inputs)
    [saved_path] = list_saved_companies()
    reloaded = load_saved_company(saved_path)

    assert reloaded.ticker == "ADBE"
    assert reloaded.company_description == "Una empresa de software."


def test_saving_same_ticker_twice_overwrites_instead_of_duplicating(tmp_path, monkeypatch):
    monkeypatch.setattr(company_store, "SAVED_COMPANIES_DIR", tmp_path / "saved_companies")
    inputs = _load_minimal_inputs()

    save_company(inputs)
    inputs.company_description = "Version actualizada."
    save_company(inputs)

    saved = list_saved_companies()
    assert len(saved) == 1
    assert load_saved_company(saved[0]).company_description == "Version actualizada."
