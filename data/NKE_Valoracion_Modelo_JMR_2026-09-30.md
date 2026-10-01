---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de NIKE, Inc."
ticker: "NKE"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1BAuhp8QPzXQx1osCIBHA4QoFC91DStgSr3h4SjFkAL4/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# NIKE, Inc. (NKE) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$38,40 por acción.** Complemento: DCF esperado por probabilidades US$35,18; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$16,63–US$50,33; precio con MOS 35% sobre el esperado: US$22,87; precio de referencia US$35,35. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$37,41), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Recuperación lenta con la vuelta a los mayoristas** (valor principal) | 45% | US$38,40 | US$17,28 |
| Conservadora · Pérdida de relevancia prolongada | 30% | US$23,36 | US$7,01 |
| Disrupción · Deterioro de los fundamentales: Aranceles y competencia estructural | 5% | US$16,63 | US$0,83 |
| Optimista · Vuelve la Nike de márgenes históricos | 20% | US$50,33 | US$10,07 |
| **DCF esperado (complemento)** | 100% | **US$35,18** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$33,96 por acción y los múltiplos, US$34,03 hoy: prácticamente igual al DCF. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$38,40 | US$32,16 | US$34,65 | US$22,87 | US$47,68 |
| Conservador | US$23,36 | US$24,46 | US$24,02 | US$22,87 | US$31,73 |
| Optimista | US$50,33 | US$40,27 | US$44,29 | US$22,87 | US$63,41 |

## 2. Datos

