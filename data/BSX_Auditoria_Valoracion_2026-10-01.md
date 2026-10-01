---
schema: "jmr-audit-v1"
ticker: "BSX"
company: "Boston Scientific Corporation"
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Boston Scientific Corporation (BSX)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$36,39 | US$37,06 |
| Historia A | US$35,35 | US$36,01 |
| Historia B | US$28,07 | US$28,71 |
| Historia C | US$21,76 | US$22,38 |
| Historia D | US$42,65 | US$43,33 |
| **Valor esperado (valor intrínseco principal)** | **US$33,95** | **US$34,60** |
| Precio con MOS sobre el esperado | US$22,06 | US$22,49 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L20 | Deuda corriente | 299,0 | 1.709,0 | Deuda corriente al 30-jun-2026 (DebtCurrent, 10-Q 2T26); antes 299, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L25 | Deuda de largo plazo | 11.137,0 | 10.915,0 | Deuda de largo plazo al 30-jun-2026 (10-Q 2T26); antes 11.137, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L14 | Inversiones no operativas | 0,00 | 2.245,0 | Inversiones al 30-jun-2026: método de participación 1.308 + sin valor de mercado 938 (10-Q). Antes 0: son activos no operativos. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 24.233,0 | 24.930,0 | Patrimonio de los accionistas al 30-jun-2026 (10-Q); antes 24.233, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 24.233,0 | 25.172,0 | Patrimonio total con minoritarios al 30-jun-2026 (10-Q). |
| Balance del último 10-Q | Input sheet B21 | Minoritarios (DCF) | 0,00 | 242,0 | Participaciones minoritarias al 30-jun-2026 (10-Q 2T26); antes 0. |
| Balance del último 10-Q | Input sheet B15 | Patrimonio (DCF) | ='Balance Sheet'!L35 | ='Balance Sheet'!L34 | Patrimonio de los accionistas (sin minoritarios, que se restan aparte). |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | 12,00 | LTM = ejercicio 1541.0 + acumulado al 2026-06-30 -1394.0 − acumulado del año anterior 135.0 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| EPS básico | Income Statement I23 | Basic EPS 2023-12-31 | 1,09 | 1,08 | EPS básico del 10-K (2023-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement J23 | Basic EPS 2024-12-31 | 1,24 | 1,26 | EPS básico del 10-K (2024-12-31); antes copiaba el diluido. |
| EPS básico | Income Statement K23 | Basic EPS 2025-12-31 | 1,94 | 1,96 | EPS básico del 10-K (2025-12-31); antes copiaba el diluido. |
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

- Arrendamientos operativos: la deuda del DCF incluye 446,0 millones de arrendamientos operativos mientras el EBIT ya descuenta el alquiler (conversor de arrendamientos desactivado). Con el criterio de Damodaran o se convierten (deuda y EBIT ajustado) o se excluyen; excluirlos subiría el DCF en ~US$0,31 por acción. Es una decisión de método pendiente; no se cambió en esta auditoría.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF esperado de las cuatro historias: US$34,60 (antes US$33,95); precio con margen de seguridad US$22,49. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
