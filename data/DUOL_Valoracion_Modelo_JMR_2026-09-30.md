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

**Valor intrínseco principal: DCF esperado de las cuatro historias, US$113,06.** Historia central A: US$119,64; rango US$59,88–US$155,74; precio con MOS 35% sobre el esperado: US$73,49; precio de referencia US$142,69. Cada historia es un DCF completo (hoja «Escenarios e historias»); el detalle está en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son la calibración técnica anterior de la hoja (Base US$119,73) y los múltiplos y el ponderado son lecturas secundarias.


| Historia | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| A · La audiencia crece y la monetización se recupera en parte | 40% | US$119,64 | US$47,86 |
| B · La monetización se estanca | 30% | US$93,58 | US$28,07 |
| C · Tesis de disrupción · Deterioro de los fundamentales: La IA generalista comoditiza los idiomas | 10% | US$59,88 | US$5,99 |
| D · La IA sube el ingreso por usuario | 20% | US$155,74 | US$31,15 |
| **DCF esperado** | 100% | **US$113,06** | |

Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$125,77 por acción y los múltiplos, US$121,75 hoy: 3% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

| Escenario | DCF técnico anterior hoy (calibración) | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$98,56 | US$97,00 | US$97,94 | US$73,49 | US$132,16 |
| Base | US$119,73 | US$120,34 | US$119,97 | US$73,49 | US$165,00 |
| Optimista | US$165,49 | US$169,51 | US$167,10 | US$73,49 | US$237,24 |

## 2. Datos

