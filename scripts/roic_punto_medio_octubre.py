#!/usr/bin/env python
"""ROIC terminal de punto medio con el costo de capital terminal de octubre (5-oct-2026).

La regla de la cartera (reference/moat_2026-09-30.json) da a una ventaja que se desvanece un ROIC después del año 10 igual al
punto medio entre el costo de capital terminal y la referencia (promedio de la industria sin superar el ROIC actual). Con la
prima de mercado de octubre el costo de capital terminal bajó de 9,38% a 8,99%, así que el punto medio baja ~0,2 puntos:
EPAM (8,99% + 15,14%) / 2 = 12,1%; LULU (8,99% + 15,77%) / 2 = 12,4%; NKE (8,99% + 15,20%) / 2 = 12,1%. PYPL ya da 15,0% y
NVO (referencia 9,19%) queda en el costo de capital. Respaldo en reference/revision_dcf_2026-10-05/roic_respaldo_<T>.json.

Uso: PYTHONPATH=.:scripts python scripts/roic_punto_medio_octubre.py [--apply]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402

OUT = _ROOT / "reference" / "revision_dcf_2026-10-05"
NUEVO = {"EPAM": 0.121, "LULU": 0.124, "NKE": 0.121}


def main(argv: list[str]) -> int:
    moat = json.loads((_ROOT / "reference" / "moat_2026-09-30.json").read_text())["empresas"]
    for tk, r in NUEVO.items():
        m = moat[tk]
        ref = m["referencia"]
        nota = (f"Ventaja que se desvanece: ROIC después del año 10 = punto medio entre el costo de capital terminal (8,99%, prima "
                f"de mercado de octubre de 2026) y la referencia ({ref * 100:.2f}%, promedio de la industria sin superar el ROIC "
                f"actual) = {r * 100:.1f}%. Antes {m['roic_terminal_antes_2026_10_05'] * 100:.1f}% con 9,38%. Cambio del "
                f"5-oct-2026.").replace(".", ",", 0)
        sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
        sh = ms.open_sheet(sid)
        antes = sh.values_get("'Input sheet'!B50", params={"valueRenderOption": "UNFORMATTED_VALUE"})["values"][0][0]
        print(f"{tk}: B50 {antes} → {r}")
        if "--apply" in argv:
            ms.write_with_backup(sh, "Input sheet", {"B50": r}, f"ROIC terminal de punto medio con 8,99% ({tk})",
                                 OUT / f"roic_respaldo_{tk}.json")
            sh.worksheet("Input sheet").update_notes({"B50": nota})
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
