---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Palantir Technologies Inc."
ticker: "PLTR"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1Y6kXnRlrAKK3C20tQtIfDd2IXYG0eKEi10wyR8TXFLA/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Palantir Technologies Inc. (PLTR) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$75,36 por acción.** Complemento: DCF esperado por probabilidades US$68,70; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$14,94–US$133,60; precio con MOS 35% sobre el esperado: US$44,66; precio de referencia US$191,53. Cada escenario es un DCF completo con la estructura de Damodaran, calculado en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción; B35 es el DCF Base) y resumido en «Escenarios e historias»; el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo son esas historias, y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Hipercrecimiento que desacelera con la escala** (valor principal) | 40% | US$75,36 | US$30,15 |
| Conservadora · Se normaliza en un software de alta calidad | 30% | US$34,47 | US$10,34 |
| Disrupción · Deterioro de los fundamentales: Comoditización y contratos perdidos | 10% | US$14,94 | US$1,49 |
| Optimista · Sistema operativo de la IA empresarial | 20% | US$133,60 | US$26,72 |
| **DCF esperado (complemento)** | 100% | **US$68,70** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$85,42 por acción y los múltiplos, US$123,49 hoy: 45% por encima del DCF, fuera del rango de ±25%. Los múltiplos suponen que en FY+3 Palantir cotiza como el software de crecimiento alto de hoy; P/E y P/OCF quedan muy por encima de EV/EBITDA porque la utilidad normalizada de FY+3 supera al EBITDA, algo que conviene revisar en la proyección.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$75,36 | US$165,53 | US$111,43 | US$44,66 | US$167,91 |
| Conservador | US$34,47 | US$82,35 | US$53,62 | US$44,66 | US$72,60 |
| Optimista | US$133,60 | US$273,97 | US$189,75 | US$44,66 | US$307,46 |

## 2. Datos

