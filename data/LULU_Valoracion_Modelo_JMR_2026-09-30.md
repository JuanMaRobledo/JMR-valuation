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

**Valor intrínseco principal: DCF esperado de las cuatro historias, US$163,26.** Historia central A: US$187,28; rango US$86,06–US$244,99; precio con MOS 30% sobre el esperado: US$114,28; precio de referencia US$96,32. Cada historia es un DCF completo (hoja «Escenarios e historias»); el detalle está en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son la calibración técnica anterior de la hoja (Base US$182,25) y los múltiplos y el ponderado son lecturas secundarias.


| Historia | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| A · Se estabiliza Américas y crece lo internacional | 40% | US$187,28 | US$74,91 |
| B · Pérdida estructural frente a Alo y Vuori | 35% | US$122,83 | US$42,99 |
| C · Tesis de disrupción · Deterioro de los fundamentales: Moda que pasa: declive de la marca | 10% | US$86,06 | US$8,61 |
| D · La marca se recupera | 15% | US$244,99 | US$36,75 |
| **DCF esperado** | 100% | **US$163,26** | |

Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$167,44 por acción y los múltiplos, US$107,52 hoy: 36% por debajo del DCF, fuera del rango de ±25%. Es un desacuerdo de historia, no una inconsistencia: el DCF supone que la marca se estabiliza y el mercado la paga como una marca que sigue perdiendo clientas (~6x EBITDA). El DCF se lee como el valor si se cumple la estabilización.

