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
import re
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
    if not isinstance(v, (int, float)):
        return "—"
    t = es(v * 100, nd)
    return ("−" + t[1:] if t.startswith("-") else t) + "%"


def usd(v):
    if not isinstance(v, (int, float)):
        return "—"
    return ("−US$" if v < 0 else "US$") + es(abs(v))


# ---------------------------------------------------------------- motor
def run_exact(grid, cases):
    """Valor por acción con el motor exacto (reproduce 'Valuation output'): insumos leídos de la hoja con
    insumosDesdeHoja y, por caso, cambios opcionales: anios (crecimiento de cada año 1-5), g (el mismo para
    los años 1-5), m (margen objetivo), wacc, s2c (años 1-5), roic (ROIC después del año 10; 0 = costo de capital),
    tg (crecimiento terminal propio), dk (suma a la tasa de descuento inicial y terminal: WACC o Ke), s2cf (multiplica
    el ventas/capital de las dos etapas), shf (multiplica las acciones: dilución) y set (sobrescribe insumos del motor). Con detalle=True devuelve el puente completo (flujos, terminal, patrimonio)."""
    js = ("const fs=require('fs'),vm=require('vm');const c={};vm.createContext(c);"
          f"vm.runInContext(fs.readFileSync({json.dumps(str(ENGINE))},'utf8'),c);"
          "const G=JSON.parse(fs.readFileSync(0,'utf8'));"
          "const col=a=>{let n=0;for(const ch of a)n=n*26+ch.charCodeAt(0)-64;return n-1;};"
          "const celda=(h,a)=>{const g=G.grid[h];if(!g)return null;const m=a.match(/^([A-Z]+)(\\d+)$/);const r=g[+m[2]-1];"
          "if(!r)return null;const v=r[col(m[1])];return (v===undefined||v==='')?null:v;};"
          "const base=c.insumosDesdeHoja(celda);"
          "const path=Array.from({length:10},(_,n)=>celda('Valuation output',String.fromCharCode(67+n)+'4'));"
          "if(path.every(v=>typeof v==='number'&&Number.isFinite(v)))base.crecimientoAnios=path;"
          "const out=G.cases.map(k=>{const i=JSON.parse(JSON.stringify(base));"
          "if(k.anios)i.crecimientoAnios=k.anios;else if(k.g!=null)i.crecimientoAnios=[k.g,k.g,k.g,k.g,k.g];"
          "if(k.wacc!=null)i.wacc=k.wacc;if(k.s2c!=null)i.salesToCapital=k.s2c;if(k.roic!=null)i.roicTerminal=k.roic;"
          "if(k.tg!=null){if(i.dcfFinanciero)i.dcfFinanciero.terminalGrowth=k.tg;else i.terminalGrowth=k.tg;}"
          "if(k.dk!=null){if(i.dcfFinanciero){i.costoPatrimonio+=k.dk;i.dcfFinanciero.terminalKe+=k.dk;}"
          "else{const t=typeof i.terminalWacc==='number'?i.terminalWacc:i.riskFreeRate+i.matureMarketERP;i.wacc+=k.dk;i.terminalWacc=t+k.dk;}}"
          "if(k.s2cf!=null){i.salesToCapital*=k.s2cf;i.salesToCapital2*=k.s2cf;}if(k.shf!=null)i.shares0*=k.shf;"
          "if(k.set)Object.assign(i,k.set);"
          "const margin=k.m!=null?k.m:(i.dcfFinanciero?i.dcfFinanciero.roeBase:i.marginBase);"
          "if(k.detalle){const d=c.runDCFDetalle(i,i.growthBase,margin,i.growthY1Base,i.marginY1Base);"
          "const f=i.dcfFinanciero,fl=d.fcff||d.fcfe,disc=[1];for(let n=1;n<=10;n++)disc[n]=disc[n-1]/(1+d.wacc[n]);"
          "let pv=0;for(let n=1;n<=10;n++)pv+=fl[n]*disc[n];"
          "const wT=f?f.terminalKe:(typeof i.terminalWacc==='number'?i.terminalWacc:i.riskFreeRate+i.matureMarketERP);"
          "const gT=f?f.terminalGrowth:(typeof i.terminalGrowth==='number'?i.terminalGrowth:i.riskFreeRate);"
          "return {v:d.valuePerShare,pvFlujos:pv,pvTerminal:d.terminalValue*disc[10],valorTerminal:d.terminalValue,"
          "activosOperativos:d.valueOpAssets,patrimonio:d.equityValue,ingresos:d.revenue||null,utilidad:d.netIncome||null,"
          "nopat:d.ebit1t||null,patrimonioContable:d.bookEquity||null,utilidadTerminal:d.terminalNetIncome||null,reinversion:d.reinvestment,flujo:fl,tasa:d.wacc,crecimiento:d.growth,margen:d.margin||d.roe,"
          "tasaTerminal:wT,gTerminal:gT,roicTerminal:f?null:(i.roicTerminal>0?i.roicTerminal:wT),"
          "caja:i.cash,deuda:i.debt,minoritarios:i.minorityInterests||0,noOperativos:i.nonOperatingAssets||0,"
          "opciones:i.optionsValue||0,preferentes:i.preferredStock||0,acciones:i.shares0,probFracaso:i.probFailure||0,nol0:i.nol0||0,"
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
# Los tramos de The Base Rate Book están en dólares de 2015: las ventas se deflactan con el IPC-U (promedio 2015 =
# 237,017; agosto de 2026 = 334,980, BLS) antes de elegir el tramo (corrección verificada en la auditoría de ADBE).
IPC_2015, IPC_HOY = 237.017, 334.980


def base_rates(revenue_mn: float) -> dict:
    br = json.loads((REF / "base_rates_5y.json").read_text())
    real = revenue_mn * IPC_2015 / IPC_HOY
    name = next(n for lim, n in BUCKETS if real < lim)
    return {"tramo": name, "ventas_2015": real, **br["tamanos"][name], "bins": br["bins"], "fuente": br["fuente"]}


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
    rng = ["'Input sheet'!A1:D80", "'Valuation output'!A1:M140", "'Financials Multiples'!A1:H120",
           "'Resumen de Valoración'!A1:U20", "'Cost of capital worksheet'!A1:C70", "'Descuento de múltiplos'!A1:E40",
           "EVEBITDA!A1:J30", "EVFCFF!A1:J30", "PE!A1:J30", "PFCFE!A1:J30", "POCF!A1:J30"]
    titulos = {w.title for w in sh.worksheets()}
    if 'DCF FCFE financiero' in titulos:
        rng.append("'DCF FCFE financiero'!A1:I62")
    if 'R& D converter' in titulos:
        rng.append("'R& D converter'!A1:H8")
    vr = sh.values_batch_get(rng, params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
    grid = {r.split("!")[0].strip("'"): v.get("values", []) for r, v in zip(rng, vr)}

    def cell(s, a):
        col, row = ord(a[0]) - 65, int(a[1:]) - 1
        g = grid.get(s, [])
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
    recs = glob.glob(str(DATOS / "valoraciones" / f"{tk}-*.json"))
    rec = json.loads(Path(recs[0]).read_text()) if recs else {}
    grid, cell = load_sheet(anc["sheet_id"])
    # Una hoja nueva sin valoración guardada en la app (p. ej. CELHN, CELH desde cero) toma precio y MOS de la hoja.
    price = rec.get("precio") or cell("Input sheet", "D1") or cell("Input sheet", "B23")
    rec.setdefault("mos", cell("Resumen de Valoración", "G4"))
    # DCF de la hoja = 'Valuation output'!B35. Desde el 2-oct-2026 ese bloque calcula la historia Base (antes era el caso
    # técnico Base de la plantilla).
    # 'Descuento de múltiplos'!D38 ya no sirve: desde el 1-oct-2026 apunta a la historia Base de «Escenarios e historias».
    dcf = cell("Valuation output", "B35")
    if cell("DCF FCFE financiero", "A1") == "DCF FCFE financiero":  # financieras: el DCF de la hoja es el FCFE Base
        dcf = cell("DCF FCFE financiero", "B42")
    if not isinstance(dcf, (int, float)):
        dcf = ((rec.get("descuentoMultiples") or {}).get("dcfHoy") or {}).get("base")
    inp = engine_inputs(cell, grid["Financials Multiples"], price)
    m_base = inp["dcfFinanciero"]["roeBase"] if inp.get("dcfFinanciero") else cell("Input sheet", "B30")
    g_vo = [x for x in grid["Valuation output"][3][2:7] if isinstance(x, (int, float))]
    # Hoja nueva: 'Valuation output' toma el crecimiento de «Escenarios e historias», que se arma con este resultado;
    # en la primera pasada (pestaña vacía) la referencia sale de la Input sheet (B27 y B29).
    g_ref = st.mean(g_vo) if g_vo else (cell("Input sheet", "B27") + 4 * cell("Input sheet", "B29")) / 5
    s2c = cell("Input sheet", "B32")
    wacc0 = cell("Input sheet", "B36")
    inp["salesToCapital"] = s2c
    # Referencia de las tablas de sensibilidad y DCF inverso (crecimiento igual en los años 1-5): se calibran contra
    # el DCF de la hoja. Las historias y la tabla de betas no se calibran: el motor reproduce la hoja exactamente.
    ref = run_exact(grid, [{"g": g_ref, "m": m_base}])[0]
    # Control de integridad: el motor sin cambios debe reproducir el DCF propio de la hoja ('Valuation output'!B35).
    motor_tecnico = run_exact(grid, [{}])[0]

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
    # Arrendamientos como deuda (Damodaran): los márgenes de las historias se escriben en base reportada y se llevan a
    # la base ajustada de la hoja (+ ajuste del EBIT / ventas); el ventas/capital propio de una historia incluye el
    # capital arrendado. Ver apply_lease_conversion.py.
    arr = spec.get("arrendamientos") or {}
    dm, kcap = arr.get("margen_pp", 0.0), arr.get("capital_ventas", 0.0)
    for h0 in spec["historias"]:
        h = dict(h0)
        if arr:
            h["margen_reportado"] = h["margen"]
            h["margen"] = h["margen"] + dm
            if h.get("s2c"):
                h["s2c_reportado"] = h["s2c"]
                h["s2c"] = 1 / (1 / h["s2c"] + kcap)
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
        # Años 6-10 propios de la historia (p. ej. vencimiento de patentes, criterio de Damodaran para farmacéuticas):
        # reemplazan la convergencia lineal al terminal y el motor recibe la trayectoria completa de 10 años.
        propio610 = h.get("crec_6a10")
        if propio610:
            a610 = [float(x) for x in propio610]
        historias.append({**h, "cagr": cagr, "rev5": rev5, "mix5": {k: v / rev5 for k, v in revs.items()},
                          "tasa_base": frac_at_least(br, cagr), "anios": anios, "anios6a10": a610, "anios6a10_propios": bool(propio610),
                          "terminal_growth": tg_uso, "terminal_propio": tg is not None and abs(tg - tg_hoja) > 1e-9,
                          "roic_terminal_usado": roic if roic is not None else inp.get("roicTerminal", 0)})
        # Cada historia es un DCF completo con la estructura de la hoja (crecimiento año a año, convergencia del
        # margen, impuestos, sales-to-capital por tramo, deuda y caja): el valor esperado es su promedio ponderado.
        tray = anios + a610 if propio610 else anios
        cases += [value(None, h["margen"], None, s2, roic, tray, tg, detalle=True),
                  value(None, h["margen"], beta_prop, s2, roic, tray, tg)]
    vals = run_exact(grid, cases)
    for i, h in enumerate(historias):
        h["detalle"] = vals[2 * i]
        # Responsabilidad limitada: el patrimonio no vale menos que cero (Damodaran). Se guarda el DCF bruto.
        h["valor_bruto"], h["valor_bruto_prop"] = vals[2 * i]["v"], vals[2 * i + 1]
        h["valor_beta_hoja"], h["valor_beta_prop"] = max(0.0, vals[2 * i]["v"]), max(0.0, vals[2 * i + 1])
    ev_h = sum(h["prob"] * h["valor_beta_hoja"] for h in historias)
    ev_p = sum(h["prob"] * h["valor_beta_prop"] for h in historias)

    # Sensibilidad de la historia Base a cada supuesto material: cada caso es un DCF completo de la Base con un solo
    # supuesto cambiado (no se reescala el resultado). Sirve a la «Justificación de los supuestos».
    iA = next(i for i, h in enumerate(historias) if h["id"] == "A")
    hA, kA = historias[iA], {k: v for k, v in cases[2 * iA].items() if k != "detalle"}
    fin_ = bool(inp.get("dcfFinanciero"))
    variantes = [("margen", -0.02, {"m": hA["margen"] - 0.02}), ("margen", 0.02, {"m": hA["margen"] + 0.02}),
                 ("crecimiento", -0.02, {"anios": [a - 0.02 for a in hA["anios"]]}),
                 ("crecimiento", 0.02, {"anios": [a + 0.02 for a in hA["anios"]]}),
                 ("tasa", -0.01, {"dk": -0.01}), ("tasa", 0.01, {"dk": 0.01}),
                 ("terminal", -0.005, {"tg": hA["terminal_growth"] - 0.005}), ("terminal", 0.005, {"tg": hA["terminal_growth"] + 0.005}),
                 ("acciones", 0.05, {"shf": 1.05})]
    if not fin_:
        variantes += [("s2c", 0.8, {"s2cf": 0.8}), ("s2c", 1.2, {"s2cf": 1.2}), ("roic_cc", 0, {"roic": 0})]
    sv_ = run_exact(grid, [{**kA, **v} for _, _, v in variantes])
    sens_base = {"base": hA["valor_bruto"], "casos": [{"supuesto": n, "cambio": d, "valor": x} for (n, d, _), x in zip(variantes, sv_)]}
    rd_vida = cell("R& D converter", "F7") if "R& D converter" in grid and str(cell("Input sheet", "B17")).lower() == "yes" else None

    # beta: DCF Base con cada beta
    beta_rows = [("Hoja (regresión o la cargada en el libro)", beta_hoja)]
    if beta_bu:
        beta_rows.append((f"Bottom-up del sector ({industria}, reapalancada)", beta_bu))
    if spec.get("riesgo", {}).get("beta_propuesta"):
        beta_rows.append(("Propuesta (sector ajustado por riesgo propio)", beta_prop))
    # Cada beta con la trayectoria completa de la historia Base (crecimiento año a año, margen, ROIC y terminal): así la
    # fila de la beta de la hoja reproduce el DCF Base (antes usaba un crecimiento constante en los años 2-5).
    bv = run_exact(grid, [{**kA, "wacc": wacc_for(b)} for _, b in beta_rows])
    betas_tab = [{"enfoque": n, "beta": b, "ke": rf + b * erp, "wacc": wacc_for(b), "dcf_base": v}
                 for (n, b), v in zip(beta_rows, bv)]

    # sensibilidad
    gs = [g_ref + d for d in (-0.04, -0.02, 0, 0.02, 0.04)]
    ms = [m_base + d for d in (-0.04, -0.02, 0, 0.02, 0.04)]
    sv = run_exact(grid, [value(g, m) for g in gs for m in ms])
    sens = {"g": gs, "m": ms, "v": [[sv[i * 5 + j] for j in range(5)] for i in range(5)],
            "referencia_constante": ref, "criterio": "DCF completo sin factor de calibración; crecimiento constante en años 1–5"}

    # DCF inverso
    inv_m = [m + dm for m in spec["margenes_inverso"]] if spec.get("margenes_inverso") else [m_base, m_base + 0.02]
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
                                   "smoothTerminalCapital", "salesToCapital2", "wacc", "costoPatrimonio", "taxEffective", "convergenceYear",
                                   "terminalWacc", "roicTerminal")}
    sup["salesToCapital"] = s2c
    sin_exceso = None if financiero else run_exact(grid, [{**kA, "roic": 0}])[0]

    seg_rev0 = {k: v * scale for k, v in segs.items()}
    return {"ticker": tk, "fecha": spec.get("fecha") or dt.date.today().isoformat(), "spec": spec,
            "mos": rec.get("mos"), "tg_hoja": tg_hoja, "segmentos_ltm": seg_rev0,
            "supuestos": sup, "financiero": financiero, "dcf_sin_exceso": sin_exceso,
            "precio": price, "dcf_base": dcf, "g_ref": g_ref, "m_base": m_base, "s2c": s2c, "wacc": wacc0,
            "beta_hoja": beta_hoja, "beta_bu": beta_bu, "beta_prop": beta_prop, "industria": industria,
            "bu_sector": bu, "rf": rf, "erp": erp, "tasas_base": br, "historias": historias,
            "valor_esperado_beta_hoja": ev_h, "valor_esperado_beta_prop": ev_p, "betas": betas_tab,
            "sensibilidad": sens, "inverso": inverso, "ingresos_ltm": rev0, "sens_base": sens_base, "rd_vida": rd_vida,
            "rd_ltm": cell("R& D converter", "F8") if rd_vida else None, "motor_tecnico": motor_tecnico}


