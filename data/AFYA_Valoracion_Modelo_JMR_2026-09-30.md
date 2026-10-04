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

**Valor intrínseco principal · DCF Base hoy: US$20,76 por acción.** Complemento: DCF esperado por probabilidades US$18,48; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$11,26–US$23,87; precio con MOS 35% sobre el esperado: US$12,01; precio de referencia US$12,22. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La escasez de plazas sostiene precio y margen** (valor principal) | 45% | US$20,76 | US$9,34 |
| Conservadora · Madurez: precio real plano | 30% | US$16,88 | US$5,06 |
| Disrupción · Deterioro de los fundamentales: Se liberan plazas y cae el precio | 15% | US$11,26 | US$1,69 |
| Optimista · Maduran los campus y crece lo digital | 10% | US$23,87 | US$2,39 |
| **DCF esperado (complemento)** | 100% | **US$18,48** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$25,29 por acción y los múltiplos, US$14,08 hoy: 44% por debajo del DCF, fuera del rango de ±25%. La brecha no es una inconsistencia del modelo: el mercado brasileño paga 5-7x EBITDA por la educación superior y Afya cotiza anclada a la relación de canje con Yduqs. El DCF manda; los múltiplos muestran cuánto descuenta hoy el mercado local.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$20,76 | US$14,57 | US$17,05 | US$12,01 | US$24,58 |
| Conservador | US$16,88 | US$12,75 | US$14,40 | US$12,01 | US$20,15 |
| Optimista | US$23,87 | US$16,42 | US$19,40 | US$12,01 | US$28,44 |

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
| Sales-to-capital años 1-5 / 6-10 | — | 0,75 / 0,75 | — | Input B32/B33 |
| DCF por acción hoy | US$16,88 | US$20,76 | US$23,87 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,10, ERP 7,33%, Ke 13,35%, costo de la deuda después de impuestos 5,74%, peso del patrimonio 58,1%, WACC inicial 10,16% y terminal 11,11%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: entre 2019 y 2021 Afya cotizaba a 30-90x por el crecimiento de sus facultades de medicina tras la salida a bolsa; desde 2024 la educación privada brasileña se re-valoró (tasas altas, madurez de plazas), así que A usa FY24, FY25 y el LTM. B: educación superior en Brasil (Cogna, Yduqs, Ser Educacional, Ânima) y Laureate (México y Perú), con datos de yfinance al 29-sep-2026. Se excluye Yduqs del P/E porque su utilidad está deprimida (P/E 24,8x frente a 6-7x del sector); Cruzeiro do Sul no tiene cotización disponible. Ajuste +10%: Afya tiene margen EBIT de ~33% frente a 17-26% de las otras educadoras brasileñas y un nicho regulado (plazas de medicina limitadas por el MEC) con demanda más estable. λ = 0,25: la Afya de FY+3 del escenario Base se parece a la de hoy (crecimiento de un dígito medio en reales).

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '24, Dec '25, LTM (etapa actual) = 6,5x | 5,2x (n=5: COGN3.SA 5,2x, YDUQ3.SA 5,2x, SEER3.SA 4,4x, ANIM3.SA 4,6x, LAUR 11,0x) × 1,10 = 5,7x | 10,3x / 10,1x / 10,4x | **7,1x** | 6,6x | 7,4x | 7,5x / 6,8x / 8,0x |
| EV/FCFF | mediana Dec '24, Dec '25, LTM (etapa actual) = 9,9x (EV/FCF × 0,70 = FCF después de intereses ÷ FCFF) | 5,7x (n=5: COGN3.SA 5,7x, YDUQ3.SA 4,9x, SEER3.SA 5,7x, ANIM3.SA 5,3x, LAUR 19,8x) × 1,10 = 6,2x | 19,8x / 17,6x / 21,1x | **11,0x** | 10,0x | 11,4x | 13,7x / 12,3x / 17,6x |
| P/E | mediana Dec '24, Dec '25, LTM (etapa actual) = 10,4x | 6,7x (n=4: COGN3.SA 6,1x, SEER3.SA 6,3x, ANIM3.SA 7,0x, LAUR 17,4x) × 1,10 = 7,3x | 9,0x / 8,3x / 9,5x | **8,9x** | 8,1x | 10,6x | 8,6x / 7,9x / 10,3x |
| P/FCFE | mediana Dec '24, Dec '25, LTM (etapa actual) = 10,7x | 4,4x (n=5: COGN3.SA 4,4x, YDUQ3.SA 3,1x, SEER3.SA 5,0x, ANIM3.SA 3,0x, LAUR 18,4x) × 1,10 = 4,8x | 13,0x / 12,0x / 13,6x | **9,1x** | 7,6x | 9,7x | 8,8x / 7,4x / 9,5x |
| P/OCF | mediana Dec '24, Dec '25, LTM (etapa actual) = 7,1x | 2,9x (n=5: COGN3.SA 2,9x, YDUQ3.SA 2,0x, SEER3.SA 3,9x, ANIM3.SA 1,9x, LAUR 13,0x) × 1,10 = 3,1x | 10,1x / 8,3x / 11,1x | **6,4x** | 5,2x | 7,4x | 6,2x / 5,2x / 7,3x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 7,1x: promedio de historia y peers 6,1x, acercado 25% al justificado (10,3x); rango de anclas 5,7x–10,3x. Atípicos excluidos de la historia: Dec '19 (33,4x: > 2,5x la mediana (11.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 11,0x: promedio de historia y peers 8,1x, acercado 25% al justificado (19,8x); rango de anclas 6,2x–19,8x. Atípicos excluidos de la historia: Dec '19 (88,3x: > 2,5x la mediana (27.6x)); Dec '20 (93,5x: > 2,5x la mediana (27.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 8,9x: promedio de historia y peers 8,9x, acercado 25% al justificado (9,0x); rango de anclas 7,3x–10,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 9,1x: promedio de historia y peers 7,8x, acercado 25% al justificado (13,0x); rango de anclas 4,8x–13,0x. Atípicos excluidos de la historia: Dec '19 (91,1x: > 2,5x la mediana (21.5x)); Dec '20 (89,6x: > 2,5x la mediana (21.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 6,4x: promedio de historia y peers 5,1x, acercado 25% al justificado (10,1x); rango de anclas 3,1x–10,1x. Atípicos excluidos de la historia: Dec '19 (42,3x: > 2,5x la mediana (12.8x)); Dec '20 (44,4x: > 2,5x la mediana (12.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$14,57 frente a US$20,76 del DCF (−30%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$14,57 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 13,35%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$11,26) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$20,76 por acción.** Complemento: DCF esperado por probabilidades US$18,48. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$20,76 | US$16,88 | US$23,87 |
| EV/EBITDA | 7,1× / 6,6× / 7,4× | 20% | 33% | US$18,29 | US$15,59 | US$20,22 |
| EV/FCFF | 11,0× / 10,0× / 11,4× | 10% | 17% | US$13,32 | US$12,90 | US$13,32 |
| P/E | 8,9× / 8,1× / 10,6× | 20% | 33% | US$12,79 | US$11,04 | US$15,89 |
| P/FCFE | 9,1× / 7,6× / 9,7× | 5% | 8% | US$13,31 | US$11,30 | US$14,46 |
| P/OCF | 6,4× / 5,2× / 7,4× | 5% | 8% | US$10,58 | US$9,42 | US$11,54 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$14,57 | US$12,75 | US$16,42 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$17,05 | US$14,40 | US$19,40 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$30,23 | US$24,57 | US$34,76 |
| EV/EBITDA (total con dividendos) | 7,1× / 6,6× / 7,4× | 20% | 33% | US$26,03 | US$21,11 | US$29,56 |
| EV/FCFF (total con dividendos) | 11,0× / 10,0× / 11,4× | 10% | 17% | US$20,28 | US$17,86 | US$21,76 |
| P/E (total con dividendos) | 8,9× / 8,1× / 10,6× | 20% | 33% | US$18,13 | US$14,98 | US$23,04 |
| P/FCFE (total con dividendos) | 9,1× / 7,6× / 9,7× | 5% | 8% | US$17,06 | US$13,21 | US$19,00 |
| P/OCF (total con dividendos) | 6,4× / 5,2× / 7,4× | 5% | 8% | US$15,58 | US$13,11 | US$17,79 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$20,82 | US$17,20 | US$24,22 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$2,00 | US$2,00 | US$2,00 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$18,82 | US$15,20 | US$22,23 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$24,58 | US$20,15 | US$28,44 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 13,35%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$18,43 | US$18,36 | US$18,07 | US$18,29 | OK |
| EV/EBITDA | Conservador | US$16,50 | US$15,57 | US$14,69 | US$15,59 | OK |
| EV/EBITDA | Optimista | US$19,71 | US$20,45 | US$20,49 | US$20,22 | OK |
| EV/FCFF | Base | US$12,68 | US$13,16 | US$14,11 | US$13,32 | OK |
| EV/FCFF | Conservador | US$13,09 | US$13,16 | US$12,45 | US$12,90 | OK |
| EV/FCFF | Optimista | US$11,16 | US$13,67 | US$15,13 | US$13,32 | OK |
| P/E | Base | US$12,89 | US$12,84 | US$12,64 | US$12,79 | OK |
| P/E | Conservador | US$11,61 | US$11,02 | US$10,48 | US$11,04 | OK |
| P/E | Optimista | US$15,60 | US$16,07 | US$16,02 | US$15,89 | OK |
| P/FCFE | Base | US$16,71 | US$11,33 | US$11,90 | US$13,31 | OK |
| P/FCFE | Conservador | US$14,56 | US$10,07 | US$9,26 | US$11,30 | OK |
| P/FCFE | Optimista | US$17,28 | US$12,87 | US$13,24 | US$14,46 | OK |
| P/OCF | Base | US$10,37 | US$10,46 | US$10,89 | US$10,58 | OK |
| P/OCF | Conservador | US$9,50 | US$9,56 | US$9,19 | US$9,42 | OK |
| P/OCF | Optimista | US$10,50 | US$11,71 | US$12,40 | US$11,54 | OK |

