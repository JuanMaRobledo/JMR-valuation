#!/usr/bin/env python
"""Reconstruye la columna LTM (L) de los tres estados de una hoja con el último 10-Q (3-oct-2026).

Para cada fila con valor en el último cierre fiscal (K) se busca la etiqueta XBRL (o su negativo) que reproduce K;
con esa misma definición:
  - flujos (Income Statement, Cash Flow Statement): LTM = ejercicio + acumulado del año − acumulado comparable;
  - saldos (Balance Sheet): el saldo del último 10-Q.
Las filas que no se pueden calibrar y son residuales («Other ...») se recalculan como cuadre para que los totales
sigan sumando; márgenes, tasas y EBITDA se recalculan con su fórmula; las filas a cero quedan en cero. Lo que no se
puede calibrar ni derivar se informa y no se toca. Corte de información: 30-sep-2026.

Escribe <T>_ltm_cambios.json en reference/auditoria_estados_2026-10-03/ para aplicar con aplicar_cambios_celdas.py.

Uso: PYTHONPATH=.:scripts python scripts/rehacer_ltm.py TICKER
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path

import audit_statements_sec as sec
from jmr_valuation.io.sheets_auth import get_gspread_client

_ROOT = Path(__file__).resolve().parents[1]
DATOS = _ROOT.parent / "Modelo-JMR-datos" / "valoraciones"
OUT = _ROOT / "reference" / "auditoria_estados_2026-10-03"
CORTE = "2026-09-30"
IS, BS, CF = "Income Statement", "Balance Sheet", "Cash Flow Statement"
PREFERIDAS = {
    "Total Common Shareholders' Equity": ("StockholdersEquity",),
    "Total Shareholders' Equity": ("StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest", "StockholdersEquity"),
    "Unearned Revenue": ("ContractWithCustomerLiabilityCurrent", "DeferredRevenueCurrent"),
    "Total Liabilities": ("Liabilities",),
    "Net Income": ("ProfitLoss", "NetIncomeLoss"),
}


def _d(s):
    return dt.date.fromisoformat(s)


def indice(f, unit="USD"):
    """Por etiqueta: anual {fin: val}, acumulados {(ini, fin): val} y saldos {fin: val}, presentación más reciente."""
    idx = {}
    for t, body in f.items():
        xs = [x for x in body.get("units", {}).get(unit, []) or []
              if x.get("filed", "") <= CORTE and x.get("form") in ("10-K", "10-Q", "10-K/A", "10-Q/A")]
        if not xs:
            continue
        a, q, s = {}, {}, {}
        for x in sorted(xs, key=lambda x: x["filed"]):
            if "start" in x:
                dias = (_d(x["end"]) - _d(x["start"])).days
                if 350 <= dias <= 380 and x["form"].startswith("10-K"):
                    a[x["end"]] = x["val"]
                else:
                    q[(x["start"], x["end"])] = x["val"]
            else:
                s[x["end"]] = x["val"]
        idx[t] = (a, q, s)
    return idx


def ltm(a, q, fy, qend):
    acum = [(s, e, v) for (s, e), v in q.items() if e == qend and abs((_d(s) - _d(fy)).days) <= 10]
    if fy not in a or not acum:
        return None
    s, e, v = acum[0]
    dias = (_d(e) - _d(s)).days
    prev = next((pv for (ps, pe), pv in q.items() if abs((_d(pe) - _d(e)).days + 364) <= 10
                 and abs((_d(pe) - _d(ps)).days - dias) <= 10), None)
    return None if prev is None else a[fy] + v - prev


def main(argv):
    tk = argv[0]
    f = sec.facts(tk, sec.cik_map()[tk])
    idx = indice(f)
    eps = indice(f, "USD/shares")
    shs = indice(f, "shares")
    rev = next(t for t in ("Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax") if t in idx and idx[t][0])
    fy = max(idx[rev][0])
    qend = max(e for (s, e) in idx[rev][1] if abs((_d(s) - _d(fy)).days) <= 10)
    qbal = max(e for t in ("Assets",) for e in idx[t][2] if e <= qend)
    print(f"{tk}: ejercicio {fy}, último trimestre {qend}")
    sid = re.search(r"/d/([^/]+)", json.loads(next(DATOS.glob(f"{tk}-*.json")).read_text())["hojaGoogle"]).group(1)
    sh = get_gspread_client().open_by_key(sid)
    g = {t: v.get("values", []) for t, v in zip((IS, BS, CF), sh.values_batch_get(
        [f"'{t}'!A1:L60" for t in (IS, BS, CF)], params={"valueRenderOption": "FORMULA"})["valueRanges"])}
    nuevo, fuente, informe = {}, {}, []

    lab_actual = [""]

    def calib(K, tipo, ix):
        cands = []
        for t, (a, q, s) in ix.items():
            v = (a.get(fy) if tipo == "flujo" else s.get(fy))
            if v is None:
                continue
            for sg in ((1, -1) if tipo == "flujo" else (1,)):
                esc = 1 if ix is eps else 1e6
                if abs(sg * v / esc - K) <= max(0.06, abs(K) * 0.0002):
                    cands.append((t, sg))
        pref = PREFERIDAS.get(lab_actual[0], ())
        cands.sort(key=lambda c: (c[0] not in pref, pref.index(c[0]) if c[0] in pref else 0))
        for t, sg in cands:
            a, q, s = ix[t]
            esc = 1e6 if ix is not eps else 1
            val = ltm(a, q, fy, qend) if tipo == "flujo" else s.get(qbal)
            if val is not None:
                return sg * val / esc, t
        return None, (cands[0][0] if cands else None)

    for tab, tipo in ((IS, "flujo"), (BS, "saldo"), (CF, "flujo")):
        for i, r in enumerate(g[tab]):
            if i < 2 or not r or len(r) < 12:
                continue
            K, L = r[10], r[11]
            if not isinstance(K, (int, float)) or (isinstance(L, str) and L.startswith("=")):
                continue
            lab = r[0]
            lab_actual[0] = lab
            if K == 0:
                if not (isinstance(L, (int, float)) and L != 0):  # un LTM distinto de cero con K = 0 es un ajuste previo
                    nuevo[(tab, i)] = 0.0
                continue
            ix = eps if "EPS" in lab else (shs if "Shares" in lab else idx)
            v, t = calib(K, tipo, ix)
            if v is not None:
                nuevo[(tab, i)], fuente[(tab, i)] = v, t
            else:
                informe.append((tab, lab, K, L, t))
    row = lambda tab, lab: next((i for i, r in enumerate(g[tab]) if r and r[0] == lab and len(r) > 11), None)  # noqa: E731
    sin = {(t, l) for t, l, *_ in informe}

    def todas(tab, labs):  # los componentes de un cuadre deben estar todos calibrados
        return not any((tab, x) in sin for x in labs)
    V = lambda tab, lab: nuevo.get((tab, row(tab, lab)))  # noqa: E731

    def setd(tab, lab, val, why):
        i = row(tab, lab)
        r = g[tab][i] if i is not None else []
        if i is not None and val is not None and len(r) > 11 and not (isinstance(r[11], str) and r[11].startswith("=")):
            nuevo[(tab, i)], fuente[(tab, i)] = val, why
            informe[:] = [x for x in informe if not (x[0] == tab and x[1] == lab)]

    # derivadas del estado de resultados
    r3, r5 = V(IS, "Total Revenues"), V(IS, "Cost of Sales")
    if r3 is not None and r5 is not None:
        gp = r3 - r5
        setd(IS, "Gross Profit", gp, "ingresos − costo de ventas")
        setd(IS, "Gross Profit Margin", gp / r3, "margen bruto")
        op, da = V(IS, "Operating Profit"), V(IS, "Depreciation & Amortization Expenses")
        if op is not None and da is not None:
            otros = gp - (V(IS, "Selling, General & Administrative Expenses") or 0) - da - (V(IS, "Research & Development Expenses") or 0) - op
            setd(IS, "Other Operating Expenses", otros, "cuadre: bruto − SG&A − D&A − I+D − operativo")
            setd(IS, "Operating Margin", op / r3, "margen operativo")
            setd(IS, "EBITDA", op + da, "operativo + D&A")
            pre = V(IS, "Income Before Provision for Income Taxes")
            if pre is not None:
                ii, ie = V(IS, "Interest and Investment Income") or 0, V(IS, "Interest Expense") or 0
                setd(IS, "Non-Operating Income", pre - op - ii - ie, "cuadre: antes de impuestos − operativo − intereses")
                setd(IS, "Total Non-Operating Income", pre - op, "antes de impuestos − operativo")
                tx = V(IS, "Provision for Income Taxes")
                if tx is not None:
                    setd(IS, "Effective Tax Rate", tx / pre, "impuesto / utilidad antes de impuestos")
    k3 = g[IS][row(IS, "Total Revenues")][10]
    if r3 is not None:
        setd(IS, "Total Revenues %Chg", r3 / k3 - 1, "LTM frente al último ejercicio")
    # balance: residuales
    tca, ta = V(BS, "Total Current Assets"), V(BS, "Total Assets")
    if tca is not None:
        setd(BS, "Other Current Assets", tca - (V(BS, "Total Cash and Cash Equivalents") or 0) - (V(BS, "Total Trade Receivables") or 0),
             "cuadre del activo corriente")
    if ta is not None and tca is not None:
        setd(BS, "Other Long-Term Assets", ta - tca - sum(V(BS, x) or 0 for x in ("Net Property, Plant & Equipment", "Net Intangible Assets",
                                                                                "Goodwill", "Long-Term Investments")), "cuadre del activo")
    tcl, tl = V(BS, "Total Current Liabilities"), V(BS, "Total Liabilities")
    tltl = V(BS, "Total Long-Term Liabilities")
    if tl is None and tcl is not None and tltl is not None:
        tl = tcl + tltl
        setd(BS, "Total Liabilities", tl, "pasivo corriente + no corriente")
    if tcl is not None:
        setd(BS, "Other Current Liabilities", tcl - sum(V(BS, x) or 0 for x in ("Accounts Payable", "Short-Term Debt", "Unearned Revenue")),
             "cuadre del pasivo corriente")
    if tl is not None and tcl is not None:
        if tltl is None:
            setd(BS, "Total Long-Term Liabilities", tl - tcl, "pasivo − pasivo corriente")
        setd(BS, "Other Long-Term Liabilities", tl - tcl - sum(V(BS, x) or 0 for x in ("Long-Term Debt", "Leases")), "cuadre del pasivo")
    # flujo: residuales
    ocf = V(CF, "Cash from Operating Activities")
    if ocf is not None:
        setd(CF, "Other Adjustments", ocf - sum(V(CF, x) or 0 for x in ("Net Income", "Depreciation & Amortization", "Share-Based Compensation Expense",
                                                                         "Changes in Trade Receivables", "Changes in Accounts Payable",
                                                                         "Changes in Income Taxes Payable", "Changes in Unearned Revenue")),
             "cuadre del flujo operativo")
        capex = V(CF, "Capital Expenditure")
        if capex is not None:
            setd(CF, "Free Cash Flow", ocf + capex, "flujo operativo − capex")
            op_, tr_ = V(IS, "Operating Profit"), V(IS, "Effective Tax Rate")
            if op_ is not None and tr_ is not None:
                setd(CF, "NOPAT", op_ * (1 - tr_), "EBIT × (1 − tasa efectiva)")
            cfi = V(CF, "Cash from Investing Activities")
            if cfi is not None:
                setd(CF, "Other Investing Activities", cfi - capex - sum(V(CF, x) or 0 for x in ("Purchases of Investments", "Proceeds from Sale of Investments")),
                     "cuadre del flujo de inversión")
    cff = V(CF, "Cash from Financing Activities")
    fin = ("Net Issuance / (Repayments) of Long-Term Debt", "Net Issuance / (Repurchases) of Common Shares", "Common Share Dividends Paid")
    if cff is not None and todas(CF, fin):
        setd(CF, "Other Financing Activities", cff - sum(V(CF, x) or 0 for x in ("Net Issuance / (Repayments) of Long-Term Debt",
                                                                                "Net Issuance / (Repurchases) of Common Shares", "Common Share Dividends Paid")),
             "cuadre del flujo de financiación")
    cambios = []
    for (tab, i), v in sorted(nuevo.items()):
        old = g[tab][i][11]
        if isinstance(old, (int, float)) and abs(old - v) <= max(0.005, abs(v) * 1e-4):
            continue
        nd = 4 if abs(v) < 5 else 2
        cambios.append({"hoja": tab, "celda": f"L{i + 1}", "antes": old, "despues": round(v, nd),
                        "motivo": f"LTM al {qend} (10-Q, SEC XBRL): {fuente.get((tab, i), 'sin cambio respecto de cero')}."})
    (OUT / f"{tk}_ltm_cambios.json").write_text(json.dumps(cambios, ensure_ascii=False, indent=1))
    for c in cambios:
        print(f"  {c['hoja'][:4]} {c['celda']:4s} {str(c['antes']):>10} -> {c['despues']:>10}  {c['motivo'][28:110]}")
    for tab, lab, K, L, t in informe:
        print(f"  SIN CALIBRAR {tab[:4]} {lab} (K {K}, L {L})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
