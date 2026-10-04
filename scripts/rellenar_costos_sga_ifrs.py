#!/usr/bin/env python
"""Costo de ventas y SG&A de PAGS (20-F, NIIF, en BRL) en la hoja en dólares, 4-oct-2026.

Mismo criterio que scripts/rellenar_costos_sga.py. Fuente por año: el estado de resultados renderizado del 20-F más
reciente que trae ese año (R*.htm de EDGAR). LTM = 20-F 2025 + 1S-2026 − 1S-2025 del 6-K del 2T-2026 (sin XBRL; cifras
del estado de resultados intermedio, en miles de BRL, accesión 0001554855-26-001791). Conversión con el tipo de cambio
IMPLÍCITO de la hoja (ingresos en USD de la hoja ÷ ingresos en BRL), como en scripts/auditar_estados_ifrs.py.

  costo de ventas = «cost of sales and services» («cost of services» en el 20-F 2025);
  SG&A = gastos de venta + gasto de pérdidas crediticias + gastos administrativos (hasta el 20-F 2024 la pérdida
         crediticia venía dentro de «selling expenses»; sumarla deja toda la serie con la misma definición).

Uso: PYTHONPATH=.:scripts python scripts/rellenar_costos_sga_ifrs.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from jmr_valuation.io.sheets_auth import get_gspread_client
from rellenar_costos_sga import DATOS, FILA, IS, OUT, estado, get

TK, CIK = "PAGS", 1712807
REV = r"^total revenue( and income)?$"
COGS = r"^cost of (sales and )?services"
SGA = [r"^selling expenses?$", r"^credit loss allowance expenses", r"^administrative expenses"]
# 6-K 2T-2026 (miles de BRL): 1S-2026, 1S-2025
SEIS_K = {"rev": (10_085_850, 9_908_326), "cogs": (4_685_122, 4_770_941),
          "sga": (794_461 + 129_624 + 501_158, 826_599 + 48_885 + 469_598)}


def main() -> int:
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{CIK:010d}.json"))
    r = s["filings"]["recent"]
    f20 = sorted([(r["filingDate"][i], r["accessionNumber"][i], r["reportDate"][i]) for i in range(len(r["form"]))
                  if r["form"][i] == "20-F" and "2022" <= r["reportDate"][i] <= "2025-12-31"])
    anual = {}
    for fd, acc, rd in f20:  # el más reciente sobrescribe
        est = estado(CIK, acc)
        for per in {k for v in est.values() for k in v if k[0] == 12}:
            def tomar(pats):
                vals = [abs(v[per]) for lab, v in est.items() if "#" not in lab and per in v
                        and any(re.search(p, lab) for p in pats)]
                return sum(vals) if vals else None
            anual[per[1].year] = {"rev": tomar([REV]), "cogs": tomar([COGS]), "sga": tomar(SGA), "src": f"20-F {rd} ({acc})"}
    fy = anual[2025]
    ltm = {c: fy[c] + (SEIS_K[c][0] - SEIS_K[c][1]) / 1e3 for c in ("rev", "cogs", "sga")}
    ltm["src"] = "20-F 2025 + 1S-2026 − 1S-2025 (6-K 2T-2026, 0001554855-26-001791)"
    sid = re.search(r"/d/([^/]+)", json.loads(next(DATOS.glob(f"{TK}-*.json")).read_text())["hojaGoogle"]).group(1)
    g = get_gspread_client().open_by_key(sid).values_get(f"'{IS}'!A1:L13", params={"valueRenderOption": "UNFORMATTED_VALUE"})["values"]
    cambios = []
    for j, h in enumerate(g[1]):
        m = re.match(r"Dec '(\d{2})", str(h))
        rec = ltm if h == "LTM" else anual.get(2000 + int(m.group(1))) if m else None
        if not rec or not rec.get("rev"):
            continue
        col = chr(65 + j)
        v = {c: g[r_ - 1][j] for c, r_ in FILA.items()}
        fx = v["rev"] / rec["rev"]
        cogs, sga = round(rec["cogs"] * fx, 2), round(rec["sga"] * fx, 2)
        gp, otro = round(v["rev"] - cogs, 2), round(v["other"] - (cogs - v["cogs"]) - (sga - v["sga"]), 2)
        src = f"SEC {rec['src']}, en USD con el tipo de cambio implícito de la hoja ({fx:.5f} USD/BRL)"
        cambios += [
            {"hoja": IS, "celda": f"{col}5", "antes": v["cogs"], "despues": cogs, "motivo": f"Costo de ventas {h}: {src}."},
            {"hoja": IS, "celda": f"{col}6", "antes": v["gp"], "despues": gp, "motivo": f"Utilidad bruta {h} = ingresos − costo de ventas."},
            {"hoja": IS, "celda": f"{col}7", "antes": v["gpm"], "despues": round(gp / v["rev"], 4), "motivo": f"Margen bruto {h}."},
            {"hoja": IS, "celda": f"{col}8", "antes": v["sga"], "despues": sga,
             "motivo": f"SG&A {h} (ventas + pérdidas crediticias + administración): {src}."},
            {"hoja": IS, "celda": f"{col}11", "antes": v["other"], "despues": otro,
             "motivo": f"Otros gastos operativos {h}: se les resta lo que pasó a costo de ventas/SG&A; la utilidad operativa no cambia."},
        ]
        print(f"{h:7s} fx {fx:.5f} costo {cogs:9.2f} SG&A {sga:8.2f} margen bruto {gp / v['rev']:.1%} otros {v['other']} -> {otro}")
    (OUT / f"{TK}_costos_sga.json").write_text(json.dumps(cambios, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
