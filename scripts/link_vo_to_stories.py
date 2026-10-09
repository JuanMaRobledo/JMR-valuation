#!/usr/bin/env python
"""Los cuatro DCF de las historias con la estructura de Damodaran (2-oct-2026).

'Valuation output' ya tiene tres bloques Damodaran (Base 2-42, Conservador 53-93, Optimista 104-144). Este script:
1. Crea el bloque «Modelo Disrupción» (157-197) con las mismas fórmulas del bloque Optimista (las referencias internas
   se trasladan; las externas no cambian).
2. Enlaza los supuestos de cada bloque a su historia de 'Escenarios e historias': crecimiento de los años 1-10 y
   terminal (fila de crecimiento de la historia, que suma los segmentos), margen objetivo (C45:C48), ventas/capital
   y ROIC terminal. Lo común (ventas LTM, margen inicial, convergencia, impuestos, costo de capital, deuda, caja,
   opciones, acciones) sigue saliendo de la 'Input sheet'.
3. En la pestaña de historias, ventas/capital por defecto se toma de la 'Input sheet' (no de 'Valuation output'),
   para no crear referencias circulares.
Con --check compara el valor por acción de cada bloque con el de la pestaña de historias (H5:H8).

Uso: PYTHONPATH=.:scripts python scripts/link_vo_to_stories.py --sheet-id ID [--apply] [--check]
"""
from __future__ import annotations

import argparse
import json
import re
import time

from jmr_valuation.io.sheets_auth import get_gspread_client

VO, EH, IS = "Valuation output", "'Escenarios e historias'", "'Input sheet'"
OPT0, OPT1, DIS_OFF = 104, 144, 53           # bloque Optimista y desplazamiento al de Disrupción (157-197)
# bloque de VO -> (fila de resumen en la pestaña de historias, fila de crecimiento de la historia, filas del bloque)
BLOCKS = {
    "Base":        {"i": 5, "g": 29,  "growth": 4,   "s2c": 40,  "roic": 42,  "target": "C46", "ps": "B35"},
    "Conservador": {"i": 6, "g": 53,  "growth": 55,  "s2c": 91,  "roic": 93,  "target": "C45", "ps": "B86"},
    "Optimista":   {"i": 8, "g": 101, "growth": 106, "s2c": 142, "roic": 144, "target": "C47", "ps": "B137"},
    "Disrupción":  {"i": 7, "g": 77,  "growth": 159, "s2c": 195, "roic": 197, "target": "C48", "ps": "B190"},
}
COLS = "CDEFGHIJKL"   # años 1..10; M = terminal
REF = re.compile(r"(?<![A-Za-z!'$\d])(\$?)([A-Z]{1,2})(\$?)(\d+)(?![\d(])")


def shift_block(f: str) -> str:
    """Traslada al bloque de Disrupción las referencias propias de 'Valuation output' dentro del bloque Optimista."""
    if not (isinstance(f, str) and f.startswith("=")):
        return f
    f = f.replace("'Valuation output'!", "")  # referencia a la propia hoja con prefijo: equivale a sin prefijo
    parts = f.split('"')
    for k in range(0, len(parts), 2):
        seg = parts[k]
        out, pos = [], 0
        for m in REF.finditer(seg):
            # referencias con prefijo de otra hoja ('Input sheet'!B27) no se tocan
            pre = seg[max(0, m.start() - 1):m.start()]
            if pre == "!":
                continue
            row = int(m.group(4))
            if OPT0 <= row <= OPT1:
                row += DIS_OFF
            elif m.group(2) == "C" and row == 47 and m.group(3) == "$":
                row = 48  # margen objetivo de la Optimista -> Disrupción
            out.append(seg[pos:m.start()] + f"{m.group(1)}{m.group(2)}{m.group(3)}{row}")
            pos = m.end()
        out.append(seg[pos:])
        parts[k] = "".join(out)
    return '"'.join(parts)


