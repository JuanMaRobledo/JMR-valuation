---
schema: "jmr-audit-v1"
ticker: "EPAM"
company: "EPAM Systems, Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de EPAM Systems, Inc. (EPAM)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$168,22 | US$183,20 |
| **DCF Base (valor intrínseco principal)** | US$165,87 | US$183,20 |
| DCF Conservadora | US$110,21 | US$120,59 |
| DCF Disrupción | US$81,42 | US$88,94 |
| DCF Optimista | US$218,87 | US$241,33 |
| DCF esperado por probabilidades (complemento) | US$148,68 | US$163,71 |
| Precio con MOS sobre el esperado | US$96,64 | US$106,41 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L21 | Arrendamientos corrientes | — | 39,30 | Porción corriente de arrendamientos al 30-jun-2026 (10-Q 2T26). |
| Balance del último 10-Q | Balance Sheet L26 | Arrendamientos de largo plazo | 81,50 | 88,00 | Arrendamientos de largo plazo al 30-jun-2026 (10-Q); antes 81,5. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 3.677,2 | 3.519,0 | Patrimonio al 30-jun-2026 (10-Q); antes 3.677,2, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 3.677,2 | 3.519,0 | Patrimonio al 30-jun-2026 (10-Q); antes 3.677,2, el cierre de 2025. |
| ROIC terminal (criterio Damodaran) | Input sheet B49 | ¿ROIC terminal propio? | No | Yes | Ventaja que se desvanece: Servicios de ingeniería con costos de cambio moderados. Evidencia: ROIC 47% → 15% en cinco años, acercándose al costo de capital. ROIC después del año 10 = 11,4%, punto medio entre el costo de capital terminal (9,0%) y el promedio de la industria (26,4%), sin superar el ROIC actual (13,8%): 13,8%, porque la ventaja se desvanece. |
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,200 | 0,114 | Ventaja que se desvanece: Servicios de ingeniería con costos de cambio moderados. Evidencia: ROIC 47% → 15% en cinco años, acercándose al costo de capital. ROIC después del año 10 = 11,4%, punto medio entre el costo de capital terminal (9,0%) y el promedio de la industria (26,4%), sin superar el ROIC actual (13,8%): 13,8%, porque la ventaja se desvanece. |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 52,20 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 41,66 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 32,38 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 26,01 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 15,22 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 10,28 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 3,33 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,105 | 0,110 | Margen en base ajustada por arrendamientos: + 0.53 pp (ajuste del EBIT 29.7 / ventas 5616.7). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,125 | 0,130 | Margen en base ajustada por arrendamientos: + 0.53 pp (ajuste del EBIT 29.7 / ventas 5616.7). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 3,50 | 3,27 | Ventas/capital con el capital arrendado: 1/(1/3.5 + 0.0201), con VP de arrendamientos 112.6 / ventas 5616.7. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 3,00 | 2,83 | Ventas/capital con el capital arrendado: 1/(1/3 + 0.0201), con VP de arrendamientos 112.6 / ventas 5616.7. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | 0,095 | 0,100 | Margen en base ajustada por arrendamientos: + 0.53 pp (ajuste del EBIT 29.7 / ventas 5616.7). |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C47 |  | 0,150 | 0,155 | Margen en base ajustada por arrendamientos: + 0.53 pp (ajuste del EBIT 29.7 / ventas 5616.7). |
| Margen objetivo Base de la hoja enlazado al de Input sheet | Valuation output C46 |  | 0,125 | ='Input sheet'!B30 | Margen objetivo Base enlazado a 'Input sheet'!B30: el valor escrito a mano no seguía a B30 (ajuste por arrendamientos de Damodaran y revisiones del 30-sep-2026), y el DCF de la hoja mezclaba un margen inicial ajustado con un objetivo sin ajustar. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | -252,2 | LTM = ejercicio 11.0 + acumulado al 2026-06-30 -507.1 − acumulado del año anterior -243.9 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement I23 | Basic EPS 2023-12-31 | 7,06 | 7,21 | EPS básico del 10-K (2023-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2024-12-31 | 7,84 | 7,93 | EPS básico del 10-K (2024-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2025-12-31 | 6,72 | 6,76 | EPS básico del 10-K (2025-12-31); antes copiaba el diluido. |
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

El valor intrínseco principal es el DCF Base: US$183,20 (antes US$165,87). El DCF esperado de las cuatro historias, complementario, es US$163,71 (antes US$148,68); precio con margen de seguridad sobre el esperado US$106,41. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
