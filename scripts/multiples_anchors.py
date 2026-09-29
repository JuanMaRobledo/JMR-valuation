"""Anclas para elegir los multiplos de salida con el prompt de valoracion v3.

Para una hoja del Modelo JMR calcula, por metodo (EV/EBITDA, EV/FCFF, P/E,
P/FCFE, P/OCF) y escenario, las tres anclas del paso 6.2 del prompt:

  A. Historia de la empresa ('Trailing Valuation', 10 cierres fiscales + LTM),
     depurada de atipicos: metrica negativa o ~0, multiplos > 2,5x o < 0,4x la
     mediana. Un valor bajo se conserva si el ultimo cierre y el LTM estan ambos
     en ese nivel ("regimen actual"). Reporta mediana 5A y 10A, P25, P75, min,
     max, LTM y la lista de excluidos.
  B. Comparables con datos de hoy (yfinance): P/E trailing, EV/EBITDA, P/FCF y
     EV/FCF con FCF = flujo operativo - capex de los ultimos 4 trimestres (la
     misma definicion que 'Trailing Valuation'), P/OCF. Mediana, P25, P75 y n.
  C. Multiplo justificado por fundamentales (Damodaran) con los SUPUESTOS de
     cada escenario en FY+3: g = punto medio entre el crecimiento promedio de
     los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC-g)
     con el WACC promedio de los años 4-10; P/FCFE = (1+g)/(Ke-g);
     P/E = (1 - g/ROE)(1+g)/(Ke-g) con ROE = utilidad FY+3 / patrimonio en
     libros LTM; EV/EBITDA = EV/FCFF x FCFF/EBITDA de FY+3; P/OCF = P/FCFE x
     FCFE/OCF de FY+3. No usa el valor del DCF.

No escribe en la hoja: produce un JSON con las anclas para que el analista
decida los multiplos (ver apply_multiples.py).

Uso:
    python scripts/multiples_anchors.py --sheet-id ID --peers ADSK INTU CRM NOW --out anclas.json
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import statistics as st
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))

from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

METHODS = {  # metodo: (hoja, fila en Trailing Valuation, etiqueta)
    "EV/EBITDA": ("EVEBITDA", 21, "EV/EBITDA"),
    "EV/FCFF": ("EVFCFF", 24, "EV/FCF"),
    "P/E": ("PE", 13, "P/E"),
    "P/FCFE": ("PFCFE", 16, "P/FCF"),
    "P/OCF": ("POCF", 15, "P/OCF"),
}
# filas de 'Financials Multiples' por escenario (primera fila de datos = Revenues)
FM_START = {"Conservador": 4, "Base": 43, "Optimista": 83}
FM_OFF = {"ebitda": 14, "net_income": 11, "fcff": 20, "ocf": 22, "fcfe": 25}
VO_GROWTH_ROW = {"Conservador": 55, "Base": 4, "Optimista": 106}
VO_WACC_ROW = {"Conservador": 65, "Base": 14, "Optimista": 116}


def _pct(values, q):
    v = sorted(values)
    if not v:
        return None
    k = (len(v) - 1) * q
    f, c = int(k), min(int(k) + 1, len(v) - 1)
    return v[f] + (v[c] - v[f]) * (k - f)


def history_anchor(labels, values):
    pts = [(lab, v) for lab, v in zip(labels, values)]
    num = [(lab, v) for lab, v in pts if isinstance(v, (int, float))]
    positive = [(lab, v) for lab, v in num if v > 0.5]
    excluded = [(lab, v, "métrica negativa o ~0") for lab, v in num if v <= 0.5]
    if not positive:
        return {"n": 0, "excluidos": excluded}
    med = st.median(v for _, v in positive)
    fy = [p for p in positive if p[0] != "LTM"]
    last_fy, ltm = (fy[-1][1] if fy else None), next((v for lab, v in positive if lab == "LTM"), None)
    regime_low = last_fy is not None and ltm is not None and last_fy < 0.6 * med and ltm < 0.6 * med
    kept = []
    for lab, v in positive:
        if v > 2.5 * med:
            excluded.append((lab, v, f"> 2,5x la mediana ({med:.1f}x)"))
        elif v < 0.4 * med and not regime_low:
            excluded.append((lab, v, f"< 0,4x la mediana ({med:.1f}x), caída puntual"))
        else:
            kept.append((lab, v))
    fy_kept = [v for lab, v in kept if lab != "LTM"]
    vals = [v for _, v in kept]
    return {
        "serie": {lab: (round(v, 2) if isinstance(v, (int, float)) else v) for lab, v in pts},
        "mediana_5a": round(st.median(fy_kept[-5:]), 2) if fy_kept else None,
        "mediana_10a": round(st.median(fy_kept), 2) if fy_kept else None,
        "p25": round(_pct(vals, 0.25), 2), "p75": round(_pct(vals, 0.75), 2),
        "min": round(min(vals), 2), "max": round(max(vals), 2),
        "ultimo_cierre": round(last_fy, 2) if last_fy else None, "ltm": round(ltm, 2) if ltm else None,
        "regimen_bajo_actual": regime_low,
        "excluidos": [(lab, round(v, 2), why) for lab, v, why in excluded],
    }


def peer_multiples(ticker):
    import yfinance as yf
    t = yf.Ticker(ticker)
    info = t.info
    mcap, ev = info.get("marketCap"), info.get("enterpriseValue")
    out = {"ticker": ticker, "nombre": info.get("shortName"), "precio": info.get("currentPrice"),
           "pe": info.get("trailingPE"), "ev_ebitda": info.get("enterpriseToEbitda"),
           "crec_ingresos": info.get("revenueGrowth"), "margen_operativo": info.get("operatingMargins"),
           "roe": info.get("returnOnEquity")}
    try:
        q = t.quarterly_cashflow
        rows = {str(i).lower(): i for i in q.index}
        ocf_row = next(rows[k] for k in rows if k in ("operating cash flow", "cash flow from continuing operating activities"))
        capex_row = next(rows[k] for k in rows if k in ("capital expenditure", "capital expenditures"))
        ocf = float(q.loc[ocf_row].iloc[:4].sum())
        capex = float(q.loc[capex_row].iloc[:4].sum())
        fcf = ocf + capex  # capex viene negativo
        out.update(p_ocf=mcap / ocf if mcap and ocf > 0 else None, p_fcf=mcap / fcf if mcap and fcf > 0 else None,
                   ev_fcf=ev / fcf if ev and fcf > 0 else None, ocf_ttm=ocf, fcf_ttm=fcf)
    except Exception as exc:  # noqa: BLE001
        out.update(p_ocf=None, p_fcf=None, ev_fcf=None, error_cashflow=str(exc)[:80])
    return out


PEER_KEY = {"EV/EBITDA": "ev_ebitda", "EV/FCFF": "ev_fcf", "P/E": "pe", "P/FCFE": "p_fcf", "P/OCF": "p_ocf"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet-id", required=True)
    ap.add_argument("--peers", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    c = get_gspread_client()
    sh = c.open_by_key(a.sheet_id)
    rng = ["'Trailing Valuation'!A2:L24", "'Financials Multiples'!A1:H120", "'Valuation output'!A1:M140",
           "'Cost of capital worksheet'!B63", "'Balance Sheet'!A35:L35", "'Input sheet'!A1:D1",
           "'Resumen de Valoración'!G3", "'Descuento de múltiplos'!B5"]
    vr = sh.values_batch_get(rng, params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
    tv, fm, vo = (v.get("values", []) for v in vr[:3])
    ke = vr[3]["values"][0][0]
    equity = [x for x in vr[4]["values"][0][1:] if isinstance(x, (int, float))][-1]
    name = vr[5]["values"][0][0]
    labels = [str(x).strip() for x in tv[0][1:]]
    rows_tv = {r[0]: r[1:] for r in tv if r}

    def fm_val(scen, key, col=6):  # col 6 = G = FY+3
        r = FM_START[scen] + FM_OFF[key] - 1
        return fm[r][col] if r < len(fm) and col < len(fm[r]) else None

    def vo_row(r):
        return vo[r - 1] if r - 1 < len(vo) else []

    anchors = {"empresa": name, "sheet_id": a.sheet_id, "fecha": dt.date.today().isoformat(), "ke": ke,
               "categoria": vr[6]["values"][0][0], "metodos": {}, "justificado": {}}
    # C: multiplo justificado por escenario
    for scen in FM_START:
        g_row = vo_row(VO_GROWTH_ROW[scen])
        w_row = vo_row(VO_WACC_ROW[scen])
        g410 = [x for x in g_row[5:12] if isinstance(x, (int, float))]
        g_term = g_row[12] if len(g_row) > 12 and isinstance(g_row[12], (int, float)) else None
        g = (st.mean(g410) + g_term) / 2 if g410 and g_term is not None else None
        wacc = st.mean([x for x in w_row[5:12] if isinstance(x, (int, float))]) if w_row else None
        ni, ebitda, fcff, ocf, fcfe = (fm_val(scen, k) for k in ("net_income", "ebitda", "fcff", "ocf", "fcfe"))
        roe = ni / equity if equity and equity > 0 and ni else None
        just = {"g": g, "g_años_4_10": st.mean(g410) if g410 else None, "g_perpetuidad": g_term, "wacc_4_10": wacc,
                "ke": ke, "roe_fy3": roe, "fcff_ebitda": fcff / ebitda if ebitda else None,
                "fcfe_ocf": fcfe / ocf if ocf else None}
        ok = g is not None and wacc and ke > g + 0.01 and wacc > g + 0.01
        evfcff = (1 + g) / (wacc - g) if ok else None
        pfcfe = (1 + g) / (ke - g) if ok else None
        payout = max(0.0, min(1.0, 1 - g / roe)) if roe and roe > 0 and g is not None else None
        just["multiplos"] = {
            "EV/FCFF": evfcff, "P/FCFE": pfcfe,
            "P/E": payout * (1 + g) / (ke - g) if ok and payout is not None else None,
            "EV/EBITDA": evfcff * just["fcff_ebitda"] if evfcff and just["fcff_ebitda"] else None,
            "P/OCF": pfcfe * just["fcfe_ocf"] if pfcfe and just["fcfe_ocf"] else None,
        }
        anchors["justificado"][scen] = just
    # B: peers
    peers = []
    for p in a.peers:
        try:
            peers.append(peer_multiples(p))
        except Exception as exc:  # noqa: BLE001
            peers.append({"ticker": p, "error": str(exc)[:80]})
    anchors["peers"] = peers
    for m, (sheet, tv_row, tv_label) in METHODS.items():
        hist = history_anchor(labels, rows_tv.get(tv_label, [])[:len(labels)])
        vals = [p.get(PEER_KEY[m]) for p in peers if isinstance(p.get(PEER_KEY[m]), (int, float)) and 0 < p[PEER_KEY[m]] < 200]
        cur = sh.values_get(f"{sheet}!F8:J30", params={"valueRenderOption": "UNFORMATTED_VALUE"}).get("values", [])
        anchors["metodos"][m] = {
            "hoja": sheet, "historia": hist,
            "peers": {"n": len(vals), "mediana": round(st.median(vals), 2) if vals else None,
                      "p25": round(_pct(vals, .25), 2) if vals else None, "p75": round(_pct(vals, .75), 2) if vals else None},
            "justificado": {s: (round(anchors["justificado"][s]["multiplos"][m], 2)
                                if anchors["justificado"][s]["multiplos"][m] else None) for s in FM_START},
            "actual_J": {"J8": cur[0][4] if cur and len(cur[0]) > 4 else None,
                         "J19": cur[11][4] if len(cur) > 11 and len(cur[11]) > 4 else None,
                         "J30": cur[22][4] if len(cur) > 22 and len(cur[22]) > 4 else None},
        }
    Path(a.out).write_text(json.dumps(anchors, ensure_ascii=False, indent=1, default=str))
    for m, d in anchors["metodos"].items():
        h = d["historia"]
        print(f"{m:10s} A: med5 {h.get('mediana_5a')} med10 {h.get('mediana_10a')} P25 {h.get('p25')} P75 {h.get('p75')} "
              f"LTM {h.get('ltm')} excl {len(h.get('excluidos', []))} | B: {d['peers']} | C: {d['justificado']} | hoy {d['actual_J']}")


if __name__ == "__main__":
    main()
