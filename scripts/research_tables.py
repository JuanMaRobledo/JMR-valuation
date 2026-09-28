"""Tablas numericas del research fundamental v4 leidas de la hoja de cada
posicion (scripts/pos_<ticker>.py): historia financiera, ratios, auditoria de
supuestos del Modelo JMR, multiplos historicos y resultados declarados.
Las cifras salen de la hoja (no se recalcula nada); el texto narrativo lo
escribe el analista en data/<TICKER>_Research_Fundamental_Modelo_JMR_v4_*.md
con marcadores {{TABLA_*}} que este modulo reemplaza."""
from __future__ import annotations

import importlib
import statistics
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402
import posiciones_ibkr  # noqa: E402,F401  (reintentos 429)

U = "UNFORMATTED_VALUE"


def _n(v, d=0):
    if v in ("", None) or isinstance(v, str):
        return "n.d."
    s = f"{v:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def _p(v, d=1):
    if v in ("", None) or isinstance(v, str):
        return "n.d."
    return _n(v * 100, d) + "%"


def _x(v, d=1):
    if v in ("", None) or isinstance(v, str) or v <= 0:
        return "n.s."
    return _n(v, d) + "x"


class Data:
    def __init__(self, ticker: str):
        self.c = importlib.import_module(f"pos_{ticker.lower()}")
        sh = ms.open_sheet(self.c.SHEET_ID)
        rng = ["'Income Statement'!A1:L30", "'Balance Sheet'!A1:L36", "'Cash Flow Statement'!A1:L40",
               "'Trailing Valuation'!A1:L24", "'Input sheet'!A1:D50", "'Cost of capital worksheet'!A1:C40",
               "'Valuation output'!A1:F140", "'Resumen de Valoración'!A1:G26", "'Supuestos de los Múltiplos'!A5:F10",
               "'Eficiencia de capital'!A1:L12", "'Salud Financiera'!A1:L15", "'Márgenes'!A1:L12"]
        res = sh.values_batch_get(rng, params={"valueRenderOption": U})["valueRanges"]
        (self.IS, self.BS, self.CF, self.TV, self.INP, self.COC, self.VO, self.RES, self.MULT,
         self.EF, self.SF, self.MG) = [r.get("values", []) for r in res]

    def row(self, tbl, label):
        found = [""] * 11
        for r in tbl:  # la ultima fila con esa etiqueta y datos gana (p.ej. 'Free Cash Flow' es titulo y fila)
            if r and str(r[0]).strip() == label and len(r) > 1:
                found = (r + [""] * 12)[1:12]
        return found

    def years(self):
        return (self.IS[1] + [""] * 12)[1:12]

    def cell(self, tbl, ref):
        col = ord(ref[0]) - 65
        row = int(ref[1:]) - 1
        try:
            return tbl[row][col]
        except IndexError:
            return ""


def tabla_hist(d: Data) -> str:
    ys = d.years()
    idx = [i for i, y in enumerate(ys) if y not in ("", "—")]
    rev, gm, om = d.row(d.IS, "Total Revenues"), d.row(d.IS, "Gross Profit Margin"), d.row(d.IS, "Operating Margin")
    ni = d.row(d.IS, "Net Income Attributable to Common Shareholders")
    eps = d.row(d.IS, "Diluted EPS")
    sh = d.row(d.IS, "Diluted Weighted Average Shares Outstanding")
    ocf, fcf = d.row(d.CF, "Cash from Operating Activities"), d.row(d.CF, "Free Cash Flow")
    sbc = d.row(d.CF, "Share-Based Compensation Expense")
    bb, dv = d.row(d.CF, "Repurchases of Common Shares"), d.row(d.CF, "Common Share Dividends Paid")
    cash = d.row(d.BS, "Total Cash and Cash Equivalents")
    debt = [sum(x for x in (a, b, c) if isinstance(x, (int, float)))
            for a, b, c in zip(d.row(d.BS, "Short-Term Debt"), d.row(d.BS, "Long-Term Debt"), d.row(d.BS, "Leases"))]
    head = "| Concepto (US$ millones) | " + " | ".join(str(ys[i]) for i in idx) + " |\n|---|" + "---:|" * len(idx) + "\n"
    lines = [
        ("Ingresos", rev, _n), ("Margen bruto", gm, _p), ("Margen operativo", om, _p), ("Utilidad neta", ni, _n),
        ("EPS diluido (US$)", eps, lambda v: _n(v, 2)), ("Acciones diluidas promedio (M)", sh, lambda v: _n(v, 1)),
        ("Flujo operativo", ocf, _n), ("Flujo de caja libre", fcf, _n), ("Compensación en acciones", sbc, _n),
        ("Recompras", bb, lambda v: _n(abs(v)) if isinstance(v, (int, float)) else "n.d."),
        ("Dividendos", dv, lambda v: _n(abs(v)) if isinstance(v, (int, float)) else "n.d."),
        ("Caja e inversiones CP", cash, _n), ("Deuda + arrendamientos (balance)", debt, _n),
    ]
    body = "".join(f"| {n} | " + " | ".join(f(vals[i]) for i in idx) + " |\n" for n, vals, f in lines)
    return head + body


