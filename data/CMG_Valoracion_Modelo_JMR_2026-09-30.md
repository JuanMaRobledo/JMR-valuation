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

**Valor intrínseco principal · DCF Base hoy: US$23,84 por acción.** Complemento: DCF esperado por probabilidades US$22,81; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$9,09–US$31,89; precio con MOS 35% sobre el esperado: US$14,83; precio de referencia US$32,36. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$23,77), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Crece por aperturas con comparables bajas** (valor principal) | 40% | US$23,84 | US$9,54 |
| Conservadora · Tráfico débil y margen presionado | 35% | US$18,39 | US$6,44 |
| Disrupción · Deterioro de los fundamentales: Crisis de marca o saturación: el tráfico cae | 5% | US$9,09 | US$0,45 |
| Optimista · Vuelve el tráfico | 20% | US$31,89 | US$6,38 |
| **DCF esperado (complemento)** | 100% | **US$22,81** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$28,19 por acción y los múltiplos, US$26,54 hoy: 6% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$23,84 | US$23,67 | US$23,78 | US$14,83 | US$31,26 |
| Conservador | US$18,39 | US$21,91 | US$19,80 | US$14,83 | US$25,17 |
| Optimista | US$31,89 | US$26,03 | US$29,55 | US$14,83 | US$39,86 |

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
| DCF por acción hoy | US$18,39 | US$23,84 | US$31,89 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 0,95, ERP 4,46%, Ke 9,23%, costo de la deuda después de impuestos 4,35%, peso del patrimonio 88,4%, WACC inicial 8,66% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Chipotle cotizó a 40-110x utilidades mientras abría tiendas y crecía en ventas comparables de dos dígitos; en 2025-2026 las ventas comparables se estancaron y la acción cayó de ~US$43 a ~US$32. La etapa actual es FY25 y el LTM. B: restaurantes de servicio rápido y casual (McDonald's, Texas Roadhouse, Yum!, Wingstop), datos de yfinance al 29-sep-2026. Se excluyen Cava (crece 31% con margen de 8%, P/E 95x) y Starbucks (reestructuración, P/E 55x distorsionado). Ajuste +10%: Chipotle todavía abre ~8-10% de tiendas nuevas al año con retornos por tienda altos y sin deuda financiera, más crecimiento que McDonald's y Yum!. λ = 0,25: la Chipotle de FY+3 del escenario Base sigue siendo una cadena en expansión de unidades, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 21,8x | 16,2x (n=4: MCD 14,7x, TXRH 16,0x, YUM 16,4x, WING 16,7x) × 1,10 = 17,9x | 12,5x / 12,0x / 13,8x | **18,0x** | 17,3x | 19,0x | 18,6x / 16,7x / 21,2x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 34,4x (EV/FCF × 1,05 = FCF después de intereses ÷ FCFF) | 24,5x (n=4: MCD 24,2x, TXRH 28,2x, YUM 24,2x, WING 24,7x) × 1,10 = 26,9x | 30,5x / 26,0x / 40,9x | **30,6x** | 28,3x | 35,3x | 31,5x / 28,4x / 36,0x |
| P/E | mediana Dec '25, LTM (etapa actual) = 31,0x | 22,1x (n=4: MCD 19,0x, TXRH 25,2x, YUM 17,3x, WING 25,7x) × 1,10 = 24,3x | 25,2x / 21,8x / 32,6x | **27,0x** | 24,2x | 31,2x | 26,7x / 23,4x / 30,8x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 29,8x | 22,7x (n=4: MCD 21,3x, TXRH 25,8x, YUM 22,4x, WING 23,0x) × 1,10 = 25,0x | 27,2x / 23,6x / 35,2x | **27,3x** | 25,2x | 31,1x | 27,1x / 24,5x / 30,7x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 20,3x | 15,1x (n=4: MCD 14,6x, TXRH 12,8x, YUM 18,0x, WING 15,6x) × 1,10 = 16,6x | 16,7x / 14,7x / 20,5x | **18,0x** | 16,4x | 20,3x | 18,1x / 15,9x / 21,1x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 18,0x: promedio de historia y peers 19,8x, acercado 25% al justificado (12,5x); rango de anclas 12,5x–21,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 30,6x: promedio de historia y peers 30,7x, acercado 25% al justificado (30,5x); rango de anclas 26,9x–34,4x. Atípicos excluidos de la historia: Dec '20 (143,7x: > 2,5x la mediana (54.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 27,0x: promedio de historia y peers 27,7x, acercado 25% al justificado (25,2x); rango de anclas 24,3x–31,0x. Atípicos excluidos de la historia: Dec '16 (377,5x: > 2,5x la mediana (54.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 27,3x: promedio de historia y peers 27,4x, acercado 25% al justificado (27,2x); rango de anclas 25,0x–29,8x. Atípicos excluidos de la historia: Dec '20 (135,6x: > 2,5x la mediana (51.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 18,0x: promedio de historia y peers 18,4x, acercado 25% al justificado (16,7x); rango de anclas 16,6x–20,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$23,67 frente a US$23,84 del DCF (−1%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$23,67 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Crecimiento»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,23%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$9,09) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$23,84 por acción.** Complemento: DCF esperado por probabilidades US$22,81. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$23,84 | US$18,39 | US$31,89 |
| EV/EBITDA | 18,0× / 17,3× / 19,0× | 10% | 25% | US$29,15 | US$25,59 | US$33,94 |
| EV/FCFF | 30,6× / 28,3× / 35,3× | 15% | 38% | US$18,64 | US$18,73 | US$18,38 |
| P/E | 27,0× / 24,2× / 31,2× | 5% | 13% | US$32,16 | US$26,46 | US$40,82 |
| P/FCFE | 27,3× / 25,2× / 31,1× | 5% | 13% | US$20,53 | US$20,36 | US$20,40 |
| P/OCF | 18,0× / 16,4× / 20,3× | 5% | 13% | US$22,46 | US$21,09 | US$23,97 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$23,67 | US$21,91 | US$26,03 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$23,78 | US$19,80 | US$29,55 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$31,07 | US$23,97 | US$41,56 |
| EV/EBITDA | 18,0× / 17,3× / 19,0× | 10% | 25% | US$38,14 | US$31,69 | US$46,92 |
| EV/FCFF | 30,6× / 28,3× / 35,3× | 15% | 38% | US$25,64 | US$23,00 | US$28,18 |
| P/E | 27,0× / 24,2× / 31,2× | 5% | 13% | US$41,85 | US$32,56 | US$56,19 |
| P/FCFE | 27,3× / 25,2× / 31,1× | 5% | 13% | US$27,67 | US$24,90 | US$30,15 |
| P/OCF | 18,0× / 16,4× / 20,3× | 5% | 13% | US$29,66 | US$26,02 | US$33,71 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 40% | 100% | US$31,55 | US$26,98 | US$37,31 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$31,26 | US$25,17 | US$39,86 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,23%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$28,86 | US$29,33 | US$29,27 | US$29,15 | OK |
| EV/EBITDA | Conservador | US$27,01 | US$25,43 | US$24,32 | US$25,59 | OK |
| EV/EBITDA | Optimista | US$31,46 | US$34,37 | US$36,00 | US$33,94 | OK |
| EV/FCFF | Base | US$16,76 | US$19,48 | US$19,68 | US$18,64 | OK |
| EV/FCFF | Conservador | US$19,96 | US$18,59 | US$17,65 | US$18,73 | OK |
| EV/FCFF | Optimista | US$13,83 | US$19,68 | US$21,63 | US$18,38 | OK |
| P/E | Base | US$31,98 | US$32,40 | US$32,11 | US$32,16 | OK |
| P/E | Conservador | US$28,07 | US$26,32 | US$24,98 | US$26,46 | OK |
| P/E | Optimista | US$37,95 | US$41,40 | US$43,12 | US$40,82 | OK |
| P/FCFE | Base | US$19,08 | US$21,28 | US$21,23 | US$20,53 | OK |
| P/FCFE | Conservador | US$21,75 | US$20,22 | US$19,11 | US$20,36 | OK |
| P/FCFE | Optimista | US$16,50 | US$21,56 | US$23,14 | US$20,40 | OK |
| P/OCF | Base | US$21,63 | US$22,98 | US$22,76 | US$22,46 | OK |
| P/OCF | Conservador | US$22,31 | US$21,00 | US$19,97 | US$21,09 | OK |
| P/OCF | Optimista | US$21,29 | US$24,76 | US$25,87 | US$23,97 | OK |

Múltiplos consolidados hoy: US$23,67 / US$21,91 / US$26,03 · DCF de las historias hoy: US$23,84 / US$18,39 / US$31,89 · Ponderado hoy: US$23,78 / US$19,80 / US$29,55 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para CMG la diferencia es de −1% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$28,19 por acción y los múltiplos, US$26,54 hoy: 6% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$32,36 supone que los ingresos crecen 13,8% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 7,2% (+6,6 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$31,07 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,2%, WACC de los años 4-10 8,8%, ROE de FY+3 73,4% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 18,0x | 13,2x | +23% | 6,4% | 5,5% | +0,9 pp | Coherente con el DCF. |
| EV/FCFF | 30,6x | 32,1x | −17% | 5,4% | 5,5% | −0,2 pp | Coherente con el DCF. |
| P/E | 27,0x | 20,1x | +35% | 5,6% | 4,3% | +1,3 pp | Revisar: el múltiplo vale 35% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 27,3x | 30,7x | −11% | 5,4% | 5,8% | −0,4 pp | Coherente con el DCF. |
| P/OCF | 18,0x | 18,9x | −5% | 5,6% | 5,8% | −0,2 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$23,78 | — |
| Múltiplos Base +20% | US$25,81 | +8,6% |
| Múltiplos Base −20% | US$21,74 | −8,6% |
| Crecimiento años 2-5 +2 pp | US$25,06 | +5,4% |
| Crecimiento años 2-5 −2 pp | US$22,61 | −4,9% |
| Margen objetivo +3 pp | US$26,76 | +12,6% |
| Margen objetivo −3 pp | US$20,79 | −12,6% |
| WACC +1 pp | US$22,84 | −3,9% |
| WACC −1 pp | US$24,78 | +4,2% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Margen objetivo −3 pp, Múltiplos Base −20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 16,67 | 17,30 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 18,59 | 18,02 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 21,25 | 18,96 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 28,41 | 28,31 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 31,54 | 30,63 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 35,97 | 35,29 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 23,45 | 24,18 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 26,72 | 27,04 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 30,77 | 31,22 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 24,52 | 25,19 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 27,08 | 27,33 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 30,68 | 31,11 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 15,89 | 16,43 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 18,11 | 18,00 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 21,06 | 20,31 | Múltiplo optimista elegido con el protocolo v3 |
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
