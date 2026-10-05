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

**Valor intrínseco principal · DCF Base hoy: US$109,60 por acción.** Complemento: DCF esperado por probabilidades US$103,97; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$57,40–US$142,11; precio con MOS 35% sobre el esperado: US$67,58; precio de referencia US$142,40. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La audiencia crece y la monetización se recupera en parte** (valor principal) | 40% | US$109,60 | US$43,84 |
| Conservadora · La monetización se estanca | 30% | US$86,56 | US$25,97 |
| Disrupción · Deterioro de los fundamentales: La IA generalista comoditiza los idiomas | 10% | US$57,40 | US$5,74 |
| Optimista · La IA sube el ingreso por usuario | 20% | US$142,11 | US$28,42 |
| **DCF esperado (complemento)** | 100% | **US$103,97** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$125,77 por acción y los múltiplos, US$121,75 hoy: 3% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$109,60 | US$102,02 | US$106,57 | US$67,58 | US$152,73 |
| Conservador | US$86,56 | US$86,37 | US$86,49 | US$67,58 | US$120,61 |
| Optimista | US$142,11 | US$119,17 | US$132,94 | US$67,58 | US$197,16 |

## 2. Datos

- Hoja del modelo: [DUOL análisis maestro](https://docs.google.com/spreadsheets/d/1k-ms7Yt54Or8wgUFD2LIuH1nvmgEmiJh_h_2hQwbL10/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$142,40.
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
| DCF por acción hoy | US$86,56 | US$109,60 | US$142,11 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,35, ERP 4,82%, Ke 11,80%, costo de la deuda después de impuestos 5,25%, peso del patrimonio 98,7%, WACC inicial 11,71% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Duolingo salió a bolsa en 2021 y hasta 2023 tuvo utilidades cercanas a cero, con múltiplos de 50-650x que reflejan hipercrecimiento; tras la desaceleración de usuarios de 2025 el mercado la re-valoró, así que A usa solo el cierre FY25 y el LTM. El P/E del FY25 y del LTM se excluye: la utilidad incluye un beneficio tributario único de US$222,7 millones por la liberación de la reserva de valuación de impuestos diferidos (10-Q del 3T25 y 10-K FY2025); sin él, el P/E real es mucho más alto y los años anteriores no son representativos, así que el P/E se ancla en peers y fundamentales. B: suscripción de consumo y plataformas digitales con datos de yfinance al 29-sep-2026: Spotify, Netflix, Reddit y Pinterest. Se excluyen Bumble (ingresos −15%, acción en dificultades) y Match (ingresos en baja): están en otra etapa. Pinterest se excluye de P/E y EV/EBITDA porque su margen operativo GAAP es negativo. Ajuste 0%: Duolingo crece más que Spotify y Netflix (Base 19% el año 1 y 16% en los años 2-5, frente a ~13-14%), lo que justificaría una prima de ~10%, pero tiene una desaceleración reciente de usuarios, menor escala y riesgo de sustitución por asistentes de IA para aprender idiomas, que justifican un descuento similar. λ = 0,15: el múltiplo justificado es inestable para Duolingo porque su crecimiento de largo plazo (g ≈ 8-10%) queda a solo 2-3 puntos del WACC y del Ke; en el Optimista no se puede calcular. Por eso pesa poco.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 43,1x | 31,4x (n=3: SPOT 35,4x, NFLX 20,1x, RDDT 31,4x) × 1,00 = 31,4x | 16,4x / 14,3x / 18,6x | **34,1x** | 29,6x | 37,3x | 38,5x / 34,0x / 41,5x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 23,2x (EV/FCF × 1,30 = FCF después de intereses ÷ FCFF) | 24,9x (n=4: SPOT 28,9x, NFLX 25,0x, PINS 8,1x, RDDT 24,7x) × 1,00 = 24,9x | 26,9x / 20,9x / 32,2x | **24,5x** | 20,6x | 27,1x | 26,3x / 22,8x / 28,1x |
| P/E | sin historia representativa (El P/E del FY25 y del LTM se excluye: la utilidad incluye un beneficio tributario único de US$222,7 millones por la liberación de la reserva de valuación de impuestos diferidos (10-Q del 3T25 y 10-K FY2025); sin él, el P/E real es mucho más alto y los años anteriores no son representativos, así que el P/E se ancla en peers y fundamentales.) | 27,3x (n=3: SPOT 27,3x, NFLX 22,1x, RDDT 33,7x) × 1,00 = 27,3x | 10,3x / 8,4x / 13,1x | **24,7x** | 21,3x | 29,6x | 25,7x / 20,7x / 28,8x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 20,6x | 26,9x (n=4: SPOT 31,1x, NFLX 26,2x, PINS 8,2x, RDDT 27,5x) × 1,00 = 26,9x | 20,4x / 16,7x / 23,4x | **23,2x** | 19,9x | 25,2x | 25,8x / 22,9x / 27,3x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 19,6x | 25,9x (n=4: SPOT 30,4x, NFLX 24,5x, PINS 7,9x, RDDT 27,3x) × 1,00 = 25,9x | 16,5x / 14,0x / 18,6x | **21,8x** | 18,7x | 23,7x | 24,9x / 21,8x / 26,7x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 34,1x: promedio de historia y peers 37,2x, acercado 15% al justificado (16,4x); rango de anclas 16,4x–43,1x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (-34,2x: métrica negativa o ~0); Dec '22 (-36,9x: métrica negativa o ~0); Dec '23 (-1.584,2x: métrica negativa o ~0); Dec '24 (198,1x: > 2,5x la mediana (50.2x)). El EBITDA GAAP de Duolingo descuenta una compensación en acciones alta, por eso su múltiplo EV/EBITDA es mayor que el de los peers. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 24,5x: promedio de historia y peers 24,1x, acercado 15% al justificado (26,9x); rango de anclas 23,2x–26,9x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (349,7x: > 2,5x la mediana (49.7x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 24,7x: promedio de historia y peers 27,3x, acercado 15% al justificado (10,3x); rango de anclas 10,3x–27,3x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (-41,3x: métrica negativa o ~0); Dec '22 (-47,1x: métrica negativa o ~0); Dec '23 (648,1x: > 2,5x la mediana (96.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 23,2x: promedio de historia y peers 23,7x, acercado 15% al justificado (20,4x); rango de anclas 20,4x–26,9x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (443,4x: > 2,5x la mediana (57.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 21,8x: promedio de historia y peers 22,7x, acercado 15% al justificado (16,5x); rango de anclas 16,5x–25,9x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (269,9x: > 2,5x la mediana (52.9x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$102,02 frente a US$109,60 del DCF (−7%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$102,02 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Software»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 11,80%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$57,40) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$109,60 por acción.** Complemento: DCF esperado por probabilidades US$103,97. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$109,60 | US$86,56 | US$142,11 |
| EV/EBITDA | 34,1× / 29,6× / 37,3× | 10% | 25% | US$205,50 | US$164,01 | US$252,79 |
| EV/FCFF | 24,5× / 20,6× / 27,1× | 15% | 37% | US$96,78 | US$86,37 | US$105,85 |
| P/E | 24,7× / 21,3× / 29,6× | 5% | 12% | US$62,22 | US$47,63 | US$85,92 |
| P/FCFE | 23,2× / 19,9× / 25,2× | 5% | 12% | US$23,67 | US$26,20 | US$18,72 |
| P/OCF | 21,8× / 18,7× / 23,7× | 5% | 12% | US$28,91 | US$30,00 | US$25,59 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$102,02 | US$86,37 | US$119,17 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$106,57 | US$86,49 | US$132,94 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$153,14 | US$120,95 | US$198,57 |
| EV/EBITDA | 34,1× / 29,6× / 37,3× | 10% | 25% | US$298,64 | US$223,96 | US$392,07 |
| EV/FCFF | 24,5× / 20,6× / 27,1× | 15% | 37% | US$145,61 | US$120,61 | US$179,13 |
| P/E | 24,7× / 21,3× / 29,6× | 5% | 12% | US$92,26 | US$66,02 | US$136,39 |
| P/FCFE | 23,2× / 19,9× / 25,2× | 5% | 12% | US$41,91 | US$40,08 | US$46,88 |
| P/OCF | 21,8× / 18,7× / 23,7× | 5% | 12% | US$48,67 | US$44,91 | US$55,65 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 40% | 100% | US$152,12 | US$120,10 | US$195,06 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$152,73 | US$120,61 | US$197,16 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 11,80%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$194,05 | US$208,71 | US$213,73 | US$205,50 | OK |
| EV/EBITDA | Conservador | US$166,40 | US$165,36 | US$160,29 | US$164,01 | OK |
| EV/EBITDA | Optimista | US$218,99 | US$258,80 | US$280,60 | US$252,79 | OK |
| EV/FCFF | Base | US$87,30 | US$98,83 | US$104,21 | US$96,78 | OK |
| EV/FCFF | Conservador | US$85,67 | US$87,12 | US$86,32 | US$86,37 | OK |
| EV/FCFF | Optimista | US$80,06 | US$109,28 | US$128,20 | US$105,85 | OK |
| P/E | Base | US$57,28 | US$63,37 | US$66,03 | US$62,22 | OK |
| P/E | Conservador | US$47,53 | US$48,11 | US$47,25 | US$47,63 | OK |
| P/E | Optimista | US$71,90 | US$88,25 | US$97,61 | US$85,92 | OK |
| P/FCFE | Base | US$16,20 | US$24,83 | US$30,00 | US$23,67 | OK |
| P/FCFE | Conservador | US$23,27 | US$26,64 | US$28,68 | US$26,20 | OK |
| P/FCFE | Optimista | US$2,23 | US$20,37 | US$33,55 | US$18,72 | OK |
| P/OCF | Base | US$21,88 | US$30,01 | US$34,83 | US$28,91 | OK |
| P/OCF | Conservador | US$27,42 | US$30,43 | US$32,14 | US$30,00 | OK |
| P/OCF | Optimista | US$9,75 | US$27,18 | US$39,83 | US$25,59 | OK |

Múltiplos consolidados hoy: US$102,02 / US$86,37 / US$119,17 · DCF de las historias hoy: US$109,60 / US$86,56 / US$142,11 · Ponderado hoy: US$106,57 / US$86,49 / US$132,94 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para DUOL la diferencia es de −7% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$125,77 por acción y los múltiplos, US$121,75 hoy: 3% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$142,40 supone que los ingresos crecen 19,7% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,5% (+8,2 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$153,14 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,8%, WACC de los años 4-10 10,5%, ROE de FY+3 13,2% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 34,1x | 15,7x | +95% | 8,6% | 6,4% | +2,2 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 95% por encima del DCF en FY+3. |
| EV/FCFF | 24,5x | 25,7x | −5% | 6,2% | 6,4% | −0,2 pp | Coherente con el DCF. |
| P/E | 24,7x | 41,0x | −40% | 11,1% | 11,4% | −0,4 pp | Revisar: el múltiplo vale 40% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 23,2x | 84,9x | −73% | 7,2% | 10,5% | −3,3 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 73% por debajo del DCF en FY+3. |
| P/OCF | 21,8x | 68,5x | −68% | 7,8% | 10,5% | −2,7 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 68% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$106,57 | — |
| Múltiplos Base +20% | US$113,66 | +6,7% |
| Múltiplos Base −20% | US$99,47 | −6,7% |
| Crecimiento años 2-5 +2 pp | US$110,56 | +3,7% |
| Crecimiento años 2-5 −2 pp | US$102,90 | −3,4% |
| Margen objetivo +3 pp | US$112,13 | +5,2% |
| Margen objetivo −3 pp | US$101,00 | −5,2% |
| WACC +1 pp | US$103,84 | −2,6% |
| WACC −1 pp | US$109,48 | +2,7% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 33,98 | 29,64 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 38,51 | 34,13 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 41,50 | 37,27 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 22,83 | 20,64 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 26,29 | 24,48 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 28,10 | 27,05 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 20,66 | 21,26 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 25,74 | 24,71 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 28,79 | 29,55 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 22,89 | 19,90 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 25,82 | 23,23 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 27,28 | 25,23 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 21,80 | 18,71 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 24,89 | 21,78 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 26,67 | 23,73 | Múltiplo optimista elegido con el protocolo v3 |
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
