---
schema: "jmr-audit-v1"
ticker: "NVO"
company: "Novo Nordisk A/S"
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Novo Nordisk A/S (NVO)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$41,96 | US$32,62 |
| **DCF Base (valor intrínseco principal)** | US$38,98 | US$32,62 |
| DCF Conservadora | US$28,26 | US$25,57 |
| DCF Disrupción | US$22,47 | US$20,71 |
| DCF Optimista | US$46,57 | US$39,84 |
| DCF esperado por probabilidades (complemento) | US$35,63 | US$30,76 |
| Precio con MOS sobre el esperado | US$23,16 | US$19,99 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Conversor de I+D alineado al LTM | R& D converter B12 | I+D año −1 | ='Income Statement'!K10 | ='Income Statement'!J10*45288/48062 | 12 meses a jun-2025 = 2024 (48.062) + 1S25 (21.998) − 1S24 (24.772) = 45.288 MDKK (6-K 2T25 y 4T24). Antes el ejercicio 2025, que se solapa con el LTM. |
| Conversor de I+D alineado al LTM | R& D converter B13 | I+D año −2 | ='Income Statement'!J10 | ='Income Statement'!I10*43360/32443 | 12 meses a jun-2024 = 2023 (32.443) + 1S24 (24.772) − 1S23 (13.855) = 43.360 MDKK. Antes el ejercicio 2024. |
| Conversor de I+D alineado al LTM | R& D converter B14 | I+D año −3 | ='Income Statement'!I10 | ='Income Statement'!H10*27573/24047 | 12 meses a jun-2023 = 2022 (24.047) + 1S23 (13.855) − 1S22 (10.329) = 27.573 MDKK. Antes el ejercicio 2023. |
| Conversor de I+D alineado al LTM | R& D converter B15 | I+D año −4 | ='Income Statement'!H10 | ='Income Statement'!G10*20213/17772 | 12 meses a jun-2022 = 2021 (17.772) + 1S22 (10.329) − 1S21 (7.888) = 20.213 MDKK. Antes el ejercicio 2022. |
| Conversor de I+D alineado al LTM | R& D converter B16 | I+D año −5 | ='Income Statement'!G10 | ='Income Statement'!F10*16282/15462 | 12 meses a jun-2021 = 2020 (15.462) + 1S21 (7.888) − 1S20 (7.068) = 16.282 MDKK. Antes el ejercicio 2021. |
| Ventas/capital contrastado con la historia y la industria | Input sheet B32 |  | 0,450 | 0,570 | Ventas/capital revisado (1-oct-2026): historia 2023-2025 0,57 (capex, intangibles y compras) e industria Drugs (Pharmaceutical) 1,11. El valor anterior quedaba fuera de ese rango por más de 10%; se lleva al borde más cercano. Incluye el capital arrendado (criterio Damodaran). |
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
| Tramo de tasas base (dólares de 2015) | >$25,000 Mn |
| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |

## Salvedades abiertas

- Arrendamientos: bajo NIIF 16 todos los arrendamientos están en el balance y el EBIT ya excluye su costo financiero, así que su pasivo es deuda; se conserva en la deuda del DCF.
- Emisor extranjero (NIIF) sin XBRL trimestral en la SEC: flujos LTM y EPS no se contrastaron de forma automática; el balance se revisó con el informe semestral.
- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$32,62 (antes US$38,98). El DCF esperado de las cuatro historias, complementario, es US$30,76 (antes US$35,63); precio con margen de seguridad sobre el esperado US$19,99. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
