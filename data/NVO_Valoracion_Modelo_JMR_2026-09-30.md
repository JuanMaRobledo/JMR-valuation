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

**Valor intrínseco principal · DCF Base hoy: US$31,21 por acción.** Complemento: DCF esperado por probabilidades US$29,48; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$20,37–US$37,65; precio con MOS 35% sobre el esperado: US$19,16; precio de referencia US$37,32. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · El volumen compensa la caída de precio** (valor principal) | 40% | US$31,21 | US$12,48 |
| Conservadora · Guerra de precios con Lilly y genéricos | 30% | US$24,77 | US$7,43 |
| Disrupción · Deterioro de los fundamentales: Novo pierde relevancia frente a Lilly | 10% | US$20,37 | US$2,04 |
| Optimista · La nueva generación recupera el liderazgo | 20% | US$37,65 | US$7,53 |
| **DCF esperado (complemento)** | 100% | **US$29,48** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$41,96 por acción y los múltiplos, US$42,59 hoy: 1% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$31,21 | US$50,00 | US$42,49 | US$19,16 | US$54,54 |
| Conservador | US$24,77 | US$42,29 | US$35,29 | US$19,16 | US$43,30 |
| Optimista | US$37,65 | US$57,47 | US$49,54 | US$19,16 | US$65,14 |

## 2. Datos

