---
schema: "jmr-audit-v1"
ticker: "NVDA"
company: "NVIDIA Corporation"
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de NVIDIA Corporation (NVDA)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$259,29 | US$222,09 |
| **DCF Base (valor intrínseco principal)** | US$204,91 | US$222,09 |
| DCF Conservadora | US$121,20 | US$132,83 |
| DCF Disrupción | US$50,24 | US$54,89 |
| DCF Optimista | US$313,47 | US$338,53 |
| DCF esperado por probabilidades (complemento) | US$186,04 | US$201,88 |
| Precio con MOS sobre el esperado | US$120,93 | US$131,22 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L4 | Inversiones de corto plazo | 0,00 | 34.143,0 | Valores negociables (deuda) al 26-jul-2026 (10-Q 2T FY27); antes 0. |
| Balance del último 10-Q | Balance Sheet L5 | Caja y valores negociables | 22.443,0 | 56.586,0 | Caja 22.443 + valores negociables 34.143 al 26-jul-2026 (10-Q). |
| Balance del último 10-Q | Balance Sheet L14 | Inversiones no operativas | 0,00 | 90.681,0 | Inversiones en acciones al 26-jul-2026: cotizadas 42.783 + no cotizadas 47.898 (10-Q); antes 0: son activos no operativos. |
| Balance del último 10-Q | Balance Sheet L20 | Deuda corriente | 999,0 | 1.000,0 | Porción corriente de la deuda al 26-jul-2026 (10-Q). |
| Balance del último 10-Q | Balance Sheet L25 | Deuda de largo plazo | 7.469,0 | 32.366,0 | Deuda de largo plazo al 26-jul-2026 (10-Q); antes 7.469, el cierre de enero de 2026. |
| Balance del último 10-Q | Balance Sheet L21 | Arrendamientos corrientes | — | 509,0 | Arrendamientos operativos corrientes al 26-jul-2026 (10-Q). |
| Balance del último 10-Q | Balance Sheet L26 | Arrendamientos de largo plazo | 2.572,0 | 4.985,0 | Arrendamientos operativos de largo plazo al 26-jul-2026 (10-Q); antes 2.572. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 157.293,0 | 228.984,0 | Patrimonio al 26-jul-2026 (10-Q); antes 157.293, el cierre de enero de 2026. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 157.293,0 | 228.984,0 | Patrimonio al 26-jul-2026 (10-Q); antes 157.293, el cierre de enero de 2026. |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 462,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-01-25 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 493,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-01-25 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 485,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-01-25 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 457,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-01-25 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 381,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-01-25 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 314,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-01-25 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 1.494,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-01-25 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-01-25 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,600 | 0,600 | Margen en base ajustada por arrendamientos: + 0.05 pp (ajuste del EBIT 151.1 / ventas 302970). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,580 | 0,580 | Margen en base ajustada por arrendamientos: + 0.05 pp (ajuste del EBIT 151.1 / ventas 302970). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 3,00 | 2,92 | Ventas/capital con el capital arrendado: 1/(1/3 + 0.0092), con VP de arrendamientos 2798.0 / ventas 302970. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 2,50 | 2,44 | Ventas/capital con el capital arrendado: 1/(1/2.5 + 0.0092), con VP de arrendamientos 2798.0 / ventas 302970. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | 0,500 | 0,500 | Margen en base ajustada por arrendamientos: + 0.05 pp (ajuste del EBIT 151.1 / ventas 302970). |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C47 |  | 0,650 | 0,650 | Margen en base ajustada por arrendamientos: + 0.05 pp (ajuste del EBIT 151.1 / ventas 302970). |
| Margen objetivo Base de la hoja enlazado al de Input sheet | Valuation output C46 |  | 0,580 | ='Input sheet'!B30 | Margen objetivo Base enlazado a 'Input sheet'!B30: el valor escrito a mano no seguía a B30 (ajuste por arrendamientos de Damodaran y revisiones del 30-sep-2026), y el DCF de la hoja mezclaba un margen inicial ajustado con un objetivo sin ajustar. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | 10.804,0 | LTM = ejercicio 2016.0 + acumulado al 2026-07-26 11838.0 − acumulado del año anterior 3050.0 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement J23 | Basic EPS 2025-01-26 | 2,94 | 2,97 | EPS básico del 10-K (2025-01-26); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2026-01-25 | 4,90 | 4,93 | EPS básico del 10-K (2026-01-25); antes copiaba el diluido. |
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

El valor intrínseco principal es el DCF Base: US$222,09 (antes US$204,91). El DCF esperado de las cuatro historias, complementario, es US$201,88 (antes US$186,04); precio con margen de seguridad sobre el esperado US$131,22. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
