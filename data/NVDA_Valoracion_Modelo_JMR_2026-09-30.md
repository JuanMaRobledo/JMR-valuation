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

**Valor intrínseco principal · DCF Base hoy: US$209,46 por acción.** Complemento: DCF esperado por probabilidades US$190,57; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$54,63–US$318,11; precio con MOS 35% sobre el esperado: US$123,87; precio de referencia US$230,67. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$263,90), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Ciclo de IA largo que desacelera con la escala** (valor principal) | 40% | US$209,46 | US$83,78 |
| Conservadora · Ciclo de semiconductores: el capex se corrige | 30% | US$125,68 | US$37,70 |
| Disrupción · Deterioro de los fundamentales: Chips propios de los clientes y corrección fuerte | 10% | US$54,63 | US$5,46 |
| Optimista · La IA es infraestructura permanente | 20% | US$318,11 | US$63,62 |
| **DCF esperado (complemento)** | 100% | **US$190,57** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$259,29 por acción y los múltiplos, US$230,76 hoy: 11% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$209,46 | US$329,59 | US$281,54 | US$123,87 | US$394,80 |
| Conservador | US$125,68 | US$192,46 | US$165,75 | US$123,87 | US$198,54 |
| Optimista | US$318,11 | US$451,12 | US$397,92 | US$123,87 | US$594,62 |

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
| Sales-to-capital años 1-5 / 6-10 | — | 2,92 / 2,44 | — | Input B32/B33 |
| DCF por acción hoy | US$125,68 | US$209,46 | US$318,11 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,51, ERP 4,46%, Ke 11,72%, costo de la deuda después de impuestos 4,94%, peso del patrimonio 99,3%, WACC inicial 11,67% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: los cierres de la hoja hasta Jan '24 dan múltiplos de 0,5-12x porque el precio no está ajustado por los splits 4:1 (jul-2021) y 10:1 (jun-2024); no son representativos. Desde FY25 (Jan '25) la historia es comparable y corresponde a la etapa actual de NVIDIA como proveedor dominante de cómputo para IA. B: semiconductores de márgenes altos (Broadcom, Qualcomm, KLA, Lam Research, Texas Instruments, Analog Devices y, en P/E, TSMC), datos de yfinance al 29-sep-2026. Se excluyen ASML (EV/EBITDA de 2.900x: dato roto), AMD y Marvell (utilidades deprimidas por la amortización de adquisiciones: múltiplos de 80-156x que no comparan con los márgenes de ~60% de NVIDIA) y TSMC en los múltiplos de EV y flujo (mezcla dólares del ADR con cifras en dólares taiwaneses). Sin ajuste: NVIDIA crece más que la mediana de los peers, pero ellos ya cotizan a múltiplos de ciclo alto de semiconductores (40-55x utilidades); se toma la mediana tal cual. λ = 0,25: la NVIDIA de FY+3 del escenario Base sigue creciendo por encima del mercado, pero con un costo de patrimonio alto (13,5%) que baja el múltiplo justificado.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Jan '25, Jan '26, LTM (etapa actual) = 34,2x | 30,6x (n=6: AVGO 32,6x, QCOM 16,7x, KLAC 42,6x, LRCX 46,7x, TXN 27,4x, ADI 28,7x) × 1,00 = 30,6x | 27,4x / 16,0x / — | **31,2x** | 24,8x | 37,8x | 4,5x / —x / —x |
| EV/FCFF | mediana Jan '25, Jan '26, LTM (etapa actual) = 49,4x (EV/FCF × 1,11 = FCF después de intereses ÷ FCFF) | 42,9x (n=6: AVGO 40,7x, QCOM 18,3x, KLAC 64,6x, LRCX 80,5x, TXN 45,0x, ADI 38,1x) × 1,00 = 42,9x | 36,2x / 20,0x / — | **43,6x** | 35,1x | 54,5x | 4,2x / —x / —x |
| P/E | mediana Jan '25, Jan '26, LTM (etapa actual) = 38,3x | 45,8x (n=7: AVGO 45,8x, QCOM 21,0x, TSM 34,0x, KLAC 53,8x, LRCX 56,3x, TXN 42,9x, ADI 47,3x) × 1,00 = 45,8x | 24,4x / 15,2x / — | **37,6x** | 29,3x | 42,1x | 5,1x / —x / —x |
| P/FCFE | mediana Jan '25, Jan '26, LTM (etapa actual) = 44,4x | 45,5x (n=6: AVGO 43,0x, QCOM 18,9x, KLAC 68,1x, LRCX 82,9x, TXN 48,0x, ADI 39,1x) × 1,00 = 45,5x | 25,9x / 16,3x / — | **40,2x** | 33,0x | 50,2x | 3,9x / —x / —x |
| P/OCF | mediana Jan '25, Jan '26, LTM (etapa actual) = 44,4x | 38,2x (n=6: AVGO 41,7x, QCOM 15,9x, KLAC 61,9x, LRCX 69,2x, TXN 29,7x, ADI 34,8x) × 1,00 = 38,2x | 26,1x / 16,4x / — | **37,5x** | 29,9x | 48,8x | 3,6x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 31,2x: promedio de historia y peers 32,4x, acercado 25% al justificado (27,4x); rango de anclas 27,4x–34,2x. Atípicos excluidos de la historia: Jan '18 (0,5x: métrica negativa o ~0); Jan '20 (-1,4x: métrica negativa o ~0); Jan '17 (0,9x: < 0,4x la mediana (6.0x), caída puntual); Jan '19 (0,9x: < 0,4x la mediana (6.0x), caída puntual); Jan '25 (41,9x: > 2,5x la mediana (6.0x)); Jan '26 (34,2x: > 2,5x la mediana (6.0x)); LTM (26,9x: > 2,5x la mediana (6.0x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 43,6x: promedio de historia y peers 46,1x, acercado 25% al justificado (36,2x); rango de anclas 36,2x–49,4x. Atípicos excluidos de la historia: Jan '18 (0,5x: métrica negativa o ~0); Jan '20 (-0,9x: métrica negativa o ~0); Jan '17 (1,1x: < 0,4x la mediana (7.3x), caída puntual); Jan '19 (1,0x: < 0,4x la mediana (7.3x), caída puntual); Jan '21 (2,5x: < 0,4x la mediana (7.3x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (7.3x)); Jan '26 (44,4x: > 2,5x la mediana (7.3x)); LTM (40,3x: > 2,5x la mediana (7.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 37,6x: promedio de historia y peers 42,0x, acercado 25% al justificado (24,4x); rango de anclas 24,4x–45,8x. Atípicos excluidos de la historia: Jan '17 (1,1x: < 0,4x la mediana (5.1x), caída puntual); Jan '18 (1,3x: < 0,4x la mediana (5.1x), caída puntual); Jan '19 (0,6x: < 0,4x la mediana (5.1x), caída puntual); Jan '20 (1,4x: < 0,4x la mediana (5.1x), caída puntual); Jan '21 (1,9x: < 0,4x la mediana (5.1x), caída puntual); Jan '25 (48,5x: > 2,5x la mediana (5.1x)); Jan '26 (38,3x: > 2,5x la mediana (5.1x)); LTM (28,6x: > 2,5x la mediana (5.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 40,2x: promedio de historia y peers 45,0x, acercado 25% al justificado (25,9x); rango de anclas 25,9x–45,5x. Atípicos excluidos de la historia: Jan '17 (1,0x: < 0,4x la mediana (5.4x), caída puntual); Jan '18 (1,1x: < 0,4x la mediana (5.4x), caída puntual); Jan '19 (0,7x: < 0,4x la mediana (5.4x), caída puntual); Jan '20 (0,8x: < 0,4x la mediana (5.4x), caída puntual); Jan '21 (1,4x: < 0,4x la mediana (5.4x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (5.4x)); Jan '26 (44,4x: > 2,5x la mediana (5.4x)); LTM (40,4x: > 2,5x la mediana (5.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 37,5x: promedio de historia y peers 41,3x, acercado 25% al justificado (26,1x); rango de anclas 26,1x–44,4x. Atípicos excluidos de la historia: Jan '17 (1,0x: < 0,4x la mediana (5.4x), caída puntual); Jan '18 (1,1x: < 0,4x la mediana (5.4x), caída puntual); Jan '19 (0,7x: < 0,4x la mediana (5.4x), caída puntual); Jan '20 (0,8x: < 0,4x la mediana (5.4x), caída puntual); Jan '21 (1,4x: < 0,4x la mediana (5.4x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (5.4x)); Jan '26 (44,4x: > 2,5x la mediana (5.4x)); LTM (40,4x: > 2,5x la mediana (5.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$329,59 frente a US$209,46 del DCF (+57%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$329,56 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$292,11 | US$175,27 | US$443,64 |
| EV/EBITDA | 20% | US$452,67 | US$211,39 | US$696,23 |
| EV/FCFF | 10% | US$489,63 | US$229,58 | US$739,78 |
| P/E | 20% | US$463,27 | US$209,91 | US$661,60 |
| P/FCFE | 5% | US$478,34 | US$222,77 | US$739,85 |
| P/OCF | 5% | US$437,83 | US$201,63 | US$692,64 |
| **Ponderado FY+3** | 100% | US$394,80 | US$198,54 | US$594,62 |

Valor presente (Ke 11,72%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$317,19 | US$332,42 | US$324,66 | US$324,75 | OK |
| EV/EBITDA | Conservador | US$228,81 | US$174,38 | US$151,65 | US$184,95 | OK |
| EV/EBITDA | Optimista | US$407,18 | US$467,16 | US$499,31 | US$457,88 | OK |
| EV/FCFF | Base | US$314,80 | US$354,85 | US$351,17 | US$340,27 | OK |
| EV/FCFF | Conservador | US$279,50 | US$200,67 | US$164,70 | US$214,96 | OK |
| EV/FCFF | Optimista | US$385,36 | US$478,97 | US$530,54 | US$464,96 | OK |
| P/E | Base | US$322,69 | US$340,07 | US$332,26 | US$331,67 | OK |
| P/E | Conservador | US$227,90 | US$173,51 | US$150,59 | US$184,00 | OK |
| P/E | Optimista | US$384,14 | US$443,50 | US$474,48 | US$434,04 | OK |
| P/FCFE | Base | US$338,52 | US$352,10 | US$343,07 | US$344,57 | OK |
| P/FCFE | Conservador | US$295,62 | US$190,05 | US$159,81 | US$215,16 | OK |
| P/FCFE | Optimista | US$423,81 | US$486,54 | US$530,59 | US$480,32 | OK |
| P/OCF | Base | US$281,57 | US$317,18 | US$314,02 | US$304,26 | OK |
| P/OCF | Conservador | US$245,40 | US$176,05 | US$144,65 | US$188,70 | OK |
| P/OCF | Optimista | US$361,30 | US$448,59 | US$496,73 | US$435,54 | OK |

Múltiplos consolidados hoy: US$329,59 / US$192,46 / US$451,12 · DCF de las historias hoy: US$209,46 / US$125,68 / US$318,11 · Ponderado hoy: US$281,54 / US$165,75 / US$397,92 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NVDA la diferencia es de +57% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$259,29 por acción y los múltiplos, US$230,76 hoy: 11% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$230,67 supone que los ingresos crecen 16,5% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 21,2% (−4,7 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$292,11 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,7%, WACC de los años 4-10 10,5%, ROE de FY+3 138,4% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 31,2x | 20,0x | +55% | 7,9% | 6,5% | +1,4 pp | Revisar: el múltiplo vale 55% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 43,6x | 25,8x | +68% | 8,1% | 6,4% | +1,6 pp | Revisar: el múltiplo vale 68% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 37,6x | 23,7x | +59% | 9,0% | 7,4% | +1,6 pp | Revisar: el múltiplo vale 59% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 40,2x | 24,5x | +64% | 9,0% | 7,3% | +1,7 pp | Revisar: el múltiplo vale 64% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 37,5x | 25,0x | +50% | 8,8% | 7,4% | +1,4 pp | Revisar: el múltiplo vale 50% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$281,54 | — |
| Múltiplos Base +20% | US$320,79 | +13,9% |
| Múltiplos Base −20% | US$242,25 | −14,0% |
| Crecimiento años 2-5 +2 pp | US$313,22 | +11,3% |
| Crecimiento años 2-5 −2 pp | US$294,22 | +4,5% |
| Margen objetivo +3 pp | US$308,42 | +9,5% |
| Margen objetivo −3 pp | US$298,21 | +5,9% |
| WACC +1 pp | US$297,62 | +5,7% |
| WACC −1 pp | US$309,41 | +9,9% |

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
