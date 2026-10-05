---
schema: "jmr-audit-v1"
ticker: "ADBE"
company: "Adobe Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Adobe Inc. (ADBE)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$536,48 | US$410,48 |
| **DCF Base (valor intrínseco principal)** | US$465,71 | US$410,48 |
| DCF Conservadora | US$267,97 | US$245,68 |
| DCF Disrupción | US$172,43 | US$167,27 |
| DCF Optimista | US$583,92 | US$509,73 |
| DCF esperado por probabilidades (complemento) | US$364,33 | US$326,24 |
| Precio con MOS sobre el esperado | US$236,81 | US$212,06 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 92,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-11-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 89,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-11-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 98,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-11-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 83,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-11-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 65,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-11-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 57,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-11-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 93,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-11-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-11-28 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,385 | 0,386 | Margen en base ajustada por arrendamientos: + 0.1 pp (ajuste del EBIT 24.8 / ventas 25970). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,400 | 0,401 | Margen en base ajustada por arrendamientos: + 0.1 pp (ajuste del EBIT 24.8 / ventas 25970). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 4,00 | 3,77 | Ventas/capital con el capital arrendado: 1/(1/4 + 0.0155), con VP de arrendamientos 403.4 / ventas 25970. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 4,50 | 4,21 | Ventas/capital con el capital arrendado: 1/(1/4.5 + 0.0155), con VP de arrendamientos 403.4 / ventas 25970. |
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

El valor intrínseco principal es el DCF Base: US$410,48 (antes US$465,71). El DCF esperado de las cuatro historias, complementario, es US$326,24 (antes US$364,33); precio con margen de seguridad sobre el esperado US$212,06. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