Múltiplos consolidados hoy: US$14,57 / US$12,75 / US$16,42 · DCF de las historias hoy: US$20,76 / US$16,88 / US$23,87 · Ponderado hoy: US$17,05 / US$14,40 / US$19,40 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para AFYA la diferencia es de −30% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$25,29 por acción y los múltiplos, US$14,08 hoy: 44% por debajo del DCF, fuera del rango de ±25%. La brecha no es una inconsistencia del modelo: el mercado brasileño paga 5-7x EBITDA por la educación superior y Afya cotiza anclada a la relación de canje con Yduqs. El DCF manda; los múltiplos muestran cuánto descuenta hoy el mercado local.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$12,22 supone que los ingresos crecen -6,9% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 5,8% (−12,7 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$30,23 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 13,3%, WACC de los años 4-10 10,6%, ROE de FY+3 17,1% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 7,1x | 8,1x | −14% | 3,0% | 3,9% | −0,9 pp | Coherente con el DCF. |
| EV/FCFF | 11,0x | 15,6x | −33% | 1,3% | 3,9% | −2,6 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 33% por debajo del DCF en FY+3. |
| P/E | 8,9x | 15,6x | −40% | 5,0% | 10,7% | −5,7 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 40% por debajo del DCF en FY+3. |
| P/FCFE | 9,1x | 17,0x | −44% | 2,1% | 7,1% | −5,0 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 44% por debajo del DCF en FY+3. |
| P/OCF | 6,4x | 13,3x | −48% | 1,0% | 7,1% | −6,0 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 48% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$17,05 | — |
| Múltiplos Base +20% | US$18,91 | +10,9% |
| Múltiplos Base −20% | US$15,18 | −10,9% |
| Crecimiento años 2-5 +2 pp | US$17,55 | +2,9% |
| Crecimiento años 2-5 −2 pp | US$16,58 | −2,7% |
| Margen objetivo +3 pp | US$18,00 | +5,6% |
| Margen objetivo −3 pp | US$16,09 | −5,6% |
| WACC +1 pp | US$16,52 | −3,1% |
| WACC −1 pp | US$17,60 | +3,3% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 6,83 | 6,64 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 7,51 | 7,12 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 8,04 | 7,37 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 12,28 | 10,00 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 13,65 | 10,99 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 17,58 | 11,37 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 7,90 | 8,14 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 8,61 | 8,90 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 10,35 | 10,64 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 7,42 | 7,58 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 8,80 | 9,08 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 9,49 | 9,70 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 5,18 | 5,17 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 6,23 | 6,39 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 7,32 | 7,36 | Múltiplo optimista elegido con el protocolo v3 |
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
