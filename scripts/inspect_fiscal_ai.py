#!/usr/bin/env python
"""Prueba la conexion a fiscal.ai y muestra una respuesta real, sin tocar CompanyInputs.

Uso:
    python scripts/inspect_fiscal_ai.py AAPL income-statement
    python scripts/inspect_fiscal_ai.py AAPL ratios

Endpoints disponibles: income-statement, balance-sheet, cash-flow, ratios,
stock-prices, shares-outstanding, profile.

El resultado se imprime formateado (JSON) -- copialo y pasaselo a Claude para
terminar de escribir el mapeo de campos en io/fiscal_ai_loader.py.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from jmr_valuation.io.fiscal_ai_client import FiscalAIClient, FiscalAIError

ENDPOINTS = {
    "income-statement": lambda c, t: c.income_statement(t),
    "balance-sheet": lambda c, t: c.balance_sheet(t),
    "cash-flow": lambda c, t: c.cash_flow_statement(t),
    "ratios": lambda c, t: c.ratios(t),
    "stock-prices": lambda c, t: c.stock_prices(t),
    "shares-outstanding": lambda c, t: c.shares_outstanding(t),
    "profile": lambda c, t: c.company_profile(t),
}


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(f"Uso: python {argv[0]} <TICKER> <endpoint>")
        print(f"Endpoints: {', '.join(ENDPOINTS)}")
        return 1

    ticker, endpoint = argv[1], argv[2]
    if endpoint not in ENDPOINTS:
        print(f"Endpoint desconocido: {endpoint!r}. Opciones: {', '.join(ENDPOINTS)}")
        return 1

    try:
        client = FiscalAIClient()
        data = ENDPOINTS[endpoint](client, ticker)
    except FiscalAIError as exc:
        print(f"Error: {exc}")
        return 1

    print(json.dumps(data, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
