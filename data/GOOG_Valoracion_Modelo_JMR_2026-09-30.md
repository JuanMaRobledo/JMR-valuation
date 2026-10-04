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

**Valor intrínseco principal · DCF Base hoy: US$317,02 por acción.** Complemento: DCF esperado por probabilidades US$269,49; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$129,33–US$416,68; precio con MOS 35% sobre el esperado: US$175,17; precio de referencia US$340,35. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Search resiste y Cloud es el segundo motor** (valor principal) | 40% | US$317,02 | US$126,81 |
| Conservadora · La IA conversacional erosiona Search | 25% | US$159,80 | US$39,95 |
| Disrupción · Deterioro de los fundamentales: Remedios antimonopolio y guerra de precios en IA | 15% | US$129,33 | US$19,40 |
| Optimista · Gemini y Cloud dominan la plataforma de IA | 20% | US$416,68 | US$83,34 |
| **DCF esperado (complemento)** | 100% | **US$269,49** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$311,55 por acción y los múltiplos, US$244,87 hoy: 21% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$317,02 | US$295,78 | US$304,28 | US$175,17 | US$411,91 |
| Conservador | US$159,80 | US$230,78 | US$202,39 | US$175,17 | US$258,61 |
| Optimista | US$416,68 | US$350,21 | US$376,80 | US$175,17 | US$531,52 |

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
| Sales-to-capital años 1-5 / 6-10 | — | 1,15 / 1,43 | — | Input B32/B33 |
| DCF por acción hoy | US$159,80 | US$317,02 | US$416,68 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,07, ERP 4,09%, Ke 9,67%, costo de la deuda después de impuestos 4,91%, peso del patrimonio 97,9%, WACC inicial 9,57% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: los cierres 2016-2021 de la hoja dan múltiplos de ~1x porque el precio no está ajustado por el split 20:1 de julio de 2022; no son representativos y se usa la historia desde Dec '22. En P/E se quita el LTM: la utilidad del primer semestre de 2026 incluye US$135,9 mil millones de ganancias en acciones de otras empresas, que bajan el P/E a 17x. En EV/FCFF y P/FCFE se quita el LTM: el capex de 2026 (US$195-205 mil millones) deja el flujo de caja en mínimos y el múltiplo en ~78x, un pico transitorio frente al flujo de FY+3. B: grandes plataformas tecnológicas (Meta, Microsoft, Amazon, Apple, Netflix), datos de yfinance al 29-sep-2026. Amazon no tiene flujo de caja libre positivo y no entra en los múltiplos de flujo. Sin ajuste: Alphabet crece 24% con margen operativo de 34%, en línea con Meta y Microsoft. λ = 0,25: la Alphabet de FY+3 del escenario Base sigue siendo una plataforma de crecimiento alto con fuerte inversión en IA, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,3x | 19,7x (n=5: META 17,4x, MSFT 19,7x, AMZN 16,5x, AAPL 28,8x, NFLX 20,1x) × 1,00 = 19,7x | 17,0x / 14,0x / 18,5x | **18,5x** | 16,6x | 21,1x | 13,0x / —x / —x |
| EV/FCFF | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 31,2x (EV/FCF × 1,09 = FCF después de intereses ÷ FCFF) | 40,0x (n=4: META 44,7x, MSFT 55,2x, AAPL 35,3x, NFLX 25,0x) × 1,00 = 40,0x | 33,9x / 23,8x / 52,2x | **35,2x** | 27,6x | 47,1x | 15,4x / —x / —x |
| P/E | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 24,0x | 27,8x (n=5: META 27,8x, MSFT 28,4x, AMZN 19,8x, AAPL 37,7x, NFLX 22,1x) × 1,00 = 27,8x | 25,4x / 18,2x / 38,3x | **25,8x** | 21,1x | 29,0x | 19,0x / —x / —x |
| P/FCFE | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 28,6x | 40,5x (n=4: META 45,9x, MSFT 56,4x, AAPL 35,2x, NFLX 26,2x) × 1,00 = 40,5x | 32,0x / 22,9x / 48,0x | **33,9x** | 26,6x | 45,1x | 16,0x / —x / —x |
| P/OCF | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,6x | 20,7x (n=5: META 14,4x, MSFT 20,7x, AMZN 17,9x, AAPL 32,8x, NFLX 24,5x) × 1,00 = 20,7x | 20,4x / 14,4x / 29,3x | **19,8x** | 16,5x | 23,0x | 11,1x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 18,5x: promedio de historia y peers 19,0x, acercado 25% al justificado (17,0x); rango de anclas 17,0x–19,7x. Atípicos excluidos de la historia: Dec '22 (13,0x: > 2,5x la mediana (1.5x)); Dec '23 (18,3x: > 2,5x la mediana (1.5x)); Dec '24 (18,2x: > 2,5x la mediana (1.5x)); Dec '25 (25,5x: > 2,5x la mediana (1.5x)); LTM (24,0x: > 2,5x la mediana (1.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 35,2x: promedio de historia y peers 35,6x, acercado 25% al justificado (33,9x); rango de anclas 31,2x–40,0x. Atípicos excluidos de la historia: Dec '22 (19,1x: > 2,5x la mediana (1.5x)); Dec '23 (25,3x: > 2,5x la mediana (1.5x)); Dec '24 (32,0x: > 2,5x la mediana (1.5x)); Dec '25 (52,2x: > 2,5x la mediana (1.5x)); LTM (76,0x: > 2,5x la mediana (1.5x)). EV/FCFF: la razón FCF después de intereses ÷ FCFF se fija en 1,09 (mediana de los tres cierres reales); el último cierre da 2,70 porque 'Interest / Other' incluye ganancias en inversiones, no intereses. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 25,8x: promedio de historia y peers 25,9x, acercado 25% al justificado (25,4x); rango de anclas 24,0x–27,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 33,9x: promedio de historia y peers 34,6x, acercado 25% al justificado (32,0x); rango de anclas 28,6x–40,5x. Atípicos excluidos de la historia: Dec '22 (19,0x: > 2,5x la mediana (1.6x)); Dec '23 (25,3x: > 2,5x la mediana (1.6x)); Dec '24 (32,0x: > 2,5x la mediana (1.6x)); Dec '25 (51,8x: > 2,5x la mediana (1.6x)); LTM (78,3x: > 2,5x la mediana (1.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 19,8x: promedio de historia y peers 19,6x, acercado 25% al justificado (20,4x); rango de anclas 18,6x–20,7x. Atípicos excluidos de la historia: Dec '22 (12,5x: > 2,5x la mediana (1.0x)); Dec '23 (17,3x: > 2,5x la mediana (1.0x)); Dec '24 (18,6x: > 2,5x la mediana (1.0x)); Dec '25 (23,0x: > 2,5x la mediana (1.0x)); LTM (22,5x: > 2,5x la mediana (1.0x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$295,78 frente a US$317,02 del DCF (−7%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$295,78 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,67%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$129,33) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$317,02 por acción.** Complemento: DCF esperado por probabilidades US$269,49. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$317,02 | US$159,80 | US$416,68 |
| EV/EBITDA | 18,5× / 16,6× / 21,1× | 20% | 33% | US$296,06 | US$237,19 | US$370,88 |
| EV/FCFF | 35,2× / 27,6× / 47,1× | 10% | 17% | US$262,58 | US$225,76 | US$252,99 |
| P/E | 25,8× / 21,1× / 29,0× | 20% | 33% | US$308,20 | US$220,15 | US$387,15 |
| P/FCFE | 33,9× / 26,6× / 45,1× | 5% | 8% | US$319,54 | US$250,91 | US$360,32 |
| P/OCF | 19,8× / 16,5× / 23,0× | 5% | 8% | US$287,66 | US$237,56 | US$304,10 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$295,78 | US$230,78 | US$350,21 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$304,28 | US$202,39 | US$376,80 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$418,13 | US$210,76 | US$549,57 |
| EV/EBITDA (total con dividendos) | 18,5× / 16,6× / 21,1× | 20% | 33% | US$400,81 | US$297,80 | US$531,85 |
| EV/FCFF (total con dividendos) | 35,2× / 27,6× / 47,1× | 10% | 17% | US$383,04 | US$290,01 | US$425,74 |
| P/E (total con dividendos) | 25,8× / 21,1× / 29,0× | 20% | 33% | US$419,03 | US$275,45 | US$559,56 |
| P/FCFE (total con dividendos) | 33,9× / 26,6× / 45,1× | 5% | 8% | US$442,57 | US$308,42 | US$553,24 |
| P/OCF (total con dividendos) | 19,8× / 16,5× / 23,0× | 5% | 8% | US$405,21 | US$304,76 | US$463,48 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$407,77 | US$290,51 | US$519,48 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$2,49 | US$2,49 | US$2,49 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$405,28 | US$288,02 | US$516,99 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$411,91 | US$258,61 | US$531,52 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,67%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$285,49 | US$298,60 | US$304,08 | US$296,06 | OK |
| EV/EBITDA | Conservador | US$248,25 | US$237,36 | US$225,98 | US$237,19 | OK |
| EV/EBITDA | Optimista | US$334,19 | US$375,03 | US$403,43 | US$370,88 | OK |
| EV/FCFF | Base | US$229,91 | US$267,21 | US$290,61 | US$262,58 | OK |
| EV/FCFF | Conservador | US$228,31 | US$228,88 | US$220,07 | US$225,76 | OK |
| EV/FCFF | Optimista | US$174,78 | US$261,22 | US$322,98 | US$252,99 | OK |
| P/E | Base | US$295,78 | US$310,92 | US$317,90 | US$308,20 | OK |
| P/E | Conservador | US$231,43 | US$220,00 | US$209,03 | US$220,15 | OK |
| P/E | Optimista | US$345,19 | US$391,81 | US$424,44 | US$387,15 | OK |
| P/FCFE | Base | US$307,27 | US$315,62 | US$335,74 | US$319,54 | OK |
| P/FCFE | Conservador | US$272,57 | US$246,13 | US$234,03 | US$250,91 | OK |
| P/FCFE | Optimista | US$303,14 | US$358,16 | US$419,65 | US$360,32 | OK |
| P/OCF | Base | US$264,32 | US$291,26 | US$307,42 | US$287,66 | OK |
| P/OCF | Conservador | US$241,50 | US$239,92 | US$231,25 | US$237,56 | OK |
| P/OCF | Optimista | US$251,43 | US$309,28 | US$351,60 | US$304,10 | OK |

Múltiplos consolidados hoy: US$295,78 / US$230,78 / US$350,21 · DCF de las historias hoy: US$317,02 / US$159,80 / US$416,68 · Ponderado hoy: US$304,28 / US$202,39 / US$376,80 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para GOOG la diferencia es de −7% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$311,55 por acción y los múltiplos, US$244,87 hoy: 21% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$340,35 supone que los ingresos crecen 15,0% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,7% (+3,3 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$418,13 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,7%, WACC de los años 4-10 9,5%, ROE de FY+3 30,8% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 18,5x | 19,2x | −4% | 6,6% | 6,7% | −0,1 pp | Coherente con el DCF. |
| EV/FCFF | 35,2x | 38,3x | −8% | 6,5% | 6,7% | −0,2 pp | Coherente con el DCF. |
| P/E | 25,8x | 25,7x | +0% | 6,4% | 6,4% | +0,0 pp | Coherente con el DCF. |
| P/FCFE | 33,9x | 32,1x | +6% | 6,5% | 6,3% | +0,2 pp | Coherente con el DCF. |
| P/OCF | 19,8x | 20,4x | −3% | 6,2% | 6,3% | −0,1 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$304,28 | — |
| Múltiplos Base +20% | US$338,63 | +11,3% |
| Múltiplos Base −20% | US$269,93 | −11,3% |
| Crecimiento años 2-5 +2 pp | US$315,16 | +3,6% |
| Crecimiento años 2-5 −2 pp | US$294,31 | −3,3% |
| Margen objetivo +3 pp | US$315,07 | +3,5% |
| Margen objetivo −3 pp | US$293,48 | −3,5% |
| WACC +1 pp | US$297,35 | −2,3% |
| WACC −1 pp | US$311,71 | +2,4% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 16,65 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 12,98 | 18,50 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 21,09 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 27,59 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 15,44 | 35,19 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 47,12 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 21,09 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 19,01 | 25,79 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 29,03 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 26,65 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 16,02 | 33,94 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 45,11 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 16,51 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 11,09 | 19,81 | Múltiplo base elegido con el protocolo v3 |
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
