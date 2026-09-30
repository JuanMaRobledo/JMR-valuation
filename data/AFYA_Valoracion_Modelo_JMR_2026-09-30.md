---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Afya Limited"
ticker: "AFYA"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1_CXhy_5n-V4rwfOSl8xI8455hywS5W92VBed_FCylvQ/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Afya Limited (AFYA) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$24,07 en el escenario Base (rango US$18,94–US$29,26). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$14,08 (−42% frente al DCF). Con los pesos de la categoría «Madura» (40% DCF, 60% múltiplos), el ponderado hoy (lectura secundaria) es US$18,07. El valor intrínseco es el DCF: US$24,07 frente a un precio de referencia de US$12,04 (+100%).

Revisión del 30-sep-2026 (ROIC terminal según el moat): moat estrecho, ROIC después del año 10 de 12,9%; el DCF da US$24,07 y los múltiplos US$14,08 hoy (42% por debajo, fuera del rango de ±25%). Revisión anterior: Revisión del 30-sep-2026 (ROIC terminal): con un ROIC después del año 10 de 14,8% el DCF pasa de US$22,43 a US$25,29. Los múltiplos (US$14,08 hoy) quedan 44% por debajo del DCF, fuera del rango de ±25%; el precio (US$12,04) está por debajo de ambos. Revisión de múltiplos: ninguna variante razonable cierra la brecha (sin el justificado, −53%; con peers ajustados por crecimiento, −44%). No es una inconsistencia del modelo: el mercado brasileño paga 5-7x EBITDA por la educación superior, y Afya cotiza además anclada a la relación de canje con Yduqs. Se mantienen. Lectura anterior, con el DCF sin ROIC terminal: Los múltiplos (US$14,08 hoy) quedan 37% por debajo del DCF (US$22,43): el mercado brasileño paga hoy ~5-6x EBITDA por las educadoras, con tasas locales altas, mientras que el DCF supone que Afya sostiene su margen EBIT de ~33% y descuenta con un Ke de 14% que ya incluye el riesgo país. Para el valor standalone de Afya el DCF es más confiable; los múltiplos reflejan el descuento que hoy aplica el mercado local y, además, la acción sigue la relación de canje de la fusión con Yduqs.

