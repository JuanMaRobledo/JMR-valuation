---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Uber Technologies, Inc"
ticker: "UBER"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1R3V8gISxXCYIujVFSITu0svVBC3AsN4GF_pQHHLs5dw/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Uber Technologies, Inc (UBER) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$81,56 por acción.** Complemento: DCF esperado por probabilidades US$73,99; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$27,74–US$110,31; precio con MOS 35% sobre el esperado: US$48,09; precio de referencia US$68,51. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Plataforma madura que escala márgenes** (valor principal) | 45% | US$81,56 | US$36,70 |
| Conservadora · Robotaxis y regulación presionan la movilidad | 25% | US$49,80 | US$12,45 |
| Disrupción · Deterioro de los fundamentales: Waymo y Tesla desintermedian a Uber | 10% | US$27,74 | US$2,77 |
| Optimista · Uber es la red de los vehículos autónomos | 20% | US$110,31 | US$22,06 |
| **DCF esperado (complemento)** | 100% | **US$73,99** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$88,85 por acción y los múltiplos, US$83,89 hoy: 6% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$81,56 | US$71,68 | US$77,60 | US$48,09 | US$107,45 |
| Conservador | US$49,80 | US$49,59 | US$49,71 | US$48,09 | US$64,96 |
| Optimista | US$110,31 | US$101,03 | US$106,60 | US$48,09 | US$152,91 |

## 2. Datos

