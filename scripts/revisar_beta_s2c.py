#!/usr/bin/env python
"""Revisión de betas y ventas/capital con criterio Damodaran (5-oct-2026): ADBE, LULU, NKE y ONON.

Criterios (Investment Valuation, cap. 8 y cap. 11, p. 44-46):
  - Beta bottom-up = beta desapalancada del negocio, corregida por caja, reapalancada con la D/E de mercado de la empresa
    (arrendamientos incluidos). Tabla del sector según dónde vende la empresa: la de EE.UU. si la mayoría de las ventas
    está en Norteamérica (ADBE 53% + 7% resto de América, LULU 70%, ONON 51% + 6%); la global si no (NKE 44%).
  - Sin primas por riesgos diversificables: la moda y la pérdida de favor de una marca ya están en las historias
    Conservadora y Disrupción; sumarlas a la beta cuenta el mismo riesgo dos veces (prompt v4: «No cuentes el mismo
    riesgo en flujos, probabilidades y tasa»). La beta de regresión queda como referencia.
  - Ventas/capital: el de la empresa hoy, el marginal y el del sector; el rendimiento implícito del capital nuevo
    (margen objetivo × (1 − t) × ventas/capital) tiene que ser creíble frente al ROIC actual, el de la industria y el
    terminal. Ni más alto que esas referencias sin justificación, ni tan bajo que suponga capital que la empresa no usa.

Cambios:
  ADBE  beta 1,39 (Software global, 1,33) → «Single Business(US)»: 1,25 corregida por caja → 1,31 reapalancada.
  LULU  beta 1,03 (0,88 + 0,15 por moda, escrita a mano) → «Single Business(US)»: Apparel 0,79 → ~0,90 reapalancada.
  ONON  beta 1,20 (1,05 + 0,15 por moda, escrita a mano) → «Single Business(US)»: Shoe 1,00 → ~1,05 reapalancada.
  NKE   ventas/capital 2,1 (Shoe global) → 2,6: el propio de Nike (2,61 con arrendamientos) y el del sector en EE.UU.
        (2,62). Al margen objetivo (11,6%) el capital nuevo rinde ~22,6%, lo mismo que rendiría el capital actual con
        ese margen; el ROIC actual (14,7%) está deprimido por el margen de un año malo, no por más capital por venta.
  Se mantienen: beta de NKE (Shoe global 0,89 → 1,01; regresión 0,98-1,04) y ventas/capital de ADBE (1,23 ≈ 1,20 actual con
  I+D capitalizado; rinde 37% = ROIC actual), LULU (1,8: entre el sector 1,77 y el actual 2,04; rinde 25% frente a 27%)
  y ONON (2,3/2,1: rinde 29%/27% frente a 28,5% actual).

Respaldo de cada celda en reference/revision_dcf_2026-10-05/beta_s2c_respaldo.json y nota en la celda. Después hay que
regenerar cada empresa: damodaran_stories, build_story_sheet, ancla C de múltiplos (multiples_anchors --solo-justificado),
apply_multiples_v3 y regenerar_cartera.sh.

Uso: PYTHONPATH=.:scripts python scripts/revisar_beta_s2c.py [--apply] [TICKER ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402

OUT = _ROOT / "reference" / "revision_dcf_2026-10-05" / "beta_s2c_respaldo.json"
CC, IS = "Cost of capital worksheet", "Input sheet"
NOTA_BETA = ("Beta bottom-up (Damodaran, 5-oct-2026): beta desapalancada de {ind} en EE.UU. corregida por caja ({bu}, ene-2026), "
             "reapalancada por la hoja con la D/E de mercado (arrendamientos incluidos). Tabla de EE.UU. porque la mayoría de "
             "las ventas está en Norteamérica. {extra}Sin primas por riesgos diversificables: la moda y la pérdida de favor de "
             "la marca están en las historias. Regresión semanal contra el S&P 500: {reg}. Antes: {antes}.")
CAMBIOS = {
    "ADBE": {CC: {"B22": "Single Business(US)"}},
    "LULU": {CC: {"B22": "Single Business(US)"}},
    "ONON": {CC: {"B22": "Single Business(US)"}},
    "NKE": {IS: {"B32": 2.6, "B33": 2.6}},
}
NOTAS = {
    "ADBE": {CC: {"B22": NOTA_BETA.format(ind="Software (System & Application)", bu="1,25", reg="1,39 (5 años) y 0,97 (2 años)",
                                        extra="La global (1,33) incluye más software de menor escala; Adobe vende 53% en EE.UU. ",
                                        antes="«Single Business(Global)», 1,33 desapalancada → 1,39")}},
    "LULU": {CC: {"B22": NOTA_BETA.format(ind="Apparel", bu="0,79", reg="1,20 (5 años) y 1,14 (2 años)", extra="",
                                        antes="1,03 escrita a mano = 0,88 bottom-up + 0,15 por moda")}},
    "ONON": {CC: {"B22": NOTA_BETA.format(ind="Shoe", bu="1,00", reg="1,78 (5 años, desde la salida a bolsa) y 1,58 (2 años); "
                                        "la regresión de una acción reciente tiene un error estándar alto", extra="",
                                        antes="1,20 escrita a mano = 1,05 bottom-up + 0,15 por moda")}},
    "NKE": {IS: {c: ("Ventas/capital 2,6 (Damodaran, 5-oct-2026): el de Nike hoy (2,61, ventas LTM / capital invertido con "
                     "arrendamientos) y el del sector Shoe en EE.UU. (2,62). Con el margen objetivo (11,6%) y el impuesto de 25% "
                     "el capital nuevo rinde ~22,6%, lo mismo que el capital actual a ese margen y cerca del ROIC de la industria "
                     "(20,9%); el ROIC actual (14,7%) está deprimido por el margen, no por más capital por venta. Antes 2,1 "
                     "(Shoe global), que suponía 24% más capital por dólar de ventas nuevas que el que Nike usa.")
                 for c in ("B32", "B33")}},
}


def sheet_id(tk: str) -> str:
    return json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    tks = [a for a in argv if not a.startswith("--")] or list(CAMBIOS)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    for tk in tks:
        sh = ms.open_sheet(sheet_id(tk))
        for hoja, upd in CAMBIOS[tk].items():
            antes = sh.worksheet(hoja).batch_get(list(upd), value_render_option="FORMULA")
            print(tk, hoja, {c: (a[0][0] if a and a[0] else "") for c, a in zip(upd, antes)}, "→", upd)
            if apply:
                ms.write_with_backup(sh, hoja, upd, f"Revisión de beta y ventas/capital con criterio Damodaran ({tk}, 5-oct-2026)",
                                     OUT)
                sh.worksheet(hoja).update_notes(NOTAS[tk][hoja])
        if apply:
            v = sh.values_batch_get([f"'{CC}'!B24", f"'{IS}'!B36"],
                                    params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
            print(f"  {tk}: beta desapalancada {v[0]['values'][0][0]:.3f} · WACC inicial {v[1]['values'][0][0]:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
