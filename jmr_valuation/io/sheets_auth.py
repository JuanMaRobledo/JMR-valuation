"""Autenticacion contra Google Sheets via service account (ver README para
como generar el JSON de credenciales -- no OAuth: este pipeline corre sin
usuario presente, y una service account evita el login interactivo).

Uso tipico:
    from jmr_valuation.io.sheets_auth import get_gspread_client

    client = get_gspread_client()
    sheet = client.open_by_key(os.environ["GOOGLE_SHEET_ID"])
"""
from __future__ import annotations

import os
from pathlib import Path

import gspread
from google.oauth2.service_account import Credentials

from jmr_valuation.io.env import load_dotenv

# Alcance minimo necesario: leer/escribir Sheets + Drive (gspread usa Drive
# para resolver `open()` por nombre; `open_by_key` no lo necesita, pero se
# deja habilitado por si se usa esa variante).
_SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


class SheetsAuthError(RuntimeError):
    pass


def get_gspread_client(credentials_path: str | Path | None = None) -> gspread.Client:
    load_dotenv()
    path = Path(credentials_path or os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", ""))
    if not path or not path.exists():
        raise SheetsAuthError(
            f"No se encontro el JSON de la service account en {path!s}. "
            "Copia el archivo descargado de Google Cloud Console a esa ruta, o "
            "seteá GOOGLE_SERVICE_ACCOUNT_JSON en tu .env apuntando al lugar correcto."
        )

    credentials = Credentials.from_service_account_file(str(path), scopes=_SCOPES)
    return gspread.authorize(credentials)


def open_target_sheet(client: gspread.Client, sheet_id: str | None = None) -> gspread.Spreadsheet:
    load_dotenv()
    resolved_id = sheet_id or os.environ.get("GOOGLE_SHEET_ID")
    if not resolved_id:
        raise SheetsAuthError(
            "Falta el ID del Google Sheet destino. Pasalo por parametro o "
            "seteá GOOGLE_SHEET_ID en tu .env (lo ves en la URL del Sheet)."
        )
    try:
        return client.open_by_key(resolved_id)
    except gspread.exceptions.APIError as exc:
        raise SheetsAuthError(
            f"No se pudo abrir el Sheet {resolved_id!r}. Verifica que lo hayas "
            "compartido (como Editor) con el email de la service account "
            f"({_service_account_email(client)})."
        ) from exc


def _service_account_email(client: gspread.Client) -> str:
    try:
        return client.http_client.auth.service_account_email  # type: ignore[union-attr]
    except AttributeError:
        return "<no disponible>"