- Hoja del modelo: [Modelo_JMR_Plantilla_Maestra PLTR](https://docs.google.com/spreadsheets/d/1Y6kXnRlrAKK3C20tQtIfDd2IXYG0eKEi10wyR8TXFLA/edit).
- Análisis del 30 de sept de 2026. Precio de referencia de la hoja: US$191,53.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 39,6% | 68,0% | 89,2% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 21,6% | 35,0% | 60,7% | Input B29 |
| Margen EBIT objetivo | 38,4% | 48,4% | 50,4% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 3,47 / 3,84 | — | Input B32/B33 |
| DCF por acción hoy | US$34,47 | US$75,36 | US$133,60 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,29%, beta apalancada 1,25, ERP 4,09%, Ke 10,40%, costo de la deuda después de impuestos 4,50%, peso del patrimonio 99,9%, WACC inicial 10,40% y terminal 8,99%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Palantir es rentable desde 2023 y cotiza como la plataforma de IA de mayor crecimiento del software (ingresos 2026 +82% según su guía), a 150-500x EBITDA. Ese múltiplo no se usa como ancla: el Base de la hoja lleva el crecimiento de 82% a 40% en FY+3, y el múltiplo de FY+3 tiene que ser el de una empresa que crece 40%, no 80%. El ancla es B (peers ajustados). la historia no representa a la Palantir de FY+3: antes de 2023 la utilidad era negativa y desde 2023 el múltiplo (150-500x) corresponde a un crecimiento de ~80% que en el escenario Base baja a 40% en FY+3; aplicarlo a la métrica de FY+3 supondría que el mercado no comprime el múltiplo mientras el crecimiento se normaliza B: software de crecimiento alto y rentable (ServiceNow, Fortinet, AppLovin, Datadog, MongoDB, Axon, Palo Alto), datos de yfinance al 29-sep-2026. Se excluyen CrowdStrike, Cloudflare y Snowflake (margen operativo GAAP negativo: sus múltiplos de utilidad y EBITDA no tienen sentido) y, en P/E, Axon, Palo Alto, MongoDB y Datadog (P/E de 170-1.000x por compensación en acciones y utilidad casi cero). Ajuste +25%: en FY+3 el escenario Base todavía crece 40%, frente a 25-35% de la mediana de los peers hoy, con márgenes más altos. λ no aplica: el múltiplo justificado C no se puede calcular en ningún escenario porque el crecimiento de los años 4-10 (19-31%) supera al WACC (10,9%); la fórmula de Gordon exige g al menos 1 pp por debajo. Sin A ni C, el Base es B.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | sin historia representativa (la historia no representa a la Palantir de FY+3: antes de 2023 la utilidad era negativa y desde 2023 el múltiplo (150-500x) corresponde a un crecimiento de ~80% que en el escenario Base baja a 40% en FY+3; aplicarlo a la métrica de FY+3 supondría que el mercado no comprime el múltiplo mientras el crecimiento se normaliza) | 47,7x (n=3: NOW 47,7x, APP 19,1x, FTNT 48,4x) × 1,25 = 59,6x | — / 32,0x / — | **59,6x** | 41,8x | 61,4x | 61,2x / 37,4x / 99,0x |
| EV/FCFF | sin historia representativa (la historia no representa a la Palantir de FY+3: antes de 2023 la utilidad era negativa y desde 2023 el múltiplo (150-500x) corresponde a un crecimiento de ~80% que en el escenario Base baja a 40% en FY+3; aplicarlo a la métrica de FY+3 supondría que el mercado no comprime el múltiplo mientras el crecimiento se normaliza) | 59,0x (n=6: NOW 29,8x, DDOG 85,6x, MDB 37,2x, AXON 157,6x, PANW 77,9x, FTNT 40,1x) × 1,25 = 73,7x | — / 36,1x / — | **73,7x** | 47,4x | 104,6x | 65,4x / 37,0x / 106,0x |
| P/E | sin historia representativa (la historia no representa a la Palantir de FY+3: antes de 2023 la utilidad era negativa y desde 2023 el múltiplo (150-500x) corresponde a un crecimiento de ~80% que en el escenario Base baja a 40% en FY+3; aplicarlo a la métrica de FY+3 supondría que el mercado no comprime el múltiplo mientras el crecimiento se normaliza) | 62,4x (n=3: NOW 81,2x, APP 23,5x, FTNT 62,4x) × 1,25 = 78,0x | — / 27,4x / — | **78,0x** | 53,7x | 89,8x | 41,8x / 26,4x / 66,6x |
| P/FCFE | sin historia representativa (la historia no representa a la Palantir de FY+3: antes de 2023 la utilidad era negativa y desde 2023 el múltiplo (150-500x) corresponde a un crecimiento de ~80% que en el escenario Base baja a 40% en FY+3; aplicarlo a la métrica de FY+3 supondría que el mercado no comprime el múltiplo mientras el crecimiento se normaliza) | 41,4x (n=5: NOW 29,4x, DDOG 89,9x, MDB 41,2x, PANW 77,2x, FTNT 41,4x) × 1,25 = 51,8x | — / 29,9x / — | **51,8x** | 50,2x | 96,6x | 42,6x / 25,6x / 68,0x |
| P/OCF | sin historia representativa (la historia no representa a la Palantir de FY+3: antes de 2023 la utilidad era negativa y desde 2023 el múltiplo (150-500x) corresponde a un crecimiento de ~80% que en el escenario Base baja a 40% en FY+3; aplicarlo a la métrica de FY+3 supondría que el mercado no comprime el múltiplo mientras el crecimiento se normaliza) | 55,2x (n=6: NOW 25,3x, DDOG 78,5x, MDB 40,7x, AXON 128,2x, PANW 69,8x, FTNT 38,0x) × 1,25 = 69,0x | — / 29,6x / — | **69,0x** | 48,4x | 95,4x | 42,3x / 25,4x / 67,4x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 59,6x: promedio de historia y peers 59,6x, acercado 0% al justificado (—x); rango de anclas 59,6x–59,6x. Atípicos excluidos de la historia: Dec '18 (0,0x: métrica negativa o ~0); Dec '20 (-34,8x: métrica negativa o ~0); Dec '21 (-86,8x: métrica negativa o ~0); Dec '22 (-78,2x: métrica negativa o ~0); Dec '19 (1,2x: < 0,4x la mediana (222.4x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 73,7x: promedio de historia y peers 73,7x, acercado 0% al justificado (—x); rango de anclas 73,7x–73,7x. Atípicos excluidos de la historia: Dec '18 (0,0x: métrica negativa o ~0); Dec '20 (-130,8x: métrica negativa o ~0); Dec '19 (3,8x: < 0,4x la mediana (107.0x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 78,0x: promedio de historia y peers 78,0x, acercado 0% al justificado (—x); rango de anclas 78,0x–78,0x. Atípicos excluidos de la historia: Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (0,0x: métrica negativa o ~0); Dec '20 (-19,6x: métrica negativa o ~0); Dec '21 (-67,4x: métrica negativa o ~0); Dec '22 (-35,7x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 51,8x: promedio de historia y peers 51,8x, acercado 0% al justificado (—x); rango de anclas 51,8x–51,8x. Atípicos excluidos de la historia: Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (0,0x: métrica negativa o ~0); Dec '20 (-136,7x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 69,0x: promedio de historia y peers 69,0x, acercado 0% al justificado (—x); rango de anclas 69,0x–69,0x. Atípicos excluidos de la historia: Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (0,0x: métrica negativa o ~0); Dec '20 (-142,3x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$165,53 frente a US$75,36 del DCF (+120%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$165,53 para los múltiplos Base.

## 5. Resultados

### Valor por acción en dos horizontes

Moneda: US$ por acción. Fecha de valoración: 2026-09-30. Escenarios en orden Base, Conservador y Optimista. Categoría de empresa «Crecimiento»: DCF 60% y múltiplos 40% (EV/EBITDA 10%, EV/FCFF 15%, P/E 5%, P/FCFE 5%, P/OCF 5%). Costo del patrimonio (Ke) 10,40%. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$14,94) y no se inventa para ellos.

**Valor intrínseco principal: DCF Base al presente, US$75,36 por acción.** Complemento: DCF esperado por probabilidades US$68,70. Múltiplos y ponderados son lecturas secundarias.

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 60% | — | US$75,36 | US$34,47 | US$133,60 |
| EV/EBITDA | 59,6× / 41,8× / 61,4× | 10% | 25% | US$138,46 | US$65,59 | US$183,83 |
| EV/FCFF | 73,7× / 47,4× / 104,6× | 15% | 37% | US$135,13 | US$64,53 | US$229,07 |
| P/E | 78,0× / 53,7× / 89,8× | 5% | 12% | US$270,37 | US$122,69 | US$403,49 |
| P/FCFE | 51,8× / 50,2× / 96,6× | 5% | 12% | US$158,36 | US$107,15 | US$367,21 |
| P/OCF | 69,0× / 48,4× / 95,4× | 5% | 12% | US$213,22 | US$104,15 | US$366,19 |
| **Ponderado de múltiplos solos al presente** | — | 40% | 100% | US$165,53 | US$82,35 | US$273,97 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$111,43 | US$53,62 | US$189,75 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 (la hoja no proyecta dividendos: precio objetivo exdividendo = total).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 60% | — | US$101,42 | US$46,39 | US$179,79 |
| EV/EBITDA | 59,6× / 41,8× / 61,4× | 10% | 25% | US$217,50 | US$87,92 | US$319,94 |
| EV/FCFF | 73,7× / 47,4× / 104,6× | 15% | 37% | US$224,17 | US$88,48 | US$433,11 |
| P/E | 78,0× / 53,7× / 89,8× | 5% | 12% | US$427,31 | US$165,27 | US$706,69 |
| P/FCFE | 51,8× / 50,2× / 96,6× | 5% | 12% | US$258,46 | US$146,39 | US$674,03 |
| P/OCF | 69,0× / 48,4× / 95,4× | 5% | 12% | US$347,95 | US$142,35 | US$671,81 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 40% | 100% | US$267,65 | US$111,91 | US$498,97 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$167,91 | US$72,60 | US$307,46 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).

Detalle del valor presente por horizonte (Ke 10,40%; consolidado por método: Promedio 1-3 años; cada dividendo descontado en su año de pago):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$112,80 | US$140,97 | US$161,62 | US$138,46 | OK |
| EV/EBITDA | Conservador | US$65,59 | US$65,87 | US$65,33 | US$65,59 | OK |
| EV/EBITDA | Optimista | US$127,53 | US$186,23 | US$237,74 | US$183,83 | OK |
| EV/FCFF | Base | US$100,16 | US$138,65 | US$166,58 | US$135,13 | OK |
| EV/FCFF | Conservador | US$62,70 | US$65,14 | US$65,74 | US$64,53 | OK |
| EV/FCFF | Optimista | US$132,88 | US$232,49 | US$321,84 | US$229,07 | OK |
| P/E | Base | US$218,13 | US$275,46 | US$317,52 | US$270,37 | OK |
| P/E | Conservador | US$121,98 | US$123,27 | US$122,81 | US$122,69 | OK |
| P/E | Optimista | US$276,44 | US$408,91 | US$525,13 | US$403,49 | OK |
| P/FCFE | Base | US$120,94 | US$162,07 | US$192,06 | US$158,36 | OK |
| P/FCFE | Conservador | US$104,67 | US$108,01 | US$108,78 | US$107,15 | OK |
| P/FCFE | Optimista | US$228,27 | US$372,51 | US$500,86 | US$367,21 | OK |
| P/OCF | Base | US$162,89 | US$218,21 | US$258,55 | US$213,22 | OK |
| P/OCF | Conservador | US$101,68 | US$104,99 | US$105,78 | US$104,15 | OK |
| P/OCF | Optimista | US$227,89 | US$371,47 | US$499,21 | US$366,19 | OK |

Múltiplos consolidados hoy: US$165,53 / US$82,35 / US$273,97 · DCF de las historias hoy: US$75,36 / US$34,47 / US$133,60 · Ponderado hoy: US$111,43 / US$53,62 / US$189,75 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para PLTR la diferencia es de +120% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$85,42 por acción y los múltiplos, US$123,49 hoy: 45% por encima del DCF, fuera del rango de ±25%. Los múltiplos suponen que en FY+3 Palantir cotiza como el software de crecimiento alto de hoy; P/E y P/OCF quedan muy por encima de EV/EBITDA porque la utilidad normalizada de FY+3 supera al EBITDA, algo que conviene revisar en la proyección.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$191,53 supone que los ingresos crecen 68,2% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 36,6% (+31,6 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$101,42 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 10,4%, WACC de los años 4-10 9,8%, ROE de FY+3 142,9% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 59,6x | 27,2x | +114% | 8,3% | 6,5% | +1,7 pp | Revisar: el múltiplo vale 114% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 73,7x | 32,7x | +121% | 8,3% | 6,5% | +1,8 pp | Revisar: el múltiplo vale 121% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| P/E | 78,0x | 18,5x | +321% | 9,1% | 4,9% | +4,2 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 321% por encima del DCF en FY+3. |
| P/FCFE | 51,8x | 20,3x | +155% | 8,3% | 5,2% | +3,1 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 155% por encima del DCF en FY+3. |
| P/OCF | 69,0x | 20,1x | +243% | 8,8% | 5,2% | +3,6 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 243% por encima del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$111,43 | — |
| Múltiplos Base +20% | US$124,53 | +11,8% |
| Múltiplos Base −20% | US$98,33 | −11,8% |
| Crecimiento años 2-5 +2 pp | US$115,14 | +3,3% |
| Crecimiento años 2-5 −2 pp | US$107,99 | −3,1% |
| Margen objetivo +3 pp | US$114,38 | +2,6% |
| Margen objetivo −3 pp | US$108,48 | −2,6% |
| WACC +1 pp | US$108,84 | −2,3% |
| WACC −1 pp | US$114,21 | +2,5% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 2-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 37,42 | 41,76 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 61,25 | 59,60 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 99,02 | 61,39 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 36,97 | 47,44 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 65,38 | 73,73 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 106,05 | 104,61 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 26,36 | 53,68 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 41,82 | 78,00 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 66,57 | 89,76 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 25,57 | 50,22 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 42,62 | 51,77 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 67,99 | 96,56 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 25,36 | 48,35 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 42,26 | 69,04 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 67,40 | 95,37 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/PLTR_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1Y6kXnRlrAKK3C20tQtIfDd2IXYG0eKEi10wyR8TXFLA/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (NOW, CRWD, DDOG, SNOW, NET, MDB, APP, AXON, PANW, FTNT).
- [Seeking Alpha: Palantir guía ingresos 2026 de US$8.150 millones](https://seekingalpha.com/news/4624208-palantir-outlines-2026-revenue-of-8_15b-8_158b-as-u-s-commercial-guidance-rises-above-3_424b)
- [I/O Fund: ¿es sostenible la valoración de Palantir?](https://io-fund.com/ai-stocks/palantir-stock-2026-forecast-valuation)

## 10. Control de calidad

| Comprobación | ¿Cumple? |
|---|---|
| No se cambiaron fórmulas, pesos ni estructura (solo J8/J19/J30 y textos) | Sí |
| Cada múltiplo Base tiene sus tres anclas con fuente y fecha | Sí, con limitación: EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF sin historia representativa (anclado en B y C) |
| Ningún múltiplo se derivó del DCF ni se ajustó después de verlo | Sí |
| Cada Base dentro del rango de sus anclas | Sí |
| Conservador < Base < Optimista en los cinco métodos; J8/J19/J30 escritos | Sí |
| Métodos no aplicables declarados | Sí |
| «Supuestos de los Múltiplos» A3 y A12 completos | Sí |
| DCF hoy, múltiplos hoy y ponderado hoy reportados por separado | Sí |
| Chequeo VP3 < FY+3 en OK en los tres escenarios | Sí |
| DCF Conservador < Base < Optimista | Sí |
