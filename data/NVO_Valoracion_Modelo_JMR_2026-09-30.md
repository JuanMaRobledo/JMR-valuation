---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Novo Nordisk A/S"
ticker: "NVO"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1_w85o-Cv_4GzFB4nq5fGqrMSVoYf-Ltafuol3ir5TMw/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Novo Nordisk A/S (NVO) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$33,17 por acción.** Complemento: DCF esperado por probabilidades US$31,29; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$21,11–US$40,49; precio con MOS 35% sobre el esperado: US$20,34; precio de referencia US$37,91. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · El volumen compensa la caída de precio** (valor principal) | 40% | US$33,17 | US$13,27 |
| Conservadora · Guerra de precios con Lilly y genéricos | 30% | US$26,03 | US$7,81 |
| Disrupción · Deterioro de los fundamentales: Novo pierde relevancia frente a Lilly | 10% | US$21,11 | US$2,11 |
| Optimista · La nueva generación recupera el liderazgo | 20% | US$40,49 | US$8,10 |
| **DCF esperado (complemento)** | 100% | **US$31,29** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$41,96 por acción y los múltiplos, US$42,59 hoy: 1% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$33,17 | US$51,45 | US$44,14 | US$20,34 | US$55,72 |
| Conservador | US$26,03 | US$43,35 | US$36,42 | US$20,34 | US$43,97 |
| Optimista | US$40,49 | US$59,40 | US$51,84 | US$20,34 | US$67,00 |

## 2. Datos

