---
schema: "jmr-audit-v1"
ticker: "UBER"
company: "Uber Technologies, Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Uber Technologies, Inc. (UBER)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$88,85 | US$88,97 |
| **DCF Base (valor intrínseco principal)** | US$89,63 | US$89,78 |
| DCF Conservadora | US$53,68 | US$54,02 |
| DCF Disrupción | US$28,29 | US$28,81 |
| DCF Optimista | US$122,08 | US$122,09 |
| DCF esperado por probabilidades (complemento) | US$81,00 | US$81,21 |
| Precio con MOS sobre el esperado | US$52,65 | US$52,79 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Conversor de I+D alineado al LTM | R& D converter B12 | I+D año −1 | ='Income Statement'!K10 | ='Income Statement'!J10+1655-1550 | I+D de los 12 meses a jun-2025 = 2024 (3.109) + 1S25 (1.655) − 1S24 (1.550) (10-Q). Antes el ejercicio 2025, que se solapa con el LTM. |
| Conversor de I+D alineado al LTM | R& D converter B13 | I+D año −2 | ='Income Statement'!J10 | ='Income Statement'!I10+1550-1583 | 12 meses a jun-2024 = 2023 + 1S24 − 1S23 (10-Q). Antes el ejercicio 2024. |
| Conversor de I+D alineado al LTM | R& D converter B14 | I+D año −3 | ='Income Statement'!I10 | ='Income Statement'!H10+1583-1291 | 12 meses a jun-2023 = 2022 + 1S23 − 1S22 (10-Q). Antes el ejercicio 2023. |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 288,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 265,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 262,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 232,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 226,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 194,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 1.592,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,140 | 0,142 | Margen en base ajustada por arrendamientos: + 0.22 pp (ajuste del EBIT 123.4 / ventas 55227). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,210 | 0,212 | Margen en base ajustada por arrendamientos: + 0.22 pp (ajuste del EBIT 123.4 / ventas 55227). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 2,50 | 2,29 | Ventas/capital con el capital arrendado: 1/(1/2.5 + 0.0358), con VP de arrendamientos 1974.8 / ventas 55227. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 3,50 | 3,11 | Ventas/capital con el capital arrendado: 1/(1/3.5 + 0.0358), con VP de arrendamientos 1974.8 / ventas 55227. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | =B6 | =(B6)+0,002235 | Margen en base ajustada por arrendamientos: + 0.22 pp (ajuste del EBIT 123.4 / ventas 55227). |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | -2.490,0 | LTM = ejercicio 1037.0 + acumulado al 2026-06-30 -2470.0 − acumulado del año anterior 1057.0 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement J23 | Basic EPS 2024-12-31 | 4,58 | 4,71 | EPS básico del 10-K (2024-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2025-12-31 | 4,74 | 4,82 | EPS básico del 10-K (2025-12-31); antes copiaba el diluido. |
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

El valor intrínseco principal es el DCF Base: US$89,78 (antes US$89,63). El DCF esperado de las cuatro historias, complementario, es US$81,21 (antes US$81,00); precio con margen de seguridad sobre el esperado US$52,79. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
