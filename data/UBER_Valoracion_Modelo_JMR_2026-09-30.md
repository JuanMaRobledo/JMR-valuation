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

**Valor intrínseco principal · DCF Base hoy: US$73,74 por acción.** Complemento: DCF esperado por probabilidades US$67,16; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$26,58–US$100,43; precio con MOS 35% sobre el esperado: US$43,65; precio de referencia US$68,11. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Plataforma madura que escala márgenes** (valor principal) | 45% | US$73,74 | US$33,18 |
| Conservadora · Robotaxis y regulación presionan la movilidad | 25% | US$44,93 | US$11,23 |
| Disrupción · Deterioro de los fundamentales: Waymo y Tesla desintermedian a Uber | 10% | US$26,58 | US$2,66 |
| Optimista · Uber es la red de los vehículos autónomos | 20% | US$100,43 | US$20,09 |
| **DCF esperado (complemento)** | 100% | **US$67,16** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$88,85 por acción y los múltiplos, US$83,89 hoy: 6% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$73,74 | US$78,56 | US$76,63 | US$43,65 | US$110,47 |
| Conservador | US$44,93 | US$53,96 | US$50,35 | US$43,65 | US$66,81 |
| Optimista | US$100,43 | US$98,56 | US$99,31 | US$43,65 | US$151,14 |

## 2. Datos

