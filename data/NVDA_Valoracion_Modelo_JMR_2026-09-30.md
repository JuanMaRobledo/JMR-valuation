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

**Valor intrínseco principal · DCF Base hoy: US$209,39 por acción.** Complemento: DCF esperado por probabilidades US$190,50; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$54,53–US$318,06; precio con MOS 35% sobre el esperado: US$123,83; precio de referencia US$233,95. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Ciclo de IA largo que desacelera con la escala** (valor principal) | 40% | US$209,39 | US$83,76 |
| Conservadora · Ciclo de semiconductores: el capex se corrige | 30% | US$125,59 | US$37,68 |
| Disrupción · Deterioro de los fundamentales: Chips propios de los clientes y corrección fuerte | 10% | US$54,53 | US$5,45 |
| Optimista · La IA es infraestructura permanente | 20% | US$318,06 | US$63,61 |
| **DCF esperado (complemento)** | 100% | **US$190,50** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$259,29 por acción y los múltiplos, US$230,76 hoy: 11% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$209,39 | US$305,42 | US$267,01 | US$123,83 | US$374,37 |
| Conservador | US$125,59 | US$211,55 | US$177,17 | US$123,83 | US$211,19 |
| Optimista | US$318,06 | US$447,11 | US$395,49 | US$123,83 | US$590,83 |

## 2. Datos

