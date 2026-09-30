---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de NIKE, Inc."
ticker: "NKE"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1BAuhp8QPzXQx1osCIBHA4QoFC91DStgSr3h4SjFkAL4/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# NIKE, Inc. (NKE) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$29,76 en el escenario Base (rango US$16,19–US$40,30). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$36,79 (+24% frente al DCF). Con los pesos de la categoría «Madura» (40% DCF, 60% múltiplos), el ponderado hoy (lectura secundaria) es US$33,98. El valor intrínseco es el DCF: US$29,76 frente a un precio de referencia de US$36,39 (−18%).

Los múltiplos (US$36,79 hoy) quedan 24% por encima del DCF (US$29,76), en el límite del rango de ±25%. Los múltiplos suponen que a FY+3 el mercado sigue pagando por Nike cerca de lo que paga hoy en plena reestructuración (~15x EBITDA, ~22x utilidad), mientras que el DCF refleja una recuperación lenta de ventas y márgenes. Si la recuperación se demora más (China, inventarios), el DCF es la referencia más prudente.

| Escenario | DCF hoy (valor intrínseco) | Múltiplos consolidados hoy (secundario) | Ponderado hoy (secundario) | Compra con MOS sobre el DCF | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$16,19 | US$24,07 | US$20,92 | US$10,52 | US$26,68 |
| Base | US$29,76 | US$36,79 | US$33,98 | US$19,34 | US$47,01 |
| Optimista | US$40,30 | US$49,21 | US$45,65 | US$26,19 | US$64,94 |

## 2. Datos

