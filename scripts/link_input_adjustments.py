#!/usr/bin/env python
"""Convierte números escritos en la Input sheet en enlace al estado financiero + ajuste explícito (2-oct-2026).

El valor no cambia: ajuste = valor escrito − valor del estado. Cada celda lleva una nota con el motivo. Respaldo en
reference/backups/enlaces_input_2026-10-02.json.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

from jmr_valuation.io.sheets_auth import get_gspread_client

_ROOT = Path(__file__).resolve().parent.parent
BS, IS = "'Balance Sheet'", "'Income Statement'"
# ticker -> [(celda, enlace, motivo)]
CELLS = {
    "CMG": [
        ("B15", f"{BS}!L35", "Patrimonio al 30-jun-2026 (10-Q 2T26). La columna LTM del balance trae dic-2025; bajó por recompras de US$1.355M en el semestre."),
        ("B16", f"{BS}!L20+{BS}!L25", "Sin deuda financiera; los arrendamientos entran por el conversor (B18)."),
        ("B19", f"{BS}!L5", "Efectivo US$228,2M + inversiones de corto plazo US$449,7M al 30-jun-2026 (10-Q 2T26)."),
        ("B20", f"{BS}!L14", "Inversiones de largo plazo al 30-jun-2026 (10-Q 2T26): US$97,1M; el balance trae US$197,1M de dic-2025."),
    ],
    "CELH": [("B16", f"{BS}!L20+{BS}!L25", "Préstamo a plazo a valor nominal US$694,75M (10-Q 2T26); el balance lo trae neto de costos de emisión. Arrendamientos por el conversor (B18).")],
    "SHAK": [
        ("B16", f"{BS}!L20+{BS}!L25", "Valor registrado antes (US$248M) frente al saldo contable de US$247,7M: diferencia de redondeo."),
        ("B22", f"{IS}!L27", "Acciones totalmente canjeadas: 40,41M clase A + 2,39M clase B (LLC Interests) al 29-jul-2026 (10-Q)."),
    ],
    "ADBE": [("B22", f"{IS}!L27", "Acciones del estado de resultados (sin ajuste).")],
}
SHEETS = {"CMG": "1VUVN1cCm3Hj8bLrmsCZFYBCDIq3DncxHGHH_jbW8ZtU", "CELH": "1tHDLsh4yBF9NQkRLNqfTU6GPM5trOWsB5xIjpALLOIw",
          "SHAK": "1RcwUptYoVjCfHvdqED5wXCsjteCds61g4HMKA_T8GCM", "ADBE": "19WcSOKymo4gR6lnKiLB1gAitYFFwfI3xl08E4BDzLDw"}


def num(x: float) -> str:
    return f"{x:.6f}".rstrip("0").rstrip(".").replace(".", ",")


def main() -> int:
    c = get_gspread_client()
    backup, report = {}, {}
    for tk, items in CELLS.items():
        sh = c.open_by_key(SHEETS[tk])
        ws = sh.worksheet("Input sheet")
        U = {"valueRenderOption": "UNFORMATTED_VALUE"}
        cur = sh.values_batch_get([f"'Input sheet'!{a}" for a, _, _ in items], params=dict(U))["valueRanges"]
        data, notes = [], []
        for (a, link, why), cv in zip(items, cur):
            val = cv["values"][0][0]
            parts = link.split("+")
            base = sum(float((sh.values_get(p, params=dict(U)).get("values") or [[0]])[0][0] or 0) for p in parts)
            adj = round(float(val) - base, 6)
            f = f"={link}" + (("+" if adj > 0 else "-") + num(abs(adj)) if abs(adj) > 1e-9 else "")
            data.append({"range": f"'Input sheet'!{a}", "values": [[f]]})
            r, col = int(a[1:]) - 1, ord(a[0]) - 65
            notes.append({"updateCells": {"range": {"sheetId": ws.id, "startRowIndex": r, "endRowIndex": r + 1,
                                                    "startColumnIndex": col, "endColumnIndex": col + 1},
                                          "rows": [{"values": [{"note": f"Enlace + ajuste (2-oct-2026): {why}"}]}], "fields": "note"}})
            backup.setdefault(tk, {})[a] = val
            report.setdefault(tk, {})[a] = {"antes": val, "formula": f}
            time.sleep(1)
        sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": data})
        sh.batch_update({"requests": notes})
        time.sleep(3)
        after = sh.values_batch_get([f"'Input sheet'!{a}" for a, _, _ in items], params=dict(U))["valueRanges"]
        for (a, _, _), av in zip(items, after):
            report[tk][a]["despues"] = av["values"][0][0]
        print(tk, json.dumps(report[tk], ensure_ascii=False))
    (_ROOT / "reference" / "backups" / "enlaces_input_2026-10-02.json").write_text(json.dumps({"antes": backup, "informe": report}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
