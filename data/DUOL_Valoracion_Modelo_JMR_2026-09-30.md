---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Duolingo, Inc."
ticker: "DUOL"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1k-ms7Yt54Or8wgUFD2LIuH1nvmgEmiJh_h_2hQwbL10/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Duolingo, Inc. (DUOL) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$115,16 por acción.** Complemento: DCF esperado por probabilidades US$109,24; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$60,21–US$149,46; precio con MOS 35% sobre el esperado: US$71,01; precio de referencia US$144,27. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La audiencia crece y la monetización se recupera en parte** (valor principal) | 40% | US$115,16 | US$46,06 |
| Conservadora · La monetización se estanca | 30% | US$90,87 | US$27,26 |
| Disrupción · Deterioro de los fundamentales: La IA generalista comoditiza los idiomas | 10% | US$60,21 | US$6,02 |
| Optimista · La IA sube el ingreso por usuario | 20% | US$149,46 | US$29,89 |
| **DCF esperado (complemento)** | 100% | **US$109,24** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$125,77 por acción y los múltiplos, US$121,75 hoy: 3% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$115,16 | US$107,67 | US$112,17 | US$71,01 | US$157,83 |
| Conservador | US$90,87 | US$90,89 | US$90,88 | US$71,01 | US$124,43 |
| Optimista | US$149,46 | US$126,14 | US$140,13 | US$71,01 | US$204,07 |

## 2. Datos

