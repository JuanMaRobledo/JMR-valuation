---
schema: "jmr-audit-v1"
ticker: "NVDA"
company: "NVIDIA Corporation"
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de NVIDIA Corporation (NVDA)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$259,29 | US$263,61 |
| Historia A | US$204,91 | US$209,15 |
| Historia B | US$121,20 | US$125,35 |
| Historia C | US$50,24 | US$54,31 |
| Historia D | US$313,47 | US$317,84 |
| **Valor esperado (valor intrínseco principal)** | **US$186,04** | **US$190,27** |
| Precio con MOS sobre el esperado | US$120,93 | US$123,67 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L4 | Inversiones de corto plazo | 0,00 | 34.143,0 | Valores negociables (deuda) al 26-jul-2026 (10-Q 2T FY27); antes 0. |
| Balance del último 10-Q | Balance Sheet L5 | Caja y valores negociables | 22.443,0 | 56.586,0 | Caja 22.443 + valores negociables 34.143 al 26-jul-2026 (10-Q). |
| Balance del último 10-Q | Balance Sheet L14 | Inversiones no operativas | 0,00 | 90.681,0 | Inversiones en acciones al 26-jul-2026: cotizadas 42.783 + no cotizadas 47.898 (10-Q); antes 0: son activos no operativos. |
| Balance del último 10-Q | Balance Sheet L20 | Deuda corriente | 999,0 | 1.000,0 | Porción corriente de la deuda al 26-jul-2026 (10-Q). |
| Balance del último 10-Q | Balance Sheet L25 | Deuda de largo plazo | 7.469,0 | 32.366,0 | Deuda de largo plazo al 26-jul-2026 (10-Q); antes 7.469, el cierre de enero de 2026. |
| Balance del último 10-Q | Balance Sheet L21 | Arrendamientos corrientes | — | 509,0 | Arrendamientos operativos corrientes al 26-jul-2026 (10-Q). |
| Balance del último 10-Q | Balance Sheet L26 | Arrendamientos de largo plazo | 2.572,0 | 4.985,0 | Arrendamientos operativos de largo plazo al 26-jul-2026 (10-Q); antes 2.572. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 157.293,0 | 228.984,0 | Patrimonio al 26-jul-2026 (10-Q); antes 157.293, el cierre de enero de 2026. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 157.293,0 | 228.984,0 | Patrimonio al 26-jul-2026 (10-Q); antes 157.293, el cierre de enero de 2026. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | 10.804,0 | LTM = ejercicio 2016.0 + acumulado al 2026-07-26 11838.0 − acumulado del año anterior 3050.0 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement J23 | Basic EPS 2025-01-26 | 2,94 | 2,97 | EPS básico del 10-K (2025-01-26); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2026-01-25 | 4,90 | 4,93 | EPS básico del 10-K (2026-01-25); antes copiaba el diluido. |
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

- Arrendamientos operativos: la deuda del DCF incluye 5.494,0 millones de arrendamientos operativos mientras el EBIT ya descuenta el alquiler (conversor de arrendamientos desactivado). Con el criterio de Damodaran o se convierten (deuda y EBIT ajustado) o se excluyen; excluirlos subiría el DCF en ~US$0,23 por acción. Es una decisión de método pendiente; no se cambió en esta auditoría.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF esperado de las cuatro historias: US$190,27 (antes US$186,04); precio con margen de seguridad US$123,67. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
