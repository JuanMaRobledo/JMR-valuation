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

**Valor intrínseco principal · DCF Base hoy: US$36,34 por acción.** Complemento: DCF esperado por probabilidades US$34,93; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$22,69–US$43,67; precio con MOS 35% sobre el esperado: US$22,71; precio de referencia US$43,66. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$37,39), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La cartera diversificada sostiene ~7%** (valor principal) | 45% | US$36,34 | US$16,35 |
| Conservadora · El campo pulsado se vuelve commodity | 30% | US$29,03 | US$8,71 |
| Disrupción · Deterioro de los fundamentales: Pierde participación y precio | 5% | US$22,69 | US$1,13 |
| Optimista · Electrofisiología y Watchman vuelven a doble dígito | 20% | US$43,67 | US$8,73 |
| **DCF esperado (complemento)** | 100% | **US$34,93** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$36,39 por acción y los múltiplos, US$38,61 hoy: 6% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$36,34 | US$29,74 | US$33,70 | US$22,71 | US$45,12 |
| Conservador | US$29,03 | US$25,06 | US$27,44 | US$22,71 | US$35,95 |
| Optimista | US$43,67 | US$38,17 | US$41,47 | US$22,71 | US$56,61 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - BSX](https://docs.google.com/spreadsheets/d/1LVn63SMyvovWzNjbF5Jdi-v0EFUPXLqp4A6n8gwbKHc/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$43,66.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 4,0% | 7,0% | 10,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 4,0% | 7,0% | 10,0% | Input B29 |
| Margen EBIT objetivo | 20,2% | 24,2% | 27,2% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,26 / 1,17 | — | Input B32/B33 |
| DCF por acción hoy | US$29,03 | US$36,34 | US$43,67 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,00, ERP 4,46%, Ke 9,45%, costo de la deuda después de impuestos 4,76%, peso del patrimonio 85,3%, WACC inicial 8,76% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Boston Scientific cotizaba a 25-55x EBITDA mientras crecía 12-20% orgánico. En 2026 la empresa bajó su guía de crecimiento orgánico a 6,5-8% (desde 10-11%, frente a 19,5% en 2025), las ventas de Watchman se estancaron y un ciberataque en agosto la llevó a retirar su guía; la acción cayó ~50% en el año. La etapa actual es solo el LTM. B: medtech diversificada de gran capitalización (Medtronic, Stryker, Abbott, Edwards, Intuitive Surgical, Zimmer Biomet), datos de yfinance al 29-sep-2026. Ajuste −5%: tras la baja de guía, Boston Scientific crece como la mediana de los peers, pero con más incertidumbre de ejecución (Watchman, electrofisiología en EE. UU. y los efectos del ciberataque). λ = 0 (30-sep-2026): el justificado C supone que el ROE de FY+3 se mantiene para siempre, mientras que el DCF supone que después del año 10 el retorno sobre el capital baja al costo de capital (BSX no cumple la regla del ROIC terminal). C se deja fuera del Base y se conserva como referencia en la tabla.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana LTM (etapa actual) = 13,5x | 16,6x (n=6: MDT 12,9x, SYK 15,9x, ABT 17,3x, EW 23,3x, ISRG 33,8x, ZBH 9,8x) × 0,95 = 10,3x | 24,8x / 19,4x / 33,7x | **11,9x** | 10,3x | 14,6x | 17,2x / 14,9x / 21,0x |
| EV/FCFF | mediana LTM (etapa actual) = 19,6x (EV/FCF × 0,95 = FCF después de intereses ÷ FCFF) | 25,1x (n=6: MDT 20,1x, SYK 23,8x, ABT 26,3x, EW 32,5x, ISRG 43,9x, ZBH 15,1x) × 0,95 = 16,4x | 31,6x / 25,0x / 42,9x | **18,0x** | 15,8x | 21,6x | 25,0x / 22,1x / 29,6x |
| P/E | mediana LTM (etapa actual) = 17,9x | 30,8x (n=6: MDT 21,5x, SYK 28,9x, ABT 32,7x, EW 52,4x, ISRG 47,3x, ZBH 22,2x) × 0,95 = 23,6x | 19,3x / 15,5x / 25,1x | **20,8x** | 17,9x | 25,8x | 22,5x / 19,3x / 27,9x |
| P/FCFE | mediana LTM (etapa actual) = 17,6x | 23,2x (n=6: MDT 18,2x, SYK 22,7x, ABT 23,7x, EW 35,4x, ISRG 45,8x, ZBH 12,4x) × 0,95 = 14,3x | 27,2x / 22,1x / 35,1x | **15,9x** | 14,1x | 19,6x | 21,6x / 19,1x / 26,6x |
| P/OCF | mediana LTM (etapa actual) = 14,1x | 18,9x (n=6: MDT 13,9x, SYK 19,4x, ABT 18,5x, EW 29,5x, ISRG 39,8x, ZBH 10,0x) × 0,95 = 11,4x | 26,1x / 19,7x / 35,7x | **12,7x** | 10,8x | 16,1x | 18,5x / 15,8x / 23,4x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 11,9x: promedio de historia y peers 11,9x, acercado 0% al justificado (24,8x); rango de anclas 10,3x–24,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 18,0x: promedio de historia y peers 18,0x, acercado 0% al justificado (31,6x); rango de anclas 16,4x–31,6x. Atípicos excluidos de la historia: Dec '18 (-9.307,0x: métrica negativa o ~0); LTM (20,7x: < 0,4x la mediana (52.0x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 20,8x: promedio de historia y peers 20,8x, acercado 0% al justificado (19,3x); rango de anclas 17,9x–23,6x. Atípicos excluidos de la historia: Dec '20 (-599,2x: métrica negativa o ~0); Dec '17 (354,1x: > 2,5x la mediana (55.6x)); Dec '19 (13,6x: < 0,4x la mediana (55.6x), caída puntual); LTM (17,9x: < 0,4x la mediana (55.6x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 15,9x: promedio de historia y peers 15,9x, acercado 0% al justificado (27,2x); rango de anclas 14,3x–27,2x. Atípicos excluidos de la historia: Dec '18 (-8.155,3x: métrica negativa o ~0); LTM (17,6x: < 0,4x la mediana (46.1x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 12,7x: promedio de historia y peers 12,7x, acercado 0% al justificado (26,1x); rango de anclas 11,4x–26,1x. Atípicos excluidos de la historia: Dec '18 (157,8x: > 2,5x la mediana (33.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$29,74 frente a US$36,34 del DCF (−18%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$29,74 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$47,65 | US$38,06 | US$57,26 |
| EV/EBITDA | 10% | US$51,23 | US$38,14 | US$71,31 |
| EV/FCFF | 15% | US$32,81 | US$27,71 | US$42,54 |
| P/E | 5% | US$56,33 | US$42,62 | US$77,65 |
| P/FCFE | 5% | US$39,86 | US$31,88 | US$53,33 |
| P/OCF | 5% | US$33,55 | US$28,28 | US$43,89 |
| **Ponderado FY+3** | 100% | US$45,12 | US$35,95 | US$56,61 |

Valor presente (Ke 9,45%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$36,94 | US$38,56 | US$39,08 | US$38,19 | OK |
| EV/EBITDA | Conservador | US$30,34 | US$29,93 | US$29,09 | US$29,78 | OK |
| EV/EBITDA | Optimista | US$47,77 | US$52,32 | US$54,39 | US$51,49 | OK |
| EV/FCFF | Base | US$19,15 | US$22,47 | US$25,03 | US$22,21 | OK |
| EV/FCFF | Conservador | US$19,48 | US$20,80 | US$21,13 | US$20,47 | OK |
| EV/FCFF | Optimista | US$19,68 | US$27,75 | US$32,45 | US$26,62 | OK |
| P/E | Base | US$40,25 | US$42,46 | US$42,96 | US$41,89 | OK |
| P/E | Conservador | US$33,75 | US$33,52 | US$32,50 | US$33,26 | OK |
| P/E | Optimista | US$50,94 | US$56,82 | US$59,22 | US$55,66 | OK |
| P/FCFE | Base | US$26,82 | US$29,00 | US$30,40 | US$28,74 | OK |
| P/FCFE | Conservador | US$24,19 | US$24,95 | US$24,31 | US$24,48 | OK |
| P/FCFE | Optimista | US$31,92 | US$38,29 | US$40,68 | US$36,96 | OK |
| P/OCF | Base | US$22,77 | US$24,37 | US$25,59 | US$24,24 | OK |
| P/OCF | Conservador | US$21,66 | US$21,91 | US$21,57 | US$21,71 | OK |
| P/OCF | Optimista | US$25,54 | US$30,65 | US$33,47 | US$29,89 | OK |

Múltiplos consolidados hoy: US$29,74 / US$25,06 / US$38,17 · DCF de las historias hoy: US$36,34 / US$29,03 / US$43,67 · Ponderado hoy: US$33,70 / US$27,44 / US$41,47 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para BSX la diferencia es de −18% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$36,39 por acción y los múltiplos, US$38,61 hoy: 6% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$43,66 supone que los ingresos crecen 10,0% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 7,0% (+3,0 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$47,65 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,4%, WACC de los años 4-10 8,9%, ROE de FY+3 19,2% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 11,9x | 11,1x | +8% | 2,2% | 1,7% | +0,5 pp | Coherente con el DCF. |
| EV/FCFF | 18,0x | 24,6x | −31% | 3,2% | 4,6% | −1,5 pp | Revisar: el múltiplo vale 31% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 20,8x | 17,6x | +18% | 5,9% | 5,1% | +0,9 pp | Coherente con el DCF. |
| P/FCFE | 15,9x | 19,1x | −16% | 3,0% | 4,0% | −1,0 pp | Coherente con el DCF. |
| P/OCF | 12,7x | 18,1x | −30% | 1,8% | 3,9% | −2,2 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 30% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$33,70 | — |
| Múltiplos Base +20% | US$36,37 | +7,9% |
| Múltiplos Base −20% | US$31,02 | −7,9% |
| Crecimiento años 2-5 +2 pp | US$36,20 | +7,4% |
| Crecimiento años 2-5 −2 pp | US$32,62 | −3,2% |
| Margen objetivo +3 pp | US$37,76 | +12,1% |
| Margen objetivo −3 pp | US$30,89 | −8,3% |
| WACC +1 pp | US$32,87 | −2,5% |
| WACC −1 pp | US$35,90 | +6,5% |

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
