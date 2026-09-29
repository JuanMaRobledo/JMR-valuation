---
schema: "jmr-valuation-v3"
title: "Valoración Modelo JMR de Zoetis Inc."
ticker: "ZTS"
analysis_date: "2026-09-29"
sheet: "https://docs.google.com/spreadsheets/d/1MYnJJfv2G9R5u4roWPYb855tFs3K0Mqt2vxCPNkXKPE/edit"
generator: "Claude Code — prompt de valoración v3 (pasos 6, 7, 8, 10 y 11 sobre una valoración existente)"
---

# Zoetis Inc. (ZTS) — Valoración Modelo JMR · prompt v3

> Estimación condicionada a los supuestos declarados; no es asesoría financiera ni una recomendación.
> Alcance de esta actualización: se aplicaron los pasos nuevos del prompt v3 (selección razonada de los múltiplos, valor presente de los múltiplos, ponderación y documentación) sobre la valoración existente. Los supuestos del DCF no se modificaron; se verificó que Conservador < Base < Optimista.

## 1. Resumen

Con los supuestos vigentes, el DCF de Damodaran da un valor por acción hoy de US$85,57 en el escenario Base (rango US$55,25–US$99,97). Los cinco múltiplos, elegidos con anclas de mercado y fundamentales y traídos a valor presente en 1, 2 y 3 años, dan US$111,20 (+30% frente al DCF). Con los pesos de la categoría «Madura» (40% DCF, 60% múltiplos), el valor intrínseco ponderado hoy es US$100,95, frente a un precio de referencia de US$71,43 (+41%).

Los múltiplos (US$111,20 hoy) quedan 30% por encima del DCF (US$85,57); el precio (US$71,43) está por debajo de ambos. Los múltiplos suponen que, a FY+3, Zoetis cotiza entre su valoración actual y la de sus peers ajustados (~14x EBITDA, ~23x utilidad), cerca de su múltiplo justificado (~25x utilidad), es decir que el mercado deja atrás las dudas sobre Librela. El DCF y el precio de hoy reflejan que la presión dura más. Si Librela se estabiliza, los múltiplos son razonables; si no, el DCF es la referencia más prudente.

| Escenario | DCF hoy | Múltiplos consolidados hoy | Valor intrínseco ponderado hoy | Compra con MOS hoy | Precio objetivo FY+3 ponderado |
|---|---:|---:|---:|---:|---:|
| Conservador | US$55,25 | US$79,61 | US$69,87 | US$45,41 | US$85,68 |
| Base | US$85,57 | US$111,20 | US$100,95 | US$65,62 | US$130,33 |
| Optimista | US$99,97 | US$132,48 | US$119,48 | US$77,66 | US$156,29 |

## 2. Datos

