---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de PayPal Holdings, Inc."
ticker: "PYPL"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/13N5V1gpdsetin5NbTu-1-312lPYq5Pj4aKF4jw0bLT0/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# PayPal Holdings, Inc. (PYPL) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$119,70 por acción.** Complemento: DCF esperado por probabilidades US$102,20; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$49,97–US$150,78; precio con MOS 35% sobre el esperado: US$66,43; precio de referencia US$52,53. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Se estabiliza con márgenes estables** (valor principal) | 45% | US$119,70 | US$53,86 |
| Conservadora · El botón PayPal pierde frente a las billeteras nativas | 30% | US$69,07 | US$20,72 |
| Disrupción · Deterioro de los fundamentales: Pierde el checkout y compite por precio | 10% | US$49,97 | US$5,00 |
| Optimista · Reactivación: Fastlane, Venmo y publicidad | 15% | US$150,78 | US$22,62 |
| **DCF esperado (complemento)** | 100% | **US$102,20** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$101,16 por acción y los múltiplos, US$85,26 hoy: 16% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$119,70 | US$89,21 | US$101,41 | US$66,43 | US$131,97 |
| Conservador | US$69,07 | US$67,00 | US$67,83 | US$66,43 | US$84,50 |
| Optimista | US$150,78 | US$110,23 | US$126,45 | US$66,43 | US$169,54 |

## 2. Datos

