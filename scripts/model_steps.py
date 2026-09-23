"""Pasos genericos del proceso de valoracion sobre la plantilla maestra
(los mismos para cualquier ticker). Los scripts por empresa (run_nke.py,
...) aportan solo los datos y decisiones propias de cada valoracion.

Extraido de run_pypl.py (que se deja tal cual como registro de la corrida
de PayPal)."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import refresh_native_model as rnm

from jmr_valuation.io import sec_edgar_loader
from jmr_valuation.io.sec_xbrl_instance import AugmentedSecEdgarClient
from jmr_valuation.io.sheets_auth import get_gspread_client, open_target_sheet

ROOT = Path(__file__).resolve().parent.parent


def open_sheet(sheet_id: str):
    return open_target_sheet(get_gspread_client(), sheet_id)


def serial(d: date) -> int:
    return (d - date(1899, 12, 30)).days


def iferror(formula: str, fallback: str = '""') -> str:
    return f"=IFERROR({formula[1:]};{fallback})"


def install_augmented_client(ticker: str, custom_tag_map: dict[str, str] | None = None) -> None:
    client = AugmentedSecEdgarClient(custom_tag_map=custom_tag_map, tickers=(ticker,))
    sec_edgar_loader.SecEdgarClient = lambda *a, **k: client  # type: ignore[assignment]


def write_with_backup(sh, sheet: str, updates: dict[str, object], reason: str, backup_path: Path) -> None:
    """Escribe celdas guardando ANTES la formula/valor anterior en
    `backup_path` (reversible). Si la celda ya estaba respaldada de una
    corrida anterior, se conserva el 'before' ORIGINAL."""
    if not updates:
        return
    ws = sh.worksheet(sheet)
    cells = list(updates)
    before = ws.batch_get(cells, value_render_option="FORMULA")
    backup = json.loads(backup_path.read_text()) if backup_path.exists() else {}
    for cell, prev in zip(cells, before):
        key = f"{sheet}!{cell}"
        old = prev[0][0] if prev and prev[0] else ""
        if key not in backup:
            backup[key] = {"before": old, "after": updates[cell], "reason": reason}
        else:
            backup[key].update(after=updates[cell], reason=reason)
    backup_path.parent.mkdir(parents=True, exist_ok=True)
    backup_path.write_text(json.dumps(backup, ensure_ascii=False, indent=1))
    rnm._apply(ws, [(c, [[v]]) for c, v in updates.items()])


def fix_template_bugs(sh, backup_path: Path) -> None:
    """Bugs estructurales de la plantilla maestra que no dependen de la
    empresa (ver log de la Tesis de PYPL): TICKER vacio (#6), tasa efectiva
    fija en la columna de 2023, activos no operativos que suman 'Other
    Long-Term Assets' (operativos), IFERROR en Option value (#5), beta
    'Direct Input' en B24 y tabla multibusiness vacia, crecimiento de
    dividendo sin año base."""
    write_with_backup(sh, "Input sheet", {
        "B1": "=A1",
        "B24": "='Income Statement'!L29",
    }, "Bugs de la plantilla (TICKER vacio; tasa efectiva fija en Dec '23)", backup_path)

    ov = sh.worksheet("Option value")
    cells = ["B18", "B23", "B24", "B26", "B27", "B29", "B30"]
    current = ov.batch_get(cells, value_render_option="FORMULA")
    write_with_backup(sh, "Option value", {
        c: iferror(v[0][0], "0") for c, v in zip(cells, current) if not v[0][0].startswith("=IFERROR")
    }, "Bug #5: IFERROR en la cadena de Option value", backup_path)

    coc = sh.worksheet("Cost of capital worksheet")
    k65, l65 = (coc.acell(c, value_render_option="FORMULA").value for c in ("K65", "L65"))
    write_with_backup(sh, "Cost of capital worksheet", {
        "B24": ('=IF(B22="Direct Input";B23/(1+(1-B39)*(C61/B61));'
                "IF(B22=\"Single Business(US)\";VLOOKUP('Input sheet'!B9;'Industry Averages(US)'!A3:G96;7);"
                "IF(B22=\"Multibusiness(US)\";K49;IF(B22=\"Single Business(Global)\";"
                "VLOOKUP('Input sheet'!B10;'Industry Averages (Global)'!A3:G96;7);"
                "'Cost of capital worksheet'!K65))))"),
        **({"K65": iferror(k65)} if not k65.startswith("=IFERROR") else {}),
        **({"L65": iferror(l65)} if not l65.startswith("=IFERROR") else {}),
    }, "B24 con Direct Input; tabla multibusiness vacia", backup_path)

    fm = sh.worksheet("Financials Multiples")
    cells = [f"{c}{r}" for r in (36, 75, 115) for c in "BCDE"]
    current = fm.batch_get(cells, value_render_option="FORMULA")
    write_with_backup(sh, "Financials Multiples", {
        c: iferror(v[0][0]) for c, v in zip(cells, current) if v and v[0] and not v[0][0].startswith("=IFERROR")
    }, "Crecimiento de dividendo sin año base", backup_path)


def _nwc_level(col: str) -> str:
    bs = "'Balance Sheet'!"
    return (f"(({bs}${col}$10-{bs}${col}$5)-({bs}${col}$24-{bs}${col}$20-{bs}${col}$21))"
            f"/'Income Statement'!${col}$3")


def fix_nwc_projection(sh, backup_path: Path) -> None:
    """Bug de la plantilla en 'Financials Multiples' (Cambio en NWC
    proyectado, filas 22/61/101): usaba PROMEDIO(ΔNWC/ΔIngresos) de 3 años.
    Con un año de ingresos casi planos (NKE FY26: +US$89M) el ratio da 21x y
    el NWC proyectado explota (+US$11.000M/año), dando FCFF/FCFE/OCF
    negativos y precios objetivo absurdos. Ademas los bloques Base y
    Optimista apuntaban a 'Income Statement'!H42/H82 (celdas vacias) en vez
    de H3. Nuevo: intensidad de NWC promedio de los ultimos 3 cierres
    (NWC / Ingresos) x ΔIngresos proyectado -- estable ante años planos."""
    fm = sh.worksheet("Financials Multiples")
    intensity = "(" + "+".join(_nwc_level(c) for c in "IJK") + ")/3"
    updates = {}
    for nwc_row, rev_row in ((22, 4), (61, 43), (101, 83)):
        existing = fm.get(f"E{nwc_row}:H{nwc_row}", value_render_option="FORMULA")
        cols = [c for c, val in zip("EFGH", (existing[0] if existing else [])) if str(val).startswith("=")]
        prev = {"E": "D", "F": "E", "G": "F", "H": "G"}
        for c in cols:
            updates[f"{c}{nwc_row}"] = f"={intensity}*({c}{rev_row}-{prev[c]}{rev_row})"
    write_with_backup(sh, "Financials Multiples", updates,
                      "Bug: NWC proyectado con ΔNWC/ΔIngresos (explota con ingresos planos) y referencias a H42/H82 vacias",
                      backup_path)


def write_tesis(sh, rows: list[list], backup_path: Path, *, text_rows: range, merges: list[str],
                bold_rows: tuple[int, ...], head_rows: tuple[int, ...], formats: list[dict]) -> None:
    """Reemplaza la pestaña 'Tesis de Inversión y Supuestos' (plantilla de
    placeholders) con `rows`. `text_rows` (indices 0-based) se escriben como
    texto literal aunque empiecen con '=' o '#' (log de correcciones)."""
    ws = sh.worksheet("Tesis de Inversión y Supuestos")
    old = ws.get("A1:H120", value_render_option="FORMULA")
    backup = json.loads(backup_path.read_text()) if backup_path.exists() else {}
    backup.setdefault("Tesis de Inversión y Supuestos!A1:H120", {"before": old, "reason": "Plantilla de placeholders reemplazada"})
    backup_path.write_text(json.dumps(backup, ensure_ascii=False, indent=1))
    ws.batch_clear(["A1:H120"])
    rows = [r + [""] * (5 - len(r)) for r in rows]
    for i in text_rows:
        rows[i] = ["'" + x if isinstance(x, str) and x[:1] in ("=", "#", "+", "-") else x for x in rows[i]]
    ws.update(values=rows, range_name="A1", value_input_option="USER_ENTERED")

    bold = {"textFormat": {"bold": True}}
    head = {"textFormat": {"bold": True}, "backgroundColor": {"red": 0.87, "green": 0.92, "blue": 0.97}}
    n = len(rows)
    ws.batch_format([
        {"range": f"A1:E{n}", "format": {"wrapStrategy": "WRAP", "verticalAlignment": "TOP",
                                           "textFormat": {"bold": False}, "backgroundColor": {"red": 1, "green": 1, "blue": 1}}},
        {"range": "A1", "format": {"textFormat": {"bold": True, "fontSize": 13}}},
        *[{"range": f"A{r}", "format": bold} for r in bold_rows],
        *[{"range": f"A{r}:E{r}", "format": head} for r in head_rows],
        *formats,
    ])
    sid = ws.id

    def width(start, end, px):
        return {"updateDimensionProperties": {"range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": start,
                                                        "endIndex": end}, "properties": {"pixelSize": px}, "fields": "pixelSize"}}
    sh.batch_update({"requests": [
        {"unmergeCells": {"range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": 120, "startColumnIndex": 0, "endColumnIndex": 8}}},
        width(0, 1, 260), width(1, 4, 150), width(4, 5, 520),
    ]})
    for m in merges:
        ws.merge_cells(m)
