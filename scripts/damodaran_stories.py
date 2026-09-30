"""Sección «Valor con criterio Damodaran» de un análisis fundamental (prompt de research v5,
sección 12; prompt de valoración v4, paso 5B).

A partir de una ficha escrita por el analista (reference/damodaran/<T>.json: historia, filtro
posible/plausible/probable, piezas del valor, 3-4 historias por segmento con probabilidades,
pre-mortem, indicadores y fuentes) calcula con el motor del Modelo JMR (docs/jmr_engine.js),
que reproduce la hoja: cada historia es un DCF completo con los insumos de la hoja (insumosDesdeHoja)
y su propio crecimiento año a año, margen, reinversión y ROIC terminal; el valor esperado es el promedio
ponderado por probabilidad. Las tablas de sensibilidad y DCF inverso se calibran contra el DCF de la hoja:

- el valor por acción de cada historia con la beta de la hoja y con la beta propuesta
  (bottom-up del sector de Damodaran, reapalancada, más el ajuste que justifique la ficha);
- el valor esperado ponderado por probabilidad;
- la sensibilidad crecimiento × margen del DCF Base;
- las tasas base de crecimiento de ventas a 5 años para el tamaño de la empresa (Mauboussin &
  Callahan, The Base Rate Book 2016, Exhibit 4; reales, se les suma una inflación de 2,5% para
  compararlas con el crecimiento nominal);
- el DCF inverso (crecimiento de los años 1-5 que justifica el precio) con dos márgenes y dos betas.

No modifica la hoja. Escribe reference/damodaran/<T>_resultado.json, la sección en HTML
(reference/damodaran/<T>_seccion.html) y en Markdown (data/<T>_Analisis_Damodaran_<fecha>.md).

Uso:
    python scripts/damodaran_stories.py CELH [ADBE ...]
"""
from __future__ import annotations

import datetime as dt
import glob
import html
import json
import statistics as st
import subprocess
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402
from valuation_report_v3 import ENGINE, engine_inputs  # noqa: E402

REF = _ROOT / "reference" / "damodaran"
DATOS = _ROOT.parent / "Modelo-JMR-datos"
INFLACION = 0.025
BUCKETS = [(325, "$0-325 Mn"), (700, "$325-700 Mn"), (1250, "$700-1,250 Mn"), (2000, "$1,250-2,000 Mn"),
           (3000, "$2,000-3,000 Mn"), (4500, "$3,000-4,500 Mn"), (7000, "$4,500-7,000 Mn"),
           (12000, "$7,000-12,000 Mn"), (25000, "$12,000-25,000 Mn"), (50000, ">$25,000 Mn"), (float("inf"), ">$50,000 Mn")]
BIN_EDGES = {"<(25)": (-60, -25), "(25)-(20)": (-25, -20), "(20)-(15)": (-20, -15), "(15)-(10)": (-15, -10),
             "(10)-(5)": (-10, -5), "(5)-0": (-5, 0), "0-5": (0, 5), "5-10": (5, 10), "10-15": (10, 15),
             "15-20": (15, 20), "20-25": (20, 25), "25-30": (25, 30), "30-35": (30, 35), "35-40": (35, 40),
             "40-45": (40, 45), ">45": (45, 80)}


# ---------------------------------------------------------------- formato
def es(v, nd=2):
    return f"{v:,.{nd}f}".replace(",", "X").replace(".", ",").replace("X", ".") if isinstance(v, (int, float)) else "—"


def pct(v, nd=1):
    return es(v * 100, nd) + "%" if isinstance(v, (int, float)) else "—"


def usd(v):
    return "US$" + es(v) if isinstance(v, (int, float)) else "—"


