---
schema: "jmr-audit-v1"
ticker: "ADSK"
company: "Autodesk, Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Autodesk, Inc. (ADSK)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$192,58 | US$192,58 |
| **DCF Base (valor intrínseco principal)** | US$192,58 | US$192,58 |
| DCF Conservadora | US$142,52 | US$142,52 |
| DCF Disrupción | US$57,76 | US$57,76 |
| DCF Optimista | US$236,72 | US$236,72 |
| DCF esperado por probabilidades (complemento) | US$166,46 | US$166,46 |
| Precio con MOS sobre el esperado | US$108,20 | US$108,20 |

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
| Tramo de tasas base (dólares de 2015) | $4,500-7,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$192,58 (antes US$192,58). El DCF esperado de las cuatro historias, complementario, es US$166,46 (antes US$166,46); precio con margen de seguridad sobre el esperado US$108,20. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
