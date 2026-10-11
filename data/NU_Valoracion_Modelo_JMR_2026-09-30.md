---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Nu Holdings Ltd."
ticker: "NU"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1FIghcohETa7UiyRciIKiDCmFeEjN7XwlaN4TBCeWO6Q/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Nu Holdings Ltd. (NU) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$12,88 por acción.** Complemento: DCF esperado por probabilidades US$10,41; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$3,29–US$15,14; precio con MOS 35% sobre el esperado: US$6,77; precio de referencia US$16,12. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Líder digital de Brasil que escala México** (valor principal) | 45% | US$12,88 | US$5,80 |
| Conservadora · Crédito, impuestos y competencia comprimen el retorno | 25% | US$5,03 | US$1,26 |
| Disrupción · Deterioro de los fundamentales: Ciclo de crédito y regulación en Brasil | 10% | US$3,29 | US$0,33 |
| Optimista · Banco digital de América Latina con opción global | 20% | US$15,14 | US$3,03 |
| **DCF esperado (complemento)** | 100% | **US$10,41** | |

Lectura del 30-sep-2026: el DCF Base da US$12,88 por acción y el P/E (único múltiplo aplicable) US$20,55 hoy: 60% por encima, fuera de ±25%. El chequeo de crecimiento implícito confirma la causa: el P/E Base de 23,3x en FY+3 equivale a un crecimiento perpetuo de 7,0% con el ROE de FY+3, mientras el DCF implica 13,2x (3,7%), porque lleva el ROE de 32% al de la industria (18,8%) en los años 6-10 y el crecimiento a 5,29%. Los anclas del P/E (historia de 2024-2025 cuando el mercado pagaba 26-28x, peers bancarios con +50% por ROE y el justificado con el ROE de FY+3) suponen que NU conserva un ROE de ~30% por mucho más tiempo. Para un banco, el DCF (ROE frente al Ke con una convergencia explícita) es más confiable: el P/E de mercado de hoy (17,1x UDM; 14,6x la utilidad Base del año 1) está más cerca del DCF que el ancla histórica. No se movió ningún múltiplo para acercarlo al DCF; la brecha se informa.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$12,88 | US$20,55 | US$17,48 | US$6,77 | US$25,68 |
| Conservador | US$5,03 | US$11,35 | US$8,82 | US$6,77 | US$12,32 |
| Optimista | US$15,14 | US$27,34 | US$22,46 | US$6,77 | US$33,76 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - NU (desde cero 2026-10-11)](https://docs.google.com/spreadsheets/d/1FIghcohETa7UiyRciIKiDCmFeEjN7XwlaN4TBCeWO6Q/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$16,12.
- Peers: datos de mercado de yfinance consultados el 2026-10-11 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 16,4% | 22,6% | 30,4% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 (compuesto) | 10,4% | 17,0% | 20,1% | Valuation output D:G (filas 55, 4 y 106) |
| Margen EBIT objetivo | 22,7% | 22,7% | 22,7% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 0,09 / 0,09 | — | Input B32/B33 |
| DCF por acción hoy | US$5,03 | US$12,88 | US$15,14 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 0,82, ERP 6,88%, Ke 10,93%, costo de la deuda después de impuestos 5,57%, peso del patrimonio 94,2%, WACC inicial 10,62% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: NU fue rentable por primera vez en 2023 (P/E de 39,7x sobre una utilidad que recién arrancaba y crecimiento de ingresos de +68%); desde 2024 la utilidad está en régimen (ROE 31-38% sobre el patrimonio de inicio). Se usan 2024, 2025 y el UDM; 2021-2022 son pérdidas. Historia corta: tres lecturas, no diez años. Solo cierres con utilidad positiva y en la etapa actual. B: bancos de Brasil y América Latina (Itaú, Bradesco, Santander Brasil, Inter, Credicorp) y un emisor de tarjetas de EE.UU. (Capital One), con precios al 30-sep-2026 (yfinance). Se excluye SoFi en P/E: ROE de 7% y P/E de 31x por una utilidad todavía deprimida. Ajuste +50% sobre la mediana: NU tiene ROE de ~30% frente a una mediana de ~16% de los peers (Itaú 21%, Bradesco 14%, Santander Brasil 11%, Inter 16%, Credicorp 20%, Capital One 9%) y crece ~15% anual en FY+3 frente a 5-10%; con un Ke de ~11% y g de ~5%, el P/E justificado de Damodaran ((1 − g/ROE)(1 + g)/(Ke − g)) es ~50-60% mayor con ese ROE. Riesgo: el mismo país (Brasil) que Itaú, Bradesco, Santander e Inter. λ = 0,25: la NU de FY+3 en la historia Base gana un ROE parecido al de hoy (32%) con menor crecimiento; el justificado se calcula con el ROE de FY+3 sobre el patrimonio de hoy y sobrestima el P/E, así que pesa poco.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | No aplica: NU es un banco: los depósitos (US$45.300 M) y el fondeo son materia prima del negocio y el valor empresa no tiene sentido; peso 0% en la categoría Financiera. | | | | | | |
| EV/FCFF | No aplica: Igual que EV/EBITDA: en un banco el FCFF no se separa de la financiación; peso 0%. | | | | | | |
| P/E | mediana Dec '24, Dec '25, LTM (etapa actual) = 25,9x | 11,9x (n=6: ITUB 10,9x, BBD 11,4x, BSBR 16,9x, INTR 8,2x, BAP 14,3x, COF 12,4x) × 1,50 = 17,8x | 27,7x / 17,9x / 36,6x | **23,3x** | 18,7x | 27,5x | 25,3x / —x / —x |
| P/FCFE | No aplica: El flujo de caja contable de NU y de los peers incluye la variación de cartera y depósitos (flujo operativo de −US$1.382 M UDM en NU; P/FCF de 0,6x en Itaú y Santander Brasil): no hay un denominador comparable. El FCFE del banco (utilidad − aumento del patrimonio) ya está en el DCF. | | | | | | |
| P/OCF | No aplica: Mismo motivo que P/FCFE: el flujo operativo de un banco incluye préstamos y depósitos y no mide la generación del accionista. | | | | | | |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **P/E.** Base 23,3x: promedio de historia y peers 21,9x, acercado 25% al justificado (27,7x); rango de anclas 17,8x–27,7x. Atípicos excluidos de la historia: Dec '21 (-93,8x: métrica negativa o ~0); Dec '22 (-50,9x: métrica negativa o ~0). Único múltiplo aplicable al banco (Damodaran usa P/BV y P/E en financieras; la plantilla no tiene P/BV, que se informa aparte como lectura: el P/BV justificado de la Base es (ROE − g)/(Ke − g)). Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$20,55 frente a US$12,88 del DCF (+60%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$20,55 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Financiera»: DCF 40% y múltiplos 60% (P/E 60%). Sin peso (no aplica): EV/EBITDA, EV/FCFF, P/FCFE, P/OCF. Costo del patrimonio (Ke) 10,93%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$3,29) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$12,88 por acción.** Complemento: DCF esperado por probabilidades US$10,41. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$12,88 | US$5,03 | US$15,14 |
| EV/EBITDA | 10,8× / 9,7× / 11,9× | 0% | 0% | US$16,33 | US$13,64 | US$18,31 |
| EV/FCFF | 0,5× / 0,4× / 0,5× | 0% | 0% | US$0,34 | US$2,74 | US$-1,33 |
| P/E | 23,3× / 18,7× / 27,5× | 60% | 100% | US$20,55 | US$11,35 | US$27,34 |
| P/FCFE | 1,7× / 1,5× / 1,8× | 0% | 0% | US$0,46 | US$0,40 | US$0,50 |
| P/OCF | 1,7× / 1,5× / 1,9× | 0% | 0% | US$-14,61 | US$-6,63 | US$-20,23 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$20,55 | US$11,35 | US$27,34 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$17,48 | US$8,82 | US$22,46 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$17,58 | US$6,86 | US$20,67 |
| EV/EBITDA | 10,8× / 9,7× / 11,9× | 0% | 0% | US$23,20 | US$18,37 | US$26,73 |
| EV/FCFF | 0,5× / 0,4× / 0,5× | 0% | 0% | US$0,57 | US$3,65 | US$-1,62 |
| P/E | 23,3× / 18,7× / 27,5× | 60% | 100% | US$31,08 | US$15,96 | US$42,48 |
| P/FCFE | 1,7× / 1,5× / 1,8× | 0% | 0% | US$0,96 | US$0,69 | US$1,08 |
| P/OCF | 1,7× / 1,5× / 1,9× | 0% | 0% | US$-17,34 | US$-7,17 | US$-24,62 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 60% | 100% | US$31,08 | US$15,96 | US$42,48 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$25,68 | US$12,32 | US$33,76 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,93%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$15,53 | US$16,47 | US$17,00 | US$16,33 | OK |
| EV/EBITDA | Conservador | US$13,74 | US$13,73 | US$13,45 | US$13,64 | OK |
| EV/EBITDA | Optimista | US$16,91 | US$18,44 | US$19,59 | US$18,31 | OK |
| EV/FCFF | Base | US$0,28 | US$0,33 | US$0,42 | US$0,34 | OK |
| EV/FCFF | Conservador | US$2,82 | US$2,72 | US$2,67 | US$2,74 | OK |
| EV/FCFF | Optimista | US$-1,34 | US$-1,47 | US$-1,19 | US$-1,33 | n/a (≤ 0) |
| P/E | Base | US$18,16 | US$20,71 | US$22,77 | US$20,55 | OK |
| P/E | Conservador | US$10,91 | US$11,45 | US$11,70 | US$11,35 | OK |
| P/E | Optimista | US$23,39 | US$27,49 | US$31,12 | US$27,34 | OK |
| P/FCFE | Base | US$0,22 | US$0,46 | US$0,71 | US$0,46 | OK |
| P/FCFE | Conservador | US$0,28 | US$0,41 | US$0,50 | US$0,40 | OK |
| P/FCFE | Optimista | US$0,21 | US$0,49 | US$0,79 | US$0,50 | OK |
| P/OCF | Base | US$-16,52 | US$-14,60 | US$-12,70 | US$-14,61 | n/a (≤ 0) |
| P/OCF | Conservador | US$-8,01 | US$-6,64 | US$-5,25 | US$-6,63 | n/a (≤ 0) |
| P/OCF | Optimista | US$-21,99 | US$-20,66 | US$-18,04 | US$-20,23 | n/a (≤ 0) |

Múltiplos consolidados hoy: US$20,55 / US$11,35 / US$27,34 · DCF de las historias hoy: US$12,88 / US$5,03 / US$15,14 · Ponderado hoy: US$17,48 / US$8,82 / US$22,46 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NU la diferencia es de +60% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base da US$12,88 por acción y el P/E (único múltiplo aplicable) US$20,55 hoy: 60% por encima, fuera de ±25%. El chequeo de crecimiento implícito confirma la causa: el P/E Base de 23,3x en FY+3 equivale a un crecimiento perpetuo de 7,0% con el ROE de FY+3, mientras el DCF implica 13,2x (3,7%), porque lleva el ROE de 32% al de la industria (18,8%) en los años 6-10 y el crecimiento a 5,29%. Los anclas del P/E (historia de 2024-2025 cuando el mercado pagaba 26-28x, peers bancarios con +50% por ROE y el justificado con el ROE de FY+3) suponen que NU conserva un ROE de ~30% por mucho más tiempo. Para un banco, el DCF (ROE frente al Ke con una convergencia explícita) es más confiable: el P/E de mercado de hoy (17,1x UDM; 14,6x la utilidad Base del año 1) está más cerca del DCF que el ancla histórica. No se movió ningún múltiplo para acercarlo al DCF; la brecha se informa.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$16,12 supone que los ingresos crecen — al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 18,9% (—). Ningún crecimiento entre −20% y 80% justifica el precio con estos márgenes.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$17,58 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,9%, WACC de los años 4-10 9,9%, ROE de FY+3 49,4% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 10,8x | — | — | — | — | — | No aplica: NU es un banco: los depósitos (US$45.300 M) y el fondeo son materia prima del negocio y el valor empresa no tiene sentid |
| EV/FCFF | 0,5x | — | — | — | — | — | No aplica: Igual que EV/EBITDA: en un banco el FCFF no se separa de la financiación; peso 0%. |
| P/E | 23,3x | 13,2x | +77% | 7,0% | 3,7% | +3,3 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 77% por encima del DCF en FY+3. |
| P/FCFE | 1,7x | — | — | — | — | — | No aplica: El flujo de caja contable de NU y de los peers incluye la variación de cartera y depósitos (flujo operativo de −US$1.382 |
| P/OCF | 1,7x | — | — | — | — | — | No aplica: Mismo motivo que P/FCFE: el flujo operativo de un banco incluye préstamos y depósitos y no mide la generación del accion |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$17,48 | — |
| Múltiplos Base +20% | US$19,95 | +14,1% |
| Múltiplos Base −20% | US$15,01 | −14,1% |
| Crecimiento años 2-5 +2 pp | US$17,82 | +1,9% |
| Crecimiento años 2-5 −2 pp | US$17,17 | −1,8% |
| Margen objetivo +3 pp | US$17,48 | +0,0% |
| Margen objetivo −3 pp | US$17,48 | +0,0% |
| WACC +1 pp | US$17,17 | −1,8% |
| WACC −1 pp | US$17,82 | +1,9% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| PE | J8 | — | 18,69 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 25,31 | 23,32 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 27,47 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/NU_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1FIghcohETa7UiyRciIKiDCmFeEjN7XwlaN4TBCeWO6Q/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-10-11 (ITUB, BBD, BSBR, INTR, BAP, SOFI, COF).
- [Nu Holdings, comunicado del 2T26 (6-K)](https://www.sec.gov/Archives/edgar/data/1691493/000129281426004222/nupr2q26_6k.htm)
- [Damodaran, Price/Book y P/E por industria, ene-2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html)

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