- Hoja del modelo: [NVO_Modelo_JMR_Valoracion_2026-09-24](https://docs.google.com/spreadsheets/d/1_w85o-Cv_4GzFB4nq5fGqrMSVoYf-Ltafuol3ir5TMw/edit).
- Análisis del 23 de sept de 2026. Precio de referencia de la hoja: US$37,32.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -7,7% | -3,0% | 0,2% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | -2,9% | 4,5% | 3,9% | Input B29 |
| Margen EBIT objetivo | 35,0% | 40,0% | 43,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 0,57 / 0,76 | — | Input B32/B33 |
| DCF por acción hoy | US$24,77 | US$31,21 | US$37,65 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,09, ERP 4,93%, Ke 10,64%, costo de la deuda después de impuestos 4,56%, peso del patrimonio 90,0%, WACC inicial 10,03% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Novo Nordisk cotizó a 16-27x EBITDA y 23-36x utilidades durante el auge de Ozempic y Wegovy. Desde 2025 perdió participación frente a Eli Lilly, bajó precios en EE. UU. (Wegovy a US$349 al mes en pago directo) y en febrero de 2026 guió una caída de ventas de 5-13% (luego −6% a 0%); la acción cayó de US$59 a US$39 en tres semanas. La etapa actual es Dec '25 y el LTM. Se excluye la columna sin fecha de la hoja. B: farmacéuticas grandes (AstraZeneca, Novartis, Sanofi, Merck, Pfizer), datos de yfinance al 29-sep-2026. Se excluye Eli Lilly (crece 48% justamente a costa de Novo; su múltiplo es de otra etapa) y, en P/E, Merck (119x por cargos puntuales de I+D adquirida). Ajuste −5%: Novo decrece en 2026 mientras los peers crecen 1-15%, aunque conserva márgenes más altos. λ = 0,25: la Novo de FY+3 del escenario Base es una farmacéutica de crecimiento bajo con márgenes altos, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 9,4x | 13,8x (n=5: AZN 14,2x, NVS 13,8x, SNY 8,5x, MRK 14,3x, PFE 8,5x) × 0,95 = 13,1x | 7,7x / 7,8x / 7,8x | **10,4x** | 8,8x | 10,8x | 11,1x / —x / —x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 22,4x (EV/FCF × 1,05 = FCF después de intereses ÷ FCFF) | 21,8x (n=4: AZN 38,0x, NVS 19,8x, MRK 23,7x, PFE 16,5x) × 0,95 = 20,7x | 12,0x / 10,5x / 14,1x | **19,2x** | 16,7x | 22,7x | 22,5x / 19,9x / 26,1x |
| P/E | mediana Dec '25, LTM (etapa actual) = 12,0x | 23,4x (n=4: AZN 24,6x, NVS 22,0x, SNY 22,1x, PFE 37,8x) × 0,95 = 22,2x | 10,6x / 9,5x / 12,0x | **15,4x** | 14,1x | 17,7x | 14,4x / —x / —x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 19,8x | 20,7x (n=4: AZN 42,1x, NVS 18,5x, MRK 22,9x, PFE 14,9x) × 0,95 = 19,7x | 10,9x / 9,6x / 12,6x | **17,5x** | 15,2x | 21,2x | 17,0x / —x / —x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 10,4x | 16,8x (n=4: AZN 18,6x, NVS 15,1x, MRK 18,4x, PFE 12,2x) × 0,95 = 15,9x | 7,5x / 6,5x / 8,7x | **11,7x** | 10,3x | 13,2x | 13,9x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 10,4x: promedio de historia y peers 11,2x, acercado 25% al justificado (7,7x); rango de anclas 7,7x–13,1x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 19,2x: promedio de historia y peers 21,5x, acercado 25% al justificado (12,0x); rango de anclas 12,0x–22,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 15,4x: promedio de historia y peers 17,1x, acercado 25% al justificado (10,6x); rango de anclas 10,6x–22,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 17,5x: promedio de historia y peers 19,7x, acercado 25% al justificado (10,9x); rango de anclas 10,9x–19,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 11,7x: promedio de historia y peers 13,1x, acercado 25% al justificado (7,5x); rango de anclas 7,5x–15,9x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$50,00 frente a US$31,21 del DCF (+60%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$50,00 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,64%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$20,37) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$31,21 por acción.** Complemento: DCF esperado por probabilidades US$29,48. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$31,21 | US$24,77 | US$37,65 |
| EV/EBITDA | 10,4× / 8,8× / 10,8× | 20% | 33% | US$44,97 | US$34,52 | US$50,45 |
| EV/FCFF | 19,2× / 16,7× / 22,7× | 10% | 17% | US$54,46 | US$51,26 | US$59,64 |
| P/E | 15,4× / 14,1× / 17,7× | 20% | 33% | US$51,61 | US$43,13 | US$62,79 |
| P/FCFE | 17,5× / 15,2× / 21,2× | 5% | 8% | US$52,53 | US$47,09 | US$60,87 |
| P/OCF | 11,7× / 10,3× / 13,2× | 5% | 8% | US$52,26 | US$47,33 | US$56,46 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$50,00 | US$42,29 | US$57,47 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$42,49 | US$35,29 | US$49,54 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$42,27 | US$33,55 | US$50,99 |
| EV/EBITDA (total con dividendos) | 10,4× / 8,8× / 10,8× | 20% | 33% | US$56,93 | US$41,68 | US$66,08 |
| EV/FCFF (total con dividendos) | 19,2× / 16,7× / 22,7× | 10% | 17% | US$67,02 | US$57,65 | US$76,25 |
| P/E (total con dividendos) | 15,4× / 14,1× / 17,7× | 20% | 33% | US$64,54 | US$51,19 | US$81,04 |
| P/FCFE (total con dividendos) | 17,5× / 15,2× / 21,2× | 5% | 8% | US$67,39 | US$55,58 | US$80,81 |
| P/OCF (total con dividendos) | 11,7× / 10,3× / 13,2× | 5% | 8% | US$65,47 | US$55,34 | US$73,11 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$62,73 | US$49,81 | US$74,58 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$7,16 | US$7,16 | US$7,16 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$55,57 | US$42,64 | US$67,41 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$54,54 | US$43,30 | US$65,14 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,64%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$48,13 | US$44,22 | US$42,57 | US$44,97 | OK |
| EV/EBITDA | Conservador | US$38,68 | US$33,57 | US$31,30 | US$34,52 | OK |
| EV/EBITDA | Optimista | US$52,20 | US$49,84 | US$49,32 | US$50,45 | OK |
| EV/FCFF | Base | US$61,48 | US$51,88 | US$50,01 | US$54,46 | OK |
| EV/FCFF | Conservador | US$61,60 | US$49,10 | US$43,09 | US$51,26 | OK |
| EV/FCFF | Optimista | US$65,72 | US$56,38 | US$56,83 | US$59,64 | OK |
| P/E | Base | US$55,88 | US$50,77 | US$48,18 | US$51,61 | OK |
| P/E | Conservador | US$49,10 | US$41,96 | US$38,33 | US$43,13 | OK |
| P/E | Optimista | US$65,95 | US$62,06 | US$60,37 | US$62,79 | OK |
| P/FCFE | Base | US$55,83 | US$51,48 | US$50,29 | US$52,53 | OK |
| P/FCFE | Conservador | US$53,39 | US$46,31 | US$41,57 | US$47,09 | OK |
| P/FCFE | Optimista | US$63,33 | US$59,07 | US$60,20 | US$60,87 | OK |
| P/OCF | Base | US$57,35 | US$50,56 | US$48,87 | US$52,26 | OK |
| P/OCF | Conservador | US$54,76 | US$45,85 | US$41,39 | US$47,33 | OK |
| P/OCF | Optimista | US$60,43 | US$54,45 | US$54,51 | US$56,46 | OK |

Múltiplos consolidados hoy: US$50,00 / US$42,29 / US$57,47 · DCF de las historias hoy: US$31,21 / US$24,77 / US$37,65 · Ponderado hoy: US$42,49 / US$35,29 / US$49,54 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NVO la diferencia es de +60% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$41,96 por acción y los múltiplos, US$42,59 hoy: 1% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$37,32 supone que los ingresos crecen 4,7% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 0,9% (+3,9 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$42,27 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,6%, WACC de los años 4-10 9,8%, ROE de FY+3 48,6% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 10,4x | 7,5x | +35% | 3,3% | 1,1% | +2,3 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 35% por encima del DCF en FY+3. |
| EV/FCFF | 19,2x | 11,6x | +59% | 4,3% | 1,1% | +3,2 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 59% por encima del DCF en FY+3. |
| P/E | 15,4x | 9,5x | +53% | 4,5% | 0,1% | +4,4 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 53% por encima del DCF en FY+3. |
| P/FCFE | 17,5x | 10,2x | +59% | 4,7% | 0,8% | +3,9 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 59% por encima del DCF en FY+3. |
| P/OCF | 11,7x | 7,1x | +55% | 4,5% | 0,8% | +3,7 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 55% por encima del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$42,49 | — |
| Múltiplos Base +20% | US$48,18 | +13,4% |
| Múltiplos Base −20% | US$36,79 | −13,4% |
| Crecimiento años 2-5 +2 pp | US$43,14 | +1,5% |
| Crecimiento años 2-5 −2 pp | US$41,89 | −1,4% |
| Margen objetivo +3 pp | US$43,30 | +1,9% |
| Margen objetivo −3 pp | US$41,68 | −1,9% |
| WACC +1 pp | US$41,84 | −1,5% |
| WACC −1 pp | US$43,18 | +1,6% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 8,76 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 11,10 | 10,36 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 10,82 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 19,88 | 16,69 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 22,53 | 19,16 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 26,10 | 22,73 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 14,14 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 14,41 | 15,45 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 17,68 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 15,17 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 16,99 | 17,51 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 21,20 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 10,27 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 13,90 | 11,74 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 13,15 | Múltiplo optimista elegido con el protocolo v3 |
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
