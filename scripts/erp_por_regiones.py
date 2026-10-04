#!/usr/bin/env python
"""Prima de riesgo de mercado ponderada por las ventas de cada región (Damodaran), 4-oct-2026.

Damodaran mide la exposición al riesgo país por dónde opera la empresa (sus ventas), no por dónde está registrada.
La plantilla tiene la calculadora «Operating regions» ('Cost of capital worksheet' G22:K33) y la tabla regional de
Damodaran ('Country equity risk premiums' A202:E211, ERP = prima madura B2 + prima país de la región). Aquí:
  - se escriben las ventas del último informe anual por región (XBRL del 10-K / 20-F; ver reference/erp_regiones_2026-10-04.json);
  - 'Cost of capital worksheet'!B26 = "Operating regions" (la prima usada es K33, el promedio ponderado);
  - Norteamérica lleva prima país 0 (E209), igual que EE.UU.: con el Treasury sin ajustar su riesgo ya está en la tasa;
  - dos filas propias: 31 = EMEA (prima país 1,64%, la de la plantilla: Europa occidental con Oriente Medio y África)
    y 32 = «Fuera de EE.UU. sin desglose» (1,80%: la prima global de Damodaran sin el peso de EE.UU.) o, en NVO y ZTS,
    «Mercados emergentes» (4,33%: promedio de Centro y Sudamérica, Europa del Este, Oriente Medio y África).
AFYA y PAGS (100% Brasil) siguen con el país de registro. Respaldo en reference/revision_dcf_2026-10-04/erp_regiones_respaldo.json.
Uso: PYTHONPATH=.:scripts python scripts/erp_por_regiones.py [--apply] [--solo TK ...]
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
FUENTE = _ROOT / "reference" / "erp_regiones_2026-10-04.json"
OUT = _ROOT / "reference" / "revision_dcf_2026-10-04" / "erp_regiones_respaldo.json"
CC, CE = "'Cost of capital worksheet'", "'Country equity risk premiums'"
FILA = {"Africa": 22, "Asia": 23, "Australia & New Zealand": 24, "Caribbean": 25, "Central and South America": 26,
        "Eastern Europe": 27, "Middle East": 28, "North America": 29, "Western Europe": 30, "EMEA": 31, "RESTO": 32}
CRP_EMEA, CRP_SIN_DESGLOSE, CRP_EMERGENTES = 0.0164, 0.0180, 0.0433  # la hoja usa coma decimal en fórmulas


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--solo", nargs="*")
    a = ap.parse_args()
    src = json.loads(FUENTE.read_text())["empresas"]
    ids = {"MAESTRA": MASTER_ID}
    for f in sorted(glob.glob(str(DATOS / "*.json"))):
        d = json.loads(Path(f).read_text())
        m = re.search(r"/d/([^/]+)", d.get("hojaGoogle", ""))
        if m:
            ids[d["ticker"]] = m.group(1)
    gc = get_gspread_client()
    respaldo = json.loads(OUT.read_text()) if OUT.exists() else {}
    for tk, sid in ids.items():
        if a.solo and tk not in a.solo:
            continue
        sh = gc.open_by_key(sid)
        antes = sh.values_get(f"{CC}!G22:I32", params={"valueRenderOption": "FORMULA"}).get("values", [])
        b26 = sh.values_get(f"{CC}!B26").get("values", [[""]])[0][0]
        data = [{"range": f"{CE}!E209", "values": [[0]]},
                {"range": f"{CC}!G31:I31", "values": [["EMEA", "", f"={CE}!$B$2+{str(CRP_EMEA).replace('.', ',')}"]]}]
        e = src.get(tk)
        if e:
            resto = e.get("resto", "sin desglose")
            crp = CRP_EMERGENTES if resto == "emergentes" else CRP_SIN_DESGLOSE
            data.append({"range": f"{CC}!G32:I32", "values": [[
                "Mercados emergentes" if resto == "emergentes" else "Fuera de EE.UU. sin desglose", "", f"={CE}!$B$2+{str(crp).replace('.', ',')}"]]})
            for reg, fila in FILA.items():
                data.append({"range": f"{CC}!H{fila}", "values": [[e["ventas"].get(reg, "")]]})
            data.append({"range": f"{CC}!B26", "values": [["Operating regions"]]})
        if a.apply:
            respaldo.setdefault(tk, {"sheet_id": sid, "G22:I32": antes, "B26": b26})
            OUT.write_text(json.dumps(respaldo, ensure_ascii=False, indent=1, default=str))
            sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": data})
            time.sleep(2)
            k = sh.values_get(f"{CC}!B28", params={"valueRenderOption": "UNFORMATTED_VALUE"}).get("values", [[None]])[0][0]
            print(f"{tk:7s} prima usada {k:.4%}" if isinstance(k, (int, float)) else f"{tk:7s} prima usada {k}" + (f"  ({b26} → Operating regions)" if e else ""))
        else:
            print(f"{tk:7s} {b26} → {'Operating regions' if e else b26}; ventas {e['ventas'] if e else '-'}")
        time.sleep(3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
