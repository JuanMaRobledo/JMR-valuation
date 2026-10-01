---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Uber Technologies, Inc"
ticker: "UBER"
analysis_date: "2026-09-30"
sheet: "https://docs.google.com/spreadsheets/d/1R3V8gISxXCYIujVFSITu0svVBC3AsN4GF_pQHHLs5dw/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Uber Technologies, Inc (UBER) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$89,78 por acción.** Complemento: DCF esperado por probabilidades US$81,21; rango de los cuatro escenarios (Base, Conservadora, Disrupción y Optimista) US$28,81–US$122,09; precio con MOS 35% sobre el esperado: US$52,79; precio de referencia US$68,91. Cada escenario es un DCF completo (hoja «Escenarios e historias»); el detalle y la justificación de los supuestos están en la sección «Valor con criterio Damodaran» del análisis fundamental. Los casos Conservador/Base/Optimista de abajo usan el DCF de las historias Conservadora, Base y Optimista; el antiguo caso técnico de la hoja ('Valuation output' B35) queda como calibración (US$88,97), y los múltiplos y el ponderado son lecturas secundarias.


| Escenario | Probabilidad | DCF hoy por acción | Aporte al esperado |
|---|---:|---:|---:|
| **Base · Plataforma madura que escala márgenes** (valor principal) | 45% | US$89,78 | US$40,40 |
| Conservadora · Robotaxis y regulación presionan la movilidad | 25% | US$54,02 | US$13,51 |
| Disrupción · Deterioro de los fundamentales: Waymo y Tesla desintermedian a Uber | 10% | US$28,81 | US$2,88 |
| Optimista · Uber es la red de los vehículos autónomos | 20% | US$122,09 | US$24,42 |
| **DCF esperado (complemento)** | 100% | **US$81,21** | |

Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$88,85 por acción y los múltiplos, US$83,89 hoy: 6% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

| Escenario | DCF de la historia hoy | Múltiplos consolidados hoy (secundario) | Mezcla auxiliar hoy | Compra con MOS sobre el valor esperado | Precio objetivo FY+3 ponderado (secundario) |
|---|---:|---:|---:|---:|---:|
| Base | US$89,78 | US$80,78 | US$84,38 | US$52,79 | US$117,79 |
| Conservador | US$54,02 | US$50,78 | US$52,08 | US$52,79 | US$67,54 |
| Optimista | US$122,09 | US$108,04 | US$113,66 | US$52,79 | US$166,11 |

## 2. Datos

