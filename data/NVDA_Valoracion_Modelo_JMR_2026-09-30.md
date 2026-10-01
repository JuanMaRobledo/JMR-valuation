---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de NVIDIA CORP"
ticker: "NVDA"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1eEsuWSHXWQrBa2Dt5l_9Fbx24M4pug15Rx_Gj-CCkMg/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# NVIDIA CORP (NVDA) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal: DCF esperado de las cuatro historias, US$190,27.** Historia central A: US$209,15; rango US$54,31–US$317,84; precio con MOS 35% sobre el esperado: US$123,67; precio de referencia US$230,67. Cada historia es un DCF completo (hoja «Escenarios e historias»); el detalle está en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son la calibración técnica anterior de la hoja (Base US$263,61) y los múltiplos y el ponderado son lecturas secundarias.


| Historia | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| A · Ciclo de IA largo que desacelera con la escala | 40% | US$209,15 | US$83,66 |
| B · Ciclo de semiconductores: el capex se corrige | 30% | US$125,35 | US$37,60 |
| C · Tesis de disrupción · Deterioro de los fundamentales: Chips propios de los clientes y corrección fuerte | 10% | US$54,31 | US$5,43 |
| D · La IA es infraestructura permanente | 20% | US$317,84 | US$63,57 |
| **DCF esperado** | 100% | **US$190,27** | |

Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$259,29 por acción y los múltiplos, US$230,76 hoy: 11% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

| Escenario | DCF técnico anterior hoy (calibración) | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$142,73 | US$149,11 | US$146,56 | US$123,67 | US$194,63 |
| Base | US$263,61 | US$233,07 | US$245,28 | US$123,67 | US$348,27 |
| Optimista | US$437,33 | US$319,39 | US$366,57 | US$123,67 | US$545,92 |

## 2. Datos

