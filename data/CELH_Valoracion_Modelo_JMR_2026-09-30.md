---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Celsius Holdings, Inc."
ticker: "CELH"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1pl_6BeI9gl_ciaSY5wDqyjRF9GS-ZhjXXK4wGVuBC4o/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Celsius Holdings, Inc. (CELH) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$18,11 en el escenario Base (rango US$9,94–US$29,71). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$21,32 (+18% frente al DCF). Con los pesos de la categoría «Crecimiento» (60% DCF, 40% múltiplos), el valor intrínseco ponderado hoy es US$19,40, frente a un precio de referencia de US$28,00 (−31%).

Los múltiplos (US$21,32 hoy) quedan 18% por encima del DCF (US$18,11). Con la historia distorsionada por la compra de Alani Nu, los múltiplos se anclan en FY24, en los peers de bebidas y en los fundamentales; el DCF es más confiable mientras no haya uno o dos años limpios después de integrar Alani Nu.

| Escenario | DCF hoy | Múltiplos consolidados hoy | Valor intrínseco ponderado hoy | Compra con MOS hoy | Precio objetivo FY+3 ponderado |
|---|---:|---:|---:|---:|---:|
| Conservador | US$9,94 | US$16,75 | US$12,66 | US$8,23 | US$16,62 |
| Base | US$18,11 | US$21,32 | US$19,40 | US$12,61 | US$27,72 |
| Optimista | US$29,71 | US$26,53 | US$28,44 | US$18,48 | US$42,74 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - CELH](https://docs.google.com/spreadsheets/d/1pl_6BeI9gl_ciaSY5wDqyjRF9GS-ZhjXXK4wGVuBC4o/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$28,00.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 2,0% | 7,0% | 12,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 2,0% | 6,0% | 12,0% | Input B29 |
| Margen EBIT objetivo | 11,0% | 17,0% | 21,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,50 / 2,00 | — | Input B32/B33 |
| DCF por acción hoy | US$9,94 | US$18,11 | US$29,71 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,50, ERP 4,46%, Ke 11,68%, costo de la deuda después de impuestos 5,19%, peso del patrimonio 91,7%, WACC inicial 11,14% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Celsius fue hipercrecimiento hasta 2023 (múltiplos de 50-500x o con utilidades negativas); desde 2024 es una marca de bebidas energéticas en consolidación. Se usa FY24 como etapa actual. El FY25 y el LTM se excluyen de todos los métodos: incluyen US$246,7 millones por terminar contratos de distribución de Alani Nu (traspaso al sistema de PepsiCo) y US$24,8 millones de costos de la adquisición (10-K FY2025), que distorsionan utilidad, EBITDA y flujo de caja. B: bebidas con marca (Monster, PepsiCo, Coca-Cola, Vita Coco), datos de yfinance al 29-sep-2026. Se excluyen Keurig Dr Pepper (crecimiento de 76% por la compra de JDE Peet's distorsiona sus múltiplos) y BellRing (nutrición, en fuerte caída). Ajuste −10%: Celsius crece más que Coca-Cola y PepsiCo, pero con márgenes menores que Monster, dependencia de PepsiCo como distribuidor y una integración reciente (Alani Nu) aún por demostrar. λ = 0,25: la Celsius de FY+3 del escenario Base es una marca madura de crecimiento medio.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '24 (etapa actual) = 32,6x | 23,1x (n=4: MNST 26,8x, PEP 11,5x, KO 23,8x, COCO 22,3x) × 0,90 = 20,8x | 11,0x / 12,1x / 15,3x | 21,2x | **23,0x** | 25,6x | 21,2x / 23,0x / 25,6x |
| EV/FCFF | mediana Dec '24 (etapa actual) = 21,3x (EV/FCF × 0,96 = FCF después de intereses ÷ FCFF) | 25,3x (n=4: MNST 37,8x, PEP 21,4x, KO 26,1x, COCO 24,5x) × 0,90 = 22,8x | 17,1x / 21,3x / 33,1x | 20,0x | **21,8x** | 27,0x | 20,5x / 22,6x / 28,0x |
| P/E | mediana Dec '24 (etapa actual) = 43,2x | 28,7x (n=4: MNST 38,6x, PEP 16,9x, KO 26,1x, COCO 31,2x) × 0,90 = 25,8x | 11,1x / 13,7x / 19,1x | 25,8x | **29,3x** | 34,6x | 25,8x / 29,3x / 34,6x |
| P/FCFE | mediana Dec '24 (etapa actual) = 25,9x | 26,2x (n=4: MNST 39,3x, PEP 18,9x, KO 26,1x, COCO 26,3x) × 0,90 = 23,6x | 13,8x / 16,4x / 22,8x | 20,9x | **22,6x** | 26,5x | 20,9x / 22,6x / 26,5x |
| P/OCF | mediana Dec '24 (etapa actual) = 23,5x | 23,9x (n=4: MNST 36,5x, PEP 13,1x, KO 22,9x, COCO 24,8x) × 0,90 = 21,5x | 11,3x / 13,8x / 18,8x | 18,1x | **20,3x** | 23,9x | 18,1x / 20,3x / 23,9x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 23,0x: promedio de historia y peers 26,7x, acercado 25% al justificado (12,1x); rango de anclas 12,1x–32,6x. Atípicos excluidos de la historia: Dec '16 (-7,5x: métrica negativa o ~0); Dec '17 (-8,1x: métrica negativa o ~0); Dec '18 (-5,5x: métrica negativa o ~0); Dec '19 (-69,0x: métrica negativa o ~0); Dec '21 (-659,4x: métrica negativa o ~0); Dec '22 (-13,1x: métrica negativa o ~0); Dec '20 (136,0x: > 2,5x la mediana (44.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 21,8x: promedio de historia y peers 22,0x, acercado 25% al justificado (21,3x); rango de anclas 21,3x–22,8x. Atípicos excluidos de la historia: Dec '16 (-8,8x: métrica negativa o ~0); Dec '17 (-7,7x: métrica negativa o ~0); Dec '18 (-5,0x: métrica negativa o ~0); Dec '21 (-18,5x: métrica negativa o ~0); Dec '19 (96,6x: > 2,5x la mediana (37.2x)); Dec '20 (417,8x: > 2,5x la mediana (37.2x)); Dec '23 (96,0x: > 2,5x la mediana (37.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 29,3x: promedio de historia y peers 34,5x, acercado 25% al justificado (13,7x); rango de anclas 13,7x–43,2x. Atípicos excluidos de la historia: Dec '18 (-5,3x: métrica negativa o ~0); Dec '22 (-14,0x: métrica negativa o ~0); Dec '19 (10,1x: < 0,4x la mediana (56.8x), caída puntual); Dec '20 (152,4x: > 2,5x la mediana (56.8x)); Dec '21 (497,2x: > 2,5x la mediana (56.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 22,6x: promedio de historia y peers 24,7x, acercado 25% al justificado (16,4x); rango de anclas 16,4x–25,9x. Atípicos excluidos de la historia: Dec '16 (-13,7x: métrica negativa o ~0); Dec '17 (-9,4x: métrica negativa o ~0); Dec '18 (-5,6x: métrica negativa o ~0); Dec '21 (-18,7x: métrica negativa o ~0); Dec '19 (110,9x: > 2,5x la mediana (36.3x)); Dec '20 (433,0x: > 2,5x la mediana (36.3x)); Dec '23 (102,1x: > 2,5x la mediana (36.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 20,3x: promedio de historia y peers 22,5x, acercado 25% al justificado (13,8x); rango de anclas 13,8x–23,5x. Atípicos excluidos de la historia: Dec '16 (-13,7x: métrica negativa o ~0); Dec '17 (-9,5x: métrica negativa o ~0); Dec '18 (-5,7x: métrica negativa o ~0); Dec '21 (-19,3x: métrica negativa o ~0); Dec '19 (110,9x: > 2,5x la mediana (32.7x)); Dec '20 (356,6x: > 2,5x la mediana (32.7x)); Dec '23 (89,5x: > 2,5x la mediana (32.7x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$21,32 frente a US$18,11 del DCF (+18%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$21,32 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$13,84 | US$25,23 | US$41,38 |
| EV/EBITDA | 10% | US$29,13 | US$46,53 | US$69,63 |
| EV/FCFF | 15% | US$17,51 | US$24,93 | US$33,73 |
| P/E | 5% | US$22,26 | US$37,70 | US$60,47 |
| P/FCFE | 5% | US$16,17 | US$22,22 | US$27,29 |
| P/OCF | 5% | US$17,09 | US$23,81 | US$29,90 |
| **Ponderado FY+3** | 100% | US$16,62 | US$27,72 | US$42,74 |

Valor presente (Ke 11,68%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$25,84 | US$23,11 | US$20,91 | US$23,29 | OK |
| EV/EBITDA | Base | US$29,51 | US$32,77 | US$33,41 | US$31,89 | OK |
| EV/EBITDA | Optimista | US$34,33 | US$44,68 | US$49,99 | US$43,00 | OK |
| EV/FCFF | Conservador | US$15,95 | US$14,03 | US$12,57 | US$14,18 | OK |
| EV/FCFF | Base | US$14,77 | US$17,24 | US$17,90 | US$16,64 | OK |
| EV/FCFF | Optimista | US$12,24 | US$20,18 | US$24,22 | US$18,88 | OK |
| P/E | Conservador | US$20,17 | US$17,81 | US$15,98 | US$17,99 | OK |
| P/E | Base | US$24,04 | US$26,62 | US$27,07 | US$25,91 | OK |
| P/E | Optimista | US$29,77 | US$38,81 | US$43,41 | US$37,33 | OK |
| P/FCFE | Conservador | US$14,73 | US$12,96 | US$11,61 | US$13,10 | OK |
| P/FCFE | Base | US$13,06 | US$15,33 | US$15,95 | US$14,78 | OK |
| P/FCFE | Optimista | US$9,22 | US$16,11 | US$19,59 | US$14,97 | OK |
| P/OCF | Conservador | US$15,42 | US$13,65 | US$12,27 | US$13,78 | OK |
| P/OCF | Base | US$14,80 | US$16,69 | US$17,09 | US$16,20 | OK |
| P/OCF | Optimista | US$12,10 | US$18,31 | US$21,46 | US$17,29 | OK |

Múltiplos consolidados hoy: US$16,75 / US$21,32 / US$26,53 · DCF hoy: US$9,94 / US$18,11 / US$29,71 · Ponderado hoy: US$12,66 / US$19,40 / US$28,44 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para CELH la diferencia es de +18% (múltiplos por encima del DCF). Los múltiplos (US$21,32 hoy) quedan 18% por encima del DCF (US$18,11). Con la historia distorsionada por la compra de Alani Nu, los múltiplos se anclan en FY24, en los peers de bebidas y en los fundamentales; el DCF es más confiable mientras no haya uno o dos años limpios después de integrar Alani Nu.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$28,00 supone que los ingresos crecen 15,3% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 6,2% (+9,1 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Crecimiento perpetuo después de FY+3 que supone cada múltiplo Base, con Ke 11,7%, WACC de los años 4-10 10,2% y ROE de FY+3 31,2%, frente al crecimiento del DCF (5,3%: punto medio entre los años 4-10 y la perpetuidad):

| Múltiplo Base FY+3 | Múltiplo | Crecimiento implícito | Diferencia vs. DCF | Lectura |
|---|---:|---:|---:|---|
| EV/EBITDA | 23,0x | 7,6% | +2,3 pp | Revisar: el múltiplo supone más crecimiento que el DCF. |
| EV/FCFF | 21,8x | 5,4% | +0,1 pp | Coherente con el DCF. |
| P/E | 29,3x | 9,0% | +3,8 pp | Revisar: el múltiplo supone más crecimiento que el DCF. |
| P/FCFE | 22,6x | 7,0% | +1,7 pp | Coherente con el DCF. |
| P/OCF | 20,3x | 7,3% | +2,0 pp | Coherente con el DCF. |

Más de 2 pp de diferencia significa que el múltiplo (o el precio) cuenta otra historia de crecimiento que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (subir el crecimiento del DCF si la evidencia lo sostiene, o acercar el múltiplo al justificado si no).

## 7. Sensibilidad del valor ponderado hoy (Base)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$19,40 | — |
| Múltiplos Base +20% | US$21,11 | +8,8% |
| Múltiplos Base −20% | US$17,68 | −8,8% |
| Crecimiento años 1-5 +2 pp | US$20,48 | +5,6% |
| Crecimiento años 1-5 −2 pp | US$18,42 | −5,1% |
| Margen objetivo +3 pp | US$21,45 | +10,6% |
| Margen objetivo −3 pp | US$17,34 | −10,6% |
| WACC +1 pp | US$18,80 | −3,1% |
| WACC −1 pp | US$20,04 | +3,3% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo −3 pp, Margen objetivo +3 pp, Múltiplos Base −20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 21,18 | 21,18 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 23,03 | 23,03 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 25,58 | 25,58 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 20,46 | 19,96 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 22,56 | 21,84 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 27,96 | 26,96 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 25,77 | 25,77 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 29,28 | 29,28 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 34,64 | 34,64 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 20,90 | 20,90 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 22,65 | 22,65 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 26,54 | 26,54 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 18,14 | 18,14 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 20,32 | 20,32 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 23,89 | 23,89 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/CELH_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1pl_6BeI9gl_ciaSY5wDqyjRF9GS-ZhjXXK4wGVuBC4o/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (MNST, KDP, PEP, KO, BRBR, COCO).
- [Celsius Holdings, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1341766/000134176626000024/celh-20251231.htm): costos de la adquisición de Alani Nu y terminación de distribuidores.

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
