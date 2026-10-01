---
schema: "jmr-audit-v1"
ticker: "ZTS"
company: "Zoetis Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Zoetis Inc. (ZTS)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$117,30 | US$117,68 |
| **DCF Base (valor intrínseco principal)** | US$118,16 | US$119,82 |
| DCF Conservadora | US$65,09 | US$66,33 |
| DCF Disrupción | US$45,96 | US$47,12 |
| DCF Optimista | US$136,73 | US$138,46 |
| DCF esperado por probabilidades (complemento) | US$95,15 | US$96,62 |
| Precio con MOS sobre el esperado | US$61,85 | US$62,80 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L4 | Inversiones de corto plazo | 0,00 | 200,0 | Inversiones de corto plazo al 30-jun-2026 (10-Q 2T26); antes 0. |
| Balance del último 10-Q | Balance Sheet L5 | Caja y valores negociables | 1.476,0 | 1.676,0 | Caja 1.476 + inversiones de corto plazo 200 al 30-jun-2026 (10-Q). |
| Balance del último 10-Q | Balance Sheet L25 | Deuda de largo plazo | 9.042,0 | 9.048,0 | Deuda de largo plazo al 30-jun-2026 (10-Q); antes 9.042. |
| Balance del último 10-Q | Balance Sheet L26 | Arrendamientos de largo plazo | 196,0 | 190,0 | Arrendamientos de largo plazo al 30-jun-2026 (10-Q); antes 196. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 3.331,0 | 3.148,0 | Patrimonio al 30-jun-2026 (10-Q); antes 3.331, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 3.331,0 | 3.148,0 | Patrimonio al 30-jun-2026 (10-Q); antes 3.331, el cierre de 2025. |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 67,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 60,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 51,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 41,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 29,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 21,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 83,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,360 | 0,364 | Margen en base ajustada por arrendamientos: + 0.36 pp (ajuste del EBIT 34.0 / ventas 9517). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,360 | 0,364 | Margen en base ajustada por arrendamientos: + 0.36 pp (ajuste del EBIT 34.0 / ventas 9517). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 2,00 | 1,91 | Ventas/capital con el capital arrendado: 1/(1/2 + 0.0243), con VP de arrendamientos 231.2 / ventas 9517. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 2,00 | 1,91 | Ventas/capital con el capital arrendado: 1/(1/2 + 0.0243), con VP de arrendamientos 231.2 / ventas 9517. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | 0,330 | 0,334 | Margen en base ajustada por arrendamientos: + 0.36 pp (ajuste del EBIT 34.0 / ventas 9517). |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C47 |  | 0,380 | 0,384 | Margen en base ajustada por arrendamientos: + 0.36 pp (ajuste del EBIT 34.0 / ventas 9517). |
| Flujos LTM | Cash Flow Statement L13 | Cash from Operating Activities | 2.887,0 | 2.840,0 | LTM = ejercicio 2904.0 + acumulado al 2026-06-30 1056.0 − acumulado del año anterior 1120.0 (NetCashProvidedByUsedInOperatingActivities). Antes 2887. |
| Flujos LTM | Cash Flow Statement L22 | Cash from Investing Activities | -713,0 | -720,0 | LTM = ejercicio -748.0 + acumulado al 2026-06-30 -387.0 − acumulado del año anterior -415.0 (NetCashProvidedByUsedInInvestingActivities). Antes -713. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | -167,0 | LTM = ejercicio 325.0 + acumulado al 2026-06-30 -974.0 − acumulado del año anterior -482.0 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement I23 | Basic EPS 2023-12-31 | 5,07 | 5,08 | EPS básico del 10-K (2023-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2025-12-31 | 6,02 | 6,03 | EPS básico del 10-K (2025-12-31); antes copiaba el diluido. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores Disrupción < Conservadora < Base < Optimista | Sí |
| DCF esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al DCF esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $4,500-7,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$119,82 (antes US$118,16). El DCF esperado de las cuatro historias, complementario, es US$96,62 (antes US$95,15); precio con margen de seguridad sobre el esperado US$62,80. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