- Hoja del modelo: [Modelo JMR — Plantilla maestra reutilizable (vigente)](https://docs.google.com/spreadsheets/d/1eEsuWSHXWQrBa2Dt5l_9Fbx24M4pug15Rx_Gj-CCkMg/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$230,67.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 32,5% | 50,0% | 56,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 6,0% | 14,0% | 22,0% | Input B29 |
| Margen EBIT objetivo | 50,0% | 58,0% | 65,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 3,00 / 2,50 | — | Input B32/B33 |
| DCF por acción hoy | US$142,73 | US$263,61 | US$437,33 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,51, ERP 4,46%, Ke 11,72%, costo de la deuda después de impuestos 4,94%, peso del patrimonio 99,2%, WACC inicial 11,67% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: los cierres de la hoja hasta Jan '24 dan múltiplos de 0,5-12x porque el precio no está ajustado por los splits 4:1 (jul-2021) y 10:1 (jun-2024); no son representativos. Desde FY25 (Jan '25) la historia es comparable y corresponde a la etapa actual de NVIDIA como proveedor dominante de cómputo para IA. B: semiconductores de márgenes altos (Broadcom, Qualcomm, KLA, Lam Research, Texas Instruments, Analog Devices y, en P/E, TSMC), datos de yfinance al 29-sep-2026. Se excluyen ASML (EV/EBITDA de 2.900x: dato roto), AMD y Marvell (utilidades deprimidas por la amortización de adquisiciones: múltiplos de 80-156x que no comparan con los márgenes de ~60% de NVIDIA) y TSMC en los múltiplos de EV y flujo (mezcla dólares del ADR con cifras en dólares taiwaneses). Sin ajuste: NVIDIA crece más que la mediana de los peers, pero ellos ya cotizan a múltiplos de ciclo alto de semiconductores (40-55x utilidades); se toma la mediana tal cual. λ = 0,25: la NVIDIA de FY+3 del escenario Base sigue creciendo por encima del mercado, pero con un costo de patrimonio alto (13,5%) que baja el múltiplo justificado.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Jan '25, Jan '26, LTM (etapa actual) = 34,2x | 30,6x (n=6: AVGO 32,6x, QCOM 16,7x, KLAC 42,6x, LRCX 46,7x, TXN 27,4x, ADI 28,7x) × 1,00 = 30,6x | 16,0x / 27,4x / — | 24,8x | **31,2x** | 37,8x | —x / 4,5x / —x |
| EV/FCFF | mediana Jan '25, Jan '26, LTM (etapa actual) = 49,4x (EV/FCF × 1,11 = FCF después de intereses ÷ FCFF) | 42,9x (n=6: AVGO 40,7x, QCOM 18,3x, KLAC 64,6x, LRCX 80,5x, TXN 45,0x, ADI 38,1x) × 1,00 = 42,9x | 20,0x / 36,2x / — | 35,1x | **43,6x** | 54,5x | —x / 4,2x / —x |
| P/E | mediana Jan '25, Jan '26, LTM (etapa actual) = 38,3x | 45,8x (n=7: AVGO 45,8x, QCOM 21,0x, TSM 34,0x, KLAC 53,8x, LRCX 56,3x, TXN 42,9x, ADI 47,3x) × 1,00 = 45,8x | 15,2x / 24,4x / — | 29,3x | **37,6x** | 42,1x | —x / 5,1x / —x |
| P/FCFE | mediana Jan '25, Jan '26, LTM (etapa actual) = 44,4x | 45,5x (n=6: AVGO 43,0x, QCOM 18,9x, KLAC 68,1x, LRCX 82,9x, TXN 48,0x, ADI 39,1x) × 1,00 = 45,5x | 16,3x / 25,9x / — | 33,0x | **40,2x** | 50,2x | —x / 3,9x / —x |
| P/OCF | mediana Jan '25, Jan '26, LTM (etapa actual) = 44,4x | 38,2x (n=6: AVGO 41,7x, QCOM 15,9x, KLAC 61,9x, LRCX 69,2x, TXN 29,7x, ADI 34,8x) × 1,00 = 38,2x | 16,4x / 26,1x / — | 29,9x | **37,5x** | 48,8x | —x / 3,6x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 31,2x: promedio de historia y peers 32,4x, acercado 25% al justificado (27,4x); rango de anclas 27,4x–34,2x. Atípicos excluidos de la historia: Jan '18 (0,5x: métrica negativa o ~0); Jan '20 (-1,4x: métrica negativa o ~0); Jan '17 (0,9x: < 0,4x la mediana (6.0x), caída puntual); Jan '19 (0,9x: < 0,4x la mediana (6.0x), caída puntual); Jan '25 (41,9x: > 2,5x la mediana (6.0x)); Jan '26 (34,2x: > 2,5x la mediana (6.0x)); LTM (26,9x: > 2,5x la mediana (6.0x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 43,6x: promedio de historia y peers 46,1x, acercado 25% al justificado (36,2x); rango de anclas 36,2x–49,4x. Atípicos excluidos de la historia: Jan '18 (0,5x: métrica negativa o ~0); Jan '20 (-0,9x: métrica negativa o ~0); Jan '17 (1,1x: < 0,4x la mediana (7.3x), caída puntual); Jan '19 (1,0x: < 0,4x la mediana (7.3x), caída puntual); Jan '21 (2,5x: < 0,4x la mediana (7.3x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (7.3x)); Jan '26 (44,4x: > 2,5x la mediana (7.3x)); LTM (40,3x: > 2,5x la mediana (7.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 37,6x: promedio de historia y peers 42,0x, acercado 25% al justificado (24,4x); rango de anclas 24,4x–45,8x. Atípicos excluidos de la historia: Jan '17 (1,1x: < 0,4x la mediana (5.1x), caída puntual); Jan '18 (1,3x: < 0,4x la mediana (5.1x), caída puntual); Jan '19 (0,6x: < 0,4x la mediana (5.1x), caída puntual); Jan '20 (1,4x: < 0,4x la mediana (5.1x), caída puntual); Jan '21 (1,9x: < 0,4x la mediana (5.1x), caída puntual); Jan '25 (48,5x: > 2,5x la mediana (5.1x)); Jan '26 (38,3x: > 2,5x la mediana (5.1x)); LTM (28,6x: > 2,5x la mediana (5.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 40,2x: promedio de historia y peers 45,0x, acercado 25% al justificado (25,9x); rango de anclas 25,9x–45,5x. Atípicos excluidos de la historia: Jan '17 (1,0x: < 0,4x la mediana (5.4x), caída puntual); Jan '18 (1,1x: < 0,4x la mediana (5.4x), caída puntual); Jan '19 (0,7x: < 0,4x la mediana (5.4x), caída puntual); Jan '20 (0,8x: < 0,4x la mediana (5.4x), caída puntual); Jan '21 (1,4x: < 0,4x la mediana (5.4x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (5.4x)); Jan '26 (44,4x: > 2,5x la mediana (5.4x)); LTM (40,4x: > 2,5x la mediana (5.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 37,5x: promedio de historia y peers 41,3x, acercado 25% al justificado (26,1x); rango de anclas 26,1x–44,4x. Atípicos excluidos de la historia: Jan '17 (1,0x: < 0,4x la mediana (5.4x), caída puntual); Jan '18 (1,1x: < 0,4x la mediana (5.4x), caída puntual); Jan '19 (0,7x: < 0,4x la mediana (5.4x), caída puntual); Jan '20 (0,8x: < 0,4x la mediana (5.4x), caída puntual); Jan '21 (1,4x: < 0,4x la mediana (5.4x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (5.4x)); Jan '26 (44,4x: > 2,5x la mediana (5.4x)); LTM (40,4x: > 2,5x la mediana (5.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$233,07 frente a US$263,61 del DCF (−12%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$233,07 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$199,05 | US$367,62 | US$609,90 |
| EV/EBITDA | 20% | US$185,64 | US$328,32 | US$503,68 |
| EV/FCFF | 10% | US$209,91 | US$348,20 | US$527,85 |
| P/E | 20% | US$185,92 | US$338,41 | US$483,17 |
| P/FCFE | 5% | US$208,24 | US$347,19 | US$537,42 |
| P/OCF | 5% | US$185,78 | US$313,92 | US$498,71 |
| **Ponderado FY+3** | 100% | US$194,63 | US$348,27 | US$545,92 |

Valor presente (Ke 11,72%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$164,01 | US$145,18 | US$133,12 | US$147,43 | OK |
| EV/EBITDA | Base | US$231,95 | US$232,44 | US$235,42 | US$233,27 | OK |
| EV/EBITDA | Optimista | US$291,03 | US$326,10 | US$361,17 | US$326,10 | OK |
| EV/FCFF | Conservador | US$157,61 | US$164,42 | US$150,52 | US$157,52 | OK |
| EV/FCFF | Base | US$201,37 | US$246,64 | US$249,68 | US$232,57 | OK |
| EV/FCFF | Optimista | US$253,02 | US$340,85 | US$378,50 | US$324,12 | OK |
| P/E | Conservador | US$162,37 | US$144,76 | US$133,32 | US$146,82 | OK |
| P/E | Base | US$235,03 | US$238,05 | US$242,66 | US$238,58 | OK |
| P/E | Optimista | US$273,63 | US$310,54 | US$346,46 | US$310,21 | OK |
| P/FCFE | Conservador | US$163,88 | US$162,10 | US$149,32 | US$158,43 | OK |
| P/FCFE | Base | US$213,45 | US$244,18 | US$248,95 | US$235,53 | OK |
| P/FCFE | Optimista | US$272,72 | US$344,86 | US$385,36 | US$334,31 | OK |
| P/OCF | Conservador | US$138,59 | US$144,67 | US$133,21 | US$138,82 | OK |
| P/OCF | Base | US$180,31 | US$220,82 | US$225,10 | US$208,75 | OK |
| P/OCF | Optimista | US$237,26 | US$319,75 | US$357,61 | US$304,87 | OK |

Múltiplos consolidados hoy: US$149,11 / US$233,07 / US$319,39 · DCF hoy: US$142,73 / US$263,61 / US$437,33 · Ponderado hoy: US$146,56 / US$245,28 / US$366,57 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NVDA la diferencia es de −12% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$259,29 por acción y los múltiplos, US$230,76 hoy: 11% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$230,67 supone que los ingresos crecen 16,5% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 21,2% (−4,7 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$367,62 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,7%, WACC de los años 4-10 10,5%, ROE de FY+3 138,4% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 31,2x | 35,0x | −11% | 7,9% | 8,2% | −0,3 pp | Coherente con el DCF. |
| EV/FCFF | 43,6x | 46,1x | −5% | 8,1% | 8,2% | −0,1 pp | Coherente con el DCF. |
| P/E | 37,6x | 40,9x | −8% | 9,0% | 9,2% | −0,2 pp | Coherente con el DCF. |
| P/FCFE | 40,2x | 42,6x | −6% | 9,0% | 9,2% | −0,1 pp | Coherente con el DCF. |
| P/OCF | 37,5x | 44,0x | −15% | 8,8% | 9,2% | −0,4 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$245,28 | — |
| Múltiplos Base +20% | US$272,98 | +11,3% |
| Múltiplos Base −20% | US$217,58 | −11,3% |
| Crecimiento años 2-5 +2 pp | US$255,20 | +4,0% |
| Crecimiento años 2-5 −2 pp | US$236,19 | −3,7% |
| Margen objetivo +3 pp | US$250,39 | +2,1% |
| Margen objetivo −3 pp | US$240,18 | −2,1% |
| WACC +1 pp | US$239,59 | −2,3% |
| WACC −1 pp | US$251,38 | +2,5% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 24,77 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 4,46 | 31,19 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 37,76 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 35,07 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 4,16 | 43,65 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 54,49 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 29,30 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 5,05 | 37,63 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 42,12 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 33,04 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 3,92 | 40,19 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 50,21 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 29,92 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 3,57 | 37,52 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 48,77 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/NVDA_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1eEsuWSHXWQrBa2Dt5l_9Fbx24M4pug15Rx_Gj-CCkMg/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (AVGO, QCOM, TSM, AMD, MRVL, ASML, KLAC, LRCX, TXN, ADI).

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
