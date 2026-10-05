#!/usr/bin/env python
"""Prima de mercado madura de Damodaran de octubre de 2026 en todas las hojas (5-oct-2026).

La valoración tiene corte al 30-sep-2026: tasa libre de riesgo 5,29% (UST 10 años de ese día). La prima implícita que
Damodaran publicó el 1-oct-2026 (ERPOct26.xlsx, «Implied Equity Risk Premium (with US treasury rate as riskfree rate)»)
se calculó con esa misma tasa y con los precios del 30-sep: 3,70%. Las hojas usaban la de septiembre (4,09%, calculada
con una tasa de 4,75% el 1-sep), es decir, mezclaban una tasa del 30-sep con una prima del 1-sep.

Cambios por hoja (respaldo en reference/revision_dcf_2026-10-05/prima_octubre_respaldo_<T>.json y nota en la celda):
  - 'Country equity risk premiums'!B2 (prima madura) = 3,70%. De ahí salen la prima de cada país y región
    (= madura + riesgo país) y el costo de capital terminal (= tasa libre + prima madura).
  - 'Cost of capital worksheet'!B27 (prima directa, solo se usa con «Will Input») = 3,70% donde valía 4,09%.
  - Supuestos terminales fijados a mano que dependen de la prima: bajan los mismos 0,39 puntos.
    AFYA 'Input sheet'!B47 11,11% → 10,72%; PAGS 'Input sheet'!B47 y 'DCF FCFE financiero'!B4 12,30% → 11,91%.

Uso: PYTHONPATH=.:scripts python scripts/prima_mercado_octubre.py [--apply] [TICKER ...]
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402

ERP_SEP, ERP_OCT = 0.0409, 0.037
OUT = _ROOT / "reference" / "revision_dcf_2026-10-05"
NOTA = ("Prima de mercado madura 3,70%: implícita de Damodaran del 1-oct-2026 (ERPOct26.xlsx), calculada con la tasa del "
        "UST a 10 años del 30-sep-2026 (5,29%), la misma de la hoja, y con los precios de esa fecha. Antes 4,09% (1-sep-2026, "
        "calculada con 4,75%). Cambio del 5-oct-2026.")
TERMINAL = {  # supuestos terminales a mano: hoja -> {celda: (antes, después)}
    "AFYA": {"Input sheet": {"B47": (0.1111, 0.1072)}},
    "PAGS": {"Input sheet": {"B47": (0.123, 0.1191)}, "DCF FCFE financiero": {"B4": (0.123, 0.1191)}},
}
NOTA_T = ("Supuesto terminal bajado 0,39 puntos por la prima de mercado de octubre de 2026 (3,70% en lugar de 4,09%), como el "
          "costo de capital terminal de las demás hojas (tasa libre + prima madura). Antes {antes}. Cambio del 5-oct-2026.")


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    tks = [a for a in argv if not a.startswith("--")] or sorted(json.loads((_ROOT / "reference" / "cartera_drive.json").read_text())["empresas"])
    for tk in tks:
        sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
        for i in range(4):
            try:
                sh = ms.open_sheet(sid)
                b2, b27 = [(x.get("values") or [[None]])[0][0] for x in sh.values_batch_get(
                    ["'Country equity risk premiums'!B2", "'Cost of capital worksheet'!B27"],
                    params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]]
                break
            except Exception:
                time.sleep(70)
        print(f"{tk:5s} B2 {b2} → {ERP_OCT} | B27 {b27}" + (f" | terminal {TERMINAL[tk]}" if tk in TERMINAL else ""))
        if not apply:
            continue
        bk = OUT / f"prima_octubre_respaldo_{tk}.json"
        if abs((b2 or 0) - ERP_OCT) > 1e-9:
            ms.write_with_backup(sh, "Country equity risk premiums", {"B2": ERP_OCT}, f"Prima de mercado de octubre ({tk})", bk)
            sh.worksheet("Country equity risk premiums").update_notes({"B2": NOTA})
        if isinstance(b27, (int, float)) and abs(b27 - ERP_SEP) < 1e-9:
            ms.write_with_backup(sh, "Cost of capital worksheet", {"B27": ERP_OCT}, f"Prima de mercado de octubre ({tk})", bk)
        for hoja, celdas in TERMINAL.get(tk, {}).items():
            ms.write_with_backup(sh, hoja, {c: d for c, (a, d) in celdas.items()}, f"Terminal con la prima de octubre ({tk})", bk)
            sh.worksheet(hoja).update_notes({c: NOTA_T.format(antes=f"{a * 100:.2f}%".replace(".", ",")) for c, (a, d) in celdas.items()})
        v = sh.values_batch_get(["'Input sheet'!B36", "'Valuation output'!M14", "'Valuation output'!B35"],
                                params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
        w0, wT, base = [x["values"][0][0] for x in v]
        print(f"      costo de capital {w0:.4f} → terminal {wT:.4f} · DCF de 'Valuation output' {base:.2f}")
        time.sleep(2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
