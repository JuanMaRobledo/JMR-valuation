"""Chequeo de crecimiento implícito (criterio Damodaran) para una valoración del Modelo JMR.

Dos preguntas, ambas con los supuestos del escenario Base de la hoja:

1. DCF inverso: ¿qué crecimiento anual de ingresos en los años 1-5 (luego converge a la
   perpetuidad, como el DCF) justifica el precio de hoy? Se compara con el crecimiento
   promedio de los años 1-5 del DCF. Se calcula con jmr_engine.js calibrado contra el DCF
   de la hoja (crecimientoImplicitoDCF).
2. Múltiplos: ¿qué crecimiento perpetuo después de FY+3 supone cada múltiplo Base (F19 de
   cada hoja)? Mismas fórmulas del múltiplo justificado, despejadas para g
   (crecimientoImplicitoMultiplo), con Ke, WACC de los años 4-10, ROE de FY+3, FCFF/EBITDA y
   FCFE/OCF de FY+3 (reference/multiplos_v3/<T>_anclas.json). Se compara con el g del
   múltiplo justificado (punto medio entre los años 4-10 y la perpetuidad).

Una diferencia de más de 2 pp es una alerta: el múltiplo (o el precio) cuenta otra historia
de crecimiento que el DCF, y hay que decidir cuál es la correcta.

Escribe:
- la pestaña 'Crecimiento implícito' de la hoja (A1:F14; el visor la lee de A5:F11),
- reference/multiplos_v3/<T>_crecimiento.json,
- el campo 'crecimientoImplicito' de la valoración guardada (Modelo-JMR-datos/valoraciones).

Uso:
    python scripts/implied_growth.py ADBE CELH ...    (o --todos)
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import statistics as st
import subprocess
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402
from valuation_report_v3 import ENGINE, MV, SHEETS, engine_inputs, es  # noqa: E402

DATOS = _ROOT.parent / "Modelo-JMR-datos" / "valoraciones"
TAB = "Crecimiento implícito"
UMBRAL = 0.02
ORDER = ("EV/EBITDA", "EV/FCFF", "P/E", "P/FCFE", "P/OCF")


def node(expr: str, **ctx) -> object:
    js = ("const fs=require('fs'),vm=require('vm');const c={};vm.createContext(c);"
          f"vm.runInContext(fs.readFileSync({json.dumps(str(ENGINE))},'utf8'),c);"
          + "".join(f"c.{k}={json.dumps(v)};" for k, v in ctx.items())
          + f"console.log(JSON.stringify(vm.runInContext({json.dumps(expr)},c)));")
    return json.loads(subprocess.check_output(["node", "-e", js]))


def pc(x):
    return "—" if not isinstance(x, (int, float)) else es(x * 100, 1) + "%"


def pp(x):
    return f"{'+' if x >= 0 else '−'}{es(abs(x) * 100, 1)} pp"


def lectura_precio(gi, gd):
    if gi is None:
        return "Ningún crecimiento entre −20% y 80% justifica el precio con estos márgenes."
    d = gi - gd
    if abs(d) <= UMBRAL:
        return "Coherente: el precio supone un crecimiento parecido al del DCF."
    if d > 0:
        return "El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador."
    return "El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto."


def lectura_multiplo(gi, gd):
    if gi is None:
        return "No se puede calcular (métrica o supuestos no aptos)."
    d = gi - gd
    if abs(d) <= UMBRAL:
        return "Coherente con el DCF."
    return ("Revisar: el múltiplo supone más crecimiento que el DCF." if d > 0
            else "Revisar: el múltiplo supone menos crecimiento que el DCF.")


def run(tk: str, client) -> dict:
    anc = json.loads((MV / f"{tk}_anclas.json").read_text())
    res = json.loads((MV / f"{tk}_decision_resultado.json").read_text())["resultado"]
    rec_path = Path(glob.glob(str(DATOS / f"{tk}-*.json"))[0])
    rec = json.loads(rec_path.read_text())
    sh = client.open_by_key(anc["sheet_id"])
    U = {"valueRenderOption": "UNFORMATTED_VALUE"}
    rng = ["'Input sheet'!A1:D70", "'Valuation output'!A1:M140", "'Financials Multiples'!A1:H120",
           "'Resumen de Valoración'!A1:U20", "'Descuento de múltiplos'!A1:K49"]
    rng += [f"{s}!F19" for s, _ in SHEETS.values()]
    vr = sh.values_batch_get(rng, params=U)["valueRanges"]
    grid = {r.split("!")[0].strip("'"): v.get("values", []) for r, v in zip(rng[:5], vr[:5])}
    f19 = {m: ((v.get("values") or [[None]])[0][0]) for m, v in zip(SHEETS, vr[5:])}

    def cell(sheet, addr):
        col, row = ord(addr[0]) - 65, int(addr[1:]) - 1
        g = grid[sheet]
        return g[row][col] if row < len(g) and col < len(g[row]) else None

    price = rec.get("precio")
    dcf_hoy = cell("Descuento de múltiplos", "D38")
    inp = engine_inputs(cell, grid["Financials Multiples"], price)
    g15 = [x for x in grid["Valuation output"][3][2:7] if isinstance(x, (int, float))]
    g_ref = st.mean(g15)
    g_imp = node("crecimientoImplicitoDCF(inp, m, g, d, p)", inp=inp, m=inp["marginBase"], g=g_ref, d=dcf_hoy, p=price)

    jb = anc["justificado"]["Base"]
    params = {"ke": jb["ke"], "wacc": jb["wacc_4_10"], "roe": jb["roe_fy3"],
              "fcffEbitda": jb["fcff_ebitda"], "fcfeOcf": jb["fcfe_ocf"]}
    g_dcf = jb["g"]
    metodos = []
    for m in ORDER:
        r = res.get(m, {})
        M = f19.get(m)
        if not r.get("aplica", True):
            metodos.append({"metodo": m, "multiplo": M, "gImplicito": None, "gDcf": g_dcf, "dif": None,
                            "aplica": False, "lectura": "No aplica: " + str(r.get("motivo", ""))[:120]})
            continue
        gi = node("crecimientoImplicitoMultiplo(m, M, p)", m=m, M=M, p=params) if isinstance(M, (int, float)) else None
        if g_dcf is not None and g_dcf >= min(params["ke"], params["wacc"]) - 0.01:
            # el DCF crece a más que la tasa después de FY+3: Gordon no representa esa historia
            metodos.append({"metodo": m, "multiplo": M, "gImplicito": gi, "gDcf": g_dcf, "dif": None, "aplica": True,
                            "lectura": "No comparable: el DCF supone después de FY+3 un crecimiento cercano o mayor "
                                       "al costo de capital (Gordon no aplica)."})
            continue
        metodos.append({"metodo": m, "multiplo": M, "gImplicito": gi, "gDcf": g_dcf,
                        "dif": gi - g_dcf if gi is not None else None, "aplica": True,
                        "lectura": lectura_multiplo(gi, g_dcf)})
    out = {
        "fecha": dt.date.today().isoformat(), "umbral": UMBRAL, "precio": price, "dcfHoy": dcf_hoy,
        "dcfInverso": {"gImplicito": g_imp, "gDcf": g_ref, "dif": g_imp - g_ref if g_imp is not None else None,
                       "lectura": lectura_precio(g_imp, g_ref)},
        "gDcf": {"anios4a10": jb.get("g_años_4_10"), "perpetuidad": jb.get("g_perpetuidad"), "puntoMedio": g_dcf},
        "parametros": params, "multiplos": metodos,
        "alertas": sum(1 for x in metodos if x["dif"] is not None and abs(x["dif"]) > UMBRAL),
    }

    # --- pestaña de la hoja ---
    try:
        ws = sh.worksheet(TAB)
        ws.clear()
    except Exception:  # noqa: BLE001
        ws = sh.add_worksheet(TAB, rows=20, cols=6)
    di = out["dcfInverso"]
    rows = [
        ["CRECIMIENTO IMPLÍCITO · chequeo de coherencia (criterio Damodaran)", "", "", "", "", ""],
        [f"Calculado el {out['fecha']} con scripts/implied_growth.py (escenario Base). Una diferencia de más de "
         f"{int(UMBRAL * 100)} pp indica que el precio o el múltiplo cuentan otra historia de crecimiento que el DCF.", "", "", "", "", ""],
        [""] * 6,
        ["Concepto", "Valor", "Crecimiento implícito", "Crecimiento del DCF", "Diferencia", "Lectura"],
        ["Precio de hoy (DCF inverso, crecimiento años 1-5)", price, di["gImplicito"] if di["gImplicito"] is not None else "—",
         g_ref, di["dif"] if di["dif"] is not None else "—", di["lectura"]],
        [""] * 6,
    ]
    for x in metodos:
        rows.append([f"{x['metodo']} Base FY+3 (crecimiento perpetuo después de FY+3)", x["multiplo"] if x["multiplo"] is not None else "—",
                     x["gImplicito"] if x["gImplicito"] is not None else "—", g_dcf,
                     x["dif"] if x["dif"] is not None else "—", x["lectura"]])
    rows += [[""] * 6,
             [f"Crecimiento del DCF para los múltiplos: punto medio entre el promedio de los años 4-10 "
              f"({es((jb.get('g_años_4_10') or 0) * 100, 1)}%) y la perpetuidad ({es((jb.get('g_perpetuidad') or 0) * 100, 1)}%). "
              f"Ke {pc(params['ke'])}, WACC años 4-10 {pc(params['wacc'])}, ROE FY+3 {pc(params['roe'])}"
              + (" (patrimonio contable negativo o sin dato: P/E no calculable)." if not params["roe"] else "."),
              "", "", "", "", ""]]
    ws.update(rows, "A1:F14", value_input_option="RAW")
    sid = ws.id
    fmt = lambda r0, r1, c0, c1, pattern, typ: {"repeatCell": {  # noqa: E731
        "range": {"sheetId": sid, "startRowIndex": r0, "endRowIndex": r1, "startColumnIndex": c0, "endColumnIndex": c1},
        "cell": {"userEnteredFormat": {"numberFormat": {"type": typ, "pattern": pattern}}}, "fields": "userEnteredFormat.numberFormat"}}
    sh.batch_update({"requests": [
        fmt(4, 5, 1, 2, "#,##0.00", "NUMBER"), fmt(6, 11, 1, 2, '0.0"x"', "NUMBER"), fmt(4, 11, 2, 5, "0.0%", "PERCENT"),
        {"repeatCell": {"range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": 1}, "cell": {"userEnteredFormat": {"textFormat": {"bold": True}}},
                        "fields": "userEnteredFormat.textFormat.bold"}},
        {"repeatCell": {"range": {"sheetId": sid, "startRowIndex": 3, "endRowIndex": 4}, "cell": {"userEnteredFormat": {"textFormat": {"bold": True}}},
                        "fields": "userEnteredFormat.textFormat.bold"}},
        {"updateDimensionProperties": {"range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": 0, "endIndex": 1},
                                       "properties": {"pixelSize": 380}, "fields": "pixelSize"}},
        {"updateDimensionProperties": {"range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": 5, "endIndex": 6},
                                       "properties": {"pixelSize": 520}, "fields": "pixelSize"}},
    ]})

    (MV / f"{tk}_crecimiento.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    rec["crecimientoImplicito"] = out
    rec_path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("tickers", nargs="*")
    ap.add_argument("--todos", action="store_true")
    a = ap.parse_args()
    tickers = a.tickers or sorted(p.name.split("_")[0] for p in MV.glob("*_decision_resultado.json"))
    client = get_gspread_client()
    for tk in tickers:
        for intento in range(3):
            try:
                o = run(tk, client)
                break
            except Exception as exc:  # noqa: BLE001
                if intento == 2:
                    print(f"{tk:5s} ERROR {str(exc)[:120]}")
                    o = None
                time.sleep(30)
        if o:
            di = o["dcfInverso"]
            gi = "—" if di["gImplicito"] is None else f"{di['gImplicito'] * 100:5.1f}%"
            ms = " ".join(f"{x['metodo']}:{'—' if x['gImplicito'] is None else format(x['gImplicito'] * 100, '.1f')}" for x in o["multiplos"])
            print(f"{tk:5s} precio {o['precio']:8.2f} DCF {o['dcfHoy']:8.2f} | g precio {gi} vs DCF {di['gDcf'] * 100:4.1f}% | "
                  f"g DCF mult {o['gDcf']['puntoMedio'] * 100:4.1f}% | {ms} | alertas {o['alertas']}", flush=True)
        time.sleep(4)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
