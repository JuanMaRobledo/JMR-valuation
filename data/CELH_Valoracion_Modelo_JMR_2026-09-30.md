---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Celsius Holdings, Inc."
ticker: "CELH"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1tHDLsh4yBF9NQkRLNqfTU6GPM5trOWsB5xIjpALLOIw/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Celsius Holdings, Inc. (CELH) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$24,24 por acción.** Complemento: DCF esperado por probabilidades US$21,55; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$7,31–US$36,12; precio con MOS 35% sobre el esperado: US$14,01; precio de referencia US$27,35. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Alani Nu sostiene un portafolio que crece algo menos que la categoría** (valor principal) | 45% | US$24,24 | US$10,91 |
| Conservadora · CELSIUS sigue cediendo y las promociones se quedan | 25% | US$16,53 | US$4,13 |
| Disrupción · Deterioro de los fundamentales: La regulación de la cafeína alcanza a Alani Nu y la moda pasa | 15% | US$7,31 | US$1,10 |
| Optimista · Plataforma multimarca con PepsiCo y exterior | 15% | US$36,12 | US$5,42 |
| **DCF esperado (complemento)** | 100% | **US$21,55** | |

Lectura del 5-oct-2026 (análisis desde cero): los múltiplos son precio relativo y salen de tres anclas; valen más que el DCF Base de las historias porque los peers (Coca-Cola, Monster) cotizan con marcas y retornos duraderos, mientras el DCF supone que Celsius no conserva retornos excedentes después del año 10. El DCF es el valor intrínseco; los múltiplos dicen cuánto pagaría el mercado si Celsius se pareciera a esos peers.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$24,24 | US$52,22 | US$41,02 | US$14,01 | US$50,63 |
| Conservador | US$16,53 | US$38,92 | US$29,96 | US$14,01 | US$33,92 |
| Optimista | US$36,12 | US$67,85 | US$55,16 | US$14,01 | US$73,43 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - CELH (desde cero 2026-10-05)](https://docs.google.com/spreadsheets/d/1tHDLsh4yBF9NQkRLNqfTU6GPM5trOWsB5xIjpALLOIw/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$27,35.
- Peers: datos de mercado de yfinance consultados el 2026-10-05 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 2,3% | 5,9% | 13,1% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | -0,1% | 4,5% | 10,6% | Input B29 |
| Margen EBIT objetivo | 17,1% | 20,1% | 23,6% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,80 / 1,60 | — | Input B32/B33 |
| DCF por acción hoy | US$16,53 | US$24,24 | US$36,12 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 0,62, ERP 3,74%, Ke 7,62%, costo de la deuda después de impuestos 4,88%, peso del patrimonio 90,2%, WACC inicial 7,35% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: hasta 2023 Celsius fue una marca única en hipercrecimiento (ventas +102% en 2023; utilidades negativas en 2021-2022): sus múltiplos de 44-1.300× no describen a la empresa de FY+3. Desde 2024 (ventas +3%) es una marca que madura y, desde 2025, un portafolio de tres marcas distribuido por PepsiCo. La etapa actual empieza en FY2024. FY2025 y LTM se excluyen en todos los métodos: la utilidad y el EBITDA incluyen US$327,5 millones (2025) y US$412,7 millones (LTM) de terminación de distribuidores y otros cargos de una vez (comunicados del 4T25 y del 2T26), y el flujo de caja incluye los reembolsos de PepsiCo por esas terminaciones, registrados como ingreso diferido (US$356,1 millones). Queda un solo cierre representativo (FY2024): el ancla A es débil y pesa menos (ver λ). B: bebidas con marca y datos de yfinance al 5-oct-2026 (precios del 2-oct): Monster, Coca-Cola, PepsiCo, National Beverage y Vita Coco. Se excluye Keurig Dr Pepper: la compra de JDE Peet's (ingresos +76%, ROE 5%) distorsiona sus múltiplos. Ajuste −20%: crecimiento a FY+3 algo menor que la mediana (Base ~5% frente a ~6,5% de Coca-Cola y PepsiCo; Monster y Vita Coco crecen 20-28%), −5%; margen operativo menor (20% objetivo frente a una mediana de 29%), −5%; ROIC y riesgo propio (ROIC ~16% sobre el capital, una sola categoría, PepsiCo con ~60% de las ventas, investigación del fiscal de Texas y demandas por la cafeína de Alani Nu), −10%. λ = 0,75 (chequeo de crecimiento implícito del 5-oct-2026, paso 6.5): con λ = 0,5 los cinco múltiplos Base implicaban bastante más crecimiento que el DCF (alertas en los cinco). La evidencia no sostiene más crecimiento en el DCF: la marca CELSIUS cae, la categoría se desaceleró a ~5-7% y el crecimiento reciente fue comprado (Alani Nu, Rockstar). Por eso se acerca el Base al justificado, que usa los supuestos de las historias, y el ancla A (un solo cierre, FY2024, de otra etapa) queda solo como referencia del Optimista. La brecha que queda es de ventaja competitiva: el justificado supone que el ROE de FY+3 dura para siempre y el DCF lleva el ROIC al costo de capital después del año 10.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '24 (etapa actual) = 32,6x | 21,6x (n=5: MNST 27,5x, KO 23,4x, PEP 11,4x, FIZZ 11,5x, COCO 21,6x) × 0,80 = 17,3x | 21,6x / 19,3x / 24,9x | **22,4x** | 18,2x | 24,2x | 32,6x / —x / —x |
| EV/FCFF | mediana Dec '24 (etapa actual) = 24,2x (EV/FCF × 1,09 = FCF después de intereses ÷ FCFF) | 23,7x (n=5: MNST 38,8x, KO 25,7x, PEP 21,1x, FIZZ 17,2x, COCO 23,7x) × 0,80 = 18,9x | 33,0x / 25,7x / 42,1x | **30,1x** | 26,8x | 33,7x | 26,2x / —x / —x |
| P/E | mediana Dec '24 (etapa actual) = 43,2x | 25,7x (n=5: MNST 39,8x, KO 25,7x, PEP 16,5x, FIZZ 16,3x, COCO 30,9x) × 0,80 = 20,6x | 34,1x / 25,6x / 46,1x | **33,5x** | 26,8x | 39,8x | 42,7x / —x / —x |
| P/FCFE | mediana Dec '24 (etapa actual) = 25,9x | 25,8x (n=5: MNST 40,4x, KO 25,8x, PEP 18,5x, FIZZ 17,5x, COCO 26,0x) × 0,80 = 20,6x | 38,2x / 28,8x / 50,9x | **34,4x** | 28,4x | 38,4x | 23,5x / —x / —x |
| P/OCF | mediana Dec '24 (etapa actual) = 23,5x | 22,6x (n=5: MNST 37,6x, KO 22,6x, PEP 12,8x, FIZZ 15,2x, COCO 24,6x) × 0,80 = 18,0x | 37,1x / 26,1x / 52,4x | **33,0x** | 26,2x | 38,6x | 24,2x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 22,4x: promedio de historia y peers 24,9x, acercado 75% al justificado (21,6x); rango de anclas 17,3x–32,6x. Atípicos excluidos de la historia: Dec '16 (-31,0x: métrica negativa o ~0); Dec '17 (-27,9x: métrica negativa o ~0); Dec '18 (-18,0x: métrica negativa o ~0); Dec '19 (-227,5x: métrica negativa o ~0); Dec '21 (-1.989,4x: métrica negativa o ~0); Dec '22 (-47,0x: métrica negativa o ~0); Dec '20 (418,0x: > 2,5x la mediana (44.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 30,1x: promedio de historia y peers 21,6x, acercado 75% al justificado (33,0x); rango de anclas 18,9x–33,0x. Atípicos excluidos de la historia: Dec '16 (-36,1x: métrica negativa o ~0); Dec '17 (-26,6x: métrica negativa o ~0); Dec '18 (-16,2x: métrica negativa o ~0); Dec '21 (-55,9x: métrica negativa o ~0); Dec '19 (318,5x: > 2,5x la mediana (73.4x)); Dec '20 (1.283,8x: > 2,5x la mediana (73.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 33,5x: promedio de historia y peers 31,9x, acercado 75% al justificado (34,1x); rango de anclas 20,6x–43,2x. Atípicos excluidos de la historia: Dec '18 (-15,9x: métrica negativa o ~0); Dec '22 (-41,9x: métrica negativa o ~0); Dec '20 (453,2x: > 2,5x la mediana (56.8x)); Dec '21 (1.462,3x: > 2,5x la mediana (56.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 34,4x: promedio de historia y peers 23,2x, acercado 75% al justificado (38,2x); rango de anclas 20,6x–38,2x. Atípicos excluidos de la historia: Dec '16 (-41,0x: métrica negativa o ~0); Dec '17 (-28,2x: métrica negativa o ~0); Dec '18 (-16,8x: métrica negativa o ~0); Dec '21 (-56,0x: métrica negativa o ~0); Dec '19 (332,8x: > 2,5x la mediana (79.6x)); Dec '20 (1.299,1x: > 2,5x la mediana (79.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 33,0x: promedio de historia y peers 20,8x, acercado 75% al justificado (37,1x); rango de anclas 18,0x–37,1x. Atípicos excluidos de la historia: Dec '16 (-41,0x: métrica negativa o ~0); Dec '17 (-28,6x: métrica negativa o ~0); Dec '18 (-17,1x: métrica negativa o ~0); Dec '21 (-57,8x: métrica negativa o ~0); Dec '19 (332,8x: > 2,5x la mediana (73.5x)); Dec '20 (1.069,8x: > 2,5x la mediana (73.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$52,22 frente a US$24,24 del DCF (+115%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$52,22 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 7,62%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$7,31) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$24,24 por acción.** Complemento: DCF esperado por probabilidades US$21,55. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$24,24 | US$16,53 | US$36,12 |
| EV/EBITDA | 22,4× / 18,2× / 24,2× | 20% | 33% | US$48,63 | US$33,31 | US$63,35 |
| EV/FCFF | 30,1× / 26,8× / 33,7× | 10% | 17% | US$41,11 | US$38,08 | US$46,64 |
| P/E | 33,5× / 26,8× / 39,8× | 20% | 33% | US$59,09 | US$41,26 | US$83,01 |
| P/FCFE | 34,4× / 28,4× / 38,4× | 5% | 8% | US$59,78 | US$48,29 | US$72,24 |
| P/OCF | 33,0× / 26,2× / 38,6× | 5% | 8% | US$53,71 | US$44,25 | US$63,18 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$52,22 | US$38,92 | US$67,85 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$41,02 | US$29,96 | US$55,16 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$30,21 | US$20,60 | US$45,02 |
| EV/EBITDA | 22,4× / 18,2× / 24,2× | 20% | 33% | US$60,18 | US$37,22 | US$85,46 |
| EV/FCFF | 30,1× / 26,8× / 33,7× | 10% | 17% | US$52,30 | US$41,81 | US$69,56 |
| P/E | 33,5× / 26,8× / 39,8× | 20% | 33% | US$72,39 | US$45,96 | US$110,67 |
| P/FCFE | 34,4× / 28,4× / 38,4× | 5% | 8% | US$68,47 | US$48,20 | US$93,56 |
| P/OCF | 33,0× / 26,2× / 38,6× | 5% | 8% | US$67,54 | US$49,06 | US$91,33 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 60% | 100% | US$64,24 | US$42,80 | US$92,38 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$50,63 | US$33,92 | US$73,43 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 7,62%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$48,80 | US$48,81 | US$48,28 | US$48,63 | OK |
| EV/EBITDA | Conservador | US$37,21 | US$32,86 | US$29,86 | US$33,31 | OK |
| EV/EBITDA | Optimista | US$57,03 | US$64,46 | US$68,56 | US$63,35 | OK |
| EV/FCFF | Base | US$40,54 | US$40,84 | US$41,96 | US$41,11 | OK |
| EV/FCFF | Conservador | US$43,30 | US$37,41 | US$33,55 | US$38,08 | OK |
| EV/FCFF | Optimista | US$36,89 | US$47,23 | US$55,80 | US$46,64 | OK |
| P/E | Base | US$59,96 | US$59,22 | US$58,08 | US$59,09 | OK |
| P/E | Conservador | US$46,22 | US$40,70 | US$36,87 | US$41,26 | OK |
| P/E | Optimista | US$75,91 | US$84,34 | US$88,79 | US$83,01 | OK |
| P/FCFE | Base | US$70,15 | US$54,25 | US$54,94 | US$59,78 | OK |
| P/FCFE | Conservador | US$63,46 | US$42,75 | US$38,67 | US$48,29 | OK |
| P/FCFE | Optimista | US$74,74 | US$66,92 | US$75,07 | US$72,24 | OK |
| P/OCF | Base | US$53,53 | US$53,39 | US$54,19 | US$53,71 | OK |
| P/OCF | Conservador | US$49,81 | US$43,59 | US$39,36 | US$44,25 | OK |
| P/OCF | Optimista | US$52,44 | US$63,83 | US$73,27 | US$63,18 | OK |

Múltiplos consolidados hoy: US$52,22 / US$38,92 / US$67,85 · DCF de las historias hoy: US$24,24 / US$16,53 / US$36,12 · Ponderado hoy: US$41,02 / US$29,96 / US$55,16 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para CELH la diferencia es de +115% (múltiplos por encima del DCF). Lectura del 5-oct-2026 (análisis desde cero): los múltiplos son precio relativo y salen de tres anclas; valen más que el DCF Base de las historias porque los peers (Coca-Cola, Monster) cotizan con marcas y retornos duraderos, mientras el DCF supone que Celsius no conserva retornos excedentes después del año 10. El DCF es el valor intrínseco; los múltiplos dicen cuánto pagaría el mercado si Celsius se pareciera a esos peers.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$27,35 supone que los ingresos crecen 7,7% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 4,8% (+2,9 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$30,21 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 7,6%, WACC de los años 4-10 8,1%, ROE de FY+3 45,8% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 22,4x | 10,5x | +99% | 5,0% | 1,7% | +3,3 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 99% por encima del DCF en FY+3. |
| EV/FCFF | 30,1x | 16,0x | +73% | 4,6% | 1,7% | +2,9 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 73% por encima del DCF en FY+3. |
| P/E | 33,5x | 14,0x | +140% | 4,8% | 0,5% | +4,3 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 140% por encima del DCF en FY+3. |
| P/FCFE | 34,4x | 15,2x | +127% | 4,6% | 1,0% | +3,6 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 127% por encima del DCF en FY+3. |
| P/OCF | 33,0x | 14,8x | +124% | 4,5% | 1,0% | +3,6 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 124% por encima del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$41,02 | — |
| Múltiplos Base +20% | US$47,55 | +15,9% |
| Múltiplos Base −20% | US$34,50 | −15,9% |
| Crecimiento años 2-5 +2 pp | US$41,85 | +2,0% |
| Crecimiento años 2-5 −2 pp | US$40,26 | −1,9% |
| Margen objetivo +3 pp | US$42,72 | +4,1% |
| Margen objetivo −3 pp | US$39,33 | −4,1% |
| WACC +1 pp | US$40,40 | −1,5% |
| WACC −1 pp | US$41,69 | +1,6% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo −3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 18,17 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 32,62 | 22,42 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 24,22 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 26,80 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 26,18 | 30,10 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 33,72 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 26,77 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 42,69 | 33,55 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 39,76 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 28,39 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 23,52 | 34,44 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 38,39 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 26,16 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 24,21 | 33,03 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 38,57 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/CELH_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1tHDLsh4yBF9NQkRLNqfTU6GPM5trOWsB5xIjpALLOIw/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-10-05 (MNST, KDP, KO, PEP, FIZZ, COCO).
- [Celsius Holdings, comunicado del 2T26, 6-ago-2026](https://www.sec.gov/Archives/edgar/data/1341766/000134176626000047/ex9912q2026.htm)
- [Celsius Holdings, comunicado del 4T25, 26-feb-2026](https://www.sec.gov/Archives/edgar/data/1341766/000134176626000017/ex9914q20251.htm)
- [Celsius Holdings, 10-Q del 2T26, 6-ago-2026](https://www.sec.gov/Archives/edgar/data/1341766/000134176626000050/celh-20260630.htm)

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
