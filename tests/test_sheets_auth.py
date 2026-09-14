import pytest

from jmr_valuation.io.sheets_auth import SheetsAuthError, get_gspread_client, open_target_sheet


def test_get_gspread_client_raises_clear_error_without_credentials_file(monkeypatch, tmp_path):
    monkeypatch.delenv("GOOGLE_SERVICE_ACCOUNT_JSON", raising=False)
    monkeypatch.setattr("jmr_valuation.io.sheets_auth.load_dotenv", lambda: None)
    missing_path = tmp_path / "no_existe.json"
    with pytest.raises(SheetsAuthError, match="No se encontro el JSON"):
        get_gspread_client(credentials_path=missing_path)


def test_open_target_sheet_raises_clear_error_without_sheet_id(monkeypatch):
    monkeypatch.delenv("GOOGLE_SHEET_ID", raising=False)
    monkeypatch.setattr("jmr_valuation.io.sheets_auth.load_dotenv", lambda: None)
    with pytest.raises(SheetsAuthError, match="Falta el ID del Google Sheet"):
        open_target_sheet(client=object(), sheet_id=None)