# ---------------------------------------------------------------- nombres visibles (contrato del 1-oct-2026)
# Las letras A-D son claves internas; en el texto visible las historias se llaman Base, Conservadora, Disrupción y
# Optimista, con el título propio de cada una. La disrupción conserva «Disrupción · Deterioro de los fundamentales».
NOMBRE = {"A": "Base", "B": "Conservadora", "C": "Disrupción", "D": "Optimista"}
_PREFIJO = re.compile(r"^(?:[A-D]|Base|Conservadora|Disrupción|Optimista)\s*·\s*(?:Tesis de disrupción\s*·\s*)?")


def titulo(h: dict) -> str:
    """Título propio de la historia, sin el nombre del escenario («Azure y Copilot sostienen el doble dígito»)."""
    t = _PREFIJO.sub("", h.get("nombre", ""))
    if h["id"] == "C":
        return h.get("descripcion") or ""
    return t


def nombre(h: dict) -> str:
    """«Base · Azure y Copilot…»; «Disrupción · Deterioro de los fundamentales: La demanda…»."""
    if h["id"] == "C":
        return "Disrupción · Deterioro de los fundamentales" + (f": {h['descripcion']}" if h.get("descripcion") else "")
    t = titulo(h)
    return NOMBRE[h["id"]] + (f" · {t}" if t else "")


# ---------------------------------------------------------------- contrato de escenarios (30-sep-2026)
def mn(v, nd=0):
    """Millones con separador de miles."""
    return es(v, nd)


def letras(hs, pred):
    return "/".join(NOMBRE[h["id"]] for h in hs if pred(h))


def agrupa(hs, f):
    """«Base/Conservadora/Optimista: 4,99%; Disrupción: 2,0%» agrupando las historias con el mismo texto."""
    grupos = {}
    for h in hs:
        grupos.setdefault(f(h), []).append(NOMBRE[h["id"]])
    return "; ".join(f"{'/'.join(ids)}: {v}" for v, ids in grupos.items())


def prob_frase(sp: dict, letra: str) -> str:
    """Frase de prob_texto que describe la historia (sin «X (nn%) es»)."""
    t = re.sub(r"\s*En las historias de erosión \([^)]*\)[^.]*\.", "", sp.get("prob_texto", ""))
    nom = NOMBRE[letra]
    partes = re.split(r"(?<=\.)\s+(?=(?:Base|Conservadora|Disrupción|Optimista) (?:\(|es ))", t)
    for x in partes:
        if x.startswith(f"{nom} ("):
            x = re.sub(rf"^{nom} \(\d+%\)\s*", "", x)
            return x[:1].upper() + x[1:]
        if x.startswith(f"{nom} es "):
            x = x[len(nom) + 1:]
            return x[:1].upper() + x[1:]
    return ""


