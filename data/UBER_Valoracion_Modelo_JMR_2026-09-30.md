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

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$111,44 en el escenario Base (rango US$47,97–US$188,22). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$124,94 (+12% frente al DCF). Con los pesos de la categoría «Madura» (40% DCF, 60% múltiplos), el valor intrínseco ponderado hoy es US$119,54, frente a un precio de referencia de US$68,16 (+75%).

Los múltiplos (US$124,94 hoy) quedan 12% por encima del DCF (US$111,44), dentro del rango de ±25%: ambos métodos coinciden. Los dos quedan muy por encima del precio (US$68,16): el mercado descuenta riesgos que el escenario Base no incorpora del todo, sobre todo la competencia de los robotaxis. Dentro de los múltiplos hay dispersión: EV/EBITDA da US$152 y EV/FCFF US$78, porque el EBITDA de FY+3 de la hoja crece más que el flujo de caja; los métodos de flujo son la referencia más prudente.

| Escenario | DCF hoy | Múltiplos consolidados hoy | Valor intrínseco ponderado hoy | Compra con MOS hoy | Precio objetivo FY+3 ponderado |
|---|---:|---:|---:|---:|---:|
| Conservador | US$47,97 | US$65,81 | US$58,67 | US$38,14 | US$72,43 |
| Base | US$111,44 | US$124,94 | US$119,54 | US$77,70 | US$167,84 |
| Optimista | US$188,22 | US$194,20 | US$191,80 | US$124,67 | US$284,86 |

## 2. Datos