- Hoja del modelo: [UBER plantilla maestra](https://docs.google.com/spreadsheets/d/1R3V8gISxXCYIujVFSITu0svVBC3AsN4GF_pQHHLs5dw/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$68,11.
- Peers: datos de mercado de yfinance consultados el 2026-09-30 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 9,9% | 13,0% | 15,4% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 7,6% | 11,0% | 15,1% | Input B29 |
| Margen EBIT objetivo | 16,3% | 21,3% | 26,3% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,11 / 1,11 | — | Input B32/B33 |
| DCF por acción hoy | US$44,93 | US$73,74 | US$100,43 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 0,80, ERP 5,04%, Ke 9,34%, costo de la deuda después de impuestos 4,55%, peso del patrimonio 91,1%, WACC inicial 8,91% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Uber es rentable desde 2023; los cierres anteriores tienen EBITDA y utilidad negativos. La etapa actual es Dec '23 a LTM. En P/E se quita Dec '24: la utilidad de 2024 incluye la liberación de ~US$6.400 millones de la reserva de impuestos diferidos, que baja el P/E a 13x. La utilidad del LTM incluye revaluaciones de sus participaciones (Didi, Grab, Aurora) que se compensan entre trimestres (−US$1.500 millones en el 1T26, +US$1.600 millones en el 2T26). Se excluye la columna sin fecha de la hoja. En EV/EBITDA se quita también Dec '23 (69x): fue el primer año con EBITDA positivo (US$1.933 millones) y el múltiplo no es representativo. B: plataformas de movilidad, reparto y viajes (DoorDash, Airbnb, Booking, Grab, Expedia), datos de yfinance al 29-sep-2026. Se excluye Lyft (P/E de 2x por la liberación de su reserva de impuestos; EV/EBITDA de 112x) y, en P/E, DoorDash (98x con margen de 4%). Sin ajuste: Uber crece ~15-18% con margen creciente, en la mitad del grupo (más que Booking y Expedia, menos que DoorDash). λ = 0 (30-sep-2026): el justificado C usa g perpetuo de 6,7% con un ROE de 54% para siempre y Ke − g de apenas 1,9 pp, mientras el DCF supone que después del año 10 el retorno sobre el capital iguala al costo de capital; no es coherente con el DCF y se deja fuera del Base (se conserva como referencia en la tabla).

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '24, Dec '25, LTM (etapa actual) = 27,6x | 25,3x (n=5: DASH 55,0x, ABNB 30,1x, BKNG 12,1x, GRAB 25,3x, EXPE 11,0x) × 1,00 = 13,5x | 10,3x / 10,5x / 11,5x | **20,6x** | 16,2x | 23,9x | 30,4x / 19,8x / 37,7x |
| EV/FCFF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 19,1x (EV/FCF × 1,03 = FCF después de intereses ÷ FCFF) | 12,1x (n=3: DASH 37,0x, BKNG 12,1x, EXPE 6,7x) × 1,00 = 10,0x | 39,6x / 26,3x / 56,0x | **14,6x** | 11,5x | 23,1x | 19,6x / 15,6x / 32,0x |
| P/E | mediana Dec '23, Dec '25, LTM (etapa actual) = 17,2x | 23,2x (n=4: ABNB 35,8x, BKNG 18,0x, GRAB 28,4x, EXPE 16,6x) × 1,00 = 20,7x | 32,6x / 22,0x / 45,2x | **19,0x** | 15,0x | 19,5x | 23,4x / 18,2x / 24,1x |
| P/FCFE | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 17,9x | 12,8x (n=3: DASH 37,9x, BKNG 12,8x, EXPE 7,2x) × 1,00 = 10,6x | 36,5x / 24,9x / 50,1x | **14,3x** | 11,3x | 22,1x | 19,6x / 15,5x / 32,2x |
| P/OCF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 17,3x | 12,4x (n=3: DASH 28,6x, BKNG 12,4x, EXPE 6,1x) × 1,00 = 9,8x | 41,0x / 26,3x / 58,1x | **13,6x** | 10,4x | 19,7x | 19,6x / 15,3x / 28,8x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 20,6x: promedio de historia y peers 20,6x, acercado 0% al justificado (10,3x); rango de anclas 10,3x–27,6x. Atípicos excluidos de la historia: Dec '18 (-0,2x: métrica negativa o ~0); Dec '19 (-5,8x: métrica negativa o ~0); Dec '20 (-22,8x: métrica negativa o ~0); Dec '21 (-30,1x: métrica negativa o ~0); Dec '22 (-63,7x: métrica negativa o ~0); Dec '17 (1,2x: < 0,4x la mediana (27.6x), caída puntual); Dec '23 (69,3x: > 2,5x la mediana (27.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 14,6x: promedio de historia y peers 14,6x, acercado 0% al justificado (39,6x); rango de anclas 10,0x–39,6x. Atípicos excluidos de la historia: Dec '18 (-0,2x: métrica negativa o ~0); Dec '19 (-9,7x: métrica negativa o ~0); Dec '20 (-29,1x: métrica negativa o ~0); Dec '21 (-119,0x: métrica negativa o ~0); Dec '17 (2,0x: < 0,4x la mediana (18.5x), caída puntual); Dec '22 (144,5x: > 2,5x la mediana (18.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 19,0x: promedio de historia y peers 19,0x, acercado 0% al justificado (32,6x); rango de anclas 17,2x–32,6x. Atípicos excluidos de la historia: Dec '17 (0,0x: métrica negativa o ~0); Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (-4,4x: métrica negativa o ~0); Dec '20 (-13,2x: métrica negativa o ~0); Dec '21 (-161,3x: métrica negativa o ~0); Dec '22 (-5,3x: métrica negativa o ~0); Dec '23 (68,4x: > 2,5x la mediana (16.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 14,3x: promedio de historia y peers 14,3x, acercado 0% al justificado (36,5x); rango de anclas 10,6x–36,5x. Atípicos excluidos de la historia: Dec '17 (0,0x: métrica negativa o ~0); Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (-10,4x: métrica negativa o ~0); Dec '20 (-28,1x: métrica negativa o ~0); Dec '21 (-110,0x: métrica negativa o ~0); Dec '22 (127,2x: > 2,5x la mediana (18.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 13,6x: promedio de historia y peers 13,6x, acercado 0% al justificado (41,0x); rango de anclas 9,8x–41,0x. Atípicos excluidos de la historia: Dec '17 (0,0x: métrica negativa o ~0); Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (-11,8x: métrica negativa o ~0); Dec '20 (-34,4x: métrica negativa o ~0); Dec '21 (-183,7x: métrica negativa o ~0); Dec '22 (77,2x: > 2,5x la mediana (17.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$78,56 frente a US$73,74 del DCF (+7%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$78,56 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,34%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$26,58) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$73,74 por acción.** Complemento: DCF esperado por probabilidades US$67,16. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$73,74 | US$44,93 | US$100,43 |
| EV/EBITDA | 20,6× / 16,2× / 23,9× | 20% | 33% | US$105,73 | US$69,39 | US$138,88 |
| EV/FCFF | 14,6× / 11,5× / 23,1× | 10% | 17% | US$12,23 | US$16,63 | US$9,45 |
| P/E | 19,0× / 15,0× / 19,5× | 20% | 33% | US$101,92 | US$66,28 | US$119,55 |
| P/FCFE | 14,3× / 11,3× / 22,1× | 5% | 8% | US$49,21 | US$39,31 | US$77,02 |
| P/OCF | 13,6× / 10,4× / 19,7× | 5% | 8% | US$38,44 | US$32,25 | US$53,03 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$78,56 | US$53,96 | US$98,56 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$76,63 | US$50,35 | US$99,31 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$96,38 | US$58,72 | US$131,26 |
| EV/EBITDA | 20,6× / 16,2× / 23,9× | 20% | 33% | US$155,82 | US$90,97 | US$218,10 |
| EV/FCFF | 14,6× / 11,5× / 23,1× | 10% | 17% | US$29,34 | US$26,27 | US$43,95 |
| P/E | 19,0× / 15,0× / 19,5× | 20% | 33% | US$152,28 | US$87,58 | US$190,66 |
| P/FCFE | 14,3× / 11,3× / 22,1× | 5% | 8% | US$79,64 | US$53,18 | US$141,23 |
| P/OCF | 13,6× / 10,4× / 19,7× | 5% | 8% | US$67,55 | US$46,52 | US$108,63 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 60% | 100% | US$119,86 | US$72,20 | US$164,40 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$110,47 | US$66,81 | US$151,14 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,34%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$89,29 | US$108,69 | US$119,22 | US$105,73 | OK |
| EV/EBITDA | Conservador | US$68,51 | US$70,06 | US$69,60 | US$69,39 | OK |
| EV/EBITDA | Optimista | US$106,04 | US$143,72 | US$166,86 | US$138,88 | OK |
| EV/FCFF | Base | US$0,07 | US$14,17 | US$22,45 | US$12,23 | OK |
| EV/FCFF | Conservador | US$12,27 | US$17,52 | US$20,10 | US$16,63 | OK |
| EV/FCFF | Optimista | US$-17,93 | US$12,64 | US$33,63 | US$9,45 | OK |
| P/E | Base | US$83,94 | US$105,32 | US$116,51 | US$101,92 | OK |
| P/E | Conservador | US$64,65 | US$67,19 | US$67,01 | US$66,28 | OK |
| P/E | Optimista | US$88,41 | US$124,38 | US$145,87 | US$119,55 | OK |
| P/FCFE | Base | US$36,06 | US$50,63 | US$60,93 | US$49,21 | OK |
| P/FCFE | Conservador | US$38,17 | US$39,07 | US$40,69 | US$39,31 | OK |
| P/FCFE | Optimista | US$42,94 | US$80,07 | US$108,05 | US$77,02 | OK |
| P/OCF | Base | US$22,54 | US$41,11 | US$51,68 | US$38,44 | OK |
| P/OCF | Conservador | US$27,87 | US$33,29 | US$35,59 | US$32,25 | OK |
| P/OCF | Optimista | US$18,50 | US$57,46 | US$83,11 | US$53,03 | OK |

Múltiplos consolidados hoy: US$78,56 / US$53,96 / US$98,56 · DCF de las historias hoy: US$73,74 / US$44,93 / US$100,43 · Ponderado hoy: US$76,63 / US$50,35 / US$99,31 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para UBER la diferencia es de +7% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$88,85 por acción y los múltiplos, US$83,89 hoy: 6% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$68,11 supone que los ingresos crecen 10,2% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,0% (−0,7 pp). Coherente: el precio supone un crecimiento parecido al del DCF.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$96,38 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,3%, WACC de los años 4-10 9,1%, ROE de FY+3 60,3% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 20,6x | 12,5x | +62% | 7,7% | 6,9% | +0,9 pp | Revisar: el múltiplo vale 62% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 14,6x | 48,1x | −70% | 2,1% | 6,9% | −4,8 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 70% por debajo del DCF en FY+3. |
| P/E | 19,0x | 12,0x | +58% | 4,2% | 1,1% | +3,2 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 58% por encima del DCF en FY+3. |
| P/FCFE | 14,3x | 17,3x | −17% | 2,2% | 3,3% | −1,2 pp | Coherente con el DCF. |
| P/OCF | 13,6x | 19,3x | −30% | 1,0% | 3,3% | −2,4 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 30% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$76,63 | — |
| Múltiplos Base +20% | US$86,02 | +12,3% |
| Múltiplos Base −20% | US$67,24 | −12,3% |
| Crecimiento años 2-5 +2 pp | US$78,49 | +2,4% |
| Crecimiento años 2-5 −2 pp | US$74,93 | −2,2% |
| Margen objetivo +3 pp | US$81,52 | +6,4% |
| Margen objetivo −3 pp | US$71,75 | −6,4% |
| WACC +1 pp | US$74,89 | −2,3% |
| WACC −1 pp | US$78,50 | +2,4% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 19,84 | 16,16 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 30,39 | 20,55 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 37,67 | 23,90 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 15,59 | 11,47 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 19,63 | 14,57 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 32,02 | 23,13 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 18,25 | 15,00 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 23,35 | 18,96 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 24,05 | 19,53 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 15,53 | 11,31 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 19,57 | 14,26 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 32,16 | 22,13 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 15,31 | 10,44 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 19,55 | 13,56 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 28,80 | 19,72 | Múltiplo optimista elegido con el protocolo v3 |
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
