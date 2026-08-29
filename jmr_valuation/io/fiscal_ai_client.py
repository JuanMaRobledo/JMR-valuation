"""Cliente minimo de la API de fiscal.ai (https://docs.fiscal.ai/docs/api-reference).

No convierte nada a CompanyInputs todavia -- eso es fiscal_ai_loader.py, que por
ahora esta incompleto a proposito (ver su docstring). Este cliente solo hace
las llamadas HTTP y devuelve el JSON tal cual, para poder inspeccionar la forma
real de la respuesta antes de escribir el mapeo de campos.
"""
from __future__ import annotations

import os

import requests

from jmr_valuation.io.env import load_dotenv

BASE_URL = "https://api.fiscal.ai"


class FiscalAIError(RuntimeError):
    pass


class FiscalAIClient:
    def __init__(self, api_key: str | None = None):
        load_dotenv()
        self.api_key = api_key or os.environ.get("FISCAL_AI_API_KEY")
        if not self.api_key:
            raise FiscalAIError(
                "Falta la API key de fiscal.ai. Pone FISCAL_AI_API_KEY=tu_clave en un "
                "archivo .env en la raiz del proyecto (copia .env.example), o pasala "
                "directamente: FiscalAIClient(api_key='...')."
            )

    def _get(self, path: str, params: dict | None = None) -> dict:
        response = requests.get(
            f"{BASE_URL}{path}",
            headers={"X-Api-Key": self.api_key},
            params=params or {},
            timeout=30,
        )
        if not response.ok:
            raise FiscalAIError(
                f"fiscal.ai respondio {response.status_code} en {path}: {response.text[:500]}"
            )
        return response.json()

    # --- Estados financieros (standardized = normalizado entre empresas) ---
    def income_statement(self, ticker: str, period_type: str = "annual") -> dict:
        return self._get(
            "/v1/company/financials/income-statement/standardized",
            {"ticker": ticker, "periodType": period_type},
        )

    def balance_sheet(self, ticker: str, period_type: str = "annual") -> dict:
        return self._get(
            "/v1/company/financials/balance-sheet/standardized",
            {"ticker": ticker, "periodType": period_type},
        )

    def cash_flow_statement(self, ticker: str, period_type: str = "annual") -> dict:
        return self._get(
            "/v1/company/financials/cash-flow-statement/standardized",
            {"ticker": ticker, "periodType": period_type},
        )

    # --- Ratios / multiplos ---
    def ratios(self, ticker: str, period_type: str = "annual") -> dict:
        return self._get("/v1/company/ratios", {"ticker": ticker, "periodType": period_type})

    # --- Mercado ---
    def stock_prices(self, ticker: str) -> dict:
        return self._get("/v3/company/stock-prices", {"ticker": ticker})

    def shares_outstanding(self, ticker: str) -> dict:
        return self._get("/v1/company/shares-outstanding", {"ticker": ticker})

    def company_profile(self, ticker: str) -> dict:
        return self._get("/v3/company/profile", {"ticker": ticker})
