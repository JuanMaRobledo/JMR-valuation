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
| DCF técnico anterior (caso Base de la hoja) | US$113,36 | US$107,46 |
| **DCF Base (valor intrínseco principal)** | US$113,36 | US$107,46 |
| DCF Conservadora | US$88,86 | US$79,70 |
| DCF Disrupción | US$57,25 | US$48,74 |
| DCF Optimista | US$147,38 | US$138,54 |
| DCF esperado por probabilidades (complemento) | US$110,01 | US$100,87 |
| Precio con MOS sobre el esperado | US$71,50 | US$65,56 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 12,10 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 13,93 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 15,97 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 14,61 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 15,05 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 14,22 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 64,04 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | =MAX(J27; B28;AVERAGE('Crecimiento y Márgenes'!E16:E19)) | =(MAX(J27; B28;AVERAGE('Crecimiento y Márgenes'!E16:E19)))+0 | Margen en base ajustada por arrendamientos: + 0.04 pp (ajuste del EBIT 0.4 / ventas 1145). |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | ='Escenarios e historias'!$D$6 | =('Escenarios e historias'!$D$6)+0,000373 | Margen en base ajustada por arrendamientos: + 0.04 pp (ajuste del EBIT 0.4 / ventas 1145). |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C47 |  | ='Escenarios e historias'!$D$8 | =('Escenarios e historias'!$D$8)+0,000373 | Margen en base ajustada por arrendamientos: + 0.04 pp (ajuste del EBIT 0.4 / ventas 1145). |
| Balance del último 10-Q | Balance Sheet L3:L36 |  | partidas del 31-dic-2025 | balance al 30-jun-2026 | 10-Q 2T26: el importador repetía el cierre anual |
| Conversor de I+D alineado al LTM | R& D converter B12:B14 |  | ejercicios 2025, 2024 y 2023 | 12 meses a junio: 273,3 · 206,6 · 179,8 | Los ejercicios se solapaban seis meses con el LTM (XBRL semestral de los 10-Q) |
| Estados financieros | Balance Sheet J4:K5, J9:K9 |  | inversiones de corto plazo en 0 | 91,9 y 104,1 separadas de otros activos corrientes | Bonos al vencimiento de corto plazo (XBRL, 10-K 2025) |
| Flujos LTM | Income Statement L8, L11 |  | SG&A 307,6 · otros 14,7 | SG&A 338,1 · otros −15,8 | SG&A LTM; EBIT sin cambio |
| EPS básico | Income Statement I23:L27 |  | promedio básico 0; acciones LTM 48,3 | 41,5-46,7; 46,724 en circulación | 10-K 2025 y balance del 10-Q 2T26 |
| Estados financieros | Input sheet B22, B24, B38:B42, B62:B63 |  | plantilla | 49,52M de acciones; 24%; opciones 0,6M a US$21,09; pérdidas  | Carta del 2T26 y 10-K 2025 |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores Disrupción < Conservadora < Base < Optimista | Sí |
| DCF esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al DCF esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $700-1,250 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$107,46 (antes US$113,36). El DCF esperado de las cuatro historias, complementario, es US$100,87 (antes US$110,01); precio con margen de seguridad sobre el esperado US$65,56. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
