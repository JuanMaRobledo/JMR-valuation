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

**Valor intrínseco principal · DCF Base hoy: US$176,02 por acción.** Complemento: DCF esperado por probabilidades US$156,93; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$85,26–US$231,58; precio con MOS 35% sobre el esperado: US$102,00; precio de referencia US$108,58. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son la calibración técnica anterior de la hoja (Base técnico US$171,68) y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · La IA compensa lo que quita: crecimiento moderado** (valor principal) | 45% | US$176,02 | US$79,21 |
| Conservadora · Deflación de horas por IA | 30% | US$114,85 | US$34,46 |
| Disrupción · Deterioro de los fundamentales: Los servicios se comoditizan | 10% | US$85,26 | US$8,53 |
| Optimista · La IA crea demanda de ingeniería | 15% | US$231,58 | US$34,74 |
| **DCF esperado (complemento)** | 100% | **US$156,93** | |

Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$168,22 por acción y los múltiplos, US$109,37 hoy: 35% por debajo del DCF, fuera del rango de ±25%. Los múltiplos reflejan lo que el mercado paga hoy por los servicios de TI bajo el temor a la IA (~7-9x EBITDA); el DCF supone que EPAM vuelve a crecer y a recuperar margen. Si la presión de los asistentes de código resulta estructural, los múltiplos son la referencia más prudente.