# ---------------------------------------------------------------- motor
def run_exact(grid, cases):
    """Valor por acción con el motor exacto (reproduce 'Valuation output'): insumos leídos de la hoja con
    insumosDesdeHoja y, por caso, cambios opcionales: anios (crecimiento de cada año 1-5), g (el mismo para
    los años 1-5), m (margen objetivo), wacc, s2c (años 1-5) y roic (ROIC después del año 10; 0 = costo de capital)."""
    js = ("const fs=require('fs'),vm=require('vm');const c={};vm.createContext(c);"
          f"vm.runInContext(fs.readFileSync({json.dumps(str(ENGINE))},'utf8'),c);"
          "const G=JSON.parse(fs.readFileSync(0,'utf8'));"
          "const col=a=>{let n=0;for(const ch of a)n=n*26+ch.charCodeAt(0)-64;return n-1;};"
          "const celda=(h,a)=>{const g=G.grid[h];if(!g)return null;const m=a.match(/^([A-Z]+)(\\d+)$/);const r=g[+m[2]-1];"
          "if(!r)return null;const v=r[col(m[1])];return (v===undefined||v==='')?null:v;};"
          "const base=c.insumosDesdeHoja(celda);"
          "const out=G.cases.map(k=>{const i=JSON.parse(JSON.stringify(base));"
          "if(k.anios)i.crecimientoAnios=k.anios;else if(k.g!=null)i.crecimientoAnios=[k.g,k.g,k.g,k.g,k.g];"
          "if(k.wacc!=null)i.wacc=k.wacc;if(k.s2c!=null)i.salesToCapital=k.s2c;if(k.roic!=null)i.roicTerminal=k.roic;"
          "const margin=k.m!=null?k.m:(i.dcfFinanciero?i.dcfFinanciero.roeBase:i.marginBase);"
          "const value=g=>{if(g!=null)i.crecimientoAnios=[g,g,g,g,g];return c.runDCFDetalle(i,i.growthBase,margin,i.growthY1Base,i.marginY1Base).valuePerShare;};"
          "if(k.target!=null){const roots=[];let pg=-.1,pf=value(pg)-k.target;"
          "for(let g=-.098;g<=.600001;g+=.002){const f=value(g)-k.target;if(pf*f<=0){let lo=pg,hi=g,fl=pf;for(let n=0;n<50;n++){const mid=(lo+hi)/2,fm=value(mid)-k.target;if(fl*fm<=0)hi=mid;else{lo=mid;fl=fm;}}roots.push((lo+hi)/2);}pg=g;pf=f;}"
          "return roots.length?roots.sort((a,b)=>Math.abs(a-k.ref)-Math.abs(b-k.ref))[0]:null;}"
          "return value(null);});"
          "console.log(JSON.stringify(out));")
    return json.loads(subprocess.check_output(["node", "-e", js], input=json.dumps({"grid": grid, "cases": cases}), text=True))


# ---------------------------------------------------------------- tasas base
def base_rates(revenue_mn: float) -> dict:
    br = json.loads((REF / "base_rates_5y.json").read_text())
    name = next(n for lim, n in BUCKETS if revenue_mn < lim)
    return {"tramo": name, **br["tamanos"][name], "bins": br["bins"], "fuente": br["fuente"]}


def frac_at_least(br: dict, g_nominal: float) -> float:
    """Fracción de empresas del tramo con CAGR real a 5 años ≥ (g nominal − inflación)."""
    x = (g_nominal - INFLACION) * 100
    tot = 0.0
    for b in br["bins"]:
        lo, hi = BIN_EDGES[b]
        p = br.get(b, 0.0)
        if x <= lo:
            tot += p
        elif x < hi:
            tot += p * (hi - x) / (hi - lo)
    return tot / 100


