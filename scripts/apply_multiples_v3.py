"""Aplica el paso 6 del prompt de valoracion v3 a una hoja del Modelo JMR.

Entrada:
  --anclas    JSON de multiples_anchors.py (historia, peers y justificado).
  --decision  JSON con el juicio del analista para esa empresa:
      {
        "ticker": "ADBE",
        "etapa_desde": "Dec '23",          # primer cierre de la etapa actual (null = toda la historia)
        "etapa_motivo": "...",
        "peers_excluir": {"P/E": ["NOW"], "*": []},   # por metodo o "*" para todos
        "historia_excluir": {"P/E": ["Dec '25", "LTM"]},  # cierres no representativos (partidas no recurrentes)
        "historia_motivo": "...",
        "peers_motivo": "...",
        "ajuste_peers": 0.05,               # ajuste sobre la mediana de peers (+5%)
        "ajuste_motivo": "...",
        "lambda": 0.25,                     # cuanto acercar el Base al justificado (0 = nada, 1 = todo)
        "lambda_motivo": "...",
        "no_aplica": {"P/FCFE": "motivo"},  # metodos no aplicables (no se escriben)
        "notas": {"P/E": "..."}             # texto extra por metodo
      }

Regla (prompt v3, 6.3):
  A = mediana de los cierres de la etapa actual (+ LTM) o mediana 5A depurada.
  B = mediana de peers (sin excluidos) x (1 + ajuste).
  C = justificado del escenario.
  Base = (1 - lambda) x promedio(A, B) + lambda x C_base; debe quedar en [min(A,B,C); max(A,B,C)].
  Conservador = Base x promedio(P25/mediana de A, P25/mediana de peers, C_cons/C_base)  (tope 0,97).
  Optimista   = Base x promedio(P75/mediana de A, P75/mediana de peers, C_opt/C_base)   (minimo 1,03),
                sin superar el maximo historico depurado.

Con --apply escribe J8/J19/J30 (respaldo previo en reference/multiplos_v3/<ticker>_respaldo.json),
'Supuestos de los Múltiplos' A3/A12 y un bloque "Origen de los múltiplos (prompt v3)" al final de
'Tesis de Inversión y Supuestos'. Sin --apply solo muestra la propuesta.
"""
from __future__ import annotations

import argparse
import json
import statistics as st
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))

from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

OUT = _ROOT / "reference" / "multiplos_v3"
PEER_KEY = {"EV/EBITDA": "ev_ebitda", "EV/FCFF": "ev_fcf", "P/E": "pe", "P/FCFE": "p_fcf", "P/OCF": "p_ocf"}
TV_LABEL = {"EV/EBITDA": "EV/EBITDA", "EV/FCFF": "EV/FCF", "P/E": "P/E", "P/FCFE": "P/FCF", "P/OCF": "P/OCF"}


def pct(values, q):
    v = sorted(values)
    k = (len(v) - 1) * q
    f, c = int(k), min(int(k) + 1, len(v) - 1)
    return v[f] + (v[c] - v[f]) * (k - f)


def es(v, nd=2):
    """Número en formato es-CO (1.234,56)."""
    return f"{v:,.{nd}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def fx(v):
    return f"{v:.1f}x".replace(".", ",") if isinstance(v, (int, float)) else "—"


