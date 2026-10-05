---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de ADOBE INC."
ticker: "ADBE"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/19WcSOKymo4gR6lnKiLB1gAitYFFwfI3xl08E4BDzLDw/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# ADOBE INC. (ADBE) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$410,48 por acción.** Complemento: DCF esperado por probabilidades US$326,24; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$167,27–US$509,73; precio con MOS 35% sobre el esperado: US$212,06; precio de referencia US$237,69. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La IA se cobra dentro de la suscripción** (valor principal) | 40% | US$410,48 | US$164,19 |
| Conservadora · Erosión gradual frente a Figma y Canva | 35% | US$245,68 | US$85,99 |
| Disrupción · Deterioro de los fundamentales: La IA generativa comoditiza la creatividad | 15% | US$167,27 | US$25,09 |
| Optimista · La IA amplía el mercado de Adobe | 10% | US$509,73 | US$50,97 |
| **DCF esperado (complemento)** | 100% | **US$326,24** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$536,48 por acción y los múltiplos, US$486,87 hoy: 9% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$410,48 | US$414,97 | US$413,18 | US$212,06 | US$573,93 |
| Conservador | US$245,68 | US$293,74 | US$274,52 | US$212,06 | US$366,06 |
| Optimista | US$509,73 | US$554,81 | US$536,78 | US$212,06 | US$775,09 |

## 2. Datos

