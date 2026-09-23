#!/usr/bin/env python
"""Corre el pipeline de refresh_native_model.py para PayPal Holdings (PYPL)
con dos complementos a SEC EDGAR 'companyfacts' (ver
jmr_valuation/io/sec_xbrl_instance.py):

  - el 10-Q de Q2 2026 (presentado 2026-07-28) todavia no estaba en
    companyfacts -- sin esto el LTM quedaba en Q1 2026;
  - PYPL reporta I+D como 'pypl:TechnologyAndDevelopmentExpense' desde 2019
    (namespace propio, companyfacts no lo expone) -- sin esto R&D = 0 en
    2019-2025 y la capitalizacion de I+D (Input sheet!B17 = Yes) no tenia
    datos.

Despues aplica las decisiones metodologicas especificas de esta valoracion
(ver run() y la hoja 'Tesis de Inversión y Supuestos').

Pasos (en orden; `--step all` corre todos):
  refresh      pipeline de datos duros (SEC EDGAR complementado + yfinance)
  assumptions  balance LTM a jun-2026, cost of capital, supuestos Base y
               correcciones de los escenarios Conservador/Optimista
  errors       barrido de errores (IFERROR en Option value, dividendos, beta)
  content      Cualitativo, Estadisticas, Stories to Numbers y la Tesis

Cada celda que se pisa despues del refresh queda respaldada (formula
anterior) en reference/backups/pypl_formula_backup.json; el estado completo
de la plantilla antes de la corrida esta en
reference/backups/pypl_template_pre_run_formulas.json.gz.

Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts python scripts/run_pypl.py --step all
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import refresh_native_model as rnm  # noqa: E402

from jmr_valuation.io import sec_edgar_loader  # noqa: E402
from jmr_valuation.io.sec_xbrl_instance import AugmentedSecEdgarClient  # noqa: E402
from jmr_valuation.io.sheets_auth import get_gspread_client, open_target_sheet  # noqa: E402

SHEET_ID = "13N5V1gpdsetin5NbTu-1-312lPYq5Pj4aKF4jw0bLT0"
TICKER = "PYPL"
# Clasificacion real de Damodaran (indname.xls, ene-2026): PayPal, Visa,
# Mastercard, Block, Fiserv, Adyen, Global Payments -> todas en esta industria.
INDUSTRY = "Financial Svcs. (Non-bank & Insurance)"
PEER_TICKERS = ["V", "MA", "XYZ", "FISV", "GPN", "AFRM"]
CUSTOM_TAG_MAP = {"TechnologyAndDevelopmentExpense": "ResearchAndDevelopmentExpense"}


BACKUP_PATH = _ROOT / "reference" / "backups" / "pypl_formula_backup.json"
VALUATION_DATE = date(2026, 9, 22)  # ultimo cierre disponible al armar el modelo

# Balance al 30-jun-2026 (10-Q Q2 2026, presentado 2026-07-28), en $M. La
# columna L (LTM) de 'Balance Sheet' la llena refresh_balance_sheet con el
# cierre de FY2025 como proxy para la mayoria de las partidas de balance --
# para PYPL eso dejaba la deuda corriente en 0 (DebtCurrent = $2.505M) y
# el patrimonio/caja de hace 6 meses.
BALANCE_JUN2026 = {
    "L3": 8306, "L4": 2950, "L5": 8306 + 2950,
    "L6": 763, "L8": 763, "L9": 62346 - 11256 - 763, "L10": 62346,
    "L11": 1731, "L12": 178, "L13": 10929, "L14": 4009, "L15": 3544, "L16": 82737,
    "L18": 208, "L20": 2505, "L21": 142, "L23": 48406 - 208 - 2505 - 142, "L24": 48406,
    "L25": 10895, "L26": 668, "L27": 62917 - 48406 - 10895 - 668, "L28": 62917 - 48406, "L29": 62917,
    "L31": 22056, "L32": -503, "L33": 34432, "L34": 19820, "L35": 19820, "L36": 82737,
}


def _serial(d: date) -> int:
    return (d - date(1899, 12, 30)).days


def _write_with_backup(sh, sheet: str, updates: dict[str, object], reason: str) -> None:
    """Escribe celdas sueltas guardando ANTES la formula/valor anterior en
    reference/backups/pypl_formula_backup.json (reversible: basta con
    reescribir 'before' en cada celda). Si la celda ya estaba respaldada de
    una corrida anterior, se conserva el 'before' ORIGINAL."""
    ws = sh.worksheet(sheet)
    cells = list(updates)
    before = ws.batch_get(cells, value_render_option="FORMULA")
    backup = json.loads(BACKUP_PATH.read_text()) if BACKUP_PATH.exists() else {}
    for cell, prev in zip(cells, before):
        key = f"{sheet}!{cell}"
        old = prev[0][0] if prev and prev[0] else ""
        if key not in backup:
            backup[key] = {"before": old, "after": updates[cell], "reason": reason}
        else:
            backup[key].update(after=updates[cell], reason=reason)
    BACKUP_PATH.parent.mkdir(parents=True, exist_ok=True)
    BACKUP_PATH.write_text(json.dumps(backup, ensure_ascii=False, indent=1))
    rnm._apply(ws, [(c, [[v]]) for c, v in updates.items()])


def _install_augmented_client() -> None:
    client = AugmentedSecEdgarClient(custom_tag_map=CUSTOM_TAG_MAP, tickers=(TICKER,))
    sec_edgar_loader.SecEdgarClient = lambda *a, **k: client  # type: ignore[assignment]


def step_refresh() -> None:
    _install_augmented_client()
    rnm.run(TICKER, sheet_id=SHEET_ID, peer_tickers=PEER_TICKERS,
            industry_us=INDUSTRY, industry_global=INDUSTRY)


def step_assumptions() -> None:
    """Pasos 2 y 4 del proceso (cost of capital + supuestos de
    crecimiento/margen) y correcciones estructurales. La justificacion de
    cada numero esta en la hoja 'Tesis de Inversión y Supuestos'."""
    sh = open_target_sheet(get_gspread_client(), SHEET_ID)

    _write_with_backup(sh, "Balance Sheet", BALANCE_JUN2026, "LTM = balance real al 30-jun-2026 (10-Q Q2 2026)")

    _write_with_backup(sh, "Input sheet", {
        "B1": "=A1",  # bug #6 del apendice: TICKER vacio en las hojas que leen Input!B1
        "B4": _serial(VALUATION_DATE),
        # Tasa efectiva: estaba fija en la columna I ('Dec 23' = 21,5%), no en
        # el LTM (16,4%) -- quedaba desalineada del resto del Input sheet.
        "B24": "='Income Statement'!L29",
        # Solo inversiones de largo plazo (US$2.269M de deuda negociable + US$1.735M
        # estrategicas). 'Other Long-Term Assets' (L15: impuestos diferidos,
        # activos por derecho de uso, etc.) son OPERATIVOS, no activos no
        # operativos -- sumarlos inflaba el equity en ~US$3.500M (~US$4/accion).
        "B20": "='Balance Sheet'!L14",
        "B27": 0.04,    # Crecimiento Año 1 (Base)
        "B28": "='Valuation output'!B6-0,008",  # Margen Año 1 = base ajustada por I+D - 0,8pp
        "B29": 0.035,   # CAGR años 2-5 (Base)
        "B30": 0.195,   # Margen objetivo pre-tax (Base)
        "B31": 6,       # Años de convergencia
        "B32": 2.6,     # Sales to capital años 1-5
        "B33": 2.6,     # Sales to capital años 6-10
        "B35": 0.0496,  # UST 10 años al 22-sep-2026
    }, "Supuestos PYPL (ver hoja Tesis de Inversión y Supuestos)")

    _write_with_backup(sh, "Country equity risk premiums", {
        "B2": 0.0409,  # ERP implicito T12m de Damodaran al 1-sep-2026 (ERPbymonth.xlsx)
        "C2": "Updated September 1, 2026",
    }, "ERP de mercado maduro actualizado")

    _write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Direct Input",
        "B23": 1.29,        # beta de regresion 5 años mensual de PYPL
        "B33": 6,           # vencimiento promedio ponderado de la deuda (10-Q Q2 2026)
        "B34": "Actual rating",
        "B36": "A3/A-",     # Moody's A3 / S&P A- (notas senior, mayo 2026)
    }, "Cost of capital PYPL")

    _write_with_backup(sh, "Valuation output", {
        # Conservador: margen objetivo = margen del Año 1 (la compresion de
        # 2026 por reinversion se vuelve permanente). Antes: =B6.
        "C45": "='Input sheet'!B28",
        # Optimista: los US$1.500M de ahorro bruto anunciados caen enteros a
        # margen en vez de reinvertirse (1.500 / ingresos LTM = +4,4pp).
        # Antes: =B30+5% fijo.
        "C47": "='Input sheet'!B30+1500/'Input sheet'!B12",
        # Conservador: crecimiento explicitamente por debajo del Base. Antes:
        # =PROMEDIO(B27; riskfree) -- con riskfree 4,96% > crecimiento Base,
        # el "conservador" crecia MAS que el Base (bug #10 del apendice).
        "C55": "=MIN('Input sheet'!B27;'Input sheet'!B29)-0,015",
    }, "Escenarios: orden Conservador < Base < Optimista")

    _write_with_backup(sh, "Resumen de Valoración", {"G3": "Madura"}, "Tipo de empresa PYPL")

    rnm.refresh_resumen_valoracion(sh, TICKER, rnm.get_market_snapshot(TICKER))


def _iferror(formula: str, fallback: str = '""') -> str:
    return f"=IFERROR({formula[1:]};{fallback})"


def step_error_sweep() -> None:
    """Paso 8: errores reales encontrados en el barrido (los 12 #DIV/0! de
    'Industry Averages(US)' son del dataset de Damodaran -- identicos en la
    plantilla en blanco -- y no se tocan)."""
    sh = open_target_sheet(get_gspread_client(), SHEET_ID)

    # Crecimiento del dividendo: PYPL empezo a pagar dividendo en 2025, el
    # año previo es 0 -> #DIV/0!.
    fm = sh.worksheet("Financials Multiples")
    cells = [f"{c}{r}" for r in (36, 75, 115) for c in "BCDE"]
    current = fm.batch_get(cells, value_render_option="FORMULA")
    _write_with_backup(sh, "Financials Multiples", {
        c: _iferror(v[0][0]) for c, v in zip(cells, current) if not v[0][0].startswith("=IFERROR")
    }, "Crecimiento de dividendo sin año base (dividendo iniciado en 2025)")

    # Bug #5 del apendice (no estaba aplicado en esta copia): Black-Scholes
    # con 0 opciones -> #DIV/0! en toda la cadena de 'Option value'.
    ov = sh.worksheet("Option value")
    cells = ["B18", "B23", "B24", "B26", "B27", "B29", "B30"]
    current = ov.batch_get(cells, value_render_option="FORMULA")
    _write_with_backup(sh, "Option value", {
        c: _iferror(v[0][0], "0") for c, v in zip(cells, current) if not v[0][0].startswith("=IFERROR")
    }, "Bug #5: IFERROR en la cadena de Option value (sin opciones de empleados)")

    # Con beta 'Direct Input', B24 caia a la rama multibusiness global
    # (K65, tabla vacia). Ahora muestra la beta desapalancada IMPLICITA en
    # la beta ingresada (informativa: C58 usa B23 directo).
    _write_with_backup(sh, "Cost of capital worksheet", {
        "B24": ('=IF(B22="Direct Input";B23/(1+(1-B39)*(C61/B61));'
                'IF(B22="Single Business(US)";VLOOKUP(\'Input sheet\'!B9;\'Industry Averages(US)\'!A3:G96;7);'
                'IF(B22="Multibusiness(US)";K49;IF(B22="Single Business(Global)";'
                'VLOOKUP(\'Input sheet\'!B10;\'Industry Averages (Global)\'!A3:G96;7);'
                '\'Cost of capital worksheet\'!K65))))'),
        "K65": _iferror(sh.worksheet("Cost of capital worksheet").acell("K65", value_render_option="FORMULA").value),
        "L65": _iferror(sh.worksheet("Cost of capital worksheet").acell("L65", value_render_option="FORMULA").value),
    }, "Beta Direct Input: B24 muestra beta desapalancada implicita; tabla multibusiness vacia con IFERROR")


def _col_width(sheet_id: int, start: int, end: int, px: int) -> dict:
    return {"updateDimensionProperties": {
        "range": {"sheetId": sheet_id, "dimension": "COLUMNS", "startIndex": start, "endIndex": end},
        "properties": {"pixelSize": px}, "fields": "pixelSize"}}


def step_content() -> None:
    """Pasos 3 y 9: Cualitativo, Estadisticas, Stories to Numbers, Supuestos
    Recomendados / de los Multiplos y la hoja 'Tesis de Inversión y Supuestos'."""
    import pypl_content as pc

    sh = open_target_sheet(get_gspread_client(), SHEET_ID)
    _write_with_backup(sh, "Cualitativo", pc.CUALITATIVO, "Contenido cualitativo PYPL (reemplaza el heredado de Adobe)")
    _write_with_backup(sh, "Estadísticas", pc.ESTADISTICAS, "Estadisticas PYPL (formulas vivas en vez de valores de otra empresa)")
    _write_with_backup(sh, "Stories to Numbers", pc.STORIES, "Historia PYPL (reemplaza la de Amazon)")
    _write_with_backup(sh, "Supuestos Recomendados", pc.SUPUESTOS_RECOMENDADOS, "Recomendaciones PYPL")
    _write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": pc.MULTIPLOS_EVALUACION}, "Evaluacion de multiplos PYPL")

    est = sh.worksheet("Estadísticas")
    pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
    num = {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}
    mult = {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}
    est.batch_format([
        {"range": "B4:B7", "format": num}, {"range": "B8", "format": num},
        {"range": "B11:B16", "format": pct}, {"range": "B19:B23", "format": pct},
        {"range": "E4:E9", "format": mult}, {"range": "E13:E17", "format": mult},
        {"range": "E12", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
        {"range": "E20:E21", "format": num}, {"range": "E22:E23", "format": mult},
        {"range": "H4:H15", "format": pct}, {"range": "H18:H19", "format": pct},
        {"range": "H20", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
    ])

    # --- Tesis: se reemplaza la plantilla de placeholders completa (backup del
    # contenido anterior bajo una sola clave). ---
    ws = sh.worksheet("Tesis de Inversión y Supuestos")
    old = ws.get("A1:H120", value_render_option="FORMULA")
    backup = json.loads(BACKUP_PATH.read_text()) if BACKUP_PATH.exists() else {}
    backup.setdefault("Tesis de Inversión y Supuestos!A1:H120", {"before": old, "reason": "Plantilla de placeholders reemplazada"})
    BACKUP_PATH.write_text(json.dumps(backup, ensure_ascii=False, indent=1))
    ws.batch_clear(["A1:H120"])
    rows = [r + [""] * (5 - len(r)) for r in pc.TESIS_ROWS]
    # Log de correcciones (filas 35-52): texto literal aunque empiece con
    # '=' o '#' (p.ej. "=L14+L15 -> 7.642"), si no Sheets lo parsea como formula.
    for r in rows[34:52]:
        for j, x in enumerate(r):
            if isinstance(x, str) and x[:1] in ("=", "#", "+", "-"):
                r[j] = "'" + x
    ws.update(values=rows, range_name="A1", value_input_option="USER_ENTERED")

    bold = {"textFormat": {"bold": True}}
    head = {"textFormat": {"bold": True}, "backgroundColor": {"red": 0.87, "green": 0.92, "blue": 0.97}}
    n = len(rows)
    ws.batch_format([
        {"range": f"A1:E{n}", "format": {"wrapStrategy": "WRAP", "verticalAlignment": "TOP", "textFormat": {"bold": False}, "backgroundColor": {"red": 1, "green": 1, "blue": 1}}},
        {"range": "A1", "format": {"textFormat": {"bold": True, "fontSize": 13}}},
        *[{"range": f"A{r}", "format": bold} for r in (4, 13, 24, 33, 55)],
        *[{"range": f"A{r}:E{r}", "format": head} for r in (7, 14, 25, 34)],
        {"range": "B15:D18", "format": pct}, {"range": "B22:D22", "format": pct},
        {"range": "B19:D19", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0"}}},
        {"range": "B20:D20", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}},
        {"range": "B21:D21", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0.00%"}}},
        {"range": "B26:C28", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
        {"range": "B29", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
        {"range": "D29", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
        {"range": "D26:E28", "format": {"numberFormat": {"type": "PERCENT", "pattern": "+0.0%;-0.0%"}}},
        {"range": "A30", "format": bold},
    ])
    sid = ws.id
    merges = [f"A{r}:E{r}" for r in (1, 2, 5, 30, 31, 33, 53, 56, 57, 59)]
    sh.batch_update({"requests": [
        {"unmergeCells": {"range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": 120, "startColumnIndex": 0, "endColumnIndex": 8}}},
        _col_width(sid, 0, 1, 260), _col_width(sid, 1, 4, 150), _col_width(sid, 4, 5, 520),
    ]})
    for m in merges:
        ws.merge_cells(m)
    # Bull/bear: A y B son cada uno un bloque de texto -> columna B un poco mas
    # ancha no alcanza; se combinan B:E para el caso bajista.
    for r in range(7, 12):
        ws.merge_cells(f"B{r}:E{r}")


STEPS = {"refresh": step_refresh, "assumptions": step_assumptions, "errors": step_error_sweep, "content": step_content}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--step", choices=[*STEPS, "all"], default="all")
    args = parser.parse_args(argv)
    for name, fn in STEPS.items():
        if args.step in (name, "all"):
            fn()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
