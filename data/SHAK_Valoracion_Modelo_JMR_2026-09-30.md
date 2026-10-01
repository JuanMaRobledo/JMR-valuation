---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Shake Shack Inc."
ticker: "SHAK"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1RcwUptYoVjCfHvdqED5wXCsjteCds61g4HMKA_T8GCM/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Shake Shack Inc. (SHAK) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$15,66 por acción.** Complemento: DCF esperado por probabilidades US$12,72; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$0,00–US$32,90; precio con MOS 35% sobre el esperado: US$8,27; precio de referencia US$59,34. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son la calibración técnica anterior de la hoja (Base técnico US$9,24) y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Crece por aperturas y el margen mejora** (valor principal) | 45% | US$15,66 | US$7,05 |
| Conservadora · Crece, pero el margen no despega | 30% | US$2,47 | US$0,74 |
| Disrupción · Deterioro de los fundamentales: Consumidor débil y aperturas que no rinden | 10% | US$0,00 | US$0,00 |
| Optimista · Economía unitaria de primer nivel | 15% | US$32,90 | US$4,94 |
| **DCF esperado (complemento)** | 100% | **US$12,72** | |

Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$20,93 por acción y los múltiplos, US$49,99 hoy: 139% por encima del DCF, fuera del rango de ±25%. En el DCF el capex de expansión absorbe casi todo el flujo de caja, mientras los múltiplos (~18x EBITDA) aplicados al EBITDA de FY+3 se parecen al precio de mercado. Conviene revisar la reinversión (sales-to-capital) y el margen del DCF.

