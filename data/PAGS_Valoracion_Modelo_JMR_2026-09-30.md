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

**Valor intrínseco principal · DCF Base hoy: US$12,71 por acción.** Complemento: DCF esperado por probabilidades US$12,38; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$10,62–US$13,66; precio con MOS 35% sobre el esperado: US$8,05; precio de referencia US$9,02. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$12,75), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Banco digital estable con ROAE de ~15%** (valor principal) | 45% | US$12,71 | US$5,72 |
| Conservadora · El PIX y la competencia erosionan | 30% | US$11,84 | US$3,55 |
| Disrupción · Deterioro de los fundamentales: Crisis de crédito en Brasil | 10% | US$10,62 | US$1,06 |
| Optimista · Crece el banco: crédito y depósitos | 15% | US$13,66 | US$2,05 |
| **DCF esperado (complemento)** | 100% | **US$12,38** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$11,92 por acción y los múltiplos, US$8,36 hoy: 30% por debajo del DCF, fuera del rango de ±25%. La diferencia viene de P/FCFE: en la proyección Base el crédito de PagBank absorbe caja y el FCFE de FY+3 queda muy por debajo de la utilidad. P/E, el método más confiable para una financiera, queda cerca del DCF.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$12,71 | US$10,72 | US$11,51 | US$8,05 | US$16,22 |
| Conservador | US$11,84 | US$8,50 | US$9,84 | US$8,05 | US$13,61 |
| Optimista | US$13,66 | US$12,56 | US$13,00 | US$8,05 | US$18,69 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - PAGS](https://docs.google.com/spreadsheets/d/1Q17gaT8w8fGx-3uRn7eCS_HsF0q-HZucEtgXGtVEIQY/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$9,02.
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
| DCF por acción hoy | US$11,84 | US$12,71 | US$13,66 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,12, ERP 7,47%, Ke 13,36%, costo de la deuda después de impuestos 4,78%, peso del patrimonio 99,5%, WACC inicial 13,32% y terminal 12,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: PagSeguro cotiza a 5-12x utilidades desde 2022; no hay un cambio de etapa. Se usa la mediana de los últimos cierres depurados, sin la columna sin fecha. B: pagos y banca digital (StoneCo, Nu, dLocal, PayPal, Adyen), datos de yfinance al 29-sep-2026. Se excluye en P/E a Shift4 (58x por amortización y deuda) y, en los múltiplos de flujo, StoneCo (su flujo incluye los fondos de clientes: P/FCF de 0,6x). Ajuste −30%: PagSeguro crece ~5% y opera en Brasil con Selic alta (costo de patrimonio de 14,7%), frente a Nu, dLocal y Adyen que crecen 20-50%. λ = 0,25: la PagSeguro de FY+3 del escenario Base es un banco digital de crecimiento moderado, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | No aplica: PagSeguro es una entidad financiera (PagBank): la deuda es materia prima del negocio, no financiación, y el valor empresa no tiene sentido; su peso en la categoría Financiera es 0%. | | | | | | |
| EV/FCFF | No aplica: Igual que EV/EBITDA: para una financiera el FCFF no se puede separar de la financiación; peso 0%. | | | | | | |
| P/E | mediana de los últimos 5 cierres + LTM depurados = 7,6x | 16,9x (n=5: STNE 3,5x, NU 16,9x, DLO 20,1x, PYPL 10,2x, ADYEY 24,5x) × 0,70 = 11,8x | 9,1x / 8,2x / 10,1x | **9,6x** | 7,4x | 11,4x | 6,2x / —x / —x |
| P/FCFE | mediana de los últimos 5 cierres + LTM depurados = 6,5x | 10,1x (n=3: DLO 10,4x, FOUR 10,1x, PYPL 7,0x) × 0,70 = 7,1x | 13,0x / 11,3x / 14,7x | **8,3x** | 6,0x | 10,3x | 2,5x / —x / —x |
| P/OCF | mediana de los últimos 5 cierres + LTM depurados = 3,2x | 6,2x (n=3: DLO 9,4x, FOUR 4,9x, PYPL 6,2x) × 0,70 = 4,3x | 6,2x / 6,0x / 6,1x | **4,4x** | 3,8x | 5,0x | 1,7x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **P/E.** Base 9,6x: promedio de historia y peers 9,7x, acercado 25% al justificado (9,1x); rango de anclas 7,6x–11,8x. Atípicos excluidos de la historia: Dec '21 (39,7x: > 2,5x la mediana (8.7x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 8,3x: promedio de historia y peers 6,8x, acercado 25% al justificado (13,0x); rango de anclas 6,5x–13,0x. Atípicos excluidos de la historia: Dec '21 (-54,5x: métrica negativa o ~0); Dec '24 (-1,9x: métrica negativa o ~0). Aplicable con cautela: el FCFE proyectado es positivo pero bajo frente a la utilidad porque el crecimiento de la cartera de crédito consume caja. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 4,4x: promedio de historia y peers 3,8x, acercado 25% al justificado (6,2x); rango de anclas 3,2x–6,2x. Atípicos excluidos de la historia: Dec '24 (-3,1x: métrica negativa o ~0); Dec '21 (51,8x: > 2,5x la mediana (4.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$10,72 frente a US$12,71 del DCF (−16%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$10,72 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Financiera»: DCF 40% y múltiplos 60% (P/E 35%, P/FCFE 20%, P/OCF 5%). Sin peso (no aplica): EV/EBITDA, EV/FCFF. Costo del patrimonio (Ke) 13,36%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$10,62) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$12,71 por acción.** Complemento: DCF esperado por probabilidades US$12,38. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$12,71 | US$11,84 | US$13,66 |
| EV/EBITDA | 2,7× / 2,4× / 3,0× | 0% | 0% | US$8,07 | US$6,64 | US$9,55 |
| EV/FCFF | 2,3× / 2,0× / 2,5× | 0% | 0% | US$2,10 | US$2,64 | US$1,46 |
| P/E | 9,6× / 7,4× / 11,4× | 35% | 58% | US$12,83 | US$9,28 | US$16,36 |
| P/FCFE | 8,3× / 6,0× / 10,3× | 20% | 33% | US$7,63 | US$7,22 | US$6,99 |
| P/OCF | 4,4× / 3,8× / 5,0× | 5% | 8% | US$8,28 | US$8,20 | US$8,18 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$10,72 | US$8,50 | US$12,56 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$11,51 | US$9,84 | US$13,00 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$18,51 | US$17,24 | US$19,90 |
| EV/EBITDA (total con dividendos) | 2,7× / 2,4× / 3,0× | 0% | 0% | US$11,43 | US$8,84 | US$14,18 |
| EV/FCFF (total con dividendos) | 2,3× / 2,0× / 2,5× | 0% | 0% | US$3,13 | US$3,50 | US$2,57 |
| P/E (total con dividendos) | 9,6× / 7,4× / 11,4× | 35% | 58% | US$17,75 | US$12,41 | US$23,33 |
| P/FCFE (total con dividendos) | 8,3× / 6,0× / 10,3× | 20% | 33% | US$10,21 | US$9,19 | US$9,91 |
| P/OCF (total con dividendos) | 4,4× / 3,8× / 5,0× | 5% | 8% | US$11,32 | US$10,65 | US$11,73 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$14,70 | US$11,19 | US$17,89 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$1,27 | US$1,27 | US$1,27 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$13,43 | US$9,92 | US$16,62 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$16,22 | US$13,61 | US$18,69 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 13,36%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$8,14 | US$8,10 | US$7,97 | US$8,07 | OK |
| EV/EBITDA | Conservador | US$7,14 | US$6,58 | US$6,19 | US$6,64 | OK |
| EV/EBITDA | Optimista | US$9,15 | US$9,65 | US$9,85 | US$9,55 | OK |
| EV/FCFF | Base | US$1,94 | US$2,10 | US$2,27 | US$2,10 | OK |
| EV/FCFF | Conservador | US$2,83 | US$2,57 | US$2,52 | US$2,64 | OK |
| EV/FCFF | Optimista | US$1,01 | US$1,49 | US$1,88 | US$1,46 | OK |
| P/E | Base | US$13,38 | US$12,81 | US$12,31 | US$12,83 | OK |
| P/E | Conservador | US$9,96 | US$9,24 | US$8,64 | US$9,28 | OK |
| P/E | Optimista | US$16,58 | US$16,37 | US$16,14 | US$16,36 | OK |
| P/FCFE | Base | US$8,24 | US$7,51 | US$7,13 | US$7,63 | OK |
| P/FCFE | Conservador | US$8,13 | US$7,11 | US$6,43 | US$7,22 | OK |
| P/FCFE | Optimista | US$7,22 | US$6,83 | US$6,93 | US$6,99 | OK |
| P/OCF | Base | US$8,73 | US$8,20 | US$7,89 | US$8,28 | OK |
| P/OCF | Conservador | US$9,08 | US$8,08 | US$7,43 | US$8,20 | OK |
| P/OCF | Optimista | US$8,27 | US$8,09 | US$8,17 | US$8,18 | OK |

Múltiplos consolidados hoy: US$10,72 / US$8,50 / US$12,56 · DCF de las historias hoy: US$12,71 / US$11,84 / US$13,66 · Ponderado hoy: US$11,51 / US$9,84 / US$13,00 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para PAGS la diferencia es de −16% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$11,92 por acción y los múltiplos, US$8,36 hoy: 30% por debajo del DCF, fuera del rango de ±25%. La diferencia viene de P/FCFE: en la proyección Base el crédito de PagBank absorbe caja y el FCFE de FY+3 queda muy por debajo de la utilidad. P/E, el método más confiable para una financiera, queda cerca del DCF.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$9,02 supone que los ingresos crecen — al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 5,8% (—). Ningún crecimiento entre −20% y 80% justifica el precio con estos márgenes.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$18,51 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 13,4%, WACC de los años 4-10 12,8%, ROE de FY+3 17,4% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 2,7x | — | — | — | — | — | No aplica: PagSeguro es una entidad financiera (PagBank): la deuda es materia prima del negocio, no financiación, y el valor empres |
| EV/FCFF | 2,3x | — | — | — | — | — | No aplica: Igual que EV/EBITDA: para una financiera el FCFF no se puede separar de la financiación; peso 0%. |
| P/E | 9,6x | 10,0x | −4% | 6,2% | 6,9% | −0,7 pp | Coherente con el DCF. |
| P/FCFE | 8,3x | 16,1x | −45% | 1,2% | 6,7% | −5,5 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 45% por debajo del DCF en FY+3. |
| P/OCF | 4,4x | 7,5x | −39% | 2,3% | 6,6% | −4,3 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 39% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$11,51 | — |
| Múltiplos Base +20% | US$12,72 | +10,5% |
| Múltiplos Base −20% | US$10,31 | −10,5% |
| Crecimiento años 2-5 +2 pp | US$11,62 | +0,9% |
| Crecimiento años 2-5 −2 pp | US$11,40 | −1,0% |
| Margen objetivo +3 pp | US$11,51 | +0,0% |
| Margen objetivo −3 pp | US$11,51 | +0,0% |
| WACC +1 pp | US$11,27 | −2,1% |
| WACC −1 pp | US$11,78 | +2,3% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, WACC −1 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| PE | J8 | — | 7,39 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 6,16 | 9,55 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 11,44 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 5,98 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 2,50 | 8,34 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 10,28 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 3,75 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 1,75 | 4,36 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 5,01 | Múltiplo optimista elegido con el protocolo v3 |
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
