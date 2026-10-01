---
schema: "jmr-audit-v1"
ticker: "NKE"
company: "NIKE, Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de NIKE, Inc. (NKE)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$33,96 | US$34,27 |
| Historia A | US$34,88 | US$35,20 |
| Historia B | US$21,68 | US$21,68 |
| Historia C | US$14,93 | US$14,93 |
| Historia D | US$46,23 | US$46,66 |
| **Valor esperado (valor intrínseco principal)** | **US$32,19** | **US$32,42** |
| Precio con MOS sobre el esperado | US$20,92 | US$21,08 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,112 | 0,114 | Ventaja que se desvanece: Marca global y escala de distribución, hoy bajo presión. Evidencia: ROIC 18-47% en 2021-2026, en descenso. ROIC después del año 10 = 11,4%, punto medio entre el costo de capital terminal (9,0%) y el promedio de la industria (20,9%), sin superar el ROIC actual (13,8%): 13,8%, porque la ventaja se desvanece. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | 99,00 | LTM = ejercicio cerrado el 2026-05-31 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement I23 | Basic EPS 2024-05-31 | 3,73 | 3,76 | EPS básico del 10-K (2024-05-31); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2025-05-31 | 2,16 | 2,17 | EPS básico del 10-K (2025-05-31); antes copiaba el diluido. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores C < B < A < D | Sí |
| Valor esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al valor esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | >$25,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- Arrendamientos operativos: la deuda del DCF incluye 3.091,0 millones de arrendamientos operativos mientras el EBIT ya descuenta el alquiler (conversor de arrendamientos desactivado). Con el criterio de Damodaran o se convierten (deuda y EBIT ajustado) o se excluyen; excluirlos subiría el DCF en ~US$2,09 por acción. Es una decisión de método pendiente; no se cambió en esta auditoría.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF esperado de las cuatro historias: US$32,42 (antes US$32,19); precio con margen de seguridad US$21,08. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