- Hoja del modelo: [UBER plantilla maestra](https://docs.google.com/spreadsheets/d/1R3V8gISxXCYIujVFSITu0svVBC3AsN4GF_pQHHLs5dw/edit).
- Análisis del 14 de sept de 2026. Precio de referencia de la hoja: US$68,16.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | 8,0% | 13,0% | 18,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | 8,0% | 11,0% | 18,0% | Input B29 |
| Margen EBIT objetivo | 13,1% | 26,0% | 31,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 3,00 / 3,50 | — | Input B32/B33 |
| DCF por acción hoy | US$47,97 | US$111,44 | US$188,22 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 0,80, ERP 4,46%, Ke 8,56%, costo de la deuda después de impuestos 4,21%, peso del patrimonio 91,5%, WACC inicial 8,19% y terminal 9,22%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Uber es rentable desde 2023; los cierres anteriores tienen EBITDA y utilidad negativos. La etapa actual es Dec '23 a LTM. En P/E se quita Dec '24: la utilidad de 2024 incluye la liberación de ~US$6.400 millones de la reserva de impuestos diferidos, que baja el P/E a 13x. La utilidad del LTM incluye revaluaciones de sus participaciones (Didi, Grab, Aurora) que se compensan entre trimestres (−US$1.500 millones en el 1T26, +US$1.600 millones en el 2T26). Se excluye la columna sin fecha de la hoja. B: plataformas de movilidad, reparto y viajes (DoorDash, Airbnb, Booking, Grab, Expedia), datos de yfinance al 29-sep-2026. Se excluye Lyft (P/E de 2x por la liberación de su reserva de impuestos; EV/EBITDA de 112x) y, en P/E, DoorDash (98x con margen de 4%). Sin ajuste: Uber crece ~15-18% con margen creciente, en la mitad del grupo (más que Booking y Expedia, menos que DoorDash). λ = 0,10: C es inestable. Con un Ke de 8,6% y g de 6,7%, Ke − g es de apenas 1,9 pp y el justificado se dispara (P/E de 51x, EV/EBITDA de 43x); se le da poco peso.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 32,6x | 25,3x (n=5: DASH 52,4x, ABNB 29,9x, BKNG 12,2x, GRAB 25,3x, EXPE 10,9x) × 1,00 = 25,3x | 29,8x / 43,4x / — | 19,8x | **30,4x** | 37,7x | —x / —x / —x |
| EV/FCFF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 19,1x (EV/FCF × 1,03 = FCF después de intereses ÷ FCFF) | 12,2x (n=3: DASH 35,2x, BKNG 12,2x, EXPE 6,7x) × 1,00 = 12,2x | 38,1x / 55,5x / — | 15,6x | **19,6x** | 32,0x | —x / —x / —x |
| P/E | mediana Dec '23, Dec '25, LTM (etapa actual) = 17,2x | 23,2x (n=4: ABNB 35,8x, BKNG 18,0x, GRAB 28,4x, EXPE 16,7x) × 1,00 = 23,2x | 32,8x / 51,5x / — | 18,2x | **23,4x** | 24,1x | —x / —x / —x |
| P/FCFE | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 17,9x | 12,8x (n=3: DASH 37,9x, BKNG 12,8x, EXPE 7,2x) × 1,00 = 12,8x | 39,1x / 57,7x / — | 15,5x | **19,6x** | 32,2x | —x / —x / —x |
| P/OCF | mediana Dec '23, Dec '24, Dec '25, LTM (etapa actual) = 17,3x | 12,4x (n=3: DASH 28,6x, BKNG 12,4x, EXPE 6,1x) × 1,00 = 12,4x | 42,2x / 62,1x / — | 15,3x | **19,6x** | 28,8x | —x / —x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 30,4x: promedio de historia y peers 28,9x, acercado 10% al justificado (43,4x); rango de anclas 25,3x–43,4x. Atípicos excluidos de la historia: Dec '18 (-0,2x: métrica negativa o ~0); Dec '19 (-5,8x: métrica negativa o ~0); Dec '20 (-22,8x: métrica negativa o ~0); Dec '21 (-30,1x: métrica negativa o ~0); Dec '22 (-63,7x: métrica negativa o ~0); Dec '17 (1,2x: < 0,4x la mediana (27.6x), caída puntual); Dec '23 (69,3x: > 2,5x la mediana (27.6x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 19,6x: promedio de historia y peers 15,7x, acercado 10% al justificado (55,5x); rango de anclas 12,2x–55,5x. Atípicos excluidos de la historia: Dec '18 (-0,2x: métrica negativa o ~0); Dec '19 (-9,7x: métrica negativa o ~0); Dec '20 (-29,1x: métrica negativa o ~0); Dec '21 (-119,0x: métrica negativa o ~0); Dec '17 (2,0x: < 0,4x la mediana (18.5x), caída puntual); Dec '22 (144,5x: > 2,5x la mediana (18.5x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 23,4x: promedio de historia y peers 20,2x, acercado 10% al justificado (51,5x); rango de anclas 17,2x–51,5x. Atípicos excluidos de la historia: Dec '17 (0,0x: métrica negativa o ~0); Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (-4,4x: métrica negativa o ~0); Dec '20 (-13,2x: métrica negativa o ~0); Dec '21 (-161,3x: métrica negativa o ~0); Dec '22 (-5,3x: métrica negativa o ~0); Dec '23 (68,4x: > 2,5x la mediana (16.3x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 19,6x: promedio de historia y peers 15,3x, acercado 10% al justificado (57,7x); rango de anclas 12,8x–57,7x. Atípicos excluidos de la historia: Dec '17 (0,0x: métrica negativa o ~0); Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (-10,4x: métrica negativa o ~0); Dec '20 (-28,1x: métrica negativa o ~0); Dec '21 (-110,0x: métrica negativa o ~0); Dec '22 (127,2x: > 2,5x la mediana (18.4x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 19,6x: promedio de historia y peers 14,8x, acercado 10% al justificado (62,1x); rango de anclas 12,4x–62,1x. Atípicos excluidos de la historia: Dec '17 (0,0x: métrica negativa o ~0); Dec '18 (0,0x: métrica negativa o ~0); Dec '19 (-11,8x: métrica negativa o ~0); Dec '20 (-34,4x: métrica negativa o ~0); Dec '21 (-183,7x: métrica negativa o ~0); Dec '22 (77,2x: > 2,5x la mediana (17.8x)).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$124,94 frente a US$111,44 del DCF (+12%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$124,94 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$61,37 | US$142,56 | US$240,78 |
| EV/EBITDA | 20% | US$88,01 | US$224,59 | US$371,20 |
| EV/FCFF | 10% | US$54,43 | US$113,78 | US$251,67 |
| P/E | 20% | US$82,62 | US$184,30 | US$255,72 |
| P/FCFE | 5% | US$86,79 | US$183,10 | US$421,02 |
| P/OCF | 5% | US$79,39 | US$169,99 | US$338,90 |
| **Ponderado FY+3** | 100% | US$72,43 | US$167,84 | US$284,86 |

Valor presente (Ke 8,56%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$77,14 | US$72,09 | US$68,80 | US$72,68 | OK |
| EV/EBITDA | Base | US$123,07 | US$158,16 | US$175,56 | US$152,26 | OK |
| EV/EBITDA | Optimista | US$159,03 | US$238,58 | US$290,17 | US$229,26 | OK |
| EV/FCFF | Conservador | US$47,81 | US$44,59 | US$42,55 | US$44,99 | OK |
| EV/FCFF | Base | US$64,60 | US$80,60 | US$88,95 | US$78,05 | OK |
| EV/FCFF | Optimista | US$112,35 | US$163,28 | US$196,73 | US$157,45 | OK |
| P/E | Conservador | US$71,84 | US$67,67 | US$64,59 | US$68,03 | OK |
| P/E | Base | US$96,18 | US$128,45 | US$144,07 | US$122,90 | OK |
| P/E | Optimista | US$103,44 | US$162,50 | US$199,90 | US$155,28 | OK |
| P/FCFE | Conservador | US$75,53 | US$70,94 | US$67,84 | US$71,44 | OK |
| P/FCFE | Base | US$106,95 | US$130,23 | US$143,13 | US$126,77 | OK |
| P/FCFE | Optimista | US$195,07 | US$275,87 | US$329,12 | US$266,69 | OK |
| P/OCF | Conservador | US$69,31 | US$64,95 | US$62,06 | US$65,44 | OK |
| P/OCF | Base | US$94,50 | US$119,93 | US$132,88 | US$115,77 | OK |
| P/OCF | Optimista | US$148,03 | US$218,85 | US$264,92 | US$210,60 | OK |

Múltiplos consolidados hoy: US$65,81 / US$124,94 / US$194,20 · DCF hoy: US$47,97 / US$111,44 / US$188,22 · Ponderado hoy: US$58,67 / US$119,54 / US$191,80 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para UBER la diferencia es de +12% (múltiplos por encima del DCF). Los múltiplos (US$124,94 hoy) quedan 12% por encima del DCF (US$111,44), dentro del rango de ±25%: ambos métodos coinciden. Los dos quedan muy por encima del precio (US$68,16): el mercado descuenta riesgos que el escenario Base no incorpora del todo, sobre todo la competencia de los robotaxis. Dentro de los múltiplos hay dispersión: EV/EBITDA da US$152 y EV/FCFF US$78, porque el EBITDA de FY+3 de la hoja crece más que el flujo de caja; los métodos de flujo son la referencia más prudente.

## 7. Sensibilidad del valor ponderado hoy (Base)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$119,54 | — |
| Múltiplos Base +20% | US$134,49 | +12,5% |
| Múltiplos Base −20% | US$104,60 | −12,5% |
| Crecimiento años 1-5 +2 pp | US$124,35 | +4,0% |
| Crecimiento años 1-5 −2 pp | US$115,19 | −3,6% |
| Margen objetivo +3 pp | US$124,82 | +4,4% |
| Margen objetivo −3 pp | US$114,27 | −4,4% |
| WACC +1 pp | US$117,02 | −2,1% |
| WACC −1 pp | US$122,25 | +2,3% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base −20%, Múltiplos Base +20%, Margen objetivo −3 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 19,84 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | — | 30,39 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 37,67 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 15,59 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | — | 19,63 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 32,02 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 18,25 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | — | 23,35 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 24,05 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 15,53 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | — | 19,57 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 32,16 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 15,31 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | — | 19,55 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 28,80 | Múltiplo optimista elegido con el protocolo v3 |
| Supuestos de los Múltiplos | A3, A12 | texto anterior | síntesis y chequeo de independencia | Documentación (paso 6.5) |
| Tesis de Inversión y Supuestos | bloque «Origen de los múltiplos» | — | tabla de origen | Paso 10.d |

Respaldo de los valores anteriores: `JMR-valuation/reference/multiplos_v3/UBER_respaldo.json`.

## 9. Fuentes

- Hoja del Modelo JMR: https://docs.google.com/spreadsheets/d/1R3V8gISxXCYIujVFSITu0svVBC3AsN4GF_pQHHLs5dw/edit
- Múltiplos de peers: Yahoo Finance vía yfinance, consultado el 2026-09-29 (LYFT, DASH, ABNB, BKNG, GRAB, EXPE).
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
