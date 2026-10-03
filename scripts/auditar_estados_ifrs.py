#!/usr/bin/env python
"""Auditoría de los estados de emisores extranjeros (20-F, NIIF) contra la SEC, 3-oct-2026.

Las hojas de AFYA, NVO, ONON y PAGS están en dólares; el XBRL de la SEC (taxonomía ifrs-full) está en la moneda de
presentación (BRL, DKK, CHF). No se usa un tipo de cambio externo: para cada cierre se toma el tipo de cambio IMPLÍCITO
de la propia hoja (ingresos en USD de la hoja ÷ ingresos de la SEC para flujos; activos totales para saldos), así la
corrección queda en la misma base que el resto de la hoja. Solo se corrigen los errores del importador ya validados
en las empresas de 10-K:
  - cambio neto de caja con la serie de relleno de la plantilla (sin dato en la SEC: se deja vacío);
  - EPS básico copiado del diluido (años con utilidad);
  - utilidad consolidada sin minoritarios (se compensa en «Other Adjustments» del flujo);
  - patrimonio total sin minoritarios.
Lo demás se informa. Los 6-K trimestrales no traen XBRL, así que la columna LTM no se puede verificar aquí.

Uso: PYTHONPATH=.:scripts python scripts/auditar_estados_ifrs.py TICKER ...
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

import audit_statements_sec as sec
from auditar_estados_sec import BASURA_CAJA, fin_de_columna, _d
from jmr_valuation.io.sheets_auth import get_gspread_client

_ROOT = Path(__file__).resolve().parents[1]
DATOS = _ROOT.parent / "Modelo-JMR-datos" / "valoraciones"
OUT = _ROOT / "reference" / "auditoria_estados_2026-10-03"
CORTE = "2026-09-30"
IS, BS, CF = "Income Statement", "Balance Sheet", "Cash Flow Statement"


def anual(f, tags, saldo=False):
    """{año: valor} de 20-F (presentación más reciente); varias etiquetas se suman si la lista es una tupla."""
    out = {}
    for t in tags:
        partes = t if isinstance(t, tuple) else (t,)
        series = []
        for p in partes:
            best = {}
            for u, xs in f.get(p, {}).get("units", {}).items():
                for x in xs:
                    if not x.get("form", "").startswith("20-F") or x.get("filed", "") > CORTE:
                        continue
                    if saldo != ("start" not in x):
                        continue
                    if not saldo and not 350 <= (_d(x["end"]) - _d(x["start"])).days <= 380:
                        continue
                    k = x["end"][:4]
                    if k not in best or x["filed"] > best[k][0]:
                        best[k] = (x["filed"], x["val"])
            series.append({k: v for k, (_, v) in best.items()})
        comunes = set.intersection(*(set(s) for s in series)) if series else set()
        for k in comunes:
            out.setdefault(k, sum(s[k] for s in series))
    return out


def main(argv):
    gc = get_gspread_client()
    ciks = sec.cik_map()
    for tk in argv:
        sec.facts(tk, ciks[tk])
        f = json.loads((sec.CACHE / f"{tk}.json").read_text())["facts"]["ifrs-full"]
        rev = anual(f, ["Revenue", "RevenueFromContractsWithCustomers"])
        act = anual(f, ["Assets"], saldo=True)
        pl, plo = anual(f, ["ProfitLoss"]), anual(f, ["ProfitLossAttributableToOwnersOfParent"])
        eq, eqo = anual(f, ["Equity"], saldo=True), anual(f, ["EquityAttributableToOwnersOfParent"], saldo=True)
        eb, ed = anual(f, ["BasicEarningsLossPerShare"]), anual(f, ["DilutedEarningsLossPerShare"])
        dc = anual(f, ["IncreaseDecreaseInCashAndCashEquivalents",
                       ("IncreaseDecreaseInCashAndCashEquivalentsBeforeEffectOfExchangeRateChanges",
                        "EffectOfExchangeRateChangesOnCashAndCashEquivalents")])
        sid = re.search(r"/d/([^/]+)", json.loads(next(DATOS.glob(f"{tk}-*.json")).read_text())["hojaGoogle"]).group(1)
        sh = gc.open_by_key(sid)
        g = {t: v.get("values", []) for t, v in zip((IS, BS, CF), sh.values_batch_get(
            [f"'{t}'!A1:L60" for t in (IS, BS, CF)], params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"])}
        row = lambda t, lab: next((i for i, r in enumerate(g[t]) if r and r[0] == lab and len(r) > 4), None)  # noqa: E731
        cell = lambda t, i, j: (g[t][i][j] if i is not None and j < len(g[t][i]) else None)  # noqa: E731
        hdr = g[IS][1]
        cambios, informe = [], []

        def put(t, i, j, new, why, old):
            if isinstance(new, (int, float)) and isinstance(old, (int, float)) and "Net Change" not in why and "caja" not in why:
                umbral = 0.01 if "EPS" in why else max(0.5, abs(old) * 0.002)
                if abs(new - old) < umbral - 1e-9:
                    return  # diferencia de redondeo, no un error
            cambios.append({"hoja": t, "celda": f"{chr(65 + j)}{i + 1}", "antes": old, "despues": new, "motivo": why})

        rR, rA = row(IS, "Total Revenues"), row(BS, "Total Assets")
        for j, h in enumerate(hdr):
            fin = fin_de_columna(h)
            if j < 4 or h == "LTM":
                continue
            y = str(fin.year) if fin else None
            hr, ha = cell(IS, rR, j), cell(BS, rA, j)
            fx_f = (hr / (rev[y] / 1e6)) if y in rev and isinstance(hr, (int, float)) and hr else None
            fx_s = (ha / (act[y] / 1e6)) if y in act and isinstance(ha, (int, float)) and ha else None
            src = f"SEC 20-F {y} (ifrs-full) convertido con el tipo de cambio implícito de la hoja"
            # cambio neto de caja
            i = row(CF, "Net Change in Cash")
            v = cell(CF, i, j)
            if isinstance(v, (int, float)) and any(abs(v - b) < 1e-6 for b in BASURA_CAJA):
                if y in dc and fx_f:
                    put(CF, i, j, round(dc[y] / 1e6 * fx_f, 2), f"Cambio neto de caja {h}: {src} ({fx_f:.4f} USD por unidad).", v)
                else:
                    put(CF, i, j, "", f"Cambio neto de caja {h}: valor de relleno de la plantilla y sin dato en la SEC; se deja vacío.", v)
            if not fx_f:
                continue
            # EPS básico copiado del diluido
            ib, idl = row(IS, "Basic EPS"), row(IS, "Diluted EPS")
            b, dl = cell(IS, ib, j), cell(IS, idl, j)
            if isinstance(b, (int, float)) and b == dl and b > 0 and y in eb and y in ed and eb[y] != ed[y]:
                nb = round(eb[y] * fx_f * (b / (ed[y] * fx_f)), 2)  # misma base de acciones (ADS) que la hoja
                put(IS, ib, j, nb, f"EPS básico {h}: {src}; la hoja copiaba el diluido (escala de ADS de la hoja).", b)
            # utilidad consolidada con minoritarios
            ic = row(IS, "Consolidated Net Income")
            c = cell(IS, ic, j)
            if isinstance(c, (int, float)) and y in pl and y in plo and abs(pl[y] - plo[y]) > 1e5:
                if abs(c - plo[y] / 1e6 * fx_f) <= max(0.3, abs(c) * 0.01):
                    nv = round(pl[y] / 1e6 * fx_f, 2)
                    put(IS, ic, j, nv, f"Utilidad consolidada {h} con minoritarios (ProfitLoss): {src}.", c)
                    rc, ro = row(CF, "Net Income"), row(CF, "Other Adjustments")
                    cn, oa = cell(CF, rc, j), cell(CF, ro, j)
                    if isinstance(cn, (int, float)) and isinstance(oa, (int, float)) and abs(cn - c) < 1e-6:
                        put(CF, rc, j, nv, "El flujo de caja parte de la utilidad consolidada.", cn)
                        put(CF, ro, j, round(oa - (nv - cn), 2), "Compensa el cambio de la utilidad para no mover el flujo operativo.", oa)
            # patrimonio total con minoritarios
            if fx_s:
                it = row(BS, "Total Shareholders' Equity")
                te = cell(BS, it, j)
                if isinstance(te, (int, float)) and y in eq and y in eqo and abs(eq[y] - eqo[y]) > 1e5:
                    if abs(te - eqo[y] / 1e6 * fx_s) <= max(0.3, abs(te) * 0.01):
                        put(BS, it, j, round(eq[y] / 1e6 * fx_s, 2), f"Patrimonio total {h} con minoritarios: SEC 20-F {y} con el tipo de cambio implícito de la hoja.", te)
        # informe: LTM que repite el cierre y filas en cero
        for t in (IS, BS, CF):
            for r in g[t]:
                if r and len(r) > 11 and isinstance(r[10], (int, float)) and r[10] != 0 and r[10] == r[11] and t == BS:
                    informe.append(f"{t}: {r[0]} LTM repite el cierre ({r[10]})")
        ic0 = row(BS, "Cash and Cash Equivalents")
        if ic0 is not None and all(cell(BS, ic0, j) in (0, "", None) for j in range(4, 12)):
            informe.append("Balance Sheet: caja en 0 en todos los cierres (el importador no la trae)")
        (OUT / f"{tk}_cambios.json").write_text(json.dumps(cambios, ensure_ascii=False, indent=1))
        (OUT / f"{tk}_diagnostico.json").write_text(json.dumps({"informe": informe}, ensure_ascii=False, indent=1))
        print(f"{tk}: {len(cambios)} cambios")
        for c in cambios:
            print(f"   {c['hoja'][:4]} {c['celda']:4s} {str(c['antes']):>10} -> {str(c['despues']):>10}  {c['motivo'][:90]}")
        for x in informe:
            print("   informa:", x)
        time.sleep(5)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
