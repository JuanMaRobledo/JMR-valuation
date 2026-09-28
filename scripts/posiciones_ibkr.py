#!/usr/bin/env python
"""Motor generico para valorar las posiciones de IBKR que todavia no tenian
valoracion en Modelo JMR (28-sep-2026). Mismo proceso que run_nvidia.py /
run_google.py (refresh SEC EDGAR -> supuestos -> contenido), pero con los
datos y textos de cada empresa en un modulo de configuracion
`scripts/pos_<ticker>.py` en vez de un par run_X.py + X_content.py por
empresa.

Cada hoja es una copia NUEVA de la plantilla maestra auditada
(Modelo_JMR_Plantilla_Maestra, 19PRUF...) hecha en Drive dentro de
Análisis/<TICKER>/ y compartida con la cuenta de servicio; nunca la hoja de
otra empresa.

Pasos: refresh | assumptions | content | check   (--step all corre todos)
Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts \
        python scripts/posiciones_ibkr.py INTU --step all
"""
from __future__ import annotations

import argparse
import importlib
import sys
from datetime import date
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402
import refresh_native_model as rnm  # noqa: E402


def _install_429_retry() -> None:
    """Varias empresas seguidas superan el limite de 'Write/Read requests per
    minute per user' de la API de Sheets (429). Reintenta cualquier request
    de gspread con espera creciente en vez de abortar a mitad de un paso."""
    import time

    from gspread.exceptions import APIError
    from gspread.http_client import HTTPClient

    original = HTTPClient.request
    if getattr(original, "_retry429", False):
        return

    def request(self, *args, **kwargs):
        for i in range(8):
            try:
                return original(self, *args, **kwargs)
            except APIError as exc:
                if "429" not in str(exc) and "503" not in str(exc) or i == 7:
                    raise
                time.sleep(20 * (i + 1))

    request._retry429 = True  # type: ignore[attr-defined]
    HTTPClient.request = request  # type: ignore[method-assign]


_install_429_retry()

VALUATION_DATE = date(2026, 9, 25)  # ultimo cierre disponible (viernes) antes del analisis del 28-sep-2026

VO, INP, COC, RES = "'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'"

WEIGHTS = {
    "Madura": "DCF (40%) con 5 múltiplos (EV/EBITDA 20%, P/E 20%, EV/FCFF 10%, P/FCFE 5%, P/OCF 5%)",
    "Crecimiento": "DCF (60%) con 5 múltiplos (EV/FCFF 15%, EV/EBITDA 10%, P/E 5%, P/FCFE 5%, P/OCF 5%)",
    "Genérico": "DCF (50%) con 5 múltiplos (10% cada uno)",
    "Defensiva": "DCF (30%) con 5 múltiplos (P/E 25%, EV/EBITDA 20%, EV/FCFF 10%, P/FCFE 10%, P/OCF 5%)",
    "Software": "DCF (60%) con 5 múltiplos (EV/FCFF 15%, EV/EBITDA 10%, P/E 5%, P/FCFE 5%, P/OCF 5%)",
    "Financiera": "DCF (40%) con P/E 35%, P/FCFE 20% y P/OCF 5% (sin múltiplos de EV)",
}


def cfg_for(ticker: str):
    return importlib.import_module(f"pos_{ticker.lower()}")


def backup_path(c) -> Path:
    return _ROOT / "reference" / "backups" / f"{c.TICKER.lower()}_formula_backup.json"


# ---------------------------------------------------------------------------
# Pasos
# ---------------------------------------------------------------------------

def step_refresh(c) -> None:
    sh = ms.open_sheet(c.SHEET_ID)
    # Fecha del analisis ANTES del refresh: el paso 11 congela en 'Resumen de
    # Valoración' el cierre real de esa fecha (no el de la plantilla, 14-sep).
    ms.write_with_backup(sh, "Input sheet", {"B4": ms.serial(VALUATION_DATE)},
                         f"Fecha del analisis {VALUATION_DATE.isoformat()}", backup_path(c))
    if getattr(c, "CUSTOM_REFRESH", None):
        c.CUSTOM_REFRESH()
        return
    ms.install_augmented_client(c.TICKER, getattr(c, "CUSTOM_TAG_MAP", None))
    if getattr(c, "SPLITS", None):
        _install_split_adjustment(c.SPLITS)
    if getattr(c, "DEBT_TAGS", None):
        _install_debt_tags(c.TICKER, c.DEBT_TAGS)
    if getattr(c, "EBIT_FROM_PRETAX", False):
        _install_ebit_from_pretax(c.TICKER)
    if getattr(c, "DEBT_LTM", None) is not None:
        _install_debt_ltm(c.TICKER, c.DEBT_LTM)
    rnm.run(c.TICKER, sheet_id=c.SHEET_ID, peer_tickers=c.PEERS, industry_us=c.INDUSTRY,
            industry_global=getattr(c, "INDUSTRY_GLOBAL", c.INDUSTRY))
    if getattr(c, "POST_REFRESH", None):
        c.POST_REFRESH(ms.open_sheet(c.SHEET_ID), backup_path(c))