def plan(sh) -> list[dict]:
    q = f"'{VO}'"
    src = sh.values_get(f"{q}!A{OPT0}:N{OPT1}", params={"valueRenderOption": "FORMULA"}).get("values", [])
    data = []
    for k, row in enumerate(src):
        r = OPT0 + DIS_OFF + k
        vals = [shift_block(v) for v in row] + [""] * (14 - len(row))
        data.append({"range": f"{q}!A{r}:N{r}", "values": [vals]})
    data.append({"range": f"{q}!A157", "values": [["Modelo Disrupción"]]})
    data.append({"range": f"{q}!B157", "values": [["Disrupción"]]})
    data.append({"range": f"{q}!A48:B48", "values": [["Disrupción", "=$C$159"]]})
    for name, b in BLOCKS.items():
        i = b["i"]
        # La Base conserva el crecimiento terminal de la maestra (M4, tasa libre de riesgo de la 'Input sheet'):
        # la pestaña de historias lo lee de ahí, y enlazarlo al revés sería circular.
        cols = COLS if name == "Base" else COLS + "M"
        data.append({"range": f"{q}!C{b['growth']}:{cols[-1]}{b['growth']}",
                     "values": [[f"={EH}!{c}{b['g']}" for c in cols]]})
        data.append({"range": f"{q}!{b['target']}", "values": [[f"={EH}!$D${i}"]]})
        data.append({"range": f"{q}!C{b['s2c']}:L{b['s2c']}",
                     "values": [[f"={EH}!$E${i}"] * 5 + [
                         f'=IF({IS}!$B$78="Yes";1/((1-({y}-5)/5)/{EH}!$F${i}+({y}-5)/5*{COLS[y-1]}{b["growth"]+2}*(1-{COLS[y-1]}{b["growth"]+4})/$M${b["roic"]});{EH}!$F${i})'
                         for y in range(6, 11)]]})
        data.append({"range": f"{q}!M{b['roic']}", "values": [[f"={EH}!$G${i}"]]})
    for name in ("Base", "Conservador", "Optimista"):
        r = {"Base": 2, "Conservador": 53, "Optimista": 104}[name]
        data.append({"range": f"{q}!A{r}", "values": [[f"Modelo {name} · historia {'Conservadora' if name == 'Conservador' else name}"]]})
    data.append({"range": f"{q}!A157", "values": [["Modelo Disrupción · historia Disrupción"]]})
    return data


def eh_s2c_fix(sh) -> list[dict]:
    """Ventas/capital de la pestaña de historias: de la 'Input sheet' (no de 'Valuation output')."""
    cur = sh.values_get(f"{EH}!E5:F8", params={"valueRenderOption": "FORMULA"}).get("values", [])
    out = []
    for k, row in enumerate(cur):
        r = 5 + k
        e = row[0] if row else ""
        f = row[1] if len(row) > 1 else ""
        if isinstance(e, str) and "Valuation output" in e:
            out.append({"range": f"{EH}!E{r}", "values": [[f"={IS}!$B$32"]]})
        if isinstance(f, str) and "Valuation output" in f:
            out.append({"range": f"{EH}!F{r}", "values": [[f"={IS}!$B$33"]]})
    return out


def check(sh) -> dict:
    q = f"'{VO}'"
    vr = sh.values_batch_get([f"{q}!{b['ps']}" for b in BLOCKS.values()] + [f"{EH}!H5:H8"],
                             params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
    eh = [r[0] if r else None for r in vr[-1].get("values", [])]
    out = {}
    for (name, b), v in zip(BLOCKS.items(), vr[:-1]):
        x = (v.get("values") or [[None]])[0][0]
        y = eh[b["i"] - 5] if len(eh) > b["i"] - 5 else None
        # el motor pone piso 0 al valor por acción (responsabilidad limitada); 'Valuation output' puede mostrar un negativo
        out[name] = {"valuation_output": x, "historias": y,
                     "dif": (max(0.0, x) - y) if isinstance(x, (int, float)) and isinstance(y, (int, float)) else None}
    return out


def format_block(sh) -> None:
    ws = sh.worksheet(VO)
    sh.batch_update({"requests": [{"copyPaste": {
        "source": {"sheetId": ws.id, "startRowIndex": OPT0 - 1, "endRowIndex": OPT1, "startColumnIndex": 0, "endColumnIndex": 14},
        "destination": {"sheetId": ws.id, "startRowIndex": OPT0 - 1 + DIS_OFF, "endRowIndex": OPT1 + DIS_OFF,
                        "startColumnIndex": 0, "endColumnIndex": 14},
        "pasteType": "PASTE_FORMAT"}}]})


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sheet-id", required=True)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--fase2", action="store_true", help="Historias y múltiplos leen de 'Valuation output'")
    a = ap.parse_args()
    sh = get_gspread_client().open_by_key(a.sheet_id)
    if a.apply:
        before = sh.values_get(f"'{VO}'!A1:N200", params={"valueRenderOption": "FORMULA"}).get("values", [])
        json.dump(before, open(f"reference/backups/vo_antes_historias_{a.sheet_id}.json", "w"), ensure_ascii=False)
        data = eh_s2c_fix(sh) + plan(sh)
        sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": data})
        format_block(sh)
        time.sleep(4)
    if a.fase2:
        apply_phase2(sh)
        time.sleep(4)
    if a.check or a.apply:
        print(json.dumps(check(sh), indent=1))
    return 0



