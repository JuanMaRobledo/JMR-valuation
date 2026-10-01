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

**Valor intrínseco principal: DCF esperado de las cuatro historias, US$443,39.** Historia central A: US$513,26; rango US$208,84–US$631,82; precio con MOS 35% sobre el esperado: US$288,20; precio de referencia US$274,77. Cada historia es un DCF completo (hoja «Escenarios e historias»); el detalle está en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son la calibración técnica anterior de la hoja (Base US$496,56) y los múltiplos y el ponderado son lecturas secundarias.


| Historia | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| A · La IA es palanca de monetización | 45% | US$513,26 | US$230,97 |
| B · La IA erosiona impuestos y contabilidad básica | 25% | US$260,68 | US$65,17 |
| C · Tesis de disrupción · Deterioro de los fundamentales: Recesión y declaración gratuita del Estado | 10% | US$208,84 | US$20,88 |
| D · Plataforma financiera de la pyme | 20% | US$631,82 | US$126,36 |
| **DCF esperado** | 100% | **US$443,39** | |

Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$496,45 por acción y los múltiplos, US$386,84 hoy: 22% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

| Escenario | DCF técnico anterior hoy (calibración) | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$373,70 | US$312,01 | US$349,02 | US$288,20 | US$460,28 |
| Base | US$496,56 | US$389,03 | US$453,55 | US$288,20 | US$609,47 |
| Optimista | US$734,72 | US$560,42 | US$665,00 | US$288,20 | US$914,66 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - INTU](https://docs.google.com/spreadsheets/d/14sbZoheKmtK5UpMOlRNzvqD1F9sCJEpHW01g4f-X8mM/edit).
- Revisión 28 de septiembre de 2026 (análisis original 25 de septiembre). Precio de referencia de la hoja: US$274,77.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 6,0% | 9,1% | 14,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 6,0% | 9,0% | 14,0% | Input B29 |
| Margen EBIT objetivo | 28,2% | 32,2% | 36,2% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,31 / 1,88 | — | Input B32/B33 |
| DCF por acción hoy | US$373,70 | US$496,56 | US$734,72 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,20, ERP 4,46%, Ke 10,34%, costo de la deuda después de impuestos 4,53%, peso del patrimonio 91,2%, WACC inicial 9,83% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

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

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$389,03 frente a US$496,56 del DCF (−22%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$389,03 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$502,33 | US$667,50 | US$987,66 |
| EV/EBITDA | 10% | US$462,67 | US$622,03 | US$978,38 |
| EV/FCFF | 15% | US$379,76 | US$490,36 | US$761,08 |
| P/E | 5% | US$398,10 | US$515,52 | US$777,74 |
| P/FCFE | 5% | US$364,80 | US$489,26 | US$742,26 |
| P/OCF | 5% | US$349,97 | US$459,55 | US$681,40 |
| **Ponderado FY+3** | 100% | US$460,28 | US$609,47 | US$914,66 |

Valor presente (Ke 10,34%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$388,92 | US$361,41 | US$344,39 | US$364,91 | OK |
| EV/EBITDA | Base | US$466,74 | US$464,20 | US$463,01 | US$464,65 | OK |
| EV/EBITDA | Optimista | US$632,31 | US$685,94 | US$728,26 | US$682,17 | OK |
| EV/FCFF | Conservador | US$317,26 | US$295,62 | US$282,68 | US$298,52 | OK |
| EV/FCFF | Base | US$366,34 | US$364,98 | US$365,00 | US$365,44 | OK |
| EV/FCFF | Optimista | US$491,53 | US$533,09 | US$566,51 | US$530,38 | OK |
| P/E | Conservador | US$331,43 | US$309,61 | US$296,32 | US$312,45 | OK |
| P/E | Base | US$380,67 | US$382,27 | US$383,73 | US$382,22 | OK |
| P/E | Optimista | US$491,92 | US$541,03 | US$578,91 | US$537,29 | OK |
| P/FCFE | Conservador | US$300,65 | US$282,32 | US$271,54 | US$284,83 | OK |
| P/FCFE | Base | US$363,12 | US$362,91 | US$364,18 | US$363,40 | OK |
| P/FCFE | Optimista | US$479,90 | US$519,50 | US$552,50 | US$517,30 | OK |
| P/OCF | Conservador | US$288,80 | US$270,88 | US$260,50 | US$273,39 | OK |
| P/OCF | Base | US$340,35 | US$340,60 | US$342,06 | US$341,01 | OK |
| P/OCF | Optimista | US$437,13 | US$475,58 | US$507,20 | US$473,30 | OK |

Múltiplos consolidados hoy: US$312,01 / US$389,03 / US$560,42 · DCF hoy: US$373,70 / US$496,56 / US$734,72 · Ponderado hoy: US$349,02 / US$453,55 / US$665,00 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para INTU la diferencia es de −22% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$496,45 por acción y los múltiplos, US$386,84 hoy: 22% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$274,77 supone que los ingresos crecen -1,9% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 9,0% (−10,9 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$667,50 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,3%, WACC de los años 4-10 9,5%, ROE de FY+3 35,3% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 17,0x | 18,3x | −7% | 4,7% | 5,0% | −0,3 pp | Coherente con el DCF. |
| EV/FCFF | 17,2x | 23,7x | −27% | 3,5% | 5,0% | −1,6 pp | Revisar: el múltiplo vale 27% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 20,3x | 26,5x | −23% | 6,0% | 7,1% | −1,1 pp | Coherente con el DCF. |
| P/FCFE | 15,4x | 21,3x | −27% | 3,6% | 5,4% | −1,8 pp | Revisar: el múltiplo vale 27% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 15,6x | 22,9x | −31% | 3,1% | 5,4% | −2,2 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 31% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$453,55 | — |
| Múltiplos Base +20% | US$483,89 | +6,7% |
| Múltiplos Base −20% | US$423,21 | −6,7% |
| Crecimiento años 2-5 +2 pp | US$481,51 | +6,2% |
| Crecimiento años 2-5 −2 pp | US$427,98 | −5,6% |
| Margen objetivo +3 pp | US$480,80 | +6,0% |
| Margen objetivo −3 pp | US$426,31 | −6,0% |
| WACC +1 pp | US$436,92 | −3,7% |
| WACC −1 pp | US$471,37 | +3,9% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 2-5 +2 pp.

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
