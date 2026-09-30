---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Novo Nordisk A/S"
ticker: "NVO"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1_w85o-Cv_4GzFB4nq5fGqrMSVoYf-Ltafuol3ir5TMw/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Novo Nordisk A/S (NVO) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$44,06 en el escenario Base (rango US$33,87–US$54,79). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$42,59 (−3% frente al DCF). Con los pesos de la categoría «Madura» (40% DCF, 60% múltiplos), el ponderado hoy (lectura secundaria) es US$43,17. El valor intrínseco es el DCF: US$44,06 frente a un precio de referencia de US$38,71 (+14%).

Revisión del 30-sep-2026 (ROIC terminal): con un ROIC después del año 10 de 16,9% el DCF pasa de US$38,01 a US$44,06. Los múltiplos (US$42,59 hoy) quedan 3% por debajo del DCF, dentro del rango de ±25%: ambos métodos coinciden; el precio (US$38,71) está por debajo de ambos. Lectura anterior, con el DCF sin ROIC terminal: Los múltiplos (US$42,59 hoy) quedan 12% por encima del DCF (US$38,01), dentro del rango de ±25%: ambos métodos coinciden, y los dos quedan cerca del precio (US$38,71). Los múltiplos de la etapa actual (~9x EBITDA, ~12x utilidad) ya incorporan la pérdida de participación frente a Lilly; los peers de farma grande los suben un poco.

| Escenario | DCF hoy (valor intrínseco) | Múltiplos consolidados hoy (secundario) | Ponderado hoy (secundario) | Compra con MOS sobre el DCF | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$33,87 | US$32,14 | US$32,83 | US$22,02 | US$42,07 |
| Base | US$44,06 | US$42,59 | US$43,17 | US$28,64 | US$56,67 |
| Optimista | US$54,79 | US$52,70 | US$53,54 | US$35,62 | US$71,90 |

## 2. Datos

