---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de ADOBE INC."
ticker: "ADBE"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/19WcSOKymo4gR6lnKiLB1gAitYFFwfI3xl08E4BDzLDw/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# ADOBE INC. (ADBE) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$466,29 por acción.** Complemento: DCF esperado por probabilidades US$364,82; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$172,96–US$584,46; precio con MOS 35% sobre el esperado: US$237,13; precio de referencia US$239,94. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son la calibración técnica anterior de la hoja (Base técnico US$537,02) y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La IA se cobra dentro de la suscripción** (valor principal) | 40% | US$466,29 | US$186,52 |
| Conservadora · Erosión gradual frente a Figma y Canva | 35% | US$268,32 | US$93,91 |
| Disrupción · Deterioro de los fundamentales: La IA generativa comoditiza la creatividad | 15% | US$172,96 | US$25,94 |
| Optimista · La IA amplía el mercado de Adobe | 10% | US$584,46 | US$58,45 |
| **DCF esperado (complemento)** | 100% | **US$364,82** | |

Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$536,48 por acción y los múltiplos, US$486,87 hoy: 9% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

| Escenario | DCF técnico anterior hoy (calibración) | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$537,02 | US$487,74 | US$507,45 | US$237,13 | US$699,90 |
| Conservador | US$413,67 | US$321,55 | US$358,40 | US$237,13 | US$482,01 |
| Optimista | US$823,48 | US$813,17 | US$817,30 | US$237,13 | US$1.198,38 |

## 2. Datos

