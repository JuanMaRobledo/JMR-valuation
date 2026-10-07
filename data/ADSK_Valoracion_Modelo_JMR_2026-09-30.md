---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Autodesk, Inc."
ticker: "ADSK"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1m-od4YZ7pQNvcQ8oFi78cKv72vQCr2S9Ak3jNDSnNfs/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Autodesk, Inc. (ADSK) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$192,58 por acción.** Complemento: DCF esperado por probabilidades US$166,46; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$57,76–US$236,72; precio con MOS 35% sobre el esperado: US$108,20; precio de referencia US$231,28. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Sistema de registro del diseño y la obra que crece a doble dígito bajo** (valor principal) | 45% | US$192,58 | US$86,66 |
| Conservadora · Crecimiento de un dígito y margen que se queda donde está | 25% | US$142,52 | US$35,63 |
| Disrupción · Deterioro de los fundamentales: La IA abarata el diseño y los clientes compran menos puestos | 15% | US$57,76 | US$8,66 |
| Optimista · Plataforma de datos del ciclo de vida que cobra por la IA | 15% | US$236,72 | US$35,51 |
| **DCF esperado (complemento)** | 100% | **US$166,46** | |

Lectura del 7-oct-2026 (análisis desde cero, peers al cierre del 30-sep-2026): los múltiplos son precio relativo y salen de tres anclas (etapa actual, peers ajustados y justificado); los consolidados Base hoy valen ~8% menos que el DCF Base y no se movió ninguno para acercarlo. El chequeo de crecimiento implícito (paso 6.5) marca tres alertas en sentido contrario al habitual: EV/FCFF (20,1×), P/FCFE (18,8×) y P/OCF (19,2×) valen 27-41% menos que lo que implica el DCF en FY+3 (26-32×). La causa es de definición, no de historia: el flujo de caja de los peers suma la compensación en acciones (9-11% de las ventas en Autodesk), que el DCF trata como costo, y el justificado (17-24×) tampoco cierra la brecha, así que subir λ no la corrige. La evidencia (facturación orgánica ~10-11%, RPO corriente +12%) sostiene el crecimiento del DCF; no se cambia ni el DCF ni los múltiplos. El DCF es el valor intrínseco; EV/EBITDA y P/E, coherentes con el DCF, son los múltiplos más confiables para Autodesk.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$192,58 | US$176,72 | US$183,07 | US$108,20 | US$264,11 |
| Conservador | US$142,52 | US$143,91 | US$143,35 | US$108,20 | US$198,40 |
| Optimista | US$236,72 | US$216,87 | US$224,81 | US$108,20 | US$333,12 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - ADSK (desde cero 2026-10-07)](https://docs.google.com/spreadsheets/d/1m-od4YZ7pQNvcQ8oFi78cKv72vQCr2S9Ak3jNDSnNfs/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$231,28.
- Peers: datos de mercado de yfinance consultados el 2026-10-07 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 8,0% | 11,1% | 12,8% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 (compuesto) | 5,6% | 8,8% | 10,3% | Valuation output D:G (filas 55, 4 y 106) |
| Margen EBIT objetivo | 30,2% | 34,2% | 38,2% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,21 / 1,21 | — | Input B32/B33 |
| DCF por acción hoy | US$142,52 | US$192,58 | US$236,72 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,43, ERP 4,77%, Ke 12,12%, costo de la deuda después de impuestos 4,24%, peso del patrimonio 90,9%, WACC inicial 11,40% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: los cierres de FY2021-FY2025 (P/E 51-61×, EV/EBITDA 41-81×) se formaron con tasas de 1,5-4% y el auge del software por suscripción; con el Treasury a 10 años en 5,29% (30-sep-2026) y la re-valoración del software de diseño de 2026 por el temor a la IA (Autodesk −27% desde su máximo; PTC, Bentley y Dassault también cayeron, Trefis, 10-sep-2026), esos cierres no describen lo que pagaría el mercado en FY+3. El prompt v4 (6.2.A) pide usar solo la etapa actual cuando hay una re-valoración del sector: A = cierre de FY2026 (ene-2026) y LTM. Los cierres de FY2017-FY2019 (pérdidas de la transición a suscripción) ya estaban excluidos. B: software de diseño e ingeniería: PTC, Bentley Systems y Dassault Systèmes (ADR), con las métricas de yfinance del 7-oct-2026 y los múltiplos llevados al cierre del 30-sep-2026 (fecha de corte): PTC subió 37% el 5-oct-2026 por la oferta de Schneider Electric (US$22.600 millones en efectivo, 42% de prima), un hecho posterior al corte que no entra en el ancla. Se excluyen Synopsys (la compra de Ansys infla el crecimiento a 42% y deja el ROE en 4%: múltiplos de 50-86×), Cadence (diseño de chips, otro mercado final con el ciclo de la IA: P/E 70×) y Trimble (hardware y utilidad negativa en los últimos doce meses). PTC crece −7% por la venta de Kepware y ThingWorx, no por dificultades: se conserva. Ajuste +5%: crecimiento a FY+3 algo mayor que la mediana (Base ~9-10% frente a ~8% de PTC orgánico, ~11% de Bentley y ~3-5% de Dassault), +5%; margen operativo GAAP mayor y en alza (26% LTM, ~31% objetivo, frente a 23-28%), +5%; riesgo algo mayor (beta 1,43, integración de MaintainX y exposición de AutoCAD LT a la IA), −5%. λ = 0,25: la empresa de FY+3 se parece a la de hoy (suscripción madura que crece ~9-10%), así que el Base se apoya sobre todo en la etapa actual y en los peers; el justificado C usa los supuestos de las historias y queda como el piso del rango.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Jan '26, LTM (etapa actual) = 24,8x | 16,7x (n=3: PTC 12,9x, BSY 23,7x, DASTY 16,7x) × 1,05 = 17,5x | 12,4x / 11,5x / 13,3x | **18,9x** | 17,1x | 21,5x | 19,3x / 18,1x / 22,1x |
| EV/FCFF | mediana Jan '26, LTM (etapa actual) = 19,1x | 17,7x (n=3: PTC 16,7x, BSY 21,3x, DASTY 17,7x) × 1,05 = 18,5x | 23,9x / 19,8x / 26,7x | **20,1x** | 18,1x | 22,2x | 22,0x / 19,4x / 23,7x |
| P/E | mediana Jan '26, LTM (etapa actual) = 37,9x | 20,3x (n=3: PTC 13,6x, BSY 35,1x, DASTY 20,3x) × 1,05 = 21,3x | 15,7x / 13,7x / 17,1x | **26,1x** | 22,3x | 31,3x | 26,5x / 23,6x / 32,3x |
| P/FCFE | mediana Jan '26, LTM (etapa actual) = 18,8x | 18,9x (n=3: PTC 16,3x, BSY 19,4x, DASTY 18,9x) × 1,05 = 19,9x | 17,1x / 14,9x / 18,6x | **18,8x** | 17,0x | 20,0x | 19,9x / 18,2x / 21,2x |
| P/OCF | mediana Jan '26, LTM (etapa actual) = 18,5x | 17,5x (n=3: PTC 16,0x, BSY 18,5x, DASTY 17,5x) × 1,05 = 18,4x | 21,4x / 17,1x / 23,9x | **19,2x** | 17,0x | 20,7x | 20,5x / 18,1x / 22,1x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 18,9x: promedio de historia y peers 21,1x, acercado 25% al justificado (12,4x); rango de anclas 12,4x–24,8x. Atípicos excluidos de la historia: Jan '17 (-49,4x: métrica negativa o ~0); Jan '18 (-64,3x: métrica negativa o ~0); Jan '19 (477,2x: > 2,5x la mediana (43.9x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 20,1x: promedio de historia y peers 18,8x, acercado 25% al justificado (23,9x); rango de anclas 18,5x–23,9x. Atípicos excluidos de la historia: Jan '18 (-517,0x: métrica negativa o ~0); Jan '17 (189,9x: > 2,5x la mediana (40.2x)); Jan '19 (108,0x: > 2,5x la mediana (40.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 26,1x: promedio de historia y peers 29,6x, acercado 25% al justificado (15,7x); rango de anclas 15,7x–37,9x. Atípicos excluidos de la historia: Jan '17 (-31,2x: métrica negativa o ~0); Jan '18 (-44,8x: métrica negativa o ~0); Jan '19 (-397,8x: métrica negativa o ~0); Jan '20 (205,1x: > 2,5x la mediana (58.7x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 18,8x: promedio de historia y peers 19,4x, acercado 25% al justificado (17,1x); rango de anclas 17,1x–19,9x. Atípicos excluidos de la historia: Jan '18 (-506,8x: métrica negativa o ~0); Jan '17 (191,2x: > 2,5x la mediana (39.7x)); Jan '19 (104,2x: > 2,5x la mediana (39.7x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 19,2x: promedio de historia y peers 18,4x, acercado 25% al justificado (21,4x); rango de anclas 18,4x–21,4x. Atípicos excluidos de la historia: Jan '17 (105,6x: > 2,5x la mediana (41.4x)); Jan '18 (28.044,3x: > 2,5x la mediana (41.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$176,72 frente a US$192,58 del DCF (−8%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$176,72 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 12,12%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$57,76) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$192,58 por acción.** Complemento: DCF esperado por probabilidades US$166,46. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$192,58 | US$142,52 | US$236,72 |
| EV/EBITDA | 18,9× / 17,1× / 21,5× | 20% | 33% | US$211,63 | US$170,47 | US$259,61 |
| EV/FCFF | 20,1× / 18,1× / 22,2× | 10% | 17% | US$102,49 | US$95,69 | US$116,14 |
| P/E | 26,1× / 22,3× / 31,3× | 20% | 33% | US$205,96 | US$158,77 | US$265,28 |
| P/FCFE | 18,8× / 17,0× / 20,0× | 5% | 8% | US$142,57 | US$122,72 | US$158,89 |
| P/OCF | 19,2× / 17,0× / 20,7× | 5% | 8% | US$102,80 | US$95,81 | US$111,69 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$176,72 | US$143,91 | US$216,87 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$183,07 | US$143,35 | US$224,81 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$271,42 | US$200,87 | US$333,62 |
| EV/EBITDA | 18,9× / 17,1× / 21,5× | 20% | 33% | US$307,87 | US$232,53 | US$393,76 |
| EV/FCFF | 20,1× / 18,1× / 22,2× | 10% | 17% | US$163,11 | US$137,63 | US$196,79 |
| P/E | 26,1× / 22,3× / 31,3× | 20% | 33% | US$298,95 | US$215,93 | US$402,20 |
| P/FCFE | 18,8× / 17,0× / 20,0× | 5% | 8% | US$196,86 | US$155,83 | US$230,67 |
| P/OCF | 19,2× / 17,0× / 20,7× | 5% | 8% | US$160,55 | US$136,15 | US$185,41 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 60% | 100% | US$259,24 | US$196,76 | US$332,79 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$264,11 | US$198,40 | US$333,12 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 12,12%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$200,99 | US$215,44 | US$218,45 | US$211,63 | OK |
| EV/EBITDA | Conservador | US$174,42 | US$172,01 | US$164,99 | US$170,47 | OK |
| EV/EBITDA | Optimista | US$233,30 | US$266,13 | US$279,39 | US$259,61 | OK |
| EV/FCFF | Base | US$86,39 | US$105,36 | US$115,73 | US$102,49 | OK |
| EV/FCFF | Conservador | US$92,14 | US$97,27 | US$97,66 | US$95,69 | OK |
| EV/FCFF | Optimista | US$87,78 | US$121,01 | US$139,63 | US$116,14 | OK |
| P/E | Base | US$196,29 | US$209,45 | US$212,12 | US$205,96 | OK |
| P/E | Conservador | US$163,15 | US$159,96 | US$153,21 | US$158,77 | OK |
| P/E | Optimista | US$238,67 | US$271,80 | US$285,38 | US$265,28 | OK |
| P/FCFE | Base | US$152,83 | US$135,20 | US$139,68 | US$142,57 | OK |
| P/FCFE | Conservador | US$142,79 | US$114,80 | US$110,57 | US$122,72 | OK |
| P/FCFE | Optimista | US$160,61 | US$152,39 | US$163,67 | US$158,89 | OK |
| P/OCF | Base | US$89,14 | US$105,34 | US$113,91 | US$102,80 | OK |
| P/OCF | Conservador | US$93,61 | US$97,20 | US$96,61 | US$95,81 | OK |
| P/OCF | Optimista | US$87,58 | US$115,92 | US$131,56 | US$111,69 | OK |

Múltiplos consolidados hoy: US$176,72 / US$143,91 / US$216,87 · DCF de las historias hoy: US$192,58 / US$142,52 / US$236,72 · Ponderado hoy: US$183,07 / US$143,35 / US$224,81 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para ADSK la diferencia es de −8% (múltiplos por debajo del DCF). Lectura del 7-oct-2026 (análisis desde cero, peers al cierre del 30-sep-2026): los múltiplos son precio relativo y salen de tres anclas (etapa actual, peers ajustados y justificado); los consolidados Base hoy valen ~8% menos que el DCF Base y no se movió ninguno para acercarlo. El chequeo de crecimiento implícito (paso 6.5) marca tres alertas en sentido contrario al habitual: EV/FCFF (20,1×), P/FCFE (18,8×) y P/OCF (19,2×) valen 27-41% menos que lo que implica el DCF en FY+3 (26-32×). La causa es de definición, no de historia: el flujo de caja de los peers suma la compensación en acciones (9-11% de las ventas en Autodesk), que el DCF trata como costo, y el justificado (17-24×) tampoco cierra la brecha, así que subir λ no la corrige. La evidencia (facturación orgánica ~10-11%, RPO corriente +12%) sostiene el crecimiento del DCF; no se cambia ni el DCF ni los múltiplos. El DCF es el valor intrínseco; EV/EBITDA y P/E, coherentes con el DCF, son los múltiplos más confiables para Autodesk.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$231,28 supone que los ingresos crecen 12,2% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 9,2% (+3,0 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$271,42 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 12,1%, WACC de los años 4-10 10,4%, ROE de FY+3 72,8% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 18,9x | 16,7x | +13% | 7,4% | 7,0% | +0,4 pp | Coherente con el DCF. |
| EV/FCFF | 20,1x | 32,2x | −40% | 5,1% | 7,0% | −1,9 pp | Revisar: el múltiplo vale 40% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 26,1x | 23,7x | +10% | 8,4% | 8,1% | +0,4 pp | Coherente con el DCF. |
| P/FCFE | 18,8x | 25,9x | −27% | 6,5% | 8,0% | −1,5 pp | Revisar: el múltiplo vale 27% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 19,2x | 32,4x | −41% | 5,2% | 8,0% | −2,7 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 41% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$183,07 | — |
| Múltiplos Base +20% | US$204,92 | +11,9% |
| Múltiplos Base −20% | US$161,21 | −11,9% |
| Crecimiento años 2-5 +2 pp | US$190,21 | +3,9% |
| Crecimiento años 2-5 −2 pp | US$176,54 | −3,6% |
| Margen objetivo +3 pp | US$190,46 | +4,0% |
| Margen objetivo −3 pp | US$175,68 | −4,0% |
| WACC +1 pp | US$178,48 | −2,5% |
| WACC −1 pp | US$187,98 | +2,7% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 18,08 | 17,06 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 19,32 | 18,95 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 22,14 | 21,49 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 19,39 | 18,10 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 21,96 | 20,06 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 23,72 | 22,18 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 23,59 | 22,32 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 26,53 | 26,11 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 32,30 | 31,26 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 18,17 | 16,97 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 19,92 | 18,79 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 21,18 | 19,96 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 18,07 | 17,01 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 20,46 | 19,18 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 22,07 | 20,67 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/ADSK_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1m-od4YZ7pQNvcQ8oFi78cKv72vQCr2S9Ak3jNDSnNfs/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-10-07 (PTC, BSY, DASTY, CDNS, SNPS, TRMB).
- [Autodesk, 10-Q del 2T FY27, 28-ago-2026](https://www.sec.gov/Archives/edgar/data/769397/000076939726000061/adsk-20260731.htm)
- [Autodesk, comunicado del 2T FY27, 27-ago-2026](https://www.sec.gov/Archives/edgar/data/769397/000076939726000059/q227pressrelease.htm)
- [Trefis, caída de la acción tras la guía, 10-sep-2026](https://www.trefis.com/stock/adsk/articles/614900/why-did-autodesk-stock-drop-so-soon-after-raising-its-forecast/2026-09-10)

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