def _avg(vals):
    v = [x for x in vals if isinstance(x, (int, float))]
    return statistics.mean(v) if v else ""


def tabla_ratios(d: Data) -> str:
    rev = d.row(d.IS, "Total Revenues")
    g = d.row(d.IS, "Total Revenues %Chg")
    gm, om = d.row(d.IS, "Gross Profit Margin"), d.row(d.IS, "Operating Margin")
    fcf = d.row(d.CF, "Free Cash Flow")
    fcfm = [f / r if isinstance(f, (int, float)) and isinstance(r, (int, float)) and r else "" for f, r in zip(fcf, rev)]
    roic = d.row(d.EF, "Return on Invested Capital")
    roe = d.row(d.EF, "Return on Equity")
    ebitda = d.row(d.IS, "EBITDA")
    netdebt = []
    for s, lt, le, c in zip(d.row(d.BS, "Short-Term Debt"), d.row(d.BS, "Long-Term Debt"), d.row(d.BS, "Leases"),
                            d.row(d.BS, "Total Cash and Cash Equivalents")):
        vals = [x for x in (s, lt, le) if isinstance(x, (int, float))]
        netdebt.append(sum(vals) - (c if isinstance(c, (int, float)) else 0) if vals else "")
    nd_eb = [n / e if isinstance(n, (int, float)) and isinstance(e, (int, float)) and e > 0 else "" for n, e in zip(netdebt, ebitda)]
    op = d.row(d.IS, "Operating Profit")
    intr = d.row(d.IS, "Interest Expense, Net")
    cov = [o / i if isinstance(o, (int, float)) and isinstance(i, (int, float)) and i > 0 else "" for o, i in zip(op, intr)]

    def line(name, vals, fmt, defin, hist_only=True):
        h = vals[:10]
        ltm = vals[10] if isinstance(vals[10], (int, float)) and name != "Crecimiento de ingresos" else h[-1]
        a3, a5, a10 = _avg(h[-3:]), _avg(h[-5:]), _avg(h)
        n10 = len([x for x in h if isinstance(x, (int, float))])
        trend = "n.d."
        if isinstance(a3, (int, float)) and isinstance(a5, (int, float)):
            trend = "al alza" if a3 > a5 * 1.03 else ("a la baja" if a3 < a5 * 0.97 else "estable")
        return f"| {name} | {fmt(ltm)} | {fmt(a3)} | {fmt(a5)} | {fmt(a10)} ({n10} obs.) | {trend} | {defin} |\n"

    head = ("| Métrica | LTM o último año | Promedio 3 años | Promedio 5 años | Promedio 10 años | Dirección | "
            "Calidad de la definición |\n|---|---:|---:|---:|---:|---|---|\n")
    return head + "".join([
        line("Crecimiento de ingresos", g, _p, "Variación anual de ingresos reportados; el LTM de la hoja no es una tasa anual."),
        line("Margen bruto", gm, _p, "Utilidad bruta / ingresos (depende de cómo cada emisor clasifica costo de ventas)."),
        line("Margen operativo", om, _p, "EBIT GAAP/IFRS reportado / ingresos; promedio simple de ratios anuales."),
        line("Margen FCF", fcfm, _p, "(Flujo operativo − capex) / ingresos; no descuenta compensación en acciones."),
        line("ROE", roe, _p, "Utilidad neta / patrimonio ('Eficiencia de capital' de la hoja)."),
        line("ROIC", roic, _p, "NOPAT / capital invertido de la hoja; incluye goodwill cuando existe."),
        line("Deuda neta / EBITDA", nd_eb, lambda v: _x(v, 1) if isinstance(v, (int, float)) else "n.d.",
             "(Deuda + arrendamientos − caja) / EBITDA; 'n.s.' = caja neta o EBITDA negativo."),
        line("Cobertura de intereses", cov, lambda v: _x(v, 1) if isinstance(v, (int, float)) else "n.d.",
             "EBIT / gasto por intereses neto; 'n.d.' si no hay gasto por intereses."),
    ])


