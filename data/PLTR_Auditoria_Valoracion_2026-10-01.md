---
schema: "jmr-audit-v1"
ticker: "PLTR"
company: "Palantir Technologies Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Palantir Technologies Inc. (PLTR)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$85,42 | US$72,60 |
| **DCF Base (valor intrínseco principal)** | US$55,62 | US$72,60 |
| DCF Conservadora | US$26,93 | US$33,36 |
| DCF Disrupción | US$15,72 | US$14,68 |
| DCF Optimista | US$95,62 | US$128,41 |
| DCF esperado por probabilidades (complemento) | US$51,02 | US$66,20 |
| Precio con MOS sobre el esperado | US$33,16 | US$43,03 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Conversor de I+D alineado al LTM | R& D converter B12 | I+D año −1 | ='Income Statement'!K10 | ='Income Statement'!J10+269,932-218,821 | I+D de los 12 meses a jun-2025 = 2024 (507,9) + 1S25 (269,9) − 1S24 (218,8) (10-Q). Antes el ejercicio 2025, que se solapa con el LTM. |
| Conversor de I+D alineado al LTM | R& D converter B13 | I+D año −2 | ='Income Statement'!J10 | ='Income Statement'!I10+218,821-189,633 | 12 meses a jun-2024 = 2023 + 1S24 − 1S23 (10-Q). Antes el ejercicio 2024. |
| Conversor de I+D alineado al LTM | R& D converter B14 | I+D año −3 | ='Income Statement'!I10 | ='Income Statement'!H10+189,633-176,772 | 12 meses a jun-2023 = 2022 + 1S23 − 1S22 (10-Q). Antes el ejercicio 2023. |
| ROIC terminal (criterio Damodaran) | Input sheet B49 | ¿ROIC terminal propio? | No | Yes | Ventaja durable: Costos de cambio: plataformas integradas en los procesos de defensa, inteligencia y grandes empresas (Gotham, Foundry, AIP). Evidencia: ROIC sobre el capital operativo (sin la caja) muy por encima del costo de capital en 2023-2025 y LTM: el negocio casi no necesita capital; el 5-12% anterior incluía la caja en el capital, contra el criterio de Damodaran. ROIC después del año 10 = el promedio de la industria (29,3%), sin superar el ROIC actual (150,0%): 29,3% (Damodaran, Investment Valuation, cap. 12). |
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,200 | 0,293 | Ventaja durable: Costos de cambio: plataformas integradas en los procesos de defensa, inteligencia y grandes empresas (Gotham, Foundry, AIP). Evidencia: ROIC sobre el capital operativo (sin la caja) muy por encima del costo de capital en 2023-2025 y LTM: el negocio casi no necesita capital; el 5-12% anterior incluía la caja en el capital, contra el criterio de Damodaran. ROIC después del año 10 = el promedio de la industria (29,3%), sin superar el ROIC actual (150,0%): 29,3% (Damodaran, Investment Valuation, cap. 12). |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 57,20 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 62,08 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 50,43 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 29,55 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 24,94 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 33,32 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 92,22 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,480 | 0,484 | Margen en base ajustada por arrendamientos: + 0.38 pp (ajuste del EBIT 23.5 / ventas 6155.9). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,480 | 0,484 | Margen en base ajustada por arrendamientos: + 0.38 pp (ajuste del EBIT 23.5 / ventas 6155.9). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 4,00 | 3,47 | Ventas/capital con el capital arrendado: 1/(1/4 + 0.0384), con VP de arrendamientos 236.1 / ventas 6155.9. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 4,50 | 3,84 | Ventas/capital con el capital arrendado: 1/(1/4.5 + 0.0384), con VP de arrendamientos 236.1 / ventas 6155.9. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | =B6 | =(B6)+0,003813 | Margen en base ajustada por arrendamientos: + 0.38 pp (ajuste del EBIT 23.5 / ventas 6155.9). |
| Acciones: dilución y estructura de capital | Input sheet B22 |  | ='Income Statement'!L27 | ='Income Statement'!L27+168,9 | Acciones con dilución: 2.402,9 millones más 168,9 millones de opciones y acciones restringidas (diluidas − básicas del 2T26, 10-Q). La hoja no restaba el valor de las opciones. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | 1.117,7 | 1.112,1 | LTM = ejercicio -668.5 + acumulado al 2026-06-30 611.9 − acumulado del año anterior -1168.7 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes 1117.738. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores Disrupción < Conservadora < Base < Optimista | Sí |
| DCF esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al DCF esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $3,000-4,500 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$72,60 (antes US$55,62). El DCF esperado de las cuatro historias, complementario, es US$66,20 (antes US$51,02); precio con margen de seguridad sobre el esperado US$43,03. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
