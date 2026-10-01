---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Microsoft Corporation"
ticker: "MSFT"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1ubjlRP0jbGmG_sXEoTrvonRkwqy5AoOd1ESrU4c3-rY/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Microsoft Corporation (MSFT) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal: DCF esperado de las cuatro historias, US$395,33.** Historia central A: US$446,95; rango US$192,69–US$585,53; precio con MOS 35% sobre el esperado: US$256,96; precio de referencia US$518,46. Cada historia es un DCF completo (hoja «Escenarios e historias»); el detalle está en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son la calibración técnica anterior de la hoja (Base US$455,44) y los múltiplos y el ponderado son lecturas secundarias.


| Historia | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| A · Azure y Copilot sostienen el doble dígito | 45% | US$446,95 | US$201,13 |
| B · El capex de IA rinde menos de lo esperado | 25% | US$231,30 | US$57,82 |
| C · Tesis de disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige | 10% | US$192,69 | US$19,27 |
| D · Microsoft gana la plataforma empresarial de IA | 20% | US$585,53 | US$117,11 |
| **DCF esperado** | 100% | **US$395,33** | |

Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$466,38 por acción y los múltiplos, US$466,16 hoy: prácticamente igual al DCF. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

| Escenario | DCF técnico anterior hoy (calibración) | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$353,32 | US$342,49 | US$348,99 | US$256,96 | US$464,40 |
| Base | US$455,44 | US$467,23 | US$460,16 | US$256,96 | US$624,00 |
| Optimista | US$541,12 | US$611,04 | US$569,09 | US$256,96 | US$780,40 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - Valoración MSFT - 2026-09-16](https://docs.google.com/spreadsheets/d/1ubjlRP0jbGmG_sXEoTrvonRkwqy5AoOd1ESrU4c3-rY/edit).
- Análisis del 16 de sept de 2026. Precio de referencia de la hoja: US$518,46.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 14,0% | 16,5% | 19,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 8,0% | 12,0% | 14,0% | Input B29 |
| Margen EBIT objetivo | 42,0% | 45,0% | 48,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 7 | 7 | 7 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 0,65 / 1,00 | — | Input B32/B33 |
| DCF por acción hoy | US$353,32 | US$455,44 | US$541,12 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,25%, beta apalancada 1,35, ERP 4,46%, Ke 10,29%, costo de la deuda después de impuestos 4,15%, peso del patrimonio 97,8%, WACC inicial 10,16% y terminal 8,48%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Sin cambio de etapa: Microsoft sigue creciendo a doble dígito y cotiza por debajo de su promedio de cinco años; se usa la mediana de los últimos 5 cierres + LTM. Se excluye la columna sin fecha de la hoja. B: grandes plataformas tecnológicas y de software (Alphabet, Apple, Amazon, Oracle, Meta, Salesforce), datos de yfinance al 29-sep-2026. Amazon y Oracle no tienen flujo de caja libre positivo y no entran en los múltiplos de flujo. Ajuste +5%: Microsoft tiene el margen operativo más alto del grupo (45% frente a ~33%) y Azure acelera (~40%) con una cartera de US$678 mil millones. λ = 0 (30-sep-2026): el justificado C supone que el ROE de FY+3 se mantiene para siempre, mientras que el DCF revisado limita el ROIC después del año 10 al 25,9% (el menor entre el actual y el de la industria). Para que los múltiplos sean coherentes con el DCF, C se deja fuera del Base y se conserva como referencia en la tabla.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana de los últimos 5 cierres + LTM depurados = 22,1x | 17,1x (n=6: GOOG 23,2x, AAPL 28,8x, AMZN 16,5x, ORCL 15,6x, META 17,4x, CRM 16,9x) × 1,05 = 18,0x | 9,4x / 13,1x / 16,9x | 17,2x | **20,0x** | 24,6x | —x / —x / —x |
| EV/FCFF | mediana de los últimos 5 cierres + LTM depurados = 42,8x (EV/FCF × 0,98 = FCF después de intereses ÷ FCFF) | 40,0x (n=4: GOOG 73,1x, AAPL 35,3x, META 44,7x, CRM 13,8x) × 1,05 = 42,0x | 25,5x / 35,7x / 44,4x | 31,2x | **42,4x** | 50,6x | —x / —x / —x |
| P/E | mediana de los últimos 5 cierres + LTM depurados = 31,8x | 21,1x (n=6: GOOG 16,9x, AAPL 37,7x, AMZN 19,8x, ORCL 21,6x, META 27,8x, CRM 20,6x) × 1,05 = 22,2x | 18,2x / 23,7x / 28,2x | 23,0x | **27,0x** | 31,9x | —x / —x / —x |
| P/FCFE | mediana de los últimos 5 cierres + LTM depurados = 44,2x | 40,5x (n=4: GOOG 77,4x, AAPL 35,2x, META 45,9x, CRM 12,2x) × 1,05 = 42,6x | 21,4x / 28,2x / 33,5x | 32,6x | **43,4x** | 51,3x | —x / —x / —x |
| P/OCF | mediana de los últimos 5 cierres + LTM depurados = 24,3x | 16,2x (n=6: GOOG 22,2x, AAPL 32,8x, AMZN 17,9x, ORCL 8,9x, META 14,4x, CRM 11,8x) × 1,05 = 17,0x | 10,0x / 13,7x / 17,0x | 16,1x | **20,7x** | 25,2x | —x / —x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 20,0x: promedio de historia y peers 20,0x, acercado 0% al justificado (13,1x); rango de anclas 13,1x–22,1x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 42,4x: promedio de historia y peers 42,4x, acercado 0% al justificado (35,7x); rango de anclas 35,7x–42,8x. Atípicos excluidos de la historia: ninguno. EV/FCFF: la razón FCF después de intereses ÷ FCFF se fija en 0,98 (mediana de los tres cierres reales); el último cierre da 1,28 porque 'Interest / Other' incluye partidas no operativas. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 27,0x: promedio de historia y peers 27,0x, acercado 0% al justificado (23,7x); rango de anclas 22,2x–31,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 43,4x: promedio de historia y peers 43,4x, acercado 0% al justificado (28,2x); rango de anclas 28,2x–44,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 20,7x: promedio de historia y peers 20,7x, acercado 0% al justificado (13,7x); rango de anclas 13,7x–24,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$467,23 frente a US$455,44 del DCF (+3%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$467,23 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$474,02 | US$611,03 | US$725,97 |
| EV/EBITDA | 10% | US$548,49 | US$726,33 | US$975,03 |
| EV/FCFF | 15% | US$372,13 | US$567,59 | US$767,38 |
| P/E | 5% | US$496,04 | US$663,87 | US$862,06 |
| P/FCFE | 5% | US$446,55 | US$700,51 | US$948,47 |
| P/OCF | 5% | US$443,75 | US$627,94 | US$833,62 |
| **Ponderado FY+3** | 100% | US$464,40 | US$624,00 | US$780,40 |

Valor presente (Ke 10,29%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$422,27 | US$415,18 | US$408,83 | US$415,42 | OK |
| EV/EBITDA | Base | US$515,17 | US$529,00 | US$541,39 | US$528,52 | OK |
| EV/EBITDA | Optimista | US$660,63 | US$695,66 | US$726,76 | US$694,35 | OK |
| EV/FCFF | Conservador | US$288,62 | US$280,49 | US$277,38 | US$282,16 | OK |
| EV/FCFF | Base | US$391,17 | US$410,38 | US$423,07 | US$408,21 | OK |
| EV/FCFF | Optimista | US$498,35 | US$541,28 | US$571,99 | US$537,20 | OK |
| P/E | Conservador | US$389,67 | US$377,86 | US$369,73 | US$379,09 | OK |
| P/E | Base | US$479,23 | US$486,20 | US$494,83 | US$486,75 | OK |
| P/E | Optimista | US$592,63 | US$617,81 | US$642,55 | US$617,66 | OK |
| P/FCFE | Conservador | US$373,84 | US$337,09 | US$332,84 | US$347,92 | OK |
| P/FCFE | Base | US$512,89 | US$507,73 | US$522,14 | US$514,25 | OK |
| P/FCFE | Optimista | US$657,64 | US$671,50 | US$706,96 | US$678,70 | OK |
| P/OCF | Conservador | US$341,22 | US$334,72 | US$330,76 | US$335,57 | OK |
| P/OCF | Base | US$441,25 | US$456,28 | US$468,05 | US$455,19 | OK |
| P/OCF | Optimista | US$559,90 | US$593,56 | US$621,36 | US$591,61 | OK |

Múltiplos consolidados hoy: US$342,49 / US$467,23 / US$611,04 · DCF hoy: US$353,32 / US$455,44 / US$541,12 · Ponderado hoy: US$348,99 / US$460,16 / US$569,09 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para MSFT la diferencia es de +3% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$466,38 por acción y los múltiplos, US$466,16 hoy: prácticamente igual al DCF. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$518,46 supone que los ingresos crecen 15,4% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 12,9% (+2,5 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$611,03 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,2%, WACC de los años 4-10 9,4%, ROE de FY+3 40,6% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 20,0x | 16,8x | +19% | 7,5% | 7,1% | +0,4 pp | Coherente con el DCF. |
| EV/FCFF | 42,4x | 45,7x | −7% | 6,9% | 7,1% | −0,2 pp | Coherente con el DCF. |
| P/E | 27,0x | 24,8x | +9% | 6,9% | 6,6% | +0,3 pp | Coherente con el DCF. |
| P/FCFE | 43,4x | 37,7x | +15% | 7,8% | 7,4% | +0,4 pp | Coherente con el DCF. |
| P/OCF | 20,7x | 20,1x | +3% | 7,7% | 7,6% | +0,1 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$460,16 | — |
| Múltiplos Base +20% | US$497,06 | +8,0% |
| Múltiplos Base −20% | US$423,26 | −8,0% |
| Crecimiento años 2-5 +2 pp | US$483,49 | +5,1% |
| Crecimiento años 2-5 −2 pp | US$438,84 | −4,6% |
| Margen objetivo +3 pp | US$478,52 | +4,0% |
| Margen objetivo −3 pp | US$441,80 | −4,0% |
| WACC +1 pp | US$444,41 | −3,4% |
| WACC −1 pp | US$477,04 | +3,7% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 17,18 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | — | 20,04 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 24,64 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 31,25 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | — | 42,41 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 50,65 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 23,01 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | — | 26,96 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 31,86 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 32,62 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | — | 43,39 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 51,33 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 16,15 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | — | 20,67 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 25,22 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/MSFT_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1ubjlRP0jbGmG_sXEoTrvonRkwqy5AoOd1ESrU4c3-rY/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (GOOG, AAPL, AMZN, ORCL, META, CRM).
- [CNBC, 29-jul-2026: resultados 4T FY26 de Microsoft](https://www.cnbc.com/2026/07/29/microsoft-msft-q4-earnings-report-2026.html)
- [CNBC, 29-abr-2026: Microsoft proyecta US$190 mil millones de capex](https://www.cnbc.com/2026/04/29/microsoft-msft-q3-earnings-report-2026.html)

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
