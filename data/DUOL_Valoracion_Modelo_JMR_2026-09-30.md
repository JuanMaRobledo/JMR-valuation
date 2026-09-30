---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Duolingo, Inc."
ticker: "DUOL"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1k-ms7Yt54Or8wgUFD2LIuH1nvmgEmiJh_h_2hQwbL10/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Duolingo, Inc. (DUOL) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$167,58 en el escenario Base (rango US$125,17–US$250,94). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$150,14 (−10% frente al DCF). Con los pesos de la categoría «Software» (60% DCF, 40% múltiplos), el valor intrínseco ponderado hoy es US$160,60, frente a un precio de referencia de US$134,30 (+20%).

Los múltiplos (US$150,14 hoy) quedan 10% por debajo del DCF (US$167,58). Los múltiplos anteriores (P/E 66x, P/FCFE 61x, P/OCF 55x) no tenían respaldo en el mercado ni en la historia reciente y hacían que el valor por múltiplos coincidiera casi exactamente con el DCF. Ahora salen de peers de hoy, del FY25/LTM y de los fundamentales. Para Duolingo el DCF es más informativo, porque la empresa sigue en crecimiento y su historia de múltiplos es corta y ruidosa.

| Escenario | DCF hoy | Múltiplos consolidados hoy | Valor intrínseco ponderado hoy | Compra con MOS hoy | Precio objetivo FY+3 ponderado |
|---|---:|---:|---:|---:|---:|
| Conservador | US$125,17 | US$120,90 | US$123,46 | US$80,25 | US$169,20 |
| Base | US$167,58 | US$150,14 | US$160,60 | US$104,39 | US$225,75 |
| Optimista | US$250,94 | US$183,01 | US$223,77 | US$145,45 | US$322,59 |

## 2. Datos

