---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Zoetis Inc."
ticker: "ZTS"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1MYnJJfv2G9R5u4roWPYb855tFs3K0Mqt2vxCPNkXKPE/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Zoetis Inc. (ZTS) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$110,65 por acción.** Complemento: DCF esperado por probabilidades US$89,35; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$43,41–US$127,93; precio con MOS 35% sobre el esperado: US$58,07; precio de referencia US$69,69. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Tropiezo temporal; vuelve a crecer con innovación** (valor principal) | 40% | US$110,65 | US$44,26 |
| Conservadora · Erosión prolongada de franquicias clave | 35% | US$61,58 | US$21,55 |
| Disrupción · Deterioro de los fundamentales: Genéricos y competencia generalizada | 10% | US$43,41 | US$4,34 |
| Optimista · Recuperación fuerte con nuevos productos | 15% | US$127,93 | US$19,19 |
| **DCF esperado (complemento)** | 100% | **US$89,35** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$117,30 por acción y los múltiplos, US$111,20 hoy: 5% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$110,65 | US$107,90 | US$109,00 | US$58,07 | US$142,69 |
| Conservador | US$61,58 | US$85,79 | US$76,11 | US$58,07 | US$96,08 |
| Optimista | US$127,93 | US$125,84 | US$126,68 | US$58,07 | US$168,40 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - ZTS](https://docs.google.com/spreadsheets/d/1MYnJJfv2G9R5u4roWPYb855tFs3K0Mqt2vxCPNkXKPE/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$69,69.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -2,0% | 2,0% | 4,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 1,0% | 5,0% | 6,7% | Input B29 |
| Margen EBIT objetivo | 33,4% | 36,4% | 38,4% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,91 / 1,91 | — | Input B32/B33 |
| DCF por acción hoy | US$61,58 | US$110,65 | US$127,93 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,11, ERP 4,09%, Ke 9,83%, costo de la deuda después de impuestos 5,12%, peso del patrimonio 80,0%, WACC inicial 8,89% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Zoetis cotizó a 18-38x EBITDA y 29-57x utilidades como líder de salud animal con crecimiento estable. En 2026 recortó dos veces su guía (ingresos de US$9.680-9.960 millones) por las dudas de seguridad de Librela, la caída de sus anticuerpos para osteoartritis canina (−24%) y menos visitas a veterinarios; la acción cae ~25% en el año. La etapa actual es Dec '25 y el LTM. B: salud animal y diagnóstico (IDEXX, Elanco, Phibro, Merck, Abbott), datos de yfinance al 29-sep-2026. Se excluye Neogen (margen casi cero), Merck en P/E (119x por cargos puntuales) y Phibro en los múltiplos de flujo libre (P/FCF de 146x por un año de capex alto). Ajuste −15%: Zoetis crece ~2-5% en 2026 (la mitad de IDEXX y Abbott) y tiene el riesgo de Librela; conserva los márgenes más altos del grupo. λ = 0,25: la Zoetis de FY+3 del escenario Base es una empresa de salud animal de crecimiento medio, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 12,0x | 14,8x (n=5: IDXX 26,5x, ELAN 14,8x, PAHC 8,8x, MRK 14,4x, ABT 17,3x) × 0,85 = 12,6x | 17,5x / 15,3x / 18,4x | **13,6x** | 12,4x | 15,2x | 9,3x / —x / —x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 19,5x (EV/FCF × 0,93 = FCF después de intereses ÷ FCFF) | 26,1x (n=4: IDXX 33,9x, ELAN 26,0x, MRK 23,8x, ABT 26,3x) × 0,85 = 22,2x | 27,8x / 23,4x / 29,8x | **22,6x** | 20,2x | 24,7x | 15,7x / —x / —x |
| P/E | mediana Dec '25, LTM (etapa actual) = 16,5x | 32,7x (n=3: IDXX 37,5x, PAHC 14,6x, ABT 32,7x) × 0,85 = 27,8x | 21,9x / 19,0x / 23,4x | **22,1x** | 18,1x | 24,1x | 12,1x / —x / —x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 17,9x | 26,7x (n=4: IDXX 34,0x, ELAN 29,8x, MRK 22,9x, ABT 23,7x) × 0,85 = 22,7x | 23,3x / 20,1x / 24,7x | **21,1x** | 18,2x | 23,6x | 12,4x / —x / —x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 14,4x | 18,5x (n=5: IDXX 30,6x, ELAN 18,3x, PAHC 20,9x, MRK 18,4x, ABT 18,5x) × 0,85 = 15,7x | 21,4x / 16,8x / 23,6x | **16,6x** | 14,7x | 18,7x | 10,2x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 13,6x: promedio de historia y peers 12,3x, acercado 25% al justificado (17,5x); rango de anclas 12,0x–17,5x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 22,6x: promedio de historia y peers 20,9x, acercado 25% al justificado (27,8x); rango de anclas 19,5x–27,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 22,1x: promedio de historia y peers 22,1x, acercado 25% al justificado (21,9x); rango de anclas 16,5x–27,8x. Atípicos excluidos de la historia: LTM (12,1x: < 0,4x la mediana (32.6x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 21,1x: promedio de historia y peers 20,3x, acercado 25% al justificado (23,3x); rango de anclas 17,9x–23,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 16,6x: promedio de historia y peers 15,0x, acercado 25% al justificado (21,4x); rango de anclas 14,4x–21,4x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$107,90 frente a US$110,65 del DCF (−2%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$107,90 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 9,83%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$43,41) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$110,65 por acción.** Complemento: DCF esperado por probabilidades US$89,35. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$110,65 | US$61,58 | US$127,93 |
| EV/EBITDA | 13,6× / 12,4× / 15,2× | 20% | 33% | US$98,24 | US$79,92 | US$117,20 |
| EV/FCFF | 22,6× / 20,2× / 24,7× | 10% | 17% | US$103,53 | US$88,04 | US$117,62 |
| P/E | 22,1× / 18,1× / 24,1× | 20% | 33% | US$118,20 | US$89,11 | US$135,82 |
| P/FCFE | 21,1× / 18,2× / 23,6× | 5% | 8% | US$116,88 | US$87,71 | US$141,92 |
| P/OCF | 16,6× / 14,7× / 18,7× | 5% | 8% | US$105,03 | US$89,60 | US$120,82 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$107,90 | US$85,79 | US$125,84 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$109,00 | US$76,11 | US$126,68 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$146,60 | US$81,59 | US$169,49 |
| EV/EBITDA (total con dividendos) | 13,6× / 12,4× / 15,2× | 20% | 33% | US$127,92 | US$98,87 | US$156,49 |
| EV/FCFF (total con dividendos) | 22,6× / 20,2× / 24,7× | 10% | 17% | US$134,11 | US$106,15 | US$157,76 |
| P/E (total con dividendos) | 22,1× / 18,1× / 24,1× | 20% | 33% | US$152,47 | US$109,74 | US$179,85 |
| P/FCFE (total con dividendos) | 21,1× / 18,2× / 23,6× | 5% | 8% | US$156,01 | US$112,83 | US$191,37 |
| P/OCF (total con dividendos) | 16,6× / 14,7× / 18,7× | 5% | 8% | US$135,27 | US$109,27 | US$159,90 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$140,09 | US$105,73 | US$167,68 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$8,59 | US$8,59 | US$8,59 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$131,50 | US$97,14 | US$159,09 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$142,69 | US$96,08 | US$168,40 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 9,83%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$99,71 | US$97,86 | US$97,15 | US$98,24 | OK |
| EV/EBITDA | Conservador | US$85,79 | US$78,75 | US$75,22 | US$79,92 | OK |
| EV/EBITDA | Optimista | US$115,38 | US$117,49 | US$118,72 | US$117,20 | OK |
| EV/FCFF | Base | US$106,06 | US$102,70 | US$101,83 | US$103,53 | OK |
| EV/FCFF | Conservador | US$97,18 | US$86,21 | US$80,72 | US$88,04 | OK |
| EV/FCFF | Optimista | US$115,05 | US$118,14 | US$119,68 | US$117,62 | OK |
| P/E | Base | US$121,08 | US$117,85 | US$115,68 | US$118,20 | OK |
| P/E | Conservador | US$95,94 | US$87,96 | US$83,43 | US$89,11 | OK |
| P/E | Optimista | US$134,88 | US$136,25 | US$136,35 | US$135,82 | OK |
| P/FCFE | Base | US$113,94 | US$118,36 | US$118,35 | US$116,88 | OK |
| P/FCFE | Conservador | US$89,68 | US$87,69 | US$85,76 | US$87,71 | OK |
| P/FCFE | Optimista | US$135,53 | US$145,18 | US$145,04 | US$141,92 | OK |
| P/OCF | Base | US$108,05 | US$104,33 | US$102,70 | US$105,03 | OK |
| P/OCF | Conservador | US$97,53 | US$88,18 | US$83,07 | US$89,60 | OK |
| P/OCF | Optimista | US$120,03 | US$121,13 | US$121,29 | US$120,82 | OK |

Múltiplos consolidados hoy: US$107,90 / US$85,79 / US$125,84 · DCF de las historias hoy: US$110,65 / US$61,58 / US$127,93 · Ponderado hoy: US$109,00 / US$76,11 / US$126,68 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para ZTS la diferencia es de −2% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$117,30 por acción y los múltiplos, US$111,20 hoy: 5% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$69,69 supone que los ingresos crecen -3,1% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 4,5% (−7,5 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$146,60 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 9,8%, WACC de los años 4-10 9,1%, ROE de FY+3 91,9% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 13,6x | 15,4x | −13% | 4,3% | 4,8% | −0,5 pp | Coherente con el DCF. |
| EV/FCFF | 22,6x | 24,5x | −9% | 4,5% | 4,8% | −0,3 pp | Coherente con el DCF. |
| P/E | 22,1x | 21,2x | +4% | 5,3% | 5,1% | +0,2 pp | Coherente con el DCF. |
| P/FCFE | 21,1x | 19,7x | +6% | 4,9% | 4,5% | +0,3 pp | Coherente con el DCF. |
| P/OCF | 16,6x | 18,1x | −8% | 4,1% | 4,5% | −0,4 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$109,00 | — |
| Múltiplos Base +20% | US$122,24 | +12,1% |
| Múltiplos Base −20% | US$95,76 | −12,1% |
| Crecimiento años 2-5 +2 pp | US$113,72 | +4,3% |
| Crecimiento años 2-5 −2 pp | US$104,69 | −4,0% |
| Margen objetivo +3 pp | US$112,98 | +3,7% |
| Margen objetivo −3 pp | US$105,02 | −3,7% |
| WACC +1 pp | US$106,21 | −2,6% |
| WACC −1 pp | US$111,99 | +2,7% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 12,39 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 9,30 | 13,62 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 15,16 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 20,23 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 15,69 | 22,57 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 24,70 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 18,06 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 12,06 | 22,08 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 24,09 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 18,18 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 12,41 | 21,06 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 23,65 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 14,66 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 10,17 | 16,62 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 18,70 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/ZTS_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1MYnJJfv2G9R5u4roWPYb855tFs3K0Mqt2vxCPNkXKPE/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (IDXX, ELAN, PAHC, MRK, NEOG, ABT).
- [Yahoo Finance: Zoetis recorta su guía por las dudas sobre Librela](https://finance.yahoo.com/news/zoetis-cuts-guidance-librela-safety-010955054.html)
- [Zacks/TradingView: Zoetis cae 24,8% en el año](https://www.tradingview.com/news/zacks:c838081a4094b:0-zoetis-stock-plummets-24-8-ytd-here-s-what-you-need-to-know/)

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
