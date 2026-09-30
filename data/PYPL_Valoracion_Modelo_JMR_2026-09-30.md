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

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$84,77 en el escenario Base (rango US$71,16–US$109,74). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$85,26 (+1% frente al DCF). Con los pesos de la categoría «Madura» (40% DCF, 60% múltiplos), el ponderado hoy (lectura secundaria) es US$85,07. El valor intrínseco es el DCF: US$84,77 frente a un precio de referencia de US$54,28 (+56%).

Los múltiplos (US$85,26 hoy) quedan 1% por encima del DCF (US$84,77): ambos métodos coinciden. Los dos quedan muy por encima del precio (US$54,28): el mercado descuenta que la utilidad no crece (guía 2026 plana) y un riesgo de ejecución con el nuevo CEO que el escenario Base no incorpora del todo. Los múltiplos ya usan la valoración de la etapa de bajo crecimiento (~9x EBITDA, ~13x utilidad), subida por peers ajustados −30% y por el justificado.

| Escenario | DCF hoy (valor intrínseco) | Múltiplos consolidados hoy (secundario) | Ponderado hoy (secundario) | Compra con MOS sobre el DCF | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$71,16 | US$67,22 | US$68,79 | US$46,25 | US$90,27 |
| Base | US$84,77 | US$85,26 | US$85,07 | US$55,10 | US$114,16 |
| Optimista | US$109,74 | US$106,75 | US$107,94 | US$71,33 | US$150,25 |

## 2. Datos

