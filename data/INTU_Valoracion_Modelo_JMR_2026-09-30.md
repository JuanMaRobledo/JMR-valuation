---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de INTUIT INC."
ticker: "INTU"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/14sbZoheKmtK5UpMOlRNzvqD1F9sCJEpHW01g4f-X8mM/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# INTUIT INC. (INTU) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$351,86 en el escenario Base (rango US$267,20–US$508,06). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$386,84 (+10% frente al DCF). Con los pesos de la categoría «Software» (60% DCF, 40% múltiplos), el valor intrínseco ponderado hoy es US$365,85, frente a un precio de referencia de US$269,40 (+36%).

Los múltiplos (US$386,84 hoy) quedan 10% por encima del DCF (US$351,86), dentro del rango de ±25%: ambos métodos coinciden. Los múltiplos ya usan la valoración de la etapa actual (~12x EBITDA, ~18x utilidad), con el temor a la IA agéntica incorporado, y los peers de software lo suben un poco.

| Escenario | DCF hoy | Múltiplos consolidados hoy | Valor intrínseco ponderado hoy | Compra con MOS hoy | Precio objetivo FY+3 ponderado |
|---|---:|---:|---:|---:|---:|
| Conservador | US$267,20 | US$309,33 | US$284,05 | US$184,63 | US$372,91 |
| Base | US$351,86 | US$386,84 | US$365,85 | US$237,80 | US$491,77 |
| Optimista | US$508,06 | US$557,16 | US$527,70 | US$343,01 | US$729,88 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - INTU](https://docs.google.com/spreadsheets/d/14sbZoheKmtK5UpMOlRNzvqD1F9sCJEpHW01g4f-X8mM/edit).
- Revisión 28 de septiembre de 2026 (análisis original 25 de septiembre). Precio de referencia de la hoja: US$269,40.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 6,0% | 9,1% | 14,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 6,0% | 9,0% | 14,0% | Input B29 |
| Margen EBIT objetivo | 28,0% | 32,0% | 36,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,50 / 2,00 | — | Input B32/B33 |
| DCF por acción hoy | US$267,20 | US$351,86 | US$508,06 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,20, ERP 4,46%, Ke 10,34%, costo de la deuda después de impuestos 4,53%, peso del patrimonio 91,1%, WACC inicial 9,82% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Intuit cotizó a 30-51x EBITDA y 44-70x utilidades mientras crecía 12-20% con TurboTax, Credit Karma y QuickBooks. En 2026 el mercado empezó a temer que los agentes de IA hagan el trabajo de impuestos y contabilidad por el que cobra; recortó la guía de TurboTax, anunció una reestructuración y su guía FY27 (9-10% de crecimiento, TurboTax 2-3%) decepcionó. La acción cayó ~60% desde su máximo. La etapa actual es el cierre Jul '26 y el LTM. B: software de aplicaciones y nómina/finanzas (Adobe, Autodesk, Salesforce, Workday, ADP, Paychex), datos de yfinance al 29-sep-2026. Sin ajuste: Intuit crece 9-10% con márgenes altos, en línea con la mediana de los peers. λ = 0,25: la Intuit de FY+3 del escenario Base crece al ~10%, parecida a la de hoy.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Jul '26, LTM (etapa actual) = 12,3x | 16,7x (n=6: ADBE 9,3x, ADSK 18,4x, CRM 16,9x, WDAY 29,0x, ADP 16,4x, PAYX 12,7x) × 1,00 = 16,7x | 19,3x / 24,6x / 43,8x | 14,5x | **17,0x** | 22,1x | —x / 13,1x / —x |
| EV/FCFF | mediana Jul '26, LTM (etapa actual) = 9,5x (EV/FCF × 1,02 = FCF después de intereses ÷ FCFF) | 15,2x (n=6: ADBE 8,5x, ADSK 15,0x, CRM 13,8x, WDAY 15,7x, ADP 20,5x, PAYX 15,4x) × 1,00 = 15,2x | 25,1x / 31,8x / 56,4x | 15,4x | **17,2x** | 22,0x | —x / 17,4x / —x |
| P/E | mediana Jul '26, LTM (etapa actual) = 18,0x | 22,3x (n=6: ADBE 13,0x, ADSK 26,3x, CRM 20,6x, WDAY 38,8x, ADP 23,9x, PAYX 19,7x) × 1,00 = 22,3x | 17,1x / 20,8x / 32,0x | 18,1x | **20,3x** | 25,2x | —x / 18,6x / —x |
| P/FCFE | mediana Jul '26, LTM (etapa actual) = 9,1x | 15,2x (n=6: ADBE 8,8x, ADSK 15,1x, CRM 12,2x, WDAY 16,0x, ADP 21,7x, PAYX 15,2x) × 1,00 = 15,2x | 20,8x / 25,2x / 38,7x | 13,6x | **15,4x** | 18,6x | —x / 15,4x / —x |
| P/OCF | mediana Jul '26, LTM (etapa actual) = 9,0x | 14,2x (n=6: ADBE 8,6x, ADSK 14,7x, CRM 11,8x, WDAY 14,8x, ADP 19,1x, PAYX 13,8x) × 1,00 = 14,2x | 21,9x / 27,4x / 43,9x | 13,6x | **15,6x** | 19,0x | —x / 16,2x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 17,0x: promedio de historia y peers 14,5x, acercado 25% al justificado (24,6x); rango de anclas 12,3x–24,6x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 17,2x: promedio de historia y peers 12,3x, acercado 25% al justificado (31,8x); rango de anclas 9,5x–31,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 20,3x: promedio de historia y peers 20,1x, acercado 25% al justificado (20,8x); rango de anclas 17,9x–22,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 15,4x: promedio de historia y peers 12,2x, acercado 25% al justificado (25,2x); rango de anclas 9,2x–25,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 15,6x: promedio de historia y peers 11,6x, acercado 25% al justificado (27,4x); rango de anclas 9,0x–27,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$386,84 frente a US$351,86 del DCF (+10%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$386,84 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$358,97 | US$472,71 | US$682,56 |
| EV/EBITDA | 10% | US$457,75 | US$618,34 | US$971,21 |
| EV/FCFF | 15% | US$375,33 | US$486,97 | US$755,07 |
| P/E | 5% | US$395,71 | US$514,36 | US$773,61 |
| P/FCFE | 5% | US$365,23 | US$492,38 | US$747,42 |
| P/OCF | 5% | US$348,17 | US$458,66 | US$678,29 |
| **Ponderado FY+3** | 100% | US$372,91 | US$491,77 | US$729,88 |

Valor presente (Ke 10,34%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$384,71 | US$357,48 | US$340,72 | US$360,97 | OK |
| EV/EBITDA | Base | US$462,12 | US$460,78 | US$460,26 | US$461,05 | OK |
| EV/EBITDA | Optimista | US$626,81 | US$680,54 | US$722,92 | US$676,76 | OK |
| EV/FCFF | Conservador | US$313,44 | US$292,07 | US$279,38 | US$294,96 | OK |
| EV/FCFF | Base | US$362,28 | US$361,89 | US$362,48 | US$362,22 | OK |
| EV/FCFF | Optimista | US$486,84 | US$528,52 | US$562,04 | US$525,80 | OK |
| P/E | Conservador | US$329,52 | US$307,76 | US$294,55 | US$310,61 | OK |
| P/E | Base | US$378,47 | US$380,96 | US$382,86 | US$380,76 | OK |
| P/E | Optimista | US$489,07 | US$538,07 | US$575,84 | US$534,33 | OK |
| P/FCFE | Conservador | US$300,99 | US$282,65 | US$271,86 | US$285,17 | OK |
| P/FCFE | Base | US$364,50 | US$364,92 | US$366,50 | US$365,31 | OK |
| P/FCFE | Optimista | US$483,47 | US$523,20 | US$556,34 | US$521,00 | OK |
| P/OCF | Conservador | US$287,36 | US$269,49 | US$259,16 | US$272,01 | OK |
| P/OCF | Base | US$338,66 | US$339,60 | US$341,40 | US$339,89 | OK |
| P/OCF | Optimista | US$434,97 | US$473,34 | US$504,88 | US$471,06 | OK |

Múltiplos consolidados hoy: US$309,33 / US$386,84 / US$557,16 · DCF hoy: US$267,20 / US$351,86 / US$508,06 · Ponderado hoy: US$284,05 / US$365,85 / US$527,70 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para INTU la diferencia es de +10% (múltiplos por encima del DCF). Los múltiplos (US$386,84 hoy) quedan 10% por encima del DCF (US$351,86), dentro del rango de ±25%: ambos métodos coinciden. Los múltiplos ya usan la valoración de la etapa actual (~12x EBITDA, ~18x utilidad), con el temor a la IA agéntica incorporado, y los peers de software lo suben un poco.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$269,40 supone que los ingresos crecen 3,8% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 9,0% (−5,2 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Crecimiento perpetuo después de FY+3 que supone cada múltiplo Base, con Ke 10,3%, WACC de los años 4-10 9,5% y ROE de FY+3 35,3%, frente al crecimiento del DCF (6,1%: punto medio entre los años 4-10 y la perpetuidad):

| Múltiplo Base FY+3 | Múltiplo | Crecimiento implícito | Diferencia vs. DCF | Lectura |
|---|---:|---:|---:|---|
| EV/EBITDA | 17,0x | 4,7% | −1,4 pp | Coherente con el DCF. |
| EV/FCFF | 17,2x | 3,5% | −2,7 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. |
| P/E | 20,3x | 6,0% | −0,1 pp | Coherente con el DCF. |
| P/FCFE | 15,4x | 3,6% | −2,5 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. |
| P/OCF | 15,6x | 3,1% | −3,0 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. |

Más de 2 pp de diferencia significa que el múltiplo (o el precio) cuenta otra historia de crecimiento que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (subir el crecimiento del DCF si la evidencia lo sostiene, o acercar el múltiplo al justificado si no).

## 7. Sensibilidad del valor ponderado hoy (Base)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$365,85 | — |
| Múltiplos Base +20% | US$396,12 | +8,3% |
| Múltiplos Base −20% | US$335,58 | −8,3% |
| Crecimiento años 1-5 +2 pp | US$388,51 | +6,2% |
| Crecimiento años 1-5 −2 pp | US$345,37 | −5,6% |
| Margen objetivo +3 pp | US$385,07 | +5,3% |
| Margen objetivo −3 pp | US$346,64 | −5,3% |
| WACC +1 pp | US$354,46 | −3,1% |
| WACC −1 pp | US$378,05 | +3,3% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 1-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 14,54 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 13,11 | 16,99 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 22,08 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 15,39 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 17,37 | 17,21 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 21,99 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 18,15 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 18,58 | 20,30 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 25,18 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 13,60 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 15,43 | 15,43 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 18,58 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 13,62 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 16,23 | 15,56 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 19,04 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/INTU_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/14sbZoheKmtK5UpMOlRNzvqD1F9sCJEpHW01g4f-X8mM/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (ADBE, ADSK, CRM, WDAY, ADP, PAYX).
- [Motley Fool, 26-ago-2026: por qué cayó Intuit](https://www.fool.com/investing/2026/08/26/why-intuit-stock-dropped-today/)
- [Intuit: resultados FY26 y guía FY27](https://investors.intuit.com/news-events/press-releases/detail/1320/intuit-reports-fourth-quarter-and-full-year-fiscal-2026-results-sets-fiscal-2027-guidance)
- [Yahoo Finance: Intuit se desplomó por el temor a la IA agéntica](https://finance.yahoo.com/markets/stocks/articles/intuit-crashed-over-agentic-ai-132427512.html)

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
