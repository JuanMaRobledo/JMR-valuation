---
schema: "jmr-audit-v1"
ticker: "GOOG"
company: "Alphabet Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Alphabet Inc. (GOOG)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$311,55 | US$334,80 |
| Historia A | US$298,81 | US$321,95 |
| Historia B | US$141,10 | US$162,74 |
| Historia C | US$110,41 | US$131,99 |
| Historia D | US$399,94 | US$423,79 |
| **Valor esperado (valor intrínseco principal)** | **US$251,35** | **US$274,02** |
| Precio con MOS sobre el esperado | US$163,37 | US$178,11 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L4 | Inversiones de corto plazo | 0,00 | 186.563,0 | Valores negociables al 30-jun-2026 (10-Q 2T26); antes 0: la caja del DCF omitía los valores negociables. |
| Balance del último 10-Q | Balance Sheet L5 | Caja y valores negociables | 55.911,0 | 242.474,0 | Caja y valores negociables al 30-jun-2026 = 55.911 + 186.563 (10-Q). |
| Balance del último 10-Q | Balance Sheet L14 | Inversiones no operativas | 0,00 | 131.461,0 | Valores no negociables y otras inversiones de largo plazo al 30-jun-2026 (10-Q); antes 0: son activos no operativos. |
| Balance del último 10-Q | Balance Sheet L20 | Deuda corriente | 1.996,0 | 1.999,0 | Porción corriente de la deuda al 30-jun-2026 (10-Q). |
| Balance del último 10-Q | Balance Sheet L25 | Deuda de largo plazo | 46.547,0 | 98.165,0 | Deuda de largo plazo al 30-jun-2026 (10-Q); antes 46.547, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L21 | Arrendamientos corrientes | — | 3.446,0 | Arrendamientos operativos corrientes al 30-jun-2026 = 18.037 − 14.591 (10-Q). |
| Balance del último 10-Q | Balance Sheet L26 | Arrendamientos de largo plazo | 12.744,0 | 14.591,0 | Arrendamientos operativos de largo plazo al 30-jun-2026 (10-Q); antes 12.744. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 415.265,0 | 640.480,0 | Patrimonio al 30-jun-2026 (10-Q); antes 415.265, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 415.265,0 | 640.480,0 | Patrimonio al 30-jun-2026 (10-Q); antes 415.265, el cierre de 2025. |
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,286 | 0,293 | Ventaja durable: Escala y efectos de red en búsqueda, YouTube y Android; datos. Evidencia: ROIC 24-31% en 2021-2026. ROIC después del año 10 = el promedio de la industria (29,3%), sin superar el ROIC actual (31,3%): 29,3% (Damodaran, Investment Valuation, cap. 12). |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | 34.875,0 | LTM = ejercicio 7242.0 + acumulado al 2026-06-30 25203.0 − acumulado del año anterior -2430.0 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement I23 | Basic EPS 2023-12-31 | 5,80 | 5,84 | EPS básico del 10-K (2023-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2024-12-31 | 8,04 | 8,13 | EPS básico del 10-K (2024-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2025-12-31 | 10,81 | 10,91 | EPS básico del 10-K (2025-12-31); antes copiaba el diluido. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores C < B < A < D | Sí |
| Valor esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al valor esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | >$50,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- Arrendamientos operativos: la deuda del DCF incluye 18.037,0 millones de arrendamientos operativos mientras el EBIT ya descuenta el alquiler (conversor de arrendamientos desactivado). Con el criterio de Damodaran o se convierten (deuda y EBIT ajustado) o se excluyen; excluirlos subiría el DCF en ~US$1,47 por acción. Es una decisión de método pendiente; no se cambió en esta auditoría.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF esperado de las cuatro historias: US$274,02 (antes US$251,35); precio con margen de seguridad US$178,11. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