- Hoja del modelo: [UBER plantilla maestra](https://docs.google.com/spreadsheets/d/1R3V8gISxXCYIujVFSITu0svVBC3AsN4GF_pQHHLs5dw/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$68,51.
- Peers: datos de mercado de yfinance consultados el 2026-09-30 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 9,9% | 13,0% | 15,4% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 7,6% | 11,0% | 15,1% | Input B29 |
| Margen EBIT objetivo | 16,3% | 21,3% | 26,3% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,20 / 2,00 | — | Input B32/B33 |
| DCF por acción hoy | US$49,80 | US$81,56 | US$110,31 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,20, ERP 4,65%, Ke 10,88%, costo de la deuda después de impuestos 4,55%, peso del patrimonio 90,7%, WACC inicial 10,29% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Uber es rentable desde 2023; los cierres anteriores tienen EBITDA y utilidad negativos. La etapa actual es Dec '23 a LTM. En P/E se quita Dec '24: la utilidad de 2024 incluye la liberación de ~US$6.400 millones de la reserva de impuestos diferidos, que baja el P/E a 13x. La utilidad del LTM incluye revaluaciones de sus participaciones (Didi, Grab, Aurora) que se compensan entre trimestres (−US$1.500 millones en el 1T26, +US$1.600 millones en el 2T26). Se excluye la columna sin fecha de la hoja. En EV/EBITDA se quita también Dec '23 (69x): fue el primer año con EBITDA positivo (US$1.933 millones) y el múltiplo no es representativo. B: plataformas de movilidad, reparto y viajes (DoorDash, Airbnb, Booking, Grab, Expedia), datos de yfinance al 29-sep-2026. Se excluye Lyft (P/E de 2x por la liberación de su reserva de impuestos; EV/EBITDA de 112x) y, en P/E, DoorDash (98x con margen de 4%). Sin ajuste: Uber crece ~15-18% con margen creciente, en la mitad del grupo (más que Booking y Expedia, menos que DoorDash). λ = 0 (30-sep-2026): el justificado C usa g perpetuo de 6,7% con un ROE de 54% para siempre y Ke − g de apenas 1,9 pp, mientras el DCF supone que después del año 10 el retorno sobre el capital iguala al costo de capital; no es coherente con el DCF y se deja fuera del Base (se conserva como referencia en la tabla).

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '24, Dec '25, LTM (etapa actual) = 27,6x | 25,3x (n=5: DASH 55,0x, ABNB 30,1x, BKNG 12,1x, GRAB 25,3x, EXPE 11,0x) × 1,00 = 13,5x | 15,3x / 12,3x / 19,0x | **20,6x** | 14,7x | 24,8x | 30,4x / 19,8x / 37,7x |
| EV/FCFF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 19,1x (EV/FCF × 1,03 = FCF después de intereses ÷ FCFF) | 12,1x (n=3: DASH 37,0x, BKNG 12,1x, EXPE 6,7x) × 1,00 = 10,0x | 32,2x / 22,8x / 42,3x | **14,6x** | 11,7x | 22,6x | 19,6x / 15,6x / 32,0x |
| P/E | mediana Dec '23, Dec '25, LTM (etapa actual) = 17,2x | 23,2x (n=4: ABNB 35,8x, BKNG 18,0x, GRAB 28,4x, EXPE 16,6x) × 1,00 = 20,7x | 21,4x / 16,1x / 26,3x | **19,0x** | 15,5x | 19,5x | 23,4x / 18,2x / 24,1x |
| P/FCFE | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 17,9x | 12,8x (n=3: DASH 37,9x, BKNG 12,8x, EXPE 7,2x) × 1,00 = 10,6x | 23,9x / 18,3x / 29,1x | **14,3x** | 11,7x | 21,4x | 19,6x / 15,5x / 32,2x |
| P/OCF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 17,3x | 12,4x (n=3: DASH 28,6x, BKNG 12,4x, EXPE 6,1x) × 1,00 = 9,8x | 26,1x / 19,1x / 32,4x | **13,6x** | 10,8x | 18,9x | 19,6x / 15,3x / 28,8x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 20,6x: promedio de historia y peers 20,6x, acercado 0% al justificado (15,3x); rango de anclas 13,5x–27,6x. Atípicos excluidos de la historia: Dec '18 (-0,2x: métrica negativa o ~0); Dec '19 (-5,8x: métrica negativa o ~0); Dec '20 (-22,8x: métrica negativa o ~0); Dec '21 (-30,1x: métrica negativa o ~0); Dec '22 (-63,7x: métrica negativa o ~0); Dec '17 (1,2x: < 0,4x la mediana (27.6x), caída puntual); Dec '23 (69,3x: > 2,5x la mediana (27.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 14,6x: promedio de historia y peers 14,6x, acercado 0% al justificado (32,2x); rango de anclas 10,0x–32,2x. Atípicos excluidos de la historia: Dec '18 (-0,2x: métrica negativa o ~0); Dec '19 (-9,7x: métrica negativa o ~0); Dec '20 (-29,1x: métrica negativa o ~0); Dec '21 (-119,0x: métrica negativa o ~0); Dec '17 (2,0x: < 0,4x la mediana (18.5x), caída puntual); Dec '22 (144,5x: > 2,5x la mediana (18.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 19,0x: promedio de historia y peers 19,0x, acercado 0% al justificado (21,4x); rango de anclas 17,2x–21,4x. Atípicos excluidos de la historia: Dec '17 (0,0x: métrica negativa o ~0); Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (-4,4x: métrica negativa o ~0); Dec '20 (-13,2x: métrica negativa o ~0); Dec '21 (-161,3x: métrica negativa o ~0); Dec '22 (-5,3x: métrica negativa o ~0); Dec '23 (68,4x: > 2,5x la mediana (16.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 14,3x: promedio de historia y peers 14,3x, acercado 0% al justificado (23,9x); rango de anclas 10,6x–23,9x. Atípicos excluidos de la historia: Dec '17 (0,0x: métrica negativa o ~0); Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (-10,4x: métrica negativa o ~0); Dec '20 (-28,1x: métrica negativa o ~0); Dec '21 (-110,0x: métrica negativa o ~0); Dec '22 (127,2x: > 2,5x la mediana (18.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 13,6x: promedio de historia y peers 13,6x, acercado 0% al justificado (26,1x); rango de anclas 9,8x–26,1x. Atípicos excluidos de la historia: Dec '17 (0,0x: métrica negativa o ~0); Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (-11,8x: métrica negativa o ~0); Dec '20 (-34,4x: métrica negativa o ~0); Dec '21 (-183,7x: métrica negativa o ~0); Dec '22 (77,2x: > 2,5x la mediana (17.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$71,68 frente a US$81,56 del DCF (−12%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$71,68 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Crecimiento»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,88%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$27,74) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$81,56 por acción.** Complemento: DCF esperado por probabilidades US$73,99. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$81,56 | US$49,80 | US$110,31 |
| EV/EBITDA | 20,6× / 14,7× / 24,8× | 10% | 25% | US$102,69 | US$61,35 | US$139,77 |
| EV/FCFF | 14,6× / 11,7× / 22,6× | 15% | 37% | US$37,78 | US$30,37 | US$58,99 |
| P/E | 19,0× / 15,5× / 19,5× | 5% | 12% | US$112,93 | US$78,04 | US$130,40 |
| P/FCFE | 14,3× / 11,7× / 21,4× | 5% | 12% | US$76,84 | US$56,51 | US$125,17 |
| P/OCF | 13,6× / 10,8× / 18,9× | 5% | 12% | US$64,92 | US$48,30 | US$96,13 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$71,68 | US$49,59 | US$101,03 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$77,60 | US$49,71 | US$106,60 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$111,16 | US$67,88 | US$150,36 |
| EV/EBITDA | 20,6× / 14,7× / 24,8× | 10% | 25% | US$155,82 | US$82,71 | US$226,19 |
| EV/FCFF | 14,6× / 11,7× / 22,6× | 15% | 37% | US$52,94 | US$35,87 | US$93,40 |
| P/E | 19,0× / 15,5× / 19,5× | 5% | 12% | US$152,28 | US$90,56 | US$190,66 |
| P/FCFE | 14,3× / 11,7× / 21,4× | 5% | 12% | US$102,73 | US$64,17 | US$184,26 |
| P/OCF | 13,6× / 10,8× / 18,9× | 5% | 12% | US$89,51 | US$56,84 | US$146,46 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 40% | 100% | US$101,87 | US$60,57 | US$156,74 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$107,45 | US$64,96 | US$152,91 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,88%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$88,05 | US$105,69 | US$114,32 | US$102,69 | OK |
| EV/EBITDA | Conservador | US$61,44 | US$61,95 | US$60,68 | US$61,35 | OK |
| EV/EBITDA | Optimista | US$108,44 | US$144,94 | US$165,94 | US$139,77 | OK |
| EV/FCFF | Base | US$34,71 | US$39,80 | US$38,84 | US$37,78 | OK |
| EV/FCFF | Conservador | US$33,34 | US$31,47 | US$26,32 | US$30,37 | OK |
| EV/FCFF | Optimista | US$46,16 | US$62,30 | US$68,52 | US$58,99 | OK |
| P/E | Base | US$110,37 | US$116,70 | US$111,72 | US$112,93 | OK |
| P/E | Conservador | US$87,89 | US$79,79 | US$66,44 | US$78,04 | OK |
| P/E | Optimista | US$116,24 | US$135,09 | US$139,88 | US$130,40 | OK |
| P/FCFE | Base | US$76,70 | US$78,45 | US$75,37 | US$76,84 | OK |
| P/FCFE | Conservador | US$65,79 | US$56,68 | US$47,08 | US$56,51 | OK |
| P/FCFE | Optimista | US$112,08 | US$128,26 | US$135,18 | US$125,17 | OK |
| P/OCF | Base | US$61,35 | US$67,75 | US$65,67 | US$64,92 | OK |
| P/OCF | Conservador | US$53,46 | US$49,75 | US$41,70 | US$48,30 | OK |
| P/OCF | Optimista | US$80,44 | US$100,49 | US$107,45 | US$96,13 | OK |

Múltiplos consolidados hoy: US$71,68 / US$49,59 / US$101,03 · DCF de las historias hoy: US$81,56 / US$49,80 / US$110,31 · Ponderado hoy: US$77,60 / US$49,71 / US$106,60 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para UBER la diferencia es de −12% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$88,85 por acción y los múltiplos, US$83,89 hoy: 6% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$68,51 supone que los ingresos crecen 8,5% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,0% (−2,5 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$111,16 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,9%, WACC de los años 4-10 9,7%, ROE de FY+3 60,3% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 20,6x | 14,5x | +40% | 7,3% | 6,2% | +1,0 pp | Revisar: el múltiplo vale 40% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 14,6x | 30,5x | −52% | 2,7% | 6,2% | −3,6 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 52% por debajo del DCF en FY+3. |
| P/E | 19,0x | 13,8x | +37% | 5,8% | 3,9% | +2,0 pp | Revisar: el múltiplo vale 37% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 14,3x | 15,4x | −8% | 3,6% | 4,1% | −0,5 pp | Coherente con el DCF. |
| P/OCF | 13,6x | 16,8x | −19% | 2,6% | 4,1% | −1,5 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$77,60 | — |
| Múltiplos Base +20% | US$83,31 | +7,3% |
| Múltiplos Base −20% | US$71,90 | −7,3% |
| Crecimiento años 2-5 +2 pp | US$81,49 | +5,0% |
| Crecimiento años 2-5 −2 pp | US$74,04 | −4,6% |
| Margen objetivo +3 pp | US$84,47 | +8,9% |
| Margen objetivo −3 pp | US$70,73 | −8,9% |
| WACC +1 pp | US$74,92 | −3,5% |
| WACC −1 pp | US$80,47 | +3,7% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Margen objetivo −3 pp, Múltiplos Base +20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 19,84 | 14,68 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 30,39 | 20,55 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 37,67 | 24,79 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 15,59 | 11,68 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 19,63 | 14,57 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 32,02 | 22,64 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 18,25 | 15,51 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 23,35 | 18,96 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 24,05 | 19,53 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 15,53 | 11,70 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 19,57 | 14,26 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 32,16 | 21,41 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 15,31 | 10,85 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 19,55 | 13,56 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 28,80 | 18,94 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/UBER_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1R3V8gISxXCYIujVFSITu0svVBC3AsN4GF_pQHHLs5dw/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-30 (LYFT, DASH, ABNB, BKNG, GRAB, EXPE).
- [Uber: resultados 2T26](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- [Uber: resultados 1T26](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000019/uberq126earningspressrelea.htm)

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