# ---------------------------------------------------------------- hoja
def load_sheet(sid: str):
    sh = get_gspread_client().open_by_key(sid)
    rng = ["'Input sheet'!A1:D75", "'Valuation output'!A1:M140", "'Financials Multiples'!A1:H120",
           "'Resumen de Valoración'!A1:U20", "'Cost of capital worksheet'!A1:C70", "'Descuento de múltiplos'!A1:E40",
           "EVEBITDA!A1:J30", "EVFCFF!A1:J30", "PE!A1:J30", "PFCFE!A1:J30", "POCF!A1:J30"]
    if 'DCF FCFE financiero' in {w.title for w in sh.worksheets()}:rng.append("'DCF FCFE financiero'!A1:I62")
    vr = sh.values_batch_get(rng, params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
    grid = {r.split("!")[0].strip("'"): v.get("values", []) for r, v in zip(rng, vr)}

    def cell(s, a):
        col, row = ord(a[0]) - 65, int(a[1:]) - 1
        g = grid[s]
        return g[row][col] if row < len(g) and col < len(g[row]) else None
    return grid, cell


def coc_row(grid, label):
    for r in grid["Cost of capital worksheet"]:
        if r and str(r[0]).strip().startswith(label):
            return [x for x in r[1:] if isinstance(x, (int, float))]
    return []


# ---------------------------------------------------------------- cálculo
def compute(tk: str) -> dict:
    spec = json.loads((REF / f"{tk}.json").read_text())
    anc = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())
    rec = json.loads(Path(glob.glob(str(DATOS / "valoraciones" / f"{tk}-*.json"))[0]).read_text())
    grid, cell = load_sheet(anc["sheet_id"])
    price = rec.get("precio")
    dcf = cell("Descuento de múltiplos", "D38") or ((rec.get("descuentoMultiples") or {}).get("dcfHoy") or {}).get("base")
    inp = engine_inputs(cell, grid["Financials Multiples"], price)
    m_base = inp["dcfFinanciero"]["roeBase"] if inp.get("dcfFinanciero") else cell("Input sheet", "B30")
    g_ref = st.mean([x for x in grid["Valuation output"][3][2:7] if isinstance(x, (int, float))])
    s2c = cell("Input sheet", "B32")
    wacc0 = cell("Input sheet", "B36")
    inp["salesToCapital"] = s2c
    # Referencia de las tablas de sensibilidad y DCF inverso (crecimiento igual en los años 1-5): se calibran contra
    # el DCF de la hoja. Las historias y la tabla de betas no se calibran: el motor reproduce la hoja exactamente.
    ref = run_exact(grid, [{"g": g_ref, "m": m_base}])[0]

    # riesgo
    rf = cell("Input sheet", "B35")
    erp = coc_row(grid, "Equity Risk Premium used")[0]
    beta_hoja = (coc_row(grid, "Levered Beta for equity") or coc_row(grid, "If direct input, enter levered beta"))[0]
    w = coc_row(grid, "Weight in Cost of Capital")
    comp = coc_row(grid, "Cost of Component")
    e_w, d_w = w[0], (w[1] if len(w) > 1 else 0.0)
    kd_at = comp[1] if len(comp) > 1 else 0.0
    tax = cell("Input sheet", "B25") or 0.25
    industria = spec.get("industria_damodaran") or cell("Input sheet", "B10")
    betas = json.loads((REF / "betas_us_2026-01.json").read_text())["industrias"]
    ind = betas.get(industria)
    bu = ind["Unlevered beta corrected for cash"] if ind else None
    de = d_w / e_w if e_w else 0.0
    beta_bu = bu * (1 + (1 - tax) * de) if bu else None
    beta_prop = spec.get("riesgo", {}).get("beta_propuesta") or beta_bu or beta_hoja

    def wacc_for(beta):
        # desplaza el WACC de la hoja por el cambio en el costo del patrimonio
        return wacc0 + e_w * (beta - beta_hoja) * erp

    def value(g, m, beta=None, s2c_=None, roic=None, anios=None):
        k = {"m": m}
        if anios is not None:
            k["anios"] = anios
        elif g is not None:
            k["g"] = g
        if roic is not None:  # ROIC después del año 10 propio de la historia (0 = igual al costo de capital)
            k["roic"] = roic
        if beta is not None:
            k["wacc"] = wacc_for(beta)
        if s2c_ is not None:
            k["s2c"] = s2c_
        return k

    br = base_rates(cell("Input sheet", "B12"))

    # historias
    segs = spec["segmentos"]
    rev0 = cell("Input sheet", "B12")
    scale = rev0 / sum(segs.values())
    historias = []
    cases = []
    for h in spec["historias"]:
        revs = {k: v * scale for k, v in segs.items()}
        anios, prev = [], rev0
        for y in range(5):
            for k in revs:
                revs[k] *= 1 + h["crec"].get(k, [0] * 5)[y]
            anios.append(sum(revs.values()) / prev - 1)
            prev = sum(revs.values())
        rev5 = sum(revs.values())
        cagr = (rev5 / rev0) ** (1 / 5) - 1
        s2 = h.get("s2c")  # sin s2c propio, la historia usa los de la hoja (años 1-5 y 6-10)
        # Una historia en la que la ventaja se erosiona no conserva retornos excedentes: "costo_capital" lleva el ROIC
        # después del año 10 al costo de capital aunque la hoja (escenario Base) use un ROIC terminal mayor.
        rt = h.get("roic_terminal")
        roic = 0.0 if rt == "costo_capital" else (rt if isinstance(rt, (int, float)) else None)
        historias.append({**h, "cagr": cagr, "rev5": rev5, "mix5": {k: v / rev5 for k, v in revs.items()},
                          "tasa_base": frac_at_least(br, cagr),
                          "roic_terminal_usado": roic if roic is not None else inp.get("roicTerminal", 0)})
        # Cada historia es un DCF completo con la estructura de la hoja (crecimiento año a año, convergencia del
        # margen, impuestos, sales-to-capital por tramo, deuda y caja): el valor esperado es su promedio ponderado.
        cases += [value(None, h["margen"], None, s2, roic, anios), value(None, h["margen"], beta_prop, s2, roic, anios)]
    vals = run_exact(grid, cases)
    for i, h in enumerate(historias):
        h["valor_beta_hoja"], h["valor_beta_prop"] = vals[2 * i], vals[2 * i + 1]
    ev_h = sum(h["prob"] * h["valor_beta_hoja"] for h in historias)
    ev_p = sum(h["prob"] * h["valor_beta_prop"] for h in historias)

    # beta: DCF Base con cada beta
    beta_rows = [("Hoja (regresión o la cargada en el libro)", beta_hoja)]
    if beta_bu:
        beta_rows.append((f"Bottom-up del sector ({industria}, reapalancada)", beta_bu))
    if spec.get("riesgo", {}).get("beta_propuesta"):
        beta_rows.append(("Propuesta (sector ajustado por riesgo propio)", beta_prop))
    bv = run_exact(grid, [{"wacc": wacc_for(b)} for _, b in beta_rows])
    betas_tab = [{"enfoque": n, "beta": b, "ke": rf + b * erp, "wacc": wacc_for(b), "dcf_base": v}
                 for (n, b), v in zip(beta_rows, bv)]

    # sensibilidad
    gs = [g_ref + d for d in (-0.04, -0.02, 0, 0.02, 0.04)]
    ms = [m_base + d for d in (-0.04, -0.02, 0, 0.02, 0.04)]
    sv = run_exact(grid, [value(g, m) for g in gs for m in ms])
    sens = {"g": gs, "m": ms, "v": [[sv[i * 5 + j] for j in range(5)] for i in range(5)],
            "referencia_constante": ref, "criterio": "DCF completo sin factor de calibración; crecimiento constante en años 1–5"}

    # DCF inverso
    inv_m = spec.get("margenes_inverso") or [m_base, m_base + 0.02]
    grid_g = [x / 1000 for x in range(-100, 601, 2)]
    inverso = []
    for b in (beta_hoja, beta_prop):
        for m in inv_m:
            case = value(None, m, b)
            case.update(target=price, ref=g_ref)
            gi = run_exact(grid, [case])[0] if price else None
            inverso.append({"beta": b, "margen": m, "g": gi, "tasa_base": frac_at_least(br, gi) if gi is not None else None})

    financiero = bool(inp.get("dcfFinanciero"))
    sup = {k: inp.get(k) for k in ("growthY1Cons", "growthY1Base", "growthY1Opt", "growthCons", "growthBase", "growthOpt",
                                   "marginY1Cons", "marginY1Base", "marginY1Opt", "marginCons", "marginBase", "marginOpt",
                                   "salesToCapital2", "wacc", "costoPatrimonio", "taxEffective", "convergenceYear",
                                   "terminalWacc", "roicTerminal")}
    sup["salesToCapital"] = s2c
    sin_exceso = None if financiero else run_exact(grid, [{"roic": 0}])[0]

    return {"ticker": tk, "fecha": spec.get("fecha") or dt.date.today().isoformat(), "spec": spec,
            "supuestos": sup, "financiero": financiero, "dcf_sin_exceso": sin_exceso,
            "precio": price, "dcf_base": dcf, "g_ref": g_ref, "m_base": m_base, "s2c": s2c, "wacc": wacc0,
            "beta_hoja": beta_hoja, "beta_bu": beta_bu, "beta_prop": beta_prop, "industria": industria,
            "bu_sector": bu, "rf": rf, "erp": erp, "tasas_base": br, "historias": historias,
            "valor_esperado_beta_hoja": ev_h, "valor_esperado_beta_prop": ev_p, "betas": betas_tab,
            "sensibilidad": sens, "inverso": inverso, "ingresos_ltm": rev0}


