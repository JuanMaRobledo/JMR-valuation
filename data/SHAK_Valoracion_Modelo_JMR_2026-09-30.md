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

**Valor intrínseco principal · DCF Base hoy: US$18,09 por acción.** Complemento: DCF esperado por probabilidades US$14,73; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$0,00–US$36,90; precio con MOS 35% sobre el esperado: US$9,57; precio de referencia US$60,98. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Crece por aperturas y el margen mejora** (valor principal) | 45% | US$18,09 | US$8,14 |
| Conservadora · Crece, pero el margen no despega | 30% | US$3,51 | US$1,05 |
| Disrupción · Deterioro de los fundamentales: Consumidor débil y aperturas que no rinden | 10% | US$0,00 | US$0,00 |
| Optimista · Economía unitaria de primer nivel | 15% | US$36,90 | US$5,53 |
| **DCF esperado (complemento)** | 100% | **US$14,73** | |

Lectura del 3-oct-2026: EV/FCFF y P/FCFE no aplican (FCFF y FCFE proyectados negativos) y su peso pasa a EV/EBITDA, P/E y P/OCF. Los múltiplos aplicables quedan muy por encima del DCF y la brecha no es un error de cálculo: A es el múltiplo de la propia acción desde 2025 (historia corta, casi el precio de mercado) y B son peers con ROIC de 20-40%, mientras el ROIC de Shake Shack con arrendamientos es ~5% y en el DCF el crecimiento apenas crea valor (ROIC terminal = costo de capital). El DCF es el método más confiable para esta empresa; los múltiplos dicen cuánto paga hoy el mercado por restaurantes en expansión. Pendiente del analista (paso 6.5): ajustar la mediana de peers por margen y ROIC (hoy solo se ajusta +10% por crecimiento) o subir λ; no se movió para acercarlo al DCF.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$18,09 | US$90,03 | US$46,87 | US$9,57 | US$68,44 |
| Conservador | US$3,51 | US$72,73 | US$31,20 | US$9,57 | US$41,97 |
| Optimista | US$36,90 | US$113,41 | US$67,51 | US$9,57 | US$102,69 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - SHAK](https://docs.google.com/spreadsheets/d/1RcwUptYoVjCfHvdqED5wXCsjteCds61g4HMKA_T8GCM/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$60,98.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 9,9% | 13,0% | 15,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 8,0% | 11,0% | 14,0% | Input B29 |
| Margen EBIT objetivo | 6,5% | 9,5% | 12,5% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,51 / 1,51 | — | Input B32/B33 |
| DCF por acción hoy | US$3,51 | US$18,09 | US$36,90 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,25, ERP 4,46%, Ke 10,56%, costo de la deuda después de impuestos 4,78%, peso del patrimonio 74,6%, WACC inicial 9,10% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: hasta 2024 la utilidad y el flujo de caja de Shake Shack eran negativos o casi cero y los múltiplos (40-680x) no son representativos. Desde 2025 el margen por restaurante subió y la utilidad es positiva; en 2026 abre 60-65 locales propios con ventas comparables de +2,5-3,0%. La etapa actual es Dec '25 y el LTM. Se excluye la columna sin fecha de la hoja. B: restaurantes de servicio rápido y casual en expansión (Chipotle, Wingstop, Texas Roadhouse, Dutch Bros), datos de yfinance al 29-sep-2026. Se excluyen Sweetgreen (margen operativo negativo) y Cava (P/E de 95x y P/FCF de 127x por su etapa de hipercrecimiento). Ajuste +10%: Shake Shack abre ~15% más locales al año, más que Chipotle, Wingstop y Texas Roadhouse, aunque con menor margen. λ = 0,10 en P/E y P/OCF: C es inestable porque el capex de expansión deja el FCFF y el FCFE de FY+3 casi en cero; en EV/EBITDA el justificado es negativo (FCFF de FY+3 < 0), no se puede calcular y λ no aplica (Base = promedio de A y B).

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 19,9x | 18,2x (n=4: CMG 19,8x, WING 16,7x, TXRH 15,9x, BROS 19,6x) × 1,10 = 20,0x | -3,0x / 0,4x / -3,8x | **20,0x** | 18,4x | 21,5x | 15,0x / —x / —x |
| EV/FCFF | No aplica: No aplica (paso 6.1): con el DCF vigente (arrendamientos capitalizados y ventas/capital 1,51 desde el 1-oct-2026) el FCFF proyectado es negativo en FY+1, FY+2 y FY+3 en los tres casos (Base −71, −49 y −30 millones). Un múltiplo sobre un flujo negativo da precios negativos; peso 0 y su peso se reparte entre los múltiplos aplicables. | | | | | | |
| P/E | mediana Dec '25, LTM (etapa actual) = 66,5x | 27,6x (n=4: CMG 29,5x, WING 25,7x, TXRH 25,2x, BROS 52,9x) × 1,10 = 30,4x | 18,1x / 13,7x / 22,2x | **45,4x** | 39,7x | 54,0x | 35,0x / —x / —x |
| P/FCFE | No aplica: No aplica (paso 6.1): el FCFE proyectado del caso Base es negativo en FY+1 (−11 millones) y ~0 en FY+2, y el del Optimista es negativo en FY+1 y FY+2; la métrica no es positiva ni representativa en FY+1-FY+3. Peso 0 y su peso se reparte entre los múltiplos aplicables. | | | | | | |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 13,7x | 16,5x (n=4: CMG 17,3x, WING 15,6x, TXRH 12,8x, BROS 18,3x) × 1,10 = 18,1x | 2,6x / 3,0x / 3,7x | **14,6x** | 14,1x | 17,4x | 12,0x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 20,0x: promedio de historia y peers 20,0x, acercado 10% al justificado (-3,0x); rango de anclas 19,9x–20,0x. Atípicos excluidos de la historia: Dec '20 (675,1x: > 2,5x la mediana (41.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 45,4x: promedio de historia y peers 48,4x, acercado 10% al justificado (18,1x); rango de anclas 18,1x–66,5x. Atípicos excluidos de la historia: Dec '20 (-74,4x: métrica negativa o ~0); Dec '21 (-318,7x: métrica negativa o ~0); Dec '22 (-69,8x: métrica negativa o ~0); Dec '24 (550,1x: > 2,5x la mediana (98.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 14,6x: promedio de historia y peers 15,9x, acercado 10% al justificado (2,6x); rango de anclas 2,6x–18,1x. Atípicos excluidos de la historia: Dec '20 (84,2x: > 2,5x la mediana (23.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$90,03 frente a US$18,09 del DCF (+398%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$90,03 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Crecimiento»: DCF 60% y múltiplos 40% (EV/EBITDA 20%, P/E 10%, P/OCF 10%). Sin peso (no aplica): EV/FCFF, P/FCFE. Costo del patrimonio (Ke) 10,56%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$0,00) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$18,09 por acción.** Complemento: DCF esperado por probabilidades US$14,73. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$18,09 | US$3,51 | US$36,90 |
| EV/EBITDA | 20,0× / 18,4× / 21,5× | 20% | 50% | US$103,30 | US$80,81 | US$125,52 |
| EV/FCFF | 47,6× / 44,8× / 61,5× | 0% | 0% | US$-57,77 | US$-20,77 | US$-89,40 |
| P/E | 45,4× / 39,7× / 54,0× | 10% | 25% | US$96,74 | US$68,20 | US$136,27 |
| P/FCFE | 41,7× / 40,0× / 53,0× | 0% | 0% | US$4,71 | US$24,24 | US$-0,17 |
| P/OCF | 14,6× / 14,1× / 17,4× | 10% | 25% | US$56,78 | US$61,10 | US$66,35 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$90,03 | US$72,73 | US$113,41 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$46,87 | US$31,20 | US$67,51 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$24,45 | US$4,74 | US$49,87 |
| EV/EBITDA | 20,0× / 18,4× / 21,5× | 20% | 50% | US$150,73 | US$107,26 | US$194,66 |
| EV/FCFF | 47,6× / 44,8× / 61,5× | 0% | 0% | US$-45,80 | US$-10,45 | US$-62,32 |
| P/E | 45,4× / 39,7× / 54,0× | 10% | 25% | US$148,66 | US$91,45 | US$227,85 |
| P/FCFE | 41,7× / 40,0× / 53,0× | 0% | 0% | US$26,17 | US$36,21 | US$43,91 |
| P/OCF | 14,6× / 14,1× / 17,4× | 10% | 25% | US$87,58 | US$85,21 | US$110,49 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 40% | 100% | US$134,42 | US$97,80 | US$181,91 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$68,44 | US$41,97 | US$102,69 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,56%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$93,03 | US$105,36 | US$111,52 | US$103,30 | OK |
| EV/EBITDA | Conservador | US$81,80 | US$81,28 | US$79,36 | US$80,81 | OK |
| EV/EBITDA | Optimista | US$103,26 | US$129,28 | US$144,02 | US$125,52 | OK |
| EV/FCFF | Base | US$-84,25 | US$-55,16 | US$-33,89 | US$-57,77 | n/a (≤ 0) |
| EV/FCFF | Conservador | US$-34,41 | US$-20,17 | US$-7,73 | US$-20,77 | n/a (≤ 0) |
| EV/FCFF | Optimista | US$-138,76 | US$-83,33 | US$-46,11 | US$-89,40 | n/a (≤ 0) |
| P/E | Base | US$80,15 | US$100,08 | US$109,99 | US$96,74 | OK |
| P/E | Conservador | US$68,15 | US$68,79 | US$67,66 | US$68,20 | OK |
| P/E | Optimista | US$96,98 | US$143,24 | US$168,58 | US$136,27 | OK |
| P/FCFE | Base | US$-7,57 | US$2,33 | US$19,36 | US$4,71 | OK |
| P/FCFE | Conservador | US$26,66 | US$19,27 | US$26,79 | US$24,24 | OK |
| P/FCFE | Optimista | US$-32,58 | US$-0,41 | US$32,49 | US$-0,17 | OK |
| P/OCF | Base | US$47,64 | US$57,91 | US$64,80 | US$56,78 | OK |
| P/OCF | Conservador | US$58,78 | US$61,47 | US$63,05 | US$61,10 | OK |
| P/OCF | Optimista | US$48,73 | US$68,57 | US$81,75 | US$66,35 | OK |

Múltiplos consolidados hoy: US$90,03 / US$72,73 / US$113,41 · DCF de las historias hoy: US$18,09 / US$3,51 / US$36,90 · Ponderado hoy: US$46,87 / US$31,20 / US$67,51 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para SHAK la diferencia es de +398% (múltiplos por encima del DCF). Lectura del 3-oct-2026: EV/FCFF y P/FCFE no aplican (FCFF y FCFE proyectados negativos) y su peso pasa a EV/EBITDA, P/E y P/OCF. Los múltiplos aplicables quedan muy por encima del DCF y la brecha no es un error de cálculo: A es el múltiplo de la propia acción desde 2025 (historia corta, casi el precio de mercado) y B son peers con ROIC de 20-40%, mientras el ROIC de Shake Shack con arrendamientos es ~5% y en el DCF el crecimiento apenas crea valor (ROIC terminal = costo de capital). El DCF es el método más confiable para esta empresa; los múltiplos dicen cuánto paga hoy el mercado por restaurantes en expansión. Pendiente del analista (paso 6.5): ajustar la mediana de peers por margen y ROIC (hoy solo se ajusta +10% por crecimiento) o subir λ; no se movió para acercarlo al DCF.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$60,98 supone que los ingresos crecen 45,2% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,0% (+34,2 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$24,45 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,6%, WACC de los años 4-10 9,1%, ROE de FY+3 24,0% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 20,0x | 2,8x | +516% | — | — | — | Revisar: el múltiplo vale 516% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 47,6x | — | — | — | — | — | No aplica: No aplica (paso 6.1): con el DCF vigente (arrendamientos capitalizados y ventas/capital 1,51 desde el 1-oct-2026) el FCF |
| P/E | 45,4x | 7,5x | +508% | 9,1% | -4,7% | +13,8 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 508% por encima del DCF en FY+3. |
| P/FCFE | 41,7x | — | — | — | — | — | No aplica: No aplica (paso 6.1): el FCFE proyectado del caso Base es negativo en FY+1 (−11 millones) y ~0 en FY+2, y el del Optimis |
| P/OCF | 14,6x | 4,1x | +258% | 9,8% | 7,8% | +2,0 pp | Revisar: el múltiplo vale 258% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$46,87 | — |
| Múltiplos Base +20% | US$54,54 | +16,4% |
| Múltiplos Base −20% | US$39,19 | −16,4% |
| Crecimiento años 2-5 +2 pp | US$47,32 | +1,0% |
| Crecimiento años 2-5 −2 pp | US$46,45 | −0,9% |
| Margen objetivo +3 pp | US$56,70 | +21,0% |
| Margen objetivo −3 pp | US$37,03 | −21,0% |
| WACC +1 pp | US$45,59 | −2,7% |
| WACC −1 pp | US$48,25 | +2,9% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Margen objetivo −3 pp, Múltiplos Base −20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 18,35 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 15,00 | 19,97 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 21,51 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 39,66 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 35,00 | 45,39 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 53,95 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 14,13 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 12,00 | 14,57 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 17,35 | Múltiplo optimista elegido con el protocolo v3 |
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
