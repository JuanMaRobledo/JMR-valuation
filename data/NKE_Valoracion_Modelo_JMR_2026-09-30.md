---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de NIKE, Inc."
ticker: "NKE"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1OITWNynG7R3PKC1sITOOazW9jzXgFWFda6qNbbOnYZI/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# NIKE, Inc. (NKE) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$30,62 por acción.** Complemento: DCF esperado por probabilidades US$27,79; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$12,16–US$41,11; precio con MOS 35% sobre el esperado: US$18,06; precio de referencia US$35,15. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Reestructuración que devuelve a Nike a crecer poco con margen de 11%** (valor principal) | 45% | US$30,62 | US$13,78 |
| Conservadora · Recuperación a medias, la marca pierde participación | 25% | US$18,29 | US$4,57 |
| Disrupción · Deterioro de los fundamentales: Nike pierde relevancia como Adidas en 2015-2016, pero sin recuperación | 10% | US$12,16 | US$1,22 |
| Optimista · Vuelve la Nike de márgenes históricos | 20% | US$41,11 | US$8,22 |
| **DCF esperado (complemento)** | 100% | **US$27,79** | |

Lectura del 2-oct-2026: el DCF Base de las historias da ~US$33,0 por acción y los múltiplos consolidados ~US$35,5 hoy, ~8% más. Las dos anclas se compensan: la historia de Nike (15-30 veces) refleja la era de crecimiento y los peers cotizan hoy deprimidos (Lululemon y Deckers a 8-11 veces utilidades). El DCF es el valor intrínseco; los múltiplos son precio relativo y confirman que el precio actual (US$35,15) está cerca del valor de la historia Base.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$30,62 | US$25,45 | US$27,52 | US$18,06 | US$39,96 |
| Conservador | US$18,29 | US$20,96 | US$19,89 | US$18,06 | US$27,52 |
| Optimista | US$41,11 | US$31,88 | US$35,57 | US$18,06 | US$53,88 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - NKE (desde cero 2026-10-02)](https://docs.google.com/spreadsheets/d/1OITWNynG7R3PKC1sITOOazW9jzXgFWFda6qNbbOnYZI/edit).
- Análisis del 01 de oct de 2026. Precio de referencia de la hoja: US$35,15.
- Peers: datos de mercado de yfinance consultados el 2026-10-02 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -9,1% | -6,6% | -3,9% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | -0,8% | 3,4% | 5,1% | Input B29 |
| Margen EBIT objetivo | 9,1% | 11,6% | 14,1% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 6 | 6 | 6 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,10 / 2,10 | — | Input B32/B33 |
| DCF por acción hoy | US$18,29 | US$30,62 | US$41,11 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,01, ERP 5,10%, Ke 10,44%, costo de la deuda después de impuestos 4,55%, peso del patrimonio 85,3%, WACC inicial 9,57% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Nike cotizó a 20-42 veces el EBITDA mientras crecía 6-8% al año y ganaba margen con la venta directa (FY2017-FY2024). Desde FY2025 está en reestructuración: ventas −10% en FY2025, planas en FY2026 y con caída de un dígito alto esperada en FY2027, margen operativo de ~8% frente a 12-16% antes. La etapa actual es May '25, May '26 y el LTM. El reembolso de aranceles IEEPA de FY2026 (US$986 millones) compensa en buena parte los aranceles pagados ese mismo año, así que FY2026 y el LTM se conservan. B: calzado y ropa deportiva con datos de yfinance al 2-oct-2026: Adidas, Deckers, On, Lululemon, Crocs y Birkenstock. Se excluye Under Armour (margen operativo negativo; su P/E no existe y su EV/EBITDA no compara). Ajuste −5%: crecimiento a FY+3 menor que la mediana de los peers (Base ~3-4% frente a 6-13% de Adidas, On y Birkenstock), −10%; margen operativo objetivo menor (11% frente a 14-29%), −5%; riesgo propio menor (la marca más grande, calificación A2/A+, caja de US$8.400 millones), +10%. λ = 0,5: la Nike de FY+3 (crecimiento de un dígito bajo-medio y margen ~10%) es distinta de la de la etapa histórica de alto múltiplo, y los peers cotizan hoy a múltiplos deprimidos (Lululemon y Deckers a 8-11 veces utilidades). El justificado (C) usa los supuestos de cada escenario y equilibra las dos anclas.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana May '25, May '26, LTM (etapa actual) = 15,5x | 9,4x (n=6: ADDYY 12,4x, DECK 7,3x, ONON 19,2x, LULU 4,8x, CROX 7,8x, BIRK 11,0x) × 0,95 = 8,9x | 10,2x / 10,5x / 10,6x | **11,2x** | 10,1x | 13,0x | 13,9x / 10,8x / 16,5x |
| EV/FCFF | mediana May '25, May '26, LTM (etapa actual) = 29,5x (EV/FCF × 1,05 = FCF después de intereses ÷ FCFF) | 13,5x (n=6: ADDYY 17,6x, DECK 8,7x, ONON 21,1x, LULU 8,4x, CROX 9,4x, BIRK 19,5x) × 0,95 = 12,8x | 22,3x / 20,5x / 23,9x | **21,7x** | 18,3x | 25,7x | 22,8x / 16,6x / 27,4x |
| P/E | mediana May '25, May '26, LTM (etapa actual) = 22,0x | 13,7x (n=6: ADDYY 18,3x, DECK 11,3x, ONON 21,9x, LULU 7,8x, CROX 10,5x, BIRK 16,1x) × 0,95 = 13,0x | 14,3x / 12,7x / 15,7x | **15,9x** | 13,5x | 18,7x | 17,5x / 13,5x / 20,9x |
| P/FCFE | mediana May '25, May '26, LTM (etapa actual) = 27,6x | 12,6x (n=6: ADDYY 15,5x, DECK 9,6x, ONON 24,0x, LULU 7,7x, CROX 8,0x, BIRK 18,9x) × 0,95 = 11,9x | 18,6x / 17,3x / 19,6x | **19,1x** | 16,2x | 22,8x | 21,1x / 15,3x / 25,2x |
| P/OCF | mediana May '25, May '26, LTM (etapa actual) = 23,9x | 10,7x (n=6: ADDYY 12,3x, DECK 9,0x, ONON 19,6x, LULU 5,3x, CROX 7,4x, BIRK 13,7x) × 0,95 = 10,1x | 16,6x / 14,4x / 18,5x | **16,8x** | 13,9x | 18,9x | 18,7x / 12,5x / 21,0x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 11,2x: promedio de historia y peers 12,2x, acercado 50% al justificado (10,2x); rango de anclas 8,9x–15,5x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 21,7x: promedio de historia y peers 21,1x, acercado 50% al justificado (22,3x); rango de anclas 12,8x–29,5x. Atípicos excluidos de la historia: May '20 (114,7x: > 2,5x la mediana (32.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 15,9x: promedio de historia y peers 17,5x, acercado 50% al justificado (14,3x); rango de anclas 13,0x–22,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 19,1x: promedio de historia y peers 19,8x, acercado 50% al justificado (18,6x); rango de anclas 11,9x–27,6x. Atípicos excluidos de la historia: May '20 (112,2x: > 2,5x la mediana (31.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 16,8x: promedio de historia y peers 17,0x, acercado 50% al justificado (16,6x); rango de anclas 10,1x–23,9x. Atípicos excluidos de la historia: May '20 (63,1x: > 2,5x la mediana (24.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$25,45 frente a US$30,62 del DCF (−17%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$25,45 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,44%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$12,16) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$30,62 por acción.** Complemento: DCF esperado por probabilidades US$27,79. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$30,62 | US$18,29 | US$41,11 |
| EV/EBITDA | 11,2× / 10,1× / 13,0× | 20% | 33% | US$26,70 | US$21,55 | US$34,53 |
| EV/FCFF | 21,7× / 18,3× / 25,7× | 10% | 17% | US$23,05 | US$21,62 | US$25,81 |
| P/E | 15,9× / 13,5× / 18,7× | 20% | 33% | US$26,00 | US$19,91 | US$34,11 |
| P/FCFE | 19,1× / 16,2× / 22,8× | 5% | 8% | US$22,37 | US$19,18 | US$27,62 |
| P/OCF | 16,8× / 13,9× / 18,9× | 5% | 8% | US$26,16 | US$23,34 | US$28,70 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$25,45 | US$20,96 | US$31,88 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$27,52 | US$19,89 | US$35,57 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$41,24 | US$24,63 | US$55,37 |
| EV/EBITDA (total con dividendos) | 11,2× / 10,1× / 13,0× | 20% | 33% | US$40,05 | US$30,50 | US$54,25 |
| EV/FCFF (total con dividendos) | 21,7× / 18,3× / 25,7× | 10% | 17% | US$35,98 | US$28,37 | US$48,07 |
| P/E (total con dividendos) | 15,9× / 13,5× / 18,7× | 20% | 33% | US$39,62 | US$28,58 | US$54,67 |
| P/FCFE (total con dividendos) | 19,1× / 16,2× / 22,8× | 5% | 8% | US$39,62 | US$29,82 | US$54,23 |
| P/OCF (total con dividendos) | 16,8× / 13,9× / 18,9× | 5% | 8% | US$38,93 | US$30,58 | US$48,64 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$39,10 | US$29,45 | US$52,89 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$5,89 | US$5,89 | US$5,89 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$33,21 | US$23,57 | US$47,00 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$39,96 | US$27,52 | US$53,88 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,44%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$22,33 | US$27,60 | US$30,18 | US$26,70 | OK |
| EV/EBITDA | Conservador | US$19,68 | US$21,88 | US$23,09 | US$21,55 | OK |
| EV/EBITDA | Optimista | US$26,66 | US$36,22 | US$40,72 | US$34,53 | OK |
| EV/FCFF | Base | US$19,10 | US$22,90 | US$27,16 | US$23,05 | OK |
| EV/FCFF | Conservador | US$22,75 | US$20,62 | US$21,51 | US$21,62 | OK |
| EV/FCFF | Optimista | US$14,23 | US$27,08 | US$36,13 | US$25,81 | OK |
| P/E | Base | US$21,15 | US$26,99 | US$29,86 | US$26,00 | OK |
| P/E | Conservador | US$17,79 | US$20,27 | US$21,66 | US$19,91 | OK |
| P/E | Optimista | US$25,33 | US$35,98 | US$41,03 | US$34,11 | OK |
| P/FCFE | Base | US$12,31 | US$24,95 | US$29,85 | US$22,37 | OK |
| P/FCFE | Conservador | US$14,66 | US$20,28 | US$22,58 | US$19,18 | OK |
| P/FCFE | Optimista | US$9,92 | US$32,23 | US$40,71 | US$27,62 | OK |
| P/OCF | Base | US$23,09 | US$26,05 | US$29,35 | US$26,16 | OK |
| P/OCF | Conservador | US$24,33 | US$22,53 | US$23,15 | US$23,34 | OK |
| P/OCF | Optimista | US$19,86 | US$29,70 | US$36,55 | US$28,70 | OK |

Múltiplos consolidados hoy: US$25,45 / US$20,96 / US$31,88 · DCF de las historias hoy: US$30,62 / US$18,29 / US$41,11 · Ponderado hoy: US$27,52 / US$19,89 / US$35,57 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NKE la diferencia es de −17% (múltiplos por debajo del DCF). Lectura del 2-oct-2026: el DCF Base de las historias da ~US$33,0 por acción y los múltiplos consolidados ~US$35,5 hoy, ~8% más. Las dos anclas se compensan: la historia de Nike (15-30 veces) refleja la era de crecimiento y los peers cotizan hoy deprimidos (Lululemon y Deckers a 8-11 veces utilidades). El DCF es el valor intrínseco; los múltiplos son precio relativo y confirman que el precio actual (US$35,15) está cerca del valor de la historia Base.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$35,15 supone que los ingresos crecen 3,4% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 1,4% (+1,9 pp). Coherente: el precio supone un crecimiento parecido al del DCF.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$41,24 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,4%, WACC de los años 4-10 9,5%, ROE de FY+3 20,7% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 11,2x | 10,9x | −3% | 5,2% | 5,1% | +0,1 pp | Coherente con el DCF. |
| EV/FCFF | 21,7x | 23,9x | −13% | 4,7% | 5,1% | −0,4 pp | Coherente con el DCF. |
| P/E | 15,9x | 16,6x | −4% | 5,6% | 5,9% | −0,3 pp | Coherente con el DCF. |
| P/FCFE | 19,1x | 20,1x | −4% | 5,0% | 5,2% | −0,2 pp | Coherente con el DCF. |
| P/OCF | 16,8x | 18,0x | −6% | 4,8% | 5,2% | −0,3 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$27,52 | — |
| Múltiplos Base +20% | US$30,27 | +10,0% |
| Múltiplos Base −20% | US$24,77 | −10,0% |
| Crecimiento años 2-5 +2 pp | US$28,35 | +3,0% |
| Crecimiento años 2-5 −2 pp | US$26,77 | −2,7% |
| Margen objetivo +3 pp | US$30,90 | +12,3% |
| Margen objetivo −3 pp | US$24,14 | −12,3% |
| WACC +1 pp | US$26,81 | −2,6% |
| WACC −1 pp | US$28,28 | +2,8% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Margen objetivo −3 pp, Múltiplos Base +20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 10,79 | 10,13 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 13,92 | 11,20 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 16,46 | 13,00 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 16,63 | 18,26 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 22,75 | 21,72 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 27,45 | 25,73 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 13,46 | 13,50 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 17,48 | 15,88 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 20,90 | 18,73 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 15,30 | 16,19 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 21,12 | 19,15 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 25,16 | 22,75 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 12,54 | 13,90 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 18,70 | 16,80 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 21,03 | 18,92 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/NKE_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1OITWNynG7R3PKC1sITOOazW9jzXgFWFda6qNbbOnYZI/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-10-02 (ADDYY, DECK, ONON, LULU, CROX, BIRK, UAA).
- [NIKE, comunicado del 1T FY2027, 1-oct-2026](https://www.sec.gov/Archives/edgar/data/0000320187/000032018726000184/q1fy27exhibit991er.htm)
- [NIKE, 10-K FY2026, 15-jul-2026](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm)

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
