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

**Valor intrínseco principal · DCF Base hoy: US$330,86 por acción.** Complemento: DCF esperado por probabilidades US$278,78; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$128,74–US$436,51; precio con MOS 35% sobre el esperado: US$181,21; precio de referencia US$343,88. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Search resiste y Cloud es el segundo motor** (valor principal) | 40% | US$330,86 | US$132,34 |
| Conservadora · La IA conversacional erosiona Search | 25% | US$159,28 | US$39,82 |
| Disrupción · Deterioro de los fundamentales: Remedios antimonopolio y guerra de precios en IA | 15% | US$128,74 | US$19,31 |
| Optimista · Gemini y Cloud dominan la plataforma de IA | 20% | US$436,51 | US$87,30 |
| **DCF esperado (complemento)** | 100% | **US$278,78** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$311,55 por acción y los múltiplos, US$244,87 hoy: 21% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$330,86 | US$284,73 | US$303,19 | US$181,21 | US$415,86 |
| Conservador | US$159,28 | US$224,37 | US$198,34 | US$181,21 | US$256,88 |
| Optimista | US$436,51 | US$339,43 | US$378,27 | US$181,21 | US$539,91 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - Alphabet (GOOG)](https://docs.google.com/spreadsheets/d/1yt2zqdGz1JWEqV3SYqqL-nHarO7C1Oud1lvR3pY9i0U/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$343,88.
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
| DCF por acción hoy | US$159,28 | US$330,86 | US$436,51 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,07, ERP 4,68%, Ke 10,30%, costo de la deuda después de impuestos 4,91%, peso del patrimonio 97,9%, WACC inicial 10,18% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: los cierres 2016-2021 de la hoja dan múltiplos de ~1x porque el precio no está ajustado por el split 20:1 de julio de 2022; no son representativos y se usa la historia desde Dec '22. En P/E se quita el LTM: la utilidad del primer semestre de 2026 incluye US$135,9 mil millones de ganancias en acciones de otras empresas, que bajan el P/E a 17x. En EV/FCFF y P/FCFE se quita el LTM: el capex de 2026 (US$195-205 mil millones) deja el flujo de caja en mínimos y el múltiplo en ~78x, un pico transitorio frente al flujo de FY+3. B: grandes plataformas tecnológicas (Meta, Microsoft, Amazon, Apple, Netflix), datos de yfinance al 29-sep-2026. Amazon no tiene flujo de caja libre positivo y no entra en los múltiplos de flujo. Sin ajuste: Alphabet crece 24% con margen operativo de 34%, en línea con Meta y Microsoft. λ = 0,25: la Alphabet de FY+3 del escenario Base sigue siendo una plataforma de crecimiento alto con fuerte inversión en IA, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,3x | 19,7x (n=5: META 17,4x, MSFT 19,7x, AMZN 16,5x, AAPL 28,8x, NFLX 20,1x) × 1,00 = 19,7x | 16,0x / 13,4x / 17,0x | **18,3x** | 16,5x | 20,6x | 13,0x / —x / —x |
| EV/FCFF | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 31,2x (EV/FCF × 1,09 = FCF después de intereses ÷ FCFF) | 40,0x (n=4: META 44,7x, MSFT 55,2x, AAPL 35,3x, NFLX 25,0x) × 1,00 = 40,0x | 32,0x / 22,9x / 47,9x | **34,7x** | 27,4x | 46,0x | 15,4x / —x / —x |
| P/E | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 24,0x | 27,8x (n=5: META 27,8x, MSFT 28,4x, AMZN 19,8x, AAPL 37,7x, NFLX 22,1x) × 1,00 = 27,8x | 21,4x / 16,0x / 29,9x | **24,8x** | 20,5x | 28,7x | 19,0x / —x / —x |
| P/FCFE | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 28,6x | 40,5x (n=4: META 45,9x, MSFT 56,4x, AAPL 35,2x, NFLX 26,2x) × 1,00 = 40,5x | 26,9x / 20,1x / 37,5x | **32,7x** | 26,0x | 42,2x | 16,0x / —x / —x |
| P/OCF | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,6x | 20,7x (n=5: META 14,4x, MSFT 20,7x, AMZN 17,9x, AAPL 32,8x, NFLX 24,5x) × 1,00 = 20,7x | 17,2x / 12,6x / 22,9x | **19,0x** | 16,0x | 23,0x | 11,1x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 18,3x: promedio de historia y peers 19,0x, acercado 25% al justificado (16,0x); rango de anclas 16,0x–19,7x. Atípicos excluidos de la historia: Dec '22 (13,0x: > 2,5x la mediana (1.5x)); Dec '23 (18,3x: > 2,5x la mediana (1.5x)); Dec '24 (18,2x: > 2,5x la mediana (1.5x)); Dec '25 (25,5x: > 2,5x la mediana (1.5x)); LTM (24,0x: > 2,5x la mediana (1.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 34,7x: promedio de historia y peers 35,6x, acercado 25% al justificado (32,0x); rango de anclas 31,2x–40,0x. Atípicos excluidos de la historia: Dec '22 (19,1x: > 2,5x la mediana (1.5x)); Dec '23 (25,3x: > 2,5x la mediana (1.5x)); Dec '24 (32,0x: > 2,5x la mediana (1.5x)); Dec '25 (52,2x: > 2,5x la mediana (1.5x)); LTM (76,0x: > 2,5x la mediana (1.5x)). EV/FCFF: la razón FCF después de intereses ÷ FCFF se fija en 1,09 (mediana de los tres cierres reales); el último cierre da 2,70 porque 'Interest / Other' incluye ganancias en inversiones, no intereses. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 24,8x: promedio de historia y peers 25,9x, acercado 25% al justificado (21,4x); rango de anclas 21,4x–27,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 32,7x: promedio de historia y peers 34,6x, acercado 25% al justificado (26,9x); rango de anclas 26,9x–40,5x. Atípicos excluidos de la historia: Dec '22 (19,0x: > 2,5x la mediana (1.6x)); Dec '23 (25,3x: > 2,5x la mediana (1.6x)); Dec '24 (32,0x: > 2,5x la mediana (1.6x)); Dec '25 (51,8x: > 2,5x la mediana (1.6x)); LTM (78,3x: > 2,5x la mediana (1.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 19,0x: promedio de historia y peers 19,6x, acercado 25% al justificado (17,2x); rango de anclas 17,2x–20,7x. Atípicos excluidos de la historia: Dec '22 (12,5x: > 2,5x la mediana (1.0x)); Dec '23 (17,3x: > 2,5x la mediana (1.0x)); Dec '24 (18,6x: > 2,5x la mediana (1.0x)); Dec '25 (23,0x: > 2,5x la mediana (1.0x)); LTM (22,5x: > 2,5x la mediana (1.0x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$284,73 frente a US$330,86 del DCF (−14%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$284,73 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,30%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$128,74) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$330,86 por acción.** Complemento: DCF esperado por probabilidades US$278,78. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$330,86 | US$159,28 | US$436,51 |
| EV/EBITDA | 18,3× / 16,5× / 20,6× | 20% | 33% | US$289,09 | US$232,85 | US$358,93 |
| EV/FCFF | 34,7× / 27,4× / 46,0× | 10% | 17% | US$256,25 | US$221,42 | US$244,22 |
| P/E | 24,8× / 20,5× / 28,7× | 20% | 33% | US$292,78 | US$211,95 | US$378,79 |
| P/FCFE | 32,7× / 26,0× / 42,2× | 5% | 8% | US$304,09 | US$242,21 | US$333,44 |
| P/OCF | 19,0× / 16,0× / 23,0× | 5% | 8% | US$272,75 | US$228,23 | US$300,46 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$284,73 | US$224,37 | US$339,43 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$303,19 | US$198,34 | US$378,27 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$443,94 | US$213,71 | US$585,70 |
| EV/EBITDA (total con dividendos) | 18,3× / 16,5× / 20,6× | 20% | 33% | US$395,90 | US$295,64 | US$520,73 |
| EV/FCFF (total con dividendos) | 34,7× / 27,4× / 46,0× | 10% | 17% | US$378,22 | US$287,68 | US$415,97 |
| P/E (total con dividendos) | 24,8× / 20,5× / 28,7× | 20% | 33% | US$402,72 | US$268,20 | US$553,99 |
| P/FCFE (total con dividendos) | 32,7× / 26,0× / 42,2× | 5% | 8% | US$426,10 | US$301,07 | US$518,20 |
| P/OCF (total con dividendos) | 19,0× / 16,0× / 23,0× | 5% | 8% | US$388,74 | US$296,15 | US$463,48 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$397,14 | US$285,66 | US$509,37 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$2,49 | US$2,49 | US$2,49 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$394,65 | US$283,17 | US$506,88 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$415,86 | US$256,88 | US$539,91 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,30%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$280,41 | US$291,60 | US$295,25 | US$289,09 | OK |
| EV/EBITDA | Conservador | US$245,05 | US$232,96 | US$220,53 | US$232,85 | OK |
| EV/EBITDA | Optimista | US$325,43 | US$363,06 | US$388,28 | US$358,93 | OK |
| EV/FCFF | Base | US$225,79 | US$260,88 | US$282,08 | US$256,25 | OK |
| EV/FCFF | Conservador | US$225,19 | US$224,46 | US$214,60 | US$221,42 | OK |
| EV/FCFF | Optimista | US$170,02 | US$252,42 | US$310,21 | US$244,22 | OK |
| P/E | Base | US$282,60 | US$295,40 | US$300,34 | US$292,78 | OK |
| P/E | Conservador | US$224,02 | US$211,76 | US$200,08 | US$211,95 | OK |
| P/E | Optimista | US$339,80 | US$383,50 | US$413,08 | US$378,79 | OK |
| P/FCFE | Base | US$294,11 | US$300,41 | US$317,76 | US$304,09 | OK |
| P/FCFE | Conservador | US$264,53 | US$237,53 | US$224,58 | US$242,21 | OK |
| P/FCFE | Optimista | US$282,28 | US$331,65 | US$386,40 | US$333,44 | OK |
| P/OCF | Base | US$252,09 | US$276,23 | US$289,92 | US$272,75 | OK |
| P/OCF | Conservador | US$233,30 | US$230,48 | US$220,92 | US$228,23 | OK |
| P/OCF | Optimista | US$249,99 | US$305,77 | US$345,62 | US$300,46 | OK |

Múltiplos consolidados hoy: US$284,73 / US$224,37 / US$339,43 · DCF de las historias hoy: US$330,86 / US$159,28 / US$436,51 · Ponderado hoy: US$303,19 / US$198,34 / US$378,27 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para GOOG la diferencia es de −14% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$311,55 por acción y los múltiplos, US$244,87 hoy: 21% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$343,88 supone que los ingresos crecen 14,3% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,7% (+2,6 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$443,94 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,3%, WACC de los años 4-10 9,7%, ROE de FY+3 30,8% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 18,3x | 20,5x | −11% | 6,7% | 7,0% | −0,3 pp | Coherente con el DCF. |
| EV/FCFF | 34,7x | 40,8x | −15% | 6,6% | 7,0% | −0,4 pp | Coherente con el DCF. |
| P/E | 24,8x | 27,3x | −9% | 7,0% | 7,3% | −0,3 pp | Coherente con el DCF. |
| P/FCFE | 32,7x | 34,0x | −4% | 7,0% | 7,1% | −0,1 pp | Coherente con el DCF. |
| P/OCF | 19,0x | 21,7x | −12% | 6,7% | 7,1% | −0,4 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$303,19 | — |
| Múltiplos Base +20% | US$336,22 | +10,9% |
| Múltiplos Base −20% | US$270,15 | −10,9% |
| Crecimiento años 2-5 +2 pp | US$314,75 | +3,8% |
| Crecimiento años 2-5 −2 pp | US$292,61 | −3,5% |
| Margen objetivo +3 pp | US$314,45 | +3,7% |
| Margen objetivo −3 pp | US$291,92 | −3,7% |
| WACC +1 pp | US$295,94 | −2,4% |
| WACC −1 pp | US$310,96 | +2,6% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 16,52 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 12,98 | 18,26 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 20,63 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 27,35 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 15,44 | 34,72 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 45,98 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 20,53 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 19,01 | 24,78 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 28,74 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 26,01 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 16,02 | 32,67 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 42,24 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 16,04 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 11,09 | 19,00 | Múltiplo base elegido con el protocolo v3 |
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
