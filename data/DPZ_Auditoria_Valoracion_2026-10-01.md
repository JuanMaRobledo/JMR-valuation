---
schema: "jmr-audit-v1"
ticker: "DPZ"
company: "Domino's Pizza, Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Domino's Pizza, Inc. (DPZ)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$349,85 | US$323,13 |
| **DCF Base (valor intrínseco principal)** | US$352,14 | US$323,13 |
| DCF Conservadora | US$172,24 | US$153,81 |
| DCF Disrupción | US$108,74 | US$93,61 |
| DCF Optimista | US$420,89 | US$387,75 |
| DCF esperado por probabilidades (complemento) | US$308,75 | US$282,25 |
| Precio con MOS sobre el esperado | US$200,69 | US$183,46 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L20 | Deuda corriente | 6,10 | 7,00 | Porción corriente de deuda y arrendamientos financieros al 14-jun-2026 (10-Q 2T26). |
| Balance del último 10-Q | Balance Sheet L25 | Deuda de largo plazo | 4.810,7 | 4.876,0 | Deuda de largo plazo con arrendamientos financieros al 14-jun-2026 (10-Q 2T26); antes 4.810,7, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L14 | Inversiones no operativas | 0,00 | 28,00 | Valores negociables de largo plazo al 14-jun-2026 (10-Q); antes 0. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | -3.901,1 | -3.982,0 | Déficit patrimonial al 14-jun-2026 (10-Q); antes −3.901,1, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | -3.901,1 | -3.982,0 | Déficit patrimonial al 14-jun-2026 (10-Q); antes −3.901,1, el cierre de 2025. |
| Balance del último 10-Q | Input sheet B16 | Deuda (DCF) | 4.816,8 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda financiera al 14-jun-2026 (antes 4.816,8 fijo, del cierre de 2025). Sin arrendamientos operativos, como antes. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 52,20 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 57,78 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 49,21 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 41,32 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 37,23 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 26,76 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 59,11 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,190 | 0,193 | Margen en base ajustada por arrendamientos: + 0.3 pp (ajuste del EBIT 15.0 / ventas 4940). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,200 | 0,203 | Margen en base ajustada por arrendamientos: + 0.3 pp (ajuste del EBIT 15.0 / ventas 4940). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 3,00 | 2,64 | Ventas/capital con el capital arrendado: 1/(1/3 + 0.0452), con VP de arrendamientos 223.5 / ventas 4940. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 3,00 | 2,64 | Ventas/capital con el capital arrendado: 1/(1/3 + 0.0452), con VP de arrendamientos 223.5 / ventas 4940. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | 0,180 | 0,183 | Margen en base ajustada por arrendamientos: + 0.3 pp (ajuste del EBIT 15.0 / ventas 4940). |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C47 |  | 0,220 | 0,223 | Margen en base ajustada por arrendamientos: + 0.3 pp (ajuste del EBIT 15.0 / ventas 4940). |
| Margen objetivo Base de la hoja enlazado al de Input sheet | Valuation output C46 |  | 0,200 | ='Input sheet'!B30 | Margen objetivo Base enlazado a 'Input sheet'!B30: el valor escrito a mano no seguía a B30 (ajuste por arrendamientos de Damodaran y revisiones del 30-sep-2026), y el DCF de la hoja mezclaba un margen inicial ajustado con un objetivo sin ajustar. |
| Flujos LTM | Cash Flow Statement L13 | Cash from Operating Activities | 792,1 | 777,8 | LTM = ejercicio 792.1 + acumulado al 2026-06-14 352.6 − acumulado del año anterior 366.9 (NetCashProvidedByUsedInOperatingActivities). Antes 792.1. |
| Flujos LTM | Cash Flow Statement L22 | Cash from Investing Activities | -70,20 | -109,6 | LTM = ejercicio -70.2 + acumulado al 2026-06-14 -24.6 − acumulado del año anterior 14.8 (NetCashProvidedByUsedInInvestingActivities). Antes -70.2. |
| Flujos LTM | Cash Flow Statement L34 | Cash from Financing Activities | -752,1 | -805,1 | LTM = ejercicio -752.1 + acumulado al 2026-06-14 -314.3 − acumulado del año anterior -261.3 (NetCashProvidedByUsedInFinancingActivities). Antes -752.1. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | -137,8 | LTM = ejercicio -28.4 + acumulado al 2026-06-14 12.8 − acumulado del año anterior 122.2 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement I23 | Basic EPS 2023-12-31 | 14,66 | 14,80 | EPS básico del 10-K (2023-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2024-12-29 | 16,69 | 16,83 | EPS básico del 10-K (2024-12-29); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2025-12-28 | 17,57 | 17,69 | EPS básico del 10-K (2025-12-28); antes copiaba el diluido. |
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

El valor intrínseco principal es el DCF Base: US$323,13 (antes US$352,14). El DCF esperado de las cuatro historias, complementario, es US$282,25 (antes US$308,75); precio con margen de seguridad sobre el esperado US$183,46. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
