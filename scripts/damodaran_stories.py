"""Sección «Valor con criterio Damodaran» de un análisis fundamental (prompt de research v5,
sección 12; prompt de valoración v4, paso 5B).

A partir de una ficha escrita por el analista (reference/damodaran/<T>.json: historia, filtro
posible/plausible/probable, piezas del valor, 3-4 historias por segmento con probabilidades,
pre-mortem, indicadores y fuentes) calcula con el motor del Modelo JMR (docs/jmr_engine.js),
calibrado para que el escenario Base reproduzca exactamente el DCF de la hoja:

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
def run(cases):
    if len(cases) > 40:
        out = []
        for k in range(0, len(cases), 40):
            out += run(cases[k:k + 40])
        return out
    js = ("const fs=require('fs'),vm=require('vm');const c={};vm.createContext(c);"
          f"vm.runInContext(fs.readFileSync({json.dumps(str(ENGINE))},'utf8'),c);c.cases={json.dumps(cases)};"
          "console.log(JSON.stringify(vm.runInContext('cases.map(function(k){return runDCF(k.inp,k.g,k.m);})',c)));")
    return json.loads(subprocess.check_output(["node", "-e", js]))


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
    rng = ["'Input sheet'!A1:D70", "'Valuation output'!A1:M140", "'Financials Multiples'!A1:H120",
           "'Resumen de Valoración'!A1:U20", "'Cost of capital worksheet'!A1:C70", "'Descuento de múltiplos'!A1:E40"]
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
    m_base = cell("Input sheet", "B30")
    g_ref = st.mean([x for x in grid["Valuation output"][3][2:7] if isinstance(x, (int, float))])
    s2c = cell("Input sheet", "B32")
    wacc0 = cell("Input sheet", "B36")
    inp["salesToCapital"] = s2c
    ref = run([{"inp": inp, "g": g_ref, "m": m_base}])[0]

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

    def value(g, m, beta=None, s2c_=None):
        i = dict(inp)
        if beta is not None:
            i["wacc"] = wacc_for(beta)
        if s2c_ is not None:
            i["salesToCapital"] = s2c_
        return {"inp": i, "g": g, "m": m}

    br = base_rates(cell("Input sheet", "B12"))

    # historias
    segs = spec["segmentos"]
    rev0 = cell("Input sheet", "B12")
    scale = rev0 / sum(segs.values())
    historias = []
    cases = []
    for h in spec["historias"]:
        revs = {k: v * scale for k, v in segs.items()}
        for y in range(5):
            for k in revs:
                revs[k] *= 1 + h["crec"].get(k, [0] * 5)[y]
        rev5 = sum(revs.values())
        cagr = (rev5 / rev0) ** (1 / 5) - 1
        s2 = h.get("s2c", s2c)
        historias.append({**h, "cagr": cagr, "rev5": rev5, "mix5": {k: v / rev5 for k, v in revs.items()},
                          "tasa_base": frac_at_least(br, cagr)})
        cases += [value(cagr, h["margen"], beta_hoja, s2), value(cagr, h["margen"], beta_prop, s2)]
    vals = [dcf * v / ref for v in run(cases)]
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
    bv = run([value(g_ref, m_base, b) for _, b in beta_rows])
    betas_tab = [{"enfoque": n, "beta": b, "ke": rf + b * erp, "wacc": wacc_for(b), "dcf_base": dcf * v / ref}
                 for (n, b), v in zip(beta_rows, bv)]

    # sensibilidad
    gs = [g_ref + d for d in (-0.04, -0.02, 0, 0.02, 0.04)]
    ms = [m_base + d for d in (-0.04, -0.02, 0, 0.02, 0.04)]
    sv = run([value(g, m) for g in gs for m in ms])
    sens = {"g": gs, "m": ms, "v": [[dcf * sv[i * 5 + j] / ref for j in range(5)] for i in range(5)]}

    # DCF inverso
    inv_m = spec.get("margenes_inverso") or [m_base, m_base + 0.02]
    grid_g = [x / 1000 for x in range(-100, 601, 2)]
    inverso = []
    for b in (beta_hoja, beta_prop):
        for m in inv_m:
            vv = [dcf * x / ref for x in run([value(g, m, b) for g in grid_g])]
            gi = next((grid_g[k] for k in range(len(grid_g)) if vv[k] >= price), None) if price else None
            inverso.append({"beta": b, "margen": m, "g": gi, "tasa_base": frac_at_least(br, gi) if gi is not None else None})

    return {"ticker": tk, "fecha": spec.get("fecha") or dt.date.today().isoformat(), "spec": spec,
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
      "piezas del valor, historias cuantificadas y, recién al final, el precio. Los valores se calculan con el motor del "
      f"Modelo JMR calibrado para que el escenario Base reproduzca el DCF de la hoja ({usd(r['dcf_base'])} por acción); "
      "la hoja no se modifica. El valor intrínseco es el DCF; los múltiplos son precio relativo y se comentan en otras "
      "secciones.")

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

    h3("Historias cuantificadas y valor esperado")
    segs = list(sp["segmentos"].keys())
    rows = []
    for h in r["historias"]:
        crec = "; ".join(f"{k}: " + ", ".join(es(x * 100, 0) + "%" for x in h["crec"].get(k, [0] * 5)) for k in segs) if len(segs) > 1 else \
            ", ".join(es(x * 100, 0) + "%" for x in h["crec"][segs[0]])
        rows.append([f"**{h['nombre']}**", pct(h["prob"], 0), crec, pct(h["cagr"]), pct(h["margen"], 0),
                     es(h.get("s2c", r["s2c"]), 1), usd(h["valor_beta_hoja"]), usd(h["valor_beta_prop"])])
    rows.append(["**Valor esperado**", "100%", "", "", "", "", f"**{usd(r['valor_esperado_beta_hoja'])}**",
                 f"**{usd(r['valor_esperado_beta_prop'])}**"])
    tab(["Historia", "Probabilidad", "Crecimiento por segmento (años 1-5)", "Crecimiento anual del grupo",
         "Margen objetivo", "Sales-to-capital", f"Valor/acción (beta {es(r['beta_hoja'])})",
         f"Valor/acción (beta {es(r['beta_prop'])})"], rows, ["l", "r", "l", "r", "r", "r", "r", "r"])
    p(sp["prob_texto"] + " **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**")
    s = r["sensibilidad"]
    p(f"Sensibilidad del DCF Base (beta {es(r['beta_hoja'])}; US$ por acción; filas = crecimiento de los años 1-5, "
      "columnas = margen operativo objetivo):")
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
            return "no alcanza"
        return f"{pct(x['g'])} ({pct(x['tasa_base'], 0)} de las empresas)"
    rows = [[f"Beta {es(b)}"] + [gi_txt(next((x for x in r['inverso'] if x['beta'] == b and x['margen'] == m), None)) for m in ms] for b in bs]
    p("DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción "
      "de empresas de este tamaño que lo logró):")
    tab([""] + [f"Margen {pct(m, 0)}" for m in ms], rows, ["l"] + ["r"] * len(ms))
    diff_h = r["precio"] / r["valor_esperado_beta_hoja"] - 1 if r["precio"] else None
    diff_p = r["precio"] / r["valor_esperado_beta_prop"] - 1 if r["precio"] else None
    p(f"Frente al valor esperado de las historias ({usd(r['valor_esperado_beta_hoja'])} con la beta de la hoja; "
      f"{usd(r['valor_esperado_beta_prop'])} con la propuesta), el precio está "
      f"{'por encima' if (diff_h or 0) > 0 else 'por debajo'} en {es(abs(diff_h) * 100, 0)}% y "
      f"{es(abs(diff_p) * 100, 0)}%, respectivamente. " + sp["precio_lectura"])

    h3("Registro de decisión")
    probs = " / ".join(f"{h['nombre'].split(' · ')[0]} {pct(h['prob'], 0)}" for h in r["historias"])
    lo = min(h["valor_beta_hoja"] for h in r["historias"])
    hi = max(h["valor_beta_prop"] for h in r["historias"])
    tab(["Campo", "Propuesta del análisis", "Tu estimación"], [
        ["Fecha", r["fecha"], ""],
        ["Historia en una frase", sp["frase"], ""],
        ["Probabilidades", probs, ""],
        ["Valor esperado (beta de la hoja / propuesta)", f"{usd(r['valor_esperado_beta_hoja'])} / {usd(r['valor_esperado_beta_prop'])}", ""],
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
    return "\n".join(md), "".join(ht)


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