def _install_split_adjustment(splits: list[tuple[str, float]]) -> None:
    """El loader SEC deja cada ejercicio con las acciones tal como se reportaron;
    un split (CMG 50:1 en jun-2024) hace que los ejercicios anteriores tengan
    acciones 50x menores y EPS/multiplos historicos absurdos (el precio de
    yfinance si viene ajustado). Reescala las series de acciones de los
    ejercicios cerrados ANTES de cada split."""
    from dataclasses import replace

    original = rnm.load_annual_series_from_sec_edgar

    def load(ticker, *a, **k):
        s = original(ticker, *a, **k)
        fields = {}
        for name in ("shares_outstanding", "diluted_shares_avg", "basic_shares_avg"):
            vals = list(getattr(s, name) or [])
            for when, factor in splits:
                vals = [v * factor if fy < when else v for v, fy in zip(vals, s.fiscal_year_ends)]
            fields[name] = vals
        return replace(s, **fields)

    rnm.load_annual_series_from_sec_edgar = load


def _install_debt_tags(ticker: str, tags: dict[str, str]) -> None:
    """Algunos emisores cambian de tag de deuda entre ejercicios y el loader
    toma uno residual (DPZ: 'LongTermDebt' = US$15M en 2024-2025, cuando la
    deuda titulizada esta en 'LongTermDebtAndCapitalLeaseObligations'). Pisa
    la serie historica con el tag indicado, cierre por cierre."""
    from dataclasses import replace

    from jmr_valuation.io.sec_edgar_client import SecEdgarClient

    facts = SecEdgarClient().company_facts(ticker)["facts"]["us-gaap"]
    by_end = {field: {r["end"]: r["val"] for r in facts[tag]["units"]["USD"] if r.get("form") == "10-K"}
              for field, tag in tags.items()}
    original = rnm.load_annual_series_from_sec_edgar

    def load(tk, *a, **k):
        s = original(tk, *a, **k)
        if tk.upper() != ticker.upper():
            return s
        fields = {f: [by_end[f].get(fy, v) for v, fy in zip(getattr(s, f), s.fiscal_year_ends)] for f in tags}
        if "dividends_paid" in tags and fields["dividends_paid"]:
            # Sin el tag en los 10-Q: el LTM de dividendos = ultimo ejercicio (aproximacion).
            fields["ltm_dividends_paid"] = fields["dividends_paid"][-1]
        return replace(s, **fields)

    rnm.load_annual_series_from_sec_edgar = load


def _install_ebit_from_pretax(ticker: str) -> None:
    """Emisores que no reportan 'OperatingIncomeLoss' en XBRL (ZTS): el loader
    deja EBIT = 0. Se reconstruye EBIT = utilidad antes de impuestos + gasto
    por intereses (el resto de 'otros ingresos/gastos' es inmaterial)."""
    from dataclasses import replace

    orig_series = rnm.load_annual_series_from_sec_edgar
    orig_inputs = rnm.load_company_inputs_from_sec_edgar

    def load_series(tk, *a, **k):
        s = orig_series(tk, *a, **k)
        if tk.upper() != ticker.upper():
            return s
        ebit = [p + i for p, i in zip(s.pretax_income, s.interest_expense)]
        return replace(s, ebit=ebit, ltm_ebit=s.ltm_pretax_income + s.ltm_interest_expense)

    def load_inputs(tk, *a, **k):
        ci = orig_inputs(tk, *a, **k)
        if tk.upper() != ticker.upper():
            return ci
        s = load_series(tk)
        ltm = (s.ltm_pretax_income + s.ltm_interest_expense) / 1e6
        prior = (s.pretax_income[-1] + s.interest_expense[-1]) / 1e6
        m = [e / r for e, r in zip(s.ebit, s.revenue) if r]
        return replace(ci, ebit_ltm=ltm, ebit_prior_10k=prior, ebit_margin_ltm=ltm / ci.revenue_ltm,
                       ebit_margin_avg_3y=sum(m[-3:]) / 3, ebit_margin_avg_5y=sum(m[-5:]) / 5,
                       ebit_margin_avg_10y=sum(m) / len(m))

    rnm.load_annual_series_from_sec_edgar = load_series
    rnm.load_company_inputs_from_sec_edgar = load_inputs


