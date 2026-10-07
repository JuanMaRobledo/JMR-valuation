#!/usr/bin/env python
"""Prepara una hoja NUEVA (copia de la plantilla maestra) para el flujo «desde cero» (6-oct-2026, aprendido con MCD).

La plantilla maestra trae 'Valuation output' enlazado a la pestaña «Escenarios e historias» (contrato de escenarios),
pero no trae esa pestaña: hasta que build_story_sheet.py la construye, el DCF de la hoja da #DIV/0! y el motor no puede
leerla (damodaran_stories.py falla). Además varios scripts suponen que la empresa ya existe en el repositorio y en la
app. Este script deja todo listo para correr la cadena:

  1. reference/multiplos_v3/<T>_anclas.json con el sheet_id (lo completa después multiples_anchors.py);
  2. pestaña «Escenarios e historias» SEMILLA si no existe: margen = Input B30, ventas/capital = B32/B33, ROIC
     terminal = B50 si B49 = Yes (si no, el WACC terminal) y crecimiento = B27 (año 1), B29 (años 2-5) convergiendo
     al terminal; build_story_sheet.py la reemplaza por los cuatro DCF de las historias;
  3. registro mínimo de la valoración en Modelo-JMR-datos/valoraciones/<T>-<ms>.json (regen_valoracion_app.py lo
     completa desde la hoja).

Orden completo del flujo desde cero: ver el prompt de valoración v4 («Flujo desde cero») y README.

Uso: PYTHONPATH=.:scripts python scripts/nueva_empresa.py TICKER SHEET_ID ["Nombre (BOLSA:TICKER)"]
"""
from __future__ import annotations

import glob
import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402

DATOS = _ROOT.parent / "Modelo-JMR-datos" / "valoraciones"
TAB = "Escenarios e historias"
IS = "'Input sheet'"


def semilla_historias(sh) -> bool:
    if TAB in [w.title for w in sh.worksheets()]:
        return False
    ws = sh.add_worksheet(TAB, rows=130, cols=14)
    data = [{"range": "A1", "values": [["Semilla provisional (scripts/nueva_empresa.py): build_story_sheet.py reemplaza esta pestaña"]]}]
    for i in range(5, 9):
        data.append({"range": f"D{i}:G{i}", "values": [[f"={IS}!B30", f"={IS}!B32", f"={IS}!B33",
                                                         f"=IF({IS}!B49=\"Yes\";{IS}!B50;'Valuation output'!M14)"]]})
    for r in (29, 53, 77, 101):
        row = [f"={IS}!B27"] + [f"={IS}!B29"] * 4 + [f"=$G{r}-($G{r}-$M{r})*({y}-5)/5" for y in range(6, 11)]
        data.append({"range": f"C{r}:M{r}", "values": [row + ["='Valuation output'!M4"]]})
    ws.batch_update(data, value_input_option="USER_ENTERED")
    return True


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 1
    tk, sid = argv[0].upper(), argv[1]
    nombre = argv[2] if len(argv) > 2 else tk
    anc = _ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json"
    if not anc.exists():
        anc.write_text(json.dumps({"sheet_id": sid, "empresa": nombre}, ensure_ascii=False, indent=1) + "\n")
        print("anclas semilla:", anc.relative_to(_ROOT))
    sh = ms.open_sheet(sid)
    print("pestaña de historias semilla:", "creada" if semilla_historias(sh) else "ya existía")
    if not glob.glob(str(DATOS / f"{tk}-*.json")):
        p = DATOS / f"{tk}-{int(time.time() * 1000)}.json"
        p.write_text(json.dumps({"ticker": tk, "hojaGoogle": f"https://docs.google.com/spreadsheets/d/{sid}/edit",
                                 "analisisFundamental": None}, ensure_ascii=False, indent=2) + "\n")
        print("valoración semilla en la app:", p.name)
    vo = sh.worksheet("Valuation output").batch_get(["B35"], value_render_option="UNFORMATTED_VALUE")
    print("DCF provisional de la hoja ('Valuation output'!B35):", vo[0][0][0] if vo and vo[0] else "—")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
