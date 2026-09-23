#!/usr/bin/env python
"""Aplica a la PLANTILLA MAESTRA (Modelo_JMR_Plantilla_Maestra) las
correcciones estructurales genericas encontradas al valorar PYPL y NKE, para
que cada copia nueva ya las traiga. Solo toca formulas que no dependen de la
empresa -- los supuestos (Input sheet!B27-B33), la industria y el cost of
capital quedan como estaban, para completarlos en cada valoracion.

Correcciones (ver el log de la hoja Tesis de PYPL/NKE):
  1. Input sheet!B1 vacio -> =A1 (bug #6: TICKER vacio en otras hojas).
  2. Input sheet!B24 fijo en la columna de 2023 -> LTM ('Income Statement'!L29).
  3. Input sheet!B20 sumaba 'Other Long-Term Assets' (operativos) como
     activo no operativo -> solo Long-Term Investments.
  4. Option value: IFERROR en la cadena de Black-Scholes (bug #5).
  5. Cost of capital!B24 con beta 'Direct Input' + tabla multibusiness vacia.
  6. Financials Multiples: crecimiento del dividendo sin año base (IFERROR).
  7. Financials Multiples: NWC proyectado con intensidad de NWC (antes
     explotaba con un año de ingresos planos y apuntaba a H42/H82 vacias).
  8. Valuation output!C55 (crecimiento Conservador): =PROMEDIO(B27;rf) podia
     superar al Base (bug #10) -> MIN(B27;B29) - 1,5pp.
  9. Valuation output!C106 (crecimiento Optimista): =B27*1,3 quedaba POR
     DEBAJO del Base con crecimiento negativo (bug #11) -> MAX(B27;B29) + 1pp.

Backup de cada formula pisada: reference/backups/plantilla_maestra_formula_backup.json
(y el estado completo previo en plantilla_maestra_pre_fix_formulas.json.gz).

Uso:
    PYTHONPATH=.:scripts python scripts/fix_master_template.py [--sheet-id ID --backup NOMBRE]

Con --sheet-id se aplica a otra copia EN BLANCO de la plantilla (no a una
valoracion ya hecha: estos fixes pisan formulas de escenarios que en una
valoracion suelen estar personalizadas).
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402

MASTER_SHEET_ID = "19PRUFiYsNavUcN6WwHBVlp-VRMozp3rNSE2R1zt7N-g"
BACKUP_PATH = _ROOT / "reference" / "backups" / "plantilla_maestra_formula_backup.json"


def main(argv: list[str]) -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--sheet-id", default=MASTER_SHEET_ID)
    parser.add_argument("--backup", default=None, help="nombre del archivo de backup en reference/backups/")
    args = parser.parse_args(argv)
    global BACKUP_PATH
    if args.backup:
        BACKUP_PATH = BACKUP_PATH.parent / args.backup
    sh = ms.open_sheet(args.sheet_id)
    ms.fix_template_bugs(sh, BACKUP_PATH)
    ms.fix_nwc_projection(sh, BACKUP_PATH)
    ms.write_with_backup(sh, "Input sheet", {"B20": "='Balance Sheet'!L14"},
                         "Other Long-Term Assets es operativo, no activo no operativo", BACKUP_PATH)
    ms.write_with_backup(sh, "Valuation output", {
        "C55": "=MIN('Input sheet'!B27;'Input sheet'!B29)-0,015",
        "C106": "=MAX('Input sheet'!B27;'Input sheet'!B29)+0,01",
    }, "Bugs #10/#11: crecimiento Conservador < Base < Optimista siempre", BACKUP_PATH)
    print(f"Listo: {sh.url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
