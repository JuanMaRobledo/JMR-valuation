---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Microsoft Corporation"
ticker: "MSFT"
analysis_date: "2026-09-29"
sheet: "https://docs.google.com/spreadsheets/d/1ubjlRP0jbGmG_sXEoTrvonRkwqy5AoOd1ESrU4c3-rY/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Microsoft Corporation (MSFT) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$329,42 en el escenario Base (rango US$263,31–US$386,35). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$437,36 (+33% frente al DCF). Con los pesos de la categoría «Software» (60% DCF, 40% múltiplos), el valor intrínseco ponderado hoy es US$372,59, frente a un precio de referencia de US$509,22 (−27%).

Los múltiplos (US$437,36 hoy) quedan 33% por encima del DCF (US$329,42). Los múltiplos suponen que Microsoft conserva a FY+3 una valoración parecida a la de sus últimos cinco años (~22x EBITDA, ~32x utilidad, ajustada por los peers), mientras que el DCF carga el capex de US$190 mil millones de 2026 contra el flujo de caja y usa un WACC de ~9,4%. El precio (US$509,22) está por encima de ambos. El DCF parece conservador frente a la aceleración de Azure (~40%) y conviene revisar su crecimiento y su reinversión; los múltiplos están más cerca de lo que paga el mercado.

