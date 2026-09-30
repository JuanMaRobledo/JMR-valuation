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

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$125,77 en el escenario Base (rango US$98,09–US$172,49). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$132,03 (+5% frente al DCF). Con los pesos de la categoría «Software» (60% DCF, 40% múltiplos), el ponderado hoy (lectura secundaria) es US$128,28. El valor intrínseco es el DCF: US$125,77 frente a un precio de referencia de US$134,30 (−6%).

Tras la revisión del DCF del 30-sep-2026 (crecimiento 12% / 11% según las reservas, margen objetivo 27%), el DCF da US$125,77 y los múltiplos US$132,03 hoy (5% por encima): los dos métodos cuentan ahora una historia parecida y quedan cerca del precio (US$134,30). Los múltiplos anteriores (P/E 66x, P/FCFE 61x, P/OCF 55x) no tenían respaldo en el mercado ni en la historia reciente; ahora salen de peers de hoy, del FY25/LTM y de los fundamentales. Dentro de los múltiplos hay mucha dispersión (EV/EBITDA US$214 frente a P/E US$59) porque el EBITDA ajustado excluye una compensación en acciones de ~15% de los ingresos; los métodos de flujo y el DCF son la referencia.

| Escenario | DCF hoy (valor intrínseco) | Múltiplos consolidados hoy (secundario) | Ponderado hoy (secundario) | Compra con MOS sobre el DCF | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$98,09 | US$106,75 | US$101,56 | US$63,76 | US$135,96 |
| Base | US$125,77 | US$132,03 | US$128,28 | US$81,75 | US$176,39 |
| Optimista | US$172,49 | US$158,14 | US$166,75 | US$112,12 | US$235,79 |

## 2. Datos

- Hoja del modelo: [DUOL análisis maestro](https://docs.google.com/spreadsheets/d/1k-ms7Yt54Or8wgUFD2LIuH1nvmgEmiJh_h_2hQwbL10/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$134,30.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 8,0% | 12,0% | 16,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 8,0% | 11,0% | 16,0% | Input B29 |
| Margen EBIT objetivo | 21,8% | 27,0% | 32,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 4,00 / 4,50 | — | Input B32/B33 |
| DCF por acción hoy | US$98,09 | US$125,77 | US$172,49 | Valuation output B86/B35/B137 |

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

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$132,03 frente a US$125,77 del DCF (+5%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$132,03 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$134,16 | US$172,01 | US$235,90 |
| EV/EBITDA | 10% | US$224,83 | US$296,83 | US$381,25 |
| EV/FCFF | 15% | US$155,55 | US$200,60 | US$253,65 |
| P/E | 5% | US$54,80 | US$82,88 | US$114,63 |
| P/FCFE | 5% | US$68,68 | US$92,55 | US$124,01 |
| P/OCF | 5% | US$69,42 | US$92,80 | US$122,87 |
| **Ponderado FY+3** | 100% | US$135,96 | US$176,39 | US$235,79 |

Valor presente (Ke 11,00%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$181,31 | US$173,54 | US$164,40 | US$173,08 | OK |
| EV/EBITDA | Base | US$208,43 | US$217,00 | US$217,04 | US$214,16 | OK |
| EV/EBITDA | Optimista | US$227,91 | US$260,92 | US$278,77 | US$255,87 | OK |
| EV/FCFF | Conservador | US$126,87 | US$120,69 | US$113,74 | US$120,43 | OK |
| EV/FCFF | Base | US$143,16 | US$147,58 | US$146,67 | US$145,80 | OK |
| EV/FCFF | Optimista | US$154,68 | US$174,96 | US$185,47 | US$171,70 | OK |
| P/E | Conservador | US$42,89 | US$41,72 | US$40,07 | US$41,56 | OK |
| P/E | Base | US$55,42 | US$59,45 | US$60,60 | US$58,49 | OK |
| P/E | Optimista | US$64,20 | US$76,64 | US$83,82 | US$74,88 | OK |
| P/FCFE | Conservador | US$53,97 | US$52,43 | US$50,22 | US$52,20 | OK |
| P/FCFE | Base | US$63,36 | US$66,77 | US$67,68 | US$65,93 | OK |
| P/FCFE | Optimista | US$71,65 | US$83,76 | US$90,68 | US$82,03 | OK |
| P/OCF | Conservador | US$54,66 | US$53,02 | US$50,76 | US$52,81 | OK |
| P/OCF | Base | US$63,47 | US$67,05 | US$67,85 | US$66,12 | OK |
| P/OCF | Optimista | US$71,19 | US$83,05 | US$89,84 | US$81,36 | OK |

Múltiplos consolidados hoy: US$106,75 / US$132,03 / US$158,14 · DCF hoy: US$98,09 / US$125,77 / US$172,49 · Ponderado hoy: US$101,56 / US$128,28 / US$166,75 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para DUOL la diferencia es de +5% (múltiplos por encima del DCF). Tras la revisión del DCF del 30-sep-2026 (crecimiento 12% / 11% según las reservas, margen objetivo 27%), el DCF da US$125,77 y los múltiplos US$132,03 hoy (5% por encima): los dos métodos cuentan ahora una historia parecida y quedan cerca del precio (US$134,30). Los múltiplos anteriores (P/E 66x, P/FCFE 61x, P/OCF 55x) no tenían respaldo en el mercado ni en la historia reciente; ahora salen de peers de hoy, del FY25/LTM y de los fundamentales. Dentro de los múltiplos hay mucha dispersión (EV/EBITDA US$214 frente a P/E US$59) porque el EBITDA ajustado excluye una compensación en acciones de ~15% de los ingresos; los métodos de flujo y el DCF son la referencia.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$134,30 supone que los ingresos crecen 13,0% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,2% (+1,8 pp). Coherente: el precio supone un crecimiento parecido al del DCF.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$172,01 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,0%, WACC de los años 4-10 10,2%, ROE de FY+3 14,9% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 38,7x | 20,6x | +73% | 7,8% | 5,7% | +2,1 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 73% por encima del DCF en FY+3. |
| EV/FCFF | 28,4x | 23,6x | +17% | 6,5% | 5,7% | +0,7 pp | Coherente con el DCF. |
| P/E | 25,7x | 53,4x | −52% | 9,4% | 10,4% | −0,9 pp | Revisar: el múltiplo vale 52% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 25,8x | 48,0x | −46% | 6,9% | 8,7% | −1,9 pp | Revisar: el múltiplo vale 46% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 24,9x | 46,1x | −46% | 6,8% | 8,7% | −1,9 pp | Revisar: el múltiplo vale 46% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$128,28 | — |
| Múltiplos Base +20% | US$137,57 | +7,2% |
| Múltiplos Base −20% | US$118,98 | −7,2% |
| Crecimiento años 1-5 +2 pp | US$134,12 | +4,6% |
| Crecimiento años 1-5 −2 pp | US$122,98 | −4,1% |
| Margen objetivo +3 pp | US$134,66 | +5,0% |
| Margen objetivo −3 pp | US$121,89 | −5,0% |
| WACC +1 pp | US$125,36 | −2,3% |
| WACC −1 pp | US$131,40 | +2,4% |

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
