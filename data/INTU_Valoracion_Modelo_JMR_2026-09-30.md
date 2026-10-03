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

**Valor intrínseco principal · DCF Base hoy: US$512,99 por acción.** Complemento: DCF esperado por probabilidades US$443,16; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$208,74–US$631,49; precio con MOS 35% sobre el esperado: US$288,05; precio de referencia US$281,08. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$512,99), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La IA es palanca de monetización** (valor principal) | 45% | US$512,99 | US$230,85 |
| Conservadora · La IA erosiona impuestos y contabilidad básica | 25% | US$260,56 | US$65,14 |
| Disrupción · Deterioro de los fundamentales: Recesión y declaración gratuita del Estado | 10% | US$208,74 | US$20,87 |
| Optimista · Plataforma financiera de la pyme | 20% | US$631,49 | US$126,30 |
| **DCF esperado (complemento)** | 100% | **US$443,16** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$496,45 por acción y los múltiplos, US$386,84 hoy: 22% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$512,99 | US$343,34 | US$445,13 | US$288,05 | US$601,22 |
| Conservador | US$260,56 | US$282,25 | US$269,23 | US$288,05 | US$353,64 |
| Optimista | US$631,49 | US$455,94 | US$561,27 | US$288,05 | US$769,34 |

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
| DCF por acción hoy | US$260,56 | US$512,99 | US$631,49 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,20, ERP 4,46%, Ke 10,34%, costo de la deuda después de impuestos 4,53%, peso del patrimonio 91,2%, WACC inicial 9,83% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Intuit cotizó a 30-51x EBITDA y 44-70x utilidades mientras crecía 12-20% con TurboTax, Credit Karma y QuickBooks. En 2026 el mercado empezó a temer que los agentes de IA hagan el trabajo de impuestos y contabilidad por el que cobra; recortó la guía de TurboTax, anunció una reestructuración y su guía FY27 (9-10% de crecimiento, TurboTax 2-3%) decepcionó. La acción cayó ~60% desde su máximo. La etapa actual es el cierre Jul '26 y el LTM. B: software de aplicaciones y nómina/finanzas (Adobe, Autodesk, Salesforce, Workday, ADP, Paychex), datos de yfinance al 29-sep-2026. Sin ajuste: Intuit crece 9-10% con márgenes altos, en línea con la mediana de los peers. λ = 0,25: la Intuit de FY+3 del escenario Base crece al ~10%, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Jul '26, LTM (etapa actual) = 12,3x | 16,7x (n=6: ADBE 9,3x, ADSK 18,4x, CRM 16,9x, WDAY 29,0x, ADP 16,4x, PAYX 12,7x) × 1,00 = 16,7x | 24,6x / 19,3x / 43,8x | **17,0x** | 14,5x | 22,1x | 13,1x / —x / —x |
| EV/FCFF | mediana Jul '26, LTM (etapa actual) = 9,5x (EV/FCF × 1,02 = FCF después de intereses ÷ FCFF) | 15,2x (n=6: ADBE 8,5x, ADSK 15,0x, CRM 13,8x, WDAY 15,7x, ADP 20,5x, PAYX 15,4x) × 1,00 = 15,2x | 31,8x / 25,1x / 56,4x | **17,2x** | 15,4x | 22,0x | 17,4x / —x / —x |
| P/E | mediana Jul '26, LTM (etapa actual) = 18,0x | 22,3x (n=6: ADBE 13,0x, ADSK 26,3x, CRM 20,6x, WDAY 38,8x, ADP 23,9x, PAYX 19,7x) × 1,00 = 22,3x | 20,8x / 17,1x / 32,0x | **20,3x** | 18,1x | 25,2x | 18,6x / —x / —x |
| P/FCFE | mediana Jul '26, LTM (etapa actual) = 9,1x | 15,2x (n=6: ADBE 8,8x, ADSK 15,1x, CRM 12,2x, WDAY 16,0x, ADP 21,7x, PAYX 15,2x) × 1,00 = 15,2x | 25,2x / 20,8x / 38,7x | **15,4x** | 13,6x | 18,6x | 15,4x / —x / —x |
| P/OCF | mediana Jul '26, LTM (etapa actual) = 9,0x | 14,2x (n=6: ADBE 8,6x, ADSK 14,7x, CRM 11,8x, WDAY 14,8x, ADP 19,1x, PAYX 13,8x) × 1,00 = 14,2x | 27,4x / 21,9x / 43,9x | **15,6x** | 13,6x | 19,0x | 16,2x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 17,0x: promedio de historia y peers 14,5x, acercado 25% al justificado (24,6x); rango de anclas 12,3x–24,6x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 17,2x: promedio de historia y peers 12,3x, acercado 25% al justificado (31,8x); rango de anclas 9,5x–31,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 20,3x: promedio de historia y peers 20,1x, acercado 25% al justificado (20,8x); rango de anclas 17,9x–22,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 15,4x: promedio de historia y peers 12,2x, acercado 25% al justificado (25,2x); rango de anclas 9,2x–25,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 15,6x: promedio de historia y peers 11,6x, acercado 25% al justificado (27,4x); rango de anclas 9,0x–27,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$343,34 frente a US$512,99 del DCF (−33%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$343,34 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Software»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,34%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$208,74) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$512,99 por acción.** Complemento: DCF esperado por probabilidades US$443,16. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$512,99 | US$260,56 | US$631,49 |
| EV/EBITDA | 17,0× / 14,5× / 22,1× | 10% | 25% | US$479,54 | US$367,41 | US$666,56 |
| EV/FCFF | 17,2× / 15,4× / 22,0× | 15% | 38% | US$278,65 | US$246,65 | US$363,24 |
| P/E | 20,3× / 18,1× / 25,2× | 5% | 13% | US$394,97 | US$315,77 | US$524,45 |
| P/FCFE | 15,4× / 13,6× / 18,6× | 5% | 13% | US$293,08 | US$238,91 | US$371,50 |
| P/OCF | 15,6× / 13,6× / 19,0× | 5% | 13% | US$263,63 | US$228,55 | US$328,71 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$343,34 | US$282,25 | US$455,94 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$445,13 | US$269,23 | US$561,27 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$689,18 | US$350,04 | US$848,37 |
| EV/EBITDA (total con dividendos) | 17,0× / 14,5× / 22,1× | 10% | 25% | US$648,03 | US$463,03 | US$938,27 |
| EV/FCFF (total con dividendos) | 17,2× / 15,4× / 22,0× | 15% | 38% | US$385,83 | US$317,00 | US$527,22 |
| P/E (total con dividendos) | 20,3× / 18,1× / 25,2× | 5% | 13% | US$535,53 | US$398,67 | US$741,83 |
| P/FCFE (total con dividendos) | 15,4× / 13,6× / 18,6× | 5% | 13% | US$400,44 | US$302,25 | US$530,09 |
| P/OCF (total con dividendos) | 15,6× / 13,6× / 19,0× | 5% | 13% | US$364,73 | US$294,25 | US$476,21 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 40% | 100% | US$469,28 | US$359,03 | US$650,79 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$20,13 | US$20,13 | US$20,13 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$449,15 | US$338,90 | US$630,66 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$601,22 | US$353,64 | US$769,34 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,34%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$474,75 | US$480,05 | US$483,81 | US$479,54 | OK |
| EV/EBITDA | Conservador | US$390,62 | US$365,49 | US$346,11 | US$367,41 | OK |
| EV/EBITDA | Optimista | US$629,05 | US$670,79 | US$699,85 | US$666,56 | OK |
| EV/FCFF | Base | US$268,37 | US$278,93 | US$288,65 | US$278,65 | OK |
| EV/FCFF | Conservador | US$256,47 | US$246,07 | US$237,41 | US$246,65 | OK |
| EV/FCFF | Optimista | US$329,34 | US$366,49 | US$393,89 | US$363,24 | OK |
| P/E | Base | US$389,07 | US$395,78 | US$400,07 | US$394,97 | OK |
| P/E | Conservador | US$334,85 | US$314,27 | US$298,21 | US$315,77 | OK |
| P/E | Optimista | US$491,19 | US$528,51 | US$553,64 | US$524,45 | OK |
| P/FCFE | Base | US$286,78 | US$292,95 | US$299,52 | US$293,08 | OK |
| P/FCFE | Conservador | US$252,76 | US$237,55 | US$226,43 | US$238,91 | OK |
| P/FCFE | Optimista | US$344,03 | US$374,44 | US$396,02 | US$371,50 | OK |
| P/OCF | Base | US$254,06 | US$263,88 | US$272,94 | US$263,63 | OK |
| P/OCF | Conservador | US$237,14 | US$228,04 | US$220,48 | US$228,55 | OK |
| P/OCF | Optimista | US$298,70 | US$331,51 | US$355,92 | US$328,71 | OK |

