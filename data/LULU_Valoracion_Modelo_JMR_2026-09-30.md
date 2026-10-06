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

**Valor intrínseco principal · DCF Base hoy: US$191,62 por acción.** Complemento: DCF esperado por probabilidades US$168,01; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$75,45–US$271,28; precio con MOS 35% sobre el esperado: US$109,20; precio de referencia US$95,86. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Américas se estabiliza y crece lo internacional** (valor principal) | 45% | US$191,62 | US$86,23 |
| Conservadora · Pérdida de participación frente a Alo y Vuori | 30% | US$111,81 | US$33,54 |
| Disrupción · Deterioro de los fundamentales: la moda pasa y la marca se vuelve una más | 10% | US$75,45 | US$7,54 |
| Optimista · La nueva CEO recupera la marca | 15% | US$271,28 | US$40,69 |
| **DCF esperado (complemento)** | 100% | **US$168,01** | |

Lectura del 2-oct-2026: el DCF Base de las historias da ~US$171,6 por acción y los múltiplos consolidados ~US$135,7 hoy, ~21% menos, dentro del ±25%. La historia reciente de lululemon (7× EBITDA en Feb '26) y los peers deprimidos (Nike, Deckers, Gap) tiran los múltiplos hacia abajo. El DCF es el valor intrínseco; los múltiplos son precio relativo y, como el precio actual (US$95,86), están más cerca de la Conservadora que de la Base.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$191,62 | US$145,85 | US$164,16 | US$109,20 | US$217,89 |
| Conservador | US$111,81 | US$108,55 | US$109,85 | US$109,20 | US$136,47 |
| Optimista | US$271,28 | US$204,21 | US$231,04 | US$109,20 | US$324,77 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - LULU (desde cero 2026-10-02)](https://docs.google.com/spreadsheets/d/1wuEhOhrjlL5t-oSO9sRd7Py0Vw-47rv_4AAwaS8-ZJw/edit).
- Análisis del 06 de mar de 2026. Precio de referencia de la hoja: US$95,86.
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
| DCF por acción hoy | US$111,81 | US$191,62 | US$271,28 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 0,91, ERP 4,21%, Ke 9,11%, costo de la deuda después de impuestos 4,42%, peso del patrimonio 84,0%, WACC inicial 8,36% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: lululemon cotizó a 15-40 veces el EBITDA mientras crecía 15-25% al año (2017-2024). Desde 2025 Américas cae (comparables −3% en 2025 y −12% en el 2T26), el margen baja de 23,7% a ~17% normalizado y la guía de 2026 es de caída de ventas: la etapa actual es Feb '25, Feb '26 y el LTM. Su mediana mezcla el fin de la etapa anterior con el mínimo actual. B: ropa y calzado deportivo con datos de yfinance al 2-oct-2026: Nike, Adidas, On, Deckers, Birkenstock y Gap. Se excluye Under Armour (margen operativo negativo). Sin ajuste: margen operativo mayor que la mediana de los peers (17% objetivo frente a 7-15% de Nike, Adidas, Gap y Deckers), +5%; crecimiento a FY+3 menor que el de On, Adidas y Birkenstock, −5%; riesgo propio parecido (una marca, sin deuda). λ = 0,5: la lululemon de FY+3 (crecimiento de un dígito medio y margen ~16%) es distinta de la de la etapa de alto crecimiento; el justificado (C) usa los supuestos de cada escenario y equilibra la historia y los peers.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Feb '25, Feb '26, LTM (etapa actual) = 7,2x | 11,0x (n=6: NKE 11,0x, ADDYY 12,4x, ONON 19,2x, DECK 7,3x, BIRK 11,0x, GAP 7,6x) × 1,00 = 11,0x | 12,5x / 11,9x / 14,4x | **10,8x** | 9,1x | 13,9x | 9,8x / 7,0x / 12,6x |
| EV/FCFF | mediana Feb '25, Feb '26, LTM (etapa actual) = 21,7x (EV/FCF × 1,03 = FCF después de intereses ÷ FCFF) | 18,5x (n=6: NKE 24,8x, ADDYY 17,6x, ONON 21,1x, DECK 8,7x, BIRK 19,5x, GAP 10,9x) × 1,00 = 18,5x | 28,8x / 24,5x / 35,7x | **24,5x** | 18,1x | 29,1x | 22,0x / 14,1x / 24,9x |
| P/E | mediana Feb '25, Feb '26, LTM (etapa actual) = 13,2x | 16,1x (n=6: NKE 16,1x, ADDYY 18,3x, ONON 21,9x, DECK 11,3x, BIRK 16,1x, GAP 6,8x) × 1,00 = 16,1x | 20,8x / 17,5x / 25,6x | **17,7x** | 14,3x | 23,1x | 15,7x / 11,7x / 19,9x |
| P/FCFE | mediana Feb '25, Feb '26, LTM (etapa actual) = 21,1x | 17,2x (n=6: NKE 23,0x, ADDYY 15,5x, ONON 24,0x, DECK 9,6x, BIRK 18,9x, GAP 8,3x) × 1,00 = 17,2x | 25,4x / 22,0x / 30,7x | **22,3x** | 16,3x | 27,5x | 19,9x / 12,7x / 23,5x |
| P/OCF | mediana Feb '25, Feb '26, LTM (etapa actual) = 12,1x | 13,0x (n=6: NKE 17,5x, ADDYY 12,3x, ONON 19,6x, DECK 9,0x, BIRK 13,7x, GAP 5,2x) × 1,00 = 13,0x | 14,9x / 12,9x / 18,3x | **13,8x** | 10,7x | 17,8x | 12,3x / 8,5x / 15,5x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 10,8x: promedio de historia y peers 9,1x, acercado 50% al justificado (12,5x); rango de anclas 7,2x–12,5x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 24,5x: promedio de historia y peers 20,1x, acercado 50% al justificado (28,8x); rango de anclas 18,5x–28,8x. Atípicos excluidos de la historia: Jan '23 (115,0x: > 2,5x la mediana (33.0x)); LTM (8,4x: < 0,4x la mediana (33.0x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 17,7x: promedio de historia y peers 14,6x, acercado 50% al justificado (20,8x); rango de anclas 13,2x–20,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 22,3x: promedio de historia y peers 19,1x, acercado 50% al justificado (25,4x); rango de anclas 17,2x–25,4x. Atípicos excluidos de la historia: Jan '23 (115,9x: > 2,5x la mediana (35.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 13,8x: promedio de historia y peers 12,6x, acercado 50% al justificado (14,9x); rango de anclas 12,1x–14,9x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$145,85 frente a US$191,62 del DCF (−24%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$145,85 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,11%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$75,45) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$191,62 por acción.** Complemento: DCF esperado por probabilidades US$168,01. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$191,62 | US$111,81 | US$271,28 |
| EV/EBITDA | 10,8× / 9,1× / 13,9× | 20% | 33% | US$149,80 | US$110,56 | US$223,08 |
| EV/FCFF | 24,5× / 18,1× / 29,1× | 10% | 17% | US$146,73 | US$116,96 | US$167,77 |
| P/E | 17,7× / 14,3× / 23,1× | 20% | 33% | US$140,38 | US$98,01 | US$213,25 |
| P/FCFE | 22,3× / 16,3× / 27,5× | 5% | 8% | US$141,50 | US$111,60 | US$168,45 |
| P/OCF | 13,8× / 10,7× / 17,8× | 5% | 8% | US$154,54 | US$122,80 | US$201,23 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$145,85 | US$108,55 | US$204,21 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$164,16 | US$109,85 | US$231,04 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$248,93 | US$145,25 | US$352,41 |
| EV/EBITDA | 10,8× / 9,1× / 13,9× | 20% | 33% | US$202,06 | US$136,69 | US$324,11 |
| EV/FCFF | 24,5× / 18,1× / 29,1× | 10% | 17% | US$198,34 | US$132,06 | US$272,65 |
| P/E | 17,7× / 14,3× / 23,1× | 20% | 33% | US$192,59 | US$122,09 | US$317,60 |
| P/FCFE | 22,3× / 16,3× / 27,5× | 5% | 8% | US$190,64 | US$126,52 | US$271,10 |
| P/OCF | 13,8× / 10,7× / 17,8× | 5% | 8% | US$200,55 | US$141,72 | US$292,92 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 60% | 100% | US$197,21 | US$130,62 | US$306,34 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$217,89 | US$136,47 | US$324,77 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,11%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$140,98 | US$152,88 | US$155,54 | US$149,80 | OK |
| EV/EBITDA | Conservador | US$115,61 | US$110,84 | US$105,22 | US$110,56 | OK |
| EV/EBITDA | Optimista | US$189,04 | US$230,72 | US$249,49 | US$223,08 | OK |
| EV/FCFF | Base | US$139,70 | US$147,81 | US$152,68 | US$146,73 | OK |
| EV/FCFF | Conservador | US$135,19 | US$114,04 | US$101,66 | US$116,96 | OK |
| EV/FCFF | Optimista | US$119,27 | US$174,15 | US$209,88 | US$167,77 | OK |
| P/E | Base | US$128,90 | US$143,99 | US$148,25 | US$140,38 | OK |
| P/E | Conservador | US$101,58 | US$98,48 | US$93,98 | US$98,01 | OK |
| P/E | Optimista | US$173,15 | US$222,13 | US$244,48 | US$213,25 | OK |
| P/FCFE | Base | US$135,19 | US$142,57 | US$146,75 | US$141,50 | OK |
| P/FCFE | Conservador | US$128,44 | US$108,97 | US$97,39 | US$111,60 | OK |
| P/FCFE | Optimista | US$121,96 | US$174,70 | US$208,69 | US$168,45 | OK |
| P/OCF | Base | US$154,42 | US$154,83 | US$154,37 | US$154,54 | OK |
| P/OCF | Conservador | US$138,77 | US$120,55 | US$109,09 | US$122,80 | OK |
| P/OCF | Optimista | US$173,13 | US$205,07 | US$225,48 | US$201,23 | OK |

Múltiplos consolidados hoy: US$145,85 / US$108,55 / US$204,21 · DCF de las historias hoy: US$191,62 / US$111,81 / US$271,28 · Ponderado hoy: US$164,16 / US$109,85 / US$231,04 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para LULU la diferencia es de −24% (múltiplos por debajo del DCF). Lectura del 2-oct-2026: el DCF Base de las historias da ~US$171,6 por acción y los múltiplos consolidados ~US$135,7 hoy, ~21% menos, dentro del ±25%. La historia reciente de lululemon (7× EBITDA en Feb '26) y los peers deprimidos (Nike, Deckers, Gap) tiran los múltiplos hacia abajo. El DCF es el valor intrínseco; los múltiplos son precio relativo y, como el precio actual (US$95,86), están más cerca de la Conservadora que de la Base.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$95,86 supone que los ingresos crecen -14,7% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 1,8% (−16,5 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$248,93 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,1%, WACC de los años 4-10 8,6%, ROE de FY+3 27,0% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 10,8x | 12,3x | −19% | 4,4% | 4,9% | −0,5 pp | Coherente con el DCF. |
| EV/FCFF | 24,5x | 28,5x | −20% | 4,4% | 4,9% | −0,6 pp | Coherente con el DCF. |
| P/E | 17,7x | 22,9x | −23% | 4,1% | 5,4% | −1,3 pp | Coherente con el DCF. |
| P/FCFE | 22,3x | 29,1x | −23% | 4,4% | 5,5% | −1,1 pp | Coherente con el DCF. |
| P/OCF | 13,8x | 17,1x | −19% | 4,7% | 5,5% | −0,8 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$164,16 | — |
| Múltiplos Base +20% | US$181,94 | +10,8% |
| Múltiplos Base −20% | US$146,37 | −10,8% |
| Crecimiento años 2-5 +2 pp | US$170,28 | +3,7% |
| Crecimiento años 2-5 −2 pp | US$158,59 | −3,4% |
| Margen objetivo +3 pp | US$176,70 | +7,6% |
| Margen objetivo −3 pp | US$151,62 | −7,6% |
| WACC +1 pp | US$159,81 | −2,6% |
| WACC −1 pp | US$168,82 | +2,8% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 7,05 | 9,12 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 9,79 | 10,78 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 12,62 | 13,90 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 14,10 | 18,15 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 22,01 | 24,47 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 24,93 | 29,07 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 11,74 | 14,28 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 15,71 | 17,70 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 19,92 | 23,07 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 12,67 | 16,31 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 19,85 | 22,29 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 23,48 | 27,53 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 8,50 | 10,74 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 12,32 | 13,75 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 15,54 | 17,75 | Múltiplo optimista elegido con el protocolo v3 |
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