| Escenario | DCF hoy | Múltiplos consolidados hoy | Valor intrínseco ponderado hoy | Compra con MOS hoy | Precio objetivo FY+3 ponderado |
|---|---:|---:|---:|---:|---:|
| Conservador | US$263,31 | US$322,80 | US$287,11 | US$186,62 | US$381,31 |
| Base | US$329,42 | US$437,36 | US$372,59 | US$242,19 | US$505,58 |
| Optimista | US$386,35 | US$569,86 | US$459,75 | US$298,84 | US$631,98 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - Valoración MSFT - 2026-09-16](https://docs.google.com/spreadsheets/d/1ubjlRP0jbGmG_sXEoTrvonRkwqy5AoOd1ESrU4c3-rY/edit).
- Análisis del 16 de sept de 2026. Precio de referencia de la hoja: US$509,22.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 14,0% | 16,5% | 19,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 8,0% | 12,0% | 14,0% | Input B29 |
| Margen EBIT objetivo | 42,0% | 45,0% | 48,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 0,65 / 1,00 | — | Input B32/B33 |
| DCF por acción hoy | US$263,31 | US$329,42 | US$386,35 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,25%, beta apalancada 1,34, ERP 4,46%, Ke 10,23%, costo de la deuda después de impuestos 4,15%, peso del patrimonio 99,0%, WACC inicial 10,17% y terminal 8,48%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Sin cambio de etapa: Microsoft sigue creciendo a doble dígito y cotiza por debajo de su promedio de cinco años; se usa la mediana de los últimos 5 cierres + LTM. Se excluye la columna sin fecha de la hoja. B: grandes plataformas tecnológicas y de software (Alphabet, Apple, Amazon, Oracle, Meta, Salesforce), datos de yfinance al 29-sep-2026. Amazon y Oracle no tienen flujo de caja libre positivo y no entran en los múltiplos de flujo. Ajuste +5%: Microsoft tiene el margen operativo más alto del grupo (45% frente a ~33%) y Azure acelera (~40%) con una cartera de US$678 mil millones. λ = 0,25: la Microsoft de FY+3 del escenario Base es una plataforma de crecimiento de dos dígitos, parecida a la de hoy.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana de los últimos 5 cierres + LTM depurados = 22,1x | 17,1x (n=6: GOOG 23,2x, AAPL 28,8x, AMZN 16,5x, ORCL 15,6x, META 17,4x, CRM 16,9x) × 1,05 = 18,0x | 9,4x / 13,1x / 16,9x | 15,7x | **18,3x** | 22,5x | —x / —x / —x |
| EV/FCFF | mediana de los últimos 5 cierres + LTM depurados = 42,8x (EV/FCF × 0,98 = FCF después de intereses ÷ FCFF) | 40,0x (n=4: GOOG 73,1x, AAPL 35,3x, META 44,7x, CRM 13,8x) × 1,05 = 42,0x | 25,5x / 35,7x / 44,4x | 30,0x | **40,7x** | 48,6x | —x / —x / —x |
| P/E | mediana de los últimos 5 cierres + LTM depurados = 31,8x | 21,1x (n=6: GOOG 16,9x, AAPL 37,7x, AMZN 19,8x, ORCL 21,6x, META 27,8x, CRM 20,6x) × 1,05 = 22,2x | 18,2x / 23,7x / 28,2x | 22,3x | **26,2x** | 30,9x | —x / —x / —x |
| P/FCFE | mediana de los últimos 5 cierres + LTM depurados = 44,2x | 40,5x (n=4: GOOG 77,4x, AAPL 35,2x, META 45,9x, CRM 12,2x) × 1,05 = 42,6x | 21,4x / 28,2x / 33,5x | 29,8x | **39,6x** | 46,9x | —x / —x / —x |
| P/OCF | mediana de los últimos 5 cierres + LTM depurados = 24,3x | 16,2x (n=6: GOOG 22,2x, AAPL 32,8x, AMZN 17,9x, ORCL 8,9x, META 14,4x, CRM 11,8x) × 1,05 = 17,0x | 10,0x / 13,7x / 17,0x | 14,8x | **18,9x** | 23,1x | —x / —x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 18,3x: promedio de historia y peers 20,0x, acercado 25% al justificado (13,1x); rango de anclas 13,1x–22,1x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 40,7x: promedio de historia y peers 42,4x, acercado 25% al justificado (35,7x); rango de anclas 35,7x–42,8x. Atípicos excluidos de la historia: ninguno. EV/FCFF: la razón FCF después de intereses ÷ FCFF se fija en 0,98 (mediana de los tres cierres reales); el último cierre da 1,28 porque 'Interest / Other' incluye partidas no operativas. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 26,2x: promedio de historia y peers 27,0x, acercado 25% al justificado (23,7x); rango de anclas 22,2x–31,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 39,6x: promedio de historia y peers 43,4x, acercado 25% al justificado (28,2x); rango de anclas 28,2x–44,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 18,9x: promedio de historia y peers 20,7x, acercado 25% al justificado (13,7x); rango de anclas 13,7x–24,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$437,36 frente a US$329,42 del DCF (+33%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$437,36 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$352,72 | US$441,27 | US$517,52 |
| EV/EBITDA | 10% | US$510,86 | US$673,57 | US$900,69 |
| EV/FCFF | 15% | US$366,76 | US$554,50 | US$746,48 |
| P/E | 5% | US$481,55 | US$644,55 | US$836,74 |
| P/FCFE | 5% | US$382,57 | US$585,00 | US$787,23 |
| P/OCF | 5% | US$407,48 | US$576,17 | US$764,64 |
| **Ponderado FY+3** | 100% | US$381,31 | US$505,58 | US$631,98 |

Valor presente (Ke 10,23%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$394,15 | US$387,41 | US$381,37 | US$387,64 | OK |
| EV/EBITDA | Base | US$479,25 | US$491,68 | US$502,84 | US$491,25 | OK |
| EV/EBITDA | Optimista | US$612,14 | US$644,02 | US$672,39 | US$642,85 | OK |
| EV/FCFF | Conservador | US$285,51 | US$277,22 | US$273,80 | US$278,84 | OK |
| EV/FCFF | Base | US$384,07 | US$402,11 | US$413,95 | US$400,04 | OK |
| EV/FCFF | Optimista | US$487,12 | US$528,02 | US$557,26 | US$524,13 | OK |
| P/E | Conservador | US$378,29 | US$367,11 | US$359,49 | US$368,30 | OK |
| P/E | Base | US$465,35 | US$472,46 | US$481,18 | US$473,00 | OK |
| P/E | Optimista | US$575,36 | US$600,21 | US$624,65 | US$600,07 | OK |
| P/FCFE | Conservador | US$307,98 | US$288,67 | US$285,60 | US$294,08 | OK |
| P/FCFE | Base | US$415,68 | US$423,73 | US$436,72 | US$425,37 | OK |
| P/FCFE | Optimista | US$528,71 | US$556,70 | US$587,69 | US$557,70 | OK |
| P/OCF | Conservador | US$312,94 | US$307,42 | US$304,19 | US$308,19 | OK |
| P/OCF | Base | US$404,61 | US$418,87 | US$430,13 | US$417,87 | OK |
| P/OCF | Optimista | US$513,40 | US$544,80 | US$570,82 | US$543,01 | OK |

Múltiplos consolidados hoy: US$322,80 / US$437,36 / US$569,86 · DCF hoy: US$263,31 / US$329,42 / US$386,35 · Ponderado hoy: US$287,11 / US$372,59 / US$459,75 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para MSFT la diferencia es de +33% (múltiplos por encima del DCF). Los múltiplos (US$437,36 hoy) quedan 33% por encima del DCF (US$329,42). Los múltiplos suponen que Microsoft conserva a FY+3 una valoración parecida a la de sus últimos cinco años (~22x EBITDA, ~32x utilidad, ajustada por los peers), mientras que el DCF carga el capex de US$190 mil millones de 2026 contra el flujo de caja y usa un WACC de ~9,4%. El precio (US$509,22) está por encima de ambos. El DCF parece conservador frente a la aceleración de Azure (~40%) y conviene revisar su crecimiento y su reinversión; los múltiplos están más cerca de lo que paga el mercado.

## 7. Sensibilidad del valor ponderado hoy (Base)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$372,59 | — |
| Múltiplos Base +20% | US$406,74 | +9,2% |
| Múltiplos Base −20% | US$338,45 | −9,2% |
| Crecimiento años 1-5 +2 pp | US$390,28 | +4,7% |
| Crecimiento años 1-5 −2 pp | US$356,51 | −4,3% |
| Margen objetivo +3 pp | US$387,37 | +4,0% |
| Margen objetivo −3 pp | US$357,82 | −4,0% |
| WACC +1 pp | US$361,40 | −3,0% |
| WACC −1 pp | US$384,60 | +3,2% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 1-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 15,69 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | — | 18,31 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 22,51 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 30,01 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | — | 40,73 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 48,65 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 22,32 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | — | 26,16 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 30,91 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 29,78 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | — | 39,60 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 46,85 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 14,79 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | — | 18,93 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 23,10 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/MSFT_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1ubjlRP0jbGmG_sXEoTrvonRkwqy5AoOd1ESrU4c3-rY/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (GOOG, AAPL, AMZN, ORCL, META, CRM).
- [CNBC, 29-jul-2026: resultados 4T FY26 de Microsoft](https://www.cnbc.com/2026/07/29/microsoft-msft-q4-earnings-report-2026.html)
- [CNBC, 29-abr-2026: Microsoft proyecta US$190 mil millones de capex](https://www.cnbc.com/2026/04/29/microsoft-msft-q3-earnings-report-2026.html)

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
