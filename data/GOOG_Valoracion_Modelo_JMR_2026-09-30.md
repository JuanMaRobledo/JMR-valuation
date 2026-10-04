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

**Valor intrínseco principal · DCF Base hoy: US$297,57 por acción.** Complemento: DCF esperado por probabilidades US$253,24; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$123,20–US$389,77; precio con MOS 35% sobre el esperado: US$164,60; precio de referencia US$340,35. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Search resiste y Cloud es el segundo motor** (valor principal) | 40% | US$297,57 | US$119,03 |
| Conservadora · La IA conversacional erosiona Search | 25% | US$151,09 | US$37,77 |
| Disrupción · Deterioro de los fundamentales: Remedios antimonopolio y guerra de precios en IA | 15% | US$123,20 | US$18,48 |
| Optimista · Gemini y Cloud dominan la plataforma de IA | 20% | US$389,77 | US$77,95 |
| **DCF esperado (complemento)** | 100% | **US$253,24** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$311,55 por acción y los múltiplos, US$244,87 hoy: 21% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$297,57 | US$276,50 | US$284,93 | US$164,60 | US$394,69 |
| Conservador | US$151,09 | US$219,68 | US$192,24 | US$164,60 | US$251,07 |
| Optimista | US$389,77 | US$325,41 | US$351,16 | US$164,60 | US$506,83 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - Alphabet (GOOG)](https://docs.google.com/spreadsheets/d/1yt2zqdGz1JWEqV3SYqqL-nHarO7C1Oud1lvR3pY9i0U/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$340,35.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 11,2% | 18,0% | 20,6% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 7,2% | 11,0% | 17,8% | Input B29 |
| Margen EBIT objetivo | 30,3% | 35,3% | 37,3% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,15 / 1,12 | — | Input B32/B33 |
| DCF por acción hoy | US$151,09 | US$297,57 | US$389,77 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,07, ERP 5,07%, Ke 10,71%, costo de la deuda después de impuestos 4,91%, peso del patrimonio 97,9%, WACC inicial 10,59% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: los cierres 2016-2021 de la hoja dan múltiplos de ~1x porque el precio no está ajustado por el split 20:1 de julio de 2022; no son representativos y se usa la historia desde Dec '22. En P/E se quita el LTM: la utilidad del primer semestre de 2026 incluye US$135,9 mil millones de ganancias en acciones de otras empresas, que bajan el P/E a 17x. En EV/FCFF y P/FCFE se quita el LTM: el capex de 2026 (US$195-205 mil millones) deja el flujo de caja en mínimos y el múltiplo en ~78x, un pico transitorio frente al flujo de FY+3. B: grandes plataformas tecnológicas (Meta, Microsoft, Amazon, Apple, Netflix), datos de yfinance al 29-sep-2026. Amazon no tiene flujo de caja libre positivo y no entra en los múltiplos de flujo. Sin ajuste: Alphabet crece 24% con margen operativo de 34%, en línea con Meta y Microsoft. λ = 0,25: la Alphabet de FY+3 del escenario Base sigue siendo una plataforma de crecimiento alto con fuerte inversión en IA, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,3x | 19,7x (n=5: META 17,4x, MSFT 19,7x, AMZN 16,5x, AAPL 28,8x, NFLX 20,1x) × 1,00 = 19,7x | 14,3x / 12,3x / 14,4x | **17,8x** | 16,3x | 19,8x | 13,0x / —x / —x |
| EV/FCFF | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 31,2x (EV/FCF × 1,09 = FCF después de intereses ÷ FCFF) | 40,0x (n=4: META 44,7x, MSFT 55,2x, AAPL 35,3x, NFLX 25,0x) × 1,00 = 40,0x | 28,5x / 21,0x / 40,6x | **33,9x** | 26,9x | 44,0x | 15,4x / —x / —x |
| P/E | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 24,0x | 27,8x (n=5: META 27,8x, MSFT 28,4x, AMZN 19,8x, AAPL 37,7x, NFLX 22,1x) × 1,00 = 27,8x | 19,3x / 14,8x / 26,1x | **24,3x** | 20,2x | 27,8x | 19,0x / —x / —x |
| P/FCFE | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 28,6x | 40,5x (n=4: META 45,9x, MSFT 56,4x, AAPL 35,2x, NFLX 26,2x) × 1,00 = 40,5x | 24,4x / 18,6x / 32,7x | **32,0x** | 25,7x | 40,9x | 16,0x / —x / —x |
| P/OCF | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,6x | 20,7x (n=5: META 14,4x, MSFT 20,7x, AMZN 17,9x, AAPL 32,8x, NFLX 24,5x) × 1,00 = 20,7x | 15,5x / 11,7x / 19,9x | **18,6x** | 15,8x | 22,8x | 11,1x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 17,8x: promedio de historia y peers 19,0x, acercado 25% al justificado (14,3x); rango de anclas 14,3x–19,7x. Atípicos excluidos de la historia: Dec '22 (13,0x: > 2,5x la mediana (1.5x)); Dec '23 (18,3x: > 2,5x la mediana (1.5x)); Dec '24 (18,2x: > 2,5x la mediana (1.5x)); Dec '25 (25,5x: > 2,5x la mediana (1.5x)); LTM (24,0x: > 2,5x la mediana (1.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 33,9x: promedio de historia y peers 35,6x, acercado 25% al justificado (28,5x); rango de anclas 28,5x–40,0x. Atípicos excluidos de la historia: Dec '22 (19,1x: > 2,5x la mediana (1.5x)); Dec '23 (25,3x: > 2,5x la mediana (1.5x)); Dec '24 (32,0x: > 2,5x la mediana (1.5x)); Dec '25 (52,2x: > 2,5x la mediana (1.5x)); LTM (76,0x: > 2,5x la mediana (1.5x)). EV/FCFF: la razón FCF después de intereses ÷ FCFF se fija en 1,09 (mediana de los tres cierres reales); el último cierre da 2,70 porque 'Interest / Other' incluye ganancias en inversiones, no intereses. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 24,3x: promedio de historia y peers 25,9x, acercado 25% al justificado (19,3x); rango de anclas 19,3x–27,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 32,0x: promedio de historia y peers 34,6x, acercado 25% al justificado (24,4x); rango de anclas 24,4x–40,5x. Atípicos excluidos de la historia: Dec '22 (19,0x: > 2,5x la mediana (1.6x)); Dec '23 (25,3x: > 2,5x la mediana (1.6x)); Dec '24 (32,0x: > 2,5x la mediana (1.6x)); Dec '25 (51,8x: > 2,5x la mediana (1.6x)); LTM (78,3x: > 2,5x la mediana (1.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 18,6x: promedio de historia y peers 19,6x, acercado 25% al justificado (15,5x); rango de anclas 15,5x–20,7x. Atípicos excluidos de la historia: Dec '22 (12,5x: > 2,5x la mediana (1.0x)); Dec '23 (17,3x: > 2,5x la mediana (1.0x)); Dec '24 (18,6x: > 2,5x la mediana (1.0x)); Dec '25 (23,0x: > 2,5x la mediana (1.0x)); LTM (22,5x: > 2,5x la mediana (1.0x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$276,50 frente a US$297,57 del DCF (−7%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$276,50 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,71%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$123,20) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$297,57 por acción.** Complemento: DCF esperado por probabilidades US$253,24. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$297,57 | US$151,09 | US$389,77 |
| EV/EBITDA | 17,8× / 16,3× / 19,8× | 20% | 33% | US$280,55 | US$228,03 | US$343,01 |
| EV/FCFF | 33,9× / 26,9× / 44,0× | 10% | 17% | US$248,39 | US$216,59 | US$232,57 |
| P/E | 24,3× / 20,2× / 27,8× | 20% | 33% | US$284,61 | US$207,54 | US$363,09 |
| P/FCFE | 32,0× / 25,7× / 40,9× | 5% | 8% | US$295,80 | US$237,50 | US$320,28 |
| P/OCF | 18,6× / 15,8× / 22,8× | 5% | 8% | US$264,84 | US$223,17 | US$295,12 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$276,50 | US$219,68 | US$325,41 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$284,93 | US$192,24 | US$351,16 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$403,82 | US$205,04 | US$528,95 |
| EV/EBITDA (total con dividendos) | 17,8× / 16,3× / 19,8× | 20% | 33% | US$387,09 | US$291,67 | US$501,38 |
| EV/FCFF (total con dividendos) | 33,9× / 26,9× / 44,0× | 10% | 17% | US$369,39 | US$283,50 | US$399,09 |
| P/E (total con dividendos) | 24,3× / 20,2× / 27,8× | 20% | 33% | US$394,48 | US$264,57 | US$535,19 |
| P/FCFE (total con dividendos) | 32,0× / 25,7× / 40,9× | 5% | 8% | US$417,67 | US$297,40 | US$501,72 |
| P/OCF (total con dividendos) | 18,6× / 15,8× / 22,8× | 5% | 8% | US$380,41 | US$291,76 | US$458,88 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$388,60 | US$281,76 | US$492,09 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$2,49 | US$2,49 | US$2,49 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$386,10 | US$279,27 | US$489,60 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$394,69 | US$251,07 | US$506,83 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,71%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$273,21 | US$283,00 | US$285,45 | US$280,55 | OK |
| EV/EBITDA | Conservador | US$240,84 | US$228,11 | US$215,13 | US$228,03 | OK |
| EV/EBITDA | Optimista | US$312,35 | US$347,03 | US$369,67 | US$343,01 | OK |
| EV/FCFF | Base | US$219,82 | US$252,93 | US$272,40 | US$248,39 | OK |
| EV/FCFF | Conservador | US$221,11 | US$219,55 | US$209,11 | US$216,59 | OK |
| EV/FCFF | Optimista | US$162,91 | US$240,53 | US$294,29 | US$232,57 | OK |
| P/E | Base | US$275,76 | US$287,18 | US$290,89 | US$284,61 | OK |
| P/E | Conservador | US$220,14 | US$207,32 | US$195,16 | US$207,54 | OK |
| P/E | Optimista | US$327,00 | US$367,68 | US$394,58 | US$363,09 | OK |
| P/FCFE | Base | US$287,19 | US$292,25 | US$307,98 | US$295,80 | OK |
| P/FCFE | Conservador | US$260,30 | US$232,86 | US$219,35 | US$237,50 | OK |
| P/FCFE | Optimista | US$272,25 | US$318,68 | US$369,91 | US$320,28 | OK |
| P/OCF | Base | US$245,74 | US$268,27 | US$280,52 | US$264,84 | OK |
| P/OCF | Conservador | US$228,96 | US$225,34 | US$215,20 | US$223,17 | OK |
| P/OCF | Optimista | US$246,57 | US$300,45 | US$338,34 | US$295,12 | OK |

Múltiplos consolidados hoy: US$276,50 / US$219,68 / US$325,41 · DCF de las historias hoy: US$297,57 / US$151,09 / US$389,77 · Ponderado hoy: US$284,93 / US$192,24 / US$351,16 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para GOOG la diferencia es de −7% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$311,55 por acción y los múltiplos, US$244,87 hoy: 21% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$340,35 supone que los ingresos crecen 16,3% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,7% (+4,6 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$403,82 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,7%, WACC de los años 4-10 10,1%, ROE de FY+3 30,8% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 17,8x | 18,5x | −4% | 7,1% | 7,2% | −0,1 pp | Coherente con el DCF. |
| EV/FCFF | 33,9x | 36,9x | −9% | 6,9% | 7,2% | −0,3 pp | Coherente con el DCF. |
| P/E | 24,3x | 24,8x | −2% | 7,3% | 7,4% | −0,1 pp | Coherente con el DCF. |
| P/FCFE | 32,0x | 31,0x | +3% | 7,4% | 7,2% | +0,1 pp | Coherente con el DCF. |
| P/OCF | 18,6x | 19,7x | −6% | 7,0% | 7,2% | −0,2 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$284,93 | — |
| Múltiplos Base +20% | US$316,99 | +11,3% |
| Múltiplos Base −20% | US$252,88 | −11,3% |
| Crecimiento años 2-5 +2 pp | US$294,95 | +3,5% |
| Crecimiento años 2-5 −2 pp | US$275,76 | −3,2% |
| Margen objetivo +3 pp | US$295,11 | +3,6% |
| Margen objetivo −3 pp | US$274,76 | −3,6% |
| WACC +1 pp | US$278,52 | −2,3% |
| WACC −1 pp | US$291,81 | +2,4% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 16,28 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 12,98 | 17,83 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 19,83 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 26,92 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 15,44 | 33,86 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 44,01 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 20,25 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 19,01 | 24,27 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 27,76 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 25,69 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 16,02 | 32,02 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 40,89 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 15,80 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 11,09 | 18,59 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 22,80 | Múltiplo optimista elegido con el protocolo v3 |
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
