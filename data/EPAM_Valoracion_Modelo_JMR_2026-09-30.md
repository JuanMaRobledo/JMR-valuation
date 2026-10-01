---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de EPAM Systems, Inc."
ticker: "EPAM"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1txQTjdUuzsnCem_4O1szofY7uAp5xLc3uda3l_iIcR0/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# EPAM Systems, Inc. (EPAM) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal: DCF esperado de las cuatro historias, US$152,15.** Historia central A: US$170,49; rango US$82,78–US$224,77; precio con MOS 35% sobre el esperado: US$98,90; precio de referencia US$108,58. Cada historia es un DCF completo (hoja «Escenarios e historias»); el detalle está en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son la calibración técnica anterior de la hoja (Base US$172,85) y los múltiplos y el ponderado son lecturas secundarias.


| Historia | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| A · La IA compensa lo que quita: crecimiento moderado | 45% | US$170,49 | US$76,72 |
| B · Deflación de horas por IA | 30% | US$111,45 | US$33,43 |
| C · Tesis de disrupción · Deterioro de los fundamentales: Los servicios se comoditizan | 10% | US$82,78 | US$8,28 |
| D · La IA crea demanda de ingeniería | 15% | US$224,77 | US$33,72 |
| **DCF esperado** | 100% | **US$152,15** | |

Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$168,22 por acción y los múltiplos, US$109,37 hoy: 35% por debajo del DCF, fuera del rango de ±25%. Los múltiplos reflejan lo que el mercado paga hoy por los servicios de TI bajo el temor a la IA (~7-9x EBITDA); el DCF supone que EPAM vuelve a crecer y a recuperar margen. Si la presión de los asistentes de código resulta estructural, los múltiplos son la referencia más prudente.

