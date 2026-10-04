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

**Valor intrínseco principal · DCF Base hoy: US$32,28 por acción.** Complemento: DCF esperado por probabilidades US$29,28; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$12,74–US$43,36; precio con MOS 35% sobre el esperado: US$19,03; precio de referencia US$35,15. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Reestructuración que devuelve a Nike a crecer poco con margen de 11%** (valor principal) | 45% | US$32,28 | US$14,52 |
| Conservadora · Recuperación a medias, la marca pierde participación | 25% | US$19,24 | US$4,81 |
| Disrupción · Deterioro de los fundamentales: Nike pierde relevancia como Adidas en 2015-2016, pero sin recuperación | 10% | US$12,74 | US$1,27 |
| Optimista · Vuelve la Nike de márgenes históricos | 20% | US$43,36 | US$8,67 |
| **DCF esperado (complemento)** | 100% | **US$29,28** | |

Lectura del 2-oct-2026: el DCF Base de las historias da ~US$33,0 por acción y los múltiplos consolidados ~US$35,5 hoy, ~8% más. Las dos anclas se compensan: la historia de Nike (15-30 veces) refleja la era de crecimiento y los peers cotizan hoy deprimidos (Lululemon y Deckers a 8-11 veces utilidades). El DCF es el valor intrínseco; los múltiplos son precio relativo y confirman que el precio actual (US$35,15) está cerca del valor de la historia Base.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$32,28 | US$27,76 | US$29,57 | US$19,03 | US$41,98 |
| Conservador | US$19,24 | US$22,72 | US$21,33 | US$19,03 | US$28,83 |
| Optimista | US$43,36 | US$34,95 | US$38,31 | US$19,03 | US$56,80 |

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
| DCF por acción hoy | US$19,24 | US$32,28 | US$43,36 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,01, ERP 4,09%, Ke 9,42%, costo de la deuda después de impuestos 4,55%, peso del patrimonio 85,3%, WACC inicial 8,70% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Nike cotizó a 20-42 veces el EBITDA mientras crecía 6-8% al año y ganaba margen con la venta directa (FY2017-FY2024). Desde FY2025 está en reestructuración: ventas −10% en FY2025, planas en FY2026 y con caída de un dígito alto esperada en FY2027, margen operativo de ~8% frente a 12-16% antes. La etapa actual es May '25, May '26 y el LTM. El reembolso de aranceles IEEPA de FY2026 (US$986 millones) compensa en buena parte los aranceles pagados ese mismo año, así que FY2026 y el LTM se conservan. B: calzado y ropa deportiva con datos de yfinance al 2-oct-2026: Adidas, Deckers, On, Lululemon, Crocs y Birkenstock. Se excluye Under Armour (margen operativo negativo; su P/E no existe y su EV/EBITDA no compara). Ajuste −5%: crecimiento a FY+3 menor que la mediana de los peers (Base ~3-4% frente a 6-13% de Adidas, On y Birkenstock), −10%; margen operativo objetivo menor (11% frente a 14-29%), −5%; riesgo propio menor (la marca más grande, calificación A2/A+, caja de US$8.400 millones), +10%. λ = 0,5: la Nike de FY+3 (crecimiento de un dígito bajo-medio y margen ~10%) es distinta de la de la etapa histórica de alto múltiplo, y los peers cotizan hoy a múltiplos deprimidos (Lululemon y Deckers a 8-11 veces utilidades). El justificado (C) usa los supuestos de cada escenario y equilibra las dos anclas.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana May '25, May '26, LTM (etapa actual) = 15,5x | 9,4x (n=6: ADDYY 12,4x, DECK 7,3x, ONON 19,2x, LULU 4,8x, CROX 7,8x, BIRK 11,0x) × 0,95 = 8,9x | 11,4x / 11,6x / 11,9x | **11,8x** | 10,6x | 13,7x | 13,9x / 10,8x / 16,5x |
| EV/FCFF | mediana May '25, May '26, LTM (etapa actual) = 29,5x (EV/FCF × 1,05 = FCF después de intereses ÷ FCFF) | 13,5x (n=6: ADDYY 17,6x, DECK 8,7x, ONON 21,1x, LULU 8,4x, CROX 9,4x, BIRK 19,5x) × 0,95 = 12,8x | 24,9x / 22,7x / 26,9x | **23,0x** | 19,3x | 27,4x | 22,8x / 16,6x / 27,4x |
| P/E | mediana May '25, May '26, LTM (etapa actual) = 22,0x | 13,7x (n=6: ADDYY 18,3x, DECK 11,3x, ONON 21,9x, LULU 7,8x, CROX 10,5x, BIRK 16,1x) × 0,95 = 13,0x | 17,4x / 15,2x / 19,4x | **17,4x** | 14,8x | 20,6x | 17,5x / 13,5x / 20,9x |
| P/FCFE | mediana May '25, May '26, LTM (etapa actual) = 27,6x | 12,6x (n=6: ADDYY 15,5x, DECK 9,6x, ONON 24,0x, LULU 7,7x, CROX 8,0x, BIRK 18,9x) × 0,95 = 11,9x | 22,6x / 20,8x / 24,3x | **21,2x** | 17,8x | 25,3x | 21,1x / 15,3x / 25,2x |
| P/OCF | mediana May '25, May '26, LTM (etapa actual) = 23,9x | 10,7x (n=6: ADDYY 12,3x, DECK 9,0x, ONON 19,6x, LULU 5,3x, CROX 7,4x, BIRK 13,7x) × 0,95 = 10,1x | 20,3x / 17,3x / 22,8x | **18,6x** | 15,3x | 21,1x | 18,7x / 12,5x / 21,0x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 11,8x: promedio de historia y peers 12,2x, acercado 50% al justificado (11,4x); rango de anclas 8,9x–15,5x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 23,0x: promedio de historia y peers 21,1x, acercado 50% al justificado (24,9x); rango de anclas 12,8x–29,5x. Atípicos excluidos de la historia: May '20 (114,7x: > 2,5x la mediana (32.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 17,4x: promedio de historia y peers 17,5x, acercado 50% al justificado (17,4x); rango de anclas 13,0x–22,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 21,2x: promedio de historia y peers 19,8x, acercado 50% al justificado (22,6x); rango de anclas 11,9x–27,6x. Atípicos excluidos de la historia: May '20 (112,2x: > 2,5x la mediana (31.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 18,6x: promedio de historia y peers 17,0x, acercado 50% al justificado (20,3x); rango de anclas 10,1x–23,9x. Atípicos excluidos de la historia: May '20 (63,1x: > 2,5x la mediana (24.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$27,76 frente a US$32,28 del DCF (−14%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$27,76 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,42%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$12,74) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$32,28 por acción.** Complemento: DCF esperado por probabilidades US$29,28. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$32,28 | US$19,24 | US$43,36 |
| EV/EBITDA | 11,8× / 10,6× / 13,7× | 20% | 33% | US$28,57 | US$22,96 | US$37,08 |
| EV/FCFF | 23,0× / 19,3× / 27,4× | 10% | 17% | US$24,80 | US$23,17 | US$27,89 |
| P/E | 17,4× / 14,8× / 20,6× | 20% | 33% | US$28,79 | US$21,86 | US$38,01 |
| P/FCFE | 21,2× / 17,8× / 25,3× | 5% | 8% | US$24,91 | US$21,19 | US$30,97 |
| P/OCF | 18,6× / 15,3× / 21,1× | 5% | 8% | US$29,20 | US$25,87 | US$32,23 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$27,76 | US$22,72 | US$34,95 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$29,57 | US$21,33 | US$38,31 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$42,28 | US$25,20 | US$56,80 |
| EV/EBITDA (total con dividendos) | 11,8× / 10,6× / 13,7× | 20% | 33% | US$41,98 | US$31,83 | US$57,07 |
| EV/FCFF (total con dividendos) | 23,0× / 19,3× / 27,4× | 10% | 17% | US$37,90 | US$29,76 | US$50,83 |
| P/E (total con dividendos) | 17,4× / 14,8× / 20,6× | 20% | 33% | US$42,96 | US$30,69 | US$59,67 |
| P/FCFE (total con dividendos) | 21,2× / 17,8× / 25,3× | 5% | 8% | US$43,21 | US$32,24 | US$59,57 |
| P/OCF (total con dividendos) | 18,6× / 15,3× / 21,1× | 5% | 8% | US$42,53 | US$33,14 | US$53,49 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$41,77 | US$31,25 | US$56,81 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$5,89 | US$5,89 | US$5,89 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$35,89 | US$25,36 | US$50,92 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$41,98 | US$28,83 | US$56,80 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,42%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$23,74 | US$29,51 | US$32,45 | US$28,57 | OK |
| EV/EBITDA | Conservador | US$20,86 | US$23,31 | US$24,71 | US$22,96 | OK |
| EV/EBITDA | Optimista | US$28,42 | US$38,85 | US$43,97 | US$37,08 | OK |
| EV/FCFF | Base | US$20,44 | US$24,61 | US$29,34 | US$24,80 | OK |
| EV/FCFF | Conservador | US$24,28 | US$22,09 | US$23,13 | US$23,17 | OK |
| EV/FCFF | Optimista | US$15,27 | US$29,19 | US$39,21 | US$27,89 | OK |
| P/E | Base | US$23,30 | US$29,87 | US$33,20 | US$28,79 | OK |
| P/E | Conservador | US$19,48 | US$22,25 | US$23,84 | US$21,86 | OK |
| P/E | Optimista | US$28,02 | US$40,06 | US$45,96 | US$38,01 | OK |
| P/FCFE | Base | US$13,58 | US$27,77 | US$33,39 | US$24,91 | OK |
| P/FCFE | Conservador | US$16,14 | US$22,41 | US$25,02 | US$21,19 | OK |
| P/FCFE | Optimista | US$10,94 | US$36,08 | US$45,88 | US$30,97 | OK |
| P/OCF | Base | US$25,67 | US$29,06 | US$32,88 | US$29,20 | OK |
| P/OCF | Conservador | US$26,93 | US$24,98 | US$25,71 | US$25,87 | OK |
| P/OCF | Optimista | US$22,13 | US$33,31 | US$41,25 | US$32,23 | OK |

Múltiplos consolidados hoy: US$27,76 / US$22,72 / US$34,95 · DCF de las historias hoy: US$32,28 / US$19,24 / US$43,36 · Ponderado hoy: US$29,57 / US$21,33 / US$38,31 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NKE la diferencia es de −14% (múltiplos por debajo del DCF). Lectura del 2-oct-2026: el DCF Base de las historias da ~US$33,0 por acción y los múltiplos consolidados ~US$35,5 hoy, ~8% más. Las dos anclas se compensan: la historia de Nike (15-30 veces) refleja la era de crecimiento y los peers cotizan hoy deprimidos (Lululemon y Deckers a 8-11 veces utilidades). El DCF es el valor intrínseco; los múltiplos son precio relativo y confirman que el precio actual (US$35,15) está cerca del valor de la historia Base.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$35,15 supone que los ingresos crecen 2,1% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 1,4% (+0,7 pp). Coherente: el precio supone un crecimiento parecido al del DCF.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$42,28 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,4%, WACC de los años 4-10 9,0%, ROE de FY+3 20,7% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 11,8x | 11,3x | −1% | 4,9% | 4,7% | +0,2 pp | Coherente con el DCF. |
| EV/FCFF | 23,0x | 24,6x | −10% | 4,5% | 4,7% | −0,3 pp | Coherente con el DCF. |
| P/E | 17,4x | 17,1x | +2% | 4,8% | 4,7% | +0,1 pp | Coherente con el DCF. |
| P/FCFE | 21,2x | 20,7x | +2% | 4,5% | 4,4% | +0,1 pp | Coherente con el DCF. |
| P/OCF | 18,6x | 18,5x | +1% | 4,4% | 4,4% | +0,0 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$29,57 | — |
| Múltiplos Base +20% | US$32,59 | +10,2% |
| Múltiplos Base −20% | US$26,54 | −10,2% |
| Crecimiento años 2-5 +2 pp | US$30,46 | +3,0% |
| Crecimiento años 2-5 −2 pp | US$28,76 | −2,7% |
| Margen objetivo +3 pp | US$33,13 | +12,0% |
| Margen objetivo −3 pp | US$26,01 | −12,0% |
| WACC +1 pp | US$28,82 | −2,5% |
| WACC −1 pp | US$30,37 | +2,7% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo −3 pp, Margen objetivo +3 pp, Múltiplos Base +20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 10,79 | 10,64 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 13,92 | 11,80 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 16,46 | 13,73 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 16,63 | 19,31 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 22,75 | 23,03 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 27,45 | 27,35 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 13,46 | 14,76 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 17,48 | 17,45 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 20,90 | 20,65 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 15,30 | 17,83 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 21,12 | 21,19 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 25,16 | 25,26 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 12,54 | 15,34 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 18,70 | 18,63 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 21,03 | 21,07 | Múltiplo optimista elegido con el protocolo v3 |
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
