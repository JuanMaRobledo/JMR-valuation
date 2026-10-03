---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de DOMINOS PIZZA INC"
ticker: "DPZ"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1voP-krWxuq4RtJDX4WYP6FEG_rRoqjMjgVXF5vPywSo/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# DOMINOS PIZZA INC (DPZ) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$328,45 por acción.** Complemento: DCF esperado por probabilidades US$286,67; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$95,35–US$394,04; precio con MOS 35% sobre el esperado: US$186,34; precio de referencia US$297,62. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Crece por tiendas con ventas mismas tiendas bajas** (valor principal) | 50% | US$328,45 | US$164,23 |
| Conservadora · Los agregadores erosionan la ventaja | 25% | US$155,48 | US$38,87 |
| Disrupción · Deterioro de los fundamentales: El sistema de franquicias se debilita | 5% | US$95,35 | US$4,77 |
| Optimista · Agregadores e internacional aceleran | 20% | US$394,04 | US$78,81 |
| **DCF esperado (complemento)** | 100% | **US$286,67** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$349,85 por acción y los múltiplos, US$408,88 hoy: 17% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$328,45 | US$389,94 | US$365,35 | US$186,34 | US$484,87 |
| Conservador | US$155,48 | US$347,72 | US$270,82 | US$186,34 | US$347,73 |
| Optimista | US$394,04 | US$456,11 | US$431,28 | US$186,34 | US$584,22 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - DPZ](https://docs.google.com/spreadsheets/d/1voP-krWxuq4RtJDX4WYP6FEG_rRoqjMjgVXF5vPywSo/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$297,62.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 2,2% | 4,0% | 6,4% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 2,4% | 4,5% | 6,4% | Input B29 |
| Margen EBIT objetivo | 18,8% | 20,3% | 21,3% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,64 / 2,64 | — | Input B32/B33 |
| DCF por acción hoy | US$155,48 | US$328,45 | US$394,04 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,17, ERP 4,46%, Ke 10,21%, costo de la deuda después de impuestos 4,70%, peso del patrimonio 67,5%, WACC inicial 8,42% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Domino's es un franquiciador maduro desde hace una década con múltiplos estables (EV/EBITDA 18-30x); no hubo cambio de etapa del negocio, así que A usa los últimos cinco cierres y el LTM. B: franquiciadores y cadenas de restaurantes (Yum!, McDonald's, Restaurant Brands, Wingstop, Darden), datos de yfinance al 29-sep-2026. Se excluye Papa John's (ingresos −9%, reestructuración). Ajuste 0%: modelo de franquicia asset-light y crecimiento similares a Yum! y Restaurant Brands. λ = 0 (30-sep-2026): el justificado C supone que el ROE de FY+3 se mantiene para siempre, mientras que el DCF revisado limita el ROIC después del año 10 al 18,4% (el menor entre el actual y el de la industria). Para que los múltiplos sean coherentes con el DCF, C se deja fuera del Base y se conserva como referencia en la tabla.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana de los últimos 5 cierres + LTM depurados = 20,5x | 14,7x (n=5: YUM 16,4x, MCD 14,7x, QSR 14,0x, WING 16,7x, DRI 14,3x) × 1,00 = 14,7x | 17,7x / 16,0x / 18,8x | **17,6x** | 16,7x | 19,1x | 18,4x / 17,0x / 21,0x |
| EV/FCFF | mediana de los últimos 5 cierres + LTM depurados = 31,6x (EV/FCF × 0,81 = FCF después de intereses ÷ FCFF) | 24,2x (n=5: YUM 24,2x, MCD 24,2x, QSR 20,2x, WING 24,7x, DRI 28,2x) × 1,00 = 24,2x | 27,9x / 24,1x / 30,4x | **27,9x** | 26,3x | 30,3x | 33,0x / 30,6x / 37,6x |
| P/E | mediana de los últimos 5 cierres + LTM depurados = 26,7x | 19,0x (n=5: YUM 17,3x, MCD 19,0x, QSR 18,0x, WING 25,7x, DRI 19,2x) × 1,00 = 19,0x | — / — / — | **22,9x** | 22,2x | 25,1x | 22,9x / 22,2x / 25,1x |
| P/FCFE | mediana de los últimos 5 cierres + LTM depurados = 29,1x | 21,3x (n=5: YUM 22,4x, MCD 21,3x, QSR 20,1x, WING 23,0x, DRI 20,4x) × 1,00 = 21,3x | 19,8x / 17,8x / 21,0x | **25,2x** | 23,7x | 27,3x | 25,2x / 23,3x / 28,2x |
| P/OCF | mediana de los últimos 5 cierres + LTM depurados = 23,9x | 15,6x (n=5: YUM 18,0x, MCD 14,6x, QSR 17,2x, WING 15,6x, DRI 12,0x) × 1,00 = 15,6x | 22,9x / 18,0x / 26,8x | **19,8x** | 17,8x | 22,1x | 21,9x / 19,2x / 25,4x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 17,6x: promedio de historia y peers 17,6x, acercado 0% al justificado (17,7x); rango de anclas 14,7x–20,5x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 27,9x: promedio de historia y peers 27,9x, acercado 0% al justificado (27,9x); rango de anclas 24,2x–31,6x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 22,9x: promedio de historia y peers 22,9x, acercado 0% al justificado (—x); rango de anclas 19,0x–26,7x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 25,2x: promedio de historia y peers 25,2x, acercado 0% al justificado (19,8x); rango de anclas 19,8x–29,1x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 19,8x: promedio de historia y peers 19,8x, acercado 0% al justificado (22,9x); rango de anclas 15,6x–23,9x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$389,94 frente a US$328,45 del DCF (+19%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$389,94 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,21%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$95,35) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$328,45 por acción.** Complemento: DCF esperado por probabilidades US$286,67. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$328,45 | US$155,48 | US$394,04 |
| EV/EBITDA | 17,6× / 16,7× / 19,1× | 20% | 33% | US$383,57 | US$333,89 | US$458,41 |
| EV/FCFF | 27,9× / 26,3× / 30,3× | 10% | 17% | US$387,38 | US$354,90 | US$436,38 |
| P/E | 22,9× / 22,2× / 25,1× | 20% | 33% | US$381,25 | US$349,83 | US$441,22 |
| P/FCFE | 25,2× / 23,7× / 27,3× | 5% | 8% | US$495,98 | US$413,33 | US$610,54 |
| P/OCF | 19,8× / 17,8× / 22,1× | 5% | 8% | US$349,25 | US$314,67 | US$391,48 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$389,94 | US$347,72 | US$456,11 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$365,35 | US$270,82 | US$431,28 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$439,66 | US$208,12 | US$527,45 |
| EV/EBITDA (total con dividendos) | 17,6× / 16,7× / 19,1× | 20% | 33% | US$510,28 | US$424,98 | US$628,58 |
| EV/FCFF (total con dividendos) | 27,9× / 26,3× / 30,3× | 10% | 17% | US$514,14 | US$448,76 | US$611,35 |
| P/E (total con dividendos) | 22,9× / 22,2× / 25,1× | 20% | 33% | US$499,23 | US$441,60 | US$593,80 |
| P/FCFE (total con dividendos) | 25,2× / 23,7× / 27,3× | 5% | 8% | US$658,17 | US$528,57 | US$820,01 |
| P/OCF (total con dividendos) | 19,8× / 17,8× / 22,1× | 5% | 8% | US$455,59 | US$397,34 | US$532,65 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$515,01 | US$440,81 | US$622,07 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$28,58 | US$28,58 | US$28,58 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$486,43 | US$412,23 | US$593,49 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$484,87 | US$347,73 | US$584,22 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,21%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$382,98 | US$384,48 | US$383,25 | US$383,57 | OK |
| EV/EBITDA | Conservador | US$349,89 | US$332,26 | US$319,53 | US$333,89 | OK |
| EV/EBITDA | Optimista | US$441,20 | US$462,39 | US$471,63 | US$458,41 | OK |
| EV/FCFF | Base | US$389,83 | US$386,17 | US$386,14 | US$387,38 | OK |
| EV/FCFF | Conservador | US$375,84 | US$351,56 | US$337,30 | US$354,90 | OK |
| EV/FCFF | Optimista | US$411,76 | US$438,63 | US$458,76 | US$436,38 | OK |
| P/E | Base | US$387,10 | US$381,64 | US$375,00 | US$381,25 | OK |
| P/E | Conservador | US$369,43 | US$348,10 | US$331,94 | US$349,83 | OK |
| P/E | Optimista | US$433,94 | US$444,08 | US$445,65 | US$441,22 | OK |
| P/FCFE | Base | US$502,71 | US$491,50 | US$493,73 | US$495,98 | OK |
| P/FCFE | Conservador | US$433,47 | US$409,62 | US$396,91 | US$413,33 | OK |
| P/FCFE | Optimista | US$605,61 | US$611,36 | US$614,64 | US$610,54 | OK |
| P/OCF | Base | US$357,52 | US$347,83 | US$342,40 | US$349,25 | OK |
| P/OCF | Conservador | US$332,84 | US$312,28 | US$298,88 | US$314,67 | OK |
| P/OCF | Optimista | US$382,31 | US$392,17 | US$399,96 | US$391,48 | OK |