- Hoja del modelo: [Modelo JMR - ZTS](https://docs.google.com/spreadsheets/d/1MYnJJfv2G9R5u4roWPYb855tFs3K0Mqt2vxCPNkXKPE/edit).
- Análisis del 25 de sept de 2026. Precio de referencia de la hoja: US$71,43.
- Peers: datos de mercado de yfinance consultados el 2026-09-29 (P/E trailing, EV/EBITDA, y P/FCF, EV/FCF y P/OCF con flujo operativo y capex de los últimos cuatro trimestres, la misma definición que 'Trailing Valuation').
- Estados financieros y conciliación: los de la valoración vigente (SEC EDGAR vía `refresh_native_model.py`); esta actualización no los modificó.

## 3. Supuestos del DCF y costo de capital

| Supuesto | Conservador | Base | Optimista | Celda |
|---|---:|---:|---:|---|
| Crecimiento año 1 | -1,0% | 2,0% | 6,0% | Input B27; Valuation output C55/C106 |
| Crecimiento años 2-5 | -1,0% | 5,0% | 6,0% | Input B29 |
| Margen EBIT objetivo | 33,0% | 36,0% | 38,0% | Input B30; Valuation output C45/C47 |
| Año de convergencia del margen | 5 | 5 | 5 | Input B31 |
| Sales-to-capital años 1-5 / 6-10 | — | 2,00 / 2,00 | — | Input B32/B33 |
| DCF por acción hoy | US$55,25 | US$85,57 | US$99,97 | Valuation output B86/B35/B137 |

Costo de capital: tasa libre de riesgo 4,99%, beta apalancada 0,90, ERP 4,46%, Ke 9,00%, costo de la deuda después de impuestos 4,88%, peso del patrimonio 80,1%, WACC inicial 8,18% y terminal 9,00%. La justificación de cada supuesto está en «Tesis de Inversión y Supuestos» y «Origen de los Supuestos» de la hoja.

## 4. Múltiplos: selección y origen

A: Zoetis cotizó a 18-38x EBITDA y 29-57x utilidades como líder de salud animal con crecimiento estable. En 2026 recortó dos veces su guía (ingresos de US$9.680-9.960 millones) por las dudas de seguridad de Librela, la caída de sus anticuerpos para osteoartritis canina (−24%) y menos visitas a veterinarios; la acción cae ~25% en el año. La etapa actual es Dec '25 y el LTM. B: salud animal y diagnóstico (IDEXX, Elanco, Phibro, Merck, Abbott), datos de yfinance al 29-sep-2026. Se excluye Neogen (margen casi cero), Merck en P/E (119x por cargos puntuales) y Phibro en los múltiplos de flujo libre (P/FCF de 146x por un año de capex alto). Ajuste −15%: Zoetis crece ~2-5% en 2026 (la mitad de IDEXX y Abbott) y tiene el riesgo de Librela; conserva los márgenes más altos del grupo. λ = 0,25: la Zoetis de FY+3 del escenario Base es una empresa de salud animal de crecimiento medio, parecida a la de hoy.

| Método | A · historia | B · peers (ajustada) | C · justificado Cons/Base/Opt | Conservador | Base | Optimista | Antes (J8/J19/J30) |
|---|---|---|---|---:|---:|---:|---|
| EV/EBITDA | mediana Dec '25, LTM (etapa actual) = 12,1x | 14,8x (n=5: IDXX 26,5x, ELAN 14,8x, PAHC 8,8x, MRK 14,4x, ABT 17,3x) × 0,85 = 12,6x | 12,7x / 18,3x / 20,0x | 11,7x | **13,8x** | 15,6x | —x / 9,3x / —x |
| EV/FCFF | mediana Dec '25, LTM (etapa actual) = 19,5x (EV/FCF × 0,93 = FCF después de intereses ÷ FCFF) | 26,1x (n=4: IDXX 33,9x, ELAN 26,0x, MRK 23,8x, ABT 26,3x) × 0,85 = 22,2x | 19,7x / 29,7x / 32,4x | 19,3x | **23,1x** | 25,4x | —x / 15,7x / —x |
| P/E | mediana Dec '25, LTM (etapa actual) = 16,5x | 32,7x (n=3: IDXX 37,5x, PAHC 14,6x, ABT 32,7x) × 0,85 = 27,8x | 17,2x / 24,6x / 26,7x | 17,4x | **22,8x** | 24,9x | —x / 12,1x / —x |
| P/FCFE | mediana Dec '25, LTM (etapa actual) = 17,9x | 26,7x (n=4: IDXX 34,0x, ELAN 29,8x, MRK 22,9x, ABT 23,7x) × 0,85 = 22,7x | 18,0x / 26,2x / 28,3x | 17,5x | **21,8x** | 24,6x | —x / 12,4x / —x |
| P/OCF | mediana Dec '25, LTM (etapa actual) = 14,3x | 18,5x (n=5: IDXX 30,6x, ELAN 18,3x, PAHC 20,9x, MRK 18,4x, ABT 18,5x) × 0,85 = 15,7x | 13,2x / 23,8x / 26,6x | 13,8x | **17,2x** | 19,4x | —x / 10,2x / —x |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Múltiplo justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), P/E = (1 − g/ROE)(1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

- **EV/EBITDA.** Base 13,8x: promedio de historia y peers 12,3x, acercado 25% al justificado (18,3x); rango de anclas 12,1x–18,3x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **EV/FCFF.** Base 23,1x: promedio de historia y peers 20,9x, acercado 25% al justificado (29,7x); rango de anclas 19,5x–29,7x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/E.** Base 22,8x: promedio de historia y peers 22,1x, acercado 25% al justificado (24,6x); rango de anclas 16,5x–27,8x. Atípicos excluidos de la historia: LTM (12,1x: < 0,4x la mediana (32.6x), caída puntual).  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/FCFE.** Base 21,8x: promedio de historia y peers 20,3x, acercado 25% al justificado (26,2x); rango de anclas 17,9x–26,2x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.
- **P/OCF.** Base 17,2x: promedio de historia y peers 15,0x, acercado 25% al justificado (23,8x); rango de anclas 14,3x–23,8x. Atípicos excluidos de la historia: ninguno.  Lo cambiaría: una revisión de la mediana de peers o del crecimiento de largo plazo, o que la empresa salga de la etapa actual.

Chequeo de independencia: los múltiplos consolidados hoy (Base) dan US$111,20 frente a US$85,57 del DCF (+30%). Ningún múltiplo se derivó del DCF ni se ajustó después de verlo; el recálculo independiente del informe da US$111,20 para los múltiplos Base.

## 5. Resultados

Precio al cierre de FY+3 (con dividendos acumulados, sin descontar), por método y escenario:

| Método | Peso | Conservador | Base | Optimista |
|---|---:|---:|---:|---:|
| DCF Damodaran | 40% | US$71,56 | US$110,83 | US$129,48 |
| EV/EBITDA | 20% | US$87,07 | US$128,09 | US$159,08 |
| EV/FCFF | 10% | US$92,83 | US$132,33 | US$160,24 |
| P/E | 20% | US$103,33 | US$160,21 | US$190,49 |
| P/FCFE | 5% | US$93,63 | US$161,11 | US$200,90 |
| P/OCF | 5% | US$100,32 | US$140,86 | US$170,29 |
| **Ponderado FY+3** | 100% | US$85,68 | US$130,33 | US$156,29 |

Valor presente (Ke 9,00%; consolidado por método: Promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Conservador | US$80,43 | US$72,62 | US$67,22 | US$73,43 | OK |
| EV/EBITDA | Base | US$100,57 | US$99,61 | US$98,90 | US$99,69 | OK |
| EV/EBITDA | Optimista | US$119,92 | US$121,94 | US$122,83 | US$121,56 | OK |
| EV/FCFF | Conservador | US$87,30 | US$77,93 | US$71,67 | US$78,97 | OK |
| EV/FCFF | Base | US$107,46 | US$103,05 | US$102,17 | US$104,23 | OK |
| EV/FCFF | Optimista | US$119,95 | US$122,51 | US$123,72 | US$122,06 | OK |
| P/E | Conservador | US$92,43 | US$85,02 | US$79,78 | US$85,74 | OK |
| P/E | Base | US$124,13 | US$123,92 | US$123,70 | US$123,91 | OK |
| P/E | Optimista | US$141,09 | US$144,89 | US$147,08 | US$144,35 | OK |
| P/FCFE | Conservador | US$84,14 | US$76,99 | US$72,29 | US$77,80 | OK |
| P/FCFE | Base | US$116,53 | US$124,71 | US$124,39 | US$121,88 | OK |
| P/FCFE | Optimista | US$150,02 | US$153,13 | US$155,12 | US$152,76 | OK |
| P/OCF | Conservador | US$89,13 | US$82,27 | US$77,46 | US$82,95 | OK |
| P/OCF | Base | US$111,34 | US$108,73 | US$108,75 | US$109,61 | OK |
| P/OCF | Optimista | US$126,70 | US$129,54 | US$131,48 | US$129,24 | OK |

Múltiplos consolidados hoy: US$79,61 / US$111,20 / US$132,48 · DCF hoy: US$55,25 / US$85,57 / US$99,97 · Ponderado hoy: US$69,87 / US$100,95 / US$119,48 (Conservador / Base / Optimista). Chequeo VP a 3 años < FY+3 sin descontar: conservador OK, base OK, optimista OK.

## 6. DCF frente a múltiplos

En la lectura de Damodaran, el DCF estima el valor intrínseco a partir de flujos y riesgo, y los múltiplos muestran cuánto pagaría el mercado por negocios comparables. Para ZTS la diferencia es de +30% (múltiplos por encima del DCF). Los múltiplos (US$111,20 hoy) quedan 30% por encima del DCF (US$85,57); el precio (US$71,43) está por debajo de ambos. Los múltiplos suponen que, a FY+3, Zoetis cotiza entre su valoración actual y la de sus peers ajustados (~14x EBITDA, ~23x utilidad), cerca de su múltiplo justificado (~25x utilidad), es decir que el mercado deja atrás las dudas sobre Librela. El DCF y el precio de hoy reflejan que la presión dura más. Si Librela se estabiliza, los múltiplos son razonables; si no, el DCF es la referencia más prudente.

## 7. Sensibilidad del valor ponderado hoy (Base)

| Cambio | Valor ponderado hoy | Variación |
|---|---:|---:|
| Vigente | US$100,95 | — |
| Múltiplos Base +20% | US$114,64 | +13,6% |
| Múltiplos Base −20% | US$87,25 | −13,6% |
| Crecimiento años 1-5 +2 pp | US$105,44 | +4,4% |
| Crecimiento años 1-5 −2 pp | US$96,90 | −4,0% |
| Margen objetivo +3 pp | US$104,11 | +3,1% |
| Margen objetivo −3 pp | US$97,79 | −3,1% |
| WACC +1 pp | US$98,76 | −2,2% |
| WACC −1 pp | US$103,28 | +2,3% |

Los cambios de crecimiento, margen y WACC se estimaron con el motor de la Calculadora (crecimiento único para los años 1-5) y se aplicaron como variación relativa al DCF de la hoja; los de múltiplos se calcularon con las fórmulas de las hojas.
Supuestos más frágiles: Múltiplos Base +20%, Múltiplos Base −20%, Crecimiento años 1-5 +2 pp.

## 8. Log de cambios en la hoja

| Hoja | Celda | Valor anterior | Valor nuevo | Motivo |
|---|---|---:|---:|---|
| EVEBITDA | J8 | — | 11,74 | Múltiplo conservador elegido con el protocolo v3 |
| EVEBITDA | J19 | 9,30 | 13,83 | Múltiplo base elegido con el protocolo v3 |
| EVEBITDA | J30 | — | 15,56 | Múltiplo optimista elegido con el protocolo v3 |
| EVFCFF | J8 | — | 19,29 | Múltiplo conservador elegido con el protocolo v3 |
| EVFCFF | J19 | 15,69 | 23,07 | Múltiplo base elegido con el protocolo v3 |
| EVFCFF | J30 | — | 25,35 | Múltiplo optimista elegido con el protocolo v3 |
| PE | J8 | — | 17,35 | Múltiplo conservador elegido con el protocolo v3 |
| PE | J19 | 12,06 | 22,76 | Múltiplo base elegido con el protocolo v3 |
| PE | J30 | — | 24,95 | Múltiplo optimista elegido con el protocolo v3 |
| PFCFE | J8 | — | 17,53 | Múltiplo conservador elegido con el protocolo v3 |
| PFCFE | J19 | 12,41 | 21,79 | Múltiplo base elegido con el protocolo v3 |
| PFCFE | J30 | — | 24,59 | Múltiplo optimista elegido con el protocolo v3 |
| POCF | J8 | — | 13,80 | Múltiplo conservador elegido con el protocolo v3 |
| POCF | J19 | 10,17 | 17,20 | Múltiplo base elegido con el protocolo v3 |
| POCF | J30 | — | 19,43 | Múltiplo optimista elegido con el protocolo v3 |
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