def tabla_auditoria(d: Data) -> str:
    c = d.c
    I = lambda r: d.cell(d.INP, r)  # noqa: E731
    C = lambda r: d.cell(d.COC, r)  # noqa: E731
    V = lambda r: d.cell(d.VO, r)  # noqa: E731
    rows = [
        ("Ingresos base (LTM)", f"US${_n(I('B12'))}M", "Dato reportado; activo", "Input sheet!B12 (SEC EDGAR/XBRL)",
         "Conciliado con los estados de la hoja", "Alta: base de toda la proyección"),
        ("Margen operativo base", _p(V('B6')), "Cálculo derivado; activo", "Valuation output!B6",
         "Conciliado con 'Income Statement' LTM", "Alta"),
        ("Crecimiento Año 1 (Base)", _p(I('B27')), "Entrada manual; activo", "Input sheet!B27 (analista, 28-sep-2026)",
         "Justificado en 'Tesis de Inversión y Supuestos'", "Alta"),
        ("Crecimiento años 2-5 (Base)", _p(I('B29')), "Entrada manual; activo", "Input sheet!B29",
         "Justificado en la Tesis; sin guía cuantitativa verificada salvo donde se cita", "Alta"),
        ("Margen objetivo (C / B / O)", f"{_p(V('C45'))} / {_p(V('C46'))} / {_p(V('C47'))}", "Entrada manual; activo",
         "Valuation output!C45:C47; Input sheet!B30", "Orden verificado C < B < O", "Alta"),
        ("Crecimiento años 1-5 Conservador / Optimista", f"{_p(V('C55'))} / {_p(V('C106'))}", "Entrada manual; activo",
         "Valuation output!C55 y C106", "Orden verificado", "Media"),
        ("Sales-to-capital (1-5 / 6-10)", f"{_n(I('B32'), 1)}x / {_n(I('B33'), 1)}x", "Entrada manual; activo",
         "Input sheet!B32:B33", "Elección razonable, no documentada por la empresa", "Media"),
        ("Tasa impositiva efectiva / marginal", f"{_p(I('B24'))} / {_p(I('B25'))}", "Dato reportado / entrada manual",
         "Input sheet!B24:B25", "Efectiva LTM conciliada; marginal = supuesto", "Media"),
        ("Beta", f"{_n(C('B23'), 2)} ({C('B22')})", "Entrada manual; activo", "Cost of capital worksheet!B22:B23",
         "Beta observado aproximado; no hay regresión documentada en el libro", "Media"),
        ("ERP y tasa libre de riesgo", f"{_p(C('B28'), 2)} / {_p(C('B25'), 2)}", "Referencia de mercado; activo",
         "Cost of capital worksheet!B25:B28 (Damodaran; UST 10 años)", "Conciliado con las tablas de la hoja", "Media"),
        ("Calificación / costo de deuda", f"{C('B36')} / {_p(C('B38'), 2)}", "Entrada manual; activo",
         "Cost of capital worksheet!B34:B38", "Ver justificación en 'Tesis'", "Baja"),
        ("WACC", _p(C('B14'), 2), "Cálculo derivado; activo", "Cost of capital worksheet!B14", "Recalculado por la hoja",
         "Alta"),
        ("WACC terminal", _p(I('B47'), 1) if str(I('B46')).strip() == "Yes" else "regla por defecto",
         "Entrada manual; activo", "Input sheet!B46:B47", "Prima sobre ERP maduro; no documentada por la empresa", "Media"),
        ("Deuda / caja usadas", f"US${_n(I('B16'))}M / US${_n(I('B19'))}M", "Dato reportado (con ajustes)",
         "Input sheet!B16 y B19", "Ver notas de deuda y arrendamientos en la hoja", "Media"),
        ("Acciones", f"{_n(I('B22'), 1)} M", "Dato reportado (con ajustes)", "Input sheet!B22", "Ver notas de dilución",
         "Media"),
        ("Categoría y ponderaciones", str(d.cell(d.RES, 'G3')), "Entrada manual; activo",
         "Resumen de Valoración!G3 (tabla I5:U11)", "Coherente con el perfil de la empresa", "Media"),
        ("Margen de seguridad", _p(d.cell(d.RES, 'G4'), 0), "Valor predeterminado del modelo", "Resumen de Valoración!G4",
         "Sin cambio", "Baja"),
    ]
    head = ("| Dato o supuesto | Valor del modelo y unidad | Tipo de origen y actividad | Fuente, fecha, hoja y celda | "
            "Resultado del contraste | Prioridad e incidencia cualitativa |\n|---|---|---|---|---|---|\n")
    return head + "".join("| " + " | ".join(r) + " |\n" for r in rows)


