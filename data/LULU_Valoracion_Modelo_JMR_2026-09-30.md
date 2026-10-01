---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de lululemon athletica inc."
ticker: "LULU"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1Skav94fUb3IYvhsucWI1MQAcN6LH-VQ87Z_7KCImu3g/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# lululemon athletica inc. (LULU) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$188,95 por acción.** Complemento: DCF esperado por probabilidades US$164,39; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$85,51–US$247,76; precio con MOS 30% sobre el esperado: US$115,07; precio de referencia US$96,32. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$183,65), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Se estabiliza Américas y crece lo internacional** (valor principal) | 40% | US$188,95 | US$75,58 |
| Conservadora · Pérdida estructural frente a Alo y Vuori | 35% | US$123,14 | US$43,10 |
| Disrupción · Deterioro de los fundamentales: Moda que pasa: declive de la marca | 10% | US$85,51 | US$8,55 |
| Optimista · La marca se recupera | 15% | US$247,76 | US$37,16 |
| **DCF esperado (complemento)** | 100% | **US$164,39** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$167,44 por acción y los múltiplos, US$107,52 hoy: 36% por debajo del DCF, fuera del rango de ±25%. Es un desacuerdo de historia, no una inconsistencia: el DCF supone que la marca se estabiliza y el mercado la paga como una marca que sigue perdiendo clientas (~6x EBITDA). El DCF se lee como el valor si se cumple la estabilización.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$188,95 | US$119,46 | US$147,25 | US$115,07 | US$193,47 |
| Conservador | US$123,14 | US$98,82 | US$108,55 | US$115,07 | US$133,28 |
| Optimista | US$247,76 | US$143,27 | US$185,07 | US$115,07 | US$254,18 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - LULU - 2026-09-16 (Valoración completa)](https://docs.google.com/spreadsheets/d/1Skav94fUb3IYvhsucWI1MQAcN6LH-VQ87Z_7KCImu3g/edit).
- Análisis del 16 de sept de 2026. Precio de referencia de la hoja: US$96,32.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -10,0% | -6,0% | -3,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 0,0% | 4,0% | 7,0% | Input B29 |
| Margen EBIT objetivo | 16,5% | 20,0% | 22,5% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 6 | 6 | 6 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,77 / 1,80 | — | Input B32/B33 |
| DCF por acción hoy | US$123,14 | US$188,95 | US$247,76 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,75%, beta apalancada 1,20, ERP 4,14%, Ke 9,72%, costo de la deuda después de impuestos 4,50%, peso del patrimonio 86,1%, WACC inicial 8,99% y terminal 8,98%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Lululemon cotizó a 15-40x EBITDA mientras crecía 15-30% al año. En 2026 guió una caída de ventas de 5-7% (US$10.350-10.500 millones), recortó la utilidad por acción a US$9,48-9,73 por aranceles y menor demanda en EE. UU., y cambió de CEO (Heidi O'Neill desde septiembre); la acción cayó 20% tras el 2T. La etapa actual es el cierre Feb '26 y el LTM. Antes el múltiplo Base se había calibrado al DCF; ahora sale de las tres anclas. B: ropa y calzado deportivo (Nike, Deckers, Adidas, Birkenstock), datos de yfinance al 29-sep-2026. Se excluyen Under Armour (con pérdidas, EV/EBITDA inflado) y On Holding (crece 14% con múltiplos de crecimiento que no comparan con una Lululemon que decrece). Ajuste −10%: Lululemon decrece 5-7% en 2026 mientras la mediana de los peers crece ~6-13%, y está en transición de CEO. λ = 0,25: la Lululemon de FY+3 del escenario Base es una marca madura de crecimiento bajo, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Feb '26, LTM (etapa actual) = 5,8x | 11,1x (n=4: NKE 11,2x, DECK 7,1x, ADDYY 12,7x, BIRK 11,0x) × 0,90 = 10,0x | 7,4x / 6,3x / 8,7x | **7,8x** | 6,9x | 8,6x | 8,0x / 6,0x / 11,0x |
| EV/FCFF | mediana Feb '26, LTM (etapa actual) = 15,0x (EV/FCF × 1,02 = FCF después de intereses ÷ FCFF) | 18,7x (n=4: NKE 25,3x, DECK 8,4x, ADDYY 18,0x, BIRK 19,5x) × 0,90 = 16,9x | 18,2x / 15,0x / 21,6x | **16,5x** | 13,4x | 19,3x | 18,0x / 12,0x / 25,0x |
| P/E | mediana Feb '26, LTM (etapa actual) = 10,7x | 16,6x (n=4: NKE 17,1x, DECK 11,0x, ADDYY 18,6x, BIRK 16,2x) × 0,90 = 15,0x | 14,1x / 12,1x / 16,4x | **13,2x** | 11,6x | 14,6x | 15,0x / 10,0x / 20,0x |
| P/FCFE | mediana Feb '26, LTM (etapa actual) = 14,5x | 17,3x (n=4: NKE 24,3x, DECK 9,5x, ADDYY 15,8x, BIRK 18,7x) × 0,90 = 15,5x | 16,1x / 13,5x / 18,7x | **15,3x** | 12,4x | 18,1x | 15,0x / 10,0x / 20,0x |
| P/OCF | mediana Feb '26, LTM (etapa actual) = 8,8x | 13,1x (n=4: NKE 18,5x, DECK 8,9x, ADDYY 12,5x, BIRK 13,6x) × 0,90 = 11,8x | 10,0x / 7,4x / 12,6x | **10,2x** | 8,3x | 12,2x | 12,0x / 8,0x / 16,0x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 7,8x: promedio de historia y peers 7,9x, acercado 25% al justificado (7,4x); rango de anclas 5,8x–10,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 16,5x: promedio de historia y peers 15,9x, acercado 25% al justificado (18,2x); rango de anclas 15,0x–18,2x. Atípicos excluidos de la historia: Jan '23 (115,0x: > 2,5x la mediana (33.0x)); LTM (8,6x: < 0,4x la mediana (33.0x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 13,2x: promedio de historia y peers 12,8x, acercado 25% al justificado (14,1x); rango de anclas 10,7x–15,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 15,3x: promedio de historia y peers 15,0x, acercado 25% al justificado (16,1x); rango de anclas 14,5x–16,1x. Atípicos excluidos de la historia: Jan '23 (115,9x: > 2,5x la mediana (35.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 10,2x: promedio de historia y peers 10,3x, acercado 25% al justificado (10,0x); rango de anclas 8,8x–11,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$119,46 frente a US$188,95 del DCF (−37%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$119,46 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$249,56 | US$162,64 | US$327,24 |
| EV/EBITDA | 25% | US$162,66 | US$115,00 | US$214,00 |
| EV/FCFF | 15% | US$149,10 | US$112,95 | US$194,93 |
| P/E | 5% | US$161,60 | US$111,54 | US$214,98 |
| P/FCFE | 10% | US$144,82 | US$109,58 | US$191,11 |
| P/OCF | 5% | US$161,13 | US$119,87 | US$213,76 |
| **Ponderado FY+3** | 100% | US$193,47 | US$133,28 | US$254,18 |

Valor presente (Ke 9,72%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$122,88 | US$124,49 | US$123,15 | US$123,51 | OK |
| EV/EBITDA | Conservador | US$105,34 | US$94,87 | US$87,07 | US$95,76 | OK |
| EV/EBITDA | Optimista | US$142,36 | US$156,56 | US$162,03 | US$153,65 | OK |
| EV/FCFF | Base | US$118,64 | US$113,22 | US$112,89 | US$114,92 | OK |
| EV/FCFF | Conservador | US$124,10 | US$99,63 | US$85,52 | US$103,08 | OK |
| EV/FCFF | Optimista | US$111,23 | US$131,27 | US$147,58 | US$130,03 | OK |
| P/E | Base | US$120,16 | US$123,05 | US$122,35 | US$121,85 | OK |
| P/E | Conservador | US$102,76 | US$92,16 | US$84,45 | US$93,12 | OK |
| P/E | Optimista | US$138,74 | US$155,86 | US$162,77 | US$152,46 | OK |
| P/FCFE | Base | US$115,35 | US$110,17 | US$109,65 | US$111,72 | OK |
| P/FCFE | Conservador | US$119,46 | US$96,38 | US$82,96 | US$99,60 | OK |
| P/FCFE | Optimista | US$110,40 | US$129,41 | US$144,69 | US$128,17 | OK |
| P/OCF | Base | US$131,13 | US$124,57 | US$121,99 | US$125,90 | OK |
| P/OCF | Conservador | US$122,81 | US$102,95 | US$90,76 | US$105,50 | OK |
| P/OCF | Optimista | US$141,70 | US$152,87 | US$161,84 | US$152,14 | OK |

Múltiplos consolidados hoy: US$119,46 / US$98,82 / US$143,27 · DCF de las historias hoy: US$188,95 / US$123,14 / US$247,76 · Ponderado hoy: US$147,25 / US$108,55 / US$185,07 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para LULU la diferencia es de −37% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$167,44 por acción y los múltiplos, US$107,52 hoy: 36% por debajo del DCF, fuera del rango de ±25%. Es un desacuerdo de historia, no una inconsistencia: el DCF supone que la marca se estabiliza y el mercado la paga como una marca que sigue perdiendo clientas (~6x EBITDA). El DCF se lee como el valor si se cumple la estabilización.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$96,32 supone que los ingresos crecen -13,8% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 2,0% (−15,8 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$249,56 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,7%, WACC de los años 4-10 9,0%, ROE de FY+3 27,6% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 7,8x | 11,2x | −35% | 3,5% | 5,1% | −1,6 pp | Revisar: el múltiplo vale 35% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 16,5x | 25,8x | −40% | 2,7% | 4,9% | −2,2 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 40% por debajo del DCF en FY+3. |
| P/E | 13,2x | 20,3x | −35% | 2,7% | 5,6% | −2,9 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 35% por debajo del DCF en FY+3. |
| P/FCFE | 15,3x | 26,3x | −42% | 3,0% | 5,7% | −2,7 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 42% por debajo del DCF en FY+3. |
| P/OCF | 10,2x | 15,8x | −35% | 3,4% | 5,6% | −2,1 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 35% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$147,25 | — |
| Múltiplos Base +20% | US$161,78 | +9,9% |
| Múltiplos Base −20% | US$132,72 | −9,9% |
| Crecimiento años 2-5 +2 pp | US$150,60 | +2,3% |
| Crecimiento años 2-5 −2 pp | US$140,14 | −4,8% |
| Margen objetivo +3 pp | US$155,80 | +5,8% |
| Margen objetivo −3 pp | US$134,46 | −8,7% |
| WACC +1 pp | US$141,11 | −4,2% |
| WACC −1 pp | US$149,44 | +1,5% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo −3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 6,00 | 6,88 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 8,00 | 7,78 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 11,00 | 8,63 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 12,00 | 13,44 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 18,00 | 16,48 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 25,00 | 19,30 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 10,00 | 11,56 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 15,00 | 13,15 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 20,00 | 14,58 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 10,00 | 12,43 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 15,00 | 15,29 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 20,00 | 18,12 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 8,00 | 8,31 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 12,00 | 10,20 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 16,00 | 12,19 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/LULU_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1Skav94fUb3IYvhsucWI1MQAcN6LH-VQ87Z_7KCImu3g/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (NKE, DECK, ONON, ADDYY, UAA, BIRK).
- [CNBC, 3-sep-2026: Lululemon cae 20% por resultados y guía](https://www.cnbc.com/2026/09/03/lululemon-lulu-q2-2026-earnings.html)
- [Quartz: Lululemon recorta su guía anual](https://qz.com/lululemon-full-year-guidance-cut-product-sales-060526)

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
