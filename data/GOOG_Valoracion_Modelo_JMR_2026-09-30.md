---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Alphabet Inc."
ticker: "GOOG"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1yt2zqdGz1JWEqV3SYqqL-nHarO7C1Oud1lvR3pY9i0U/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Alphabet Inc. (GOOG) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$311,55 en el escenario Base (rango US$244,12–US$434,60). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$228,88 (−27% frente al DCF). Con los pesos de la categoría «Madura» (40% DCF, 60% múltiplos), el ponderado hoy (lectura secundaria) es US$261,95. El valor intrínseco es el DCF: US$311,55 frente a un precio de referencia de US$339,16 (−8%).

Revisión del 30-sep-2026 (ROIC terminal): con un ROIC después del año 10 de 28,6% el DCF pasa de US$206,14 a US$311,58. Los múltiplos (US$228,88 hoy) quedan 27% por debajo del DCF, fuera del rango de ±25%; el precio (US$339,16) está por encima de ambos. Lectura anterior, con el DCF sin ROIC terminal: Tras la revisión del DCF del 30-sep-2026 (crecimiento 18% / 11%, sales-to-capital 1,2 por el capex de IA de US$195-205 mil millones, margen 35%, beta 1,07), el DCF da US$206,14 y los múltiplos US$228,88 hoy: 11% por encima, dentro del rango de ±25%, así que ambos métodos coinciden. Los dos quedan muy por debajo del precio (US$339,16): el mercado descuenta más crecimiento de Cloud e IA, y más duración, que el escenario Base. Además, las participaciones de Alphabet en otras empresas (que generaron US$135,9 mil millones de ganancias en el 1S26) no están en los múltiplos operativos; conviene revisar que la hoja las incluya a valor actual como activos no operativos.

