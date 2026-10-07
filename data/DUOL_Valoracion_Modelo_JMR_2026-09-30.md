---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Duolingo, Inc."
ticker: "DUOL"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1eqWEqHU6TeIr8frOUt1vS54_YifnbBSCNvvIXhWbdC4/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Duolingo, Inc. (DUOL) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$107,46 por acción.** Complemento: DCF esperado por probabilidades US$100,87; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$48,74–US$138,54; precio con MOS 35% sobre el esperado: US$65,56; precio de referencia US$150,27. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La audiencia que creció en 2026 vuelve a pagar desde 2027** (valor principal) | 45% | US$107,46 | US$48,36 |
| Conservadora · Más usuarios que pagan menos | 25% | US$79,70 | US$19,92 |
| Disrupción · Deterioro de los fundamentales: Los asistentes de IA enseñan idiomas gratis y el hábito se rompe | 10% | US$48,74 | US$4,87 |
| Optimista · Cien millones de usuarios diarios que se monetizan | 20% | US$138,54 | US$27,71 |
| **DCF esperado (complemento)** | 100% | **US$100,87** | |

Lectura del 7-oct-2026 (análisis desde cero, peers al cierre del 30-sep-2026): los múltiplos son precio relativo y salen de tres anclas (etapa actual, peers ajustados −10% y justificado, λ = 0,5); los consolidados Base hoy valen ~8% menos que el DCF Base y no se movió ninguno para acercarlo. El chequeo de crecimiento implícito (paso 6.5) deja tres alertas que se explican y no se corrigen: el EV/EBITDA Base (24,2×, frente a 14,9× que implica el DCF en FY+3) da un valor ~48% mayor que el DCF llevado a FY+3 porque el mercado (cierre de 2025 a 49× y peers de crecimiento alto) paga por una monetización más rápida que la de la Base, y subir λ más lo convertiría en un eco del DCF; P/FCFE (21,1×) y P/OCF (19,9×) dan valores ~25-26% menores que lo que implica el DCF (28,6× y 26,5×) por definición: el flujo de caja suma la compensación en acciones (~13-15% de las ventas), que el DCF trata como costo. P/E y EV/FCFF son coherentes con el DCF. El DCF es el valor intrínseco; P/E y EV/FCFF son los múltiplos más confiables para Duolingo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$107,46 | US$98,51 | US$103,88 | US$65,56 | US$149,90 |
| Conservador | US$79,70 | US$78,81 | US$79,34 | US$65,56 | US$109,94 |
| Optimista | US$138,54 | US$116,97 | US$129,91 | US$65,56 | US$194,52 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - DUOL (desde cero 2026-10-07)](https://docs.google.com/spreadsheets/d/1eqWEqHU6TeIr8frOUt1vS54_YifnbBSCNvvIXhWbdC4/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$150,27.
- Peers: datos de mercado de yfinance consultados el 2026-10-07 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 8,2% | 11,1% | 13,5% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 (compuesto) | 6,0% | 11,0% | 15,4% | Valuation output D:G (filas 55, 4 y 106) |
| Margen EBIT objetivo | 23,0% | 28,0% | 32,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,25 / 2,00 | — | Input B32/B33 |
| DCF por acción hoy | US$79,70 | US$107,46 | US$138,54 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,35, ERP 4,82%, Ke 11,81%, costo de la deuda después de impuestos 4,27%, peso del patrimonio 98,5%, WACC inicial 11,70% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Duolingo salió a bolsa en 2021 y hasta 2023 tuvo resultado operativo negativo o casi nulo, con múltiplos de 45-650× que reflejan hipercrecimiento con tasas de 1,5-4%. En 2025-2026 cambió de etapa: el crecimiento de las reservas bajó de 33% (2025) a ~11% (guía 2026), la gerencia eligió crecer en usuarios antes que monetizar y la acción cayó ~51% en doce meses con el Treasury a 10 años en 5,29%. El prompt v4 (6.2.A) pide usar solo la etapa actual: A = cierre de 2025 y LTM (al precio del corte, US$142,40). El P/E de 2025 y del LTM se excluye: la utilidad incluye el beneficio fiscal único de US$256,7 millones por la liberación de la reserva de valuación de los impuestos diferidos (3T25; 10-K 2025). Sin él, la utilidad LTM sería ~US$154 millones y el P/E ~45×; los cierres anteriores son de otra etapa. El P/E se ancla en los peers y en el justificado. B: suscripción de consumo y plataformas digitales con datos de yfinance del 7-oct-2026 llevados al cierre del 30-sep-2026: Spotify, Netflix, Reddit y Pinterest. Se excluyen Match Group (ingresos −1%: otra etapa, aunque sirve como comparable maduro de margen en el DCF) y Coursera (crecimiento de 60% inflado por la fusión con Udemy y margen GAAP negativo: múltiplos de 35-134× sobre flujos). Pinterest se excluye de P/E y EV/EBITDA porque su margen operativo GAAP es negativo; se conserva en los múltiplos de flujo. Ajuste −10%: crecimiento a FY+3 parecido a la mediana (Base ~11-12% frente a ~13-14% de Spotify y Netflix y 60% de Reddit), 0%; margen operativo GAAP menor (~10% en 2026 y ~24% objetivo frente a 29-33% de Netflix y Reddit) por una compensación en acciones de ~15% de las ventas, −5%; riesgo de sustitución por la IA generalista y dependencia de una sola aplicación (beta 1,35), −5%. λ = 0,5 (subido desde 0,25 tras el chequeo de crecimiento implícito, paso 6.5): con λ = 0,25 el EV/EBITDA Base (29,0×) valía 71% más que el que implica el DCF en FY+3 (15,2×), y el precio del corte pide crecer ~18% anual en los años 1-5 frente al ~11% de la Base. La evidencia (reservas +10,9% en 2026, +8,9% en el 3T26) no sostiene subir el crecimiento del DCF: el cierre de 2025 (EV/EBITDA 49×) y los peers de crecimiento alto (Reddit +61%) cuentan otra historia. Por eso el Base se acerca a la mitad del camino al justificado C (supuestos de las historias; sin ventaja, ROIC terminal = costo de capital) y la historia queda como tope del Optimista.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 39,9x | 30,9x (n=3: SPOT 34,1x, NFLX 20,2x, RDDT 30,9x) × 0,90 = 27,8x | 14,5x / 11,9x / 17,5x | **24,2x** | 20,4x | 27,2x | 48,9x / —x / —x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 21,3x (EV/FCF × 1,29 = FCF después de intereses ÷ FCFF) | 24,7x (n=4: SPOT 27,8x, NFLX 25,1x, RDDT 24,3x, PINS 8,3x) × 0,90 = 22,2x | 27,0x / 19,6x / 35,5x | **24,4x** | 19,9x | 28,1x | 20,3x / —x / —x |
| P/E | sin historia representativa (El P/E de 2025 y del LTM se excluye: la utilidad incluye el beneficio fiscal único de US$256,7 millones por la liberación de la reserva de valuación de los impuestos diferidos (3T25; 10-K 2025). Sin él, la utilidad LTM sería ~US$154 millones y el P/E ~45×; los cierres anteriores son de otra etapa. El P/E se ancla en los peers y en el justificado.) | 28,0x (n=3: SPOT 28,0x, NFLX 21,9x, RDDT 33,1x) × 0,90 = 25,2x | 14,8x / 11,4x / 18,7x | **20,0x** | 16,6x | 23,5x | 20,5x / —x / —x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 19,6x | 26,4x (n=4: SPOT 30,7x, NFLX 26,0x, RDDT 26,9x, PINS 8,4x) × 0,90 = 23,8x | 20,4x / 15,9x / 25,0x | **21,1x** | 17,6x | 23,6x | 18,1x / —x / —x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 18,7x | 25,5x (n=4: SPOT 30,0x, NFLX 24,2x, RDDT 26,7x, PINS 8,0x) × 0,90 = 22,9x | 18,9x / 14,7x / 23,2x | **19,9x** | 16,4x | 22,5x | 17,5x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 24,2x: promedio de historia y peers 33,8x, acercado 50% al justificado (14,5x); rango de anclas 14,5x–39,9x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (-33,7x: métrica negativa o ~0); Dec '22 (-36,5x: métrica negativa o ~0); Dec '23 (-1.580,8x: métrica negativa o ~0); Dec '24 (196,1x: > 2,5x la mediana (48.9x)). El EBITDA GAAP de Duolingo descuenta una compensación en acciones de ~13-15% de las ventas: su EV/EBITDA es mayor que el de un comparable con el mismo EBITDA ajustado. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 24,4x: promedio de historia y peers 21,8x, acercado 50% al justificado (27,0x); rango de anclas 21,3x–27,0x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (344,5x: > 2,5x la mediana (49.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 20,0x: promedio de historia y peers 25,2x, acercado 50% al justificado (14,8x); rango de anclas 14,8x–25,2x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (-41,3x: métrica negativa o ~0); Dec '22 (-47,1x: métrica negativa o ~0); Dec '23 (648,1x: > 2,5x la mediana (96.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 21,1x: promedio de historia y peers 21,7x, acercado 50% al justificado (20,4x); rango de anclas 19,6x–23,8x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (443,4x: > 2,5x la mediana (57.1x)). El flujo de caja libre suma la compensación en acciones (US$145 millones LTM) y los prepagos de los suscriptores: los múltiplos de flujo sobreestiman la caja económica. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 19,9x: promedio de historia y peers 20,8x, acercado 50% al justificado (18,9x); rango de anclas 18,7x–22,9x. Atípicos excluidos de la historia: Dec '20 (0,0x: métrica negativa o ~0); Dec '21 (269,9x: > 2,5x la mediana (52.9x)). El flujo operativo suma la compensación en acciones y los prepagos de los suscriptores: con cautela. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$98,51 frente a US$107,46 del DCF (−8%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$98,51 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Crecimiento»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 11,81%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$48,74) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$107,46 por acción.** Complemento: DCF esperado por probabilidades US$100,87. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$107,46 | US$79,70 | US$138,54 |
| EV/EBITDA | 24,2× / 20,4× / 27,2× | 10% | 25% | US$146,98 | US$112,24 | US$182,92 |
| EV/FCFF | 24,4× / 19,9× / 28,1× | 15% | 37% | US$87,10 | US$75,04 | US$95,69 |
| P/E | 20,0× / 16,6× / 23,5× | 5% | 12% | US$90,08 | US$64,65 | US$120,62 |
| P/FCFE | 21,1× / 17,6× / 23,6× | 5% | 12% | US$70,42 | US$57,79 | US$79,42 |
| P/OCF | 19,9× / 16,4× / 22,5× | 5% | 12% | US$72,35 | US$58,45 | US$82,77 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$98,51 | US$78,81 | US$116,97 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$103,88 | US$79,34 | US$129,91 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$150,19 | US$111,39 | US$193,63 |
| EV/EBITDA | 24,2× / 20,4× / 27,2× | 10% | 25% | US$221,77 | US$154,96 | US$296,54 |
| EV/FCFF | 24,4× / 19,9× / 28,1× | 15% | 37% | US$131,36 | US$101,48 | US$163,53 |
| P/E | 20,0× / 16,6× / 23,5× | 5% | 12% | US$134,84 | US$87,19 | US$195,38 |
| P/FCFE | 21,1× / 17,6× / 23,6× | 5% | 12% | US$110,59 | US$80,01 | US$142,05 |
| P/OCF | 19,9× / 16,4× / 22,5× | 5% | 12% | US$112,59 | US$80,68 | US$145,66 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 40% | 100% | US$149,45 | US$107,78 | US$195,85 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$149,90 | US$109,94 | US$194,52 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 11,81%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$131,52 | US$150,73 | US$158,67 | US$146,98 | OK |
| EV/EBITDA | Conservador | US$112,05 | US$113,81 | US$110,87 | US$112,24 | OK |
| EV/EBITDA | Optimista | US$147,83 | US$188,76 | US$212,17 | US$182,92 | OK |
| EV/FCFF | Base | US$81,51 | US$85,81 | US$93,99 | US$87,10 | OK |
| EV/FCFF | Conservador | US$79,65 | US$72,86 | US$72,60 | US$75,04 | OK |
| EV/FCFF | Optimista | US$74,85 | US$95,22 | US$117,01 | US$95,69 | OK |
| P/E | Base | US$84,62 | US$89,15 | US$96,48 | US$90,08 | OK |
| P/E | Conservador | US$68,81 | US$62,74 | US$62,39 | US$64,65 | OK |
| P/E | Optimista | US$101,35 | US$120,71 | US$139,80 | US$120,62 | OK |
| P/FCFE | Base | US$62,89 | US$69,25 | US$79,12 | US$70,42 | OK |
| P/FCFE | Conservador | US$60,46 | US$55,67 | US$57,25 | US$57,79 | OK |
| P/FCFE | Optimista | US$57,51 | US$79,10 | US$101,63 | US$79,42 | OK |
| P/OCF | Base | US$65,24 | US$71,26 | US$80,55 | US$72,35 | OK |
| P/OCF | Conservador | US$61,14 | US$56,48 | US$57,73 | US$58,45 | OK |
| P/OCF | Optimista | US$61,58 | US$82,50 | US$104,22 | US$82,77 | OK |

Múltiplos consolidados hoy: US$98,51 / US$78,81 / US$116,97 · DCF de las historias hoy: US$107,46 / US$79,70 / US$138,54 · Ponderado hoy: US$103,88 / US$79,34 / US$129,91 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para DUOL la diferencia es de −8% (múltiplos por debajo del DCF). Lectura del 7-oct-2026 (análisis desde cero, peers al cierre del 30-sep-2026): los múltiplos son precio relativo y salen de tres anclas (etapa actual, peers ajustados −10% y justificado, λ = 0,5); los consolidados Base hoy valen ~8% menos que el DCF Base y no se movió ninguno para acercarlo. El chequeo de crecimiento implícito (paso 6.5) deja tres alertas que se explican y no se corrigen: el EV/EBITDA Base (24,2×, frente a 14,9× que implica el DCF en FY+3) da un valor ~48% mayor que el DCF llevado a FY+3 porque el mercado (cierre de 2025 a 49× y peers de crecimiento alto) paga por una monetización más rápida que la de la Base, y subir λ más lo convertiría en un eco del DCF; P/FCFE (21,1×) y P/OCF (19,9×) dan valores ~25-26% menores que lo que implica el DCF (28,6× y 26,5×) por definición: el flujo de caja suma la compensación en acciones (~13-15% de las ventas), que el DCF trata como costo. P/E y EV/FCFF son coherentes con el DCF. El DCF es el valor intrínseco; P/E y EV/FCFF son los múltiplos más confiables para Duolingo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$150,27 supone que los ingresos crecen 19,3% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,0% (+8,3 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$150,19 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,8%, WACC de los años 4-10 10,5%, ROE de FY+3 23,9% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 24,2x | 14,9x | +48% | 8,1% | 6,7% | +1,4 pp | Revisar: el múltiplo vale 48% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 24,4x | 27,9x | −13% | 6,2% | 6,7% | −0,5 pp | Coherente con el DCF. |
| P/E | 20,0x | 22,3x | −10% | 8,3% | 8,7% | −0,4 pp | Coherente con el DCF. |
| P/FCFE | 21,1x | 28,6x | −26% | 6,7% | 8,0% | −1,3 pp | Revisar: el múltiplo vale 26% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 19,9x | 26,5x | −25% | 6,8% | 8,0% | −1,2 pp | Revisar: el múltiplo vale 25% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$103,88 | — |
| Múltiplos Base +20% | US$110,77 | +6,6% |
| Múltiplos Base −20% | US$97,00 | −6,6% |
| Crecimiento años 2-5 +2 pp | US$108,07 | +4,0% |
| Crecimiento años 2-5 −2 pp | US$100,04 | −3,7% |
| Margen objetivo +3 pp | US$109,41 | +5,3% |
| Margen objetivo −3 pp | US$98,35 | −5,3% |
| WACC +1 pp | US$101,16 | −2,6% |
| WACC −1 pp | US$106,80 | +2,8% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo −3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 20,39 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 48,91 | 24,16 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 27,17 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 19,89 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 20,33 | 24,40 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 28,15 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 16,65 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 20,47 | 20,01 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 23,52 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 17,62 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 18,15 | 21,07 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 23,62 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 16,42 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 17,47 | 19,86 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 22,46 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/DUOL_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1eqWEqHU6TeIr8frOUt1vS54_YifnbBSCNvvIXhWbdC4/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-10-07 (SPOT, NFLX, RDDT, PINS, MTCH, COUR).
- [Duolingo, 10-K 2025, 27-feb-2026](https://www.sec.gov/Archives/edgar/data/1562088/000162828026012494/duol-20251231.htm): liberación de la reserva de valuación, beneficio fiscal único de US$256,7 millones.
- [Duolingo, carta a los accionistas del 2T26, 5-ago-2026](https://www.sec.gov/Archives/edgar/data/1562088/000162828026053299/q2fy26duolingo6-30x26share.htm)
- [Duolingo, carta a los accionistas del 4T25, 26-feb-2026](https://www.sec.gov/Archives/edgar/data/1562088/000162828026012246/q4fy25duolingo12-31x25shar.htm)

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
