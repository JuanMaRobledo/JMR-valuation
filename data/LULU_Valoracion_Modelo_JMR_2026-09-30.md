---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de lululemon athletica inc."
ticker: "LULU"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1wuEhOhrjlL5t-oSO9sRd7Py0Vw-47rv_4AAwaS8-ZJw/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# lululemon athletica inc. (LULU) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$171,60 por acción.** Complemento: DCF esperado por probabilidades US$152,10; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$72,11–US$241,60; precio con MOS 35% sobre el esperado: US$98,86; precio de referencia US$95,86. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$171,34), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Américas se estabiliza y crece lo internacional** (valor principal) | 45% | US$171,60 | US$77,22 |
| Conservadora · Pérdida de participación frente a Alo y Vuori | 30% | US$104,75 | US$31,42 |
| Disrupción · Deterioro de los fundamentales: la moda pasa y la marca se vuelve una más | 10% | US$72,11 | US$7,21 |
| Optimista · La nueva CEO recupera la marca | 15% | US$241,60 | US$36,24 |
| **DCF esperado (complemento)** | 100% | **US$152,10** | |

Lectura del 2-oct-2026: el DCF Base de las historias da ~US$171,6 por acción y los múltiplos consolidados ~US$135,7 hoy, ~21% menos, dentro del ±25%. La historia reciente de lululemon (7× EBITDA en Feb '26) y los peers deprimidos (Nike, Deckers, Gap) tiran los múltiplos hacia abajo. El DCF es el valor intrínseco; los múltiplos son precio relativo y, como el precio actual (US$95,86), están más cerca de la Conservadora que de la Base.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$171,60 | US$126,93 | US$144,80 | US$98,86 | US$195,86 |
| Conservador | US$104,75 | US$83,73 | US$92,14 | US$98,86 | US$117,08 |
| Optimista | US$241,60 | US$170,54 | US$198,96 | US$98,86 | US$284,66 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - LULU (desde cero 2026-10-02)](https://docs.google.com/spreadsheets/d/1wuEhOhrjlL5t-oSO9sRd7Py0Vw-47rv_4AAwaS8-ZJw/edit).
- Análisis del 01 de oct de 2026. Precio de referencia de la hoja: US$95,86.
- Peers: datos de mercado de yfinance consultados el 2026-10-02 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -8,0% | -6,5% | 4,9% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | -8,0% | 3,9% | 4,9% | Input B29 |
| Margen EBIT objetivo | 18,4% | 18,4% | 23,4% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,80 / 1,80 | — | Input B32/B33 |
| DCF por acción hoy | US$104,75 | US$171,60 | US$241,60 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,24%, beta apalancada 1,15, ERP 4,09%, Ke 9,94%, costo de la deuda después de impuestos 4,42%, peso del patrimonio 86,2%, WACC inicial 9,18% y terminal 9,33%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: lululemon cotizó a 15-40 veces el EBITDA mientras crecía 15-25% al año (2017-2024). Desde 2025 Américas cae (comparables −3% en 2025 y −12% en el 2T26), el margen baja de 23,7% a ~17% normalizado y la guía de 2026 es de caída de ventas: la etapa actual es Feb '25, Feb '26 y el LTM. Su mediana mezcla el fin de la etapa anterior con el mínimo actual. B: ropa y calzado deportivo con datos de yfinance al 2-oct-2026: Nike, Adidas, On, Deckers, Birkenstock y Gap. Se excluye Under Armour (margen operativo negativo). Sin ajuste: margen operativo mayor que la mediana de los peers (17% objetivo frente a 7-15% de Nike, Adidas, Gap y Deckers), +5%; crecimiento a FY+3 menor que el de On, Adidas y Birkenstock, −5%; riesgo propio parecido (una marca, sin deuda). λ = 0,5: la lululemon de FY+3 (crecimiento de un dígito medio y margen ~16%) es distinta de la de la etapa de alto crecimiento; el justificado (C) usa los supuestos de cada escenario y equilibra la historia y los peers.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Feb '25, Feb '26, LTM (etapa actual) = 7,2x | 11,0x (n=6: NKE 11,0x, ADDYY 12,4x, ONON 19,2x, DECK 7,3x, BIRK 11,0x, GAP 7,6x) × 1,00 = 11,0x | 10,2x / 6,3x / 10,2x | **9,7x** | 7,1x | 12,0x | 9,8x / 7,0x / 12,6x |
| EV/FCFF | mediana Feb '25, Feb '26, LTM (etapa actual) = 21,7x (EV/FCF × 1,03 = FCF después de intereses ÷ FCFF) | 18,5x (n=6: NKE 24,8x, ADDYY 17,6x, ONON 21,1x, DECK 8,7x, BIRK 19,5x, GAP 10,9x) × 1,00 = 18,5x | 23,9x / 13,0x / 25,6x | **22,0x** | 14,1x | 24,9x | 22,0x / 14,1x / 24,9x |
| P/E | mediana Feb '25, Feb '26, LTM (etapa actual) = 13,2x | 16,1x (n=6: NKE 16,1x, ADDYY 18,3x, ONON 21,9x, DECK 11,3x, BIRK 16,1x, GAP 6,8x) × 1,00 = 16,1x | 16,9x / 11,1x / 18,6x | **15,7x** | 11,8x | 19,8x | 15,7x / 11,7x / 19,9x |
| P/FCFE | mediana Feb '25, Feb '26, LTM (etapa actual) = 21,1x | 17,2x (n=6: NKE 23,0x, ADDYY 15,5x, ONON 24,0x, DECK 9,6x, BIRK 18,9x, GAP 8,3x) × 1,00 = 17,2x | 20,6x / 12,0x / 21,9x | **19,9x** | 12,7x | 23,6x | 19,9x / 12,7x / 23,5x |
| P/OCF | mediana Feb '25, Feb '26, LTM (etapa actual) = 12,1x | 13,0x (n=6: NKE 17,5x, ADDYY 12,3x, ONON 19,6x, DECK 9,0x, BIRK 13,7x, GAP 5,2x) × 1,00 = 13,0x | 12,0x / 7,0x / 13,0x | **12,3x** | 8,4x | 15,3x | 12,3x / 8,5x / 15,5x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 9,7x: promedio de historia y peers 9,1x, acercado 50% al justificado (10,2x); rango de anclas 7,2x–11,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 22,0x: promedio de historia y peers 20,1x, acercado 50% al justificado (23,9x); rango de anclas 18,5x–23,9x. Atípicos excluidos de la historia: Jan '23 (115,0x: > 2,5x la mediana (33.0x)); LTM (8,4x: < 0,4x la mediana (33.0x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 15,7x: promedio de historia y peers 14,6x, acercado 50% al justificado (16,9x); rango de anclas 13,2x–16,9x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 19,9x: promedio de historia y peers 19,1x, acercado 50% al justificado (20,6x); rango de anclas 17,2x–21,1x. Atípicos excluidos de la historia: Jan '23 (115,9x: > 2,5x la mediana (35.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 12,3x: promedio de historia y peers 12,6x, acercado 50% al justificado (12,0x); rango de anclas 12,0x–13,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$126,93 frente a US$171,60 del DCF (−26%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$126,93 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,94%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$72,11) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$171,60 por acción.** Complemento: DCF esperado por probabilidades US$152,10. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$171,60 | US$104,75 | US$241,60 |
| EV/EBITDA | 9,7× / 7,1× / 12,0× | 20% | 33% | US$131,99 | US$84,55 | US$188,10 |
| EV/FCFF | 22,0× / 14,1× / 24,9× | 10% | 17% | US$128,61 | US$88,90 | US$139,31 |
| P/E | 15,7× / 11,8× / 19,8× | 20% | 33% | US$120,61 | US$77,83 | US$177,29 |
| P/FCFE | 19,9× / 12,7× / 23,6× | 5% | 8% | US$121,36 | US$83,70 | US$138,35 |
| P/OCF | 12,3× / 8,4× / 15,3× | 5% | 8% | US$134,14 | US$93,73 | US$167,90 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$126,93 | US$83,73 | US$170,54 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$144,80 | US$92,14 | US$198,96 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$228,05 | US$139,21 | US$321,08 |
| EV/EBITDA | 9,7× / 7,1× / 12,0× | 20% | 33% | US$180,74 | US$106,12 | US$277,67 |
| EV/FCFF | 22,0× / 14,1× / 24,9× | 10% | 17% | US$176,62 | US$101,80 | US$230,81 |
| P/E | 15,7× / 11,8× / 19,8× | 20% | 33% | US$168,37 | US$98,51 | US$268,97 |
| P/FCFE | 19,9× / 12,7× / 23,6× | 5% | 8% | US$166,37 | US$96,18 | US$227,62 |
| P/OCF | 12,3× / 8,4× / 15,3× | 5% | 8% | US$176,85 | US$109,71 | US$248,74 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 60% | 100% | US$174,41 | US$102,33 | US$260,38 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$195,86 | US$117,08 | US$284,66 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,94%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$125,23 | US$134,75 | US$136,00 | US$131,99 | OK |
| EV/EBITDA | Conservador | US$89,04 | US$84,76 | US$79,85 | US$84,55 | OK |
| EV/EBITDA | Optimista | US$160,65 | US$194,70 | US$208,94 | US$188,10 | OK |
| EV/FCFF | Base | US$123,32 | US$129,61 | US$132,90 | US$128,61 | OK |
| EV/FCFF | Conservador | US$103,48 | US$86,61 | US$76,60 | US$88,90 | OK |
| EV/FCFF | Optimista | US$99,35 | US$144,90 | US$173,68 | US$139,31 | OK |
| P/E | Base | US$111,31 | US$123,82 | US$126,70 | US$120,61 | OK |
| P/E | Conservador | US$81,16 | US$78,21 | US$74,13 | US$77,83 | OK |
| P/E | Optimista | US$144,52 | US$184,96 | US$202,39 | US$177,29 | OK |
| P/FCFE | Base | US$116,56 | US$122,34 | US$125,19 | US$121,36 | OK |
| P/FCFE | Conservador | US$97,09 | US$81,65 | US$72,37 | US$83,70 | OK |
| P/FCFE | Optimista | US$99,96 | US$143,82 | US$171,28 | US$138,35 | OK |
| P/OCF | Base | US$134,95 | US$134,40 | US$133,07 | US$134,14 | OK |
| P/OCF | Conservador | US$106,68 | US$91,94 | US$82,56 | US$93,73 | OK |
| P/OCF | Optimista | US$145,26 | US$171,26 | US$187,17 | US$167,90 | OK |

Múltiplos consolidados hoy: US$126,93 / US$83,73 / US$170,54 · DCF de las historias hoy: US$171,60 / US$104,75 / US$241,60 · Ponderado hoy: US$144,80 / US$92,14 / US$198,96 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para LULU la diferencia es de −26% (múltiplos por debajo del DCF). Lectura del 2-oct-2026: el DCF Base de las historias da ~US$171,6 por acción y los múltiplos consolidados ~US$135,7 hoy, ~21% menos, dentro del ±25%. La historia reciente de lululemon (7× EBITDA en Feb '26) y los peers deprimidos (Nike, Deckers, Gap) tiran los múltiplos hacia abajo. El DCF es el valor intrínseco; los múltiplos son precio relativo y, como el precio actual (US$95,86), están más cerca de la Conservadora que de la Base.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$95,86 supone que los ingresos crecen -12,1% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 1,8% (−14,0 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$228,05 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,9%, WACC de los años 4-10 9,2%, ROE de FY+3 26,6% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 9,7x | 11,4x | −21% | 4,6% | 5,3% | −0,7 pp | Coherente con el DCF. |
| EV/FCFF | 22,0x | 26,5x | −23% | 4,5% | 5,3% | −0,8 pp | Coherente con el DCF. |
| P/E | 15,7x | 21,3x | −26% | 4,4% | 6,1% | −1,7 pp | Revisar: el múltiplo vale 26% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 19,9x | 27,2x | −27% | 4,7% | 6,1% | −1,4 pp | Revisar: el múltiplo vale 27% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 12,3x | 15,8x | −22% | 5,0% | 6,1% | −1,1 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$144,80 | — |
| Múltiplos Base +20% | US$160,17 | +10,6% |
| Múltiplos Base −20% | US$129,42 | −10,6% |
| Crecimiento años 2-5 +2 pp | US$149,97 | +3,6% |
| Crecimiento años 2-5 −2 pp | US$140,08 | −3,3% |
| Margen objetivo +3 pp | US$156,23 | +7,9% |
| Margen objetivo −3 pp | US$133,36 | −7,9% |
| WACC +1 pp | US$140,98 | −2,6% |
| WACC −1 pp | US$148,88 | +2,8% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo −3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 7,05 | 7,09 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 9,79 | 9,66 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 12,62 | 11,97 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 14,10 | 14,10 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 22,01 | 22,01 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 24,93 | 24,93 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 11,74 | 11,75 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 15,71 | 15,74 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 19,92 | 19,83 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 12,67 | 12,67 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 19,85 | 19,88 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 23,48 | 23,60 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 8,50 | 8,42 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 12,32 | 12,28 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 15,54 | 15,26 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/LULU_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1wuEhOhrjlL5t-oSO9sRd7Py0Vw-47rv_4AAwaS8-ZJw/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-10-02 (NKE, ADDYY, ONON, DECK, BIRK, GAP, UAA).
- [lululemon, comunicado del 2T26, 3-sep-2026](https://www.sec.gov/Archives/edgar/data/1397187/000139718726000126/lulu-20260802xex991.htm)
- [lululemon, 10-K 2025, 17-mar-2026](https://www.sec.gov/Archives/edgar/data/1397187/000139718726000020/lulu-20260201.htm)

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