| Escenario | DCF técnico anterior hoy (calibración) | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$171,68 | US$112,92 | US$136,42 | US$102,00 | US$184,18 |
| Conservador | US$120,61 | US$90,62 | US$102,61 | US$102,00 | US$132,14 |
| Optimista | US$252,90 | US$150,04 | US$191,18 | US$102,00 | US$269,42 |

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
| Margen EBIT objetivo | 10,0% | 13,0% | 15,5% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 3,27 / 2,83 | — | Input B32/B33 |
| DCF por acción hoy | US$120,61 | US$171,68 | US$252,90 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,30, ERP 4,46%, Ke 10,79%, costo de la deuda después de impuestos 4,38%, peso del patrimonio 97,6%, WACC inicial 10,63% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: EPAM cotizó a 15-59x EBITDA mientras crecía 15-25% al año como proveedor de ingeniería de software. En febrero de 2026 guió un crecimiento orgánico de solo 3-6% y luego lo bajó a 3,2-4,2%; el mercado lo lee como presión estructural de los asistentes de código con IA sobre la subcontratación tradicional, y la acción cayó a mínimos. La etapa actual es solo el LTM. B: servicios de TI y consultoría (Accenture, Globant, Cognizant, Infosys, ExlService), datos de yfinance al 29-sep-2026. Se excluye Wipro (sus cifras mezclan rupias y dólares: EV/EBITDA negativo) y, en los múltiplos de EV, Infosys (EV/EBITDA de 18,8x incoherente con su P/E de 13x). Sin ajuste: EPAM crece como Accenture y Cognizant (3-6%), con menor margen operativo pero sin deuda y con recompras; las diferencias se compensan. λ = 0,25: la EPAM de FY+3 del escenario Base es una empresa de servicios de TI de crecimiento bajo, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana LTM (etapa actual) = 7,1x | 7,5x (n=4: ACN 8,4x, GLOB 4,7x, CTSH 6,6x, EXLS 14,4x) × 1,00 = 7,5x | 14,8x / 12,2x / 19,2x | **9,2x** | 8,1x | 11,1x | 7,1x / —x / —x |
| EV/FCFF | mediana LTM (etapa actual) = 10,0x (EV/FCF × 0,98 = FCF después de intereses ÷ FCFF) | 9,3x (n=4: ACN 8,5x, GLOB 6,6x, CTSH 10,1x, EXLS 18,8x) × 1,00 = 9,3x | 21,1x / 17,0x / 27,8x | **12,5x** | 11,1x | 15,2x | 10,2x / —x / —x |
| P/E | mediana LTM (etapa actual) = 15,2x | 13,3x (n=5: ACN 14,1x, GLOB 13,3x, CTSH 12,3x, INFY 13,1x, EXLS 21,9x) × 1,00 = 13,3x | 12,2x / 10,0x / 15,6x | **13,7x** | 12,8x | 15,3x | 15,2x / —x / —x |
| P/FCFE | mediana LTM (etapa actual) = 11,6x | 9,8x (n=5: ACN 8,6x, GLOB 5,8x, CTSH 9,9x, INFY 11,3x, EXLS 19,1x) × 1,00 = 9,8x | 18,1x / 15,0x / 22,8x | **12,6x** | 11,3x | 14,3x | 11,6x / —x / —x |
| P/OCF | mediana LTM (etapa actual) = 10,4x | 8,8x (n=5: ACN 8,2x, GLOB 4,3x, CTSH 8,8x, INFY 10,5x, EXLS 16,0x) × 1,00 = 8,8x | 17,1x / 13,9x / 21,8x | **11,5x** | 10,5x | 13,3x | 10,4x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 9,2x: promedio de historia y peers 7,3x, acercado 25% al justificado (14,8x); rango de anclas 7,1x–14,8x. Atípicos excluidos de la historia: LTM (7,1x: < 0,4x la mediana (25.5x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 12,5x: promedio de historia y peers 9,6x, acercado 25% al justificado (21,1x); rango de anclas 9,3x–21,1x. Atípicos excluidos de la historia: Dec '21 (79,7x: > 2,5x la mediana (28.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 13,7x: promedio de historia y peers 14,2x, acercado 25% al justificado (12,2x); rango de anclas 12,2x–15,2x. Atípicos excluidos de la historia: LTM (15,2x: < 0,4x la mediana (42.1x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 12,6x: promedio de historia y peers 10,7x, acercado 25% al justificado (18,1x); rango de anclas 9,8x–18,1x. Atípicos excluidos de la historia: Dec '21 (82,4x: > 2,5x la mediana (32.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 11,5x: promedio de historia y peers 9,6x, acercado 25% al justificado (17,1x); rango de anclas 8,8x–17,1x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$112,92 frente a US$171,68 del DCF (−34%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$112,92 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$233,57 | US$164,08 | US$344,09 |
| EV/EBITDA | 20% | US$158,72 | US$115,30 | US$234,05 |
| EV/FCFF | 10% | US$152,40 | US$113,80 | US$222,91 |
| P/E | 20% | US$144,92 | US$105,67 | US$208,11 |
| P/FCFE | 5% | US$149,93 | US$109,51 | US$212,48 |
| P/OCF | 5% | US$145,69 | US$109,21 | US$208,68 |
| **Ponderado FY+3** | 100% | US$184,18 | US$132,14 | US$269,42 |

Valor presente (Ke 10,79%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$122,86 | US$120,84 | US$116,72 | US$120,14 | OK |
| EV/EBITDA | Conservador | US$105,91 | US$94,03 | US$84,79 | US$94,91 | OK |
| EV/EBITDA | Optimista | US$150,30 | US$165,88 | US$172,12 | US$162,77 | OK |
| EV/FCFF | Base | US$117,43 | US$115,77 | US$112,07 | US$115,09 | OK |
| EV/FCFF | Conservador | US$104,36 | US$92,68 | US$83,69 | US$93,58 | OK |
| EV/FCFF | Optimista | US$141,36 | US$157,29 | US$163,93 | US$154,19 | OK |
| P/E | Base | US$105,80 | US$107,63 | US$106,57 | US$106,67 | OK |
| P/E | Conservador | US$95,24 | US$85,26 | US$77,71 | US$86,07 | OK |
| P/E | Optimista | US$122,33 | US$142,65 | US$153,05 | US$139,34 | OK |
| P/FCFE | Base | US$109,42 | US$111,00 | US$110,26 | US$110,23 | OK |
| P/FCFE | Conservador | US$96,99 | US$87,55 | US$80,54 | US$88,36 | OK |
| P/FCFE | Optimista | US$126,26 | US$145,69 | US$156,26 | US$142,74 | OK |
| P/OCF | Base | US$106,85 | US$108,05 | US$107,14 | US$107,35 | OK |
| P/OCF | Conservador | US$96,47 | US$87,25 | US$80,31 | US$88,01 | OK |
| P/OCF | Optimista | US$125,55 | US$143,62 | US$153,46 | US$140,88 | OK |

Múltiplos consolidados hoy: US$112,92 / US$90,62 / US$150,04 · DCF técnico hoy: US$171,68 / US$120,61 / US$252,90 · Ponderado hoy: US$136,42 / US$102,61 / US$191,18 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para EPAM la diferencia es de −34% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$168,22 por acción y los múltiplos, US$109,37 hoy: 35% por debajo del DCF, fuera del rango de ±25%. Los múltiplos reflejan lo que el mercado paga hoy por los servicios de TI bajo el temor a la IA (~7-9x EBITDA); el DCF supone que EPAM vuelve a crecer y a recuperar margen. Si la presión de los asistentes de código resulta estructural, los múltiplos son la referencia más prudente.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$108,58 supone que los ingresos crecen -6,1% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 5,0% (−11,1 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$233,57 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,8%, WACC de los años 4-10 10,0%, ROE de FY+3 15,3% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 9,2x | 13,9x | −32% | 2,2% | 4,7% | −2,5 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 32% por debajo del DCF en FY+3. |
| EV/FCFF | 12,5x | 19,8x | −35% | 1,8% | 4,7% | −2,9 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 35% por debajo del DCF en FY+3. |
| P/E | 13,7x | 22,1x | −38% | 6,2% | 8,7% | −2,5 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 38% por debajo del DCF en FY+3. |
| P/FCFE | 12,6x | 19,6x | −36% | 2,6% | 5,4% | −2,8 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 36% por debajo del DCF en FY+3. |
| P/OCF | 11,5x | 18,4x | −38% | 2,4% | 5,4% | −3,0 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 38% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$136,42 | — |
| Múltiplos Base +20% | US$149,30 | +9,4% |
| Múltiplos Base −20% | US$123,54 | −9,4% |
| Crecimiento años 2-5 +2 pp | US$141,44 | +3,7% |
| Crecimiento años 2-5 −2 pp | US$131,84 | −3,4% |
| Margen objetivo +3 pp | US$151,31 | +10,9% |
| Margen objetivo −3 pp | US$121,53 | −10,9% |
| WACC +1 pp | US$133,03 | −2,5% |
| WACC −1 pp | US$140,05 | +2,7% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Margen objetivo −3 pp, Múltiplos Base −20%.

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
