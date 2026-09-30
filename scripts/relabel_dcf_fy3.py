"""Cambia el rótulo 'DCF Damodaran' de 'Resumen de Valoración'!A6 por 'DCF Damodaran (llevado a FY+3)'.

La fila 6 del Resumen es el DCF de hoy × (1 + Ke)^3, para ponerlo en la misma fecha que los
múltiplos a FY+3; el rótulo viejo se confundía con el «DCF hoy (valor presente)» de la fila 32.
Como el peso de B6 se busca con VLOOKUP(A6; tabla de pesos), B6 pasa a buscar el texto fijo
"DCF Damodaran" (la clave de la tabla no cambia). Solo toca hojas cuyo A6 es exactamente
'DCF Damodaran' y cuyo B6 hace VLOOKUP(A6...; es idempotente.

Uso:
    python scripts/relabel_dcf_fy3.py --targets-json reference/descuento_multiples_targets.json [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from discount_multiples import _open  # noqa: E402
from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

NEW = "DCF Damodaran (llevado a FY+3)"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--targets-json", nargs="+", required=True)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    client = get_gspread_client()
    targets = [t for f in a.targets_json for t in json.loads(Path(f).read_text())]
    for sid, name in targets:
        try:
            sh = _open(client, sid)
            ws = sh.worksheet("Resumen de Valoración")
            a6, b6 = ws.get("A6:B6", value_render_option="FORMULA")[0][:2]
        except Exception as exc:  # noqa: BLE001
            print(f"{name[:45]:45s} omitida: {str(exc)[:60]}")
            continue
        if a6 == NEW:
            print(f"{name[:45]:45s} ya tenía el rótulo nuevo")
        elif a6 != "DCF Damodaran" or "VLOOKUP(A6" not in str(b6):
            print(f"{name[:45]:45s} omitida: A6={a6!r} B6={str(b6)[:40]!r}")
        else:
            new_b6 = str(b6).replace("VLOOKUP(A6", 'VLOOKUP("DCF Damodaran"', 1)
            if not a.dry_run:
                ws.update([[NEW, new_b6]], "A6:B6", value_input_option="USER_ENTERED")
                chk = ws.get("A6:B6")[0]
                ok = chk[0] == NEW and chk[1] not in ("", "#N/A")
            else:
                ok = True
            print(f"{name[:45]:45s} {'OK' if ok else 'REVISAR'} peso DCF = {ws.get('B6')[0][0] if not a.dry_run else '(dry-run)'}")
        time.sleep(3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
