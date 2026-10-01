---
schema: "jmr-audit-v1"
ticker: "LULU"
company: "lululemon athletica inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de lululemon athletica inc. (LULU)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$167,44 | US$167,44 |
| Historia A | US$172,25 | US$172,25 |
| Historia B | US$108,35 | US$108,35 |
| Historia C | US$71,34 | US$71,34 |
| Historia D | US$229,97 | US$229,97 |
| **Valor esperado (valor intrínseco principal)** | **US$148,45** | **US$148,45** |
| Precio con MOS sobre el esperado | US$103,91 | US$103,91 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| ROIC terminal (criterio Damodaran) | Input sheet B49 | ¿ROIC terminal propio? | No | Yes | Ventaja que se desvanece: Marca premium (una sola fuente). Evidencia: ROIC 27-52% en 2021-2026, en descenso. ROIC después del año 10 = 12,4%, punto medio entre el costo de capital terminal (9,0%) y el promedio de la industria (15,8%), sin superar el ROIC actual (25,2%): 15,8%, porque la ventaja se desvanece. |
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,158 | 0,124 | Ventaja que se desvanece: Marca premium (una sola fuente). Evidencia: ROIC 27-52% en 2021-2026, en descenso. ROIC después del año 10 = 12,4%, punto medio entre el costo de capital terminal (9,0%) y el promedio de la industria (15,8%), sin superar el ROIC actual (25,2%): 15,8%, porque la ventaja se desvanece. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | 1.117,7 | 233,9 | LTM = ejercicio -177.1 + acumulado al 2026-08-02 -417.5 − acumulado del año anterior -828.5 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes 1117.738. |
| EPS básico | Income Statement I23 | Basic EPS 2024-01-28 | 12,20 | 12,23 | EPS básico del 10-K (2024-01-28); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2025-02-02 | 14,64 | 14,67 | EPS básico del 10-K (2025-02-02); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2026-02-01 | 13,26 | 13,27 | EPS básico del 10-K (2026-02-01); antes copiaba el diluido. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores C < B < A < D | Sí |
| Valor esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al valor esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $7,000-12,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- Arrendamientos operativos: la deuda del DCF incluye 2.141,1 millones de arrendamientos operativos mientras el EBIT ya descuenta el alquiler (conversor de arrendamientos desactivado). Con el criterio de Damodaran o se convierten (deuda y EBIT ajustado) o se excluyen; excluirlos subiría el DCF en ~US$19,34 por acción. Es una decisión de método pendiente; no se cambió en esta auditoría.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF esperado de las cuatro historias: US$148,45 (antes US$148,45); precio con margen de seguridad US$103,91. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
