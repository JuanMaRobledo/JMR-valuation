"""Chequeo de crecimiento implícito (criterio Damodaran) para una valoración del Modelo JMR.

Dos preguntas, ambas con los supuestos del escenario Base de la hoja:

1. DCF inverso: ¿qué crecimiento anual de ingresos en los años 1-5 (luego converge a la
   perpetuidad, como el DCF) justifica el precio de hoy? Se compara con el crecimiento
   promedio de los años 1-5 del DCF. Se calcula con jmr_engine.js calibrado contra el DCF
   de la hoja (crecimientoImplicitoDCF).
2. Múltiplos (revisado el 30-sep-2026): ¿cuenta cada múltiplo Base (F19 de cada hoja) la misma historia
   que el DCF? Se calcula el MÚLTIPLO QUE IMPLICA EL DCF en FY+3: el que, con la misma métrica FY+3, deuda
   neta, acciones y dividendos de la hoja, da el DCF llevado a FY+3. Múltiplo y múltiplo del DCF pasan por
   la MISMA fórmula de crecimiento perpetuo (justificado despejado para g, con Ke, WACC de los años 4-10,
   ROE de FY+3, FCFF/EBITDA y FCFE/OCF de FY+3; crecimientoImplicitoMultiplo) y se comparan entre sí.
   Así el sesgo de la fórmula (supone el ROE de FY+3 para siempre, mientras el DCF lleva el retorno al
   costo de capital después del año 10) se cancela. Antes se comparaba contra el crecimiento del DCF
   (punto medio años 4-10 / perpetuidad), lo que marcaba como "menos crecimiento" a múltiplos que en
   valor coincidían con el DCF (empresas de ROE alto, p. ej. UBER). También se informa la diferencia de
   valor: precio FY+3 con el múltiplo (+ dividendos) frente al DCF llevado a FY+3.

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
UMBRAL_VALOR = 0.25  # diferencia de valor frente al DCF llevado a FY+3
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


def lectura_multiplo(gi, gd, dv):
    """Alerta si el crecimiento implícito difiere más de 2 pp del que implica el DCF o si, en valor, el precio
    FY+3 con el múltiplo se aparta más de 25% del DCF llevado a FY+3 (con múltiplos altos el crecimiento de
    Gordon se acerca al costo de capital en ambos casos y deja de distinguir diferencias grandes de valor)."""
    g_d = (gi - gd) if (gi is not None and gd is not None) else None
    g_ok = g_d is None or abs(g_d) <= UMBRAL
    v_ok = dv is None or abs(dv) <= UMBRAL_VALOR
    if g_d is None and dv is None:
        return "No se puede calcular (métrica o supuestos no aptos)."
    if g_ok and v_ok:
        return "Coherente con el DCF."
    vtxt = f" En valor, {es(abs(dv) * 100, 0)}% {'por encima' if dv > 0 else 'por debajo'} del DCF en FY+3." if dv is not None else ""
    if not g_ok:
        return ("Revisar: el múltiplo supone más crecimiento que el DCF." if g_d > 0
                else "Revisar: el múltiplo supone menos crecimiento que el DCF.") + vtxt
    return (f"Revisar: el múltiplo vale {es(abs(dv) * 100, 0)}% {'más' if dv > 0 else 'menos'} que el DCF en FY+3 "
            "(a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia).")


def run(tk: str, client, escribir: bool = True) -> dict:
    anc = json.loads((MV / f"{tk}_anclas.json").read_text())
    res = json.loads((MV / f"{tk}_decision_resultado.json").read_text())["resultado"]
    recs = glob.glob(str(DATOS / f"{tk}-*.json"))
    rec_path = Path(recs[0]) if recs else None  # hoja nueva sin valoración guardada (p. ej. CELHN)
    rec = json.loads(rec_path.read_text()) if rec_path else {}
    sh = client.open_by_key(anc["sheet_id"])
    U = {"valueRenderOption": "UNFORMATTED_VALUE"}
    rng = ["'Input sheet'!A1:D80", "'Valuation output'!A1:M140", "'Financials Multiples'!A1:H120",
           "'Resumen de Valoración'!A1:U20", "'Descuento de múltiplos'!A1:K49"]
    rng += [f"{s}!F19:H23" for s, _ in SHEETS.values()]
    # Limitación conocida: en financieras (PAGS) el DCF inverso usa el motor FCFF calibrado contra 'Valuation output'!B35;
    # crecimientoImplicitoDCF no admite el FCFE financiero.
    vr = sh.values_batch_get(rng, params=U)["valueRanges"]
    grid = {r.split("!")[0].strip("'"): v.get("values", []) for r, v in zip(rng[:5], vr[:5])}
    blk = {m: (v.get("values") or []) for m, v in zip(SHEETS, vr[5:])}

    def bget(m, r, c):  # r: 0=multiplo(19) 1=métrica(20) 2=precio(21) 3=dividendos(22) 4=total(23); c: 0=F 1=G 2=H
        rows = blk.get(m) or []
        x = rows[r][c] if r < len(rows) and c < len(rows[r]) else None
        return x if isinstance(x, (int, float)) else None
    f19 = {m: bget(m, 0, 0) for m in SHEETS}

    def cell(sheet, addr):
        col, row = ord(addr[0]) - 65, int(addr[1:]) - 1
        g = grid.get(sheet, [])
        return g[row][col] if row < len(g) and col < len(g[row]) else None

    price = rec.get("precio") or cell("Input sheet", "D1")
    inp = engine_inputs(cell, grid["Financials Multiples"], price)
    # DCF técnico de la hoja (VO B35): desde el 1-oct-2026 'Descuento de múltiplos'!D38 muestra la historia Base, que no
    # usa los mismos supuestos que el motor calibrado aquí. Financieras: D38 (FCFE financiero).
    dcf_hoy = cell("Descuento de múltiplos", "D38") if inp.get("dcfFinanciero") else cell("Valuation output", "B35")
    g15 = [x for x in grid["Valuation output"][3][2:7] if isinstance(x, (int, float))]
    g_ref = st.mean(g15)
    # Calibración (2-oct-2026): el motor no reproduce exactamente el DCF de la hoja cuando esta usa trayectorias por
    # región, fracción de año o costos restados aparte (NKE con Pace). Se busca el crecimiento que lleva el motor al
    # precio escalado por motor/hoja en la Base, así el DCF inverso responde a la hoja y no al sesgo del motor.
    # 6-oct-2026 (MCD): el motor se calibra con la TRAYECTORIA real de los años 1-5 de la hoja ('Valuation output'!C4:G4).
    # Antes usaba el crecimiento del año 2 (D4) como si fuera el de los años 2-5; con historias de crecimiento desigual
    # (refranquiciamiento de MCD: −0,9%, −4,7%, +1,6%, +4,6%, +4,6%) el factor de calibración salía muy lejos de 1 y el
    # DCF inverso encontraba otra raíz (−3,4% en lugar de ~2%).
    inp_cal = dict(inp, crecimientoAnios=g15) if len(g15) == 5 else inp
    eng0 = None if inp.get("dcfFinanciero") else node(
        "runDCF(inp, inp.growthBase, inp.marginBase, inp.growthY1Base, inp.marginY1Base)", inp=inp_cal)
    k = (eng0 / dcf_hoy) if (isinstance(eng0, (int, float)) and eng0 > 0 and dcf_hoy) else 1.0
    g_imp = node("crecimientoImplicitoDCF(inp, m, g, d, p)", inp=inp, m=inp["marginBase"], g=g_ref, d=dcf_hoy, p=price * k)

    jb = anc["justificado"]["Base"]
    params = {"ke": jb["ke"], "wacc": jb["wacc_4_10"], "roe": jb["roe_fy3"],
              "fcffEbitda": jb["fcff_ebitda"], "fcfeOcf": jb["fcfe_ocf"]}
    g_dcf = jb["g"]
    # DCF llevado a FY+3 (Base) y el puente precio <- múltiplo de las pestañas de cada método:
    # EV: precio = (M × métrica − deuda neta) / acciones FY+3; patrimonio: precio = M × métrica / acciones FY+3.
    dcf_fy3 = None
    for row in grid["Resumen de Valoración"]:
        if row and str(row[0]).startswith(("DCF Damodaran", "DCF capitalizado")) and len(row) > 3 and isinstance(row[3], (int, float)):
            dcf_fy3 = row[3]
            break
    nd = sum((cell("Input sheet", a) or 0) * sg for a, sg in (("B16", 1), ("B19", -1), ("B20", -1), ("B21", 1)))
    fm = grid["Financials Multiples"]
    sh_e = fm[69][4] if len(fm) > 69 and len(fm[69]) > 4 else None
    sh_g = fm[69][6] if len(fm) > 69 and len(fm[69]) > 6 else None
    metodos = []
    for m in ORDER:
        r = res.get(m, {})
        M = f19.get(m)
        if not r.get("aplica", True):
            metodos.append({"metodo": m, "multiplo": M, "multiploDcf": None, "gImplicito": None, "gDcf": None, "dif": None,
                            "difValor": None, "aplica": False, "lectura": "No aplica: " + str(r.get("motivo", ""))[:120]})
            continue
        ev = SHEETS[m][1]
        metric, divs, total = bget(m, 1, 2), bget(m, 3, 2) or 0, bget(m, 4, 2)
        shares = (max(x for x in (sh_e, sh_g) if isinstance(x, (int, float))) if ev else sh_g) if (sh_e or sh_g) else None
        m_dcf = None
        if dcf_fy3 and metric and metric > 0 and shares:
            m_dcf = (((dcf_fy3 - divs) * shares + (nd if ev else 0)) / metric)
            if m_dcf <= 0:
                m_dcf = None
        gi = node("crecimientoImplicitoMultiplo(m, M, p)", m=m, M=M, p=params) if isinstance(M, (int, float)) else None
        gd = node("crecimientoImplicitoMultiplo(m, M, p)", m=m, M=m_dcf, p=params) if m_dcf else None
        dv = (total / dcf_fy3 - 1) if (total is not None and dcf_fy3) else None
        metodos.append({"metodo": m, "multiplo": M, "multiploDcf": m_dcf, "gImplicito": gi, "gDcf": gd,
                        "dif": (gi - gd) if (gi is not None and gd is not None) else None, "difValor": dv, "aplica": True,
                        "lectura": lectura_multiplo(gi, gd, dv)})
    out = {
        "fecha": dt.date.today().isoformat(), "umbral": UMBRAL, "precio": price, "dcfHoy": dcf_hoy,
        "dcfInverso": {"gImplicito": g_imp, "gDcf": g_ref, "dif": g_imp - g_ref if g_imp is not None else None,
                       "lectura": lectura_precio(g_imp, g_ref)},
        "gDcf": {"anios4a10": jb.get("g_años_4_10"), "perpetuidad": jb.get("g_perpetuidad"), "puntoMedio": g_dcf},
        "parametros": params, "multiplos": metodos,
        "dcfFy3": dcf_fy3, "metodo": "v2: múltiplo frente al múltiplo que implica el DCF en FY+3, ambos por la misma fórmula",
        "alertas": sum(1 for x in metodos if x["lectura"].startswith("Revisar")),
    }

    if not escribir:  # --sin-escribir: solo calcula (p. ej. para medir el efecto de un cambio en toda la cartera)
        return out

    # --- pestaña de la hoja ---
    try:
        ws = sh.worksheet(TAB)
        ws.clear()
    except Exception:  # noqa: BLE001
        ws = sh.add_worksheet(TAB, rows=20, cols=8)
    if ws.col_count < 8:
        ws.add_cols(8 - ws.col_count)
    di = out["dcfInverso"]
    E = [""] * 8
    na = lambda v: v if v is not None else "—"  # noqa: E731
    rows = [
        ["CRECIMIENTO IMPLÍCITO · chequeo de coherencia (criterio Damodaran)"] + [""] * 7,
        [f"Calculado el {out['fecha']} con scripts/implied_growth.py (escenario Base). Alerta: más de {int(UMBRAL * 100)} pp de "
         f"diferencia en crecimiento, o más de {int(UMBRAL_VALOR * 100)}% en valor frente al DCF llevado a FY+3."] + [""] * 7,
        E,
        ["Concepto", "Valor", "Crecimiento implícito", "Crecimiento del DCF", "Diferencia", "Lectura", "Múltiplo que implica el DCF", "Diferencia de valor"],
        ["Precio de hoy (DCF inverso, crecimiento años 1-5)", price, na(di["gImplicito"]), g_ref, na(di["dif"]), di["lectura"], "", ""],
        E,
    ]
    for x in metodos:
        rows.append([f"{x['metodo']} Base FY+3 (crecimiento perpetuo después de FY+3)", na(x["multiplo"]), na(x["gImplicito"]),
                     na(x["gDcf"]), na(x["dif"]), x["lectura"], na(x.get("multiploDcf")), na(x.get("difValor"))])
    rows += [E,
             [f"Múltiplos: cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 "
              f"({es(dcf_fy3) if dcf_fy3 else '—'} por acción, con la misma métrica, deuda neta, acciones y dividendos de la hoja); "
              f"los dos pasan por la misma fórmula de crecimiento perpetuo (Ke {pc(params['ke'])}, WACC años 4-10 {pc(params['wacc'])}, "
              f"ROE FY+3 {pc(params['roe'])}, FCFF/EBITDA y FCFE/OCF de FY+3), así que el sesgo de la fórmula se cancela. "
              f"Diferencia de valor = precio FY+3 con el múltiplo (+ dividendos) ÷ DCF llevado a FY+3 − 1."
              + (" Patrimonio contable negativo o sin dato: P/E no calculable." if not params["roe"] else "")] + [""] * 7]
    ws.update(rows, "A1:H14", value_input_option="RAW")
    sid = ws.id
    fmt = lambda r0, r1, c0, c1, pattern, typ: {"repeatCell": {  # noqa: E731
        "range": {"sheetId": sid, "startRowIndex": r0, "endRowIndex": r1, "startColumnIndex": c0, "endColumnIndex": c1},
        "cell": {"userEnteredFormat": {"numberFormat": {"type": typ, "pattern": pattern}}}, "fields": "userEnteredFormat.numberFormat"}}
    sh.batch_update({"requests": [
        fmt(4, 5, 1, 2, "#,##0.00", "NUMBER"), fmt(6, 11, 1, 2, '0.0"x"', "NUMBER"), fmt(4, 11, 2, 5, "0.0%", "PERCENT"),
        fmt(6, 11, 6, 7, '0.0"x"', "NUMBER"), fmt(6, 11, 7, 8, "0.0%", "PERCENT"),
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
    if rec_path:
        rec["crecimientoImplicito"] = out
        rec_path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("tickers", nargs="*")
    ap.add_argument("--todos", action="store_true")
    ap.add_argument("--sin-escribir", action="store_true", help="calcula e imprime sin tocar hoja, JSON ni app")
    a = ap.parse_args()
    tickers = a.tickers or sorted(p.name.split("_")[0] for p in MV.glob("*_decision_resultado.json"))
    client = get_gspread_client()
    for tk in tickers:
        for intento in range(3):
            try:
                o = run(tk, client, escribir=not a.sin_escribir)
                break
            except Exception as exc:  # noqa: BLE001
                if intento == 2:
                    print(f"{tk:5s} ERROR {str(exc)[:120]}")
                    o = None
                time.sleep(30)
        if o:
            di = o["dcfInverso"]
            gi = "—" if di["gImplicito"] is None else f"{di['gImplicito'] * 100:5.1f}%"
            ms = " ".join(f"{x['metodo']}:{'—' if x['multiplo'] is None else format(x['multiplo'], '.1f')}x/"
                          f"{'—' if not x.get('multiploDcf') else format(x['multiploDcf'], '.1f')}x" for x in o["multiplos"])
            print(f"{tk:5s} precio {o['precio']:8.2f} DCF {o['dcfHoy']:8.2f} | g precio {gi} vs DCF {di['gDcf'] * 100:4.1f}% | "
                  f"múltiplo/DCF {ms} | alertas {o['alertas']}", flush=True)
        time.sleep(4)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
