---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de BOSTON SCIENTIFIC CORP"
ticker: "BSX"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1LVn63SMyvovWzNjbF5Jdi-v0EFUPXLqp4A6n8gwbKHc/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# BOSTON SCIENTIFIC CORP (BSX) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$36,40 en el escenario Base (rango US$24,74–US$49,34). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$38,61 (+6% frente al DCF). Con los pesos de la categoría «Crecimiento» (60% DCF, 40% múltiplos), el ponderado hoy (lectura secundaria) es US$37,28. El valor intrínseco es el DCF: US$36,40 frente a un precio de referencia de US$44,11 (−17%).

Revisión del 30-sep-2026 (tasa de impuestos): la tasa efectiva de los años 1-5 pasa de 5% (LTM, con beneficios fiscales de una vez) a 17,8% (promedio 2023-2025). El DCF da US$36,39 y los múltiplos US$38,61 hoy (6% por encima): ambos métodos coinciden y quedan por debajo del precio (US$44,11). Alpha Spread da ~US$102-112 porque usa un múltiplo de salida de 23,1x EV/EBIT, margen ajustado de ~28% y una tasa de 7,8%; con criterio Damodaran se mantienen los supuestos de la hoja. Revisión anterior: Revisión del 30-sep-2026: el ROIC terminal de 11,1% se revirtió porque BSX no cumple la regla del prompt. Incluida la plusvalía de sus compras, su ROIC estuvo por debajo del costo de capital hasta 2025, así que el DCF vuelve a suponer que después del año 10 gana solo su costo de capital: US$39,13. Los múltiplos ajustan los peers por el crecimiento de 7% de FY+3 y dejan fuera el justificado: dan US$42,83, 9% por encima del DCF, dentro del rango de ±25%. Los dos métodos rodean el precio (~US$44): el mercado ya descuenta la desaceleración de 2026 y paga algo por la recuperación de Watchman y electrofisiología.