def decide(anc: dict, dec: dict) -> dict:
    out = {}
    adj = 1 + dec.get("ajuste_peers", 0.0)
    lam = dec.get("lambda", 0.0)
    for m, d in anc["metodos"].items():
        if m in dec.get("no_aplica", {}):
            out[m] = {"aplica": False, "motivo": dec["no_aplica"][m]}
            continue
        hist = d["historia"]
        serie = hist["serie"]
        labels = list(serie)
        excl = {e[0] for e in hist["excluidos"]} | set(dec.get("historia_excluir", {}).get(m, []))
        start = dec.get("etapa_desde")
        idx = labels.index(start) if start in labels else 0
        stage = [(lab, v) for lab, v in list(serie.items())[idx:] if isinstance(v, (int, float)) and v > 0.5 and lab not in excl]
        a_vals = [v for _, v in stage]
        if not a_vals:
            a = a_p25 = a_p75 = a_max = None
            a_desc = "sin historia representativa (" + (dec.get("historia_motivo") or "todos los cierres excluidos") + ")"
        elif start:
            a = st.median(a_vals)
            a_desc = f"mediana {', '.join(lab for lab, _ in stage)} (etapa actual) = {fx(a)}"
        else:
            a = st.median(a_vals[-6:])
            a_desc = f"mediana de los últimos 5 cierres + LTM depurados = {fx(a)}"
        if a_vals:
            a_p25, a_p75 = pct(a_vals, .25), pct(a_vals, .75)
        a_max = hist.get("max")  # tope del Optimista: máximo de toda la historia depurada
        skip = set(dec.get("peers_excluir", {}).get(m, [])) | set(dec.get("peers_excluir", {}).get("*", []))
        pv = [(p["ticker"], p.get(PEER_KEY[m])) for p in anc["peers"]]
        pv = [(t, v) for t, v in pv if isinstance(v, (int, float)) and 0 < v < 200 and t not in skip]
        if len(pv) < 3:
            raise SystemExit(f"{m}: menos de 3 peers válidos ({pv})")
        vals = [v for _, v in pv]
        b_med = st.median(vals)
        b = b_med * adj
        b_p25, b_p75 = pct(vals, .25) * adj, pct(vals, .75) * adj
        cj = d["justificado"]
        c_base, c_cons, c_opt = cj["Base"], cj["Conservador"], cj["Optimista"]
        market = (a + b) / 2 if a is not None else b
        base = (1 - lam) * market + lam * c_base if c_base else market
        anchors_ok = [x for x in (a, b, c_base) if x is not None]
        lo, hi = min(anchors_ok), max(anchors_ok)
        in_range = lo - 1e-9 <= base <= hi + 1e-9
        # Conservador y Optimista: el Base escalado por la dispersión de cada ancla
        # (P25/mediana y P75/mediana de A y de B; justificado Cons/Base y Opt/Base de C).
        down = [x for x in ((a_p25 / a) if a and a_p25 else None, pct(vals, .25) / b_med,
                            (c_cons / c_base) if c_cons and c_base else None) if x]
        up = [x for x in ((a_p75 / a) if a and a_p75 else None, pct(vals, .75) / b_med,
                          (c_opt / c_base) if c_opt and c_base else None) if x]
        f_down, f_up = min(st.mean(down), 0.97), max(st.mean(up), 1.03)
        cons, opt = base * f_down, base * f_up
        opt_cap = None
        if a_max and opt > a_max:
            opt_cap, opt = opt, max(a_max, base * 1.03)
        out[m] = {
            "aplica": True, "hoja": d["hoja"],
            "A": round(a, 2) if a is not None else None, "A_desc": a_desc,
            "A_p25": round(a_p25, 2) if a_p25 else None, "A_p75": round(a_p75, 2) if a_p75 else None, "A_max": a_max,
            "A_excluidos": hist["excluidos"],
            "B_mediana": round(b_med, 2), "B_ajustada": round(b, 2), "B_n": len(vals),
            "B_peers": ", ".join(f"{t} {fx(v)}" for t, v in pv), "B_excluidos": sorted(skip),
            "C": {k: round(v, 2) if v else None for k, v in cj.items()},
            "mercado": round(market, 2), "lambda": lam,
            "conservador": round(cons, 2), "base": round(base, 2), "optimista": round(opt, 2),
            "factor_cons": round(f_down, 3), "factor_opt": round(f_up, 3), "opt_tope_historico": opt_cap,
            "base_en_rango": in_range, "rango": [round(lo, 2), round(hi, 2)],
            "antes": d["actual_J"], "nota": dec.get("notas", {}).get(m, ""),
        }
    return out


