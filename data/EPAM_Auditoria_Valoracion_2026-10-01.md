---
schema: "jmr-audit-v1"
ticker: "EPAM"
company: "EPAM Systems, Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de EPAM Systems, Inc. (EPAM)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$168,22 | US$169,54 |
| Historia A | US$165,87 | US$167,18 |
| Historia B | US$110,21 | US$109,51 |
| Historia C | US$81,42 | US$80,66 |
| Historia D | US$218,87 | US$221,07 |
| **Valor esperado (valor intrínseco principal)** | **US$148,68** | **US$149,31** |
| Precio con MOS sobre el esperado | US$96,64 | US$97,05 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L21 | Arrendamientos corrientes | — | 39,30 | Porción corriente de arrendamientos al 30-jun-2026 (10-Q 2T26). |
| Balance del último 10-Q | Balance Sheet L26 | Arrendamientos de largo plazo | 81,50 | 88,00 | Arrendamientos de largo plazo al 30-jun-2026 (10-Q); antes 81,5. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 3.677,2 | 3.519,0 | Patrimonio al 30-jun-2026 (10-Q); antes 3.677,2, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 3.677,2 | 3.519,0 | Patrimonio al 30-jun-2026 (10-Q); antes 3.677,2, el cierre de 2025. |
| ROIC terminal (criterio Damodaran) | Input sheet B49 | ¿ROIC terminal propio? | No | Yes | Ventaja que se desvanece: Servicios de ingeniería con costos de cambio moderados. Evidencia: ROIC 47% → 15% en cinco años, acercándose al costo de capital. ROIC después del año 10 = 11,4%, punto medio entre el costo de capital terminal (9,0%) y el promedio de la industria (26,4%), sin superar el ROIC actual (13,8%): 13,8%, porque la ventaja se desvanece. |
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,200 | 0,114 | Ventaja que se desvanece: Servicios de ingeniería con costos de cambio moderados. Evidencia: ROIC 47% → 15% en cinco años, acercándose al costo de capital. ROIC después del año 10 = 11,4%, punto medio entre el costo de capital terminal (9,0%) y el promedio de la industria (26,4%), sin superar el ROIC actual (13,8%): 13,8%, porque la ventaja se desvanece. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | -252,2 | LTM = ejercicio 11.0 + acumulado al 2026-06-30 -507.1 − acumulado del año anterior -243.9 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement I23 | Basic EPS 2023-12-31 | 7,06 | 7,21 | EPS básico del 10-K (2023-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2024-12-31 | 7,84 | 7,93 | EPS básico del 10-K (2024-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2025-12-31 | 6,72 | 6,76 | EPS básico del 10-K (2025-12-31); antes copiaba el diluido. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores C < B < A < D | Sí |
| Valor esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al valor esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $3,000-4,500 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- Arrendamientos operativos: la deuda del DCF incluye 127,3 millones de arrendamientos operativos mientras el EBIT ya descuenta el alquiler (conversor de arrendamientos desactivado). Con el criterio de Damodaran o se convierten (deuda y EBIT ajustado) o se excluyen; excluirlos subiría el DCF en ~US$2,47 por acción. Es una decisión de método pendiente; no se cambió en esta auditoría.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF esperado de las cuatro historias: US$149,31 (antes US$148,68); precio con margen de seguridad US$97,05. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
