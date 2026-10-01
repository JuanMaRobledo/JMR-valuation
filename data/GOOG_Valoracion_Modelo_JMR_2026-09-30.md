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

**Valor intrínseco principal · DCF Base hoy: US$323,88 por acción.** Complemento: DCF esperado por probabilidades US$275,68; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$133,16–US$425,90; precio con MOS 35% sobre el esperado: US$179,19; precio de referencia US$346,22. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son la calibración técnica anterior de la hoja (Base técnico US$334,21) y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Search resiste y Cloud es el segundo motor** (valor principal) | 40% | US$323,88 | US$129,55 |
| Conservadora · La IA conversacional erosiona Search | 25% | US$163,89 | US$40,97 |
| Disrupción · Deterioro de los fundamentales: Remedios antimonopolio y guerra de precios en IA | 15% | US$133,16 | US$19,97 |
| Optimista · Gemini y Cloud dominan la plataforma de IA | 20% | US$425,90 | US$85,18 |
| **DCF esperado (complemento)** | 100% | **US$275,68** | |

Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$311,55 por acción y los múltiplos, US$244,87 hoy: 21% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

| Escenario | DCF técnico anterior hoy (calibración) | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$334,21 | US$256,95 | US$287,85 | US$179,19 | US$387,61 |
| Conservador | US$268,73 | US$199,47 | US$227,18 | US$179,19 | US$299,38 |
| Optimista | US$478,41 | US$363,30 | US$409,35 | US$179,19 | US$575,06 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - Alphabet (GOOG)](https://docs.google.com/spreadsheets/d/1yt2zqdGz1JWEqV3SYqqL-nHarO7C1Oud1lvR3pY9i0U/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$346,22.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 9,0% | 18,0% | 20,6% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 9,0% | 11,0% | 16,0% | Input B29 |
| Margen EBIT objetivo | 31,3% | 35,3% | 38,3% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,15 / 1,43 | — | Input B32/B33 |
| DCF por acción hoy | US$268,73 | US$334,21 | US$478,41 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,07, ERP 4,46%, Ke 9,76%, costo de la deuda después de impuestos 4,65%, peso del patrimonio 97,9%, WACC inicial 9,65% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: los cierres 2016-2021 de la hoja dan múltiplos de ~1x porque el precio no está ajustado por el split 20:1 de julio de 2022; no son representativos y se usa la historia desde Dec '22. En P/E se quita el LTM: la utilidad del primer semestre de 2026 incluye US$135,9 mil millones de ganancias en acciones de otras empresas, que bajan el P/E a 17x. En EV/FCFF y P/FCFE se quita el LTM: el capex de 2026 (US$195-205 mil millones) deja el flujo de caja en mínimos y el múltiplo en ~78x, un pico transitorio frente al flujo de FY+3. B: grandes plataformas tecnológicas (Meta, Microsoft, Amazon, Apple, Netflix), datos de yfinance al 29-sep-2026. Amazon no tiene flujo de caja libre positivo y no entra en los múltiplos de flujo. Sin ajuste: Alphabet crece 24% con margen operativo de 34%, en línea con Meta y Microsoft. λ = 0,25: la Alphabet de FY+3 del escenario Base sigue siendo una plataforma de crecimiento alto con fuerte inversión en IA, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,3x | 19,7x (n=5: META 17,4x, MSFT 19,7x, AMZN 16,5x, AAPL 28,8x, NFLX 20,1x) × 1,00 = 19,7x | 14,6x / 11,6x / 32,5x | **17,9x** | 16,0x | 25,5x | 13,0x / —x / —x |
| EV/FCFF | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 31,2x (EV/FCF × 1,09 = FCF después de intereses ÷ FCFF) | 40,0x (n=4: META 44,7x, MSFT 55,2x, AAPL 35,3x, NFLX 25,0x) × 1,00 = 40,0x | 39,6x / 32,5x / 85,5x | **36,6x** | 30,1x | 52,2x | 15,4x / —x / —x |
| P/E | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 24,0x | 27,8x (n=5: META 27,8x, MSFT 28,4x, AMZN 19,8x, AAPL 37,7x, NFLX 22,1x) × 1,00 = 27,8x | 29,4x / 24,2x / 55,4x | **26,8x** | 22,9x | 29,0x | 19,0x / —x / —x |
| P/FCFE | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 28,6x | 40,5x (n=4: META 45,9x, MSFT 56,4x, AAPL 35,2x, NFLX 26,2x) × 1,00 = 40,5x | 34,9x / 29,3x / 66,5x | **34,7x** | 28,6x | 50,7x | 16,0x / —x / —x |
| P/OCF | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,6x | 20,7x (n=5: META 14,4x, MSFT 20,7x, AMZN 17,9x, AAPL 32,8x, NFLX 24,5x) × 1,00 = 20,7x | 19,3x / 15,5x / 39,2x | **19,5x** | 16,9x | 23,0x | 11,1x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 17,9x: promedio de historia y peers 19,0x, acercado 25% al justificado (14,6x); rango de anclas 14,6x–19,7x. Atípicos excluidos de la historia: Dec '22 (13,0x: > 2,5x la mediana (1.5x)); Dec '23 (18,3x: > 2,5x la mediana (1.5x)); Dec '24 (18,2x: > 2,5x la mediana (1.5x)); Dec '25 (25,5x: > 2,5x la mediana (1.5x)); LTM (24,8x: > 2,5x la mediana (1.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 36,6x: promedio de historia y peers 35,6x, acercado 25% al justificado (39,6x); rango de anclas 31,2x–40,0x. Atípicos excluidos de la historia: Dec '22 (19,1x: > 2,5x la mediana (1.5x)); Dec '23 (25,3x: > 2,5x la mediana (1.5x)); Dec '24 (32,0x: > 2,5x la mediana (1.5x)); Dec '25 (52,2x: > 2,5x la mediana (1.5x)); LTM (78,4x: > 2,5x la mediana (1.5x)). EV/FCFF: la razón FCF después de intereses ÷ FCFF se fija en 1,09 (mediana de los tres cierres reales); el último cierre da 2,70 porque 'Interest / Other' incluye ganancias en inversiones, no intereses. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 26,8x: promedio de historia y peers 25,9x, acercado 25% al justificado (29,4x); rango de anclas 24,0x–29,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 34,7x: promedio de historia y peers 34,6x, acercado 25% al justificado (34,9x); rango de anclas 28,6x–40,5x. Atípicos excluidos de la historia: Dec '22 (19,0x: > 2,5x la mediana (1.6x)); Dec '23 (25,3x: > 2,5x la mediana (1.6x)); Dec '24 (32,0x: > 2,5x la mediana (1.6x)); Dec '25 (51,8x: > 2,5x la mediana (1.6x)); LTM (78,3x: > 2,5x la mediana (1.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 19,5x: promedio de historia y peers 19,6x, acercado 25% al justificado (19,3x); rango de anclas 18,6x–20,7x. Atípicos excluidos de la historia: Dec '22 (12,5x: > 2,5x la mediana (1.0x)); Dec '23 (17,3x: > 2,5x la mediana (1.0x)); Dec '24 (18,6x: > 2,5x la mediana (1.0x)); Dec '25 (23,0x: > 2,5x la mediana (1.0x)); LTM (22,5x: > 2,5x la mediana (1.0x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$256,95 frente a US$334,21 del DCF (−23%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$256,95 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$441,93 | US$355,36 | US$632,62 |
| EV/EBITDA | 20% | US$350,85 | US$274,67 | US$581,59 |
| EV/FCFF | 10% | US$270,99 | US$195,14 | US$461,73 |
| P/E | 20% | US$403,36 | US$295,39 | US$529,76 |
| P/FCFE | 5% | US$333,62 | US$229,90 | US$621,29 |
| P/OCF | 5% | US$324,25 | US$244,28 | US$450,20 |
| **Ponderado FY+3** | 100% | US$387,61 | US$299,38 | US$575,06 |

Valor presente (Ke 9,76%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$257,41 | US$262,07 | US$265,32 | US$261,60 | OK |
| EV/EBITDA | Conservador | US$215,74 | US$211,15 | US$207,70 | US$211,53 | OK |
| EV/EBITDA | Optimista | US$364,74 | US$406,51 | US$439,80 | US$403,68 | OK |
| EV/FCFF | Base | US$181,68 | US$200,98 | US$204,92 | US$195,86 | OK |
| EV/FCFF | Conservador | US$155,83 | US$150,92 | US$147,56 | US$151,44 | OK |
| EV/FCFF | Optimista | US$248,54 | US$312,41 | US$349,17 | US$303,37 | OK |
| P/E | Base | US$280,77 | US$293,38 | US$305,03 | US$293,06 | OK |
| P/E | Conservador | US$221,83 | US$221,66 | US$223,38 | US$222,29 | OK |
| P/E | Optimista | US$311,22 | US$359,25 | US$400,61 | US$357,03 | OK |
| P/FCFE | Base | US$229,10 | US$240,56 | US$252,28 | US$240,65 | OK |
| P/FCFE | Conservador | US$172,31 | US$172,32 | US$173,85 | US$172,83 | OK |
| P/FCFE | Optimista | US$343,85 | US$412,70 | US$469,82 | US$408,79 | OK |
| P/OCF | Base | US$216,80 | US$235,05 | US$245,20 | US$232,35 | OK |
| P/OCF | Conservador | US$180,98 | US$182,42 | US$184,73 | US$182,71 | OK |
| P/OCF | Optimista | US$258,39 | US$304,87 | US$340,44 | US$301,24 | OK |

Múltiplos consolidados hoy: US$256,95 / US$199,47 / US$363,30 · DCF técnico hoy: US$334,21 / US$268,73 / US$478,41 · Ponderado hoy: US$287,85 / US$227,18 / US$409,35 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para GOOG la diferencia es de −23% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$311,55 por acción y los múltiplos, US$244,87 hoy: 21% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$346,22 supone que los ingresos crecen 12,9% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 12,4% (+0,5 pp). Coherente: el precio supone un crecimiento parecido al del DCF.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$441,93 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,8%, WACC de los años 4-10 9,4%, ROE de FY+3 42,1% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 17,9x | 22,9x | −21% | 7,2% | 7,7% | −0,5 pp | Coherente con el DCF. |
| EV/FCFF | 36,6x | 62,1x | −39% | 6,5% | 7,7% | −1,2 pp | Revisar: el múltiplo vale 39% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 26,8x | 29,3x | −9% | 6,4% | 6,7% | −0,3 pp | Coherente con el DCF. |
| P/FCFE | 34,7x | 46,0x | −25% | 6,7% | 7,4% | −0,7 pp | Coherente con el DCF. |
| P/OCF | 19,5x | 26,7x | −27% | 6,7% | 7,5% | −0,8 pp | Revisar: el múltiplo vale 27% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$287,85 | — |
| Múltiplos Base +20% | US$317,40 | +10,3% |
| Múltiplos Base −20% | US$258,30 | −10,3% |
| Crecimiento años 2-5 +2 pp | US$299,22 | +3,9% |
| Crecimiento años 2-5 −2 pp | US$277,46 | −3,6% |
| Margen objetivo +3 pp | US$299,22 | +4,0% |
| Margen objetivo −3 pp | US$276,48 | −4,0% |
| WACC +1 pp | US$280,68 | −2,5% |
| WACC −1 pp | US$295,54 | +2,7% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 15,96 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 12,98 | 17,90 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 25,46 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 30,14 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 15,44 | 36,63 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 52,19 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 22,88 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 19,01 | 26,77 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 29,03 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 28,64 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 16,02 | 34,67 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 50,74 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 16,94 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 11,09 | 19,53 | Múltiplo base elegido con el protocolo v3 |
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
