---
schema: "jmr-audit-v1"
ticker: "MSFT"
company: "Microsoft Corporation"
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Microsoft Corporation (MSFT)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$467,89 | US$467,13 |
| **DCF Base (valor intrínseco principal)** | US$459,29 | US$458,42 |
| DCF Conservadora | US$240,06 | US$237,05 |
| DCF Disrupción | US$201,50 | US$197,86 |
| DCF Optimista | US$599,21 | US$599,73 |
| DCF esperado por probabilidades (complemento) | US$406,69 | US$405,29 |
| Precio con MOS sobre el esperado | US$264,35 | US$263,44 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Conversor de I+D alineado al LTM | R& D converter B12 | I+D año −1 | ='Income Statement'!K10 | ='Income Statement'!J10 | Año −1 = ejercicio a jun-2025 (32.488). Antes repetía el ejercicio a jun-2026, que es el mismo LTM: el activo de I+D contaba dos veces el año actual. |
| Conversor de I+D alineado al LTM | R& D converter B13 | I+D año −2 | ='Income Statement'!J10 | ='Income Statement'!I10 | Año −2 = ejercicio a jun-2024. Antes el ejercicio a jun-2025. |
| Conversor de I+D alineado al LTM | R& D converter B14 | I+D año −3 | ='Income Statement'!I10 | ='Income Statement'!H10 | Año −3 = ejercicio a jun-2023. Antes el ejercicio a jun-2024. |
| Balance del último 10-Q | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | Se suman los arrendamientos financieros (66.594 al 30-jun-2026, 10-K FY26): son deuda (centros de datos) y su costo no está en el EBIT como alquiler. Antes se omitían. |
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,259 | 0,265 | Ventaja durable: Costos de cambio y efectos de red (Office, Azure, Windows, LinkedIn). Evidencia: ROIC 30-72% en 2021-2026. ROIC después del año 10 = el promedio de la industria (29,3%), sin superar el ROIC actual (26,5%): 26,5% (Damodaran, Investment Valuation, cap. 12). |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25+66594 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. MSFT: incluye los 66.594 de arrendamientos financieros. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 6.968,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-06-30 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 6.082,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-06-30 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 4.334,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-06-30 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 3.146,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-06-30 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 2.612,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-06-30 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 2.316,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-06-30 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 6.216,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-06-30 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2026-06-30 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,463 | 0,475 | Margen en base ajustada por arrendamientos: + 1.21 pp (ajuste del EBIT 4000.9 / ventas 331839). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,450 | 0,462 | Margen en base ajustada por arrendamientos: + 1.21 pp (ajuste del EBIT 4000.9 / ventas 331839). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 0,650 | 0,625 | Ventas/capital con el capital arrendado: 1/(1/0.65 + 0.0626), con VP de arrendamientos 20769.8 / ventas 331839. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 1,00 | 0,941 | Ventas/capital con el capital arrendado: 1/(1/1 + 0.0626), con VP de arrendamientos 20769.8 / ventas 331839. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | 0,420 | 0,432 | Margen en base ajustada por arrendamientos: + 1.21 pp (ajuste del EBIT 4000.9 / ventas 331839). |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C47 |  | 0,480 | 0,492 | Margen en base ajustada por arrendamientos: + 1.21 pp (ajuste del EBIT 4000.9 / ventas 331839). |
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

El valor intrínseco principal es el DCF Base: US$458,42 (antes US$459,29). El DCF esperado de las cuatro historias, complementario, es US$405,29 (antes US$406,69); precio con margen de seguridad sobre el esperado US$263,44. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
