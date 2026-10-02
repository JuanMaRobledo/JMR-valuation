---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de On Holding AG"
ticker: "ONON"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1nlN8qDy9BipM5IWwGE5Fgf6VKpyYQScLXIPvqtAE9Oo/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# On Holding AG (ONON) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$33,24 por acción.** Complemento: DCF esperado por probabilidades US$30,73; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$12,53–US$46,56; precio con MOS 35% sobre el esperado: US$19,97; precio de referencia US$30,20. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$34,02), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Marca premium global que crece ~15% con margen de 16,5%** (valor principal) | 45% | US$33,24 | US$14,96 |
| Conservadora · El ciclo de moda se enfría | 25% | US$20,80 | US$5,20 |
| Disrupción · Deterioro de los fundamentales: pasa la moda y las ventas caen como en Under Armour | 10% | US$12,53 | US$1,25 |
| Optimista · On se vuelve una marca deportiva global de primera línea | 20% | US$46,56 | US$9,31 |
| **DCF esperado (complemento)** | 100% | **US$30,73** | |

Lectura del 2-oct-2026: el DCF Base de las historias da ~US$33,2 por acción y los múltiplos consolidados ~US$47 hoy, ~40% más, fuera del ±25%. Los múltiplos no se movieron para acercarlos. La diferencia es la ventaja competitiva: el justificado (C) supone que el ROE de FY+3 (~22%) dura para siempre y la historia de On (P/E de 60-96×) refleja la etapa de hipercrecimiento, mientras el DCF lleva el ROIC al costo de capital después del año 10 porque la marca tiene 16 años y no está probada. El DCF es el valor intrínseco; los múltiplos dicen cuánto pagaría el mercado si On sostuviera retornos excedentes como una marca consolidada.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$33,24 | US$47,29 | US$38,86 | US$19,97 | US$54,57 |
| Conservador | US$20,80 | US$33,87 | US$26,03 | US$19,97 | US$39,24 |
| Optimista | US$46,56 | US$66,30 | US$54,46 | US$19,97 | US$84,78 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - ONON (desde cero 2026-10-02)](https://docs.google.com/spreadsheets/d/1nlN8qDy9BipM5IWwGE5Fgf6VKpyYQScLXIPvqtAE9Oo/edit).
- Análisis del 01 de oct de 2026. Precio de referencia de la hoja: US$30,20.
- Peers: datos de mercado de yfinance consultados el 2026-10-02 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 12,5% | 17,5% | 18,5% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 12,5% | 14,0% | 18,5% | Input B29 |
| Margen EBIT objetivo | 13,8% | 16,5% | 21,5% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,30 / 2,10 | — | Input B32/B33 |
| DCF por acción hoy | US$20,80 | US$33,24 | US$46,56 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,24%, beta apalancada 1,30, ERP 4,09%, Ke 10,56%, costo de la deuda después de impuestos 4,62%, peso del patrimonio 93,6%, WACC inicial 10,18% y terminal 9,33%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: 2021 (pérdida por los pagos en acciones de la salida a bolsa) y 2022 (flujo negativo por inventario) no son comparables. Desde 2023 On es una marca rentable que crece 20-30% al año: la etapa actual es Dec '23, Dec '24, Dec '25 y el LTM, con múltiplos de 24-48× EBITDA que bajan con el precio. B: calzado y ropa deportiva con datos de yfinance al 2-oct-2026: Deckers, Nike, Lululemon, Birkenstock, Adidas y Crocs. Ajuste +25%: crecimiento a FY+3 mucho mayor que la mediana de los peers (Base ~14% frente a −4% a +13%), +25%; margen bruto mayor (65% frente a 45-60%), +5%; riesgo propio mayor (marca joven, beta 1,30), −5%. λ = 0,5: los peers son marcas maduras o en caída y la historia de On refleja múltiplos de la etapa de hipercrecimiento; el justificado (C) usa los supuestos de cada escenario y equilibra ambos.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 27,3x | 9,4x (n=6: DECK 7,3x, NKE 11,0x, LULU 4,8x, BIRK 11,0x, ADDYY 12,4x, CROX 7,8x) × 1,25 = 11,7x | 32,1x / 26,1x / — | **25,8x** | 20,6x | 31,4x | 24,2x / —x / —x |
| EV/FCFF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 18,2x (EV/FCF × 0,47 = FCF después de intereses ÷ FCFF) | 13,5x (n=6: DECK 8,7x, NKE 24,8x, LULU 8,4x, BIRK 19,5x, ADDYY 17,6x, CROX 9,4x) × 1,25 = 16,9x | 52,0x / 42,9x / — | **34,8x** | 26,5x | 44,0x | 28,9x / —x / —x |
| P/E | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 63,2x | 13,5x (n=6: DECK 11,2x, NKE 15,8x, LULU 7,8x, BIRK 16,1x, ADDYY 18,2x, CROX 10,6x) × 1,25 = 16,9x | 24,7x / 19,8x / — | **32,4x** | 26,0x | 37,7x | 62,6x / —x / —x |
| P/FCFE | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 39,8x | 12,5x (n=6: DECK 9,6x, NKE 22,6x, LULU 7,7x, BIRK 18,8x, ADDYY 15,4x, CROX 8,1x) × 1,25 = 15,6x | 38,3x / 33,1x / — | **33,0x** | 25,9x | 42,3x | 33,9x / —x / —x |
| P/OCF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 32,9x | 10,6x (n=6: DECK 9,0x, NKE 17,2x, LULU 5,3x, BIRK 13,7x, ADDYY 12,2x, CROX 7,5x) × 1,25 = 13,3x | 36,4x / 30,7x / — | **29,7x** | 24,1x | 34,6x | 29,7x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 25,8x: promedio de historia y peers 19,5x, acercado 50% al justificado (32,1x); rango de anclas 11,7x–32,1x. Atípicos excluidos de la historia: Dec '21 (-93,8x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 34,8x: promedio de historia y peers 17,5x, acercado 50% al justificado (52,0x); rango de anclas 16,9x–52,0x. Atípicos excluidos de la historia: Dec '21 (-465,0x: métrica negativa o ~0); Dec '22 (-15,8x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 32,4x: promedio de historia y peers 40,1x, acercado 50% al justificado (24,7x); rango de anclas 16,9x–63,2x. Atípicos excluidos de la historia: Dec '21 (-63,0x: métrica negativa o ~0); LTM (20,3x: < 0,4x la mediana (64.4x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 33,0x: promedio de historia y peers 27,7x, acercado 50% al justificado (38,3x); rango de anclas 15,6x–39,8x. Atípicos excluidos de la historia: Dec '21 (-486,5x: métrica negativa o ~0); Dec '22 (-16,5x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 29,7x: promedio de historia y peers 23,1x, acercado 50% al justificado (36,4x); rango de anclas 13,3x–36,4x. Atípicos excluidos de la historia: Dec '22 (-22,4x: métrica negativa o ~0); Dec '21 (764,5x: > 2,5x la mediana (34.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$47,29 frente a US$33,24 del DCF (+42%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$47,29 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$45,97 | US$35,08 | US$71,94 |
| EV/EBITDA | 10% | US$83,64 | US$57,77 | US$126,84 |
| EV/FCFF | 15% | US$69,89 | US$45,85 | US$110,30 |
| P/E | 5% | US$48,15 | US$32,33 | US$72,92 |
| P/FCFE | 5% | US$58,88 | US$39,20 | US$96,18 |
| P/OCF | 5% | US$55,81 | US$39,25 | US$78,65 |
| **Ponderado FY+3** | 100% | US$54,57 | US$39,24 | US$84,78 |

Valor presente (Ke 10,56%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$55,95 | US$59,98 | US$61,90 | US$59,28 | OK |
| EV/EBITDA | Conservador | US$43,21 | US$43,20 | US$42,75 | US$43,05 | OK |
| EV/EBITDA | Optimista | US$68,31 | US$83,85 | US$93,87 | US$82,01 | OK |
| EV/FCFF | Base | US$44,10 | US$49,91 | US$51,72 | US$48,58 | OK |
| EV/FCFF | Conservador | US$34,35 | US$34,43 | US$33,93 | US$34,24 | OK |
| EV/FCFF | Optimista | US$55,20 | US$71,66 | US$81,62 | US$69,49 | OK |
| P/E | Base | US$31,29 | US$34,00 | US$35,63 | US$33,64 | OK |
| P/E | Conservador | US$24,10 | US$23,98 | US$23,92 | US$24,00 | OK |
| P/E | Optimista | US$36,74 | US$47,04 | US$53,96 | US$45,91 | OK |
| P/FCFE | Base | US$38,87 | US$42,10 | US$43,58 | US$41,52 | OK |
| P/FCFE | Conservador | US$28,92 | US$29,27 | US$29,01 | US$29,07 | OK |
| P/FCFE | Optimista | US$50,35 | US$63,25 | US$71,18 | US$61,59 | OK |
| P/OCF | Base | US$35,47 | US$39,94 | US$41,30 | US$38,90 | OK |
| P/OCF | Conservador | US$28,96 | US$29,29 | US$29,05 | US$29,10 | OK |
| P/OCF | Optimista | US$41,18 | US$51,72 | US$58,21 | US$50,37 | OK |

Múltiplos consolidados hoy: US$47,29 / US$33,87 / US$66,30 · DCF de las historias hoy: US$33,24 / US$20,80 / US$46,56 · Ponderado hoy: US$38,86 / US$26,03 / US$54,46 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para ONON la diferencia es de +42% (múltiplos por encima del DCF). Lectura del 2-oct-2026: el DCF Base de las historias da ~US$33,2 por acción y los múltiplos consolidados ~US$47 hoy, ~40% más, fuera del ±25%. Los múltiplos no se movieron para acercarlos. La diferencia es la ventaja competitiva: el justificado (C) supone que el ROE de FY+3 (~22%) dura para siempre y la historia de On (P/E de 60-96×) refleja la etapa de hipercrecimiento, mientras el DCF lleva el ROIC al costo de capital después del año 10 porque la marca tiene 16 años y no está probada. El DCF es el valor intrínseco; los múltiplos dicen cuánto pagaría el mercado si On sostuviera retornos excedentes como una marca consolidada.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$30,20 supone que los ingresos crecen 11,8% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 14,7% (−2,9 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$45,97 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,6%, WACC de los años 4-10 9,8%, ROE de FY+3 21,8% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 25,8x | 13,8x | +82% | 7,3% | 5,1% | +2,1 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 82% por encima del DCF en FY+3. |
| EV/FCFF | 34,8x | 22,5x | +52% | 6,7% | 5,1% | +1,6 pp | Revisar: el múltiplo vale 52% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 32,4x | 30,9x | +5% | 8,5% | 8,4% | +0,1 pp | Coherente con el DCF. |
| P/FCFE | 33,0x | 25,8x | +28% | 7,3% | 6,4% | +0,9 pp | Revisar: el múltiplo vale 28% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/OCF | 29,7x | 24,5x | +21% | 7,1% | 6,4% | +0,7 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$38,86 | — |
| Múltiplos Base +20% | US$42,55 | +9,5% |
| Múltiplos Base −20% | US$35,18 | −9,5% |
| Crecimiento años 2-5 +2 pp | US$40,75 | +4,9% |
| Crecimiento años 2-5 −2 pp | US$38,02 | −2,2% |
| Margen objetivo +3 pp | US$43,16 | +11,0% |
| Margen objetivo −3 pp | US$35,50 | −8,6% |
| WACC +1 pp | US$38,26 | −1,5% |
| WACC −1 pp | US$40,47 | +4,1% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Múltiplos Base +20%, Múltiplos Base −20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 20,56 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 24,24 | 25,79 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 31,45 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 26,49 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 28,92 | 34,76 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 44,02 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 26,04 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 62,59 | 32,37 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 37,69 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 25,89 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 33,88 | 32,99 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 42,29 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 24,08 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 29,69 | 29,73 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 34,57 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/ONON_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1nlN8qDy9BipM5IWwGE5Fgf6VKpyYQScLXIPvqtAE9Oo/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-10-02 (DECK, NKE, LULU, BIRK, ADDYY, CROX).
- [On, comunicado del 2T26, 11-ago-2026](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm)
- [On, Investor Day 2026, 22-sep-2026](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000021/exhibit991oninvestorday202.htm)

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
