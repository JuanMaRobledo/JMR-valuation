#!/usr/bin/env python
"""Presentacion del Modelo JMR (auditoria sep-2026):

1. Hoja nueva 'Origen de los Supuestos': explica de donde sale cada
   supuesto de crecimiento, margen, costo de capital y multiplo objetivo,
   con formulas VIVAS (el valor de cada escenario, la formula real de la
   celda via FORMULATEXT y las anclas historicas / de industria para
   contrastarlo). Si alguien cambia una regla, la hoja lo refleja sola.
2. Formato uniforme para las hojas de texto (Tesis, Cualitativo,
   Supuestos Recomendados, Supuestos de los Multiplos, Stories to Numbers):
   tipografia, bandas de seccion, encabezados, bordes, texto ajustado y
   alto de fila calculado para que ningun parrafo quede cortado.

Solo cambia formato y la hoja nueva; el unico contenido que MUEVE es el
texto del caso bajista de la Tesis (columna B -> D, para darle el mismo
ancho que al alcista), y solo si C:E de esas filas estan vacias.

Uso:
    PYTHONPATH=.:scripts python scripts/model_presentation.py --sheet-id ID
    PYTHONPATH=.:scripts python scripts/model_presentation.py --targets-json targets.json
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from gspread.exceptions import APIError, WorksheetNotFound  # noqa: E402

from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

ORIGEN = "Origen de los Supuestos"
BACKUP_DIR = _ROOT / "reference" / "backups" / "auditoria_2026-09-26"
_TEXT_SHEETS = ("Tesis de Inversión y Supuestos", "Supuestos Recomendados", "Supuestos de los Múltiplos", "Cualitativo",
                "Stories to Numbers", "Resumen de Valoración")

# --- paleta y tipografia -----------------------------------------------------
FONT = "Roboto"


def _rgb(h: str) -> dict:
    h = h.lstrip("#")
    return {"red": int(h[0:2], 16) / 255, "green": int(h[2:4], 16) / 255, "blue": int(h[4:6], 16) / 255}


NAVY, INK, MUTED = _rgb("1F3864"), _rgb("262626"), _rgb("595959")
HEAD_BG, ZEBRA, WHITE, LINE = _rgb("DCE4F2"), _rgb("F6F8FB"), _rgb("FFFFFF"), _rgb("C9D1DE")
GREEN_BG, RED_BG = _rgb("E6F2EA"), _rgb("FBE9E7")

PCT, MULT, NUM, USD, INT = "0.0%", '0.0"x"', "#,##0.00", '"$"#,##0.00', "0"


def _txt(size=10, bold=False, italic=False, color=INK) -> dict:
    return {"fontFamily": FONT, "fontSize": size, "bold": bold, "italic": italic, "foregroundColor": color}


def _border(color=LINE, style="SOLID") -> dict:
    return {"style": style, "color": color}


class Req:
    """Acumula requests de batch_update para una hoja."""

    def __init__(self, sheet_id: int):
        self.sid = sheet_id
        self.items: list[dict] = []

    def grid(self, r0, r1, c0, c1) -> dict:  # filas/columnas 1-based inclusivas
        return {"sheetId": self.sid, "startRowIndex": r0 - 1, "endRowIndex": r1, "startColumnIndex": c0 - 1, "endColumnIndex": c1}

    def fmt(self, r0, r1, c0, c1, **cell):
        fields = ",".join(f"userEnteredFormat.{k}" for k in cell)
        self.items.append({"repeatCell": {"range": self.grid(r0, r1, c0, c1), "cell": {"userEnteredFormat": cell}, "fields": fields}})

    def borders(self, r0, r1, c0, c1, inner=True, color=LINE):
        b = _border(color)
        body = {"range": self.grid(r0, r1, c0, c1), "top": b, "bottom": b, "left": b, "right": b}
        if inner:
            body |= {"innerHorizontal": b, "innerVertical": b}
        self.items.append({"updateBorders": body})

    def merge(self, r0, r1, c0, c1):
        self.items.append({"mergeCells": {"range": self.grid(r0, r1, c0, c1), "mergeType": "MERGE_ALL"}})

    def unmerge(self, r0, r1, c0, c1):
        self.items.append({"unmergeCells": {"range": self.grid(r0, r1, c0, c1)}})

    def width(self, c0, c1, px):
        self.items.append({"updateDimensionProperties": {
            "range": {"sheetId": self.sid, "dimension": "COLUMNS", "startIndex": c0 - 1, "endIndex": c1},
            "properties": {"pixelSize": px}, "fields": "pixelSize"}})

    def height(self, r0, r1, px):
        self.items.append({"updateDimensionProperties": {
            "range": {"sheetId": self.sid, "dimension": "ROWS", "startIndex": r0 - 1, "endIndex": r1},
            "properties": {"pixelSize": int(px)}, "fields": "pixelSize"}})

    def sheet_props(self, frozen_rows=0, hide_grid=True, tab=None):
        props = {"sheetId": self.sid, "gridProperties": {"frozenRowCount": frozen_rows, "hideGridlines": hide_grid}}
        fields = "gridProperties.frozenRowCount,gridProperties.hideGridlines"
        if tab:
            props["tabColorStyle"] = {"rgbColor": tab}
            fields += ",tabColorStyle"
        self.items.append({"updateSheetProperties": {"properties": props, "fields": fields}})


def _retry(fn, tries=6):
    for i in range(tries):
        try:
            return fn()
        except APIError as exc:
            if "429" not in str(exc) or i == tries - 1:
                raise
            time.sleep(30 * (i + 1))


# --- alto de fila ------------------------------------------------------------

def _lines(text: str, width_px: float, size: int = 10) -> int:
    """Lineas que ocupa `text` ajustado a `width_px` (ancho medio de un
    caracter Roboto ~0,62 x tamaño en px)."""
    if not text:
        return 1
    per_line = max(1, int((width_px - 10) / (size * 0.62)))
    return sum(max(1, math.ceil(len(p) / per_line)) for p in str(text).split("\n"))


def fit_row_heights(sh, ws, r0: int, r1: int, *, min_px: int = 21, size_by_row: dict[int, int] | None = None) -> list[dict]:
    """Calcula el alto de cada fila segun el texto (con celdas combinadas),
    porque el auto-ajuste de Sheets ignora las celdas combinadas."""
    meta = sh.fetch_sheet_metadata(params={
        "ranges": [f"'{ws.title}'!A{r0}:Z{r1}"],
        "fields": "sheets(merges,data(columnMetadata(pixelSize),rowData(values(formattedValue,effectiveFormat(textFormat(fontSize),wrapStrategy)))))"})
    s = meta["sheets"][0]
    data = s.get("data", [{}])[0]
    widths = [c.get("pixelSize", 100) for c in data.get("columnMetadata", [])]
    rows = data.get("rowData", [])
    span: dict[tuple[int, int], int] = {}
    covered: set[tuple[int, int]] = set()
    for m in s.get("merges", []):
        if m["endRowIndex"] - m["startRowIndex"] != 1:
            continue
        r, c0, c1 = m["startRowIndex"], m["startColumnIndex"], m["endColumnIndex"]
        span[(r, c0)] = sum(widths[c0:c1]) if widths else 100 * (c1 - c0)
        covered |= {(r, c) for c in range(c0 + 1, c1)}
    req = Req(ws.id)
    for i, rd in enumerate(rows):
        r = r0 - 1 + i
        need = min_px
        for c, cell in enumerate(rd.get("values", [])):
            txt = cell.get("formattedValue")
            if not txt or (r, c) in covered:
                continue
            ef = cell.get("effectiveFormat", {})
            size = (size_by_row or {}).get(r + 1) or ef.get("textFormat", {}).get("fontSize", 10)
            w = span.get((r, c), widths[c] if c < len(widths) else 100)
            wraps = ef.get("wrapStrategy") == "WRAP" or (r, c) in span
            n = _lines(txt, w, size) if wraps else 1
            need = max(need, int(n * size * 1.6 + 9))
        req.height(r + 1, r + 1, need)
    return req.items


# --- hoja 'Origen de los Supuestos' ------------------------------------------

VO, IN, CM, RS, COC, FMS = ("'Valuation output'", "'Input sheet'", "'Crecimiento y Márgenes'", "'Resumen de Valoración'",
                            "'Cost of capital worksheet'", "'Financials Multiples'")


def _ft(ref: str, fmt: str = "0.0%") -> str:
    """Formula real de la celda, o 'fijo X' si es un valor tipeado."""
    return f'IFERROR(FORMULATEXT({ref});"fijo "&TEXT({ref};"{fmt}"))'


_MULTS = (  # hoja, etiqueta, fila en 'Supuestos de los Múltiplos'
    ("EVEBITDA", "EV/EBITDA", 10), ("EVFCFF", "EV/FCFF", 6), ("PE", "P/E", 8), ("PFCFE", "P/FCFE", 9), ("POCF", "P/OCF", 7))


def origen_rows() -> list[tuple[str, list, str | None]]:
    """(tipo, celdas A..K, formato numerico de B:D y F:K)."""
    R: list[tuple[str, list, str | None]] = []
    add = lambda kind, cells, nf=None: R.append((kind, cells, nf))  # noqa: E731

    add("title", [f"=\"Origen de los supuestos — \"&{IN}!A1"])
    add("subtitle", ["De dónde sale cada número que mueve el precio objetivo. Todas las cifras son fórmulas vivas del modelo; "
                     "la columna «Regla» muestra la fórmula real de la celda, así que si una valoración cambia una regla, esta hoja lo refleja."])
    add("blank", [])

    add("section", ["1. CÓMO SE ARMA EL PRECIO OBJETIVO"])
    for t in (
        "• Seis métodos: DCF de Damodaran y cinco múltiplos (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF). El precio objetivo es su promedio "
        "ponderado, con los pesos de la categoría de empresa elegida en 'Resumen de Valoración'!G3 (tabla I5:U11; ver sección 7).",
        "• Horizonte común de 3 años. Los múltiplos dan el precio al cierre del año fiscal FY+3 más los dividendos cobrados en el camino; "
        "el DCF da el valor intrínseco HOY, por eso se lleva a 3 años con el costo del equity: valor × (1 + Ke)³. Así el «CAGR a 3 años» "
        "compara magnitudes del mismo momento. Si una valoración usa otra convención, la sección 7 muestra la fórmula real de su Resumen.",
        "• Tres escenarios. El Base lo fija el analista (Input sheet B27–B33) con la guía de la empresa, el consenso y la historia, y se "
        "justifica en 'Tesis de Inversión y Supuestos'. Conservador y Optimista salen de reglas en 'Valuation output' (C45, C47, C55, C106) "
        "que se muestran abajo. Las columnas de la derecha son las anclas históricas y de industria para verificar que ningún supuesto sea extremo.",
    ):
        add("para", [t])
    add("blank", [])

    add("section", ["2. CRECIMIENTO DE INGRESOS"])
    add("header", ["Tramo", "Conservador", "Base", "Optimista", "Regla (fórmula real de la celda)", "Último año fiscal",
                   "CAGR 3 años", "CAGR 5 años", "CAGR 9 años", "Industria (mediana peers)", "Industria Damodaran"])
    add("data", ["Año 1", f"={VO}!C55", f"={IN}!B27", f"={VO}!C106",
                 f'="Cons: "&{_ft(VO + "!C55")}&"  ·  Base: analista (Input B27)  ·  Opt: "&{_ft(VO + "!C106")}',
                 f"={CM}!C6", f"={CM}!C7", f"={CM}!C8", f"={CM}!C9", f"={CM}!C17", f"={IN}!J26"], PCT)
    add("data", ["Años 2-5", f"={VO}!D55", f"={IN}!B29", f"={VO}!D106",
                 f'="Cons: "&{_ft(VO + "!D55")}&"  ·  Base: analista (Input B29)  ·  Opt: "&{_ft(VO + "!D106")}'], PCT)
    add("data", ["Año 10 (convergencia)", f"={VO}!L55", f"={VO}!L4", f"={VO}!L106",
                 "Entre los años 6 y 10 el crecimiento converge en línea recta a la tasa de perpetuidad (Damodaran)."], PCT)
    add("data", ["Perpetuidad", f"={VO}!M55", f"={VO}!M4", f"={VO}!M106",
                 "Igual a la tasa libre de riesgo (Input B35): ninguna empresa crece más que la economía para siempre. Override en Input B65–B69."], PCT)
    add("note", ["Regla de la plantilla: Conservador = mín(Año 1; Años 2-5) − 1,5 pp; Optimista = máx(Año 1; Años 2-5) + 1 pp. "
                 "Cada valoración puede cambiarla (queda a la vista en la columna Regla). Las columnas F–I salen de 'Crecimiento y Márgenes' "
                 "(ingresos reales del Income Statement); J es la mediana de los peers de la hoja 'Sector'; K, el promedio de la industria de Damodaran."])
    add("blank", [])

    add("section", ["3. MARGEN OPERATIVO (EBIT) Y EFICIENCIA DEL CAPITAL"])
    add("header", ["Tramo", "Conservador", "Base", "Optimista", "Regla (fórmula real de la celda)", "Último (LTM)",
                   "Promedio 3 años", "Promedio 5 años", "Promedio 10 años", "Industria (mediana peers)", "Industria Damodaran"])
    add("data", ["Año 0 (base)", f"={VO}!B57", f"={VO}!B6", f"={VO}!B108",
                 "EBIT base ÷ ingresos (Input B13 ÷ B12), con I+D y arriendos capitalizados si Input B17/B18 = Yes.",
                 f"={CM}!D6", f"={CM}!D7", f"={CM}!D8", f"={CM}!D9", f"={CM}!E17", f"={IN}!J27"], PCT)
    add("data", ["Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
                 f'="Cons: "&{_ft(VO + "!C57")}&"  ·  Base: analista (Input B28)  ·  Opt: "&{_ft(VO + "!C108")}'], PCT)
    add("data", ["Margen objetivo", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
                 f'="Cons: "&{_ft(VO + "!C45")}&"  ·  Base: "&{_ft(VO + "!C46")}&"  ·  Opt: "&{_ft(VO + "!C47")}'], PCT)
    add("data", ["Año en que se alcanza", f"={IN}!B31", f"={IN}!B31", f"={IN}!B31",
                 "El margen va en línea recta del Año 1 al objetivo en este año, y luego se mantiene."], INT)
    add("data", ["Sales-to-capital años 1-5", f"={IN}!B32", f"={IN}!B32", f"={IN}!B32",
                 "Reinversión = Δ ingresos ÷ sales-to-capital. F = ratio actual de la empresa; K = industria.",
                 f"={IN}!I28", "", "", "", "", f"={IN}!J28"], NUM)
    add("data", ["Sales-to-capital años 6-10", f"={IN}!B33", f"={IN}!B33", f"={IN}!B33", "Input B33."], NUM)
    add("data", ["ROIC implícito año 10", f"={VO}!L93", f"={VO}!L42", f"={VO}!L144",
                 "Chequeo de coherencia: margen × sales-to-capital. Si supera por mucho al actual (F) o a la industria (K), revisar.",
                 f"={IN}!I30", "", "", "", "", f"={IN}!J30"], PCT)
    add("note", ["Regla de la plantilla: Conservador = el margen no mejora (se queda en el margen base, VO!B6); "
                 "Optimista = margen objetivo Base + 5 pp. El Base se ancla en la guía de la empresa, el margen histórico (F–I) y los comparables (J–K)."])
    add("blank", [])

    add("section", ["4. COSTO DE CAPITAL Y VALOR TERMINAL"])
    add("header", ["Componente", "Valor", "", "", "Fuente / regla"])
    for label, ref, nf, why in (
        ("Tasa libre de riesgo", f"={IN}!B35", PCT, "Bono del gobierno a 10 años en la moneda de la valoración, a la fecha del análisis."),
        ("Beta apalancada", f"={COC}!C58", NUM,
         f'="Beta desapalancada "&TEXT({COC}!B24;"0.00")&" ("&{COC}!B22&"), reapalancada con la deuda/equity de mercado."'),
        ("Prima de riesgo del mercado (ERP)", f"={COC}!B28", PCT, "Damodaran, según el país de incorporación ('Country equity risk premiums')."),
        ("Costo del equity (Ke)", f"={COC}!B63", PCT, "Rf + beta × ERP. También es la tasa con la que el DCF se lleva a 3 años en el Resumen."),
        ("Costo de la deuda después de impuestos", f"={COC}!C63", PCT, "Rf + spread del rating (real o sintético), × (1 − tasa marginal)."),
        ("Peso del equity", f"={COC}!B62", PCT, "Valores de mercado: capitalización vs deuda + arriendos."),
        ("WACC inicial (años 1-5)", f"={IN}!B36", PCT, "'Cost of capital worksheet'!B14. Converge al terminal entre los años 6 y 10."),
        ("WACC terminal", f"={VO}!M14", PCT, "Rf + ERP maduro: en perpetuidad la empresa tiene el riesgo de una empresa promedio (override Input B46–B47)."),
        ("Crecimiento a perpetuidad", f"={VO}!M4", PCT, "Igual a la tasa libre de riesgo (sección 2)."),
    ):
        add("data", [label, ref, "", "", why], nf)
    add("blank", [])

    add("section", ["5. MÚLTIPLOS OBJETIVO (SALIDA AL CIERRE FY+3)"])
    add("header", ["Múltiplo", "Conservador", "Base", "Optimista", "Regla del Base", "Mínimo positivo 4 cierres",
                   "Mediana 5 años", "Mediana 10 años", "Actual (LTM)", "Industria (mediana peers)", "Override Cons./Opt."])
    for sheet, label, srow in _MULTS:
        add("data", [label, f"={sheet}!F8", f"={sheet}!F19", f"={sheet}!F30",
                     f'=IF({sheet}!J19="";"Mediana 5 años (J19 vacía)";IFERROR(IF(ISNUMBER(SEARCH("MINIFS";FORMULATEXT({sheet}!J19)));'
                     f'"Mínimo positivo de los 4 últimos cierres";"J19: "&FORMULATEXT({sheet}!J19));"Fijado a mano en J19"))',
                     f'=IF(COUNTIF({sheet}!B19:E19;">0")=0;"—";MINIFS({sheet}!B19:E19;{sheet}!B19:E19;">0"))',
                     f"={sheet}!B40", f"={sheet}!B39", f"={sheet}!B42", f"='Supuestos de los Múltiplos'!M{srow}",
                     f'=IF(COUNTA({sheet}!J8;{sheet}!J30)>0;"Sí (J8/J30)";"No: ×0,9 / ×1,1")'], MULT)
    for t in (
        "Regla de la plantilla: el múltiplo Base es el MENOR múltiplo positivo que pagó el mercado por la empresa en sus últimos 4 cierres "
        "fiscales (celda J19 de cada hoja de múltiplo). Se usa el mínimo, no el promedio, por disciplina de margen de seguridad: si la tesis "
        "funciona aun al múltiplo más bajo reciente, el retorno viene del negocio y no de una re-valoración. Conservador = Base × 0,9; "
        "Optimista = Base × 1,1, salvo override en J8/J30.",
        "Cálculo del precio: múltiplo × métrica proyectada al cierre FY+3 del mismo escenario ('Financials Multiples', que usa el crecimiento "
        "y el margen de ese escenario del DCF) ÷ acciones proyectadas. En EV/EBITDA y EV/FCFF se resta la deuda neta (deuda + arriendos − caja "
        "− activos no operativos + minoritarios). A cada precio se le suman los dividendos por acción de FY+1 a FY+3 (sección 6).",
        "Cómo usar las columnas F–J: si el múltiplo Base queda muy por encima de la mediana de 10 años, del actual o de la industria, el "
        "precio objetivo depende de que el mercado vuelva a pagar más; conviene documentarlo en la Tesis o bajar el múltiplo.",
    ):
        add("note", [t])
    add("blank", [])

    add("section", ["6. DIVIDENDOS INCLUIDOS EN LOS MÚLTIPLOS"])
    add("header", ["Concepto", "Valor", "", "", "Regla"])
    add("data", ["DPS últimos 12 meses", "=Dividendos!L4", "", "", "Dividendos pagados (Cash Flow Statement fila 32) ÷ acciones en circulación."], USD)
    add("data", ["Crecimiento anual supuesto del DPS", f"={FMS}!E36", "", "",
                 "CAGR de 5 años del DPS ('Dividendos' F4→K4), acotado entre 0% y 15%."], PCT)
    add("data", ["DPS FY+1 / FY+2 / FY+3", f"={FMS}!E35", f"={FMS}!F35", f"={FMS}!G35", "DPS LTM × (1 + g) cada año."], USD)
    add("data", ["Dividendos acumulados al FY+3", f"=SUM({FMS}!E35:G35)", "", "", "Se suman al precio de salida de cada múltiplo."], USD)
    add("blank", [])

    add("section", ["7. PONDERACIÓN, RESULTADO Y ZONAS DE COMPRA"])
    add("header", ["Método", "Conservador", "Base", "Optimista", "Qué valor entra", "Peso"])
    add("data", ["DCF — valor intrínseco hoy", f"={VO}!B86", f"={VO}!B35", f"={VO}!B137", "Referencia: no entra al ponderado."], USD)
    rows = (("DCF — llevado a 3 años", 6, "Valor hoy × (1 + Ke)³."),
            ("EV/EBITDA", 7, "Precio FY+3 + dividendos acumulados."), ("EV/FCFF", 8, "Precio FY+3 + dividendos acumulados."),
            ("P/E", 9, "Precio FY+3 + dividendos acumulados."), ("P/FCFE", 10, "Precio FY+3 + dividendos acumulados."),
            ("P/OCF", 11, "Precio FY+3 + dividendos acumulados."))
    for label, r, why in rows:
        # si el Resumen de esta valoracion usa otra convencion, se muestra su formula real
        std = '"^3"' if r == 6 else f'"={_MULTS_BY_ROW[r]}!"'
        add("data", [label if r != 6 else f'=IF(ISNUMBER(SEARCH("^3";FORMULATEXT({RS}!D6)));"{label}";"DCF (según el Resumen)")',
                     f"={RS}!C{r}", f"={RS}!D{r}", f"={RS}!E{r}",
                     f'=IFERROR(IF(ISNUMBER(SEARCH({std};SUBSTITUTE(FORMULATEXT({RS}!D{r});"$";"")));"{why}";'
                     f'"Personalizado en esta valoración: "&FORMULATEXT({RS}!D{r}));"{why}")', f"={RS}!B{r}"], USD)
    add("data", ["Precio objetivo ponderado", f"={RS}!C12", f"={RS}!D12", f"={RS}!E12",
                 f'="Pesos de la categoría «"&{RS}!G3&"» (\'Resumen de Valoración\'!I5:U11)."', f"={RS}!B12"], USD)
    add("data", ["CAGR a 3 años vs precio del análisis", f"={RS}!C13", f"={RS}!D13", f"={RS}!E13", "(Precio objetivo ÷ precio del análisis)^(1/3) − 1."], PCT)
    add("data", ["Zona Value (máx / mín)", f"={RS}!B16", f"={RS}!C16", "", "70% / 65% del precio objetivo Base."], USD)
    add("data", ["Zona Deep Value (máx / mín)", f"={RS}!B17", f"={RS}!C17", "", "60% / 55% del precio objetivo Base."], USD)
    add("data", ["Valoración histórica (máx / mín)", f"={RS}!B18", f"={RS}!C18", "", "50% / 45% del precio objetivo Base."], USD)
    add("data", ["Precio con margen de seguridad (Base / Cons.)", f"={RS}!B19", f"={RS}!C19", "",
                 f'="Precio objetivo × (1 − MOS de "&TEXT({RS}!G4;"0%")&")."'], USD)
    add("blank", [])
    add("note", ["Fuentes de la metodología: Aswath Damodaran (NYU Stern) — DCF «story to numbers», datos de industria y primas de riesgo "
                 "(ene/sep-2026); Modelo JMR — múltiplos contra la propia historia y zonas de compra (Modelo-JMR/modelo/METODOLOGIA.md). "
                 "Auditoría de la plantilla del 26-sep-2026: JMR-valuation/scripts/audit_fix_model.py."])
    return R


_NCOL = 11
_MULTS_BY_ROW = {7: "EVEBITDA", 8: "EVFCFF", 9: "PE", 10: "PFCFE", 11: "POCF"}


def build_origen(sh) -> None:
    titles = [w.title for w in sh.worksheets()]
    if ORIGEN in titles:
        ws = sh.worksheet(ORIGEN)
        sh.batch_update({"requests": [{"unmergeCells": {"range": {"sheetId": ws.id}}}]})
        ws.clear()
    else:
        idx = titles.index("Tesis de Inversión y Supuestos") + 1 if "Tesis de Inversión y Supuestos" in titles else len(titles)
        ws = sh.add_worksheet(ORIGEN, rows=120, cols=_NCOL, index=idx)
    rows = origen_rows()
    values = [cells + [""] * (_NCOL - len(cells)) for _, cells, _ in rows]
    ws.update(values=values, range_name="A1", value_input_option="USER_ENTERED")

    q = Req(ws.id)
    n = len(rows)
    q.sheet_props(frozen_rows=1, tab=NAVY)
    q.fmt(1, n + 5, 1, _NCOL, textFormat=_txt(), verticalAlignment="MIDDLE", wrapStrategy="WRAP", backgroundColor=WHITE)
    q.width(1, 1, 240), q.width(2, 4, 100), q.width(5, 5, 360), q.width(6, _NCOL, 100)
    zebra = False
    for i, (kind, cells, nf) in enumerate(rows, start=1):
        if kind == "title":
            q.merge(i, i, 1, _NCOL)
            q.fmt(i, i, 1, _NCOL, textFormat=_txt(16, bold=True, color=NAVY), verticalAlignment="BOTTOM")
            q.height(i, i, 40)
        elif kind == "subtitle":
            q.merge(i, i, 1, _NCOL)
            q.fmt(i, i, 1, _NCOL, textFormat=_txt(10, italic=True, color=MUTED))
        elif kind == "section":
            q.merge(i, i, 1, _NCOL)
            q.fmt(i, i, 1, _NCOL, textFormat=_txt(11, bold=True, color=WHITE), backgroundColor=NAVY)
            q.height(i, i, 28)
            zebra = False
        elif kind in ("para", "note"):
            q.merge(i, i, 1, _NCOL)
            q.fmt(i, i, 1, _NCOL, textFormat=_txt(10 if kind == "para" else 9, italic=kind == "note", color=INK if kind == "para" else MUTED),
                  verticalAlignment="TOP")
        elif kind == "header":
            q.fmt(i, i, 1, _NCOL, textFormat=_txt(9, bold=True, color=NAVY), backgroundColor=HEAD_BG, horizontalAlignment="CENTER")
            q.fmt(i, i, 1, 1, horizontalAlignment="LEFT")
            q.borders(i, i, 1, _NCOL)
        elif kind == "data":
            zebra = not zebra
            q.fmt(i, i, 1, _NCOL, backgroundColor=ZEBRA if zebra else WHITE)
            q.fmt(i, i, 1, 1, textFormat=_txt(10, bold=True))
            q.fmt(i, i, 5, 5, textFormat=_txt(9, color=MUTED))
            if nf:
                q.fmt(i, i, 2, 4, numberFormat={"type": "NUMBER", "pattern": nf}, horizontalAlignment="RIGHT")
                q.fmt(i, i, 6, _NCOL, numberFormat={"type": "NUMBER", "pattern": nf}, horizontalAlignment="RIGHT")
            q.fmt(i, i, 3, 3, textFormat=_txt(10, bold=True, color=NAVY))
            q.borders(i, i, 1, _NCOL)
    # la columna "Peso" de la seccion 7 es porcentaje
    for i, (kind, cells, _) in enumerate(rows, start=1):
        if kind == "data" and len(cells) >= 6 and str(cells[5]).startswith(f"={RS}!B"):
            q.fmt(i, i, 6, 6, numberFormat={"type": "NUMBER", "pattern": "0%"})
    _retry(lambda: sh.batch_update({"requests": q.items}))
    _retry(lambda: sh.batch_update({"requests": fit_row_heights(sh, ws, 2, n, size_by_row={1: 16})}))


# --- formato de las hojas de texto -------------------------------------------

_SECTION = re.compile(r"^\s*\d+\.\s+\S")


def _cells(ws_values: list[list], r: int) -> list[str]:
    row = ws_values[r - 1] if r - 1 < len(ws_values) else []
    return [str(v) for v in row]


def style_tesis(sh) -> None:
    ws = sh.worksheet("Tesis de Inversión y Supuestos")
    vals = ws.get("A1:H130", value_render_option="FORMULA")
    n = len(vals)
    if not n:
        return
    ncol = 5
    q = Req(ws.id)
    q.unmerge(1, max(n, 1) + 5, 1, 8)
    q.sheet_props(frozen_rows=0, tab=NAVY)
    q.fmt(1, n, 1, 8, textFormat=_txt(), wrapStrategy="WRAP", verticalAlignment="TOP", backgroundColor=WHITE,
          borders={})
    q.width(1, 1, 290), q.width(2, 4, 120), q.width(5, 5, 440)

    # caso alcista / bajista: el bajista se mueve de B a D para que ambos tengan media pagina
    moves: dict[str, str] = {}
    bull = [r for r in range(1, n + 1) if _cells(vals, r)[:1] and _cells(vals, r)[0].lower().startswith("caso alcista")]
    bull_rows: list[int] = []
    if bull:
        r = bull[0]
        while r <= n and any(x.strip() for x in _cells(vals, r)):
            c = [x.strip() for x in _cells(vals, r) + [""] * 5]
            if not any(c[2:5]):            # layout original: bajista en B
                if c[1]:
                    moves[f"B{r}"], moves[f"D{r}"] = "", _cells(vals, r)[1]
            elif c[1] or c[2] or c[4]:     # otra estructura: no se toca
                bull_rows, moves = [], {}
                break
            bull_rows.append(r)            # (o ya movido a D en una corrida anterior)
            r += 1
    if moves:
        # primero descombinar: en la Tesis original el bajista suele estar
        # combinado B:E, y un valor escrito en D (celda cubierta) se pierde.
        _retry(lambda: sh.batch_update({"requests": [{"unmergeCells": {"range": q.grid(1, n + 5, 1, 8)}}]}))
        safe = {k: (v if v.startswith("=") or v[:1] not in "+-" else "'" + v) for k, v in moves.items()}
        ws.batch_update([{"range": k, "values": [[v]]} for k, v in safe.items()], value_input_option="USER_ENTERED")

    zebra = False
    header_next = False
    for r in range(1, n + 1):
        c = _cells(vals, r)
        filled = [i for i, x in enumerate(c[:ncol]) if x.strip()]
        if not filled:
            header_next = False
            continue
        first = c[0] if c else ""
        if r in bull_rows:
            q.merge(r, r, 1, 3), q.merge(r, r, 4, 5)
            if r == bull_rows[0]:
                q.fmt(r, r, 1, 3, textFormat=_txt(10, bold=True, color=_rgb("1E6B3A")), backgroundColor=GREEN_BG)
                q.fmt(r, r, 4, 5, textFormat=_txt(10, bold=True, color=_rgb("9C2B23")), backgroundColor=RED_BG)
            else:
                q.fmt(r, r, 1, 5, textFormat=_txt(10), backgroundColor=WHITE)
                q.borders(r, r, 1, 5)
            continue
        if r == 1:
            q.merge(1, 1, 1, ncol)
            q.fmt(1, 1, 1, ncol, textFormat=_txt(16, bold=True, color=NAVY), verticalAlignment="BOTTOM")
            continue
        if r == 2 and filled == [0]:
            q.merge(2, 2, 1, ncol)
            q.fmt(2, 2, 1, ncol, textFormat=_txt(10, italic=True, color=MUTED))
            continue
        if filled == [0] and _SECTION.match(first):
            q.merge(r, r, 1, ncol)
            q.fmt(r, r, 1, ncol, textFormat=_txt(11, bold=True, color=WHITE), backgroundColor=NAVY, verticalAlignment="MIDDLE")
            header_next, zebra = True, False
            continue
        if filled == [0]:
            q.merge(r, r, 1, ncol)
            note = first.startswith(("*", "Fuentes", "=IF(AND"))
            q.fmt(r, r, 1, ncol, textFormat=_txt(9 if note else 10, italic=note, color=MUTED if note else INK))
            header_next = False
            continue
        if header_next:
            q.fmt(r, r, 1, ncol, textFormat=_txt(9, bold=True, color=NAVY), backgroundColor=HEAD_BG, verticalAlignment="MIDDLE")
            q.borders(r, r, 1, ncol)
            header_next = False
            continue
        zebra = not zebra
        q.fmt(r, r, 1, ncol, backgroundColor=ZEBRA if zebra else WHITE)
        q.fmt(r, r, 1, 1, textFormat=_txt(10, bold=True))
        q.fmt(r, r, 5, 5, textFormat=_txt(9, color=INK))
        q.borders(r, r, 1, ncol)
    _retry(lambda: sh.batch_update({"requests": q.items}))
    _retry(lambda: sh.batch_update({"requests": fit_row_heights(sh, ws, 1, n, size_by_row={1: 16})}))


NOTE_RECOMENDADOS = (
    "Nota: el escenario Base (Input sheet B27–B33) lo fija el analista; esta tabla deja la recomendación, su justificación y las "
    "anclas (mín./máx. de 10 años de la empresa y mediana/promedio de sus peers). Conservador y Optimista NO se eligen aquí: salen de "
    "reglas sobre el Base en 'Valuation output' (C45, C47, C55, C106). De dónde sale cada número: hoja «Origen de los Supuestos».")
NOTE_MULTIPLOS = (
    "Cómo se fija el múltiplo de salida en las 5 hojas de múltiplos (EVFCFF, POCF, PE, PFCFE, EVEBITDA): el escenario BASE usa el MENOR "
    "múltiplo POSITIVO de los últimos 4 cierres fiscales (celda J19 de cada hoja; si no hay ninguno positivo, la mediana de 5 años). Es un "
    "ancla conservadora: no extrapola múltiplos de pico. Conservador = Base × 0,9 y Optimista = Base × 1,1. Si se escribe un número en "
    "J8/J19/J30, reemplaza el cálculo automático (columna E). El precio sale al cierre FY+3, con la deuda neta restada en los múltiplos EV "
    "y los dividendos acumulados sumados. Detalle: hoja «Origen de los Supuestos».")


def _refresh_note(ws, starts: tuple[str, ...], text: str, header: dict[str, tuple[str, str]] | None = None) -> None:
    """Actualiza el texto boilerplate de la plantilla (fila 3 y encabezados)
    solo si todavia es el de la plantilla."""
    a3 = ws.acell("A3").value or ""
    data = []
    if a3.startswith(starts):
        data.append({"range": "A3", "values": [[text]]})
    for cell, (old, new) in (header or {}).items():
        if (ws.acell(cell).value or "") == old:
            data.append({"range": cell, "values": [[new]]})
    if data:
        ws.batch_update(data, value_input_option="RAW")


def style_supuestos(sh, title: str, widths: list[int], text_cols: tuple[int, ...], header_row: int = 5,
                    number_formats: dict[int, str] | None = None,
                    cell_formats: list[tuple[int, int, int, int, str]] = ()) -> None:
    """'Supuestos Recomendados' / 'Supuestos de los Múltiplos': titulo en la
    fila 2, nota en la 3, tabla con encabezado en la 5 y parrafos sueltos
    (una sola celda llena) debajo."""
    ws = sh.worksheet(title)
    if title == "Supuestos Recomendados":
        _refresh_note(ws, ("Nota: 'Modelo Base'",), NOTE_RECOMENDADOS)
    elif title == "Supuestos de los Múltiplos":
        _refresh_note(ws, ("Como se fija el multiplo",), NOTE_MULTIPLOS,
                      {"C5": ("Base (MIN últimos 4Y)", "Base (mín. positivo 4 cierres)")})
    vals = ws.get("A1:M40", value_render_option="FORMULA")
    n, ncol = len(vals), len(widths)
    if n < header_row:
        return
    q = Req(ws.id)
    q.unmerge(2, n + 3, 1, ncol)
    q.sheet_props(frozen_rows=header_row, tab=NAVY)
    q.fmt(2, n + 3, 1, ncol, textFormat=_txt(), wrapStrategy="WRAP", verticalAlignment="MIDDLE", backgroundColor=WHITE)
    for i, w in enumerate(widths, start=1):
        q.width(i, i, w)
    q.fmt(1, 1, 1, ncol, textFormat=_txt(9, bold=True, color=MUTED))
    q.merge(2, 2, 1, ncol)
    q.fmt(2, 2, 1, ncol, textFormat=_txt(15, bold=True, color=NAVY), verticalAlignment="BOTTOM")
    q.merge(3, 3, 1, ncol)
    q.fmt(3, 3, 1, ncol, textFormat=_txt(9, italic=True, color=MUTED), verticalAlignment="TOP")
    q.fmt(header_row, header_row, 1, ncol, textFormat=_txt(9, bold=True, color=NAVY), backgroundColor=HEAD_BG,
          horizontalAlignment="CENTER", verticalAlignment="MIDDLE")
    q.borders(header_row, header_row, 1, ncol)
    last = header_row
    for r in range(header_row + 1, n + 1):
        c = _cells(vals, r)
        filled = [i for i, x in enumerate(c[:ncol]) if x.strip()]
        if not filled:
            continue
        if filled == [0] and r > header_row + 1 and len(c[0]) > 60:
            q.merge(r, r, 1, ncol)
            q.fmt(r, r, 1, ncol, textFormat=_txt(9, color=INK), verticalAlignment="TOP", backgroundColor=_rgb("FFF8E5"))
            q.borders(r, r, 1, ncol, inner=False, color=_rgb("E8D9A8"))
            continue
        last = r
        q.fmt(r, r, 1, ncol, backgroundColor=ZEBRA if (r - header_row) % 2 == 0 else WHITE)
        q.fmt(r, r, 1, 1, textFormat=_txt(10, bold=True))
        for tc in text_cols:
            q.fmt(r, r, tc, tc, textFormat=_txt(9), horizontalAlignment="LEFT", verticalAlignment="TOP")
        for col, pat in (number_formats or {}).items():
            q.fmt(r, r, col, col, numberFormat={"type": "NUMBER", "pattern": pat}, horizontalAlignment="RIGHT")
    for r0, r1, c0, c1, pat in cell_formats:
        q.fmt(r0, r1, c0, c1, numberFormat={"type": "NUMBER", "pattern": pat}, horizontalAlignment="RIGHT")
    if last > header_row:
        q.borders(header_row + 1, last, 1, ncol)
    _retry(lambda: sh.batch_update({"requests": q.items}))
    _retry(lambda: sh.batch_update({"requests": fit_row_heights(sh, ws, 2, n, size_by_row={2: 15})}))


def style_wrap_only(sh, title: str, r0: int, r1: int, ncol: int, widths: list[int] | None = None) -> None:
    """Hojas con diseño propio (Cualitativo, Stories to Numbers): no se
    toca la paleta; solo se asegura texto ajustado, alineacion arriba y un
    alto de fila suficiente para que nada quede cortado."""
    ws = sh.worksheet(title)
    q = Req(ws.id)
    q.fmt(r0, r1, 1, ncol, wrapStrategy="WRAP", verticalAlignment="TOP")
    for i, w in enumerate(widths or [], start=1):
        q.width(i, i, w)
    _retry(lambda: sh.batch_update({"requests": q.items}))
    _retry(lambda: sh.batch_update({"requests": fit_row_heights(sh, ws, r0, r1)}))


def tesis_live_results(sh) -> bool:
    """Seccion 3 de la Tesis (resultado por escenario): si quedo con cifras
    TIPEADAS (p.ej. "$155,16"), se reemplaza por formulas vivas para que no
    queden desactualizadas tras cualquier cambio del modelo."""
    ws = sh.worksheet("Tesis de Inversión y Supuestos")
    vals = ws.get("A1:E90", value_render_option="FORMULA")
    labels = [(_cells(vals, r) + [""])[0].strip() for r in range(1, len(vals) + 1)]
    for i in range(1, len(labels) - 2):
        if labels[i:i + 3] != ["Conservador", "Base", "Optimista"]:
            continue
        sec = next((labels[j] for j in range(i - 1, -1, -1) if _SECTION.match(labels[j] or "")), "")
        if "RESULTADO" not in sec.upper():
            continue
        body = [(_cells(vals, i + 1 + k) + [""] * 5)[1:5] for k in range(3)]
        if all(str(x).startswith("=") for row in body for x in row if str(x).strip()):
            return False
        r = i + 1  # fila 1-based de 'Conservador'
        price = f"{RS}!$C$25"
        data = [["Escenario", "Valor DCF hoy / acción", "Precio objetivo ponderado (3 años)",
                 "DCF vs. precio del análisis", "Ponderado vs. precio del análisis"]]
        for k, (dcf, res) in enumerate((("B86", "C12"), ("B35", "D12"), ("B137", "E12"))):
            rr = r + k
            data.append([labels[i + k], f"={VO}!{dcf}", f"={RS}!{res}", f"=B{rr}/{price}-1", f"=C{rr}/{price}-1"])
        ws.update(values=data, range_name=f"A{r - 1}", value_input_option="USER_ENTERED")
        q = Req(ws.id)
        q.fmt(r, r + 2, 2, 3, numberFormat={"type": "NUMBER", "pattern": NUM})
        q.fmt(r, r + 2, 4, 5, numberFormat={"type": "NUMBER", "pattern": "+0.0%;-0.0%"})
        _retry(lambda: sh.batch_update({"requests": q.items}))
        return True
    return False


def resumen_note(sh) -> None:
    """Nota bajo el Resumen explicando el horizonte (solo si A28 esta libre
    y el DCF ya fue llevado a 3 años por audit_fix_model.py)."""
    ws = sh.worksheet("Resumen de Valoración")
    got = ws.get("A28:E29", value_render_option="FORMULA")
    c6 = ws.acell("C6", value_render_option="FORMULA").value or ""
    if any(str(v).strip() for row in got for v in row) or "^3" not in c6:
        return
    ws.update(values=[["Horizonte común de 3 años: el DCF (valor intrínseco hoy) se lleva a 3 años × (1 + Ke)³ y los múltiplos dan "
                       "el precio al cierre FY+3 más los dividendos acumulados. De dónde sale cada supuesto: hoja «Origen de los Supuestos»."]],
              range_name="A28", value_input_option="RAW")
    q = Req(ws.id)
    q.merge(28, 28, 1, 5)
    q.fmt(28, 28, 1, 5, textFormat=_txt(9, italic=True, color=MUTED), wrapStrategy="WRAP", verticalAlignment="TOP")
    q.height(28, 28, 48)
    _retry(lambda: sh.batch_update({"requests": q.items}))


def present(client, sheet_id: str) -> list[str]:
    sh = _retry(lambda: client.open_by_key(sheet_id))
    titles = {w.title for w in _retry(sh.worksheets)}
    backup = BACKUP_DIR / f"{sheet_id}_textos.json"
    if not backup.exists():  # contenido de las hojas de texto ANTES de tocarlas
        names = [t for t in _TEXT_SHEETS if t in titles]
        got = _retry(lambda: sh.values_batch_get([f"'{t}'!A1:M130" for t in names], params={"valueRenderOption": "FORMULA"}))
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        backup.write_text(json.dumps({"title": sh.title, "sheets": {t: g.get("values", []) for t, g in zip(names, got["valueRanges"])}},
                                     ensure_ascii=False, indent=1))
    done = []
    steps = [
        (ORIGEN, lambda: build_origen(sh)),
        ("Tesis de Inversión y Supuestos", lambda: (tesis_live_results(sh), style_tesis(sh))),
        ("Supuestos Recomendados", lambda: style_supuestos(
            sh, "Supuestos Recomendados", [250, 110, 110, 430, 90, 90, 100, 100], text_cols=(4,),
            cell_formats=[(6, 9, 2, 3, PCT), (6, 9, 5, 8, PCT), (10, 10, 2, 3, INT), (11, 12, 2, 3, "0.00")])),
        ("Supuestos de los Múltiplos", lambda: style_supuestos(
            sh, "Supuestos de los Múltiplos", [110, 110, 120, 110, 150, 85, 85, 85, 85, 85, 85, 95, 95], text_cols=(5,),
            number_formats={c: '0.0"x"' for c in (2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13)})),
        ("Cualitativo", lambda: style_wrap_only(sh, "Cualitativo", 1, 60, 8, widths=[230, 330, 300, 360])),
        ("Stories to Numbers", lambda: style_wrap_only(sh, "Stories to Numbers", 3, 15, 8)),
        ("Resumen de Valoración", lambda: resumen_note(sh)),
    ]
    for name, fn in steps:
        if name != ORIGEN and name not in titles:
            continue
        try:
            _retry(fn)
            done.append(name)
        except (APIError, WorksheetNotFound, ValueError) as exc:
            done.append(f"{name}: ERROR {str(exc)[:120]}")
        time.sleep(2)
    return done


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--sheet-id", action="append")
    g.add_argument("--targets-json")
    args = ap.parse_args(argv)
    targets = [(s, s) for s in args.sheet_id] if args.sheet_id else [tuple(t[:2]) for t in json.loads(Path(args.targets_json).read_text())]
    client = get_gspread_client()
    for sid, name in targets:
        print(f"{name[:60]:60s}", " | ".join(present(client, sid)), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
