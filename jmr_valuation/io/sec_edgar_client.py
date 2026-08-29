"""Cliente minimo de la API publica de SEC EDGAR (https://www.sec.gov/edgar/sec-api-documentation).

A diferencia de fiscal.ai, no hace falta una API key -- es un servicio publico
y gratuito. La SEC si exige un header 'User-Agent' que identifique quien hace
las llamadas (nombre + contacto); sin eso, devuelve 403. Por eso
SEC_EDGAR_USER_AGENT es obligatorio (ver .env.example).

Este cliente solo hace las llamadas HTTP y devuelve el JSON tal cual -- el
mapeo a CompanyInputs vive en sec_edgar_loader.py.
"""
from __future__ import annotations

import os
from functools import lru_cache

import requests

from jmr_valuation.io.env import load_dotenv

WWW_BASE_URL = "https://www.sec.gov"
DATA_BASE_URL = "https://data.sec.gov"


class SecEdgarError(RuntimeError):
    pass


@lru_cache(maxsize=1)
def _ticker_to_cik(user_agent: str) -> dict[str, str]:
    """Descarga (una sola vez por proceso) el listado completo ticker->CIK que
    publica la SEC. No depende de ninguna empresa en particular -- se cachea
    porque son ~10 mil filas y no cambia dentro de una misma corrida."""
    response = requests.get(
        f"{WWW_BASE_URL}/files/company_tickers.json",
        headers={"User-Agent": user_agent},
        timeout=30,
    )
    if not response.ok:
        raise SecEdgarError(
            f"No se pudo descargar el listado de tickers de SEC EDGAR "
            f"(status {response.status_code}): {response.text[:500]}"
        )
    data = response.json()
    return {entry["ticker"].upper(): f"{entry['cik_str']:010d}" for entry in data.values()}


class SecEdgarClient:
    def __init__(self, user_agent: str | None = None):
        load_dotenv()
        self.user_agent = user_agent or os.environ.get("SEC_EDGAR_USER_AGENT")
        if not self.user_agent:
            raise SecEdgarError(
                "Falta SEC_EDGAR_USER_AGENT. La SEC exige identificar quien llama a su API "
                "(nombre de la app + un email de contacto), o devuelve 403. Pone algo como "
                "SEC_EDGAR_USER_AGENT=\"JMR Valuation tu_email@ejemplo.com\" en tu .env "
                "(copia .env.example), o pasalo directo: SecEdgarClient(user_agent='...')."
            )

    def _get(self, url: str, params: dict | None = None) -> dict:
        response = requests.get(
            url, headers={"User-Agent": self.user_agent}, params=params or {}, timeout=30,
        )
        if not response.ok:
            raise SecEdgarError(
                f"SEC EDGAR respondio {response.status_code} en {url}: {response.text[:500]}"
            )
        return response.json()

    def cik_for_ticker(self, ticker: str) -> str:
        mapping = _ticker_to_cik(self.user_agent)
        cik = mapping.get(ticker.upper())
        if cik is None:
            raise SecEdgarError(
                f"No se encontro el ticker {ticker!r} en el listado de SEC EDGAR "
                "(revisa que este bien escrito, o que sea una empresa que reporta a la SEC)."
            )
        return cik

    def _resolve_cik(self, ticker_or_cik: str) -> str:
        return ticker_or_cik if ticker_or_cik.isdigit() else self.cik_for_ticker(ticker_or_cik)

    def company_facts(self, ticker_or_cik: str) -> dict:
        """Todos los datos XBRL (estados financieros) que la empresa reporto, taggeados
        por concepto estandar (us-gaap:Revenues, us-gaap:OperatingIncomeLoss, etc.)."""
        cik = self._resolve_cik(ticker_or_cik)
        return self._get(f"{DATA_BASE_URL}/api/xbrl/companyfacts/CIK{cik}.json")

    def company_submissions(self, ticker_or_cik: str) -> dict:
        """Perfil de la empresa (nombre, SIC, pais/estado de incorporacion) + listado
        de presentaciones. No trae datos financieros, eso esta en company_facts."""
        cik = self._resolve_cik(ticker_or_cik)
        return self._get(f"{DATA_BASE_URL}/submissions/CIK{cik}.json")