def origen_calculo(r: dict, W) -> None:
    sp, hs, tk = r["spec"], r["historias"], r["ticker"]
    fin = r.get("financiero")
    A = next(h for h in hs if h["id"] == "A")
    dA = A["detalle"]
    ve = r["valor_esperado_beta_hoja"]
    W.h3("De dónde sale el cálculo: de la historia al valor por acción", f"{tk.lower()}-origen-calculo")
    W.p(f"El valor intrínseco principal es el DCF Base: {usd(A['valor_beta_hoja'])} por acción, un DCF completo de diez años más "
        "valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos "
        "(Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es "
        f"{usd(ve)}. Cada historia tiene su propia trayectoria de "
        f"{'beneficios' if fin else 'ventas'}, {'ROE' if fin else 'margen'} objetivo, crecimiento terminal y retorno terminal. "
        + ("Ninguna cifra se obtiene mezclando el DCF con múltiplos." if hoja_historias(r) else
           f"Ninguna cifra se obtiene aplicando descuentos al antiguo caso técnico de la hoja ({usd(r['dcf_base'])}) ni mezclando el "
           "DCF con múltiplos.") + " «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio "
        "de desenlaces con pesos subjetivos.")

    W.h4("1. Datos de partida y origen de los supuestos")
    segs = r["segmentos_ltm"]
    tg_txt = agrupa(hs, lambda h: pct(h["terminal_growth"], 2))
    propios = [h for h in hs if h.get("terminal_propio")]
    tg_origen = ("Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian."
                 if not fin else "Terminal de la hoja («DCF FCFE financiero» B5) en las historias que no lo cambian.")
    for h in propios:
        tg_origen += (f" {NOMBRE[h['id']]} se estabiliza sin recuperarse: " +
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
                  "".join(f" {NOMBRE[h['id']]} usa {es(h['s2c'], 2)}x en años 1–5." for h in hs if h.get("s2c"))]]
    rows.append(["Crecimiento perpetuo", tg_txt, tg_origen])
    if not fin:
        rt = lambda h: pct(h["detalle"]["roicTerminal"], 2) + (" (= WACC terminal)" if abs(h["detalle"]["roicTerminal"] - h["detalle"]["tasaTerminal"]) < 1e-9 else "")  # noqa: E731
        moat = (json.loads((_ROOT / "reference" / "moat_2026-09-30.json").read_text())["empresas"]).get(tk) or {}
        rows.append(["ROIC terminal", agrupa(hs, rt),
                     f"Criterio de ventaja competitiva ({moat.get('ventaja', 'sin clasificar')}). Las historias de erosión igualan el "
                     "retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre."])
        extra = [(dA["noOperativos"], "activos no operativos"), (dA["minoritarios"], "minoritarios"), (dA["opciones"], "opciones"),
                 (dA.get("preferentes", 0), "acciones preferentes")]
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
        W.p(f"Ejemplo Base, año 1: {terms} = US${mn(rev[1], 2)} millones. Frente a {mn(r['ingresos_ltm'])}, el crecimiento consolidado es "
            f"{pct(rev[1] / rev[0] - 1, 2)}. En los años 2–5 es " + ", ".join(pct(g, 2) for g in A["anios"][1:]) +
            f"; las ventas del año 5 son US${mn(rev[5], 2)} millones. El {pct(A['cagr'])} de la tabla es el crecimiento anual "
            f"compuesto de los cinco años: ({mn(rev[5], 2)} / {mn(rev[0])})^(1/5) − 1; no se usa como tasa constante.")

        W.h4("3. Del ingreso al flujo libre y su valor presente")
        lag = "(ventasₜ − ventasₜ₋₁) / ventas-capital: financia el crecimiento del mismo año" if dA["rezago0"] else \
            "(ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente"
        W.p(f"NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es {lag}. FCFFₜ = NOPATₜ − "
            "reinversiónₜ. No se resta además el capex como una segunda reinversión.")
        W.p(f"En la Base, año 1: NOPAT = {mn(rev[1], 2)} × {pct(dA['margen'][1], 2)} × (1 − {pct(dA['impuestoEf'], 2)}) = "
            f"US${mn(dA['nopat'][1], 2)} millones" + (" (con el escudo de las pérdidas fiscales acumuladas)" if dA["nol0"] else "") +
            f". La reinversión es US${mn(dA['reinversion'][1], 2)} millones y el FCFF es {_um2(dA['flujo'][1])} millones. "
            "Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].")
        tasas = "; ".join(f"{NOMBRE[h['id']]}, {pct(h['detalle']['gTerminal'] / h['detalle']['roicTerminal'], 1)} "
                          f"({pct(h['detalle']['gTerminal'], 2)} / {pct(h['detalle']['roicTerminal'], 2)})" for h in hs)
        W.p(f"En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / "
            f"(WACC terminal − g), con WACC terminal {pct(dA['tasaTerminal'], 2)}. Reinversión terminal sobre el NOPAT: {tasas}. "
            "Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.")
    else:
        W.h4("2. De la utilidad al flujo del accionista")
        W.p(f"Utilidadₜ = ROEₜ × patrimonio contableₜ₋₁ (Damodaran, bancos). Reinversión patrimonial = patrimonioₜ₋₁ × crecimientoₜ "
            f"(crecer exige más capital); FCFE = utilidad − reinversión. En la Base, año 1: utilidad US${mn(dA['utilidad'][1], 2)} millones, "
            f"reinversión US${mn(dA['reinversion'][1], 2)} millones y FCFE US${mn(dA['flujo'][1], 2)} millones. Se descuenta al costo del "
            "patrimonio; en perpetuidad el ROE es el Ke terminal, utilidad₁₁ = Ke terminal × patrimonio₁₀, FCFE₁₁ = utilidad₁₁ × "
            "(1 − g / Ke terminal) y valor terminal = FCFE₁₁ / (Ke terminal − g) = patrimonio₁₀. No se resta deuda.")

    trayectorias(r, W, f"{3 if fin else 4}. Trayectoria anual de cada historia")

    W.h4(f"{4 if fin else 5}. Puente numérico de los cuatro DCF")
    W.p(f"Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.")
    flujo = "FCFE" if fin else "FCFF"
    rows = [[NOMBRE[h["id"]], mn(h["detalle"]["pvFlujos"], 2), mn(h["detalle"]["pvTerminal"], 2)] +
            ([] if fin else [mn(h["detalle"]["activosOperativos"], 2)]) + [mn(h["detalle"]["patrimonio"], 2), es(h["valor_beta_hoja"])]
            for h in hs]
    W.tab(["Historia", f"VP {flujo} años 1–10", "VP terminal"] + ([] if fin else ["Activos operativos"]) +
          ["Patrimonio" + ("" if fin else ", tras caja y deuda"), "DCF/acción"], rows, ["l"] + ["r"] * (4 if fin else 5))
    if fin:
        W.p(f"Ejemplo Base: ({mn(dA['pvFlujos'], 2)} + {mn(dA['pvTerminal'], 2)}) / {es(dA['acciones'], 1)} = {usd(A['valor_beta_hoja'])} por acción.")
    else:
        signos = [(dA["caja"], "+"), (dA["noOperativos"], "+"), (dA["deuda"], "−"), (dA["minoritarios"], "−"), (dA["opciones"], "−"),
                  (dA.get("preferentes", 0), "−")]
        ajustes = "".join(f" {sg} {mn(v)}" for v, sg in signos if v)
        fr = (f"[{mn(dA['activosOperativos'], 2)}" if dA["probFracaso"] else f"({mn(dA['pvFlujos'], 2)} + {mn(dA['pvTerminal'], 2)}")
        cierre = "]" if dA["probFracaso"] else ")"
        W.p(f"Ejemplo Base: {fr}{ajustes}{cierre} / {es(dA['acciones'], 1)} = {usd(A['valor_beta_hoja'])} por acción. El terminal "
            f"representa {pct(dA['pvTerminal'] / (dA['pvFlujos'] + dA['pvTerminal']))} del valor operativo de la Base: el resultado depende "
            "materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente." +
            (f" Los activos operativos ya descuentan la probabilidad de fracaso de {pct(dA['probFracaso'], 0)}." if dA["probFracaso"] else ""))

    W.h4(f"{5 if fin else 6}. DCF esperado (complemento), probabilidades y margen de seguridad")
    W.p("Las probabilidades " + " / ".join(pct(h["prob"], 0) for h in hs) + " son juicio del analista (ver «Historias "
        "cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos "
        "discutibles y revisables, no como precisión empírica.")
    W.p("DCF esperado = " + " + ".join(f"{es(h['prob'], 2)} × {es(h['valor_beta_hoja'], 6)}" for h in hs) +
        f" = US${es(ve, 6)} ≈ {usd(ve)}. Los aportes son " + " + ".join(usd(h["prob"] * h["valor_beta_hoja"]) for h in hs) + " por acción.")
    mos = r.get("mos")
    if isinstance(mos, (int, float)):
        W.p(f"Precio con MOS = DCF esperado × (1 − {pct(mos, 0)}) = {es(ve, 6)} × {es(1 - mos, 2)} = US${es(ve * (1 - mos), 6)} ≈ "
            f"{usd(ve * (1 - mos))}. El {pct(mos, 0)} es la política de margen de seguridad del analista para este tipo de empresa; "
            "no lo estima el DCF. Se aplica al esperado, no al DCF Base" +
            ("" if hoja_historias(r) else " ni al antiguo caso técnico de la hoja") +
            ": la jerarquía de presentación (Base primero) no cambia esa fórmula.")
    if not fin:
        W.p("Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas "
            "2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La "
            "pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; "
            "Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro "
            "resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.")
        return
    W.p("Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; Base H11; rango H12:H13; "
        "MOS H14. Los DCF completos empiezan en las filas 22 (Base), 46 (Conservadora), 70 (Disrupción) y 94 (Optimista); sus valores por acción están en "
        "B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia "
        "verifica la aritmética, no la validez económica de los supuestos.")


# ---------------------------------------------------------------- justificación de los supuestos (1-oct-2026)
METODO_HOJA = {"EVEBITDA": "EV/EBITDA", "EVFCFF": "EV/FCFF", "PE": "P/E", "PFCFE": "P/FCFE", "POCF": "P/OCF"}


def _filas_snapshot(rec: dict, patron: str, num) -> dict:
    out = {}
    for hoja, met in METODO_HOJA.items():
        t = ((rec.get("hojas") or {}).get("valoracion") or {}).get(hoja)
        if not t:
            continue
        filas = []
        for tr in re.findall(r"<tr\b[^>]*>[\s\S]*?</tr>", str(t), flags=re.I):
            cs = [re.sub(r"<[^>]*>", "", c).strip() for c in re.findall(r"<t[dh]\b[^>]*>[\s\S]*?</t[dh]>", tr, flags=re.I)]
            if cs and re.match(patron, cs[0]):
                filas.append(cs)
        if len(filas) != 3:
            continue
        caso = {}
        for k, cs in zip(("conservador", "base", "optimista"), filas):
            try:
                caso[k] = [num(x) for x in cs[5:8]]
            except ValueError:
                pass
        out[met] = caso
    return out


def _num_foto(x: str) -> float:
    """Número de una foto de pestaña, en formato inglés («1,190.85») o español («1.190,85», «19,57»)."""
    t = re.sub(r"[$xX\s]", "", x)
    if "," in t and "." in t:
        t = t.replace(".", "").replace(",", ".") if t.rfind(",") > t.rfind(".") else t.replace(",", "")
    elif "," in t:
        t = t.replace(",", ".") if re.fullmatch(r"-?\d+,\d{1,2}", t) else t.replace(",", "")
    elif t.count(".") > 1:
        t = t.replace(".", "")
    return float(t)


def multiplos_aplicados(rec: dict) -> dict:
    """Múltiplo aplicado en FY+1..FY+3 por método y caso auxiliar (conservador/base/optimista), leído de las fotos de
    las pestañas de múltiplos guardadas con la valoración (filas «Múltiplo …», formato «17.18x»)."""
    return _filas_snapshot(rec, r"^Múltiplo (EV/|P/)", _num_foto)


def precios_snapshot(rec: dict) -> dict:
    """Precio objetivo + dividendos FY+1..FY+3 de las mismas fotos (fila «Total Target Price + Dividends»)."""
    return _filas_snapshot(rec, r"^Total Target Price \+ Dividends", _num_foto)


_IND = {"crecimiento": r"crec|ingres|ventas|cliente|usuario|suscri|ARR|tienda|apertur|volumen|demanda|tráfico|comparable|asiento|nube|Azure|reserva|TPV|GMV|viaje|prescrip|cuota",
        "margen": r"margen|precio|costo|EBIT|rentab|descuento|arancel",
        "reinversion": r"capex|capital|inversi|apertur|centros de datos",
        "riesgo": r"deuda|tasa|beta|apalanc|crédito|morosidad|regula"}


def _indicador(sp, clave, usado=()):
    for x in sp.get("indicadores") or []:
        if x[0] not in usado and re.search(_IND[clave], x[0], flags=re.I):
            return x
    return None


def _oraciones(t: str, n: int = 2) -> str:
    """Las primeras n oraciones de un texto de la ficha (no corta en «US$4.500» ni en «2,5»)."""
    partes = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿(])", (t or "").strip())
    return " ".join(partes[:n]).strip()


