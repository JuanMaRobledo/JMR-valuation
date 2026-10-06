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

**Valor intrínseco principal · DCF Base hoy: US$26,38 por acción.** Complemento: DCF esperado por probabilidades US$25,22; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$9,61–US$35,29; precio con MOS 35% sobre el esperado: US$16,39; precio de referencia US$30,79. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Crece por aperturas con comparables bajas** (valor principal) | 40% | US$26,38 | US$10,55 |
| Conservadora · Tráfico débil y margen presionado | 35% | US$20,37 | US$7,13 |
| Disrupción · Deterioro de los fundamentales: Crisis de marca o saturación: el tráfico cae | 5% | US$9,61 | US$0,48 |
| Optimista · Vuelve el tráfico | 20% | US$35,29 | US$7,06 |
| **DCF esperado (complemento)** | 100% | **US$25,22** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$28,19 por acción y los múltiplos, US$26,54 hoy: 6% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$26,38 | US$29,30 | US$28,13 | US$16,39 | US$36,29 |
| Conservador | US$20,37 | US$25,53 | US$23,47 | US$16,39 | US$29,03 |
| Optimista | US$35,29 | US$35,41 | US$35,36 | US$16,39 | US$47,34 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - CMG](https://docs.google.com/spreadsheets/d/1VUVN1cCm3Hj8bLrmsCZFYBCDIq3DncxHGHH_jbW8ZtU/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$30,79.
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
| DCF por acción hoy | US$20,37 | US$26,38 | US$35,29 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 0,86, ERP 3,70%, Ke 8,47%, costo de la deuda después de impuestos 4,58%, peso del patrimonio 88,4%, WACC inicial 8,02% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Chipotle cotizó a 40-110x utilidades mientras abría tiendas y crecía en ventas comparables de dos dígitos; en 2025-2026 las ventas comparables se estancaron y la acción cayó de ~US$43 a ~US$32. La etapa actual es FY25 y el LTM. B: restaurantes de servicio rápido y casual (McDonald's, Texas Roadhouse, Yum!, Wingstop), datos de yfinance al 29-sep-2026. Se excluyen Cava (crece 31% con margen de 8%, P/E 95x) y Starbucks (reestructuración, P/E 55x distorsionado). Ajuste +10%: Chipotle todavía abre ~8-10% de tiendas nuevas al año con retornos por tienda altos y sin deuda financiera, más crecimiento que McDonald's y Yum!. λ = 0,25: la Chipotle de FY+3 del escenario Base sigue siendo una cadena en expansión de unidades, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 21,8x | 16,2x (n=4: MCD 14,7x, TXRH 16,0x, YUM 16,4x, WING 16,7x) × 1,10 = 17,9x | 15,1x / 14,0x / 17,8x | **18,7x** | 17,8x | 20,1x | 18,6x / 16,7x / 21,2x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 34,4x (EV/FCF × 1,05 = FCF después de intereses ÷ FCFF) | 24,5x (n=4: MCD 24,2x, TXRH 28,2x, YUM 24,2x, WING 24,7x) × 1,10 = 26,9x | 36,7x / 30,5x / 52,8x | **32,2x** | 29,5x | 38,1x | 31,5x / 28,4x / 36,0x |
| P/E | mediana Dec '25, LTM (etapa actual) = 31,0x | 22,1x (n=4: MCD 19,0x, TXRH 25,2x, YUM 17,3x, WING 25,7x) × 1,10 = 24,3x | 34,1x / 28,3x / 48,8x | **29,3x** | 25,8x | 35,1x | 26,7x / 23,4x / 30,8x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 29,8x | 22,7x (n=4: MCD 21,3x, TXRH 25,8x, YUM 22,4x, WING 23,0x) × 1,10 = 25,0x | 36,3x / 30,2x / 51,9x | **29,6x** | 26,9x | 35,0x | 27,1x / 24,5x / 30,7x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 20,3x | 15,1x (n=4: MCD 14,6x, TXRH 12,8x, YUM 18,0x, WING 15,6x) × 1,10 = 16,6x | 22,3x / 18,8x / 30,3x | **19,4x** | 17,5x | 22,7x | 18,1x / 15,9x / 21,1x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 18,7x: promedio de historia y peers 19,8x, acercado 25% al justificado (15,1x); rango de anclas 15,1x–21,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 32,2x: promedio de historia y peers 30,7x, acercado 25% al justificado (36,7x); rango de anclas 26,9x–36,7x. Atípicos excluidos de la historia: Dec '20 (143,7x: > 2,5x la mediana (54.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 29,3x: promedio de historia y peers 27,7x, acercado 25% al justificado (34,1x); rango de anclas 24,3x–34,1x. Atípicos excluidos de la historia: Dec '16 (377,5x: > 2,5x la mediana (54.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 29,6x: promedio de historia y peers 27,4x, acercado 25% al justificado (36,3x); rango de anclas 25,0x–36,3x. Atípicos excluidos de la historia: Dec '20 (135,6x: > 2,5x la mediana (51.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 19,4x: promedio de historia y peers 18,4x, acercado 25% al justificado (22,3x); rango de anclas 16,6x–22,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$29,30 frente a US$26,38 del DCF (+11%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$29,30 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 8,47%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$9,61) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$26,38 por acción.** Complemento: DCF esperado por probabilidades US$25,22. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$26,38 | US$20,37 | US$35,29 |
| EV/EBITDA | 18,7× / 17,8× / 20,1× | 20% | 33% | US$30,77 | US$26,75 | US$36,78 |
| EV/FCFF | 32,2× / 29,5× / 38,1× | 10% | 17% | US$20,08 | US$19,97 | US$20,45 |
| P/E | 29,3× / 25,8× / 35,1× | 20% | 33% | US$35,31 | US$28,66 | US$46,59 |
| P/FCFE | 29,6× / 26,9× / 35,0× | 5% | 8% | US$22,56 | US$22,07 | US$23,32 |
| P/OCF | 19,4× / 17,5× / 22,7× | 5% | 8% | US$24,54 | US$22,75 | US$27,20 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$29,30 | US$25,53 | US$35,41 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$28,13 | US$23,47 | US$35,36 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$33,67 | US$26,00 | US$45,04 |
| EV/EBITDA | 18,7× / 17,8× / 20,1× | 20% | 33% | US$39,69 | US$32,68 | US$50,07 |
| EV/FCFF | 32,2× / 29,5× / 38,1× | 10% | 17% | US$27,20 | US$24,18 | US$30,80 |
| P/E | 29,3× / 25,8× / 35,1× | 20% | 33% | US$45,32 | US$34,79 | US$63,23 |
| P/FCFE | 29,6× / 26,9× / 35,0× | 5% | 8% | US$29,97 | US$26,63 | US$33,96 |
| P/OCF | 19,4× / 17,5× / 22,7× | 5% | 8% | US$31,97 | US$27,68 | US$37,71 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 60% | 100% | US$38,03 | US$31,05 | US$48,87 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$36,29 | US$29,03 | US$47,34 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 8,47%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$30,27 | US$30,96 | US$31,10 | US$30,77 | OK |
| EV/EBITDA | Conservador | US$28,05 | US$26,59 | US$25,60 | US$26,75 | OK |
| EV/EBITDA | Optimista | US$33,88 | US$37,22 | US$39,23 | US$36,78 | OK |
| EV/FCFF | Base | US$17,96 | US$20,97 | US$21,31 | US$20,08 | OK |
| EV/FCFF | Conservador | US$21,15 | US$19,83 | US$18,95 | US$19,97 | OK |
| EV/FCFF | Optimista | US$15,37 | US$21,86 | US$24,13 | US$20,45 | OK |
| P/E | Base | US$34,87 | US$35,57 | US$35,50 | US$35,31 | OK |
| P/E | Conservador | US$30,20 | US$28,52 | US$27,26 | US$28,66 | OK |
| P/E | Optimista | US$43,00 | US$47,23 | US$49,54 | US$46,59 | OK |
| P/FCFE | Base | US$20,81 | US$23,38 | US$23,48 | US$22,56 | OK |
| P/FCFE | Conservador | US$23,42 | US$21,93 | US$20,86 | US$22,07 | OK |
| P/FCFE | Optimista | US$18,72 | US$24,63 | US$26,61 | US$23,32 | OK |
| P/OCF | Base | US$23,47 | US$25,11 | US$25,05 | US$24,54 | OK |
| P/OCF | Conservador | US$23,90 | US$22,65 | US$21,69 | US$22,75 | OK |
| P/OCF | Optimista | US$23,98 | US$28,09 | US$29,54 | US$27,20 | OK |

Múltiplos consolidados hoy: US$29,30 / US$25,53 / US$35,41 · DCF de las historias hoy: US$26,38 / US$20,37 / US$35,29 · Ponderado hoy: US$28,13 / US$23,47 / US$35,36 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para CMG la diferencia es de +11% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$28,19 por acción y los múltiplos, US$26,54 hoy: 6% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$30,79 supone que los ingresos crecen 10,9% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 7,2% (+3,7 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$33,67 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 8,5%, WACC de los años 4-10 8,4%, ROE de FY+3 94,5% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 18,7x | 14,3x | +18% | 6,1% | 5,4% | +0,7 pp | Coherente con el DCF. |
| EV/FCFF | 32,2x | 34,9x | −19% | 5,2% | 5,4% | −0,2 pp | Coherente con el DCF. |
| P/E | 29,3x | 21,8x | +35% | 5,1% | 3,9% | +1,2 pp | Revisar: el múltiplo vale 35% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 29,6x | 33,3x | −11% | 4,9% | 5,3% | −0,4 pp | Coherente con el DCF. |
| P/OCF | 19,4x | 20,4x | −5% | 5,1% | 5,3% | −0,2 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$28,13 | — |
| Múltiplos Base +20% | US$31,82 | +13,1% |
| Múltiplos Base −20% | US$24,45 | −13,1% |
| Crecimiento años 2-5 +2 pp | US$29,10 | +3,4% |
| Crecimiento años 2-5 −2 pp | US$27,26 | −3,1% |
| Margen objetivo +3 pp | US$30,31 | +7,7% |
| Margen objetivo −3 pp | US$25,96 | −7,7% |
| WACC +1 pp | US$27,45 | −2,4% |
| WACC −1 pp | US$28,87 | +2,6% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 16,67 | 17,75 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 18,59 | 18,66 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 21,25 | 20,12 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 28,41 | 29,50 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 31,54 | 32,19 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 35,97 | 38,13 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 23,45 | 25,84 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 26,72 | 29,28 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 30,77 | 35,13 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 24,52 | 26,94 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 27,08 | 29,61 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 30,68 | 35,04 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 15,89 | 17,48 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 18,11 | 19,40 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 21,06 | 22,72 | Múltiplo optimista elegido con el protocolo v3 |
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
