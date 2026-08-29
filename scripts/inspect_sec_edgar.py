#!/usr/bin/env python
"""Prueba la conexion a SEC EDGAR y muestra una respuesta real, sin tocar CompanyInputs.

Util cuando load_company_inputs_from_sec_edgar() da un numero raro para una
empresa puntual -- los nombres de tag XBRL varian entre empresas, y esto deja
ver cuales uso realmente esa empresa para completar _TAGS en sec_edgar_loader.py.

Uso:
    python scripts/inspect_sec_edgar.py ADBE facts
    python scripts/inspect_sec_edgar.py ADBE submissions
    python scripts/inspect_sec_edgar.py ADBE tags          -- solo lista los nombres de tag us-gaap
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from jmr_valuation.io.sec_edgar_client import SecEdgarClient, SecEdgarError

ENDPOINTS = {
    "facts": lambda c, t: c.company_facts(t),
    "submissions": lambda c, t: c.company_submissions(t),
    "tags": lambda c, t: sorted(c.company_facts(t).get("facts", {}).get("us-gaap", {})),
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
        client = SecEdgarClient()
        data = ENDPOINTS[endpoint](client, ticker)
    except SecEdgarError as exc:
        print(f"Error: {exc}")
        return 1

    print(json.dumps(data, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
