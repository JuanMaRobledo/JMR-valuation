---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Afya Limited"
ticker: "AFYA"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1_CXhy_5n-V4rwfOSl8xI8455hywS5W92VBed_FCylvQ/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Afya Limited (AFYA) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$26,06 por acción.** Complemento: DCF esperado por probabilidades US$22,83; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$12,55–US$30,25; precio con MOS 35% sobre el esperado: US$14,84; precio de referencia US$12,22. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La escasez de plazas sostiene precio y margen** (valor principal) | 45% | US$26,06 | US$11,73 |
| Conservadora · Madurez: precio real plano | 30% | US$20,67 | US$6,20 |
| Disrupción · Deterioro de los fundamentales: Se liberan plazas y cae el precio | 15% | US$12,55 | US$1,88 |
| Optimista · Maduran los campus y crece lo digital | 10% | US$30,25 | US$3,02 |
| **DCF esperado (complemento)** | 100% | **US$22,83** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$25,29 por acción y los múltiplos, US$14,08 hoy: 44% por debajo del DCF, fuera del rango de ±25%. La brecha no es una inconsistencia del modelo: el mercado brasileño paga 5-7x EBITDA por la educación superior y Afya cotiza anclada a la relación de canje con Yduqs. El DCF manda; los múltiplos muestran cuánto descuenta hoy el mercado local.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$26,06 | US$15,29 | US$19,60 | US$14,84 | US$28,58 |
| Conservador | US$20,67 | US$12,97 | US$16,05 | US$14,84 | US$22,82 |
| Optimista | US$30,25 | US$17,82 | US$22,79 | US$14,84 | US$33,65 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - AFYA](https://docs.google.com/spreadsheets/d/1_CXhy_5n-V4rwfOSl8xI8455hywS5W92VBed_FCylvQ/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$12,22.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 4,7% | 6,0% | 9,1% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 3,8% | 5,0% | 8,2% | Input B29 |
| Margen EBIT objetivo | 30,0% | 33,0% | 35,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,50 / 1,20 | — | Input B32/B33 |
| DCF por acción hoy | US$20,67 | US$26,06 | US$30,25 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,18%, beta apalancada 1,20, ERP 7,33%, Ke 13,99%, costo de la deuda después de impuestos 7,39%, peso del patrimonio 58,1%, WACC inicial 11,22% y terminal 11,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: entre 2019 y 2021 Afya cotizaba a 30-90x por el crecimiento de sus facultades de medicina tras la salida a bolsa; desde 2024 la educación privada brasileña se re-valoró (tasas altas, madurez de plazas), así que A usa FY24, FY25 y el LTM. B: educación superior en Brasil (Cogna, Yduqs, Ser Educacional, Ânima) y Laureate (México y Perú), con datos de yfinance al 29-sep-2026. Se excluye Yduqs del P/E porque su utilidad está deprimida (P/E 24,8x frente a 6-7x del sector); Cruzeiro do Sul no tiene cotización disponible. Ajuste +10%: Afya tiene margen EBIT de ~33% frente a 17-26% de las otras educadoras brasileñas y un nicho regulado (plazas de medicina limitadas por el MEC) con demanda más estable. λ = 0,25: la Afya de FY+3 del escenario Base se parece a la de hoy (crecimiento de un dígito medio en reales).

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '24, Dec '25, LTM (etapa actual) = 6,5x | 5,2x (n=5: COGN3.SA 5,2x, YDUQ3.SA 5,2x, SEER3.SA 4,4x, ANIM3.SA 4,6x, LAUR 11,0x) × 1,10 = 5,7x | 11,9x / 10,8x / 13,3x | **7,5x** | 6,8x | 8,0x | 7,5x / 6,8x / 8,0x |
| EV/FCFF | mediana Dec '24, Dec '25, LTM (etapa actual) = 9,9x (EV/FCF × 0,70 = FCF después de intereses ÷ FCFF) | 5,7x (n=5: COGN3.SA 5,7x, YDUQ3.SA 4,9x, SEER3.SA 5,7x, ANIM3.SA 5,3x, LAUR 19,8x) × 1,10 = 6,2x | 17,5x / 16,3x / 19,5x | **10,4x** | 9,6x | 10,9x | 13,7x / 12,3x / 17,6x |
| P/E | mediana Dec '24, Dec '25, LTM (etapa actual) = 10,4x | 6,7x (n=4: COGN3.SA 6,1x, SEER3.SA 6,3x, ANIM3.SA 7,0x, LAUR 17,4x) × 1,10 = 7,3x | 7,9x / 7,3x / 8,4x | **8,6x** | 7,9x | 10,3x | 8,6x / 7,9x / 10,3x |
| P/FCFE | mediana Dec '24, Dec '25, LTM (etapa actual) = 10,7x | 4,4x (n=5: COGN3.SA 4,4x, YDUQ3.SA 3,1x, SEER3.SA 5,0x, ANIM3.SA 3,0x, LAUR 18,4x) × 1,10 = 4,8x | 11,9x / 11,3x / 12,8x | **8,8x** | 7,4x | 9,5x | 8,8x / 7,4x / 9,5x |
| P/OCF | mediana Dec '24, Dec '25, LTM (etapa actual) = 7,1x | 2,9x (n=5: COGN3.SA 2,9x, YDUQ3.SA 2,0x, SEER3.SA 3,9x, ANIM3.SA 1,9x, LAUR 13,0x) × 1,10 = 3,1x | 9,5x / 8,4x / 11,0x | **6,2x** | 5,2x | 7,3x | 6,2x / 5,2x / 7,3x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 7,5x: promedio de historia y peers 6,1x, acercado 25% al justificado (11,9x); rango de anclas 5,7x–11,9x. Atípicos excluidos de la historia: Dec '19 (33,4x: > 2,5x la mediana (11.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 10,4x: promedio de historia y peers 8,1x, acercado 25% al justificado (17,5x); rango de anclas 6,2x–17,5x. Atípicos excluidos de la historia: Dec '19 (88,3x: > 2,5x la mediana (27.6x)); Dec '20 (93,5x: > 2,5x la mediana (27.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 8,6x: promedio de historia y peers 8,9x, acercado 25% al justificado (7,9x); rango de anclas 7,3x–10,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 8,8x: promedio de historia y peers 7,8x, acercado 25% al justificado (11,9x); rango de anclas 4,8x–11,9x. Atípicos excluidos de la historia: Dec '19 (91,1x: > 2,5x la mediana (21.5x)); Dec '20 (89,6x: > 2,5x la mediana (21.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 6,2x: promedio de historia y peers 5,1x, acercado 25% al justificado (9,5x); rango de anclas 3,1x–9,5x. Atípicos excluidos de la historia: Dec '19 (42,3x: > 2,5x la mediana (12.8x)); Dec '20 (44,4x: > 2,5x la mediana (12.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$15,29 frente a US$26,06 del DCF (−41%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$15,29 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 13,99%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$12,55) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$26,06 por acción.** Complemento: DCF esperado por probabilidades US$22,83. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$26,06 | US$20,67 | US$30,25 |
| EV/EBITDA | 7,5× / 6,8× / 8,0× | 20% | 33% | US$19,24 | US$15,95 | US$22,08 |
| EV/FCFF | 10,4× / 9,6× / 10,9× | 10% | 17% | US$15,17 | US$13,58 | US$16,43 |
| P/E | 8,6× / 7,9× / 10,3× | 20% | 33% | US$12,27 | US$10,63 | US$15,32 |
| P/FCFE | 8,8× / 7,4× / 9,5× | 5% | 8% | US$15,19 | US$12,07 | US$17,39 |
| P/OCF | 6,2× / 5,2× / 7,3× | 5% | 8% | US$11,91 | US$10,10 | US$13,95 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$15,29 | US$12,97 | US$17,82 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$19,60 | US$16,05 | US$22,79 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$38,59 | US$30,61 | US$44,79 |
| EV/EBITDA (total con dividendos) | 7,5× / 6,8× / 8,0× | 20% | 33% | US$27,64 | US$21,81 | US$32,54 |
| EV/FCFF (total con dividendos) | 10,4× / 9,6× / 10,9× | 10% | 17% | US$22,53 | US$18,77 | US$25,52 |
| P/E (total con dividendos) | 8,6× / 7,9× / 10,3× | 20% | 33% | US$17,60 | US$14,60 | US$22,47 |
| P/FCFE (total con dividendos) | 8,8× / 7,4× / 9,5× | 5% | 8% | US$19,51 | US$14,29 | US$22,71 |
| P/OCF (total con dividendos) | 6,2× / 5,2× / 7,3× | 5% | 8% | US$17,31 | US$14,05 | US$20,85 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$21,90 | US$17,63 | US$26,22 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$2,00 | US$2,00 | US$2,00 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$19,90 | US$15,63 | US$24,22 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$28,58 | US$22,82 | US$33,65 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 13,99%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$19,56 | US$19,32 | US$18,86 | US$19,24 | OK |
| EV/EBITDA | Conservador | US$17,00 | US$15,93 | US$14,93 | US$15,95 | OK |
| EV/EBITDA | Optimista | US$21,75 | US$22,34 | US$22,17 | US$22,08 | OK |
| EV/FCFF | Base | US$14,95 | US$15,15 | US$15,41 | US$15,17 | OK |
| EV/FCFF | Conservador | US$14,20 | US$13,69 | US$12,87 | US$13,58 | OK |
| EV/FCFF | Optimista | US$15,12 | US$16,74 | US$17,43 | US$16,43 | OK |
| P/E | Base | US$12,42 | US$12,32 | US$12,08 | US$12,27 | OK |
| P/E | Conservador | US$11,23 | US$10,61 | US$10,05 | US$10,63 | OK |
| P/E | Optimista | US$15,10 | US$15,49 | US$15,37 | US$15,32 | OK |
| P/FCFE | Base | US$18,82 | US$13,37 | US$13,37 | US$15,19 | OK |
| P/FCFE | Conservador | US$15,60 | US$10,76 | US$9,85 | US$12,07 | OK |
| P/FCFE | Optimista | US$20,82 | US$15,82 | US$15,53 | US$17,39 | OK |
| P/OCF | Base | US$11,98 | US$11,88 | US$11,88 | US$11,91 | OK |
| P/OCF | Conservador | US$10,45 | US$10,17 | US$9,68 | US$10,10 | OK |
| P/OCF | Optimista | US$13,47 | US$14,10 | US$14,28 | US$13,95 | OK |

Múltiplos consolidados hoy: US$15,29 / US$12,97 / US$17,82 · DCF de las historias hoy: US$26,06 / US$20,67 / US$30,25 · Ponderado hoy: US$19,60 / US$16,05 / US$22,79 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para AFYA la diferencia es de −41% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$25,29 por acción y los múltiplos, US$14,08 hoy: 44% por debajo del DCF, fuera del rango de ±25%. La brecha no es una inconsistencia del modelo: el mercado brasileño paga 5-7x EBITDA por la educación superior y Afya cotiza anclada a la relación de canje con Yduqs. El DCF manda; los múltiplos muestran cuánto descuenta hoy el mercado local.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$12,22 supone que los ingresos crecen -7,0% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 5,8% (−12,9 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$38,59 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 14,0%, WACC de los años 4-10 11,1%, ROE de FY+3 15,2% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 7,5x | 10,2x | −28% | 1,9% | 4,2% | −2,3 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 28% por debajo del DCF en FY+3. |
| EV/FCFF | 10,4x | 16,9x | −42% | 1,4% | 4,9% | −3,5 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 42% por debajo del DCF en FY+3. |
| P/E | 8,6x | 20,2x | −54% | 8,2% | 13,3% | −5,1 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 54% por debajo del DCF en FY+3. |
| P/FCFE | 8,8x | 18,4x | −49% | 2,4% | 8,1% | −5,8 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 49% por debajo del DCF en FY+3. |
| P/OCF | 6,2x | 14,9x | −55% | 1,0% | 8,2% | −7,2 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 55% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$19,60 | — |
| Múltiplos Base +20% | US$21,55 | +10,0% |
| Múltiplos Base −20% | US$17,65 | −10,0% |
| Crecimiento años 2-5 +2 pp | US$20,54 | +4,8% |
| Crecimiento años 2-5 −2 pp | US$18,73 | −4,4% |
| Margen objetivo +3 pp | US$20,67 | +5,4% |
| Margen objetivo −3 pp | US$18,53 | −5,4% |
| WACC +1 pp | US$18,97 | −3,2% |
| WACC −1 pp | US$20,27 | +3,4% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 6,83 | 6,83 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 7,51 | 7,51 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 8,04 | 8,04 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 12,28 | 9,62 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 13,65 | 10,43 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 17,58 | 10,94 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 7,90 | 7,90 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 8,61 | 8,61 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 10,35 | 10,35 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 7,42 | 7,42 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 8,80 | 8,80 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 9,49 | 9,49 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 5,18 | 5,18 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 6,23 | 6,23 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 7,32 | 7,32 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/AFYA_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1_CXhy_5n-V4rwfOSl8xI8455hywS5W92VBed_FCylvQ/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (COGN3.SA, YDUQ3.SA, SEER3.SA, ANIM3.SA, LAUR, CRUZ3.SA).

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
