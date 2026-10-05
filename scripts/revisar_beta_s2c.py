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
    # Tercera tanda (5-oct-2026): resto de la cartera, una a una
    "UBER": {CC: {"B22": "Direct Input", "B23": 1.2}, IS: {"B32": 2.2, "B33": 2.0, "B62": "Yes", "B63": "=(3177+1641-1312)/0,25"}},
    "PAGS": {CC: {"B23": 0.82}},
    "AFYA": {IS: {"B32": 1.5, "B33": 1.2}},
    "INTU": {IS: {"B32": 1.54, "B33": 1.54}},
    # Ventas/capital que la auditoría del 4-oct topó con el ROIC actual (que incluye el crédito mercantil de las compras)
    "BSX": {IS: {"B32": 1.2595, "B33": 1.1654}},
    "EPAM": {IS: {"B32": 3.2705, "B33": 2.8298}},
    "PYPL": {IS: {"B32": 2.4752, "B33": 2.4752}},
    "GOOG": {IS: {"B33": 1.4283}},
    "MSFT": {CC: {"B22": "Single Business(US)"}, IS: {"B33": 0.9411}},
    "NVO": {CC: {"B22": "Single Business(US)"}, IS: {"B33": 1.1}},
    "ZTS": {IS: {"B32": 1.11, "B33": 1.11}},
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
    "UBER": {CC: {
        "B22": ("Beta 1,20 directa (Damodaran, 5-oct-2026). La de «Transportation» (0,71-0,75 desapalancada; 0,76-0,80 "
                "reapalancada) es de logística con activos (FedEx, UPS, C.H. Robinson) y no describe a una plataforma de "
                "viajes y entregas de consumo discrecional: la regresión semanal de Uber contra el S&P 500 da 1,21 (2 años, "
                "error estándar 0,20) y 1,28 (5 años, 0,14), 3-4 errores estándar por encima. Los comparables puros dan más "
                "(desapalancadas con caja: Lyft ~1,8, DoorDash ~1,75, Instacart ~0,85; Grab distorsionada por la caja), pero son "
                "más chicos y menos diversificados. Se usa la regresión del período rentable (2 años), consistente con la de "
                "5 años. Antes: «Single Business(Global)», 0,80."),
        "B23": "Beta apalancada 1,20: ver nota de B22."},
             IS: {
        "B32": ("Ventas/capital 2,2 en los años 1-5 (Damodaran, 5-oct-2026). El capital invertido de la hoja (US$31.546M) incluye "
                "US$10.162M de impuestos diferidos activos (liberación de la reserva de valuación en 2024-2025; 10-Q del 2T26), "
                "que no son capital operativo: sin ellos Uber vende 2,58 por dólar de capital y su ROIC es ~26%; en tres años "
                "las ventas crecieron US$20.140M sin capital operativo neto adicional. Damodaran trata a Uber como de baja "
                "intensidad de capital (ventas/capital 5,0 en su valoración de 2014). Se baja de 2,58 a 2,2 por las flotas "
                "autónomas: Uber o sus socios de flota comprarán 10.000 robotaxis R2 de Rivian (desde 2028) con opción a 40.000 "
                "más desde 2030, además de los acuerdos con Lucid y Nuro; ~US$3.000M a cargo de Uber en cinco años elevan el "
                "capital por dólar de ventas nuevas de 0,39 a 0,45. La inversión de hasta US$1.250M en acciones de Rivian es una "
                "participación, no capital operativo. Delivery Hero no entra: la Base crece de forma orgánica; si la compra se cierra, se suman juntos sus "
                "ingresos y su precio. Con el margen objetivo (21,3%) el capital nuevo rinde ~35%. Antes 1,11 (auditoría del "
                "4-oct: topaba el rendimiento en el ROIC de 17,7%, deprimido por los impuestos diferidos)."),
        "B33": ("Ventas/capital 2,0 en los años 6-10 (Damodaran, 5-oct-2026): baja hacia el del sector en EE.UU. (1,98); el "
                "capital nuevo rinde ~32% antes del ROIC terminal = costo de capital. Antes 1,11."),
        "B62": "Sí: Uber tiene pérdidas fiscales y créditos que reducen los impuestos de los próximos años (ver B63).",
        "B63": ("Pérdidas fiscales equivalentes antes de impuestos (10-K 2025, nota de impuestos): impuestos diferidos por "
                "pérdidas US$3.177M + créditos de I+D US$1.641M − reserva de valuación US$1.312M = US$3.506M de ahorro fiscal; "
                "÷ 25% (tasa marginal de la hoja) = US$14.024M. NOL: federal US$4.143M, estatal US$7.000M y extranjero "
                "US$20.300M. Antes no se reconocían (impuestos de 25% desde el año 1, aunque Uber pagó US$345M en 2025).")}},
    "PAGS": {CC: {"B23": (
        "Beta 0,82 (Damodaran, 5-oct-2026): beta del patrimonio de «Financial Svcs. (Non-bank & Insurance)» en la tabla global "
        "(1.138 empresas, ene-2026). En una financiera la desapalancada no sirve (la deuda es materia prima), así que se usa la "
        "del patrimonio. Tabla global porque PagSeguro vende 100% en Brasil; el riesgo de Brasil va en la prima de mercado "
        "(7,33%), no en la beta. Sin prima por tamaño: es riesgo diversificable y Damodaran no la usa. Regresión semanal contra "
        "el S&P 500: 0,80 (2 años) y 1,42 (5 años); contra el índice de Brasil (EWZ) ~1,2, como StoneCo, XP e Inter. Antes 1,12 "
        "= 0,97 (tabla de EE.UU.) + 0,15 por empresa pequeña.")}},
    "AFYA": {IS: {
        "B32": ("Ventas/capital 1,5 en los años 1-5 (Damodaran, 5-oct-2026; vuelve el valor del analista anterior a la auditoría "
                "del 4-oct). La Base crece de forma orgánica (plazas de Medicina ya autorizadas que maduran, educación continua y "
                "soluciones digitales), sin compras. Con 1,5 el FCFF del año 1 (~US$190M) coincide con el FCFF real de los últimos "
                "doce meses: la reinversión del modelo es la que Afya hace. El capital actual (ventas 0,51 veces el capital; "
                "marginal 0,25-0,64) está cargado de plazas compradas (R$4.400M) y de la conversión del real. Con el margen "
                "objetivo (33%) el capital nuevo rinde ~33% con la tasa marginal de 34%: más que el ROIC actual (14,9%), que paga "
                "el sobreprecio de las compras. Antes 0,75 (la auditoría del 4-oct topaba el rendimiento en el ROIC actual)."),
        "B33": ("Ventas/capital 1,2 en los años 6-10 (Damodaran, 5-oct-2026; valor del analista anterior a la auditoría del "
                "4-oct): cuando las plazas autorizadas maduran, crecer exige plazas nuevas, compradas o construidas; queda cerca "
                "del sector Education en la tabla global (1,16). Antes 0,75.")}},
    "MSFT": {CC: {"B22": NOTA_BETA.format(
        ind="Software (System & Application)", bu="1,25", reg="1,15 (5 años) y 1,13 (2 años)",
        extra="Microsoft vende 51% en EE.UU. ", antes="«Single Business(Global)», 1,33 desapalancada → 1,36")}, IS: {'B33': 'Ventas/capital 0,94 (años 6-10). Damodaran (Investment Valuation, cap. 11): el ventas/capital se elige con el de la empresa hoy, el marginal y el del sector, y el rendimiento del capital nuevo debe ser creíble frente al ROIC de la industria. La auditoría del 4-oct-2026 lo había topado con el ROIC actual, que incluye el crédito mercantil de compras pasadas y subestima lo que rinde el crecimiento orgánico; se quita el tope (revisión del 5-oct-2026). Microsoft: hoy 0,63, marginal 0,48-0,53 por el capex de IA, sector 1,54. Los años 1-5 (0,62) cargan ese capex; en los 6-10 la capacidad madura sin volver a un modelo liviano. El capital nuevo rinde ~34%, frente al ROIC terminal de 20,6%. Antes 0,70.'}},
    "NVO": {CC: {"B22": NOTA_BETA.format(
        ind="Drugs (Pharmaceutical)", bu="0,92", reg="0,78 (5 años) y 1,12 (2 años)",
        extra="Novo Nordisk vende 56% en Norteamérica. ", antes="«Single Business(Global)» → 1,09")}, IS: {'B33': 'Ventas/capital 1,10 (años 6-10). Damodaran (Investment Valuation, cap. 11): el ventas/capital se elige con el de la empresa hoy, el marginal y el del sector, y el rendimiento del capital nuevo debe ser creíble frente al ROIC de la industria. La auditoría del 4-oct-2026 lo había topado con el ROIC actual, que incluye el crédito mercantil de compras pasadas y subestima lo que rinde el crecimiento orgánico; se quita el tope (revisión del 5-oct-2026). Novo Nordisk: hoy 0,61, marginal 0,17-0,47 por el capex de capacidad y la compra de plantas, sector Drugs (Pharmaceutical) 1,11. Los años 1-5 (0,57) cargan ese capex; en los 6-10 la capacidad ya está construida. La pérdida de la ventaja va en el margen y en el ROIC terminal (9,2%), no en el capital. Antes 0,76.'}},
    "INTU": {IS: {c: ("Ventas/capital 1,54 (Damodaran, 5-oct-2026): el del sector Software (System & Application) en EE.UU. La "
                      "Base crece de forma orgánica (QuickBooks, nómina, pagos, TurboTax, Credit Karma) y Intuit no compra desde "
                      "Mailchimp (2021). El capital actual (ventas 1,08 veces el capital) carga ~US$14.000M de crédito mercantil "
                      "de Credit Karma y Mailchimp, y el capex orgánico es mínimo (US$175M en FY26 frente a US$8.838M de flujo "
                      "operativo): el ventas/capital orgánico es mucho mayor. El del sector, que ya incluye empresas que compran, "
                      "es una referencia prudente. Con el margen objetivo (32,2%) y un impuesto de 23% el capital nuevo rinde ~38%. "
                      "Antes " + a + " (la auditoría del 4-oct topaba el rendimiento en el ROIC de la industria, 29,3%).")
                 for c, a in (("B32", "1,18; antes de la auditoría 2,31"), ("B33", "1,18; antes de la auditoría 1,88"))}},
    'BSX': {IS: {'B32': 'Ventas/capital 1,26 (años 1-5). Damodaran (Investment Valuation, cap. 11): el ventas/capital se elige con el de la empresa hoy, el marginal y el del sector, y el rendimiento del capital nuevo debe ser creíble frente al ROIC de la industria. La auditoría del 4-oct-2026 lo había topado con el ROIC actual, que incluye el crédito mercantil de compras pasadas y subestima lo que rinde el crecimiento orgánico; se quita el tope (revisión del 5-oct-2026). Boston Scientific: hoy 0,60 (con US$18.640M de crédito mercantil), marginal 2,01 (último año) y 0,87 (tres años, con compras), sector Healthcare Products 1,48. La Base crece con los segmentos (5-10%), sin las compras: el capital nuevo rinde ~25% con el margen objetivo (24,2%), frente a 17% de la industria; el ROIC terminal sigue igual al costo de capital. Valor del analista, con el capital arrendado. Antes 0,86.', 'B33': 'Ventas/capital 1,17 (años 6-10). Damodaran (Investment Valuation, cap. 11): el ventas/capital se elige con el de la empresa hoy, el marginal y el del sector, y el rendimiento del capital nuevo debe ser creíble frente al ROIC de la industria. La auditoría del 4-oct-2026 lo había topado con el ROIC actual, que incluye el crédito mercantil de compras pasadas y subestima lo que rinde el crecimiento orgánico; se quita el tope (revisión del 5-oct-2026). Rinde ~23%. Valor del analista, con el capital arrendado. Antes 0,86.'}},
    'EPAM': {IS: {'B32': 'Ventas/capital 3,27 (años 1-5). Damodaran (Investment Valuation, cap. 11): el ventas/capital se elige con el de la empresa hoy, el marginal y el del sector, y el rendimiento del capital nuevo debe ser creíble frente al ROIC de la industria. La auditoría del 4-oct-2026 lo había topado con el ROIC actual, que incluye el crédito mercantil de compras pasadas y subestima lo que rinde el crecimiento orgánico; se quita el tope (revisión del 5-oct-2026). EPAM: hoy 1,95 (con el crédito mercantil de las compras y caja), sector Computer Services 5,19; servicios profesionales con capex mínimo (US$56M LTM). El capital nuevo rinde ~32%, frente a 26% de la industria; el ROIC terminal (12%) refleja una ventaja que se desvanece. Valor del analista, con el capital arrendado. Antes 2,65.', 'B33': 'Ventas/capital 2,83 (años 6-10). Damodaran (Investment Valuation, cap. 11): el ventas/capital se elige con el de la empresa hoy, el marginal y el del sector, y el rendimiento del capital nuevo debe ser creíble frente al ROIC de la industria. La auditoría del 4-oct-2026 lo había topado con el ROIC actual, que incluye el crédito mercantil de compras pasadas y subestima lo que rinde el crecimiento orgánico; se quita el tope (revisión del 5-oct-2026). Rinde ~28%. Valor del analista, con el capital arrendado. Antes 2,65.'}},
    'PYPL': {IS: {'B32': 'Ventas/capital 2,48. Damodaran (Investment Valuation, cap. 11): el ventas/capital se elige con el de la empresa hoy, el marginal y el del sector, y el rendimiento del capital nuevo debe ser creíble frente al ROIC de la industria. La auditoría del 4-oct-2026 lo había topado con el ROIC actual, que incluye el crédito mercantil de compras pasadas y subestima lo que rinde el crecimiento orgánico; se quita el tope (revisión del 5-oct-2026). PayPal: hoy 1,38 (con US$10.900M de crédito mercantil), marginal 3,19 (último año) y 7,68 (tres años); 2020-2025: ΔIngresos US$11.718M / ΔCapital con I+D ~US$4.550M = 2,6. El capital nuevo rinde ~37%. Valor del analista, con el capital arrendado. Antes 1,42.', 'B33': 'Ventas/capital 2,48. Damodaran (Investment Valuation, cap. 11): el ventas/capital se elige con el de la empresa hoy, el marginal y el del sector, y el rendimiento del capital nuevo debe ser creíble frente al ROIC de la industria. La auditoría del 4-oct-2026 lo había topado con el ROIC actual, que incluye el crédito mercantil de compras pasadas y subestima lo que rinde el crecimiento orgánico; se quita el tope (revisión del 5-oct-2026). PayPal: hoy 1,38 (con US$10.900M de crédito mercantil), marginal 3,19 (último año) y 7,68 (tres años); 2020-2025: ΔIngresos US$11.718M / ΔCapital con I+D ~US$4.550M = 2,6. El capital nuevo rinde ~37%. Valor del analista, con el capital arrendado. Antes 1,42.'}},
    'GOOG': {IS: {'B33': 'Ventas/capital 1,43 (años 6-10). Damodaran (Investment Valuation, cap. 11): el ventas/capital se elige con el de la empresa hoy, el marginal y el del sector, y el rendimiento del capital nuevo debe ser creíble frente al ROIC de la industria. La auditoría del 4-oct-2026 lo había topado con el ROIC actual, que incluye el crédito mercantil de compras pasadas y subestima lo que rinde el crecimiento orgánico; se quita el tope (revisión del 5-oct-2026). Alphabet: hoy 1,22, marginal 0,44-0,65 por el pico de capex de IA, sector Software (Internet) 1,35. Los años 1-5 (1,15) cargan ese capex; en los 6-10 la capacidad ya está construida. El capital nuevo rinde ~42%, frente al ROIC terminal de 29,3% (industria). Antes 1,12.'}},
    'ZTS': {IS: {'B32': 'Ventas/capital 1,11 (el del sector Drugs (Pharmaceutical)). Damodaran (Investment Valuation, cap. 11): el ventas/capital se elige con el de la empresa hoy, el marginal y el del sector, y el rendimiento del capital nuevo debe ser creíble frente al ROIC de la industria. La auditoría del 4-oct-2026 lo había topado con el ROIC actual, que incluye el crédito mercantil de compras pasadas y subestima lo que rinde el crecimiento orgánico; se quita el tope (revisión del 5-oct-2026). Zoetis: hoy 0,89 (con el crédito mercantil de las compras), marginal 0,32 (último año) y 1,03 (tres años); capex de US$521M LTM con D&A de ~US$480M. El capital nuevo rinde ~32%; no se vuelve al 1,91 anterior a la auditoría porque implicaba ~55%, muy por encima de su industria (17%). Antes 0,91.', 'B33': 'Ventas/capital 1,11 (el del sector Drugs (Pharmaceutical)). Damodaran (Investment Valuation, cap. 11): el ventas/capital se elige con el de la empresa hoy, el marginal y el del sector, y el rendimiento del capital nuevo debe ser creíble frente al ROIC de la industria. La auditoría del 4-oct-2026 lo había topado con el ROIC actual, que incluye el crédito mercantil de compras pasadas y subestima lo que rinde el crecimiento orgánico; se quita el tope (revisión del 5-oct-2026). Zoetis: hoy 0,89 (con el crédito mercantil de las compras), marginal 0,32 (último año) y 1,03 (tres años); capex de US$521M LTM con D&A de ~US$480M. El capital nuevo rinde ~32%; no se vuelve al 1,91 anterior a la auditoría porque implicaba ~55%, muy por encima de su industria (17%). Antes 0,91.'}},
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
