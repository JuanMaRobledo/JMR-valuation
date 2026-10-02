#!/usr/bin/env python
"""Auditoría (solo lectura): ¿cada hoja de valoración usa las fórmulas de la plantilla maestra?

Regla (2-oct-2026): todas las empresas usan las mismas fórmulas de la maestra; entre historias y empresas solo
cambian supuestos (celdas de entrada) y datos reportados. Para cada pestaña de cálculo compara, celda por celda,
las celdas donde la maestra tiene fórmula: si la empresa tiene otra fórmula o un número fijo, es una desviación.
Excepciones de contrato (no se cuentan): Resumen C6:E6 (DCF de las historias × (1+Ke)^3), filas 28-50 del Resumen,
'Descuento de múltiplos' (la reescribe discount_multiples.py) y los múltiplos objetivo J8/J19/J30.

Uso:
    PYTHONPATH=.:scripts python scripts/audit_master_formulas.py --targets sheets.json --out reference/auditoria_formulas_maestra.json
"""
from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path

from jmr_valuation.io.sheets_auth import get_gspread_client

MASTER_ID = "19PRUFiYsNavUcN6WwHBVlp-VRMozp3rNSE2R1zt7N-g"
TABS = {"Input sheet": "A1:D80", "Valuation output": "A1:M140", "Financials Multiples": "A1:H120",
        "Cost of capital worksheet": "A1:E70", "Operating lease converter": "A1:G40", "Option value": "A1:F40",
        "Trailing Valuation": "A1:P40", "Forward Valuation": "A1:P40", "Resumen de Valoración": "A1:U27",
        "EVEBITDA": "A1:J35", "EVFCFF": "A1:J35", "PE": "A1:J35", "PFCFE": "A1:J35", "POCF": "A1:J35"}
EXCEPT = {("Resumen de Valoración", a) for a in ("C6", "D6", "E6", "A6")} | \
         {(t, a) for t in ("EVEBITDA", "EVFCFF", "PE", "PFCFE", "POCF") for a in ("J8", "J19", "J30")}


def norm(v):
    return re.sub(r"\s+", "", str(v)) if v is not None else ""


def grid_of(sh, tabs):
    rng = [f"'{t}'!{r}" for t, r in tabs.items()]
    vr = sh.values_batch_get(rng, params={"valueRenderOption": "FORMULA"})["valueRanges"]
    return {t: v.get("values", []) for t, v in zip(tabs, vr)}


def cells(g):
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            yield f"{chr(65 + c)}{r + 1}", v


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--targets", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    client = get_gspread_client()
    master = grid_of(client.open_by_key(MASTER_ID), TABS)
    report = {}
    for tk, sid in json.loads(Path(a.targets).read_text()):
        sh = client.open_by_key(sid)
        titles = {w.title for w in sh.worksheets()}
        tabs = {t: r for t, r in TABS.items() if t in titles}
        g = grid_of(sh, tabs)
        dev = {}
        for t in tabs:
            comp = {addr: v for addr, v in cells(g[t])}
            for addr, mv in cells(master[t]):
                if not (isinstance(mv, str) and mv.startswith("=")) or (t, addr) in EXCEPT:
                    continue
                if t == "Resumen de Valoración" and int(addr[1:]) >= 28:
                    continue
                cv = comp.get(addr, "")
                if norm(cv) != norm(mv):
                    kind = "formula" if isinstance(cv, str) and cv.startswith("=") else "valor"
                    dev.setdefault(t, []).append({"celda": addr, "tipo": kind, "maestra": mv, "empresa": cv})
        missing = [t for t in TABS if t not in titles]
        report[tk] = {"sheet_id": sid, "pestanas_faltantes": missing,
                      "desviaciones": {t: len(v) for t, v in dev.items()}, "detalle": dev}
        print(f"{tk:5s} faltan {missing} " + " ".join(f"{t[:14]}:{len(v)}" for t, v in dev.items()))
        time.sleep(4)
    Path(a.out).write_text(json.dumps(report, ensure_ascii=False, indent=1, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