| Escenario | DCF técnico anterior hoy (calibración) | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$116,61 | US$86,87 | US$98,76 | US$98,90 | US$127,12 |
| Base | US$172,85 | US$109,90 | US$135,08 | US$98,90 | US$183,37 |
| Optimista | US$245,79 | US$144,45 | US$184,99 | US$98,90 | US$260,94 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - EPAM](https://docs.google.com/spreadsheets/d/1txQTjdUuzsnCem_4O1szofY7uAp5xLc3uda3l_iIcR0/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$108,58.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 1,0% | 5,0% | 9,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 1,0% | 5,0% | 9,0% | Input B29 |
| Margen EBIT objetivo | 9,5% | 12,5% | 15,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 3,50 / 3,00 | — | Input B32/B33 |
| DCF por acción hoy | US$116,61 | US$172,85 | US$245,79 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,30, ERP 4,46%, Ke 10,79%, costo de la deuda después de impuestos 4,38%, peso del patrimonio 99,4%, WACC inicial 10,75% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: EPAM cotizó a 15-59x EBITDA mientras crecía 15-25% al año como proveedor de ingeniería de software. En febrero de 2026 guió un crecimiento orgánico de solo 3-6% y luego lo bajó a 3,2-4,2%; el mercado lo lee como presión estructural de los asistentes de código con IA sobre la subcontratación tradicional, y la acción cayó a mínimos. La etapa actual es solo el LTM. B: servicios de TI y consultoría (Accenture, Globant, Cognizant, Infosys, ExlService), datos de yfinance al 29-sep-2026. Se excluye Wipro (sus cifras mezclan rupias y dólares: EV/EBITDA negativo) y, en los múltiplos de EV, Infosys (EV/EBITDA de 18,8x incoherente con su P/E de 13x). Sin ajuste: EPAM crece como Accenture y Cognizant (3-6%), con menor margen operativo pero sin deuda y con recompras; las diferencias se compensan. λ = 0,25: la EPAM de FY+3 del escenario Base es una empresa de servicios de TI de crecimiento bajo, parecida a la de hoy.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana LTM (etapa actual) = 7,1x | 7,5x (n=4: ACN 8,4x, GLOB 4,7x, CTSH 6,6x, EXLS 14,4x) × 1,00 = 7,5x | 12,2x / 14,8x / 19,2x | 8,1x | **9,2x** | 11,1x | —x / 7,1x / —x |
| EV/FCFF | mediana LTM (etapa actual) = 10,0x (EV/FCF × 0,98 = FCF después de intereses ÷ FCFF) | 9,3x (n=4: ACN 8,5x, GLOB 6,6x, CTSH 10,1x, EXLS 18,8x) × 1,00 = 9,3x | 17,0x / 21,1x / 27,8x | 11,1x | **12,5x** | 15,2x | —x / 10,2x / —x |
| P/E | mediana LTM (etapa actual) = 15,2x | 13,3x (n=5: ACN 14,1x, GLOB 13,3x, CTSH 12,3x, INFY 13,1x, EXLS 21,9x) × 1,00 = 13,3x | 10,0x / 12,2x / 15,6x | 12,8x | **13,7x** | 15,3x | —x / 15,2x / —x |
| P/FCFE | mediana LTM (etapa actual) = 11,6x | 9,8x (n=5: ACN 8,6x, GLOB 5,8x, CTSH 9,9x, INFY 11,3x, EXLS 19,1x) × 1,00 = 9,8x | 15,0x / 18,1x / 22,8x | 11,3x | **12,6x** | 14,3x | —x / 11,6x / —x |
| P/OCF | mediana LTM (etapa actual) = 10,4x | 8,8x (n=5: ACN 8,2x, GLOB 4,3x, CTSH 8,8x, INFY 10,5x, EXLS 16,0x) × 1,00 = 8,8x | 13,9x / 17,1x / 21,8x | 10,5x | **11,5x** | 13,3x | —x / 10,4x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 9,2x: promedio de historia y peers 7,3x, acercado 25% al justificado (14,8x); rango de anclas 7,1x–14,8x. Atípicos excluidos de la historia: LTM (7,1x: < 0,4x la mediana (25.5x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 12,5x: promedio de historia y peers 9,6x, acercado 25% al justificado (21,1x); rango de anclas 9,3x–21,1x. Atípicos excluidos de la historia: Dec '21 (79,7x: > 2,5x la mediana (28.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 13,7x: promedio de historia y peers 14,2x, acercado 25% al justificado (12,2x); rango de anclas 12,2x–15,2x. Atípicos excluidos de la historia: LTM (15,2x: < 0,4x la mediana (42.1x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 12,6x: promedio de historia y peers 10,7x, acercado 25% al justificado (18,1x); rango de anclas 9,8x–18,1x. Atípicos excluidos de la historia: Dec '21 (82,4x: > 2,5x la mediana (32.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 11,5x: promedio de historia y peers 9,6x, acercado 25% al justificado (17,1x); rango de anclas 8,8x–17,1x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$109,90 frente a US$172,85 del DCF (−36%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$109,90 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$158,56 | US$235,05 | US$334,23 |
| EV/EBITDA | 20% | US$111,02 | US$156,54 | US$226,71 |
| EV/FCFF | 10% | US$109,50 | US$150,22 | US$215,54 |
| P/E | 20% | US$100,32 | US$142,35 | US$200,11 |
| P/FCFE | 5% | US$104,79 | US$147,58 | US$205,00 |
| P/OCF | 5% | US$104,82 | US$143,54 | US$201,73 |
| **Ponderado FY+3** | 100% | US$127,12 | US$183,37 | US$260,94 |

Valor presente (Ke 10,79%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$102,13 | US$90,58 | US$81,64 | US$91,45 | OK |
| EV/EBITDA | Base | US$118,39 | US$118,30 | US$115,12 | US$117,27 | OK |
| EV/EBITDA | Optimista | US$144,72 | US$160,39 | US$166,72 | US$157,28 | OK |
| EV/FCFF | Conservador | US$100,56 | US$89,21 | US$80,53 | US$90,10 | OK |
| EV/FCFF | Base | US$112,98 | US$113,24 | US$110,47 | US$112,23 | OK |
| EV/FCFF | Optimista | US$135,76 | US$151,78 | US$158,51 | US$148,68 | OK |
| P/E | Conservador | US$90,68 | US$81,02 | US$73,78 | US$81,83 | OK |
| P/E | Base | US$100,73 | US$104,69 | US$104,68 | US$103,37 | OK |
| P/E | Optimista | US$116,47 | US$136,78 | US$147,16 | US$133,47 | OK |
| P/FCFE | Conservador | US$92,97 | US$83,81 | US$77,07 | US$84,62 | OK |
| P/FCFE | Base | US$104,78 | US$108,31 | US$108,53 | US$107,21 | OK |
| P/FCFE | Optimista | US$120,78 | US$140,20 | US$150,76 | US$137,25 | OK |
| P/OCF | Conservador | US$92,74 | US$83,78 | US$77,09 | US$84,53 | OK |
| P/OCF | Base | US$102,61 | US$105,59 | US$105,56 | US$104,59 | OK |
| P/OCF | Optimista | US$120,46 | US$138,52 | US$148,35 | US$135,78 | OK |

Múltiplos consolidados hoy: US$86,87 / US$109,90 / US$144,45 · DCF hoy: US$116,61 / US$172,85 / US$245,79 · Ponderado hoy: US$98,76 / US$135,08 / US$184,99 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para EPAM la diferencia es de −36% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$168,22 por acción y los múltiplos, US$109,37 hoy: 35% por debajo del DCF, fuera del rango de ±25%. Los múltiplos reflejan lo que el mercado paga hoy por los servicios de TI bajo el temor a la IA (~7-9x EBITDA); el DCF supone que EPAM vuelve a crecer y a recuperar margen. Si la presión de los asistentes de código resulta estructural, los múltiplos son la referencia más prudente.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$108,58 supone que los ingresos crecen -6,2% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 5,0% (−11,2 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$235,05 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,8%, WACC de los años 4-10 10,0%, ROE de FY+3 15,3% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 9,2x | 14,2x | −33% | 2,2% | 4,8% | −2,6 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 33% por debajo del DCF en FY+3. |
| EV/FCFF | 12,5x | 20,3x | −36% | 1,8% | 4,8% | −3,0 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 36% por debajo del DCF en FY+3. |
| P/E | 13,7x | 22,6x | −39% | 6,2% | 8,7% | −2,6 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 39% por debajo del DCF en FY+3. |
| P/FCFE | 12,6x | 20,0x | −37% | 2,6% | 5,5% | −2,9 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 37% por debajo del DCF en FY+3. |
| P/OCF | 11,5x | 18,8x | −39% | 2,4% | 5,5% | −3,1 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 39% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$135,08 | — |
| Múltiplos Base +20% | US$147,60 | +9,3% |
| Múltiplos Base −20% | US$122,56 | −9,3% |
| Crecimiento años 2-5 +2 pp | US$140,17 | +3,8% |
| Crecimiento años 2-5 −2 pp | US$130,43 | −3,4% |
| Margen objetivo +3 pp | US$149,87 | +11,0% |
| Margen objetivo −3 pp | US$120,29 | −11,0% |
| WACC +1 pp | US$131,71 | −2,5% |
| WACC −1 pp | US$138,69 | +2,7% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Margen objetivo −3 pp, Múltiplos Base +20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 8,09 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 7,12 | 9,19 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 11,05 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 11,10 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 10,16 | 12,51 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 15,16 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 12,83 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 15,16 | 13,71 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 15,27 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 11,31 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 11,57 | 12,56 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 14,27 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 10,51 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 10,37 | 11,46 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 13,26 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/EPAM_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1txQTjdUuzsnCem_4O1szofY7uAp5xLc3uda3l_iIcR0/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (ACN, GLOB, CTSH, INFY, EXLS, WIT).
- [Trefis, 20-feb-2026: EPAM −17% por una guía 2026 cauta](https://www.trefis.com/stock/epam/articles/591182/epam-stock-17-cautious-2026-guidance-ignites-investor-revolt/2026-02-20)
- [Finimize: EPAM recorta su guía 2026](https://finimize.com/content/epam-cuts-its-2026-revenue-outlook-as-ai-fears-linger)
- [Morningstar: EPAM vulnerable a la disrupción de la IA](https://www.morningstar.com/company-reports/1450663-no-moat-epam-systems-is-vulnerable-to-ais-potential-disruption)

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
