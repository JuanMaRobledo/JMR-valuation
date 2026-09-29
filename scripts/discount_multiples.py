#!/usr/bin/env python
"""Multiplos a valor presente en 1, 2 y 3 años (29-sep-2026).

El DCF da el valor por accion HOY; cada multiplo da un precio al cierre de
FY+1, FY+2 y FY+3 (multiplo x metrica proyectada) mas los dividendos
acumulados hasta ese año. Esos precios estan en dolares futuros y no se
pueden ponderar con el DCF tal cual. Este script deja en la plantilla
maestra y en cada valoracion:

1. Hoja 'Descuento de múltiplos' (se reconstruye entera):
   - Por metodo (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF), escenario y
     horizonte n = 1, 2, 3:
         VP_n = (Precio objetivo FY+n + Dividendos acumulados FY+1..FY+n) / (1 + Ke)^n
     Los dividendos se suman nominales (simplificacion decidida); el total
     de cada horizonte ya viene asi de las hojas de multiplos (filas 12, 23
     y 34, columnas F:H). 5 metodos x 3 horizontes = 15 VP por escenario.
   - Consolidado por metodo: promedio simple de los 3 VP (por defecto) o
     solo el de 3 años (celda C6, lista desplegable).
   - Multiplos consolidados = promedio de los 5 metodos con sus pesos del
     Resumen reescalados a 100% dentro de los multiplos.
   - Valor intrinseco ponderado = DCF x peso DCF + multiplos x peso multiplos
     (pesos de la categoria de empresa, 'Resumen de Valoración' I5:U11).
   - Chequeo: VP a 3 años < precio FY+3 sin descontar, por metodo y total.
   Ke = 'Cost of capital worksheet'!B63 (costo del patrimonio del DCF, el
   mismo que usa el Resumen para llevar el DCF a FY+3), con entrada manual
   en C5. Es la tasa correcta para un precio por accion (patrimonio); el
   WACC descuenta flujos a la firma.

2. 'Resumen de Valoración' filas 28-47: bloque "valor por accion hoy" con
   las tres cifras por separado (DCF, multiplos consolidados y ponderado)
   y cada metodo a valor hoy. Las celdas C32:E34 conservan su significado
   (DCF / multiplos / combinado hoy) para el visor web.

El bloque superior del Resumen (precio FY+3, CAGR, zonas) no cambia.
Antes de escribir se respaldan la hoja anterior y el bloque del Resumen en
reference/backups/descuento_multiples_2026-09-29/<id>.json. Si las filas
29-50 del Resumen tienen algo que no es el bloque conocido, no se tocan y
la hoja queda listada como "personalizada".

Uso:
    PYTHONPATH=.:scripts python scripts/discount_multiples.py --sheet-id ID [--dry-run]
    PYTHONPATH=.:scripts python scripts/discount_multiples.py --targets-json targets.json [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
for p in (_ROOT, _ROOT / "scripts"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

from gspread.exceptions import APIError, SpreadsheetNotFound  # noqa: E402

from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402
from model_presentation import (  # noqa: E402
    HEAD_BG, MUTED, NAVY, NUM, PCT, WHITE, ZEBRA, GREEN_BG, Req, _retry, _txt,
)

SHEET = "Descuento de múltiplos"
RES = "Resumen de Valoración"
Q = f"'{SHEET}'"
R = f"'{RES}'"
BACKUP_DIR = _ROOT / "reference" / "backups" / "descuento_multiples_2026-09-29"

# (hoja del multiplo, fila del metodo en el Resumen)
METHODS = (("EVEBITDA", 7), ("EVFCFF", 8), ("PE", 9), ("PFCFE", 10), ("POCF", 11))
# escenario -> (fila de "Total Target Price + Dividends" en las hojas de multiplos,
#               celda del DCF hoy en 'Valuation output', columna del Resumen)
SCENARIOS = (("Conservador", 12, "B86", "C"), ("Base", 23, "B35", "D"), ("Optimista", 34, "B137", "E"))
FIRST_ROW = {"Conservador": 11, "Base": 20, "Optimista": 29}  # primera fila de metodos de cada bloque
KE, CRIT, DEFAULT_CRIT, ONLY3 = "$B$5", "$B$6", "Promedio 1-3 años", "Solo 3 años"
SUM_TITLE, SUM_HDR, SUM_DCF, SUM_MULT, SUM_W, SUM_PRICE, SUM_DISC, SUM_MOS = 36, 37, 38, 39, 40, 41, 42, 43
CHK_TITLE, CHK_HDR, CHK_NOM, CHK_PV, CHK_OK = 45, 46, 47, 48, 49
NOTE_ROW = 51
NCOL = 11

@dataclass(frozen=True)
class Layout:
    """Donde esta cada cosa en una hoja concreta. DEFAULT = plantilla maestra actual; las
    versiones anteriores (jul-ago 2026) nombran las hojas 'EV/EBITDA' o 'EV∕EBITDA', usan
    ',' como separador (locale es_MX) o tienen todo una fila mas arriba."""
    sheets: tuple[str, ...] = tuple(s for s, _ in METHODS)        # nombre real de cada hoja de multiplo
    src_rows: tuple[int, int, int] = (12, 23, 34)                  # "Total Target Price + Dividends"
    res_dcf_row: int = 6
    res_rows: tuple[int, ...] = tuple(r for _, r in METHODS)        # filas de los 5 multiplos en el Resumen
    dcf_refs: tuple[str, str, str] = ("B86", "B35", "B137")         # DCF hoy en 'Valuation output'
    ke_expr: str = "IFERROR('Cost of capital worksheet'!B63;'Input sheet'!B36)"
    ke_label: str = "'Cost of capital worksheet'!B63"
    mos_ref: str = "G4"
    price_ref: str = "'Input sheet'!D1"
    title_expr: str = "'Input sheet'!A1"
    sep: str = ";"

    def q(self, i: int) -> str:
        return "'" + self.sheets[i].replace("'", "''") + "'" if not self.sheets[i].isalnum() else self.sheets[i]


DEFAULT = Layout()


def _localize(rows: list[list[str]], sep: str) -> list[list[str]]:
    """Las formulas se escriben con ';' (locale es_CO); en hojas con ',' como separador
    (es_MX, en_US) se cambia fuera de los textos entre comillas, y el formato de TEXT()."""
    if sep == ";":
        return rows

    def conv(v: str) -> str:
        if not v.startswith("="):
            return v
        parts = v.split('"')
        for i in range(0, len(parts), 2):
            parts[i] = parts[i].replace(";", ",")
        return '"'.join(parts).replace('"0,00%"', '"0.00%"')
    return [[conv(v) for v in row] for row in rows]


_NORM = lambda t: re.sub(r"[/∕ ]", "", t).upper()  # noqa: E731


def detect_layout(sh) -> tuple[Layout | None, str]:
    """Ubica hojas, filas y celdas por sus rotulos. Devuelve (None, motivo) si no es el modelo."""
    titles = [w.title for w in sh.worksheets()]
    names = []
    for key, _ in METHODS:
        found = [t for t in titles if _NORM(t) == key]
        if not found:
            return None, f"falta la hoja {key}"
        names.append(found[0])
    for t in (RES, "Valuation output"):
        if t not in titles:
            return None, f"falta la hoja {t}"
    quoted = ["'" + n + "'" for n in names]
    ranges = [f"{q}!A1:A60" for q in quoted] + [f"{R}!A1:G26"]
    has_coc = "Cost of capital worksheet" in titles
    if has_coc:
        ranges.append("'Cost of capital worksheet'!A50:A80")
    vr = sh.values_batch_get(ranges, params={"valueRenderOption": "FORMULA"})["valueRanges"]
    src = None
    for v in vr[:5]:
        rows = tuple(i + 1 for i, r in enumerate(v.get("values", [])) if r and "Total Target Price" in str(r[0]))
        if len(rows) != 3 or (src and rows != src):
            return None, f"filas 'Total Target Price' no reconocidas en {names}: {rows}"
        src = rows
    res = [r + [""] * (7 - len(r)) for r in vr[5].get("values", [])]
    col_a = [str(r[0]).strip() for r in res]
    if "DCF Damodaran" not in col_a:
        return None, "Resumen sin fila 'DCF Damodaran'"
    dcf_row = col_a.index("DCF Damodaran") + 1
    labels = ["EV/EBITDA", "EV/FCFF", "P/E", "P/FCFE", "P/OCF"]
    if col_a[dcf_row:dcf_row + 5] != labels:
        return None, f"Resumen: multiplos no siguen al DCF ({col_a[dcf_row:dcf_row + 5]})"
    refs = []
    for c in (2, 3, 4):
        m = re.search(r"'Valuation output'!\$?B\$?(\d+)", str(res[dcf_row - 1][c]))
        if not m:
            return None, f"DCF del Resumen sin referencia a 'Valuation output': {res[dcf_row - 1][c]}"
        refs.append(f"B{m.group(1)}")
    sep = ";" if ";" in str(res[dcf_row - 1][1]) else ","
    mos = next((f"G{i + 1}" for i, r in enumerate(res) if str(r[5]).startswith("Margen de Seguridad")), None)
    if not mos:
        return None, "Resumen sin 'Margen de Seguridad (MOS)'"
    ke_expr, ke_label = "'Input sheet'!B36", "'Input sheet'!B36"
    if has_coc:
        coc = [str(r[0]).strip() if r else "" for r in vr[6].get("values", [])]
        if "Cost of Component" in coc:
            cell = f"'Cost of capital worksheet'!B{50 + coc.index('Cost of Component')}"
            ke_expr, ke_label = f"IFERROR({cell};'Input sheet'!B36)", cell
    a1, c1, d1 = str(res[0][0]), str(res[0][2]).strip(), str(res[0][3])
    if a1 == "='Input sheet'!A1":
        title = "'Input sheet'!A1"
    elif a1.strip().upper() == "TICKER":
        title = f"{R}!B1"
    else:
        title = '"' + sh.title.replace('"', "'") + '"'
    if d1 == "='Input sheet'!D1" or (c1 == "Precio" and "Input sheet" in d1):
        price = "'Input sheet'!D1"
    elif c1 == "Precio":
        price = f"{R}!D1"
    else:
        row = next((i + 1 for i, a in enumerate(col_a) if a.startswith("Precio al día del análisis")), None)
        if not row:
            return None, "Resumen sin precio de referencia"
        price = f"{R}!B{row}"
    return Layout(sheets=tuple(names), src_rows=src, res_dcf_row=dcf_row,
                  res_rows=tuple(range(dcf_row + 1, dcf_row + 6)), dcf_refs=tuple(refs), ke_expr=ke_expr,
                  ke_label=ke_label, mos_ref=mos, price_ref=price, title_expr=title, sep=sep), ""


HEADERS = ["Método", "Peso total", "Peso en múltiplos", "Precio + div. FY+1", "Precio + div. FY+2",
           "Precio + div. FY+3", "VP 1 año", "VP 2 años", "VP 3 años", "Consolidado hoy", "Chequeo VP3 < FY+3"]


def _method_row(sheet: str, res_row: int, r: int, first: int, src_row: int) -> list[str]:
    last = first + len(METHODS) - 1
    return [
        f"={R}!A{res_row}",
        f"={R}!B{res_row}",
        f"=IFERROR(B{r}/SUM($B${first}:$B${last});0)",
        f"={sheet}!F{src_row}", f"={sheet}!G{src_row}", f"={sheet}!H{src_row}",
        f'=IFERROR(D{r}/(1+{KE});"")',
        f'=IFERROR(E{r}/(1+{KE})^2;"")',
        f'=IFERROR(F{r}/(1+{KE})^3;"")',
        f'=IFERROR(IF({CRIT}="{ONLY3}";I{r};AVERAGE(G{r}:I{r}));"")',
        f'=IF(NOT(ISNUMBER(I{r}));"";IF(F{r}<=0;"n/a (≤ 0)";IF(I{r}<F{r};"OK";"REVISAR")))',
    ]


def _total_row(r: int, first: int) -> list[str]:
    last = first + len(METHODS) - 1
    rng = lambda c: f"{c}{first}:{c}{last}"  # noqa: E731
    row = ["Múltiplos consolidados", f"=SUM({rng('B')})", f"=SUM({rng('C')})"]
    for c in "DEFGHIJ":
        row.append(f'=IFERROR(SUMPRODUCT($C${first}:$C${last};{rng(c)});"")')
    row.append(f'=IF(NOT(ISNUMBER(I{r}));"";IF(F{r}<=0;"n/a (≤ 0)";IF(I{r}<F{r};"OK";"REVISAR")))')
    return row


def sheet_values(lay: Layout = DEFAULT) -> list[list[str]]:
    """Contenido completo de la hoja (filas 1..NOTE_ROW+3, columnas A:K)."""
    rows: list[list[str]] = [[""] * NCOL for _ in range(NOTE_ROW + 3)]

    def put(r: int, values: list[str], c0: int = 0):
        for i, v in enumerate(values):
            rows[r - 1][c0 + i] = v

    put(1, [f"={lay.title_expr}&\" · Múltiplos a valor presente (1, 2 y 3 años)\""])
    put(2, ["Cada múltiplo da un precio objetivo al cierre de FY+1, FY+2 y FY+3 (múltiplo × métrica proyectada ÷ acciones). "
            "Se le suman los dividendos por acción acumulados hasta ese año, sin descontarlos uno a uno, y el total se trae a hoy "
            "con el costo del patrimonio: VP = (Precio FY+n + Dividendos FY+1..FY+n) ÷ (1 + Ke)^n."])
    put(4, ["Parámetro", "Valor usado", "Entrada manual", "Automático"])
    put(5, ["Tasa de descuento: Ke (costo del patrimonio del DCF)", "=IF(ISNUMBER(C5);C5;D5)", "",
            f"={lay.ke_expr}"])
    put(6, ["Criterio para consolidar cada método", f'=IF(C6="{ONLY3}";"{ONLY3}";"{DEFAULT_CRIT}")', "", DEFAULT_CRIT])
    put(7, ["Factor de descuento a 1, 2 y 3 años", "=1/(1+B5)", "=1/(1+B5)^2", "=1/(1+B5)^3"])

    for k, (name, *_rest) in enumerate(SCENARIOS):
        first = FIRST_ROW[name]
        put(first - 2, [name.upper()])
        put(first - 1, HEADERS)
        for i in range(len(METHODS)):
            put(first + i, _method_row(lay.q(i), lay.res_rows[i], first + i, first, lay.src_rows[k]))
        put(first + len(METHODS), _total_row(first + len(METHODS), first))

    put(SUM_TITLE, ["VALOR INTRÍNSECO HOY · DCF + MÚLTIPLOS DESCONTADOS"])
    put(SUM_HDR, ["Concepto", "Peso", "Conservador", "Base", "Optimista"])
    put(SUM_DCF, ["DCF (valor presente)", f"={R}!B{lay.res_dcf_row}"] + [f"='Valuation output'!{d}" for d in lay.dcf_refs])
    put(SUM_MULT, ["Múltiplos consolidados (valor presente)", f"=SUM({R}!B{lay.res_rows[0]}:B{lay.res_rows[-1]})"]
        + [f"=J{FIRST_ROW[n] + len(METHODS)}" for n, *_ in SCENARIOS])
    put(SUM_W, ["Valor intrínseco ponderado", f"=B{SUM_DCF}+B{SUM_MULT}"]
        + [f'=IFERROR({c}{SUM_DCF}*$B${SUM_DCF}+{c}{SUM_MULT}*$B${SUM_MULT};"")' for c in "CDE"])
    put(SUM_PRICE, ["Precio de referencia de la hoja", f"={lay.price_ref}"])
    put(SUM_DISC, ["Descuento del precio frente al ponderado", ""]
        + [f'=IFERROR(1-$B${SUM_PRICE}/{c}{SUM_W};"")' for c in "CDE"])
    put(SUM_MOS, ["Precio de compra con MOS", f"={R}!{lay.mos_ref}"]
        + [f'=IFERROR({c}{SUM_W}*(1-$B${SUM_MOS});"")' for c in "CDE"])

    put(CHK_TITLE, ["CHEQUEO MATEMÁTICO · MÚLTIPLOS A 3 AÑOS"])
    put(CHK_HDR, ["Concepto", "", "Conservador", "Base", "Optimista"])
    put(CHK_NOM, ["Múltiplos FY+3 sin descontar (ponderado)", ""]
        + [f"=F{FIRST_ROW[n] + len(METHODS)}" for n, *_ in SCENARIOS])
    put(CHK_PV, ["Múltiplos a 3 años descontados (ponderado)", ""]
        + [f"=I{FIRST_ROW[n] + len(METHODS)}" for n, *_ in SCENARIOS])
    put(CHK_OK, ["VP a 3 años < FY+3 sin descontar", ""]
        + [f'=IF(NOT(ISNUMBER({c}{CHK_PV}));"";IF({c}{CHK_NOM}<=0;"n/a (≤ 0)";IF({c}{CHK_PV}<{c}{CHK_NOM};"OK";"REVISAR")))'
           for c in "CDE"])

    put(NOTE_ROW, [f"Fuentes: precio + dividendos de cada horizonte = filas {', '.join(map(str, lay.src_rows))} (columnas F:H) "
                   f"de {', '.join(lay.sheets)}; dividendos por acción de «Financials Multiples». Ke = {lay.ke_label} "
                   "(C5 lo reemplaza). C6 = «Solo 3 años» usa solo el VP a 3 años; vacío = promedio simple de 1, 2 y 3 años."])
    put(NOTE_ROW + 1, ["Los pesos salen de la categoría de empresa del Resumen (I5:U11): el DCF conserva su peso y el de los "
                       "múltiplos se reparte entre los 5 métodos en la misma proporción. Resumen C32:E47 muestra DCF, múltiplos "
                       "consolidados, ponderado y cada método por separado."])
    return _localize(rows, lay.sep)


RES_FIRST, RES_LAST = 28, 50


def resumen_values(lay: Layout = DEFAULT) -> list[list[str]]:
    """'Resumen de Valoración' A28:E50."""
    rows = [[""] * 5 for _ in range(RES_LAST - RES_FIRST + 1)]

    def put(r: int, values: list[str]):
        for i, v in enumerate(values):
            rows[r - RES_FIRST][i] = v

    put(28, ["Arriba: precio al cierre FY+3 (DCF × (1 + Ke)³ y múltiplos con dividendos). Abajo: valor por acción HOY — "
             "cada múltiplo se trae a valor presente en 1, 2 y 3 años y se consolida; el DCF ya está en valor presente. "
             "Detalle en «Descuento de múltiplos»."])
    put(30, ["VALOR POR ACCIÓN HOY | DCF + MÚLTIPLOS DESCONTADOS"])
    put(31, ["Método", "Peso", "Conservador", "Base", "Optimista"])
    d, m0, m1 = lay.res_dcf_row, lay.res_rows[0], lay.res_rows[-1]
    for r, label, src, w in ((32, "DCF hoy (valor presente)", SUM_DCF, f"=B{d}"),
                             (33, "Múltiplos consolidados hoy", SUM_MULT, f"=SUM(B{m0}:B{m1})"),
                             (34, "Valor intrínseco ponderado hoy", SUM_W, "=SUM(B32:B33)")):
        put(r, [label, w] + [f"={Q}!{c}{src}" for c in "CDE"])
    put(35, ["Descuento del precio frente al ponderado", ""] + [f"={Q}!{c}{SUM_DISC}" for c in "CDE"])
    put(36, ["Compra con MOS", ""] + [f"={Q}!{c}{SUM_MOS}" for c in "CDE"])
    put(37, ["Chequeo: múltiplos VP 3 años < FY+3", ""] + [f"={Q}!{c}{CHK_OK}" for c in "CDE"])
    put(39, ["CADA MÉTODO A VALOR HOY"])
    put(40, ["Método", "Peso", "Conservador", "Base", "Optimista"])
    put(41, ["DCF Damodaran", f"=B{d}"] + [f"={Q}!{c}{SUM_DCF}" for c in "CDE"])
    for i, res_row in enumerate(lay.res_rows):
        put(42 + i, [f"=A{res_row}", f"=B{res_row}"] + [f"={Q}!J{FIRST_ROW[n] + i}" for n, *_ in SCENARIOS])
    put(47, [f'={Q}!B6&" · Ke "&TEXT({Q}!B5;"0,00%")'])
    return _localize(rows, lay.sep)


def _format_sheet(ws) -> list[dict]:
    q = Req(ws.id)
    # la hoja anterior (puente a 3 años) dejaba formato en J:L y altos de fila propios
    q.items.append({"updateCells": {"range": {"sheetId": ws.id}, "fields": "userEnteredFormat"}})
    q.height(1, ws.row_count, 21)
    q.fmt(1, NOTE_ROW + 3, 1, NCOL, textFormat=_txt(10), backgroundColor=WHITE, verticalAlignment="MIDDLE")
    q.fmt(1, 1, 1, NCOL, textFormat=_txt(13, bold=True, color=NAVY))
    for r in (2, NOTE_ROW, NOTE_ROW + 1):
        q.merge(r, r, 1, NCOL)
        q.fmt(r, r, 1, NCOL, wrapStrategy="WRAP", textFormat=_txt(9, italic=True, color=MUTED))
        q.height(r, r, 48)
    q.fmt(4, 4, 1, 4, backgroundColor=HEAD_BG, textFormat=_txt(10, bold=True))
    q.borders(4, 7, 1, 4)
    q.fmt(5, 5, 2, 4, numberFormat={"type": "NUMBER", "pattern": "0.00%"}, horizontalAlignment="RIGHT")
    q.fmt(7, 7, 2, 4, numberFormat={"type": "NUMBER", "pattern": "0.0000"}, horizontalAlignment="RIGHT")
    q.fmt(5, 6, 3, 3, backgroundColor={"red": 1, "green": 0.95, "blue": 0.7})
    q.items.append({"setDataValidation": {"range": q.grid(6, 6, 3, 3), "rule": {
        "condition": {"type": "ONE_OF_LIST", "values": [{"userEnteredValue": DEFAULT_CRIT}, {"userEnteredValue": ONLY3}]},
        "strict": True, "showCustomUi": True}}})
    for name, *_ in SCENARIOS:
        first = FIRST_ROW[name]
        last = first + len(METHODS)
        q.fmt(first - 2, first - 2, 1, NCOL, textFormat=_txt(11, bold=True, color=NAVY))
        q.fmt(first - 1, first - 1, 1, NCOL, backgroundColor=HEAD_BG, textFormat=_txt(10, bold=True),
              wrapStrategy="WRAP", horizontalAlignment="CENTER")
        q.height(first - 1, first - 1, 36)
        q.fmt(first, last, 2, 3, numberFormat={"type": "NUMBER", "pattern": PCT}, horizontalAlignment="RIGHT")
        q.fmt(first, last, 4, 10, numberFormat={"type": "NUMBER", "pattern": NUM}, horizontalAlignment="RIGHT")
        q.fmt(first, last, 11, 11, horizontalAlignment="CENTER")
        q.fmt(first, last, 7, 10, backgroundColor=ZEBRA)
        q.fmt(last, last, 1, NCOL, textFormat=_txt(10, bold=True), backgroundColor=GREEN_BG)
        q.borders(first - 1, last, 1, NCOL)
    for title, hdr, last in ((SUM_TITLE, SUM_HDR, SUM_MOS), (CHK_TITLE, CHK_HDR, CHK_OK)):
        q.fmt(title, title, 1, NCOL, textFormat=_txt(11, bold=True, color=NAVY))
        q.fmt(hdr, hdr, 1, 5, backgroundColor=HEAD_BG, textFormat=_txt(10, bold=True), horizontalAlignment="CENTER")
        q.fmt(hdr + 1, last, 3, 5, numberFormat={"type": "NUMBER", "pattern": NUM}, horizontalAlignment="RIGHT")
        q.borders(hdr, last, 1, 5)
    q.fmt(SUM_DCF, SUM_W, 2, 2, numberFormat={"type": "NUMBER", "pattern": PCT}, horizontalAlignment="RIGHT")
    q.fmt(SUM_PRICE, SUM_PRICE, 2, 2, numberFormat={"type": "NUMBER", "pattern": NUM}, horizontalAlignment="RIGHT")
    q.fmt(SUM_MOS, SUM_MOS, 2, 2, numberFormat={"type": "NUMBER", "pattern": PCT}, horizontalAlignment="RIGHT")
    q.fmt(SUM_DISC, SUM_DISC, 3, 5, numberFormat={"type": "NUMBER", "pattern": PCT})
    q.fmt(SUM_W, SUM_W, 1, 5, textFormat=_txt(10, bold=True), backgroundColor=GREEN_BG)
    q.fmt(CHK_OK, CHK_OK, 3, 5, horizontalAlignment="CENTER", textFormat=_txt(10, bold=True))
    q.width(1, 1, 340)
    q.width(2, NCOL, 112)
    q.sheet_props(frozen_rows=0, hide_grid=True, tab=NAVY)
    return q.items


def _format_resumen(ws) -> list[dict]:
    q = Req(ws.id)
    q.items.append({"unmergeCells": {"range": q.grid(29, RES_LAST, 1, 8)}})
    q.fmt(29, RES_LAST, 1, 5, textFormat=_txt(10), backgroundColor=WHITE)
    q.merge(28, 28, 1, 5)
    q.fmt(28, 28, 1, 5, wrapStrategy="WRAP", textFormat=_txt(9, italic=True, color=MUTED))
    q.height(28, 28, 48)
    for title, hdr, last in ((30, 31, 37), (39, 40, 46)):
        q.fmt(title, title, 1, 5, textFormat=_txt(11, bold=True, color=NAVY))
        q.fmt(hdr, hdr, 1, 5, backgroundColor=HEAD_BG, textFormat=_txt(10, bold=True), horizontalAlignment="CENTER")
        q.fmt(hdr + 1, last, 2, 2, numberFormat={"type": "NUMBER", "pattern": PCT}, horizontalAlignment="RIGHT")
        q.fmt(hdr + 1, last, 3, 5, numberFormat={"type": "NUMBER", "pattern": NUM}, horizontalAlignment="RIGHT")
        q.borders(hdr, last, 1, 5)
    q.fmt(34, 34, 1, 5, textFormat=_txt(10, bold=True), backgroundColor=GREEN_BG)
    q.fmt(35, 35, 3, 5, numberFormat={"type": "NUMBER", "pattern": PCT})
    q.fmt(37, 37, 3, 5, horizontalAlignment="CENTER")
    q.fmt(47, 47, 1, 5, textFormat=_txt(9, italic=True, color=MUTED))
    return q.items


def _move_charts(sh, res_id: int) -> list[dict]:
    """El grafico flotante del Resumen esta anclado en A30 y tapa el bloque de valor hoy: pasa a G30."""
    md = sh.fetch_sheet_metadata({"fields": "sheets(properties.sheetId,charts(chartId,position))"})
    out = []
    for s in md["sheets"]:
        if s["properties"]["sheetId"] != res_id:
            continue
        for ch in s.get("charts", []):
            pos = ch.get("position", {}).get("overlayPosition")
            if not pos:
                continue
            anchor = pos["anchorCell"]
            if RES_FIRST - 2 <= anchor.get("rowIndex", 0) <= RES_LAST and anchor.get("columnIndex", 0) < 5:
                out.append({"updateEmbeddedObjectPosition": {
                    "objectId": ch["chartId"], "fields": "anchorCell,offsetXPixels,offsetYPixels",
                    "newPosition": {"overlayPosition": {**pos, "anchorCell": {"sheetId": res_id, "rowIndex": 29, "columnIndex": 6},
                                                        "offsetXPixels": 12, "offsetYPixels": 0}}}})
    return out


def _known_resumen_block(block: list[list[str]]) -> bool:
    """True si A29:H50 esta vacio o tiene el bloque de valor hoy (anterior o este)."""
    flat = {(RES_FIRST + 1 + i, j): str(v).strip() for i, row in enumerate(block) for j, v in enumerate(row) if str(v).strip()}
    if not flat:
        return True
    a30 = flat.get((30, 0), "")
    return a30.startswith("VALOR POR ACCIÓN HOY") and all(r <= RES_LAST for r, _ in flat)


def apply(client, sheet_id: str, *, dry_run: bool) -> dict:
    sh = _open(client, sheet_id)
    titles = {ws.title for ws in sh.worksheets()}
    lay, why = detect_layout(sh)
    if lay is None:
        return {"estado": "omitida", "motivo": why}
    got = sh.values_batch_get([f"{R}!A29:H{RES_LAST}", f"{R}!A28:E{RES_LAST}"], params={"valueRenderOption": "FORMULA"})
    block = got["valueRanges"][0].get("values", [])
    if not _known_resumen_block(block):
        return {"estado": "personalizada", "motivo": "Resumen A29:H50 tiene contenido propio"}

    backup = {"resumen_A28_E50": got["valueRanges"][1].get("values", [])}
    if SHEET in titles:
        backup["descuento"] = sh.worksheet(SHEET).get_all_values(value_render_option="FORMULA")
    if dry_run:
        return {"estado": "dry-run", "hoja_existia": SHEET in titles, "layout": lay.__dict__}

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    backup_path = BACKUP_DIR / f"{sheet_id}.json"
    if not backup_path.exists():  # una segunda corrida no pisa el respaldo de la version original
        backup_path.write_text(json.dumps(backup, ensure_ascii=False, indent=1))

    if SHEET in titles:
        ws = sh.worksheet(SHEET)
        ws.clear()
        sh.batch_update({"requests": [{"unmergeCells": {"range": {"sheetId": ws.id}}},
                                      {"setDataValidation": {"range": {"sheetId": ws.id}}}]})
    else:
        res_index = sh.worksheet(RES).index
        ws = sh.add_worksheet(SHEET, rows=80, cols=NCOL + 2, index=res_index + 1)
    if ws.col_count < NCOL:
        ws.add_cols(NCOL - ws.col_count)
    values = sheet_values(lay)
    ws.update(values=values, range_name=f"A1:K{len(values)}", value_input_option="USER_ENTERED")
    res = sh.worksheet(RES)
    res.batch_clear([f"A29:H{RES_LAST}"])
    sh.batch_update({"requests": _format_sheet(ws) + _format_resumen(res) + _move_charts(sh, res.id)})
    res.update(values=resumen_values(lay), range_name=f"A{RES_FIRST}:E{RES_LAST}", value_input_option="USER_ENTERED")
    time.sleep(2)
    return {"estado": "aplicada", **check(sh, lay)}


def check(sh, lay: Layout | None = None) -> dict:
    """Lee los resultados y verifica VP3 < FY+3 y que las columnas FY+3 coincidan con el Resumen."""
    lay = lay or detect_layout(sh)[0] or DEFAULT
    vr = sh.values_batch_get([f"{Q}!A11:K34", f"{Q}!C{SUM_DCF}:E{CHK_OK}", f"{R}!C{lay.res_rows[0]}:E{lay.res_rows[-1]}"],
                             params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
    grid = vr[0].get("values", [])
    summ = vr[1].get("values", [])
    res = vr[2].get("values", [])
    out: dict = {"escenarios": {}, "alertas": []}
    for k, (name, *_rest) in enumerate(SCENARIOS):
        first = FIRST_ROW[name] - 11
        rows = grid[first:first + len(METHODS) + 1]
        per = {}
        for i, row in enumerate(rows):
            row = row + [""] * (NCOL - len(row))
            label = row[0] if i < len(METHODS) else "Múltiplos consolidados"
            per[label] = {"fy": row[3:6], "vp": row[6:9], "consolidado": row[9], "chequeo": row[10]}
            if row[10] == "REVISAR":
                out["alertas"].append(f"{name} {label}: VP3 {row[8]} no es menor que FY+3 {row[5]}")
            if i < len(METHODS) and i < len(res) and isinstance(row[5], (int, float)) and isinstance(res[i][k], (int, float)) \
                    and abs(row[5] - res[i][k]) > 1e-6 * max(1, abs(row[5])):
                out["alertas"].append(f"{name} {label}: FY+3 de la hoja {row[5]} != Resumen {res[i][k]}")
        col = lambda r: (summ[r][k] if r < len(summ) and k < len(summ[r]) else "")  # noqa: E731
        out["escenarios"][name] = {"metodos": per, "dcf_hoy": col(0), "multiplos_hoy": col(1),
                                   "ponderado_hoy": col(2), "multiplos_fy3_nominal": col(CHK_NOM - SUM_DCF),
                                   "multiplos_vp3": col(CHK_PV - SUM_DCF), "chequeo": col(CHK_OK - SUM_DCF)}
    return out


def _open(client, sid: str, tries: int = 5):
    """open_by_key con reintentos ante errores 429/5xx transitorios de la API."""
    for i in range(tries):
        try:
            return client.open_by_key(sid)
        except APIError as exc:
            code = getattr(getattr(exc, "response", None), "status_code", 0)
            if (code != 429 and code < 500) or i == tries - 1:
                raise
            time.sleep(20 * (i + 1))


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--sheet-id", action="append")
    g.add_argument("--targets-json", help="JSON con [[id, nombre], ...]")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check-only", action="store_true", help="Solo lee y verifica, no escribe")
    ap.add_argument("--report", default=str(_ROOT / "reference" / "descuento_multiples_2026-09-29_informe.json"))
    args = ap.parse_args(argv)

    targets = [(s, s) for s in args.sheet_id] if args.sheet_id else [tuple(t[:2]) for t in json.loads(Path(args.targets_json).read_text())]
    client = get_gspread_client()
    report = json.loads(Path(args.report).read_text()) if Path(args.report).exists() else {}
    for sid, name in targets:
        try:
            _open(client, sid)
        except (SpreadsheetNotFound, PermissionError):
            print(f"{name[:55]:55s} no encontrada (borrada o sin acceso)")
            continue
        if args.check_only:
            rep = {"estado": "verificada", **check(_open(client, sid))}
        else:
            rep = _retry(lambda: apply(client, sid, dry_run=args.dry_run))
        base = rep.get("escenarios", {}).get("Base", {})
        print(f"{name[:55]:55s} {rep['estado']:13s} {rep.get('motivo', '')}"
              + (f" DCF={base.get('dcf_hoy')!s:.8} Mult={base.get('multiplos_hoy')!s:.8} "
                 f"Pond={base.get('ponderado_hoy')!s:.8} chequeo={base.get('chequeo')}" if base else ""))
        for a in rep.get("alertas", []):
            print("    !", a)
        if not args.dry_run:
            report[sid] = {"nombre": name, **rep}
            Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=1, default=str))
        time.sleep(3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
