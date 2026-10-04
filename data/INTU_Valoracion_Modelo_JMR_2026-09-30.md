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

**Valor intrínseco principal · DCF Base hoy: US$488,09 por acción.** Complemento: DCF esperado por probabilidades US$421,97; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$199,15–US$600,33; precio con MOS 35% sobre el esperado: US$274,28; precio de referencia US$281,08. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La IA es palanca de monetización** (valor principal) | 45% | US$488,09 | US$219,64 |
| Conservadora · La IA erosiona impuestos y contabilidad básica | 25% | US$249,38 | US$62,34 |
| Disrupción · Deterioro de los fundamentales: Recesión y declaración gratuita del Estado | 10% | US$199,15 | US$19,92 |
| Optimista · Plataforma financiera de la pyme | 20% | US$600,33 | US$120,07 |
| **DCF esperado (complemento)** | 100% | **US$421,97** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$496,45 por acción y los múltiplos, US$386,84 hoy: 22% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$488,09 | US$320,13 | US$420,91 | US$274,28 | US$574,60 |
| Conservador | US$249,38 | US$259,80 | US$253,55 | US$274,28 | US$336,75 |
| Optimista | US$600,33 | US$366,30 | US$506,72 | US$274,28 | US$700,82 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - INTU](https://docs.google.com/spreadsheets/d/14sbZoheKmtK5UpMOlRNzvqD1F9sCJEpHW01g4f-X8mM/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$281,08.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 7,1% | 9,1% | 13,8% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 5,4% | 9,0% | 13,1% | Input B29 |
| Margen EBIT objetivo | 29,2% | 32,2% | 35,2% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,31 / 1,88 | — | Input B32/B33 |
| DCF por acción hoy | US$249,38 | US$488,09 | US$600,33 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,34, ERP 4,09%, Ke 10,77%, costo de la deuda después de impuestos 4,76%, peso del patrimonio 91,3%, WACC inicial 10,25% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Intuit cotizó a 30-51x EBITDA y 44-70x utilidades mientras crecía 12-20% con TurboTax, Credit Karma y QuickBooks. En 2026 el mercado empezó a temer que los agentes de IA hagan el trabajo de impuestos y contabilidad por el que cobra; recortó la guía de TurboTax, anunció una reestructuración y su guía FY27 (9-10% de crecimiento, TurboTax 2-3%) decepcionó. La acción cayó ~60% desde su máximo. La etapa actual es el cierre Jul '26 y el LTM. B: software de aplicaciones y nómina/finanzas (Adobe, Autodesk, Salesforce, Workday, ADP, Paychex), datos de yfinance al 29-sep-2026. Sin ajuste: Intuit crece 9-10% con márgenes altos, en línea con la mediana de los peers. λ = 0,25: la Intuit de FY+3 del escenario Base crece al ~10%, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Jul '26, LTM (etapa actual) = 12,3x | 16,7x (n=6: ADBE 9,3x, ADSK 18,4x, CRM 16,9x, WDAY 29,0x, ADP 16,4x, PAYX 12,7x) × 1,00 = 16,7x | 16,7x / 13,3x / 19,2x | **15,0x** | 12,9x | 16,3x | 13,1x / —x / —x |
| EV/FCFF | mediana Jul '26, LTM (etapa actual) = 9,5x (EV/FCF × 1,02 = FCF después de intereses ÷ FCFF) | 15,2x (n=6: ADBE 8,5x, ADSK 15,0x, CRM 13,8x, WDAY 15,7x, ADP 20,5x, PAYX 15,4x) × 1,00 = 15,2x | 28,9x / 20,9x / 34,5x | **16,5x** | 14,4x | 17,9x | 17,4x / —x / —x |
| P/E | mediana Jul '26, LTM (etapa actual) = 18,0x | 22,3x (n=6: ADBE 13,0x, ADSK 26,3x, CRM 20,6x, WDAY 38,8x, ADP 23,9x, PAYX 19,7x) × 1,00 = 22,3x | 19,4x / 14,9x / 22,4x | **19,9x** | 17,5x | 22,2x | 18,6x / —x / —x |
| P/FCFE | mediana Jul '26, LTM (etapa actual) = 9,1x | 15,2x (n=6: ADBE 8,8x, ADSK 15,1x, CRM 12,2x, WDAY 16,0x, ADP 21,7x, PAYX 15,2x) × 1,00 = 15,2x | 23,3x / 17,8x / 26,7x | **14,9x** | 12,9x | 16,1x | 15,4x / —x / —x |
| P/OCF | mediana Jul '26, LTM (etapa actual) = 9,0x | 14,2x (n=6: ADBE 8,6x, ADSK 14,7x, CRM 11,8x, WDAY 14,8x, ADP 19,1x, PAYX 13,8x) × 1,00 = 14,2x | 25,9x / 18,3x / 30,6x | **15,2x** | 12,8x | 16,5x | 16,2x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 15,0x: promedio de historia y peers 14,5x, acercado 25% al justificado (16,7x); rango de anclas 12,3x–16,7x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 16,5x: promedio de historia y peers 12,3x, acercado 25% al justificado (28,9x); rango de anclas 9,5x–28,9x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 19,9x: promedio de historia y peers 20,1x, acercado 25% al justificado (19,4x); rango de anclas 17,9x–22,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 14,9x: promedio de historia y peers 12,2x, acercado 25% al justificado (23,3x); rango de anclas 9,2x–23,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 15,2x: promedio de historia y peers 11,6x, acercado 25% al justificado (25,9x); rango de anclas 9,0x–25,9x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$320,13 frente a US$488,09 del DCF (−34%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$320,13 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Software»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,77%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$199,15) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$488,09 por acción.** Complemento: DCF esperado por probabilidades US$421,97. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$488,09 | US$249,38 | US$600,33 |
| EV/EBITDA | 15,0× / 12,9× / 16,3× | 10% | 25% | US$421,63 | US$324,69 | US$491,52 |
| EV/FCFF | 16,5× / 14,4× / 17,9× | 15% | 37% | US$265,13 | US$229,28 | US$294,38 |
| P/E | 19,9× / 17,5× / 22,2× | 5% | 12% | US$384,99 | US$302,24 | US$460,44 |
| P/FCFE | 14,9× / 12,9× / 16,1× | 5% | 12% | US$281,94 | US$224,81 | US$320,25 |
| P/OCF | 15,2× / 12,8× / 16,5× | 5% | 12% | US$255,47 | US$214,14 | US$283,55 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$320,13 | US$259,80 | US$366,30 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$420,91 | US$253,55 | US$506,72 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$663,40 | US$338,94 | US$815,95 |
| EV/EBITDA (total con dividendos) | 15,0× / 12,9× / 16,3× | 10% | 25% | US$574,86 | US$413,03 | US$698,74 |
| EV/FCFF (total con dividendos) | 16,5× / 14,4× / 17,9× | 15% | 37% | US$370,21 | US$297,32 | US$431,61 |
| P/E (total con dividendos) | 19,9× / 17,5× / 22,2× | 5% | 12% | US$526,13 | US$384,70 | US$657,00 |
| P/FCFE (total con dividendos) | 14,9× / 12,9× / 16,1× | 5% | 12% | US$388,36 | US$286,90 | US$461,20 |
| P/OCF (total con dividendos) | 15,2× / 12,8× / 16,5× | 5% | 12% | US$356,31 | US$278,15 | US$414,65 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 40% | 100% | US$441,39 | US$333,47 | US$528,14 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$20,13 | US$20,13 | US$20,13 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$421,26 | US$313,34 | US$508,01 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$574,60 | US$336,75 | US$700,82 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,77%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$418,36 | US$422,07 | US$424,45 | US$421,63 | OK |
| EV/EBITDA | Conservador | US$345,76 | US$322,94 | US$305,38 | US$324,69 | OK |
| EV/EBITDA | Optimista | US$464,31 | US$494,67 | US$515,59 | US$491,52 | OK |
| EV/FCFF | Base | US$256,11 | US$265,41 | US$273,87 | US$265,13 | OK |
| EV/FCFF | Conservador | US$238,88 | US$228,70 | US$220,25 | US$229,28 | OK |
| EV/FCFF | Optimista | US$267,04 | US$297,05 | US$319,05 | US$294,38 | OK |
| P/E | Base | US$380,59 | US$385,78 | US$388,60 | US$384,99 | OK |
| P/E | Conservador | US$321,43 | US$300,75 | US$284,54 | US$302,24 | OK |
| P/E | Optimista | US$432,39 | US$464,05 | US$484,88 | US$460,44 | OK |
| P/FCFE | Base | US$276,77 | US$281,81 | US$287,23 | US$281,94 | OK |
| P/FCFE | Conservador | US$238,37 | US$223,49 | US$212,58 | US$224,81 | OK |
| P/FCFE | Optimista | US$297,11 | US$322,82 | US$340,82 | US$320,25 | OK |
| P/OCF | Base | US$247,03 | US$255,72 | US$263,65 | US$255,47 | OK |
| P/OCF | Conservador | US$222,65 | US$213,64 | US$206,14 | US$214,14 | OK |
| P/OCF | Optimista | US$258,08 | US$286,01 | US$306,57 | US$283,55 | OK |

Múltiplos consolidados hoy: US$320,13 / US$259,80 / US$366,30 · DCF de las historias hoy: US$488,09 / US$249,38 / US$600,33 · Ponderado hoy: US$420,91 / US$253,55 / US$506,72 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para INTU la diferencia es de −34% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$496,45 por acción y los múltiplos, US$386,84 hoy: 22% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$281,08 supone que los ingresos crecen 0,4% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 9,8% (−9,4 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$663,40 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,8%, WACC de los años 4-10 9,9%, ROE de FY+3 37,0% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 15,0x | 17,3x | −13% | 5,8% | 6,3% | −0,5 pp | Coherente con el DCF. |
| EV/FCFF | 16,5x | 30,0x | −44% | 3,6% | 6,3% | −2,7 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 44% por debajo del DCF en FY+3. |
| P/E | 19,9x | 25,3x | −21% | 6,3% | 7,4% | −1,0 pp | Coherente con el DCF. |
| P/FCFE | 14,9x | 26,1x | −41% | 3,8% | 6,7% | −2,9 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 41% por debajo del DCF en FY+3. |
| P/OCF | 15,2x | 29,0x | −46% | 3,2% | 6,7% | −3,5 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 46% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$420,91 | — |
| Múltiplos Base +20% | US$445,80 | +5,9% |
| Múltiplos Base −20% | US$396,02 | −5,9% |
| Crecimiento años 2-5 +2 pp | US$448,14 | +6,5% |
| Crecimiento años 2-5 −2 pp | US$395,98 | −5,9% |
| Margen objetivo +3 pp | US$447,77 | +6,4% |
| Margen objetivo −3 pp | US$394,05 | −6,4% |
| WACC +1 pp | US$404,57 | −3,9% |
| WACC −1 pp | US$438,41 | +4,2% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Crecimiento años 2-5 +2 pp, Margen objetivo −3 pp, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 12,91 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 13,11 | 15,02 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 16,34 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 14,38 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 17,37 | 16,48 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 17,87 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 17,48 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 18,58 | 19,93 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 22,22 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 12,86 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 15,43 | 14,94 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 16,07 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 12,82 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 16,23 | 15,18 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 16,47 | Múltiplo optimista elegido con el protocolo v3 |
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
