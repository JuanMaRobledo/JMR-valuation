---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de ADOBE INC."
ticker: "ADBE"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/19WcSOKymo4gR6lnKiLB1gAitYFFwfI3xl08E4BDzLDw/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# ADOBE INC. (ADBE) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$536,48 en el escenario Base (rango US$408,85–US$823,06). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$486,87 (−9% frente al DCF). Con los pesos de la categoría «Madura» (40% DCF, 60% múltiplos), el ponderado hoy (lectura secundaria) es US$506,71. El valor intrínseco es el DCF: US$536,48 frente a un precio de referencia de US$240,24 (+123%).

Lectura del 30-sep-2026: el DCF (valor intrínseco) da US$536,48 por acción y los múltiplos, US$486,87 hoy: 9% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el DCF manda y los múltiplos son precio relativo.

| Escenario | DCF hoy (valor intrínseco) | Múltiplos consolidados hoy (secundario) | Ponderado hoy (secundario) | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$408,85 | US$318,83 | US$354,84 | US$239,07 | US$475,99 |
| Base | US$536,48 | US$486,87 | US$506,71 | US$239,07 | US$698,88 |
| Optimista | US$823,06 | US$812,69 | US$816,83 | US$239,07 | US$1.197,71 |

## 2. Datos

- Hoja del modelo: [Modelo_JMR_Plantilla_Maestra ADBE](https://docs.google.com/spreadsheets/d/19WcSOKymo4gR6lnKiLB1gAitYFFwfI3xl08E4BDzLDw/edit).
- Revisión de datos y modelo: 28 de septiembre de 2026 (precio del análisis: 14 de septiembre de 2026). Precio de referencia de la hoja: US$240,24.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 6,0% | 12,0% | 16,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 6,0% | 10,0% | 16,0% | Input B29 |
| Margen EBIT objetivo | 38,7% | 40,0% | 45,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 3 | 3 | 3 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 4,00 / 4,50 | — | Input B32/B33 |
| DCF por acción hoy | US$408,85 | US$536,48 | US$823,06 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,39, ERP 4,46%, Ke 11,20%, costo de la deuda después de impuestos 4,32%, peso del patrimonio 94,2%, WACC inicial 10,80% y terminal 9,22%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Adobe pasó de crecer 15-25% anual (FY16-FY21) a ~10-11% (FY23-FY25: +10,2%, +10,8%, +10,5%), y el mercado re-valoró el software de aplicaciones por el riesgo de la IA generativa; los múltiplos de 40-60x de la etapa anterior no describen a la empresa de FY+3, así que A usa solo los cierres FY23-FY25 y el LTM. B: peers de software de aplicaciones con datos de yfinance al 29-sep-2026 (ADSK, INTU, CRM, WDAY, PTC); se excluye ServiceNow (NOW) porque crece 24% con margen operativo GAAP de 4%, lo que infla sus múltiplos (P/E 81x). No se usa MSFT (megacap diversificada). Ajuste +5%: margen operativo de Adobe 35-39% frente a ~21% de mediana de los peers y conversión de caja superior (+10%), compensado en parte por un crecimiento algo menor (10-12% vs ~13% de mediana, -5%). λ = 0,25: la Adobe de FY+3 del escenario Base (crecimiento ~10%, margen 40%) es parecida a la de hoy, así que el Base se acerca solo un 25% al múltiplo justificado.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 21,8x | 16,9x (n=5: ADSK 18,4x, INTU 10,7x, CRM 16,9x, WDAY 28,9x, PTC 12,9x) × 1,05 = 17,8x | 14,8x / 19,0x / 35,0x | 13,9x | **19,6x** | 28,5x | 13,9x / 19,6x / 28,6x |
| EV/FCFF | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 21,1x | 15,0x (n=5: ADSK 15,0x, INTU 8,3x, CRM 13,8x, WDAY 15,6x, PTC 16,6x) × 1,05 = 15,7x | 21,7x / 28,8x / 54,4x | 15,9x | **21,0x** | 31,0x | 16,1x / 21,1x / 31,2x |
| P/E | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 30,5x | 20,6x (n=5: ADSK 26,3x, INTU 16,3x, CRM 20,6x, WDAY 38,8x, PTC 13,3x) × 1,05 = 21,6x | 16,6x / 20,8x / 33,0x | 17,9x | **24,7x** | 35,6x | 17,9x / 24,7x / 35,6x |
| P/FCFE | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 21,2x | 15,1x (n=5: ADSK 15,1x, INTU 8,3x, CRM 12,2x, WDAY 16,0x, PTC 16,0x) × 1,05 = 15,9x | 17,8x / 22,3x / 35,3x | 14,2x | **19,5x** | 26,8x | 14,2x / 19,5x / 26,8x |
| P/OCF | mediana Dec '23, Nov '24, Nov '25, LTM (etapa actual) = 20,7x | 14,7x (n=5: ADSK 14,7x, INTU 8,1x, CRM 11,8x, WDAY 14,8x, PTC 15,6x) × 1,05 = 15,4x | 17,1x / 21,4x / 34,0x | 13,8x | **18,9x** | 25,7x | 13,8x / 18,9x / 25,7x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 19,6x: promedio de historia y peers 19,8x, acercado 25% al justificado (19,0x); rango de anclas 17,8x–21,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 21,0x: promedio de historia y peers 18,4x, acercado 25% al justificado (28,8x); rango de anclas 15,7x–28,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 24,7x: promedio de historia y peers 26,1x, acercado 25% al justificado (20,8x); rango de anclas 20,8x–30,5x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 19,5x: promedio de historia y peers 18,5x, acercado 25% al justificado (22,3x); rango de anclas 15,9x–22,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 18,9x: promedio de historia y peers 18,1x, acercado 25% al justificado (21,4x); rango de anclas 15,4x–21,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$486,87 frente a US$536,48 del DCF (−9%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$486,87 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$562,22 | US$737,73 | US$1.131,80 |
| EV/EBITDA | 20% | US$466,38 | US$771,14 | US$1.444,35 |
| EV/FCFF | 10% | US$361,68 | US$545,79 | US$1.007,95 |
| P/E | 20% | US$441,28 | US$714,63 | US$1.331,88 |
| P/FCFE | 5% | US$332,83 | US$518,35 | US$892,84 |
| P/OCF | 5% | US$335,16 | US$522,86 | US$886,10 |
| **Ponderado FY+3** | 100% | US$475,99 | US$698,88 | US$1.197,71 |

Valor presente (Ke 11,20%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$372,91 | US$355,51 | US$339,16 | US$355,86 | OK |
| EV/EBITDA | Base | US$556,01 | US$560,99 | US$560,78 | US$559,26 | OK |
| EV/EBITDA | Optimista | US$840,26 | US$963,01 | US$1.050,34 | US$951,21 | OK |
| EV/FCFF | Conservador | US$287,27 | US$275,19 | US$263,02 | US$275,16 | OK |
| EV/FCFF | Base | US$388,56 | US$395,55 | US$396,90 | US$393,67 | OK |
| EV/FCFF | Optimista | US$562,90 | US$664,09 | US$732,99 | US$653,33 | OK |
| P/E | Conservador | US$350,97 | US$335,95 | US$320,91 | US$335,94 | OK |
| P/E | Base | US$511,19 | US$518,80 | US$519,69 | US$516,56 | OK |
| P/E | Optimista | US$761,52 | US$883,79 | US$968,56 | US$871,29 | OK |
| P/FCFE | Conservador | US$264,63 | US$253,36 | US$242,04 | US$253,34 | OK |
| P/FCFE | Base | US$369,56 | US$375,90 | US$376,95 | US$374,14 | OK |
| P/FCFE | Optimista | US$499,71 | US$588,71 | US$649,28 | US$579,23 | OK |
| P/OCF | Conservador | US$266,54 | US$255,15 | US$243,73 | US$255,14 | OK |
| P/OCF | Base | US$373,37 | US$379,37 | US$380,23 | US$377,66 | OK |
| P/OCF | Optimista | US$499,29 | US$585,43 | US$644,38 | US$576,36 | OK |

Múltiplos consolidados hoy: US$318,83 / US$486,87 / US$812,69 · DCF hoy: US$408,85 / US$536,48 / US$823,06 · Ponderado hoy: US$354,84 / US$506,71 / US$816,83 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para ADBE la diferencia es de −9% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF (valor intrínseco) da US$536,48 por acción y los múltiplos, US$486,87 hoy: 9% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el DCF manda y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$239,66 supone que los ingresos crecen -4,0% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 10,4% (−14,4 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$737,73 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,2%, WACC de los años 4-10 10,1%, ROE de FY+3 95,6% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 19,6x | 18,7x | +5% | 6,5% | 6,4% | +0,2 pp | Coherente con el DCF. |
| EV/FCFF | 21,0x | 28,3x | −26% | 5,1% | 6,4% | −1,3 pp | Revisar: el múltiplo vale 26% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 24,7x | 25,5x | −3% | 7,2% | 7,3% | −0,1 pp | Coherente con el DCF. |
| P/FCFE | 19,5x | 27,7x | −30% | 5,8% | 7,3% | −1,6 pp | Revisar: el múltiplo vale 30% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 18,9x | 26,7x | −29% | 5,8% | 7,3% | −1,5 pp | Revisar: el múltiplo vale 29% menos que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$506,71 | — |
| Múltiplos Base +20% | US$565,28 | +11,6% |
| Múltiplos Base −20% | US$448,15 | −11,6% |
| Crecimiento años 2-5 +2 pp | US$527,46 | +4,1% |
| Crecimiento años 2-5 −2 pp | US$487,73 | −3,7% |
| Margen objetivo +3 pp | US$522,45 | +3,1% |
| Margen objetivo −3 pp | US$490,97 | −3,1% |
| WACC +1 pp | US$494,98 | −2,3% |
| WACC −1 pp | US$519,28 | +2,5% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 13,90 | 13,90 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 19,57 | 19,57 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 28,65 | 28,51 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 16,08 | 15,87 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 21,10 | 21,00 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 31,21 | 30,99 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 17,94 | 17,94 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 24,73 | 24,73 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 35,57 | 35,57 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 14,22 | 14,22 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 19,46 | 19,46 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 26,83 | 26,83 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 13,78 | 13,78 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 18,89 | 18,89 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 25,70 | 25,70 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/ADBE_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/19WcSOKymo4gR6lnKiLB1gAitYFFwfI3xl08E4BDzLDw/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (ADSK, INTU, CRM, NOW, WDAY, PTC).

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
