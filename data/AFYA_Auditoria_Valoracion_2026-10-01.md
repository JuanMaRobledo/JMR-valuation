---
schema: "jmr-audit-v1"
ticker: "AFYA"
company: "Afya Limited"
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Afya Limited (AFYA)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$25,29 | US$23,77 |
| **DCF Base (valor intrínseco principal)** | US$26,06 | US$23,77 |
| DCF Conservadora | US$20,67 | US$19,18 |
| DCF Disrupción | US$12,55 | US$12,31 |
| DCF Optimista | US$30,25 | US$27,41 |
| DCF esperado por probabilidades (complemento) | US$22,83 | US$21,04 |
| Precio con MOS sobre el esperado | US$14,84 | US$13,67 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| ROIC terminal (criterio Damodaran) | Input sheet B50 | ROIC después del año 10 | 0,129 | 0,148 | Ventaja durable: Licencias reguladas de Medicina (una sola fuente, depende de la política). Evidencia: ROIC 12-16%, apenas 1-5 pp sobre el costo de capital desde 2022. ROIC después del año 10 = el promedio de la industria (15,9%), sin superar el ROIC actual (14,8%): 14,8% (Damodaran, Investment Valuation, cap. 12). |
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
| Tramo de tasas base (dólares de 2015) | $325-700 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- Arrendamientos: bajo NIIF 16 todos los arrendamientos están en el balance y el EBIT ya excluye su costo financiero, así que su pasivo es deuda; se conserva en la deuda del DCF.
- Emisor extranjero (NIIF) sin XBRL trimestral en la SEC: flujos LTM y EPS no se contrastaron de forma automática; el balance se revisó con el informe semestral.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$23,77 (antes US$26,06). El DCF esperado de las cuatro historias, complementario, es US$21,04 (antes US$22,83); precio con margen de seguridad sobre el esperado US$13,67. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
