---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de NVIDIA CORP"
ticker: "NVDA"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1eEsuWSHXWQrBa2Dt5l_9Fbx24M4pug15Rx_Gj-CCkMg/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# NVIDIA CORP (NVDA) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$222,09 por acción.** Complemento: DCF esperado por probabilidades US$201,88; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$54,89–US$338,53; precio con MOS 35% sobre el esperado: US$131,22; precio de referencia US$241,71. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Ciclo de IA largo que desacelera con la escala** (valor principal) | 40% | US$222,09 | US$88,84 |
| Conservadora · Ciclo de semiconductores: el capex se corrige | 30% | US$132,83 | US$39,85 |
| Disrupción · Deterioro de los fundamentales: Chips propios de los clientes y corrección fuerte | 10% | US$54,89 | US$5,49 |
| Optimista · La IA es infraestructura permanente | 20% | US$338,53 | US$67,71 |
| **DCF esperado (complemento)** | 100% | **US$201,88** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$259,29 por acción y los múltiplos, US$230,76 hoy: 11% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$222,09 | US$308,91 | US$256,82 | US$131,22 | US$359,60 |
| Conservador | US$132,83 | US$222,61 | US$168,74 | US$131,22 | US$207,44 |
| Optimista | US$338,53 | US$459,15 | US$386,78 | US$131,22 | US$567,63 |

## 2. Datos

