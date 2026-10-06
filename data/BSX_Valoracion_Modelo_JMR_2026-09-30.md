---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de BOSTON SCIENTIFIC CORP"
ticker: "BSX"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1LVn63SMyvovWzNjbF5Jdi-v0EFUPXLqp4A6n8gwbKHc/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# BOSTON SCIENTIFIC CORP (BSX) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$35,22 por acción.** Complemento: DCF esperado por probabilidades US$33,91; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$21,86–US$42,59; precio con MOS 35% sobre el esperado: US$22,04; precio de referencia US$43,65. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La cartera diversificada sostiene ~7%** (valor principal) | 45% | US$35,22 | US$15,85 |
| Conservadora · El campo pulsado se vuelve commodity | 30% | US$28,19 | US$8,46 |
| Disrupción · Deterioro de los fundamentales: Pierde participación y precio | 5% | US$21,86 | US$1,09 |
| Optimista · Electrofisiología y Watchman vuelven a doble dígito | 20% | US$42,59 | US$8,52 |
| **DCF esperado (complemento)** | 100% | **US$33,91** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$36,39 por acción y los múltiplos, US$38,61 hoy: 6% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$35,22 | US$35,87 | US$35,61 | US$22,04 | US$47,98 |
| Conservador | US$28,19 | US$30,41 | US$29,52 | US$22,04 | US$38,45 |
| Optimista | US$42,59 | US$44,13 | US$43,51 | US$22,04 | US$60,39 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - BSX](https://docs.google.com/spreadsheets/d/1LVn63SMyvovWzNjbF5Jdi-v0EFUPXLqp4A6n8gwbKHc/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$43,65.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 1,9% | 7,0% | 5,9% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 4,9% | 7,0% | 10,7% | Input B29 |
| Margen EBIT objetivo | 22,2% | 24,2% | 26,2% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,26 / 1,17 | — | Input B32/B33 |
| DCF por acción hoy | US$28,19 | US$35,22 | US$42,59 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 0,98, ERP 4,35%, Ke 9,56%, costo de la deuda después de impuestos 5,00%, peso del patrimonio 85,7%, WACC inicial 8,91% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Boston Scientific cotizaba a 25-55x EBITDA mientras crecía 12-20% orgánico. En 2026 la empresa bajó su guía de crecimiento orgánico a 6,5-8% (desde 10-11%, frente a 19,5% en 2025), las ventas de Watchman se estancaron y un ciberataque en agosto la llevó a retirar su guía; la acción cayó ~50% en el año. La etapa actual es solo el LTM. B: medtech diversificada de gran capitalización (Medtronic, Stryker, Abbott, Edwards, Intuitive Surgical, Zimmer Biomet), datos de yfinance al 29-sep-2026. Ajuste −5%: tras la baja de guía, Boston Scientific crece como la mediana de los peers, pero con más incertidumbre de ejecución (Watchman, electrofisiología en EE. UU. y los efectos del ciberataque). λ = 0 (30-sep-2026): el justificado C supone que el ROE de FY+3 se mantiene para siempre, mientras que el DCF supone que después del año 10 el retorno sobre el capital baja al costo de capital (BSX no cumple la regla del ROIC terminal). C se deja fuera del Base y se conserva como referencia en la tabla.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana LTM (etapa actual) = 13,7x | 16,6x (n=6: MDT 12,9x, SYK 15,9x, ABT 17,3x, EW 23,3x, ISRG 33,8x, ZBH 9,8x) × 0,95 = 10,3x | 14,0x / 13,1x / 15,1x | **12,0x** | 11,0x | 13,6x | 17,2x / 14,9x / 21,0x |
| EV/FCFF | mediana LTM (etapa actual) = 19,9x (EV/FCF × 0,95 = FCF después de intereses ÷ FCFF) | 25,1x (n=6: MDT 20,1x, SYK 23,8x, ABT 26,3x, EW 32,5x, ISRG 43,9x, ZBH 15,1x) × 0,95 = 16,4x | 30,4x / 25,8x / 34,5x | **18,2x** | 16,3x | 20,4x | 25,0x / 22,1x / 29,6x |
| P/E | mediana LTM (etapa actual) = 17,9x | 30,8x (n=6: MDT 21,5x, SYK 28,9x, ABT 32,7x, EW 52,4x, ISRG 47,3x, ZBH 22,2x) × 0,95 = 23,6x | 17,2x / 14,9x / 19,6x | **20,8x** | 18,3x | 24,6x | 22,5x / 19,3x / 27,9x |
| P/FCFE | mediana LTM (etapa actual) = 17,6x | 23,2x (n=6: MDT 18,2x, SYK 22,7x, ABT 23,7x, EW 35,4x, ISRG 45,8x, ZBH 12,4x) × 0,95 = 14,3x | 25,9x / 22,4x / 28,8x | **15,9x** | 14,3x | 18,7x | 21,6x / 19,1x / 26,6x |
| P/OCF | mediana LTM (etapa actual) = 14,1x | 18,9x (n=6: MDT 13,9x, SYK 19,4x, ABT 18,5x, EW 29,5x, ISRG 39,8x, ZBH 10,0x) × 0,95 = 11,4x | 24,5x / 19,4x / 28,6x | **12,7x** | 11,0x | 15,2x | 18,5x / 15,8x / 23,4x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 12,0x: promedio de historia y peers 12,0x, acercado 0% al justificado (14,0x); rango de anclas 10,3x–14,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 18,2x: promedio de historia y peers 18,2x, acercado 0% al justificado (30,4x); rango de anclas 16,4x–30,4x. Atípicos excluidos de la historia: Dec '18 (-9.307,0x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 20,8x: promedio de historia y peers 20,8x, acercado 0% al justificado (17,2x); rango de anclas 17,2x–23,6x. Atípicos excluidos de la historia: Dec '20 (-599,2x: métrica negativa o ~0); Dec '17 (354,1x: > 2,5x la mediana (55.6x)); Dec '19 (13,6x: < 0,4x la mediana (55.6x), caída puntual); LTM (17,9x: < 0,4x la mediana (55.6x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 15,9x: promedio de historia y peers 15,9x, acercado 0% al justificado (25,9x); rango de anclas 14,3x–25,9x. Atípicos excluidos de la historia: Dec '18 (-8.155,3x: métrica negativa o ~0); LTM (17,6x: < 0,4x la mediana (46.1x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 12,7x: promedio de historia y peers 12,7x, acercado 0% al justificado (24,5x); rango de anclas 11,4x–24,5x. Atípicos excluidos de la historia: Dec '18 (157,8x: > 2,5x la mediana (33.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$35,87 frente a US$35,22 del DCF (+2%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$35,87 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,56%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$21,86) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$35,22 por acción.** Complemento: DCF esperado por probabilidades US$33,91. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$35,22 | US$28,19 | US$42,59 |
| EV/EBITDA | 12,0× / 11,0× / 13,6× | 20% | 33% | US$39,49 | US$33,12 | US$48,83 |
| EV/FCFF | 18,2× / 16,3× / 20,4× | 10% | 17% | US$23,22 | US$22,03 | US$25,34 |
| P/E | 20,8× / 18,3× / 24,6× | 20% | 33% | US$42,71 | US$34,81 | US$54,42 |
| P/FCFE | 15,9× / 14,3× / 18,7× | 5% | 8% | US$30,38 | US$26,53 | US$37,12 |
| P/OCF | 12,7× / 11,0× / 15,2× | 5% | 8% | US$24,84 | US$22,60 | US$28,77 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$35,87 | US$30,41 | US$44,13 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$35,61 | US$29,52 | US$43,51 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$46,31 | US$37,07 | US$56,00 |
| EV/EBITDA | 12,0× / 11,0× / 13,6× | 20% | 33% | US$53,16 | US$42,50 | US$68,14 |
| EV/FCFF | 18,2× / 16,3× / 20,4× | 10% | 17% | US$34,81 | US$30,08 | US$42,37 |
| P/E | 20,8× / 18,3× / 24,6× | 20% | 33% | US$57,65 | US$44,74 | US$76,41 |
| P/FCFE | 15,9× / 14,3× / 18,7× | 5% | 8% | US$41,40 | US$33,66 | US$53,20 |
| P/OCF | 12,7× / 11,0× / 15,2× | 5% | 8% | US$34,83 | US$29,68 | US$43,63 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 60% | 100% | US$49,09 | US$39,37 | US$63,31 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$47,98 | US$38,45 | US$60,39 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,56%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$38,08 | US$39,95 | US$40,42 | US$39,49 | OK |
| EV/EBITDA | Conservador | US$33,71 | US$33,32 | US$32,32 | US$33,12 | OK |
| EV/EBITDA | Optimista | US$44,79 | US$49,88 | US$51,82 | US$48,83 | OK |
| EV/FCFF | Base | US$19,23 | US$23,96 | US$26,47 | US$23,22 | OK |
| EV/FCFF | Conservador | US$20,60 | US$22,61 | US$22,87 | US$22,03 | OK |
| EV/FCFF | Optimista | US$16,03 | US$27,77 | US$32,22 | US$25,34 | OK |
| P/E | Base | US$40,92 | US$43,37 | US$43,84 | US$42,71 | OK |
| P/E | Conservador | US$35,27 | US$35,12 | US$34,03 | US$34,81 | OK |
| P/E | Optimista | US$49,36 | US$55,81 | US$58,10 | US$54,42 | OK |
| P/FCFE | Base | US$28,82 | US$30,83 | US$31,49 | US$30,38 | OK |
| P/FCFE | Conservador | US$27,31 | US$26,69 | US$25,60 | US$26,53 | OK |
| P/FCFE | Optimista | US$30,56 | US$40,33 | US$40,46 | US$37,12 | OK |
| P/OCF | Base | US$22,73 | US$25,32 | US$26,48 | US$24,84 | OK |
| P/OCF | Conservador | US$22,27 | US$22,97 | US$22,57 | US$22,60 | OK |
| P/OCF | Optimista | US$22,60 | US$30,53 | US$33,18 | US$28,77 | OK |

Múltiplos consolidados hoy: US$35,87 / US$30,41 / US$44,13 · DCF de las historias hoy: US$35,22 / US$28,19 / US$42,59 · Ponderado hoy: US$35,61 / US$29,52 / US$43,51 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para BSX la diferencia es de +2% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$36,39 por acción y los múltiplos, US$38,61 hoy: 6% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$43,65 supone que los ingresos crecen 11,0% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 6,1% (+4,9 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$46,31 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,6%, WACC de los años 4-10 8,9%, ROE de FY+3 16,5% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 12,0x | 10,6x | +15% | 4,9% | 4,4% | +0,5 pp | Coherente con el DCF. |
| EV/FCFF | 18,2x | 23,0x | −25% | 3,3% | 4,4% | −1,1 pp | Coherente con el DCF. |
| P/E | 20,8x | 16,7x | +24% | 6,4% | 5,3% | +1,2 pp | Coherente con el DCF. |
| P/FCFE | 15,9x | 17,8x | −11% | 3,1% | 3,7% | −0,6 pp | Coherente con el DCF. |
| P/OCF | 12,7x | 16,9x | −25% | 2,0% | 3,7% | −1,8 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$35,61 | — |
| Múltiplos Base +20% | US$40,27 | +13,1% |
| Múltiplos Base −20% | US$30,95 | −13,1% |
| Crecimiento años 2-5 +2 pp | US$36,79 | +3,3% |
| Crecimiento años 2-5 −2 pp | US$34,52 | −3,0% |
| Margen objetivo +3 pp | US$37,80 | +6,1% |
| Margen objetivo −3 pp | US$33,42 | −6,1% |
| WACC +1 pp | US$34,68 | −2,6% |
| WACC −1 pp | US$36,60 | +2,8% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo −3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 14,92 | 11,04 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 17,18 | 12,00 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 21,03 | 13,56 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 22,13 | 16,28 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 25,01 | 18,19 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 29,58 | 20,43 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 19,33 | 18,28 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 22,50 | 20,79 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 27,91 | 24,63 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 19,08 | 14,34 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 21,65 | 15,95 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 26,64 | 18,67 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 15,75 | 10,97 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 18,53 | 12,72 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 23,44 | 15,24 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/BSX_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1LVn63SMyvovWzNjbF5Jdi-v0EFUPXLqp4A6n8gwbKHc/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (MDT, SYK, ABT, EW, ISRG, ZBH).
- [Motley Fool, 29-may-2026: por qué caía Boston Scientific](https://www.fool.com/investing/2026/05/29/why-boston-scientific-stock-was-sliding-this-week/)
- [Nasdaq: ciberataque y guía 2026 débil](https://www.nasdaq.com/articles/cyberattack-weak-2026-outlook-weigh-bsx-stock-sell)
- [TIKR: BSX cae tras el impacto del ciberataque](https://www.tikr.com/blog/boston-scientific-bsx-stock-falls-cyberattack-sales-profit-impact)

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
