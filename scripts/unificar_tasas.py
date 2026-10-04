#!/usr/bin/env python
"""Tasa libre de riesgo, prima de mercado y costo de capital terminal únicos en la cartera (Damodaran), 4-oct-2026.

Damodaran usa, para todas las valoraciones en una misma moneda y fecha, la misma tasa libre de riesgo y la misma prima
de mercado. Las hojas tenían tasas de distintos días de septiembre (4,25% a 5,29%) y dos cortes de prima madura
(4,23% de enero y 4,09% de septiembre). Criterio único al corte del 30-sep-2026:

  - Tasa libre de riesgo: Treasury a 10 años del 30-sep-2026 = 5,29% (Tesoro de EE.UU. / FRED DGS10). Input B35.
  - Prima madura: 4,09%, la implícita de Damodaran de septiembre de 2026 sobre el Treasury sin ajustar (ERPSept26.xlsx,
    C45; reference/mature_market_erp.txt). 'Country equity risk premiums'!B2.
  - Prima país: la de la tabla de Damodaran (columna E). Con el Treasury sin ajustar, EE.UU. no lleva prima país (su
    riesgo de impago ya está en la tasa; sumar el 0,23% sería contarlo dos veces): 'Country equity risk premiums' fila de
    United States, columna E = 0.
  - Costo de capital terminal: el valor por defecto del Ginzu (tasa libre de riesgo + prima madura = 9,38%) en todas las
    empresas de mercados desarrollados (Input B46 = "No"). Brasil conserva su prima país en perpetuidad (Damodaran no la
    elimina salvo que se espere que el país madure): AFYA y PAGS mantienen su diferencial sobre la tasa anterior
    (AFYA 11% → 11,11%; PAGS Ke terminal 12% → 12,30%).
  - ROIC terminal (Input B50): si es un número menor que el nuevo costo de capital terminal, se sube a ese costo (la regla
    de la cartera exige ROIC terminal ≥ costo de capital).

Respaldo de cada celda en reference/revision_dcf_2026-10-04/tasas_respaldo.json. Uso:
    PYTHONPATH=.:scripts python scripts/unificar_tasas.py [--apply] [--solo TK ...]
"""
from __future__ import annotations

import argparse
import glob
import json
import re
import time
from pathlib import Path

from jmr_valuation.io.sheets_auth import get_gspread_client
from audit_master_formulas import MASTER_ID

_ROOT = Path(__file__).resolve().parents[1]
DATOS = _ROOT.parent / "Modelo-JMR-datos" / "valoraciones"
OUT = _ROOT / "reference" / "revision_dcf_2026-10-04" / "tasas_respaldo.json"
RF, ERP_MADURA = 0.0529, 0.0409
TERMINAL_BRASIL = {"AFYA": 0.1111, "PAGS": 0.123}
IN, CE, FCFE = "'Input sheet'", "'Country equity risk premiums'", "'DCF FCFE financiero'"


def hojas() -> dict:
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
    ap.add_argument("--solo", nargs="*")
    a = ap.parse_args()
    gc = get_gspread_client()
    respaldo = json.loads(OUT.read_text()) if OUT.exists() else {}
    for tk, sid in hojas().items():
        if a.solo and tk not in a.solo:
            continue
        sh = gc.open_by_key(sid)
        titulos = {w.title for w in sh.worksheets()}
        rng = [f"{IN}!B35", f"{IN}!B46:B47", f"{IN}!B50", f"{CE}!B2", f"{CE}!A6:E196"]
        if "DCF FCFE financiero" in titulos:
            rng.append(f"{FCFE}!B4")
        v = {r: x.get("values", []) for r, x in zip(rng, sh.values_batch_get(rng, params={"valueRenderOption": "FORMULA"})["valueRanges"])}
        cambios = []

        def put(rango, antes, despues):
            if antes != despues:
                cambios.append({"range": rango, "antes": antes, "values": [[despues]]})

        put(f"{IN}!B35", v[f"{IN}!B35"][0][0], RF)
        put(f"{CE}!B2", v[f"{CE}!B2"][0][0], ERP_MADURA)
        fila_us = next((i for i, r in enumerate(v[f"{CE}!A6:E196"]) if r and r[0] == "United States"), None)
        if fila_us is not None:
            put(f"{CE}!E{6 + fila_us}", v[f"{CE}!A6:E196"][fila_us][4], 0)
        ovr = v[f"{IN}!B46:B47"]
        ovr_si, wt_antes = str(ovr[0][0]).strip(), (ovr[1][0] if len(ovr) > 1 and ovr[1] else None)
        if tk in TERMINAL_BRASIL:
            put(f"{IN}!B46", ovr[0][0], "Yes")
            put(f"{IN}!B47", wt_antes, TERMINAL_BRASIL[tk])
            if f"{FCFE}!B4" in v:
                put(f"{FCFE}!B4", v[f"{FCFE}!B4"][0][0], TERMINAL_BRASIL[tk])
            wt = TERMINAL_BRASIL[tk]
        else:
            put(f"{IN}!B46", ovr[0][0], "No")
            wt = RF + ERP_MADURA
        roic = (v[f"{IN}!B50"] or [[None]])[0][0]
        if isinstance(roic, (int, float)) and 0 < roic < wt - 1e-9:
            put(f"{IN}!B50", roic, round(wt, 4))
        print(f"{tk:7s} " + "; ".join(f"{c['range'].split('!')[0].strip(chr(39))[:7]}!{c['range'].split('!')[1]} "
                                       f"{c['antes']} → {c['values'][0][0]}" for c in cambios))
        if a.apply and cambios:
            respaldo.setdefault(tk, {"sheet_id": sid, "celdas": [{"range": c["range"], "antes": c["antes"]} for c in cambios]})
            OUT.write_text(json.dumps(respaldo, ensure_ascii=False, indent=1, default=str))
            sh.values_batch_update({"valueInputOption": "USER_ENTERED",
                                    "data": [{"range": c["range"], "values": c["values"]} for c in cambios]})
        time.sleep(4)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
