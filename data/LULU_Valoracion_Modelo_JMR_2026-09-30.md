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

**Valor intrínseco principal · DCF Base hoy: US$175,88 por acción.** Complemento: DCF esperado por probabilidades US$155,59; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$72,45–US$248,28; precio con MOS 35% sobre el esperado: US$101,14; precio de referencia US$95,86. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Américas se estabiliza y crece lo internacional** (valor principal) | 45% | US$175,88 | US$79,15 |
| Conservadora · Pérdida de participación frente a Alo y Vuori | 30% | US$106,54 | US$31,96 |
| Disrupción · Deterioro de los fundamentales: la moda pasa y la marca se vuelve una más | 10% | US$72,45 | US$7,24 |
| Optimista · La nueva CEO recupera la marca | 15% | US$248,28 | US$37,24 |
| **DCF esperado (complemento)** | 100% | **US$155,59** | |

Lectura del 2-oct-2026: el DCF Base de las historias da ~US$171,6 por acción y los múltiplos consolidados ~US$135,7 hoy, ~21% menos, dentro del ±25%. La historia reciente de lululemon (7× EBITDA en Feb '26) y los peers deprimidos (Nike, Deckers, Gap) tiran los múltiplos hacia abajo. El DCF es el valor intrínseco; los múltiplos son precio relativo y, como el precio actual (US$95,86), están más cerca de la Conservadora que de la Base.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$175,88 | US$137,31 | US$152,74 | US$101,14 | US$204,59 |
| Conservador | US$106,54 | US$102,72 | US$104,25 | US$101,14 | US$130,63 |
| Optimista | US$248,28 | US$191,15 | US$214,00 | US$101,14 | US$303,77 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - LULU (desde cero 2026-10-02)](https://docs.google.com/spreadsheets/d/1wuEhOhrjlL5t-oSO9sRd7Py0Vw-47rv_4AAwaS8-ZJw/edit).
- Análisis del 01 de oct de 2026. Precio de referencia de la hoja: US$95,86.
- Peers: datos de mercado de yfinance consultados el 2026-10-02 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -8,7% | -6,5% | -3,7% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | -1,8% | 3,9% | 6,7% | Input B29 |
| Margen EBIT objetivo | 15,2% | 18,7% | 22,7% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,80 / 1,80 | — | Input B32/B33 |
| DCF por acción hoy | US$106,54 | US$175,88 | US$248,28 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,03, ERP 4,09%, Ke 9,50%, costo de la deuda después de impuestos 4,42%, peso del patrimonio 84,0%, WACC inicial 8,69% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: lululemon cotizó a 15-40 veces el EBITDA mientras crecía 15-25% al año (2017-2024). Desde 2025 Américas cae (comparables −3% en 2025 y −12% en el 2T26), el margen baja de 23,7% a ~17% normalizado y la guía de 2026 es de caída de ventas: la etapa actual es Feb '25, Feb '26 y el LTM. Su mediana mezcla el fin de la etapa anterior con el mínimo actual. B: ropa y calzado deportivo con datos de yfinance al 2-oct-2026: Nike, Adidas, On, Deckers, Birkenstock y Gap. Se excluye Under Armour (margen operativo negativo). Sin ajuste: margen operativo mayor que la mediana de los peers (17% objetivo frente a 7-15% de Nike, Adidas, Gap y Deckers), +5%; crecimiento a FY+3 menor que el de On, Adidas y Birkenstock, −5%; riesgo propio parecido (una marca, sin deuda). λ = 0,5: la lululemon de FY+3 (crecimiento de un dígito medio y margen ~16%) es distinta de la de la etapa de alto crecimiento; el justificado (C) usa los supuestos de cada escenario y equilibra la historia y los peers.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Feb '25, Feb '26, LTM (etapa actual) = 7,2x | 11,0x (n=6: NKE 11,0x, ADDYY 12,4x, ONON 19,2x, DECK 7,3x, BIRK 11,0x, GAP 7,6x) × 1,00 = 11,0x | 11,4x / 11,0x / 12,9x | **10,2x** | 8,7x | 13,1x | 9,8x / 7,0x / 12,6x |
| EV/FCFF | mediana Feb '25, Feb '26, LTM (etapa actual) = 21,7x (EV/FCF × 1,03 = FCF después de intereses ÷ FCFF) | 18,5x (n=6: NKE 24,8x, ADDYY 17,6x, ONON 21,1x, DECK 8,7x, BIRK 19,5x, GAP 10,9x) × 1,00 = 18,5x | 26,3x / 22,6x / 31,9x | **23,2x** | 17,3x | 27,4x | 22,0x / 14,1x / 24,9x |
| P/E | mediana Feb '25, Feb '26, LTM (etapa actual) = 13,2x | 16,1x (n=6: NKE 16,1x, ADDYY 18,3x, ONON 21,9x, DECK 11,3x, BIRK 16,1x, GAP 6,8x) × 1,00 = 16,1x | 19,0x / 16,1x / 23,0x | **16,8x** | 13,6x | 21,8x | 15,7x / 11,7x / 19,9x |
| P/FCFE | mediana Feb '25, Feb '26, LTM (etapa actual) = 21,1x | 17,2x (n=6: NKE 23,0x, ADDYY 15,5x, ONON 24,0x, DECK 9,6x, BIRK 18,9x, GAP 8,3x) × 1,00 = 17,2x | 23,3x / 20,3x / 27,6x | **21,2x** | 15,6x | 26,0x | 19,9x / 12,7x / 23,5x |
| P/OCF | mediana Feb '25, Feb '26, LTM (etapa actual) = 12,1x | 13,0x (n=6: NKE 17,5x, ADDYY 12,3x, ONON 19,6x, DECK 9,0x, BIRK 13,7x, GAP 5,2x) × 1,00 = 13,0x | 13,6x / 11,9x / 16,4x | **13,1x** | 10,3x | 16,8x | 12,3x / 8,5x / 15,5x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 10,2x: promedio de historia y peers 9,1x, acercado 50% al justificado (11,4x); rango de anclas 7,2x–11,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 23,2x: promedio de historia y peers 20,1x, acercado 50% al justificado (26,3x); rango de anclas 18,5x–26,3x. Atípicos excluidos de la historia: Jan '23 (115,0x: > 2,5x la mediana (33.0x)); LTM (8,4x: < 0,4x la mediana (33.0x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 16,8x: promedio de historia y peers 14,6x, acercado 50% al justificado (19,0x); rango de anclas 13,2x–19,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 21,2x: promedio de historia y peers 19,1x, acercado 50% al justificado (23,3x); rango de anclas 17,2x–23,3x. Atípicos excluidos de la historia: Jan '23 (115,9x: > 2,5x la mediana (35.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 13,1x: promedio de historia y peers 12,6x, acercado 50% al justificado (13,6x); rango de anclas 12,1x–13,6x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$137,31 frente a US$175,88 del DCF (−22%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$137,31 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,50%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$72,45) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$175,88 por acción.** Complemento: DCF esperado por probabilidades US$155,59. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$175,88 | US$106,54 | US$248,28 |
| EV/EBITDA | 10,2× / 8,7× / 13,1× | 20% | 33% | US$140,75 | US$104,51 | US$208,58 |
| EV/FCFF | 23,2× / 17,3× / 27,4× | 10% | 17% | US$137,87 | US$110,45 | US$156,40 |
| P/E | 16,8× / 13,6× / 21,8× | 20% | 33% | US$132,28 | US$92,76 | US$199,82 |
| P/FCFE | 21,2× / 15,6× / 26,0× | 5% | 8% | US$133,62 | US$105,88 | US$158,04 |
| P/OCF | 13,1× / 10,3× / 16,8× | 5% | 8% | US$146,30 | US$116,74 | US$189,38 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$137,31 | US$102,72 | US$191,15 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$152,74 | US$104,25 | US$214,00 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$230,93 | US$139,88 | US$326,00 |
| EV/EBITDA | 10,2× / 8,7× / 13,1× | 20% | 33% | US$191,27 | US$130,14 | US$305,37 |
| EV/FCFF | 23,2× / 17,3× / 27,4× | 10% | 17% | US$187,76 | US$125,54 | US$256,28 |
| P/E | 16,8× / 13,6× / 21,8× | 20% | 33% | US$182,80 | US$116,36 | US$299,84 |
| P/FCFE | 21,2× / 15,6× / 26,0× | 5% | 8% | US$181,32 | US$120,85 | US$256,33 |
| P/OCF | 13,1× / 10,3× / 16,8× | 5% | 8% | US$191,21 | US$135,65 | US$277,74 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 60% | 100% | US$187,03 | US$124,46 | US$288,95 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$204,59 | US$130,63 | US$303,77 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,50%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$132,91 | US$143,66 | US$145,67 | US$140,75 | OK |
| EV/EBITDA | Conservador | US$109,65 | US$104,77 | US$99,11 | US$104,51 | OK |
| EV/EBITDA | Optimista | US$177,37 | US$215,80 | US$232,57 | US$208,58 | OK |
| EV/FCFF | Base | US$131,71 | US$138,90 | US$142,99 | US$137,87 | OK |
| EV/FCFF | Conservador | US$128,09 | US$107,64 | US$95,61 | US$110,45 | OK |
| EV/FCFF | Optimista | US$111,55 | US$162,47 | US$195,18 | US$156,40 | OK |
| P/E | Base | US$121,92 | US$135,70 | US$139,22 | US$132,28 | OK |
| P/E | Conservador | US$96,47 | US$93,19 | US$88,62 | US$92,76 | OK |
| P/E | Optimista | US$162,89 | US$208,22 | US$228,36 | US$199,82 | OK |
| P/FCFE | Base | US$128,12 | US$134,64 | US$138,09 | US$133,62 | OK |
| P/FCFE | Conservador | US$122,25 | US$103,35 | US$92,04 | US$105,88 | OK |
| P/FCFE | Optimista | US$114,90 | US$164,01 | US$195,22 | US$158,04 | OK |
| P/OCF | Base | US$146,71 | US$146,58 | US$145,63 | US$146,30 | OK |
| P/OCF | Conservador | US$132,35 | US$114,56 | US$103,31 | US$116,74 | OK |
| P/OCF | Optimista | US$163,57 | US$193,06 | US$211,53 | US$189,38 | OK |

Múltiplos consolidados hoy: US$137,31 / US$102,72 / US$191,15 · DCF de las historias hoy: US$175,88 / US$106,54 / US$248,28 · Ponderado hoy: US$152,74 / US$104,25 / US$214,00 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para LULU la diferencia es de −22% (múltiplos por debajo del DCF). Lectura del 2-oct-2026: el DCF Base de las historias da ~US$171,6 por acción y los múltiplos consolidados ~US$135,7 hoy, ~21% menos, dentro del ±25%. La historia reciente de lululemon (7× EBITDA en Feb '26) y los peers deprimidos (Nike, Deckers, Gap) tiran los múltiplos hacia abajo. El DCF es el valor intrínseco; los múltiplos son precio relativo y, como el precio actual (US$95,86), están más cerca de la Conservadora que de la Base.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$95,86 supone que los ingresos crecen -13,3% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 1,8% (−15,1 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$230,93 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,5%, WACC de los años 4-10 9,0%, ROE de FY+3 27,0% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 10,2x | 11,4x | −17% | 4,6% | 5,0% | −0,4 pp | Coherente con el DCF. |
| EV/FCFF | 23,2x | 26,3x | −19% | 4,5% | 5,0% | −0,5 pp | Coherente con el DCF. |
| P/E | 16,8x | 21,2x | −21% | 4,3% | 5,5% | −1,3 pp | Coherente con el DCF. |
| P/FCFE | 21,2x | 27,0x | −21% | 4,6% | 5,6% | −1,0 pp | Coherente con el DCF. |
| P/OCF | 13,1x | 15,8x | −17% | 4,8% | 5,6% | −0,8 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$152,74 | — |
| Múltiplos Base +20% | US$169,50 | +11,0% |
| Múltiplos Base −20% | US$135,98 | −11,0% |
| Crecimiento años 2-5 +2 pp | US$158,13 | +3,5% |
| Crecimiento años 2-5 −2 pp | US$147,83 | −3,2% |
| Margen objetivo +3 pp | US$164,26 | +7,5% |
| Margen objetivo −3 pp | US$141,22 | −7,5% |
| WACC +1 pp | US$148,79 | −2,6% |
| WACC −1 pp | US$156,97 | +2,8% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 7,05 | 8,70 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 9,79 | 10,22 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 12,62 | 13,11 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 14,10 | 17,29 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 22,01 | 23,20 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 24,93 | 27,36 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 11,74 | 13,61 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 15,71 | 16,80 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 19,92 | 21,78 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 12,67 | 15,58 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 19,85 | 21,20 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 23,48 | 26,03 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 8,50 | 10,28 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 12,32 | 13,11 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 15,54 | 16,83 | Múltiplo optimista elegido con el protocolo v3 |
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
