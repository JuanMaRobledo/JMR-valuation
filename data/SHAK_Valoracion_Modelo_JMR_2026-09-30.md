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

**Valor intrínseco principal: DCF esperado de las cuatro historias, US$18,06.** Historia central A: US$20,35; rango US$7,26–US$35,75; precio con MOS 35% sobre el esperado: US$11,74; precio de referencia US$59,34. Cada historia es un DCF completo (hoja «Escenarios e historias»); el detalle está en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son la calibración técnica anterior de la hoja (Base US$20,30) y los múltiplos y el ponderado son lecturas secundarias.


| Historia | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| A · Crece por aperturas y el margen mejora | 45% | US$20,35 | US$9,16 |
| B · Crece, pero el margen no despega | 30% | US$9,40 | US$2,82 |
| C · Tesis de disrupción · Deterioro de los fundamentales: Consumidor débil y aperturas que no rinden | 10% | US$7,26 | US$0,73 |
| D · Economía unitaria de primer nivel | 15% | US$35,75 | US$5,36 |
| **DCF esperado** | 100% | **US$18,06** | |

Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$20,93 por acción y los múltiplos, US$49,99 hoy: 139% por encima del DCF, fuera del rango de ±25%. En el DCF el capex de expansión absorbe casi todo el flujo de caja, mientras los múltiplos (~18x EBITDA) aplicados al EBITDA de FY+3 se parecen al precio de mercado. Conviene revisar la reinversión (sales-to-capital) y el margen del DCF.