def justificacion(r: dict, W) -> None:
    """Párrafos del análisis fundamental que justifican cada supuesto material de la tesis Base y su cambio entre
    escenarios: valor y trayectoria, evidencia con fuente y fecha, mecanismo, por qué esa cifra, qué la invalidaría y
    sensibilidad cuantificada (DCF completo de la Base con un solo supuesto cambiado)."""
    sp, hs, tk = r["spec"], r["historias"], r["ticker"]
    fin = r.get("financiero")
    H = {h["id"]: h for h in hs}
    A, dA = H["A"], H["A"]["detalle"]
    sb = r.get("sens_base") or {"base": A.get("valor_bruto", A["valor_beta_hoja"]), "casos": []}
    v0 = sb["base"]

    def sv(nom, d):
        x = next((c["valor"] for c in sb["casos"] if c["supuesto"] == nom and abs(c["cambio"] - d) < 1e-9), None)
        if x is None:
            return None
        d_ = abs(x / v0 - 1) * 100 if v0 else 0
        return f"{usd(x)} ({'+' if x >= v0 else '−'}{es(d_, 0 if d_ >= 1 else 1)}%)" if v0 else usd(x)

    def _sv(nom, d):
        return next((c["valor"] for c in sb["casos"] if c["supuesto"] == nom and abs(c["cambio"] - d) < 1e-9), None)

    def par(nom, lo, hi, txt):
        a, b = sv(nom, lo), sv(nom, hi)
        return f" Sensibilidad: {txt} lleva el DCF Base de {usd(v0)} a {a} y {b}, respectivamente." if a and b else ""

    fuentes = sp.get("fuentes") or []
    f0 = fuentes[0][0] if fuentes else "estados financieros de la empresa"
    aud = _ROOT / "reference" / "auditoria_estados_2026-10-01" / f"{tk}_resumen.json"
    fecha_ev = "datos contrastados con la SEC el 1-oct-2026" if aud.exists() and not fin else f"datos revisados al {sp.get('fecha', r['fecha'])}"
    usados = []

    def invalida(clave, defecto):
        x = _indicador(sp, clave, usados)
        if not x:
            return defecto
        usados.append(x[0])
        return f"Obligaría a revisarlo este indicador: {x[0]}, {low(x[3])} (hoy: {x[1]})."

    lista = lambda f: "; ".join(f"{NOMBRE[h['id']]} {f(h)}" for h in hs if h["id"] != "A")  # noqa: E731
    W.h3("Justificación de los supuestos", f"{tk.lower()}-justificacion")
    W.p("Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué "
        "trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las "
        "alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las "
        "sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara "
        "provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.")
    if sp.get("justificacion"):  # prosa propia del analista (ADBE): las cifras vienen del cálculo vigente
        for titulo_, texto in sp["justificacion"]:
            W.p((f"**{titulo_}** " + texto).format_map(_cifras(r)))
        if r.get("rd_vida") and not any("I+D" in t_ for t_, _ in sp["justificacion"]):
            W.p(_parrafo_rd(r))
    else:
        an = A["anios"]
        ritmo = ("desacelera" if an[4] < an[0] - 1e-9 else "se mantiene" if abs(an[4] - an[0]) < 1e-9 else "acelera")
        mecanismo = prob_frase(sp, "A")
        W.p(f"**Crecimiento de {'beneficios' if fin else 'ingresos'}.** La Base supone {pct(an[0])} el año 1 y {pct(an[4])} el año 5: la trayectoria {ritmo} y "
            f"equivale a {pct(A['cagr'])} anual compuesto en cinco años; después converge al terminal en los años 6–10. Los demás "
            f"escenarios: {lista(lambda h: pct(h['cagr']))} de crecimiento compuesto. Evidencia ({f0}; {fecha_ev}): "
            f"{_oraciones((sp.get('crecimiento') or {}).get('texto', ''))} "
            + (f"Mecanismo de la Base: {low(mecanismo)} " if mecanismo else "") +
            f"Por qué esta cifra: la visión externa (The Base Rate Book) indica que ~{pct(A['tasa_base'], 0)} de las empresas de su "
            f"tamaño lograron ese crecimiento, frente a ~{pct(H['D']['tasa_base'], 0)} para el de la Optimista; la Base no extrapola "
            "el mejor resultado reciente ni supone la caída de la Disrupción. Los porcentajes son juicio del analista, no guía de la "
            f"empresa. {invalida('crecimiento', 'Obligaría a revisarlo que el crecimiento reportado se aparte de forma sostenida de la trayectoria.')}"
            + par("crecimiento", -0.02, 0.02, "restar o sumar 2 pp al crecimiento de cada año 1–5")
            + (" Crecer más resta valor: el retorno sobre el capital nuevo (con los arrendamientos) es menor que el costo de "
               "capital, así que el supuesto clave no es el crecimiento sino la rentabilidad del capital que exige."
               if (_sv("crecimiento", 0.02) or v0) < v0 else ""))
        unidad = "ROE" if fin else "margen operativo"
        aj = [x for x, ok in (("I+D capitalizado", r.get("rd_vida")), ("arrendamientos como deuda", sp.get("arrendamientos"))) if ok]
        base_aj = "" if fin else (f" en base ajustada ({' y '.join(aj)}, según la hoja)" if aj else " en la base del modelo")
        arr_ = sp.get("arrendamientos")
        y1 = "" if fin else f", desde {pct(dA['margenY1'])} en el año 1 y con convergencia en el año {es(dA['convergencia'], 0)}"
        if arr_ and not fin and A.get("margen_reportado") is not None:
            y1 = (f" ({pct(A['margen_reportado'], 1)} en base reportada + {es(arr_['margen_pp'] * 100, 2)} pp por el ajuste de "
                  f"arrendamientos)" + y1)
        W.p(f"**{unidad[:1].upper() + unidad[1:]}.** La Base usa un {unidad} objetivo de {pct(A['margen'], 1)}{base_aj}{y1}. "
            f"Escenarios: {lista(lambda h: pct(h['margen'], 1))}. Evidencia ({fecha_ev}): "
            f"{_oraciones((sp.get('margenes') or {}).get('texto', ''))} Mecanismo y elección: el objetivo de la Base refleja la "
            "economía de su tesis (escala, mezcla y precio frente a los costos que exige crecer); la Conservadora y la Disrupción "
            "lo bajan porque defender ingresos cuesta precio o gasto, y la Optimista solo lo sube si la monetización supera esos "
            f"costos. No es una promesa de la empresa. {invalida('margen', f'Obligaría a revisarlo que el {unidad} reportado se aleje de la trayectoria durante varios trimestres.')}"
            + par("margen", -0.02, 0.02, f"restar o sumar 2 pp al {unidad} objetivo"))
        if fin:
            W.p(f"**Reinversión patrimonial.** En el DCF de flujo al accionista la reinversión es el aumento del patrimonio contable "
                f"(patrimonio del año anterior × crecimiento): crecer exige retener capital regulatorio. Evidencia: {_oraciones((sp.get('reinversion') or {}).get('texto', ''))} "
                "Supuesto provisional mientras no se concilie con el capital regulatorio exigido en cada escenario.")
        else:
            cap1, cap2 = 1 / dA["s2c"], 1 / dA["s2c2"]
            arr = sp.get("arrendamientos")
            propios = "".join(f" {NOMBRE[h['id']]} usa {es(h['s2c'], 2)}x." for h in hs if h.get("s2c"))
            W.p(f"**Reinversión y ventas/capital.** La Base reinvierte con un ventas/capital de {es(dA['s2c'], 2)}x en los años 1–5 y "
                f"{es(dA['s2c2'], 2)}x en los años 6–10: cada dólar de ventas nuevas exige ~US${es(cap1, 2)} y ~US${es(cap2, 2)} de "
                f"capital, respectivamente.{propios} Evidencia: {_oraciones((sp.get('reinversion') or {}).get('texto', ''))} "
                + (f"Incluye el capital arrendado ({es(arr['capital_ventas'], 2)} dólares por dólar de ventas, criterio de Damodaran). " if arr else "") +
                "Mecanismo: la reinversión es lo que financia el crecimiento; si el retorno del capital nuevo supera el costo de "
                "capital, crecer suma valor. Salvedad: es una hipótesis de la hoja, no un dato reportado; falta una serie homogénea "
                "de capital invertido incremental (con I+D, adquisiciones y capital de trabajo) que la confirme, así que queda "
                f"provisional. {invalida('reinversion', 'Obligaría a revisarlo que el capital invertido crezca más rápido que las ventas.')}"
                + par("s2c", 0.8, 1.2, "un ventas/capital 20% menor o mayor en ambas etapas"))
        if r.get("rd_vida"):
            W.p(_parrafo_rd(r))
        if False:
            W.p(f"**Vida útil de I+D.** La hoja capitaliza el I+D (US${mn(r['rd_ltm'])} millones en el último año) y lo amortiza en "
                f"{es(r['rd_vida'], 0)} años. Mecanismo: el I+D crea activos que rinden varios años; capitalizarlo mueve el gasto del "
                "EBIT al capital invertido. La vida elegida es una convención del modelo (tabla de Damodaran por sector), no un dato "
                "reportado: una vida más larga eleva el activo y reduce el ROIC medido; una más corta hace lo contrario, y cambia "
                "también el EBIT ajustado. No se recalcula aquí porque modifica la hoja de conversión, no un input del DCF; queda "
                "provisional hasta contrastarla con la duración de los beneficios de los productos.")
        tasa = "Ke" if fin else "WACC"
        betas = r.get("betas") or []
        alt = (f" La beta bottom-up de {r['industria']} reapalancada ({es(r['beta_bu'])}) daría un {tasa} inicial de "
               f"{pct(betas[1]['wacc'], 2)}." if r.get("beta_bu") and len(betas) > 1 else "")
        W.p(f"**Costo de capital ({tasa}).** {tasa} de {pct(dA['wacc0'], 2)} en los años 1–5, que converge a {pct(dA['tasaTerminal'], 2)} "
            f"en el año 10: tasa libre de riesgo {pct(r['rf'], 2)}, beta {es(r['beta_hoja'])} y prima de riesgo {pct(r['erp'], 2)} "
            f"(Damodaran, betas por sector y ERP, enero de 2026).{alt} Se usa la misma tasa en los cuatro escenarios: el riesgo "
            "propio del negocio va en los flujos de cada historia, no en una prima arbitraria. La convergencia supone que el riesgo "
            "y la estructura financiera se normalizan; no es automática. Obligaría a revisarlo un cambio de la tasa libre de "
            + ("riesgo, de la prima de mercado o del capital regulatorio exigido." if fin else
               "riesgo, de la prima de mercado o de la deuda (incluidos los arrendamientos).")
            + par("tasa", 0.01, -0.01, f"sumar o restar 1 pp al {tasa} inicial y terminal"))
        term = dA["pvTerminal"] / (dA["pvFlujos"] + dA["pvTerminal"]) if (dA["pvFlujos"] + dA["pvTerminal"]) else None
        propio = [h for h in hs if h.get("terminal_propio")]
        W.p(f"**Crecimiento terminal.** La Base crece {pct(A['terminal_growth'], 2)} a perpetuidad"
            + (", la tasa libre de riesgo: Damodaran pide que el crecimiento estable no supere el de la economía, y la tasa "
               "libre de riesgo es su techo práctico" if abs(A["terminal_growth"] - r["rf"]) < 5e-4 else
               f", el terminal de la hoja, por debajo de la tasa libre de riesgo ({pct(r['rf'], 2)}): Damodaran pide que el "
               "crecimiento estable no supere el de la economía") + ". "
            + ("".join(f"{NOMBRE[h['id']]} se estabiliza en {pct(h['terminal_growth'], 2)} sin recuperarse. " for h in propio)) +
            ((f"El valor terminal explica {pct(term)} del valor operativo de la Base, así que este supuesto pesa "
              f"{'mucho' if term > 0.5 else 'de forma relevante'}. " if term <= 1 else
              "El valor terminal supera al valor operativo de la Base (los flujos de los años 1–10 restan en valor presente), así "
              "que todo el valor depende de la perpetuidad. ") if term else "") +
            "Obligaría a revisarlo un cambio persistente de la inflación o del crecimiento nominal de largo plazo de su moneda."
            + par("terminal", -0.005, 0.005, "restar o sumar 0,5 pp al crecimiento terminal"))
        if not fin:
            moat = (json.loads((_ROOT / "reference" / "moat_2026-09-30.json").read_text())["empresas"]).get(tk) or {}
            rt = dA["roicTerminal"]
            igual = abs(rt - dA["tasaTerminal"]) < 1e-9
            amenaza = re.sub(r"historia ([A-D])", lambda m_: "historia " + NOMBRE[m_.group(1)], moat.get("amenaza", ""))
            W.p(f"**ROIC terminal.** La Base usa {pct(rt, 1)}" + (" (igual al costo de capital)" if igual else "") +
                f" después del año 10. Criterio de ventaja competitiva: {moat.get('ventaja', 'sin clasificar')}"
                + (f" ({moat['fuentes'].rstrip('.')}; evidencia: {moat['evidencia'].rstrip('.')})" if moat.get("fuentes") else "") +
                f". ROIC actual del modelo {pct(moat.get('roic_actual'))}" + (f"; industria (Damodaran) {pct(moat['roic_industria'])}" if moat.get("roic_industria") else "") +
                ". Con ventaja durable se toma el ROIC de la industria sin superar el actual; si se desvanece, el punto medio hacia el "
                "costo de capital; sin ventaja, el costo de capital. Las historias de erosión usan el costo de capital porque una "
                "ventaja perdida no deja retornos excedentes. No es un ROIC futuro observado: es la hipótesis de cuánto dura la "
                "ventaja." + (f" Lo invalidaría: {low(amenaza.rstrip('.'))}." if amenaza.strip(" —-") else "")
                + (f" Sensibilidad: con ROIC terminal igual al costo de capital la Base vale {sv('roic_cc', 0)}." if sv("roic_cc", 0) and not igual else ""))
        W.p(f"**Acciones y dilución.** Los cuatro escenarios usan {es(dA['acciones'], 1)} millones de acciones, sin recompras ni "
            "dilución proyectadas; así se comparan sobre la misma base. No demuestra que la compensación en acciones carezca de "
            "costo: si es material, debería modelarse como gasto o como más acciones. Supuesto provisional."
            + (f" Sensibilidad: 5% más acciones con el mismo patrimonio llevan la Base a {sv('acciones', 0.05)}." if sv("acciones", 0.05) else ""))
    calculo_en_prosa(r, W)
    _justifica_multiplos(r, W)
    casos = {("margen", -0.02): "Margen objetivo −2 pp" if not fin else "ROE −2 pp", ("margen", 0.02): "Margen objetivo +2 pp" if not fin else "ROE +2 pp",
             ("crecimiento", -0.02): "Crecimiento años 1–5 −2 pp", ("crecimiento", 0.02): "Crecimiento años 1–5 +2 pp",
             ("s2c", 0.8): "Ventas/capital −20%", ("s2c", 1.2): "Ventas/capital +20%",
             ("tasa", 0.01): f"{'Ke' if fin else 'WACC'} +1 pp", ("tasa", -0.01): f"{'Ke' if fin else 'WACC'} −1 pp",
             ("terminal", -0.005): "Crecimiento terminal −0,5 pp", ("terminal", 0.005): "Crecimiento terminal +0,5 pp",
             ("roic_cc", 0): "ROIC terminal = costo de capital", ("acciones", 0.05): "Acciones +5%"}
    filas = []
    for (n, d), lab in casos.items():
        x = next((c["valor"] for c in sb["casos"] if c["supuesto"] == n and abs(c["cambio"] - d) < 1e-9), None)
        if x is not None and v0 and abs(x - v0) > 1e-9:
            filas.append([lab, usd(x), f"{'+' if x >= v0 else '−'}{es(abs(x / v0 - 1) * 100, 1)}%"])
    if filas:
        W.p(f"Sensibilidad del DCF Base ({usd(v0)}; cada fila es un DCF completo con un solo supuesto cambiado):")
        W.tab(["Supuesto cambiado", "DCF Base", "Variación"], filas, ["l", "r", "r"])


