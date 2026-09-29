---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de PagSeguro Digital Ltd."
ticker: "PAGS"
analysis_date: "2026-09-29"
sheet: "https://docs.google.com/spreadsheets/d/1Q17gaT8w8fGx-3uRn7eCS_HsF0q-HZucEtgXGtVEIQY/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# PagSeguro Digital Ltd. (PAGS) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$12,53 en el escenario Base (rango US$9,47–US$15,69). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$8,36 (−33% frente al DCF). Con los pesos de la categoría «Financiera» (40% DCF, 60% múltiplos), el valor intrínseco ponderado hoy es US$10,03, frente a un precio de referencia de US$8,90 (+13%).

Los múltiplos (US$8,36 hoy) quedan 33% por debajo del DCF (US$12,53). La diferencia viene casi toda de P/FCFE (US$2,8, peso 20%): en la proyección Base el crédito que otorga PagBank absorbe caja (cambio en capital de trabajo de ~US$215-240 millones al año), y el FCFE de FY+3 queda en US$0,41 por acción frente a una utilidad de US$1,77. P/E, el método más confiable para una financiera, da US$11,9, cerca del DCF. Queda a tu decisión: revisar el supuesto de capital de trabajo o mover el peso de P/FCFE a P/E en la categoría Financiera (el prompt v3 pide hacerlo en la tabla compartida y registrarlo).

