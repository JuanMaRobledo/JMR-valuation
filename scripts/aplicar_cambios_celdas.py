#!/usr/bin/env python
"""Aplica a una hoja del Modelo JMR una lista revisada de cambios de celdas, con respaldo y nota (3-oct-2026).

Entrada: JSON con [{"hoja", "celda", "antes", "despues", "motivo"}, ...] (p. ej.
reference/auditoria_estados_2026-10-03/SHAK_cambios.json, armado contra la SEC). Antes de escribir comprueba que cada
celda siga teniendo el valor «antes» (si alguien la cambió, no la toca y lo informa), guarda el valor vigente en
<json>_respaldo.json y deja en cada celda una nota con antes, después y motivo.

Uso: PYTHONPATH=.:scripts python scripts/aplicar_cambios_celdas.py SHAK reference/auditoria_estados_2026-10-03/SHAK_cambios.json [--apply]
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
import time
from pathlib import Path

from jmr_valuation.io.sheets_auth import get_gspread_client

_ROOT = Path(__file__).resolve().parents[1]
DATOS = _ROOT.parent / "Modelo-JMR-datos" / "valoraciones"


def main(argv: list[str]) -> int:
    tk, path = argv[0], Path(argv[1])
    apply = "--apply" in argv
    cambios = json.loads(path.read_text())
    sid = re.search(r"/d/([^/]+)", json.loads(next(DATOS.glob(f"{tk}-*.json")).read_text())["hojaGoogle"]).group(1)
    sh = get_gspread_client().open_by_key(sid)
    rngs = [f"'{c['hoja']}'!{c['celda']}" for c in cambios]
    cur = [(r.get("values") or [[None]])[0][0] for r in
           sh.values_batch_get(rngs, params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]]
    ok, saltar = [], []
    for c, v in zip(cambios, cur):
        same = (v == c["antes"]) or (isinstance(v, (int, float)) and isinstance(c["antes"], (int, float))
                                     and abs(v - c["antes"]) < 1e-6)
        (ok if same else saltar).append({**c, "vigente": v})
    for c in saltar:
        print(f"NO SE TOCA {c['hoja']}!{c['celda']}: vigente {c['vigente']} ≠ antes {c['antes']}")
    print(f"{tk}: {len(ok)} cambios listos, {len(saltar)} omitidos")
    if not apply:
        return 0
    path.with_name(path.stem + "_respaldo.json").write_text(json.dumps(
        {"sheet_id": sid, "fecha": dt.date.today().isoformat(), "celdas": ok, "omitidas": saltar}, ensure_ascii=False, indent=1))
    sh.values_batch_update({"valueInputOption": "USER_ENTERED",
                            "data": [{"range": f"'{c['hoja']}'!{c['celda']}", "values": [[c["despues"]]]} for c in ok]})
    hoy = dt.date.today().strftime("%d-%b-%Y")
    for hoja in sorted({c["hoja"] for c in ok}):
        ws = sh.worksheet(hoja)
        ws.update_notes({c["celda"]: f"Auditoría SEC {hoy}: antes {c['antes']}, ahora {c['despues']}. {c['motivo']}"
                         for c in ok if c["hoja"] == hoja})
        time.sleep(2)
    print(f"{tk}: aplicados {len(ok)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
