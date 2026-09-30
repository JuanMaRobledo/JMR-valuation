---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de CHIPOTLE MEXICAN GRILL INC"
ticker: "CMG"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1VUVN1cCm3Hj8bLrmsCZFYBCDIq3DncxHGHH_jbW8ZtU/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# CHIPOTLE MEXICAN GRILL INC (CMG) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$25,48 en el escenario Base (rango US$18,32–US$34,84). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$26,41 (+4% frente al DCF). Con los pesos de la categoría «Crecimiento» (60% DCF, 40% múltiplos), el ponderado hoy (lectura secundaria) es US$25,85. El valor intrínseco es el DCF: US$25,48 frente a un precio de referencia de US$31,85 (−20%).

Revisión del 30-sep-2026 (ROIC terminal según el moat): moat estrecho, ROIC después del año 10 de 13,7%; el DCF da US$25,48 y los múltiplos US$26,41 hoy (4% por encima, dentro del rango de ±25%). Revisión anterior: Revisión del 30-sep-2026 (ROIC terminal): con un ROIC después del año 10 de 18,4% el DCF pasa de US$20,52 a US$27,91. Los múltiplos (US$26,41 hoy) quedan 5% por debajo del DCF, dentro del rango de ±25%: ambos métodos coinciden; el precio (US$31,85) está por encima de ambos. Lectura anterior, con el DCF sin ROIC terminal: Los múltiplos (US$26,41 hoy) quedan 29% por encima del DCF (US$20,52): los múltiplos suponen que Chipotle conserva a FY+3 una prima parecida a la de hoy frente a otros restaurantes (~27x utilidad), mientras que el DCF refleja un crecimiento de ventas comparables más bajo. El DCF es más confiable hasta que las ventas comparables vuelvan a crecer; los múltiplos indican lo que pagaría el mercado si Chipotle recupera su historia de crecimiento de unidades.