- Hoja del modelo: [Modelo_JMR_Plantilla_Maestra ADBE](https://docs.google.com/spreadsheets/d/19WcSOKymo4gR6lnKiLB1gAitYFFwfI3xl08E4BDzLDw/edit).
- Revisión de datos y modelo: 28 de septiembre de 2026 (precio del análisis: 14 de septiembre de 2026). Precio de referencia de la hoja: US$239,94.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 6,0% | 12,0% | 16,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 6,0% | 10,0% | 16,0% | Input B29 |
| Margen EBIT objetivo | 39,3% | 40,1% | 45,1% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 3 | 3 | 3 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 3,77 / 4,21 | — | Input B32/B33 |
| DCF por acción hoy | US$413,67 | US$537,02 | US$823,48 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,39, ERP 4,46%, Ke 11,21%, costo de la deuda después de impuestos 4,32%, peso del patrimonio 94,1%, WACC inicial 10,80% y terminal 9,22%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Adobe pasó de crecer 15-25% anual (FY16-FY21) a ~10-11% (FY23-FY25: +10,2%, +10,8%, +10,5%), y el mercado re-valoró el software de aplicaciones por el riesgo de la IA generativa; los múltiplos de 40-60x de la etapa anterior no describen a la empresa de FY+3, así que A usa solo los cierres FY23-FY25 y el LTM. B: peers de software de aplicaciones con datos de yfinance al 29-sep-2026 (ADSK, INTU, CRM, WDAY, PTC); se excluye ServiceNow (NOW) porque crece 24% con margen operativo GAAP de 4%, lo que infla sus múltiplos (P/E 81x). No se usa MSFT (megacap diversificada). Ajuste +5%: margen operativo de Adobe 35-39% frente a ~21% de mediana de los peers y conversión de caja superior (+10%), compensado en parte por un crecimiento algo menor (10-12% vs ~13% de mediana, -5%). λ = 0,25: la Adobe de FY+3 del escenario Base (crecimiento ~10%, margen 40%) es parecida a la de hoy, así que el Base se acerca solo un 25% al múltiplo justificado.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 21,8x | 16,9x (n=5: ADSK 18,4x, INTU 10,7x, CRM 16,9x, WDAY 28,9x, PTC 12,9x) × 1,05 = 17,8x | 19,0x / 14,8x / 35,0x | **19,6x** | 13,9x | 28,5x | 19,6x / 13,9x / 28,6x |
| EV/FCFF | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 21,1x | 15,0x (n=5: ADSK 15,0x, INTU 8,3x, CRM 13,8x, WDAY 15,6x, PTC 16,6x) × 1,05 = 15,7x | 28,8x / 21,7x / 54,4x | **21,0x** | 15,9x | 31,0x | 21,1x / 16,1x / 31,2x |
| P/E | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 30,5x | 20,6x (n=5: ADSK 26,3x, INTU 16,3x, CRM 20,6x, WDAY 38,8x, PTC 13,3x) × 1,05 = 21,6x | 20,8x / 16,6x / 33,0x | **24,7x** | 17,9x | 35,6x | 24,7x / 17,9x / 35,6x |
| P/FCFE | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 21,2x | 15,1x (n=5: ADSK 15,1x, INTU 8,3x, CRM 12,2x, WDAY 16,0x, PTC 16,0x) × 1,05 = 15,9x | 22,3x / 17,8x / 35,3x | **19,5x** | 14,2x | 26,8x | 19,5x / 14,2x / 26,8x |
| P/OCF | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 20,7x | 14,7x (n=5: ADSK 14,7x, INTU 8,1x, CRM 11,8x, WDAY 14,8x, PTC 15,6x) × 1,05 = 15,4x | 21,4x / 17,1x / 34,0x | **18,9x** | 13,8x | 25,7x | 18,9x / 13,8x / 25,7x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 19,6x: promedio de historia y peers 19,8x, acercado 25% al justificado (19,0x); rango de anclas 17,8x–21,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 21,0x: promedio de historia y peers 18,4x, acercado 25% al justificado (28,8x); rango de anclas 15,7x–28,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 24,7x: promedio de historia y peers 26,1x, acercado 25% al justificado (20,8x); rango de anclas 20,8x–30,5x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 19,5x: promedio de historia y peers 18,5x, acercado 25% al justificado (22,3x); rango de anclas 15,9x–22,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 18,9x: promedio de historia y peers 18,1x, acercado 25% al justificado (21,4x); rango de anclas 15,4x–21,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$487,74 frente a US$537,02 del DCF (−9%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$487,74 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$738,53 | US$568,89 | US$1.132,47 |
| EV/EBITDA | 20% | US$773,85 | US$473,07 | US$1.448,21 |
| EV/FCFF | 10% | US$545,29 | US$366,61 | US$1.003,37 |
| P/E | 20% | US$716,34 | US$447,12 | US$1.334,70 |
| P/FCFE | 5% | US$516,96 | US$336,40 | US$888,03 |
| P/OCF | 5% | US$521,51 | US$338,62 | US$881,49 |
| **Ponderado FY+3** | 100% | US$699,90 | US$482,01 | US$1.198,38 |

Valor presente (Ke 11,21%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$558,18 | US$563,03 | US$562,71 | US$561,31 | OK |
| EV/EBITDA | Conservador | US$374,67 | US$359,47 | US$343,99 | US$359,38 | OK |
| EV/EBITDA | Optimista | US$843,06 | US$965,76 | US$1.053,07 | US$953,96 | OK |
| EV/FCFF | Base | US$388,34 | US$395,24 | US$396,51 | US$393,36 | OK |
| EV/FCFF | Conservador | US$288,00 | US$277,93 | US$266,58 | US$277,50 | OK |
| EV/FCFF | Optimista | US$560,06 | US$660,97 | US$729,60 | US$650,21 | OK |
| P/E | Base | US$512,45 | US$520,03 | US$520,89 | US$517,79 | OK |
| P/E | Conservador | US$351,83 | US$339,18 | US$325,13 | US$338,71 | OK |
| P/E | Optimista | US$763,39 | US$885,71 | US$970,53 | US$873,21 | OK |
| P/FCFE | Base | US$368,52 | US$374,86 | US$375,91 | US$373,09 | OK |
| P/FCFE | Conservador | US$264,47 | US$255,11 | US$244,62 | US$254,73 | OK |
| P/FCFE | Optimista | US$496,48 | US$585,32 | US$645,73 | US$575,84 | OK |
| P/OCF | Base | US$372,36 | US$378,36 | US$379,22 | US$376,64 | OK |
| P/OCF | Conservador | US$266,39 | US$256,85 | US$246,23 | US$256,49 | OK |
| P/OCF | Optimista | US$496,19 | US$582,18 | US$640,98 | US$573,12 | OK |

Múltiplos consolidados hoy: US$487,74 / US$321,55 / US$813,17 · DCF técnico hoy: US$537,02 / US$413,67 / US$823,48 · Ponderado hoy: US$507,45 / US$358,40 / US$817,30 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para ADBE la diferencia es de −9% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$536,48 por acción y los múltiplos, US$486,87 hoy: 9% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$239,94 supone que los ingresos crecen -4,0% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 10,4% (−14,4 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$738,53 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,2%, WACC de los años 4-10 10,1%, ROE de FY+3 95,6% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 19,6x | 18,7x | +5% | 6,5% | 6,4% | +0,2 pp | Coherente con el DCF. |
| EV/FCFF | 21,0x | 28,4x | −26% | 5,1% | 6,4% | −1,3 pp | Revisar: el múltiplo vale 26% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 24,7x | 25,5x | −3% | 7,2% | 7,3% | −0,1 pp | Coherente con el DCF. |
| P/FCFE | 19,5x | 27,8x | −30% | 5,8% | 7,3% | −1,6 pp | Revisar: el múltiplo vale 30% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 18,9x | 26,8x | −29% | 5,8% | 7,3% | −1,5 pp | Revisar: el múltiplo vale 29% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$507,45 | — |
| Múltiplos Base +20% | US$566,07 | +11,6% |
| Múltiplos Base −20% | US$448,83 | −11,6% |
| Crecimiento años 2-5 +2 pp | US$528,17 | +4,1% |
| Crecimiento años 2-5 −2 pp | US$488,49 | −3,7% |
| Margen objetivo +3 pp | US$523,19 | +3,1% |
| Margen objetivo −3 pp | US$491,71 | −3,1% |
| WACC +1 pp | US$495,70 | −2,3% |
| WACC −1 pp | US$520,04 | +2,5% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 13,90 | 13,90 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 19,57 | 19,57 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 28,65 | 28,51 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 16,08 | 15,87 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 21,10 | 21,00 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 31,21 | 30,99 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 17,94 | 17,94 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 24,73 | 24,73 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 35,57 | 35,57 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 14,22 | 14,22 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 19,46 | 19,46 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 26,83 | 26,83 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 13,78 | 13,78 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 18,89 | 18,89 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 25,70 | 25,70 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/ADBE_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/19WcSOKymo4gR6lnKiLB1gAitYFFwfI3xl08E4BDzLDw/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (ADSK, INTU, CRM, NOW, WDAY, PTC).

## 10. Control de calidad

| Comprobación | ¿Cumple? |
|---|---|
| No se cambiaron fórmulas, pesos ni estructura (solo J8/J19/J30 y textos) | Sí |
| Cada múltiplo Base tiene sus tres anclas con fuente y fecha | Sí |
| Ningún múltiplo se derivó del DCF ni se ajustó después de verlo | Sí |
| Cada Base dentro del rango de sus anclas | Sí |
| Conservador < Base < Optimista en los cinco métodos; J8/J19/J30 escritos | Sí |
| Métodos no aplicables declarados | Sí |
| «Supuestos de los Múltiplos» A3 y A12 completos | Sí |
| DCF hoy, múltiplos hoy y ponderado hoy reportados por separado | Sí |
| Chequeo VP3 < FY+3 en OK en los tres escenarios | Sí |
| DCF Conservador < Base < Optimista | Sí |
