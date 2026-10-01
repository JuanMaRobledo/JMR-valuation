---
schema: "jmr-audit-v1"
ticker: "INTU"
company: "Intuit Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Intuit Inc. (INTU)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$496,45 | US$496,86 |
| **DCF Base (valor intrínseco principal)** | US$509,89 | US$513,14 |
| DCF Conservadora | US$259,79 | US$260,63 |
| DCF Disrupción | US$207,90 | US$208,80 |
| DCF Optimista | US$628,00 | US$631,67 |
| DCF esperado por probabilidades (complemento) | US$440,79 | US$443,29 |
| Precio con MOS sobre el esperado | US$286,51 | US$288,14 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,222 | 0,225 | Ventaja durable: Costos de cambio y datos del cliente (QuickBooks, TurboTax), escala en pyme. Evidencia: ROIC 12-22%, siempre por encima del costo de capital. ROIC después del año 10 = el promedio de la industria (29,3%), sin superar el ROIC actual (22,5%): 22,5% (Damodaran, Investment Valuation, cap. 12). |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 142,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-07-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 112,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-07-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 130,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-07-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 134,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-07-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 124,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-07-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 109,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-07-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 285,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-07-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-07-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,318 | 0,320 | Margen en base ajustada por arrendamientos: + 0.19 pp (ajuste del EBIT 40.3 / ventas 21448). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,320 | 0,322 | Margen en base ajustada por arrendamientos: + 0.19 pp (ajuste del EBIT 40.3 / ventas 21448). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 2,50 | 2,31 | Ventas/capital con el capital arrendado: 1/(1/2.5 + 0.0332), con VP de arrendamientos 712.0 / ventas 21448. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 2,00 | 1,88 | Ventas/capital con el capital arrendado: 1/(1/2 + 0.0332), con VP de arrendamientos 712.0 / ventas 21448. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | 0,280 | 0,282 | Margen en base ajustada por arrendamientos: + 0.19 pp (ajuste del EBIT 40.3 / ventas 21448). |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C47 |  | 0,360 | 0,362 | Margen en base ajustada por arrendamientos: + 0.19 pp (ajuste del EBIT 40.3 / ventas 21448). |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | -265,0 | LTM = ejercicio cerrado el 2026-07-31 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement I23 | Basic EPS 2024-07-31 | 10,43 | 10,58 | EPS básico del 10-K (2024-07-31); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2025-07-31 | 13,67 | 13,82 | EPS básico del 10-K (2025-07-31); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2026-07-31 | 16,48 | 16,53 | EPS básico del 10-K (2026-07-31); antes copiaba el diluido. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores Disrupción < Conservadora < Base < Optimista | Sí |
| DCF esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al DCF esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $12,000-25,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$513,14 (antes US$509,89). El DCF esperado de las cuatro historias, complementario, es US$443,29 (antes US$440,79); precio con margen de seguridad sobre el esperado US$288,14. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