- Hoja del modelo: [Modelo_JMR_Plantilla_Maestra NKE (automático)](https://docs.google.com/spreadsheets/d/1BAuhp8QPzXQx1osCIBHA4QoFC91DStgSr3h4SjFkAL4/edit).
- Análisis del 22 de sept de 2026. Precio de referencia de la hoja: US$36,39.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -3,0% | -2,0% | 4,5% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | -3,0% | 3,5% | 4,5% | Input B29 |
| Margen EBIT objetivo | 6,5% | 11,0% | 13,4% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,10 / 2,10 | — | Input B32/B33 |
| DCF por acción hoy | US$16,19 | US$29,76 | US$40,30 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,96%, beta apalancada 1,00, ERP 4,32%, Ke 9,27%, costo de la deuda después de impuestos 4,30%, peso del patrimonio 86,6%, WACC inicial 8,60% y terminal 9,05%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Nike cotizó a 20-42x EBITDA mientras crecía y ganaba margen con la venta directa. Desde FY25 está en reestructuración: las ventas cayeron ~10% en FY25 y quedaron planas en FY26 (US$46.400 millones, −2% sin efecto cambiario), China cae 12% y el CEO Elliott Hill reconoce que la recuperación toma más de lo esperado. La etapa actual es May '25, May '26 y el LTM. B: ropa y calzado deportivo (Adidas, Lululemon, Deckers, On Holding), datos de yfinance al 29-sep-2026. Se excluyen Under Armour y VF Corp (margen operativo negativo; sus múltiplos no comparan). Sin ajuste: Nike es la marca más grande del sector, pero hoy no crece; queda entre On/Adidas (crecen) y Lululemon (decrece). λ = 0,25: la Nike de FY+3 del escenario Base es una marca madura en recuperación lenta, parecida a la de hoy.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana May '25, May '26, LTM (etapa actual) = 15,5x | 9,9x (n=4: ADDYY 12,7x, LULU 5,0x, DECK 7,1x, ONON 19,1x) × 1,00 = 9,9x | 11,9x / 16,4x / 17,7x | 10,4x | **13,6x** | 16,7x | —x / 15,5x / —x |
| EV/FCFF | mediana May '25, May '26, LTM (etapa actual) = 29,9x (EV/FCF × 1,07 = FCF después de intereses ÷ FCFF) | 13,4x (n=4: ADDYY 18,0x, LULU 8,8x, DECK 8,4x, ONON 20,9x) × 1,00 = 13,4x | 16,8x / 24,6x / 26,4x | 17,1x | **22,4x** | 26,5x | —x / 22,6x / —x |
| P/E | mediana May '25, May '26, LTM (etapa actual) = 22,0x | 14,8x (n=4: ADDYY 18,6x, LULU 8,0x, DECK 11,0x, ONON 20,8x) × 1,00 = 14,8x | 12,9x / 17,8x / 19,6x | 14,1x | **18,3x** | 21,5x | —x / 22,0x / —x |
| P/FCFE | mediana May '25, May '26, LTM (etapa actual) = 27,6x | 12,6x (n=4: ADDYY 15,8x, LULU 7,9x, DECK 9,5x, ONON 23,0x) × 1,00 = 12,6x | 15,6x / 22,1x / 23,6x | 16,3x | **20,6x** | 24,2x | 10,1x / 17,9x / 19,5x |
| P/OCF | mediana May '25, May '26, LTM (etapa actual) = 23,9x | 10,7x (n=4: ADDYY 12,5x, LULU 5,4x, DECK 8,9x, ONON 18,8x) × 1,00 = 10,7x | 11,2x / 20,7x / 22,8x | 13,2x | **18,1x** | 20,7x | —x / 19,2x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 13,6x: promedio de historia y peers 12,7x, acercado 25% al justificado (16,4x); rango de anclas 9,9x–16,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 22,4x: promedio de historia y peers 21,6x, acercado 25% al justificado (24,6x); rango de anclas 13,4x–29,9x. Atípicos excluidos de la historia: May '20 (114,7x: > 2,5x la mediana (32.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 18,3x: promedio de historia y peers 18,4x, acercado 25% al justificado (17,8x); rango de anclas 14,8x–22,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 20,6x: promedio de historia y peers 20,1x, acercado 25% al justificado (22,1x); rango de anclas 12,6x–27,6x. Atípicos excluidos de la historia: May '20 (112,2x: > 2,5x la mediana (31.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 18,1x: promedio de historia y peers 17,3x, acercado 25% al justificado (20,7x); rango de anclas 10,7x–23,9x. Atípicos excluidos de la historia: May '20 (63,1x: > 2,5x la mediana (24.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$36,79 frente a US$29,76 del DCF (+24%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$36,79 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$21,12 | US$38,82 | US$52,58 |
| EV/EBITDA | 20% | US$29,12 | US$50,01 | US$71,28 |
| EV/FCFF | 10% | US$33,09 | US$54,23 | US$75,38 |
| P/E | 20% | US$28,82 | US$50,33 | US$69,76 |
| P/FCFE | 5% | US$31,66 | US$61,61 | US$86,29 |
| P/OCF | 5% | US$34,97 | US$58,25 | US$77,03 |
| **Ponderado FY+3** | 100% | US$26,68 | US$47,01 | US$64,94 |

Valor presente (Ke 9,27%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$24,25 | US$23,25 | US$22,32 | US$23,27 | OK |
| EV/EBITDA | Base | US$31,86 | US$36,53 | US$38,33 | US$35,57 | OK |
| EV/EBITDA | Optimista | US$41,45 | US$50,83 | US$54,63 | US$48,97 | OK |
| EV/FCFF | Conservador | US$28,11 | US$26,70 | US$25,37 | US$26,72 | OK |
| EV/FCFF | Base | US$36,35 | US$39,26 | US$41,57 | US$39,06 | OK |
| EV/FCFF | Optimista | US$40,97 | US$52,92 | US$57,78 | US$50,56 | OK |
| P/E | Conservador | US$22,81 | US$22,42 | US$22,09 | US$22,44 | OK |
| P/E | Base | US$29,43 | US$35,50 | US$38,58 | US$34,51 | OK |
| P/E | Optimista | US$36,52 | US$47,80 | US$53,47 | US$45,93 | OK |
| P/FCFE | Conservador | US$25,40 | US$24,87 | US$24,27 | US$24,84 | OK |
| P/FCFE | Base | US$32,94 | US$44,13 | US$47,22 | US$41,43 | OK |
| P/FCFE | Optimista | US$47,58 | US$60,14 | US$66,14 | US$57,96 | OK |
| P/OCF | Conservador | US$28,46 | US$27,64 | US$26,80 | US$27,63 | OK |
| P/OCF | Base | US$38,45 | US$41,83 | US$44,65 | US$41,65 | OK |
| P/OCF | Optimista | US$42,82 | US$53,75 | US$59,04 | US$51,87 | OK |

Múltiplos consolidados hoy: US$24,07 / US$36,79 / US$49,21 · DCF hoy: US$16,19 / US$29,76 / US$40,30 · Ponderado hoy: US$20,92 / US$33,98 / US$45,65 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NKE la diferencia es de +24% (múltiplos por encima del DCF). Los múltiplos (US$36,79 hoy) quedan 24% por encima del DCF (US$29,76), en el límite del rango de ±25%. Los múltiplos suponen que a FY+3 el mercado sigue pagando por Nike cerca de lo que paga hoy en plena reestructuración (~15x EBITDA, ~22x utilidad), mientras que el DCF refleja una recuperación lenta de ventas y márgenes. Si la recuperación se demora más (China, inventarios), el DCF es la referencia más prudente.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$36,39 supone que los ingresos crecen 8,3% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 2,4% (+5,9 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Crecimiento perpetuo después de FY+3 que supone cada múltiplo Base, con Ke 9,3%, WACC de los años 4-10 8,8% y ROE de FY+3 23,0%, frente al crecimiento del DCF (4,5%: punto medio entre los años 4-10 y la perpetuidad):

| Múltiplo Base FY+3 | Múltiplo | Crecimiento implícito | Diferencia vs. DCF | Lectura |
|---|---:|---:|---:|---|
| EV/EBITDA | 13,6x | 3,7% | −0,8 pp | Coherente con el DCF. |
| EV/FCFF | 22,4x | 4,1% | −0,4 pp | Coherente con el DCF. |
| P/E | 18,3x | 4,7% | +0,2 pp | Coherente con el DCF. |
| P/FCFE | 20,6x | 4,2% | −0,3 pp | Coherente con el DCF. |
| P/OCF | 18,1x | 3,9% | −0,6 pp | Coherente con el DCF. |

Más de 2 pp de diferencia significa que el múltiplo (o el precio) cuenta otra historia de crecimiento que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (subir el crecimiento del DCF si la evidencia lo sostiene, o acercar el múltiplo al justificado si no).

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$33,98 | — |
| Múltiplos Base +20% | US$38,07 | +12,0% |
| Múltiplos Base −20% | US$29,89 | −12,0% |
| Crecimiento años 1-5 +2 pp | US$34,76 | +2,3% |
| Crecimiento años 1-5 −2 pp | US$33,26 | −2,1% |
| Margen objetivo +3 pp | US$37,39 | +10,0% |
| Margen objetivo −3 pp | US$30,57 | −10,0% |
| WACC +1 pp | US$33,37 | −1,8% |
| WACC −1 pp | US$34,63 | +1,9% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 10,39 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 15,51 | 13,62 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 16,72 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 17,06 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 22,64 | 22,37 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 26,48 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 14,05 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 22,03 | 18,26 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 21,49 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 10,14 | 16,26 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 17,93 | 20,61 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 19,46 | 24,25 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 13,18 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 19,23 | 18,15 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 20,74 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/NKE_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1BAuhp8QPzXQx1osCIBHA4QoFC91DStgSr3h4SjFkAL4/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (ADDYY, LULU, DECK, ONON, UAA, VFC).
- [Nike: resultados FY26](https://about.nike.com/en/newsroom/releases/nike-inc-reports-fiscal-2026-fourth-quarter-and-full-year-results)
- [CNBC, 30-jun-2026: Nike supera estimados pero China cae 12%](https://www.cnbc.com/2026/06/30/nike-nke-q4-2026-earnings.html)

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