- Hoja del modelo: [DUOL análisis maestro](https://docs.google.com/spreadsheets/d/1k-ms7Yt54Or8wgUFD2LIuH1nvmgEmiJh_h_2hQwbL10/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$144,27.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 9,5% | 12,0% | 19,2% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 8,5% | 11,0% | 17,2% | Input B29 |
| Margen EBIT objetivo | 23,1% | 27,1% | 32,1% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,79 / 1,79 | — | Input B32/B33 |
| DCF por acción hoy | US$90,87 | US$115,16 | US$149,46 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,35, ERP 4,46%, Ke 11,01%, costo de la deuda después de impuestos 5,25%, peso del patrimonio 98,8%, WACC inicial 10,94% y terminal 9,22%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Duolingo salió a bolsa en 2021 y hasta 2023 tuvo utilidades cercanas a cero, con múltiplos de 50-650x que reflejan hipercrecimiento; tras la desaceleración de usuarios de 2025 el mercado la re-valoró, así que A usa solo el cierre FY25 y el LTM. El P/E del FY25 y del LTM se excluye: la utilidad incluye un beneficio tributario único de US$222,7 millones por la liberación de la reserva de valuación de impuestos diferidos (10-Q del 3T25 y 10-K FY2025); sin él, el P/E real es mucho más alto y los años anteriores no son representativos, así que el P/E se ancla en peers y fundamentales. B: suscripción de consumo y plataformas digitales con datos de yfinance al 29-sep-2026: Spotify, Netflix, Reddit y Pinterest. Se excluyen Bumble (ingresos −15%, acción en dificultades) y Match (ingresos en baja): están en otra etapa. Pinterest se excluye de P/E y EV/EBITDA porque su margen operativo GAAP es negativo. Ajuste 0%: Duolingo crece más que Spotify y Netflix (Base 19% el año 1 y 16% en los años 2-5, frente a ~13-14%), lo que justificaría una prima de ~10%, pero tiene una desaceleración reciente de usuarios, menor escala y riesgo de sustitución por asistentes de IA para aprender idiomas, que justifican un descuento similar. λ = 0,15: el múltiplo justificado es inestable para Duolingo porque su crecimiento de largo plazo (g ≈ 8-10%) queda a solo 2-3 puntos del WACC y del Ke; en el Optimista no se puede calcular. Por eso pesa poco.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 43,1x | 31,4x (n=3: SPOT 35,4x, NFLX 20,1x, RDDT 31,4x) × 1,00 = 31,4x | 16,9x / 14,6x / 19,3x | **34,2x** | 29,6x | 37,4x | 38,5x / 34,0x / 41,5x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 23,2x (EV/FCF × 1,30 = FCF después de intereses ÷ FCFF) | 24,9x (n=4: SPOT 28,9x, NFLX 25,0x, PINS 8,1x, RDDT 24,7x) × 1,00 = 24,9x | 27,8x / 21,4x / 33,5x | **24,6x** | 20,7x | 27,3x | 26,3x / 22,8x / 28,1x |
| P/E | sin historia representativa (El P/E del FY25 y del LTM se excluye: la utilidad incluye un beneficio tributario único de US$222,7 millones por la liberación de la reserva de valuación de impuestos diferidos (10-Q del 3T25 y 10-K FY2025); sin él, el P/E real es mucho más alto y los años anteriores no son representativos, así que el P/E se ancla en peers y fundamentales.) | 27,3x (n=3: SPOT 27,3x, NFLX 22,1x, RDDT 33,7x) × 1,00 = 27,3x | 11,9x / 9,6x / 15,3x | **25,0x** | 21,3x | 30,0x | 25,7x / 20,7x / 28,8x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 20,6x | 26,9x (n=4: SPOT 31,1x, NFLX 26,2x, PINS 8,2x, RDDT 27,5x) × 1,00 = 26,9x | 22,9x / 18,4x / 26,7x | **23,6x** | 20,1x | 25,8x | 25,8x / 22,9x / 27,3x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 19,6x | 25,9x (n=4: SPOT 30,4x, NFLX 24,5x, PINS 7,9x, RDDT 27,3x) × 1,00 = 25,9x | 18,5x / 15,4x / 21,2x | **22,1x** | 18,8x | 24,2x | 24,9x / 21,8x / 26,7x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 34,2x: promedio de historia y peers 37,2x, acercado 15% al justificado (16,9x); rango de anclas 16,9x–43,1x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (-34,2x: métrica negativa o ~0); Dec '22 (-36,9x: métrica negativa o ~0); Dec '23 (-1.584,2x: métrica negativa o ~0); Dec '24 (198,1x: > 2,5x la mediana (50.2x)). El EBITDA GAAP de Duolingo descuenta una compensación en acciones alta, por eso su múltiplo EV/EBITDA es mayor que el de los peers. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 24,6x: promedio de historia y peers 24,1x, acercado 15% al justificado (27,8x); rango de anclas 23,2x–27,8x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (349,7x: > 2,5x la mediana (49.7x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 25,0x: promedio de historia y peers 27,3x, acercado 15% al justificado (11,9x); rango de anclas 11,9x–27,3x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (-41,3x: métrica negativa o ~0); Dec '22 (-47,1x: métrica negativa o ~0); Dec '23 (648,1x: > 2,5x la mediana (96.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 23,6x: promedio de historia y peers 23,7x, acercado 15% al justificado (22,9x); rango de anclas 20,6x–26,9x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (443,4x: > 2,5x la mediana (57.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 22,1x: promedio de historia y peers 22,7x, acercado 15% al justificado (18,5x); rango de anclas 18,5x–25,9x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (269,9x: > 2,5x la mediana (52.9x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$107,67 frente a US$115,16 del DCF (−7%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$107,67 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Software»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 11,01%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$60,21) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$115,16 por acción.** Complemento: DCF esperado por probabilidades US$109,24. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$115,16 | US$90,87 | US$149,46 |
| EV/EBITDA | 34,2× / 29,6× / 37,4× | 10% | 25% | US$216,39 | US$172,29 | US$266,84 |
| EV/FCFF | 24,6× / 20,7× / 27,3× | 15% | 37% | US$102,14 | US$90,94 | US$112,01 |
| P/E | 25,0× / 21,3× / 30,0× | 5% | 12% | US$66,05 | US$50,20 | US$91,71 |
| P/FCFE | 23,6× / 20,1× / 25,8× | 5% | 12% | US$25,30 | US$27,78 | US$20,19 |
| P/OCF | 22,1× / 18,8× / 24,2× | 5% | 12% | US$30,82 | US$31,73 | US$27,49 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$107,67 | US$90,89 | US$126,14 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$112,17 | US$90,88 | US$140,13 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$157,54 | US$124,30 | US$204,46 |
| EV/EBITDA | 34,2× / 29,6× / 37,4× | 10% | 25% | US$310,00 | US$231,98 | US$407,84 |
| EV/FCFF | 24,6× / 20,7× / 27,3× | 15% | 37% | US$151,48 | US$125,22 | US$186,77 |
| P/E | 25,0× / 21,3× / 30,0× | 5% | 12% | US$96,53 | US$68,61 | US$143,43 |
| P/FCFE | 23,6× / 20,1× / 25,8× | 5% | 12% | US$44,11 | US$41,89 | US$49,66 |
| P/OCF | 22,1× / 18,8× / 24,2× | 5% | 12% | US$51,11 | US$46,82 | US$58,79 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 40% | 100% | US$158,27 | US$124,62 | US$203,48 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$157,83 | US$124,43 | US$204,07 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 11,01%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$202,84 | US$219,72 | US$226,61 | US$216,39 | OK |
| EV/EBITDA | Conservador | US$173,58 | US$173,72 | US$169,58 | US$172,29 | OK |
| EV/EBITDA | Optimista | US$229,37 | US$273,02 | US$298,14 | US$266,84 | OK |
| EV/FCFF | Base | US$91,42 | US$104,26 | US$110,73 | US$102,14 | OK |
| EV/FCFF | Conservador | US$89,55 | US$91,73 | US$91,54 | US$90,94 | OK |
| EV/FCFF | Optimista | US$83,97 | US$115,52 | US$136,53 | US$112,01 | OK |
| P/E | Base | US$60,35 | US$67,24 | US$70,57 | US$66,05 | OK |
| P/E | Conservador | US$49,75 | US$50,70 | US$50,15 | US$50,20 | OK |
| P/E | Optimista | US$76,15 | US$94,13 | US$104,85 | US$91,71 | OK |
| P/FCFE | Base | US$17,17 | US$26,50 | US$32,24 | US$25,30 | OK |
| P/FCFE | Conservador | US$24,49 | US$28,24 | US$30,62 | US$27,78 | OK |
| P/FCFE | Optimista | US$2,38 | US$21,89 | US$36,30 | US$20,19 | OK |
| P/OCF | Base | US$23,14 | US$31,96 | US$37,36 | US$30,82 | OK |
| P/OCF | Conservador | US$28,78 | US$32,17 | US$34,23 | US$31,73 | OK |
| P/OCF | Optimista | US$10,37 | US$29,12 | US$42,97 | US$27,49 | OK |

Múltiplos consolidados hoy: US$107,67 / US$90,89 / US$126,14 · DCF de las historias hoy: US$115,16 / US$90,87 / US$149,46 · Ponderado hoy: US$112,17 / US$90,88 / US$140,13 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para DUOL la diferencia es de −7% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$125,77 por acción y los múltiplos, US$121,75 hoy: 3% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$144,27 supone que los ingresos crecen 18,7% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,5% (+7,2 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$157,54 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,0%, WACC de los años 4-10 10,2%, ROE de FY+3 13,2% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 34,2x | 15,5x | +97% | 8,3% | 6,0% | +2,2 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 97% por encima del DCF en FY+3. |
| EV/FCFF | 24,6x | 25,4x | −4% | 5,9% | 6,0% | −0,1 pp | Coherente con el DCF. |
| P/E | 25,0x | 40,7x | −39% | 9,9% | 10,4% | −0,5 pp | Revisar: el múltiplo vale 39% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 23,6x | 84,3x | −72% | 6,5% | 9,7% | −3,2 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 72% por debajo del DCF en FY+3. |
| P/OCF | 22,1x | 68,1x | −68% | 7,1% | 9,7% | −2,6 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 68% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$112,17 | — |
| Múltiplos Base +20% | US$119,66 | +6,7% |
| Múltiplos Base −20% | US$104,67 | −6,7% |
| Crecimiento años 2-5 +2 pp | US$116,37 | +3,7% |
| Crecimiento años 2-5 −2 pp | US$108,30 | −3,4% |
| Margen objetivo +3 pp | US$118,03 | +5,2% |
| Margen objetivo −3 pp | US$106,30 | −5,2% |
| WACC +1 pp | US$109,27 | −2,6% |
| WACC −1 pp | US$115,26 | +2,8% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 33,98 | 29,64 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 38,51 | 34,21 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 41,50 | 37,44 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 22,83 | 20,70 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 26,29 | 24,61 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 28,10 | 27,26 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 20,66 | 21,33 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 25,74 | 24,96 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 28,79 | 30,00 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 22,89 | 20,08 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 25,82 | 23,60 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 27,28 | 25,80 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 21,80 | 18,83 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 24,89 | 22,08 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 26,67 | 24,20 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/DUOL_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1k-ms7Yt54Or8wgUFD2LIuH1nvmgEmiJh_h_2hQwbL10/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (SPOT, NFLX, MTCH, PINS, BMBL, RDDT).
- [Duolingo, Form 10-Q del 3T25 (30-sep-2025)](https://www.sec.gov/Archives/edgar/data/1562088/000162828025049743/duol-20250930.htm): liberación de la reserva de valuación, beneficio tributario único de US$222,7 millones.
- [Duolingo, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1562088/000162828026012494/duol-20251231.htm): beneficio tributario de US$231,7 millones en 2025.

## 10. Control de calidad

| Comprobación | ¿Cumple? |
|---|---|
| No se cambiaron fórmulas, pesos ni estructura (solo J8/J19/J30 y textos) | Sí |
| Cada múltiplo Base tiene sus tres anclas con fuente y fecha | Sí, con limitación: P/E sin historia representativa (anclado en B y C) |
| Ningún múltiplo se derivó del DCF ni se ajustó después de verlo | Sí |
| Cada Base dentro del rango de sus anclas | Sí |
| Conservador < Base < Optimista en los cinco métodos; J8/J19/J30 escritos | Sí |
| Métodos no aplicables declarados | Sí |
| «Supuestos de los Múltiplos» A3 y A12 completos | Sí |
| DCF hoy, múltiplos hoy y ponderado hoy reportados por separado | Sí |
| Chequeo VP3 < FY+3 en OK en los tres escenarios | Sí |
| DCF Conservador < Base < Optimista | Sí |
