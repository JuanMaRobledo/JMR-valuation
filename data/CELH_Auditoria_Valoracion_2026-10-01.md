---
schema: "jmr-audit-v1"
ticker: "CELH"
company: "Celsius Holdings, Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Celsius Holdings, Inc. (CELH)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$18,12 | US$18,12 |
| Historia A | US$22,22 | US$22,23 |
| Historia B | US$15,48 | US$15,49 |
| Historia C | US$8,94 | US$8,95 |
| Historia D | US$28,84 | US$28,85 |
| **Valor esperado (valor intrínseco principal)** | **US$18,53** | **US$18,54** |
| Precio con MOS sobre el esperado | US$12,05 | US$12,05 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L25 | Deuda de largo plazo | 669,9 | 668,0 | Deuda de largo plazo al 30-jun-2026 (10-Q 2T26); antes 669,9, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 1.181,5 | 1.200,0 | Patrimonio al 30-jun-2026 (10-Q); antes 1.181,5, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 1.181,5 | 1.200,0 | Patrimonio al 30-jun-2026 (10-Q); antes 1.181,5, el cierre de 2025. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | 17,90 | LTM = ejercicio -350.2 + acumulado al 2026-06-30 93.1 − acumulado del año anterior -275.0 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores C < B < A < D | Sí |
| Valor esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al valor esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $2,000-3,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- Arrendamientos operativos: la deuda del DCF incluye 13,8 millones de arrendamientos operativos mientras el EBIT ya descuenta el alquiler (conversor de arrendamientos desactivado). Con el criterio de Damodaran o se convierten (deuda y EBIT ajustado) o se excluyen; excluirlos subiría el DCF en ~US$0,05 por acción. Es una decisión de método pendiente; no se cambió en esta auditoría.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF esperado de las cuatro historias: US$18,54 (antes US$18,53); precio con margen de seguridad US$12,05. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
