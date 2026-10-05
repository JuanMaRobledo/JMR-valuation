---
schema: "jmr-audit-v1"
ticker: "PYPL"
company: "PayPal Holdings, Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de PayPal Holdings, Inc. (PYPL)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$101,14 | US$119,70 |
| **DCF Base (valor intrínseco principal)** | US$105,13 | US$119,70 |
| DCF Conservadora | US$65,52 | US$69,07 |
| DCF Disrupción | US$47,56 | US$49,97 |
| DCF Optimista | US$132,13 | US$150,78 |
| DCF esperado por probabilidades (complemento) | US$91,54 | US$102,20 |
| Precio con MOS sobre el esperado | US$59,50 | US$66,43 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Conversor de I+D alineado al LTM | R& D converter B12 | I+D año −1 | ='Income Statement'!K10 | ='Income Statement'!J10+1498-1460 | Tecnología y desarrollo de los 12 meses a jun-2025 = 2024 (2.979) + 1S25 (1.498) − 1S24 (1.460) (10-Q). Antes el ejercicio 2025, que se solapa con el LTM. |
| Conversor de I+D alineado al LTM | R& D converter B13 | I+D año −2 | ='Income Statement'!J10 | ='Income Statement'!I10+1460-1464 | 12 meses a jun-2024 = 2023 + 1S24 − 1S23 (10-Q). Antes el ejercicio 2024. |
| Conversor de I+D alineado al LTM | R& D converter B14 | I+D año −3 | ='Income Statement'!I10 | ='Income Statement'!H10+1464-1630 | 12 meses a jun-2023 = 2022 + 1S23 − 1S22 (10-Q). Antes el ejercicio 2023. |
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,134 | 0,148 | Ventaja que se desvanece: Red de dos lados (comercios y usuarios) y marca en el checkout. Evidencia: ROIC 13-25% en 2021-2026. ROIC después del año 10 = 14,8%, punto medio entre el costo de capital terminal (9,0%) y el promedio de la industria (sin dato), sin superar el ROIC actual (20,6%): 20,6%, porque la ventaja se desvanece. |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 162,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 174,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 170,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 116,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 98,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 83,00 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 151,0 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,195 | 0,197 | Margen en base ajustada por arrendamientos: + 0.15 pp (ajuste del EBIT 51.7 / ventas 34128). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 2,60 | 2,48 | Ventas/capital con el capital arrendado: 1/(1/2.6 + 0.0194), con VP de arrendamientos 661.9 / ventas 34128. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 2,60 | 2,48 | Ventas/capital con el capital arrendado: 1/(1/2.6 + 0.0194), con VP de arrendamientos 661.9 / ventas 34128. |
| EPS básico | Income Statement I23 | Basic EPS 2023-12-31 | 3,84 | 3,85 | EPS básico del 10-K (2023-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2024-12-31 | 3,99 | 4,03 | EPS básico del 10-K (2024-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2025-12-31 | 5,41 | 5,46 | EPS básico del 10-K (2025-12-31); antes copiaba el diluido. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | =L13+L22+L34 | Cambio de caja LTM = operación + inversión + financiación (sin efecto cambiario); la SEC solo publica hasta mar-2026. |
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

- La API XBRL de la SEC solo publica hasta mar-2026 para PayPal: se conservaron los flujos LTM a jun-2026 de la hoja.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$119,70 (antes US$105,13). El DCF esperado de las cuatro historias, complementario, es US$102,20 (antes US$91,54); precio con margen de seguridad sobre el esperado US$66,43. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
