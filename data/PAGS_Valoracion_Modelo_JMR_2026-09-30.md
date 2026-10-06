---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de PagSeguro Digital Ltd."
ticker: "PAGS"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1Q17gaT8w8fGx-3uRn7eCS_HsF0q-HZucEtgXGtVEIQY/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# PagSeguro Digital Ltd. (PAGS) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$12,26 por acción.** Complemento: DCF esperado por probabilidades US$11,68; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$9,35–US$13,32; precio con MOS 35% sobre el esperado: US$7,59; precio de referencia US$10,72. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$12,27), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Banco digital estable con ROAE de ~15%** (valor principal) | 45% | US$12,26 | US$5,51 |
| Conservadora · El PIX y la competencia erosionan | 30% | US$10,76 | US$3,23 |
| Disrupción · Deterioro de los fundamentales: Crisis de crédito en Brasil | 10% | US$9,35 | US$0,94 |
| Optimista · Crece el banco: crédito y depósitos | 15% | US$13,32 | US$2,00 |
| **DCF esperado (complemento)** | 100% | **US$11,68** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$11,92 por acción y los múltiplos, US$8,36 hoy: 30% por debajo del DCF, fuera del rango de ±25%. La diferencia viene de P/FCFE: en la proyección Base el crédito de PagBank absorbe caja y el FCFE de FY+3 queda muy por debajo de la utilidad. P/E, el método más confiable para una financiera, queda cerca del DCF.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$12,26 | US$12,56 | US$12,44 | US$7,59 | US$16,55 |
| Conservador | US$10,76 | US$8,35 | US$9,32 | US$7,59 | US$12,19 |
| Optimista | US$13,32 | US$14,60 | US$14,09 | US$7,59 | US$19,22 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - PAGS](https://docs.google.com/spreadsheets/d/1Q17gaT8w8fGx-3uRn7eCS_HsF0q-HZucEtgXGtVEIQY/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$10,72.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 2,0% | 5,0% | 9,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 2,0% | 6,0% | 9,0% | Input B29 |
| Margen EBIT objetivo | 11,0% | 14,0% | 16,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,40 / 1,40 | — | Input B32/B33 |
| DCF por acción hoy | US$10,76 | US$12,26 | US$13,32 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 0,82, ERP 6,94%, Ke 10,98%, costo de la deuda después de impuestos 5,00%, peso del patrimonio 99,5%, WACC inicial 10,95% y terminal 11,91%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: PagSeguro cotiza a 5-12x utilidades desde 2022; no hay un cambio de etapa. Se usa la mediana de los últimos cierres depurados, sin la columna sin fecha. B: pagos y banca digital (StoneCo, Nu, dLocal, PayPal, Adyen), datos de yfinance al 29-sep-2026. Se excluye en P/E a Shift4 (58x por amortización y deuda) y, en los múltiplos de flujo, StoneCo (su flujo incluye los fondos de clientes: P/FCF de 0,6x). Ajuste −30%: PagSeguro crece ~5% y opera en Brasil con Selic alta (costo de patrimonio de 13,4%), frente a Nu, dLocal y Adyen que crecen 20-50%. λ = 0,25: la PagSeguro de FY+3 del escenario Base es un banco digital de crecimiento moderado, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | No aplica: PagSeguro es una entidad financiera (PagBank): la deuda es materia prima del negocio, no financiación, y el valor empresa no tiene sentido; su peso en la categoría Financiera es 0%. | | | | | | |
| EV/FCFF | No aplica: Igual que EV/EBITDA: para una financiera el FCFF no se puede separar de la financiación; peso 0%. | | | | | | |
| P/E | mediana de los últimos 5 cierres + LTM depurados = 7,6x | 16,9x (n=5: STNE 3,5x, NU 16,9x, DLO 20,1x, PYPL 10,2x, ADYEY 24,5x) × 0,70 = 11,8x | 13,1x / 10,5x / 15,8x | **10,6x** | 7,8x | 12,1x | 6,2x / —x / —x |
| P/FCFE | mediana de los últimos 5 cierres + LTM depurados = 6,5x | 10,1x (n=3: DLO 10,4x, FOUR 10,1x, PYPL 7,0x) × 0,70 = 7,1x | 19,2x / 15,7x / 23,0x | **9,9x** | 6,9x | 10,4x | 2,5x / —x / —x |
| P/OCF | mediana de los últimos 5 cierres + LTM depurados = 3,2x | 6,2x (n=3: DLO 9,4x, FOUR 4,9x, PYPL 6,2x) × 0,70 = 4,3x | 8,9x / 7,8x / 9,3x | **5,1x** | 4,2x | 5,2x | 1,7x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **P/E.** Base 10,6x: promedio de historia y peers 9,7x, acercado 25% al justificado (13,1x); rango de anclas 7,6x–13,1x. Atípicos excluidos de la historia: Dec '21 (39,7x: > 2,5x la mediana (8.7x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 9,9x: promedio de historia y peers 6,8x, acercado 25% al justificado (19,2x); rango de anclas 6,5x–19,2x. Atípicos excluidos de la historia: Dec '21 (-54,5x: métrica negativa o ~0); Dec '24 (-1,9x: métrica negativa o ~0). Aplicable con cautela: el FCFE proyectado es positivo pero bajo frente a la utilidad porque el crecimiento de la cartera de crédito consume caja. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 5,1x: promedio de historia y peers 3,8x, acercado 25% al justificado (8,9x); rango de anclas 3,2x–8,9x. Atípicos excluidos de la historia: Dec '24 (-3,1x: métrica negativa o ~0); Dec '21 (51,8x: > 2,5x la mediana (4.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$12,56 frente a US$12,26 del DCF (+2%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$12,56 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Financiera»: DCF 40% y múltiplos 60% (P/E 38%, P/FCFE 22%). Sin peso (no aplica): EV/EBITDA, EV/FCFF, P/OCF. Costo del patrimonio (Ke) 10,98%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$9,35) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$12,26 por acción.** Complemento: DCF esperado por probabilidades US$11,68. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$12,26 | US$10,76 | US$13,32 |
| EV/EBITDA | 2,7× / 2,4× / 3,0× | 0% | 0% | US$8,27 | US$6,80 | US$9,80 |
| EV/FCFF | 2,3× / 2,0× / 2,5× | 0% | 0% | US$2,15 | US$2,70 | US$1,50 |
| P/E | 10,6× / 7,8× / 12,1× | 38% | 64% | US$14,50 | US$8,83 | US$18,61 |
| P/FCFE | 9,9× / 6,9× / 10,4× | 22% | 36% | US$9,15 | US$7,50 | US$7,57 |
| P/OCF | 5,1× / 4,2× / 5,2× | 0% | 0% | US$9,75 | US$8,67 | US$9,08 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$12,56 | US$8,35 | US$14,60 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$12,44 | US$9,32 | US$14,09 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$16,75 | US$14,71 | US$18,21 |
| EV/EBITDA (total con dividendos) | 2,7× / 2,4× / 3,0× | 0% | 0% | US$11,24 | US$8,70 | US$13,95 |
| EV/FCFF (total con dividendos) | 2,3× / 2,0× / 2,5× | 0% | 0% | US$3,08 | US$3,45 | US$2,53 |
| P/E (total con dividendos) | 10,6× / 7,8× / 12,1× | 38% | 64% | US$19,13 | US$11,29 | US$25,38 |
| P/FCFE (total con dividendos) | 9,9× / 6,9× / 10,4× | 22% | 36% | US$11,66 | US$9,11 | US$10,27 |
| P/OCF (total con dividendos) | 5,1× / 4,2× / 5,2× | 0% | 0% | US$12,72 | US$10,74 | US$12,45 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$16,41 | US$10,50 | US$19,89 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$1,25 | US$1,25 | US$1,25 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$15,16 | US$9,25 | US$18,64 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$16,55 | US$12,19 | US$19,22 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,98%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$8,18 | US$8,30 | US$8,33 | US$8,27 | OK |
| EV/EBITDA | Conservador | US$7,17 | US$6,75 | US$6,47 | US$6,80 | OK |
| EV/EBITDA | Optimista | US$9,19 | US$9,90 | US$10,31 | US$9,80 | OK |
| EV/FCFF | Base | US$1,95 | US$2,15 | US$2,36 | US$2,15 | OK |
| EV/FCFF | Conservador | US$2,85 | US$2,64 | US$2,63 | US$2,70 | OK |
| EV/FCFF | Optimista | US$1,02 | US$1,52 | US$1,96 | US$1,50 | OK |
| P/E | Base | US$14,94 | US$14,47 | US$14,10 | US$14,50 | OK |
| P/E | Conservador | US$9,34 | US$8,79 | US$8,37 | US$8,83 | OK |
| P/E | Optimista | US$18,58 | US$18,59 | US$18,67 | US$18,61 | OK |
| P/FCFE | Base | US$9,82 | US$9,01 | US$8,63 | US$9,15 | OK |
| P/FCFE | Conservador | US$8,35 | US$7,38 | US$6,77 | US$7,50 | OK |
| P/FCFE | Optimista | US$7,72 | US$7,39 | US$7,62 | US$7,57 | OK |
| P/OCF | Base | US$10,19 | US$9,66 | US$9,41 | US$9,75 | OK |
| P/OCF | Conservador | US$9,50 | US$8,54 | US$7,96 | US$8,67 | OK |
| P/OCF | Optimista | US$9,05 | US$8,97 | US$9,21 | US$9,08 | OK |

Múltiplos consolidados hoy: US$12,56 / US$8,35 / US$14,60 · DCF de las historias hoy: US$12,26 / US$10,76 / US$13,32 · Ponderado hoy: US$12,44 / US$9,32 / US$14,09 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para PAGS la diferencia es de +2% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$11,92 por acción y los múltiplos, US$8,36 hoy: 30% por debajo del DCF, fuera del rango de ±25%. La diferencia viene de P/FCFE: en la proyección Base el crédito de PagBank absorbe caja y el FCFE de FY+3 queda muy por debajo de la utilidad. P/E, el método más confiable para una financiera, queda cerca del DCF.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$10,72 supone que los ingresos crecen -16,4% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 5,8% (−22,2 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$16,75 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,0%, WACC de los años 4-10 11,4%, ROE de FY+3 17,3% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 2,7x | — | — | — | — | — | No aplica: PagSeguro es una entidad financiera (PagBank): la deuda es materia prima del negocio, no financiación, y el valor empres |
| EV/FCFF | 2,3x | — | — | — | — | — | No aplica: Igual que EV/EBITDA: para una financiera el FCFF no se puede separar de la financiación; peso 0%. |
| P/E | 10,6x | 9,2x | +14% | 2,8% | 0,1% | +2,7 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 14% por encima del DCF en FY+3. |
| P/FCFE | 9,9x | 14,7x | −30% | 0,8% | 3,9% | −3,1 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 30% por debajo del DCF en FY+3. |
| P/OCF | 5,1x | 6,8x | −24% | 1,7% | 3,9% | −2,3 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 24% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$12,44 | — |
| Múltiplos Base +20% | US$13,86 | +11,4% |
| Múltiplos Base −20% | US$11,01 | −11,4% |
| Crecimiento años 2-5 +2 pp | US$12,47 | +0,3% |
| Crecimiento años 2-5 −2 pp | US$12,40 | −0,3% |
| Margen objetivo +3 pp | US$12,44 | +0,0% |
| Margen objetivo −3 pp | US$12,44 | +0,0% |
| WACC +1 pp | US$12,20 | −1,9% |
| WACC −1 pp | US$12,69 | +2,1% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, WACC −1 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| PE | J8 | — | 7,80 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 6,16 | 10,56 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 12,11 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 6,94 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 2,50 | 9,89 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 10,38 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 4,18 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 1,75 | 5,06 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 5,21 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/PAGS_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1Q17gaT8w8fGx-3uRn7eCS_HsF0q-HZucEtgXGtVEIQY/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (STNE, NU, DLO, FOUR, PYPL, ADYEY).
- [Nasdaq: puntos del 1T26 de PagSeguro](https://www.nasdaq.com/articles/pagseguro-digital-q1-earnings-call-highlights)

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
