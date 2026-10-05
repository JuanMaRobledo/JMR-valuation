---
schema: "jmr-audit-v1"
ticker: "BSX"
company: "Boston Scientific Corporation"
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Boston Scientific Corporation (BSX)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$36,39 | US$36,23 |
| **DCF Base (valor intrínseco principal)** | US$35,35 | US$36,23 |
| DCF Conservadora | US$28,07 | US$28,93 |
| DCF Disrupción | US$21,76 | US$22,49 |
| DCF Optimista | US$42,65 | US$43,56 |
| DCF esperado por probabilidades (complemento) | US$33,95 | US$34,82 |
| Precio con MOS sobre el esperado | US$22,06 | US$22,63 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L20 | Deuda corriente | 299,0 | 1.709,0 | Deuda corriente al 30-jun-2026 (DebtCurrent, 10-Q 2T26); antes 299, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L25 | Deuda de largo plazo | 11.137,0 | 10.915,0 | Deuda de largo plazo al 30-jun-2026 (10-Q 2T26); antes 11.137, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L14 | Inversiones no operativas | 0,00 | 2.245,0 | Inversiones al 30-jun-2026: método de participación 1.308 + sin valor de mercado 938 (10-Q). Antes 0: son activos no operativos. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 24.233,0 | 24.930,0 | Patrimonio de los accionistas al 30-jun-2026 (10-Q); antes 24.233, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 24.233,0 | 25.172,0 | Patrimonio total con minoritarios al 30-jun-2026 (10-Q). |
| Balance del último 10-Q | Input sheet B21 | Minoritarios (DCF) | 0,00 | 242,0 | Participaciones minoritarias al 30-jun-2026 (10-Q 2T26); antes 0. |
| Balance del último 10-Q | Input sheet B15 | Patrimonio (DCF) | ='Balance Sheet'!L35 | ='Balance Sheet'!L34 | Patrimonio de los accionistas (sin minoritarios, que se restan aparte). |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 117,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 107,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 96,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 82,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 69,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 56,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 248,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,200 | 0,202 | Margen en base ajustada por arrendamientos: + 0.25 pp (ajuste del EBIT 52.1 / ventas 20996). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,240 | 0,242 | Margen en base ajustada por arrendamientos: + 0.25 pp (ajuste del EBIT 52.1 / ventas 20996). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 1,30 | 1,26 | Ventas/capital con el capital arrendado: 1/(1/1.3 + 0.0247), con VP de arrendamientos 519.2 / ventas 20996. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 1,20 | 1,17 | Ventas/capital con el capital arrendado: 1/(1/1.2 + 0.0247), con VP de arrendamientos 519.2 / ventas 20996. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | 0,200 | 0,202 | Margen en base ajustada por arrendamientos: + 0.25 pp (ajuste del EBIT 52.1 / ventas 20996). |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C47 |  | 0,270 | 0,272 | Margen en base ajustada por arrendamientos: + 0.25 pp (ajuste del EBIT 52.1 / ventas 20996). |
| Margen objetivo Base de la hoja enlazado al de Input sheet | Valuation output C46 |  | 0,240 | ='Input sheet'!B30 | Margen objetivo Base enlazado a 'Input sheet'!B30: el valor escrito a mano no seguía a B30 (ajuste por arrendamientos de Damodaran y revisiones del 30-sep-2026), y el DCF de la hoja mezclaba un margen inicial ajustado con un objetivo sin ajustar. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | 12,00 | LTM = ejercicio 1541.0 + acumulado al 2026-06-30 -1394.0 − acumulado del año anterior 135.0 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement I23 | Basic EPS 2023-12-31 | 1,09 | 1,08 | EPS básico del 10-K (2023-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2024-12-31 | 1,24 | 1,26 | EPS básico del 10-K (2024-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2025-12-31 | 1,94 | 1,96 | EPS básico del 10-K (2025-12-31); antes copiaba el diluido. |
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

El valor intrínseco principal es el DCF Base: US$36,23 (antes US$35,35). El DCF esperado de las cuatro historias, complementario, es US$34,82 (antes US$33,95); precio con margen de seguridad sobre el esperado US$22,63. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