Múltiplos consolidados hoy: US$343,34 / US$282,25 / US$455,94 · DCF de las historias hoy: US$512,99 / US$260,56 / US$631,49 · Ponderado hoy: US$445,13 / US$269,23 / US$561,27 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para INTU la diferencia es de −33% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$496,45 por acción y los múltiplos, US$386,84 hoy: 22% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$281,08 supone que los ingresos crecen -0,4% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 9,8% (−10,2 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$689,18 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,3%, WACC de los años 4-10 9,5%, ROE de FY+3 35,3% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 17,0x | 18,0x | −6% | 4,7% | 5,0% | −0,3 pp | Coherente con el DCF. |
| EV/FCFF | 17,2x | 31,2x | −44% | 3,5% | 6,1% | −2,6 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 44% por debajo del DCF en FY+3. |
| P/E | 20,3x | 26,4x | −22% | 6,0% | 7,1% | −1,1 pp | Coherente con el DCF. |
| P/FCFE | 15,4x | 27,1x | −42% | 3,6% | 6,4% | −2,8 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 42% por debajo del DCF en FY+3. |
| P/OCF | 15,6x | 30,2x | −47% | 3,1% | 6,5% | −3,4 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 47% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$445,13 | — |
| Múltiplos Base +20% | US$471,87 | +6,0% |
| Múltiplos Base −20% | US$418,39 | −6,0% |
| Crecimiento años 2-5 +2 pp | US$474,00 | +6,5% |
| Crecimiento años 2-5 −2 pp | US$418,70 | −5,9% |
| Margen objetivo +3 pp | US$473,37 | +6,3% |
| Margen objetivo −3 pp | US$416,89 | −6,3% |
| WACC +1 pp | US$427,83 | −3,9% |
| WACC −1 pp | US$463,67 | +4,2% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Crecimiento años 2-5 +2 pp, Margen objetivo +3 pp, Margen objetivo −3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 14,54 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 13,11 | 16,99 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 22,08 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 15,39 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 17,37 | 17,21 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 21,99 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 18,15 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 18,58 | 20,30 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 25,18 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 13,60 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 15,43 | 15,43 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 18,58 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 13,62 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 16,23 | 15,56 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 19,04 | Múltiplo optimista elegido con el protocolo v3 |
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