def _install_debt_ltm(ticker: str, debt_musd: float) -> None:
    """Deuda financiera LTM (US$ millones, del 10-Q/10-K) para el Input sheet y
    los multiplos LTM cuando el loader no la encuentra bien (ver DEBT_TAGS)."""
    from dataclasses import replace

    original = rnm.load_company_inputs_from_sec_edgar

    def load(tk, *a, **k):
        ci = original(tk, *a, **k)
        if tk.upper() != ticker.upper():
            return ci
        return replace(ci, book_value_debt_ltm=debt_musd, book_value_debt_prior_10k=debt_musd)

    rnm.load_company_inputs_from_sec_edgar = load


def step_assumptions(c) -> None:
    sh = ms.open_sheet(c.SHEET_ID)
    bk = backup_path(c)
    a = c.BASE
    ms.write_with_backup(sh, "Input sheet", {
        "B17": a.get("rd", "No"), "B18": a.get("leases", "No"),
        "B27": a["g1"], "B28": a["m1"], "B29": a["g25"], "B30": a["mt"], "B31": a.get("conv", 5),
        "B32": a["s2c1"], "B33": a["s2c2"], "B25": a["tax"],
        "B46": "Yes" if a.get("wacc_term") else "No", **({"B47": a["wacc_term"]} if a.get("wacc_term") else {}),
        **getattr(c, "INPUT_EXTRA", {}),
    }, f"Supuestos {c.TICKER} Base (ver hoja Tesis de Inversión y Supuestos)", bk)
    ms.write_with_backup(sh, "Cost of capital worksheet", c.COC, f"Costo de capital {c.TICKER}", bk)
    s = c.SCEN
    ms.write_with_backup(sh, "Valuation output", {
        "C45": s["mt_cons"], "C46": a["mt"], "C47": s["mt_opt"], "C55": s["g1_cons"], "C106": s["g1_opt"],
        **getattr(c, "VO_EXTRA", {}),
    }, f"Escenarios {c.TICKER}: orden Conservador < Base < Optimista", bk)
    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": c.CATEGORY}, f"Tipo de empresa {c.TICKER}", bk)
    if getattr(c, "MULT_ANCHOR", None) == "LTM":
        # Override manual (columna J del bloque Base) = multiplo LTM vivo al dia del
        # analisis, para empresas re-valuadas con fuerza en 2026: la mediana de los
        # ultimos cierres fiscales refleja un multiplo que el mercado ya no paga.
        # Conservador/Optimista siguen siendo x0,9 / x1,1 del Base.
        for sheet, row in MULT_ROWS.items():
            ms.write_with_backup(sh, sheet, {"J19": f"='Trailing Valuation'!L{row}"},
                                 f"Ancla de multiplo {sheet} = LTM ({c.TICKER} re-valuada en 2026)", bk)
    for sheet, cells in getattr(c, "SHEET_EXTRA", {}).items():
        ms.write_with_backup(sh, sheet, cells, f"Ajuste puntual {sheet} ({c.TICKER}, ver pos_{c.TICKER.lower()}.py)", bk)
    for sheet, value in getattr(c, "MULT_OVERRIDE", {}).items():
        # Override manual numerico (utilidad GAAP distorsionada por cargos no recurrentes:
        # ni la historia ni el LTM sirven de ancla). Justificado en MULTIPLOS_EVALUACION.
        ms.write_with_backup(sh, sheet, {"J19": value}, f"Multiplo Base {sheet} manual ({c.TICKER})", bk)


# Fila de 'Trailing Valuation' de cada multiplo (misma que usa 'Supuestos de los Múltiplos'!F6:F10).
MULT_ROWS = {"EVFCFF": 24, "POCF": 15, "PE": 13, "PFCFE": 16, "EVEBITDA": 21}


