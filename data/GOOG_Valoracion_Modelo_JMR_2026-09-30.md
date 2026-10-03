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

**Valor intrínseco principal · DCF Base hoy: US$322,64 por acción.** Complemento: DCF esperado por probabilidades US$274,33; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$131,64–US$424,63; precio con MOS 35% sobre el esperado: US$178,32; precio de referencia US$340,35. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Search resiste y Cloud es el segundo motor** (valor principal) | 40% | US$322,64 | US$129,06 |
| Conservadora · La IA conversacional erosiona Search | 25% | US$162,42 | US$40,60 |
| Disrupción · Deterioro de los fundamentales: Remedios antimonopolio y guerra de precios en IA | 15% | US$131,64 | US$19,75 |
| Optimista · Gemini y Cloud dominan la plataforma de IA | 20% | US$424,63 | US$84,93 |
| **DCF esperado (complemento)** | 100% | **US$274,33** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$311,55 por acción y los múltiplos, US$244,87 hoy: 21% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$322,64 | US$291,17 | US$303,76 | US$178,32 | US$411,94 |
| Conservador | US$162,42 | US$228,35 | US$201,98 | US$178,32 | US$258,69 |
| Optimista | US$424,63 | US$347,91 | US$378,60 | US$178,32 | US$534,71 |

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
| DCF por acción hoy | US$162,42 | US$322,64 | US$424,63 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,07, ERP 4,46%, Ke 9,76%, costo de la deuda después de impuestos 4,65%, peso del patrimonio 97,8%, WACC inicial 9,65% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: los cierres 2016-2021 de la hoja dan múltiplos de ~1x porque el precio no está ajustado por el split 20:1 de julio de 2022; no son representativos y se usa la historia desde Dec '22. En P/E se quita el LTM: la utilidad del primer semestre de 2026 incluye US$135,9 mil millones de ganancias en acciones de otras empresas, que bajan el P/E a 17x. En EV/FCFF y P/FCFE se quita el LTM: el capex de 2026 (US$195-205 mil millones) deja el flujo de caja en mínimos y el múltiplo en ~78x, un pico transitorio frente al flujo de FY+3. B: grandes plataformas tecnológicas (Meta, Microsoft, Amazon, Apple, Netflix), datos de yfinance al 29-sep-2026. Amazon no tiene flujo de caja libre positivo y no entra en los múltiplos de flujo. Sin ajuste: Alphabet crece 24% con margen operativo de 34%, en línea con Meta y Microsoft. λ = 0,25: la Alphabet de FY+3 del escenario Base sigue siendo una plataforma de crecimiento alto con fuerte inversión en IA, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,3x | 19,7x (n=5: META 17,4x, MSFT 19,7x, AMZN 16,5x, AAPL 28,8x, NFLX 20,1x) × 1,00 = 19,7x | 16,4x / 13,6x / 17,6x | **18,4x** | 16,6x | 21,1x | 13,0x / —x / —x |
| EV/FCFF | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 31,2x (EV/FCF × 1,09 = FCF después de intereses ÷ FCFF) | 40,0x (n=4: META 44,7x, MSFT 55,2x, AAPL 35,3x, NFLX 25,0x) × 1,00 = 40,0x | 32,8x / 23,3x / 49,7x | **34,9x** | 27,4x | 46,5x | 15,4x / —x / —x |
| P/E | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 24,0x | 27,8x (n=5: META 27,8x, MSFT 28,4x, AMZN 19,8x, AAPL 37,7x, NFLX 22,1x) × 1,00 = 27,8x | 23,4x / 17,2x / 33,8x | **25,3x** | 20,8x | 29,0x | 19,0x / —x / —x |
| P/FCFE | mediana Dec '22, Dec '23, Dec '24, Dec '25 (etapa actual) = 28,6x | 40,5x (n=4: META 45,9x, MSFT 56,4x, AAPL 35,2x, NFLX 26,2x) × 1,00 = 40,5x | 29,2x / 21,4x / 42,1x | **33,2x** | 26,3x | 43,5x | 16,0x / —x / —x |
| P/OCF | mediana Dec '22, Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,6x | 20,7x (n=5: META 14,4x, MSFT 20,7x, AMZN 17,9x, AAPL 32,8x, NFLX 24,5x) × 1,00 = 20,7x | 18,6x / 13,4x / 25,7x | **19,4x** | 16,2x | 23,0x | 11,1x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 18,4x: promedio de historia y peers 19,0x, acercado 25% al justificado (16,4x); rango de anclas 16,4x–19,7x. Atípicos excluidos de la historia: Dec '22 (13,0x: > 2,5x la mediana (1.5x)); Dec '23 (18,3x: > 2,5x la mediana (1.5x)); Dec '24 (18,2x: > 2,5x la mediana (1.5x)); Dec '25 (25,5x: > 2,5x la mediana (1.5x)); LTM (24,8x: > 2,5x la mediana (1.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 34,9x: promedio de historia y peers 35,6x, acercado 25% al justificado (32,8x); rango de anclas 31,2x–40,0x. Atípicos excluidos de la historia: Dec '22 (19,1x: > 2,5x la mediana (1.5x)); Dec '23 (25,3x: > 2,5x la mediana (1.5x)); Dec '24 (32,0x: > 2,5x la mediana (1.5x)); Dec '25 (52,2x: > 2,5x la mediana (1.5x)); LTM (78,4x: > 2,5x la mediana (1.5x)). EV/FCFF: la razón FCF después de intereses ÷ FCFF se fija en 1,09 (mediana de los tres cierres reales); el último cierre da 2,70 porque 'Interest / Other' incluye ganancias en inversiones, no intereses. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 25,3x: promedio de historia y peers 25,9x, acercado 25% al justificado (23,4x); rango de anclas 23,4x–27,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 33,2x: promedio de historia y peers 34,6x, acercado 25% al justificado (29,2x); rango de anclas 28,6x–40,5x. Atípicos excluidos de la historia: Dec '22 (19,0x: > 2,5x la mediana (1.6x)); Dec '23 (25,3x: > 2,5x la mediana (1.6x)); Dec '24 (32,0x: > 2,5x la mediana (1.6x)); Dec '25 (51,8x: > 2,5x la mediana (1.6x)); LTM (78,3x: > 2,5x la mediana (1.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 19,4x: promedio de historia y peers 19,6x, acercado 25% al justificado (18,6x); rango de anclas 18,6x–20,7x. Atípicos excluidos de la historia: Dec '22 (12,5x: > 2,5x la mediana (1.0x)); Dec '23 (17,3x: > 2,5x la mediana (1.0x)); Dec '24 (18,6x: > 2,5x la mediana (1.0x)); Dec '25 (23,0x: > 2,5x la mediana (1.0x)); LTM (22,5x: > 2,5x la mediana (1.0x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$291,17 frente a US$322,64 del DCF (−10%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$291,17 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,76%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$131,64) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$322,64 por acción.** Complemento: DCF esperado por probabilidades US$274,33. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$322,64 | US$162,42 | US$424,63 |
| EV/EBITDA | 18,4× / 16,6× / 21,1× | 20% | 33% | US$293,42 | US$235,72 | US$370,04 |
| EV/FCFF | 34,9× / 27,4× / 46,5× | 10% | 17% | US$260,14 | US$224,22 | US$249,20 |
| P/E | 25,3× / 20,8× / 29,0× | 20% | 33% | US$301,72 | US$217,08 | US$386,45 |
| P/FCFE | 33,2× / 26,3× / 43,5× | 5% | 8% | US$312,43 | US$247,12 | US$347,03 |
| P/OCF | 19,4× / 16,2× / 23,0× | 5% | 8% | US$280,80 | US$233,43 | US$303,54 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$291,17 | US$228,35 | US$347,91 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$303,76 | US$201,98 | US$378,60 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$426,65 | US$214,78 | US$561,53 |
| EV/EBITDA (total con dividendos) | 18,4× / 16,6× / 21,1× | 20% | 33% | US$397,93 | US$296,45 | US$531,59 |
| EV/FCFF (total con dividendos) | 34,9× / 27,4× / 46,5× | 10% | 17% | US$380,15 | US$288,54 | US$420,07 |
| P/E (total con dividendos) | 25,3× / 20,8× / 29,0× | 20% | 33% | US$410,96 | US$272,08 | US$559,56 |
| P/FCFE (total con dividendos) | 33,2× / 26,3× / 43,5× | 5% | 8% | US$433,49 | US$304,28 | US$533,82 |
| P/OCF (total con dividendos) | 19,4× / 16,2× / 23,0× | 5% | 8% | US$396,27 | US$300,00 | US$463,48 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$402,13 | US$287,96 | US$516,84 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$2,49 | US$2,49 | US$2,49 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$399,64 | US$285,47 | US$514,34 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$411,94 | US$258,69 | US$534,71 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,76%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$283,20 | US$295,94 | US$301,11 | US$293,42 | OK |
| EV/EBITDA | Conservador | US$246,91 | US$235,88 | US$224,37 | US$235,72 | OK |
| EV/EBITDA | Optimista | US$333,73 | US$374,19 | US$402,18 | US$370,04 | OK |
| EV/FCFF | Base | US$228,02 | US$264,75 | US$287,66 | US$260,14 | OK |
| EV/FCFF | Conservador | US$226,96 | US$227,32 | US$218,39 | US$224,22 | OK |
| EV/FCFF | Optimista | US$172,43 | US$257,34 | US$317,85 | US$249,20 | OK |
| P/E | Base | US$289,80 | US$304,39 | US$310,96 | US$301,72 | OK |
| P/E | Conservador | US$228,39 | US$216,92 | US$205,94 | US$217,08 | OK |
| P/E | Optimista | US$344,89 | US$391,12 | US$423,33 | US$386,45 | OK |
| P/FCFE | Base | US$300,68 | US$308,60 | US$328,00 | US$312,43 | OK |
| P/FCFE | Conservador | US$268,67 | US$242,41 | US$230,29 | US$247,12 | OK |
| P/FCFE | Optimista | US$292,23 | US$344,99 | US$403,87 | US$347,03 | OK |
| P/OCF | Base | US$258,24 | US$284,32 | US$299,85 | US$280,80 | OK |
| P/OCF | Conservador | US$237,50 | US$235,75 | US$227,05 | US$233,43 | OK |
| P/OCF | Optimista | US$251,21 | US$308,74 | US$350,68 | US$303,54 | OK |

