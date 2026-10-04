---
schema: "jmr-audit-v1"
ticker: "GOOG"
company: "Alphabet Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Alphabet Inc. (GOOG)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$311,55 | US$317,02 |
| **DCF Base (valor intrínseco principal)** | US$298,81 | US$317,02 |
| DCF Conservadora | US$141,10 | US$159,80 |
| DCF Disrupción | US$110,41 | US$129,33 |
| DCF Optimista | US$399,94 | US$416,68 |
| DCF esperado por probabilidades (complemento) | US$251,35 | US$269,49 |
| Precio con MOS sobre el esperado | US$163,37 | US$175,17 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L4 | Inversiones de corto plazo | 0,00 | 186.563,0 | Valores negociables al 30-jun-2026 (10-Q 2T26); antes 0: la caja del DCF omitía los valores negociables. |
| Balance del último 10-Q | Balance Sheet L5 | Caja y valores negociables | 55.911,0 | 242.474,0 | Caja y valores negociables al 30-jun-2026 = 55.911 + 186.563 (10-Q). |
| Balance del último 10-Q | Balance Sheet L14 | Inversiones no operativas | 0,00 | 131.461,0 | Valores no negociables y otras inversiones de largo plazo al 30-jun-2026 (10-Q); antes 0: son activos no operativos. |
| Balance del último 10-Q | Balance Sheet L20 | Deuda corriente | 1.996,0 | 1.999,0 | Porción corriente de la deuda al 30-jun-2026 (10-Q). |
| Balance del último 10-Q | Balance Sheet L25 | Deuda de largo plazo | 46.547,0 | 98.165,0 | Deuda de largo plazo al 30-jun-2026 (10-Q); antes 46.547, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L21 | Arrendamientos corrientes | — | 3.446,0 | Arrendamientos operativos corrientes al 30-jun-2026 = 18.037 − 14.591 (10-Q). |
| Balance del último 10-Q | Balance Sheet L26 | Arrendamientos de largo plazo | 12.744,0 | 14.591,0 | Arrendamientos operativos de largo plazo al 30-jun-2026 (10-Q); antes 12.744. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 415.265,0 | 640.480,0 | Patrimonio al 30-jun-2026 (10-Q); antes 415.265, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 415.265,0 | 640.480,0 | Patrimonio al 30-jun-2026 (10-Q); antes 415.265, el cierre de 2025. |
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,286 | 0,293 | Ventaja durable: Escala y efectos de red en búsqueda, YouTube y Android; datos. Evidencia: ROIC 24-31% en 2021-2026. ROIC después del año 10 = el promedio de la industria (29,3%), sin superar el ROIC actual (31,3%): 29,3% (Damodaran, Investment Valuation, cap. 12). |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 3.345,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 3.275,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 3.082,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 2.510,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 2.061,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 1.669,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 5.654,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,325 | 0,328 | Margen en base ajustada por arrendamientos: + 0.27 pp (ajuste del EBIT 1212.9 / ventas 445866). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,350 | 0,353 | Margen en base ajustada por arrendamientos: + 0.27 pp (ajuste del EBIT 1212.9 / ventas 445866). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 1,20 | 1,15 | Ventas/capital con el capital arrendado: 1/(1/1.2 + 0.0335), con VP de arrendamientos 14924.4 / ventas 445866. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 1,50 | 1,43 | Ventas/capital con el capital arrendado: 1/(1/1.5 + 0.0335), con VP de arrendamientos 14924.4 / ventas 445866. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | 0,310 | 0,313 | Margen en base ajustada por arrendamientos: + 0.27 pp (ajuste del EBIT 1212.9 / ventas 445866). |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C47 |  | 0,380 | 0,383 | Margen en base ajustada por arrendamientos: + 0.27 pp (ajuste del EBIT 1212.9 / ventas 445866). |
| Margen objetivo Base de la hoja enlazado al de Input sheet | Valuation output C46 |  | 0,335 | ='Input sheet'!B30 | Margen objetivo Base enlazado a 'Input sheet'!B30: el valor escrito a mano no seguía a B30 (ajuste por arrendamientos de Damodaran y revisiones del 30-sep-2026), y el DCF de la hoja mezclaba un margen inicial ajustado con un objetivo sin ajustar. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | 34.875,0 | LTM = ejercicio 7242.0 + acumulado al 2026-06-30 25203.0 − acumulado del año anterior -2430.0 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement I23 | Basic EPS 2023-12-31 | 5,80 | 5,84 | EPS básico del 10-K (2023-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2024-12-31 | 8,04 | 8,13 | EPS básico del 10-K (2024-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2025-12-31 | 10,81 | 10,91 | EPS básico del 10-K (2025-12-31); antes copiaba el diluido. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores Disrupción < Conservadora < Base < Optimista | Sí |
| DCF esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al DCF esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | >$50,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$317,02 (antes US$298,81). El DCF esperado de las cuatro historias, complementario, es US$269,49 (antes US$251,35); precio con margen de seguridad sobre el esperado US$175,17. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