| Escenario | DCF técnico anterior hoy (calibración) | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$11,66 | US$30,64 | US$19,25 | US$11,74 | US$27,63 |
| Base | US$20,30 | US$49,67 | US$32,05 | US$11,74 | US$48,33 |
| Optimista | US$32,12 | US$92,84 | US$56,41 | US$11,74 | US$90,80 |

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
| Margen EBIT objetivo | 6,0% | 8,0% | 10,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,40 / 1,60 | — | Input B32/B33 |
| DCF por acción hoy | US$11,66 | US$20,30 | US$32,12 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,60, ERP 4,46%, Ke 12,13%, costo de la deuda después de impuestos 4,78%, peso del patrimonio 91,6%, WACC inicial 11,51% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: hasta 2024 la utilidad y el flujo de caja de Shake Shack eran negativos o casi cero y los múltiplos (40-680x) no son representativos. Desde 2025 el margen por restaurante subió y la utilidad es positiva; en 2026 abre 60-65 locales propios con ventas comparables de +2,5-3,0%. La etapa actual es Dec '25 y el LTM. Se excluye la columna sin fecha de la hoja. B: restaurantes de servicio rápido y casual en expansión (Chipotle, Wingstop, Texas Roadhouse, Dutch Bros), datos de yfinance al 29-sep-2026. Se excluyen Sweetgreen (margen operativo negativo) y Cava (P/E de 95x y P/FCF de 127x por su etapa de hipercrecimiento). Ajuste +10%: Shake Shack abre ~15% más locales al año, más que Chipotle, Wingstop y Texas Roadhouse, aunque con menor margen. λ = 0,10: C es inestable. El capex de expansión deja el FCFF de FY+3 en ~9% del EBITDA, lo que hunde el EV/EBITDA justificado a 2,7x y el P/OCF a 5,1x; se le da poco peso.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 19,8x | 18,2x (n=4: CMG 19,8x, WING 16,7x, TXRH 15,9x, BROS 19,6x) × 1,10 = 20,0x | 0,7x / 2,7x / 7,9x | 12,7x | **18,2x** | 30,7x | —x / 15,0x / —x |
| EV/FCFF | mediana Dec '25 (etapa actual) = 68,2x | 28,4x (n=4: CMG 28,7x, WING 24,7x, TXRH 28,0x, BROS 53,8x) × 1,10 = 31,2x | 24,7x / 28,6x / 47,1x | 44,8x | **47,6x** | 61,5x | —x / 30,0x / —x |
| P/E | mediana Dec '25, LTM (etapa actual) = 66,5x | 27,6x (n=4: CMG 29,5x, WING 25,7x, TXRH 25,2x, BROS 52,9x) × 1,10 = 30,4x | 10,4x / 12,9x / 18,6x | 39,9x | **44,9x** | 56,5x | —x / 35,0x / —x |
| P/FCFE | mediana Dec '25 (etapa actual) = 60,0x | 25,7x (n=4: CMG 25,7x, WING 23,0x, TXRH 25,8x, BROS 70,3x) × 1,10 = 28,3x | 17,7x / 19,7x / 27,1x | 40,0x | **41,7x** | 53,0x | —x / 30,0x / —x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 13,7x | 16,5x (n=4: CMG 17,3x, WING 15,6x, TXRH 12,8x, BROS 18,3x) × 1,10 = 18,1x | 3,1x / 5,1x / 10,0x | 12,2x | **14,8x** | 20,1x | —x / 12,0x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 18,2x: promedio de historia y peers 19,9x, acercado 10% al justificado (2,7x); rango de anclas 2,7x–20,0x. Atípicos excluidos de la historia: Dec '20 (682,7x: > 2,5x la mediana (41.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 47,6x: promedio de historia y peers 49,7x, acercado 10% al justificado (28,6x); rango de anclas 28,6x–68,2x. Atípicos excluidos de la historia: Dec '19 (-132,8x: métrica negativa o ~0); Dec '20 (-105,5x: métrica negativa o ~0); Dec '21 (-71,5x: métrica negativa o ~0); Dec '22 (-30,8x: métrica negativa o ~0); Dec '23 (-267,9x: métrica negativa o ~0); LTM (-242,5x: métrica negativa o ~0). La razón FCF después de intereses ÷ FCFF se fija en 1,0: el FCFF de Shake Shack es pequeño frente a sus ingresos por intereses y la razón calculada (1,37) es inestable. Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 44,9x: promedio de historia y peers 48,4x, acercado 10% al justificado (12,9x); rango de anclas 12,9x–66,5x. Atípicos excluidos de la historia: Dec '20 (-74,4x: métrica negativa o ~0); Dec '21 (-318,7x: métrica negativa o ~0); Dec '22 (-69,8x: métrica negativa o ~0); Dec '24 (574,0x: > 2,5x la mediana (98.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 41,7x: promedio de historia y peers 44,2x, acercado 10% al justificado (19,7x); rango de anclas 19,7x–60,0x. Atípicos excluidos de la historia: Dec '19 (-116,7x: métrica negativa o ~0); Dec '20 (-99,3x: métrica negativa o ~0); Dec '21 (-63,6x: métrica negativa o ~0); Dec '22 (-25,4x: métrica negativa o ~0); Dec '23 (-238,1x: métrica negativa o ~0); LTM (-198,5x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 14,8x: promedio de historia y peers 15,9x, acercado 10% al justificado (5,1x); rango de anclas 5,1x–18,1x. Atípicos excluidos de la historia: Dec '20 (84,2x: > 2,5x la mediana (23.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$49,67 frente a US$20,30 del DCF (+145%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$49,67 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$16,44 | US$28,61 | US$45,27 |
| EV/EBITDA | 10% | US$74,17 | US$124,60 | US$254,61 |
| EV/FCFF | 15% | US$8,09 | US$31,50 | US$86,13 |
| P/E | 5% | US$73,67 | US$108,75 | US$181,47 |
| P/FCFE | 5% | US$40,06 | US$72,37 | US$159,35 |
| P/OCF | 5% | US$69,02 | US$98,45 | US$164,23 |
| **Ponderado FY+3** | 100% | US$27,63 | US$48,33 | US$90,80 |

Valor presente (Ke 12,13%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$53,78 | US$53,78 | US$52,62 | US$53,39 | OK |
| EV/EBITDA | Base | US$79,82 | US$86,30 | US$88,39 | US$84,84 | OK |
| EV/EBITDA | Optimista | US$137,73 | US$164,72 | US$180,61 | US$161,02 | OK |
| EV/FCFF | Conservador | US$0,96 | US$4,72 | US$5,74 | US$3,81 | OK |
| EV/FCFF | Base | US$7,20 | US$17,02 | US$22,35 | US$15,52 | OK |
| EV/FCFF | Optimista | US$15,12 | US$45,52 | US$61,10 | US$40,58 | OK |
| P/E | Conservador | US$46,72 | US$51,12 | US$52,26 | US$50,03 | OK |
| P/E | Base | US$54,41 | US$70,14 | US$77,14 | US$67,23 | OK |
| P/E | Optimista | US$70,34 | US$107,61 | US$128,73 | US$102,23 | OK |
| P/FCFE | Conservador | US$24,45 | US$27,88 | US$28,42 | US$26,91 | OK |
| P/FCFE | Base | US$39,45 | US$46,08 | US$51,34 | US$45,62 | OK |
| P/FCFE | Optimista | US$63,37 | US$95,63 | US$113,04 | US$90,68 | OK |
| P/OCF | Conservador | US$50,69 | US$50,24 | US$48,97 | US$49,97 | OK |
| P/OCF | Base | US$66,08 | US$68,85 | US$69,84 | US$68,26 | OK |
| P/OCF | Optimista | US$93,78 | US$107,93 | US$116,50 | US$106,07 | OK |

Múltiplos consolidados hoy: US$30,64 / US$49,67 / US$92,84 · DCF hoy: US$11,66 / US$20,30 / US$32,12 · Ponderado hoy: US$19,25 / US$32,05 / US$56,41 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para SHAK la diferencia es de +145% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF técnico anterior (caso Base de la hoja) da US$20,93 por acción y los múltiplos, US$49,99 hoy: 139% por encima del DCF, fuera del rango de ±25%. En el DCF el capex de expansión absorbe casi todo el flujo de caja, mientras los múltiplos (~18x EBITDA) aplicados al EBITDA de FY+3 se parecen al precio de mercado. Conviene revisar la reinversión (sales-to-capital) y el margen del DCF.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$59,34 supone que los ingresos crecen — al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,4% (—). Ningún crecimiento entre −20% y 80% justifica el precio con estos márgenes.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$28,61 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 12,1%, WACC de los años 4-10 10,4%, ROE de FY+3 19,6% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 18,2x | 4,1x | +335% | 9,9% | 7,9% | +1,9 pp | Revisar: el múltiplo vale 335% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 47,6x | 43,1x | +10% | 8,2% | 7,9% | +0,2 pp | Coherente con el DCF. |
| P/E | 44,9x | 11,8x | +280% | 11,0% | 5,8% | +5,2 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 280% por encima del DCF en FY+3. |
| P/FCFE | 41,7x | 16,5x | +153% | 9,5% | 5,7% | +3,8 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 153% por encima del DCF en FY+3. |
| P/OCF | 14,8x | 4,3x | +244% | 10,2% | 5,7% | +4,5 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 244% por encima del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$32,05 | — |
| Múltiplos Base +20% | US$35,99 | +12,3% |
| Múltiplos Base −20% | US$28,10 | −12,3% |
| Crecimiento años 2-5 +2 pp | US$31,76 | −0,9% |
| Crecimiento años 2-5 −2 pp | US$32,32 | +0,9% |
| Margen objetivo +3 pp | US$40,69 | +27,0% |
| Margen objetivo −3 pp | US$23,40 | −27,0% |
| WACC +1 pp | US$31,19 | −2,7% |
| WACC −1 pp | US$32,97 | +2,9% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Margen objetivo −3 pp, Múltiplos Base −20%.

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