| Escenario | DCF técnico anterior hoy (calibración) | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$125,29 | US$89,63 | US$103,90 | US$114,28 | US$132,50 |
| Base | US$182,25 | US$127,83 | US$149,60 | US$114,28 | US$194,93 |
| Optimista | US$235,51 | US$154,97 | US$187,19 | US$114,28 | US$251,38 |

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
| Sales-to-capital años 1-5 / 6-10 | — | 1,53 / 1,80 | — | Input B32/B33 |
| DCF por acción hoy | US$125,29 | US$182,25 | US$235,51 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,75%, beta apalancada 1,20, ERP 4,14%, Ke 9,72%, costo de la deuda después de impuestos 4,50%, peso del patrimonio 86,1%, WACC inicial 8,99% y terminal 8,98%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Lululemon cotizó a 15-40x EBITDA mientras crecía 15-30% al año. En 2026 guió una caída de ventas de 5-7% (US$10.350-10.500 millones), recortó la utilidad por acción a US$9,48-9,73 por aranceles y menor demanda en EE. UU., y cambió de CEO (Heidi O'Neill desde septiembre); la acción cayó 20% tras el 2T. La etapa actual es el cierre Feb '26 y el LTM. Antes el múltiplo Base se había calibrado al DCF; ahora sale de las tres anclas. B: ropa y calzado deportivo (Nike, Deckers, Adidas, Birkenstock), datos de yfinance al 29-sep-2026. Se excluyen Under Armour (con pérdidas, EV/EBITDA inflado) y On Holding (crece 14% con múltiplos de crecimiento que no comparan con una Lululemon que decrece). Ajuste −10%: Lululemon decrece 5-7% en 2026 mientras la mediana de los peers crece ~6-13%, y está en transición de CEO. λ = 0,25: la Lululemon de FY+3 del escenario Base es una marca madura de crecimiento bajo, parecida a la de hoy.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Feb '26, LTM (etapa actual) = 5,8x | 11,1x (n=4: NKE 11,2x, DECK 7,1x, ADDYY 12,7x, BIRK 11,0x) × 0,90 = 10,0x | 6,3x / 7,4x / 8,7x | 6,9x | **7,8x** | 8,6x | 6,0x / 8,0x / 11,0x |
| EV/FCFF | mediana Feb '26, LTM (etapa actual) = 15,0x (EV/FCF × 1,02 = FCF después de intereses ÷ FCFF) | 18,7x (n=4: NKE 25,3x, DECK 8,4x, ADDYY 18,0x, BIRK 19,5x) × 0,90 = 16,9x | 15,0x / 18,2x / 21,6x | 13,4x | **16,5x** | 19,3x | 12,0x / 18,0x / 25,0x |
| P/E | mediana Feb '26, LTM (etapa actual) = 10,7x | 16,6x (n=4: NKE 17,1x, DECK 11,0x, ADDYY 18,6x, BIRK 16,2x) × 0,90 = 15,0x | 12,1x / 14,1x / 16,4x | 11,6x | **13,2x** | 14,6x | 10,0x / 15,0x / 20,0x |
| P/FCFE | mediana Feb '26, LTM (etapa actual) = 14,5x | 17,3x (n=4: NKE 24,3x, DECK 9,5x, ADDYY 15,8x, BIRK 18,7x) × 0,90 = 15,5x | 13,5x / 16,1x / 18,7x | 12,4x | **15,3x** | 18,1x | 10,0x / 15,0x / 20,0x |
| P/OCF | mediana Feb '26, LTM (etapa actual) = 8,8x | 13,1x (n=4: NKE 18,5x, DECK 8,9x, ADDYY 12,5x, BIRK 13,6x) × 0,90 = 11,8x | 7,4x / 10,0x / 12,6x | 8,3x | **10,2x** | 12,2x | 8,0x / 12,0x / 16,0x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 7,8x: promedio de historia y peers 7,9x, acercado 25% al justificado (7,4x); rango de anclas 5,8x–10,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 16,5x: promedio de historia y peers 15,9x, acercado 25% al justificado (18,2x); rango de anclas 15,0x–18,2x. Atípicos excluidos de la historia: Jan '23 (115,0x: > 2,5x la mediana (33.0x)); LTM (8,6x: < 0,4x la mediana (33.0x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 13,2x: promedio de historia y peers 12,8x, acercado 25% al justificado (14,1x); rango de anclas 10,7x–15,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 15,3x: promedio de historia y peers 15,0x, acercado 25% al justificado (16,1x); rango de anclas 14,5x–16,1x. Atípicos excluidos de la historia: Jan '23 (115,9x: > 2,5x la mediana (35.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 10,2x: promedio de historia y peers 10,3x, acercado 25% al justificado (10,0x); rango de anclas 8,8x–11,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$127,83 frente a US$182,25 del DCF (−30%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$127,83 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$165,49 | US$240,72 | US$311,06 |
| EV/EBITDA | 25% | US$121,65 | US$174,13 | US$219,88 |
| EV/FCFF | 15% | US$104,71 | US$158,65 | US$204,42 |
| P/E | 5% | US$108,29 | US$167,30 | US$217,16 |
| P/FCFE | 10% | US$92,88 | US$147,39 | US$195,82 |
| P/OCF | 5% | US$109,58 | US$164,17 | US$217,70 |
| **Ponderado FY+3** | 100% | US$132,50 | US$194,93 | US$251,38 |

Valor presente (Ke 9,72%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$101,18 | US$98,17 | US$92,11 | US$97,15 | OK |
| EV/EBITDA | Base | US$132,83 | US$134,88 | US$131,84 | US$133,18 | OK |
| EV/EBITDA | Optimista | US$150,82 | US$163,11 | US$166,47 | US$160,13 | OK |
| EV/FCFF | Conservador | US$102,77 | US$82,92 | US$79,28 | US$88,32 | OK |
| EV/FCFF | Base | US$145,10 | US$120,15 | US$120,12 | US$128,46 | OK |
| EV/FCFF | Optimista | US$160,78 | US$146,21 | US$154,77 | US$153,92 | OK |
| P/E | Conservador | US$82,79 | US$84,26 | US$81,99 | US$83,01 | OK |
| P/E | Base | US$116,94 | US$124,75 | US$126,66 | US$122,78 | OK |
| P/E | Optimista | US$134,17 | US$154,31 | US$164,42 | US$150,97 | OK |
| P/FCFE | Conservador | US$86,99 | US$71,28 | US$70,32 | US$76,20 | OK |
| P/FCFE | Base | US$127,47 | US$108,03 | US$111,59 | US$115,70 | OK |
| P/FCFE | Optimista | US$144,30 | US$135,32 | US$148,26 | US$142,63 | OK |
| P/OCF | Conservador | US$99,29 | US$86,11 | US$82,97 | US$89,46 | OK |
| P/OCF | Base | US$137,76 | US$123,34 | US$124,30 | US$128,47 | OK |
| P/OCF | Optimista | US$162,10 | US$156,09 | US$164,82 | US$161,00 | OK |

Múltiplos consolidados hoy: US$89,63 / US$127,83 / US$154,97 · DCF hoy: US$125,29 / US$182,25 / US$235,51 · Ponderado hoy: US$103,90 / US$149,60 / US$187,19 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para LULU la diferencia es de −30% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$167,44 por acción y los múltiplos, US$107,52 hoy: 36% por debajo del DCF, fuera del rango de ±25%. Es un desacuerdo de historia, no una inconsistencia: el DCF supone que la marca se estabiliza y el mercado la paga como una marca que sigue perdiendo clientas (~6x EBITDA). El DCF se lee como el valor si se cumple la estabilización.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$96,32 supone que los ingresos crecen -14,7% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 2,0% (−16,7 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$240,72 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,7%, WACC de los años 4-10 9,0%, ROE de FY+3 27,6% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 7,8x | 11,0x | −28% | 3,5% | 5,1% | −1,5 pp | Revisar: el múltiplo vale 28% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 16,5x | 25,7x | −34% | 2,7% | 4,9% | −2,1 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 34% por debajo del DCF en FY+3. |
| P/E | 13,2x | 18,9x | −31% | 2,7% | 5,2% | −2,5 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 31% por debajo del DCF en FY+3. |
| P/FCFE | 15,3x | 25,0x | −39% | 3,0% | 5,5% | −2,5 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 39% por debajo del DCF en FY+3. |
| P/OCF | 10,2x | 15,0x | −32% | 3,4% | 5,3% | −1,9 pp | Revisar: el múltiplo vale 32% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$149,60 | — |
| Múltiplos Base +20% | US$164,16 | +9,7% |
| Múltiplos Base −20% | US$135,04 | −9,7% |
| Crecimiento años 2-5 +2 pp | US$154,76 | +3,5% |
| Crecimiento años 2-5 −2 pp | US$144,89 | −3,1% |
| Margen objetivo +3 pp | US$160,27 | +7,1% |
| Margen objetivo −3 pp | US$138,93 | −7,1% |
| WACC +1 pp | US$145,59 | −2,7% |
| WACC −1 pp | US$153,89 | +2,9% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

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
