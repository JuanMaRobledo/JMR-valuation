---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Celsius Holdings, Inc."
ticker: "CELH"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1pl_6BeI9gl_ciaSY5wDqyjRF9GS-ZhjXXK4wGVuBC4o/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Celsius Holdings, Inc. (CELH) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$18,41 por acción.** Complemento: DCF esperado por probabilidades US$14,21; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$3,30–US$25,93; precio con MOS 35% sobre el esperado: US$9,24; precio de referencia US$27,42. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$13,74), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Alani lidera y Celsius se estabiliza** (valor principal) | 40% | US$18,41 | US$7,36 |
| Conservadora · Alani crece, Celsius sigue cediendo | 35% | US$10,74 | US$3,76 |
| Disrupción · Deterioro de los fundamentales: La moda se desgasta | 15% | US$3,30 | US$0,50 |
| Optimista · Plataforma multimarca | 10% | US$25,93 | US$2,59 |
| **DCF esperado (complemento)** | 100% | **US$14,21** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$18,12 por acción y los múltiplos, US$21,32 hoy: 18% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$18,41 | US$22,41 | US$20,01 | US$9,24 | US$30,64 |
| Conservador | US$10,74 | US$18,28 | US$13,76 | US$9,24 | US$19,62 |
| Optimista | US$25,93 | US$22,94 | US$24,74 | US$9,24 | US$41,77 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - CELH](https://docs.google.com/spreadsheets/d/1pl_6BeI9gl_ciaSY5wDqyjRF9GS-ZhjXXK4wGVuBC4o/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$27,42.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 2,0% | 7,0% | 12,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 2,0% | 6,0% | 12,0% | Input B29 |
| Margen EBIT objetivo | 11,1% | 17,1% | 21,1% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,47 / 1,98 | — | Input B32/B33 |
| DCF por acción hoy | US$10,74 | US$18,41 | US$25,93 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 1,50, ERP 4,46%, Ke 11,68%, costo de la deuda después de impuestos 5,19%, peso del patrimonio 90,6%, WACC inicial 11,07% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Celsius fue hipercrecimiento hasta 2023 (múltiplos de 50-500x o con utilidades negativas); desde 2024 es una marca de bebidas energéticas en consolidación. Se usa FY24 como etapa actual. El FY25 y el LTM se excluyen de todos los métodos: incluyen US$246,7 millones por terminar contratos de distribución de Alani Nu (traspaso al sistema de PepsiCo) y US$24,8 millones de costos de la adquisición (10-K FY2025), que distorsionan utilidad, EBITDA y flujo de caja. B: bebidas con marca (Monster, PepsiCo, Coca-Cola, Vita Coco), datos de yfinance al 29-sep-2026. Se excluyen Keurig Dr Pepper (crecimiento de 76% por la compra de JDE Peet's distorsiona sus múltiplos) y BellRing (nutrición, en fuerte caída). Ajuste −10%: Celsius crece más que Coca-Cola y PepsiCo, pero con márgenes menores que Monster, dependencia de PepsiCo como distribuidor y una integración reciente (Alani Nu) aún por demostrar. λ = 0,25: la Celsius de FY+3 del escenario Base es una marca madura de crecimiento medio.

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '24 (etapa actual) = 32,6x | 23,1x (n=4: MNST 26,8x, PEP 11,5x, KO 23,8x, COCO 22,3x) × 0,90 = 20,8x | 12,1x / 11,0x / 15,3x | **23,0x** | 21,2x | 25,6x | 23,0x / 21,2x / 25,6x |
| EV/FCFF | mediana Dec '24 (etapa actual) = 21,3x (EV/FCF × 0,96 = FCF después de intereses ÷ FCFF) | 25,3x (n=4: MNST 37,8x, PEP 21,4x, KO 26,1x, COCO 24,5x) × 0,90 = 22,8x | 21,3x / 17,1x / 33,1x | **21,8x** | 20,0x | 27,0x | 22,6x / 20,5x / 28,0x |
| P/E | mediana Dec '24 (etapa actual) = 43,2x | 28,7x (n=4: MNST 38,6x, PEP 16,9x, KO 26,1x, COCO 31,2x) × 0,90 = 25,8x | 13,7x / 11,1x / 19,1x | **29,3x** | 25,8x | 34,6x | 29,3x / 25,8x / 34,6x |
| P/FCFE | mediana Dec '24 (etapa actual) = 25,9x | 26,2x (n=4: MNST 39,3x, PEP 18,9x, KO 26,1x, COCO 26,3x) × 0,90 = 23,6x | 16,4x / 13,8x / 22,8x | **22,6x** | 20,9x | 26,5x | 22,6x / 20,9x / 26,5x |
| P/OCF | mediana Dec '24 (etapa actual) = 23,5x | 23,9x (n=4: MNST 36,5x, PEP 13,1x, KO 22,9x, COCO 24,8x) × 0,90 = 21,5x | 13,8x / 11,3x / 18,8x | **20,3x** | 18,1x | 23,9x | 20,3x / 18,1x / 23,9x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 23,0x: promedio de historia y peers 26,7x, acercado 25% al justificado (12,1x); rango de anclas 12,1x–32,6x. Atípicos excluidos de la historia: Dec '16 (-7,5x: métrica negativa o ~0); Dec '17 (-8,1x: métrica negativa o ~0); Dec '18 (-5,5x: métrica negativa o ~0); Dec '19 (-69,0x: métrica negativa o ~0); Dec '21 (-659,4x: métrica negativa o ~0); Dec '22 (-13,1x: métrica negativa o ~0); Dec '20 (136,0x: > 2,5x la mediana (44.1x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 21,8x: promedio de historia y peers 22,0x, acercado 25% al justificado (21,3x); rango de anclas 21,3x–22,8x. Atípicos excluidos de la historia: Dec '16 (-8,8x: métrica negativa o ~0); Dec '17 (-7,7x: métrica negativa o ~0); Dec '18 (-5,0x: métrica negativa o ~0); Dec '21 (-18,5x: métrica negativa o ~0); Dec '19 (96,6x: > 2,5x la mediana (37.2x)); Dec '20 (417,8x: > 2,5x la mediana (37.2x)); Dec '23 (96,0x: > 2,5x la mediana (37.2x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 29,3x: promedio de historia y peers 34,5x, acercado 25% al justificado (13,7x); rango de anclas 13,7x–43,2x. Atípicos excluidos de la historia: Dec '18 (-5,3x: métrica negativa o ~0); Dec '22 (-14,0x: métrica negativa o ~0); Dec '19 (10,1x: < 0,4x la mediana (56.8x), caída puntual); Dec '20 (152,4x: > 2,5x la mediana (56.8x)); Dec '21 (497,2x: > 2,5x la mediana (56.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 22,6x: promedio de historia y peers 24,7x, acercado 25% al justificado (16,4x); rango de anclas 16,4x–25,9x. Atípicos excluidos de la historia: Dec '16 (-13,7x: métrica negativa o ~0); Dec '17 (-9,4x: métrica negativa o ~0); Dec '18 (-5,6x: métrica negativa o ~0); Dec '21 (-18,7x: métrica negativa o ~0); Dec '19 (110,9x: > 2,5x la mediana (36.3x)); Dec '20 (433,0x: > 2,5x la mediana (36.3x)); Dec '23 (102,1x: > 2,5x la mediana (36.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 20,3x: promedio de historia y peers 22,5x, acercado 25% al justificado (13,8x); rango de anclas 13,8x–23,5x. Atípicos excluidos de la historia: Dec '16 (-13,7x: métrica negativa o ~0); Dec '17 (-9,5x: métrica negativa o ~0); Dec '18 (-5,7x: métrica negativa o ~0); Dec '21 (-19,3x: métrica negativa o ~0); Dec '19 (110,9x: > 2,5x la mediana (32.7x)); Dec '20 (356,6x: > 2,5x la mediana (32.7x)); Dec '23 (89,5x: > 2,5x la mediana (32.7x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$22,41 frente a US$18,41 del DCF (+22%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$22,41 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 60% | US$25,64 | US$14,96 | US$36,12 |
| EV/EBITDA | 10% | US$56,33 | US$37,44 | US$81,77 |
| EV/FCFF | 15% | US$26,56 | US$18,73 | US$32,04 |
| P/E | 5% | US$51,44 | US$34,36 | US$77,14 |
| P/FCFE | 5% | US$29,72 | US$23,43 | US$30,79 |
| P/OCF | 5% | US$31,54 | US$24,05 | US$34,25 |
| **Ponderado FY+3** | 100% | US$30,64 | US$19,62 | US$41,77 |

Valor presente (Ke 11,68%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$28,82 | US$36,98 | US$40,44 | US$35,41 | OK |
| EV/EBITDA | Conservador | US$24,16 | US$26,68 | US$26,88 | US$25,91 | OK |
| EV/EBITDA | Optimista | US$34,91 | US$50,80 | US$58,71 | US$48,14 | OK |
| EV/FCFF | Base | US$6,97 | US$14,22 | US$19,07 | US$13,42 | OK |
| EV/FCFF | Conservador | US$10,49 | US$12,84 | US$13,45 | US$12,26 | OK |
| EV/FCFF | Optimista | US$-10,34 | US$8,35 | US$23,00 | US$7,00 | OK |
| P/E | Base | US$28,53 | US$34,63 | US$36,93 | US$33,37 | OK |
| P/E | Conservador | US$23,70 | US$25,04 | US$24,67 | US$24,47 | OK |
| P/E | Optimista | US$35,64 | US$49,01 | US$55,38 | US$46,68 | OK |
| P/FCFE | Base | US$10,97 | US$17,17 | US$21,33 | US$16,49 | OK |
| P/FCFE | Conservador | US$15,16 | US$16,77 | US$16,82 | US$16,25 | OK |
| P/FCFE | Optimista | US$-7,48 | US$8,91 | US$22,10 | US$7,85 | OK |
| P/OCF | Base | US$13,48 | US$18,99 | US$22,64 | US$18,37 | OK |
| P/OCF | Conservador | US$16,23 | US$17,42 | US$17,26 | US$16,97 | OK |
| P/OCF | Optimista | US$-2,21 | US$12,69 | US$24,59 | US$11,69 | OK |

Múltiplos consolidados hoy: US$22,41 / US$18,28 / US$22,94 · DCF de las historias hoy: US$18,41 / US$10,74 / US$25,93 · Ponderado hoy: US$20,01 / US$13,76 / US$24,74 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para CELH la diferencia es de +22% (múltiplos por encima del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$18,12 por acción y los múltiplos, US$21,32 hoy: 18% por encima del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$27,42 supone que los ingresos crecen 12,4% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 6,2% (+6,2 pp). El precio supone más crecimiento que el DCF: mercado optimista o DCF conservador.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$25,64 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 11,7%, WACC de los años 4-10 10,2%, ROE de FY+3 31,2% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 23,0x | 9,4x | +120% | 7,6% | 3,9% | +3,7 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 120% por encima del DCF en FY+3. |
| EV/FCFF | 21,8x | 16,7x | +4% | 5,4% | 4,0% | +1,4 pp | Coherente con el DCF. |
| P/E | 29,3x | 14,6x | +101% | 9,0% | 5,8% | +3,3 pp | Revisar: el múltiplo supone más crecimiento que el DCF. En valor, 101% por encima del DCF en FY+3. |
| P/FCFE | 22,6x | 19,5x | +16% | 7,0% | 6,2% | +0,7 pp | Coherente con el DCF. |
| P/OCF | 20,3x | 16,5x | +23% | 7,3% | 6,3% | +1,0 pp | Coherente con el DCF. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$20,01 | — |
| Múltiplos Base +20% | US$22,09 | +10,4% |
| Múltiplos Base −20% | US$17,93 | −10,4% |
| Crecimiento años 2-5 +2 pp | US$22,30 | +11,4% |
| Crecimiento años 2-5 −2 pp | US$20,53 | +2,6% |
| Margen objetivo +3 pp | US$23,59 | +17,9% |
| Margen objetivo −3 pp | US$19,16 | −4,2% |
| WACC +1 pp | US$20,72 | +3,5% |
| WACC −1 pp | US$22,09 | +10,4% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Margen objetivo +3 pp, Crecimiento años 2-5 +2 pp, Múltiplos Base −20%.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 21,18 | 21,18 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 23,03 | 23,03 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 25,58 | 25,58 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 20,46 | 19,96 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 22,56 | 21,84 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 27,96 | 26,96 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 25,77 | 25,77 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 29,28 | 29,28 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 34,64 | 34,64 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 20,90 | 20,90 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 22,65 | 22,65 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 26,54 | 26,54 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 18,14 | 18,14 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 20,32 | 20,32 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 23,89 | 23,89 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/CELH_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1pl_6BeI9gl_ciaSY5wDqyjRF9GS-ZhjXXK4wGVuBC4o/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (MNST, KDP, PEP, KO, BRBR, COCO).
- [Celsius Holdings, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1341766/000134176626000024/celh-20251231.htm): costos de la adquisición de Alani Nu y terminación de distribuidores.

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
