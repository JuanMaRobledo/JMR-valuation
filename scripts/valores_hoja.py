#!/usr/bin/env python
"""Cifras de una valoración leídas de su hoja de cálculo (fuente única de los análisis), 5-oct-2026.

Los textos y tablas del research deben salir de la hoja. Esta función lee, en una sola llamada, las celdas de las que salen
la tasa, el ventas/capital y los valores de las historias:
  - tasa libre de riesgo 'Input sheet'!B35; prima de mercado 'Cost of capital worksheet'!B28; beta apalancada C58;
    costo de capital inicial 'Input sheet'!B36 y terminal 'Valuation output'!M14 (en financieras, Ke inicial y terminal
    de 'DCF FCFE financiero'!B6 y B4);
  - ventas/capital 'Input sheet'!B32:B33, margen objetivo de la Base 'Escenarios e historias'!D5 e impuesto marginal
    'Input sheet'!B25;
  - DCF de las historias y esperado 'Escenarios e historias'!H5:H11 (H5 Base, H6 Conservadora, H7 Disrupción,
    H8 Optimista, H10 esperado, H11 Base) y precio 'Input sheet'!D1.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402

RANGOS = ["'Input sheet'!B35", "'Cost of capital worksheet'!B28", "'Cost of capital worksheet'!C58", "'Input sheet'!B36",
          "'Valuation output'!M14", "'Input sheet'!B32:B33", "'Escenarios e historias'!D5", "'Input sheet'!B25",
          "'Escenarios e historias'!H5:H11", "'Input sheet'!D1"]
RANGOS_FIN = ["'DCF FCFE financiero'!B4", "'DCF FCFE financiero'!B6"]


def _num(x):
    if isinstance(x, (int, float)):
        return float(x)
    try:
        return float(str(x).replace("$", "").replace(".", "").replace(",", ".").strip())
    except ValueError:
        return None


def leer(tk: str, intentos: int = 4) -> dict:
    sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
    for i in range(intentos):
        try:
            sh = ms.open_sheet(sid)
            fin = tk == "PAGS"
            vr = sh.values_batch_get(RANGOS + (RANGOS_FIN if fin else []),
                                     params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
            break
        except Exception:  # cuota de lecturas de Google (60 por minuto)
            if i == intentos - 1:
                raise
            time.sleep(70)
    v = [x.get("values") or [[None]] for x in vr]
    h = [(r[0] if r else None) for r in v[8]]
    d = {"rf": v[0][0][0], "erp": v[1][0][0], "beta": v[2][0][-1], "w0": v[3][0][0], "wT": v[4][0][0],
         "s1": v[5][0][0], "s2": v[5][1][0] if len(v[5]) > 1 else v[5][0][0], "margen": v[6][0][0], "t": v[7][0][0],
         "vA": h[0], "vB": h[1], "vC": h[2], "vD": h[3], "ve": h[5], "base": h[6], "precio": _num(v[9][0][0]),
         "fin": tk == "PAGS"}
    if d["fin"]:
        d["wT"], d["w0"] = v[10][0][0], v[11][0][0]
    u = (d["margen"] or 0) * (1 - (d["t"] or 0))
    d["r1"], d["r2"] = u * (d["s1"] or 0), u * (d["s2"] or 0)
    return d


if __name__ == "__main__":
    for tk in sys.argv[1:]:
        print(tk, json.dumps(leer(tk), ensure_ascii=False))
