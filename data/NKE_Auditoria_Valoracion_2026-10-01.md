---
schema: "jmr-audit-v1"
ticker: "NKE"
company: "NIKE, Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de NIKE, Inc. (NKE)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$33,96 | US$32,28 |
| **DCF Base (valor intrínseco principal)** | US$34,88 | US$32,28 |
| DCF Conservadora | US$21,68 | US$19,24 |
| DCF Disrupción | US$14,93 | US$12,74 |
| DCF Optimista | US$46,23 | US$43,36 |
| DCF esperado por probabilidades (complemento) | US$32,19 | US$29,28 |
| Precio con MOS sobre el esperado | US$20,92 | US$19,03 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,112 | 0,114 | Ventaja que se desvanece: Marca global y escala de distribución, hoy bajo presión. Evidencia: ROIC 18-47% en 2021-2026, en descenso. ROIC después del año 10 = 11,4%, punto medio entre el costo de capital terminal (9,0%) y el promedio de la industria (20,9%), sin superar el ROIC actual (13,8%): 13,8%, porque la ventaja se desvanece. |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 693,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-05-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 564,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-05-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 553,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-05-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 512,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-05-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 456,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-05-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 361,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-05-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 1.146,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-05-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-05-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,065 | 0,071 | Margen en base ajustada por arrendamientos: + 0.6 pp (ajuste del EBIT 279.1 / ventas 46398). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,110 | 0,116 | Margen en base ajustada por arrendamientos: + 0.6 pp (ajuste del EBIT 279.1 / ventas 46398). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 2,10 | 1,86 | Ventas/capital con el capital arrendado: 1/(1/2.1 + 0.0624), con VP de arrendamientos 2897.0 / ventas 46398. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 2,10 | 1,86 | Ventas/capital con el capital arrendado: 1/(1/2.1 + 0.0624), con VP de arrendamientos 2897.0 / ventas 46398. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C47 |  | =AVERAGE('Income Statement'!F13:I13) | =(AVERAGE('Income Statement'!F13:I13))+0,006016 | Margen en base ajustada por arrendamientos: + 0.6 pp (ajuste del EBIT 279.1 / ventas 46398). |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | 99,00 | LTM = ejercicio cerrado el 2026-05-31 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement I23 | Basic EPS 2024-05-31 | 3,73 | 3,76 | EPS básico del 10-K (2024-05-31); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2025-05-31 | 2,16 | 2,17 | EPS básico del 10-K (2025-05-31); antes copiaba el diluido. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores Disrupción < Conservadora < Base < Optimista | Sí |
| DCF esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al DCF esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | >$25,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$32,28 (antes US$34,88). El DCF esperado de las cuatro historias, complementario, es US$29,28 (antes US$32,19); precio con margen de seguridad sobre el esperado US$19,03. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
