---
schema: "jmr-audit-v1"
ticker: "ONON"
company: "On Holding AG"
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de On Holding AG (ONON)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$38,92 | US$38,84 |
| Historia A | US$38,33 | US$38,25 |
| Historia B | US$22,96 | US$22,87 |
| Historia C | US$14,81 | US$14,71 |
| Historia D | US$53,37 | US$53,31 |
| **Valor esperado (valor intrínseco principal)** | **US$34,38** | **US$34,29** |
| Precio con MOS sobre el esperado | US$22,34 | US$22,29 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L20 | Deuda corriente | 102,6 | 108,7 | Arrendamientos corrientes al 30-jun-2026: 87,9 MCHF × 1,2366 (6-K 1S26). Antes 102,6, el cierre de 2025. Sin deuda bancaria dispuesta. |
| Balance del último 10-Q | Balance Sheet L26 | Arrendamientos de largo plazo | 556,1 | 586,9 | Arrendamientos no corrientes al 30-jun-2026: 474,6 MCHF × 1,2366 (6-K 1S26). Antes 556,1. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 2.061,9 | 2.363,6 | Patrimonio al 30-jun-2026: 1.911,4 MCHF × 1,2366 (6-K 1S26). Antes 2.061,9, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 2.061,9 | 2.363,6 | Patrimonio al 30-jun-2026: 1.911,4 MCHF × 1,2366 (6-K 1S26). Antes 2.061,9, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L16 | Activos totales | 3.581,4 | 4.010,2 | Activos totales al 30-jun-2026: 3.242,9 MCHF × 1,2366 (6-K 1S26). |
| Balance del último 10-Q | Balance Sheet L29 | Pasivos totales | 1.519,5 | 1.646,5 | Pasivos totales al 30-jun-2026: 1.331,5 MCHF × 1,2366 (6-K 1S26). |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | =L13+L22+L34 | Auditoría 1-oct-2026: cambio de caja LTM = operación + inversión + financiación (sin efecto cambiario). Antes −14, un valor de relleno del importador. |
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

- Arrendamientos operativos: la deuda del DCF incluye 586,9 millones de arrendamientos operativos mientras el EBIT ya descuenta el alquiler (conversor de arrendamientos desactivado). Con el criterio de Damodaran o se convierten (deuda y EBIT ajustado) o se excluyen; excluirlos subiría el DCF en ~US$1,77 por acción. Es una decisión de método pendiente; no se cambió en esta auditoría.
- Emisor extranjero (NIIF) sin XBRL trimestral en la SEC: flujos LTM y EPS no se contrastaron de forma automática; el balance se revisó con el informe semestral.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF esperado de las cuatro historias: US$34,29 (antes US$34,38); precio con margen de seguridad US$22,29. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
