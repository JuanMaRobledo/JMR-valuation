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

**Valor intrínseco principal · DCF Base hoy: US$388,50 por acción.** Complemento: DCF esperado por probabilidades US$342,95; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$168,69–US$504,17; precio con MOS 35% sobre el esperado: US$222,92; precio de referencia US$517,53. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Azure y Copilot sostienen el doble dígito** (valor principal) | 45% | US$388,50 | US$174,82 |
| Conservadora · El capex de IA rinde menos de lo esperado | 25% | US$201,69 | US$50,42 |
| Disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige | 10% | US$168,69 | US$16,87 |
| Optimista · Microsoft gana la plataforma empresarial de IA | 20% | US$504,17 | US$100,83 |
| **DCF esperado (complemento)** | 100% | **US$342,95** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$466,38 por acción y los múltiplos, US$466,16 hoy: prácticamente igual al DCF. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$388,50 | US$437,39 | US$408,05 | US$222,92 | US$588,07 |
| Conservador | US$201,69 | US$390,98 | US$277,40 | US$222,92 | US$384,89 |
| Optimista | US$504,17 | US$422,12 | US$471,35 | US$222,92 | US$712,72 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - Valoración MSFT - 2026-09-16](https://docs.google.com/spreadsheets/d/1ubjlRP0jbGmG_sXEoTrvonRkwqy5AoOd1ESrU4c3-rY/edit).
- Análisis del 16 de sept de 2026. Precio de referencia de la hoja: US$517,53.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 11,4% | 16,5% | 20,8% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 8,6% | 12,0% | 19,7% | Input B29 |
| Margen EBIT objetivo | 41,2% | 46,2% | 49,2% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 0,62 / 0,70 | — | Input B32/B33 |
| DCF por acción hoy | US$201,69 | US$388,50 | US$504,17 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,36, ERP 4,96%, Ke 12,03%, costo de la deuda después de impuestos 4,15%, peso del patrimonio 97,5%, WACC inicial 11,83% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Sin cambio de etapa: Microsoft sigue creciendo a doble dígito y cotiza por debajo de su promedio de cinco años; se usa la mediana de los últimos 5 cierres + LTM. Se excluye la columna sin fecha de la hoja. B: grandes plataformas tecnológicas y de software (Alphabet, Apple, Amazon, Oracle, Meta, Salesforce), datos de yfinance al 29-sep-2026. Amazon y Oracle no tienen flujo de caja libre positivo y no entran en los múltiplos de flujo. Ajuste +5%: Microsoft tiene el margen operativo más alto del grupo (45% frente a ~33%) y Azure acelera (~40%) con una cartera de US$678 mil millones. λ = 0 (30-sep-2026): el justificado C supone que el ROE de FY+3 se mantiene para siempre, mientras que el DCF revisado limita el ROIC después del año 10 al 25,9% (el menor entre el actual y el de la industria). Para que los múltiplos sean coherentes con el DCF, C se deja fuera del Base y se conserva como referencia en la tabla.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana de los últimos 5 cierres + LTM depurados = 22,3x | 17,1x (n=6: GOOG 23,2x, AAPL 28,8x, AMZN 16,5x, ORCL 15,6x, META 17,4x, CRM 16,9x) × 1,05 = 18,0x | 9,3x / 9,8x / 7,7x | **20,1x** | 19,5x | 21,6x | —x / —x / —x |
| EV/FCFF | mediana de los últimos 5 cierres + LTM depurados = 42,8x (EV/FCF × 0,98 = FCF después de intereses ÷ FCFF) | 40,0x (n=4: GOOG 73,1x, AAPL 35,3x, META 44,7x, CRM 13,8x) × 1,05 = 42,0x | 26,9x / 20,4x / 36,8x | **42,4x** | 31,8x | 52,4x | —x / —x / —x |
| P/E | mediana de los últimos 5 cierres + LTM depurados = 32,0x | 21,1x (n=6: GOOG 16,9x, AAPL 37,7x, AMZN 19,8x, ORCL 21,6x, META 27,8x, CRM 20,6x) × 1,05 = 22,2x | 17,2x / 13,8x / 21,8x | **27,1x** | 23,4x | 32,6x | —x / —x / —x |
| P/FCFE | mediana de los últimos 5 cierres + LTM depurados = 44,2x | 40,5x (n=4: GOOG 77,4x, AAPL 35,2x, META 45,9x, CRM 12,2x) × 1,05 = 42,6x | 20,5x / 16,4x / 25,8x | **43,4x** | 33,2x | 52,4x | —x / —x / —x |
| P/OCF | mediana de los últimos 5 cierres + LTM depurados = 24,3x | 16,2x (n=6: GOOG 22,2x, AAPL 32,8x, AMZN 17,9x, ORCL 8,9x, META 14,4x, CRM 11,8x) × 1,05 = 17,0x | 10,6x / 9,1x / 11,8x | **20,7x** | 17,1x | 24,4x | —x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 20,1x: promedio de historia y peers 20,1x, acercado 0% al justificado (9,3x); rango de anclas 9,3x–22,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 42,4x: promedio de historia y peers 42,4x, acercado 0% al justificado (26,9x); rango de anclas 26,9x–42,8x. Atípicos excluidos de la historia: ninguno. EV/FCFF: la razón FCF después de intereses ÷ FCFF se fija en 0,98 (mediana de los tres cierres reales); el último cierre da 1,28 porque 'Interest / Other' incluye partidas no operativas. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 27,1x: promedio de historia y peers 27,1x, acercado 0% al justificado (17,2x); rango de anclas 17,2x–32,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 43,4x: promedio de historia y peers 43,4x, acercado 0% al justificado (20,5x); rango de anclas 20,5x–44,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 20,7x: promedio de historia y peers 20,7x, acercado 0% al justificado (10,6x); rango de anclas 10,6x–24,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$437,39 frente a US$388,50 del DCF (+13%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$437,39 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Software»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 12,03%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$168,69) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$388,50 por acción.** Complemento: DCF esperado por probabilidades US$342,95. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$388,50 | US$201,69 | US$504,17 |
| EV/EBITDA | 20,1× / 19,5× / 21,6× | 10% | 25% | US$532,12 | US$461,09 | US$629,85 |
| EV/FCFF | 42,4× / 31,8× / 52,4× | 15% | 37% | US$355,42 | US$347,39 | US$222,42 |
| P/E | 27,1× / 23,4× / 32,6× | 5% | 12% | US$492,40 | US$380,11 | US$654,57 |
| P/FCFE | 43,4× / 33,2× / 52,4× | 5% | 12% | US$451,23 | US$405,25 | US$369,87 |
| P/OCF | 20,7× / 17,1× / 24,4× | 5% | 12% | US$424,95 | US$378,10 | US$425,54 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$437,39 | US$390,98 | US$422,12 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$408,05 | US$277,40 | US$471,35 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$546,22 | US$283,57 | US$708,85 |
| EV/EBITDA (total con dividendos) | 20,1× / 19,5× / 21,6× | 10% | 25% | US$761,42 | US$618,56 | US$950,70 |
| EV/FCFF (total con dividendos) | 42,4× / 31,8× / 52,4× | 15% | 37% | US$557,33 | US$490,00 | US$488,22 |
| P/E (total con dividendos) | 27,1× / 23,4× / 32,6× | 5% | 12% | US$698,84 | US$504,34 | US$981,58 |
| P/FCFE (total con dividendos) | 43,4× / 33,2× / 52,4× | 5% | 12% | US$682,60 | US$559,60 | US$693,78 |
| P/OCF (total con dividendos) | 20,7× / 17,1× / 24,4× | 5% | 12% | US$630,59 | US$523,83 | US$706,89 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 40% | 100% | US$650,86 | US$536,86 | US$718,54 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$13,00 | US$13,00 | US$13,00 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$637,86 | US$523,86 | US$705,54 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$588,07 | US$384,89 | US$712,72 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 12,03%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$519,11 | US$534,61 | US$542,64 | US$532,12 | OK |
| EV/EBITDA | Conservador | US$481,45 | US$460,80 | US$441,03 | US$461,09 | OK |
| EV/EBITDA | Optimista | US$578,40 | US$633,89 | US$677,27 | US$629,85 | OK |
| EV/FCFF | Base | US$311,46 | US$357,33 | US$397,48 | US$355,42 | OK |
| EV/FCFF | Conservador | US$346,73 | US$345,84 | US$349,59 | US$347,39 | OK |
| EV/FCFF | Optimista | US$108,84 | US$210,10 | US$348,33 | US$222,42 | OK |
| P/E | Base | US$485,38 | US$493,68 | US$498,13 | US$492,40 | OK |
| P/E | Conservador | US$401,92 | US$378,63 | US$359,80 | US$380,11 | OK |
| P/E | Optimista | US$606,61 | US$657,86 | US$699,23 | US$654,57 | OK |
| P/FCFE | Base | US$415,01 | US$452,11 | US$486,58 | US$451,23 | OK |
| P/FCFE | Conservador | US$415,05 | US$401,61 | US$399,09 | US$405,25 | OK |
| P/FCFE | Optimista | US$255,42 | US$359,66 | US$494,53 | US$369,87 | OK |
| P/OCF | Base | US$398,43 | US$426,85 | US$449,59 | US$424,95 | OK |
| P/OCF | Conservador | US$382,79 | US$377,87 | US$373,66 | US$378,10 | OK |
| P/OCF | Optimista | US$351,78 | US$421,00 | US$503,86 | US$425,54 | OK |

Múltiplos consolidados hoy: US$437,39 / US$390,98 / US$422,12 · DCF de las historias hoy: US$388,50 / US$201,69 / US$504,17 · Ponderado hoy: US$408,05 / US$277,40 / US$471,35 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para MSFT la diferencia es de +13% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$466,38 por acción y los múltiplos, US$466,16 hoy: prácticamente igual al DCF. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$517,53 supone que los ingresos crecen 20,4% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 13,0% (+7,4 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$546,22 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 12,0%, WACC de los años 4-10 10,8%, ROE de FY+3 42,7% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 20,1x | 14,3x | +39% | 8,9% | 8,2% | +0,7 pp | Revisar: el múltiplo vale 39% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 42,4x | 41,3x | +2% | 8,2% | 8,2% | +0,1 pp | Coherente con el DCF. |
| P/E | 27,1x | 21,1x | +28% | 8,8% | 7,8% | +1,0 pp | Revisar: el múltiplo vale 28% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 43,4x | 34,6x | +25% | 9,5% | 8,9% | +0,6 pp | Coherente con el DCF. |
| P/OCF | 20,7x | 17,8x | +15% | 9,3% | 8,9% | +0,4 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$408,05 | — |
| Múltiplos Base +20% | US$442,57 | +8,5% |
| Múltiplos Base −20% | US$373,54 | −8,5% |
| Crecimiento años 2-5 +2 pp | US$427,08 | +4,7% |
| Crecimiento años 2-5 −2 pp | US$390,63 | −4,3% |
| Margen objetivo +3 pp | US$424,02 | +3,9% |
| Margen objetivo −3 pp | US$392,09 | −3,9% |
| WACC +1 pp | US$394,68 | −3,3% |
| WACC −1 pp | US$422,38 | +3,5% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 19,48 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | — | 20,12 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 21,59 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 31,83 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | — | 42,41 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 52,43 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 23,38 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | — | 27,08 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 32,63 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 33,23 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | — | 43,39 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 52,44 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 17,13 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | — | 20,67 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 24,35 | Múltiplo optimista elegido con el protocolo v3 |
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