- Hoja del modelo: [Modelo JMR — Plantilla maestra reutilizable (vigente)](https://docs.google.com/spreadsheets/d/1eEsuWSHXWQrBa2Dt5l_9Fbx24M4pug15Rx_Gj-CCkMg/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$233,95.
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
| DCF por acción hoy | US$125,59 | US$209,39 | US$318,06 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,51, ERP 4,46%, Ke 11,72%, costo de la deuda después de impuestos 4,94%, peso del patrimonio 99,2%, WACC inicial 11,67% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: los cierres de la hoja hasta Jan '24 dan múltiplos de 0,5-12x porque el precio no está ajustado por los splits 4:1 (jul-2021) y 10:1 (jun-2024); no son representativos. Desde FY25 (Jan '25) la historia es comparable y corresponde a la etapa actual de NVIDIA como proveedor dominante de cómputo para IA. B: semiconductores de márgenes altos (Broadcom, Qualcomm, KLA, Lam Research, Texas Instruments, Analog Devices y, en P/E, TSMC), datos de yfinance al 29-sep-2026. Se excluyen ASML (EV/EBITDA de 2.900x: dato roto), AMD y Marvell (utilidades deprimidas por la amortización de adquisiciones: múltiplos de 80-156x que no comparan con los márgenes de ~60% de NVIDIA) y TSMC en los múltiplos de EV y flujo (mezcla dólares del ADR con cifras en dólares taiwaneses). Sin ajuste: NVIDIA crece más que la mediana de los peers, pero ellos ya cotizan a múltiplos de ciclo alto de semiconductores (40-55x utilidades); se toma la mediana tal cual. λ = 0,25: la NVIDIA de FY+3 del escenario Base sigue creciendo por encima del mercado, pero con un costo de patrimonio alto (13,5%) que baja el múltiplo justificado.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Jan '25, Jan '26, LTM (etapa actual) = 34,2x | 30,6x (n=6: AVGO 32,6x, QCOM 16,7x, KLAC 42,6x, LRCX 46,7x, TXN 27,4x, ADI 28,7x) × 1,00 = 30,6x | 15,9x / 17,1x / 23,4x | **28,3x** | 27,1x | 36,7x | 4,5x / —x / —x |
| EV/FCFF | mediana Jan '25, Jan '26, LTM (etapa actual) = 49,4x (EV/FCF × 1,11 = FCF después de intereses ÷ FCFF) | 42,9x (n=6: AVGO 40,7x, QCOM 18,3x, KLAC 64,6x, LRCX 80,5x, TXN 45,0x, ADI 38,1x) × 1,00 = 42,9x | 20,6x / 22,3x / 31,7x | **39,8x** | 38,6x | 53,6x | 4,2x / —x / —x |
| P/E | mediana Jan '25, Jan '26, LTM (etapa actual) = 38,3x | 45,8x (n=7: AVGO 45,8x, QCOM 21,0x, TSM 34,0x, KLAC 53,8x, LRCX 56,3x, TXN 42,9x, ADI 47,3x) × 1,00 = 45,8x | 16,0x / 16,4x / 22,4x | **35,5x** | 32,5x | 43,1x | 5,1x / —x / —x |
| P/FCFE | mediana Jan '25, Jan '26, LTM (etapa actual) = 44,4x | 45,5x (n=6: AVGO 43,0x, QCOM 18,9x, KLAC 68,1x, LRCX 82,9x, TXN 48,0x, ADI 39,1x) × 1,00 = 45,5x | 16,7x / 17,8x / 23,4x | **37,9x** | 36,6x | 49,3x | 3,9x / —x / —x |
| P/OCF | mediana Jan '25, Jan '26, LTM (etapa actual) = 44,4x | 38,2x (n=6: AVGO 41,7x, QCOM 15,9x, KLAC 61,9x, LRCX 69,2x, TXN 29,7x, ADI 34,8x) × 1,00 = 38,2x | 17,0x / 17,8x / 24,3x | **35,2x** | 33,0x | 47,3x | 3,6x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 28,3x: promedio de historia y peers 32,4x, acercado 25% al justificado (15,9x); rango de anclas 15,9x–34,2x. Atípicos excluidos de la historia: Jan '18 (0,5x: métrica negativa o ~0); Jan '20 (-1,4x: métrica negativa o ~0); Jan '17 (0,9x: < 0,4x la mediana (6.0x), caída puntual); Jan '19 (0,9x: < 0,4x la mediana (6.0x), caída puntual); Jan '25 (41,9x: > 2,5x la mediana (6.0x)); Jan '26 (34,2x: > 2,5x la mediana (6.0x)); LTM (26,9x: > 2,5x la mediana (6.0x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 39,8x: promedio de historia y peers 46,1x, acercado 25% al justificado (20,6x); rango de anclas 20,6x–49,4x. Atípicos excluidos de la historia: Jan '18 (0,5x: métrica negativa o ~0); Jan '20 (-0,9x: métrica negativa o ~0); Jan '17 (1,1x: < 0,4x la mediana (7.3x), caída puntual); Jan '19 (1,0x: < 0,4x la mediana (7.3x), caída puntual); Jan '21 (2,5x: < 0,4x la mediana (7.3x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (7.3x)); Jan '26 (44,4x: > 2,5x la mediana (7.3x)); LTM (40,3x: > 2,5x la mediana (7.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 35,5x: promedio de historia y peers 42,0x, acercado 25% al justificado (16,0x); rango de anclas 16,0x–45,8x. Atípicos excluidos de la historia: Jan '17 (1,1x: < 0,4x la mediana (5.1x), caída puntual); Jan '18 (1,3x: < 0,4x la mediana (5.1x), caída puntual); Jan '19 (0,6x: < 0,4x la mediana (5.1x), caída puntual); Jan '20 (1,4x: < 0,4x la mediana (5.1x), caída puntual); Jan '21 (1,9x: < 0,4x la mediana (5.1x), caída puntual); Jan '25 (48,5x: > 2,5x la mediana (5.1x)); Jan '26 (38,3x: > 2,5x la mediana (5.1x)); LTM (28,6x: > 2,5x la mediana (5.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 37,9x: promedio de historia y peers 45,0x, acercado 25% al justificado (16,7x); rango de anclas 16,7x–45,5x. Atípicos excluidos de la historia: Jan '17 (1,0x: < 0,4x la mediana (5.4x), caída puntual); Jan '18 (1,1x: < 0,4x la mediana (5.4x), caída puntual); Jan '19 (0,7x: < 0,4x la mediana (5.4x), caída puntual); Jan '20 (0,8x: < 0,4x la mediana (5.4x), caída puntual); Jan '21 (1,4x: < 0,4x la mediana (5.4x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (5.4x)); Jan '26 (44,4x: > 2,5x la mediana (5.4x)); LTM (40,4x: > 2,5x la mediana (5.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 35,2x: promedio de historia y peers 41,3x, acercado 25% al justificado (17,0x); rango de anclas 17,0x–44,4x. Atípicos excluidos de la historia: Jan '17 (1,0x: < 0,4x la mediana (5.4x), caída puntual); Jan '18 (1,1x: < 0,4x la mediana (5.4x), caída puntual); Jan '19 (0,7x: < 0,4x la mediana (5.4x), caída puntual); Jan '20 (0,8x: < 0,4x la mediana (5.4x), caída puntual); Jan '21 (1,4x: < 0,4x la mediana (5.4x), caída puntual); Jan '25 (54,5x: > 2,5x la mediana (5.4x)); Jan '26 (44,4x: > 2,5x la mediana (5.4x)); LTM (40,4x: > 2,5x la mediana (5.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$305,42 frente a US$209,39 del DCF (+46%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$305,42 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 11,72%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$54,53) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$209,39 por acción.** Complemento: DCF esperado por probabilidades US$190,50. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$209,39 | US$125,59 | US$318,06 |
| EV/EBITDA | 28,3× / 27,1× / 36,7× | 20% | 33% | US$295,19 | US$202,02 | US$444,96 |
| EV/FCFF | 39,8× / 38,6× / 53,6× | 10% | 17% | US$310,33 | US$235,92 | US$457,62 |
| P/E | 35,5× / 32,5× / 43,1× | 20% | 33% | US$313,20 | US$202,98 | US$444,04 |
| P/FCFE | 37,9× / 36,6× / 49,3× | 5% | 8% | US$324,97 | US$238,63 | US$471,54 |
| P/OCF | 35,2× / 33,0× / 47,3× | 5% | 8% | US$285,89 | US$208,21 | US$422,53 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$305,42 | US$211,55 | US$447,11 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$267,01 | US$177,17 | US$395,49 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$292,01 | US$175,15 | US$443,57 |
| EV/EBITDA (total con dividendos) | 28,3× / 27,1× / 36,7× | 20% | 33% | US$411,43 | US$230,83 | US$676,57 |
| EV/FCFF (total con dividendos) | 39,8× / 38,6× / 53,6× | 10% | 17% | US$446,51 | US$251,85 | US$728,11 |
| P/E (total con dividendos) | 35,5× / 32,5× / 43,1× | 20% | 33% | US$437,48 | US$231,52 | US$676,83 |
| P/FCFE (total con dividendos) | 37,9× / 36,6× / 49,3× | 5% | 8% | US$451,14 | US$247,03 | US$726,33 |
| P/OCF (total con dividendos) | 35,2× / 33,0× / 47,3× | 5% | 8% | US$411,40 | US$222,44 | US$671,95 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$429,27 | US$235,21 | US$689,01 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$0,84 | US$0,84 | US$0,84 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$428,42 | US$234,37 | US$688,17 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$374,37 | US$211,19 | US$590,83 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 11,72%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$288,33 | US$302,15 | US$295,09 | US$295,19 | OK |
| EV/EBITDA | Conservador | US$250,01 | US$190,45 | US$165,59 | US$202,02 | OK |
| EV/EBITDA | Optimista | US$395,68 | US$453,97 | US$485,22 | US$444,96 | OK |
| EV/FCFF | Base | US$287,13 | US$323,61 | US$320,25 | US$310,33 | OK |
| EV/FCFF | Conservador | US$306,87 | US$220,21 | US$180,67 | US$235,92 | OK |
| EV/FCFF | Optimista | US$379,27 | US$471,41 | US$522,17 | US$457,62 | OK |
| P/E | Base | US$304,70 | US$321,13 | US$313,77 | US$313,20 | OK |
| P/E | Conservador | US$251,44 | US$191,40 | US$166,09 | US$202,98 | OK |
| P/E | Optimista | US$392,99 | US$453,71 | US$485,40 | US$444,04 | OK |
| P/FCFE | Base | US$319,26 | US$332,08 | US$323,57 | US$324,97 | OK |
| P/FCFE | Conservador | US$327,90 | US$210,77 | US$177,21 | US$238,63 | OK |
| P/FCFE | Optimista | US$416,06 | US$477,65 | US$520,90 | US$471,54 | OK |
| P/OCF | Base | US$264,56 | US$298,03 | US$295,07 | US$285,89 | OK |
| P/OCF | Conservador | US$270,81 | US$194,24 | US$159,58 | US$208,21 | OK |
| P/OCF | Optimista | US$350,50 | US$435,19 | US$481,90 | US$422,53 | OK |

Múltiplos consolidados hoy: US$305,42 / US$211,55 / US$447,11 · DCF de las historias hoy: US$209,39 / US$125,59 / US$318,06 · Ponderado hoy: US$267,01 / US$177,17 / US$395,49 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NVDA la diferencia es de +46% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$259,29 por acción y los múltiplos, US$230,76 hoy: 11% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$233,95 supone que los ingresos crecen 25,3% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 17,9% (+7,4 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$292,01 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,7%, WACC de los años 4-10 10,5%, ROE de FY+3 131,6% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 28,3x | 20,0x | +41% | 7,6% | 6,4% | +1,2 pp | Revisar: el múltiplo vale 41% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 39,8x | 25,8x | +53% | 7,8% | 6,4% | +1,4 pp | Revisar: el múltiplo vale 53% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 35,5x | 23,7x | +50% | 8,9% | 7,4% | +1,4 pp | Revisar: el múltiplo vale 50% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 37,9x | 24,5x | +54% | 8,9% | 7,3% | +1,5 pp | Revisar: el múltiplo vale 54% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 35,2x | 25,0x | +41% | 8,6% | 7,3% | +1,2 pp | Revisar: el múltiplo vale 41% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$267,01 | — |
| Múltiplos Base +20% | US$303,38 | +13,6% |
| Múltiplos Base −20% | US$230,64 | −13,6% |
| Crecimiento años 2-5 +2 pp | US$274,77 | +2,9% |
| Crecimiento años 2-5 −2 pp | US$259,87 | −2,7% |
| Margen objetivo +3 pp | US$271,15 | +1,6% |
| Margen objetivo −3 pp | US$262,87 | −1,6% |
| WACC +1 pp | US$262,39 | −1,7% |
| WACC −1 pp | US$271,96 | +1,9% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 27,12 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 4,46 | 28,32 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 36,69 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 38,57 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 4,16 | 39,77 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 53,63 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 32,45 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 5,05 | 35,53 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 43,09 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 36,65 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 3,92 | 37,90 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 49,29 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 33,02 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 3,57 | 35,25 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 47,31 | Múltiplo optimista elegido con el protocolo v3 |
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