| Escenario | DCF hoy (valor intrínseco) | Múltiplos consolidados hoy (secundario) | Ponderado hoy (secundario) | Compra con MOS sobre el DCF | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$18,32 | US$20,93 | US$19,36 | US$11,91 | US$25,03 |
| Base | US$25,48 | US$26,41 | US$25,85 | US$16,56 | US$34,62 |
| Optimista | US$34,84 | US$34,12 | US$34,55 | US$22,65 | US$47,62 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - CMG](https://docs.google.com/spreadsheets/d/1VUVN1cCm3Hj8bLrmsCZFYBCDIq3DncxHGHH_jbW8ZtU/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$31,85.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 5,0% | 8,0% | 11,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 5,0% | 8,0% | 11,0% | Input B29 |
| Margen EBIT objetivo | 14,0% | 17,0% | 20,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,60 / 2,20 | — | Input B32/B33 |
| DCF por acción hoy | US$18,32 | US$25,48 | US$34,84 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,10, ERP 4,46%, Ke 9,90%, costo de la deuda después de impuestos 4,35%, peso del patrimonio 100,0%, WACC inicial 9,90% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Chipotle cotizó a 40-110x utilidades mientras abría tiendas y crecía en ventas comparables de dos dígitos; en 2025-2026 las ventas comparables se estancaron y la acción cayó de ~US$43 a ~US$32. La etapa actual es FY25 y el LTM. B: restaurantes de servicio rápido y casual (McDonald's, Texas Roadhouse, Yum!, Wingstop), datos de yfinance al 29-sep-2026. Se excluyen Cava (crece 31% con margen de 8%, P/E 95x) y Starbucks (reestructuración, P/E 55x distorsionado). Ajuste +10%: Chipotle todavía abre ~8-10% de tiendas nuevas al año con retornos por tienda altos y sin deuda financiera, más crecimiento que McDonald's y Yum!. λ = 0,25: la Chipotle de FY+3 del escenario Base sigue siendo una cadena en expansión de unidades, parecida a la de hoy.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 21,8x | 16,2x (n=4: MCD 14,7x, TXRH 16,0x, YUM 16,4x, WING 16,7x) × 1,10 = 17,9x | 11,3x / 14,8x / 20,4x | 16,7x | **18,6x** | 21,2x | 16,7x / 18,6x / 21,2x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 34,4x (EV/FCF × 1,05 = FCF después de intereses ÷ FCFF) | 24,5x (n=4: MCD 24,2x, TXRH 28,2x, YUM 24,2x, WING 24,7x) × 1,10 = 26,9x | 23,2x / 28,9x / 38,0x | 27,4x | **30,2x** | 34,6x | 28,4x / 31,5x / 36,0x |
| P/E | mediana Dec '25, LTM (etapa actual) = 31,0x | 22,1x (n=4: MCD 19,0x, TXRH 25,2x, YUM 17,3x, WING 25,7x) × 1,10 = 24,3x | 19,5x / 23,9x / 30,7x | 23,4x | **26,7x** | 30,8x | 23,4x / 26,7x / 30,8x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 29,8x | 22,7x (n=4: MCD 21,3x, TXRH 25,8x, YUM 22,4x, WING 23,0x) × 1,10 = 25,0x | 21,4x / 26,2x / 33,5x | 24,5x | **27,1x** | 30,7x | 24,5x / 27,1x / 30,7x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 20,3x | 15,1x (n=4: MCD 14,6x, TXRH 12,8x, YUM 18,0x, WING 15,6x) × 1,10 = 16,6x | 13,3x / 17,1x / 22,8x | 15,9x | **18,1x** | 21,1x | 15,9x / 18,1x / 21,1x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 18,6x: promedio de historia y peers 19,8x, acercado 25% al justificado (14,8x); rango de anclas 14,8x–21,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 30,2x: promedio de historia y peers 30,7x, acercado 25% al justificado (28,9x); rango de anclas 26,9x–34,4x. Atípicos excluidos de la historia: Dec '20 (143,7x: > 2,5x la mediana (54.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 26,7x: promedio de historia y peers 27,7x, acercado 25% al justificado (23,9x); rango de anclas 23,9x–31,0x. Atípicos excluidos de la historia: Dec '16 (377,5x: > 2,5x la mediana (54.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 27,1x: promedio de historia y peers 27,4x, acercado 25% al justificado (26,2x); rango de anclas 25,0x–29,8x. Atípicos excluidos de la historia: Dec '20 (135,6x: > 2,5x la mediana (51.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 18,1x: promedio de historia y peers 18,4x, acercado 25% al justificado (17,1x); rango de anclas 16,6x–20,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$26,41 frente a US$25,48 del DCF (+4%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$26,41 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$24,31 | US$33,82 | US$46,25 |
| EV/EBITDA | 10% | US$30,22 | US$40,34 | US$54,64 |
| EV/FCFF | 15% | US$24,28 | US$33,72 | US$47,60 |
| P/E | 5% | US$28,18 | US$39,31 | US$54,61 |
| P/FCFE | 5% | US$23,16 | US$32,31 | US$45,23 |
| P/OCF | 5% | US$24,24 | US$33,05 | US$45,49 |
| **Ponderado FY+3** | 100% | US$25,03 | US$34,62 | US$47,62 |

Valor presente (Ke 9,90%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$25,86 | US$24,08 | US$22,77 | US$24,24 | OK |
| EV/EBITDA | Base | US$29,62 | US$30,28 | US$30,40 | US$30,10 | OK |
| EV/EBITDA | Optimista | US$34,75 | US$38,82 | US$41,17 | US$38,24 | OK |
| EV/FCFF | Conservador | US$21,21 | US$19,46 | US$18,30 | US$19,65 | OK |
| EV/FCFF | Base | US$24,03 | US$25,03 | US$25,40 | US$24,82 | OK |
| EV/FCFF | Optimista | US$28,25 | US$33,09 | US$35,87 | US$32,40 | OK |
| P/E | Conservador | US$23,63 | US$22,25 | US$21,23 | US$22,37 | OK |
| P/E | Base | US$27,69 | US$29,03 | US$29,62 | US$28,78 | OK |
| P/E | Optimista | US$32,77 | US$37,99 | US$41,15 | US$37,30 | OK |
| P/FCFE | Conservador | US$19,70 | US$18,32 | US$17,45 | US$18,49 | OK |
| P/FCFE | Base | US$22,41 | US$23,67 | US$24,34 | US$23,47 | OK |
| P/FCFE | Optimista | US$26,13 | US$31,03 | US$34,08 | US$30,41 | OK |
| P/OCF | Conservador | US$20,19 | US$19,05 | US$18,26 | US$19,17 | OK |
| P/OCF | Base | US$23,69 | US$24,49 | US$24,90 | US$24,36 | OK |
| P/OCF | Optimista | US$28,34 | US$31,94 | US$34,28 | US$31,52 | OK |

Múltiplos consolidados hoy: US$20,93 / US$26,41 / US$34,12 · DCF hoy: US$18,32 / US$25,48 / US$34,84 · Ponderado hoy: US$19,36 / US$25,85 / US$34,55 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para CMG la diferencia es de +4% (múltiplos por encima del DCF). Revisión del 30-sep-2026 (ROIC terminal según el moat): moat estrecho, ROIC después del año 10 de 13,7%; el DCF da US$25,48 y los múltiplos US$26,41 hoy (4% por encima, dentro del rango de ±25%). Revisión anterior: Revisión del 30-sep-2026 (ROIC terminal): con un ROIC después del año 10 de 18,4% el DCF pasa de US$20,52 a US$27,91. Los múltiplos (US$26,41 hoy) quedan 5% por debajo del DCF, dentro del rango de ±25%: ambos métodos coinciden; el precio (US$31,85) está por encima de ambos. Lectura anterior, con el DCF sin ROIC terminal: Los múltiplos (US$26,41 hoy) quedan 29% por encima del DCF (US$20,52): los múltiplos suponen que Chipotle conserva a FY+3 una prima parecida a la de hoy frente a otros restaurantes (~27x utilidad), mientras que el DCF refleja un crecimiento de ventas comparables más bajo. El DCF es más confiable hasta que las ventas comparables vuelvan a crecer; los múltiplos indican lo que pagaría el mercado si Chipotle recupera su historia de crecimiento de unidades.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$31,85 supone que los ingresos crecen 12,5% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 8,0% (+4,5 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$33,82 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,9%, WACC de los años 4-10 9,5%, ROE de FY+3 68,0% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 18,6x | 15,6x | +19% | 6,6% | 6,0% | +0,6 pp | Coherente con el DCF. |
| EV/FCFF | 30,2x | 30,3x | −0% | 6,0% | 6,0% | −0,0 pp | Coherente con el DCF. |
| P/E | 26,7x | 23,0x | +16% | 6,3% | 5,7% | +0,6 pp | Coherente con el DCF. |
| P/FCFE | 27,1x | 28,4x | −4% | 6,0% | 6,2% | −0,2 pp | Coherente con el DCF. |
| P/OCF | 18,1x | 18,5x | −2% | 6,1% | 6,2% | −0,1 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$25,85 | — |
| Múltiplos Base +20% | US$27,95 | +8,1% |
| Múltiplos Base −20% | US$23,75 | −8,1% |
| Crecimiento años 1-5 +2 pp | US$27,44 | +6,1% |
| Crecimiento años 1-5 −2 pp | US$24,43 | −5,5% |
| Margen objetivo +3 pp | US$28,52 | +10,3% |
| Margen objetivo −3 pp | US$23,19 | −10,3% |
| WACC +1 pp | US$25,02 | −3,2% |
| WACC −1 pp | US$26,75 | +3,5% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo −3 pp, Margen objetivo +3 pp, Múltiplos Base +20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 16,67 | 16,67 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 18,59 | 18,59 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 21,25 | 21,25 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 28,41 | 27,44 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 31,54 | 30,23 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 35,97 | 34,59 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 23,45 | 23,45 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 26,72 | 26,72 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 30,77 | 30,77 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 24,52 | 24,52 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 27,08 | 27,08 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 30,68 | 30,68 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 15,89 | 15,89 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 18,11 | 18,11 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 21,06 | 21,06 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/CMG_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1VUVN1cCm3Hj8bLrmsCZFYBCDIq3DncxHGHH_jbW8ZtU/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (MCD, CAVA, TXRH, YUM, WING, SBUX).

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
