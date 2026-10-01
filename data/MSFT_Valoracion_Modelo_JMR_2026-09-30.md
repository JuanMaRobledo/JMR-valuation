---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Microsoft Corporation"
ticker: "MSFT"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1ubjlRP0jbGmG_sXEoTrvonRkwqy5AoOd1ESrU4c3-rY/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Microsoft Corporation (MSFT) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$458,42 por acción.** Complemento: DCF esperado por probabilidades US$405,29; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$197,86–US$599,73; precio con MOS 35% sobre el esperado: US$263,44; precio de referencia US$518,46. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son la calibración técnica anterior de la hoja (Base técnico US$467,13) y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Azure y Copilot sostienen el doble dígito** (valor principal) | 45% | US$458,42 | US$206,29 |
| Conservadora · El capex de IA rinde menos de lo esperado | 25% | US$237,05 | US$59,26 |
| Disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige | 10% | US$197,86 | US$19,79 |
| Optimista · Microsoft gana la plataforma empresarial de IA | 20% | US$599,73 | US$119,95 |
| **DCF esperado (complemento)** | 100% | **US$405,29** | |

Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$466,38 por acción y los múltiplos, US$466,16 hoy: prácticamente igual al DCF. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

| Escenario | DCF técnico anterior hoy (calibración) | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$467,13 | US$482,31 | US$473,20 | US$263,44 | US$641,83 |
| Conservador | US$361,69 | US$345,41 | US$355,18 | US$263,44 | US$474,01 |
| Optimista | US$552,57 | US$614,62 | US$577,39 | US$263,44 | US$793,87 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - Valoración MSFT - 2026-09-16](https://docs.google.com/spreadsheets/d/1ubjlRP0jbGmG_sXEoTrvonRkwqy5AoOd1ESrU4c3-rY/edit).
- Análisis del 16 de sept de 2026. Precio de referencia de la hoja: US$518,46.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 14,0% | 16,5% | 19,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 8,0% | 12,0% | 14,0% | Input B29 |
| Margen EBIT objetivo | 43,2% | 46,2% | 49,2% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 0,62 / 0,94 | — | Input B32/B33 |
| DCF por acción hoy | US$361,69 | US$467,13 | US$552,57 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,25%, beta apalancada 1,36, ERP 4,46%, Ke 10,30%, costo de la deuda después de impuestos 4,15%, peso del patrimonio 97,5%, WACC inicial 10,15% y terminal 8,48%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Sin cambio de etapa: Microsoft sigue creciendo a doble dígito y cotiza por debajo de su promedio de cinco años; se usa la mediana de los últimos 5 cierres + LTM. Se excluye la columna sin fecha de la hoja. B: grandes plataformas tecnológicas y de software (Alphabet, Apple, Amazon, Oracle, Meta, Salesforce), datos de yfinance al 29-sep-2026. Amazon y Oracle no tienen flujo de caja libre positivo y no entran en los múltiplos de flujo. Ajuste +5%: Microsoft tiene el margen operativo más alto del grupo (45% frente a ~33%) y Azure acelera (~40%) con una cartera de US$678 mil millones. λ = 0 (30-sep-2026): el justificado C supone que el ROE de FY+3 se mantiene para siempre, mientras que el DCF revisado limita el ROIC después del año 10 al 25,9% (el menor entre el actual y el de la industria). Para que los múltiplos sean coherentes con el DCF, C se deja fuera del Base y se conserva como referencia en la tabla.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana de los últimos 5 cierres + LTM depurados = 22,1x | 17,1x (n=6: GOOG 23,2x, AAPL 28,8x, AMZN 16,5x, ORCL 15,6x, META 17,4x, CRM 16,9x) × 1,05 = 18,0x | 13,1x / 9,4x / 16,9x | **20,0x** | 17,2x | 24,6x | —x / —x / —x |
| EV/FCFF | mediana de los últimos 5 cierres + LTM depurados = 42,8x (EV/FCF × 0,98 = FCF después de intereses ÷ FCFF) | 40,0x (n=4: GOOG 73,1x, AAPL 35,3x, META 44,7x, CRM 13,8x) × 1,05 = 42,0x | 35,7x / 25,5x / 44,4x | **42,4x** | 31,2x | 50,6x | —x / —x / —x |
| P/E | mediana de los últimos 5 cierres + LTM depurados = 31,8x | 21,1x (n=6: GOOG 16,9x, AAPL 37,7x, AMZN 19,8x, ORCL 21,6x, META 27,8x, CRM 20,6x) × 1,05 = 22,2x | 23,7x / 18,2x / 28,2x | **27,0x** | 23,0x | 31,9x | —x / —x / —x |
| P/FCFE | mediana de los últimos 5 cierres + LTM depurados = 44,2x | 40,5x (n=4: GOOG 77,4x, AAPL 35,2x, META 45,9x, CRM 12,2x) × 1,05 = 42,6x | 28,2x / 21,4x / 33,5x | **43,4x** | 32,6x | 51,3x | —x / —x / —x |
| P/OCF | mediana de los últimos 5 cierres + LTM depurados = 24,3x | 16,2x (n=6: GOOG 22,2x, AAPL 32,8x, AMZN 17,9x, ORCL 8,9x, META 14,4x, CRM 11,8x) × 1,05 = 17,0x | 13,7x / 10,0x / 17,0x | **20,7x** | 16,1x | 25,2x | —x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 20,0x: promedio de historia y peers 20,0x, acercado 0% al justificado (13,1x); rango de anclas 13,1x–22,1x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 42,4x: promedio de historia y peers 42,4x, acercado 0% al justificado (35,7x); rango de anclas 35,7x–42,8x. Atípicos excluidos de la historia: ninguno. EV/FCFF: la razón FCF después de intereses ÷ FCFF se fija en 0,98 (mediana de los tres cierres reales); el último cierre da 1,28 porque 'Interest / Other' incluye partidas no operativas. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 27,0x: promedio de historia y peers 27,0x, acercado 0% al justificado (23,7x); rango de anclas 22,2x–31,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 43,4x: promedio de historia y peers 43,4x, acercado 0% al justificado (28,2x); rango de anclas 28,2x–44,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 20,7x: promedio de historia y peers 20,7x, acercado 0% al justificado (13,7x); rango de anclas 13,7x–24,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$482,31 frente a US$467,13 del DCF (+3%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$482,31 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$626,92 | US$485,42 | US$741,59 |
| EV/EBITDA | 10% | US$744,27 | US$555,96 | US$986,02 |
| EV/FCFF | 15% | US$596,63 | US$382,06 | US$784,13 |
| P/E | 5% | US$681,02 | US$501,74 | US$871,25 |
| P/FCFE | 5% | US$713,04 | US$447,51 | US$941,64 |
| P/OCF | 5% | US$641,09 | US$447,76 | US$840,90 |
| **Ponderado FY+3** | 100% | US$641,83 | US$474,01 | US$793,87 |

Valor presente (Ke 10,30%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$528,49 | US$542,24 | US$554,57 | US$541,77 | OK |
| EV/EBITDA | Conservador | US$424,23 | US$419,57 | US$414,26 | US$419,35 | OK |
| EV/EBITDA | Optimista | US$662,57 | US$701,54 | US$734,70 | US$699,60 | OK |
| EV/FCFF | Base | US$412,52 | US$431,79 | US$444,56 | US$429,62 | OK |
| EV/FCFF | Conservador | US$290,59 | US$286,16 | US$284,68 | US$287,14 | OK |
| EV/FCFF | Optimista | US$500,30 | US$549,96 | US$584,27 | US$544,84 | OK |
| P/E | Base | US$491,56 | US$498,67 | US$507,44 | US$499,22 | OK |
| P/E | Conservador | US$389,62 | US$380,67 | US$373,86 | US$381,38 | OK |
| P/E | Optimista | US$592,56 | US$622,09 | US$649,19 | US$621,28 | OK |
| P/FCFE | Base | US$518,37 | US$516,80 | US$531,29 | US$522,16 | OK |
| P/FCFE | Conservador | US$364,61 | US$335,69 | US$333,45 | US$344,58 | OK |
| P/FCFE | Optimista | US$637,95 | US$662,87 | US$701,63 | US$667,48 | OK |
| P/OCF | Base | US$450,70 | US$465,82 | US$477,69 | US$464,73 | OK |
| P/OCF | Conservador | US$341,18 | US$336,68 | US$333,63 | US$337,16 | OK |
| P/OCF | Optimista | US$559,84 | US$596,92 | US$626,57 | US$594,44 | OK |

Múltiplos consolidados hoy: US$482,31 / US$345,41 / US$614,62 · DCF técnico hoy: US$467,13 / US$361,69 / US$552,57 · Ponderado hoy: US$473,20 / US$355,18 / US$577,39 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para MSFT la diferencia es de +3% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$466,38 por acción y los múltiplos, US$466,16 hoy: prácticamente igual al DCF. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$518,46 supone que los ingresos crecen 14,9% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 12,9% (+2,0 pp). Coherente: el precio supone un crecimiento parecido al del DCF.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$626,92 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,2%, WACC de los años 4-10 9,4%, ROE de FY+3 40,6% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 20,0x | 16,8x | +19% | 7,5% | 7,1% | +0,4 pp | Coherente con el DCF. |
| EV/FCFF | 42,4x | 44,6x | −5% | 6,9% | 7,0% | −0,1 pp | Coherente con el DCF. |
| P/E | 27,0x | 24,8x | +9% | 6,9% | 6,6% | +0,3 pp | Coherente con el DCF. |
| P/FCFE | 43,4x | 38,1x | +14% | 7,8% | 7,4% | +0,3 pp | Coherente con el DCF. |
| P/OCF | 20,7x | 20,2x | +2% | 7,7% | 7,6% | +0,1 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$473,20 | — |
| Múltiplos Base +20% | US$511,22 | +8,0% |
| Múltiplos Base −20% | US$435,19 | −8,0% |
| Crecimiento años 2-5 +2 pp | US$497,11 | +5,1% |
| Crecimiento años 2-5 −2 pp | US$451,36 | −4,6% |
| Margen objetivo +3 pp | US$491,61 | +3,9% |
| Margen objetivo −3 pp | US$454,80 | −3,9% |
| WACC +1 pp | US$457,02 | −3,4% |
| WACC −1 pp | US$490,56 | +3,7% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 17,18 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | — | 20,04 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 24,64 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 31,25 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | — | 42,41 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 50,65 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 23,01 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | — | 26,96 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 31,86 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 32,62 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | — | 43,39 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 51,33 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 16,15 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | — | 20,67 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 25,22 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/MSFT_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1ubjlRP0jbGmG_sXEoTrvonRkwqy5AoOd1ESrU4c3-rY/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (GOOG, AAPL, AMZN, ORCL, META, CRM).
- [CNBC, 29-jul-2026: resultados 4T FY26 de Microsoft](https://www.cnbc.com/2026/07/29/microsoft-msft-q4-earnings-report-2026.html)
- [CNBC, 29-abr-2026: Microsoft proyecta US$190 mil millones de capex](https://www.cnbc.com/2026/04/29/microsoft-msft-q3-earnings-report-2026.html)

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