- Hoja del modelo: [NVO_Modelo_JMR_Valoracion_2026-09-24](https://docs.google.com/spreadsheets/d/1_w85o-Cv_4GzFB4nq5fGqrMSVoYf-Ltafuol3ir5TMw/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$37,91.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -7,7% | -3,0% | 0,2% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | -2,9% | 4,5% | 3,9% | Input B29 |
| Margen EBIT objetivo | 35,0% | 40,0% | 43,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 0,57 / 1,10 | — | Input B32/B33 |
| DCF por acción hoy | US$26,03 | US$33,17 | US$40,49 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 0,99, ERP 4,54%, Ke 9,81%, costo de la deuda después de impuestos 4,56%, peso del patrimonio 89,9%, WACC inicial 9,28% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Novo Nordisk cotizó a 16-27x EBITDA y 23-36x utilidades durante el auge de Ozempic y Wegovy. Desde 2025 perdió participación frente a Eli Lilly, bajó precios en EE. UU. (Wegovy a US$349 al mes en pago directo) y en febrero de 2026 guió una caída de ventas de 5-13% (luego −6% a 0%); la acción cayó de US$59 a US$39 en tres semanas. La etapa actual es Dec '25 y el LTM. Se excluye la columna sin fecha de la hoja. B: farmacéuticas grandes (AstraZeneca, Novartis, Sanofi, Merck, Pfizer), datos de yfinance al 29-sep-2026. Se excluye Eli Lilly (crece 48% justamente a costa de Novo; su múltiplo es de otra etapa) y, en P/E, Merck (119x por cargos puntuales de I+D adquirida). Ajuste −5%: Novo decrece en 2026 mientras los peers crecen 1-15%, aunque conserva márgenes más altos. λ = 0,25: la Novo de FY+3 del escenario Base es una farmacéutica de crecimiento bajo con márgenes altos, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 9,4x | 13,8x (n=5: AZN 14,2x, NVS 13,8x, SNY 8,5x, MRK 14,3x, PFE 8,5x) × 0,95 = 13,1x | 8,3x / 8,3x / 8,5x | **10,5x** | 8,8x | 11,0x | 11,1x / —x / —x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 22,4x (EV/FCF × 1,05 = FCF después de intereses ÷ FCFF) | 21,8x (n=4: AZN 38,0x, NVS 19,8x, MRK 23,7x, PFE 16,5x) × 0,95 = 20,7x | 12,9x / 11,2x / 15,4x | **19,4x** | 16,8x | 23,1x | 22,5x / 19,9x / 26,1x |
| P/E | mediana Dec '25, LTM (etapa actual) = 12,0x | 23,4x (n=4: AZN 24,6x, NVS 22,0x, SNY 22,1x, PFE 37,8x) × 0,95 = 22,2x | 11,6x / 10,4x / 13,4x | **15,7x** | 14,3x | 18,1x | 14,4x / —x / —x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 19,8x | 20,7x (n=4: AZN 42,1x, NVS 18,5x, MRK 22,9x, PFE 14,9x) × 0,95 = 19,7x | 11,9x / 10,4x / 14,0x | **17,8x** | 15,3x | 21,6x | 17,0x / —x / —x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 10,4x | 16,8x (n=4: AZN 18,6x, NVS 15,1x, MRK 18,4x, PFE 12,2x) × 0,95 = 15,9x | 8,3x / 7,1x / 9,7x | **11,9x** | 10,4x | 13,4x | 13,9x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 10,5x: promedio de historia y peers 11,2x, acercado 25% al justificado (8,3x); rango de anclas 8,3x–13,1x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 19,4x: promedio de historia y peers 21,5x, acercado 25% al justificado (12,9x); rango de anclas 12,9x–22,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 15,7x: promedio de historia y peers 17,1x, acercado 25% al justificado (11,6x); rango de anclas 11,6x–22,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 17,8x: promedio de historia y peers 19,7x, acercado 25% al justificado (11,9x); rango de anclas 11,9x–19,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 11,9x: promedio de historia y peers 13,1x, acercado 25% al justificado (8,3x); rango de anclas 8,3x–15,9x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$51,45 frente a US$33,17 del DCF (+55%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$51,45 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,81%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$21,11) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$33,17 por acción.** Complemento: DCF esperado por probabilidades US$31,29. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$33,17 | US$26,03 | US$40,49 |
| EV/EBITDA | 10,5× / 8,8× / 11,0× | 20% | 33% | US$46,27 | US$35,35 | US$52,12 |
| EV/FCFF | 19,4× / 16,8× / 23,1× | 10% | 17% | US$55,89 | US$52,43 | US$61,48 |
| P/E | 15,7× / 14,3× / 18,1× | 20% | 33% | US$53,18 | US$44,27 | US$65,00 |
| P/FCFE | 17,8× / 15,3× / 21,6× | 5% | 8% | US$54,06 | US$48,28 | US$62,92 |
| P/OCF | 11,9× / 10,4× / 13,4× | 5% | 8% | US$53,81 | US$48,56 | US$58,39 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$51,45 | US$43,35 | US$59,40 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$44,14 | US$36,42 | US$51,84 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$43,92 | US$34,47 | US$53,61 |
| EV/EBITDA (total con dividendos) | 10,5× / 8,8× / 11,0× | 20% | 33% | US$57,70 | US$42,06 | US$67,23 |
| EV/FCFF (total con dividendos) | 19,4× / 16,8× / 23,1× | 10% | 17% | US$67,77 | US$58,13 | US$77,43 |
| P/E (total con dividendos) | 15,7× / 14,3× / 18,1× | 20% | 33% | US$65,50 | US$51,78 | US$82,63 |
| P/FCFE (total con dividendos) | 17,8× / 15,3× / 21,6× | 5% | 8% | US$68,32 | US$56,15 | US$82,27 |
| P/OCF (total con dividendos) | 11,9× / 10,4× / 13,4× | 5% | 8% | US$66,41 | US$55,94 | US$74,46 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$63,59 | US$50,31 | US$75,92 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$7,16 | US$7,16 | US$7,16 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$56,43 | US$43,15 | US$68,75 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$55,72 | US$43,97 | US$67,00 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,81%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$49,22 | US$45,52 | US$44,08 | US$46,27 | OK |
| EV/EBITDA | Conservador | US$39,39 | US$34,40 | US$32,27 | US$35,35 | OK |
| EV/EBITDA | Optimista | US$53,59 | US$51,50 | US$51,27 | US$52,12 | OK |
| EV/FCFF | Base | US$62,71 | US$53,28 | US$51,69 | US$55,89 | OK |
| EV/FCFF | Conservador | US$62,63 | US$50,27 | US$44,40 | US$52,43 | OK |
| EV/FCFF | Optimista | US$67,31 | US$58,14 | US$58,98 | US$61,48 | OK |
| P/E | Base | US$57,22 | US$52,33 | US$49,97 | US$53,18 | OK |
| P/E | Conservador | US$50,11 | US$43,11 | US$39,61 | US$44,27 | OK |
| P/E | Optimista | US$67,83 | US$64,27 | US$62,91 | US$65,00 | OK |
| P/FCFE | Base | US$57,09 | US$53,00 | US$52,10 | US$54,06 | OK |
| P/FCFE | Conservador | US$54,41 | US$47,52 | US$42,91 | US$48,28 | OK |
| P/FCFE | Optimista | US$65,04 | US$61,07 | US$62,64 | US$62,92 | OK |
| P/OCF | Base | US$58,69 | US$52,09 | US$50,66 | US$53,81 | OK |
| P/OCF | Conservador | US$55,85 | US$47,08 | US$42,75 | US$48,56 | OK |
| P/OCF | Optimista | US$62,10 | US$56,32 | US$56,74 | US$58,39 | OK |

Múltiplos consolidados hoy: US$51,45 / US$43,35 / US$59,40 · DCF de las historias hoy: US$33,17 / US$26,03 / US$40,49 · Ponderado hoy: US$44,14 / US$36,42 / US$51,84 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NVO la diferencia es de +55% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$41,96 por acción y los múltiplos, US$42,59 hoy: 1% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$37,91 supone que los ingresos crecen 3,4% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 0,9% (+2,5 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$43,92 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,8%, WACC de los años 4-10 9,2%, ROE de FY+3 48,6% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 10,5x | 7,8x | +31% | 2,9% | 0,8% | +2,0 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 31% por encima del DCF en FY+3. |
| EV/FCFF | 19,4x | 12,1x | +54% | 3,8% | 0,8% | +3,0 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 54% por encima del DCF en FY+3. |
| P/E | 15,7x | 9,9x | +49% | 3,7% | -0,3% | +4,0 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 49% por encima del DCF en FY+3. |
| P/FCFE | 17,8x | 10,7x | +56% | 4,0% | 0,4% | +3,5 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 56% por encima del DCF en FY+3. |
| P/OCF | 11,9x | 7,4x | +51% | 3,8% | 0,4% | +3,4 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 51% por encima del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$44,14 | — |
| Múltiplos Base +20% | US$50,01 | +13,3% |
| Múltiplos Base −20% | US$38,27 | −13,3% |
| Crecimiento años 2-5 +2 pp | US$44,91 | +1,7% |
| Crecimiento años 2-5 −2 pp | US$43,44 | −1,6% |
| Margen objetivo +3 pp | US$45,00 | +1,9% |
| Margen objetivo −3 pp | US$43,28 | −1,9% |
| WACC +1 pp | US$43,44 | −1,6% |
| WACC −1 pp | US$44,89 | +1,7% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 8,85 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 11,10 | 10,51 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 11,02 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 19,88 | 16,84 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 22,53 | 19,39 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 26,10 | 23,10 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 14,33 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 14,41 | 15,71 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 18,06 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 15,35 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 16,99 | 17,78 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 21,62 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 10,40 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 13,90 | 11,93 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 13,42 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/NVO_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1_w85o-Cv_4GzFB4nq5fGqrMSVoYf-Ltafuol3ir5TMw/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (LLY, AZN, NVS, SNY, MRK, PFE).
- [CNBC, 4-feb-2026: Novo cae; el CEO dice que empeorará antes de mejorar](https://www.cnbc.com/2026/02/04/novo-nordisk-stock-ceo-earnings-guidance-ozempic-wegovy.html)
- [CNBC, 4-ago-2026: la guía de Novo decepciona](https://www.cnbc.com/2026/08/04/novo-nordisk-releases-earnings-and-guidance.html)
- [Fierce Pharma: advertencia de ventas y utilidad 2026](https://www.fiercepharma.com/pharma/novo-shares-plummet-sales-profit-warning-26)

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