- Hoja del modelo: [UBER plantilla maestra](https://docs.google.com/spreadsheets/d/1R3V8gISxXCYIujVFSITu0svVBC3AsN4GF_pQHHLs5dw/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$68,91.
- Peers: datos de mercado de yfinance consultados el 2026-09-30 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 8,0% | 13,0% | 18,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 8,0% | 11,0% | 18,0% | Input B29 |
| Margen EBIT objetivo | 13,7% | 21,2% | 26,2% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,29 / 3,11 | — | Input B32/B33 |
| DCF por acción hoy | US$54,02 | US$89,78 | US$122,09 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 0,80, ERP 4,46%, Ke 8,56%, costo de la deuda después de impuestos 4,33%, peso del patrimonio 91,4%, WACC inicial 8,19% y terminal 9,22%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Uber es rentable desde 2023; los cierres anteriores tienen EBITDA y utilidad negativos. La etapa actual es Dec '23 a LTM. En P/E se quita Dec '24: la utilidad de 2024 incluye la liberación de ~US$6.400 millones de la reserva de impuestos diferidos, que baja el P/E a 13x. La utilidad del LTM incluye revaluaciones de sus participaciones (Didi, Grab, Aurora) que se compensan entre trimestres (−US$1.500 millones en el 1T26, +US$1.600 millones en el 2T26). Se excluye la columna sin fecha de la hoja. En EV/EBITDA se quita también Dec '23 (69x): fue el primer año con EBITDA positivo (US$1.933 millones) y el múltiplo no es representativo. B: plataformas de movilidad, reparto y viajes (DoorDash, Airbnb, Booking, Grab, Expedia), datos de yfinance al 29-sep-2026. Se excluye Lyft (P/E de 2x por la liberación de su reserva de impuestos; EV/EBITDA de 112x) y, en P/E, DoorDash (98x con margen de 4%). Sin ajuste: Uber crece ~15-18% con margen creciente, en la mitad del grupo (más que Booking y Expedia, menos que DoorDash). λ = 0 (30-sep-2026): el justificado C usa g perpetuo de 6,7% con un ROE de 54% para siempre y Ke − g de apenas 1,9 pp, mientras el DCF supone que después del año 10 el retorno sobre el capital iguala al costo de capital; no es coherente con el DCF y se deja fuera del Base (se conserva como referencia en la tabla).

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista | Antes (J19/J8/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '24, Dec '25, LTM (etapa actual) = 27,6x | 25,3x (n=5: DASH 55,0x, ABNB 30,1x, BKNG 12,1x, GRAB 25,3x, EXPE 11,0x) × 1,00 = 13,5x | 43,6x / 29,8x / — | **20,6x** | 13,9x | 24,4x | 30,4x / 19,8x / 37,7x |
| EV/FCFF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 19,1x (EV/FCF × 1,03 = FCF después de intereses ÷ FCFF) | 12,1x (n=3: DASH 37,0x, BKNG 12,1x, EXPE 6,7x) × 1,00 = 10,0x | 55,5x / 38,1x / — | **14,6x** | 11,6x | 24,4x | 19,6x / 15,6x / 32,0x |
| P/E | mediana Dec '23, Dec '25, LTM (etapa actual) = 17,2x | 23,2x (n=4: ABNB 35,8x, BKNG 18,0x, GRAB 28,4x, EXPE 16,6x) × 1,00 = 20,7x | 50,5x / 32,8x / — | **19,0x** | 14,9x | 19,5x | 23,4x / 18,2x / 24,1x |
| P/FCFE | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 17,9x | 12,8x (n=3: DASH 37,9x, BKNG 12,8x, EXPE 7,2x) × 1,00 = 10,6x | 57,7x / 39,1x / — | **14,3x** | 11,3x | 23,4x | 19,6x / 15,5x / 32,2x |
| P/OCF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 17,3x | 12,4x (n=3: DASH 28,6x, BKNG 12,4x, EXPE 6,1x) × 1,00 = 9,8x | 62,8x / 42,2x / — | **13,6x** | 10,6x | 20,0x | 19,6x / 15,3x / 28,8x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 20,6x: promedio de historia y peers 20,6x, acercado 0% al justificado (43,6x); rango de anclas 13,5x–43,6x. Atípicos excluidos de la historia: Dec '18 (-0,2x: métrica negativa o ~0); Dec '19 (-5,8x: métrica negativa o ~0); Dec '20 (-22,8x: métrica negativa o ~0); Dec '21 (-30,1x: métrica negativa o ~0); Dec '22 (-63,7x: métrica negativa o ~0); Dec '17 (1,2x: < 0,4x la mediana (27.6x), caída puntual); Dec '23 (69,3x: > 2,5x la mediana (27.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 14,6x: promedio de historia y peers 14,6x, acercado 0% al justificado (55,5x); rango de anclas 10,0x–55,5x. Atípicos excluidos de la historia: Dec '18 (-0,2x: métrica negativa o ~0); Dec '19 (-9,7x: métrica negativa o ~0); Dec '20 (-29,1x: métrica negativa o ~0); Dec '21 (-119,0x: métrica negativa o ~0); Dec '17 (2,0x: < 0,4x la mediana (18.5x), caída puntual); Dec '22 (144,5x: > 2,5x la mediana (18.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 19,0x: promedio de historia y peers 19,0x, acercado 0% al justificado (50,5x); rango de anclas 17,2x–50,5x. Atípicos excluidos de la historia: Dec '17 (0,0x: métrica negativa o ~0); Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (-4,4x: métrica negativa o ~0); Dec '20 (-13,2x: métrica negativa o ~0); Dec '21 (-161,3x: métrica negativa o ~0); Dec '22 (-5,3x: métrica negativa o ~0); Dec '23 (68,4x: > 2,5x la mediana (16.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 14,3x: promedio de historia y peers 14,3x, acercado 0% al justificado (57,7x); rango de anclas 10,6x–57,7x. Atípicos excluidos de la historia: Dec '17 (0,0x: métrica negativa o ~0); Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (-10,4x: métrica negativa o ~0); Dec '20 (-28,1x: métrica negativa o ~0); Dec '21 (-110,0x: métrica negativa o ~0); Dec '22 (127,2x: > 2,5x la mediana (18.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 13,6x: promedio de historia y peers 13,6x, acercado 0% al justificado (62,8x); rango de anclas 9,8x–62,8x. Atípicos excluidos de la historia: Dec '17 (0,0x: métrica negativa o ~0); Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (-11,8x: métrica negativa o ~0); Dec '20 (-34,4x: métrica negativa o ~0); Dec '21 (-183,7x: métrica negativa o ~0); Dec '22 (77,2x: > 2,5x la mediana (17.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$80,78 frente a US$89,78 del DCF (−10%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$80,78 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Base | Conservador | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$114,87 | US$69,12 | US$156,21 |
| EV/EBITDA | 20% | US$146,60 | US$73,76 | US$209,16 |
| EV/FCFF | 10% | US$49,51 | US$33,50 | US$93,64 |
| P/E | 20% | US$142,95 | US$81,49 | US$179,04 |
| P/FCFE | 5% | US$96,00 | US$58,01 | US$188,30 |
| P/OCF | 5% | US$83,59 | US$51,87 | US$144,14 |
| **Ponderado FY+3** | 100% | US$117,79 | US$67,54 | US$166,11 |

Valor presente (Ke 8,56%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$84,63 | US$103,74 | US$114,59 | US$100,99 | OK |
| EV/EBITDA | Conservador | US$56,00 | US$57,65 | US$57,66 | US$57,10 | OK |
| EV/EBITDA | Optimista | US$102,42 | US$139,82 | US$163,48 | US$135,24 | OK |
| EV/FCFF | Base | US$19,83 | US$31,81 | US$38,70 | US$30,11 | OK |
| EV/FCFF | Conservador | US$21,50 | US$24,80 | US$26,18 | US$24,16 | OK |
| EV/FCFF | Optimista | US$24,23 | US$53,75 | US$73,19 | US$50,39 | OK |
| P/E | Base | US$79,27 | US$100,25 | US$111,73 | US$97,08 | OK |
| P/E | Conservador | US$60,56 | US$63,41 | US$63,70 | US$62,56 | OK |
| P/E | Optimista | US$83,49 | US$118,43 | US$139,94 | US$113,95 | OK |
| P/FCFE | Base | US$48,88 | US$65,91 | US$75,04 | US$63,28 | OK |
| P/FCFE | Conservador | US$41,96 | US$44,72 | US$45,34 | US$44,01 | OK |
| P/FCFE | Optimista | US$76,13 | US$119,97 | US$147,18 | US$114,43 | OK |
| P/OCF | Base | US$39,43 | US$55,95 | US$65,33 | US$53,57 | OK |
| P/OCF | Conservador | US$35,40 | US$39,18 | US$40,54 | US$38,37 | OK |
| P/OCF | Optimista | US$51,97 | US$88,86 | US$112,66 | US$84,50 | OK |

Múltiplos consolidados hoy: US$80,78 / US$50,78 / US$108,04 · DCF de las historias hoy: US$89,78 / US$54,02 / US$122,09 · Ponderado hoy: US$84,38 / US$52,08 / US$113,66 (Base / Conservador / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para UBER la diferencia es de −10% (múltiplos por debajo del DCF). Lectura del 30-sep-2026: el DCF Base de las historias (valor intrínseco principal) da US$88,85 por acción y los múltiplos, US$83,89 hoy: 6% por debajo del DCF, dentro del rango de ±25%. Ambos métodos cuentan una historia parecida; el valor intrínseco principal es el DCF Base de las historias y los múltiplos son precio relativo.

### 6.1 Coherencia del crecimiento (criterio Damodaran)

DCF inverso: con el resto de supuestos del escenario Base, el precio de US$68,91 supone que los ingresos crecen 6,1% al año en los años 1-5 (luego convergen a la perpetuidad); el DCF supone 11,4% (−5,3 pp). El precio supone menos crecimiento que el DCF: posible oportunidad si el DCF es correcto.

Cada múltiplo Base se compara con el múltiplo que implica el DCF llevado a FY+3 (US$114,87 por acción, con la misma métrica FY+3, deuda neta, acciones y dividendos de la hoja). Los dos pasan por la misma fórmula de crecimiento perpetuo (Ke 8,6%, WACC de los años 4-10 8,6%, ROE de FY+3 53,8% y conversión a caja de FY+3), así que el sesgo de la fórmula (supone el ROE de FY+3 para siempre) se cancela:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 20,6x | 15,9x | +28% | 4,6% | 3,5% | +1,1 pp | Revisar: el múltiplo vale 28% más que el DCF en FY+3 (a este nivel de múltiplo la fórmula de crecimiento casi no distingue la diferencia). |
| EV/FCFF | 14,6x | 33,9x | −57% | 1,7% | 5,5% | −3,9 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 57% por debajo del DCF en FY+3. |
| P/E | 19,0x | 15,2x | +24% | 3,4% | 2,1% | +1,3 pp | Coherente con el DCF. |
| P/FCFE | 14,3x | 17,1x | −16% | 1,4% | 2,5% | −1,1 pp | Coherente con el DCF. |
| P/OCF | 13,6x | 18,6x | −27% | 0,5% | 2,6% | −2,1 pp | Revisar: el múltiplo supone menos crecimiento que el DCF. En valor, 27% por debajo del DCF en FY+3. |

Alerta: más de 2 pp de diferencia en crecimiento implícito o más de 25% en valor. Significa que el múltiplo (o el precio) cuenta otra historia que el DCF: hay que decidir con evidencia cuál es la correcta y alinear los supuestos (revisar el DCF si la evidencia lo sostiene, o acercar el múltiplo al que implica el DCF si no). Con múltiplos altos el crecimiento implícito se acerca al costo de capital en los dos casos y casi no distingue diferencias grandes; por eso también se mira la diferencia de valor.

## 7. Sensibilidad del valor ponderado hoy (Base, lectura secundaria)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$84,38 | — |
| Múltiplos Base +20% | US$94,02 | +11,4% |
| Múltiplos Base −20% | US$74,74 | −11,4% |
| Crecimiento años 2-5 +2 pp | US$87,00 | +3,1% |
| Crecimiento años 2-5 −2 pp | US$81,36 | −3,6% |
| Margen objetivo +3 pp | US$89,22 | +5,7% |
| Margen objetivo −3 pp | US$78,89 | −6,5% |
| WACC +1 pp | US$82,06 | −2,7% |
| WACC −1 pp | US$86,19 | +2,1% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Margen objetivo −3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | 19,84 | 13,89 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 30,39 | 20,55 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | 37,67 | 24,37 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | 15,59 | 11,59 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 19,63 | 14,57 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | 32,02 | 24,39 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | 18,25 | 14,88 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 23,35 | 18,96 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | 24,05 | 19,53 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | 15,53 | 11,31 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 19,57 | 14,26 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | 32,16 | 23,42 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | 15,31 | 10,59 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 19,55 | 13,56 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | 28,80 | 19,97 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/UBER_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1R3V8gISxXCYIujVFSITu0svVBC3AsN4GF_pQHHLs5dw/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-30 (LYFT, DASH, ABNB, BKNG, GRAB, EXPE).
- [Uber: resultados 2T26](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm)
- [Uber: resultados 1T26](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000019/uberq126earningspressrelea.htm)

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
