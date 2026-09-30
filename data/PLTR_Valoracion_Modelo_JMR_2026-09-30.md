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

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$105,73 en el escenario Base (rango US$58,58–US$180,31). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$137,05 (+30% frente al DCF). Con los pesos de la categoría «Crecimiento» (60% DCF, 40% múltiplos), el ponderado hoy (lectura secundaria) es US$118,26. El valor intrínseco es el DCF: US$105,73 frente a un precio de referencia de US$187,48 (−44%).

Los múltiplos (US$137,05 hoy) quedan 30% por encima del DCF (US$105,73); el precio (US$187,48) está por encima de ambos. Los múltiplos suponen que a FY+3 Palantir cotiza como el software de crecimiento alto de hoy con una prima de 25% (~60x EBITDA, ~78x utilidad), mientras que el DCF lleva el crecimiento de 40% en FY+3 a 5% en el año 10 con un WACC de 10,9%. El mercado paga por un crecimiento alto más largo que ambos. Ojo: P/E da US$196 porque la utilidad normalizada de FY+3 de la hoja (US$12.204 millones) supera al EBITDA (US$7.991 millones); conviene revisar esa proyección. Mientras tanto, el DCF y los múltiplos de flujo son la referencia más prudente.

| Escenario | DCF hoy (valor intrínseco) | Múltiplos consolidados hoy (secundario) | Ponderado hoy (secundario) | Compra con MOS sobre el DCF | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Conservador | US$58,58 | US$76,96 | US$65,93 | US$38,08 | US$95,70 |
| Base | US$105,73 | US$137,05 | US$118,26 | US$68,73 | US$179,64 |
| Optimista | US$180,31 | US$221,90 | US$196,94 | US$117,20 | US$310,97 |

## 2. Datos

