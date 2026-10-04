---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de EPAM Systems, Inc."
ticker: "EPAM"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1txQTjdUuzsnCem_4O1szofY7uAp5xLc3uda3l_iIcR0/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# EPAM Systems, Inc. (EPAM) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$174,72 por acción.** Complemento: DCF esperado por probabilidades US$156,31; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$85,69–US$229,62; precio con MOS 35% sobre el esperado: US$101,60; precio de referencia US$108,29. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La IA compensa lo que quita: crecimiento moderado** (valor principal) | 45% | US$174,72 | US$78,62 |
| Conservadora · Deflación de horas por IA | 30% | US$115,60 | US$34,68 |
| Disrupción · Deterioro de los fundamentales: Los servicios se comoditizan | 10% | US$85,69 | US$8,57 |
| Optimista · La IA crea demanda de ingeniería | 15% | US$229,62 | US$34,44 |
| **DCF esperado (complemento)** | 100% | **US$156,31** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$168,22 por acción y los múltiplos, US$109,37 hoy: 35% por debajo del DCF, fuera del rango de ±25%. Los múltiplos reflejan lo que el mercado paga hoy por los servicios de TI bajo el temor a la IA (~7-9x EBITDA); el DCF supone que EPAM vuelve a crecer y a recuperar margen. Si la presión de los asistentes de código resulta estructural, los múltiplos son la referencia más prudente.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$174,72 | US$106,82 | US$133,98 | US$101,60 | US$178,63 |
| Conservador | US$115,60 | US$90,65 | US$100,63 | US$101,60 | US$128,40 |
| Optimista | US$229,62 | US$129,66 | US$169,64 | US$101,60 | US$234,90 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - EPAM](https://docs.google.com/spreadsheets/d/1txQTjdUuzsnCem_4O1szofY7uAp5xLc3uda3l_iIcR0/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$108,29.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 1,6% | 5,0% | 8,8% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 1,8% | 5,0% | 9,4% | Input B29 |
| Margen EBIT objetivo | 10,6% | 13,1% | 14,6% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 3,27 / 2,83 | — | Input B32/B33 |
| DCF por acción hoy | US$115,60 | US$174,72 | US$229,62 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 0,98, ERP 5,05%, Ke 10,24%, costo de la deuda después de impuestos 4,61%, peso del patrimonio 97,3%, WACC inicial 10,09% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: EPAM cotizó a 15-59x EBITDA mientras crecía 15-25% al año como proveedor de ingeniería de software. En febrero de 2026 guió un crecimiento orgánico de solo 3-6% y luego lo bajó a 3,2-4,2%; el mercado lo lee como presión estructural de los asistentes de código con IA sobre la subcontratación tradicional, y la acción cayó a mínimos. La etapa actual es solo el LTM. B: servicios de TI y consultoría (Accenture, Globant, Cognizant, Infosys, ExlService), datos de yfinance al 29-sep-2026. Se excluye Wipro (sus cifras mezclan rupias y dólares: EV/EBITDA negativo) y, en los múltiplos de EV, Infosys (EV/EBITDA de 18,8x incoherente con su P/E de 13x). Sin ajuste: EPAM crece como Accenture y Cognizant (3-6%), con menor margen operativo pero sin deuda y con recompras; las diferencias se compensan. λ = 0,25: la EPAM de FY+3 del escenario Base es una empresa de servicios de TI de crecimiento bajo, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana LTM (etapa actual) = 7,2x | 7,5x (n=4: ACN 8,4x, GLOB 4,7x, CTSH 6,6x, EXLS 14,4x) × 1,00 = 7,5x | 11,9x / 10,9x / 13,4x | **8,5x** | 7,7x | 9,7x | 7,1x / —x / —x |
| EV/FCFF | mediana LTM (etapa actual) = 10,0x (EV/FCF × 0,98 = FCF después de intereses ÷ FCFF) | 9,3x (n=4: ACN 8,5x, GLOB 6,6x, CTSH 10,1x, EXLS 18,8x) × 1,00 = 9,3x | 23,6x / 19,6x / 28,5x | **13,2x** | 11,8x | 15,5x | 10,2x / —x / —x |
| P/E | mediana LTM (etapa actual) = 15,2x | 13,3x (n=5: ACN 14,1x, GLOB 13,3x, CTSH 12,3x, INFY 13,1x, EXLS 21,9x) × 1,00 = 13,3x | 14,8x / 12,2x / 18,0x | **14,3x** | 13,5x | 15,7x | 15,2x / —x / —x |
| P/FCFE | mediana LTM (etapa actual) = 11,6x | 9,8x (n=5: ACN 8,6x, GLOB 5,8x, CTSH 9,9x, INFY 11,3x, EXLS 19,1x) × 1,00 = 9,8x | 21,4x / 18,1x / 25,4x | **13,4x** | 12,1x | 14,9x | 11,6x / —x / —x |
| P/OCF | mediana LTM (etapa actual) = 10,4x | 8,8x (n=5: ACN 8,2x, GLOB 4,3x, CTSH 8,8x, INFY 10,5x, EXLS 16,0x) × 1,00 = 8,8x | 19,7x / 16,6x / 23,4x | **12,1x** | 11,2x | 13,7x | 10,4x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 8,5x: promedio de historia y peers 7,3x, acercado 25% al justificado (11,9x); rango de anclas 7,2x–11,9x. Atípicos excluidos de la historia: LTM (7,2x: < 0,4x la mediana (25.5x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 13,2x: promedio de historia y peers 9,7x, acercado 25% al justificado (23,6x); rango de anclas 9,3x–23,6x. Atípicos excluidos de la historia: Dec '21 (79,7x: > 2,5x la mediana (28.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 14,3x: promedio de historia y peers 14,2x, acercado 25% al justificado (14,8x); rango de anclas 13,3x–15,2x. Atípicos excluidos de la historia: LTM (15,2x: < 0,4x la mediana (42.1x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 13,4x: promedio de historia y peers 10,7x, acercado 25% al justificado (21,4x); rango de anclas 9,8x–21,4x. Atípicos excluidos de la historia: Dec '21 (82,4x: > 2,5x la mediana (32.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 12,1x: promedio de historia y peers 9,6x, acercado 25% al justificado (19,7x); rango de anclas 8,8x–19,7x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$106,82 frente a US$174,72 del DCF (−39%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$106,82 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,24%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$85,69) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$174,72 por acción.** Complemento: DCF esperado por probabilidades US$156,31. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$174,72 | US$115,60 | US$229,62 |
| EV/EBITDA | 8,5× / 7,7× / 9,7× | 20% | 33% | US$115,58 | US$95,09 | US$145,58 |
| EV/FCFF | 13,2× / 11,8× / 15,5× | 10% | 17% | US$91,18 | US$83,27 | US$104,31 |
| P/E | 14,3× / 13,5× / 15,7× | 20% | 33% | US$115,80 | US$95,52 | US$142,66 |
| P/FCFE | 13,4× / 12,1× / 14,9× | 5% | 8% | US$87,50 | US$79,20 | US$96,79 |
| P/OCF | 12,1× / 11,2× / 13,7× | 5% | 8% | US$86,39 | US$79,63 | US$97,48 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$106,82 | US$90,65 | US$129,66 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$133,98 | US$100,63 | US$169,64 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$234,06 | US$154,87 | US$307,61 |
| EV/EBITDA | 8,5× / 7,7× / 9,7× | 20% | 33% | US$152,13 | US$116,85 | US$204,43 |
| EV/FCFF | 13,2× / 11,8× / 15,5× | 10% | 17% | US$121,56 | US$100,85 | US$155,86 |
| P/E | 14,3× / 13,5× / 15,7× | 20% | 33% | US$153,75 | US$116,83 | US$203,69 |
| P/FCFE | 13,4× / 12,1× / 14,9× | 5% | 8% | US$117,71 | US$95,92 | US$146,69 |
| P/OCF | 12,1× / 11,2× / 13,7× | 5% | 8% | US$115,82 | US$96,66 | US$146,17 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 60% | 100% | US$141,68 | US$110,75 | US$186,42 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$178,63 | US$128,40 | US$234,90 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,24%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$116,76 | US$116,43 | US$113,56 | US$115,58 | OK |
| EV/EBITDA | Conservador | US$103,64 | US$94,41 | US$87,22 | US$95,09 | OK |
| EV/EBITDA | Optimista | US$136,25 | US$147,91 | US$152,60 | US$145,58 | OK |
| EV/FCFF | Base | US$90,08 | US$92,73 | US$90,74 | US$91,18 | OK |
| EV/FCFF | Conservador | US$92,50 | US$82,04 | US$75,28 | US$83,27 | OK |
| EV/FCFF | Optimista | US$90,38 | US$106,20 | US$116,34 | US$104,31 | OK |
| P/E | Base | US$115,63 | US$117,01 | US$114,77 | US$115,80 | OK |
| P/E | Conservador | US$104,55 | US$94,80 | US$87,21 | US$95,52 | OK |
| P/E | Optimista | US$130,30 | US$145,64 | US$152,05 | US$142,66 | OK |
| P/FCFE | Base | US$85,54 | US$89,11 | US$87,87 | US$87,50 | OK |
| P/FCFE | Conservador | US$88,11 | US$77,88 | US$71,60 | US$79,20 | OK |
| P/FCFE | Optimista | US$82,17 | US$98,71 | US$109,50 | US$96,79 | OK |
| P/OCF | Base | US$84,83 | US$87,88 | US$86,45 | US$86,39 | OK |
| P/OCF | Conservador | US$88,31 | US$78,44 | US$72,15 | US$79,63 | OK |
| P/OCF | Optimista | US$84,05 | US$99,29 | US$109,11 | US$97,48 | OK |

Múltiplos consolidados hoy: US$106,82 / US$90,65 / US$129,66 · DCF de las historias hoy: US$174,72 / US$115,60 / US$229,62 · Ponderado hoy: US$133,98 / US$100,63 / US$169,64 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para EPAM la diferencia es de −39% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$168,22 por acción y los múltiplos, US$109,37 hoy: 35% por debajo del DCF, fuera del rango de ±25%. Los múltiplos reflejan lo que el mercado paga hoy por los servicios de TI bajo el temor a la IA (~7-9x EBITDA); el DCF supone que EPAM vuelve a crecer y a recuperar margen. Si la presión de los asistentes de código resulta estructural, los múltiplos son la referencia más prudente.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$108,29 supone que los ingresos crecen -5,8% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 5,5% (−11,3 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$234,06 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,2%, WACC de los años 4-10 9,8%, ROE de FY+3 17,1% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 8,5x | 13,3x | −35% | 3,6% | 5,8% | −2,1 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 35% por debajo del DCF en FY+3. |
| EV/FCFF | 13,2x | 26,4x | −48% | 2,0% | 5,8% | −3,7 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 48% por debajo del DCF en FY+3. |
| P/E | 14,3x | 21,8x | −34% | 5,1% | 7,5% | −2,4 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 34% por debajo del DCF en FY+3. |
| P/FCFE | 13,4x | 26,6x | −50% | 2,6% | 6,2% | −3,7 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 50% por debajo del DCF en FY+3. |
| P/OCF | 12,1x | 24,5x | −51% | 2,5% | 6,2% | −3,8 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 51% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$133,98 | — |
| Múltiplos Base +20% | US$146,23 | +9,1% |
| Múltiplos Base −20% | US$121,73 | −9,1% |
| Crecimiento años 2-5 +2 pp | US$139,07 | +3,8% |
| Crecimiento años 2-5 −2 pp | US$129,32 | −3,5% |
| Margen objetivo +3 pp | US$149,31 | +11,4% |
| Margen objetivo −3 pp | US$118,64 | −11,4% |
| WACC +1 pp | US$130,49 | −2,6% |
| WACC −1 pp | US$137,71 | +2,8% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo −3 pp, Margen objetivo +3 pp, Múltiplos Base +20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 7,72 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 7,12 | 8,47 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 9,73 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 11,80 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 10,16 | 13,16 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 15,49 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 13,49 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 15,16 | 14,35 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 15,70 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 12,13 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 11,57 | 13,39 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 14,89 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 11,21 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 10,37 | 12,10 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 13,67 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/EPAM_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1txQTjdUuzsnCem_4O1szofY7uAp5xLc3uda3l_iIcR0/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (ACN, GLOB, CTSH, INFY, EXLS, WIT).
- [Trefis, 20-feb-2026: EPAM −17% por una guía 2026 cauta](https://www.trefis.com/stock/epam/articles/591182/epam-stock-17-cautious-2026-guidance-ignites-investor-revolt/2026-02-20)
- [Finimize: EPAM recorta su guía 2026](https://finimize.com/content/epam-cuts-its-2026-revenue-outlook-as-ai-fears-linger)
- [Morningstar: EPAM vulnerable a la disrupción de la IA](https://www.morningstar.com/company-reports/1450663-no-moat-epam-systems-is-vulnerable-to-ais-potential-disruption)

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
