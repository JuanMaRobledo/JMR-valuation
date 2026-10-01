---
schema: "jmr-audit-v1"
ticker: "PAGS"
company: "PagSeguro Digital Ltd."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de PagSeguro Digital Ltd. (PAGS)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$11,92 | US$11,92 |
| **DCF Base (valor intrínseco principal)** | US$11,89 | US$11,89 |
| DCF Conservadora | US$11,14 | US$11,14 |
| DCF Disrupción | US$9,99 | US$9,99 |
| DCF Optimista | US$12,73 | US$12,73 |
| DCF esperado por probabilidades (complemento) | US$11,60 | US$11,60 |
| Precio con MOS sobre el esperado | US$7,54 | US$7,54 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 2.673,3 | 2.742,0 | Patrimonio al 30-jun-2026: R$15.015.865 mil / 5.4762 (6-K 1S26). Antes 2.673,3, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 2.673,3 | 2.742,0 | Patrimonio al 30-jun-2026: R$15.015.865 mil / 5.4762 (6-K 1S26). Antes 2.673,3, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L16 | Activos totales | 13.587,8 | 13.823,0 | Activos totales al 30-jun-2026: R$75.697.476 mil / 5.4762 (6-K 1S26). |
| Balance del último 10-Q | Balance Sheet L29 | Pasivos totales | 10.914,5 | 11.080,9 | Pasivos totales al 30-jun-2026 = activos − patrimonio (6-K 1S26). |
| Balance del último 10-Q | Cash Flow Statement K22 |  | 0,00 | -411,6 | Flujo de inversión 2025: −R$2.299.796 mil / 5.5877 (20-F 2025). Antes 0 (no importado). |
| Balance del último 10-Q | Cash Flow Statement K34 |  | 0,00 | -775,4 | Flujo de financiación 2025: −R$4.332.796 mil / 5.5877 (20-F 2025). Antes 0 (no importado). |
| Balance del último 10-Q | Cash Flow Statement L13 |  | 1.429,4 | 1.082,6 | Flujo operativo LTM = 2025 (7.562.431) + 1S26 (1.938.645) − 1S25 (3.451.822) = R$6.049.254 mil / 5.5877 (20-F y 6-K). |
| Balance del último 10-Q | Cash Flow Statement L22 |  | 0,00 | -431,9 | Flujo de inversión LTM = −2.299.796 − 1.215.583 + 1.101.798 = −R$2.413.581 mil / 5.5877 (20-F y 6-K). Antes 0. |
| Balance del último 10-Q | Cash Flow Statement L34 | Patrimonio de los accionistas | 0,00 | -740,9 | Flujo de financiación LTM = −4.332.796 − 1.956.893 + 2.149.485 = −R$4.140.204 mil / 5.5877 (20-F y 6-K). Antes 0. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | =L13+L22+L34 | Auditoría 1-oct-2026: cambio de caja LTM = operación + inversión + financiación (sin efecto cambiario). Antes −14, un valor de relleno del importador. Inversión y financiación LTM están en 0 en la hoja (no importadas); no afectan al DCF de flujo al accionista. |
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
- Financiera (DCF de flujo al accionista): balance y flujos LTM actualizados con el 20-F 2025 y el 6-K del 1S26 (convertidos a los tipos implícitos de la hoja); no afectan al valor, que depende de utilidad, ROE y costo del patrimonio.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$11,89 (antes US$11,89). El DCF esperado de las cuatro historias, complementario, es US$11,60 (antes US$11,60); precio con margen de seguridad sobre el esperado US$7,54. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
