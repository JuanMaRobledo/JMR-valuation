---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de CHIPOTLE MEXICAN GRILL INC"
ticker: "CMG"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1VUVN1cCm3Hj8bLrmsCZFYBCDIq3DncxHGHH_jbW8ZtU/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# CHIPOTLE MEXICAN GRILL INC (CMG) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$23,05 por acción.** Complemento: DCF esperado por probabilidades US$22,05; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$8,91–US$30,76; precio con MOS 35% sobre el esperado: US$14,33; precio de referencia US$32,36. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Crece por aperturas con comparables bajas** (valor principal) | 40% | US$23,05 | US$9,22 |
| Conservadora · Tráfico débil y margen presionado | 35% | US$17,82 | US$6,24 |
| Disrupción · Deterioro de los fundamentales: Crisis de marca o saturación: el tráfico cae | 5% | US$8,91 | US$0,45 |
| Optimista · Vuelve el tráfico | 20% | US$30,76 | US$6,15 |
| **DCF esperado (complemento)** | 100% | **US$22,05** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$28,19 por acción y los múltiplos, US$26,54 hoy: 6% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$23,05 | US$23,52 | US$23,24 | US$14,33 | US$31,04 |
| Conservador | US$17,82 | US$20,96 | US$19,08 | US$14,33 | US$24,64 |
| Optimista | US$30,76 | US$26,68 | US$29,12 | US$14,33 | US$39,94 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - CMG](https://docs.google.com/spreadsheets/d/1VUVN1cCm3Hj8bLrmsCZFYBCDIq3DncxHGHH_jbW8ZtU/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$32,36.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 6,0% | 8,0% | 11,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 5,0% | 8,0% | 11,0% | Input B29 |
| Margen EBIT objetivo | 15,3% | 18,3% | 19,3% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,51 / 1,51 | — | Input B32/B33 |
| DCF por acción hoy | US$17,82 | US$23,05 | US$30,76 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,10, ERP 4,46%, Ke 9,90%, costo de la deuda después de impuestos 4,35%, peso del patrimonio 89,0%, WACC inicial 9,29% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Chipotle cotizó a 40-110x utilidades mientras abría tiendas y crecía en ventas comparables de dos dígitos; en 2025-2026 las ventas comparables se estancaron y la acción cayó de ~US$43 a ~US$32. La etapa actual es FY25 y el LTM. B: restaurantes de servicio rápido y casual (McDonald's, Texas Roadhouse, Yum!, Wingstop), datos de yfinance al 29-sep-2026. Se excluyen Cava (crece 31% con margen de 8%, P/E 95x) y Starbucks (reestructuración, P/E 55x distorsionado). Ajuste +10%: Chipotle todavía abre ~8-10% de tiendas nuevas al año con retornos por tienda altos y sin deuda financiera, más crecimiento que McDonald's y Yum!. λ = 0,25: la Chipotle de FY+3 del escenario Base sigue siendo una cadena en expansión de unidades, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 21,8x | 16,2x (n=4: MCD 14,7x, TXRH 16,0x, YUM 16,4x, WING 16,7x) × 1,10 = 17,9x | 14,8x / 11,3x / 20,4x | **18,6x** | 16,7x | 21,2x | 18,6x / 16,7x / 21,2x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 34,4x (EV/FCF × 1,05 = FCF después de intereses ÷ FCFF) | 24,5x (n=4: MCD 24,2x, TXRH 28,2x, YUM 24,2x, WING 24,7x) × 1,10 = 26,9x | 28,9x / 23,2x / 38,0x | **30,2x** | 27,4x | 34,6x | 31,5x / 28,4x / 36,0x |
| P/E | mediana Dec '25, LTM (etapa actual) = 31,0x | 22,1x (n=4: MCD 19,0x, TXRH 25,2x, YUM 17,3x, WING 25,7x) × 1,10 = 24,3x | 23,9x / 19,5x / 30,7x | **26,7x** | 23,4x | 30,8x | 26,7x / 23,4x / 30,8x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 29,8x | 22,7x (n=4: MCD 21,3x, TXRH 25,8x, YUM 22,4x, WING 23,0x) × 1,10 = 25,0x | 26,2x / 21,4x / 33,5x | **27,1x** | 24,5x | 30,7x | 27,1x / 24,5x / 30,7x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 20,3x | 15,1x (n=4: MCD 14,6x, TXRH 12,8x, YUM 18,0x, WING 15,6x) × 1,10 = 16,6x | 17,1x / 13,3x / 22,8x | **18,1x** | 15,9x | 21,1x | 18,1x / 15,9x / 21,1x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 18,6x: promedio de historia y peers 19,8x, acercado 25% al justificado (14,8x); rango de anclas 14,8x–21,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 30,2x: promedio de historia y peers 30,7x, acercado 25% al justificado (28,9x); rango de anclas 26,9x–34,4x. Atípicos excluidos de la historia: Dec '20 (143,7x: > 2,5x la mediana (54.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 26,7x: promedio de historia y peers 27,7x, acercado 25% al justificado (23,9x); rango de anclas 23,9x–31,0x. Atípicos excluidos de la historia: Dec '16 (377,5x: > 2,5x la mediana (54.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 27,1x: promedio de historia y peers 27,4x, acercado 25% al justificado (26,2x); rango de anclas 25,0x–29,8x. Atípicos excluidos de la historia: Dec '20 (135,6x: > 2,5x la mediana (51.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 18,1x: promedio de historia y peers 18,4x, acercado 25% al justificado (17,1x); rango de anclas 16,6x–20,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$23,52 frente a US$23,05 del DCF (+2%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$23,52 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Crecimiento»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,90%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$8,91) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$23,05 por acción.** Complemento: DCF esperado por probabilidades US$22,05. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$23,05 | US$17,82 | US$30,76 |
| EV/EBITDA | 18,6× / 16,7× / 21,2× | 10% | 25% | US$29,93 | US$24,40 | US$38,04 |
| EV/FCFF | 30,2× / 27,4× / 34,6× | 15% | 38% | US$18,25 | US$17,99 | US$17,82 |
| P/E | 26,7× / 23,4× / 30,8× | 5% | 13% | US$31,31 | US$25,28 | US$39,63 |
| P/FCFE | 27,1× / 24,5× / 30,7× | 5% | 13% | US$20,00 | US$19,51 | US$19,76 |
| P/OCF | 18,1× / 15,9× / 21,1× | 5% | 13% | US$22,26 | US$20,11 | US$24,48 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$23,52 | US$20,96 | US$26,68 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$23,24 | US$19,08 | US$29,12 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$30,59 | US$23,65 | US$40,82 |
| EV/EBITDA | 18,6× / 16,7× / 21,2× | 10% | 25% | US$39,61 | US$30,59 | US$53,13 |
| EV/FCFF | 30,2× / 27,4× / 34,6× | 15% | 38% | US$25,40 | US$22,34 | US$27,66 |
| P/E | 26,7× / 23,4× / 30,8× | 5% | 13% | US$41,24 | US$31,49 | US$55,24 |
| P/FCFE | 27,1× / 24,5× / 30,7× | 5% | 13% | US$27,30 | US$24,14 | US$29,60 |
| P/OCF | 18,1× / 15,9× / 21,1× | 5% | 13% | US$29,77 | US$25,10 | US$34,86 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 40% | 100% | US$31,72 | US$26,11 | US$38,62 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$31,04 | US$24,64 | US$39,94 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,90%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$29,84 | US$30,11 | US$29,84 | US$29,93 | OK |
| EV/EBITDA | Conservador | US$25,92 | US$24,25 | US$23,05 | US$24,40 | OK |
| EV/EBITDA | Optimista | US$35,56 | US$38,51 | US$40,03 | US$38,04 | OK |
| EV/FCFF | Base | US$16,54 | US$19,07 | US$19,14 | US$18,25 | OK |
| EV/FCFF | Conservador | US$19,28 | US$17,84 | US$16,83 | US$17,99 | OK |
| EV/FCFF | Optimista | US$13,53 | US$19,10 | US$20,84 | US$17,82 | OK |
| P/E | Base | US$31,32 | US$31,54 | US$31,07 | US$31,31 | OK |
| P/E | Conservador | US$26,98 | US$25,15 | US$23,72 | US$25,28 | OK |
| P/E | Optimista | US$37,07 | US$40,20 | US$41,62 | US$39,63 | OK |
| P/FCFE | Base | US$18,70 | US$20,74 | US$20,57 | US$20,00 | OK |
| P/FCFE | Conservador | US$20,96 | US$19,37 | US$18,19 | US$19,51 | OK |
| P/FCFE | Optimista | US$16,07 | US$20,90 | US$22,30 | US$19,76 | OK |
| P/OCF | Base | US$21,57 | US$22,78 | US$22,43 | US$22,26 | OK |
| P/OCF | Conservador | US$21,39 | US$20,01 | US$18,91 | US$20,11 | OK |
| P/OCF | Optimista | US$21,87 | US$25,29 | US$26,26 | US$24,48 | OK |

Múltiplos consolidados hoy: US$23,52 / US$20,96 / US$26,68 · DCF de las historias hoy: US$23,05 / US$17,82 / US$30,76 · Ponderado hoy: US$23,24 / US$19,08 / US$29,12 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para CMG la diferencia es de +2% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$28,19 por acción y los múltiplos, US$26,54 hoy: 6% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$32,36 supone que los ingresos crecen 14,5% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 7,2% (+7,3 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$30,59 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,9%, WACC de los años 4-10 9,5%, ROE de FY+3 68,0% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 18,6x | 13,0x | +29% | 6,6% | 5,4% | +1,2 pp | Revisar: el múltiplo vale 29% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 30,2x | 31,7x | −17% | 6,0% | 6,2% | −0,2 pp | Coherente con el DCF. |
| P/E | 26,7x | 19,8x | +35% | 6,3% | 5,0% | +1,3 pp | Revisar: el múltiplo vale 35% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 27,1x | 30,3x | −11% | 6,0% | 6,4% | −0,4 pp | Coherente con el DCF. |
| P/OCF | 18,1x | 18,6x | −3% | 6,1% | 6,2% | −0,1 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$23,24 | — |
| Múltiplos Base +20% | US$25,25 | +8,7% |
| Múltiplos Base −20% | US$21,22 | −8,7% |
| Crecimiento años 2-5 +2 pp | US$24,46 | +5,2% |
| Crecimiento años 2-5 −2 pp | US$22,12 | −4,8% |
| Margen objetivo +3 pp | US$26,12 | +12,4% |
| Margen objetivo −3 pp | US$20,36 | −12,4% |
| WACC +1 pp | US$22,34 | −3,9% |
| WACC −1 pp | US$24,20 | +4,1% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Margen objetivo −3 pp, Múltiplos Base +20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 16,67 | 16,67 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 18,59 | 18,59 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 21,25 | 21,25 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 28,41 | 27,44 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 31,54 | 30,23 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 35,97 | 34,59 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 23,45 | 23,45 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 26,72 | 26,72 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 30,77 | 30,77 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 24,52 | 24,52 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 27,08 | 27,08 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 30,68 | 30,68 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 15,89 | 15,89 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 18,11 | 18,11 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 21,06 | 21,06 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/CMG_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1VUVN1cCm3Hj8bLrmsCZFYBCDIq3DncxHGHH_jbW8ZtU/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (MCD, CAVA, TXRH, YUM, WING, SBUX).

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
