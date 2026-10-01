---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de DOMINOS PIZZA INC"
ticker: "DPZ"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1voP-krWxuq4RtJDX4WYP6FEG_rRoqjMjgVXF5vPywSo/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# DOMINOS PIZZA INC (DPZ) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal: DCF esperado de las cuatro historias, US$307,85.** Historia central A: US$351,28; rango US$107,72–US$420,06; precio con MOS 35% sobre el esperado: US$200,10; precio de referencia US$299,23. Cada historia es un DCF completo (hoja «Escenarios e historias»); el detalle está en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son la calibración técnica anterior de la hoja (Base US$348,94) y los múltiplos y el ponderado son lecturas secundarias.


| Historia | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| A · Crece por tiendas con ventas mismas tiendas bajas | 50% | US$351,28 | US$175,64 |
| B · Los agregadores erosionan la ventaja | 25% | US$171,26 | US$42,81 |
| C · Tesis de disrupción · Deterioro de los fundamentales: El sistema de franquicias se debilita | 5% | US$107,72 | US$5,39 |
| D · Agregadores e internacional aceleran | 20% | US$420,06 | US$84,01 |
| **DCF esperado** | 100% | **US$307,85** | |

Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$349,85 por acción y los múltiplos, US$408,88 hoy: 17% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

| Escenario | DCF técnico anterior hoy (calibración) | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$249,73 | US$343,81 | US$306,17 | US$200,10 | US$384,67 |
| Base | US$348,94 | US$408,57 | US$384,72 | US$200,10 | US$500,76 |
| Optimista | US$459,80 | US$509,14 | US$489,40 | US$200,10 | US$653,10 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - DPZ](https://docs.google.com/spreadsheets/d/1voP-krWxuq4RtJDX4WYP6FEG_rRoqjMjgVXF5vPywSo/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$299,23.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 2,0% | 4,0% | 6,5% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 2,0% | 4,5% | 6,5% | Input B29 |
| Margen EBIT objetivo | 18,0% | 20,0% | 22,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 3,00 / 3,00 | — | Input B32/B33 |
| DCF por acción hoy | US$249,73 | US$348,94 | US$459,80 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 0,90, ERP 4,46%, Ke 9,00%, costo de la deuda después de impuestos 4,70%, peso del patrimonio 68,7%, WACC inicial 7,66% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Domino's es un franquiciador maduro desde hace una década con múltiplos estables (EV/EBITDA 18-30x); no hubo cambio de etapa del negocio, así que A usa los últimos cinco cierres y el LTM. B: franquiciadores y cadenas de restaurantes (Yum!, McDonald's, Restaurant Brands, Wingstop, Darden), datos de yfinance al 29-sep-2026. Se excluye Papa John's (ingresos −9%, reestructuración). Ajuste 0%: modelo de franquicia asset-light y crecimiento similares a Yum! y Restaurant Brands. λ = 0 (30-sep-2026): el justificado C supone que el ROE de FY+3 se mantiene para siempre, mientras que el DCF revisado limita el ROIC después del año 10 al 18,4% (el menor entre el actual y el de la industria). Para que los múltiplos sean coherentes con el DCF, C se deja fuera del Base y se conserva como referencia en la tabla.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana de los últimos 5 cierres + LTM depurados = 20,5x | 14,7x (n=5: YUM 16,4x, MCD 14,7x, QSR 14,0x, WING 16,7x, DRI 14,3x) × 1,00 = 14,7x | 17,2x / 20,9x / 25,4x | 16,2x | **17,6x** | 20,0x | 17,0x / 18,4x / 21,0x |
| EV/FCFF | mediana de los últimos 5 cierres + LTM depurados = 31,6x (EV/FCF × 0,81 = FCF después de intereses ÷ FCFF) | 24,2x (n=5: YUM 24,2x, MCD 24,2x, QSR 20,2x, WING 24,7x, DRI 28,2x) × 1,00 = 24,2x | 25,4x / 30,9x / 37,4x | 25,9x | **27,9x** | 31,4x | 30,6x / 33,0x / 37,6x |
| P/E | mediana de los últimos 5 cierres + LTM depurados = 26,7x | 19,0x (n=5: YUM 17,3x, MCD 19,0x, QSR 18,0x, WING 25,7x, DRI 19,2x) × 1,00 = 19,0x | — / — / — | 22,2x | **22,9x** | 25,1x | 22,2x / 22,9x / 25,1x |
| P/FCFE | mediana de los últimos 5 cierres + LTM depurados = 29,1x | 21,3x (n=5: YUM 22,4x, MCD 21,3x, QSR 20,1x, WING 23,0x, DRI 20,4x) × 1,00 = 21,3x | 21,4x / 25,2x / 29,4x | 23,3x | **25,2x** | 28,2x | 23,3x / 25,2x / 28,2x |
| P/OCF | mediana de los últimos 5 cierres + LTM depurados = 23,9x | 15,6x (n=5: YUM 18,0x, MCD 14,6x, QSR 17,2x, WING 15,6x, DRI 12,0x) × 1,00 = 15,6x | 20,6x / 28,5x / 36,6x | 17,3x | **19,8x** | 22,8x | 19,2x / 21,9x / 25,4x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 17,6x: promedio de historia y peers 17,6x, acercado 0% al justificado (20,9x); rango de anclas 14,7x–20,9x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 27,9x: promedio de historia y peers 27,9x, acercado 0% al justificado (30,9x); rango de anclas 24,2x–31,6x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 22,9x: promedio de historia y peers 22,9x, acercado 0% al justificado (—x); rango de anclas 19,0x–26,7x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 25,2x: promedio de historia y peers 25,2x, acercado 0% al justificado (25,2x); rango de anclas 21,3x–29,1x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 19,8x: promedio de historia y peers 19,8x, acercado 0% al justificado (28,5x); rango de anclas 15,6x–28,5x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$408,57 frente a US$348,94 del DCF (+17%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$408,57 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$323,44 | US$451,94 | US$595,52 |
| EV/EBITDA | 20% | US$394,04 | US$508,68 | US$681,80 |
| EV/FCFF | 10% | US$434,61 | US$555,44 | US$733,02 |
| P/E | 20% | US$439,20 | US$511,04 | US$626,53 |
| P/FCFE | 5% | US$506,85 | US$710,21 | US$963,01 |
| P/OCF | 5% | US$396,79 | US$499,77 | US$635,56 |
| **Ponderado FY+3** | 100% | US$384,67 | US$500,76 | US$653,10 |

Valor presente (Ke 9,00%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$338,19 | US$318,53 | US$304,24 | US$320,32 | OK |
| EV/EBITDA | Base | US$385,87 | US$392,22 | US$392,75 | US$390,28 | OK |
| EV/EBITDA | Optimista | US$470,27 | US$507,82 | US$526,42 | US$501,50 | OK |
| EV/FCFF | Conservador | US$377,27 | US$353,16 | US$335,56 | US$355,33 | OK |
| EV/FCFF | Base | US$422,62 | US$428,93 | US$428,85 | US$426,80 | OK |
| EV/FCFF | Optimista | US$500,36 | US$544,77 | US$565,97 | US$537,03 | OK |
| P/E | Conservador | US$367,07 | US$350,74 | US$339,10 | US$352,30 | OK |
| P/E | Base | US$385,36 | US$392,03 | US$394,57 | US$390,66 | OK |
| P/E | Optimista | US$432,37 | US$464,90 | US$483,74 | US$460,34 | OK |
| P/FCFE | Conservador | US$425,17 | US$406,03 | US$391,34 | US$407,51 | OK |
| P/FCFE | Base | US$530,18 | US$549,33 | US$548,35 | US$542,62 | OK |
| P/FCFE | Optimista | US$689,34 | US$724,49 | US$743,54 | US$719,12 | OK |
| P/OCF | Conservador | US$328,75 | US$315,91 | US$306,36 | US$317,01 | OK |
| P/OCF | Base | US$378,63 | US$383,98 | US$385,87 | US$382,83 | OK |
| P/OCF | Optimista | US$443,17 | US$473,48 | US$490,71 | US$469,12 | OK |

Múltiplos consolidados hoy: US$343,81 / US$408,57 / US$509,14 · DCF hoy: US$249,73 / US$348,94 / US$459,80 · Ponderado hoy: US$306,17 / US$384,72 / US$489,40 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para DPZ la diferencia es de +17% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$349,85 por acción y los múltiplos, US$408,88 hoy: 17% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco es el DCF esperado de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$299,23 supone que los ingresos crecen 2,4% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 4,4% (−2,0 pp). Coherente: el precio supone un crecimiento parecido al del DCF.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$451,94 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,0%, WACC de los años 4-10 8,2%, ROE de FY+3 — y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 17,6x | 16,0x | +13% | 4,2% | 3,8% | +0,4 pp | Coherente con el DCF. |
| EV/FCFF | 27,9x | 23,5x | +23% | 4,5% | 3,8% | +0,7 pp | Coherente con el DCF. |
| P/E | 22,9x | 20,1x | +13% | — | — | — | Coherente con el DCF. |
| P/FCFE | 25,2x | 15,7x | +57% | 4,8% | 2,5% | +2,4 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 57% por encima del DCF en FY+3. |
| P/OCF | 19,8x | 17,8x | +11% | 3,1% | 2,5% | +0,6 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$384,72 | — |
| Múltiplos Base +20% | US$438,91 | +14,1% |
| Múltiplos Base −20% | US$330,53 | −14,1% |
| Crecimiento años 2-5 +2 pp | US$402,78 | +4,7% |
| Crecimiento años 2-5 −2 pp | US$368,25 | −4,3% |
| Margen objetivo +3 pp | US$412,59 | +7,2% |
| Margen objetivo −3 pp | US$356,85 | −7,2% |
| WACC +1 pp | US$373,88 | −2,8% |
| WACC −1 pp | US$396,34 | +3,0% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 17,00 | 16,22 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 18,41 | 17,57 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 20,99 | 20,03 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 30,63 | 25,88 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 33,02 | 27,89 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 37,65 | 31,40 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 22,17 | 22,17 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 22,85 | 22,85 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 25,09 | 25,09 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 23,30 | 23,30 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 25,23 | 25,23 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 28,17 | 28,17 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 19,24 | 17,32 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 21,94 | 19,76 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 25,37 | 22,84 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/DPZ_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1voP-krWxuq4RtJDX4WYP6FEG_rRoqjMjgVXF5vPywSo/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (YUM, MCD, PZZA, QSR, WING, DRI).

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
