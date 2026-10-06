---
schema: "jmr-audit-v1"
ticker: "MCD"
company: "McDonald's Corporation"
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de McDonald's Corporation (MCD)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$224,12 | US$224,12 |
| **DCF Base (valor intrínseco principal)** | US$224,12 | US$224,12 |
| DCF Conservadora | US$185,42 | US$185,42 |
| DCF Disrupción | US$75,44 | US$75,44 |
| DCF Optimista | US$253,34 | US$253,34 |
| DCF esperado por probabilidades (complemento) | US$203,96 | US$203,96 |
| Precio con MOS sobre el esperado | US$132,57 | US$132,57 |

## Hallazgos y correcciones

Sin correcciones de datos: los estados de la hoja coinciden con la SEC en las filas revisadas.

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores Disrupción < Conservadora < Base < Optimista | Sí |
| DCF esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al DCF esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $12,000-25,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$224,12 (antes US$224,12). El DCF esperado de las cuatro historias, complementario, es US$203,96 (antes US$203,96); precio con margen de seguridad sobre el esperado US$132,57. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