def _justifica_multiplos(r: dict, W) -> None:
    try:
        rec = json.loads(Path(glob.glob(str(DATOS / "valoraciones" / f"{r['ticker']}-*.json"))[0]).read_text())
    except (IndexError, OSError):
        return
    dm = rec.get("descuentoMultiples") or {}
    mets = dm.get("metodos") or []
    if not mets:
        return
    ap = multiplos_aplicados(rec)
    partes = []
    for m in mets:
        a = (ap.get(m["nombre"]) or {}).get("base")
        mult = (f"{es(a[0])}×" if a and len(set(round(x, 4) for x in a)) == 1 else
                " / ".join(f"FY+{i + 1} {es(x)}×" for i, x in enumerate(a)) if a else "múltiplo no disponible")
        partes.append(f"{m['nombre']} {mult} (peso {pct(m.get('pesoMultiplos', m.get('peso')), 0)} dentro de los múltiplos)")
    W.p("**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: " + "; ".join(partes) + ". Cada múltiplo se elige con "
        "tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por "
        "crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del "
        f"patrimonio ({pct(dm.get('costoPatrimonio'))}). Son precio relativo, no valor intrínseco: si el mercado entero está caro, "
        "también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un "
        "resultado de Disrupción. La tabla por método está en la valoración vigente.")


def avisos_coherencia(r: dict) -> list[str]:
    """Controles de coherencia económica de cada historia (criterio Damodaran, 6-oct-2026, aprendidos con MCD):

    1. Liberación de capital: con ventas/capital, una caída de ingresos da reinversión NEGATIVA (la empresa «libera»
       capital). Damodaran la admite solo si el capital realmente sale (venta de activos, menos capital de trabajo); en
       un refranquiciamiento o una desinversión hay que compararla con lo que se cobra por lo vendido.
       La reinversión es Δingresos / ventas/capital: SUBIR el ventas/capital de esos años reduce lo liberado (MCD,
       Disrupción: 1,70 para liberar ~US$0,35 por dólar de venta propia perdida, lo cobrado en 2015-2018).
    2. Rendimiento del capital nuevo: margen objetivo × (1 − impuesto marginal) × ventas/capital frente al ROIC
       terminal; si lo duplica, el ventas/capital supone crecer casi sin invertir (Investment Valuation, cap. 11).
       Solo si la historia invierte en los años 1-5 (alguna reinversión positiva).
    """
    out = []
    for h in r.get("historias", []):
        d = h.get("detalle") or {}
        reinv, nopat = d.get("reinversion") or [], d.get("nopat") or []
        neg = [(i, x) for i, x in enumerate(reinv) if isinstance(x, (int, float)) and x < 0
               and i < len(nopat) and isinstance(nopat[i], (int, float)) and nopat[i] > 0 and -x > 0.10 * nopat[i]]
        if neg:
            total = -sum(x for _, x in neg)
            out.append(f"{h['id']} libera capital en {len(neg)} año(s) (US${total:,.0f} M, hasta {max(-x / nopat[i] for i, x in neg):.0%} "
                       "del NOPAT): justificar con lo que se cobra por los activos que salen (refranquiciamiento, ventas) o "
                       "subir el ventas/capital propio de la historia (menos capital por dólar de ingreso perdido)")
        m, s2c, tm = (d.get("margen") or [None])[-1], d.get("s2c"), d.get("impuestoMarg")
        rt = h.get("roic_terminal_usado") or d.get("roicTerminal")
        invierte = any(isinstance(x, (int, float)) and x > 0 for x in reinv[1:6])  # sin capital nuevo no hay rendimiento que medir
        if invierte and all(isinstance(x, (int, float)) for x in (m, s2c, tm, rt)) and rt > 0:
            rn = m * (1 - tm) * s2c
            if rn > 2 * rt:
                out.append(f"{h['id']}: el capital nuevo rinde {rn:.0%} (margen × (1 − t) × ventas/capital), más del doble del "
                           f"ROIC terminal ({rt:.0%}): revisar el ventas/capital")
    return out


def _cifras(r: dict) -> dict:
    """Cifras vigentes para la prosa propia de una ficha (spec["justificacion"]): {clave} se sustituye al redactar."""
    H = {h["id"]: h for h in r["historias"]}
    A, dA = H["A"], H["A"]["detalle"]
    d = {"vA": usd(A["valor_beta_hoja"]), "ve": usd(r["valor_esperado_beta_hoja"]), "acciones": es(dA["acciones"], 1),
         "cagrA": pct(A["cagr"]), "g1A": pct(A["anios"][0], 2), "tgA": pct(A["terminal_growth"], 2),
         "wacc0": pct(dA["tasa"][1] if r.get("financiero") else dA["wacc0"], 2), "waccT": pct(dA["tasaTerminal"], 2), "roicT": pct(dA["roicTerminal"], 1),
         "terminal": pct(dA["pvTerminal"] / (dA["pvFlujos"] + dA["pvTerminal"])), "margenY1": pct(dA.get("margenY1")),
         "s2c1": es(dA.get("s2c") or 0, 2), "s2c2": es(dA.get("s2c2") or 0, 2),
         "cap1": es(1 / dA["s2c"], 2) if dA.get("s2c") else "—", "cap2": es(1 / dA["s2c2"], 2) if dA.get("s2c2") else "—"}
    corte = json.loads((_ROOT / "reference" / "corte_vigente.json").read_text())  # corte vigente (datos_mercado.py)
    d["fecha_corte"] = corte["fecha_corte_es"]  # fecha de la tasa libre de riesgo y de la prima
    d["mes_erp"] = corte["erp_mes"].split(" de ")[0]
    for k, h in H.items():
        d[f"m{k}"] = pct(h["margen"], 1)
        d[f"mrep{k}"] = pct(h.get("margen_reportado", h["margen"]), 1)
        d[f"tg{k}"] = pct(h["terminal_growth"], 2)
        d[f"g5{k}"] = pct(h["anios"][4], 2)
        d[f"cagr{k}"] = pct(h["cagr"])
        d[f"g1{k}"] = pct(h["anios"][0], 1)
        d[f"p{k}"] = pct(h["prob"], 0)
        d[f"v{k}"] = usd(h["valor_beta_hoja"])
        d[f"tb{k}"] = pct(h.get("tasa_base"), 0)
        d[f"s2c{k}"] = es(h.get("s2c") or dA.get("s2c") or 0, 2)
    mos = r.get("mos")
    d["mos"] = pct(mos, 0) if isinstance(mos, (int, float)) else "—"
    d["vmos"] = usd(r["valor_esperado_beta_hoja"] * (1 - mos)) if isinstance(mos, (int, float)) else "—"
    d["g5A"] = pct(A["anios"][4], 1)
    d["conv"] = es(dA.get("convergencia") or 0, 0)
    d["rf"], d["erp"], d["beta"] = pct(r["rf"], 2), pct(r["erp"], 2), es(r["beta_hoja"])
    d["betabu"] = es(r["beta_bu"]) if r.get("beta_bu") else "—"
    d["tecnico"] = usd(r.get("dcf_base"))
    d["precio"] = usd(r.get("precio"))
    d["rd_vida"] = es(r["rd_vida"], 0) if r.get("rd_vida") else "—"
    arr = (r.get("spec") or {}).get("arrendamientos") or {}
    d["arr_pp"] = es(arr.get("margen_pp", 0) * 100, 2)
    d["arr_vp"] = es(arr.get("vp", 0), 0)
    sb = r.get("sens_base") or {"base": None, "casos": []}
    v0 = sb["base"]
    for n, dd, k in (("margen", -0.02, "s_m_lo"), ("margen", 0.02, "s_m_hi"), ("crecimiento", -0.02, "s_g_lo"),
                     ("crecimiento", 0.02, "s_g_hi"), ("tasa", 0.01, "s_k_hi"), ("tasa", -0.01, "s_k_lo"),
                     ("terminal", -0.005, "s_tg_lo"), ("terminal", 0.005, "s_tg_hi"), ("s2c", 0.8, "s_s_lo"),
                     ("s2c", 1.2, "s_s_hi"), ("roic_cc", 0, "s_roic"), ("acciones", 0.05, "s_acc")):
        x = next((c["valor"] for c in sb["casos"] if c["supuesto"] == n and abs(c["cambio"] - dd) < 1e-9), None)
        if x is None or not v0:
            d[k] = "—"
        else:
            q = abs(x / v0 - 1) * 100
            d[k] = f"{usd(x)} ({'+' if x >= v0 else '−'}{es(q, 0 if q >= 1 else 1)}%)"
    return d


def _parrafo_rd(r: dict) -> str:
    return (f"**Vida útil de I+D.** La hoja capitaliza el I+D (US${mn(r['rd_ltm'])} millones en el último año) y lo amortiza en "
            f"{es(r['rd_vida'], 0)} años. Mecanismo: el I+D crea activos que rinden varios años; capitalizarlo mueve el gasto del "
            "EBIT al capital invertido. La vida elegida es una convención del modelo (tabla de Damodaran por sector), no un dato "
            "reportado: una vida más larga eleva el activo y reduce el ROIC medido; una más corta hace lo contrario, y cambia "
            "también el EBIT ajustado. No se recalcula aquí porque modifica la hoja de conversión, no un input del DCF; queda "
            "provisional hasta contrastarla con la duración de los beneficios de los productos.")