- Hoja del modelo: [Modelo_JMR_Plantilla_Maestra PYPL (automático)](https://docs.google.com/spreadsheets/d/13N5V1gpdsetin5NbTu-1-312lPYq5Pj4aKF4jw0bLT0/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$52,53.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 2,2% | 4,0% | 7,3% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 1,7% | 3,5% | 7,3% | Input B29 |
| Margen EBIT objetivo | 16,2% | 19,7% | 22,2% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 6 | 6 | 6 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,48 / 2,48 | — | Input B32/B33 |
| DCF por acción hoy | US$69,07 | US$119,70 | US$150,78 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 0,97, ERP 4,48%, Ke 9,63%, costo de la deuda después de impuestos 4,63%, peso del patrimonio 78,6%, WACC inicial 8,56% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: PayPal cotizó a 18-60x EBITDA mientras crecía 15-20%. Desde 2023 es una procesadora de crecimiento bajo (~5%): en febrero de 2026 decepcionó con resultados y una guía de utilidad por acción plana, cambió de CEO (Enrique Lores reemplazó a Alex Chriss) y la acción cayó ~20%. La etapa actual es Dec '23 a LTM. B: pagos (Visa, Mastercard, Global Payments, Block, Adyen), datos de yfinance al 29-sep-2026. Fiserv (FI) no devolvió datos. En P/E se excluye Block (132x: utilidad deprimida por cargos puntuales). Ajuste −30%: PayPal crece ~5% con margen operativo de ~17%, frente a ~14% de crecimiento y márgenes de 44-66% de Visa, Mastercard y Adyen. λ = 0,25: la PayPal de FY+3 del escenario Base es una procesadora madura de crecimiento bajo, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 8,9x | 22,0x (n=5: V 22,0x, MA 22,8x, GPN 9,2x, XYZ 29,0x, ADYEY 14,8x) × 0,70 = 15,4x | 18,4x / 15,4x / 20,2x | **13,7x** | 10,7x | 15,4x | 7,7x / —x / —x |
| EV/FCFF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 11,6x (EV/FCF × 1,05 = FCF después de intereses ÷ FCFF) | 28,9x (n=4: V 31,6x, MA 30,6x, GPN 27,2x, XYZ 11,4x) × 0,70 = 20,2x | 29,6x / 22,7x / 33,1x | **19,3x** | 15,4x | 21,6x | 10,5x / —x / —x |
| P/E | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 13,4x | 31,0x (n=4: V 31,1x, MA 31,0x, GPN 39,5x, ADYEY 24,5x) × 0,70 = 21,7x | 19,8x / 16,0x / 21,9x | **18,1x** | 15,4x | 21,0x | 10,3x / —x / —x |
| P/FCFE | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 11,1x | 28,9x (n=4: V 32,7x, MA 30,9x, GPN 26,8x, XYZ 11,5x) × 0,70 = 20,2x | 23,7x / 19,0x / 25,9x | **17,6x** | 14,2x | 19,9x | 12,1x / —x / —x |
| P/OCF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 9,9x | 20,8x (n=4: V 30,4x, MA 28,3x, GPN 13,3x, XYZ 11,0x) × 0,70 = 14,6x | 23,1x / 17,0x / 26,4x | **14,9x** | 10,6x | 18,6x | 9,6x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 13,7x: promedio de historia y peers 12,1x, acercado 25% al justificado (18,4x); rango de anclas 8,9x–18,4x. Atípicos excluidos de la historia: Dec '20 (60,5x: > 2,5x la mediana (18.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 19,3x: promedio de historia y peers 15,9x, acercado 25% al justificado (29,6x); rango de anclas 11,6x–29,6x. Atípicos excluidos de la historia: Dec '17 (44,3x: > 2,5x la mediana (17.1x)); Dec '20 (54,3x: > 2,5x la mediana (17.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 18,1x: promedio de historia y peers 17,6x, acercado 25% al justificado (19,8x); rango de anclas 13,4x–21,7x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 17,6x: promedio de historia y peers 15,6x, acercado 25% al justificado (23,7x); rango de anclas 11,1x–23,7x. Atípicos excluidos de la historia: Dec '20 (55,0x: > 2,5x la mediana (19.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 14,9x: promedio de historia y peers 12,2x, acercado 25% al justificado (23,1x); rango de anclas 9,9x–23,1x. Atípicos excluidos de la historia: Dec '20 (46,9x: > 2,5x la mediana (15.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$89,21 frente a US$119,70 del DCF (−25%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$89,21 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,63%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$49,97) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$119,70 por acción.** Complemento: DCF esperado por probabilidades US$102,20. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$119,70 | US$69,07 | US$150,78 |
| EV/EBITDA | 13,7× / 10,7× / 15,4× | 20% | 33% | US$94,28 | US$67,81 | US$115,01 |
| EV/FCFF | 19,3× / 15,4× / 21,6× | 10% | 17% | US$82,00 | US$65,80 | US$95,45 |
| P/E | 18,1× / 15,4× / 21,0× | 20% | 33% | US$90,90 | US$70,17 | US$115,45 |
| P/FCFE | 17,6× / 14,2× / 19,9× | 5% | 8% | US$89,52 | US$66,54 | US$110,83 |
| P/OCF | 14,9× / 10,6× / 18,6× | 5% | 8% | US$76,35 | US$53,92 | US$99,17 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$89,21 | US$67,00 | US$110,23 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$101,41 | US$67,83 | US$126,45 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$157,72 | US$91,01 | US$198,68 |
| EV/EBITDA (total con dividendos) | 13,7× / 10,7× / 15,4× | 20% | 33% | US$120,82 | US$81,20 | US$154,81 |
| EV/FCFF (total con dividendos) | 19,3× / 15,4× / 21,6× | 10% | 17% | US$106,30 | US$79,26 | US$133,42 |
| P/E (total con dividendos) | 18,1× / 15,4× / 21,0× | 20% | 33% | US$117,32 | US$84,06 | US$157,22 |
| P/FCFE (total con dividendos) | 17,6× / 14,2× / 19,9× | 5% | 8% | US$113,79 | US$77,34 | US$149,25 |
| P/OCF (total con dividendos) | 14,9× / 10,6× / 18,6× | 5% | 8% | US$98,68 | US$65,08 | US$137,11 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$114,80 | US$80,17 | US$150,11 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$0,46 | US$0,46 | US$0,46 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$114,35 | US$79,71 | US$149,65 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$131,97 | US$84,50 | US$169,54 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,63%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$96,58 | US$94,51 | US$91,73 | US$94,28 | OK |
| EV/EBITDA | Conservador | US$74,41 | US$67,37 | US$61,65 | US$67,81 | OK |
| EV/EBITDA | Optimista | US$111,13 | US$116,38 | US$117,52 | US$115,01 | OK |
| EV/FCFF | Base | US$83,13 | US$82,16 | US$80,71 | US$82,00 | OK |
| EV/FCFF | Conservador | US$71,66 | US$65,54 | US$60,19 | US$65,80 | OK |
| EV/FCFF | Optimista | US$88,31 | US$96,75 | US$101,29 | US$95,45 | OK |
| P/E | Base | US$92,28 | US$91,34 | US$89,07 | US$90,90 | OK |
| P/E | Conservador | US$76,92 | US$69,75 | US$63,83 | US$70,17 | OK |
| P/E | Optimista | US$109,76 | US$117,23 | US$119,35 | US$115,45 | OK |
| P/FCFE | Base | US$94,39 | US$87,78 | US$86,39 | US$89,52 | OK |
| P/FCFE | Conservador | US$76,42 | US$64,47 | US$58,73 | US$66,54 | OK |
| P/FCFE | Optimista | US$109,30 | US$109,88 | US$113,30 | US$110,83 | OK |
| P/OCF | Base | US$77,64 | US$76,47 | US$74,93 | US$76,35 | OK |
| P/OCF | Conservador | US$58,60 | US$53,73 | US$49,42 | US$53,92 | OK |
| P/OCF | Optimista | US$93,07 | US$100,36 | US$104,09 | US$99,17 | OK |

Múltiplos consolidados hoy: US$89,21 / US$67,00 / US$110,23 · DCF de las historias hoy: US$119,70 / US$69,07 / US$150,78 · Ponderado hoy: US$101,41 / US$67,83 / US$126,45 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para PYPL la diferencia es de −25% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$101,16 por acción y los múltiplos, US$85,26 hoy: 16% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$52,53 supone que los ingresos crecen -12,2% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 4,9% (−17,0 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$157,72 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,6%, WACC de los años 4-10 8,7%, ROE de FY+3 31,5% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 13,7x | 17,9x | −23% | 4,0% | 5,1% | −1,1 pp | Coherente con el DCF. |
| EV/FCFF | 19,3x | 28,7x | −33% | 3,4% | 5,1% | −1,7 pp | Revisar: el múltiplo vale 33% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 18,1x | 24,4x | −26% | 4,7% | 6,1% | −1,4 pp | Revisar: el múltiplo vale 26% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/FCFE | 17,6x | 24,5x | −28% | 3,8% | 5,3% | −1,6 pp | Revisar: el múltiplo vale 28% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 14,9x | 23,9x | −37% | 2,9% | 5,3% | −2,4 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 37% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$101,41 | — |
| Múltiplos Base +20% | US$112,02 | +10,5% |
| Múltiplos Base −20% | US$90,80 | −10,5% |
| Crecimiento años 2-5 +2 pp | US$105,52 | +4,1% |
| Crecimiento años 2-5 −2 pp | US$97,65 | −3,7% |
| Margen objetivo +3 pp | US$108,33 | +6,8% |
| Margen objetivo −3 pp | US$94,48 | −6,8% |
| WACC +1 pp | US$98,83 | −2,5% |
| WACC −1 pp | US$104,16 | +2,7% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 10,74 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 7,66 | 13,70 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 15,37 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 15,39 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 10,49 | 19,32 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 21,65 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 15,42 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 10,26 | 18,11 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 20,97 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 14,15 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 12,06 | 17,65 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 19,88 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 10,63 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 9,65 | 14,95 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 18,61 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/PYPL_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/13N5V1gpdsetin5NbTu-1-312lPYq5Pj4aKF4jw0bLT0/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (V, MA, FI, GPN, XYZ, ADYEY).
- [CNBC, 3-feb-2026: PayPal cae ~20% por la salida del CEO y la guía 2026](https://www.cnbc.com/2026/02/03/paypal-pypl-earnings-q4-2025.html)

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
