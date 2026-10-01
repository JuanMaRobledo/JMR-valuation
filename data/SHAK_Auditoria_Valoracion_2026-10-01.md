---
schema: "jmr-audit-v1"
ticker: "SHAK"
company: "Shake Shack Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Shake Shack Inc. (SHAK)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$20,93 | US$20,30 |
| Historia A | US$21,00 | US$20,35 |
| Historia B | US$10,04 | US$9,40 |
| Historia C | US$7,90 | US$7,26 |
| Historia D | US$36,39 | US$35,75 |
| **Valor esperado (valor intrínseco principal)** | **US$18,71** | **US$18,06** |
| Precio con MOS sobre el esperado | US$12,16 | US$11,74 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L26 | Arrendamientos de largo plazo | 575,1 | 622,0 | Arrendamientos operativos de largo plazo al 1-jul-2026 (10-Q 2T26); antes 575,1. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 525,3 | 544,0 | Patrimonio de los accionistas al 1-jul-2026 (10-Q); antes 525,3, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 525,3 | 572,0 | Patrimonio total con minoritarios al 1-jul-2026 (10-Q). |
| Balance del último 10-Q | Input sheet B15 | Patrimonio (DCF) | ='Balance Sheet'!L35 | ='Balance Sheet'!L34 | Patrimonio de los accionistas (sin minoritarios, que se restan aparte). |
| Balance del último 10-Q | Input sheet B21 | Minoritarios (DCF) | 0,00 | 27,00 | Participaciones minoritarias al 1-jul-2026 (10-Q 2T26); antes 0. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | -28,80 | LTM = ejercicio 39.4 + acumulado al 2026-07-01 -52.2 − acumulado del año anterior 16.1 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
| Capital invertido operativo | Valuation output B41 | Invested capital | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | =IF('Input sheet'!$B$18="Yes";IF('Input sheet'!$B$17="Yes";' | Capital invertido operativo: se restan los activos no operativos (Input B20). |

## Verificación de las historias

| Control | Resultado |
|---|---|
| Las probabilidades suman 100% | Sí |
| Orden de valores C < B < A < D | Sí |
| Valor esperado = Σ probabilidad × DCF | Sí |
| MOS aplicado al valor esperado | Sí |
| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |
| Tramo de tasas base (dólares de 2015) | $700-1,250 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF esperado de las cuatro historias: US$18,06 (antes US$18,71); precio con margen de seguridad US$11,74. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