- Hoja del modelo: [Modelo_JMR_Plantilla_Maestra NKE (automático)](https://docs.google.com/spreadsheets/d/1BAuhp8QPzXQx1osCIBHA4QoFC91DStgSr3h4SjFkAL4/edit).
- Análisis del 22 de sept de 2026. Precio de referencia de la hoja: US$35,35.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -3,0% | -2,0% | 4,5% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | -3,0% | 3,5% | 4,5% | Input B29 |
| Margen EBIT objetivo | 7,1% | 11,6% | 14,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,86 / 1,86 | — | Input B32/B33 |
| DCF por acción hoy | US$23,36 | US$38,40 | US$50,33 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,96%, beta apalancada 1,01, ERP 4,32%, Ke 9,32%, costo de la deuda después de impuestos 4,30%, peso del patrimonio 85,2%, WACC inicial 8,58% y terminal 9,05%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Nike cotizó a 20-42x EBITDA mientras crecía y ganaba margen con la venta directa. Desde FY25 está en reestructuración: las ventas cayeron ~10% en FY25 y quedaron planas en FY26 (US$46.400 millones, −2% sin efecto cambiario), China cae 12% y el CEO Elliott Hill reconoce que la recuperación toma más de lo esperado. La etapa actual es May '25, May '26 y el LTM. B: ropa y calzado deportivo (Adidas, Lululemon, Deckers, On Holding), datos de yfinance al 29-sep-2026. Se excluyen Under Armour y VF Corp (margen operativo negativo; sus múltiplos no comparan). Sin ajuste: Nike es la marca más grande del sector, pero hoy no crece; queda entre On/Adidas (crecen) y Lululemon (decrece). λ = 0 (30-sep-2026): el justificado C supone que el ROE de FY+3 se mantiene para siempre, mientras que el DCF revisado limita el ROIC después del año 10 al 13,3% (el menor entre el actual y el de la industria). Para que los múltiplos sean coherentes con el DCF, C se deja fuera del Base y se conserva como referencia en la tabla.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana May '25, May '26, LTM (etapa actual) = 15,5x | 9,9x (n=4: ADDYY 12,7x, LULU 5,0x, DECK 7,1x, ONON 19,1x) × 1,00 = 8,7x | 16,4x / 11,9x / 17,7x | **12,1x** | 9,2x | 14,8x | 15,5x / —x / —x |
| EV/FCFF | mediana May '25, May '26, LTM (etapa actual) = 29,9x (EV/FCF × 1,07 = FCF después de intereses ÷ FCFF) | 13,4x (n=4: ADDYY 18,0x, LULU 8,8x, DECK 8,4x, ONON 20,9x) × 1,00 = 11,7x | 24,6x / 16,8x / 26,4x | **20,8x** | 15,9x | 24,6x | 22,6x / —x / —x |
| P/E | mediana May '25, May '26, LTM (etapa actual) = 22,0x | 14,8x (n=4: ADDYY 18,6x, LULU 8,0x, DECK 11,0x, ONON 20,8x) × 1,00 = 12,2x | 17,8x / 12,9x / 19,6x | **17,1x** | 13,2x | 20,1x | 22,0x / —x / —x |
| P/FCFE | mediana May '25, May '26, LTM (etapa actual) = 27,6x | 12,6x (n=4: ADDYY 15,8x, LULU 7,9x, DECK 9,5x, ONON 23,0x) × 1,00 = 11,6x | 22,1x / 15,6x / 23,6x | **19,6x** | 15,5x | 23,1x | 17,9x / 10,1x / 19,5x |
| P/OCF | mediana May '25, May '26, LTM (etapa actual) = 23,9x | 10,7x (n=4: ADDYY 12,5x, LULU 5,4x, DECK 8,9x, ONON 18,8x) × 1,00 = 9,3x | 20,7x / 11,2x / 22,8x | **16,6x** | 12,0x | 18,9x | 19,2x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 12,1x: promedio de historia y peers 12,1x, acercado 0% al justificado (16,4x); rango de anclas 8,7x–16,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 20,8x: promedio de historia y peers 20,8x, acercado 0% al justificado (24,6x); rango de anclas 11,7x–29,9x. Atípicos excluidos de la historia: May '20 (114,7x: > 2,5x la mediana (32.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 17,1x: promedio de historia y peers 17,1x, acercado 0% al justificado (17,8x); rango de anclas 12,2x–22,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 19,6x: promedio de historia y peers 19,6x, acercado 0% al justificado (22,1x); rango de anclas 11,6x–27,6x. Atípicos excluidos de la historia: May '20 (112,2x: > 2,5x la mediana (31.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 16,6x: promedio de historia y peers 16,6x, acercado 0% al justificado (20,7x); rango de anclas 9,3x–23,9x. Atípicos excluidos de la historia: May '20 (63,1x: > 2,5x la mediana (24.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$32,16 frente a US$38,40 del DCF (−16%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$31,98 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$50,17 | US$30,52 | US$65,76 |
| EV/EBITDA | 20% | US$48,40 | US$32,49 | US$67,05 |
| EV/FCFF | 10% | US$38,28 | US$31,32 | US$49,45 |
| P/E | 20% | US$49,10 | US$32,93 | US$66,17 |
| P/FCFE | 5% | US$44,19 | US$34,33 | US$58,99 |
| P/OCF | 5% | US$41,54 | US$31,79 | US$51,43 |
| **Ponderado FY+3** | 100% | US$47,68 | US$31,73 | US$63,41 |

Valor presente (Ke 9,32%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$30,75 | US$35,22 | US$37,45 | US$34,47 | OK |
| EV/EBITDA | Conservador | US$23,22 | US$24,46 | US$25,28 | US$24,32 | OK |
| EV/EBITDA | Optimista | US$38,29 | US$47,18 | US$51,72 | US$45,73 | OK |
| EV/FCFF | Base | US$21,90 | US$26,31 | US$29,71 | US$25,97 | OK |
| EV/FCFF | Conservador | US$25,16 | US$23,22 | US$24,37 | US$24,25 | OK |
| EV/FCFF | Optimista | US$18,80 | US$28,47 | US$38,25 | US$28,51 | OK |
| P/E | Base | US$30,24 | US$35,39 | US$37,99 | US$34,54 | OK |
| P/E | Conservador | US$23,22 | US$24,67 | US$25,61 | US$24,50 | OK |
| P/E | Optimista | US$36,02 | US$45,94 | US$51,05 | US$44,33 | OK |
| P/FCFE | Base | US$21,55 | US$30,57 | US$34,23 | US$28,78 | OK |
| P/FCFE | Conservador | US$23,91 | US$24,63 | US$26,68 | US$25,07 | OK |
| P/FCFE | Optimista | US$20,92 | US$35,69 | US$45,55 | US$34,05 | OK |
| P/OCF | Base | US$25,77 | US$29,42 | US$32,20 | US$29,13 | OK |
| P/OCF | Conservador | US$25,31 | US$23,81 | US$24,74 | US$24,62 | OK |
| P/OCF | Optimista | US$24,06 | US$31,94 | US$39,77 | US$31,92 | OK |

Múltiplos consolidados hoy: US$32,16 / US$24,46 / US$40,27 · DCF de las historias hoy: US$38,40 / US$23,36 / US$50,33 · Ponderado hoy: US$34,65 / US$24,02 / US$44,29 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NKE la diferencia es de −16% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$33,96 por acción y los múltiplos, US$34,03 hoy: prácticamente igual al DCF. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$35,35 supone que los ingresos crecen 0,6% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 2,4% (−1,8 pp). Coherente: el precio supone un crecimiento parecido al del DCF.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$50,17 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,3%, WACC de los años 4-10 8,8%, ROE de FY+3 23,0% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 12,1x | 12,0x | −4% | 3,1% | 3,1% | +0,0 pp | Coherente con el DCF. |
| EV/FCFF | 20,8x | 27,1x | −24% | 3,8% | 4,9% | −1,1 pp | Coherente con el DCF. |
| P/E | 17,1x | 17,5x | −2% | 4,3% | 4,5% | −0,2 pp | Coherente con el DCF. |
| P/FCFE | 19,6x | 22,7x | −12% | 4,0% | 4,6% | −0,7 pp | Coherente con el DCF. |
| P/OCF | 16,6x | 20,6x | −17% | 3,4% | 4,5% | −1,1 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$34,65 | — |
| Múltiplos Base +20% | US$38,05 | +9,8% |
| Múltiplos Base −20% | US$31,04 | −10,4% |
| Crecimiento años 2-5 +2 pp | US$35,20 | +1,6% |
| Crecimiento años 2-5 −2 pp | US$33,40 | −3,6% |
| Margen objetivo +3 pp | US$38,24 | +10,3% |
| Margen objetivo −3 pp | US$30,28 | −12,6% |
| WACC +1 pp | US$33,41 | −3,6% |
| WACC −1 pp | US$35,17 | +1,5% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo −3 pp, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 9,22 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 15,51 | 12,10 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 14,85 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 15,88 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 22,64 | 20,82 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 24,64 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 13,15 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 22,03 | 17,09 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 20,12 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 10,14 | 15,47 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 17,93 | 19,60 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 19,46 | 23,06 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 12,04 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 19,23 | 16,58 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 18,95 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/NKE_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1BAuhp8QPzXQx1osCIBHA4QoFC91DStgSr3h4SjFkAL4/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (ADDYY, LULU, DECK, ONON, UAA, VFC).
- [Nike: resultados FY26](https://about.nike.com/en/newsroom/releases/nike-inc-reports-fiscal-2026-fourth-quarter-and-full-year-results)
- [CNBC, 30-jun-2026: Nike supera estimados pero China cae 12%](https://www.cnbc.com/2026/06/30/nike-nke-q4-2026-earnings.html)

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
