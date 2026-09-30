---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de DOMINOS PIZZA INC"
ticker: "DPZ"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1voP-krWxuq4RtJDX4WYP6FEG_rRoqjMjgVXF5vPywSo/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# DOMINOS PIZZA INC (DPZ) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$226,68 en el escenario Base (rango US$156,64–US$305,18). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$422,49 (+86% frente al DCF). Con los pesos de la categoría «Madura» (40% DCF, 60% múltiplos), el ponderado hoy (lectura secundaria) es US$344,17. El valor intrínseco es el DCF: US$226,68 frente a un precio de referencia de US$292,27 (−22%).

Los múltiplos (US$422,49 hoy) quedan 86% por encima del DCF (US$226,68). Domino's cotizó durante una década a 25-30x utilidades y hoy los franquiciadores comparables cotizan a ~19x; incluso el ancla más baja implica un valor mayor que el del DCF, que queda por debajo del precio actual (US$292). La brecha sugiere que los supuestos del DCF (crecimiento y margen de largo plazo) son más conservadores que cualquier referencia de mercado para un franquiciador de flujos estables: conviene revisarlos antes de dar más peso a uno de los dos métodos.

| Escenario | DCF hoy (valor intrínseco) | Múltiplos consolidados hoy (secundario) | Ponderado hoy (secundario) | Compra con MOS sobre el DCF | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$156,64 | US$355,81 | US$276,14 | US$101,81 | US$345,07 |
| Base | US$226,68 | US$422,49 | US$344,17 | US$147,34 | US$447,94 |
| Optimista | US$305,18 | US$526,04 | US$437,69 | US$198,36 | US$586,34 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - DPZ](https://docs.google.com/spreadsheets/d/1voP-krWxuq4RtJDX4WYP6FEG_rRoqjMjgVXF5vPywSo/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$292,27.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 2,0% | 4,0% | 6,5% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 2,0% | 4,5% | 6,5% | Input B29 |
| Margen EBIT objetivo | 18,0% | 20,0% | 22,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 3,00 / 3,00 | — | Input B32/B33 |
| DCF por acción hoy | US$156,64 | US$226,68 | US$305,18 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 0,90, ERP 4,46%, Ke 9,00%, costo de la deuda después de impuestos 4,70%, peso del patrimonio 69,1%, WACC inicial 7,67% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Domino's es un franquiciador maduro desde hace una década con múltiplos estables (EV/EBITDA 18-30x); no hubo cambio de etapa del negocio, así que A usa los últimos cinco cierres y el LTM. B: franquiciadores y cadenas de restaurantes (Yum!, McDonald's, Restaurant Brands, Wingstop, Darden), datos de yfinance al 29-sep-2026. Se excluye Papa John's (ingresos −9%, reestructuración). Ajuste 0%: modelo de franquicia asset-light y crecimiento similares a Yum! y Restaurant Brands. λ = 0,25: la Domino's de FY+3 es la misma empresa madura de hoy. El P/E justificado no se calcula porque el patrimonio es negativo (recompras con deuda), así que el P/E se ancla en historia y peers.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana de los últimos 5 cierres + LTM depurados = 20,5x | 14,7x (n=5: YUM 16,4x, MCD 14,7x, QSR 14,0x, WING 16,7x, DRI 14,3x) × 1,00 = 14,7x | 17,2x / 20,9x / 25,4x | 17,0x | **18,4x** | 21,0x | 17,0x / 18,4x / 21,0x |
| EV/FCFF | mediana de los últimos 5 cierres + LTM depurados = 31,6x (EV/FCF × 0,81 = FCF después de intereses ÷ FCFF) | 24,2x (n=5: YUM 24,2x, MCD 24,2x, QSR 20,2x, WING 24,7x, DRI 28,2x) × 1,00 = 24,2x | 25,4x / 30,9x / 37,4x | 26,6x | **28,6x** | 32,2x | 30,6x / 33,0x / 37,6x |
| P/E | mediana de los últimos 5 cierres + LTM depurados = 26,7x | 19,0x (n=5: YUM 17,3x, MCD 19,0x, QSR 18,0x, WING 25,7x, DRI 19,2x) × 1,00 = 19,0x | — / — / — | 22,2x | **22,9x** | 25,1x | 22,2x / 22,9x / 25,1x |
| P/FCFE | mediana de los últimos 5 cierres + LTM depurados = 29,1x | 21,3x (n=5: YUM 22,4x, MCD 21,3x, QSR 20,1x, WING 23,0x, DRI 20,4x) × 1,00 = 21,3x | 21,4x / 25,2x / 29,4x | 23,3x | **25,2x** | 28,2x | 23,3x / 25,2x / 28,2x |
| P/OCF | mediana de los últimos 5 cierres + LTM depurados = 23,9x | 15,6x (n=5: YUM 18,0x, MCD 14,6x, QSR 17,2x, WING 15,6x, DRI 12,0x) × 1,00 = 15,6x | 20,6x / 28,5x / 36,6x | 19,2x | **21,9x** | 25,4x | 19,2x / 21,9x / 25,4x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 18,4x: promedio de historia y peers 17,6x, acercado 25% al justificado (20,9x); rango de anclas 14,7x–20,9x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 28,6x: promedio de historia y peers 27,9x, acercado 25% al justificado (30,9x); rango de anclas 24,2x–31,6x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 22,9x: promedio de historia y peers 22,9x, acercado 25% al justificado (—x); rango de anclas 19,0x–26,7x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 25,2x: promedio de historia y peers 25,2x, acercado 25% al justificado (25,2x); rango de anclas 21,3x–29,1x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 21,9x: promedio de historia y peers 19,8x, acercado 25% al justificado (28,5x); rango de anclas 15,6x–28,5x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$422,49 frente a US$226,68 del DCF (+86%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$422,49 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$202,87 | US$293,59 | US$395,26 |
| EV/EBITDA | 20% | US$419,33 | US$539,31 | US$720,80 |
| EV/FCFF | 10% | US$450,42 | US$574,65 | US$756,92 |
| P/E | 20% | US$439,20 | US$511,04 | US$626,53 |
| P/FCFE | 5% | US$505,87 | US$707,73 | US$958,83 |
| P/OCF | 5% | US$437,61 | US$551,75 | US$702,80 |
| **Ponderado FY+3** | 100% | US$345,07 | US$447,94 | US$586,34 |

Valor presente (Ke 9,00%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$361,16 | US$339,62 | US$323,76 | US$341,52 | OK |
| EV/EBITDA | Base | US$411,00 | US$416,72 | US$416,40 | US$414,71 | OK |
| EV/EBITDA | Optimista | US$499,51 | US$537,92 | US$556,53 | US$531,32 | OK |
| EV/FCFF | Conservador | US$391,69 | US$366,37 | US$347,77 | US$368,61 | OK |
| EV/FCFF | Base | US$438,39 | US$444,30 | US$443,69 | US$442,12 | OK |
| EV/FCFF | Optimista | US$518,13 | US$563,18 | US$584,42 | US$555,24 | OK |
| P/E | Conservador | US$367,07 | US$350,74 | US$339,10 | US$352,30 | OK |
| P/E | Base | US$385,36 | US$392,03 | US$394,57 | US$390,66 | OK |
| P/E | Optimista | US$432,37 | US$464,90 | US$483,74 | US$460,34 | OK |
| P/FCFE | Conservador | US$424,35 | US$405,24 | US$390,58 | US$406,72 | OK |
| P/FCFE | Base | US$528,38 | US$547,37 | US$546,43 | US$540,73 | OK |
| P/FCFE | Optimista | US$686,09 | US$721,25 | US$740,31 | US$715,88 | OK |
| P/OCF | Conservador | US$364,35 | US$349,28 | US$337,87 | US$350,50 | OK |
| P/OCF | Base | US$419,57 | US$424,70 | US$426,01 | US$423,42 | OK |
| P/OCF | Optimista | US$491,42 | US$524,28 | US$542,63 | US$519,44 | OK |

Múltiplos consolidados hoy: US$355,81 / US$422,49 / US$526,04 · DCF hoy: US$156,64 / US$226,68 / US$305,18 · Ponderado hoy: US$276,14 / US$344,17 / US$437,69 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para DPZ la diferencia es de +86% (múltiplos por encima del DCF). Los múltiplos (US$422,49 hoy) quedan 86% por encima del DCF (US$226,68). Domino's cotizó durante una década a 25-30x utilidades y hoy los franquiciadores comparables cotizan a ~19x; incluso el ancla más baja implica un valor mayor que el del DCF, que queda por debajo del precio actual (US$292). La brecha sugiere que los supuestos del DCF (crecimiento y margen de largo plazo) son más conservadores que cualquier referencia de mercado para un franquiciador de flujos estables: conviene revisarlos antes de dar más peso a uno de los dos métodos.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$292,27 supone que los ingresos crecen 7,8% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 4,4% (+3,4 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$293,59 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,0%, WACC de los años 4-10 8,2%, ROE de FY+3 — y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 18,4x | 11,4x | +84% | 4,4% | 2,2% | +2,2 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 84% por encima del DCF en FY+3. |
| EV/FCFF | 28,6x | 16,8x | +96% | 4,6% | 2,2% | +2,4 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 96% por encima del DCF en FY+3. |
| P/E | 22,9x | 12,6x | +74% | — | — | — | Revisar: el múltiplo vale 74% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 25,2x | 9,8x | +141% | 4,8% | -1,0% | +5,9 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 141% por encima del DCF en FY+3. |
| P/OCF | 21,9x | 11,1x | +88% | 3,7% | -1,0% | +4,7 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 88% por encima del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$344,17 | — |
| Múltiplos Base +20% | US$399,97 | +16,2% |
| Múltiplos Base −20% | US$288,36 | −16,2% |
| Crecimiento años 1-5 +2 pp | US$359,45 | +4,4% |
| Crecimiento años 1-5 −2 pp | US$330,37 | −4,0% |
| Margen objetivo +3 pp | US$364,69 | +6,0% |
| Margen objetivo −3 pp | US$323,64 | −6,0% |
| WACC +1 pp | US$336,38 | −2,3% |
| WACC −1 pp | US$352,50 | +2,4% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 17,00 | 17,00 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 18,41 | 18,41 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 20,99 | 20,99 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 30,63 | 26,58 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 33,02 | 28,65 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 37,65 | 32,25 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 22,17 | 22,17 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 22,85 | 22,85 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 25,09 | 25,09 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 23,30 | 23,30 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 25,23 | 25,23 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 28,17 | 28,17 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 19,24 | 19,24 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 21,94 | 21,94 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 25,37 | 25,37 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/DPZ_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1voP-krWxuq4RtJDX4WYP6FEG_rRoqjMjgVXF5vPywSo/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (YUM, MCD, PZZA, QSR, WING, DRI).

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
