#!/usr/bin/env python
"""Auditoría de los estados financieros de las hojas contra la SEC (XBRL companyfacts), 3-oct-2026.

Generaliza la revisión hecha a mano en SHAK (reference/auditoria_estados_2026-10-03/SHAK_cambios.json). Para cada
empresa que presenta 10-K/10-Q compara, columna por columna (cierres fiscales y LTM), las filas de 'Income Statement',
'Balance Sheet' y 'Cash Flow Statement' con la etiqueta XBRL equivalente, y propone corregir solo los tipos de error
del importador ya validados:
  - utilidad neta consolidada (con minoritarios, ProfitLoss) y su reflejo en el flujo de caja (se compensa en
    «Other Adjustments» para no mover el flujo operativo reportado);
  - EPS básico y diluido;
  - patrimonio total con minoritarios;
  - cambio neto de caja (el importador lo traía con otra escala);
  - columna LTM del balance que repite el cierre anual (se lleva al último 10-Q).
Las demás diferencias se informan, pero no se escriben: pueden ser definiciones distintas y requieren revisión.

Sin --apply escribe el informe reference/auditoria_estados_2026-10-03/<T>_diagnostico.json y la lista de cambios
<T>_cambios.json (que aplica scripts/aplicar_cambios_celdas.py). Corte de información: 30-sep-2026.

Uso: PYTHONPATH=.:scripts python scripts/auditar_estados_sec.py TICKER ...
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
import time
from pathlib import Path

import audit_statements_sec as sec
from jmr_valuation.io.sheets_auth import get_gspread_client

_ROOT = Path(__file__).resolve().parents[1]
DATOS = _ROOT.parent / "Modelo-JMR-datos" / "valoraciones"
OUT = _ROOT / "reference" / "auditoria_estados_2026-10-03"
CORTE = "2026-09-30"
IS, BS, CF = "Income Statement", "Balance Sheet", "Cash Flow Statement"
MESES = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}

# fila -> (estado, etiquetas en orden de preferencia, tipo: flujo|saldo, unidad, se corrige)
FILAS = {
    "Total Revenues": (IS, ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax"], "flujo", "USD", False),
    "Operating Profit": (IS, ["OperatingIncomeLoss"], "flujo", "USD", False),
    "Income Before Provision for Income Taxes": (IS, [
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"], "flujo", "USD", False),
    "Provision for Income Taxes": (IS, ["IncomeTaxExpenseBenefit"], "flujo", "USD", False),
    "Consolidated Net Income": (IS, ["ProfitLoss", "NetIncomeLoss"], "flujo", "USD", True),
    "Net Income Attributable to Common Shareholders": (IS, ["NetIncomeLoss"], "flujo", "USD", False),
    "Basic EPS": (IS, ["EarningsPerShareBasic"], "flujo", "USD/shares", True),
    "Diluted EPS": (IS, ["EarningsPerShareDiluted"], "flujo", "USD/shares", True),
    "Cash and Cash Equivalents": (BS, ["CashAndCashEquivalentsAtCarryingValue"], "saldo", "USD", False),
    "Total Assets": (BS, ["Assets"], "saldo", "USD", True),
    "Total Liabilities": (BS, ["Liabilities"], "saldo", "USD", True),
    "Total Common Shareholders' Equity": (BS, ["StockholdersEquity"], "saldo", "USD", True),
    "Total Shareholders' Equity": (BS, ["StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest", "StockholdersEquity"], "saldo", "USD", True),
    "Total Liabilities and Shareholders' Equity": (BS, ["LiabilitiesAndStockholdersEquity"], "saldo", "USD", True),
    "Total Current Assets": (BS, ["AssetsCurrent"], "saldo", "USD", True),
    "Total Current Liabilities": (BS, ["LiabilitiesCurrent"], "saldo", "USD", True),
    "Net Property, Plant & Equipment": (BS, ["PropertyPlantAndEquipmentNet"], "saldo", "USD", True),
    "Cash from Operating Activities": (CF, ["NetCashProvidedByUsedInOperatingActivities"], "flujo", "USD", False),
    "Cash from Investing Activities": (CF, ["NetCashProvidedByUsedInInvestingActivities"], "flujo", "USD", False),
    "Cash from Financing Activities": (CF, ["NetCashProvidedByUsedInFinancingActivities"], "flujo", "USD", False),
    "Net Change in Cash": (CF, ["CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect",
                                "CashAndCashEquivalentsPeriodIncreaseDecrease",
                                "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseExcludingExchangeRateEffect"],
                           "flujo", "USD", True),
}
# filas del balance cuyo LTM se corrige solo si repite el cierre anual (no se tocan saldos de cierres fiscales)
BASURA_CAJA = (149, 1286.2, -661, 1020, 1825, -608, 443, 2896, 481, -2216, -14)
SOLO_LTM = {"Total Assets", "Total Liabilities", "Total Liabilities and Shareholders' Equity", "Total Current Assets",
            "Total Current Liabilities", "Net Property, Plant & Equipment", "Total Common Shareholders' Equity"}


def _d(s):
    return dt.date.fromisoformat(s)


def serie(f, tags, unit, tipo):
    """{fin: valor} anual (10-K, ~1 año) y, para saldos, también trimestral. Para cada fecha gana la primera etiqueta
    con datos y, dentro de ella, la presentación más reciente (cifras reexpresadas: ASC 606, cambios de perímetro)."""
    out, q = {}, {}
    for t in tags:
        mejor_a, mejor_q = {}, {}
        for x in f.get(t, {}).get("units", {}).get(unit, []) or []:
            if x.get("filed", "") > CORTE or x.get("form") not in ("10-K", "10-Q", "10-K/A", "10-Q/A"):
                continue
            if tipo == "saldo" and "start" not in x:
                k, dest = x["end"], mejor_q
            elif "start" in x:
                dias = (_d(x["end"]) - _d(x["start"])).days
                if 350 <= dias <= 380 and x["form"].startswith("10-K"):
                    k, dest = x["end"], mejor_a
                else:
                    k, dest = (x["start"], x["end"]), mejor_q
            else:
                continue
            if k not in dest or x["filed"] > dest[k][0]:
                dest[k] = (x["filed"], x["val"])
        for k, (_, v) in mejor_a.items():
            out.setdefault(k, v)
        for k, (_, v) in mejor_q.items():
            q.setdefault(k, v)
    return out, q


def cerca(d: dict, fecha: dt.date, tol=20):
    k = min(d, key=lambda e: abs((_d(e) - fecha).days), default=None)
    return (k, d[k]) if k and abs((_d(k) - fecha).days) <= tol else (None, None)


def fin_de_columna(lbl: str):
    m = re.match(r"([A-Z][a-z]{2}) '(\d{2})", str(lbl))
    if not m:
        return None
    y, mo = 2000 + int(m.group(2)), MESES[m.group(1)]
    nxt = dt.date(y + (mo == 12), mo % 12 + 1, 1)
    return nxt - dt.timedelta(days=1)


def ltm_flujo(anual: dict, q: dict, fy_end: str):
    """LTM = ejercicio + acumulado más reciente − acumulado comparable del año anterior."""
    if not fy_end or fy_end not in anual:
        return None, None
    acum = [(s, e, v) for (s, e), v in q.items() if e > fy_end and (_d(s) - _d(fy_end)).days in range(-5, 10)]
    if not acum:
        return anual[fy_end], fy_end
    s, e, v = max(acum, key=lambda a: a[1])
    dias = (_d(e) - _d(s)).days
    prev = next((pv for (ps, pe), pv in q.items() if abs((_d(pe) - _d(e)).days + 364) <= 10
                 and abs((_d(pe) - _d(ps)).days - dias) <= 10), None)
    return (anual[fy_end] + v - prev, e) if prev is not None else (None, None)


def main(argv: list[str]) -> int:
    gc = get_gspread_client()
    OUT.mkdir(parents=True, exist_ok=True)
    ciks = sec.cik_map()
    for tk in [a for a in argv if not a.startswith("--")]:
        f = sec.facts(tk, ciks[tk])
        sid = re.search(r"/d/([^/]+)", json.loads(next(DATOS.glob(f"{tk}-*.json")).read_text())["hojaGoogle"]).group(1)
        sh = gc.open_by_key(sid)
        grids = {t: v.get("values", []) for t, v in zip((IS, BS, CF), sh.values_batch_get(
            [f"'{t}'!A1:M70" for t in (IS, BS, CF)], params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"])}
        hdr = grids[IS][1] if len(grids[IS]) > 1 else []
        cols = [(j, h) for j, h in enumerate(hdr) if j >= 1 and (fin_de_columna(h) or h == "LTM")]
        # escala de la hoja: millones (se calibra con los ingresos del último cierre)
        diag, cambios = [], []
        for lab, (tab, tags, tipo, unit, corrige) in FILAS.items():
            rows = grids[tab]
            i = next((i for i, r in enumerate(rows) if r and r[0] == lab), None)
            if i is None:
                continue
            anual, q = serie(f, tags, unit, tipo)
            esc = 1 if unit == "USD/shares" else 1e6
            fy_last = max((e for e in anual), default=None) if tipo == "flujo" else max(
                (e for e in q if any(abs((_d(e) - fin_de_columna(h)).days) <= 20 for _, h in cols if h != "LTM")), default=None)
            for j, h in cols:
                hv = rows[i][j] if j < len(rows[i]) else None
                if not isinstance(hv, (int, float)):
                    continue
                if h == "LTM":
                    if tipo == "flujo":
                        sv, ref = ltm_flujo(anual, q, fy_last)
                    else:
                        ref = max(q) if q else None
                        sv = q.get(ref)
                else:
                    ref, sv = cerca(anual if tipo == "flujo" else q, fin_de_columna(h))
                if sv is None:
                    continue
                sv = sv / esc
                tol = 0.011 if unit == "USD/shares" else max(0.15, abs(sv) * 0.005)
                if abs(hv - sv) <= tol:
                    continue
                cell = f"{chr(65 + j)}{i + 1}"
                d = {"hoja": tab, "fila": lab, "celda": cell, "columna": h, "hoja_valor": hv, "sec": round(sv, 4),
                     "fecha_sec": ref, "etiquetas": tags}
                ok = False  # solo errores del importador demostrables
                if lab == "Net Change in Cash":  # serie de relleno de la plantilla (o vacío) en vez del dato
                    ok = hv == 0 or any(abs(hv - b) < 1e-6 for b in BASURA_CAJA)
                    d["nota"] = "valor de relleno de la plantilla" if ok else "diferencia de definición (tipo de cambio o caja restringida)"
                elif lab in SOLO_LTM or (lab == "Total Shareholders' Equity" and h == "LTM"):
                    prev = rows[i][j - 1] if j >= 1 and j - 1 < len(rows[i]) else None
                    ok = h == "LTM" and isinstance(prev, (int, float)) and abs(prev - hv) < 1e-9  # repite el cierre
                elif lab == "Basic EPS" and h != "LTM":
                    rd = next((r for r in rows if r and r[0] == "Diluted EPS"), None)
                    ok = (rd is not None and j < len(rd) and isinstance(rd[j], (int, float)) and abs(rd[j] - hv) < 1e-9
                          and hv > 0)  # con pérdidas el básico es igual al diluido por norma
                    d["nota"] = "básico copiado del diluido" if ok else "diferencia sin evidencia de copia"
                elif lab in ("Consolidated Net Income", "Total Shareholders' Equity"):
                    alt = ["NetIncomeLoss"] if lab == "Consolidated Net Income" else ["StockholdersEquity"]
                    a2, q2 = serie(f, alt, unit, tipo)
                    if h == "LTM":
                        av = ltm_flujo(a2, q2, fy_last)[0] if tipo == "flujo" else q2.get(ref)
                    else:
                        av = (a2 if tipo == "flujo" else q2).get(ref)
                    ok = av is not None and abs(hv - av / esc) <= tol  # la hoja tiene la cifra sin minoritarios
                    d["nota"] = "la hoja tiene la cifra sin minoritarios" if ok else "diferencia por reexpresión u otra definición"
                if unit == "USD/shares" and sv and not 0.8 <= hv / sv <= 1.25:
                    ok, d["nota"] = False, "posible ajuste por split o cambio de clase (la hoja ajustada no se toca)"
                d["se_corrige"] = ok
                diag.append(d)
                if ok:
                    cambios.append({"hoja": tab, "celda": cell, "antes": hv, "despues": round(sv, 2 if unit != "USD/shares" else 4),
                                    "motivo": f"{lab} {h}: SEC XBRL ({', '.join(tags[:1])}) al {ref}; antes {hv}."})
                    if lab == "Consolidated Net Income":  # el flujo parte de la utilidad consolidada; se compensa
                        rc = next((k for k, r in enumerate(grids[CF]) if r and r[0] == "Net Income"), None)
                        ro = next((k for k, r in enumerate(grids[CF]) if r and r[0] == "Other Adjustments"), None)
                        if rc is not None and ro is not None and j < len(grids[CF][rc]) and j < len(grids[CF][ro]):
                            cn, oa = grids[CF][rc][j], grids[CF][ro][j]
                            if isinstance(cn, (int, float)) and isinstance(oa, (int, float)) and abs(cn - hv) < 1e-9:
                                cambios.append({"hoja": CF, "celda": f"{chr(65 + j)}{rc + 1}", "antes": cn, "despues": round(sv, 2),
                                                "motivo": f"El flujo de caja parte de la utilidad consolidada ({h})."})
                                cambios.append({"hoja": CF, "celda": f"{chr(65 + j)}{ro + 1}", "antes": oa,
                                                "despues": round(oa - (sv - cn), 2),
                                                "motivo": "Compensa el cambio de la utilidad para que el flujo operativo siga igual al reportado."})
        desfase = any(d["fila"] == "Total Revenues" and d["columna"] == "LTM" for d in diag)
        if desfase:
            for d in diag:
                if d["columna"] == "LTM" and d["se_corrige"]:
                    d["se_corrige"], d["nota"] = False, "LTM de la hoja desfasado frente al último 10-Q: se revisa aparte"
            ltm_cells = {d["celda"] for d in diag if d["columna"] == "LTM"}
            col = {c[0] for c in ltm_cells}
            cambios = [c for c in cambios if c["celda"][0] not in col]
        (OUT / f"{tk}_diagnostico.json").write_text(json.dumps(diag, ensure_ascii=False, indent=1))
        (OUT / f"{tk}_cambios.json").write_text(json.dumps(cambios, ensure_ascii=False, indent=1))
        por_fila = {}
        for d in diag:
            por_fila.setdefault((d["fila"], d["se_corrige"]), []).append(d["columna"])
        print(f"{tk}: {len(diag)} diferencias, {len(cambios)} cambios propuestos" + (" · LTM DESFASADO" if desfase else ""), flush=True)
        for (fila, ok), cs in por_fila.items():
            print(f"   {'CORRIGE' if ok else 'informa'} {fila}: {', '.join(map(str, cs))}")
        time.sleep(6)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