def _um2(v) -> str:
    return ("−US$" if v < 0 else "US$") + mn(abs(v), 2)


def _um(v) -> str:
    """Millones con signo antes de la moneda: −US$165 millones."""
    return ("−US$" if v < 0 else "US$") + mn(abs(v))


def calculo_en_prosa(r: dict, W) -> None:
    """Explica en palabras, con las cifras de la Base, cómo se pasa de los supuestos al valor por acción."""
    H = {h["id"]: h for h in r["historias"]}
    A, d = H["A"], H["A"]["detalle"]
    if r.get("financiero"):
        u = d["utilidad"]
        W.p(f"**Del supuesto al valor: cómo se calcula la Base.** El punto de partida es la utilidad del último año, {_um(u[0])} "
            f"millones. Cada año es el ROE de la Base por el patrimonio contable del año anterior: {_um(u[5])} millones en el año 5 "
            f"y {_um(u[10])} millones en el año 10, cuando el ROE ya bajó al costo del patrimonio. No toda esa utilidad se puede "
            "repartir: para crecer, un banco o una financiera tiene que aumentar su patrimonio al mismo ritmo, y esa parte se "
            "retiene. Lo que queda es el flujo del accionista (FCFE): "
            f"{_um(d['flujo'][1])} millones el primer año. Esos flujos se traen a hoy con el costo del patrimonio, que empieza en "
            f"{pct(d['tasa'][1], 2)} y baja a {pct(d['tasaTerminal'], 2)}; suman {_um(d['pvFlujos'])} millones. Después del año 10 se "
            f"supone un crecimiento perpetuo de {pct(d['gTerminal'], 2)}: el valor de esa perpetuidad, traído a hoy, es "
            f"{_um(d['pvTerminal'])} millones. La suma es el valor del patrimonio, {_um(d['patrimonio'])} millones; dividido "
            f"entre {es(d['acciones'], 1)} millones de acciones da {usd(A['valor_beta_hoja'])} por acción. Aquí no se resta deuda: "
            "en una financiera la deuda es materia prima del negocio y ya está dentro del flujo del accionista.")
        return
    rev, m = d["ingresos"], d["margen"]
    tot = d["pvFlujos"] + d["pvTerminal"]
    puente = [f"más caja por {_um(d['caja'])} millones"]
    if d["noOperativos"]:
        puente.append(f"más activos no operativos por {_um(d['noOperativos'])} millones")
    puente.append(f"menos deuda por {_um(d['deuda'])} millones" + (" (incluye los arrendamientos capitalizados)" if (r.get("spec") or {}).get("arrendamientos") else ""))
    if d["minoritarios"]:
        puente.append(f"menos minoritarios por {_um(d['minoritarios'])} millones")
    if d["opciones"]:
        puente.append(f"menos opciones por {_um(d['opciones'])} millones")
    if d.get("preferentes"):
        puente.append(f"menos acciones preferentes por {_um(d['preferentes'])} millones")
    W.p(f"**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por {_um(rev[0])} "
        f"millones. Con el crecimiento de la Base llegan a {_um(rev[5])} millones en el año 5 y a {_um(rev[10])} millones en el "
        f"año 10. A esas ventas se les aplica el margen operativo, que pasa de {pct(m[1])} en el año 1 a {pct(m[10])} al final, y "
        f"se descuentan impuestos ({pct(d['impuestoEf'], 1)} al principio y {pct(d['impuestoMarg'], 1)} a largo plazo): el resultado "
        f"es el beneficio operativo después de impuestos (NOPAT), {_um(d['nopat'][1])} millones el primer año. Crecer no es "
        f"gratis: cada dólar de ventas nuevas exige capital, y esa reinversión ({'+' if d['reinversion'][1] >= 0 else '−'}"
        f"{_um(abs(d['reinversion'][1]))} millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de "
        f"la empresa (FCFF), {_um(d['flujo'][1])} millones el primer año. Cada flujo se trae a hoy con el costo de capital "
        f"({pct(d['tasa'][1], 2)} al principio, {pct(d['tasaTerminal'], 2)} al final): los diez años suman {_um(d['pvFlujos'])} "
        f"millones. Después del año 10 se supone que la empresa crece {pct(d['gTerminal'], 2)} para siempre y reinvierte lo justo "
        f"para ese crecimiento con un retorno de {pct(d['roicTerminal'], 1)}; esa perpetuidad vale hoy {_um(d['pvTerminal'])} "
        f"millones" + (f", {pct(d['pvTerminal'] / tot, 0)} del total" if 0 < d["pvTerminal"] / tot <= 1 else "") +
        f". Flujos más terminal dan el valor de las operaciones, {_um(d['activosOperativos'])} millones. Para llegar al "
        f"accionista se suma y se resta lo que no es operativo: {', '.join(puente)}. Queda un patrimonio de "
        f"{_um(d['patrimonio'])} millones que, repartido entre {es(d['acciones'], 1)} millones de acciones, da "
        f"{usd(A['valor_beta_hoja'])} por acción" + (" (si el patrimonio fuera negativo, se toma cero: el accionista no responde por "
        "más de lo que puso)." if A.get("valor_bruto", 1) < 0 else ".") +
        " Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio "
        "ponderado por probabilidad.")


