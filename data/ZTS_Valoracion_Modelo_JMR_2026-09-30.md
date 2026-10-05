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

**Valor intrínseco principal · DCF Base hoy: US$101,03 por acción.** Complemento: DCF esperado por probabilidades US$81,55; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$40,19–US$116,63; precio con MOS 35% sobre el esperado: US$53,00; precio de referencia US$69,83. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Tropiezo temporal; vuelve a crecer con innovación** (valor principal) | 40% | US$101,03 | US$40,41 |
| Conservadora · Erosión prolongada de franquicias clave | 35% | US$56,06 | US$19,62 |
| Disrupción · Deterioro de los fundamentales: Genéricos y competencia generalizada | 10% | US$40,19 | US$4,02 |
| Optimista · Recuperación fuerte con nuevos productos | 15% | US$116,63 | US$17,49 |
| **DCF esperado (complemento)** | 100% | **US$81,55** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$117,30 por acción y los múltiplos, US$111,20 hoy: 5% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$101,03 | US$97,92 | US$99,16 | US$53,00 | US$132,97 |
| Conservador | US$56,06 | US$79,85 | US$70,33 | US$53,00 | US$90,58 |
| Optimista | US$116,63 | US$112,78 | US$114,32 | US$53,00 | US$155,81 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - ZTS](https://docs.google.com/spreadsheets/d/1MYnJJfv2G9R5u4roWPYb855tFs3K0Mqt2vxCPNkXKPE/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$69,83.
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
| DCF por acción hoy | US$56,06 | US$101,03 | US$116,63 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,11, ERP 5,07%, Ke 10,92%, costo de la deuda después de impuestos 5,12%, peso del patrimonio 80,1%, WACC inicial 9,76% y terminal 9,38%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Zoetis cotizó a 18-38x EBITDA y 29-57x utilidades como líder de salud animal con crecimiento estable. En 2026 recortó dos veces su guía (ingresos de US$9.680-9.960 millones) por las dudas de seguridad de Librela, la caída de sus anticuerpos para osteoartritis canina (−24%) y menos visitas a veterinarios; la acción cae ~25% en el año. La etapa actual es Dec '25 y el LTM. B: salud animal y diagnóstico (IDEXX, Elanco, Phibro, Merck, Abbott), datos de yfinance al 29-sep-2026. Se excluye Neogen (margen casi cero), Merck en P/E (119x por cargos puntuales) y Phibro en los múltiplos de flujo libre (P/FCF de 146x por un año de capex alto). Ajuste −15%: Zoetis crece ~2-5% en 2026 (la mitad de IDEXX y Abbott) y tiene el riesgo de Librela; conserva los márgenes más altos del grupo. λ = 0,25: la Zoetis de FY+3 del escenario Base es una empresa de salud animal de crecimiento medio, parecida a la de hoy.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 12,0x | 14,8x (n=5: IDXX 26,5x, ELAN 14,8x, PAHC 8,8x, MRK 14,4x, ABT 17,3x) × 0,85 = 12,6x | 14,3x / 13,2x / 14,6x | **12,8x** | 11,9x | 14,1x | 9,3x / —x / —x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 19,5x (EV/FCF × 0,93 = FCF después de intereses ÷ FCFF) | 26,1x (n=4: IDXX 33,9x, ELAN 26,0x, MRK 23,8x, ABT 26,3x) × 0,85 = 22,2x | 24,5x / 21,1x / 26,1x | **21,8x** | 19,6x | 23,8x | 15,7x / —x / —x |
| P/E | mediana Dec '25, LTM (etapa actual) = 16,5x | 32,7x (n=3: IDXX 37,5x, PAHC 14,6x, ABT 32,7x) × 0,85 = 27,8x | 17,7x / 15,7x / 18,6x | **21,0x** | 17,3x | 22,8x | 12,1x / —x / —x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 17,9x | 26,7x (n=4: IDXX 34,0x, ELAN 29,8x, MRK 22,9x, ABT 23,7x) × 0,85 = 22,7x | 18,8x / 16,7x / 19,7x | **19,9x** | 17,4x | 22,3x | 12,4x / —x / —x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 14,4x | 18,5x (n=5: IDXX 30,6x, ELAN 18,3x, PAHC 20,9x, MRK 18,4x, ABT 18,5x) × 0,85 = 15,7x | 17,1x / 13,8x / 18,8x | **15,6x** | 13,8x | 17,4x | 10,2x / —x / —x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 12,8x: promedio de historia y peers 12,3x, acercado 25% al justificado (14,3x); rango de anclas 12,0x–14,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 21,8x: promedio de historia y peers 20,9x, acercado 25% al justificado (24,5x); rango de anclas 19,5x–24,5x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 21,0x: promedio de historia y peers 22,1x, acercado 25% al justificado (17,7x); rango de anclas 16,5x–27,8x. Atípicos excluidos de la historia: LTM (12,1x: < 0,4x la mediana (32.6x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 19,9x: promedio de historia y peers 20,3x, acercado 25% al justificado (18,8x); rango de anclas 17,9x–22,7x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 15,6x: promedio de historia y peers 15,0x, acercado 25% al justificado (17,1x); rango de anclas 14,4x–17,1x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$97,92 frente a US$101,03 del DCF (−3%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$97,92 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Madura»: DCF 40% y múltiplos 60% (EV/EBITDA 20%, EV/FCFF 10%, P/E 20%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,92%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$40,19) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$101,03 por acción.** Complemento: DCF esperado por probabilidades US$81,55. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$101,03 | US$56,06 | US$116,63 |
| EV/EBITDA | 12,8× / 11,9× / 14,1× | 20% | 33% | US$90,08 | US$74,67 | US$106,57 |
| EV/FCFF | 21,8× / 19,6× / 23,8× | 10% | 17% | US$89,85 | US$80,85 | US$99,00 |
| P/E | 21,0× / 17,3× / 22,8× | 20% | 33% | US$110,55 | US$84,14 | US$126,53 |
| P/FCFE | 19,9× / 17,4× / 22,3× | 5% | 8% | US$101,60 | US$80,02 | US$120,63 |
| P/OCF | 15,6× / 13,8× / 17,4× | 5% | 8% | US$91,19 | US$81,28 | US$102,35 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$97,92 | US$79,85 | US$112,78 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$99,16 | US$70,33 | US$114,32 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$137,87 | US$76,49 | US$159,15 |
| EV/EBITDA (total con dividendos) | 12,8× / 11,9× / 14,1× | 20% | 33% | US$119,81 | US$94,27 | US$145,39 |
| EV/FCFF (total con dividendos) | 21,8× / 19,6× / 23,8× | 10% | 17% | US$118,54 | US$97,87 | US$136,14 |
| P/E (total con dividendos) | 21,0× / 17,3× / 22,8× | 20% | 33% | US$145,50 | US$105,71 | US$170,96 |
| P/FCFE (total con dividendos) | 19,9× / 17,4× / 22,3× | 5% | 8% | US$138,47 | US$103,87 | US$166,65 |
| P/OCF (total con dividendos) | 15,6× / 13,8× / 17,4× | 5% | 8% | US$119,68 | US$100,11 | US$138,55 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$129,70 | US$99,97 | US$153,57 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$8,59 | US$8,59 | US$8,59 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$121,11 | US$91,38 | US$144,98 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$132,97 | US$90,58 | US$155,81 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,92%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$92,07 | US$89,71 | US$88,44 | US$90,08 | OK |
| EV/EBITDA | Conservador | US$80,75 | US$73,53 | US$69,73 | US$74,67 | OK |
| EV/EBITDA | Optimista | US$105,67 | US$106,84 | US$107,19 | US$106,57 | OK |
| EV/FCFF | Base | US$93,32 | US$88,72 | US$87,51 | US$89,85 | OK |
| EV/FCFF | Conservador | US$91,47 | US$78,72 | US$72,37 | US$80,85 | OK |
| EV/FCFF | Optimista | US$97,09 | US$99,50 | US$100,41 | US$99,00 | OK |
| P/E | Base | US$114,19 | US$110,19 | US$107,27 | US$110,55 | OK |
| P/E | Conservador | US$91,30 | US$83,01 | US$78,11 | US$84,14 | OK |
| P/E | Optimista | US$126,74 | US$126,92 | US$125,93 | US$126,53 | OK |
| P/FCFE | Base | US$100,01 | US$102,67 | US$102,12 | US$101,60 | OK |
| P/FCFE | Conservador | US$83,61 | US$79,67 | US$76,76 | US$80,02 | OK |
| P/FCFE | Optimista | US$115,46 | US$123,67 | US$122,77 | US$120,63 | OK |
| P/OCF | Base | US$94,94 | US$90,29 | US$88,35 | US$91,19 | OK |
| P/OCF | Conservador | US$90,15 | US$79,67 | US$74,00 | US$81,28 | OK |
| P/OCF | Optimista | US$102,25 | US$102,64 | US$102,18 | US$102,35 | OK |

Múltiplos consolidados hoy: US$97,92 / US$79,85 / US$112,78 · DCF de las historias hoy: US$101,03 / US$56,06 / US$116,63 · Ponderado hoy: US$99,16 / US$70,33 / US$114,32 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para ZTS la diferencia es de −3% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$117,30 por acción y los múltiplos, US$111,20 hoy: 5% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$69,83 supone que los ingresos crecen -2,1% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 4,5% (−6,6 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$137,87 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,9%, WACC de los años 4-10 9,6%, ROE de FY+3 91,9% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 12,8x | 14,6x | −13% | 4,8% | 5,4% | −0,6 pp | Coherente con el DCF. |
| EV/FCFF | 21,8x | 25,0x | −14% | 4,8% | 5,4% | −0,6 pp | Coherente con el DCF. |
| P/E | 21,0x | 19,8x | +6% | 6,2% | 5,9% | +0,3 pp | Coherente con el DCF. |
| P/FCFE | 19,9x | 19,8x | +0% | 5,6% | 5,6% | +0,0 pp | Coherente con el DCF. |
| P/OCF | 15,6x | 18,1x | −13% | 4,8% | 5,6% | −0,8 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$99,16 | — |
| Múltiplos Base +20% | US$111,20 | +12,1% |
| Múltiplos Base −20% | US$87,12 | −12,1% |
| Crecimiento años 2-5 +2 pp | US$103,16 | +4,0% |
| Crecimiento años 2-5 −2 pp | US$95,52 | −3,7% |
| Margen objetivo +3 pp | US$102,93 | +3,8% |
| Margen objetivo −3 pp | US$95,39 | −3,8% |
| WACC +1 pp | US$96,59 | −2,6% |
| WACC −1 pp | US$101,91 | +2,8% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 11,86 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 9,30 | 12,81 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 14,14 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 19,62 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 15,69 | 21,77 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 23,76 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 17,34 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 12,06 | 21,01 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 22,84 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 17,36 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 12,41 | 19,93 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 22,31 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 13,82 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 10,17 | 15,56 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 17,45 | Múltiplo optimista elegido con el protocolo v3 |
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