- Hoja del modelo: [Modelo_JMR_Plantilla_Maestra ADBE](https://docs.google.com/spreadsheets/d/19WcSOKymo4gR6lnKiLB1gAitYFFwfI3xl08E4BDzLDw/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$237,69.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 8,8% | 12,0% | 12,7% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 6,0% | 10,0% | 12,2% | Input B29 |
| Margen EBIT objetivo | 37,1% | 40,1% | 43,1% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 3 | 3 | 3 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,23 / 1,23 | — | Input B32/B33 |
| DCF por acción hoy | US$245,68 | US$410,48 | US$509,73 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,31, ERP 5,02%, Ke 11,84%, costo de la deuda después de impuestos 4,55%, peso del patrimonio 94,2%, WACC inicial 11,42% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Adobe pasó de crecer 15-25% anual (FY16-FY21) a ~10-11% (FY23-FY25: +10,2%, +10,8%, +10,5%), y el mercado re-valoró el software de aplicaciones por el riesgo de la IA generativa; los múltiplos de 40-60x de la etapa anterior no describen a la empresa de FY+3, así que A usa solo los cierres FY23-FY25 y el LTM. B: peers de software de aplicaciones con datos de yfinance al 29-sep-2026 (ADSK, INTU, CRM, WDAY, PTC); se excluye ServiceNow (NOW) porque crece 24% con margen operativo GAAP de 4%, lo que infla sus múltiplos (P/E 81x). No se usa MSFT (megacap diversificada). Ajuste +5%: margen operativo de Adobe 35-39% frente a ~21% de mediana de los peers y conversión de caja superior (+10%), compensado en parte por un crecimiento algo menor (10-12% vs ~13% de mediana, -5%). λ = 0,25: la Adobe de FY+3 del escenario Base (crecimiento ~10%, margen 40%) es parecida a la de hoy, así que el Base se acerca solo un 25% al múltiplo justificado.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 21,8x | 16,9x (n=5: ADSK 18,4x, INTU 10,7x, CRM 16,9x, WDAY 28,9x, PTC 12,9x) × 1,05 = 17,8x | 12,8x / 11,6x / 14,2x | **18,0x** | 13,6x | 21,9x | 19,6x / 13,9x / 28,6x |
| EV/FCFF | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 21,1x | 15,0x (n=5: ADSK 15,0x, INTU 8,3x, CRM 13,8x, WDAY 15,6x, PTC 16,6x) × 1,05 = 15,7x | 21,6x / 18,3x / 26,0x | **19,2x** | 15,1x | 23,9x | 21,1x / 16,1x / 31,2x |
| P/E | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 30,5x | 20,6x (n=5: ADSK 26,3x, INTU 16,3x, CRM 20,6x, WDAY 38,8x, PTC 13,3x) × 1,05 = 21,6x | 16,0x / 14,0x / 18,5x | **23,5x** | 17,6x | 30,5x | 24,7x / 17,9x / 35,6x |
| P/FCFE | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 21,2x | 15,1x (n=5: ADSK 15,1x, INTU 8,3x, CRM 12,2x, WDAY 16,0x, PTC 16,0x) × 1,05 = 15,9x | 17,1x / 14,9x / 19,7x | **18,2x** | 13,7x | 22,4x | 19,5x / 14,2x / 26,8x |
| P/OCF | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 20,7x | 14,7x (n=5: ADSK 14,7x, INTU 8,1x, CRM 11,8x, WDAY 14,8x, PTC 15,6x) × 1,05 = 15,4x | 17,4x / 14,9x / 20,6x | **17,9x** | 13,4x | 21,9x | 18,9x / 13,8x / 25,7x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 18,0x: promedio de historia y peers 19,8x, acercado 25% al justificado (12,8x); rango de anclas 12,8x–21,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 19,2x: promedio de historia y peers 18,4x, acercado 25% al justificado (21,6x); rango de anclas 15,7x–21,6x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 23,5x: promedio de historia y peers 26,1x, acercado 25% al justificado (16,0x); rango de anclas 16,0x–30,5x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 18,2x: promedio de historia y peers 18,5x, acercado 25% al justificado (17,1x); rango de anclas 15,9x–21,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 17,9x: promedio de historia y peers 18,1x, acercado 25% al justificado (17,4x); rango de anclas 15,4x–20,7x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$414,97 frente a US$410,48 del DCF (+1%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$414,97 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 11,84%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$167,27) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$410,48 por acción.** Complemento: DCF esperado por probabilidades US$326,24. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$410,48 | US$245,68 | US$509,73 |
| EV/EBITDA | 18,0× / 13,6× / 21,9× | 20% | 33% | US$484,10 | US$335,63 | US$640,37 |
| EV/FCFF | 19,2× / 15,1× / 23,9× | 10% | 17% | US$292,33 | US$229,26 | US$361,40 |
| P/E | 23,5× / 17,6× / 30,5× | 20% | 33% | US$462,44 | US$318,16 | US$654,54 |
| P/FCFE | 18,2× / 13,7× / 22,4× | 5% | 8% | US$315,40 | US$232,57 | US$397,06 |
| P/OCF | 17,9× / 13,4× / 21,9× | 5% | 8% | US$293,49 | US$218,70 | US$358,19 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$414,97 | US$293,74 | US$554,81 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$413,18 | US$274,52 | US$536,78 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$574,29 | US$343,72 | US$713,15 |
| EV/EBITDA | 18,0× / 13,6× / 21,9× | 20% | 33% | US$663,41 | US$432,67 | US$930,61 |
| EV/FCFF | 19,2× / 15,1× / 23,9× | 10% | 17% | US$417,93 | US$305,37 | US$556,57 |
| P/E | 23,5× / 17,6× / 30,5× | 20% | 33% | US$635,89 | US$410,39 | US$956,55 |
| P/FCFE | 18,2× / 13,7× / 22,4× | 5% | 8% | US$433,31 | US$297,57 | US$586,77 |
| P/OCF | 17,9× / 13,4× / 21,9× | 5% | 8% | US$417,87 | US$290,80 | US$547,96 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 60% | 100% | US$573,69 | US$380,95 | US$816,38 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$573,93 | US$366,06 | US$775,09 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 11,84%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$490,75 | US$487,37 | US$474,18 | US$484,10 | OK |
| EV/EBITDA | Conservador | US$363,02 | US$334,61 | US$309,26 | US$335,63 | OK |
| EV/EBITDA | Optimista | US$606,55 | US$649,39 | US$665,16 | US$640,37 | OK |
| EV/FCFF | Base | US$282,09 | US$296,18 | US$298,72 | US$292,33 | OK |
| EV/FCFF | Conservador | US$240,01 | US$229,49 | US$218,27 | US$229,26 | OK |
| EV/FCFF | Optimista | US$316,27 | US$370,10 | US$397,81 | US$361,40 | OK |
| P/E | Base | US$466,65 | US$466,16 | US$454,51 | US$462,44 | OK |
| P/E | Conservador | US$343,79 | US$317,36 | US$293,33 | US$318,16 | OK |
| P/E | Optimista | US$614,96 | US$664,95 | US$683,70 | US$654,54 | OK |
| P/FCFE | Base | US$325,18 | US$311,31 | US$309,71 | US$315,40 | OK |
| P/FCFE | Conservador | US$258,79 | US$226,22 | US$212,69 | US$232,57 | OK |
| P/FCFE | Optimista | US$374,61 | US$397,17 | US$419,40 | US$397,06 | OK |
| P/OCF | Base | US$284,63 | US$297,16 | US$298,67 | US$293,49 | OK |
| P/OCF | Conservador | US$229,34 | US$218,92 | US$207,85 | US$218,70 | OK |
| P/OCF | Optimista | US$316,55 | US$366,35 | US$391,66 | US$358,19 | OK |

Múltiplos consolidados hoy: US$414,97 / US$293,74 / US$554,81 · DCF de las historias hoy: US$410,48 / US$245,68 / US$509,73 · Ponderado hoy: US$413,18 / US$274,52 / US$536,78 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para ADBE la diferencia es de +1% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$536,48 por acción y los múltiplos, US$486,87 hoy: 9% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$237,69 supone que los ingresos crecen -1,6% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 8,1% (−9,7 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$574,29 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,8%, WACC de los años 4-10 10,5%, ROE de FY+3 91,9% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 18,0x | 15,6x | +16% | 7,0% | 6,5% | +0,5 pp | Coherente con el DCF. |
| EV/FCFF | 19,2x | 26,3x | −27% | 5,1% | 6,5% | −1,4 pp | Revisar: el múltiplo vale 27% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 23,5x | 21,3x | +11% | 7,7% | 7,2% | +0,5 pp | Coherente con el DCF. |
| P/FCFE | 18,2x | 24,1x | −25% | 6,0% | 7,4% | −1,4 pp | Coherente con el DCF. |
| P/OCF | 17,9x | 24,6x | −27% | 5,8% | 7,4% | −1,6 pp | Revisar: el múltiplo vale 27% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$413,18 | — |
| Múltiplos Base +20% | US$463,10 | +12,1% |
| Múltiplos Base −20% | US$363,25 | −12,1% |
| Crecimiento años 2-5 +2 pp | US$427,52 | +3,5% |
| Crecimiento años 2-5 −2 pp | US$400,06 | −3,2% |
| Margen objetivo +3 pp | US$425,82 | +3,1% |
| Margen objetivo −3 pp | US$400,53 | −3,1% |
| WACC +1 pp | US$404,21 | −2,2% |
| WACC −1 pp | US$422,78 | +2,3% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 13,90 | 13,59 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 19,57 | 18,02 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 28,65 | 21,87 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 16,08 | 15,10 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 21,10 | 19,20 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 31,21 | 23,93 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 17,94 | 17,65 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 24,73 | 23,54 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 35,57 | 30,49 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 14,22 | 13,72 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 19,46 | 18,16 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 26,83 | 22,45 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 13,78 | 13,39 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 18,89 | 17,89 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 25,70 | 21,94 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/ADBE_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/19WcSOKymo4gR6lnKiLB1gAitYFFwfI3xl08E4BDzLDw/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (ADSK, INTU, CRM, NOW, WDAY, PTC).

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
