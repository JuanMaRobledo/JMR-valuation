---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de NIKE, Inc."
ticker: "NKE"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1OITWNynG7R3PKC1sITOOazW9jzXgFWFda6qNbbOnYZI/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# NIKE, Inc. (NKE) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$32,98 por acción.** Complemento: DCF esperado por probabilidades US$29,93; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$13,06–US$44,26; precio con MOS 35% sobre el esperado: US$19,45; precio de referencia US$35,15. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$32,93), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Reestructuración que devuelve a Nike a crecer poco con margen de 11%** (valor principal) | 45% | US$32,98 | US$14,84 |
| Conservadora · Recuperación a medias, la marca pierde participación | 25% | US$19,71 | US$4,93 |
| Disrupción · Deterioro de los fundamentales: Nike pierde relevancia como Adidas en 2015-2016, pero sin recuperación | 10% | US$13,06 | US$1,31 |
| Optimista · Vuelve la Nike de márgenes históricos | 20% | US$44,26 | US$8,85 |
| **DCF esperado (complemento)** | 100% | **US$29,93** | |

Lectura del 2-oct-2026: el DCF Base de las historias da ~US$33,0 por acción y los múltiplos consolidados ~US$35,5 hoy, ~8% más. Las dos anclas se compensan: la historia de Nike (15-30 veces) refleja la era de crecimiento y los peers cotizan hoy deprimidos (Lululemon y Deckers a 8-11 veces utilidades). El DCF es el valor intrínseco; los múltiplos son precio relativo y confirman que el precio actual (US$35,15) está cerca del valor de la historia Base.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$32,98 | US$35,51 | US$34,50 | US$19,45 | US$48,59 |
| Conservador | US$19,71 | US$22,09 | US$21,14 | US$19,45 | US$25,22 |
| Optimista | US$44,26 | US$52,84 | US$49,41 | US$19,45 | US$80,29 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - NKE (desde cero 2026-10-02)](https://docs.google.com/spreadsheets/d/1OITWNynG7R3PKC1sITOOazW9jzXgFWFda6qNbbOnYZI/edit).
- Análisis del 01 de oct de 2026. Precio de referencia de la hoja: US$35,15.
- Peers: datos de mercado de yfinance consultados el 2026-10-02 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -8,1% | -6,6% | 4,4% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | -8,1% | 3,4% | 4,4% | Input B29 |
| Margen EBIT objetivo | 7,5% | 11,6% | 16,6% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 6 | 6 | 6 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,10 / 2,10 | — | Input B32/B33 |
| DCF por acción hoy | US$19,71 | US$32,98 | US$44,26 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,24%, beta apalancada 1,01, ERP 4,09%, Ke 9,37%, costo de la deuda después de impuestos 4,51%, peso del patrimonio 85,3%, WACC inicial 8,65% y terminal 9,33%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Nike cotizó a 20-42 veces el EBITDA mientras crecía 6-8% al año y ganaba margen con la venta directa (FY2017-FY2024). Desde FY2025 está en reestructuración: ventas −10% en FY2025, planas en FY2026 y con caída de un dígito alto esperada en FY2027, margen operativo de ~8% frente a 12-16% antes. La etapa actual es May '25, May '26 y el LTM. El reembolso de aranceles IEEPA de FY2026 (US$986 millones) compensa en buena parte los aranceles pagados ese mismo año, así que FY2026 y el LTM se conservan. B: calzado y ropa deportiva con datos de yfinance al 2-oct-2026: Adidas, Deckers, On, Lululemon, Crocs y Birkenstock. Se excluye Under Armour (margen operativo negativo; su P/E no existe y su EV/EBITDA no compara). Ajuste −5%: crecimiento a FY+3 menor que la mediana de los peers (Base ~3-4% frente a 6-13% de Adidas, On y Birkenstock), −10%; margen operativo objetivo menor (11% frente a 14-29%), −5%; riesgo propio menor (la marca más grande, calificación A2/A+, caja de US$8.400 millones), +10%. λ = 0,5: la Nike de FY+3 (crecimiento de un dígito bajo-medio y margen ~10%) es distinta de la de la etapa histórica de alto múltiplo, y los peers cotizan hoy a múltiplos deprimidos (Lululemon y Deckers a 8-11 veces utilidades). El justificado (C) usa los supuestos de cada escenario y equilibra las dos anclas.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana May '25, May '26, LTM (etapa actual) = 15,5x | 9,4x (n=6: ADDYY 12,4x, DECK 7,3x, ONON 19,2x, LULU 4,8x, CROX 7,8x, BIRK 11,0x) × 0,95 = 8,9x | 16,2x / 10,3x / 17,9x | **14,2x** | 11,0x | 16,8x | 15,5x / —x / —x |
| EV/FCFF | mediana May '25, May '26, LTM (etapa actual) = 29,5x (EV/FCF × 1,05 = FCF después de intereses ÷ FCFF) | 13,5x (n=6: ADDYY 17,6x, DECK 8,7x, ONON 21,1x, LULU 8,4x, CROX 9,4x, BIRK 19,5x) × 0,95 = 12,8x | 24,8x / 13,5x / 26,6x | **22,9x** | 16,4x | 27,2x | 22,6x / —x / —x |
| P/E | mediana May '25, May '26, LTM (etapa actual) = 22,0x | 13,6x (n=6: ADDYY 18,5x, DECK 11,3x, ONON 21,3x, LULU 7,9x, CROX 10,4x, BIRK 15,9x) × 0,95 = 12,9x | 17,6x / 11,4x / 20,3x | **17,6x** | 13,5x | 21,1x | 22,0x / —x / —x |
| P/FCFE | mediana May '25, May '26, LTM (etapa actual) = 27,6x | 12,5x (n=6: ADDYY 15,4x, DECK 9,7x, ONON 23,5x, LULU 7,8x, CROX 8,1x, BIRK 18,7x) × 0,95 = 11,9x | 22,5x / 12,8x / 24,0x | **21,1x** | 15,3x | 25,1x | 24,5x / —x / —x |
| P/OCF | mediana May '25, May '26, LTM (etapa actual) = 23,9x | 10,6x (n=6: ADDYY 12,2x, DECK 9,1x, ONON 19,2x, LULU 5,4x, CROX 7,5x, BIRK 13,6x) × 0,95 = 10,1x | 20,5x / 8,2x / 22,6x | **18,7x** | 12,6x | 21,0x | 19,2x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 14,2x: promedio de historia y peers 12,2x, acercado 50% al justificado (16,2x); rango de anclas 8,9x–16,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 22,9x: promedio de historia y peers 21,1x, acercado 50% al justificado (24,8x); rango de anclas 12,8x–29,5x. Atípicos excluidos de la historia: May '20 (114,7x: > 2,5x la mediana (32.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 17,6x: promedio de historia y peers 17,5x, acercado 50% al justificado (17,6x); rango de anclas 12,9x–22,0x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 21,1x: promedio de historia y peers 19,8x, acercado 50% al justificado (22,5x); rango de anclas 11,9x–27,6x. Atípicos excluidos de la historia: May '20 (112,2x: > 2,5x la mediana (31.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 18,7x: promedio de historia y peers 17,0x, acercado 50% al justificado (20,5x); rango de anclas 10,1x–23,9x. Atípicos excluidos de la historia: May '20 (63,1x: > 2,5x la mediana (24.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$35,51 frente a US$32,98 del DCF (+8%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$35,51 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$43,08 | US$21,17 | US$73,76 |
| EV/EBITDA | 20% | US$52,48 | US$28,56 | US$83,54 |
| EV/FCFF | 10% | US$55,18 | US$31,74 | US$90,44 |
| P/E | 20% | US$47,31 | US$24,89 | US$78,63 |
| P/FCFE | 5% | US$59,47 | US$26,00 | US$98,18 |
| P/OCF | 5% | US$58,10 | US$31,65 | US$87,90 |
| **Ponderado FY+3** | 100% | US$48,59 | US$25,22 | US$80,29 |

Valor presente (Ke 9,37%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$30,84 | US$37,51 | US$40,12 | US$36,15 | OK |
| EV/EBITDA | Conservador | US$23,93 | US$23,15 | US$21,83 | US$22,97 | OK |
| EV/EBITDA | Optimista | US$40,15 | US$56,92 | US$63,86 | US$53,64 | OK |
| EV/FCFF | Base | US$36,52 | US$38,85 | US$42,18 | US$39,18 | OK |
| EV/FCFF | Conservador | US$27,02 | US$25,97 | US$24,26 | US$25,75 | OK |
| EV/FCFF | Optimista | US$38,94 | US$60,26 | US$69,13 | US$56,11 | OK |
| P/E | Base | US$24,57 | US$32,30 | US$36,17 | US$31,01 | OK |
| P/E | Conservador | US$19,00 | US$19,35 | US$19,03 | US$19,13 | OK |
| P/E | Optimista | US$32,40 | US$51,01 | US$60,10 | US$47,84 | OK |
| P/FCFE | Base | US$27,83 | US$41,25 | US$45,46 | US$38,18 | OK |
| P/FCFE | Conservador | US$19,82 | US$20,30 | US$19,88 | US$20,00 | OK |
| P/FCFE | Optimista | US$42,75 | US$64,68 | US$75,05 | US$60,82 | OK |
| P/OCF | Base | US$37,58 | US$40,64 | US$44,41 | US$40,88 | OK |
| P/OCF | Conservador | US$26,06 | US$25,42 | US$24,19 | US$25,22 | OK |
| P/OCF | Optimista | US$39,83 | US$58,36 | US$67,19 | US$55,13 | OK |

Múltiplos consolidados hoy: US$35,51 / US$22,09 / US$52,84 · DCF de las historias hoy: US$32,98 / US$19,71 / US$44,26 · Ponderado hoy: US$34,50 / US$21,14 / US$49,41 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para NKE la diferencia es de +8% (múltiplos por encima del DCF). Lectura del 2-oct-2026: el DCF Base de las historias da ~US$33,0 por acción y los múltiplos consolidados ~US$35,5 hoy, ~8% más. Las dos anclas se compensan: la historia de Nike (15-30 veces) refleja la era de crecimiento y los peers cotizan hoy deprimidos (Lululemon y Deckers a 8-11 veces utilidades). El DCF es el valor intrínseco; los múltiplos son precio relativo y confirman que el precio actual (US$35,15) está cerca del valor de la historia Base.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$35,15 supone que los ingresos crecen 2,4% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 1,4% (+1,0 pp). Coherente: el precio supone un crecimiento parecido al del DCF.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$43,08 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,4%, WACC de los años 4-10 8,9%, ROE de FY+3 21,9% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 14,2x | 11,3x | +22% | 4,1% | 3,0% | +1,2 pp | Coherente con el DCF. |
| EV/FCFF | 22,9x | 17,3x | +28% | 4,4% | 3,0% | +1,4 pp | Revisar: el múltiplo vale 28% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 17,6x | 15,8x | +10% | 4,7% | 4,0% | +0,7 pp | Coherente con el DCF. |
| P/FCFE | 21,1x | 14,7x | +38% | 4,4% | 2,4% | +2,0 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 38% por encima del DCF en FY+3. |
| P/OCF | 18,7x | 13,3x | +35% | 4,3% | 2,4% | +1,9 pp | Revisar: el múltiplo vale 35% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$34,50 | — |
| Múltiplos Base +20% | US$38,37 | +11,2% |
| Múltiplos Base −20% | US$30,62 | −11,2% |
| Crecimiento años 2-5 +2 pp | US$35,40 | +2,6% |
| Crecimiento años 2-5 −2 pp | US$33,64 | −2,5% |
| Margen objetivo +3 pp | US$38,17 | +10,6% |
| Margen objetivo −3 pp | US$30,78 | −10,8% |
| WACC +1 pp | US$33,70 | −2,3% |
| WACC −1 pp | US$35,30 | +2,3% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo −3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 11,01 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 15,51 | 14,23 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 16,83 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 16,43 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 22,64 | 22,95 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 27,23 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 13,51 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 22,03 | 17,55 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 21,06 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 15,34 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 24,48 | 21,12 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 25,07 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 12,64 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 19,23 | 18,73 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 20,99 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/NKE_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1OITWNynG7R3PKC1sITOOazW9jzXgFWFda6qNbbOnYZI/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-10-02 (ADDYY, DECK, ONON, LULU, CROX, BIRK, UAA).
- [NIKE, comunicado del 1T FY2027, 1-oct-2026](https://www.sec.gov/Archives/edgar/data/0000320187/000032018726000184/q1fy27exhibit991er.htm)
- [NIKE, 10-K FY2026, 15-jul-2026](https://www.sec.gov/Archives/edgar/data/320187/000032018726000088/nke-20260531.htm)

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