- Hoja del modelo: [Modelo_JMR_Plantilla_Maestra PLTR](https://docs.google.com/spreadsheets/d/1Y6kXnRlrAKK3C20tQtIfDd2IXYG0eKEi10wyR8TXFLA/edit).
- Análisis del 16 de sept de 2026. Precio de referencia de la hoja: US$187,48.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 60,0% | 82,0% | 95,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 30,0% | 40,0% | 50,0% | Input B29 |
| Margen EBIT objetivo | 45,3% | 50,0% | 55,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 4,00 / 4,50 | — | Input B32/B33 |
| DCF por acción hoy | US$58,58 | US$105,73 | US$180,31 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 5,00%, beta apalancada 1,62, ERP 4,46%, Ke 12,23%, costo de la deuda después de impuestos 4,50%, peso del patrimonio 100,0%, WACC inicial 12,23% y terminal 9,23%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Palantir es rentable desde 2023 y cotiza como la plataforma de IA de mayor crecimiento del software (ingresos 2026 +82% según su guía), a 150-500x EBITDA. Ese múltiplo no se usa como ancla: el Base de la hoja lleva el crecimiento de 82% a 40% en FY+3, y el múltiplo de FY+3 tiene que ser el de una empresa que crece 40%, no 80%. El ancla es B (peers ajustados). la historia no representa a la Palantir de FY+3: antes de 2023 la utilidad era negativa y desde 2023 el múltiplo (150-500x) corresponde a un crecimiento de ~80% que en el escenario Base baja a 40% en FY+3; aplicarlo a la métrica de FY+3 supondría que el mercado no comprime el múltiplo mientras el crecimiento se normaliza B: software de crecimiento alto y rentable (ServiceNow, Fortinet, AppLovin, Datadog, MongoDB, Axon, Palo Alto), datos de yfinance al 29-sep-2026. Se excluyen CrowdStrike, Cloudflare y Snowflake (margen operativo GAAP negativo: sus múltiplos de utilidad y EBITDA no tienen sentido) y, en P/E, Axon, Palo Alto, MongoDB y Datadog (P/E de 170-1.000x por compensación en acciones y utilidad casi cero). Ajuste +25%: en FY+3 el escenario Base todavía crece 40%, frente a 25-35% de la mediana de los peers hoy, con márgenes más altos. λ no aplica: el múltiplo justificado C no se puede calcular en ningún escenario porque el crecimiento de los años 4-10 (19-31%) supera al WACC (10,9%); la fórmula de Gordon exige g al menos 1 pp por debajo. Sin A ni C, el Base es B.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | sin historia representativa (la historia no representa a la Palantir de FY+3: antes de 2023 la utilidad era negativa y desde 2023 el múltiplo (150-500x) corresponde a un crecimiento de ~80% que en el escenario Base baja a 40% en FY+3; aplicarlo a la métrica de FY+3 supondría que el mercado no comprime el múltiplo mientras el crecimiento se normaliza) | 47,7x (n=3: NOW 47,7x, APP 19,1x, FTNT 48,4x) × 1,25 = 59,6x | — / — / — | 41,8x | **59,6x** | 61,4x | 37,4x / 61,2x / 99,0x |
| EV/FCFF | sin historia representativa (la historia no representa a la Palantir de FY+3: antes de 2023 la utilidad era negativa y desde 2023 el múltiplo (150-500x) corresponde a un crecimiento de ~80% que en el escenario Base baja a 40% en FY+3; aplicarlo a la métrica de FY+3 supondría que el mercado no comprime el múltiplo mientras el crecimiento se normaliza) | 59,0x (n=6: NOW 29,8x, DDOG 85,6x, MDB 37,2x, AXON 157,6x, PANW 77,9x, FTNT 40,1x) × 1,25 = 73,7x | — / — / — | 47,4x | **73,7x** | 104,6x | 37,0x / 65,4x / 106,0x |
| P/E | sin historia representativa (la historia no representa a la Palantir de FY+3: antes de 2023 la utilidad era negativa y desde 2023 el múltiplo (150-500x) corresponde a un crecimiento de ~80% que en el escenario Base baja a 40% en FY+3; aplicarlo a la métrica de FY+3 supondría que el mercado no comprime el múltiplo mientras el crecimiento se normaliza) | 62,4x (n=3: NOW 81,2x, APP 23,5x, FTNT 62,4x) × 1,25 = 78,0x | — / — / — | 53,7x | **78,0x** | 89,8x | 26,4x / 41,8x / 66,6x |
| P/FCFE | sin historia representativa (la historia no representa a la Palantir de FY+3: antes de 2023 la utilidad era negativa y desde 2023 el múltiplo (150-500x) corresponde a un crecimiento de ~80% que en el escenario Base baja a 40% en FY+3; aplicarlo a la métrica de FY+3 supondría que el mercado no comprime el múltiplo mientras el crecimiento se normaliza) | 41,4x (n=5: NOW 29,4x, DDOG 89,9x, MDB 41,2x, PANW 77,2x, FTNT 41,4x) × 1,25 = 51,8x | — / — / — | 50,2x | **51,8x** | 96,6x | 25,6x / 42,6x / 68,0x |
| P/OCF | sin historia representativa (la historia no representa a la Palantir de FY+3: antes de 2023 la utilidad era negativa y desde 2023 el múltiplo (150-500x) corresponde a un crecimiento de ~80% que en el escenario Base baja a 40% en FY+3; aplicarlo a la métrica de FY+3 supondría que el mercado no comprime el múltiplo mientras el crecimiento se normaliza) | 55,2x (n=6: NOW 25,3x, DDOG 78,5x, MDB 40,7x, AXON 128,2x, PANW 69,8x, FTNT 38,0x) × 1,25 = 69,0x | — / — / — | 48,4x | **69,0x** | 95,4x | 25,4x / 42,3x / 67,4x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 59,6x: promedio de historia y peers 59,6x, acercado 0% al justificado (—x); rango de anclas 59,6x–59,6x. Atípicos excluidos de la historia: Dec '18 (0,0x: métrica negativa o ~0); Dec '20 (-34,8x: métrica negativa o ~0); Dec '21 (-86,8x: métrica negativa o ~0); Dec '22 (-78,2x: métrica negativa o ~0); Dec '19 (1,2x: < 0,4x la mediana (222.4x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 73,7x: promedio de historia y peers 73,7x, acercado 0% al justificado (—x); rango de anclas 73,7x–73,7x. Atípicos excluidos de la historia: Dec '18 (0,0x: métrica negativa o ~0); Dec '20 (-130,8x: métrica negativa o ~0); Dec '19 (3,8x: < 0,4x la mediana (107.0x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 78,0x: promedio de historia y peers 78,0x, acercado 0% al justificado (—x); rango de anclas 78,0x–78,0x. Atípicos excluidos de la historia: Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (0,0x: métrica negativa o ~0); Dec '20 (-19,6x: métrica negativa o ~0); Dec '21 (-67,4x: métrica negativa o ~0); Dec '22 (-35,7x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 51,8x: promedio de historia y peers 51,8x, acercado 0% al justificado (—x); rango de anclas 51,8x–51,8x. Atípicos excluidos de la historia: Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (0,0x: métrica negativa o ~0); Dec '20 (-136,7x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 69,0x: promedio de historia y peers 69,0x, acercado 0% al justificado (—x); rango de anclas 69,0x–69,0x. Atípicos excluidos de la historia: Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (0,0x: métrica negativa o ~0); Dec '20 (-142,3x: métrica negativa o ~0).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$137,05 frente a US$105,73 del DCF (+30%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$137,05 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$82,79 | US$149,45 | US$254,85 |
| EV/EBITDA | 10% | US$84,52 | US$165,58 | US$221,26 |
| EV/FCFF | 15% | US$96,57 | US$207,61 | US$383,19 |
| P/E | 5% | US$159,54 | US$324,60 | US$487,46 |
| P/FCFE | 5% | US$153,35 | US$222,18 | US$542,17 |
| P/OCF | 5% | US$148,88 | US$298,65 | US$539,49 |
| **Ponderado FY+3** | 100% | US$95,70 | US$179,64 | US$310,97 |

Valor presente (Ke 12,23%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$53,92 | US$56,37 | US$59,80 | US$56,70 | OK |
| EV/EBITDA | Base | US$85,54 | US$100,26 | US$117,15 | US$100,98 | OK |
| EV/EBITDA | Optimista | US$94,07 | US$122,70 | US$156,54 | US$124,44 | OK |
| EV/FCFF | Conservador | US$62,66 | US$64,29 | US$68,32 | US$65,09 | OK |
| EV/FCFF | Base | US$109,50 | US$125,54 | US$146,88 | US$127,31 | OK |
| EV/FCFF | Optimista | US$165,66 | US$212,01 | US$271,11 | US$216,26 | OK |
| P/E | Conservador | US$99,08 | US$105,15 | US$112,87 | US$105,70 | OK |
| P/E | Base | US$163,77 | US$194,75 | US$229,66 | US$196,06 | OK |
| P/E | Optimista | US$201,92 | US$267,81 | US$344,88 | US$271,54 | OK |
| P/FCFE | Conservador | US$96,77 | US$101,13 | US$108,49 | US$102,13 | OK |
| P/FCFE | Base | US$114,30 | US$133,44 | US$157,20 | US$134,98 | OK |
| P/FCFE | Optimista | US$229,23 | US$298,37 | US$383,59 | US$303,73 | OK |
| P/OCF | Conservador | US$93,91 | US$98,17 | US$105,34 | US$99,14 | OK |
| P/OCF | Base | US$153,65 | US$179,38 | US$211,30 | US$181,44 | OK |
| P/OCF | Optimista | US$228,20 | US$296,95 | US$381,69 | US$302,28 | OK |

Múltiplos consolidados hoy: US$76,96 / US$137,05 / US$221,90 · DCF hoy: US$58,58 / US$105,73 / US$180,31 · Ponderado hoy: US$65,93 / US$118,26 / US$196,94 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para PLTR la diferencia es de +30% (múltiplos por encima del DCF). Los múltiplos (US$137,05 hoy) quedan 30% por encima del DCF (US$105,73); el precio (US$187,48) está por encima de ambos. Los múltiplos suponen que a FY+3 Palantir cotiza como el software de crecimiento alto de hoy con una prima de 25% (~60x EBITDA, ~78x utilidad), mientras que el DCF lleva el crecimiento de 40% en FY+3 a 5% en el año 10 con un WACC de 10,9%. El mercado paga por un crecimiento alto más largo que ambos. Ojo: P/E da US$196 porque la utilidad normalizada de FY+3 de la hoja (US$12.204 millones) supera al EBITDA (US$7.991 millones); conviene revisar esa proyección. Mientras tanto, el DCF y los múltiplos de flujo son la referencia más prudente.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$187,48 supone que los ingresos crecen 61,9% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 48,4% (+13,5 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Crecimiento perpetuo después de FY+3 que supone cada múltiplo Base, con Ke 12,2%, WACC de los años 4-10 10,9% y ROE de FY+3 123,5%, frente al crecimiento del DCF (15,0%: punto medio entre los años 4-10 y la perpetuidad):

| Múltiplo Base FY+3 | Múltiplo | Crecimiento implícito | Diferencia vs. DCF | Lectura |
|---|---:|---:|---:|---|
| EV/EBITDA | 59,6x | 9,1% | — | No comparable: el DCF supone después de FY+3 un crecimiento cercano o mayor al costo de capital (Gordon no aplica). |
| EV/FCFF | 73,7x | 9,5% | — | No comparable: el DCF supone después de FY+3 un crecimiento cercano o mayor al costo de capital (Gordon no aplica). |
| P/E | 78,0x | 10,9% | — | No comparable: el DCF supone después de FY+3 un crecimiento cercano o mayor al costo de capital (Gordon no aplica). |
| P/FCFE | 51,8x | 10,1% | — | No comparable: el DCF supone después de FY+3 un crecimiento cercano o mayor al costo de capital (Gordon no aplica). |
| P/OCF | 69,0x | 10,6% | — | No comparable: el DCF supone después de FY+3 un crecimiento cercano o mayor al costo de capital (Gordon no aplica). |

Más de 2 pp de diferencia significa que el múltiplo (o el precio) cuenta otra historia de crecimiento que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (subir el crecimiento del DCF si la evidencia lo sostiene, o acercar el múltiplo al justificado si no).

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$118,26 | — |
| Múltiplos Base +20% | US$129,09 | +9,2% |
| Múltiplos Base −20% | US$107,43 | −9,2% |
| Crecimiento años 1-5 +2 pp | US$123,31 | +4,3% |
| Crecimiento años 1-5 −2 pp | US$113,54 | −4,0% |
| Margen objetivo +3 pp | US$122,21 | +3,3% |
| Margen objetivo −3 pp | US$114,30 | −3,3% |
| WACC +1 pp | US$114,57 | −3,1% |
| WACC −1 pp | US$122,21 | +3,3% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Crecimiento años 1-5 +2 pp.

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
