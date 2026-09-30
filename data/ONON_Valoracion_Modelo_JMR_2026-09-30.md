---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de On Holding AG"
ticker: "ONON"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/17E_Rd-MD-u5i8Vez7sYwcWIdVYvDdjNhOu-6NWAzGnQ/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# On Holding AG (ONON) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$38,92 en el escenario Base (rango US$24,80–US$63,65). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$34,52 (−11% frente al DCF). Con los pesos de la categoría «Crecimiento» (60% DCF, 40% múltiplos), el valor intrínseco ponderado hoy es US$37,16, frente a un precio de referencia de US$30,00 (+24%).

Los múltiplos (US$34,52 hoy) quedan 11% por debajo del DCF (US$38,92), dentro del rango de ±25%: ambos métodos coinciden. Los dos quedan por encima del precio (US$30,00): el mercado descuenta, tras el recorte de la guía, un crecimiento menor que el escenario Base. P/E, P/FCFE y P/OCF dan menos que los múltiplos de EV porque la proyección mantiene 'Interest / Other' en −25% del EBIT (trata como recurrentes las pérdidas cambiarias de 2023 y 2025); conviene revisar ese supuesto.

| Escenario | DCF hoy | Múltiplos consolidados hoy | Valor intrínseco ponderado hoy | Compra con MOS hoy | Precio objetivo FY+3 ponderado |
|---|---:|---:|---:|---:|---:|
| Conservador | US$24,80 | US$23,85 | US$24,42 | US$15,87 | US$32,99 |
| Base | US$38,92 | US$34,52 | US$37,16 | US$24,15 | US$52,25 |
| Optimista | US$63,65 | US$45,41 | US$56,35 | US$36,63 | US$81,76 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - ONON](https://docs.google.com/spreadsheets/d/17E_Rd-MD-u5i8Vez7sYwcWIdVYvDdjNhOu-6NWAzGnQ/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$30,00.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 10,0% | 18,0% | 22,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 10,0% | 14,0% | 22,0% | Input B29 |
| Margen EBIT objetivo | 13,0% | 17,0% | 20,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,50 / 2,20 | — | Input B32/B33 |
| DCF por acción hoy | US$24,80 | US$38,92 | US$63,65 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,50, ERP 4,23%, Ke 11,33%, costo de la deuda después de impuestos 4,61%, peso del patrimonio 92,0%, WACC inicial 10,80% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: On cotizó a 24-48x EBITDA y 64-96x utilidades como marca de hipercrecimiento. En agosto de 2026 bajó su guía de crecimiento a ~20% (desde ≥23%) tras ventas por debajo de lo esperado en EE. UU., y la acción cayó 22% en un día hasta mínimos de dos años. La etapa actual es solo el LTM. B: ropa y calzado deportivo (Deckers, Nike, Lululemon, Birkenstock, Adidas, Crocs), datos de yfinance al 29-sep-2026. Ajuste +30%: On crece ~20% al año frente a 0-13% de los peers, con margen parecido y sin deuda. λ = 0,25: la On de FY+3 del escenario Base sigue creciendo más que el sector, pero ya como marca establecida.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana LTM (etapa actual) = 12,4x | 9,5x (n=6: DECK 7,1x, NKE 11,2x, LULU 5,0x, BIRK 11,0x, ADDYY 12,7x, CROX 8,0x) × 1,30 = 12,3x | 21,0x / 31,2x / — | 13,9x | **17,1x** | 18,6x | —x / 12,4x / —x |
| EV/FCFF | mediana LTM (etapa actual) = 16,8x | 13,8x (n=6: DECK 8,4x, NKE 25,3x, LULU 8,8x, BIRK 19,5x, ADDYY 18,0x, CROX 9,6x) × 1,30 = 17,9x | 29,5x / 43,7x / — | 18,6x | **23,9x** | 28,6x | —x / 16,8x / —x |
| P/E | mediana LTM (etapa actual) = 19,8x | 13,6x (n=6: DECK 11,0x, NKE 17,1x, LULU 8,0x, BIRK 16,2x, ADDYY 18,6x, CROX 10,9x) × 1,30 = 17,7x | 15,2x / 21,2x / — | 16,3x | **19,4x** | 21,7x | —x / 19,8x / —x |
| P/FCFE | mediana LTM (etapa actual) = 18,3x | 12,6x (n=6: DECK 9,5x, NKE 24,3x, LULU 7,9x, BIRK 18,7x, ADDYY 15,8x, CROX 8,3x) × 1,30 = 16,4x | 21,7x / 28,5x / — | 16,4x | **20,2x** | 24,4x | —x / 18,3x / —x |
| P/OCF | mediana LTM (etapa actual) = 15,0x | 10,7x (n=6: DECK 8,9x, NKE 18,5x, LULU 5,4x, BIRK 13,6x, ADDYY 12,5x, CROX 7,7x) × 1,30 = 13,9x | 19,5x / 27,1x / — | 14,5x | **17,6x** | 19,8x | —x / 15,0x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 17,1x: promedio de historia y peers 12,3x, acercado 25% al justificado (31,2x); rango de anclas 12,3x–31,2x. Atípicos excluidos de la historia: Dec '21 (-92,2x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 23,9x: promedio de historia y peers 17,4x, acercado 25% al justificado (43,7x); rango de anclas 16,8x–43,7x. Atípicos excluidos de la historia: Dec '21 (-524,1x: métrica negativa o ~0); Dec '22 (-16,0x: métrica negativa o ~0). La razón FCF después de intereses ÷ FCFF se fija en 1,0: On casi no tiene deuda y su 'Interest / Other' es sobre todo diferencia cambiaria (francos suizos), no intereses. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 19,4x: promedio de historia y peers 18,8x, acercado 25% al justificado (21,2x); rango de anclas 17,7x–21,2x. Atípicos excluidos de la historia: Dec '21 (-61,0x: métrica negativa o ~0); LTM (19,8x: < 0,4x la mediana (65.2x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 20,2x: promedio de historia y peers 17,4x, acercado 25% al justificado (28,5x); rango de anclas 16,4x–28,5x. Atípicos excluidos de la historia: Dec '21 (-558,0x: métrica negativa o ~0); Dec '22 (-16,7x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 17,6x: promedio de historia y peers 14,4x, acercado 25% al justificado (27,1x); rango de anclas 13,9x–27,1x. Atípicos excluidos de la historia: Dec '22 (-22,9x: métrica negativa o ~0); Dec '21 (636,4x: > 2,5x la mediana (33.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$34,52 frente a US$38,92 del DCF (−11%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$34,52 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$34,22 | US$53,71 | US$87,84 |
| EV/EBITDA | 10% | US$36,71 | US$57,43 | US$79,62 |
| EV/FCFF | 15% | US$35,00 | US$57,54 | US$84,86 |
| P/E | 5% | US$21,05 | US$34,04 | US$50,20 |
| P/FCFE | 5% | US$25,10 | US$41,09 | US$65,24 |
| P/OCF | 5% | US$24,58 | US$37,80 | US$51,85 |
| **Ponderado FY+3** | 100% | US$32,99 | US$52,25 | US$81,76 |

Valor presente (Ke 11,33%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$29,59 | US$28,08 | US$26,60 | US$28,09 | OK |
| EV/EBITDA | Base | US$38,18 | US$40,71 | US$41,62 | US$40,17 | OK |
| EV/EBITDA | Optimista | US$42,64 | US$51,45 | US$57,70 | US$50,59 | OK |
| EV/FCFF | Conservador | US$28,43 | US$26,91 | US$25,36 | US$26,90 | OK |
| EV/FCFF | Base | US$35,95 | US$40,50 | US$41,69 | US$39,38 | OK |
| EV/FCFF | Optimista | US$42,48 | US$53,88 | US$61,49 | US$52,62 | OK |
| P/E | Conservador | US$17,03 | US$16,00 | US$15,25 | US$16,09 | OK |
| P/E | Base | US$21,75 | US$23,67 | US$24,66 | US$23,36 | OK |
| P/E | Optimista | US$25,14 | US$31,59 | US$36,37 | US$31,04 | OK |
| P/FCFE | Conservador | US$20,01 | US$19,17 | US$18,19 | US$19,13 | OK |
| P/FCFE | Base | US$26,63 | US$28,90 | US$29,77 | US$28,43 | OK |
| P/FCFE | Optimista | US$33,51 | US$41,69 | US$47,27 | US$40,83 | OK |
| P/OCF | Conservador | US$19,54 | US$18,73 | US$17,81 | US$18,69 | OK |
| P/OCF | Base | US$23,65 | US$26,63 | US$27,39 | US$25,89 | OK |
| P/OCF | Optimista | US$26,53 | US$33,10 | US$37,57 | US$32,40 | OK |

Múltiplos consolidados hoy: US$23,85 / US$34,52 / US$45,41 · DCF hoy: US$24,80 / US$38,92 / US$63,65 · Ponderado hoy: US$24,42 / US$37,16 / US$56,35 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para ONON la diferencia es de −11% (múltiplos por debajo del DCF). Los múltiplos (US$34,52 hoy) quedan 11% por debajo del DCF (US$38,92), dentro del rango de ±25%: ambos métodos coinciden. Los dos quedan por encima del precio (US$30,00): el mercado descuenta, tras el recorte de la guía, un crecimiento menor que el escenario Base. P/E, P/FCFE y P/OCF dan menos que los múltiplos de EV porque la proyección mantiene 'Interest / Other' en −25% del EBIT (trata como recurrentes las pérdidas cambiarias de 2023 y 2025); conviene revisar ese supuesto.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$30,00 supone que los ingresos crecen 8,7% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 14,8% (−6,1 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Crecimiento perpetuo después de FY+3 que supone cada múltiplo Base, con Ke 11,3%, WACC de los años 4-10 10,0% y ROE de FY+3 29,4%, frente al crecimiento del DCF (7,6%: punto medio entre los años 4-10 y la perpetuidad):

| Múltiplo Base FY+3 | Múltiplo | Crecimiento implícito | Diferencia vs. DCF | Lectura |
|---|---:|---:|---:|---|
| EV/EBITDA | 17,1x | 5,6% | −2,0 pp | Coherente con el DCF. |
| EV/FCFF | 23,9x | 5,6% | −2,0 pp | Coherente con el DCF. |
| P/E | 19,4x | 7,2% | −0,4 pp | Coherente con el DCF. |
| P/FCFE | 20,2x | 6,1% | −1,5 pp | Coherente con el DCF. |
| P/OCF | 17,6x | 5,6% | −1,9 pp | Coherente con el DCF. |

Más de 2 pp de diferencia significa que el múltiplo (o el precio) cuenta otra historia de crecimiento que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (subir el crecimiento del DCF si la evidencia lo sostiene, o acercar el múltiplo al justificado si no).

## 7. Sensibilidad del valor ponderado hoy (Base)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$37,16 | — |
| Múltiplos Base +20% | US$39,82 | +7,2% |
| Múltiplos Base −20% | US$34,50 | −7,2% |
| Crecimiento años 1-5 +2 pp | US$39,31 | +5,8% |
| Crecimiento años 1-5 −2 pp | US$35,20 | −5,3% |
| Margen objetivo +3 pp | US$41,43 | +11,5% |
| Margen objetivo −3 pp | US$32,89 | −11,5% |
| WACC +1 pp | US$35,92 | −3,3% |
| WACC −1 pp | US$38,49 | +3,6% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo −3 pp, Margen objetivo +3 pp, Múltiplos Base +20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 13,93 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 12,37 | 17,07 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 18,56 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 18,58 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 16,80 | 23,94 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 28,59 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 16,28 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 19,84 | 19,38 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 21,67 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 16,42 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 18,34 | 20,17 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 24,45 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 14,48 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 14,98 | 17,60 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 19,78 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/ONON_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/17E_Rd-MD-u5i8Vez7sYwcWIdVYvDdjNhOu-6NWAzGnQ/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (DECK, NKE, LULU, BIRK, ADDYY, CROX).
- [Yahoo Finance: On cae 22% tras el 2T y baja su guía](https://finance.yahoo.com/markets/stocks/articles/holding-shares-fall-sharply-q2-094135863.html)
- [Trefis, 23-sep-2026: On confirma su guía y recompra US$1.000 millones](https://www.trefis.com/stock/onon/articles/616301/why-did-on-holding-stock-jump-if-its-near-term-guidance-did-not-change/2026-09-23)

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
