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

**Valor intrínseco principal · DCF Base hoy: US$38,58 por acción.** Complemento: DCF esperado por probabilidades US$34,56; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$14,77–US$53,76; precio con MOS 35% sobre el esperado: US$22,47; precio de referencia US$29,61. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$39,20), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Marca premium que cumple sus metas 2029** (valor principal) | 40% | US$38,58 | US$15,43 |
| Conservadora · El ciclo de moda se enfría | 30% | US$23,01 | US$6,90 |
| Disrupción · Deterioro de los fundamentales: Pasa la moda: las ventas caen | 10% | US$14,77 | US$1,48 |
| Optimista · On se vuelve una marca deportiva global | 20% | US$53,76 | US$10,75 |
| **DCF esperado (complemento)** | 100% | **US$34,56** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$38,92 por acción y los múltiplos, US$34,52 hoy: 11% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$38,58 | US$25,44 | US$33,32 | US$22,47 | US$47,89 |
| Conservador | US$23,01 | US$20,82 | US$22,13 | US$22,47 | US$30,06 |
| Optimista | US$53,76 | US$29,97 | US$44,25 | US$22,47 | US$65,16 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - ONON](https://docs.google.com/spreadsheets/d/17E_Rd-MD-u5i8Vez7sYwcWIdVYvDdjNhOu-6NWAzGnQ/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$29,61.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 10,0% | 18,0% | 22,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 10,0% | 14,0% | 22,0% | Input B29 |
| Margen EBIT objetivo | 13,0% | 17,0% | 20,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,50 / 2,62 | — | Input B32/B33 |
| DCF por acción hoy | US$23,01 | US$38,58 | US$53,76 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,50, ERP 4,23%, Ke 11,33%, costo de la deuda después de impuestos 4,61%, peso del patrimonio 91,9%, WACC inicial 10,79% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: On cotizó a 24-48x EBITDA y 64-96x utilidades como marca de hipercrecimiento. En agosto de 2026 bajó su guía de crecimiento a ~20% (desde ≥23%) tras ventas por debajo de lo esperado en EE. UU., y la acción cayó 22% en un día hasta mínimos de dos años. La etapa actual es solo el LTM. B: ropa y calzado deportivo (Deckers, Nike, Lululemon, Birkenstock, Adidas, Crocs), datos de yfinance al 29-sep-2026. Ajuste +30%: On crece ~20% al año frente a 0-13% de los peers, con margen parecido y sin deuda. λ = 0,25: la On de FY+3 del escenario Base sigue creciendo más que el sector, pero ya como marca establecida.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana LTM (etapa actual) = 12,4x | 9,5x (n=6: DECK 7,1x, NKE 11,2x, LULU 5,0x, BIRK 11,0x, ADDYY 12,7x, CROX 8,0x) × 1,30 = 12,3x | 31,2x / 21,0x / — | **17,1x** | 13,9x | 18,6x | 12,4x / —x / —x |
| EV/FCFF | mediana LTM (etapa actual) = 16,8x | 13,8x (n=6: DECK 8,4x, NKE 25,3x, LULU 8,8x, BIRK 19,5x, ADDYY 18,0x, CROX 9,6x) × 1,30 = 17,9x | 43,7x / 29,5x / — | **23,9x** | 18,6x | 28,6x | 16,8x / —x / —x |
| P/E | mediana LTM (etapa actual) = 19,8x | 13,6x (n=6: DECK 11,0x, NKE 17,1x, LULU 8,0x, BIRK 16,2x, ADDYY 18,6x, CROX 10,9x) × 1,30 = 17,7x | 21,2x / 15,2x / — | **19,4x** | 16,3x | 21,7x | 19,8x / —x / —x |
| P/FCFE | mediana LTM (etapa actual) = 18,3x | 12,6x (n=6: DECK 9,5x, NKE 24,3x, LULU 7,9x, BIRK 18,7x, ADDYY 15,8x, CROX 8,3x) × 1,30 = 16,4x | 28,5x / 21,7x / — | **20,2x** | 16,4x | 24,4x | 18,3x / —x / —x |
| P/OCF | mediana LTM (etapa actual) = 15,0x | 10,7x (n=6: DECK 8,9x, NKE 18,5x, LULU 5,4x, BIRK 13,6x, ADDYY 12,5x, CROX 7,7x) × 1,30 = 13,9x | 27,1x / 19,5x / — | **17,6x** | 14,5x | 19,8x | 15,0x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 17,1x: promedio de historia y peers 12,3x, acercado 25% al justificado (31,2x); rango de anclas 12,3x–31,2x. Atípicos excluidos de la historia: Dec '21 (-92,2x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 23,9x: promedio de historia y peers 17,4x, acercado 25% al justificado (43,7x); rango de anclas 16,8x–43,7x. Atípicos excluidos de la historia: Dec '21 (-524,1x: métrica negativa o ~0); Dec '22 (-16,0x: métrica negativa o ~0). La razón FCF después de intereses ÷ FCFF se fija en 1,0: On casi no tiene deuda y su 'Interest / Other' es sobre todo diferencia cambiaria (francos suizos), no intereses. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 19,4x: promedio de historia y peers 18,8x, acercado 25% al justificado (21,2x); rango de anclas 17,7x–21,2x. Atípicos excluidos de la historia: Dec '21 (-61,0x: métrica negativa o ~0); LTM (19,8x: < 0,4x la mediana (65.2x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 20,2x: promedio de historia y peers 17,4x, acercado 25% al justificado (28,5x); rango de anclas 16,4x–28,5x. Atípicos excluidos de la historia: Dec '21 (-558,0x: métrica negativa o ~0); Dec '22 (-16,7x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 17,6x: promedio de historia y peers 14,4x, acercado 25% al justificado (27,1x); rango de anclas 13,9x–27,1x. Atípicos excluidos de la historia: Dec '22 (-22,9x: métrica negativa o ~0); Dec '21 (636,4x: > 2,5x la mediana (33.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$25,44 frente a US$38,58 del DCF (−34%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$25,44 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$53,24 | US$31,75 | US$74,20 |
| EV/EBITDA | 10% | US$61,28 | US$36,65 | US$79,62 |
| EV/FCFF | 15% | US$37,47 | US$29,16 | US$48,04 |
| P/E | 5% | US$36,42 | US$21,23 | US$50,20 |
| P/FCFE | 5% | US$24,62 | US$18,45 | US$32,83 |
| P/OCF | 5% | US$22,86 | US$19,78 | US$26,38 |
| **Ponderado FY+3** | 100% | US$47,89 | US$30,06 | US$65,16 |

Valor presente (Ke 11,33%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$37,98 | US$42,18 | US$44,40 | US$41,52 | OK |
| EV/EBITDA | Conservador | US$29,44 | US$28,25 | US$26,55 | US$28,08 | OK |
| EV/EBITDA | Optimista | US$42,43 | US$51,62 | US$57,69 | US$50,58 | OK |
| EV/FCFF | Base | US$17,64 | US$23,11 | US$27,15 | US$22,63 | OK |
| EV/FCFF | Conservador | US$22,29 | US$22,02 | US$21,13 | US$21,81 | OK |
| EV/FCFF | Optimista | US$15,15 | US$26,45 | US$34,81 | US$25,47 | OK |
| P/E | Base | US$21,68 | US$24,59 | US$26,39 | US$24,22 | OK |
| P/E | Conservador | US$17,00 | US$16,25 | US$15,38 | US$16,21 | OK |
| P/E | Optimista | US$25,07 | US$31,73 | US$36,38 | US$31,06 | OK |
| P/FCFE | Base | US$11,51 | US$15,15 | US$17,84 | US$14,84 | OK |
| P/FCFE | Conservador | US$14,79 | US$14,02 | US$13,37 | US$14,06 | OK |
| P/FCFE | Optimista | US$10,60 | US$18,16 | US$23,79 | US$17,51 | OK |
| P/OCF | Base | US$10,27 | US$13,81 | US$16,57 | US$13,55 | OK |
| P/OCF | Conservador | US$14,84 | US$14,83 | US$14,34 | US$14,67 | OK |
| P/OCF | Optimista | US$7,70 | US$14,15 | US$19,12 | US$13,65 | OK |

Múltiplos consolidados hoy: US$25,44 / US$20,82 / US$29,97 · DCF de las historias hoy: US$38,58 / US$23,01 / US$53,76 · Ponderado hoy: US$33,32 / US$22,13 / US$44,25 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para ONON la diferencia es de −34% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$38,92 por acción y los múltiplos, US$34,52 hoy: 11% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$29,61 supone que los ingresos crecen 8,2% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 14,8% (−6,6 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$53,24 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,3%, WACC de los años 4-10 10,0%, ROE de FY+3 29,4% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 17,1x | 14,7x | +15% | 5,6% | 4,9% | +0,7 pp | Coherente con el DCF. |
| EV/FCFF | 23,9x | 34,7x | −30% | 5,6% | 6,9% | −1,3 pp | Revisar: el múltiplo vale 30% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 19,4x | 28,3x | −32% | 7,2% | 8,6% | −1,5 pp | Revisar: el múltiplo vale 32% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 20,2x | 43,6x | −54% | 6,1% | 8,8% | −2,8 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 54% por debajo del DCF en FY+3. |
| P/OCF | 17,6x | 41,0x | −57% | 5,6% | 8,8% | −3,2 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 57% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$33,32 | — |
| Múltiplos Base +20% | US$35,26 | +5,8% |
| Múltiplos Base −20% | US$31,39 | −5,8% |
| Crecimiento años 2-5 +2 pp | US$35,43 | +6,3% |
| Crecimiento años 2-5 −2 pp | US$32,10 | −3,7% |
| Margen objetivo +3 pp | US$37,80 | +13,4% |
| Margen objetivo −3 pp | US$29,59 | −11,2% |
| WACC +1 pp | US$32,49 | −2,5% |
| WACC −1 pp | US$34,99 | +5,0% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Margen objetivo −3 pp, Crecimiento años 2-5 +2 pp.

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