| Escenario | DCF hoy (valor intrínseco) | Múltiplos consolidados hoy (secundario) | Ponderado hoy (secundario) | Compra con MOS sobre el DCF | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$24,74 | US$29,26 | US$26,55 | US$16,08 | US$33,78 |
| Base | US$36,40 | US$38,61 | US$37,28 | US$23,66 | US$49,03 |
| Optimista | US$49,34 | US$53,14 | US$50,86 | US$32,07 | US$68,50 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - BSX](https://docs.google.com/spreadsheets/d/1LVn63SMyvovWzNjbF5Jdi-v0EFUPXLqp4A6n8gwbKHc/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$44,11.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 4,0% | 7,0% | 10,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 4,0% | 7,0% | 10,0% | Input B29 |
| Margen EBIT objetivo | 20,0% | 24,0% | 27,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,30 / 1,20 | — | Input B32/B33 |
| DCF por acción hoy | US$24,74 | US$36,40 | US$49,34 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,00, ERP 4,46%, Ke 9,45%, costo de la deuda después de impuestos 4,76%, peso del patrimonio 86,6%, WACC inicial 8,82% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Boston Scientific cotizaba a 25-55x EBITDA mientras crecía 12-20% orgánico. En 2026 la empresa bajó su guía de crecimiento orgánico a 6,5-8% (desde 10-11%, frente a 19,5% en 2025), las ventas de Watchman se estancaron y un ciberataque en agosto la llevó a retirar su guía; la acción cayó ~50% en el año. La etapa actual es solo el LTM. B: medtech diversificada de gran capitalización (Medtronic, Stryker, Abbott, Edwards, Intuitive Surgical, Zimmer Biomet), datos de yfinance al 29-sep-2026. Ajuste −5%: tras la baja de guía, Boston Scientific crece como la mediana de los peers, pero con más incertidumbre de ejecución (Watchman, electrofisiología en EE. UU. y los efectos del ciberataque). λ = 0 (30-sep-2026): el justificado C supone que el ROE de FY+3 se mantiene para siempre, mientras que el DCF supone que después del año 10 el retorno sobre el capital baja al costo de capital (BSX no cumple la regla del ROIC terminal). C se deja fuera del Base y se conserva como referencia en la tabla.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana LTM (etapa actual) = 13,5x | 16,6x (n=6: MDT 12,9x, SYK 15,9x, ABT 17,3x, EW 23,3x, ISRG 33,8x, ZBH 9,8x) × 0,95 = 10,3x | 19,4x / 24,8x / 33,7x | 10,3x | **11,9x** | 14,6x | 14,9x / 17,2x / 21,0x |
| EV/FCFF | mediana LTM (etapa actual) = 19,6x (EV/FCF × 0,95 = FCF después de intereses ÷ FCFF) | 25,1x (n=6: MDT 20,1x, SYK 23,8x, ABT 26,3x, EW 32,5x, ISRG 43,9x, ZBH 15,1x) × 0,95 = 16,4x | 25,0x / 31,6x / 42,9x | 15,8x | **18,0x** | 21,6x | 22,1x / 25,0x / 29,6x |
| P/E | mediana LTM (etapa actual) = 17,9x | 30,8x (n=6: MDT 21,5x, SYK 28,9x, ABT 32,7x, EW 52,4x, ISRG 47,3x, ZBH 22,2x) × 0,95 = 23,6x | 15,5x / 19,3x / 25,1x | 17,9x | **20,8x** | 25,8x | 19,3x / 22,5x / 27,9x |
| P/FCFE | mediana LTM (etapa actual) = 17,6x | 23,2x (n=6: MDT 18,2x, SYK 22,7x, ABT 23,7x, EW 35,4x, ISRG 45,8x, ZBH 12,4x) × 0,95 = 14,3x | 22,1x / 27,2x / 35,1x | 14,1x | **15,9x** | 19,6x | 19,1x / 21,6x / 26,6x |
| P/OCF | mediana LTM (etapa actual) = 14,1x | 18,9x (n=6: MDT 13,9x, SYK 19,4x, ABT 18,5x, EW 29,5x, ISRG 39,8x, ZBH 10,0x) × 0,95 = 11,4x | 19,7x / 26,1x / 35,7x | 10,8x | **12,7x** | 16,1x | 15,8x / 18,5x / 23,4x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 11,9x: promedio de historia y peers 11,9x, acercado 0% al justificado (24,8x); rango de anclas 10,3x–24,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 18,0x: promedio de historia y peers 18,0x, acercado 0% al justificado (31,6x); rango de anclas 16,4x–31,6x. Atípicos excluidos de la historia: Dec '18 (-9.307,0x: métrica negativa o ~0); LTM (20,7x: < 0,4x la mediana (52.0x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 20,8x: promedio de historia y peers 20,8x, acercado 0% al justificado (19,3x); rango de anclas 17,9x–23,6x. Atípicos excluidos de la historia: Dec '20 (-599,2x: métrica negativa o ~0); Dec '17 (354,1x: > 2,5x la mediana (55.6x)); Dec '19 (13,6x: < 0,4x la mediana (55.6x), caída puntual); LTM (17,9x: < 0,4x la mediana (55.6x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 15,9x: promedio de historia y peers 15,9x, acercado 0% al justificado (27,2x); rango de anclas 14,3x–27,2x. Atípicos excluidos de la historia: Dec '18 (-8.155,3x: métrica negativa o ~0); LTM (17,6x: < 0,4x la mediana (46.1x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 12,7x: promedio de historia y peers 12,7x, acercado 0% al justificado (26,1x); rango de anclas 11,4x–26,1x. Atípicos excluidos de la historia: Dec '18 (157,8x: > 2,5x la mediana (33.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$38,61 frente a US$36,40 del DCF (+6%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$38,61 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$32,44 | US$47,71 | US$64,68 |
| EV/EBITDA | 10% | US$33,89 | US$48,91 | US$72,05 |
| EV/FCFF | 15% | US$35,76 | US$51,20 | US$73,47 |
| P/E | 5% | US$38,17 | US$54,19 | US$78,91 |
| P/FCFE | 5% | US$39,05 | US$55,93 | US$83,35 |
| P/OCF | 5% | US$34,01 | US$46,61 | US$67,05 |
| **Ponderado FY+3** | 100% | US$33,78 | US$49,03 | US$68,50 |

Valor presente (Ke 9,45%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$29,45 | US$27,48 | US$25,85 | US$27,59 | OK |
| EV/EBITDA | Base | US$36,15 | US$37,25 | US$37,30 | US$36,90 | OK |
| EV/EBITDA | Optimista | US$47,31 | US$52,38 | US$54,95 | US$51,55 | OK |
| EV/FCFF | Conservador | US$31,32 | US$29,06 | US$27,27 | US$29,22 | OK |
| EV/FCFF | Base | US$37,40 | US$38,84 | US$39,05 | US$38,43 | OK |
| EV/FCFF | Optimista | US$46,94 | US$52,96 | US$56,03 | US$51,98 | OK |
| P/E | Conservador | US$33,24 | US$31,11 | US$29,11 | US$31,15 | OK |
| P/E | Base | US$39,81 | US$41,39 | US$41,33 | US$40,85 | OK |
| P/E | Optimista | US$50,76 | US$57,28 | US$60,19 | US$56,08 | OK |
| P/FCFE | Conservador | US$34,63 | US$31,96 | US$29,78 | US$32,13 | OK |
| P/FCFE | Base | US$43,08 | US$43,29 | US$42,66 | US$43,01 | OK |
| P/FCFE | Optimista | US$57,69 | US$61,76 | US$63,57 | US$61,01 | OK |
| P/OCF | Conservador | US$30,10 | US$27,82 | US$25,94 | US$27,95 | OK |
| P/OCF | Base | US$36,01 | US$36,12 | US$35,55 | US$35,89 | OK |
| P/OCF | Optimista | US$46,30 | US$49,65 | US$51,14 | US$49,03 | OK |

Múltiplos consolidados hoy: US$29,26 / US$38,61 / US$53,14 · DCF hoy: US$24,74 / US$36,40 / US$49,34 · Ponderado hoy: US$26,55 / US$37,28 / US$50,86 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para BSX la diferencia es de +6% (múltiplos por encima del DCF). Revisión del 30-sep-2026 (tasa de impuestos): la tasa efectiva de los años 1-5 pasa de 5% (LTM, con beneficios fiscales de una vez) a 17,8% (promedio 2023-2025). El DCF da US$36,39 y los múltiplos US$38,61 hoy (6% por encima): ambos métodos coinciden y quedan por debajo del precio (US$44,11). Alpha Spread da ~US$102-112 porque usa un múltiplo de salida de 23,1x EV/EBIT, margen ajustado de ~28% y una tasa de 7,8%; con criterio Damodaran se mantienen los supuestos de la hoja. Revisión anterior: Revisión del 30-sep-2026: el ROIC terminal de 11,1% se revirtió porque BSX no cumple la regla del prompt. Incluida la plusvalía de sus compras, su ROIC estuvo por debajo del costo de capital hasta 2025, así que el DCF vuelve a suponer que después del año 10 gana solo su costo de capital: US$39,13. Los múltiplos ajustan los peers por el crecimiento de 7% de FY+3 y dejan fuera el justificado: dan US$42,83, 9% por encima del DCF, dentro del rango de ±25%. Los dos métodos rodean el precio (~US$44): el mercado ya descuenta la desaceleración de 2026 y paga algo por la recuperación de Watchman y electrofisiología.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$44,11 supone que los ingresos crecen 10,7% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 7,0% (+3,7 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$47,71 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,4%, WACC de los años 4-10 8,9%, ROE de FY+3 19,2% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 11,9x | 11,6x | +3% | 2,2% | 2,0% | +0,1 pp | Coherente con el DCF. |
| EV/FCFF | 18,0x | 17,0x | +7% | 3,2% | 2,8% | +0,3 pp | Coherente con el DCF. |
| P/E | 20,8x | 18,3x | +14% | 5,9% | 5,3% | +0,6 pp | Coherente con el DCF. |
| P/FCFE | 15,9x | 13,6x | +17% | 3,0% | 2,0% | +1,0 pp | Coherente con el DCF. |
| P/OCF | 12,7x | 13,0x | −2% | 1,8% | 1,9% | −0,2 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$37,28 | — |
| Múltiplos Base +20% | US$40,68 | +9,1% |
| Múltiplos Base −20% | US$33,88 | −9,1% |
| Crecimiento años 1-5 +2 pp | US$39,69 | +6,5% |
| Crecimiento años 1-5 −2 pp | US$35,09 | −5,9% |
| Margen objetivo +3 pp | US$40,69 | +9,1% |
| Margen objetivo −3 pp | US$33,87 | −9,1% |
| WACC +1 pp | US$35,83 | −3,9% |
| WACC −1 pp | US$38,83 | +4,2% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Margen objetivo −3 pp, Múltiplos Base +20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 14,92 | 10,33 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 17,18 | 11,89 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 21,03 | 14,56 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 22,13 | 15,79 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 25,01 | 18,03 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 29,58 | 21,59 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 19,33 | 17,86 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 22,50 | 20,79 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 27,91 | 25,79 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 19,08 | 14,06 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 21,65 | 15,95 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 26,64 | 19,63 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 15,75 | 10,81 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 18,53 | 12,72 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 23,44 | 16,09 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/BSX_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1LVn63SMyvovWzNjbF5Jdi-v0EFUPXLqp4A6n8gwbKHc/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (MDT, SYK, ABT, EW, ISRG, ZBH).
- [Motley Fool, 29-may-2026: por qué caía Boston Scientific](https://www.fool.com/investing/2026/05/29/why-boston-scientific-stock-was-sliding-this-week/)
- [Nasdaq: ciberataque y guía 2026 débil](https://www.nasdaq.com/articles/cyberattack-weak-2026-outlook-weigh-bsx-stock-sell)
- [TIKR: BSX cae tras el impacto del ciberataque](https://www.tikr.com/blog/boston-scientific-bsx-stock-falls-cyberattack-sales-profit-impact)

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
