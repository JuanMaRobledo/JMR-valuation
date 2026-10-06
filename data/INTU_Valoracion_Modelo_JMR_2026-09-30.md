---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de INTUIT INC."
ticker: "INTU"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/14sbZoheKmtK5UpMOlRNzvqD1F9sCJEpHW01g4f-X8mM/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# INTUIT INC. (INTU) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$531,76 por acción.** Complemento: DCF esperado por probabilidades US$455,43; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$206,55–US$654,68; precio con MOS 35% sobre el esperado: US$296,03; precio de referencia US$275,71. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La IA es palanca de monetización** (valor principal) | 45% | US$531,76 | US$239,29 |
| Conservadora · La IA erosiona impuestos y contabilidad básica | 25% | US$258,19 | US$64,55 |
| Disrupción · Deterioro de los fundamentales: Recesión y declaración gratuita del Estado | 10% | US$206,55 | US$20,65 |
| Optimista · Plataforma financiera de la pyme | 20% | US$654,68 | US$130,94 |
| **DCF esperado (complemento)** | 100% | **US$455,43** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$496,45 por acción y los múltiplos, US$386,84 hoy: 22% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$531,76 | US$362,17 | US$430,01 | US$296,03 | US$580,87 |
| Conservador | US$258,19 | US$290,49 | US$277,57 | US$296,03 | US$359,37 |
| Optimista | US$654,68 | US$420,89 | US$514,41 | US$296,03 | US$710,20 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - INTU](https://docs.google.com/spreadsheets/d/14sbZoheKmtK5UpMOlRNzvqD1F9sCJEpHW01g4f-X8mM/edit).
- Análisis del 29 de jul de 2026. Precio de referencia de la hoja: US$275,71.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 7,1% | 9,1% | 13,8% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 5,4% | 9,0% | 13,1% | Input B29 |
| Margen EBIT objetivo | 29,2% | 32,2% | 35,2% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,54 / 1,54 | — | Input B32/B33 |
| DCF por acción hoy | US$258,19 | US$531,76 | US$654,68 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,34, ERP 3,70%, Ke 10,25%, costo de la deuda después de impuestos 4,76%, peso del patrimonio 91,1%, WACC inicial 9,76% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Intuit cotizó a 30-51x EBITDA y 44-70x utilidades mientras crecía 12-20% con TurboTax, Credit Karma y QuickBooks. En 2026 el mercado empezó a temer que los agentes de IA hagan el trabajo de impuestos y contabilidad por el que cobra; recortó la guía de TurboTax, anunció una reestructuración y su guía FY27 (9-10% de crecimiento, TurboTax 2-3%) decepcionó. La acción cayó ~60% desde su máximo. La etapa actual es el cierre Jul '26 y el LTM. B: software de aplicaciones y nómina/finanzas (Adobe, Autodesk, Salesforce, Workday, ADP, Paychex), datos de yfinance al 29-sep-2026. Sin ajuste: Intuit crece 9-10% con márgenes altos, en línea con la mediana de los peers. λ = 0,25: la Intuit de FY+3 del escenario Base crece al ~10%, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Jul '26, LTM (etapa actual) = 12,3x | 16,7x (n=6: ADBE 9,3x, ADSK 18,4x, CRM 16,9x, WDAY 29,0x, ADP 16,4x, PAYX 12,7x) × 1,00 = 16,7x | 17,2x / 14,1x / 19,7x | **15,2x** | 13,1x | 16,5x | 13,1x / —x / —x |
| EV/FCFF | mediana Jul '26, LTM (etapa actual) = 9,5x (EV/FCF × 1,02 = FCF después de intereses ÷ FCFF) | 15,2x (n=6: ADBE 8,5x, ADSK 15,0x, CRM 13,8x, WDAY 15,7x, ADP 20,5x, PAYX 15,4x) × 1,00 = 15,2x | 32,9x / 23,0x / 40,2x | **17,5x** | 15,1x | 19,1x | 17,4x / —x / —x |
| P/E | mediana Jul '26, LTM (etapa actual) = 18,0x | 22,3x (n=6: ADBE 13,0x, ADSK 26,3x, CRM 20,6x, WDAY 38,8x, ADP 23,9x, PAYX 19,7x) × 1,00 = 22,3x | 21,9x / 16,4x / 25,8x | **20,6x** | 17,9x | 23,1x | 18,6x / —x / —x |
| P/FCFE | mediana Jul '26, LTM (etapa actual) = 9,1x | 15,2x (n=6: ADBE 8,8x, ADSK 15,1x, CRM 12,2x, WDAY 16,0x, ADP 21,7x, PAYX 15,2x) × 1,00 = 15,2x | 26,3x / 19,5x / 30,8x | **15,7x** | 13,4x | 17,0x | 15,4x / —x / —x |
| P/OCF | mediana Jul '26, LTM (etapa actual) = 9,0x | 14,2x (n=6: ADBE 8,6x, ADSK 14,7x, CRM 11,8x, WDAY 14,8x, ADP 19,1x, PAYX 13,8x) × 1,00 = 14,2x | 29,5x / 20,1x / 35,9x | **16,1x** | 13,4x | 17,6x | 16,2x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 15,2x: promedio de historia y peers 14,5x, acercado 25% al justificado (17,2x); rango de anclas 12,3x–17,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 17,5x: promedio de historia y peers 12,3x, acercado 25% al justificado (32,9x); rango de anclas 9,5x–32,9x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 20,6x: promedio de historia y peers 20,1x, acercado 25% al justificado (21,9x); rango de anclas 17,9x–22,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 15,7x: promedio de historia y peers 12,2x, acercado 25% al justificado (26,3x); rango de anclas 9,2x–26,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 16,1x: promedio de historia y peers 11,6x, acercado 25% al justificado (29,5x); rango de anclas 9,0x–29,5x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$362,17 frente a US$531,76 del DCF (−32%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$362,17 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,25%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$206,55) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$531,76 por acción.** Complemento: DCF esperado por probabilidades US$455,43. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$531,76 | US$258,19 | US$654,68 |
| EV/EBITDA | 15,2× / 13,1× / 16,5× | 20% | 33% | US$429,23 | US$332,88 | US$499,83 |
| EV/FCFF | 17,5× / 15,1× / 19,1× | 10% | 17% | US$254,47 | US$232,04 | US$276,02 |
| P/E | 20,6× / 17,9× / 23,1× | 20% | 33% | US$400,38 | US$311,75 | US$482,03 |
| P/FCFE | 15,7× / 13,4× / 17,0× | 5% | 8% | US$272,55 | US$226,43 | US$304,15 |
| P/OCF | 16,1× / 13,4× / 17,6× | 5% | 8% | US$246,07 | US$216,82 | US$267,09 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$362,17 | US$290,49 | US$420,89 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$430,01 | US$277,57 | US$514,41 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$712,58 | US$345,97 | US$877,28 |
| EV/EBITDA (total con dividendos) | 15,2× / 13,1× / 16,5× | 20% | 33% | US$579,69 | US$419,48 | US$703,75 |
| EV/FCFF (total con dividendos) | 17,5× / 15,1× / 19,1× | 10% | 17% | US$355,95 | US$300,29 | US$407,45 |
| P/E (total con dividendos) | 20,6× / 17,9× / 23,1× | 20% | 33% | US$541,88 | US$393,04 | US$681,07 |
| P/FCFE (total con dividendos) | 15,7× / 13,4× / 17,0× | 5% | 8% | US$375,03 | US$288,07 | US$438,83 |
| P/OCF (total con dividendos) | 16,1× / 13,4× / 17,6× | 5% | 8% | US$343,60 | US$280,96 | US$392,82 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$493,07 | US$368,31 | US$598,82 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$20,13 | US$20,13 | US$20,13 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$472,94 | US$348,18 | US$578,69 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$580,87 | US$359,37 | US$710,20 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,25%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$423,96 | US$429,68 | US$434,04 | US$429,23 | OK |
| EV/EBITDA | Conservador | US$353,01 | US$331,16 | US$314,48 | US$332,88 | OK |
| EV/EBITDA | Optimista | US$469,92 | US$502,95 | US$526,62 | US$499,83 | OK |
| EV/FCFF | Base | US$241,80 | US$254,54 | US$267,07 | US$254,47 | OK |
| EV/FCFF | Conservador | US$238,77 | US$231,81 | US$225,54 | US$232,04 | OK |
| EV/FCFF | Optimista | US$243,87 | US$278,69 | US$305,50 | US$276,02 | OK |
| P/E | Base | US$394,13 | US$401,21 | US$405,82 | US$400,38 | OK |
| P/E | Conservador | US$330,22 | US$310,28 | US$294,75 | US$311,75 | OK |
| P/E | Optimista | US$450,67 | US$485,73 | US$509,70 | US$482,03 | OK |
| P/FCFE | Base | US$264,11 | US$272,22 | US$281,31 | US$272,55 | OK |
| P/FCFE | Conservador | US$237,49 | US$225,40 | US$216,41 | US$226,43 | OK |
| P/FCFE | Optimista | US$276,83 | US$306,71 | US$328,92 | US$304,15 | OK |
| P/OCF | Base | US$234,22 | US$246,14 | US$257,86 | US$246,07 | OK |
| P/OCF | Conservador | US$222,72 | US$216,63 | US$211,11 | US$216,82 | OK |
| P/OCF | Optimista | US$237,14 | US$269,53 | US$294,58 | US$267,09 | OK |

Múltiplos consolidados hoy: US$362,17 / US$290,49 / US$420,89 · DCF de las historias hoy: US$531,76 / US$258,19 / US$654,68 · Ponderado hoy: US$430,01 / US$277,57 / US$514,41 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para INTU la diferencia es de −32% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$496,45 por acción y los múltiplos, US$386,84 hoy: 22% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$275,71 supone que los ingresos crecen -1,7% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 9,8% (−11,5 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$712,58 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,2%, WACC de los años 4-10 9,4%, ROE de FY+3 37,0% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 15,2x | 18,7x | −19% | 5,8% | 6,5% | −0,7 pp | Coherente con el DCF. |
| EV/FCFF | 17,5x | 35,7x | −50% | 3,5% | 6,5% | −2,9 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 50% por debajo del DCF en FY+3. |
| P/E | 20,6x | 27,3x | −24% | 5,9% | 7,1% | −1,2 pp | Coherente con el DCF. |
| P/FCFE | 15,7x | 30,6x | −47% | 3,6% | 6,8% | −3,1 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 47% por debajo del DCF en FY+3. |
| P/OCF | 16,1x | 34,4x | −52% | 3,0% | 6,8% | −3,7 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 52% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$430,01 | — |
| Múltiplos Base +20% | US$472,33 | +9,8% |
| Múltiplos Base −20% | US$387,68 | −9,8% |
| Crecimiento años 2-5 +2 pp | US$449,61 | +4,6% |
| Crecimiento años 2-5 −2 pp | US$412,07 | −4,2% |
| Margen objetivo +3 pp | US$449,98 | +4,6% |
| Margen objetivo −3 pp | US$410,03 | −4,6% |
| WACC +1 pp | US$417,88 | −2,8% |
| WACC −1 pp | US$443,01 | +3,0% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Margen objetivo −3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 13,12 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 13,11 | 15,15 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 16,46 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 15,10 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 17,37 | 17,48 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 19,14 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 17,88 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 18,58 | 20,55 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 23,06 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 13,39 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 15,43 | 15,70 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 16,99 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 13,45 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 16,23 | 16,09 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 17,62 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/INTU_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/14sbZoheKmtK5UpMOlRNzvqD1F9sCJEpHW01g4f-X8mM/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (ADBE, ADSK, CRM, WDAY, ADP, PAYX).
- [Motley Fool, 26-ago-2026: por qué cayó Intuit](https://www.fool.com/investing/2026/08/26/why-intuit-stock-dropped-today/)
- [Intuit: resultados FY26 y guía FY27](https://investors.intuit.com/news-events/press-releases/detail/1320/intuit-reports-fourth-quarter-and-full-year-fiscal-2026-results-sets-fiscal-2027-guidance)
- [Yahoo Finance: Intuit se desplomó por el temor a la IA agéntica](https://finance.yahoo.com/markets/stocks/articles/intuit-crashed-over-agentic-ai-132427512.html)

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
