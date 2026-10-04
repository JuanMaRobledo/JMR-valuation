#!/usr/bin/env python
"""Tabla de ventas/capital de Damodaran por empresa (Investment Valuation, cap. 11, p. 44-46), 4-oct-2026.

Para cada empresa, las tres referencias con las que Damodaran elige el ventas/capital, más la usada en la hoja:
  - actual: ingresos LTM / capital invertido (el de 'Valuation output' B41: patrimonio + deuda − caja − no operativos,
    con arrendamientos e I+D capitalizado cuando la hoja los convierte);
  - marginal: Δingresos / Δcapital invertido del último año y de los últimos tres años (cierres anuales), con el capital
    de cada cierre armado igual que B41 desde el balance de la hoja (I+D capitalizado con su historia y su vida). Sin
    ratio cuando el capital o las ventas no crecieron (no hay inversión que medir);
  - sector: «Sales/ Invested Capital (LTM)» de la base de capex de Damodaran (enero de 2026) para su industria;
  - usada: Input B32 (años 1-5) y B33 (años 6-10), con el rendimiento que implica sobre el capital nuevo.
Salida: reference/ventas_capital_2026-10-04.json (la lee scripts/damodaran_stories.py para el análisis).
Uso: PYTHONPATH=.:scripts python scripts/tabla_ventas_capital.py [TK ...]
"""
from __future__ import annotations

import glob
import json
import re
import sys
import time
from pathlib import Path

from jmr_valuation.io.sheets_auth import get_gspread_client

_ROOT = Path(__file__).resolve().parents[1]
DATOS = _ROOT.parent / "Modelo-JMR-datos" / "valoraciones"
SECTOR = _ROOT / "reference" / "damodaran_ventas_capital_sector_2026-01.json"
OUT = _ROOT / "reference" / "ventas_capital_2026-10-04.json"
NO_COMPARABLE = {"Financial Svcs. (Non-bank & Insurance)"}  # el capital de una financiera no es comparable


def fila(g, *nombres):
    for n in nombres:
        for r in g:
            if r and str(r[0]).strip().lower() == n.lower():
                return r
    return None


def num(r, j):
    if r is None or j >= len(r):
        return 0.0
    v = r[j]
    return float(v) if isinstance(v, (int, float)) else 0.0


def main(argv) -> int:
    sector = json.loads(SECTOR.read_text())["sectores"]
    res = json.loads(OUT.read_text()) if OUT.exists() else {}
    gc = get_gspread_client()
    for f in sorted(glob.glob(str(DATOS / "*.json"))):
        d = json.loads(Path(f).read_text())
        tk = d["ticker"]
        if (argv and tk not in argv) or tk == "PAGS":
            continue
        rjs = json.loads((_ROOT / "reference" / "damodaran" / f"{tk}_resultado.json").read_text())
        sh = gc.open_by_key(re.search(r"/d/([^/]+)", d["hojaGoogle"]).group(1))
        rng = ["'Income Statement'!A1:L30", "'Balance Sheet'!A1:L60", "'Input sheet'!B17:B33", "'Valuation output'!B5",
               "'Valuation output'!B41", "'Valuation output'!B42", "'R& D converter'!F7"]
        v = [x.get("values", []) for x in sh.values_batch_get(rng, params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]]
        IS, BS, inp = v[0], v[1], {17 + i: (r[0] if r else None) for i, r in enumerate(v[2])}
        rev_ltm, ic_ltm, roic0 = v[3][0][0], v[4][0][0], v[5][0][0]
        hdr = IS[1]
        rev = fila(IS, "Total Revenues")
        rd = fila(IS, "Research & Development Expenses")
        eq = fila(BS, "Total Shareholders' Equity")
        deuda = [fila(BS, n) for n in ("Short-Term Debt", "Current Portion of Leases", "Long-Term Debt", "Leases")]
        caja = fila(BS, "Total Cash and Cash Equivalents", "Cash and Cash Equivalents")
        lti = fila(BS, "Long-Term Investments")
        con_rd = str(inp.get(17, "")).strip().lower() == "yes"
        vida = int(v[6][0][0]) if con_rd and v[6] and isinstance(v[6][0][0], (int, float)) else 0

        def ic(j):  # capital invertido del cierre de la columna j, como B41
            base = num(eq, j) + sum(num(x, j) for x in deuda) - num(caja, j) - num(lti, j)
            if vida:
                base += sum(num(rd, j - k) * (vida - k) / vida for k in range(1, vida) if j - k >= 1)
            return base

        cols = [j for j in range(1, 11) if j < len(hdr) and re.match(r"[A-Z][a-z]{2} '\d\d", str(hdr[j]))]
        k_ult = cols[-1]
        marg = {}
        for n in (1, 3):  # del cierre de hace n años al último cierre anual (mismo armado del capital en ambos)
            j0 = k_ult - n
            if j0 < 1 or j0 not in cols:
                marg[n] = None
                continue
            dr, di = num(rev, k_ult) - num(rev, j0), ic(k_ult) - ic(j0)
            marg[n] = {"desde": str(hdr[j0]), "hasta": str(hdr[k_ult]), "dventas": round(dr, 1), "dcapital": round(di, 1),
                       "ratio": round(dr / di, 2) if di > 0 and dr > 0 else None}
        ind = rjs.get("industria")
        s1, s2, m_obj, t_mg = inp.get(32), inp.get(33), inp.get(30), inp.get(25)
        u = (m_obj or 0) * (1 - (t_mg or 0))
        res[tk] = {"industria": ind, "actual": round(rev_ltm / ic_ltm, 2) if ic_ltm else None,
                   "ventas_ltm": rev_ltm, "capital_ltm": ic_ltm, "roic_actual": roic0,
                   "marginal_ultimo": marg[1], "marginal_3a": marg[3],
                   "sector": None if ind in NO_COMPARABLE else sector.get(ind),
                   "usada": [s1, s2], "rendimiento_capital_nuevo": [round(u * s1, 4), round(u * s2, 4)],
                   "con_id": con_rd, "vida_id": vida}
        r_ = res[tk]
        print(f"{tk:5s} actual {r_['actual']} | marginal 1a {(marg[1] or {}).get('ratio')} 3a {(marg[3] or {}).get('ratio')} | "
              f"sector {r_['sector']} | usada {s1:.2f}/{s2:.2f}")
        time.sleep(4)
    OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
