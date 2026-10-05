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

**Valor intrínseco principal · DCF Base hoy: US$403,20 por acción.** Complemento: DCF esperado por probabilidades US$356,20; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$174,71–US$524,51; precio con MOS 35% sobre el esperado: US$231,53; precio de referencia US$512,90. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Azure y Copilot sostienen el doble dígito** (valor principal) | 45% | US$403,20 | US$181,44 |
| Conservadora · El capex de IA rinde menos de lo esperado | 25% | US$209,54 | US$52,38 |
| Disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige | 10% | US$174,71 | US$17,47 |
| Optimista · Microsoft gana la plataforma empresarial de IA | 20% | US$524,51 | US$104,90 |
| **DCF esperado (complemento)** | 100% | **US$356,20** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$466,38 por acción y los múltiplos, US$466,16 hoy: prácticamente igual al DCF. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$403,20 | US$440,77 | US$418,23 | US$231,53 | US$596,63 |
| Conservador | US$209,54 | US$391,91 | US$282,48 | US$231,53 | US$388,42 |
| Optimista | US$524,51 | US$428,49 | US$486,10 | US$231,53 | US$726,89 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - Valoración MSFT - 2026-09-16](https://docs.google.com/spreadsheets/d/1ubjlRP0jbGmG_sXEoTrvonRkwqy5AoOd1ESrU4c3-rY/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$512,90.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 11,4% | 16,5% | 20,8% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 8,6% | 12,0% | 19,7% | Input B29 |
| Margen EBIT objetivo | 41,2% | 46,2% | 49,2% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 0,62 / 0,94 | — | Input B32/B33 |
| DCF por acción hoy | US$209,54 | US$403,20 | US$524,51 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,27, ERP 4,96%, Ke 11,60%, costo de la deuda después de impuestos 4,15%, peso del patrimonio 97,6%, WACC inicial 11,43% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Sin cambio de etapa: Microsoft sigue creciendo a doble dígito y cotiza por debajo de su promedio de cinco años; se usa la mediana de los últimos 5 cierres + LTM. Se excluye la columna sin fecha de la hoja. B: grandes plataformas tecnológicas y de software (Alphabet, Apple, Amazon, Oracle, Meta, Salesforce), datos de yfinance al 29-sep-2026. Amazon y Oracle no tienen flujo de caja libre positivo y no entran en los múltiplos de flujo. Ajuste +5%: Microsoft tiene el margen operativo más alto del grupo (45% frente a ~33%) y Azure acelera (~40%) con una cartera de US$678 mil millones. λ = 0 (30-sep-2026): el justificado C supone que el ROE de FY+3 se mantiene para siempre, mientras que el DCF revisado limita el ROIC después del año 10 al 25,9% (el menor entre el actual y el de la industria). Para que los múltiplos sean coherentes con el DCF, C se deja fuera del Base y se conserva como referencia en la tabla.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana de los últimos 5 cierres + LTM depurados = 22,3x | 17,1x (n=6: GOOG 23,2x, AAPL 28,8x, AMZN 16,5x, ORCL 15,6x, META 17,4x, CRM 16,9x) × 1,05 = 18,0x | 9,9x / 10,3x / 8,4x | **20,1x** | 19,4x | 21,7x | —x / —x / —x |
| EV/FCFF | mediana de los últimos 5 cierres + LTM depurados = 42,8x (EV/FCF × 0,98 = FCF después de intereses ÷ FCFF) | 40,0x (n=4: GOOG 73,1x, AAPL 35,3x, META 44,7x, CRM 13,8x) × 1,05 = 42,0x | 28,6x / 21,3x / 40,0x | **42,4x** | 31,7x | 52,9x | —x / —x / —x |
| P/E | mediana de los últimos 5 cierres + LTM depurados = 32,0x | 21,1x (n=6: GOOG 16,9x, AAPL 37,7x, AMZN 19,8x, ORCL 21,6x, META 27,8x, CRM 20,6x) × 1,05 = 22,2x | 18,7x / 14,8x / 24,2x | **27,1x** | 23,3x | 32,9x | —x / —x / —x |
| P/FCFE | mediana de los últimos 5 cierres + LTM depurados = 44,2x | 40,5x (n=4: GOOG 77,4x, AAPL 35,2x, META 45,9x, CRM 12,2x) × 1,05 = 42,6x | 22,3x / 17,6x / 28,8x | **43,4x** | 33,0x | 52,9x | —x / —x / —x |
| P/OCF | mediana de los últimos 5 cierres + LTM depurados = 24,3x | 16,2x (n=6: GOOG 22,2x, AAPL 32,8x, AMZN 17,9x, ORCL 8,9x, META 14,4x, CRM 11,8x) × 1,05 = 17,0x | 11,5x / 9,7x / 13,1x | **20,7x** | 17,0x | 24,5x | —x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 20,1x: promedio de historia y peers 20,1x, acercado 0% al justificado (9,9x); rango de anclas 9,9x–22,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 42,4x: promedio de historia y peers 42,4x, acercado 0% al justificado (28,6x); rango de anclas 28,6x–42,8x. Atípicos excluidos de la historia: ninguno. EV/FCFF: la razón FCF después de intereses ÷ FCFF se fija en 0,98 (mediana de los tres cierres reales); el último cierre da 1,28 porque 'Interest / Other' incluye partidas no operativas. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 27,1x: promedio de historia y peers 27,1x, acercado 0% al justificado (18,7x); rango de anclas 18,7x–32,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 43,4x: promedio de historia y peers 43,4x, acercado 0% al justificado (22,3x); rango de anclas 22,3x–44,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 20,7x: promedio de historia y peers 20,7x, acercado 0% al justificado (11,5x); rango de anclas 11,5x–24,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$440,77 frente a US$403,20 del DCF (+9%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$440,77 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Software»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 11,60%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$174,71) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$403,20 por acción.** Complemento: DCF esperado por probabilidades US$356,20. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$403,20 | US$209,54 | US$524,51 |
| EV/EBITDA | 20,1× / 19,4× / 21,7× | 10% | 25% | US$536,19 | US$461,95 | US$638,26 |
| EV/FCFF | 42,4× / 31,7× / 52,9× | 15% | 37% | US$358,22 | US$348,40 | US$226,20 |
| P/E | 27,1× / 23,3× / 32,9× | 5% | 12% | US$496,15 | US$381,17 | US$664,86 |
| P/FCFE | 43,4× / 33,0× / 52,9× | 5% | 12% | US$454,75 | US$406,01 | US$375,84 |
| P/OCF | 20,7× / 17,0× / 24,5× | 5% | 12% | US$428,24 | US$378,99 | US$432,08 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$440,77 | US$391,91 | US$428,49 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$418,23 | US$282,48 | US$486,10 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$560,48 | US$291,27 | US$729,10 |
| EV/EBITDA (total con dividendos) | 20,1× / 19,4× / 21,7× | 10% | 25% | US$761,42 | US$615,13 | US$955,93 |
| EV/FCFF (total con dividendos) | 42,4× / 31,7× / 52,9× | 15% | 37% | US$557,33 | US$487,74 | US$492,13 |
| P/E (total con dividendos) | 27,1× / 23,3× / 32,9× | 5% | 12% | US$698,84 | US$502,03 | US$989,30 |
| P/FCFE (total con dividendos) | 43,4× / 33,0× / 52,9× | 5% | 12% | US$682,60 | US$556,47 | US$699,10 |
| P/OCF (total con dividendos) | 20,7× / 17,0× / 24,5× | 5% | 12% | US$630,59 | US$521,15 | US$712,02 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 40% | 100% | US$650,86 | US$534,14 | US$723,58 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$13,00 | US$13,00 | US$13,00 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$637,86 | US$521,14 | US$710,59 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$596,63 | US$388,42 | US$726,89 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 11,60%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$521,09 | US$538,67 | US$548,82 | US$536,19 | OK |
| EV/EBITDA | Conservador | US$480,56 | US$461,70 | US$443,58 | US$461,95 | OK |
| EV/EBITDA | Optimista | US$583,82 | US$642,22 | US$688,74 | US$638,26 | OK |
| EV/FCFF | Base | US$312,64 | US$360,03 | US$401,99 | US$358,22 | OK |
| EV/FCFF | Conservador | US$346,41 | US$346,85 | US$351,93 | US$348,40 | OK |
| EV/FCFF | Optimista | US$110,14 | US$213,38 | US$355,09 | US$226,20 | OK |
| P/E | Base | US$487,22 | US$497,43 | US$503,79 | US$496,15 | OK |
| P/E | Conservador | US$401,57 | US$379,74 | US$362,21 | US$381,17 | OK |
| P/E | Optimista | US$613,75 | US$668,09 | US$712,75 | US$664,86 | OK |
| P/FCFE | Base | US$416,59 | US$455,54 | US$492,12 | US$454,75 | OK |
| P/FCFE | Conservador | US$414,26 | US$402,38 | US$401,38 | US$406,01 | OK |
| P/FCFE | Optimista | US$258,37 | US$365,16 | US$503,98 | US$375,84 | OK |
| P/OCF | Base | US$399,94 | US$430,08 | US$454,70 | US$428,24 | OK |
| P/OCF | Conservador | US$382,24 | US$378,77 | US$375,96 | US$378,99 | OK |
| P/OCF | Optimista | US$355,71 | US$427,27 | US$513,28 | US$432,08 | OK |

Múltiplos consolidados hoy: US$440,77 / US$391,91 / US$428,49 · DCF de las historias hoy: US$403,20 / US$209,54 / US$524,51 · Ponderado hoy: US$418,23 / US$282,48 / US$486,10 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para MSFT la diferencia es de +9% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$466,38 por acción y los múltiplos, US$466,16 hoy: prácticamente igual al DCF. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$512,90 supone que los ingresos crecen 19,4% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 13,0% (+6,4 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$560,48 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,6%, WACC de los años 4-10 10,6%, ROE de FY+3 42,7% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 20,1x | 14,7x | +36% | 8,7% | 8,0% | +0,7 pp | Revisar: el múltiplo vale 36% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 42,4x | 42,4x | −1% | 8,0% | 8,0% | −0,0 pp | Coherente con el DCF. |
| P/E | 27,1x | 21,6x | +25% | 8,4% | 7,5% | +0,9 pp | Coherente con el DCF. |
| P/FCFE | 43,4x | 35,5x | +22% | 9,1% | 8,5% | +0,5 pp | Coherente con el DCF. |
| P/OCF | 20,7x | 18,3x | +13% | 8,9% | 8,5% | +0,3 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$418,23 | — |
| Múltiplos Base +20% | US$453,01 | +8,3% |
| Múltiplos Base −20% | US$383,45 | −8,3% |
| Crecimiento años 2-5 +2 pp | US$438,40 | +4,8% |
| Crecimiento años 2-5 −2 pp | US$399,78 | −4,4% |
| Margen objetivo +3 pp | US$434,55 | +3,9% |
| Margen objetivo −3 pp | US$401,92 | −3,9% |
| WACC +1 pp | US$404,30 | −3,3% |
| WACC −1 pp | US$433,16 | +3,6% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 19,37 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | — | 20,12 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 21,71 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 31,68 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | — | 42,41 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 52,86 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 23,27 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | — | 27,08 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 32,89 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 33,04 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | — | 43,39 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 52,85 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 17,04 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | — | 20,67 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 24,53 | Múltiplo optimista elegido con el protocolo v3 |
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