# ---------------------------------------------------------------- render
def table(cols, rows, align=None):
    align = align or ["l"] * len(cols)
    md = "| " + " | ".join(cols) + " |\n|" + "|".join("---:" if a == "r" else "---" for a in align) + "|\n"
    md += "".join("| " + " | ".join(str(c) for c in r) + " |\n" for r in rows)
    ht = "<table><thead><tr>" + "".join(f"<th>{html.escape(str(c))}</th>" for c in cols) + "</tr></thead><tbody>"
    ht += "".join("<tr>" + "".join(f"<td>{inline_html(str(c))}</td>" for c in r) + "</tr>" for r in rows) + "</tbody></table>"
    return md, ht


def inline_html(s: str) -> str:
    """Markdown mínimo: **negrita**, *cursiva* y [texto](url)."""
    import re
    t = html.escape(s)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\s][^*]*?)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>', t)
    return t


def render(r: dict) -> tuple[str, str]:
    sp = r["spec"]
    md, ht = [], []

    def h3(t):
        md.append(f"\n### {t}\n")
        ht.append(f"<h3>{html.escape(t)}</h3>")

    def p(t):
        md.append(t + "\n")
        ht.append(f"<p>{inline_html(t)}</p>")

    def tab(cols, rows, align=None):
        a, b = table(cols, rows, align)
        md.append(a)
        ht.append(b)

    def ul(items):
        md.append("".join(f"{i + 1}. {x}\n" for i, x in enumerate(items)))
        ht.append("<ol>" + "".join(f"<li>{inline_html(x)}</li>" for x in items) + "</ol>")

    p("Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, "
      "piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el "
      f"motor del Modelo JMR, que reproduce la hoja (DCF Base de {usd(r['dcf_base'])} por acción): solo cambian el "
      "crecimiento de cada año, el margen objetivo, la reinversión y el ROIC después del año 10 de la historia; la tasa "
      "de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las "
      "historias ponderado por su probabilidad. La hoja no se modifica. Los múltiplos son precio relativo y se comentan "
      "en otras secciones.")

    h3("La historia en un párrafo")
    p(sp["historia"])
    tab(["Afirmación", "¿Posible?", "¿Plausible?", "¿Probable?"], sp["filtro"])

    br = r["tasas_base"]
    h3("Visión externa: tasas base")
    p(f"Con ventas LTM de US${es(r['ingresos_ltm'], 0)} millones, la empresa está en el tramo **{br['tramo']}** de las "
      f"tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, "
      f"1950-2015). En ese tramo el crecimiento real anual tuvo una media de {es(br['Mean'], 1)}% y una mediana de "
      f"{es(br['Median'], 1)}% (desviación estándar {es(br['StDev'], 1)}%); sumando una inflación de "
      f"{es(INFLACION * 100, 1)}%, la mediana nominal ronda {es(br['Median'] + INFLACION * 100, 1)}%.")
    rows = [[h["nombre"], pct(h["cagr"]), pct(h["tasa_base"], 0)] for h in r["historias"]]
    tab(["Historia", "Crecimiento anual de ingresos (5 años)", "Empresas de este tamaño que lo lograron"], rows, ["l", "r", "r"])
    p(sp["tasas_base_nota"])

    h3("Piezas del valor")
    for key, titulo in (("crecimiento", "Crecimiento"), ("margenes", "Márgenes"), ("reinversion", "Reinversión y retorno")):
        blk = sp.get(key) or {}
        if blk.get("texto"):
            p(f"**{titulo}.** " + blk["texto"])
        if blk.get("tabla"):
            tab(blk["tabla"]["cols"], blk["tabla"]["rows"], blk["tabla"].get("align"))
    rk = sp.get("riesgo", {})
    p("**Riesgo.** " + rk.get("texto", ""))
    tab(["Enfoque", "Beta", "Costo del patrimonio", "WACC inicial", "DCF Base por acción"],
        [[b["enfoque"], es(b["beta"]), pct(b["ke"]), pct(b["wacc"]), usd(b["dcf_base"])] for b in r["betas"]],
        ["l", "r", "r", "r", "r"])

    su = r.get("supuestos") or {}
    if r.get("financiero"):
        h3("DCF financiero: supuestos y limitaciones")
        p((sp.get("margenes") or {}).get("texto", "") + " " + (sp.get("reinversion") or {}).get("texto", ""))
    elif su.get("growthBase") is not None:
        h3("Supuestos vigentes verificados")
        tab(["Supuesto", "Conservador", "Base", "Optimista"],
            [[lab] + [pct(su.get(k + s_)) for s_ in ("Cons", "Base", "Opt")] for lab, k in (
                ("Crecimiento año 1", "growthY1"), ("Crecimiento años 2–5", "growth"),
                ("Margen año 1 (base ajustada del modelo)", "marginY1"), ("Margen objetivo", "margin"))],
            ["l", "r", "r", "r"])
        p(f"Ventas/capital: {es(su.get('salesToCapital'), 1)}x en años 1–5 y {es(su.get('salesToCapital2'), 1)}x en 6–10. "
          f"WACC: {pct(su.get('wacc'))}. Ke: {pct(su.get('costoPatrimonio'))}. Impuesto efectivo: {pct(su.get('taxEffective'))}. "
          f"Convergencia: {es(su.get('convergenceYear'), 0)} años. Estos parámetros son escenarios del analista, no cifras reportadas.")
    moat = (json.loads((_ROOT / "reference" / "moat_2026-09-30.json").read_text())["empresas"]).get(r["ticker"])
    if moat and not r.get("financiero") and r.get("dcf_sin_exceso") is not None:
        rt = moat.get("roic_terminal")
        h3("Ventaja competitiva y ROIC terminal: comprobación")
        tab(["Ventaja (criterio Damodaran)", "ROIC actual (modelo)", "ROIC de la industria (Damodaran)", "Costo de capital terminal",
             "ROIC terminal usado", "DCF Base", "DCF con ROIC terminal = costo de capital"],
            [[moat["ventaja"].capitalize(), pct(moat["roic_actual"]), pct(moat["roic_industria"]) if moat.get("roic_industria") else "No disponible",
              pct(moat["costo_capital_terminal"]), pct(rt) if rt else "= costo de capital", usd(r["dcf_base"]), usd(r["dcf_sin_exceso"])]],
            ["l", "r", "r", "r", "r", "r", "r"])
        p(f"Fuentes de ventaja: {moat['fuentes']}. Evidencia: {moat['evidencia']}. Criterio (Damodaran, *Investment Valuation*, "
          "cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el "
          "promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre "
          "ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del "
          "motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.")

    h3("Historias cuantificadas y valor esperado")
    segs = list(sp["segmentos"].keys())
    same = abs(r["beta_prop"] - r["beta_hoja"]) < 0.005  # la hoja ya usa la beta propuesta: una sola columna
    con_roic = any((h.get("roic_terminal_usado") or 0) > 0 for h in r["historias"])
    roic_txt = lambda h: (pct(h["roic_terminal_usado"]) if (h.get("roic_terminal_usado") or 0) > 0 else "= costo de capital")  # noqa: E731
    rows = []
    for h in r["historias"]:
        crec = "; ".join(f"{k}: " + ", ".join(es(x * 100, 0) + "%" for x in h["crec"].get(k, [0] * 5)) for k in segs) if len(segs) > 1 else \
            ", ".join(es(x * 100, 0) + "%" for x in h["crec"][segs[0]])
        rows.append([f"**{h['nombre']}**", pct(h["prob"], 0), crec, pct(h["cagr"]), pct(h["margen"], 0),
                     es(h.get("s2c", r["s2c"]), 1)] + ([roic_txt(h)] if con_roic else []) +
                    [usd(h["valor_beta_hoja"])] + ([] if same else [usd(h["valor_beta_prop"])]))
    rows.append(["**Valor esperado**", "100%", "", "", "", ""] + ([""] if con_roic else []) + [f"**{usd(r['valor_esperado_beta_hoja'])}**"] +
                ([] if same else [f"**{usd(r['valor_esperado_beta_prop'])}**"]))
    tab(["Historia", "Probabilidad", "Crecimiento por segmento (años 1-5)", "Crecimiento anual del grupo",
         "Margen objetivo", "Sales-to-capital"] + (["ROIC después del año 10"] if con_roic else []) + [f"Valor/acción (beta {es(r['beta_hoja'])})"] +
        ([] if same else [f"Valor/acción (beta {es(r['beta_prop'])})"]), rows,
        ["l", "r", "l", "r", "r", "r"] + (["r"] if con_roic else []) + ["r"] + ([] if same else ["r"]))
    p(sp["prob_texto"] + " **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**")
    s = r["sensibilidad"]
    p(f"Sensibilidad del DCF Base (beta {es(r['beta_hoja'])}; US$ por acción; filas = crecimiento de los años 1-5, "
      "columnas = margen operativo objetivo):")
    p("Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; "
      "si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.")
    tab(["Crecimiento \\ Margen"] + [pct(m) for m in s["m"]],
        [[pct(g)] + [es(v) for v in row] for g, row in zip(s["g"], s["v"])], ["l"] + ["r"] * 5)

    h3("Pre-mortem")
    ul(sp["premortem"])
    p("**Evidencia en contra de la historia más probable:** " + sp["contra"])

    h3("Indicadores y actualización de probabilidades")
    tab(["Indicador", "Hoy", "Refuerza historias favorables si…", "Refuerza historias desfavorables si…"], sp["indicadores"])
    p("Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies "
      "el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).")

    h3("El precio al final")
    p(f"Precio de referencia de la valoración guardada: **{usd(r['precio'])}**.")
    ms = sorted({x["margen"] for x in r["inverso"]})
    bs = []
    for x in r["inverso"]:
        if x["beta"] not in bs:
            bs.append(x["beta"])

    def gi_txt(x):
        if x is None or x["g"] is None:
            return "ninguno entre −10% y 60%"
        if x["g"] <= -0.1:  # piso de la búsqueda: el precio supone una caída aún mayor
            return "≤ −10% (el precio supone una caída mayor)"
        return f"{pct(x['g'])} ({pct(x['tasa_base'], 0)} de las empresas)"
    rows = [[f"Beta {es(b)}"] + [gi_txt(next((x for x in r['inverso'] if x['beta'] == b and x['margen'] == m), None)) for m in ms] for b in bs]
    p("DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción "
      "de empresas de este tamaño que lo logró):")
    tab([""] + [f"Margen {pct(m, 0)}" for m in ms], rows, ["l"] + ["r"] * len(ms))
    diff_h = r["precio"] / r["valor_esperado_beta_hoja"] - 1 if r["precio"] else None
    diff_p = r["precio"] / r["valor_esperado_beta_prop"] - 1 if r["precio"] else None
    pos = lambda d: f"{'por encima' if d > 0 else 'por debajo'} en {es(abs(d) * 100, 0)}%"  # noqa: E731
    if same:
        p(f"Frente al valor esperado de las historias ({usd(r['valor_esperado_beta_hoja'])}), el precio está {pos(diff_h)}. " + sp["precio_lectura"])
    else:
        p(f"Frente al valor esperado de las historias ({usd(r['valor_esperado_beta_hoja'])} con la beta de la hoja; "
          f"{usd(r['valor_esperado_beta_prop'])} con la propuesta), el precio está {pos(diff_h)} y {pos(diff_p)}, respectivamente. " + sp["precio_lectura"])

    h3("Registro de decisión")
    probs = " / ".join(f"{h['nombre'].split(' · ')[0]} {pct(h['prob'], 0)}" for h in r["historias"])
    lo = min(min(h["valor_beta_hoja"], h["valor_beta_prop"]) for h in r["historias"])
    hi = max(max(h["valor_beta_hoja"], h["valor_beta_prop"]) for h in r["historias"])
    tab(["Campo", "Propuesta del análisis", "Tu estimación"], [
        ["Fecha", r["fecha"], ""],
        ["Historia en una frase", sp["frase"], ""],
        ["Probabilidades", probs, ""],
        ["Valor esperado" + ("" if same else " (beta de la hoja / propuesta)"), usd(r['valor_esperado_beta_hoja']) + ("" if same else f" / {usd(r['valor_esperado_beta_prop'])}"), ""],
        ["Rango (historia más débil a más fuerte)", f"{usd(lo)} a {usd(hi)}", ""],
        ["Confianza", sp["confianza"], ""],
        ["Qué cambiaría la opinión", sp["cambiaria"], ""],
        ["Revisión", sp["revision"], ""],
    ])
    p("La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no "
      "la toma por ti.")
    if sp.get("fuentes"):
        h3("Fuentes de esta sección")
        md.append("".join((f"- [{t}]({u})\n" if u else f"- {t}\n") for t, u in sp["fuentes"]))
        ht.append("<ul>" + "".join((f'<li><a href="{html.escape(u)}" target="_blank" rel="noopener">{html.escape(t)}</a></li>' if u
                                    else f"<li>{html.escape(t)}</li>") for t, u in sp["fuentes"]) + "</ul>")
    out_md, out_ht = "\n".join(md), "".join(ht)
    if r.get("financiero"):  # DCF de flujo al accionista: ROE en lugar de margen operativo
        for x, y in (("Margen objetivo", "ROE objetivo"), ("Sales-to-capital", "Reinversión patrimonial"),
                     ("crecimiento anual de ingresos", "crecimiento anual de beneficios"), ("margen operativo objetivo", "ROE objetivo")):
            out_md, out_ht = out_md.replace(x, y), out_ht.replace(x, y)
    return out_md, out_ht


