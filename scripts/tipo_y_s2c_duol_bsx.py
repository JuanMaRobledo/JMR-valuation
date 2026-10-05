#!/usr/bin/env python
"""Ciclo de vida de Damodaran y ventas/capital de DUOL (5-oct-2026).

Clasificación (Damodaran, The Corporate Life Cycle, 2024: crecimiento de ventas, márgenes y reinversión/flujo de caja):
  - DUOL: crecimiento alto que pasa a crecimiento maduro (ventas +39% en 2025 y +18% en el 2T26, margen operativo en
    alza, se autofinancia y recompra acciones) -> tipo «Crecimiento» (antes «Software»; los pesos son los mismos).
  - BSX: madura (US$21.000 millones de ventas que crecen ~6-7%, márgenes estables, flujo libre de ~US$3.800 millones y
    recompras) -> tipo «Madura» (antes «Crecimiento»): el precio relativo pesa P/E y EV/EBITDA como en una empresa madura.
Ventas/capital de DUOL: el capital invertido de la hoja incluía US$206 millones de impuestos diferidos activos creados al
liberar la reserva de valuación en el 3T25 (no es capital operativo; mismo criterio que UBER y NVDA). Sin ellos, el
ventas/capital es 2,45 hoy y 3,0-3,2 en el marginal de 1 y 3 años: los clientes prepagan (ingresos diferidos de US$505
millones) y financian buena parte del crecimiento. Se usa 3,0 en los años 1-5 (marginal de tres años) y 2,45 en los 6-10
(el de hoy, camino al sector: 1,35); rinden ~61% y ~50% sobre el capital nuevo frente a un ROIC actual de ~53%.
Respaldo en reference/revision_dcf_2026-10-05/tipo_s2c_respaldo_<T>.json.

Uso: PYTHONPATH=.:scripts python scripts/tipo_y_s2c_duol_bsx.py [--apply]
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
NOTA_TIPO = {
    "DUOL": ("Tipo de empresa «Crecimiento» (ciclo de vida de Damodaran: crecimiento alto que pasa a crecimiento maduro; "
             "ventas +39% en 2025, margen en alza, flujo libre positivo y recompras). Antes «Software», con los mismos pesos. "
             "Cambio del 5-oct-2026."),
    "BSX": ("Tipo de empresa «Madura» (ciclo de vida de Damodaran: US$21.000 millones de ventas que crecen ~6-7%, márgenes "
            "estables, flujo libre alto y recompras). Antes «Crecimiento». Cambio del 5-oct-2026."),
}
CAMBIOS = {
    "DUOL": {"Resumen de Valoración": {"G3": "Crecimiento"}, "Input sheet": {"B32": 3.0, "B33": 2.45}},
    "BSX": {"Resumen de Valoración": {"G3": "Madura"}},
}
NOTA_S2C = ("Ventas/capital {v}: el capital invertido sin los impuestos diferidos activos de la liberación de la reserva de "
            "valuación (US$206 millones al 30-jun-2026) da 2,45 hoy, 3,23 marginal de un año y 3,04 de tres años; sector "
            "1,35. Años 1-5: 3,0 (marginal de tres años); años 6-10: 2,45 (el de hoy). Antes 1,79, calculado sin el capital de "
            "trabajo negativo de los prepagos. Cambio del 5-oct-2026.")


def main(argv: list[str]) -> int:
    for tk, hojas in CAMBIOS.items():
        sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
        sh = ms.open_sheet(sid)
        for hoja, celdas in hojas.items():
            antes = [sh.values_get(f"'{hoja}'!{c}", params={"valueRenderOption": "UNFORMATTED_VALUE"}).get("values", [[None]])[0][0]
                     for c in celdas]
            print(f"{tk} {hoja}: {dict(zip(celdas, antes))} -> {celdas}")
            if "--apply" not in argv:
                continue
            ms.write_with_backup(sh, hoja, celdas, f"Ciclo de vida y ventas/capital ({tk}, 5-oct-2026)",
                                 OUT / f"tipo_s2c_respaldo_{tk}.json")
            notas = {"G3": NOTA_TIPO[tk]} if "G3" in celdas else {c: NOTA_S2C.format(v=str(v).replace(".", ","))
                                                                    for c, v in celdas.items()}
            sh.worksheet(hoja).update_notes(notas)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