def tabla_multiplos(d: Data) -> str:
    ys = d.years()
    idx = [i for i, y in enumerate(ys) if y not in ("", "—")]
    names = [("P/E", "P/E"), ("P/OCF", "P/OCF"), ("P/FCF", "P/FCF"), ("EV/EBITDA", "EV/EBITDA"), ("EV/Sales", "EV/Sales")]
    head = "| Múltiplo (al cierre fiscal) | " + " | ".join(str(ys[i]) for i in idx) + " |\n|---|" + "---:|" * len(idx) + "\n"
    body = ""
    for lab, key in names:
        vals = d.row(d.TV, key)
        body += f"| {lab} | " + " | ".join(_x(vals[i]) for i in idx) + " |\n"
    anchor = "".join(f"| {r[0]} | {_x(r[1])} | {_x(r[2])} | {_x(r[3])} | {r[4] if len(r) > 4 else ''} |\n" for r in d.MULT[1:6])
    return (head + body + "\nPrecio de cierre de cada ejercicio (yfinance) × acciones de la hoja; EV = capitalización + deuda + "
            "arrendamientos − caja. 'n.s.' = no significativo (denominador negativo).\n\n"
            "| Múltiplo de salida FY+3 | Conservador | Base | Optimista | Override manual |\n|---|---:|---:|---:|---|\n" + anchor)


def tabla_resultados(d: Data) -> str:
    res = d.RES
    rows = [r for r in res[5:12] if r]
    head = "| Método | Peso | Conservador | Base | Optimista |\n|---|---:|---:|---:|---:|\n"
    body = "".join(f"| {r[0]} | {_p(r[1], 0)} | US${_n(r[2], 2)} | US${_n(r[3], 2)} | US${_n(r[4], 2)} |\n" for r in rows)
    dcf = [d.cell(d.VO, x) for x in ("B86", "B35", "B137")]
    extra = (f"| DCF (valor intrínseco hoy, por acción) | — | US${_n(dcf[0], 2)} | US${_n(dcf[1], 2)} | US${_n(dcf[2], 2)} |\n"
             f"| CAGR a 3 años desde el precio del análisis | — | {_p(d.cell(res, 'C13'))} | {_p(d.cell(res, 'D13'))} | "
             f"{_p(d.cell(res, 'E13'))} |\n")
    note = (f"\nPrecio del análisis: US${_n(d.cell(res, 'C25'), 2)} (cierre del 25-sep-2026). Los valores por método son "
            "precios a 3 años (FY+3): el DCF se lleva a 3 años con (1+Ke)³ y los múltiplos suman dividendos acumulados; "
            "la fila 'valor intrínseco hoy' es el DCF sin llevar a 3 años ('Valuation output'!B86/B35/B137). Resultados "
            "declarados por el Modelo JMR del usuario; este informe no los recalcula.\n")
    return head + body + extra + note


def render(ticker: str, template: str) -> str:
    d = Data(ticker)
    for k, fn in {"TABLA_HIST": tabla_hist, "TABLA_RATIOS": tabla_ratios, "TABLA_AUDITORIA": tabla_auditoria,
                  "TABLA_MULTIPLOS": tabla_multiplos, "TABLA_RESULTADOS": tabla_resultados}.items():
        if "{{" + k + "}}" in template:
            template = template.replace("{{" + k + "}}", fn(d).rstrip("\n"))
    return template


if __name__ == "__main__":
    t = sys.argv[1]
    d = Data(t)
    for fn in (tabla_hist, tabla_ratios, tabla_auditoria, tabla_multiplos, tabla_resultados):
        print(fn(d))
