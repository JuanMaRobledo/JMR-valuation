import json

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


def _generate_throwaway_pem() -> str:
    """Clave RSA generada al vuelo solo para que Credentials.from_service_account_info
    pueda parsear un PEM valido en el test -- no se usa para nada real."""
    from cryptography.hazmat.primitives import serialization
    from cryptography.hazmat.primitives.asymmetric import rsa

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    ).decode()


_FAKE_SERVICE_ACCOUNT_INFO = {
    "type": "service_account", "project_id": "p", "private_key_id": "k",
    "private_key": _generate_throwaway_pem(),
    "client_email": "bot@p.iam.gserviceaccount.com", "client_id": "1",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://x", "universe_domain": "googleapis.com",
}


def test_get_gspread_client_uses_json_content_env_var_when_no_file(monkeypatch, tmp_path):
    """Para corridas programadas (rutina/sesion nueva) sin un archivo local
    persistente -- la credencial completa vive en una variable de entorno de
    la Cloud Environment en vez de un archivo en disco."""
    monkeypatch.delenv("GOOGLE_SERVICE_ACCOUNT_JSON", raising=False)
    monkeypatch.setattr("jmr_valuation.io.sheets_auth.load_dotenv", lambda: None)
    monkeypatch.setenv("GOOGLE_SERVICE_ACCOUNT_JSON_CONTENT", json.dumps(_FAKE_SERVICE_ACCOUNT_INFO))

    client = get_gspread_client()
    assert client.http_client.auth.service_account_email == "bot@p.iam.gserviceaccount.com"


def test_get_gspread_client_raises_clear_error_on_invalid_json_content(monkeypatch):
    monkeypatch.delenv("GOOGLE_SERVICE_ACCOUNT_JSON", raising=False)
    monkeypatch.setattr("jmr_valuation.io.sheets_auth.load_dotenv", lambda: None)
    monkeypatch.setenv("GOOGLE_SERVICE_ACCOUNT_JSON_CONTENT", "{not valid json")
    with pytest.raises(SheetsAuthError, match="no es JSON valido"):
        get_gspread_client()


def test_get_gspread_client_explicit_path_takes_precedence_over_env_content(monkeypatch, tmp_path):
    monkeypatch.setenv("GOOGLE_SERVICE_ACCOUNT_JSON_CONTENT", json.dumps(_FAKE_SERVICE_ACCOUNT_INFO))
    monkeypatch.setattr("jmr_valuation.io.sheets_auth.load_dotenv", lambda: None)
    missing_path = tmp_path / "no_existe.json"
    with pytest.raises(SheetsAuthError, match="No se encontro el JSON"):
        get_gspread_client(credentials_path=missing_path)