def origin_rows(tk: str, anc: dict, dec: dict, res: dict) -> list[list[str]]:
    rows = [[f"ORIGEN DE LOS MÚLTIPLOS (prompt de valoración v3, {anc['fecha']})"],
            ["Método", "Aplica", "A · historia", "B · peers (ajustada)", "C · justificado (Cons/Base/Opt)",
             "Conservador", "Base", "Optimista", "Regla y excepciones", "Celdas"]]
    for m, r in res.items():
        if not r["aplica"]:
            rows.append([m, "No", "", "", "", "", "", "", r["motivo"], ""])
            continue
        c = r["C"]
        rows.append([
            m, "Sí", r["A_desc"],
            f"mediana {fx(r['B_mediana'])} (n={r['B_n']}: {r['B_peers']}) × {es(1 + dec.get('ajuste_peers', 0))} = {fx(r['B_ajustada'])}",
            f"{fx(c['Conservador'])} / {fx(c['Base'])} / {fx(c['Optimista'])}",
            r["conservador"], r["base"], r["optimista"],
            (f"Base = {es(1 - r['lambda'])} × {'promedio(A,B)' if r['A'] is not None else 'B'} {fx(r['mercado'])} + {es(r['lambda'])} × C. "
             f"Cons = Base × {es(r['factor_cons'])} y Opt = Base × {es(r['factor_opt'])} (dispersión P25/P75 de historia y peers y justificado por escenario). "
             f"Rango de anclas {fx(r['rango'][0])}-{fx(r['rango'][1])}: {'dentro' if r['base_en_rango'] else 'FUERA, ver nota'}. {r['nota']}"),
            f"{r['hoja']}!J8/J19/J30"])
    rows.append(["Criterios: " + " ".join(x for x in (dec.get("etapa_motivo", ""), dec.get("historia_motivo", ""), dec.get("peers_motivo", ""),
                                                        dec.get("ajuste_motivo", ""), dec.get("lambda_motivo", "")) if x)])
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--anclas", required=True)
    ap.add_argument("--decision", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    anc = json.loads(Path(a.anclas).read_text())
    dec = json.loads(Path(a.decision).read_text())
    tk = dec["ticker"]
    res = decide(anc, dec)
    for m, r in res.items():
        if r["aplica"]:
            print(f"{m:10s} A {fx(r['A'])} B {fx(r['B_ajustada'])} C {fx(r['C']['Base'])} -> "
                  f"Cons {fx(r['conservador'])} Base {fx(r['base'])} Opt {fx(r['optimista'])} "
                  f"(antes {r['antes']}) rango {'OK' if r['base_en_rango'] else 'FUERA'}")
        else:
            print(f"{m:10s} no aplica: {r['motivo']}")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / f"{tk}_decision_resultado.json").write_text(json.dumps({"decision": dec, "resultado": res}, ensure_ascii=False, indent=1))
    if not a.apply:
        return
    sh = get_gspread_client().open_by_key(anc["sheet_id"])
    backup_path = OUT / f"{tk}_respaldo.json"
    if not backup_path.exists():
        rng = [f"{r['hoja']}!J8:J30" for r in res.values() if r["aplica"]] + ["'Supuestos de los Múltiplos'!A3", "'Supuestos de los Múltiplos'!A12"]
        vr = sh.values_batch_get(rng, params={"valueRenderOption": "FORMULA"})["valueRanges"]
        backup_path.write_text(json.dumps({r: v.get("values", []) for r, v in zip(rng, vr)}, ensure_ascii=False, indent=1))
    data = []
    for r in res.values():
        if r["aplica"]:
            for cell, key in (("J8", "conservador"), ("J19", "base"), ("J30", "optimista")):
                data.append({"range": f"{r['hoja']}!{cell}", "values": [[r[key]]]})
    applied = [m for m, r in res.items() if r["aplica"]]
    synth = (f"Múltiplos de salida fijados el {anc['fecha']} con el prompt de valoración v3 (J8/J19/J30 explícitos; los rótulos "
             f"«x0,9» y «mín. positivo 4 cierres» de la fila 5 ya no describen la regla). Cada Base = promedio de A (historia "
             f"{'de la etapa actual desde ' + dec['etapa_desde'] if dec.get('etapa_desde') else 'depurada 5 años'}) y B (mediana de "
             f"peers de hoy × {es(1 + dec.get('ajuste_peers', 0))}), acercado un {es(dec.get('lambda', 0) * 100, 0)}% al múltiplo justificado C. "
             f"Base: " + "; ".join(f"{m} {fx(res[m]['base'])}" for m in applied) + ". Detalle en «Tesis de Inversión y Supuestos».")
    data.append({"range": "'Supuestos de los Múltiplos'!A3", "values": [[synth]]})
    sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": data})
    time.sleep(3)
    # chequeo de independencia
    dm = sh.values_get("'Descuento de múltiplos'!C38:E40", params={"valueRenderOption": "UNFORMATTED_VALUE"})["values"]
    dcf, mult, pond = dm[0], dm[1], dm[2]
    gap = mult[1] / dcf[1] - 1
    eval_txt = (f"Chequeo de independencia ({anc['fecha']}): múltiplos consolidados hoy (Base) {es(mult[1])} frente a DCF hoy "
                f"{es(dcf[1])} ({'+' if gap >= 0 else '−'}{es(abs(gap) * 100, 0)}%). {dec.get('evaluacion', '')}")
    sh.values_update("'Supuestos de los Múltiplos'!A12", params={"valueInputOption": "USER_ENTERED"}, body={"values": [[eval_txt]]})
    # bloque de origen en la hoja de tesis
    ws = sh.worksheet("Tesis de Inversión y Supuestos")
    col_a = ws.col_values(1)
    marker = next((i + 1 for i, v in enumerate(col_a) if v.startswith("ORIGEN DE LOS MÚLTIPLOS (prompt de valoración v3")), None)
    start = marker or len(col_a) + 3
    rows = origin_rows(tk, anc, dec, res)
    need = start + len(rows) + 2
    if ws.row_count < need:
        ws.add_rows(need - ws.row_count)
    if ws.col_count < 10:
        ws.add_cols(10 - ws.col_count)
    if marker:
        ws.batch_clear([f"A{start}:J{start + len(rows) + 5}"])
    ws.update(values=[r + [""] * (10 - len(r)) for r in rows], range_name=f"A{start}:J{start + len(rows) - 1}",
              value_input_option="USER_ENTERED")
    q = {"sheetId": ws.id}
    sh.batch_update({"requests": [
        {"repeatCell": {"range": {**q, "startRowIndex": start - 1, "endRowIndex": start, "startColumnIndex": 0, "endColumnIndex": 10},
                        "cell": {"userEnteredFormat": {"textFormat": {"bold": True, "fontSize": 11}}}, "fields": "userEnteredFormat.textFormat"}},
        {"repeatCell": {"range": {**q, "startRowIndex": start, "endRowIndex": start + 1, "startColumnIndex": 0, "endColumnIndex": 10},
                        "cell": {"userEnteredFormat": {"textFormat": {"bold": True}, "backgroundColor": {"red": .86, "green": .89, "blue": .95},
                                                       "wrapStrategy": "WRAP"}}, "fields": "userEnteredFormat(textFormat,backgroundColor,wrapStrategy)"}},
        {"repeatCell": {"range": {**q, "startRowIndex": start + 1, "endRowIndex": start + len(rows), "startColumnIndex": 0, "endColumnIndex": 10},
                        "cell": {"userEnteredFormat": {"wrapStrategy": "WRAP", "verticalAlignment": "TOP"}}, "fields": "userEnteredFormat(wrapStrategy,verticalAlignment)"}},
    ]})
    result = {"dcf_hoy": dcf, "multiplos_hoy": mult, "ponderado_hoy": pond, "brecha_base": gap, "fila_origen": start}
    (OUT / f"{tk}_decision_resultado.json").write_text(json.dumps({"decision": dec, "resultado": res, "hoja": result}, ensure_ascii=False, indent=1))
    print("aplicado:", json.dumps(result, default=str))


if __name__ == "__main__":
    main()