| Escenario | DCF hoy | Múltiplos consolidados hoy | Valor intrínseco ponderado hoy | Compra con MOS hoy | Precio objetivo FY+3 ponderado |
|---|---:|---:|---:|---:|---:|
| Conservador | US$9,47 | US$6,42 | US$7,64 | US$4,96 | US$11,00 |
| Base | US$12,53 | US$8,36 | US$10,03 | US$6,52 | US$15,07 |
| Optimista | US$15,69 | US$10,01 | US$12,28 | US$7,98 | US$19,25 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - PAGS](https://docs.google.com/spreadsheets/d/1Q17gaT8w8fGx-3uRn7eCS_HsF0q-HZucEtgXGtVEIQY/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$8,90.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 2,0% | 5,0% | 9,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 2,0% | 6,0% | 9,0% | Input B29 |
| Margen EBIT objetivo | 11,0% | 14,0% | 16,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,40 / 1,40 | — | Input B32/B33 |
| DCF por acción hoy | US$9,47 | US$12,53 | US$15,69 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,30, ERP 7,47%, Ke 14,70%, costo de la deuda después de impuestos 4,78%, peso del patrimonio 99,5%, WACC inicial 14,65% y terminal 12,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: PagSeguro cotiza a 5-12x utilidades desde 2022; no hay un cambio de etapa. Se usa la mediana de los últimos cierres depurados, sin la columna sin fecha. B: pagos y banca digital (StoneCo, Nu, dLocal, PayPal, Adyen), datos de yfinance al 29-sep-2026. Se excluye en P/E a Shift4 (58x por amortización y deuda) y, en los múltiplos de flujo, StoneCo (su flujo incluye los fondos de clientes: P/FCF de 0,6x). Ajuste −30%: PagSeguro crece ~5% y opera en Brasil con Selic alta (costo de patrimonio de 14,7%), frente a Nu, dLocal y Adyen que crecen 20-50%. λ = 0,25: la PagSeguro de FY+3 del escenario Base es un banco digital de crecimiento moderado, parecida a la de hoy.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | No aplica: PagSeguro es una entidad financiera (PagBank): la deuda es materia prima del negocio, no financiación, y el valor empresa no tiene sentido; su peso en la categoría Financiera es 0%. | | | | | | |
| EV/FCFF | No aplica: Igual que EV/EBITDA: para una financiera el FCFF no se puede separar de la financiación; peso 0%. | | | | | | |
| P/E | mediana de los últimos 5 cierres + LTM depurados = 7,6x | 16,9x (n=5: STNE 3,5x, NU 16,9x, DLO 20,1x, PYPL 10,2x, ADYEY 24,5x) × 0,70 = 11,8x | 6,9x / 7,9x / 8,8x | 7,1x | **9,2x** | 11,1x | —x / 6,2x / —x |
| P/FCFE | mediana de los últimos 5 cierres + LTM depurados = 6,5x | 10,1x (n=3: DLO 10,4x, FOUR 10,1x, PYPL 7,0x) × 0,70 = 7,1x | 9,9x / 11,2x / 12,4x | 5,7x | **7,9x** | 9,7x | —x / 2,5x / —x |
| P/OCF | mediana de los últimos 5 cierres + LTM depurados = 3,1x | 6,2x (n=3: DLO 9,4x, FOUR 4,9x, PYPL 6,2x) × 0,70 = 4,3x | 2,7x / 2,0x / 1,1x | 3,2x | **3,3x** | 3,5x | —x / 1,7x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **P/E.** Base 9,2x: promedio de historia y peers 9,7x, acercado 25% al justificado (7,9x); rango de anclas 7,6x–11,8x. Atípicos excluidos de la historia: Dec '21 (39,7x: > 2,5x la mediana (8.7x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 7,9x: promedio de historia y peers 6,8x, acercado 25% al justificado (11,2x); rango de anclas 6,5x–11,2x. Atípicos excluidos de la historia: Dec '21 (-54,5x: métrica negativa o ~0); Dec '24 (-1,9x: métrica negativa o ~0). Aplicable con cautela: el FCFE proyectado es positivo pero bajo frente a la utilidad porque el crecimiento de la cartera de crédito consume caja. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 3,3x: promedio de historia y peers 3,7x, acercado 25% al justificado (2,0x); rango de anclas 2,0x–4,3x. Atípicos excluidos de la historia: Dec '24 (-3,1x: métrica negativa o ~0); Dec '21 (51,8x: > 2,5x la mediana (4.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$8,36 frente a US$12,53 del DCF (−33%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$8,36 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$14,28 | US$18,92 | US$23,68 |
| EV/EBITDA | 0% | US$8,96 | US$11,62 | US$14,47 |
| EV/FCFF | 0% | US$2,64 | US$2,21 | US$1,74 |
| P/E | 35% | US$11,02 | US$17,63 | US$24,79 |
| P/FCFE | 20% | US$4,94 | US$4,48 | US$3,19 |
| P/OCF | 5% | US$8,77 | US$8,84 | US$9,32 |
| **Ponderado FY+3** | 100% | US$11,00 | US$15,07 | US$19,25 |

Valor presente (Ke 14,70%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$7,07 | US$6,44 | US$5,93 | US$6,48 | OK |
| EV/EBITDA | Base | US$8,04 | US$7,95 | US$7,70 | US$7,90 | OK |
| EV/EBITDA | Optimista | US$9,13 | US$9,55 | US$9,59 | US$9,42 | OK |
| EV/FCFF | Conservador | US$1,69 | US$1,71 | US$1,75 | US$1,72 | OK |
| EV/FCFF | Base | US$1,09 | US$1,23 | US$1,46 | US$1,26 | OK |
| EV/FCFF | Optimista | US$0,07 | US$0,76 | US$1,15 | US$0,66 | OK |
| P/E | Conservador | US$8,98 | US$8,01 | US$7,30 | US$8,10 | OK |
| P/E | Base | US$11,95 | US$11,98 | US$11,68 | US$11,87 | OK |
| P/E | Optimista | US$14,83 | US$16,09 | US$16,42 | US$15,78 | OK |
| P/FCFE | Conservador | US$3,82 | US$3,47 | US$3,28 | US$3,52 | OK |
| P/FCFE | Base | US$2,80 | US$2,65 | US$2,97 | US$2,81 | OK |
| P/FCFE | Optimista | US$-0,47 | US$1,23 | US$2,11 | US$0,96 | OK |
| P/OCF | Conservador | US$6,76 | US$6,24 | US$5,81 | US$6,27 | OK |
| P/OCF | Base | US$6,12 | US$5,91 | US$5,86 | US$5,96 | OK |
| P/OCF | Optimista | US$5,34 | US$5,93 | US$6,17 | US$5,81 | OK |

Múltiplos consolidados hoy: US$6,42 / US$8,36 / US$10,01 · DCF hoy: US$9,47 / US$12,53 / US$15,69 · Ponderado hoy: US$7,64 / US$10,03 / US$12,28 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para PAGS la diferencia es de −33% (múltiplos por debajo del DCF). Los múltiplos (US$8,36 hoy) quedan 33% por debajo del DCF (US$12,53). La diferencia viene casi toda de P/FCFE (US$2,8, peso 20%): en la proyección Base el crédito que otorga PagBank absorbe caja (cambio en capital de trabajo de ~US$215-240 millones al año), y el FCFE de FY+3 queda en US$0,41 por acción frente a una utilidad de US$1,77. P/E, el método más confiable para una financiera, da US$11,9, cerca del DCF. Queda a tu decisión: revisar el supuesto de capital de trabajo o mover el peso de P/FCFE a P/E en la categoría Financiera (el prompt v3 pide hacerlo en la tabla compartida y registrarlo).

## 7. Sensibilidad del valor ponderado hoy (Base)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$10,03 | — |
| Múltiplos Base +20% | US$10,96 | +9,3% |
| Múltiplos Base −20% | US$9,10 | −9,3% |
| Crecimiento años 1-5 +2 pp | US$10,21 | +1,8% |
| Crecimiento años 1-5 −2 pp | US$9,86 | −1,7% |
| Margen objetivo +3 pp | US$11,15 | +11,2% |
| Margen objetivo −3 pp | US$8,91 | −11,2% |
| WACC +1 pp | US$9,79 | −2,4% |
| WACC −1 pp | US$10,28 | +2,5% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Margen objetivo −3 pp, Múltiplos Base +20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| PE | J8 | — | 7,08 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 6,16 | 9,25 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 11,12 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 5,69 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 2,50 | 7,88 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 9,66 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 3,17 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 1,75 | 3,27 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 3,51 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/PAGS_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1Q17gaT8w8fGx-3uRn7eCS_HsF0q-HZucEtgXGtVEIQY/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (STNE, NU, DLO, FOUR, PYPL, ADYEY).
- [Nasdaq: puntos del 1T26 de PagSeguro](https://www.nasdaq.com/articles/pagseguro-digital-q1-earnings-call-highlights)

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