| Escenario | DCF técnico anterior hoy (calibración) | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$9,24 | US$57,99 | US$28,74 | US$8,27 | US$41,79 |
| Conservador | US$5,71 | US$40,98 | US$19,82 | US$8,27 | US$28,21 |
| Optimista | US$31,17 | US$110,54 | US$62,92 | US$8,27 | US$100,22 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - SHAK](https://docs.google.com/spreadsheets/d/1RcwUptYoVjCfHvdqED5wXCsjteCds61g4HMKA_T8GCM/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$59,34.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 9,0% | 13,0% | 16,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 9,0% | 11,0% | 16,0% | Input B29 |
| Margen EBIT objetivo | 7,3% | 9,3% | 11,3% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,51 / 1,51 | — | Input B32/B33 |
| DCF por acción hoy | US$5,71 | US$9,24 | US$31,17 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,60, ERP 4,46%, Ke 12,13%, costo de la deuda después de impuestos 4,78%, peso del patrimonio 75,5%, WACC inicial 10,33% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: hasta 2024 la utilidad y el flujo de caja de Shake Shack eran negativos o casi cero y los múltiplos (40-680x) no son representativos. Desde 2025 el margen por restaurante subió y la utilidad es positiva; en 2026 abre 60-65 locales propios con ventas comparables de +2,5-3,0%. La etapa actual es Dec '25 y el LTM. Se excluye la columna sin fecha de la hoja. B: restaurantes de servicio rápido y casual en expansión (Chipotle, Wingstop, Texas Roadhouse, Dutch Bros), datos de yfinance al 29-sep-2026. Se excluyen Sweetgreen (margen operativo negativo) y Cava (P/E de 95x y P/FCF de 127x por su etapa de hipercrecimiento). Ajuste +10%: Shake Shack abre ~15% más locales al año, más que Chipotle, Wingstop y Texas Roadhouse, aunque con menor margen. λ = 0,10: C es inestable. El capex de expansión deja el FCFF de FY+3 en ~9% del EBITDA, lo que hunde el EV/EBITDA justificado a 2,7x y el P/OCF a 5,1x; se le da poco peso.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 19,8x | 18,2x (n=4: CMG 19,8x, WING 16,7x, TXRH 15,9x, BROS 19,6x) × 1,10 = 20,0x | 2,7x / 0,7x / 7,9x | **18,2x** | 12,7x | 30,7x | 15,0x / —x / —x |
| EV/FCFF | mediana Dec '25 (etapa actual) = 68,2x | 28,4x (n=4: CMG 28,7x, WING 24,7x, TXRH 28,0x, BROS 53,8x) × 1,10 = 31,2x | 28,6x / 24,7x / 47,1x | **47,6x** | 44,8x | 61,5x | 30,0x / —x / —x |
| P/E | mediana Dec '25, LTM (etapa actual) = 66,5x | 27,6x (n=4: CMG 29,5x, WING 25,7x, TXRH 25,2x, BROS 52,9x) × 1,10 = 30,4x | 12,9x / 10,4x / 18,6x | **44,9x** | 39,9x | 56,5x | 35,0x / —x / —x |
| P/FCFE | mediana Dec '25 (etapa actual) = 60,0x | 25,7x (n=4: CMG 25,7x, WING 23,0x, TXRH 25,8x, BROS 70,3x) × 1,10 = 28,3x | 19,7x / 17,7x / 27,1x | **41,7x** | 40,0x | 53,0x | 30,0x / —x / —x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 13,7x | 16,5x (n=4: CMG 17,3x, WING 15,6x, TXRH 12,8x, BROS 18,3x) × 1,10 = 18,1x | 5,1x / 3,1x / 10,0x | **14,8x** | 12,2x | 20,1x | 12,0x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 18,2x: promedio de historia y peers 19,9x, acercado 10% al justificado (2,7x); rango de anclas 2,7x–20,0x. Atípicos excluidos de la historia: Dec '20 (682,7x: > 2,5x la mediana (41.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 47,6x: promedio de historia y peers 49,7x, acercado 10% al justificado (28,6x); rango de anclas 28,6x–68,2x. Atípicos excluidos de la historia: Dec '19 (-132,8x: métrica negativa o ~0); Dec '20 (-105,5x: métrica negativa o ~0); Dec '21 (-71,5x: métrica negativa o ~0); Dec '22 (-30,8x: métrica negativa o ~0); Dec '23 (-267,9x: métrica negativa o ~0); LTM (-242,5x: métrica negativa o ~0). La razón FCF después de intereses ÷ FCFF se fija en 1,0: el FCFF de Shake Shack es pequeño frente a sus ingresos por intereses y la razón calculada (1,37) es inestable. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 44,9x: promedio de historia y peers 48,4x, acercado 10% al justificado (12,9x); rango de anclas 12,9x–66,5x. Atípicos excluidos de la historia: Dec '20 (-74,4x: métrica negativa o ~0); Dec '21 (-318,7x: métrica negativa o ~0); Dec '22 (-69,8x: métrica negativa o ~0); Dec '24 (574,0x: > 2,5x la mediana (98.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 41,7x: promedio de historia y peers 44,2x, acercado 10% al justificado (19,7x); rango de anclas 19,7x–60,0x. Atípicos excluidos de la historia: Dec '19 (-116,7x: métrica negativa o ~0); Dec '20 (-99,3x: métrica negativa o ~0); Dec '21 (-63,6x: métrica negativa o ~0); Dec '22 (-25,4x: métrica negativa o ~0); Dec '23 (-238,1x: métrica negativa o ~0); LTM (-198,5x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 14,8x: promedio de historia y peers 15,9x, acercado 10% al justificado (5,1x); rango de anclas 5,1x–18,1x. Atípicos excluidos de la historia: Dec '20 (84,2x: > 2,5x la mediana (23.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$57,99 frente a US$9,24 del DCF (+528%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$57,99 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$13,02 | US$8,04 | US$43,94 |
| EV/EBITDA | 10% | US$129,83 | US$82,23 | US$276,96 |
| EV/FCFF | 15% | US$40,14 | US$26,22 | US$115,76 |
| P/E | 5% | US$117,51 | US$91,80 | US$212,38 |
| P/FCFE | 5% | US$80,51 | US$58,20 | US$188,35 |
| P/OCF | 5% | US$101,35 | US$74,54 | US$175,22 |
| **Ponderado FY+3** | 100% | US$41,79 | US$28,21 | US$100,22 |

Valor presente (Ke 12,13%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$88,82 | US$91,78 | US$92,10 | US$90,90 | OK |
| EV/EBITDA | Conservador | US$60,00 | US$59,74 | US$58,34 | US$59,36 | OK |
| EV/EBITDA | Optimista | US$152,89 | US$180,22 | US$196,47 | US$176,53 | OK |
| EV/FCFF | Base | US$22,45 | US$26,19 | US$28,48 | US$25,70 | OK |
| EV/FCFF | Conservador | US$14,85 | US$18,08 | US$18,60 | US$17,18 | OK |
| EV/FCFF | Optimista | US$35,17 | US$66,04 | US$82,12 | US$61,11 | OK |
| P/E | Base | US$70,47 | US$79,62 | US$83,36 | US$77,82 | OK |
| P/E | Conservador | US$60,51 | US$64,44 | US$65,12 | US$63,36 | OK |
| P/E | Optimista | US$91,11 | US$128,96 | US$150,66 | US$123,58 | OK |
| P/FCFE | Base | US$54,40 | US$54,89 | US$57,12 | US$55,47 | OK |
| P/FCFE | Conservador | US$38,25 | US$41,20 | US$41,28 | US$40,25 | OK |
| P/FCFE | Optimista | US$82,85 | US$115,64 | US$133,61 | US$110,70 | OK |
| P/OCF | Base | US$71,39 | US$71,98 | US$71,89 | US$71,75 | OK |
| P/OCF | Conservador | US$54,89 | US$54,29 | US$52,88 | US$54,02 | OK |
| P/OCF | Optimista | US$101,17 | US$115,52 | US$124,30 | US$113,66 | OK |

Múltiplos consolidados hoy: US$57,99 / US$40,98 / US$110,54 · DCF técnico hoy: US$9,24 / US$5,71 / US$31,17 · Ponderado hoy: US$28,74 / US$19,82 / US$62,92 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para SHAK la diferencia es de +528% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$20,93 por acción y los múltiplos, US$49,99 hoy: 139% por encima del DCF, fuera del rango de ±25%. En el DCF el capex de expansión absorbe casi todo el flujo de caja, mientras los múltiplos (~18x EBITDA) aplicados al EBITDA de FY+3 se parecen al precio de mercado. Conviene revisar la reinversión (sales-to-capital) y el margen del DCF.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$59,34 supone que los ingresos crecen — al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,4% (—). Ningún crecimiento entre −20% y 80% justifica el precio con estos márgenes.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$13,02 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 12,1%, WACC de los años 4-10 10,4%, ROE de FY+3 19,6% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 18,2x | 1,6x | +897% | 9,9% | 4,4% | +5,4 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 897% por encima del DCF en FY+3. |
| EV/FCFF | 47,6x | 14,3x | +208% | 8,2% | 3,2% | +5,0 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 208% por encima del DCF en FY+3. |
| P/E | 44,9x | 5,0x | +802% | 11,0% | -20,7% | +31,8 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 802% por encima del DCF en FY+3. |
| P/FCFE | 41,7x | 6,8x | +518% | 9,5% | -2,3% | +11,8 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 518% por encima del DCF en FY+3. |
| P/OCF | 14,8x | 1,9x | +678% | 10,2% | -1,4% | +11,6 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 678% por encima del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$28,74 | — |
| Múltiplos Base +20% | US$33,32 | +15,9% |
| Múltiplos Base −20% | US$24,16 | −15,9% |
| Crecimiento años 2-5 +2 pp | US$28,61 | −0,4% |
| Crecimiento años 2-5 −2 pp | US$28,86 | +0,4% |
| Margen objetivo +3 pp | US$37,79 | +31,5% |
| Margen objetivo −3 pp | US$19,69 | −31,5% |
| WACC +1 pp | US$27,82 | −3,2% |
| WACC −1 pp | US$29,73 | +3,4% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Margen objetivo −3 pp, Múltiplos Base +20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 12,65 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 15,00 | 18,19 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 30,69 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 44,78 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 30,00 | 47,62 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 61,55 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 39,94 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 35,00 | 44,87 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 56,51 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 39,96 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 30,00 | 41,73 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 53,00 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 12,15 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 12,00 | 14,83 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 20,09 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/SHAK_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1RcwUptYoVjCfHvdqED5wXCsjteCds61g4HMKA_T8GCM/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (CMG, CAVA, WING, TXRH, BROS, SG).
- [Shake Shack: carta a los accionistas del 2T26](https://www.sec.gov/Archives/edgar/data/0001620533/000162053326000033/a2q26shareholderletter.htm)
- [TipRanks: Shake Shack baja su guía 2026](https://www.tipranks.com/news/company-announcements/shake-shack-lowers-2026-outlook-amid-softer-guidance)

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
