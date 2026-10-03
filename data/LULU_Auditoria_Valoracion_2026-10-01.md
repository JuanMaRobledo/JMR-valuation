---
schema: "jmr-audit-v1"
ticker: "LULU"
company: "lululemon athletica inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de lululemon athletica inc. (LULU)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$167,44 | US$177,10 |
| **DCF Base (valor intrínseco principal)** | US$172,25 | US$177,10 |
| DCF Conservadora | US$108,35 | US$107,12 |
| DCF Disrupción | US$71,34 | US$72,82 |
| DCF Optimista | US$229,97 | US$250,05 |
| DCF esperado por probabilidades (complemento) | US$148,45 | US$156,62 |
| Precio con MOS sobre el esperado | US$103,91 | US$101,80 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| ROIC terminal (criterio Damodaran) | Input sheet B49 | ¿ROIC terminal propio? | No | Yes | Ventaja que se desvanece: Marca premium (una sola fuente). Evidencia: ROIC 27-52% en 2021-2026, en descenso. ROIC después del año 10 = 12,4%, punto medio entre el costo de capital terminal (9,0%) y el promedio de la industria (15,8%), sin superar el ROIC actual (25,2%): 15,8%, porque la ventaja se desvanece. |
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,158 | 0,124 | Ventaja que se desvanece: Marca premium (una sola fuente). Evidencia: ROIC 27-52% en 2021-2026, en descenso. ROIC después del año 10 = 12,4%, punto medio entre el costo de capital terminal (9,0%) y el promedio de la industria (15,8%), sin superar el ROIC actual (25,2%): 15,8%, porque la ventaja se desvanece. |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 406,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-02-01 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 370,7 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-02-01 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 392,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-02-01 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 334,1 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-02-01 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 287,4 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-02-01 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 182,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-02-01 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 537,6 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-02-01 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-02-01 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,140 | 0,155 | Margen en base ajustada por arrendamientos: + 1.46 pp (ajuste del EBIT 161.6 / ventas 11094). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,185 | 0,200 | Margen en base ajustada por arrendamientos: + 1.46 pp (ajuste del EBIT 161.6 / ventas 11094). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 2,00 | 1,53 | Ventas/capital con el capital arrendado: 1/(1/2 + 0.1542), con VP de arrendamientos 1711.0 / ventas 11094. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 2,50 | 1,80 | Ventas/capital con el capital arrendado: 1/(1/2.5 + 0.1542), con VP de arrendamientos 1711.0 / ventas 11094. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | 0,150 | 0,165 | Margen en base ajustada por arrendamientos: + 1.46 pp (ajuste del EBIT 161.6 / ventas 11094). |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C47 |  | 0,210 | 0,225 | Margen en base ajustada por arrendamientos: + 1.46 pp (ajuste del EBIT 161.6 / ventas 11094). |
| Ventas/capital contrastado con la historia y la industria | Input sheet B32 |  | 1,53 | 1,77 | Ventas/capital revisado (1-oct-2026): historia 3,02 (con arrendamientos) e industria Apparel 1,77. El valor anterior quedaba fuera de ese rango por más de 10%; se lleva al borde más cercano. Incluye el capital arrendado (criterio Damodaran). |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | 1.117,7 | 233,9 | LTM = ejercicio -177.1 + acumulado al 2026-08-02 -417.5 − acumulado del año anterior -828.5 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes 1117.738. |
| EPS básico | Income Statement I23 | Basic EPS 2024-01-28 | 12,20 | 12,23 | EPS básico del 10-K (2024-01-28); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2025-02-02 | 14,64 | 14,67 | EPS básico del 10-K (2025-02-02); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2026-02-01 | 13,26 | 13,27 | EPS básico del 10-K (2026-02-01); antes copiaba el diluido. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores Disrupción < Conservadora < Base < Optimista | Sí |
| DCF esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al DCF esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $7,000-12,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$177,10 (antes US$172,25). El DCF esperado de las cuatro historias, complementario, es US$156,62 (antes US$148,45); precio con margen de seguridad sobre el esperado US$101,80. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