def _estadisticas(c) -> dict:
    div = getattr(c, "DIVIDEND", False)
    d = {
        "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
        "B7": "='Income Statement'!L3", "B8": c.EMPLOYEES,
        "B12": "='Income Statement'!L30", "B13": "='Income Statement'!L13",
        "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
        "B16": "='Márgenes'!L9",
        "B21": "='Eficiencia de capital'!L5", "B23": "='Eficiencia de capital'!L3",
        "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
        "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
        "E12": "='Resumen de Valoración'!D12",
        "E13": "=PE!F19", "E14": "=IFERROR(E4/('Input sheet'!B29*100);\"\")",
        "E15": "N/D", "E16": "=IFERROR('Trailing Valuation'!L6/'Financials Multiples'!E57;\"\")", "E17": "N/D",
        "E20": "='Balance Sheet'!L5",
        "E21": "='Input sheet'!B16-'Input sheet'!B19",
        "E22": "=IFERROR('Input sheet'!B16/'Input sheet'!B15;\"\")",
        "E23": "=IFERROR('Income Statement'!L12/'Income Statement'!L16;\"\")",
        "H4": "=IF('Income Statement'!H3<=0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1;\"\"))",
        "H5": "=IF('Income Statement'!F3<=0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1;\"\"))",
        "H6": "=IF('Income Statement'!B3<=0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K3/'Income Statement'!B3)^(1/9)-1;\"\"))",
        "H7": "=IF('Income Statement'!H24<=0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K24/'Income Statement'!H24)^(1/3)-1;\"\"))",
        "H8": "=IF('Income Statement'!F24<=0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K24/'Income Statement'!F24)^(1/5)-1;\"\"))",
        "H9": "=IF('Income Statement'!B24<=0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K24/'Income Statement'!B24)^(1/9)-1;\"\"))",
        "H10": "=IF('Cash Flow Statement'!F36<=0;\"N/A (base negativa)\";IFERROR(('Cash Flow Statement'!K36/'Cash Flow Statement'!F36)^(1/5)-1;\"\"))",
        "H11": "=IF('Income Statement'!F26<=0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K26/'Income Statement'!F26)^(1/5)-1;\"\"))",
        "H12": "N/D (guía externa; sin dato verificado para esta empresa)",
        "H13": "N/D (guía externa; sin dato verificado para esta empresa)",
        "H14": "N/D (guía externa; sin dato verificado para esta empresa)",
        "H15": "N/D (guía externa; sin dato verificado para esta empresa)",
        "H24": "N/D",
    }
    if div:
        d.update({
            "H18": "=IFERROR(Dividendos!L4/'Input sheet'!D1;\"\")", "H19": "=Dividendos!L5", "H20": "=Dividendos!L4",
            "H21": "=IFERROR((Dividendos!K4/Dividendos!H4)^(1/3)-1;\"N/D\")",
            "H22": "=IFERROR((Dividendos!K4/Dividendos!F4)^(1/5)-1;\"N/D\")",
            "H23": "=IFERROR((Dividendos!K4/Dividendos!B4)^(1/9)-1;\"N/D\")",
        })
    else:
        nd = f"N/D ({c.SHORT} no paga dividendo)"
        d.update({k: nd for k in ("H18", "H19", "H20", "H21", "H22", "H23")})
    return d


def _format_estadisticas(sh) -> None:
    est = sh.worksheet("Estadísticas")
    pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
    num = {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}
    mult = {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}
    cur = {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}
    est.batch_format([
        {"range": "B4:B8", "format": num}, {"range": "B11:B16", "format": pct}, {"range": "B19:B23", "format": pct},
        {"range": "E4:E9", "format": mult}, {"range": "E13:E17", "format": mult}, {"range": "E12", "format": cur},
        {"range": "E20:E21", "format": num}, {"range": "E22:E23", "format": mult},
        {"range": "H4:H15", "format": pct}, {"range": "H18:H19", "format": pct}, {"range": "H20", "format": cur},
        {"range": "H21:H24", "format": pct},
    ])


def _cualitativo(c) -> dict:
    q = c.CUALI
    d = {"B5": c.COMPANY, "B6": q["ceo"], "B7": q["sector"], "B8": q["web"], "B11": "Descripción",
         "B12": q["overview"], "B21": "Argumento", "B27": "Riesgo",
         "A32": c.SOURCES}
    for (row, (title, text)) in zip((13, 14, 15, 16), q["segments"]):
        d[f"A{row}"], d[f"B{row}"] = title, text
    for (row, (title, text)) in zip((22, 23, 24), q["bulls"]):
        d[f"A{row}"], d[f"B{row}"] = title, text
    for (row, (title, text)) in zip((28, 29, 30), q["bears"]):
        d[f"A{row}"], d[f"B{row}"] = title, text
    return d