def trayectorias(r: dict, W, titulo: str) -> None:
    """Tabla año por año (1-10 y perpetuidad) de cada historia: lo que la hoja calcula en «Escenarios e historias»."""
    fin = r.get("financiero")
    W.h4(titulo)
    W.p("Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en " +
        ("«Escenarios e historias»: " if fin else "los bloques de 'Valuation output': ") + ("utilidad, crecimiento, ROE, reinversión patrimonial, flujo al accionista (FCFE), costo del patrimonio "
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
                ni = (d.get("utilidadTerminal") or base[10] * (1 + g)) if t else base[y]
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
        W.p(f"**{nombre(h)}** — probabilidad {pct(h['prob'], 0)}; valor terminal {es(d['valorTerminal'], nd)} (VP {es(d['pvTerminal'], nd)}); "
            f"DCF {usd(h['valor_beta_hoja'])} por acción.")
        if fin:
            W.tab(["Año", "Utilidad", "Crecimiento", "ROE", "Reinversión", "FCFE", "Ke", "VP del FCFE"], rows, ["l"] + ["r"] * 7)
            exceso(h, W, nd)
        else:
            W.tab(["Año", "Ingresos", "Crecimiento", "Margen", "NOPAT", "Reinversión", "FCFF", "WACC", "VP del FCFF"], rows,
                  ["l"] + ["r"] * 8)


def exceso(h: dict, W, nd: int) -> None:
    """Tabla del modelo de rendimientos en exceso de Damodaran para bancos: valor del patrimonio = patrimonio contable de hoy
    + VP de (ROE − Ke) × patrimonio inicial de cada año. Con utilidad = ROE × patrimonio y reinversión = aumento del patrimonio
    es idéntico al FCFE; la tabla lo comprueba."""
    d = h["detalle"]
    bv = d.get("patrimonioContable")
    if not bv or bv[0] is None:
        return
    rows, pv = [], 0.0
    for y in range(1, 11):
        ke, roe, ni = d["tasa"][y], d["margen"][y], d["utilidad"][y]
        costo = ke * bv[y - 1]
        ex = ni - costo
        v = ex / _acum(d["tasa"], y)
        pv += v
        z = lambda x: 0.0 if abs(x) < 0.05 else x  # noqa: E731
        rows.append([str(y), es(bv[y - 1], nd), pct(roe), es(ni, nd), pct(ke), es(costo, nd), es(z(ex), nd), es(z(v), nd)])
    rows.append(["Terminal", es(bv[10], nd), pct(d["tasaTerminal"]), es(d["tasaTerminal"] * bv[10], nd), pct(d["tasaTerminal"]),
                 es(d["tasaTerminal"] * bv[10], nd), es(0, nd), "0"])
    valor = (bv[0] + pv) / d["acciones"]
    W.p(f"Modelo de rendimientos en exceso (Damodaran, bancos): patrimonio contable de hoy {es(bv[0], nd)} + VP de los "
        f"rendimientos en exceso {es(pv, nd)} = {es(bv[0] + pv, nd)} millones; entre {es(d['acciones'], 2)} millones de acciones da "
        f"{usd(valor)} por acción, igual que el FCFE ({usd(d['v'])}). En perpetuidad el ROE es el costo del patrimonio: no hay "
        "rendimiento en exceso y crecer no suma valor.")
    W.tab(["Año", "Patrimonio inicial", "ROE", "Utilidad", "Ke", "Costo del patrimonio", "Rendimiento en exceso", "VP"], rows,
          ["l"] + ["r"] * 7)


def tabla_s2c(r: dict, W) -> None:
    """Las referencias de Damodaran para elegir el ventas/capital (Investment Valuation, cap. 11, p. 44-46): el de la
    empresa hoy, el marginal reciente y el del sector, frente al usado y al rendimiento que implica sobre el capital nuevo."""
    p = Path(__file__).resolve().parents[1] / "reference" / "ventas_capital_2026-10-04.json"
    if not p.exists():
        return
    x = json.loads(p.read_text()).get(r["ticker"])
    if not x:
        return
    def m_(k):
        mm = x.get(k)
        if not mm:
            return "—", "sin datos suficientes"
        det = (f"Δventas {mn(mm['dventas'], 1)} / Δcapital {mn(mm['dcapital'], 1)} millones ({mm['desde']} → {mm['hasta']})")
        return (es(mm["ratio"], 2) if mm.get("ratio") else "—"), (det if mm.get("ratio") else det + ": el capital o las ventas no crecieron (recompras, venta de negocios o caída de ventas), no hay inversión que medir")
    m1, m3 = m_("marginal_ultimo"), m_("marginal_3a")
    s1, s2 = x["usada"]
    r1, r2 = x["rendimiento_capital_nuevo"]
    rows = [["Empresa hoy", es(x["actual"], 2), f"ventas LTM {mn(x['ventas_ltm'], 1)} / capital invertido {mn(x['capital_ltm'], 1)} millones"
             + (" (con I+D capitalizado a " + str(x["vida_id"]) + " años)" if x.get("con_id") else "")
             + (f"; {x['ajuste']}" if x.get("ajuste") else "")],
            ["Marginal, último año", m1[0], m1[1]],
            ["Marginal, últimos tres años", m3[0], m3[1]],
            ["Sector (Damodaran, enero de 2026)", es(x["sector"], 2) if x.get("sector") else "—",
             (x.get("industria") or "") + ("" if x.get("sector") else ": no comparable (el capital de una financiera es otra cosa)")],
            ["Usado en la hoja", f"{es(s1, 2)} / {es(s2, 2)}",
             f"años 1-5 / 6-10; rinde ~{pct(r1, 0)} / ~{pct(r2, 0)} sobre el capital nuevo (ROIC actual {pct(x['roic_actual'], 1)})"]]
    refs = [v for v in (x.get("actual"), (x.get("marginal_3a") or {}).get("ratio"), x.get("sector")) if v]
    if refs and min(s1, s2) > max(refs) * 1.05:
        lect = ("El usado está por encima de todas las referencias: supone que la empresa crecerá con menos capital del que "
                "necesitó hasta ahora y del que necesita su sector. Lo sostiene solo si el ROIC lo respalda (control de la p. 45).")
    elif refs and max(s1, s2) < min(refs) * 0.95:
        lect = ("El usado está por debajo de todas las referencias: es prudente (más reinversión por dólar de crecimiento); "
                "la nota de la hoja (Input sheet B32-B33) explica por qué.")
    else:
        lect = "El usado está dentro del rango de las referencias."
    W.p("**Ventas/capital: las referencias de Damodaran.** Damodaran elige el ventas/capital mirando el de la empresa hoy, "
        "el marginal de los últimos años y el promedio del sector, y comprueba que el rendimiento que implica sobre el capital "
        "nuevo sea creíble frente a lo que gana la empresa o su sector (Investment Valuation, cap. 11, p. 44-46). El marginal "
        "es volátil: recompras de acciones y adquisiciones mueven el capital contable. " + lect)
    W.tab(["Referencia", "Ventas/capital", "Detalle"], rows, ["l", "r", "l"])


def _acum(tasas, y):
    f = 1.0
    for n in range(1, y + 1):
        f *= 1 + tasas[n]
    return f


def low(t: str) -> str:
    """Minúscula inicial salvo siglas (EBITDA, ARR, ROE)."""
    return t[:1].lower() + t[1:] if len(t) > 1 and not t[1].isupper() else t




def cuatro_tesis(r: dict, W) -> None:
    sp, hs = r["spec"], r["historias"]
    fin = r.get("financiero")
    A = next(h for h in hs if h["id"] == "A")
    segs = list(sp["segmentos"].keys())
    ind = sp.get("indicadores") or []
    W.h3("Las cuatro tesis: Base, Conservadora, Disrupción y Optimista")
    W.p(f"La tesis Base es la trayectoria central defendida y su DCF, {usd(A['valor_beta_hoja'])}, es el valor intrínseco principal. "
        f"El DCF esperado de {usd(r['valor_esperado_beta_hoja'])} combina las cuatro tesis con sus probabilidades y se presenta como "
        "complemento. " + ("" if hoja_historias(r) else "La antigua calibración técnica Conservador/Base/Optimista de la hoja "
                            "no define estas tesis. ") + "Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.")
    for h in hs:
        desc = h.get("tesis_titulo") or titulo(h)
        W.h4(("Disrupción · Deterioro de los fundamentales" if h["id"] == "C" else NOMBRE[h["id"]]) + (f": {desc}" if desc else ""))
        frase = prob_frase(sp, h["id"])
        if h.get("tesis_que"):  # prosa del analista (ADBE)
            W.p("**Qué tiene que ocurrir.** " + h["tesis_que"])
        elif frase:
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
        if h.get("tesis_contraste"):
            W.p("**Cómo contrastarla.** " + h["tesis_contraste"])
        elif ind:
            if h["id"] == "A":
                c = ("Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (" +
                     "; ".join(f"{low(x[0])}: {x[1]}" for x in ind[:3]) + "). Pierde peso si cruzan cualquiera de los umbrales "
                     "de la tabla de indicadores.")
            elif h["id"] == "D":
                c = "La confirmarían: " + "; ".join(f"{low(x[0])}: {low(x[2])}" for x in ind[:4]) + "."
            else:
                c = (("La apoyarían: " if h["id"] == "B" else "La apoyaría, con más intensidad y duración que la Conservadora: ") +
                     "; ".join(f"{low(x[0])}: {low(x[3])}" for x in ind[:4]) + ".")
            W.p("**Cómo contrastarla.** " + c)
    iguales = "la misma tasa de descuento" + ("" if fin else " y la misma estructura de impuestos y deuda")
    tgs = agrupa(hs, lambda h: pct(h["terminal_growth"], 2))
    vb = {h["id"]: h.get("valor_bruto", h["valor_beta_hoja"]) for h in hs}
    sev = [k for k, _ in sorted(vb.items(), key=lambda x: x[1])]
    sev_txt = " < ".join(NOMBRE[k] for k in sev)
    nota_orden = "" if sev == ["C", "B", "A", "D"] else (
        f" El orden de los DCF ({sev_txt}) no sigue exactamente la severidad de las tesis: " +
        ("crecer destruye valor porque el retorno sobre el capital (con los arrendamientos) es menor que el costo de capital, así "
         "que la historia que más crece y reinvierte puede valer menos." if vb["B"] < vb["C"] else
         "la diferencia sale de los supuestos de cada historia (crecimiento, margen, reinversión y terminal), no de un error de cálculo."))
    neg = [h for h in hs if h.get("valor_bruto", 0) < 0]
    if neg:
        W.p("**Responsabilidad limitada.** " + "; ".join(f"{NOMBRE[h['id']]} da un DCF bruto de {usd(h['valor_bruto'])} por acción" for h in neg) +
            ": el valor de las operaciones no alcanza para cubrir la deuda (incluidos los arrendamientos). El patrimonio no vale menos "
            "que cero, así que esas historias entran al valor esperado con US$0. Que crecer reste valor es la señal de un retorno "
            "sobre el capital (con los arrendamientos) por debajo del costo de capital.")
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


def hoja_historias(r: dict) -> bool:
    """Desde el 2-oct-2026 los bloques de 'Valuation output' calculan las historias: el DCF de la hoja (B35) es el de la
    historia Base y ya no hay un caso técnico aparte. Las financieras (PAGS) conservan el DCF FCFE y su pestaña."""
    A = next((h for h in r.get("historias", []) if h.get("id") == "A"), None)
    return (not r.get("financiero") and A is not None and isinstance(r.get("dcf_base"), (int, float))
            and abs(r["dcf_base"] - A["valor_beta_hoja"]) < 0.01)


def _tecnico(x, k=None):
    """En las fichas, «DCF Base» designa el antiguo caso técnico de la hoja (textos de riesgo y sensibilidad): se
    reescribe como «DCF técnico anterior» para no confundirlo con el DCF de la tesis Base, que es el valor principal."""
    if isinstance(x, str):
        return x.replace("DCF Base", "DCF técnico anterior")
    if isinstance(x, dict):
        return {kk: (v if kk == "justificacion" else _tecnico(v, kk)) for kk, v in x.items()}
    if isinstance(x, list):
        return [_tecnico(v) for v in x]
    return x


def render(r: dict) -> tuple[str, str]:
    sp = r["spec"] if hoja_historias(r) else _tecnico(r["spec"])
    r = {**r, "spec": sp}
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
    hh = hoja_historias(r)
    lo_h, hi_h = min(h["valor_beta_hoja"] for h in hs), max(h["valor_beta_hoja"] for h in hs)
    rango = f"US${es(lo_h)}–{es(hi_h)}"
    mos_txt = (f" El MOS {pct(mos, 0)} se aplica al esperado: {usd(ve * (1 - mos))}." if isinstance(mos, (int, float)) else "")
    p(f"**Valor intrínseco principal · DCF Base hoy: {usd(central['valor_beta_hoja'])} por acción** ({nombre(central)}).")
    p(f"**Complemento · DCF esperado por probabilidades: {usd(ve)}.** Los cuatro escenarios DCF activos son Base, "
      f"Conservadora, Disrupción y Optimista; su rango es {rango}.{mos_txt} " +
      ("La hoja calcula las cuatro en 'Valuation output'. " if hh else
       f"El antiguo caso técnico de la hoja ({usd(r['dcf_base'])}) se conserva solo como calibración; no es el DCF Base. ") +
      "Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.")
    aud_p = _ROOT / "reference" / "auditoria_estados_2026-10-01" / f"{r['ticker']}_resumen.json"
    if aud_p.exists():
        a = json.loads(aud_p.read_text())
        tipos = sorted({c["tipo"] for c in a["cambios"]})
        p(f"**Auditoría, {a['fecha']}:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las "
          f"historias y sus textos. " + (f"Correcciones: {', '.join(t_.lower() for t_ in tipos)} ({len(a['cambios'])} "
          f"{'cambios' if any(':' in str(c_.get('celda', '')) or ',' in str(c_.get('celda', '')) for c_ in a['cambios']) else 'celdas'}, "
          "con respaldo). " if a["cambios"] else "Sin correcciones de datos. ") +
          f"DCF esperado {usd(a['antes']['valorEsperado'])} → {usd(a['despues']['valorEsperado'])}. " +
          ("Salvedades abiertas: " + " ".join(a["salvedades"][:-1]) + " " if len(a["salvedades"]) > 1 else "") +
          "La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.")
    p("Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, "
      "piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el "
      "motor del Modelo JMR, que reproduce la hoja (" + (f"bloque Base de 'Valuation output': {usd(r['dcf_base'])} por acción" if hh
      else f"DCF técnico anterior de {usd(r['dcf_base'])} por acción") + "): solo cambian el "
      "crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de "
      "la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el "
      "promedio de las historias ponderado por su probabilidad. " + ("La hoja calcula estos cuatro DCF en 'Valuation output' (bloques "
      "Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». " if hh else
      "La hoja incluye estos cuatro DCF en «Escenarios e historias». ") +
      "Los múltiplos son precio relativo y se comentan en otras secciones.")

    h3("La historia en un párrafo")
    p(sp["historia"])
    tab(["Afirmación", "¿Posible?", "¿Plausible?", "¿Probable?"], sp["filtro"])

    br = r["tasas_base"]
    h3("Visión externa: tasas base")
    real = br.get("ventas_2015") or r["ingresos_ltm"] * IPC_2015 / IPC_HOY
    p(f"Con ventas LTM de US${es(r['ingresos_ltm'], 0)} millones (US${es(real, 0)} millones en dólares de 2015, deflactadas con "
      f"el IPC-U: × {es(IPC_2015, 3)} / {es(IPC_HOY, 3)}), la empresa está en el tramo **{br['tramo']}** de las "
      f"tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, "
      f"1950-2015). En ese tramo el crecimiento real anual tuvo una media de {es(br['Mean'], 1)}% y una mediana de "
      f"{es(br['Median'], 1)}% (desviación estándar {es(br['StDev'], 1)}%); sumando una inflación de "
      f"{es(INFLACION * 100, 1)}%, la mediana nominal ronda {es(br['Median'] + INFLACION * 100, 1)}%.")
    rows = [[nombre(h), pct(h["cagr"]), pct(h["tasa_base"], 0)] for h in r["historias"]]
    tab(["Historia", "Crecimiento anual de ingresos (5 años)", "Empresas de este tamaño que lo lograron"], rows, ["l", "r", "r"])
    p(sp["tasas_base_nota"].format_map(_cifras(r)) if "{" in sp["tasas_base_nota"] else sp["tasas_base_nota"])

    from types import SimpleNamespace
    W = SimpleNamespace(h3=h3, h4=h4, p=p, tab=tab)
    justificacion(r, W)

    h3("Piezas del valor")
    for key, titulo in (("crecimiento", "Crecimiento"), ("margenes", "Márgenes"), ("reinversion", "Reinversión y retorno")):
        blk = sp.get(key) or {}
        if blk.get("texto"):
            p(f"**{titulo}.** " + (blk["texto"].format_map(_cifras(r)) if "{" in blk["texto"] else blk["texto"]))
        if blk.get("tabla"):
            tab(blk["tabla"]["cols"], blk["tabla"]["rows"], blk["tabla"].get("align"))
        if key == "reinversion" and not r.get("financiero"):
            tabla_s2c(r, W)
    arr = sp.get("arrendamientos")
    if arr:
        p(f"**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente "
          f"(US${es(arr['vp'], 0)} millones, compromisos del {arr.get('informe', '10-Q' if str(arr['cierre'])[5:7] != '12' else '10-K')} al {arr['cierre']}) se suma a la deuda y al peso de la deuda "
          f"del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación "
          f"del activo arrendado (US${es(arr['ajuste_ebit'], 0)} millones, +{es(arr['margen_pp'] * 100, 2)} pp de margen). Por eso "
          "los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y "
          f"el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además {es(arr['capital_ventas'], 2)} dólares "
          "de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.")
    rk = sp.get("riesgo", {})
    p("**Riesgo.** " + rk.get("texto", ""))
    tab(["Enfoque", "Beta", "Costo del patrimonio", "WACC inicial", "DCF Base por acción" if hh else "DCF técnico anterior por acción"],
        [[b["enfoque"], es(b["beta"]), pct(b["ke"]), pct(b["wacc"]), usd(b["dcf_base"])] for b in r["betas"]],
        ["l", "r", "r", "r", "r"])

    su = r.get("supuestos") or {}
    if r.get("financiero"):
        h3("DCF financiero: supuestos y limitaciones")
        _t = (sp.get("margenes") or {}).get("texto", "") + " " + (sp.get("reinversion") or {}).get("texto", "")
        p(_t.format_map(_cifras(r)) if "{" in _t else _t)  # cifras vivas (Ke, beta) en lugar de las de la fecha del informe
    elif su.get("growthBase") is not None and not hh:
        h3("Calibración técnica anterior Conservador/Base/Optimista (referencia auxiliar)")
        tab(["Supuesto", "Conservador", "Base", "Optimista"],
            [[lab] + [pct(su.get(k + s_)) for s_ in ("Cons", "Base", "Opt")] for lab, k in (
                ("Crecimiento año 1", "growthY1"), ("Crecimiento años 2–5", "growth"),
                ("Margen año 1 (base ajustada del modelo)", "marginY1"), ("Margen objetivo", "margin"))],
            ["l", "r", "r", "r"])
        p(f"Ventas/capital: {es(su.get('salesToCapital'), 1)}x en años 1–5 y {es(su.get('salesToCapital2'), 1)}x en 6–10. "
          f"WACC: {pct(su.get('wacc'))}. Ke: {pct(su.get('costoPatrimonio'))}. Impuesto efectivo: {pct(su.get('taxEffective'))}. "
          f"Convergencia: {es(su.get('convergenceYear'), 0)} años. Estos parámetros son escenarios del analista, no cifras reportadas. "
          "Los casos Conservador, Base y Optimista de la hoja ya no son escenarios activos: sirven de calibración y de supuestos "
          "auxiliares de múltiplos. No confundir el antiguo caso técnico Base con la tesis Base.")
    moat = (json.loads((_ROOT / "reference" / "moat_2026-09-30.json").read_text())["empresas"]).get(r["ticker"])
    if moat and not r.get("financiero") and r.get("dcf_sin_exceso") is not None:
        rt = moat.get("roic_terminal")
        h3("Ventaja competitiva y ROIC terminal: comprobación")
        tab(["Ventaja (criterio Damodaran)", "ROIC actual (modelo)", "ROIC de la industria (Damodaran)", "Costo de capital terminal",
             "ROIC terminal usado", "DCF Base de la hoja" if hh else "DCF técnico anterior", "DCF con ROIC terminal = costo de capital"],
            [[moat["ventaja"].capitalize(), pct(moat["roic_actual"]), pct(moat["roic_industria"]) if moat.get("roic_industria") else "No disponible",
              pct(moat["costo_capital_terminal"]), pct(rt) if rt else "= costo de capital", usd(r["dcf_base"]), usd(r["dcf_sin_exceso"])]],
            ["l", "r", "r", "r", "r", "r", "r"])
        p(f"Fuentes de ventaja: {moat['fuentes']}. Evidencia: {moat['evidencia']}. Criterio (Damodaran, *Investment Valuation*, "
          "cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el "
          "promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el Modelo JMR adopta como convención el punto medio entre "
          "ambos; esa cifra no es una regla universal de Damodaran. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del "
          "motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.")

    if su.get("smoothTerminalCapital"):
        p("Transición del capital nuevo: en años 6–10 se interpola la intensidad de capital (1/ventas-capital) desde el ancla de la segunda etapa hasta margen después de impuestos / ROIC terminal. En el año 10, la productividad del capital incremental coincide con el ROIC terminal de cada historia. Esto evita el salto de reinversión al año 11; no obliga al ROIC medio del capital instalado a converger en cinco años. La transición es un supuesto explícito del analista.")
    origen_calculo(r, W)
    cuatro_tesis(r, W)

    h3("Historias cuantificadas: DCF Base y DCF esperado")
    segs = list(sp["segmentos"].keys())
    same = abs(r["beta_prop"] - r["beta_hoja"]) < 0.005  # la hoja ya usa la beta propuesta: una sola columna
    con_roic = any((h.get("roic_terminal_usado") or 0) > 0 for h in r["historias"])
    roic_txt = lambda h: (pct(h["roic_terminal_usado"]) if (h.get("roic_terminal_usado") or 0) > 0 else "= costo de capital")  # noqa: E731
    rows = []
    for h in r["historias"]:
        crec = "; ".join(f"{k}: " + ", ".join(es(x * 100, 0) + "%" for x in h["crec"].get(k, [0] * 5)) for k in segs) if len(segs) > 1 else \
            ", ".join(es(x * 100, 0) + "%" for x in h["crec"][segs[0]])
        rows.append([f"**{nombre(h)}**", pct(h["prob"], 0), crec, pct(h["cagr"]), pct(h["margen"], 1),
                     es(h.get("s2c", r["s2c"]), 1)] + ([roic_txt(h)] if con_roic else []) + [pct(h["terminal_growth"], 2)] +
                    [usd(h["valor_beta_hoja"]) + (f" (DCF bruto {usd(h['valor_bruto'])})" if h.get("valor_bruto", 0) < 0 else "")] +
                    ([] if same else [usd(h["valor_beta_prop"])]))
    rows.append(["**DCF esperado (complemento)**", "100%", "", "", "", ""] + ([""] if con_roic else []) + [""] + [f"**{usd(r['valor_esperado_beta_hoja'])}**"] +
                ([] if same else [f"**{usd(r['valor_esperado_beta_prop'])}**"]))
    tab(["Historia", "Probabilidad", "Crecimiento por segmento (años 1-5)", "CAGR de ingresos del grupo (años 1–5)",
         "Margen objetivo", "Sales-to-capital"] + (["ROIC después del año 10"] if con_roic else []) + ["Crecimiento terminal"] +
        [f"Valor/acción (beta {es(r['beta_hoja'])})"] +
        ([] if same else [f"Valor/acción (beta {es(r['beta_prop'])})"]), rows,
        ["l", "r", "l", "r", "r", "r"] + (["r"] if con_roic else []) + ["r", "r"] + ([] if same else ["r"]))
    p(sp["prob_texto"] + " **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**")
    s = r["sensibilidad"]
    p(f"Sensibilidad del {'DCF Base' if hh else 'DCF técnico anterior'} (beta {es(r['beta_hoja'])}; US$ por acción; filas = crecimiento de los años 1-5, "
      "columnas = margen operativo objetivo):")
    p("Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; "
      "si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del " +
      ("DCF Base de la hoja." if hh else "DCF técnico anterior de la hoja."))
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
        if all(abs(x["beta"] - y) >= 0.02 for y in bs):  # la propuesta casi igual a la de la hoja no agrega una fila
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
    vb_ = central["valor_beta_hoja"]
    if r["precio"] and vb_ > 0:
        p(f"Frente al DCF Base ({usd(vb_)}), el valor intrínseco principal, el precio está {pos(r['precio'] / vb_ - 1)}.")
    if same:
        p(f"Frente al DCF esperado de las historias ({usd(r['valor_esperado_beta_hoja'])}), el complemento, el precio está {pos(diff_h)}. " + (sp["precio_lectura"].format_map(_cifras(r)) if "{" in sp["precio_lectura"] else sp["precio_lectura"]))
    else:
        p(f"Frente al DCF esperado de las historias ({usd(r['valor_esperado_beta_hoja'])} con la beta de la hoja; "
          f"{usd(r['valor_esperado_beta_prop'])} con la propuesta), el precio está {pos(diff_h)} y {pos(diff_p)}, respectivamente. " + (sp["precio_lectura"].format_map(_cifras(r)) if "{" in sp["precio_lectura"] else sp["precio_lectura"]))

    h3("Registro de decisión")
    probs = " / ".join(f"{NOMBRE[h['id']]} {pct(h['prob'], 0)}" for h in r["historias"])
    lo = min(min(h["valor_beta_hoja"], h["valor_beta_prop"]) for h in r["historias"])
    hi = max(max(h["valor_beta_hoja"], h["valor_beta_prop"]) for h in r["historias"])
    tab(["Campo", "Propuesta del análisis", "Tu estimación"], [
        ["Fecha", r["fecha"], ""],
        ["Historia en una frase", sp["frase"], ""],
        ["Probabilidades", probs, ""],
        ["DCF Base hoy (valor intrínseco principal)", usd(central["valor_beta_hoja"]), ""],
        ["DCF esperado por probabilidades (complemento)" + ("" if same else " (beta de la hoja / propuesta)"), usd(r['valor_esperado_beta_hoja']) + ("" if same else f" / {usd(r['valor_esperado_beta_prop'])}"), ""],
        ["Precio con MOS sobre el DCF esperado", usd(ve * (1 - mos)) + f" (MOS {pct(mos, 0)})" if isinstance(mos, (int, float)) else "—", ""],
        ["Rango (historia más débil a más fuerte)", f"{usd(lo)} a {usd(hi)}", ""],
        ["Confianza", sp["confianza"], ""],
        ["Qué cambiaría la opinión", sp["cambiaria"], ""],
        ["Revisión", sp["revision"], ""],
    ])
    p("La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no "
      "la toma por ti.")
    if sp.get("notas_historicas"):
        h3("Antecedentes de revisiones anteriores")
        p("Notas de revisiones previas, con las cifras de su fecha; las cifras vigentes son las de esta sección.")
        for titulo, texto in sp["notas_historicas"]:
            p(f"**{titulo}.** {texto}")
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
        previos = sorted((_ROOT / "data").glob(f"{tk}_Analisis_Damodaran_*.md"))
        if len(previos) == 1:  # el nombre del archivo (y de su copia en Drive) queda fijo aunque cambie la fecha del análisis
            out_md = previos[0]
        if r["spec"].get("md_propio"):
            out_md = REF / f"{tk}_seccion.md"  # hay un documento escrito a mano con ese nombre; no se pisa
        out_md.write_text(head + md)
        # Desde el 2-oct-2026 'Valuation output'!B35 es el DCF de la historia Base: el control es historia Base = hoja.
        # Las financieras siguen comparando el motor técnico con 'DCF FCFE financiero'!B42.
        A = next(h for h in r["historias"] if h["id"] == "A")["valor_beta_hoja"]
        ref, que = (r.get("motor_tecnico"), "el motor técnico") if r.get("financiero") else (A, "la historia Base")
        if isinstance(ref, (int, float)) and isinstance(r.get("dcf_base"), (int, float)) and abs(ref - r["dcf_base"]) > 0.01:
            print(f"{tk:5s} AVISO: {que} da {ref:.2f} y la hoja (VO B35 o FCFE financiero B42) {r['dcf_base']:.2f}"
                  + (" (con --offline, el DCF de la hoja guardado puede ser anterior: correr sin --offline)" if offline else ""),
                  flush=True)
        for aviso in avisos_coherencia(r):
            print(f"{tk:5s} AVISO: {aviso}", flush=True)
        print(f"{tk:5s} DCF {r['dcf_base']:.2f} | VE {r['valor_esperado_beta_hoja']:.2f} / {r['valor_esperado_beta_prop']:.2f} | "
              f"beta {r['beta_hoja']:.2f}→{r['beta_prop']:.2f} | " +
              " ".join(f"{h['id']}:{h['valor_beta_hoja']:.1f}" for h in r["historias"]), flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
