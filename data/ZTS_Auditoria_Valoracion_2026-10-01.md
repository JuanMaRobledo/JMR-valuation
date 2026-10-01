---
schema: "jmr-audit-v1"
ticker: "ZTS"
company: "Zoetis Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Zoetis Inc. (ZTS)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$117,30 | US$117,80 |
| Historia A | US$118,16 | US$118,64 |
| Historia B | US$65,09 | US$65,58 |
| Historia C | US$45,96 | US$46,44 |
| Historia D | US$136,73 | US$137,21 |
| **Valor esperado (valor intrínseco principal)** | **US$95,15** | **US$95,64** |
| Precio con MOS sobre el esperado | US$61,85 | US$62,16 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L4 | Inversiones de corto plazo | 0,00 | 200,0 | Inversiones de corto plazo al 30-jun-2026 (10-Q 2T26); antes 0. |
| Balance del último 10-Q | Balance Sheet L5 | Caja y valores negociables | 1.476,0 | 1.676,0 | Caja 1.476 + inversiones de corto plazo 200 al 30-jun-2026 (10-Q). |
| Balance del último 10-Q | Balance Sheet L25 | Deuda de largo plazo | 9.042,0 | 9.048,0 | Deuda de largo plazo al 30-jun-2026 (10-Q); antes 9.042. |
| Balance del último 10-Q | Balance Sheet L26 | Arrendamientos de largo plazo | 196,0 | 190,0 | Arrendamientos de largo plazo al 30-jun-2026 (10-Q); antes 196. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 3.331,0 | 3.148,0 | Patrimonio al 30-jun-2026 (10-Q); antes 3.331, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 3.331,0 | 3.148,0 | Patrimonio al 30-jun-2026 (10-Q); antes 3.331, el cierre de 2025. |
| Flujos LTM | Cash Flow Statement L13 | Cash from Operating Activities | 2.887,0 | 2.840,0 | LTM = ejercicio 2904.0 + acumulado al 2026-06-30 1056.0 − acumulado del año anterior 1120.0 (NetCashProvidedByUsedInOperatingActivities). Antes 2887. |
| Flujos LTM | Cash Flow Statement L22 | Cash from Investing Activities | -713,0 | -720,0 | LTM = ejercicio -748.0 + acumulado al 2026-06-30 -387.0 − acumulado del año anterior -415.0 (NetCashProvidedByUsedInInvestingActivities). Antes -713. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | -167,0 | LTM = ejercicio 325.0 + acumulado al 2026-06-30 -974.0 − acumulado del año anterior -482.0 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement I23 | Basic EPS 2023-12-31 | 5,07 | 5,08 | EPS básico del 10-K (2023-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2025-12-31 | 6,02 | 6,03 | EPS básico del 10-K (2025-12-31); antes copiaba el diluido. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores C < B < A < D | Sí |
| Valor esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al valor esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $4,500-7,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- Arrendamientos operativos: la deuda del DCF incluye 190,0 millones de arrendamientos operativos mientras el EBIT ya descuenta el alquiler (conversor de arrendamientos desactivado). Con el criterio de Damodaran o se convierten (deuda y EBIT ajustado) o se excluyen; excluirlos subiría el DCF en ~US$0,46 por acción. Es una decisión de método pendiente; no se cambió en esta auditoría.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF esperado de las cuatro historias: US$95,64 (antes US$95,15); precio con margen de seguridad US$62,16. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
