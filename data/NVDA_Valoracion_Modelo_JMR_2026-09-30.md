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

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$162,65 en el escenario Base (rango US$72,62–US$206,15). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$212,28 (+31% frente al DCF). Con los pesos de la categoría «Madura» (40% DCF, 60% múltiplos), el ponderado hoy (lectura secundaria) es US$192,43. El valor intrínseco es el DCF: US$162,65 frente a un precio de referencia de US$228,86 (−29%).

Los múltiplos (US$212,28 hoy) quedan 31% por encima del DCF (US$162,65); el precio (US$228,86) está por encima de ambos. Los múltiplos reflejan lo que el mercado paga hoy en el ciclo de IA (~30x EBITDA, ~36x utilidad, en línea con Broadcom, KLA y Lam), mientras que el DCF usa un costo de patrimonio de 13,5% y un crecimiento que se desacelera. La diferencia es sobre todo riesgo de ciclo: si la inversión en centros de datos se frena, los múltiplos de todo el sector bajan y el DCF es la mejor referencia. Antes los múltiplos daban ~4-5x porque la historia de la hoja no estaba ajustada por los splits; esa cifra era un error y queda corregida.

| Escenario | DCF hoy (valor intrínseco) | Múltiplos consolidados hoy (secundario) | Ponderado hoy (secundario) | Compra con MOS sobre el DCF | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$72,62 | US$113,97 | US$97,43 | US$47,21 | US$131,37 |
| Base | US$162,65 | US$212,28 | US$192,43 | US$105,72 | US$284,53 |
| Optimista | US$206,15 | US$262,51 | US$239,97 | US$134,00 | US$373,09 |

## 2. Datos