| Escenario | DCF hoy (valor intrínseco) | Múltiplos consolidados hoy (secundario) | Ponderado hoy (secundario) | Compra con MOS sobre el DCF | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$244,12 | US$182,79 | US$207,32 | US$158,68 | US$273,83 |
| Base | US$311,55 | US$228,88 | US$261,95 | US$202,51 | US$354,10 |
| Optimista | US$434,60 | US$336,57 | US$375,78 | US$282,49 | US$529,34 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - Alphabet (GOOG)](https://docs.google.com/spreadsheets/d/1yt2zqdGz1JWEqV3SYqqL-nHarO7C1Oud1lvR3pY9i0U/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$339,16.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 9,0% | 18,0% | 16,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 9,0% | 11,0% | 16,0% | Input B29 |
| Margen EBIT objetivo | 31,0% | 35,0% | 38,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,20 / 1,50 | — | Input B32/B33 |
| DCF por acción hoy | US$244,12 | US$311,55 | US$434,60 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,07, ERP 4,46%, Ke 9,76%, costo de la deuda después de impuestos 4,65%, peso del patrimonio 98,8%, WACC inicial 9,70% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: los cierres 2016-2021 de la hoja dan múltiplos de ~1x porque el precio no está ajustado por el split 20:1 de julio de 2022; no son representativos y se usa la historia desde Dec '22. En P/E se quita el LTM: la utilidad del primer semestre de 2026 incluye US$135,9 mil millones de ganancias en acciones de otras empresas, que bajan el P/E a 17x. En EV/FCFF y P/FCFE se quita el LTM: el capex de 2026 (US$195-205 mil millones) deja el flujo de caja en mínimos y el múltiplo en ~78x, un pico transitorio frente al flujo de FY+3. B: grandes plataformas tecnológicas (Meta, Microsoft, Amazon, Apple, Netflix), datos de yfinance al 29-sep-2026. Amazon no tiene flujo de caja libre positivo y no entra en los múltiplos de flujo. Sin ajuste: Alphabet crece 24% con margen operativo de 34%, en línea con Meta y Microsoft. λ = 0,25: la Alphabet de FY+3 del escenario Base sigue siendo una plataforma de crecimiento alto con fuerte inversión en IA, parecida a la de hoy.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,3x | 19,7x (n=5: META 17,4x, MSFT 19,7x, AMZN 16,5x, AAPL 28,8x, NFLX 20,1x) × 1,00 = 19,7x | 9,9x / 10,7x / 33,3x | 15,8x | **16,9x** | 25,5x | —x / 13,0x / —x |
| EV/FCFF | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 31,2x (EV/FCF × 1,09 = FCF después de intereses ÷ FCFF) | 40,0x (n=4: META 44,7x, MSFT 55,2x, AAPL 35,3x, NFLX 25,0x) × 1,00 = 40,0x | 25,9x / 27,9x / 89,2x | 28,9x | **33,7x** | 52,2x | —x / 15,4x / —x |
| P/E | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 24,0x | 27,8x (n=5: META 27,8x, MSFT 28,4x, AMZN 19,8x, AAPL 37,7x, NFLX 22,1x) × 1,00 = 27,8x | 20,2x / 21,8x / 58,4x | 22,1x | **24,9x** | 29,0x | —x / 19,0x / —x |
| P/FCFE | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 28,6x | 40,5x (n=4: META 45,9x, MSFT 56,4x, AAPL 35,2x, NFLX 26,2x) × 1,00 = 40,5x | 24,0x / 25,7x / 70,3x | 27,8x | **32,4x** | 51,8x | —x / 16,0x / —x |
| P/OCF | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,6x | 20,7x (n=5: META 14,4x, MSFT 20,7x, AMZN 17,9x, AAPL 32,8x, NFLX 24,5x) × 1,00 = 20,7x | 12,9x / 14,0x / 41,0x | 16,5x | **18,2x** | 23,0x | —x / 11,1x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 16,9x: promedio de historia y peers 19,0x, acercado 25% al justificado (10,7x); rango de anclas 10,7x–19,7x. Atípicos excluidos de la historia: Dec '22 (13,0x: > 2,5x la mediana (1.5x)); Dec '23 (18,3x: > 2,5x la mediana (1.5x)); Dec '24 (18,2x: > 2,5x la mediana (1.5x)); Dec '25 (25,5x: > 2,5x la mediana (1.5x)); LTM (24,8x: > 2,5x la mediana (1.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 33,7x: promedio de historia y peers 35,6x, acercado 25% al justificado (27,9x); rango de anclas 27,9x–40,0x. Atípicos excluidos de la historia: Dec '22 (19,1x: > 2,5x la mediana (1.5x)); Dec '23 (25,3x: > 2,5x la mediana (1.5x)); Dec '24 (32,0x: > 2,5x la mediana (1.5x)); Dec '25 (52,2x: > 2,5x la mediana (1.5x)); LTM (78,4x: > 2,5x la mediana (1.5x)). EV/FCFF: la razón FCF después de intereses ÷ FCFF se fija en 1,09 (mediana de los tres cierres reales); el último cierre da 2,70 porque 'Interest / Other' incluye ganancias en inversiones, no intereses. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 24,9x: promedio de historia y peers 25,9x, acercado 25% al justificado (21,8x); rango de anclas 21,8x–27,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 32,4x: promedio de historia y peers 34,6x, acercado 25% al justificado (25,7x); rango de anclas 25,7x–40,5x. Atípicos excluidos de la historia: Dec '22 (19,0x: > 2,5x la mediana (1.6x)); Dec '23 (25,3x: > 2,5x la mediana (1.6x)); Dec '24 (32,0x: > 2,5x la mediana (1.6x)); Dec '25 (51,8x: > 2,5x la mediana (1.6x)); LTM (78,3x: > 2,5x la mediana (1.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 18,2x: promedio de historia y peers 19,6x, acercado 25% al justificado (14,0x); rango de anclas 14,0x–20,7x. Atípicos excluidos de la historia: Dec '22 (12,5x: > 2,5x la mediana (1.0x)); Dec '23 (17,3x: > 2,5x la mediana (1.0x)); Dec '24 (18,6x: > 2,5x la mediana (1.0x)); Dec '25 (23,0x: > 2,5x la mediana (1.0x)); LTM (22,5x: > 2,5x la mediana (1.0x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$228,88 frente a US$311,55 del DCF (−27%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$228,88 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$322,85 | US$412,03 | US$574,75 |
| EV/EBITDA | 20% | US$247,35 | US$309,48 | US$533,75 |
| EV/FCFF | 10% | US$162,74 | US$227,04 | US$416,12 |
| P/E | 20% | US$282,99 | US$373,99 | US$505,62 |
| P/FCFE | 5% | US$210,97 | US$295,98 | US$569,26 |
| P/OCF | 5% | US$235,92 | US$301,77 | US$429,91 |
| **Ponderado FY+3** | 100% | US$273,83 | US$354,10 | US$529,34 |

Valor presente (Ke 9,76%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$191,47 | US$188,77 | US$187,05 | US$189,10 | OK |
| EV/EBITDA | Base | US$222,19 | US$229,01 | US$234,03 | US$228,41 | OK |
| EV/EBITDA | Optimista | US$328,30 | US$370,12 | US$403,63 | US$367,35 | OK |
| EV/FCFF | Conservador | US$127,53 | US$124,63 | US$123,06 | US$125,07 | OK |
| EV/FCFF | Base | US$145,39 | US$165,95 | US$171,69 | US$161,01 | OK |
| EV/FCFF | Optimista | US$226,04 | US$277,93 | US$314,67 | US$272,88 | OK |
| P/E | Conservador | US$212,52 | US$212,35 | US$214,00 | US$212,96 | OK |
| P/E | Base | US$258,94 | US$271,53 | US$282,82 | US$271,10 | OK |
| P/E | Optimista | US$296,78 | US$342,79 | US$382,36 | US$340,64 | OK |
| P/FCFE | Conservador | US$158,28 | US$158,17 | US$159,54 | US$158,66 | OK |
| P/FCFE | Base | US$195,84 | US$212,65 | US$223,82 | US$210,77 | OK |
| P/FCFE | Optimista | US$308,78 | US$376,70 | US$430,48 | US$371,98 | OK |
| P/OCF | Conservador | US$174,76 | US$176,16 | US$178,40 | US$176,44 | OK |
| P/OCF | Base | US$200,73 | US$218,39 | US$228,20 | US$215,78 | OK |
| P/OCF | Optimista | US$251,39 | US$291,06 | US$325,10 | US$289,18 | OK |

Múltiplos consolidados hoy: US$182,79 / US$228,88 / US$336,57 · DCF hoy: US$244,12 / US$311,55 / US$434,60 · Ponderado hoy: US$207,32 / US$261,95 / US$375,78 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para GOOG la diferencia es de −27% (múltiplos por debajo del DCF). Revisión del 30-sep-2026 (ROIC terminal): con un ROIC después del año 10 de 28,6% el DCF pasa de US$206,14 a US$311,58. Los múltiplos (US$228,88 hoy) quedan 27% por debajo del DCF, fuera del rango de ±25%; el precio (US$339,16) está por encima de ambos. Lectura anterior, con el DCF sin ROIC terminal: Tras la revisión del DCF del 30-sep-2026 (crecimiento 18% / 11%, sales-to-capital 1,2 por el capex de IA de US$195-205 mil millones, margen 35%, beta 1,07), el DCF da US$206,14 y los múltiplos US$228,88 hoy: 11% por encima, dentro del rango de ±25%, así que ambos métodos coinciden. Los dos quedan muy por debajo del precio (US$339,16): el mercado descuenta más crecimiento de Cloud e IA, y más duración, que el escenario Base. Además, las participaciones de Alphabet en otras empresas (que generaron US$135,9 mil millones de ganancias en el 1S26) no están en los múltiplos operativos; conviene revisar que la hoja las incluya a valor actual como activos no operativos.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$339,16 supone que los ingresos crecen 14,0% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 12,4% (+1,6 pp). Coherente: el precio supone un crecimiento parecido al del DCF.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$412,03 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,7%, WACC de los años 4-10 9,3%, ROE de FY+3 36,8% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 16,9x | 22,6x | −25% | 6,9% | 7,5% | −0,6 pp | Coherente con el DCF. |
| EV/FCFF | 33,7x | 61,4x | −45% | 6,2% | 7,6% | −1,4 pp | Revisar: el múltiplo vale 45% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 24,9x | 27,4x | −9% | 6,1% | 6,5% | −0,4 pp | Coherente con el DCF. |
| P/FCFE | 32,4x | 45,2x | −28% | 6,4% | 7,3% | −0,9 pp | Revisar: el múltiplo vale 28% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 18,2x | 24,9x | −27% | 6,5% | 7,3% | −0,8 pp | Revisar: el múltiplo vale 27% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$261,95 | — |
| Múltiplos Base +20% | US$289,28 | +10,4% |
| Múltiplos Base −20% | US$234,62 | −10,4% |
| Crecimiento años 1-5 +2 pp | US$275,53 | +5,2% |
| Crecimiento años 1-5 −2 pp | US$249,66 | −4,7% |
| Margen objetivo +3 pp | US$273,84 | +4,5% |
| Margen objetivo −3 pp | US$250,06 | −4,5% |
| WACC +1 pp | US$254,60 | −2,8% |
| WACC −1 pp | US$269,84 | +3,0% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 1-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 15,79 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 12,98 | 16,93 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 25,46 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 28,93 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 15,44 | 33,70 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 52,19 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 22,10 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 19,01 | 24,89 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 29,03 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 27,76 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 16,02 | 32,36 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 51,77 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 16,48 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 11,09 | 18,22 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 23,03 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/GOOG_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1yt2zqdGz1JWEqV3SYqqL-nHarO7C1Oud1lvR3pY9i0U/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (META, MSFT, AMZN, AAPL, NFLX).
- [Alphabet, 8-K 2T26: ganancias en acciones y capex](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm)
- [Yahoo Finance: Alphabet sube el capex a US$205 mil millones y el flujo de caja se vuelve negativo](https://finance.yahoo.com/markets/stocks/articles/alphabet-lifts-capex-205-billion-123356486.html)

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