- Hoja del modelo: [DUOL análisis maestro](https://docs.google.com/spreadsheets/d/1k-ms7Yt54Or8wgUFD2LIuH1nvmgEmiJh_h_2hQwbL10/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$142,69.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 8,0% | 12,0% | 16,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 8,0% | 11,0% | 16,0% | Input B29 |
| Margen EBIT objetivo | 24,2% | 27,1% | 32,1% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,97 / 3,24 | — | Input B32/B33 |
| DCF por acción hoy | US$98,56 | US$119,73 | US$165,49 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,35, ERP 4,46%, Ke 11,01%, costo de la deuda después de impuestos 5,25%, peso del patrimonio 98,7%, WACC inicial 10,94% y terminal 9,22%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Duolingo salió a bolsa en 2021 y hasta 2023 tuvo utilidades cercanas a cero, con múltiplos de 50-650x que reflejan hipercrecimiento; tras la desaceleración de usuarios de 2025 el mercado la re-valoró, así que A usa solo el cierre FY25 y el LTM. El P/E del FY25 y del LTM se excluye: la utilidad incluye un beneficio tributario único de US$222,7 millones por la liberación de la reserva de valuación de impuestos diferidos (10-Q del 3T25 y 10-K FY2025); sin él, el P/E real es mucho más alto y los años anteriores no son representativos, así que el P/E se ancla en peers y fundamentales. B: suscripción de consumo y plataformas digitales con datos de yfinance al 29-sep-2026: Spotify, Netflix, Reddit y Pinterest. Se excluyen Bumble (ingresos −15%, acción en dificultades) y Match (ingresos en baja): están en otra etapa. Pinterest se excluye de P/E y EV/EBITDA porque su margen operativo GAAP es negativo. Ajuste 0%: Duolingo crece más que Spotify y Netflix (Base 19% el año 1 y 16% en los años 2-5, frente a ~13-14%), lo que justificaría una prima de ~10%, pero tiene una desaceleración reciente de usuarios, menor escala y riesgo de sustitución por asistentes de IA para aprender idiomas, que justifican un descuento similar. λ = 0,15: el múltiplo justificado es inestable para Duolingo porque su crecimiento de largo plazo (g ≈ 8-10%) queda a solo 2-3 puntos del WACC y del Ke; en el Optimista no se puede calcular. Por eso pesa poco.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 43,5x | 31,4x (n=3: SPOT 35,4x, NFLX 20,1x, RDDT 31,4x) × 1,00 = 31,4x | 21,4x / 26,6x / 46,0x | 30,4x | **35,8x** | 46,2x | 34,0x / 38,5x / 41,5x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 23,4x (EV/FCF × 1,30 = FCF después de intereses ÷ FCFF) | 24,9x (n=4: SPOT 28,9x, NFLX 25,0x, PINS 8,1x, RDDT 24,7x) × 1,00 = 24,9x | 24,3x / 30,5x / 52,3x | 21,4x | **25,1x** | 32,0x | 22,8x / 26,3x / 28,1x |
| P/E | sin historia representativa (El P/E del FY25 y del LTM se excluye: la utilidad incluye un beneficio tributario único de US$222,7 millones por la liberación de la reserva de valuación de impuestos diferidos (10-Q del 3T25 y 10-K FY2025); sin él, el P/E real es mucho más alto y los años anteriores no son representativos, así que el P/E se ancla en peers y fundamentales.) | 27,3x (n=3: SPOT 27,3x, NFLX 22,1x, RDDT 33,7x) × 1,00 = 27,3x | 8,5x / 11,1x / 17,3x | 20,8x | **24,8x** | 33,2x | 20,7x / 25,7x / 28,8x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 20,6x | 26,9x (n=4: SPOT 31,1x, NFLX 26,2x, PINS 8,2x, RDDT 27,5x) × 1,00 = 26,9x | 20,6x / 24,9x / 37,8x | 20,5x | **23,9x** | 28,9x | 22,9x / 25,8x / 27,3x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 19,6x | 25,9x (n=4: SPOT 30,4x, NFLX 24,5x, PINS 7,9x, RDDT 27,3x) × 1,00 = 25,9x | 19,4x / 23,9x / 37,2x | 19,4x | **22,9x** | 28,2x | 21,8x / 24,9x / 26,7x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 35,8x: promedio de historia y peers 37,5x, acercado 15% al justificado (26,6x); rango de anclas 26,6x–43,5x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (-34,2x: métrica negativa o ~0); Dec '22 (-36,9x: métrica negativa o ~0); Dec '23 (-1.584,2x: métrica negativa o ~0); Dec '24 (198,1x: > 2,5x la mediana (50.2x)). El EBITDA GAAP de Duolingo descuenta una compensación en acciones alta, por eso su múltiplo EV/EBITDA es mayor que el de los peers. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 25,1x: promedio de historia y peers 24,2x, acercado 15% al justificado (30,5x); rango de anclas 23,4x–30,5x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (349,7x: > 2,5x la mediana (49.7x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 24,8x: promedio de historia y peers 27,3x, acercado 15% al justificado (11,1x); rango de anclas 11,1x–27,3x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (-41,3x: métrica negativa o ~0); Dec '22 (-47,1x: métrica negativa o ~0); Dec '23 (648,1x: > 2,5x la mediana (96.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 23,9x: promedio de historia y peers 23,7x, acercado 15% al justificado (24,9x); rango de anclas 20,6x–26,9x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (443,4x: > 2,5x la mediana (57.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 22,9x: promedio de historia y peers 22,7x, acercado 15% al justificado (23,9x); rango de anclas 19,6x–25,9x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (269,9x: > 2,5x la mediana (52.9x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$120,34 frente a US$119,73 del DCF (+1%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$120,34 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$134,85 | US$163,81 | US$226,42 |
| EV/EBITDA | 10% | US$209,72 | US$275,28 | US$420,53 |
| EV/FCFF | 15% | US$140,73 | US$179,11 | US$267,39 |
| P/E | 5% | US$57,93 | US$80,31 | US$132,65 |
| P/FCFE | 5% | US$61,26 | US$80,48 | US$121,48 |
| P/OCF | 5% | US$64,32 | US$85,64 | US$130,53 |
| **Ponderado FY+3** | 100% | US$132,16 | US$165,00 | US$237,24 |

Valor presente (Ke 11,01%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$162,99 | US$159,89 | US$153,29 | US$158,72 | OK |
| EV/EBITDA | Base | US$193,29 | US$201,20 | US$201,21 | US$198,57 | OK |
| EV/EBITDA | Optimista | US$249,42 | US$286,89 | US$307,37 | US$281,23 | OK |
| EV/FCFF | Conservador | US$111,00 | US$107,98 | US$102,86 | US$107,28 | OK |
| EV/FCFF | Base | US$128,08 | US$131,85 | US$130,92 | US$130,28 | OK |
| EV/FCFF | Optimista | US$161,57 | US$183,76 | US$195,44 | US$180,26 | OK |
| P/E | Conservador | US$43,30 | US$43,45 | US$42,35 | US$43,03 | OK |
| P/E | Base | US$53,73 | US$57,60 | US$58,70 | US$56,68 | OK |
| P/E | Optimista | US$74,35 | US$88,69 | US$96,95 | US$86,66 | OK |
| P/FCFE | Conservador | US$46,02 | US$46,08 | US$44,77 | US$45,63 | OK |
| P/FCFE | Base | US$54,31 | US$57,90 | US$58,83 | US$57,01 | OK |
| P/FCFE | Optimista | US$68,91 | US$81,61 | US$88,79 | US$79,77 | OK |
| P/OCF | Conservador | US$48,72 | US$48,51 | US$47,01 | US$48,08 | OK |
| P/OCF | Base | US$58,60 | US$61,87 | US$62,60 | US$61,02 | OK |
| P/OCF | Optimista | US$75,67 | US$88,23 | US$95,40 | US$86,43 | OK |

Múltiplos consolidados hoy: US$97,00 / US$120,34 / US$169,51 · DCF hoy: US$98,56 / US$119,73 / US$165,49 · Ponderado hoy: US$97,94 / US$119,97 / US$167,10 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para DUOL la diferencia es de +1% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$125,77 por acción y los múltiplos, US$121,75 hoy: 3% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$142,69 supone que los ingresos crecen 15,7% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,2% (+4,5 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$163,81 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,0%, WACC de los años 4-10 10,2%, ROE de FY+3 12,1% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 35,8x | 19,7x | +68% | 7,6% | 5,5% | +2,1 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 68% por encima del DCF en FY+3. |
| EV/FCFF | 25,1x | 22,6x | +9% | 6,0% | 5,5% | +0,5 pp | Coherente con el DCF. |
| P/E | 24,8x | 50,7x | −51% | 10,3% | 10,7% | −0,4 pp | Revisar: el múltiplo vale 51% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 23,9x | 48,6x | −51% | 6,5% | 8,8% | −2,2 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 51% por debajo del DCF en FY+3. |
| P/OCF | 22,9x | 43,8x | −48% | 6,5% | 8,6% | −2,1 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 48% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$119,97 | — |
| Múltiplos Base +20% | US$128,43 | +7,1% |
| Múltiplos Base −20% | US$111,51 | −7,1% |
| Crecimiento años 2-5 +2 pp | US$124,67 | +3,9% |
| Crecimiento años 2-5 −2 pp | US$115,66 | −3,6% |
| Margen objetivo +3 pp | US$125,65 | +4,7% |
| Margen objetivo −3 pp | US$114,30 | −4,7% |
| WACC +1 pp | US$117,05 | −2,4% |
| WACC −1 pp | US$123,10 | +2,6% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 33,98 | 30,41 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 38,51 | 35,83 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 41,50 | 46,23 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 22,83 | 21,41 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 26,29 | 25,12 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 28,10 | 32,03 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 20,66 | 20,76 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 25,74 | 24,84 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 28,79 | 33,19 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 22,89 | 20,54 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 25,82 | 23,89 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 27,28 | 28,92 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 21,80 | 19,36 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 24,89 | 22,89 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 26,67 | 28,24 | Múltiplo optimista elegido con el protocolo v3 |
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
