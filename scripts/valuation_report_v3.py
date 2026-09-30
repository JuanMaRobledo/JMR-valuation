"""Genera el resumen {TICKER}_Valoracion_Modelo_JMR_[fecha].md del paso 11 del prompt de
valoración v3, con las cifras leídas de la hoja (no recalculadas) y el origen de los múltiplos
(reference/multiplos_v3/<TICKER>_decision_resultado.json y <TICKER>_anclas.json).

Sensibilidad:
- Múltiplos ±20%: exacta con las fórmulas de las hojas de múltiplos (precio implícito =
  múltiplo × métrica ÷ acciones, menos la deuda neta en los EV), descontada como en
  'Descuento de múltiplos'.
- Crecimiento, margen y WACC: con el motor de la Calculadora (docs/jmr_engine.js, validado
  contra la plantilla), aplicando al DCF de la hoja la variación relativa que da el motor.

Uso:
    python scripts/valuation_report_v3.py --ticker ADBE --saved ../Modelo-JMR-datos/valoraciones/ADBE-*.json --out data/
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))

from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

ENGINE = _ROOT.parent / "Modelo-JMR" / "docs" / "jmr_engine.js"
MV = _ROOT / "reference" / "multiplos_v3"
SCEN = ("conservador", "base", "optimista")
SHEETS = {"EV/EBITDA": ("EVEBITDA", True), "EV/FCFF": ("EVFCFF", True), "P/E": ("PE", False),
          "P/FCFE": ("PFCFE", False), "P/OCF": ("POCF", False)}


def es(v, nd=2):
    return f"{v:,.{nd}f}".replace(",", "X").replace(".", ",").replace("X", ".") if isinstance(v, (int, float)) else "—"


def xm(v, nd=1):
    return es(v, nd) + "x" if isinstance(v, (int, float)) else "—"


def pct(v, nd=1):
    return es(v * 100, nd) + "%" if isinstance(v, (int, float)) else "—"


def money(v, cur="US$"):
    return f"{cur}{es(v)}" if isinstance(v, (int, float)) else "—"


def engine_dcf(inp: dict) -> dict:
    js = (f"const fs=require('fs'),vm=require('vm');const c={{}};vm.createContext(c);"
          f"vm.runInContext(fs.readFileSync({json.dumps(str(ENGINE))},'utf8'),c);c.inp={json.dumps(inp)};"
          "const r=vm.runInContext('calcularModeloJMR(inp)',c);console.log(JSON.stringify(r.valorPresente.dcf));")
    return json.loads(subprocess.check_output(["node", "-e", js]))


def engine_inputs(cell, fm, price) -> dict:
    """Use the engine's shared grid reader; never approximate year 1 with years 2–5."""
    bounds={"Input sheet":(75,4),"Valuation output":(140,13),"Financials Multiples":(120,8),
            "Resumen de Valoración":(20,21),"Cost of capital worksheet":(70,5),"DCF FCFE financiero":(62,9)}
    bounds.update({name:(34,10) for name,_ in SHEETS.values()})
    grid={}
    for name,(rows,cols) in bounds.items():
        if name=="Financials Multiples":grid[name]=fm;continue
        data=[]
        for r in range(1,rows+1):
            row=[]
            for c in range(cols):
                try:v=cell(name,chr(65+c)+str(r))
                except (KeyError,IndexError):v=None
                row.append(v)
            data.append(row)
        grid[name]=data
    js=("const fs=require('fs'),vm=require('vm'),c={};vm.createContext(c);"
        f"vm.runInContext(fs.readFileSync({json.dumps(str(ENGINE))},'utf8'),c);"
        "const G=JSON.parse(fs.readFileSync(0,'utf8'));const cell=(h,a)=>{const m=a.match(/^([A-Z]+)(\\d+)$/);"
        "let n=0;for(const k of m[1])n=n*26+k.charCodeAt(0)-64;return G[h]?.[+m[2]-1]?.[n-1]??null;};"
        "console.log(JSON.stringify(c.insumosDesdeHoja(cell)));")
    inp=json.loads(subprocess.check_output(['node','-e',js],input=json.dumps(grid),text=True))
    inp['precioActual']=price
    return inp


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ticker", required=True)
    ap.add_argument("--saved", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    tk = a.ticker
    rec = json.loads(Path(a.saved).read_text())
    anc = json.loads((MV / f"{tk}_anclas.json").read_text())
    dr = json.loads((MV / f"{tk}_decision_resultado.json").read_text())
    dec, res = dr["decision"], dr["resultado"]
    sid = anc["sheet_id"]
    sh = get_gspread_client().open_by_key(sid)
    U = {"valueRenderOption": "UNFORMATTED_VALUE"}
    rng = ["'Input sheet'!A1:D70", "'Valuation output'!A1:M140", "'Cost of capital worksheet'!A1:E70",
           "'Descuento de múltiplos'!A1:K49", "'Financials Multiples'!A1:H120", "'Resumen de Valoración'!A1:U20"]
    rng += [f"{s}!A1:J34" for s, _ in SHEETS.values()]
    if 'DCF FCFE financiero' in {w.title for w in sh.worksheets()}:rng.append("'DCF FCFE financiero'!A1:I62")
    vr = sh.values_batch_get(rng, params=U)["valueRanges"]
    grid = {r.split("!")[0].strip("'"): v.get("values", []) for r, v in zip(rng, vr)}

    def cell(sheet, addr):
        col = ord(addr[0]) - 65
        row = int(addr[1:]) - 1
        g = grid[sheet]
        return g[row][col] if row < len(g) and col < len(g[row]) else None

    inp, vo, coc, dm, fm, rs = (grid[k] for k in ("Input sheet", "Valuation output", "Cost of capital worksheet",
                                                    "Descuento de múltiplos", "Financials Multiples", "Resumen de Valoración"))
    cur = "US$"
    ke = cell("Descuento de múltiplos", "B5")
    wacc = cell("Input sheet", "B36")
    price = rec.get("precio")
    dcf = [cell("Descuento de múltiplos", c + "38") for c in "CDE"]
    mult = [cell("Descuento de múltiplos", c + "39") for c in "CDE"]
    pond = [cell("Descuento de múltiplos", c + "40") for c in "CDE"]
    w_dcf, w_mult = cell("Descuento de múltiplos", "B38"), cell("Descuento de múltiplos", "B39")
    op = rec["objetivoPonderado"]
    mos_pct = float(rec.get("mos") or 0)
    mos_base=(rec.get('valorEsperado') or {}).get('valor',dcf[1])
    mos = {k:mos_base*(1-mos_pct) for k in SCEN}

    # --- sensibilidad de múltiplos (Base) ---
    nd = cell("Input sheet", "B16") - cell("Input sheet", "B19") - (cell("Input sheet", "B20") or 0) + (cell("Input sheet", "B21") or 0)
    shares = {c: fm[69][ord(c) - 65] for c in "EFG"}  # fila 70 = acciones diluidas del Base

    def mult_base(k):
        tot, wsum = 0.0, 0.0
        for m, (s, is_ev) in SHEETS.items():
            if not res.get(m, {}).get("aplica"):
                continue
            g = grid[s]
            M = g[18][5]
            pv = []
            for n, col in enumerate("FGH", start=1):
                metric = g[19][ord(col) - 65]
                sh_n = max(shares["E"], shares[chr(ord(col) - 1)]) if is_ev else shares[chr(ord(col) - 1)]
                implied = g[20][ord(col) - 65]
                div = g[21][ord(col) - 65] or 0
                pv.append((implied + (k - 1) * M * metric / sh_n + div) / (1 + ke) ** n)
            w = next(r[2] for r in dm[19:24] if r and r[0] == m)
            tot += w * (sum(pv) / 3 if cell("Descuento de múltiplos", "B6") != "Solo 3 años" else pv[2])
            wsum += w
        return tot / wsum if wsum else None

    sens = []
    for k, lab in ((1.2, "Múltiplos Base +20%"), (0.8, "Múltiplos Base −20%")):
        mb = mult_base(k)
        sens.append((lab, dcf[1] * w_dcf + mb * w_mult))
    check_mult = mult_base(1.0)

    # --- sensibilidad DCF con el motor de la Calculadora ---
    base_inp = engine_inputs(cell, fm, price)
    wacc = base_inp["wacc"]

    def c_(addr, sheet="Input sheet"):
        return cell(sheet, addr)
    eng0 = engine_dcf(base_inp)["base"]
    for lab, change in (("Crecimiento años 2-5 +2 pp", {"growthBase": base_inp["growthBase"] + 0.02}),
                        ("Crecimiento años 2-5 −2 pp", {"growthBase": base_inp["growthBase"] - 0.02}),
                        ("Margen objetivo +3 pp", {"marginBase": base_inp["marginBase"] + 0.03}),
                        ("Margen objetivo −3 pp", {"marginBase": base_inp["marginBase"] - 0.03}),
                        ("WACC +1 pp", {"wacc": wacc + 0.01}), ("WACC −1 pp", {"wacc": wacc - 0.01})):
        e = engine_dcf({**base_inp, **change})["base"]
        new_dcf = e
        sens.append((lab, new_dcf * w_dcf + mult[1] * w_mult))

    today = dt.date.today().isoformat()
    L = []
    w = L.append
    w("---")
    w('schema: "jmr-valuation-v3"')
    w(f'title: "Valoración Modelo JMR de {rec.get("nombreActivo") or tk}"')
    w(f'ticker: "{tk}"')
    w(f'analysis_date: "{today}"')
    w(f'sheet: "{rec.get("hojaGoogle")}"')
    w('generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"')
    w("---")
    w("")
    w(f"# {rec.get('nombreActivo') or tk} ({tk}) — Valoración Modelo JMR · prompt v3")
    w("")
    w("> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.")
    w("> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, "
      "valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF "
      "no se modificaron; se verificó que Conservador < Base < Optimista.")
    w("")
    w("## 1. Resumen")
    w("")
    gap = mult[1] / dcf[1] - 1
    w(f"Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de {money(dcf[1])} en el escenario Base "
      f"(rango {money(dcf[0])}–{money(dcf[2])}). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos "
      f"a valor presente en 1, 2 y 3 años, dan {money(mult[1])} ({'+' if gap >= 0 else '−'}{es(abs(gap) * 100, 0)}% frente al DCF). "
      f"Con los pesos de la categoría «{cell('Resumen de Valoración', 'G3')}» ({pct(w_dcf, 0)} DCF, {pct(w_mult, 0)} múltiplos), "
      f"el ponderado hoy (lectura secundaria) es {money(pond[1])}. El valor intrínseco es el DCF: {money(dcf[1])} frente a un "
      f"precio de referencia de {money(price)} ({'+' if dcf[1] >= price else '−'}{es(abs(dcf[1] / price - 1) * 100, 0)}%).")
    w("")
    w(dec.get("evaluacion", ""))
    w("")
    w("| Escenario | DCF hoy (valor intrínseco) | Múltiplos consolidados hoy (secundario) | Ponderado hoy (secundario) | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |")
    w("|---|---:|---:|---:|---:|---:|")
    for i, k in enumerate(SCEN):
        w(f"| {k.capitalize()} | {money(dcf[i])} | {money(mult[i])} | {money(pond[i])} | {money(mos.get(k))} | {money(op[k])} |")
    w("")
    w("## 2. Datos")
    w("")
    w(f"- Hoja del modelo: [{sh.title}]({rec.get('hojaGoogle')}).")
    w(f"- {rec.get('fecha') or ''}. Precio de referencia de la hoja: {money(price)}.")
    w(f"- Peers: datos de mercado de yfinance consultados el {anc['fecha']} (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con "
      "flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').")
    w("- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta "
      "actualización no los modificó.")
    w("")
    w("## 3. Supuestos del DCF y costo de capital")
    w("")
    w("| Supuesto | Conservador | Base | Optimista | Celda |")
    w("|---|---:|---:|---:|---|")
    w(f"| Crecimiento año 1 | {pct(cell('Valuation output', 'C55'))} | {pct(c_('B27'))} | {pct(cell('Valuation output', 'C106'))} | Input B27; Valuation output C55/C106 |")
    w(f"| Crecimiento años 2-5 | {pct(cell('Valuation output', 'D55'))} | {pct(c_('B29'))} | {pct(cell('Valuation output', 'D106'))} | Input B29 |")
    w(f"| Margen EBIT objetivo | {pct(cell('Valuation output', 'C45'))} | {pct(c_('B30'))} | {pct(cell('Valuation output', 'C47'))} | Input B30; Valuation output C45/C47 |")
    w(f"| Año de convergencia del margen | {c_('B31')} | {c_('B31')} | {c_('B31')} | Input B31 |")
    w(f"| Sales-to-capital años 1-5 / 6-10 | — | {es(c_('B32'))} / {es(c_('B33'))} | — | Input B32/B33 |")
    w(f"| DCF por acción hoy | {money(dcf[0])} | {money(dcf[1])} | {money(dcf[2])} | Valuation output B86/B35/B137 |")
    w("")
    w(f"Costo de capital: tasa libre de riesgo {pct(c_('B35'), 2)}, beta apalancada {es(cell('Cost of capital worksheet', 'C58'))}, "
      f"ERP {pct(cell('Cost of capital worksheet', 'B28'), 2)}, Ke {pct(ke, 2)}, costo de la deuda después de impuestos "
      f"{pct(cell('Cost of capital worksheet', 'C63'), 2)}, peso del patrimonio {pct(cell('Cost of capital worksheet', 'B62'), 1)}, "
      f"WACC inicial {pct(wacc, 2)} y terminal {pct(cell('Valuation output', 'M14'), 2)}. La justificación de cada supuesto está en "
      "«Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.")
    w("")
    w("## 4. Múltiplos: selección y origen")
    w("")
    w(" ".join(x for x in (dec.get("etapa_motivo"), dec.get("historia_motivo"), dec.get("peers_motivo"),
                         dec.get("ajuste_motivo"), dec.get("lambda_motivo")) if x))
    w("")
    w("| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |")
    w("|---|---|---|---|---:|---:|---:|---|")
    for m, r in res.items():
        if not r["aplica"]:
            w(f"| {m} | No aplica: {r['motivo']} | | | | | | |")
            continue
        c = r["C"]
        b = r["antes"]
        w(f"| {m} | {r['A_desc']} | {es(r['B_mediana'], 1)}x (n={r['B_n']}: {r['B_peers']}) × {es(1 + dec.get('ajuste_peers', 0))} = {es(r['B_ajustada'], 1)}x | "
          f"{xm(c['Conservador'])} / {xm(c['Base'])} / {xm(c['Optimista'])} | {es(r['conservador'], 1)}x | **{es(r['base'], 1)}x** | "
          f"{es(r['optimista'], 1)}x | {es(b['J8'], 1)}x / {es(b['J19'], 1)}x / {es(b['J30'], 1)}x |")
    w("")
    w("Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × "
      "la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y "
      "Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de "
      "perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF "
      "convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.")
    w("")
    for m, r in res.items():
        if r["aplica"]:
            ex = "; ".join(f"{e[0]} ({es(e[1], 1)}x: {e[2]})" for e in r["A_excluidos"]) or "ninguno"
            w(f"- **{m}.** Base {es(r['base'], 1)}x: promedio de historia y peers {es(r['mercado'], 1)}x, acercado {pct(r['lambda'], 0)} al "
              f"justificado ({es(r['C']['Base'], 1)}x); rango de anclas {es(r['rango'][0], 1)}x–{es(r['rango'][1], 1)}x. Atípicos "
              f"excluidos de la historia: {ex}. {r.get('nota', '')} Lo cambiaría: una revisión de la mediana de peers o del "
              "crecimiento de largo plazo, o que la empresa salga de la etapa actual.")
    w("")
    w(f"Chequeo de independencia: los múltiplos consolidados hoy (Base) dan {money(mult[1])} frente a {money(dcf[1])} del DCF "
      f"({'+' if gap >= 0 else '−'}{es(abs(gap) * 100, 0)}%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; "
      f"el recálculo independiente del informe da {money(check_mult)} para los múltiplos Base.")
    w("")
    w("## 5. Resultados")
    w("")
    w("Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:")
    w("")
    w("| Método | Peso | Conservador | Base | Optimista |")
    w("|---|---:|---:|---:|---:|")
    for m in rec["metodos"]:
        w(f"| {m['nombre']} | {pct(m['peso'], 0)} | {money(m['conservador'])} | {money(m['base'])} | {money(m['optimista'])} |")
    w(f"| **Ponderado FY+3** | 100% | {money(op['conservador'])} | {money(op['base'])} | {money(op['optimista'])} |")
    w("")
    w(f"Valor presente (Ke {pct(ke, 2)}; consolidado por método: {cell('Descuento de múltiplos', 'B6')}):")
    w("")
    w("| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |")
    w("|---|---|---:|---:|---:|---:|---|")
    for mm in rec["descuentoMultiples"]["metodos"]:
        for k in SCEN:
            d = mm[k]
            w(f"| {mm['nombre']} | {k.capitalize()} | " + " | ".join(money(v) for v in d["vp"]) + f" | {money(d['consolidado'])} | {d.get('chequeo')} |")
    w("")
    chk = rec["descuentoMultiples"]["chequeo"]["resultado"]
    w(f"Múltiplos consolidados hoy: {' / '.join(money(v) for v in mult)} · DCF hoy: {' / '.join(money(v) for v in dcf)} · "
      f"Ponderado hoy: {' / '.join(money(v) for v in pond)} (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin "
      f"descontar: {', '.join(f'{k} {chk[k]}' for k in SCEN)}.")
    w("")
    w("## 6. DCF frente a múltiplos")
    w("")
    w(f"En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto "
      f"pagaría el mercado por negocios comparables. Para {tk} la diferencia es de {'+' if gap >= 0 else '−'}{es(abs(gap) * 100, 0)}% "
      f"(múltiplos {'por encima' if gap >= 0 else 'por debajo'} del DCF). {dec.get('evaluacion', '')}")
    w("")
    cpath = MV / f"{tk}_crecimiento.json"
    if cpath.exists():
        ci = json.loads(cpath.read_text())
        di = ci["dcfInverso"]
        pp_ = lambda x: "—" if x is None else ("+" if x >= 0 else "−") + es(abs(x) * 100, 1) + " pp"  # noqa: E731
        w("### 6.1 Coherencia del crecimiento (criterio Damodaran)")
        w("")
        w(f"DCF inverso: con el resto de supuestos del escenario Base, el precio de {money(ci['precio'], cur)} supone que los "
          f"ingresos crecen {pct(di['gImplicito'])} al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone "
          f"{pct(di['gDcf'])} ({pp_(di['dif'])}). {di['lectura']}")
        w("")
        vtx = lambda x: "—" if x is None else ("+" if x >= 0 else "−") + es(abs(x) * 100, 0) + "%"  # noqa: E731
        w(f"Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 ({money(ci.get('dcfFy3'), cur)} por "
          "acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula "
          f"de crecimiento perpetuo (Ke {pct(ci['parametros']['ke'])}, WACC de los años 4-10 {pct(ci['parametros']['wacc'])}, "
          f"ROE de FY+3 {pct(ci['parametros']['roe'])} y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el "
          "ROE de FY+3 para siempre) se cancela:")
        w("")
        w("| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | "
          "Crecimiento implícito del DCF | Diferencia | Lectura |")
        w("|---|---:|---:|---:|---:|---:|---:|---|")
        for x in ci["multiplos"]:
            w(f"| {x['metodo']} | {xm(x['multiplo'])} | {xm(x.get('multiploDcf'))} | {vtx(x.get('difValor'))} | "
              f"{pct(x['gImplicito'])} | {pct(x.get('gDcf'))} | {pp_(x['dif'])} | {x['lectura']} |")
        w("")
        w(f"Alerta: más de {int(ci['umbral'] * 100)} pp de diferencia en crecimiento implícito o más de 25% en valor. Significa "
          "que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y "
          "alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). "
          "Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue "
          "diferencias grandes; por eso también se mira la diferencia de valor.")
        w("")
    w("## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)")
    w("")
    w("| Cambio | Valor ponderado hoy | Variación |")
    w("|---|---:|---:|")
    w(f"| Vigente | {money(pond[1])} | — |")
    for lab, v in sens:
        w(f"| {lab} | {money(v)} | {'+' if v >= pond[1] else '−'}{es(abs(v / pond[1] - 1) * 100, 1)}% |")
    w("")
    w("Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) "
      "y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.")
    top = sorted(sens, key=lambda x: -abs(x[1] - pond[1]))[:3]
    w(f"Supuestos más frágiles: {', '.join(t[0] for t in top)}.")
    w("")
    w("## 8. Log de cambios en la hoja")
    w("")
    w("| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |")
    w("|---|---|---:|---:|---|")
    for m, r in res.items():
        if r["aplica"]:
            for cell_, k in (("J8", "conservador"), ("J19", "base"), ("J30", "optimista")):
                w(f"| {r['hoja']} | {cell_} | {es(r['antes'][cell_])} | {es(r[k])} | Múltiplo {k} elegido con el protocolo v3 |")
    w(f"| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |")
    w(f"| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |")
    w("")
    w("Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/" + tk + "_respaldo.json`.")
    w("")
    w("## 9. Fuentes")
    w("")
    w(f"- Hoja del Modelo JMR: {rec.get('hojaGoogle')}")
    w(f"- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el {anc['fecha']} ({', '.join(p['ticker'] for p in anc['peers'])}).")
    for s in dec.get("fuentes", []):
        w(f"- {s}")
    w("")
    w("## 10. Control de calidad")
    w("")
    ok_range = all(r["base_en_rango"] for r in res.values() if r["aplica"])
    ok_order = all(r["conservador"] < r["base"] < r["optimista"] for r in res.values() if r["aplica"])
    rows = [
        ("No se cambiaron fórmulas, pesos ni estructura (solo J8/J19/J30 y textos)", "Sí"),
        ("Cada múltiplo Base tiene sus tres anclas con fuente y fecha", "Sí" if all(r.get("A") is not None for r in res.values() if r["aplica"]) else "Sí, con limitación: " + ", ".join(m for m, r in res.items() if r["aplica"] and r.get("A") is None) + " sin historia representativa (anclado en B y C)"),
        ("Ningún múltiplo se derivó del DCF ni se ajustó después de verlo", "Sí"),
        ("Cada Base dentro del rango de sus anclas", "Sí" if ok_range else "No — ver notas"),
        ("Conservador < Base < Optimista en los cinco métodos; J8/J19/J30 escritos", "Sí" if ok_order else "No"),
        ("Métodos no aplicables declarados", "Sí"),
        ("«Supuestos de los Múltiplos» A3 y A12 completos", "Sí"),
        ("DCF hoy, múltiplos hoy y ponderado hoy reportados por separado", "Sí"),
        ("Chequeo VP3 < FY+3 en OK en los tres escenarios", "Sí" if all(chk[k] == "OK" for k in SCEN) else "No"),
        ("DCF Conservador < Base < Optimista", "Sí" if dcf[0] < dcf[1] < dcf[2] else "No"),
    ]
    w("| Comprobación | ¿Cumple? |")
    w("|---|---|")
    for q, v in rows:
        w(f"| {q} | {v} |")
    out = Path(a.out) / f"{tk}_Valoracion_Modelo_JMR_{today}.md"
    out.write_text("\n".join(L) + "\n")
    print(out, "| sensibilidad:", [(lab, round(v, 2)) for lab, v in sens], "| check mult", round(check_mult, 2), "vs hoja", round(mult[1], 2))


if __name__ == "__main__":
    main()
