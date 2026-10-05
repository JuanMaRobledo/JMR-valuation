#!/usr/bin/env python
"""Fija el precio y la fecha de valoración de cada hoja al corte de la cartera (5-oct-2026).

Una valoración se hace a una fecha: el precio entra en el costo de capital (pesos a valor de mercado) y en las opciones,
así que una hoja con GOOGLEFINANCE(...; "price") cambia de valor mientras el mercado está abierto y no se puede regenerar
ni auditar de forma reproducible. CELH, LULU, NKE y ONON ya tienen el precio fijo; este script hace lo mismo en el resto:
  - 'Input sheet'!D1 = cierre del 30-sep-2026 (Yahoo Finance, sin ajustar), como número;
  - 'Input sheet'!B4 = 30-sep-2026 (las hojas que toman el cierre histórico hasta B4 quedan en la misma fecha);
  - 'Trailing Valuation'!L3 = 'Input sheet'!D1 cuando era un número suelto;
  - 'Resumen de Valoración'!C25 = el mismo cierre en las hojas cuyo precio del modelo (Input B23) sale de ahí (precio
    fijado a mano en una fecha anterior: ADBE, AFYA, MSFT, NVO, PYPL).
Respaldo en reference/revision_dcf_2026-10-05/precio_corte_respaldo_<T>.json y nota en cada celda.

Uso: PYTHONPATH=.:scripts python scripts/fijar_precio_corte.py [--apply] TICKER ...
"""
from __future__ import annotations

import datetime as dt
import glob
import json
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402

CORTE = dt.date(2026, 9, 30)
SERIAL = (CORTE - dt.date(1899, 12, 30)).days  # 46295
# Cierres del 30-sep-2026 (Yahoo Finance, «Close» sin ajustar por dividendos)
CIERRE = {"ADBE": 239.94, "AFYA": 12.04, "BSX": 43.65, "CMG": 31.95, "DPZ": 299.61, "DUOL": 142.40, "EPAM": 108.36,
          "GOOG": 340.74, "INTU": 275.71, "MSFT": 512.90, "NVDA": 228.38, "NVO": 37.91, "PAGS": 8.90, "PLTR": 187.05,
          "PYPL": 52.53, "SHAK": 58.68, "UBER": 68.51, "ZTS": 69.83}
OUT = _ROOT / "reference" / "revision_dcf_2026-10-05"


def sheet_id(tk: str) -> str:
    d = json.loads(Path([p for p in glob.glob(str(_ROOT.parent / "Modelo-JMR-datos" / "valoraciones" / f"{tk}-*.json"))
                         if "regen" not in p][0]).read_text())
    return re.search(r"/d/([^/]+)", d["hojaGoogle"]).group(1)


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    for tk in [a for a in argv if not a.startswith("--")]:
        sh = ms.open_sheet(sheet_id(tk))
        antes = sh.values_batch_get(["'Input sheet'!D1", "'Input sheet'!B4", "'Trailing Valuation'!L3", "'Input sheet'!B23",
                                     "'Resumen de Valoración'!C25"], params={"valueRenderOption": "FORMULA"})["valueRanges"]
        d1, b4, l3, b23, c25 = [(x.get("values") or [[""]])[0][0] for x in antes]
        print(f"{tk:5s} D1 {str(d1)[:40]} → {CIERRE[tk]} | B4 {b4} → {SERIAL} | L3 {str(l3)[:30]}")
        if not apply:
            continue
        nota = (f"Precio de corte: cierre del {CORTE:%d-%m-%Y} (Yahoo Finance), fijo para que la valoración tenga fecha y sea "
                f"reproducible (el precio entra en los pesos del costo de capital). Antes: {str(d1)[:120]}. Fijado el 5-oct-2026.")
        ms.write_with_backup(sh, "Input sheet", {"D1": CIERRE[tk], "B4": SERIAL}, f"Precio y fecha de corte ({tk})",
                             OUT / f"precio_corte_respaldo_{tk}.json")
        sh.worksheet("Input sheet").update_notes({"D1": nota, "B4": f"Fecha de valoración: {CORTE:%d-%m-%Y} (corte de la cartera)."})
        if "Resumen de Valoración'!C25" in str(b23):
            ms.write_with_backup(sh, "Resumen de Valoración", {"C25": CIERRE[tk]}, f"Precio de corte ({tk})",
                                 OUT / f"precio_corte_respaldo_{tk}.json")
            sh.worksheet("Resumen de Valoración").update_notes({"C25": nota.replace("Antes: " + str(d1)[:120], f"Antes: {c25}")})
        if isinstance(l3, (int, float)):
            ms.write_with_backup(sh, "Trailing Valuation", {"L3": "='Input sheet'!D1"}, f"Precio de corte ({tk})",
                                 OUT / f"precio_corte_respaldo_{tk}.json")
        v = sh.values_batch_get(["'Input sheet'!B23", "'Valuation output'!B35"],
                                params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
        print(f"      precio en B23 {v[0]['values'][0][0]} · DCF de la hoja {v[1]['values'][0][0]:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