def _stories(c) -> dict:
    s = c.STORY
    return {"A3": s["title"], "A4": s["text"], "G10": s["g"], "G11": s["m"], "G12": s["tax"],
            "G13": s["s2c"], "G14": s["roic"], "G15": s["wacc"]}


def _recomendados(c) -> dict:
    a, r = c.BASE, c.RECO
    return {"C6": a["g1"], "D6": r["g1"], "C7": a["m1"], "D7": r["m1"], "C8": a["g25"], "D8": r["g25"],
            "C9": a["mt"], "D9": r["mt"], "C10": a.get("conv", 5), "D10": r.get("conv", "Horizonte estándar de convergencia del modelo."),
            "C11": a["s2c1"], "D11": r["s2c1"], "C12": a["s2c2"], "D12": r["s2c2"]}


def _tesis_rows(c) -> list[list]:
    t = c.TESIS
    rows: list[list] = [
        [f"{c.TICKER} ({c.COMPANY}) — Tesis de Inversión: De la Historia a los Números"],
        [f'="Metodología Damodaran (NYU Stern) | Precio al día del análisis: US$"&TEXT({RES}!C25;"0.00")&" | WACC: "&TEXT({COC}!B14;"0.00%")'],
        [],
        ["1. LA HISTORIA"],
        [t["historia"]],
        [],
        ["Caso alcista (Bull)", "Caso bajista (Bear)"],
        *[[b, r] for b, r in t["bull_bear"]],
        [],
        ["2. DE LA HISTORIA A LOS NÚMEROS — LOS TRES ESCENARIOS (fórmulas vivas del modelo)"],
        ["Supuesto", "Conservador", "Base", "Optimista", "Justificación y fuente (dato real)"],
        ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={INP}!B27", f"={VO}!C106", t["j_g1"]],
        ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={INP}!B29", f"={VO}!D106", t["j_g25"]],
        ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108", t["j_m1"]],
        ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47", t["j_mt"]],
        ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31", t.get("j_conv", "5 años: horizonte estándar del modelo.")],
        ["Sales-to-Capital (años 1-5 / 6-10)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32", t["j_s2c"]],
        ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14", t["j_wacc"]],
        ["Referencia: margen base (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6", t["j_mbase"]],
        [],
        ["3. RESULTADO DEL DCF POR ESCENARIO"],
        ["Escenario", "Valor DCF / acción", "Precio Objetivo Ponderado*", "DCF vs. precio del análisis", "Ponderado vs. precio del análisis"],
    ]
    r0 = len(rows) + 1  # fila de Conservador
    rows += [
        ["Conservador", f"={VO}!B86", f"={RES}!C12", f"=B{r0}/{RES}!$C$25-1", f"=C{r0}/{RES}!$C$25-1"],
        ["Base", f"={VO}!B35", f"={RES}!D12", f"=B{r0+1}/{RES}!$C$25-1", f"=C{r0+1}/{RES}!$C$25-1"],
        ["Optimista", f"={VO}!B137", f"={RES}!E12", f"=B{r0+2}/{RES}!$C$25-1", f"=C{r0+2}/{RES}!$C$25-1"],
        ["Precio del análisis (cierre)", f"={RES}!C25"],
        [f'=IF(AND(B{r0}<B{r0+1};B{r0+1}<B{r0+2};C{r0}<C{r0+1};C{r0+1}<C{r0+2};{VO}!C55<{INP}!B27;{INP}!B27<{VO}!C106;{VO}!C45<{VO}!C46;{VO}!C46<{VO}!C47);"✔ Orden verificado: Conservador < Base < Optimista en crecimiento, margen objetivo, valor DCF y precio ponderado";"✖ REVISAR: el orden Conservador < Base < Optimista no se cumple")'],
        [f"*El Precio Objetivo Ponderado combina el {WEIGHTS[c.CATEGORY]} según la categoría '{c.CATEGORY}' "
         f"de 'Resumen de Valoración'!G3. {t['nota_multiplos']}"],
        [],
        ["4. CONCLUSIÓN"],
        [f'="A US$"&TEXT({RES}!C25;"0.00")&", {c.SHORT} cotiza "&IF({VO}!B35>{RES}!C25;"por DEBAJO";"por ENCIMA")&" de su DCF Base (US$"&TEXT({VO}!B35;"0.00")&", "&TEXT({VO}!B35/{RES}!C25-1;"+0%;-0%")&") y "&IF({RES}!D12>{RES}!C25;"por DEBAJO";"por ENCIMA")&" del precio objetivo ponderado Base (US$"&TEXT({RES}!D12;"0.00")&"). {t["conclusion"]}"'],
        [t["monitor"]],
        [],
        [c.SOURCES],
    ]
    return rows


