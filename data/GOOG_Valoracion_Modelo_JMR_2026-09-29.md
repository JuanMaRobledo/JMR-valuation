---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Alphabet Inc."
ticker: "GOOG"
analysis_date: "2026-09-29"
sheet: "https://docs.google.com/spreadsheets/d/1yt2zqdGz1JWEqV3SYqqL-nHarO7C1Oud1lvR3pY9i0U/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Alphabet Inc. (GOOG) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$174,29 en el escenario Base (rango US$155,29–US$292,41). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$209,76 (+20% frente al DCF). Con los pesos de la categoría «Madura» (40% DCF, 60% múltiplos), el valor intrínseco ponderado hoy es US$195,57, frente a un precio de referencia de US$339,16 (−42%).

Los múltiplos (US$209,76 hoy) quedan 20% por encima del DCF (US$174,29), dentro del rango de ±25%: ambos métodos coinciden razonablemente. Los dos quedan muy por debajo del precio (US$339,16): el mercado descuenta más crecimiento de Cloud e IA que el escenario Base, y además las participaciones de Alphabet en otras empresas (que generaron US$135,9 mil millones de ganancias en el 1S26) no están en los múltiplos operativos; conviene revisar que la hoja las incluya a valor actual como activos no operativos.

| Escenario | DCF hoy | Múltiplos consolidados hoy | Valor intrínseco ponderado hoy | Compra con MOS hoy | Precio objetivo FY+3 ponderado |
|---|---:|---:|---:|---:|---:|
| Conservador | US$155,29 | US$177,22 | US$168,44 | US$109,49 | US$220,04 |
| Base | US$174,29 | US$209,76 | US$195,57 | US$127,12 | US$258,82 |
| Optimista | US$292,41 | US$333,28 | US$316,93 | US$206,00 | US$448,08 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - Alphabet (GOOG)](https://docs.google.com/spreadsheets/d/1yt2zqdGz1JWEqV3SYqqL-nHarO7C1Oud1lvR3pY9i0U/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$339,16.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 6,0% | 11,0% | 16,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 6,0% | 7,0% | 16,0% | Input B29 |
| Margen EBIT objetivo | 32,5% | 33,5% | 37,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,50 / 2,00 | — | Input B32/B33 |
| DCF por acción hoy | US$155,29 | US$174,29 | US$292,41 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,05, ERP 4,46%, Ke 9,67%, costo de la deuda después de impuestos 4,65%, peso del patrimonio 98,7%, WACC inicial 9,61% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: los cierres 2016-2021 de la hoja dan múltiplos de ~1x porque el precio no está ajustado por el split 20:1 de julio de 2022; no son representativos y se usa la historia desde Dec '22. En P/E se quita el LTM: la utilidad del primer semestre de 2026 incluye US$135,9 mil millones de ganancias en acciones de otras empresas, que bajan el P/E a 17x. En EV/FCFF y P/FCFE se quita el LTM: el capex de 2026 (US$195-205 mil millones) deja el flujo de caja en mínimos y el múltiplo en ~78x, un pico transitorio frente al flujo de FY+3. B: grandes plataformas tecnológicas (Meta, Microsoft, Amazon, Apple, Netflix), datos de yfinance al 29-sep-2026. Amazon no tiene flujo de caja libre positivo y no entra en los múltiplos de flujo. Sin ajuste: Alphabet crece 24% con margen operativo de 34%, en línea con Meta y Microsoft. λ = 0,25: la Alphabet de FY+3 del escenario Base sigue siendo una plataforma de crecimiento alto con fuerte inversión en IA, parecida a la de hoy.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,3x | 19,7x (n=5: META 17,4x, MSFT 19,7x, AMZN 16,5x, AAPL 28,8x, NFLX 20,1x) × 1,00 = 19,7x | 9,9x / 10,7x / 33,3x | 15,8x | **16,9x** | 25,5x | —x / 13,0x / —x |
| EV/FCFF | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 31,2x (EV/FCF × 1,09 = FCF después de intereses ÷ FCFF) | 40,0x (n=4: META 44,7x, MSFT 55,2x, AAPL 35,3x, NFLX 25,0x) × 1,00 = 40,0x | 25,9x / 27,9x / 89,2x | 28,9x | **33,7x** | 52,2x | —x / 15,4x / —x |
| P/E | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 24,0x | 27,8x (n=5: META 27,8x, MSFT 28,4x, AMZN 19,8x, AAPL 37,7x, NFLX 22,1x) × 1,00 = 27,8x | 20,2x / 21,8x / 58,4x | 22,1x | **24,9x** | 29,0x | —x / 19,0x / —x |
| P/FCFE | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 28,6x | 40,5x (n=4: META 45,9x, MSFT 56,4x, AAPL 35,2x, NFLX 26,2x) × 1,00 = 40,5x | 24,0x / 25,7x / 70,3x | 27,8x | **32,4x** | 51,8x | —x / 16,0x / —x |
| P/OCF | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,6x | 20,7x (n=5: META 14,4x, MSFT 20,7x, AMZN 17,9x, AAPL 32,8x, NFLX 24,5x) × 1,00 = 20,7x | 12,9x / 14,0x / 41,0x | 16,5x | **18,2x** | 23,0x | —x / 11,1x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 16,9x: promedio de historia y peers 19,0x, acercado 25% al justificado (10,7x); rango de anclas 10,7x–19,7x. Atípicos excluidos de la historia: Dec '22 (13,0x: > 2,5x la mediana (1.5x)); Dec '23 (18,3x: > 2,5x la mediana (1.5x)); Dec '24 (18,2x: > 2,5x la mediana (1.5x)); Dec '25 (25,5x: > 2,5x la mediana (1.5x)); LTM (24,8x: > 2,5x la mediana (1.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 33,7x: promedio de historia y peers 35,6x, acercado 25% al justificado (27,9x); rango de anclas 27,9x–40,0x. Atípicos excluidos de la historia: Dec '22 (19,1x: > 2,5x la mediana (1.5x)); Dec '23 (25,3x: > 2,5x la mediana (1.5x)); Dec '24 (32,0x: > 2,5x la mediana (1.5x)); Dec '25 (52,2x: > 2,5x la mediana (1.5x)); LTM (78,4x: > 2,5x la mediana (1.5x)). EV/FCFF: la razón FCF después de intereses ÷ FCFF se fija en 1,09 (mediana de los tres cierres reales); el último cierre da 2,70 porque 'Interest / Other' incluye ganancias en inversiones, no intereses. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 24,9x: promedio de historia y peers 25,9x, acercado 25% al justificado (21,8x); rango de anclas 21,8x–27,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 32,4x: promedio de historia y peers 34,6x, acercado 25% al justificado (25,7x); rango de anclas 25,7x–40,5x. Atípicos excluidos de la historia: Dec '22 (19,0x: > 2,5x la mediana (1.6x)); Dec '23 (25,3x: > 2,5x la mediana (1.6x)); Dec '24 (32,0x: > 2,5x la mediana (1.6x)); Dec '25 (51,8x: > 2,5x la mediana (1.6x)); LTM (78,3x: > 2,5x la mediana (1.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 18,2x: promedio de historia y peers 19,6x, acercado 25% al justificado (14,0x); rango de anclas 14,0x–20,7x. Atípicos excluidos de la historia: Dec '22 (12,5x: > 2,5x la mediana (1.0x)); Dec '23 (17,3x: > 2,5x la mediana (1.0x)); Dec '24 (18,6x: > 2,5x la mediana (1.0x)); Dec '25 (23,0x: > 2,5x la mediana (1.0x)); LTM (22,5x: > 2,5x la mediana (1.0x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$209,76 frente a US$174,29 del DCF (+20%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$209,76 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$204,85 | US$229,92 | US$385,74 |
| EV/EBITDA | 20% | US$233,22 | US$270,78 | US$525,89 |
| EV/FCFF | 10% | US$163,58 | US$207,44 | US$402,98 |
| P/E | 20% | US$267,81 | US$327,22 | US$497,19 |
| P/FCFE | 5% | US$204,82 | US$261,23 | US$554,22 |
| P/OCF | 5% | US$225,87 | US$269,02 | US$423,22 |
| **Ponderado FY+3** | 100% | US$220,04 | US$258,82 | US$448,08 |

Valor presente (Ke 9,67%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$186,36 | US$181,79 | US$176,80 | US$181,65 | OK |
| EV/EBITDA | Base | US$209,20 | US$208,10 | US$205,26 | US$207,52 | OK |
| EV/EBITDA | Optimista | US$328,56 | US$366,97 | US$398,66 | US$364,73 | OK |
| EV/FCFF | Conservador | US$128,52 | US$126,71 | US$124,00 | US$126,41 | OK |
| EV/FCFF | Base | US$147,93 | US$157,60 | US$157,25 | US$154,26 | OK |
| EV/FCFF | Optimista | US$226,22 | US$272,11 | US$305,48 | US$267,94 | OK |
| P/E | Conservador | US$206,86 | US$204,98 | US$203,02 | US$204,95 | OK |
| P/E | Base | US$243,83 | US$246,75 | US$248,05 | US$246,21 | OK |
| P/E | Optimista | US$297,03 | US$339,40 | US$376,90 | US$337,78 | OK |
| P/FCFE | Conservador | US$155,13 | US$155,67 | US$155,26 | US$155,35 | OK |
| P/FCFE | Base | US$187,08 | US$194,94 | US$198,03 | US$193,35 | OK |
| P/FCFE | Optimista | US$309,03 | US$370,28 | US$420,13 | US$366,48 | OK |
| P/OCF | Conservador | US$172,61 | US$172,22 | US$171,22 | US$172,02 | OK |
| P/OCF | Base | US$194,98 | US$202,23 | US$203,93 | US$200,38 | OK |
| P/OCF | Optimista | US$251,59 | US$288,40 | US$320,83 | US$286,94 | OK |

Múltiplos consolidados hoy: US$177,22 / US$209,76 / US$333,28 · DCF hoy: US$155,29 / US$174,29 / US$292,41 · Ponderado hoy: US$168,44 / US$195,57 / US$316,93 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para GOOG la diferencia es de +20% (múltiplos por encima del DCF). Los múltiplos (US$209,76 hoy) quedan 20% por encima del DCF (US$174,29), dentro del rango de ±25%: ambos métodos coinciden razonablemente. Los dos quedan muy por debajo del precio (US$339,16): el mercado descuenta más crecimiento de Cloud e IA que el escenario Base, y además las participaciones de Alphabet en otras empresas (que generaron US$135,9 mil millones de ganancias en el 1S26) no están en los múltiplos operativos; conviene revisar que la hoja las incluya a valor actual como activos no operativos.

## 7. Sensibilidad del valor ponderado hoy (Base)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$195,57 | — |
| Múltiplos Base +20% | US$220,61 | +12,8% |
| Múltiplos Base −20% | US$170,54 | −12,8% |
| Crecimiento años 1-5 +2 pp | US$203,02 | +3,8% |
| Crecimiento años 1-5 −2 pp | US$188,83 | −3,4% |
| Margen objetivo +3 pp | US$201,55 | +3,1% |
| Margen objetivo −3 pp | US$189,59 | −3,1% |
| WACC +1 pp | US$191,82 | −1,9% |
| WACC −1 pp | US$199,59 | +2,1% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 1-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 15,79 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 12,98 | 16,93 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 25,46 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 28,93 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 15,44 | 33,70 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 52,19 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 22,10 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 19,01 | 24,89 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 29,03 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 27,76 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 16,02 | 32,36 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 51,77 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 16,48 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 11,09 | 18,22 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 23,03 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/GOOG_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1yt2zqdGz1JWEqV3SYqqL-nHarO7C1Oud1lvR3pY9i0U/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (META, MSFT, AMZN, AAPL, NFLX).
- [Alphabet, 8-K 2T26: ganancias en acciones y capex](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm)
- [Yahoo Finance: Alphabet sube el capex a US$205 mil millones y el flujo de caja se vuelve negativo](https://finance.yahoo.com/markets/stocks/articles/alphabet-lifts-capex-205-billion-123356486.html)

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
