#!/usr/bin/env python
"""Novedades de la SEC por empresa desde una fecha (6-oct-2026).

Lista 10-K, 10-Q, 20-F, 6-K y 8-K (con sus ítems) presentados después de --desde (por defecto, la fecha del corte
vigente menos 100 días) y marca qué hacer:
  - 10-Q / 10-K / 20-F nuevos después del último cierre de la hoja: actualizar estados (scripts/refresh_native_model.py
    o el importador de la hoja), revisar la historia (reference/damodaran/<T>.json) y regenerar (regenerar_una.sh);
  - 8-K / 6-K: leer cada uno (2.02 resultados y guía; 1.05 ciberataques; 2.05 reestructuraciones; 5.02 directivos;
    8.01 otros): un hecho material cambia los supuestos aunque aún no esté en los estados.
Prompt de valoración v4, paso 3: TODOS los 8-K/6-K entre el último 10-Q/10-K y la fecha de corte.

Uso: python scripts/novedades_sec.py [--desde AAAA-MM-DD] [TICKER ...]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import time
from pathlib import Path

import requests

_ROOT = Path(__file__).resolve().parents[1]
H = {"User-Agent": "JMR Valuation juan0804@gmail.com"}
ITEMS = {"1.01": "acuerdo material", "1.05": "ciberataque", "2.01": "compra o venta de activos", "2.02": "resultados",
         "2.05": "reestructuración", "2.06": "deterioro", "5.02": "directivos", "7.01": "Reg FD", "8.01": "otros eventos",
         "9.01": "anexos"}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde")
    ap.add_argument("tickers", nargs="*")
    a = ap.parse_args(argv)
    corte = json.loads((_ROOT / "reference" / "corte_vigente.json").read_text())
    desde = a.desde or str(dt.date.fromisoformat(corte["fecha_corte"]) - dt.timedelta(days=100))
    tks = a.tickers or sorted(corte["cierres"])
    mapa = {v["ticker"]: str(v["cik_str"]).zfill(10) for v in
            requests.get("https://www.sec.gov/files/company_tickers.json", headers=H, timeout=60).json().values()}
    for tk in tks:
        cik = mapa.get(tk) or mapa.get({"GOOG": "GOOGL"}.get(tk, tk))
        r = requests.get(f"https://data.sec.gov/submissions/CIK{cik}.json", headers=H, timeout=60).json()["filings"]["recent"]
        filas = [(r["filingDate"][i], r["form"][i], r.get("items", [""] * len(r["form"]))[i], r["accessionNumber"][i],
                  r["primaryDocument"][i]) for i in range(len(r["form"]))
                 if r["filingDate"][i] >= desde and r["form"][i] in ("10-K", "10-Q", "20-F", "6-K", "8-K", "40-F")]
        print(f"===== {tk} (desde {desde})")
        for fecha, form, items, acc, doc in sorted(filas):
            det = ", ".join(f"{i} {ITEMS.get(i, '')}".strip() for i in items.split(",") if i) if items else ""
            url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc.replace('-', '')}/{doc}"
            marca = "  <- estados nuevos" if form in ("10-K", "10-Q", "20-F") else ""
            print(f"  {fecha} {form:5s} {det:45s} {url}{marca}")
        time.sleep(0.2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
