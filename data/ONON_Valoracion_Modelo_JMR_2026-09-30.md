---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de On Holding AG"
ticker: "ONON"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1nlN8qDy9BipM5IWwGE5Fgf6VKpyYQScLXIPvqtAE9Oo/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# On Holding AG (ONON) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$33,10 por acción.** Complemento: DCF esperado por probabilidades US$30,60; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$12,49–US$46,35; precio con MOS 35% sobre el esperado: US$19,89; precio de referencia US$30,20. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Marca premium global que crece ~15% con margen de 16,5%** (valor principal) | 45% | US$33,10 | US$14,89 |
| Conservadora · El ciclo de moda se enfría | 25% | US$20,72 | US$5,18 |
| Disrupción · Deterioro de los fundamentales: pasa la moda y las ventas caen como en Under Armour | 10% | US$12,49 | US$1,25 |
| Optimista · On se vuelve una marca deportiva global de primera línea | 20% | US$46,35 | US$9,27 |
| **DCF esperado (complemento)** | 100% | **US$30,60** | |

Lectura del 2-oct-2026: el DCF Base de las historias da ~US$33,2 por acción y los múltiplos consolidados ~US$47 hoy, ~40% más, fuera del ±25%. Los múltiplos no se movieron para acercarlos. La diferencia es la ventaja competitiva: el justificado (C) supone que el ROE de FY+3 (~22%) dura para siempre y la historia de On (P/E de 60-96×) refleja la etapa de hipercrecimiento, mientras el DCF lleva el ROIC al costo de capital después del año 10 porque la marca tiene 16 años y no está probada. El DCF es el valor intrínseco; los múltiplos dicen cuánto pagaría el mercado si On sostuviera retornos excedentes como una marca consolidada.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$33,10 | US$29,16 | US$31,52 | US$19,89 | US$44,99 |
| Conservador | US$20,72 | US$21,87 | US$21,18 | US$19,89 | US$28,26 |
| Optimista | US$46,35 | US$38,88 | US$43,37 | US$19,89 | US$64,75 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - ONON (desde cero 2026-10-02)](https://docs.google.com/spreadsheets/d/1nlN8qDy9BipM5IWwGE5Fgf6VKpyYQScLXIPvqtAE9Oo/edit).
- Análisis del 01 de oct de 2026. Precio de referencia de la hoja: US$30,20.
- Peers: datos de mercado de yfinance consultados el 2026-10-02 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 10,9% | 17,5% | 21,5% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 8,7% | 14,0% | 20,6% | Input B29 |
| Margen EBIT objetivo | 13,0% | 16,5% | 20,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,30 / 2,10 | — | Input B32/B33 |
| DCF por acción hoy | US$20,72 | US$33,10 | US$46,35 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,05, ERP 5,02%, Ke 10,58%, costo de la deuda después de impuestos 4,62%, peso del patrimonio 93,6%, WACC inicial 10,20% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: 2021 (pérdida por los pagos en acciones de la salida a bolsa) y 2022 (flujo negativo por inventario) no son comparables. Desde 2023 On es una marca rentable que crece 20-30% al año: la etapa actual es Dec '23, Dec '24, Dec '25 y el LTM, con múltiplos de 24-48× EBITDA que bajan con el precio. B: calzado y ropa deportiva con datos de yfinance al 2-oct-2026: Deckers, Nike, Lululemon, Birkenstock, Adidas y Crocs. Ajuste +25%: crecimiento a FY+3 mucho mayor que la mediana de los peers (Base ~14% frente a −4% a +13%), +25%; margen bruto mayor (65% frente a 45-60%), +5%; riesgo propio mayor (marca joven, beta 1,30), −5%. λ = 0,5: los peers son marcas maduras o en caída y la historia de On refleja múltiplos de la etapa de hipercrecimiento; el justificado (C) usa los supuestos de cada escenario y equilibra ambos.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 27,3x | 9,4x (n=6: DECK 7,3x, NKE 11,0x, LULU 4,8x, BIRK 11,0x, ADDYY 12,4x, CROX 7,8x) × 1,25 = 11,7x | 13,3x / 10,8x / 17,8x | **16,4x** | 13,1x | 20,7x | 25,8x / 20,6x / 31,4x |
| EV/FCFF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,2x (EV/FCF × 0,47 = FCF después de intereses ÷ FCFF) | 13,5x (n=6: DECK 8,7x, NKE 24,8x, LULU 8,4x, BIRK 19,5x, ADDYY 17,6x, CROX 9,4x) × 1,25 = 16,9x | 39,5x / 24,8x / 55,3x | **28,5x** | 19,9x | 37,4x | 34,8x / 26,5x / 44,0x |
| P/E | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 63,2x | 13,7x (n=6: DECK 11,3x, NKE 16,1x, LULU 7,8x, BIRK 16,1x, ADDYY 18,3x, CROX 10,5x) × 1,25 = 17,1x | 22,3x / 14,6x / 30,1x | **31,2x** | 23,4x | 38,2x | 32,4x / 26,0x / 37,7x |
| P/FCFE | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 39,8x | 12,6x (n=6: DECK 9,6x, NKE 23,0x, LULU 7,7x, BIRK 18,9x, ADDYY 15,5x, CROX 8,0x) × 1,25 = 15,7x | 31,1x / 21,1x / 40,2x | **29,4x** | 21,2x | 37,8x | 33,0x / 25,9x / 42,3x |
| P/OCF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 32,9x | 10,7x (n=6: DECK 9,0x, NKE 17,5x, LULU 5,3x, BIRK 13,7x, ADDYY 12,3x, CROX 7,4x) × 1,25 = 13,3x | 29,0x / 17,2x / 40,2x | **26,0x** | 18,8x | 32,2x | 29,7x / 24,1x / 34,6x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 16,4x: promedio de historia y peers 19,5x, acercado 50% al justificado (13,3x); rango de anclas 11,7x–27,3x. Atípicos excluidos de la historia: Dec '21 (-93,8x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 28,5x: promedio de historia y peers 17,5x, acercado 50% al justificado (39,5x); rango de anclas 16,9x–39,5x. Atípicos excluidos de la historia: Dec '21 (-465,0x: métrica negativa o ~0); Dec '22 (-15,8x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 31,2x: promedio de historia y peers 40,1x, acercado 50% al justificado (22,3x); rango de anclas 17,1x–63,2x. Atípicos excluidos de la historia: Dec '21 (-63,0x: métrica negativa o ~0); LTM (20,3x: < 0,4x la mediana (64.4x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 29,4x: promedio de historia y peers 27,7x, acercado 50% al justificado (31,1x); rango de anclas 15,7x–39,8x. Atípicos excluidos de la historia: Dec '21 (-486,5x: métrica negativa o ~0); Dec '22 (-16,5x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 26,0x: promedio de historia y peers 23,1x, acercado 50% al justificado (29,0x); rango de anclas 13,3x–32,9x. Atípicos excluidos de la historia: Dec '22 (-22,4x: métrica negativa o ~0); Dec '21 (764,5x: > 2,5x la mediana (34.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$29,16 frente a US$33,10 del DCF (−12%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$29,16 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Crecimiento»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,58%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$12,49) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$33,10 por acción.** Complemento: DCF esperado por probabilidades US$30,60. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$33,10 | US$20,72 | US$46,35 |
| EV/EBITDA | 16,4× / 13,1× / 20,7× | 10% | 25% | US$44,24 | US$29,69 | US$62,55 |
| EV/FCFF | 28,5× / 19,9× / 37,4× | 15% | 37% | US$22,73 | US$19,67 | US$28,37 |
| P/E | 31,2× / 23,4× / 38,2× | 5% | 12% | US$37,58 | US$22,83 | US$53,32 |
| P/FCFE | 29,4× / 21,2× / 37,8× | 5% | 12% | US$21,12 | US$17,04 | US$27,29 |
| P/OCF | 26,0× / 18,8× / 32,2× | 5% | 12% | US$17,93 | US$16,68 | US$20,25 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$29,16 | US$21,87 | US$38,88 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$31,52 | US$21,18 | US$43,37 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$44,76 | US$28,02 | US$62,68 |
| EV/EBITDA | 16,4× / 13,1× / 20,7× | 10% | 25% | US$64,14 | US$38,51 | US$97,10 |
| EV/FCFF | 28,5× / 19,9× / 37,4× | 15% | 37% | US$38,56 | US$26,28 | US$57,59 |
| P/E | 31,2× / 23,4× / 38,2× | 5% | 12% | US$55,37 | US$29,59 | US$84,83 |
| P/FCFE | 29,4× / 21,2× / 37,8× | 5% | 12% | US$32,52 | US$20,76 | US$49,15 |
| P/OCF | 26,0× / 18,8× / 32,2× | 5% | 12% | US$30,93 | US$22,66 | US$41,87 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 40% | 100% | US$45,35 | US$28,61 | US$67,85 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$44,99 | US$28,26 | US$64,75 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,58%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$40,40 | US$44,90 | US$47,44 | US$44,24 | OK |
| EV/EBITDA | Conservador | US$30,83 | US$29,76 | US$28,48 | US$29,69 | OK |
| EV/EBITDA | Optimista | US$51,91 | US$63,92 | US$71,81 | US$62,55 | OK |
| EV/FCFF | Base | US$16,64 | US$23,02 | US$28,52 | US$22,73 | OK |
| EV/FCFF | Conservador | US$20,05 | US$19,54 | US$19,43 | US$19,67 | OK |
| EV/FCFF | Optimista | US$13,19 | US$29,35 | US$42,59 | US$28,37 | OK |
| P/E | Base | US$33,69 | US$38,09 | US$40,95 | US$37,58 | OK |
| P/E | Conservador | US$23,84 | US$22,76 | US$21,88 | US$22,83 | OK |
| P/E | Optimista | US$42,67 | US$54,54 | US$62,74 | US$53,32 | OK |
| P/FCFE | Base | US$19,76 | US$19,55 | US$24,05 | US$21,12 | OK |
| P/FCFE | Conservador | US$20,38 | US$15,37 | US$15,36 | US$17,04 | OK |
| P/FCFE | Optimista | US$19,71 | US$25,81 | US$36,35 | US$27,29 | OK |
| P/OCF | Base | US$12,82 | US$18,10 | US$22,87 | US$17,93 | OK |
| P/OCF | Conservador | US$16,70 | US$16,60 | US$16,76 | US$16,68 | OK |
| P/OCF | Optimista | US$8,99 | US$20,80 | US$30,96 | US$20,25 | OK |

Múltiplos consolidados hoy: US$29,16 / US$21,87 / US$38,88 · DCF de las historias hoy: US$33,10 / US$20,72 / US$46,35 · Ponderado hoy: US$31,52 / US$21,18 / US$43,37 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para ONON la diferencia es de −12% (múltiplos por debajo del DCF). Lectura del 2-oct-2026: el DCF Base de las historias da ~US$33,2 por acción y los múltiplos consolidados ~US$47 hoy, ~40% más, fuera del ±25%. Los múltiplos no se movieron para acercarlos. La diferencia es la ventaja competitiva: el justificado (C) supone que el ROE de FY+3 (~22%) dura para siempre y la historia de On (P/E de 60-96×) refleja la etapa de hipercrecimiento, mientras el DCF lleva el ROIC al costo de capital después del año 10 porque la marca tiene 16 años y no está probada. El DCF es el valor intrínseco; los múltiplos dicen cuánto pagaría el mercado si On sostuviera retornos excedentes como una marca consolidada.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$30,20 supone que los ingresos crecen 14,6% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 14,7% (−0,1 pp). Coherente: el precio supone un crecimiento parecido al del DCF.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$44,76 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,6%, WACC de los años 4-10 9,8%, ROE de FY+3 25,1% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 16,4x | 11,3x | +43% | 7,6% | 6,7% | +1,0 pp | Revisar: el múltiplo vale 43% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 28,5x | 33,4x | −14% | 6,1% | 6,7% | −0,5 pp | Coherente con el DCF. |
| P/E | 31,2x | 25,2x | +24% | 8,2% | 7,6% | +0,6 pp | Coherente con el DCF. |
| P/FCFE | 29,4x | 40,5x | −27% | 6,9% | 7,9% | −1,0 pp | Revisar: el múltiplo vale 27% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 26,0x | 37,7x | −31% | 6,8% | 7,9% | −1,2 pp | Revisar: el múltiplo vale 31% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$31,52 | — |
| Múltiplos Base +20% | US$33,76 | +7,1% |
| Múltiplos Base −20% | US$29,29 | −7,1% |
| Crecimiento años 2-5 +2 pp | US$32,94 | +4,5% |
| Crecimiento años 2-5 −2 pp | US$30,23 | −4,1% |
| Margen objetivo +3 pp | US$35,39 | +12,3% |
| Margen objetivo −3 pp | US$27,66 | −12,3% |
| WACC +1 pp | US$30,46 | −3,4% |
| WACC −1 pp | US$32,66 | +3,6% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Margen objetivo −3 pp, Múltiplos Base +20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 20,56 | 13,05 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 25,79 | 16,43 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 31,45 | 20,67 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 26,49 | 19,85 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 34,76 | 28,53 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 44,02 | 37,38 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 26,04 | 23,41 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 32,37 | 31,23 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 37,69 | 38,25 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 25,89 | 21,19 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 32,99 | 29,44 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 42,29 | 37,80 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 24,08 | 18,82 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 29,73 | 26,03 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 34,57 | 32,20 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/ONON_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1nlN8qDy9BipM5IWwGE5Fgf6VKpyYQScLXIPvqtAE9Oo/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-10-02 (DECK, NKE, LULU, BIRK, ADDYY, CROX).
- [On, comunicado del 2T26, 11-ago-2026](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm)
- [On, Investor Day 2026, 22-sep-2026](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000021/exhibit991oninvestorday202.htm)

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