def _write_tesis(c, sh, bk) -> None:
    rows = _tesis_rows(c)
    n_bb = len(c.TESIS["bull_bear"])
    h2 = 7 + n_bb + 2          # "2. DE LA HISTORIA..."
    hdr2 = h2 + 1
    first = hdr2 + 1           # primera fila de supuestos
    h3 = first + 8 + 1         # "3. RESULTADO..."
    hdr3 = h3 + 1
    r0 = hdr3 + 1
    h4 = r0 + 7
    pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
    ms.write_tesis(
        sh, rows, bk, text_rows=(),
        merges=[f"A{r}:E{r}" for r in (1, 2, 5, h2, h3, r0 + 4, r0 + 5, h4, h4 + 1, h4 + 2, h4 + 4)]
        + [f"B{r}:E{r}" for r in range(7, 8 + n_bb)],
        bold_rows=(4, h2, h3, h4), head_rows=(7, hdr2, hdr3),
        formats=[
            {"range": f"B{first}:D{first+3}", "format": pct},
            {"range": f"B{first+7}:D{first+7}", "format": pct},
            {"range": f"B{first+4}:D{first+4}", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0"}}},
            {"range": f"B{first+5}:D{first+5}", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}},
            {"range": f"B{first+6}:D{first+6}", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0.00%"}}},
            {"range": f"B{r0}:C{r0+2}", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
            {"range": f"B{r0+3}", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
            {"range": f"D{r0}:E{r0+2}", "format": {"numberFormat": {"type": "PERCENT", "pattern": "+0.0%;-0.0%"}}},
        ])


def step_content(c) -> None:
    sh = ms.open_sheet(c.SHEET_ID)
    bk = backup_path(c)
    ms.write_with_backup(sh, "Cualitativo", _cualitativo(c), f"Contenido cualitativo {c.TICKER}", bk)
    ms.write_with_backup(sh, "Estadísticas", _estadisticas(c), f"Estadisticas {c.TICKER} (formulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", _stories(c), f"Historia {c.TICKER}", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", _recomendados(c), f"Recomendaciones {c.TICKER}", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": c.MULTIPLOS_EVALUACION},
                         f"Evaluacion de multiplos {c.TICKER}", bk)
    _format_estadisticas(sh)
    _write_tesis(c, sh, bk)


def step_check(c) -> dict:
    sh = ms.open_sheet(c.SHEET_ID)
    vo = sh.worksheet("Valuation output")
    res = sh.worksheet("Resumen de Valoración")
    get = lambda ws, r: ws.get(r, value_render_option="UNFORMATTED_VALUE")  # noqa: E731
    dcf = [get(vo, x)[0][0] for x in ("B86", "B35", "B137")]
    tbl = get(res, "A6:E14")
    price = get(res, "C25")[0][0]
    coc = get(sh.worksheet("Cost of capital worksheet"), "B14")[0][0]
    out = {"ticker": c.TICKER, "price": price, "wacc": coc, "dcf": dcf,
           "methods": {r[0]: r[2:5] for r in tbl[:6]}, "ponderado": tbl[6][2:5], "cagr": tbl[7][2:5]}
    print(f"{c.TICKER}: precio {price:.2f} | WACC {coc:.2%} | DCF C/B/O {[round(x, 2) for x in dcf]}")
    for k, v in out["methods"].items():
        print(f"   {k:<14} {[round(x, 2) if isinstance(x, (int, float)) else x for x in v]}")
    print(f"   Ponderado      {[round(x, 2) for x in out['ponderado']]}   CAGR3 {[f'{x:.1%}' for x in out['cagr']]}")
    return out


STEPS = {"refresh": step_refresh, "assumptions": step_assumptions, "content": step_content, "check": step_check}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ticker")
    ap.add_argument("--step", choices=[*STEPS, "all"], default="all")
    args = ap.parse_args(argv)
    c = cfg_for(args.ticker)
    for name, fn in STEPS.items():
        if args.step in (name, "all"):
            fn(c)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
