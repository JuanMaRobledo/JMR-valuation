---
schema: "jmr-audit-v1"
ticker: "INTU"
company: "Intuit Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Intuit Inc. (INTU)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$496,45 | US$497,72 |
| Historia A | US$509,89 | US$511,24 |
| Historia B | US$259,79 | US$259,79 |
| Historia C | US$207,90 | US$207,90 |
| Historia D | US$628,00 | US$629,70 |
| **Valor esperado (valor intrínseco principal)** | **US$440,79** | **US$441,74** |
| Precio con MOS sobre el esperado | US$286,51 | US$287,13 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,222 | 0,225 | Ventaja durable: Costos de cambio y datos del cliente (QuickBooks, TurboTax), escala en pyme. Evidencia: ROIC 12-22%, siempre por encima del costo de capital. ROIC después del año 10 = el promedio de la industria (29,3%), sin superar el ROIC actual (22,5%): 22,5% (Damodaran, Investment Valuation, cap. 12). |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | -265,0 | LTM = ejercicio cerrado el 2026-07-31 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement I23 | Basic EPS 2024-07-31 | 10,43 | 10,58 | EPS básico del 10-K (2024-07-31); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2025-07-31 | 13,67 | 13,82 | EPS básico del 10-K (2025-07-31); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2026-07-31 | 16,48 | 16,53 | EPS básico del 10-K (2026-07-31); antes copiaba el diluido. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores C < B < A < D | Sí |
| Valor esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al valor esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $12,000-25,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- Arrendamientos operativos: la deuda del DCF incluye 667,0 millones de arrendamientos operativos mientras el EBIT ya descuenta el alquiler (conversor de arrendamientos desactivado). Con el criterio de Damodaran o se convierten (deuda y EBIT ajustado) o se excluyen; excluirlos subiría el DCF en ~US$2,50 por acción. Es una decisión de método pendiente; no se cambió en esta auditoría.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF esperado de las cuatro historias: US$441,74 (antes US$440,79); precio con margen de seguridad US$287,13. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