- Hoja del modelo: [DUOL análisis maestro](https://docs.google.com/spreadsheets/d/1k-ms7Yt54Or8wgUFD2LIuH1nvmgEmiJh_h_2hQwbL10/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$134,30.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 15,0% | 19,0% | 23,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 15,0% | 16,0% | 23,0% | Input B29 |
| Margen EBIT objetivo | 21,8% | 30,0% | 35,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 4,00 / 4,50 | — | Input B32/B33 |
| DCF por acción hoy | US$125,17 | US$167,58 | US$250,94 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,35, ERP 4,46%, Ke 11,00%, costo de la deuda después de impuestos 5,25%, peso del patrimonio 99,0%, WACC inicial 10,94% y terminal 9,22%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Duolingo salió a bolsa en 2021 y hasta 2023 tuvo utilidades cercanas a cero, con múltiplos de 50-650x que reflejan hipercrecimiento; tras la desaceleración de usuarios de 2025 el mercado la re-valoró, así que A usa solo el cierre FY25 y el LTM. El P/E del FY25 y del LTM se excluye: la utilidad incluye un beneficio tributario único de US$222,7 millones por la liberación de la reserva de valuación de impuestos diferidos (10-Q del 3T25 y 10-K FY2025); sin él, el P/E real es mucho más alto y los años anteriores no son representativos, así que el P/E se ancla en peers y fundamentales. B: suscripción de consumo y plataformas digitales con datos de yfinance al 29-sep-2026: Spotify, Netflix, Reddit y Pinterest. Se excluyen Bumble (ingresos −15%, acción en dificultades) y Match (ingresos en baja): están en otra etapa. Pinterest se excluye de P/E y EV/EBITDA porque su margen operativo GAAP es negativo. Ajuste 0%: Duolingo crece más que Spotify y Netflix (Base 19% el año 1 y 16% en los años 2-5, frente a ~13-14%), lo que justificaría una prima de ~10%, pero tiene una desaceleración reciente de usuarios, menor escala y riesgo de sustitución por asistentes de IA para aprender idiomas, que justifican un descuento similar. λ = 0,15: el múltiplo justificado es inestable para Duolingo porque su crecimiento de largo plazo (g ≈ 8-10%) queda a solo 2-3 puntos del WACC y del Ke; en el Optimista no se puede calcular. Por eso pesa poco.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 43,5x | 31,4x (n=3: SPOT 35,4x, NFLX 20,1x, RDDT 31,4x) × 1,00 = 31,4x | 41,4x / 46,0x / — | 34,1x | **38,7x** | 41,5x | 34,0x / 38,5x / 41,5x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 23,4x (EV/FCF × 1,30 = FCF después de intereses ÷ FCFF) | 24,9x (n=4: SPOT 28,9x, NFLX 25,0x, PINS 8,1x, RDDT 24,7x) × 1,00 = 24,9x | 45,8x / 52,3x / — | 24,9x | **28,4x** | 30,0x | 22,8x / 26,3x / 28,1x |
| P/E | sin historia representativa (El P/E del FY25 y del LTM se excluye: la utilidad incluye un beneficio tributario único de US$222,7 millones por la liberación de la reserva de valuación de impuestos diferidos (10-Q del 3T25 y 10-K FY2025); sin él, el P/E real es mucho más alto y los años anteriores no son representativos, así que el P/E se ancla en peers y fundamentales.) | 27,3x (n=3: SPOT 27,3x, NFLX 22,1x, RDDT 33,7x) × 1,00 = 27,3x | 12,0x / 17,1x / — | 20,7x | **25,7x** | 28,8x | 20,7x / 25,7x / 28,8x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 20,6x | 26,9x (n=4: SPOT 31,1x, NFLX 26,2x, PINS 8,2x, RDDT 27,5x) × 1,00 = 26,9x | 34,2x / 37,8x / — | 22,9x | **25,8x** | 27,3x | 22,9x / 25,8x / 27,3x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 19,6x | 25,9x (n=4: SPOT 30,4x, NFLX 24,5x, PINS 7,9x, RDDT 27,3x) × 1,00 = 25,9x | 33,6x / 37,2x / — | 21,8x | **24,9x** | 26,7x | 21,8x / 24,9x / 26,7x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 38,7x: promedio de historia y peers 37,5x, acercado 15% al justificado (46,0x); rango de anclas 31,4x–46,0x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (-34,2x: métrica negativa o ~0); Dec '22 (-36,9x: métrica negativa o ~0); Dec '23 (-1.584,2x: métrica negativa o ~0); Dec '24 (198,1x: > 2,5x la mediana (50.2x)). El EBITDA GAAP de Duolingo descuenta una compensación en acciones alta, por eso su múltiplo EV/EBITDA es mayor que el de los peers. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 28,4x: promedio de historia y peers 24,2x, acercado 15% al justificado (52,3x); rango de anclas 23,4x–52,3x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (349,7x: > 2,5x la mediana (49.7x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 25,7x: promedio de historia y peers 27,3x, acercado 15% al justificado (17,1x); rango de anclas 17,1x–27,3x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (-41,3x: métrica negativa o ~0); Dec '22 (-47,1x: métrica negativa o ~0); Dec '23 (648,1x: > 2,5x la mediana (96.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 25,8x: promedio de historia y peers 23,7x, acercado 15% al justificado (37,8x); rango de anclas 20,6x–37,8x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (443,4x: > 2,5x la mediana (57.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 24,9x: promedio de historia y peers 22,7x, acercado 15% al justificado (37,2x); rango de anclas 19,6x–37,2x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (269,9x: > 2,5x la mediana (52.9x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$150,14 frente a US$167,58 del DCF (−10%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$150,14 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$171,18 | US$229,19 | US$343,19 |
| EV/EBITDA | 10% | US$265,15 | US$355,85 | US$468,95 |
| EV/FCFF | 15% | US$185,44 | US$240,16 | US$312,09 |
| P/E | 5% | US$66,16 | US$101,55 | US$143,65 |
| P/FCFE | 5% | US$89,82 | US$116,82 | US$160,72 |
| P/OCF | 5% | US$87,25 | US$114,17 | US$154,99 |
| **Ponderado FY+3** | 100% | US$169,20 | US$225,75 | US$322,59 |

Valor presente (Ke 11,00%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$191,20 | US$193,38 | US$193,87 | US$192,82 | OK |
| EV/EBITDA | Base | US$219,66 | US$245,96 | US$260,19 | US$241,94 | OK |
| EV/EBITDA | Optimista | US$239,93 | US$299,35 | US$342,89 | US$294,06 | OK |
| EV/FCFF | Conservador | US$136,05 | US$136,32 | US$135,59 | US$135,99 | OK |
| EV/FCFF | Base | US$151,71 | US$167,30 | US$175,60 | US$164,87 | OK |
| EV/FCFF | Optimista | US$163,71 | US$201,09 | US$228,19 | US$197,66 | OK |
| P/E | Conservador | US$45,67 | US$47,30 | US$48,38 | US$47,12 | OK |
| P/E | Base | US$58,88 | US$68,58 | US$74,25 | US$67,24 | OK |
| P/E | Optimista | US$68,07 | US$89,32 | US$105,03 | US$87,48 | OK |
| P/FCFE | Conservador | US$62,41 | US$64,44 | US$65,67 | US$64,17 | OK |
| P/FCFE | Base | US$71,15 | US$79,61 | US$85,42 | US$78,72 | OK |
| P/FCFE | Optimista | US$79,88 | US$101,39 | US$117,51 | US$99,59 | OK |
| P/OCF | Conservador | US$60,67 | US$62,61 | US$63,80 | US$62,36 | OK |
| P/OCF | Base | US$68,67 | US$77,86 | US$83,48 | US$76,67 | OK |
| P/OCF | Optimista | US$76,76 | US$97,68 | US$113,33 | US$95,92 | OK |

Múltiplos consolidados hoy: US$120,90 / US$150,14 / US$183,01 · DCF hoy: US$125,17 / US$167,58 / US$250,94 · Ponderado hoy: US$123,46 / US$160,60 / US$223,77 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para DUOL la diferencia es de −10% (múltiplos por debajo del DCF). Los múltiplos (US$150,14 hoy) quedan 10% por debajo del DCF (US$167,58). Los múltiplos anteriores (P/E 66x, P/FCFE 61x, P/OCF 55x) no tenían respaldo en el mercado ni en la historia reciente y hacían que el valor por múltiplos coincidiera casi exactamente con el DCF. Ahora salen de peers de hoy, del FY25/LTM y de los fundamentales. Para Duolingo el DCF es más informativo, porque la empresa sigue en crecimiento y su historia de múltiplos es corta y ruidosa.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$134,30 supone que los ingresos crecen 10,9% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 16,6% (−5,7 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Crecimiento perpetuo después de FY+3 que supone cada múltiplo Base, con Ke 11,0%, WACC de los años 4-10 10,2% y ROE de FY+3 14,9%, frente al crecimiento del DCF (8,1%: punto medio entre los años 4-10 y la perpetuidad):

| Múltiplo Base FY+3 | Múltiplo | Crecimiento implícito | Diferencia vs. DCF | Lectura |
|---|---:|---:|---:|---|
| EV/EBITDA | 38,7x | 7,8% | −0,4 pp | Coherente con el DCF. |
| EV/FCFF | 28,4x | 6,5% | −1,7 pp | Coherente con el DCF. |
| P/E | 25,7x | 9,4% | +1,3 pp | Coherente con el DCF. |
| P/FCFE | 25,8x | 6,9% | −1,3 pp | Coherente con el DCF. |
| P/OCF | 24,9x | 6,8% | −1,4 pp | Coherente con el DCF. |

Más de 2 pp de diferencia significa que el múltiplo (o el precio) cuenta otra historia de crecimiento que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (subir el crecimiento del DCF si la evidencia lo sostiene, o acercar el múltiplo al justificado si no).

## 7. Sensibilidad del valor ponderado hoy (Base)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$160,60 | — |
| Múltiplos Base +20% | US$171,34 | +6,7% |
| Múltiplos Base −20% | US$149,86 | −6,7% |
| Crecimiento años 1-5 +2 pp | US$169,14 | +5,3% |
| Crecimiento años 1-5 −2 pp | US$152,84 | −4,8% |
| Margen objetivo +3 pp | US$169,60 | +5,6% |
| Margen objetivo −3 pp | US$151,61 | −5,6% |
| WACC +1 pp | US$156,15 | −2,8% |
| WACC −1 pp | US$165,37 | +3,0% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Margen objetivo −3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 33,98 | 34,11 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 38,51 | 38,74 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 41,50 | 41,46 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 22,83 | 24,94 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 26,29 | 28,39 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 28,10 | 29,97 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 20,66 | 20,66 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 25,74 | 25,74 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 28,79 | 28,79 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 22,89 | 22,89 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 25,82 | 25,82 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 27,28 | 27,28 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 21,80 | 21,80 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 24,89 | 24,89 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 26,67 | 26,67 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/DUOL_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1k-ms7Yt54Or8wgUFD2LIuH1nvmgEmiJh_h_2hQwbL10/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (SPOT, NFLX, MTCH, PINS, BMBL, RDDT).
- [Duolingo, Form 10-Q del 3T25 (30-sep-2025)](https://www.sec.gov/Archives/edgar/data/1562088/000162828025049743/duol-20250930.htm): liberación de la reserva de valuación, beneficio tributario único de US$222,7 millones.
- [Duolingo, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1562088/000162828026012494/duol-20251231.htm): beneficio tributario de US$231,7 millones en 2025.

## 10. Control de calidad

| Comprobación | ¿Cumple? |
|---|---|
| No se cambiaron fórmulas, pesos ni estructura (solo J8/J19/J30 y textos) | Sí |
| Cada múltiplo Base tiene sus tres anclas con fuente y fecha | Sí, con limitación: P/E sin historia representativa (anclado en B y C) |
| Ningún múltiplo se derivó del DCF ni se ajustó después de verlo | Sí |
| Cada Base dentro del rango de sus anclas | Sí |
| Conservador < Base < Optimista en los cinco métodos; J8/J19/J30 escritos | Sí |
| Métodos no aplicables declarados | Sí |
| «Supuestos de los Múltiplos» A3 y A12 completos | Sí |
| DCF hoy, múltiplos hoy y ponderado hoy reportados por separado | Sí |
| Chequeo VP3 < FY+3 en OK en los tres escenarios | Sí |
| DCF Conservador < Base < Optimista | Sí |