- Hoja del modelo: [Modelo JMR — Plantilla maestra reutilizable (vigente)](https://docs.google.com/spreadsheets/d/1eEsuWSHXWQrBa2Dt5l_9Fbx24M4pug15Rx_Gj-CCkMg/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$241,71.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 32,5% | 50,0% | 56,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | -9,0% | 14,0% | 28,9% | Input B29 |
| Margen EBIT objetivo | 50,1% | 58,1% | 60,1% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,92 / 2,44 | — | Input B32/B33 |
| DCF por acción hoy | US$132,83 | US$222,09 | US$338,53 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,51, ERP 4,16%, Ke 11,58%, costo de la deuda después de impuestos 5,19%, peso del patrimonio 99,2%, WACC inicial 11,53% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: los cierres de la hoja hasta Jan '24 dan múltiplos de 0,5-12x porque el precio no está ajustado por los splits 4:1 (jul-2021) y 10:1 (jun-2024); no son representativos. Desde FY25 (Jan '25) la historia es comparable y corresponde a la etapa actual de NVIDIA como proveedor dominante de cómputo para IA. B: semiconductores de márgenes altos (Broadcom, Qualcomm, KLA, Lam Research, Texas Instruments, Analog Devices y, en P/E, TSMC), datos de yfinance al 29-sep-2026. Se excluyen ASML (EV/EBITDA de 2.900x: dato roto), AMD y Marvell (utilidades deprimidas por la amortización de adquisiciones: múltiplos de 80-156x que no comparan con los márgenes de ~60% de NVIDIA) y TSMC en los múltiplos de EV y flujo (mezcla dólares del ADR con cifras en dólares taiwaneses). Sin ajuste: NVIDIA crece más que la mediana de los peers, pero ellos ya cotizan a múltiplos de ciclo alto de semiconductores (40-55x utilidades); se toma la mediana tal cual. λ = 0,25: la NVIDIA de FY+3 del escenario Base sigue creciendo por encima del mercado, pero con un costo de patrimonio alto (13,5%) que baja el múltiplo justificado.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Jan '25, Jan '26, LTM (etapa actual) = 34,2x | 30,6x (n=6: AVGO 32,6x, QCOM 16,7x, KLAC 42,6x, LRCX 46,7x, TXN 27,4x, ADI 28,7x) × 1,00 = 30,6x | 17,0x / 18,3x / 25,7x | **28,6x** | 27,4x | 37,5x | 4,5x / —x / —x |
| EV/FCFF | mediana Jan '25, Jan '26, LTM (etapa actual) = 49,4x (EV/FCF × 1,11 = FCF después de intereses ÷ FCFF) | 42,9x (n=6: AVGO 40,7x, QCOM 18,3x, KLAC 64,6x, LRCX 80,5x, TXN 45,0x, ADI 38,1x) × 1,00 = 42,9x | 21,9x / 23,9x / 34,9x | **40,1x** | 38,9x | 54,5x | 4,2x / —x / —x |
| P/E | mediana Jan '25, Jan '26, LTM (etapa actual) = 38,3x | 45,8x (n=7: AVGO 45,8x, QCOM 21,0x, TSM 34,0x, KLAC 53,8x, LRCX 56,3x, TXN 42,9x, ADI 47,3x) × 1,00 = 45,8x | 17,0x / 17,5x / 24,4x | **35,8x** | 32,7x | 43,8x | 5,1x / —x / —x |
| P/FCFE | mediana Jan '25, Jan '26, LTM (etapa actual) = 44,4x | 45,5x (n=6: AVGO 43,0x, QCOM 18,9x, KLAC 68,1x, LRCX 82,9x, TXN 48,0x, ADI 39,1x) × 1,00 = 45,5x | 17,8x / 19,0x / 25,5x | **38,2x** | 37,0x | 50,0x | 3,9x / —x / —x |
| P/OCF | mediana Jan '25, Jan '26, LTM (etapa actual) = 44,4x | 38,2x (n=6: AVGO 41,7x, QCOM 15,9x, KLAC 61,9x, LRCX 69,2x, TXN 29,7x, ADI 34,8x) × 1,00 = 38,2x | 18,1x / 19,0x / 26,4x | **35,5x** | 33,3x | 48,1x | 3,6x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 28,6x: promedio de historia y peers 32,4x, acercado 25% al justificado (17,0x); rango de anclas 17,0x–34,2x. Atípicos excluidos de la historia: Jan '18 (0,5x: métrica negativa o ~0); Jan '20 (-1,4x: métrica negativa o ~0); Jan '17 (0,9x: < 0,4x la mediana (6.0x), caída puntual); Jan '19 (0,9x: < 0,4x la mediana (6.0x), caída puntual); Jan '25 (41,9x: > 2,5x la mediana (6.0x)); Jan '26 (34,2x: > 2,5x la mediana (6.0x)); LTM (26,6x: > 2,5x la mediana (6.0x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 40,1x: promedio de historia y peers 46,1x, acercado 25% al justificado (21,9x); rango de anclas 21,9x–49,4x. Atípicos excluidos de la historia: Jan '18 (0,5x: métrica negativa o ~0); Jan '20 (-0,9x: métrica negativa o ~0); Jan '17 (1,1x: < 0,4x la mediana (7.3x), caída puntual); Jan '19 (1,0x: < 0,4x la mediana (7.3x), caída puntual); Jan '21 (2,5x: < 0,4x la mediana (7.3x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (7.3x)); Jan '26 (44,4x: > 2,5x la mediana (7.3x)); LTM (40,0x: > 2,5x la mediana (7.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 35,8x: promedio de historia y peers 42,0x, acercado 25% al justificado (17,0x); rango de anclas 17,0x–45,8x. Atípicos excluidos de la historia: Jan '17 (1,1x: < 0,4x la mediana (5.1x), caída puntual); Jan '18 (1,3x: < 0,4x la mediana (5.1x), caída puntual); Jan '19 (0,6x: < 0,4x la mediana (5.1x), caída puntual); Jan '20 (1,4x: < 0,4x la mediana (5.1x), caída puntual); Jan '21 (1,9x: < 0,4x la mediana (5.1x), caída puntual); Jan '25 (48,5x: > 2,5x la mediana (5.1x)); Jan '26 (38,3x: > 2,5x la mediana (5.1x)); LTM (28,6x: > 2,5x la mediana (5.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 38,2x: promedio de historia y peers 45,0x, acercado 25% al justificado (17,8x); rango de anclas 17,8x–45,5x. Atípicos excluidos de la historia: Jan '17 (1,0x: < 0,4x la mediana (5.4x), caída puntual); Jan '18 (1,1x: < 0,4x la mediana (5.4x), caída puntual); Jan '19 (0,7x: < 0,4x la mediana (5.4x), caída puntual); Jan '20 (0,8x: < 0,4x la mediana (5.4x), caída puntual); Jan '21 (1,4x: < 0,4x la mediana (5.4x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (5.4x)); Jan '26 (44,4x: > 2,5x la mediana (5.4x)); LTM (40,4x: > 2,5x la mediana (5.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 35,5x: promedio de historia y peers 41,3x, acercado 25% al justificado (18,1x); rango de anclas 18,1x–44,4x. Atípicos excluidos de la historia: Jan '17 (1,0x: < 0,4x la mediana (5.4x), caída puntual); Jan '18 (1,1x: < 0,4x la mediana (5.4x), caída puntual); Jan '19 (0,7x: < 0,4x la mediana (5.4x), caída puntual); Jan '20 (0,8x: < 0,4x la mediana (5.4x), caída puntual); Jan '21 (1,4x: < 0,4x la mediana (5.4x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (5.4x)); Jan '26 (44,4x: > 2,5x la mediana (5.4x)); LTM (40,4x: > 2,5x la mediana (5.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$308,91 frente a US$222,09 del DCF (+39%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$308,91 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Crecimiento»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 11,58%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$54,89) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$222,09 por acción.** Complemento: DCF esperado por probabilidades US$201,88. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$222,09 | US$132,83 | US$338,53 |
| EV/EBITDA | 28,6× / 27,4× / 37,5× | 10% | 25% | US$298,54 | US$204,41 | US$455,81 |
| EV/FCFF | 40,1× / 38,9× / 54,5× | 15% | 37% | US$313,71 | US$238,41 | US$466,18 |
| P/E | 35,8× / 32,7× / 43,8× | 5% | 12% | US$316,14 | US$205,10 | US$452,47 |
| P/FCFE | 38,2× / 37,0× / 50,0× | 5% | 12% | US$328,05 | US$241,14 | US$480,10 |
| P/OCF | 35,5× / 33,3× / 48,1× | 5% | 12% | US$288,84 | US$210,60 | US$430,49 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$308,91 | US$222,61 | US$459,15 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$256,82 | US$168,74 | US$386,78 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$308,52 | US$184,52 | US$470,25 |
| EV/EBITDA (total con dividendos) | 28,6× / 27,4× / 37,5× | 10% | 25% | US$415,02 | US$232,99 | US$691,21 |
| EV/FCFF (total con dividendos) | 40,1× / 38,9× / 54,5× | 15% | 37% | US$450,18 | US$253,90 | US$739,71 |
| P/E (total con dividendos) | 35,8× / 32,7× / 43,8× | 5% | 12% | US$440,42 | US$233,37 | US$687,82 |
| P/FCFE (total con dividendos) | 38,2× / 37,0× / 50,0× | 5% | 12% | US$454,23 | US$249,04 | US$737,52 |
| P/OCF (total con dividendos) | 35,5× / 33,3× / 48,1× | 5% | 12% | US$414,55 | US$224,45 | US$682,73 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 40% | 100% | US$436,22 | US$241,82 | US$713,70 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$0,84 | US$0,84 | US$0,84 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$435,38 | US$240,98 | US$712,86 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$359,60 | US$207,44 | US$567,63 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 11,58%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$291,22 | US$305,58 | US$298,84 | US$298,54 | OK |
| EV/EBITDA | Conservador | US$252,70 | US$192,74 | US$167,80 | US$204,41 | OK |
| EV/EBITDA | Optimista | US$404,75 | US$465,00 | US$497,66 | US$455,81 | OK |
| EV/FCFF | Base | US$289,86 | US$327,12 | US$324,15 | US$313,71 | OK |
| EV/FCFF | Conservador | US$309,79 | US$222,59 | US$182,85 | US$238,41 | OK |
| EV/FCFF | Optimista | US$385,79 | US$480,16 | US$532,57 | US$466,18 | OK |
| P/E | Base | US$307,16 | US$324,14 | US$317,13 | US$316,14 | OK |
| P/E | Conservador | US$253,79 | US$193,44 | US$168,07 | US$205,10 | OK |
| P/E | Optimista | US$399,89 | US$462,29 | US$495,22 | US$452,47 | OK |
| P/FCFE | Base | US$321,87 | US$335,23 | US$327,07 | US$328,05 | OK |
| P/FCFE | Conservador | US$331,02 | US$213,05 | US$179,35 | US$241,14 | OK |
| P/FCFE | Optimista | US$423,03 | US$486,28 | US$531,00 | US$480,10 | OK |
| P/OCF | Base | US$266,93 | US$301,10 | US$298,50 | US$288,84 | OK |
| P/OCF | Conservador | US$273,63 | US$196,52 | US$161,65 | US$210,60 | OK |
| P/OCF | Optimista | US$356,60 | US$443,33 | US$491,55 | US$430,49 | OK |

Múltiplos consolidados hoy: US$308,91 / US$222,61 / US$459,15 · DCF de las historias hoy: US$222,09 / US$132,83 / US$338,53 · Ponderado hoy: US$256,82 / US$168,74 / US$386,78 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NVDA la diferencia es de +39% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$259,29 por acción y los múltiplos, US$230,76 hoy: 11% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$241,71 supone que los ingresos crecen 24,8% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 17,9% (+6,8 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$308,52 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,6%, WACC de los años 4-10 10,4%, ROE de FY+3 131,6% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 28,6x | 21,1x | +35% | 7,5% | 6,5% | +1,0 pp | Revisar: el múltiplo vale 35% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 40,1x | 27,3x | +46% | 7,8% | 6,5% | +1,2 pp | Revisar: el múltiplo vale 46% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 35,8x | 25,0x | +43% | 8,7% | 7,5% | +1,2 pp | Revisar: el múltiplo vale 43% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 38,2x | 25,9x | +47% | 8,7% | 7,4% | +1,3 pp | Revisar: el múltiplo vale 47% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 35,5x | 26,4x | +34% | 8,5% | 7,4% | +1,0 pp | Revisar: el múltiplo vale 34% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$256,82 | — |
| Múltiplos Base +20% | US$281,31 | +9,5% |
| Múltiplos Base −20% | US$232,33 | −9,5% |
| Crecimiento años 2-5 +2 pp | US$269,28 | +4,9% |
| Crecimiento años 2-5 −2 pp | US$245,37 | −4,5% |
| Margen objetivo +3 pp | US$263,43 | +2,6% |
| Margen objetivo −3 pp | US$250,21 | −2,6% |
| WACC +1 pp | US$249,42 | −2,9% |
| WACC −1 pp | US$264,75 | +3,1% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 27,38 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 4,46 | 28,57 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 37,49 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 38,89 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 4,16 | 40,10 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 54,49 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 32,71 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 5,05 | 35,77 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 43,79 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 36,95 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 3,92 | 38,16 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 50,05 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 33,32 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 3,57 | 35,52 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 48,07 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/NVDA_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1eEsuWSHXWQrBa2Dt5l_9Fbx24M4pug15Rx_Gj-CCkMg/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (AVGO, QCOM, TSM, AMD, MRVL, ASML, KLAC, LRCX, TXN, ADI).

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
