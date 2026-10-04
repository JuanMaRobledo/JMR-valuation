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
| DCF técnico anterior (caso Base de la hoja) | US$38,92 | US$33,74 |
| **DCF Base (valor intrínseco principal)** | US$38,33 | US$33,74 |
| DCF Conservadora | US$22,96 | US$21,08 |
| DCF Disrupción | US$14,81 | US$12,66 |
| DCF Optimista | US$53,37 | US$47,29 |
| DCF esperado por probabilidades (complemento) | US$34,38 | US$31,18 |
| Precio con MOS sobre el esperado | US$22,34 | US$20,27 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L20 | Deuda corriente | 102,6 | 108,7 | Arrendamientos corrientes al 30-jun-2026: 87,9 MCHF × 1,2366 (6-K 1S26). Antes 102,6, el cierre de 2025. Sin deuda bancaria dispuesta. |
| Balance del último 10-Q | Balance Sheet L26 | Arrendamientos de largo plazo | 556,1 | 586,9 | Arrendamientos no corrientes al 30-jun-2026: 474,6 MCHF × 1,2366 (6-K 1S26). Antes 556,1. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 2.061,9 | 2.363,6 | Patrimonio al 30-jun-2026: 1.911,4 MCHF × 1,2366 (6-K 1S26). Antes 2.061,9, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 2.061,9 | 2.363,6 | Patrimonio al 30-jun-2026: 1.911,4 MCHF × 1,2366 (6-K 1S26). Antes 2.061,9, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L16 | Activos totales | 3.581,4 | 4.010,2 | Activos totales al 30-jun-2026: 3.242,9 MCHF × 1,2366 (6-K 1S26). |
| Balance del último 10-Q | Balance Sheet L29 | Pasivos totales | 1.519,5 | 1.646,5 | Pasivos totales al 30-jun-2026: 1.331,5 MCHF × 1,2366 (6-K 1S26). |
| Ventas/capital contrastado con la historia y la industria | Input sheet B33 |  | 2,20 | 2,62 | Ventas/capital revisado (1-oct-2026): historia 2023-2025 2,77 (con derechos de uso) e industria Shoe 2,62. El valor anterior quedaba fuera de ese rango por más de 10%; se lleva al borde más cercano. Incluye el capital arrendado (criterio Damodaran). |
| Margen objetivo Base de la hoja enlazado al de Input sheet | Valuation output C46 |  | 0,170 | ='Input sheet'!B30 | Margen objetivo Base enlazado a 'Input sheet'!B30: el valor escrito a mano no seguía a B30 (ajuste por arrendamientos de Damodaran y revisiones del 30-sep-2026), y el DCF de la hoja mezclaba un margen inicial ajustado con un objetivo sin ajustar. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | =L13+L22+L34 | Auditoría 1-oct-2026: cambio de caja LTM = operación + inversión + financiación (sin efecto cambiario). Antes −14, un valor de relleno del importador. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores Disrupción < Conservadora < Base < Optimista | Sí |
| DCF esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al DCF esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $2,000-3,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- Arrendamientos: bajo NIIF 16 todos los arrendamientos están en el balance y el EBIT ya excluye su costo financiero, así que su pasivo es deuda; se conserva en la deuda del DCF.
- Emisor extranjero (NIIF) sin XBRL trimestral en la SEC: flujos LTM y EPS no se contrastaron de forma automática; el balance se revisó con el informe semestral.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$33,74 (antes US$38,33). El DCF esperado de las cuatro historias, complementario, es US$31,18 (antes US$34,38); precio con margen de seguridad sobre el esperado US$20,27. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