Múltiplos consolidados hoy: US$389,94 / US$347,72 / US$456,11 · DCF de las historias hoy: US$328,45 / US$155,48 / US$394,04 · Ponderado hoy: US$365,35 / US$270,82 / US$431,28 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para DPZ la diferencia es de +19% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$349,85 por acción y los múltiplos, US$408,88 hoy: 17% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$297,62 supone que los ingresos crecen 2,9% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 4,5% (−1,6 pp). Coherente: el precio supone un crecimiento parecido al del DCF.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$439,66 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,2%, WACC de los años 4-10 8,7%, ROE de FY+3 — y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 17,6x | 15,4x | +16% | 4,9% | 4,4% | +0,5 pp | Coherente con el DCF. |
| EV/FCFF | 27,9x | 24,3x | +17% | 4,9% | 4,4% | +0,5 pp | Coherente con el DCF. |
| P/E | 22,9x | 20,0x | +14% | — | — | — | Coherente con el DCF. |
| P/FCFE | 25,2x | 16,5x | +50% | 6,0% | 3,9% | +2,1 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 50% por encima del DCF en FY+3. |
| P/OCF | 19,8x | 19,0x | +4% | 4,1% | 3,9% | +0,2 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$365,35 | — |
| Múltiplos Base +20% | US$417,41 | +14,3% |
| Múltiplos Base −20% | US$313,28 | −14,3% |
| Crecimiento años 2-5 +2 pp | US$382,66 | +4,7% |
| Crecimiento años 2-5 −2 pp | US$349,56 | −4,3% |
| Margen objetivo +3 pp | US$392,22 | +7,4% |
| Margen objetivo −3 pp | US$338,47 | −7,4% |
| WACC +1 pp | US$354,84 | −2,9% |
| WACC −1 pp | US$376,61 | +3,1% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 17,00 | 16,71 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 18,41 | 17,57 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 20,99 | 19,15 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 30,63 | 26,28 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 33,02 | 27,89 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 37,65 | 30,30 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 22,17 | 22,17 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 22,85 | 22,85 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 25,09 | 25,09 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 23,30 | 23,72 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 25,23 | 25,23 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 28,17 | 27,30 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 19,24 | 17,76 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 21,94 | 19,76 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 25,37 | 22,10 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/DPZ_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1voP-krWxuq4RtJDX4WYP6FEG_rRoqjMjgVXF5vPywSo/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (YUM, MCD, PZZA, QSR, WING, DRI).

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
