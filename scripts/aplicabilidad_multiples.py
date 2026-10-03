#!/usr/bin/env python
"""Aplicabilidad de los múltiplos en la ponderación (paso 6.1 del prompt de valoración v4), 3-oct-2026.

El paso 6.1 dice que un múltiplo cuya métrica proyectada de FY+1 a FY+3 es negativa o casi cero NO aplica y que se
resuelve en la ponderación. La plantilla solo tomaba el peso de la categoría (tabla I5:U11 del Resumen), así que un
método sin sentido seguía pesando: en SHAK, EV/FCFF (FCFF negativo en FY+1..FY+3) daba precios negativos con 15% de
peso y hundía los múltiplos consolidados.

Cambio de plantilla (maestra y todas las hojas, una sola fórmula):
  - 'Resumen de Valoración'!F5 = "¿Aplica? (paso 6.1)"; F7:F11 = "No" cuando el método no aplica (vacío = aplica).
  - B7:B11 = peso de la categoría × (F ≠ "No"), reescalado para que los múltiplos aplicables sumen el mismo peso
    total de múltiplos de la categoría (1 − peso del DCF). Con F vacío el resultado es idéntico al anterior.
También corrige 'Resumen de Valoración'!D38 («Valor esperado de historias · DCF hoy»), que en varias hojas quedó como
un número fijo desactualizado (alimenta D36 y 'Descuento de múltiplos'!D43): pasa a ='Escenarios e historias'!H10,
como en ADBE.

Respaldo de cada celda antes de escribir en reference/backups/aplicabilidad_multiples_<fecha>/.

Uso:
    PYTHONPATH=.:scripts python scripts/aplicabilidad_multiples.py [--apply] [--no-aplica SHAK:EV/FCFF,P/FCFE]
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import re
import time
from pathlib import Path

from jmr_valuation.io.sheets_auth import get_gspread_client
from audit_master_formulas import MASTER_ID

_ROOT = Path(__file__).resolve().parent.parent
DATOS = _ROOT.parent / "Modelo-JMR-datos" / "valoraciones"
RES = "'Resumen de Valoración'"
ROWS = {"EV/EBITDA": 7, "EV/FCFF": 8, "P/E": 9, "P/FCFE": 10, "P/OCF": 11}
HEADER = "¿Aplica? (paso 6.1)"


def peso(r: int) -> str:
    cat = "MATCH($G$3; $I$5:$U$5; 0)"
    return (f'=IFERROR(VLOOKUP(A{r}; $I$6:$U$11; {cat}; FALSE)*($F{r}<>"No")*(1-$B$6)'
            f'/SUMPRODUCT(INDEX($I$7:$U$11; 0; {cat})*($F$7:$F$11<>"No")); 0)')


def targets() -> dict[str, str]:
    out = {"MAESTRA": MASTER_ID}
    for f in sorted(glob.glob(str(DATOS / "*.json"))):
        d = json.loads(Path(f).read_text())
        m = re.search(r"/d/([^/]+)", d.get("hojaGoogle", ""))
        if m:
            out[d["ticker"]] = m.group(1)
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--no-aplica", action="append", default=[], help="TICKER:METODO[,METODO]")
    ap.add_argument("--solo", nargs="*", help="limitar a estos tickers (MAESTRA incluida si se nombra)")
    a = ap.parse_args()
    no_aplica = {}
    for spec in a.no_aplica:
        tk, ms = spec.split(":")
        no_aplica[tk] = [m.strip() for m in ms.split(",")]
    fecha = dt.date.today().isoformat()
    bdir = _ROOT / "reference" / "backups" / f"aplicabilidad_multiples_{fecha}"
    client = get_gspread_client()
    resumen = {}
    for tk, sid in targets().items():
        if a.solo and tk not in a.solo:
            continue
        time.sleep(8)  # cuota de 60 lecturas/min
        sh = client.open_by_key(sid)
        rngs = [f"{RES}!B6:B11", f"{RES}!F5:F11", f"{RES}!D38"]
        before = {r: v.get("values", []) for r, v in zip(rngs, sh.values_batch_get(
            rngs, params={"valueRenderOption": "FORMULA"})["valueRanges"])}
        vals_before = sh.values_get(f"{RES}!B6:B11", params={"valueRenderOption": "UNFORMATTED_VALUE"}).get("values", [])
        data = [{"range": f"{RES}!F5", "values": [[HEADER]]}]
        data += [{"range": f"{RES}!B{r}", "values": [[peso(r)]]} for r in ROWS.values()]
        flags = no_aplica.get(tk, [])
        data += [{"range": f"{RES}!F{r}", "values": [["No" if m in flags else ""]]} for m, r in ROWS.items()]
        d38 = (before[f"{RES}!D38"] or [[""]])[0][0] if before[f"{RES}!D38"] else ""
        fix_d38 = tk != "MAESTRA" and isinstance(d38, (int, float))
        if fix_d38:
            data.append({"range": f"{RES}!D38", "values": [["='Escenarios e historias'!H10"]]})
        resumen[tk] = {"sheet_id": sid, "antes": before, "pesos_antes": vals_before, "no_aplica": flags,
                       "d38_corregida": fix_d38}
        print(f"{tk:7s} no aplica {flags or '-'}; D38 fija {d38 if fix_d38 else '-'}")
        if a.apply:
            bdir.mkdir(parents=True, exist_ok=True)
            (bdir / f"{tk}.json").write_text(json.dumps(resumen[tk], ensure_ascii=False, indent=1, default=str))
            sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": data})
            time.sleep(2)
            after = sh.values_get(f"{RES}!B6:B12", params={"valueRenderOption": "UNFORMATTED_VALUE"}).get("values", [])
            resumen[tk]["pesos_despues"] = after
            same = [row[0] for row in vals_before] == [row[0] for row in after[:6]]
            print(f"        pesos {[round(r[0], 4) for r in after]} {'(sin cambio)' if same else '(CAMBIO)'}")
            time.sleep(3)
    if a.apply:
        (bdir / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