Múltiplos consolidados hoy: US$291,17 / US$228,35 / US$347,91 · DCF de las historias hoy: US$322,64 / US$162,42 / US$424,63 · Ponderado hoy: US$303,76 / US$201,98 / US$378,60 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para GOOG la diferencia es de −10% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$311,55 por acción y los múltiplos, US$244,87 hoy: 21% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$340,35 supone que los ingresos crecen 14,6% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,7% (+2,9 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$426,65 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,8%, WACC de los años 4-10 9,4%, ROE de FY+3 30,8% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 18,4x | 19,6x | −7% | 6,5% | 6,6% | −0,2 pp | Coherente con el DCF. |
| EV/FCFF | 34,9x | 39,2x | −11% | 6,3% | 6,6% | −0,3 pp | Coherente con el DCF. |
| P/E | 25,3x | 26,3x | −4% | 6,4% | 6,6% | −0,1 pp | Coherente con el DCF. |
| P/FCFE | 33,2x | 32,7x | +2% | 6,6% | 6,5% | +0,1 pp | Coherente con el DCF. |
| P/OCF | 19,4x | 20,9x | −7% | 6,3% | 6,5% | −0,2 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$303,76 | — |
| Múltiplos Base +20% | US$337,56 | +11,1% |
| Múltiplos Base −20% | US$269,96 | −11,1% |
| Crecimiento años 2-5 +2 pp | US$314,91 | +3,7% |
| Crecimiento años 2-5 −2 pp | US$293,55 | −3,4% |
| Margen objetivo +3 pp | US$314,74 | +3,6% |
| Margen objetivo −3 pp | US$292,78 | −3,6% |
| WACC +1 pp | US$296,69 | −2,3% |
| WACC −1 pp | US$311,34 | +2,5% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 16,57 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 12,98 | 18,36 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 21,08 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 27,44 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 15,44 | 34,91 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 46,46 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 20,83 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 19,01 | 25,29 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 29,03 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 26,29 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 16,02 | 33,24 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 43,52 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 16,25 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 11,09 | 19,37 | Múltiplo base elegido con el protocolo v3 |
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