- Hoja del modelo: [Modelo JMR — Plantilla maestra reutilizable (vigente)](https://docs.google.com/spreadsheets/d/1eEsuWSHXWQrBa2Dt5l_9Fbx24M4pug15Rx_Gj-CCkMg/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$228,86.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 6,0% | 50,0% | 22,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 6,0% | 14,0% | 22,0% | Input B29 |
| Margen EBIT objetivo | 50,0% | 58,0% | 65,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 3,00 / 2,50 | — | Input B32/B33 |
| DCF por acción hoy | US$72,62 | US$162,65 | US$206,15 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,90, ERP 4,46%, Ke 13,46%, costo de la deuda después de impuestos 4,94%, peso del patrimonio 99,5%, WACC inicial 13,42% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: los cierres de la hoja hasta Jan '24 dan múltiplos de 0,5-12x porque el precio no está ajustado por los splits 4:1 (jul-2021) y 10:1 (jun-2024); no son representativos. Desde FY25 (Jan '25) la historia es comparable y corresponde a la etapa actual de NVIDIA como proveedor dominante de cómputo para IA. B: semiconductores de márgenes altos (Broadcom, Qualcomm, KLA, Lam Research, Texas Instruments, Analog Devices y, en P/E, TSMC), datos de yfinance al 29-sep-2026. Se excluyen ASML (EV/EBITDA de 2.900x: dato roto), AMD y Marvell (utilidades deprimidas por la amortización de adquisiciones: múltiplos de 80-156x que no comparan con los márgenes de ~60% de NVIDIA) y TSMC en los múltiplos de EV y flujo (mezcla dólares del ADR con cifras en dólares taiwaneses). Sin ajuste: NVIDIA crece más que la mediana de los peers, pero ellos ya cotizan a múltiplos de ciclo alto de semiconductores (40-55x utilidades); se toma la mediana tal cual. λ = 0,25: la NVIDIA de FY+3 del escenario Base sigue creciendo por encima del mercado, pero con un costo de patrimonio alto (13,5%) que baja el múltiplo justificado.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Jan '25, Jan '26, LTM (etapa actual) = 34,2x | 30,6x (n=6: AVGO 32,6x, QCOM 16,7x, KLAC 42,6x, LRCX 46,7x, TXN 27,4x, ADI 28,7x) × 1,00 = 30,6x | 13,5x / 20,6x / 47,6x | 24,1x | **29,5x** | 41,9x | —x / 4,5x / —x |
| EV/FCFF | mediana Jan '25, Jan '26, LTM (etapa actual) = 49,4x (EV/FCF × 1,11 = FCF después de intereses ÷ FCFF) | 42,9x (n=6: AVGO 40,7x, QCOM 18,3x, KLAC 64,6x, LRCX 80,5x, TXN 45,0x, ADI 38,1x) × 1,00 = 42,9x | 16,9x / 27,1x / 65,5x | 34,2x | **41,4x** | 54,5x | —x / 4,2x / —x |
| P/E | mediana Jan '25, Jan '26, LTM (etapa actual) = 38,3x | 45,8x (n=7: AVGO 45,8x, QCOM 21,0x, TSM 34,0x, KLAC 53,8x, LRCX 56,3x, TXN 42,9x, ADI 47,3x) × 1,00 = 45,8x | 12,0x / 17,2x / 28,2x | 28,8x | **35,8x** | 46,3x | —x / 5,1x / —x |
| P/FCFE | mediana Jan '25, Jan '26, LTM (etapa actual) = 44,4x | 45,5x (n=6: AVGO 43,0x, QCOM 18,9x, KLAC 68,1x, LRCX 82,9x, TXN 48,0x, ADI 39,1x) × 1,00 = 45,5x | 12,9x / 18,2x / 30,4x | 32,4x | **38,3x** | 53,2x | —x / 3,9x / —x |
| P/OCF | mediana Jan '25, Jan '26, LTM (etapa actual) = 44,4x | 38,2x (n=6: AVGO 41,7x, QCOM 15,9x, KLAC 61,9x, LRCX 69,2x, TXN 29,7x, ADI 34,8x) × 1,00 = 38,2x | 12,9x / 18,4x / 30,8x | 29,3x | **35,6x** | 50,7x | —x / 3,6x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 29,5x: promedio de historia y peers 32,4x, acercado 25% al justificado (20,6x); rango de anclas 20,6x–34,2x. Atípicos excluidos de la historia: Jan '18 (0,5x: métrica negativa o ~0); Jan '20 (-1,4x: métrica negativa o ~0); Jan '17 (0,9x: < 0,4x la mediana (6.0x), caída puntual); Jan '19 (0,9x: < 0,4x la mediana (6.0x), caída puntual); Jan '25 (41,9x: > 2,5x la mediana (6.0x)); Jan '26 (34,2x: > 2,5x la mediana (6.0x)); LTM (26,9x: > 2,5x la mediana (6.0x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 41,4x: promedio de historia y peers 46,1x, acercado 25% al justificado (27,1x); rango de anclas 27,1x–49,4x. Atípicos excluidos de la historia: Jan '18 (0,5x: métrica negativa o ~0); Jan '20 (-0,9x: métrica negativa o ~0); Jan '17 (1,1x: < 0,4x la mediana (7.3x), caída puntual); Jan '19 (1,0x: < 0,4x la mediana (7.3x), caída puntual); Jan '21 (2,5x: < 0,4x la mediana (7.3x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (7.3x)); Jan '26 (44,4x: > 2,5x la mediana (7.3x)); LTM (40,3x: > 2,5x la mediana (7.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 35,8x: promedio de historia y peers 42,0x, acercado 25% al justificado (17,2x); rango de anclas 17,2x–45,8x. Atípicos excluidos de la historia: Jan '17 (1,1x: < 0,4x la mediana (5.1x), caída puntual); Jan '18 (1,3x: < 0,4x la mediana (5.1x), caída puntual); Jan '19 (0,6x: < 0,4x la mediana (5.1x), caída puntual); Jan '20 (1,4x: < 0,4x la mediana (5.1x), caída puntual); Jan '21 (1,9x: < 0,4x la mediana (5.1x), caída puntual); Jan '25 (48,5x: > 2,5x la mediana (5.1x)); Jan '26 (38,3x: > 2,5x la mediana (5.1x)); LTM (28,6x: > 2,5x la mediana (5.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 38,3x: promedio de historia y peers 45,0x, acercado 25% al justificado (18,2x); rango de anclas 18,2x–45,5x. Atípicos excluidos de la historia: Jan '17 (1,0x: < 0,4x la mediana (5.4x), caída puntual); Jan '18 (1,1x: < 0,4x la mediana (5.4x), caída puntual); Jan '19 (0,7x: < 0,4x la mediana (5.4x), caída puntual); Jan '20 (0,8x: < 0,4x la mediana (5.4x), caída puntual); Jan '21 (1,4x: < 0,4x la mediana (5.4x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (5.4x)); Jan '26 (44,4x: > 2,5x la mediana (5.4x)); LTM (40,4x: > 2,5x la mediana (5.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 35,6x: promedio de historia y peers 41,3x, acercado 25% al justificado (18,4x); rango de anclas 18,4x–44,4x. Atípicos excluidos de la historia: Jan '17 (1,0x: < 0,4x la mediana (5.4x), caída puntual); Jan '18 (1,1x: < 0,4x la mediana (5.4x), caída puntual); Jan '19 (0,7x: < 0,4x la mediana (5.4x), caída puntual); Jan '20 (0,8x: < 0,4x la mediana (5.4x), caída puntual); Jan '21 (1,4x: < 0,4x la mediana (5.4x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (5.4x)); Jan '26 (44,4x: > 2,5x la mediana (5.4x)); LTM (40,4x: > 2,5x la mediana (5.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$212,28 frente a US$162,65 del DCF (+31%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$212,28 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$106,09 | US$237,59 | US$301,13 |
| EV/EBITDA | 20% | US$141,74 | US$306,65 | US$433,91 |
| EV/FCFF | 10% | US$160,88 | US$326,57 | US$409,88 |
| P/E | 20% | US$145,65 | US$322,26 | US$415,28 |
| P/FCFE | 5% | US$161,83 | US$323,24 | US$430,78 |
| P/OCF | 5% | US$145,50 | US$297,82 | US$405,50 |
| **Ponderado FY+3** | 100% | US$131,37 | US$284,53 | US$373,09 |

Valor presente (Ke 13,46%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$123,16 | US$107,37 | US$97,03 | US$109,19 | OK |
| EV/EBITDA | Base | US$212,61 | US$210,15 | US$209,93 | US$210,90 | OK |
| EV/EBITDA | Optimista | US$245,79 | US$271,87 | US$297,05 | US$271,57 | OK |
| EV/FCFF | Conservador | US$140,63 | US$122,09 | US$110,14 | US$124,28 | OK |
| EV/FCFF | Base | US$184,79 | US$223,94 | US$223,56 | US$210,76 | OK |
| EV/FCFF | Optimista | US$230,74 | US$256,15 | US$280,60 | US$255,83 | OK |
| P/E | Conservador | US$125,15 | US$109,91 | US$99,71 | US$111,59 | OK |
| P/E | Base | US$220,37 | US$219,79 | US$220,62 | US$220,26 | OK |
| P/E | Optimista | US$231,55 | US$258,77 | US$284,29 | US$258,20 | OK |
| P/FCFE | Conservador | US$139,88 | US$122,14 | US$110,78 | US$124,27 | OK |
| P/FCFE | Base | US$186,55 | US$220,45 | US$221,28 | US$209,43 | OK |
| P/FCFE | Optimista | US$240,04 | US$267,84 | US$294,90 | US$267,59 | OK |
| P/OCF | Conservador | US$125,78 | US$109,81 | US$99,60 | US$111,73 | OK |
| P/OCF | Base | US$168,43 | US$203,11 | US$203,88 | US$191,81 | OK |
| P/OCF | Optimista | US$225,78 | US$252,06 | US$277,60 | US$251,81 | OK |

Múltiplos consolidados hoy: US$113,97 / US$212,28 / US$262,51 · DCF hoy: US$72,62 / US$162,65 / US$206,15 · Ponderado hoy: US$97,43 / US$192,43 / US$239,97 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NVDA la diferencia es de +31% (múltiplos por encima del DCF). Los múltiplos (US$212,28 hoy) quedan 31% por encima del DCF (US$162,65); el precio (US$228,86) está por encima de ambos. Los múltiplos reflejan lo que el mercado paga hoy en el ciclo de IA (~30x EBITDA, ~36x utilidad, en línea con Broadcom, KLA y Lam), mientras que el DCF usa un costo de patrimonio de 13,5% y un crecimiento que se desacelera. La diferencia es sobre todo riesgo de ciclo: si la inversión en centros de datos se frena, los múltiplos de todo el sector bajan y el DCF es la mejor referencia. Antes los múltiplos daban ~4-5x porque la historia de la hoja no estaba ajustada por los splits; esa cifra era un error y queda corregida.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$228,86 supone que los ingresos crecen 28,1% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 21,2% (+6,9 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Crecimiento perpetuo después de FY+3 que supone cada múltiplo Base, con Ke 13,5%, WACC de los años 4-10 11,5% y ROE de FY+3 138,4%, frente al crecimiento del DCF (7,6%: punto medio entre los años 4-10 y la perpetuidad):

| Múltiplo Base FY+3 | Múltiplo | Crecimiento implícito | Diferencia vs. DCF | Lectura |
|---|---:|---:|---:|---|
| EV/EBITDA | 29,5x | 8,7% | +1,2 pp | Coherente con el DCF. |
| EV/FCFF | 41,4x | 8,9% | +1,3 pp | Coherente con el DCF. |
| P/E | 35,8x | 10,6% | +3,0 pp | Revisar: el múltiplo supone más crecimiento que el DCF. |
| P/FCFE | 38,3x | 10,6% | +3,0 pp | Revisar: el múltiplo supone más crecimiento que el DCF. |
| P/OCF | 35,6x | 10,3% | +2,8 pp | Revisar: el múltiplo supone más crecimiento que el DCF. |

Más de 2 pp de diferencia significa que el múltiplo (o el precio) cuenta otra historia de crecimiento que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (subir el crecimiento del DCF si la evidencia lo sostiene, o acercar el múltiplo al justificado si no).

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$192,43 | — |
| Múltiplos Base +20% | US$217,83 | +13,2% |
| Múltiplos Base −20% | US$167,03 | −13,2% |
| Crecimiento años 1-5 +2 pp | US$198,50 | +3,2% |
| Crecimiento años 1-5 −2 pp | US$186,83 | −2,9% |
| Margen objetivo +3 pp | US$195,87 | +1,8% |
| Margen objetivo −3 pp | US$188,98 | −1,8% |
| WACC +1 pp | US$188,73 | −1,9% |
| WACC −1 pp | US$196,39 | +2,1% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 1-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 24,11 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 4,46 | 29,48 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 41,92 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 34,19 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 4,16 | 41,40 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 54,49 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 28,77 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 5,05 | 35,83 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 46,29 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 32,42 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 3,92 | 38,28 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 53,16 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 29,26 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 3,57 | 35,59 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 50,70 | Múltiplo optimista elegido con el protocolo v3 |
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