| Escenario | DCF hoy (valor intrínseco) | Múltiplos consolidados hoy (secundario) | Ponderado hoy (secundario) | Compra con MOS sobre el DCF | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$18,94 | US$11,63 | US$14,56 | US$12,31 | US$20,83 |
| Base | US$24,07 | US$14,08 | US$18,07 | US$15,64 | US$26,35 |
| Optimista | US$29,26 | US$16,59 | US$21,66 | US$19,02 | US$32,12 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - AFYA](https://docs.google.com/spreadsheets/d/1_CXhy_5n-V4rwfOSl8xI8455hywS5W92VBed_FCylvQ/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$12,04.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 3,5% | 6,0% | 7,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 3,5% | 5,0% | 7,0% | Input B29 |
| Margen EBIT objetivo | 29,0% | 33,0% | 36,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,50 / 1,20 | — | Input B32/B33 |
| DCF por acción hoy | US$18,94 | US$24,07 | US$29,26 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,18%, beta apalancada 1,20, ERP 7,33%, Ke 13,99%, costo de la deuda después de impuestos 7,39%, peso del patrimonio 58,1%, WACC inicial 11,22% y terminal 11,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: entre 2019 y 2021 Afya cotizaba a 30-90x por el crecimiento de sus facultades de medicina tras la salida a bolsa; desde 2024 la educación privada brasileña se re-valoró (tasas altas, madurez de plazas), así que A usa FY24, FY25 y el LTM. B: educación superior en Brasil (Cogna, Yduqs, Ser Educacional, Ânima) y Laureate (México y Perú), con datos de yfinance al 29-sep-2026. Se excluye Yduqs del P/E porque su utilidad está deprimida (P/E 24,8x frente a 6-7x del sector); Cruzeiro do Sul no tiene cotización disponible. Ajuste +10%: Afya tiene margen EBIT de ~33% frente a 17-26% de las otras educadoras brasileñas y un nicho regulado (plazas de medicina limitadas por el MEC) con demanda más estable. λ = 0,25: la Afya de FY+3 del escenario Base se parece a la de hoy (crecimiento de un dígito medio en reales).

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '24, Dec '25, LTM (etapa actual) = 6,5x | 5,2x (n=5: COGN3.SA 5,2x, YDUQ3.SA 5,2x, SEER3.SA 4,4x, ANIM3.SA 4,6x, LAUR 11,0x) × 1,10 = 5,7x | 10,8x / 11,9x / 13,3x | 6,8x | **7,5x** | 8,0x | 6,8x / 7,5x / 8,0x |
| EV/FCFF | mediana Dec '24, Dec '25, LTM (etapa actual) = 9,9x (EV/FCF × 0,70 = FCF después de intereses ÷ FCFF) | 5,7x (n=5: COGN3.SA 5,7x, YDUQ3.SA 4,9x, SEER3.SA 5,7x, ANIM3.SA 5,3x, LAUR 19,8x) × 1,10 = 6,2x | 16,3x / 17,5x / 19,5x | 9,6x | **10,4x** | 10,9x | 12,3x / 13,7x / 17,6x |
| P/E | mediana Dec '24, Dec '25, LTM (etapa actual) = 10,4x | 6,7x (n=4: COGN3.SA 6,1x, SEER3.SA 6,3x, ANIM3.SA 7,0x, LAUR 17,4x) × 1,10 = 7,3x | 7,3x / 7,9x / 8,4x | 7,9x | **8,6x** | 10,3x | 7,9x / 8,6x / 10,3x |
| P/FCFE | mediana Dec '24, Dec '25, LTM (etapa actual) = 10,7x | 4,4x (n=5: COGN3.SA 4,4x, YDUQ3.SA 3,1x, SEER3.SA 5,0x, ANIM3.SA 3,0x, LAUR 18,4x) × 1,10 = 4,8x | 11,3x / 11,9x / 12,8x | 7,4x | **8,8x** | 9,5x | 7,4x / 8,8x / 9,5x |
| P/OCF | mediana Dec '24, Dec '25, LTM (etapa actual) = 7,1x | 2,9x (n=5: COGN3.SA 2,9x, YDUQ3.SA 2,0x, SEER3.SA 3,9x, ANIM3.SA 1,9x, LAUR 13,0x) × 1,10 = 3,1x | 8,4x / 9,5x / 11,0x | 5,2x | **6,2x** | 7,3x | 5,2x / 6,2x / 7,3x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 7,5x: promedio de historia y peers 6,1x, acercado 25% al justificado (11,9x); rango de anclas 5,7x–11,9x. Atípicos excluidos de la historia: Dec '19 (33,4x: > 2,5x la mediana (11.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 10,4x: promedio de historia y peers 8,1x, acercado 25% al justificado (17,5x); rango de anclas 6,2x–17,5x. Atípicos excluidos de la historia: Dec '19 (88,3x: > 2,5x la mediana (27.6x)); Dec '20 (93,5x: > 2,5x la mediana (27.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 8,6x: promedio de historia y peers 8,9x, acercado 25% al justificado (7,9x); rango de anclas 7,3x–10,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 8,8x: promedio de historia y peers 7,8x, acercado 25% al justificado (11,9x); rango de anclas 4,8x–11,9x. Atípicos excluidos de la historia: Dec '19 (91,1x: > 2,5x la mediana (21.5x)); Dec '20 (89,6x: > 2,5x la mediana (21.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 6,2x: promedio de historia y peers 5,1x, acercado 25% al justificado (9,5x); rango de anclas 3,1x–9,5x. Atípicos excluidos de la historia: Dec '19 (42,3x: > 2,5x la mediana (12.8x)); Dec '20 (44,4x: > 2,5x la mediana (12.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$14,08 frente a US$24,07 del DCF (−42%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$14,08 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$28,05 | US$35,65 | US$43,33 |
| EV/EBITDA | 20% | US$19,08 | US$24,19 | US$28,85 |
| EV/FCFF | 10% | US$17,68 | US$22,54 | US$26,61 |
| P/E | 20% | US$13,17 | US$15,85 | US$20,43 |
| P/FCFE | 5% | US$14,30 | US$19,34 | US$23,83 |
| P/OCF | 5% | US$13,52 | US$17,31 | US$21,49 |
| **Ponderado FY+3** | 100% | US$20,83 | US$26,35 | US$32,12 |

Valor presente (Ke 13,99%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$14,98 | US$13,81 | US$12,89 | US$13,89 | OK |
| EV/EBITDA | Base | US$17,38 | US$16,97 | US$16,33 | US$16,90 | OK |
| EV/EBITDA | Optimista | US$19,11 | US$19,62 | US$19,48 | US$19,40 | OK |
| EV/FCFF | Conservador | US$14,01 | US$12,82 | US$11,94 | US$12,92 | OK |
| EV/FCFF | Base | US$15,92 | US$15,73 | US$15,22 | US$15,62 | OK |
| EV/FCFF | Optimista | US$17,07 | US$17,91 | US$17,97 | US$17,65 | OK |
| P/E | Conservador | US$10,21 | US$9,48 | US$8,89 | US$9,53 | OK |
| P/E | Base | US$11,33 | US$11,10 | US$10,70 | US$11,04 | OK |
| P/E | Optimista | US$13,62 | US$13,95 | US$13,79 | US$13,79 | OK |
| P/FCFE | Conservador | US$11,11 | US$10,31 | US$9,65 | US$10,36 | OK |
| P/FCFE | Base | US$14,58 | US$13,65 | US$13,06 | US$13,76 | OK |
| P/FCFE | Optimista | US$16,32 | US$16,43 | US$16,09 | US$16,28 | OK |
| P/OCF | Conservador | US$10,34 | US$9,69 | US$9,13 | US$9,72 | OK |
| P/OCF | Base | US$12,56 | US$12,20 | US$11,69 | US$12,15 | OK |
| P/OCF | Optimista | US$14,76 | US$14,82 | US$14,51 | US$14,70 | OK |

Múltiplos consolidados hoy: US$11,63 / US$14,08 / US$16,59 · DCF hoy: US$18,94 / US$24,07 / US$29,26 · Ponderado hoy: US$14,56 / US$18,07 / US$21,66 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para AFYA la diferencia es de −42% (múltiplos por debajo del DCF). Revisión del 30-sep-2026 (ROIC terminal según el moat): moat estrecho, ROIC después del año 10 de 12,9%; el DCF da US$24,07 y los múltiplos US$14,08 hoy (42% por debajo, fuera del rango de ±25%). Revisión anterior: Revisión del 30-sep-2026 (ROIC terminal): con un ROIC después del año 10 de 14,8% el DCF pasa de US$22,43 a US$25,29. Los múltiplos (US$14,08 hoy) quedan 44% por debajo del DCF, fuera del rango de ±25%; el precio (US$12,04) está por debajo de ambos. Revisión de múltiplos: ninguna variante razonable cierra la brecha (sin el justificado, −53%; con peers ajustados por crecimiento, −44%). No es una inconsistencia del modelo: el mercado brasileño paga 5-7x EBITDA por la educación superior, y Afya cotiza además anclada a la relación de canje con Yduqs. Se mantienen. Lectura anterior, con el DCF sin ROIC terminal: Los múltiplos (US$14,08 hoy) quedan 37% por debajo del DCF (US$22,43): el mercado brasileño paga hoy ~5-6x EBITDA por las educadoras, con tasas locales altas, mientras que el DCF supone que Afya sostiene su margen EBIT de ~33% y descuenta con un Ke de 14% que ya incluye el riesgo país. Para el valor standalone de Afya el DCF es más confiable; los múltiplos reflejan el descuento que hoy aplica el mercado local y, además, la acción sigue la relación de canje de la fusión con Yduqs.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$12,04 supone que los ingresos crecen -7,0% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 5,2% (−12,2 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$35,65 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 14,0%, WACC de los años 4-10 11,1%, ROE de FY+3 15,2% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 7,5x | 10,6x | −32% | 1,9% | 4,5% | −2,5 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 32% por debajo del DCF en FY+3. |
| EV/FCFF | 10,4x | 15,7x | −37% | 1,4% | 4,5% | −3,1 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 37% por debajo del DCF en FY+3. |
| P/E | 8,6x | 20,9x | −56% | 8,2% | 13,3% | −5,1 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 56% por debajo del DCF en FY+3. |
| P/FCFE | 8,8x | 17,1x | −46% | 2,4% | 7,7% | −5,3 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 46% por debajo del DCF en FY+3. |
| P/OCF | 6,2x | 13,7x | −51% | 1,0% | 7,7% | −6,7 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 51% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$18,07 | — |
| Múltiplos Base +20% | US$19,89 | +10,0% |
| Múltiplos Base −20% | US$16,26 | −10,0% |
| Crecimiento años 1-5 +2 pp | US$19,18 | +6,1% |
| Crecimiento años 1-5 −2 pp | US$17,07 | −5,5% |
| Margen objetivo +3 pp | US$19,05 | +5,4% |
| Margen objetivo −3 pp | US$17,10 | −5,4% |
| WACC +1 pp | US$17,49 | −3,2% |
| WACC −1 pp | US$18,69 | +3,4% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 1-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 6,83 | 6,83 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 7,51 | 7,51 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 8,04 | 8,04 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 12,28 | 9,62 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 13,65 | 10,43 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 17,58 | 10,94 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 7,90 | 7,90 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 8,61 | 8,61 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 10,35 | 10,35 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 7,42 | 7,42 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 8,80 | 8,80 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 9,49 | 9,49 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 5,18 | 5,18 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 6,23 | 6,23 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 7,32 | 7,32 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/AFYA_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1_CXhy_5n-V4rwfOSl8xI8455hywS5W92VBed_FCylvQ/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (COGN3.SA, YDUQ3.SA, SEER3.SA, ANIM3.SA, LAUR, CRUZ3.SA).

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