# ---------------------------------------------------------------- fase 2
# 'Financials Multiples': cada escenario toma de su bloque Damodaran (ventas, crecimiento, margen, impuesto, reinversión)
FM_FROM_VO = {4: {"rev": 56, "g": 55, "m": 57, "ebit": 58, "t": 59, "nopat": 60, "reinv": 61},     # Conservador
              43: {"rev": 5, "g": 4, "m": 6, "ebit": 7, "t": 8, "nopat": 9, "reinv": 10},           # Base
              83: {"rev": 107, "g": 106, "m": 108, "ebit": 109, "t": 110, "nopat": 111, "reinv": 112}}  # Optimista
STARTS = {"A": 22, "B": 46, "C": 70, "D": 94}   # bloques de la pestaña de historias
PS = {"A": "B35", "B": "B86", "C": "B190", "D": "B137"}


def fm_links() -> list[dict]:
    q, v = "'Financials Multiples'", f"'{VO}'"
    data = []
    for r_rev, s in FM_FROM_VO.items():
        for i, col in enumerate("EFGH"):
            c = "CDEF"[i]
            data += [
                {"range": f"{q}!{col}{r_rev}", "values": [[f"={v}!{c}{s['rev']}"]]},
                {"range": f"{q}!{col}{r_rev + 1}", "values": [[f"={v}!{c}{s['g']}"]]},
                {"range": f"{q}!{col}{r_rev + 4}", "values": [[f"={v}!{c}{s['m']}"]]},
                {"range": f"{q}!{col}{r_rev + 10}", "values": [[f"=IFERROR(1-{v}!{c}{s['nopat']}/{v}!{c}{s['ebit']};{v}!{c}{s['t']})"]]},
                {"range": f"{q}!{col}{r_rev + 18}", "values": [[f"={col}{r_rev + 16}+{col}{r_rev + 17}+{v}!{c}{s['reinv']}"]]},
            ]
    return data


def eh_phase2() -> tuple[list[dict], list[str]]:
    """Resumen H5:H8 desde 'Valuation output'; se borran las filas de DCF de cada bloque (se conservan segmentos,
    ingresos totales y crecimiento, que alimentan 'Valuation output')."""
    data, clear = [], []
    for hid, r0 in STARTS.items():
        i = 5 + "ABCD".index(hid)
        data.append({"range": f"{EH}!H{i}", "values": [[f"=MAX(0;'{VO}'!{PS[hid]})"]]})
        clear.append(f"{EH}!A{r0 + 8}:M{r0 + 22}")
    data.append({"range": f"{EH}!A19", "values": [[
        "Cada historia se calcula en 'Valuation output' con la estructura de Damodaran (Base 2-42, Conservador 53-93, "
        "Optimista 104-144, Disrupción 157-197); esta pestaña guarda los supuestos de cada historia (crecimiento por segmento, "
        "margen objetivo, ventas/capital, ROIC y crecimiento terminal, probabilidad) y la suma de los segmentos."]]})
    return data, clear


def apply_phase2(sh) -> None:
    data, clear = eh_phase2()
    sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": fm_links() + data})
    sh.values_batch_clear(body={"ranges": clear})


if __name__ == "__main__":
    raise SystemExit(main())
