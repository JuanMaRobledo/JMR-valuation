---
schema: "jmr-audit-v1"
ticker: "DUOL"
company: "Duolingo, Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Duolingo, Inc. (DUOL)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$125,77 | US$119,73 |
| Historia A | US$125,64 | US$119,64 |
| Historia B | US$98,99 | US$93,58 |
| Historia C | US$64,28 | US$59,88 |
| Historia D | US$162,33 | US$155,74 |
| **Valor esperado (valor intrínseco principal)** | **US$118,85** | **US$113,06** |
| Precio con MOS sobre el esperado | US$77,25 | US$73,49 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Conversor de I+D alineado al LTM | R& D converter B12 | I+D año −1 | ='Income Statement'!K10 | ='Income Statement'!J10+144,06-106,025 | I+D de los 12 meses a jun-2025 = 2024 (235,3) + 1S25 (144,06) − 1S24 (106,025) = 273,3 (10-Q 2T25 y 2T24). Antes el ejercicio 2025, que se solapa con el LTM. |
| Conversor de I+D alineado al LTM | R& D converter B13 | I+D año −2 | ='Income Statement'!J10 | ='Income Statement'!I10+106,025-93,791 | 12 meses a jun-2024 = 2023 + 1S24 − 1S23 (10-Q). Antes el ejercicio 2024. |
| Conversor de I+D alineado al LTM | R& D converter B14 | I+D año −3 | ='Income Statement'!I10 | ='Income Statement'!H10+93,791-63,998 | 12 meses a jun-2023 = 2022 + 1S23 − 1S22 (10-Q). Antes el ejercicio 2023. |
| Balance del último 10-Q | Balance Sheet L4 | Inversiones de corto plazo | 0,00 | 133,0 | Inversiones mantenidas al vencimiento de corto plazo al 30-jun-2026 (10-Q 2T26); antes 0. |
| Balance del último 10-Q | Balance Sheet L5 | Caja y valores negociables | 1.180,9 | 1.313,9 | Caja 1.180,9 + inversiones de corto plazo 133 al 30-jun-2026 (10-Q). |
| Balance del último 10-Q | Balance Sheet L14 | Inversiones no operativas | 135,1 | 103,0 | Inversiones de largo plazo al 30-jun-2026 (10-Q); antes 135,1, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L26 | Arrendamientos de largo plazo | 93,80 | 86,00 | Arrendamientos de largo plazo al 30-jun-2026 (10-Q); antes 93,8. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 1.347,0 | 1.410,0 | Patrimonio al 30-jun-2026 (10-Q); antes 1.347, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 1.347,0 | 1.410,0 | Patrimonio al 30-jun-2026 (10-Q); antes 1.347, el cierre de 2025. |
| Balance del último 10-Q | Input sheet B20 | Activos no operativos (DCF) | ='Balance Sheet'!L14+'Balance Sheet'!L15 | ='Balance Sheet'!L14 | Activos no operativos = inversiones de largo plazo. Antes sumaba «Other Long-Term Assets» (320,8), que no son inversiones. |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 12,10 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 13,93 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 15,97 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 14,61 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 15,05 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 14,22 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 64,04 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,200 | 0,201 | Margen en base ajustada por arrendamientos: + 0.09 pp (ajuste del EBIT 1.1 / ventas 1145). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,270 | 0,271 | Margen en base ajustada por arrendamientos: + 0.09 pp (ajuste del EBIT 1.1 / ventas 1145). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 4,00 | 2,97 | Ventas/capital con el capital arrendado: 1/(1/4 + 0.0866), con VP de arrendamientos 99.2 / ventas 1145. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 4,50 | 3,24 | Ventas/capital con el capital arrendado: 1/(1/4.5 + 0.0866), con VP de arrendamientos 99.2 / ventas 1145. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | =B6 | =(B6)+0,000944 | Margen en base ajustada por arrendamientos: + 0.09 pp (ajuste del EBIT 1.1 / ventas 1145). |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | 204,7 | LTM = ejercicio 250.6 + acumulado al 2026-06-30 144.5 − acumulado del año anterior 190.4 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores C < B < A < D | Sí |
| Valor esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al valor esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $700-1,250 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF esperado de las cuatro historias: US$113,06 (antes US$118,85); precio con margen de seguridad US$73,49. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