- Hoja del modelo: [NVO_Modelo_JMR_Valoracion_2026-09-24](https://docs.google.com/spreadsheets/d/1_w85o-Cv_4GzFB4nq5fGqrMSVoYf-Ltafuol3ir5TMw/edit).
- Análisis del 23 de sept de 2026. Precio de referencia de la hoja: US$38,71.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -7,0% | -3,0% | -1,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 1,0% | 4,5% | 7,0% | Input B29 |
| Margen EBIT objetivo | 35,0% | 40,0% | 45,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 0,45 / 1,10 | — | Input B32/B33 |
| DCF por acción hoy | US$33,87 | US$44,06 | US$54,79 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,11%, beta apalancada 1,09, ERP 4,09%, Ke 9,55%, costo de la deuda después de impuestos 4,42%, peso del patrimonio 89,9%, WACC inicial 9,03% y terminal 9,20%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Novo Nordisk cotizó a 16-27x EBITDA y 23-36x utilidades durante el auge de Ozempic y Wegovy. Desde 2025 perdió participación frente a Eli Lilly, bajó precios en EE. UU. (Wegovy a US$349 al mes en pago directo) y en febrero de 2026 guió una caída de ventas de 5-13% (luego −6% a 0%); la acción cayó de US$59 a US$39 en tres semanas. La etapa actual es Dec '25 y el LTM. Se excluye la columna sin fecha de la hoja. B: farmacéuticas grandes (AstraZeneca, Novartis, Sanofi, Merck, Pfizer), datos de yfinance al 29-sep-2026. Se excluye Eli Lilly (crece 48% justamente a costa de Novo; su múltiplo es de otra etapa) y, en P/E, Merck (119x por cargos puntuales de I+D adquirida). Ajuste −5%: Novo decrece en 2026 mientras los peers crecen 1-15%, aunque conserva márgenes más altos. λ = 0,25: la Novo de FY+3 del escenario Base es una farmacéutica de crecimiento bajo con márgenes altos, parecida a la de hoy.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 9,4x | 13,8x (n=5: AZN 14,2x, NVS 13,8x, SNY 8,5x, MRK 14,3x, PFE 8,5x) × 0,95 = 13,1x | 6,6x / 8,7x / 10,8x | 8,1x | **10,6x** | 11,9x | —x / 11,1x / —x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 22,4x (EV/FCF × 1,05 = FCF después de intereses ÷ FCFF) | 21,8x (n=4: AZN 38,0x, NVS 19,8x, MRK 23,7x, PFE 16,5x) × 0,95 = 20,7x | 16,3x / 19,5x / 22,7x | 18,1x | **21,0x** | 24,9x | 19,9x / 22,5x / 26,1x |
| P/E | mediana Dec '25, LTM (etapa actual) = 12,0x | 23,4x (n=4: AZN 24,6x, NVS 22,0x, SNY 22,1x, PFE 37,8x) × 0,95 = 22,2x | 14,0x / 16,4x / 18,8x | 15,2x | **16,9x** | 19,4x | —x / 14,4x / —x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 19,8x | 20,7x (n=4: AZN 42,1x, NVS 18,5x, MRK 22,9x, PFE 14,9x) × 0,95 = 19,7x | 15,2x / 18,0x / 20,7x | 16,5x | **19,3x** | 23,3x | —x / 17,0x / —x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 10,4x | 16,8x (n=4: AZN 18,6x, NVS 15,1x, MRK 18,4x, PFE 12,2x) × 0,95 = 15,9x | 7,9x / 10,7x / 13,4x | 10,4x | **12,5x** | 14,4x | —x / 13,9x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 10,6x: promedio de historia y peers 11,2x, acercado 25% al justificado (8,7x); rango de anclas 8,7x–13,1x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 21,0x: promedio de historia y peers 21,5x, acercado 25% al justificado (19,5x); rango de anclas 19,5x–22,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 16,9x: promedio de historia y peers 17,1x, acercado 25% al justificado (16,4x); rango de anclas 12,0x–22,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 19,3x: promedio de historia y peers 19,7x, acercado 25% al justificado (18,0x); rango de anclas 18,0x–19,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 12,5x: promedio de historia y peers 13,1x, acercado 25% al justificado (10,7x); rango de anclas 10,4x–15,9x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$42,59 frente a US$44,06 del DCF (−3%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$42,59 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$44,54 | US$57,93 | US$72,04 |
| EV/EBITDA | 20% | US$35,66 | US$52,96 | US$65,70 |
| EV/FCFF | 10% | US$32,90 | US$47,30 | US$65,30 |
| P/E | 20% | US$50,09 | US$63,74 | US$80,61 |
| P/FCFE | 5% | US$35,17 | US$52,29 | US$74,39 |
| P/OCF | 5% | US$41,19 | US$56,28 | US$71,42 |
| **Ponderado FY+3** | 100% | US$42,07 | US$56,67 | US$71,90 |

Valor presente (Ke 9,55%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$29,92 | US$27,89 | US$27,12 | US$28,31 | OK |
| EV/EBITDA | Base | US$41,32 | US$40,42 | US$40,28 | US$40,67 | OK |
| EV/EBITDA | Optimista | US$47,34 | US$48,68 | US$49,97 | US$48,66 | OK |
| EV/FCFF | Conservador | US$26,19 | US$26,05 | US$25,02 | US$25,76 | OK |
| EV/FCFF | Base | US$33,96 | US$35,97 | US$35,98 | US$35,30 | OK |
| EV/FCFF | Optimista | US$42,29 | US$47,96 | US$49,66 | US$46,64 | OK |
| P/E | Conservador | US$44,09 | US$40,20 | US$38,10 | US$40,80 | OK |
| P/E | Base | US$50,83 | US$49,23 | US$48,48 | US$49,51 | OK |
| P/E | Optimista | US$59,16 | US$60,34 | US$61,31 | US$60,27 | OK |
| P/FCFE | Conservador | US$22,46 | US$27,71 | US$26,75 | US$25,64 | OK |
| P/FCFE | Base | US$32,24 | US$39,79 | US$39,77 | US$37,26 | OK |
| P/FCFE | Optimista | US$42,28 | US$54,89 | US$56,58 | US$51,25 | OK |
| P/OCF | Conservador | US$32,71 | US$32,25 | US$31,33 | US$32,09 | OK |
| P/OCF | Base | US$41,65 | US$42,82 | US$42,80 | US$42,43 | OK |
| P/OCF | Optimista | US$49,16 | US$52,89 | US$54,32 | US$52,12 | OK |

Múltiplos consolidados hoy: US$32,14 / US$42,59 / US$52,70 · DCF hoy: US$33,87 / US$44,06 / US$54,79 · Ponderado hoy: US$32,83 / US$43,17 / US$53,54 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NVO la diferencia es de −3% (múltiplos por debajo del DCF). Revisión del 30-sep-2026 (ROIC terminal): con un ROIC después del año 10 de 16,9% el DCF pasa de US$38,01 a US$44,06. Los múltiplos (US$42,59 hoy) quedan 3% por debajo del DCF, dentro del rango de ±25%: ambos métodos coinciden; el precio (US$38,71) está por debajo de ambos. Lectura anterior, con el DCF sin ROIC terminal: Los múltiplos (US$42,59 hoy) quedan 12% por encima del DCF (US$38,01), dentro del rango de ±25%: ambos métodos coinciden, y los dos quedan cerca del precio (US$38,71). Los múltiplos de la etapa actual (~9x EBITDA, ~12x utilidad) ya incorporan la pérdida de participación frente a Lilly; los peers de farma grande los suben un poco.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$38,71 supone que los ingresos crecen -0,3% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 3,0% (−3,3 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$57,93 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,6%, WACC de los años 4-10 9,1%, ROE de FY+3 43,2% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 10,6x | 11,7x | −9% | 4,7% | 5,1% | −0,4 pp | Coherente con el DCF. |
| EV/FCFF | 21,0x | 26,2x | −18% | 4,2% | 5,1% | −0,9 pp | Coherente con el DCF. |
| P/E | 16,9x | 15,2x | +10% | 4,0% | 3,3% | +0,7 pp | Coherente con el DCF. |
| P/FCFE | 19,3x | 21,7x | −10% | 4,2% | 4,7% | −0,6 pp | Coherente con el DCF. |
| P/OCF | 12,5x | 13,0x | −3% | 4,6% | 4,7% | −0,2 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$43,17 | — |
| Múltiplos Base +20% | US$48,00 | +11,2% |
| Múltiplos Base −20% | US$38,34 | −11,2% |
| Crecimiento años 1-5 +2 pp | US$44,58 | +3,3% |
| Crecimiento años 1-5 −2 pp | US$41,90 | −2,9% |
| Margen objetivo +3 pp | US$44,33 | +2,7% |
| Margen objetivo −3 pp | US$42,02 | −2,7% |
| WACC +1 pp | US$42,25 | −2,1% |
| WACC −1 pp | US$44,16 | +2,3% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 1-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 8,08 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 11,10 | 10,60 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 11,86 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 19,88 | 18,06 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 22,53 | 21,03 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 26,10 | 24,86 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 15,21 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 14,41 | 16,91 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 19,39 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 16,47 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 16,99 | 19,30 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 23,29 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 10,44 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 13,90 | 12,54 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 14,41 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/NVO_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1_w85o-Cv_4GzFB4nq5fGqrMSVoYf-Ltafuol3ir5TMw/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (LLY, AZN, NVS, SNY, MRK, PFE).
- [CNBC, 4-feb-2026: Novo cae; el CEO dice que empeorará antes de mejorar](https://www.cnbc.com/2026/02/04/novo-nordisk-stock-ceo-earnings-guidance-ozempic-wegovy.html)
- [CNBC, 4-ago-2026: la guía de Novo decepciona](https://www.cnbc.com/2026/08/04/novo-nordisk-releases-earnings-and-guidance.html)
- [Fierce Pharma: advertencia de ventas y utilidad 2026](https://www.fiercepharma.com/pharma/novo-shares-plummet-sales-profit-warning-26)

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