def main(tickers):
    for tk in tickers:
        r = compute(tk)
        md, ht = render(r)
        (REF / f"{tk}_resultado.json").write_text(json.dumps({k: v for k, v in r.items() if k != "spec"}, ensure_ascii=False, indent=1))
        (REF / f"{tk}_seccion.html").write_text(ht)
        head = (f"---\nschema: \"jmr-analisis-damodaran-v1\"\nticker: \"{tk}\"\nanalysis_date: \"{r['fecha']}\"\n---\n\n"
                f"# {r['spec'].get('empresa', tk)} ({tk}) — Valor con criterio Damodaran\n\n"
                "> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría "
                "financiera ni una recomendación.\n")
        out_md = _ROOT / "data" / f"{tk}_Analisis_Damodaran_{r['fecha']}.md"
        if r["spec"].get("md_propio"):
            out_md = REF / f"{tk}_seccion.md"  # hay un documento escrito a mano con ese nombre; no se pisa
        out_md.write_text(head + md)
        print(f"{tk:5s} DCF {r['dcf_base']:.2f} | VE {r['valor_esperado_beta_hoja']:.2f} / {r['valor_esperado_beta_prop']:.2f} | "
              f"beta {r['beta_hoja']:.2f}→{r['beta_prop']:.2f} | " +
              " ".join(f"{h['nombre'].split(' · ')[0]}:{h['valor_beta_hoja']:.1f}" for h in r["historias"]), flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
