#!/usr/bin/env python
"""Revisión de betas y ventas/capital con criterio Damodaran (5-oct-2026): ADBE, LULU, NKE y ONON; después, una a una,
CELH, CMG, DPZ y SHAK.

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
  CELH  beta 1,0 (0,62 + 0,38 por categoría única y distribuidor, escrita a mano) → «Single Business(US)»: Beverage
        (Soft) 0,58 → ~0,62 reapalancada (96% de las ventas en Norteamérica). Ventas/capital 1,8/1,6 se mantiene: rinde
        27%/24% frente a 29% de la industria; el actual (1,0) y el marginal (0,6) incluyen la compra de Alani Nu.
  CMG   beta 0,95 (0,85 + 0,10 por un solo concepto, escrita a mano) → «Single Business(US)»: Restaurant/Dining 0,78 →
        ~0,86 reapalancada (regresión 0,89-1,00). Ventas/capital 1,51 (el del sector) se mantiene: rinde ~21%, entre el
        ROIC de la industria (18,4%) y el actual (23-25%); Chipotle no franquicia, así que el sector es comparable.
  DPZ   beta 1,17 (1,07 + 0,10 por un solo concepto, escrita a mano) → «Single Business(US)»: Restaurant/Dining 0,78 →
        ~1,07 reapalancada con la D/E alta (~0,48). Ventas/capital 2,64 → 5,4 (años 1-5, el propio: franquiciadora, el sector
        no es comparable) y 3,4 (años 6-10, punto medio hacia el sector): el capital nuevo rinde ~84% → ~53%, frente a un ROIC
        actual de ~81% y un terminal de 18,4%.
  SHAK  beta 1,25 (0,98 + ~0,27 por cadena pequeña, un solo concepto y márgenes finos, escrita a mano) → «Single
        Business(US)»: Restaurant/Dining 0,78 → ~0,98 reapalancada con los arrendamientos. Regresión 1,54-1,55 como
        referencia. Ventas/capital 1,51 → 1,9 (años 1-5, marginal del último año) y 1,7 (años 6-10): rinde ~13,6% → ~12%.
  Se mantienen: beta de NKE (Shoe global 0,89 → 1,01; regresión 0,98-1,04) y ventas/capital de ADBE (1,23 ≈ 1,20 actual con
  I+D capitalizado; rinde 37% = ROIC actual), LULU (1,8: entre el sector 1,77 y el actual 2,04; rinde 25% frente a 27%)
  y ONON (2,3/2,1: rinde 29%/27% frente a 28,5% actual).

Respaldo de cada celda en reference/revision_dcf_2026-10-05/beta_s2c_respaldo.json (CELH, CMG, DPZ y SHAK:
beta_s2c_respaldo_<TICKER>.json) y nota en la celda. Después hay que
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
PRIMERA_TANDA = ("ADBE", "LULU", "NKE", "ONON")  # el respaldo va por celda: la segunda tanda usa un archivo por empresa


def respaldo(tk: str) -> Path:
    return OUT if tk in PRIMERA_TANDA else OUT.with_name(f"beta_s2c_respaldo_{tk}.json")
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
    # Segunda tanda (5-oct-2026), una empresa a la vez
    "CELH": {CC: {"B22": "Single Business(US)"}},
    "CMG": {CC: {"B22": "Single Business(US)"}},
    "DPZ": {CC: {"B22": "Single Business(US)"}, IS: {"B32": 5.4, "B33": 3.4}},
    "SHAK": {CC: {"B22": "Single Business(US)"}, IS: {"B32": 1.9, "B33": 1.7}},
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
    "CELH": {CC: {"B22": NOTA_BETA.format(
        ind="Beverage (Soft)", bu="0,58", reg="1,55 (5 años) y 0,83 (2 años); Monster 0,49 y 0,36",
        extra="Celsius vende 96% en Norteamérica. La dependencia de un distribuidor (~60% de las ventas) y la categoría "
              "única son riesgos propios, diversificables: van en las historias (Conservadora: pérdida de espacio en "
              "anaquel; Disrupción: la categoría pierde favor), no en la tasa. Fabricación tercerizada: el apalancamiento "
              "operativo no es mayor que el del sector. ",
        antes="1,0 escrita a mano = ~0,62 bottom-up + ~0,38 por categoría única y distribuidor")}},
    "CMG": {CC: {"B22": NOTA_BETA.format(
        ind="Restaurant/Dining", bu="0,78", reg="1,00 (5 años) y 0,89 (2 años)",
        extra="Chipotle vende 100% en Norteamérica. Tener un solo concepto es un riesgo propio y diversificable: va en las "
              "historias (Conservadora: el concepto pierde tráfico), no en la tasa. ",
        antes="0,95 escrita a mano = 0,85 bottom-up + 0,10 por un solo concepto de restaurante")}},
    "DPZ": {CC: {"B22": NOTA_BETA.format(
        ind="Restaurant/Dining", bu="0,78", reg="0,77 (5 años) y 0,63 (2 años)",
        extra="Domino's vende 93% en Norteamérica. La D/E de mercado alta (~0,48, deuda titulizada) explica que la beta "
              "reapalancada (~1,07) supere a la del sector. Un solo concepto (pizza a domicilio) es un riesgo propio y "
              "diversificable: va en las historias, no en la tasa. ",
        antes="1,17 escrita a mano = 1,07 bottom-up + 0,10 por un solo concepto")},
            IS: {"B32": ("Ventas/capital 5,4 en los años 1-5 (Damodaran, 5-oct-2026): el de Domino's hoy (5,37, ventas LTM / "
                         "capital invertido con arrendamientos). Es franquiciadora: las tiendas las pagan los franquiciados y en "
                         "tres años las ventas crecieron US$403M con US$6M de capital; el sector (1,51) es de operadores con "
                         "locales propios y no es comparable. Con el margen objetivo (20,3%) y un impuesto de 23% el capital "
                         "nuevo rinde ~84%, igual al ROIC actual (~81-83%). Antes 2,6415 (3 ajustado por arrendamientos), que "
                         "suponía el doble del capital que Domino's usa por dólar de ventas."),
                 "B33": ("Ventas/capital 3,4 en los años 6-10 (Damodaran, 5-oct-2026): punto medio entre el de Domino's (5,37) y "
                         "el del sector (1,51), para que el rendimiento del capital nuevo baje gradualmente (~84% → ~53%) hacia "
                         "el ROIC terminal de la industria (18,4%). Antes 2,6415.")}},
    "SHAK": {CC: {"B22": NOTA_BETA.format(
        ind="Restaurant/Dining", bu="0,78", reg="1,54 (5 años) y 1,55 (2 años); CAVA 1,63-1,85, Sweetgreen 1,67-1,71, "
                                              "Wingstop 1,15-1,39, Chipotle 0,89-1,00",
        extra="Shake Shack vende 97% en Norteamérica. Los arrendamientos entran como deuda, así que el costo fijo del "
              "alquiler ya sube la beta reapalancada (~0,98). Cadena pequeña, un solo concepto y márgenes finos son riesgos "
              "propios: van en las historias (la Conservadora no alcanza el margen objetivo), no en la tasa; la prima por "
              "tamaño no es parte del criterio de Damodaran. ",
        antes="1,25 escrita a mano = 0,98 bottom-up + ~0,27 por cadena pequeña, un solo concepto y márgenes finos")},
             IS: {"B32": ("Ventas/capital 1,9 en los años 1-5 (Damodaran, 5-oct-2026): el marginal del último año (1,88; 2,31 en "
                          "tres años), con arrendamientos. Los locales nuevos (formatos más chicos, ventanilla) usan menos capital "
                          "por venta que la base actual (1,36), cargada de locales en maduración. Con el margen objetivo (9,5%) y "
                          "un impuesto de 25% el capital nuevo rinde ~13,6%: más que el ROIC actual (4,6%), menos que el de la "
                          "industria (18,4%). Antes 1,51 (el del sector)."),
                  "B33": ("Ventas/capital 1,7 en los años 6-10 (Damodaran, 5-oct-2026): baja hacia el del sector (1,51); el capital "
                          "nuevo rinde ~12%. Antes 1,51.")}},
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
                                     respaldo(tk))
                sh.worksheet(hoja).update_notes(NOTAS[tk][hoja])
        if apply:
            v = sh.values_batch_get([f"'{CC}'!B24", f"'{IS}'!B36"],
                                    params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
            print(f"  {tk}: beta desapalancada {v[0]['values'][0][0]:.3f} · WACC inicial {v[1]['values'][0][0]:.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
