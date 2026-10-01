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
    python scripts/damodaran_stories.py CELH [ADBE ...] [--offline]
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
    los años 1-5), m (margen objetivo), wacc, s2c (años 1-5), roic (ROIC después del año 10; 0 = costo de capital) y
    tg (crecimiento terminal propio). Con detalle=True devuelve el puente completo (flujos, terminal, patrimonio)."""
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
          "if(k.tg!=null){if(i.dcfFinanciero)i.dcfFinanciero.terminalGrowth=k.tg;else i.terminalGrowth=k.tg;}"
          "const margin=k.m!=null?k.m:(i.dcfFinanciero?i.dcfFinanciero.roeBase:i.marginBase);"
          "if(k.detalle){const d=c.runDCFDetalle(i,i.growthBase,margin,i.growthY1Base,i.marginY1Base);"
          "const f=i.dcfFinanciero,fl=d.fcff||d.fcfe,disc=[1];for(let n=1;n<=10;n++)disc[n]=disc[n-1]/(1+d.wacc[n]);"
          "let pv=0;for(let n=1;n<=10;n++)pv+=fl[n]*disc[n];"
          "const wT=f?f.terminalKe:(typeof i.terminalWacc==='number'?i.terminalWacc:i.riskFreeRate+i.matureMarketERP);"
          "const gT=f?f.terminalGrowth:(typeof i.terminalGrowth==='number'?i.terminalGrowth:i.riskFreeRate);"
          "return {v:d.valuePerShare,pvFlujos:pv,pvTerminal:d.terminalValue*disc[10],valorTerminal:d.terminalValue,"
          "activosOperativos:d.valueOpAssets,patrimonio:d.equityValue,ingresos:d.revenue||null,utilidad:d.netIncome||null,"
          "nopat:d.ebit1t||null,reinversion:d.reinvestment,flujo:fl,tasa:d.wacc,crecimiento:d.growth,margen:d.margin||d.roe,"
          "tasaTerminal:wT,gTerminal:gT,roicTerminal:f?null:(i.roicTerminal>0?i.roicTerminal:wT),"
          "caja:i.cash,deuda:i.debt,minoritarios:i.minorityInterests||0,noOperativos:i.nonOperatingAssets||0,"
          "opciones:i.optionsValue||0,acciones:i.shares0,probFracaso:i.probFailure||0,nol0:i.nol0||0,"
          "impuestoEf:i.taxEffective,impuestoMarg:i.taxMarginal,s2c:i.salesToCapital,s2c2:i.salesToCapital2,"
          "rezago0:i.reinvestLag===0,convergencia:i.convergenceYear,wacc0:i.wacc,margenY1:i.marginY1Base};}"
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

    def value(g, m, beta=None, s2c_=None, roic=None, anios=None, tg=None, detalle=False):
        k = {"m": m}
        if tg is not None:
            k["tg"] = tg
        if detalle:
            k["detalle"] = True
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
    # Crecimiento terminal de la hoja (Valuation output M4; en financieras, el de 'DCF FCFE financiero').
    tg_hoja = inp["dcfFinanciero"]["terminalGrowth"] if inp.get("dcfFinanciero") else (cell("Valuation output", "M4") or rf)
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
        # Crecimiento terminal propio (contrato del 30-sep-2026): la tesis de disrupción se estabiliza sin recuperación;
        # parte del crecimiento de su año 5, sin superar el terminal de la hoja y con piso de 0% nominal si el año 5 es
        # negativo. Las demás historias conservan el terminal de la hoja.
        tg = max(0.0, min(anios[4], tg_hoja)) if h.get("terminal") == "estabilizacion" else None
        tg_uso = tg if tg is not None else tg_hoja
        a610, step = [], (anios[4] - tg_uso) / 5
        for n in range(5):
            a610.append((a610[-1] if a610 else anios[4]) - step)
        historias.append({**h, "cagr": cagr, "rev5": rev5, "mix5": {k: v / rev5 for k, v in revs.items()},
                          "tasa_base": frac_at_least(br, cagr), "anios": anios, "anios6a10": a610,
                          "terminal_growth": tg_uso, "terminal_propio": tg is not None and abs(tg - tg_hoja) > 1e-9,
                          "roic_terminal_usado": roic if roic is not None else inp.get("roicTerminal", 0)})
        # Cada historia es un DCF completo con la estructura de la hoja (crecimiento año a año, convergencia del
        # margen, impuestos, sales-to-capital por tramo, deuda y caja): el valor esperado es su promedio ponderado.
        cases += [value(None, h["margen"], None, s2, roic, anios, tg, detalle=True),
                  value(None, h["margen"], beta_prop, s2, roic, anios, tg)]
    vals = run_exact(grid, cases)
    for i, h in enumerate(historias):
        h["detalle"] = vals[2 * i]
        h["valor_beta_hoja"], h["valor_beta_prop"] = vals[2 * i]["v"], vals[2 * i + 1]
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

    seg_rev0 = {k: v * scale for k, v in segs.items()}
    return {"ticker": tk, "fecha": spec.get("fecha") or dt.date.today().isoformat(), "spec": spec,
            "mos": rec.get("mos"), "tg_hoja": tg_hoja, "segmentos_ltm": seg_rev0,
            "supuestos": sup, "financiero": financiero, "dcf_sin_exceso": sin_exceso,
            "precio": price, "dcf_base": dcf, "g_ref": g_ref, "m_base": m_base, "s2c": s2c, "wacc": wacc0,
            "beta_hoja": beta_hoja, "beta_bu": beta_bu, "beta_prop": beta_prop, "industria": industria,
            "bu_sector": bu, "rf": rf, "erp": erp, "tasas_base": br, "historias": historias,
            "valor_esperado_beta_hoja": ev_h, "valor_esperado_beta_prop": ev_p, "betas": betas_tab,
            "sensibilidad": sens, "inverso": inverso, "ingresos_ltm": rev0}


# ---------------------------------------------------------------- contrato de escenarios (30-sep-2026)
def mn(v, nd=0):
    """Millones con separador de miles."""
    return es(v, nd)


def letras(hs, pred):
    return "/".join(h["id"] for h in hs if pred(h))


def agrupa(hs, f):
    """«A/B/D: 4,99%; C: 2,0%» agrupando las historias con el mismo texto."""
    grupos = {}
    for h in hs:
        grupos.setdefault(f(h), []).append(h["id"])
    return "; ".join(f"{'/'.join(ids)}: {v}" for v, ids in grupos.items())


def prob_frase(sp: dict, letra: str) -> str:
    """Frase de prob_texto que describe la historia (sin «X (nn%) es»)."""
    import re
    t = re.sub(r"\s*En las historias de erosión \([^)]*\)[^.]*\.", "", sp.get("prob_texto", ""))
    partes = re.split(r"(?<=\.)\s+(?=[A-D] (?:\(|es ))", t)
    for x in partes:
        if x.startswith(f"{letra} ("):
            x = re.sub(rf"^{letra} \(\d+%\)\s*", "", x)
            return x[:1].upper() + x[1:]
        if x.startswith(f"{letra} es "):
            return x[2:3].upper() + x[3:]
    return ""


def origen_calculo(r: dict, W) -> None:
    sp, hs, tk = r["spec"], r["historias"], r["ticker"]
    fin = r.get("financiero")
    A = next(h for h in hs if h["id"] == "A")
    dA = A["detalle"]
    ve = r["valor_esperado_beta_hoja"]
    W.h3("De dónde sale el cálculo: de la historia al valor por acción", f"{tk.lower()}-origen-calculo")
    W.p(f"El valor principal de {usd(ve)} se obtiene ejecutando cuatro DCF completos de diez años más valor terminal y "
        "ponderándolos por sus probabilidades. Cada historia tiene su propia trayectoria de "
        f"{'beneficios' if fin else 'ventas'}, {'ROE' if fin else 'margen'} objetivo, crecimiento terminal y retorno terminal. "
        f"No se obtiene aplicando descuentos al antiguo Base de {usd(r['dcf_base'])} ni mezclando el DCF con múltiplos. "
        f"La historia central A vale {usd(A['valor_beta_hoja'])}; «central» y «esperado» son conceptos distintos.")

    W.h4("1. Datos de partida y origen de los supuestos")
    segs = r["segmentos_ltm"]
    tg_txt = agrupa(hs, lambda h: pct(h["terminal_growth"], 2))
    propios = [h for h in hs if h.get("terminal_propio")]
    tg_origen = ("Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian."
                 if not fin else "Terminal de la hoja («DCF FCFE financiero» B5) en las historias que no lo cambian.")
    for h in propios:
        tg_origen += (f" {h['id']} se estabiliza sin recuperarse: " +
                      (f"mantiene su crecimiento del año 5 ({pct(h['terminal_growth'], 2)}) en los años 6–10 y en perpetuidad, en lugar "
                       "de subir al terminal de la hoja" if abs(h["anios"][4] - h["terminal_growth"]) < 1e-9 else
                       f"parte de su crecimiento del año 5 ({pct(h['anios'][4])}) y converge a {pct(h['terminal_growth'], 2)} en el año 10") +
                      (" (piso de 0% nominal: el negocio residual deja de achicarse, lo que en términos reales sigue siendo contracción)"
                       if h["anios"][4] < 0 else "") + ".")
    if propios:
        tg_origen += " Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa."
    rows = []
    if fin:
        rows += [["Utilidad neta base", f"US${mn(dA['utilidad'][0])} millones", "«DCF FCFE financiero» B3: utilidad LTM del año base."],
                 ["ROE objetivo", agrupa(hs, lambda h: pct(h["margen"], 1)), "Años 1–5 al ROE de la historia; converge al Ke terminal en los años 6–10."],
                 ["Descuento", f"Ke {pct(dA['tasa'][1], 2)} → {pct(dA['tasaTerminal'], 2)}",
                  f"Costo del patrimonio de la hoja; tasa libre de riesgo {pct(r['rf'], 2)}, beta {es(r['beta_hoja'])}, ERP {pct(r['erp'], 2)}. Igual en las cuatro historias."]]
    else:
        puente = " + ".join(mn(v) for v in segs.values())
        rows += [["Ingresos LTM", f"US${mn(r['ingresos_ltm'])} millones",
                  "Input sheet B12: últimos doce meses de los estados financieros (ver fuentes)." +
                  (f" Por segmentos: {puente} = {mn(r['ingresos_ltm'])}." if len(segs) > 1 else "")],
                 ["Margen inicial del DCF", f"{pct(dA['margenY1'])} en año 1",
                  f"Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año {es(dA['convergencia'], 0)} (Input sheet B31)."],
                 ["Impuesto", f"{pct(dA['impuestoEf'], 2)} en años 1–5; {pct(dA['impuestoMarg'], 2)} en terminal",
                  "Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10." +
                  (f" Pérdidas fiscales acumuladas de US${mn(dA['nol0'])} millones protegen la utilidad hasta agotarse." if dA["nol0"] else
                   " No hay pérdidas fiscales iniciales.")],
                 ["Descuento", f"WACC {pct(dA['wacc0'], 2)} → {pct(dA['tasaTerminal'], 2)}",
                  f"Tasa libre de riesgo {pct(r['rf'], 2)}, beta {es(r['beta_hoja'])}, ERP {pct(r['erp'], 2)}. Constante en años 1–5 y "
                  "converge linealmente en los años 6–10. Es la misma en las cuatro historias."],
                 ["Ventas/capital", f"{es(dA['s2c'], 2)}x en años 1–5; {es(dA['s2c2'], 2)}x en años 6–10",
                  "Input sheet B32/B33: hipótesis del analista, no datos reportados." +
                  "".join(f" {h['id']} usa {es(h['s2c'], 2)}x en años 1–5." for h in hs if h.get("s2c"))]]
    rows.append(["Crecimiento perpetuo", tg_txt, tg_origen])
    if not fin:
        rt = lambda h: pct(h["detalle"]["roicTerminal"], 2) + (" (= WACC terminal)" if abs(h["detalle"]["roicTerminal"] - h["detalle"]["tasaTerminal"]) < 1e-9 else "")  # noqa: E731
        moat = (json.loads((_ROOT / "reference" / "moat_2026-09-30.json").read_text())["empresas"]).get(tk) or {}
        rows.append(["ROIC terminal", agrupa(hs, rt),
                     f"Criterio de ventaja competitiva ({moat.get('ventaja', 'sin clasificar')}). Las historias de erosión igualan el "
                     "retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre."])
        extra = [(dA["noOperativos"], "activos no operativos"), (dA["minoritarios"], "minoritarios"), (dA["opciones"], "opciones")]
        W_extra = "".join(f"; {n} {mn(v)}" for v, n in extra if v)
        rows.append(["Puente al patrimonio", f"Caja {mn(dA['caja'])}; deuda {mn(dA['deuda'])}{W_extra}; acciones {es(dA['acciones'], 1)} millones",
                     "Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución." +
                     (f" Probabilidad de fracaso {pct(dA['probFracaso'], 0)} (B24)." if dA["probFracaso"] else "")])
    else:
        rows.append(["Acciones", f"{es(dA['acciones'], 1)} millones", "Valuation output B34. En FCFE no se resta deuda: el flujo ya es del accionista."])
    W.tab(["Entrada", "Valor usado", "Origen y tratamiento"], rows)

    if not fin:
        W.h4("2. Cómo se convierte cada historia en ingresos")
        W.p("Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los "
            "segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del "
            "analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el "
            "crecimiento converge linealmente al terminal de cada historia.")
        terms = " + ".join(f"{mn(v, 0)} × {es(1 + A['crec'].get(k, [0] * 5)[0], 2)}" for k, v in segs.items())
        rev = dA["ingresos"]
        W.p(f"Ejemplo A, año 1: {terms} = US${mn(rev[1], 2)} millones. Frente a {mn(r['ingresos_ltm'])}, el crecimiento consolidado es "
            f"{pct(rev[1] / rev[0] - 1, 2)}. En los años 2–5 es " + ", ".join(pct(g, 2) for g in A["anios"][1:]) +
            f"; las ventas del año 5 son US${mn(rev[5], 2)} millones. El {pct(A['cagr'])} de la tabla es el crecimiento anual "
            f"compuesto de los cinco años: ({mn(rev[5], 2)} / {mn(rev[0])})^(1/5) − 1; no se usa como tasa constante.")

        W.h4("3. Del ingreso al flujo libre y su valor presente")
        lag = "(ventasₜ − ventasₜ₋₁) / ventas-capital: financia el crecimiento del mismo año" if dA["rezago0"] else \
            "(ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente"
        W.p(f"NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es {lag}. FCFFₜ = NOPATₜ − "
            "reinversiónₜ. No se resta además el capex como una segunda reinversión.")
        W.p(f"En A, año 1: NOPAT = {mn(rev[1], 2)} × {pct(dA['margen'][1], 2)} × (1 − {pct(dA['impuestoEf'], 2)}) = "
            f"US${mn(dA['nopat'][1], 2)} millones" + (" (con el escudo de las pérdidas fiscales acumuladas)" if dA["nol0"] else "") +
            f". La reinversión es US${mn(dA['reinversion'][1], 2)} millones y el FCFF es US${mn(dA['flujo'][1], 2)} millones. "
            "Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].")
        tasas = "; ".join(f"{h['id']}, {pct(h['detalle']['gTerminal'] / h['detalle']['roicTerminal'], 1)} "
                          f"({pct(h['detalle']['gTerminal'], 2)} / {pct(h['detalle']['roicTerminal'], 2)})" for h in hs)
        W.p(f"En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / "
            f"(WACC terminal − g), con WACC terminal {pct(dA['tasaTerminal'], 2)}. Reinversión terminal sobre el NOPAT: {tasas}. "
            "Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.")
    else:
        W.h4("2. De la utilidad al flujo del accionista")
        W.p(f"Utilidadₜ = utilidadₜ₋₁ × (1 + crecimientoₜ). Reinversión patrimonial = utilidad × crecimiento / ROE; FCFE = utilidad − "
            f"reinversión. En A, año 1: utilidad US${mn(dA['utilidad'][1], 2)} millones, reinversión US${mn(dA['reinversion'][1], 2)} "
            f"millones y FCFE US${mn(dA['flujo'][1], 2)} millones. Se descuenta al costo del patrimonio; en perpetuidad, "
            "FCFE₁₁ = utilidad₁₁ × (1 − g / Ke terminal) y valor terminal = FCFE₁₁ / (Ke terminal − g). No se resta deuda.")

    trayectorias(r, W, f"{3 if fin else 4}. Trayectoria anual de cada historia")

    W.h4(f"{4 if fin else 5}. Puente numérico de los cuatro DCF")
    W.p(f"Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.")
    flujo = "FCFE" if fin else "FCFF"
    rows = [[h["id"], mn(h["detalle"]["pvFlujos"], 2), mn(h["detalle"]["pvTerminal"], 2)] +
            ([] if fin else [mn(h["detalle"]["activosOperativos"], 2)]) + [mn(h["detalle"]["patrimonio"], 2), es(h["valor_beta_hoja"])]
            for h in hs]
    W.tab(["Historia", f"VP {flujo} años 1–10", "VP terminal"] + ([] if fin else ["Activos operativos"]) +
          ["Patrimonio" + ("" if fin else ", tras caja y deuda"), "DCF/acción"], rows, ["l"] + ["r"] * (4 if fin else 5))
    if fin:
        W.p(f"Ejemplo A: ({mn(dA['pvFlujos'], 2)} + {mn(dA['pvTerminal'], 2)}) / {es(dA['acciones'], 1)} = {usd(A['valor_beta_hoja'])} por acción.")
    else:
        signos = [(dA["caja"], "+"), (dA["noOperativos"], "+"), (dA["deuda"], "−"), (dA["minoritarios"], "−"), (dA["opciones"], "−")]
        ajustes = "".join(f" {sg} {mn(v)}" for v, sg in signos if v)
        fr = (f"[{mn(dA['activosOperativos'], 2)}" if dA["probFracaso"] else f"({mn(dA['pvFlujos'], 2)} + {mn(dA['pvTerminal'], 2)}")
        cierre = "]" if dA["probFracaso"] else ")"
        W.p(f"Ejemplo A: {fr}{ajustes}{cierre} / {es(dA['acciones'], 1)} = {usd(A['valor_beta_hoja'])} por acción. El terminal "
            f"representa {pct(dA['pvTerminal'] / (dA['pvFlujos'] + dA['pvTerminal']))} del valor operativo de A: el resultado depende "
            "materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente." +
            (f" Los activos operativos ya descuentan la probabilidad de fracaso de {pct(dA['probFracaso'], 0)}." if dA["probFracaso"] else ""))

    W.h4(f"{5 if fin else 6}. Valor esperado, probabilidades y margen de seguridad")
    W.p("Las probabilidades " + " / ".join(pct(h["prob"], 0) for h in hs) + " son juicio del analista (ver «Historias "
        "cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos "
        "discutibles y revisables, no como precisión empírica.")
    W.p("Valor esperado = " + " + ".join(f"{es(h['prob'], 2)} × {es(h['valor_beta_hoja'], 6)}" for h in hs) +
        f" = US${es(ve, 6)} ≈ {usd(ve)}. Los aportes son " + " + ".join(usd(h["prob"] * h["valor_beta_hoja"]) for h in hs) + " por acción.")
    mos = r.get("mos")
    if isinstance(mos, (int, float)):
        W.p(f"Precio con MOS = valor esperado × (1 − {pct(mos, 0)}) = {es(ve, 6)} × {es(1 - mos, 2)} = US${es(ve * (1 - mos), 6)} ≈ "
            f"{usd(ve * (1 - mos))}. El {pct(mos, 0)} es la política de margen de seguridad del analista para este tipo de empresa; "
            "no lo estima el DCF. No se aplica al antiguo Base ni a la historia central A.")
    W.p("Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; central H11; rango H12:H13; "
        "MOS H14. Los DCF completos empiezan en las filas 22 (A), 46 (B), 70 (C) y 94 (D); sus valores por acción están en "
        "B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia "
        "verifica la aritmética, no la validez económica de los supuestos.")


def trayectorias(r: dict, W, titulo: str) -> None:
    """Tabla año por año (1-10 y perpetuidad) de cada historia: lo que la hoja calcula en «Escenarios e historias»."""
    fin = r.get("financiero")
    W.h4(titulo)
    W.p("Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en «Escenarios e "
        "historias»: " + ("utilidad, crecimiento, ROE, reinversión patrimonial, flujo al accionista (FCFE), costo del patrimonio "
                          "y su valor presente." if fin else
                          "ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente.") +
        " Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el "
        "factor del año 10).")
    for h in r["historias"]:
        d = h["detalle"]
        base = d["utilidad"] if fin else d["ingresos"]
        big = max(abs(x) for x in base[1:11]) >= 10000
        nd = 0 if big else 1
        rows = []
        for y in range(1, 12):
            t = y == 11
            g = d["gTerminal"] if t else d["crecimiento"][y]
            if fin:
                ni = base[10] * (1 + g) if t else base[y]
                roe = d["tasaTerminal"] if t else d["margen"][y]
                reinv = ni * g / d["tasaTerminal"] if t else d["reinversion"][y]
                fl = ni - reinv
                rows.append(["Terminal" if t else str(y), es(ni, nd), pct(g), pct(roe), es(reinv, nd), es(fl, nd),
                             pct(d["tasaTerminal"] if t else d["tasa"][y]), "—" if t else es(d["flujo"][y] / _acum(d["tasa"], y), nd)])
            else:
                rev = base[11] if t else base[y]
                m = d["margen"][10] if t else d["margen"][y]
                nop = rev * m * (1 - d["impuestoMarg"]) if t else d["nopat"][y]
                reinv = nop * g / d["roicTerminal"] if t else d["reinversion"][y]
                fl = nop - reinv
                rows.append(["Terminal" if t else str(y), es(rev, nd), pct(g), pct(m), es(nop, nd), es(reinv, nd), es(fl, nd),
                             pct(d["tasaTerminal"] if t else d["tasa"][y]), "—" if t else es(d["flujo"][y] / _acum(d["tasa"], y), nd)])
        nom = h["nombre"] + (f": {h['descripcion']}" if h.get("descripcion") else "")
        W.p(f"**{nom}** — probabilidad {pct(h['prob'], 0)}; valor terminal {es(d['valorTerminal'], nd)} (VP {es(d['pvTerminal'], nd)}); "
            f"DCF {usd(h['valor_beta_hoja'])} por acción.")
        if fin:
            W.tab(["Año", "Utilidad", "Crecimiento", "ROE", "Reinversión", "FCFE", "Ke", "VP del FCFE"], rows, ["l"] + ["r"] * 7)
        else:
            W.tab(["Año", "Ingresos", "Crecimiento", "Margen", "NOPAT", "Reinversión", "FCFF", "WACC", "VP del FCFF"], rows,
                  ["l"] + ["r"] * 8)


def _acum(tasas, y):
    f = 1.0
    for n in range(1, y + 1):
        f *= 1 + tasas[n]
    return f


def low(t: str) -> str:
    """Minúscula inicial salvo siglas (EBITDA, ARR, ROE)."""
    return t[:1].lower() + t[1:] if len(t) > 1 and not t[1].isupper() else t


TITULO_TESIS = {"A": "A · Tesis base", "B": "B · Tesis conservadora", "C": "C · Tesis de disrupción · Deterioro de los fundamentales",
                "D": "D · Tesis optimista"}


def cuatro_tesis(r: dict, W) -> None:
    sp, hs = r["spec"], r["historias"]
    fin = r.get("financiero")
    A = next(h for h in hs if h["id"] == "A")
    segs = list(sp["segmentos"].keys())
    ind = sp.get("indicadores") or []
    W.h3("Las cuatro tesis: base, conservadora, disrupción y optimista")
    W.p(f"Estas etiquetas describen las historias A–D activas. La tesis base es A, con un DCF de {usd(A['valor_beta_hoja'])}; el "
        f"valor esperado de {usd(r['valor_esperado_beta_hoja'])} combina las cuatro tesis con sus probabilidades. La antigua "
        "calibración C/B/O de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no "
        "presupone IA ni quiebra.")
    for h in hs:
        desc = h.get("descripcion") or h["nombre"].split(" · ", 1)[-1]
        W.h4(f"{TITULO_TESIS[h['id']]}: {desc}")
        frase = prob_frase(sp, h["id"])
        if frase:
            W.p("**Qué plantea.** " + frase)
        crec = ("; ".join(f"{k} crece " + ", ".join(es(x * 100, 0) + "%" for x in h["crec"].get(k, [0] * 5)) for k in segs)
                if len(segs) > 1 else ("Crece " + ", ".join(es(x * 100, 0) + "%" for x in h["crec"][segs[0]])))
        d = h["detalle"]
        roic = "" if fin else (" El ROIC terminal es " + (f"el costo de capital ({pct(d['roicTerminal'], 2)})" if abs(d["roicTerminal"] - d["tasaTerminal"]) < 1e-9
                                                         else pct(d["roicTerminal"], 1)) + ".")
        tg = (f" El crecimiento terminal es {pct(h['terminal_growth'], 2)}" +
              ((": se mantiene el crecimiento del año 5, sin recuperación." if abs(h["anios"][4] - h["terminal_growth"]) < 1e-9 else
                f": los años 6–10 pasan de {pct(h['anios'][4])} a ese nivel, sin recuperación.") if h.get("terminal_propio") else ", el de la hoja."))
        W.p(f"**Traducción al modelo.** {crec}. El crecimiento anual compuesto de cinco años es {pct(h['cagr'])}; el "
            f"{'ROE' if fin else 'margen operativo'} objetivo es {pct(h['margen'], 1)}.{roic}{tg} Probabilidad: {pct(h['prob'], 0)}; "
            f"DCF: {usd(h['valor_beta_hoja'])} por acción.")
        if ind:
            if h["id"] == "A":
                c = ("Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (" +
                     "; ".join(f"{low(x[0])}: {x[1]}" for x in ind[:3]) + "). Pierde peso si cruzan cualquiera de los umbrales "
                     "de la tabla de indicadores.")
            elif h["id"] == "D":
                c = "La confirmarían: " + "; ".join(f"{low(x[0])}: {low(x[2])}" for x in ind[:4]) + "."
            else:
                c = (("La apoyarían: " if h["id"] == "B" else "La apoyaría, con más intensidad y duración que B: ") +
                     "; ".join(f"{low(x[0])}: {low(x[3])}" for x in ind[:4]) + ".")
            W.p("**Cómo contrastarla.** " + c)
    iguales = "la misma tasa de descuento" + ("" if fin else " y la misma estructura de impuestos y deuda")
    tgs = agrupa(hs, lambda h: pct(h["terminal_growth"], 2))
    orden = sorted(hs, key=lambda h: h["valor_beta_hoja"])
    sev = [h["id"] for h in orden]
    nota_orden = "" if sev == ["C", "B", "A", "D"] else (
        f" El orden de los valores ({' < '.join(sev)}) no sigue exactamente la severidad de las tesis: la diferencia sale de "
        "los supuestos de cada historia (crecimiento, margen, reinversión y terminal), no de un error de cálculo.")
    W.p(f"**Reglas comunes.** Los cuatro DCF usan {iguales}. Crecimiento terminal: {tgs}. Las diferencias proceden de "
        f"{'beneficios' if fin else 'ventas'}, {'ROE' if fin else 'margen'}{'' if fin else ', crecimiento terminal y ROIC terminal'}"
        f"{' y crecimiento terminal' if fin else ''}. Las "
        "probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se "
        "separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual." + nota_orden)


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

    def h3(t, ident=None):
        md.append(f"\n### {t}\n")
        attr = f' id="{ident}"' if ident else ""
        ht.append(f"<h3{attr}>{html.escape(t)}</h3>")

    def h4(t):
        md.append(f"\n#### {t}\n")
        ht.append(f"<h4>{html.escape(t)}</h4>")

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

    hs = r["historias"]
    ve, mos = r["valor_esperado_beta_hoja"], r.get("mos")
    central = next(h for h in hs if h.get("id") == "A")
    lo_h, hi_h = min(h["valor_beta_hoja"] for h in hs), max(h["valor_beta_hoja"] for h in hs)
    rango = f"US${es(lo_h)}–{es(hi_h)}"
    mos_txt = (f" El MOS {pct(mos, 0)} se aplica al esperado: {usd(ve * (1 - mos))}." if isinstance(mos, (int, float)) else "")
    p(f"**Escenarios e historias unificados:** A, B, C y D son los cuatro escenarios DCF activos. La cifra principal es el "
      f"valor intrínseco esperado {usd(ve)}; la historia central A vale {usd(central['valor_beta_hoja'])} y el rango es "
      f"{rango}.{mos_txt} El antiguo caso Base de la hoja ({usd(r['dcf_base'])}) se conserva solo como calibración técnica; "
      "no es el DCF de la historia central A. Los múltiplos y su mezcla son lecturas auxiliares con sus propios supuestos.")
    p("Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, "
      "piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el "
      f"motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de {usd(r['dcf_base'])} por acción): solo cambian el "
      "crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de "
      "la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el "
      "promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». "
      "Los múltiplos son precio relativo y se comentan en otras secciones.")

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
        h3("Calibración técnica anterior C/B/O (referencia auxiliar)")
        tab(["Supuesto", "Conservador", "Base", "Optimista"],
            [[lab] + [pct(su.get(k + s_)) for s_ in ("Cons", "Base", "Opt")] for lab, k in (
                ("Crecimiento año 1", "growthY1"), ("Crecimiento años 2–5", "growth"),
                ("Margen año 1 (base ajustada del modelo)", "marginY1"), ("Margen objetivo", "margin"))],
            ["l", "r", "r", "r"])
        p(f"Ventas/capital: {es(su.get('salesToCapital'), 1)}x en años 1–5 y {es(su.get('salesToCapital2'), 1)}x en 6–10. "
          f"WACC: {pct(su.get('wacc'))}. Ke: {pct(su.get('costoPatrimonio'))}. Impuesto efectivo: {pct(su.get('taxEffective'))}. "
          f"Convergencia: {es(su.get('convergenceYear'), 0)} años. Estos parámetros son escenarios del analista, no cifras reportadas. "
          "Los casos Conservador, Base y Optimista de la hoja ya no son escenarios activos: sirven de calibración y de supuestos "
          "auxiliares de múltiplos. No confundir el antiguo Base con la historia A.")
    moat = (json.loads((_ROOT / "reference" / "moat_2026-09-30.json").read_text())["empresas"]).get(r["ticker"])
    if moat and not r.get("financiero") and r.get("dcf_sin_exceso") is not None:
        rt = moat.get("roic_terminal")
        h3("Ventaja competitiva y ROIC terminal: comprobación")
        tab(["Ventaja (criterio Damodaran)", "ROIC actual (modelo)", "ROIC de la industria (Damodaran)", "Costo de capital terminal",
             "ROIC terminal usado", "DCF técnico anterior", "DCF con ROIC terminal = costo de capital"],
            [[moat["ventaja"].capitalize(), pct(moat["roic_actual"]), pct(moat["roic_industria"]) if moat.get("roic_industria") else "No disponible",
              pct(moat["costo_capital_terminal"]), pct(rt) if rt else "= costo de capital", usd(r["dcf_base"]), usd(r["dcf_sin_exceso"])]],
            ["l", "r", "r", "r", "r", "r", "r"])
        p(f"Fuentes de ventaja: {moat['fuentes']}. Evidencia: {moat['evidencia']}. Criterio (Damodaran, *Investment Valuation*, "
          "cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el "
          "promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre "
          "ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del "
          "motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.")

    from types import SimpleNamespace
    W = SimpleNamespace(h3=h3, h4=h4, p=p, tab=tab)
    origen_calculo(r, W)
    cuatro_tesis(r, W)

    h3("Historias cuantificadas y valor esperado")
    segs = list(sp["segmentos"].keys())
    same = abs(r["beta_prop"] - r["beta_hoja"]) < 0.005  # la hoja ya usa la beta propuesta: una sola columna
    con_roic = any((h.get("roic_terminal_usado") or 0) > 0 for h in r["historias"])
    roic_txt = lambda h: (pct(h["roic_terminal_usado"]) if (h.get("roic_terminal_usado") or 0) > 0 else "= costo de capital")  # noqa: E731
    rows = []
    for h in r["historias"]:
        crec = "; ".join(f"{k}: " + ", ".join(es(x * 100, 0) + "%" for x in h["crec"].get(k, [0] * 5)) for k in segs) if len(segs) > 1 else \
            ", ".join(es(x * 100, 0) + "%" for x in h["crec"][segs[0]])
        nom = h["nombre"] + (f": {h['descripcion']}" if h.get("descripcion") else "")
        rows.append([f"**{nom}**", pct(h["prob"], 0), crec, pct(h["cagr"]), pct(h["margen"], 0),
                     es(h.get("s2c", r["s2c"]), 1)] + ([roic_txt(h)] if con_roic else []) + [pct(h["terminal_growth"], 2)] +
                    [usd(h["valor_beta_hoja"])] + ([] if same else [usd(h["valor_beta_prop"])]))
    rows.append(["**Valor esperado**", "100%", "", "", "", ""] + ([""] if con_roic else []) + [""] + [f"**{usd(r['valor_esperado_beta_hoja'])}**"] +
                ([] if same else [f"**{usd(r['valor_esperado_beta_prop'])}**"]))
    tab(["Historia", "Probabilidad", "Crecimiento por segmento (años 1-5)", "CAGR de ingresos del grupo (años 1–5)",
         "Margen objetivo", "Sales-to-capital"] + (["ROIC después del año 10"] if con_roic else []) + ["Crecimiento terminal"] +
        [f"Valor/acción (beta {es(r['beta_hoja'])})"] +
        ([] if same else [f"Valor/acción (beta {es(r['beta_prop'])})"]), rows,
        ["l", "r", "l", "r", "r", "r"] + (["r"] if con_roic else []) + ["r", "r"] + ([] if same else ["r"]))
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
        ["Valor esperado (valor principal)" + ("" if same else " (beta de la hoja / propuesta)"), usd(r['valor_esperado_beta_hoja']) + ("" if same else f" / {usd(r['valor_esperado_beta_prop'])}"), ""],
        ["DCF base hoy (historia A)", usd(central["valor_beta_hoja"]), ""],
        ["Precio con MOS sobre el valor esperado", usd(ve * (1 - mos)) + f" (MOS {pct(mos, 0)})" if isinstance(mos, (int, float)) else "—", ""],
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
    # El antiguo caso Base de la hoja es ahora calibración técnica: no se confunde con la historia A.
    out_md, out_ht = out_md.replace("DCF Base", "DCF técnico anterior"), out_ht.replace("DCF Base", "DCF técnico anterior")
    if r.get("financiero"):  # DCF de flujo al accionista: ROE en lugar de margen operativo
        for x, y in (("Margen objetivo", "ROE objetivo"), ("Sales-to-capital", "Reinversión patrimonial"),
                     ("crecimiento anual de ingresos", "crecimiento anual de beneficios"), ("margen operativo objetivo", "ROE objetivo")):
            out_md, out_ht = out_md.replace(x, y), out_ht.replace(x, y)
    return out_md, out_ht


def main(tickers):
    offline = "--offline" in tickers  # vuelve a redactar desde <T>_resultado.json, sin leer la hoja
    for tk in [t for t in tickers if not t.startswith("--")]:
        if offline:
            r = json.loads((REF / f"{tk}_resultado.json").read_text())
            r["spec"] = json.loads((REF / f"{tk}.json").read_text())
        else:
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
