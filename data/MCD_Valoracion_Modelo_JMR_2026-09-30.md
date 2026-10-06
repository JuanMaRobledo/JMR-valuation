---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de MCDONALDS CORP"
ticker: "MCD"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1D44qNMrcbmbDbWuGO4EdFJdWdg9xE6cYg_pDCwLb30M/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# MCDONALDS CORP (MCD) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$224,12 por acción.** Complemento: DCF esperado por probabilidades US$203,96; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$75,44–US$253,34; precio con MOS 35% sobre el esperado: US$132,57; precio de referencia US$230,94. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Refranquiciamiento a 98% y comparables de 2-3%** (valor principal) | 50% | US$224,12 | US$112,06 |
| Conservadora · El tráfico de EE.UU. no vuelve y el valor cuesta margen | 25% | US$185,42 | US$46,35 |
| Disrupción · Deterioro de los fundamentales: Los franquiciados pierden rentabilidad y la renta deja de crecer | 10% | US$75,44 | US$7,54 |
| Optimista · NEXT recupera el tráfico y la escala se nota en el margen | 15% | US$253,34 | US$38,00 |
| **DCF esperado (complemento)** | 100% | **US$203,96** | |

Lectura del 6-oct-2026 (análisis desde cero): los múltiplos consolidados Base hoy (US$279,64) valen 25% más que el DCF Base (US$224,12), en el límite del ±25%. No se movió ningún múltiplo para acercarlos. La causa es de crecimiento del BPA: la historia de cinco años (P/E 25,6×) se formó cuando el BPA crecía ~8-10% al año, y la Base del DCF supone ingresos casi planos por el refranquiciamiento y un margen que sube poco a poco. El chequeo de crecimiento implícito no da alertas (los cinco múltiplos Base difieren menos de 1 pp del que implica el DCF en FY+3). El DCF es la lectura más confiable; los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$224,12 | US$279,64 | US$257,43 | US$132,57 | US$307,67 |
| Conservador | US$185,42 | US$251,29 | US$224,94 | US$132,57 | US$263,70 |
| Optimista | US$253,34 | US$301,64 | US$282,32 | US$132,57 | US$341,89 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - MCD (desde cero 2026-10-06)](https://docs.google.com/spreadsheets/d/1D44qNMrcbmbDbWuGO4EdFJdWdg9xE6cYg_pDCwLb30M/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$230,94.
- Peers: datos de mercado de yfinance consultados el 2026-10-06 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -2,2% | -0,9% | -0,2% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | -5,9% | 1,5% | -3,6% | Input B29 |
| Margen EBIT objetivo | 51,5% | 55,5% | 58,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 0,50 / 0,50 | — | Input B32/B33 |
| DCF por acción hoy | US$185,42 | US$224,12 | US$253,34 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 0,79, ERP 4,33%, Ke 8,69%, costo de la deuda después de impuestos 5,35%, peso del patrimonio 79,9%, WACC inicial 8,02% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: McDonald's es un franquiciador maduro desde hace décadas; no hubo cambio de etapa del negocio, así que A usa la mediana de los últimos cinco cierres (FY2021-FY2025) y el LTM. El LTM (P/E 18,9×, EV/EBITDA 13,7×) es el más bajo de la década: refleja la caída de la acción en 2026 (tráfico débil en EE.UU. y el plan NEXT), no un cambio de etapa. B: franquiciadores de comida rápida con datos de yfinance al 6-oct-2026 (precios del 2-oct): Yum! Brands, Restaurant Brands International y Domino's. Se excluyen Wendy's (seis trimestres de comparables negativas, −7% en el 2T26; P/OCF 3×), Papa John's (ingresos −8,8%, reestructuración) y Chipotle (opera sus locales: otro modelo de negocio). Ajuste +5%: crecimiento de los ingresos reportados a FY+3 menor que la mediana por el refranquiciamiento (~1-4% frente a 4-12%), −5%, aunque las ventas del sistema crecen parecido (~5%); margen operativo mayor (~50% frente a 19-33%), +5%; riesgo menor (calificación Baa1/BBB+ frente a grado especulativo de Yum! y RBI, beta ~0,8, propiedad de los inmuebles), +5%. λ = 0,25: la empresa de FY+3 se parece a la de hoy (franquiciador maduro), así que el Base se apoya sobre todo en la historia y en los peers. P/E no tiene justificado: el patrimonio contable es negativo (−US$1.023 millones por US$80.527 millones de recompras acumuladas), así que el ROE no tiene sentido y el Base de P/E es el promedio de A y B.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana de los últimos 5 cierres + LTM depurados = 18,3x | 14,4x (n=3: YUM 16,3x, QSR 13,8x, DPZ 14,5x) × 1,05 = 15,2x | 16,6x / 15,7x / 17,0x | **16,7x** | 15,6x | 17,4x | 17,9x / —x / —x |
| EV/FCFF | mediana de los últimos 5 cierres + LTM depurados = 31,0x (EV/FCF × 0,87 = FCF después de intereses ÷ FCFF) | 19,9x (n=3: YUM 24,0x, QSR 19,9x, DPZ 18,3x) × 1,05 = 20,9x | 31,5x / 27,5x / 34,9x | **27,4x** | 25,0x | 30,6x | 27,3x / —x / —x |
| P/E | mediana de los últimos 5 cierres + LTM depurados = 25,6x | 17,2x (n=3: YUM 17,3x, QSR 17,6x, DPZ 16,9x) × 1,05 = 18,1x | — / — / — | **21,9x** | 21,2x | 22,5x | 25,4x / —x / —x |
| P/FCFE | mediana de los últimos 5 cierres + LTM depurados = 30,2x | 19,6x (n=3: YUM 22,3x, QSR 19,6x, DPZ 15,0x) × 1,05 = 20,6x | 29,2x / 25,7x / 32,1x | **26,4x** | 23,5x | 28,9x | 22,5x / —x / —x |
| P/OCF | mediana de los últimos 5 cierres + LTM depurados = 22,1x | 16,8x (n=3: YUM 17,9x, QSR 16,8x, DPZ 12,6x) × 1,05 = 17,6x | 22,9x / 19,2x / 26,4x | **20,6x** | 17,8x | 22,5x | 19,2x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 16,7x: promedio de historia y peers 16,7x, acercado 25% al justificado (16,6x); rango de anclas 15,2x–18,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 27,4x: promedio de historia y peers 26,0x, acercado 25% al justificado (31,5x); rango de anclas 20,9x–31,5x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 21,9x: promedio de historia y peers 21,9x, acercado 25% al justificado (—x); rango de anclas 18,1x–25,6x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 26,4x: promedio de historia y peers 25,4x, acercado 25% al justificado (29,2x); rango de anclas 20,6x–30,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 20,6x: promedio de historia y peers 19,9x, acercado 25% al justificado (22,9x); rango de anclas 17,6x–22,9x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$279,64 frente a US$224,12 del DCF (+25%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$279,64 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 8,69%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$75,44) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$224,12 por acción.** Complemento: DCF esperado por probabilidades US$203,96. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$224,12 | US$185,42 | US$253,34 |
| EV/EBITDA | 16,7× / 15,6× / 17,4× | 20% | 33% | US$269,57 | US$234,71 | US$292,75 |
| EV/FCFF | 27,4× / 25,0× / 30,6× | 10% | 17% | US$299,74 | US$276,43 | US$329,03 |
| P/E | 21,9× / 21,2× / 22,5× | 20% | 33% | US$263,26 | US$243,81 | US$279,45 |
| P/FCFE | 26,4× / 23,5× / 28,9× | 5% | 8% | US$306,94 | US$268,12 | US$336,32 |
| P/OCF | 20,6× / 17,8× / 22,5× | 5% | 8% | US$317,91 | US$280,42 | US$336,50 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$279,64 | US$251,29 | US$301,64 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$257,43 | US$224,94 | US$282,32 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$287,78 | US$238,09 | US$325,31 |
| EV/EBITDA (total con dividendos) | 16,7× / 15,6× / 17,4× | 20% | 33% | US$334,42 | US$281,67 | US$372,13 |
| EV/FCFF (total con dividendos) | 27,4× / 25,0× / 30,6× | 10% | 17% | US$282,21 | US$255,28 | US$313,50 |
| P/E (total con dividendos) | 21,9× / 21,2× / 22,5× | 20% | 33% | US$326,35 | US$293,29 | US$354,09 |
| P/FCFE (total con dividendos) | 26,4× / 23,5× / 28,9× | 5% | 8% | US$321,79 | US$277,13 | US$360,58 |
| P/OCF (total con dividendos) | 20,6× / 17,8× / 22,5× | 5% | 8% | US$321,79 | US$281,71 | US$342,93 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$320,92 | US$280,77 | US$352,95 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$25,58 | US$25,58 | US$25,58 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$295,34 | US$255,19 | US$327,37 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$307,67 | US$263,70 | US$341,89 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 8,69%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$281,87 | US$264,71 | US$262,13 | US$269,57 | OK |
| EV/EBITDA | Conservador | US$254,54 | US$228,53 | US$221,05 | US$234,71 | OK |
| EV/EBITDA | Optimista | US$297,97 | US$288,78 | US$291,50 | US$292,75 | OK |
| EV/FCFF | Base | US$407,85 | US$269,91 | US$221,47 | US$299,74 | OK |
| EV/FCFF | Conservador | US$383,78 | US$245,00 | US$200,50 | US$276,43 | OK |
| EV/FCFF | Optimista | US$443,05 | US$298,20 | US$245,84 | US$329,03 | OK |
| P/E | Base | US$274,40 | US$259,54 | US$255,84 | US$263,26 | OK |
| P/E | Conservador | US$262,68 | US$238,66 | US$230,10 | US$243,81 | OK |
| P/E | Optimista | US$284,31 | US$276,59 | US$277,45 | US$279,45 | OK |
| P/FCFE | Base | US$447,31 | US$221,21 | US$252,29 | US$306,94 | OK |
| P/FCFE | Conservador | US$397,77 | US$189,08 | US$217,52 | US$268,12 | OK |
| P/FCFE | Optimista | US$480,24 | US$246,23 | US$282,51 | US$336,32 | OK |
| P/OCF | Base | US$407,43 | US$294,01 | US$252,29 | US$317,91 | OK |
| P/OCF | Conservador | US$363,18 | US$256,99 | US$221,09 | US$280,42 | OK |
| P/OCF | Optimista | US$428,49 | US$312,24 | US$268,76 | US$336,50 | OK |

Múltiplos consolidados hoy: US$279,64 / US$251,29 / US$301,64 · DCF de las historias hoy: US$224,12 / US$185,42 / US$253,34 · Ponderado hoy: US$257,43 / US$224,94 / US$282,32 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para MCD la diferencia es de +25% (múltiplos por encima del DCF). Lectura del 6-oct-2026 (análisis desde cero): los múltiplos consolidados Base hoy (US$279,64) valen 25% más que el DCF Base (US$224,12), en el límite del ±25%. No se movió ningún múltiplo para acercarlos. La causa es de crecimiento del BPA: la historia de cinco años (P/E 25,6×) se formó cuando el BPA crecía ~8-10% al año, y la Base del DCF supone ingresos casi planos por el refranquiciamiento y un margen que sube poco a poco. El chequeo de crecimiento implícito no da alertas (los cinco múltiplos Base difieren menos de 1 pp del que implica el DCF en FY+3). El DCF es la lectura más confiable; los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$230,94 supone que los ingresos crecen -3,4% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 1,1% (−4,4 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$287,78 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 8,7%, WACC de los años 4-10 8,4%, ROE de FY+3 — y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 16,7x | 14,0x | +16% | 5,1% | 4,5% | +0,6 pp | Coherente con el DCF. |
| EV/FCFF | 27,4x | 26,6x | −2% | 4,6% | 4,5% | +0,1 pp | Coherente con el DCF. |
| P/E | 21,9x | 19,1x | +13% | — | — | — | Coherente con el DCF. |
| P/FCFE | 26,4x | 23,3x | +12% | 4,7% | 4,2% | +0,5 pp | Coherente con el DCF. |
| P/OCF | 20,6x | 18,3x | +12% | 4,7% | 4,2% | +0,5 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$257,43 | — |
| Múltiplos Base +20% | US$292,96 | +13,8% |
| Múltiplos Base −20% | US$221,90 | −13,8% |
| Crecimiento años 2-5 +2 pp | US$266,90 | +3,7% |
| Crecimiento años 2-5 −2 pp | US$248,86 | −3,3% |
| Margen objetivo +3 pp | US$263,44 | +2,3% |
| Margen objetivo −3 pp | US$251,42 | −2,3% |
| WACC +1 pp | US$250,81 | −2,6% |
| WACC −1 pp | US$264,51 | +2,8% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 15,56 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 17,85 | 16,69 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 17,36 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 25,02 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 27,28 | 27,35 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 30,65 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 21,18 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 25,45 | 21,86 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 22,52 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 23,47 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 22,53 | 26,35 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 28,91 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 17,79 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 19,23 | 20,62 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 22,49 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/MCD_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1D44qNMrcbmbDbWuGO4EdFJdWdg9xE6cYg_pDCwLb30M/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-10-06 (YUM, QSR, DPZ, WEN, PZZA, CMG).
- [McDonald's, 10-Q del 2T26, 7-ago-2026](https://www.sec.gov/Archives/edgar/data/63908/000006390826000073/mcd-20260630.htm)
- [McDonald's, 10-K 2025, 24-feb-2026](https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm)
- [Restaurant Dive, ventas comparables de 18 cadenas, 27-ago-2026](https://www.restaurantdive.com/news/tracking-same-store-sales-18-major-restaurant-chains/742371/)

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
