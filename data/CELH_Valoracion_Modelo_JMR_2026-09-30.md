---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Celsius Holdings, Inc."
ticker: "CELH"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1E_s_A35yIAZRGatTIElusnMZs5NIvFJ9CUlGlqf7-j8/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Celsius Holdings, Inc. (CELH) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$24,03 por acción.** Complemento: DCF esperado por probabilidades US$20,90; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$7,06–US$32,43; precio con MOS 35% sobre el esperado: US$13,59; precio de referencia US$27,35. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$24,24), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Portafolio de tres marcas que crece con la categoría** (valor principal) | 45% | US$24,03 | US$10,81 |
| Conservadora · Alani crece, CELSIUS sigue cediendo | 25% | US$16,68 | US$4,17 |
| Disrupción · Deterioro de los fundamentales: La moda pasa y la regulación de la cafeína alcanza a Alani Nu | 15% | US$7,06 | US$1,06 |
| Optimista · Plataforma multimarca con PepsiCo y expansión internacional | 15% | US$32,43 | US$4,86 |
| **DCF esperado (complemento)** | 100% | **US$20,90** | |

Lectura del 1-oct-2026: el DCF Base de las historias da ~US$24,0 por acción y los múltiplos consolidados ~US$38 hoy, ~60% más. La diferencia es la ventaja competitiva: los múltiplos usan peers con marcas y retornos duraderos (Coca-Cola, Monster), mientras el DCF supone que Celsius no conserva retornos excedentes después del año 10. El DCF es el valor intrínseco; los múltiplos son precio relativo y dicen cuánto pagaría el mercado si Celsius se pareciera a esos peers.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$24,03 | US$43,61 | US$31,86 | US$13,59 | US$41,37 |
| Conservador | US$16,68 | US$35,59 | US$24,24 | US$13,59 | US$29,63 |
| Optimista | US$32,43 | US$53,14 | US$40,71 | US$13,59 | US$55,54 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - CELH (desde cero 2026-10-01)](https://docs.google.com/spreadsheets/d/1E_s_A35yIAZRGatTIElusnMZs5NIvFJ9CUlGlqf7-j8/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$27,35.
- Peers: datos de mercado de yfinance consultados el 2026-10-02 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 2,8% | 7,8% | 11,1% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 0,8% | 5,5% | 10,2% | Input B29 |
| Margen EBIT objetivo | 18,6% | 21,1% | 24,1% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,00 / 1,70 | — | Input B32/B33 |
| DCF por acción hoy | US$16,68 | US$24,03 | US$32,43 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,00, ERP 4,09%, Ke 9,38%, costo de la deuda después de impuestos 4,88%, peso del patrimonio 90,2%, WACC inicial 8,94% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: hasta 2023 Celsius fue una marca única en hipercrecimiento (ventas +102% en 2023, utilidades negativas en 2021-2022): sus múltiplos de 44-136× no describen a la empresa de FY+3. Desde 2024 (ventas +3%) es una marca de bebidas energéticas que madura y, desde 2025, un portafolio de tres marcas distribuido por PepsiCo. Se usa FY2024 como etapa actual. FY2025 y LTM se excluyen en todos los métodos: la utilidad y el EBITDA incluyen US$327,5 millones (2025) y US$412,8 millones (LTM) de terminación de distribuidores y otros cargos de una vez (comunicados del 4T25 y 2T26), y el flujo de caja incluye los reembolsos de PepsiCo por esas terminaciones (ingresos diferidos +US$329,6 millones LTM). Con un solo cierre representativo (FY2024), el ancla A es débil y pesa menos (ver λ). B: bebidas con marca y datos de yfinance al 1-oct-2026: Monster, Coca-Cola, PepsiCo, National Beverage y Vita Coco. Se excluye Keurig Dr Pepper: su compra de JDE Peet's (crecimiento de ingresos de 76%) distorsiona sus múltiplos. Ajuste −15%: crecimiento a FY+3 parecido a la mediana (Base ~5,5% frente a ~6-7% de Coca-Cola y PepsiCo; Monster crece más), 0%; margen operativo menor (21% objetivo frente a 29% de Monster y 35% de Coca-Cola), −5%; riesgo propio mayor (una sola categoría, un distribuidor que concentra más de 40% de las ventas, investigación del fiscal de Texas y demandas colectivas), −10%. λ = 0,5: la Celsius de FY+3 (portafolio de tres marcas, crecimiento de un dígito medio, margen ~21%) es distinta de la de FY2024 y el ancla A tiene un solo cierre. Chequeo de crecimiento implícito (1-oct-2026): con λ = 0,5 los múltiplos valen ~30-60% más que el DCF en FY+3. Se probó λ = 0,75 y la brecha creció, porque el justificado (C) supone que el retorno de FY+3 dura para siempre, mientras el DCF lleva el ROIC al costo de capital después del año 10 (sin ventaja defendible). La diferencia no es de crecimiento sino de ventaja competitiva: los peers (Coca-Cola, Monster) cotizan con retornos excedentes duraderos. Se deja λ = 0,5 y la diferencia se explica; el DCF manda.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '24 (etapa actual) = 32,6x | 22,0x (n=5: MNST 27,0x, KO 23,6x, PEP 11,3x, FIZZ 11,3x, COCO 22,0x) × 0,85 = 18,7x | 17,9x / 18,2x / 22,8x | **21,8x** | 18,4x | 24,3x | 22,8x / 18,4x / 25,9x |
| EV/FCFF | mediana Dec '24 (etapa actual) = 24,2x (EV/FCF × 1,09 = FCF después de intereses ÷ FCFF) | 24,2x (n=5: MNST 38,0x, KO 25,8x, PEP 21,0x, FIZZ 16,8x, COCO 24,2x) × 0,85 = 20,5x | 27,9x / 24,9x / 37,5x | **25,1x** | 23,1x | 28,6x | 25,1x / 23,2x / 28,5x |
| P/E | mediana Dec '24 (etapa actual) = 43,2x | 25,7x (n=5: MNST 39,8x, KO 25,7x, PEP 16,5x, FIZZ 16,3x, COCO 30,9x) × 0,85 = 21,9x | 23,6x / 20,9x / 31,1x | **28,1x** | 23,6x | 32,9x | 27,8x / 23,5x / 32,8x |
| P/FCFE | mediana Dec '24 (etapa actual) = 25,9x | 25,8x (n=5: MNST 40,4x, KO 25,8x, PEP 18,5x, FIZZ 17,5x, COCO 26,0x) × 0,85 = 21,9x | 26,1x / 23,5x / 34,4x | **25,0x** | 21,8x | 27,7x | 25,0x / 21,8x / 27,9x |
| P/OCF | mediana Dec '24 (etapa actual) = 23,5x | 22,6x (n=5: MNST 37,6x, KO 22,6x, PEP 12,8x, FIZZ 15,2x, COCO 24,6x) × 0,85 = 19,2x | 25,8x / 21,9x / 35,2x | **23,6x** | 19,8x | 27,1x | 23,6x / 19,9x / 27,2x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 21,8x: promedio de historia y peers 25,7x, acercado 50% al justificado (17,9x); rango de anclas 17,9x–32,6x. Atípicos excluidos de la historia: Dec '16 (-31,0x: métrica negativa o ~0); Dec '17 (-27,9x: métrica negativa o ~0); Dec '18 (-18,0x: métrica negativa o ~0); Dec '19 (-227,5x: métrica negativa o ~0); Dec '21 (-1.989,4x: métrica negativa o ~0); Dec '22 (-47,0x: métrica negativa o ~0); Dec '20 (418,0x: > 2,5x la mediana (44.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 25,1x: promedio de historia y peers 22,4x, acercado 50% al justificado (27,9x); rango de anclas 20,5x–27,9x. Atípicos excluidos de la historia: Dec '16 (-36,1x: métrica negativa o ~0); Dec '17 (-26,6x: métrica negativa o ~0); Dec '18 (-16,2x: métrica negativa o ~0); Dec '21 (-55,9x: métrica negativa o ~0); Dec '19 (318,5x: > 2,5x la mediana (73.4x)); Dec '20 (1.283,8x: > 2,5x la mediana (73.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 28,1x: promedio de historia y peers 32,5x, acercado 50% al justificado (23,6x); rango de anclas 21,9x–43,2x. Atípicos excluidos de la historia: Dec '18 (-15,9x: métrica negativa o ~0); Dec '22 (-41,9x: métrica negativa o ~0); Dec '20 (453,2x: > 2,5x la mediana (56.8x)); Dec '21 (1.462,3x: > 2,5x la mediana (56.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 25,0x: promedio de historia y peers 23,9x, acercado 50% al justificado (26,1x); rango de anclas 21,9x–26,1x. Atípicos excluidos de la historia: Dec '16 (-41,0x: métrica negativa o ~0); Dec '17 (-28,2x: métrica negativa o ~0); Dec '18 (-16,8x: métrica negativa o ~0); Dec '21 (-56,0x: métrica negativa o ~0); Dec '19 (332,8x: > 2,5x la mediana (79.6x)); Dec '20 (1.299,1x: > 2,5x la mediana (79.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 23,6x: promedio de historia y peers 21,4x, acercado 50% al justificado (25,8x); rango de anclas 19,2x–25,8x. Atípicos excluidos de la historia: Dec '16 (-41,0x: métrica negativa o ~0); Dec '17 (-28,6x: métrica negativa o ~0); Dec '18 (-17,1x: métrica negativa o ~0); Dec '21 (-57,8x: métrica negativa o ~0); Dec '19 (332,8x: > 2,5x la mediana (73.5x)); Dec '20 (1.069,8x: > 2,5x la mediana (73.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$43,61 frente a US$24,03 del DCF (+82%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$43,61 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Crecimiento»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,38%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$7,06) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$24,03 por acción.** Complemento: DCF esperado por probabilidades US$20,90. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$24,03 | US$16,68 | US$32,43 |
| EV/EBITDA | 21,8× / 18,4× / 24,3× | 10% | 25% | US$48,43 | US$34,67 | US$61,30 |
| EV/FCFF | 25,1× / 23,1× / 28,6× | 15% | 38% | US$34,27 | US$32,14 | US$39,78 |
| P/E | 28,1× / 23,6× / 32,9× | 5% | 13% | US$56,17 | US$41,36 | US$73,86 |
| P/FCFE | 25,0× / 21,8× / 27,7× | 5% | 13% | US$49,54 | US$40,98 | US$58,23 |
| P/OCF | 23,6× / 19,8× / 27,1× | 5% | 13% | US$43,48 | US$36,63 | US$51,11 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$43,61 | US$35,59 | US$53,14 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$31,86 | US$24,24 | US$40,71 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$31,44 | US$21,82 | US$42,44 |
| EV/EBITDA | 21,8× / 18,4× / 24,3× | 10% | 25% | US$62,90 | US$41,18 | US$85,28 |
| EV/FCFF | 25,1× / 23,1× / 28,6× | 15% | 38% | US$45,36 | US$37,51 | US$59,53 |
| P/E | 28,1× / 23,6× / 32,9× | 5% | 13% | US$72,19 | US$48,85 | US$101,55 |
| P/FCFE | 25,0× / 21,8× / 27,7× | 5% | 13% | US$59,31 | US$44,02 | US$77,07 |
| P/OCF | 23,6× / 19,8× / 27,1× | 5% | 13% | US$56,69 | US$43,00 | US$73,82 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 40% | 100% | US$56,26 | US$41,35 | US$75,20 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$41,37 | US$29,63 | US$55,54 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,38%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$48,50 | US$48,70 | US$48,07 | US$48,43 | OK |
| EV/EBITDA | Conservador | US$38,16 | US$34,37 | US$31,47 | US$34,67 | OK |
| EV/EBITDA | Optimista | US$56,31 | US$62,43 | US$65,17 | US$61,30 | OK |
| EV/FCFF | Base | US$33,80 | US$34,35 | US$34,66 | US$34,27 | OK |
| EV/FCFF | Conservador | US$36,02 | US$31,73 | US$28,67 | US$32,14 | OK |
| EV/FCFF | Optimista | US$33,15 | US$40,68 | US$45,49 | US$39,78 | OK |
| P/E | Base | US$56,94 | US$56,41 | US$55,16 | US$56,17 | OK |
| P/E | Conservador | US$45,76 | US$40,98 | US$37,33 | US$41,36 | OK |
| P/E | Optimista | US$68,88 | US$75,09 | US$77,60 | US$73,86 | OK |
| P/FCFE | Base | US$57,59 | US$45,69 | US$45,32 | US$49,54 | OK |
| P/FCFE | Conservador | US$52,33 | US$36,97 | US$33,64 | US$40,98 | OK |
| P/FCFE | Optimista | US$60,52 | US$55,29 | US$58,89 | US$58,23 | OK |
| P/OCF | Base | US$43,57 | US$43,56 | US$43,32 | US$43,48 | OK |
| P/OCF | Conservador | US$40,79 | US$36,24 | US$32,86 | US$36,63 | OK |
| P/OCF | Optimista | US$44,86 | US$52,05 | US$56,41 | US$51,11 | OK |

Múltiplos consolidados hoy: US$43,61 / US$35,59 / US$53,14 · DCF de las historias hoy: US$24,03 / US$16,68 / US$32,43 · Ponderado hoy: US$31,86 / US$24,24 / US$40,71 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para CELH la diferencia es de +82% (múltiplos por encima del DCF). Lectura del 1-oct-2026: el DCF Base de las historias da ~US$24,0 por acción y los múltiplos consolidados ~US$38 hoy, ~60% más. La diferencia es la ventaja competitiva: los múltiplos usan peers con marcas y retornos duraderos (Coca-Cola, Monster), mientras el DCF supone que Celsius no conserva retornos excedentes después del año 10. El DCF es el valor intrínseco; los múltiplos son precio relativo y dicen cuánto pagaría el mercado si Celsius se pareciera a esos peers.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$27,35 supone que los ingresos crecen 8,9% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 5,9% (+2,9 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$31,44 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,4%, WACC de los años 4-10 9,1%, ROE de FY+3 54,7% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 21,8x | 10,2x | +100% | 6,0% | 2,6% | +3,4 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 100% por encima del DCF en FY+3. |
| EV/FCFF | 25,1x | 15,8x | +44% | 5,0% | 2,6% | +2,3 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 44% por encima del DCF en FY+3. |
| P/E | 28,1x | 12,2x | +130% | 6,0% | 1,3% | +4,7 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 130% por encima del DCF en FY+3. |
| P/FCFE | 25,0x | 13,3x | +89% | 5,2% | 1,7% | +3,5 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 89% por encima del DCF en FY+3. |
| P/OCF | 23,6x | 13,1x | +80% | 5,0% | 1,7% | +3,3 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 80% por encima del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$31,86 | — |
| Múltiplos Base +20% | US$35,55 | +11,6% |
| Múltiplos Base −20% | US$28,16 | −11,6% |
| Crecimiento años 2-5 +2 pp | US$33,11 | +3,9% |
| Crecimiento años 2-5 −2 pp | US$30,71 | −3,6% |
| Margen objetivo +3 pp | US$34,25 | +7,5% |
| Margen objetivo −3 pp | US$29,46 | −7,5% |
| WACC +1 pp | US$30,95 | −2,8% |
| WACC −1 pp | US$32,83 | +3,0% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo +3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 18,36 | 18,40 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 22,78 | 21,80 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 25,87 | 24,27 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 23,19 | 23,15 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 25,14 | 25,12 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 28,54 | 28,56 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 23,51 | 23,64 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 27,80 | 28,05 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 32,83 | 32,93 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 21,81 | 21,83 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 25,04 | 25,01 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 27,88 | 27,73 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 19,94 | 19,80 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 23,55 | 23,56 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 27,22 | 27,14 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/CELH_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1E_s_A35yIAZRGatTIElusnMZs5NIvFJ9CUlGlqf7-j8/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-10-02 (MNST, KDP, KO, PEP, FIZZ, COCO).
- [Celsius Holdings, comunicado del 2T26, 6-ago-2026](https://www.sec.gov/Archives/edgar/data/1341766/000134176626000047/ex9912q2026.htm)
- [Celsius Holdings, comunicado del 4T25, 26-feb-2026](https://www.sec.gov/Archives/edgar/data/1341766/000134176626000017/ex9914q20251.htm)

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