- Hoja del modelo: [Modelo_JMR_Plantilla_Maestra PYPL (automático)](https://docs.google.com/spreadsheets/d/13N5V1gpdsetin5NbTu-1-312lPYq5Pj4aKF4jw0bLT0/edit).
- Análisis del 22 de sept de 2026. Precio de referencia de la hoja: US$54,28.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 2,0% | 4,0% | 5,2% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 2,0% | 3,5% | 5,2% | Input B29 |
| Margen EBIT objetivo | 17,3% | 19,5% | 23,9% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 6 | 6 | 6 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,60 / 2,60 | — | Input B32/B33 |
| DCF por acción hoy | US$71,16 | US$84,77 | US$109,74 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,96%, beta apalancada 1,29, ERP 4,32%, Ke 10,53%, costo de la deuda después de impuestos 4,39%, peso del patrimonio 78,5%, WACC inicial 9,21% y terminal 9,05%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: PayPal cotizó a 18-60x EBITDA mientras crecía 15-20%. Desde 2023 es una procesadora de crecimiento bajo (~5%): en febrero de 2026 decepcionó con resultados y una guía de utilidad por acción plana, cambió de CEO (Enrique Lores reemplazó a Alex Chriss) y la acción cayó ~20%. La etapa actual es Dec '23 a LTM. B: pagos (Visa, Mastercard, Global Payments, Block, Adyen), datos de yfinance al 29-sep-2026. Fiserv (FI) no devolvió datos. En P/E se excluye Block (132x: utilidad deprimida por cargos puntuales). Ajuste −30%: PayPal crece ~5% con margen operativo de ~17%, frente a ~14% de crecimiento y márgenes de 44-66% de Visa, Mastercard y Adyen. λ = 0,25: la PayPal de FY+3 del escenario Base es una procesadora madura de crecimiento bajo, parecida a la de hoy.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 8,9x | 22,0x (n=5: V 22,0x, MA 22,8x, GPN 9,2x, XYZ 29,0x, ADYEY 14,8x) × 0,70 = 15,4x | 15,4x / 17,0x / 19,2x | 10,8x | **13,3x** | 15,1x | —x / 7,7x / —x |
| EV/FCFF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 11,6x (EV/FCF × 1,05 = FCF después de intereses ÷ FCFF) | 28,9x (n=4: V 31,6x, MA 30,6x, GPN 27,2x, XYZ 11,4x) × 0,70 = 20,2x | 20,7x / 22,7x / 25,5x | 14,9x | **17,6x** | 19,8x | —x / 10,5x / —x |
| P/E | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 13,4x | 31,0x (n=4: V 31,1x, MA 31,0x, GPN 39,5x, ADYEY 24,5x) × 0,70 = 21,7x | 13,7x / 14,8x / 16,3x | 15,0x | **16,9x** | 19,5x | —x / 10,3x / —x |
| P/FCFE | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 11,1x | 28,9x (n=4: V 32,7x, MA 30,9x, GPN 26,8x, XYZ 11,5x) × 0,70 = 20,2x | 16,2x / 17,4x / 19,1x | 13,6x | **16,1x** | 18,1x | —x / 12,1x / —x |
| P/OCF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 9,9x | 20,8x (n=4: V 30,4x, MA 28,3x, GPN 13,3x, XYZ 11,0x) × 0,70 = 14,6x | 14,9x / 16,7x / 18,9x | 10,2x | **13,3x** | 16,6x | —x / 9,6x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 13,3x: promedio de historia y peers 12,1x, acercado 25% al justificado (17,0x); rango de anclas 8,9x–17,0x. Atípicos excluidos de la historia: Dec '20 (60,5x: > 2,5x la mediana (18.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 17,6x: promedio de historia y peers 15,9x, acercado 25% al justificado (22,7x); rango de anclas 11,6x–22,7x. Atípicos excluidos de la historia: Dec '17 (44,3x: > 2,5x la mediana (17.1x)); Dec '20 (54,3x: > 2,5x la mediana (17.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 16,9x: promedio de historia y peers 17,6x, acercado 25% al justificado (14,8x); rango de anclas 13,4x–21,7x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 16,1x: promedio de historia y peers 15,6x, acercado 25% al justificado (17,4x); rango de anclas 11,1x–20,2x. Atípicos excluidos de la historia: Dec '20 (55,0x: > 2,5x la mediana (19.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 13,3x: promedio de historia y peers 12,2x, acercado 25% al justificado (16,7x); rango de anclas 9,9x–16,7x. Atípicos excluidos de la historia: Dec '20 (46,9x: > 2,5x la mediana (15.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$85,26 frente a US$84,77 del DCF (+1%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$85,26 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$96,09 | US$114,48 | US$148,19 |
| EV/EBITDA | 20% | US$81,40 | US$111,00 | US$144,36 |
| EV/FCFF | 10% | US$83,73 | US$109,38 | US$141,88 |
| P/E | 20% | US$93,52 | US$117,20 | US$158,32 |
| P/FCFE | 5% | US$93,26 | US$126,21 | US$168,90 |
| P/OCF | 5% | US$76,21 | US$109,62 | US$156,00 |
| **Ponderado FY+3** | 100% | US$90,27 | US$114,16 | US$150,25 |

Valor presente (Ke 10,53%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$71,09 | US$65,34 | US$60,28 | US$65,57 | OK |
| EV/EBITDA | Base | US$89,48 | US$86,37 | US$82,20 | US$86,02 | OK |
| EV/EBITDA | Optimista | US$102,36 | US$107,27 | US$106,90 | US$105,51 | OK |
| EV/FCFF | Conservador | US$73,31 | US$67,25 | US$62,00 | US$67,52 | OK |
| EV/FCFF | Base | US$87,70 | US$84,98 | US$81,00 | US$84,56 | OK |
| EV/FCFF | Optimista | US$99,05 | US$104,91 | US$105,06 | US$103,01 | OK |
| P/E | Conservador | US$71,43 | US$70,34 | US$69,25 | US$70,34 | OK |
| P/E | Base | US$81,78 | US$85,17 | US$86,79 | US$84,58 | OK |
| P/E | Optimista | US$95,60 | US$109,37 | US$117,24 | US$107,40 | OK |
| P/FCFE | Conservador | US$71,89 | US$70,31 | US$69,06 | US$70,42 | OK |
| P/FCFE | Base | US$90,41 | US$92,13 | US$93,46 | US$92,00 | OK |
| P/FCFE | Optimista | US$105,41 | US$117,76 | US$125,07 | US$116,08 | OK |
| P/OCF | Conservador | US$58,66 | US$57,42 | US$56,43 | US$57,51 | OK |
| P/OCF | Base | US$77,80 | US$80,06 | US$81,17 | US$79,68 | OK |
| P/OCF | Optimista | US$97,50 | US$108,80 | US$115,52 | US$107,27 | OK |

Múltiplos consolidados hoy: US$67,22 / US$85,26 / US$106,75 · DCF hoy: US$71,16 / US$84,77 / US$109,74 · Ponderado hoy: US$68,79 / US$85,07 / US$107,94 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para PYPL la diferencia es de +1% (múltiplos por encima del DCF). Los múltiplos (US$85,26 hoy) quedan 1% por encima del DCF (US$84,77): ambos métodos coinciden. Los dos quedan muy por encima del precio (US$54,28): el mercado descuenta que la utilidad no crece (guía 2026 plana) y un riesgo de ejecución con el nuevo CEO que el escenario Base no incorpora del todo. Los múltiplos ya usan la valoración de la etapa de bajo crecimiento (~9x EBITDA, ~13x utilidad), subida por peers ajustados −30% y por el justificado.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$54,28 supone que los ingresos crecen -6,6% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 3,6% (−10,2 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$114,48 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,5%, WACC de los años 4-10 9,1%, ROE de FY+3 29,8% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 13,3x | 13,8x | −3% | 3,4% | 3,5% | −0,2 pp | Coherente con el DCF. |
| EV/FCFF | 17,6x | 18,4x | −4% | 3,3% | 3,5% | −0,3 pp | Coherente con el DCF. |
| P/E | 16,9x | 16,5x | +2% | 5,4% | 5,3% | +0,1 pp | Coherente con el DCF. |
| P/FCFE | 16,1x | 14,6x | +10% | 4,1% | 3,4% | +0,6 pp | Coherente con el DCF. |
| P/OCF | 13,3x | 13,9x | −4% | 3,1% | 3,4% | −0,3 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$85,07 | — |
| Múltiplos Base +20% | US$95,22 | +11,9% |
| Múltiplos Base −20% | US$74,92 | −11,9% |
| Crecimiento años 1-5 +2 pp | US$88,30 | +3,8% |
| Crecimiento años 1-5 −2 pp | US$82,15 | −3,4% |
| Margen objetivo +3 pp | US$89,88 | +5,7% |
| Margen objetivo −3 pp | US$80,26 | −5,7% |
| WACC +1 pp | US$83,37 | −2,0% |
| WACC −1 pp | US$86,88 | +2,1% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 10,77 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 7,66 | 13,34 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 15,11 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 14,88 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 10,49 | 17,61 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 19,76 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 15,02 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 10,26 | 16,87 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 19,50 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 13,58 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 12,06 | 16,09 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 18,13 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 10,19 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 9,65 | 13,33 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 16,57 | Múltiplo optimista elegido con el protocolo v3 |
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
