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

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$39,12 en el escenario Base (rango US$26,90–US$52,67). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$59,06 (+51% frente al DCF). Con los pesos de la categoría «Crecimiento» (60% DCF, 40% múltiplos), el valor intrínseco ponderado hoy es US$47,10, frente a un precio de referencia de US$44,11 (+7%).

Los múltiplos (US$59,06 hoy) quedan 51% por encima del DCF (US$39,12). Los múltiplos suponen que, a FY+3, el mercado vuelve a pagar por Boston Scientific algo parecido a sus peers de medtech (~16x EBITDA, ~22x utilidad); el DCF ya incorpora la desaceleración de 2026 y da un valor incluso menor que el precio. Mientras no se confirme que el crecimiento se recupera (Watchman, electrofisiología) y que el ciberataque fue puntual, el DCF es la referencia más prudente; los múltiplos muestran el potencial si la empresa vuelve a cotizar como sus peers.

| Escenario | DCF hoy | Múltiplos consolidados hoy | Valor intrínseco ponderado hoy | Compra con MOS hoy | Precio objetivo FY+3 ponderado |
|---|---:|---:|---:|---:|---:|
| Conservador | US$26,90 | US$45,19 | US$34,22 | US$22,24 | US$43,25 |
| Base | US$39,12 | US$59,06 | US$47,10 | US$30,61 | US$61,92 |
| Optimista | US$52,67 | US$80,58 | US$63,83 | US$41,49 | US$86,33 |

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
| DCF por acción hoy | US$26,90 | US$39,12 | US$52,67 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,00, ERP 4,46%, Ke 9,45%, costo de la deuda después de impuestos 4,76%, peso del patrimonio 86,7%, WACC inicial 8,82% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Boston Scientific cotizaba a 25-55x EBITDA mientras crecía 12-20% orgánico. En 2026 la empresa bajó su guía de crecimiento orgánico a 6,5-8% (desde 10-11%, frente a 19,5% en 2025), las ventas de Watchman se estancaron y un ciberataque en agosto la llevó a retirar su guía; la acción cayó ~50% en el año. La etapa actual es solo el LTM. B: medtech diversificada de gran capitalización (Medtronic, Stryker, Abbott, Edwards, Intuitive Surgical, Zimmer Biomet), datos de yfinance al 29-sep-2026. Ajuste −5%: tras la baja de guía, Boston Scientific crece como la mediana de los peers, pero con más incertidumbre de ejecución (Watchman, electrofisiología en EE. UU. y los efectos del ciberataque). λ = 0,25: la BSX de FY+3 del escenario Base es una medtech de crecimiento de un dígito alto, parecida a la de hoy.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana LTM (etapa actual) = 13,5x | 16,6x (n=6: MDT 12,9x, SYK 15,9x, ABT 17,3x, EW 23,3x, ISRG 33,8x, ZBH 9,8x) × 0,95 = 15,8x | 19,4x / 24,8x / 33,7x | 14,9x | **17,2x** | 21,0x | 14,9x / 17,2x / 21,0x |
| EV/FCFF | mediana LTM (etapa actual) = 19,6x (EV/FCF × 0,95 = FCF después de intereses ÷ FCFF) | 25,1x (n=6: MDT 20,1x, SYK 23,8x, ABT 26,3x, EW 32,5x, ISRG 43,9x, ZBH 15,1x) × 0,95 = 23,8x | 25,0x / 31,6x / 42,9x | 21,2x | **24,2x** | 29,0x | 22,1x / 25,0x / 29,6x |
| P/E | mediana LTM (etapa actual) = 17,9x | 30,8x (n=6: MDT 21,5x, SYK 28,9x, ABT 32,7x, EW 52,4x, ISRG 47,3x, ZBH 22,2x) × 0,95 = 29,2x | 15,5x / 19,3x / 25,1x | 19,3x | **22,5x** | 27,9x | 19,3x / 22,5x / 27,9x |
| P/FCFE | mediana LTM (etapa actual) = 17,6x | 23,2x (n=6: MDT 18,2x, SYK 22,7x, ABT 23,7x, EW 35,4x, ISRG 45,8x, ZBH 12,4x) × 0,95 = 22,1x | 22,1x / 27,2x / 35,1x | 19,1x | **21,6x** | 26,6x | 19,1x / 21,6x / 26,6x |
| P/OCF | mediana LTM (etapa actual) = 14,1x | 18,9x (n=6: MDT 13,9x, SYK 19,4x, ABT 18,5x, EW 29,5x, ISRG 39,8x, ZBH 10,0x) × 0,95 = 18,0x | 19,7x / 26,1x / 35,7x | 15,8x | **18,5x** | 23,4x | 15,8x / 18,5x / 23,4x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 17,2x: promedio de historia y peers 14,6x, acercado 25% al justificado (24,8x); rango de anclas 13,5x–24,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 24,2x: promedio de historia y peers 21,7x, acercado 25% al justificado (31,6x); rango de anclas 19,6x–31,6x. Atípicos excluidos de la historia: Dec '18 (-9.307,0x: métrica negativa o ~0); LTM (20,7x: < 0,4x la mediana (52.0x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 22,5x: promedio de historia y peers 23,6x, acercado 25% al justificado (19,3x); rango de anclas 17,9x–29,2x. Atípicos excluidos de la historia: Dec '20 (-599,2x: métrica negativa o ~0); Dec '17 (354,1x: > 2,5x la mediana (55.6x)); Dec '19 (13,6x: < 0,4x la mediana (55.6x), caída puntual); LTM (17,9x: < 0,4x la mediana (55.6x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 21,6x: promedio de historia y peers 19,8x, acercado 25% al justificado (27,2x); rango de anclas 17,6x–27,2x. Atípicos excluidos de la historia: Dec '18 (-8.155,3x: métrica negativa o ~0); LTM (17,6x: < 0,4x la mediana (46.1x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 18,5x: promedio de historia y peers 16,0x, acercado 25% al justificado (26,1x); rango de anclas 14,1x–26,1x. Atípicos excluidos de la historia: Dec '18 (157,8x: > 2,5x la mediana (33.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$59,06 frente a US$39,12 del DCF (+51%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$59,06 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$35,28 | US$51,30 | US$69,06 |
| EV/EBITDA | 10% | US$52,22 | US$73,94 | US$107,33 |
| EV/FCFF | 15% | US$58,45 | US$82,32 | US$116,66 |
| P/E | 5% | US$47,74 | US$67,79 | US$98,70 |
| P/FCFE | 5% | US$59,34 | US$84,71 | US$125,80 |
| P/OCF | 5% | US$54,79 | US$75,43 | US$108,85 |
| **Ponderado FY+3** | 100% | US$43,25 | US$61,92 | US$86,33 |

Valor presente (Ke 9,45%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$45,62 | US$42,47 | US$39,83 | US$42,64 | OK |
| EV/EBITDA | Base | US$55,32 | US$56,60 | US$56,39 | US$56,11 | OK |
| EV/EBITDA | Optimista | US$71,41 | US$78,43 | US$81,86 | US$77,23 | OK |
| EV/FCFF | Conservador | US$51,32 | US$47,61 | US$44,58 | US$47,84 | OK |
| EV/FCFF | Base | US$60,71 | US$62,72 | US$62,78 | US$62,07 | OK |
| EV/FCFF | Optimista | US$75,36 | US$84,49 | US$88,97 | US$82,94 | OK |
| P/E | Conservador | US$41,57 | US$38,91 | US$36,41 | US$38,97 | OK |
| P/E | Base | US$49,79 | US$51,78 | US$51,70 | US$51,09 | OK |
| P/E | Optimista | US$63,49 | US$71,65 | US$75,28 | US$70,14 | OK |
| P/FCFE | Conservador | US$52,53 | US$48,55 | US$45,26 | US$48,78 | OK |
| P/FCFE | Base | US$64,93 | US$65,48 | US$64,61 | US$65,01 | OK |
| P/FCFE | Optimista | US$86,46 | US$93,03 | US$95,95 | US$91,81 | OK |
| P/OCF | Conservador | US$48,41 | US$44,81 | US$41,79 | US$45,00 | OK |
| P/OCF | Base | US$57,98 | US$58,36 | US$57,53 | US$57,96 | OK |
| P/OCF | Optimista | US$74,64 | US$80,43 | US$83,02 | US$79,36 | OK |

Múltiplos consolidados hoy: US$45,19 / US$59,06 / US$80,58 · DCF hoy: US$26,90 / US$39,12 / US$52,67 · Ponderado hoy: US$34,22 / US$47,10 / US$63,83 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para BSX la diferencia es de +51% (múltiplos por encima del DCF). Los múltiplos (US$59,06 hoy) quedan 51% por encima del DCF (US$39,12). Los múltiplos suponen que, a FY+3, el mercado vuelve a pagar por Boston Scientific algo parecido a sus peers de medtech (~16x EBITDA, ~22x utilidad); el DCF ya incorpora la desaceleración de 2026 y da un valor incluso menor que el precio. Mientras no se confirme que el crecimiento se recupera (Watchman, electrofisiología) y que el ciberataque fue puntual, el DCF es la referencia más prudente; los múltiplos muestran el potencial si la empresa vuelve a cotizar como sus peers.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$44,11 supone que los ingresos crecen 9,3% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 7,0% (+2,3 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Crecimiento perpetuo después de FY+3 que supone cada múltiplo Base, con Ke 9,4%, WACC de los años 4-10 8,9% y ROE de FY+3 19,2%, frente al crecimiento del DCF (5,6%: punto medio entre los años 4-10 y la perpetuidad):

| Múltiplo Base FY+3 | Múltiplo | Crecimiento implícito | Diferencia vs. DCF | Lectura |
|---|---:|---:|---:|---|
| EV/EBITDA | 17,2x | 4,2% | −1,4 pp | Coherente con el DCF. |
| EV/FCFF | 24,2x | 4,6% | −1,0 pp | Coherente con el DCF. |
| P/E | 22,5x | 6,3% | +0,7 pp | Coherente con el DCF. |
| P/FCFE | 21,6x | 4,6% | −0,9 pp | Coherente con el DCF. |
| P/OCF | 18,5x | 4,1% | −1,5 pp | Coherente con el DCF. |

Más de 2 pp de diferencia significa que el múltiplo (o el precio) cuenta otra historia de crecimiento que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (subir el crecimiento del DCF si la evidencia lo sostiene, o acercar el múltiplo al justificado si no).

## 7. Sensibilidad del valor ponderado hoy (Base)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$47,10 | — |
| Múltiplos Base +20% | US$52,14 | +10,7% |
| Múltiplos Base −20% | US$42,06 | −10,7% |
| Crecimiento años 1-5 +2 pp | US$49,64 | +5,4% |
| Crecimiento años 1-5 −2 pp | US$44,79 | −4,9% |
| Margen objetivo +3 pp | US$50,65 | +7,5% |
| Margen objetivo −3 pp | US$43,54 | −7,5% |
| WACC +1 pp | US$45,60 | −3,2% |
| WACC −1 pp | US$48,71 | +3,4% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 14,92 | 14,92 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 17,18 | 17,18 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 21,03 | 21,03 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 22,13 | 21,19 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 25,01 | 24,20 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 29,58 | 28,97 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 19,33 | 19,33 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 22,50 | 22,50 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 27,91 | 27,91 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 19,08 | 19,08 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 21,65 | 21,65 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 26,64 | 26,64 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 15,75 | 15,75 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 18,53 | 18,53 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 23,44 | 23,44 | Múltiplo optimista elegido con el protocolo v3 |
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
