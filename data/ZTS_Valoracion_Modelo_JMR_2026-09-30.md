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

**Valor intrínseco principal · DCF Base hoy: US$112,58 por acción.** Complemento: DCF esperado por probabilidades US$89,61; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$42,64–US$129,93; precio con MOS 35% sobre el esperado: US$58,25; precio de referencia US$71,64. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Tropiezo temporal; vuelve a crecer con innovación** (valor principal) | 40% | US$112,58 | US$45,03 |
| Conservadora · Erosión prolongada de franquicias clave | 35% | US$59,51 | US$20,83 |
| Disrupción · Deterioro de los fundamentales: Genéricos y competencia generalizada | 10% | US$42,64 | US$4,26 |
| Optimista · Recuperación fuerte con nuevos productos | 15% | US$129,93 | US$19,49 |
| **DCF esperado (complemento)** | 100% | **US$89,61** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$117,30 por acción y los múltiplos, US$111,20 hoy: 5% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$112,58 | US$100,91 | US$105,58 | US$58,25 | US$140,28 |
| Conservador | US$59,51 | US$82,02 | US$73,02 | US$58,25 | US$93,22 |
| Optimista | US$129,93 | US$116,42 | US$121,82 | US$58,25 | US$164,43 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - ZTS](https://docs.google.com/spreadsheets/d/1MYnJJfv2G9R5u4roWPYb855tFs3K0Mqt2vxCPNkXKPE/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$71,64.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -2,0% | 2,0% | 4,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 1,0% | 5,0% | 6,7% | Input B29 |
| Margen EBIT objetivo | 33,4% | 36,4% | 38,4% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 1,11 / 1,11 | — | Input B32/B33 |
| DCF por acción hoy | US$59,51 | US$112,58 | US$129,93 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,11, ERP 4,68%, Ke 10,48%, costo de la deuda después de impuestos 5,12%, peso del patrimonio 80,1%, WACC inicial 9,42% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Zoetis cotizó a 18-38x EBITDA y 29-57x utilidades como líder de salud animal con crecimiento estable. En 2026 recortó dos veces su guía (ingresos de US$9.680-9.960 millones) por las dudas de seguridad de Librela, la caída de sus anticuerpos para osteoartritis canina (−24%) y menos visitas a veterinarios; la acción cae ~25% en el año. La etapa actual es Dec '25 y el LTM. B: salud animal y diagnóstico (IDEXX, Elanco, Phibro, Merck, Abbott), datos de yfinance al 29-sep-2026. Se excluye Neogen (margen casi cero), Merck en P/E (119x por cargos puntuales) y Phibro en los múltiplos de flujo libre (P/FCF de 146x por un año de capex alto). Ajuste −15%: Zoetis crece ~2-5% en 2026 (la mitad de IDEXX y Abbott) y tiene el riesgo de Librela; conserva los márgenes más altos del grupo. λ = 0,25: la Zoetis de FY+3 del escenario Base es una empresa de salud animal de crecimiento medio, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 12,0x | 14,8x (n=5: IDXX 26,5x, ELAN 14,8x, PAHC 8,8x, MRK 14,4x, ABT 17,3x) × 0,85 = 12,6x | 15,6x / 14,2x / 16,1x | **13,1x** | 12,1x | 14,5x | 9,3x / —x / —x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 19,5x (EV/FCF × 0,93 = FCF después de intereses ÷ FCFF) | 26,1x (n=4: IDXX 33,9x, ELAN 26,0x, MRK 23,8x, ABT 26,3x) × 0,85 = 22,2x | 26,8x / 22,8x / 28,8x | **22,3x** | 20,1x | 24,4x | 15,7x / —x / —x |
| P/E | mediana Dec '25, LTM (etapa actual) = 16,5x | 32,7x (n=3: IDXX 37,5x, PAHC 14,6x, ABT 32,7x) × 0,85 = 27,8x | 19,2x / 16,8x / 20,2x | **21,4x** | 17,6x | 23,3x | 12,1x / —x / —x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 17,9x | 26,7x (n=4: IDXX 34,0x, ELAN 29,8x, MRK 22,9x, ABT 23,7x) × 0,85 = 22,7x | 20,3x / 17,9x / 21,4x | **20,3x** | 17,6x | 22,8x | 12,4x / —x / —x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 14,4x | 18,5x (n=5: IDXX 30,6x, ELAN 18,3x, PAHC 20,9x, MRK 18,4x, ABT 18,5x) × 0,85 = 15,7x | 18,6x / 14,8x / 20,4x | **15,9x** | 14,1x | 17,9x | 10,2x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 13,1x: promedio de historia y peers 12,3x, acercado 25% al justificado (15,6x); rango de anclas 12,0x–15,6x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 22,3x: promedio de historia y peers 20,9x, acercado 25% al justificado (26,8x); rango de anclas 19,5x–26,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 21,4x: promedio de historia y peers 22,1x, acercado 25% al justificado (19,2x); rango de anclas 16,5x–27,8x. Atípicos excluidos de la historia: LTM (12,1x: < 0,4x la mediana (32.6x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 20,3x: promedio de historia y peers 20,3x, acercado 25% al justificado (20,3x); rango de anclas 17,9x–22,7x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 15,9x: promedio de historia y peers 15,0x, acercado 25% al justificado (18,6x); rango de anclas 14,4x–18,6x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$100,91 frente a US$112,58 del DCF (−10%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$100,91 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,48%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$42,64) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$112,58 por acción.** Complemento: DCF esperado por probabilidades US$89,61. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$112,58 | US$59,51 | US$129,93 |
| EV/EBITDA | 13,1× / 12,1× / 14,5× | 20% | 33% | US$93,35 | US$77,09 | US$110,62 |
| EV/FCFF | 22,3× / 20,1× / 24,4× | 10% | 17% | US$93,15 | US$83,44 | US$102,85 |
| P/E | 21,4× / 17,6× / 23,3× | 20% | 33% | US$113,28 | US$85,93 | US$129,82 |
| P/FCFE | 20,3× / 17,6× / 22,8× | 5% | 8% | US$104,30 | US$81,89 | US$123,99 |
| P/OCF | 15,9× / 14,1× / 17,9× | 5% | 8% | US$93,85 | US$83,45 | US$105,57 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$100,91 | US$82,02 | US$116,42 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$105,58 | US$73,02 | US$121,82 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$151,84 | US$80,26 | US$175,23 |
| EV/EBITDA (total con dividendos) | 13,1× / 12,1× / 14,5× | 20% | 33% | US$123,11 | US$96,53 | US$149,64 |
| EV/FCFF (total con dividendos) | 22,3× / 20,1× / 24,4× | 10% | 17% | US$121,86 | US$100,20 | US$140,21 |
| P/E (total con dividendos) | 21,4× / 17,6× / 23,3× | 20% | 33% | US$147,91 | US$107,11 | US$174,02 |
| P/FCFE (total con dividendos) | 20,3× / 17,6× / 22,8× | 5% | 8% | US$141,01 | US$105,46 | US$169,91 |
| P/OCF (total con dividendos) | 15,9× / 14,1× / 17,9× | 5% | 8% | US$122,17 | US$101,96 | US$141,75 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$132,58 | US$101,86 | US$157,23 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$8,59 | US$8,59 | US$8,59 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$123,99 | US$93,27 | US$148,63 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$140,28 | US$93,22 | US$164,43 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,48%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$95,16 | US$92,98 | US$91,91 | US$93,35 | OK |
| EV/EBITDA | Conservador | US$83,13 | US$75,93 | US$72,20 | US$77,09 | OK |
| EV/EBITDA | Optimista | US$109,38 | US$110,90 | US$111,58 | US$110,62 | OK |
| EV/FCFF | Base | US$96,48 | US$91,99 | US$90,98 | US$93,15 | OK |
| EV/FCFF | Conservador | US$94,13 | US$81,28 | US$74,92 | US$83,44 | OK |
| EV/FCFF | Optimista | US$100,59 | US$103,36 | US$104,59 | US$102,85 | OK |
| P/E | Base | US$116,62 | US$112,92 | US$110,30 | US$113,28 | OK |
| P/E | Conservador | US$92,95 | US$84,79 | US$80,04 | US$85,93 | OK |
| P/E | Optimista | US$129,59 | US$130,23 | US$129,66 | US$129,82 | OK |
| P/FCFE | Base | US$102,32 | US$105,40 | US$105,18 | US$104,30 | OK |
| P/FCFE | Conservador | US$85,30 | US$81,56 | US$78,82 | US$81,89 | OK |
| P/FCFE | Optimista | US$118,25 | US$127,11 | US$126,61 | US$123,99 | OK |
| P/OCF | Base | US$97,40 | US$92,93 | US$91,22 | US$93,85 | OK |
| P/OCF | Conservador | US$92,29 | US$81,83 | US$76,23 | US$83,45 | OK |
| P/OCF | Optimista | US$105,12 | US$105,87 | US$105,73 | US$105,57 | OK |

Múltiplos consolidados hoy: US$100,91 / US$82,02 / US$116,42 · DCF de las historias hoy: US$112,58 / US$59,51 / US$129,93 · Ponderado hoy: US$105,58 / US$73,02 / US$121,82 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para ZTS la diferencia es de −10% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$117,30 por acción y los múltiplos, US$111,20 hoy: 5% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$71,64 supone que los ingresos crecen -3,4% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 4,5% (−7,8 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$151,84 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,5%, WACC de los años 4-10 9,2%, ROE de FY+3 91,9% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 13,1x | 16,0x | −19% | 4,6% | 5,4% | −0,8 pp | Coherente con el DCF. |
| EV/FCFF | 22,3x | 27,4x | −20% | 4,6% | 5,4% | −0,8 pp | Coherente con el DCF. |
| P/E | 21,4x | 22,0x | −3% | 5,8% | 6,0% | −0,1 pp | Coherente con el DCF. |
| P/FCFE | 20,3x | 22,0x | −7% | 5,3% | 5,7% | −0,4 pp | Coherente con el DCF. |
| P/OCF | 15,9x | 20,1x | −20% | 4,5% | 5,7% | −1,2 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$105,58 | — |
| Múltiplos Base +20% | US$117,98 | +11,7% |
| Múltiplos Base −20% | US$93,18 | −11,7% |
| Crecimiento años 2-5 +2 pp | US$110,12 | +4,3% |
| Crecimiento años 2-5 −2 pp | US$101,45 | −3,9% |
| Margen objetivo +3 pp | US$109,74 | +3,9% |
| Margen objetivo −3 pp | US$101,43 | −3,9% |
| WACC +1 pp | US$102,72 | −2,7% |
| WACC −1 pp | US$108,65 | +2,9% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 12,12 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 9,30 | 13,14 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 14,53 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 20,05 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 15,69 | 22,34 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 24,43 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 17,59 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 12,06 | 21,38 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 23,27 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 17,65 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 12,41 | 20,32 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 22,77 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 14,10 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 10,17 | 15,91 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 17,88 | Múltiplo optimista elegido con el protocolo v3 |
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
