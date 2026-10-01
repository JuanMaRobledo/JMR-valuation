---
schema: "jmr-audit-v1"
ticker: "CELH"
company: "Celsius Holdings, Inc."
analysis_date: "2026-10-01"
information_cutoff: "2026-09-30"
language: "es"
---

# Auditoría de la valoración de Celsius Holdings, Inc. (CELH)

Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.

## Resultados antes y después

| Concepto | Antes | Después |
|---|---:|---:|
| DCF técnico anterior (caso Base de la hoja) | US$18,12 | US$18,41 |
| **DCF Base (valor intrínseco principal)** | US$22,22 | US$18,41 |
| DCF Conservadora | US$15,48 | US$10,74 |
| DCF Disrupción | US$8,94 | US$3,30 |
| DCF Optimista | US$28,84 | US$25,93 |
| DCF esperado por probabilidades (complemento) | US$18,53 | US$14,21 |
| Precio con MOS sobre el esperado | US$12,05 | US$9,24 |

## Hallazgos y correcciones

| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |
|---|---|---|---:|---:|---|
| Balance del último 10-Q | Balance Sheet L25 | Deuda de largo plazo | 669,9 | 668,0 | Deuda de largo plazo al 30-jun-2026 (10-Q 2T26); antes 669,9, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L34 | Patrimonio de los accionistas | 1.181,5 | 1.200,0 | Patrimonio al 30-jun-2026 (10-Q); antes 1.181,5, el cierre de 2025. |
| Balance del último 10-Q | Balance Sheet L35 | Patrimonio total | 1.181,5 | 1.200,0 | Patrimonio al 30-jun-2026 (10-Q); antes 1.181,5, el cierre de 2025. |
| Deuda de balance sin arrendamientos operativos | Input sheet B16 | Deuda (DCF) | ='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25 | ='Balance Sheet'!L20+'Balance Sheet'!L25 | Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda. |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter E5 |  | 295,0 | 5,70 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B8 |  | 287,0 | 5,01 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B9 |  | 235,0 | 5,19 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B10 |  | 194,0 | 4,01 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B11 |  | 151,0 | 3,70 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B12 | I+D año −1 | 98,00 | 0,680 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Operating lease converter B13 | I+D año −2 | 605,0 | 2,02 | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B18 |  | No | Yes | Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al 2025-12-31 (SEC XBRL). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B28 |  | 0,120 | 0,121 | Margen en base ajustada por arrendamientos: + 0.09 pp (ajuste del EBIT 2.8 / ventas 3047.3). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B30 |  | 0,170 | 0,171 | Margen en base ajustada por arrendamientos: + 0.09 pp (ajuste del EBIT 2.8 / ventas 3047.3). |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B32 |  | 2,50 | 2,47 | Ventas/capital con el capital arrendado: 1/(1/2.5 + 0.0056), con VP de arrendamientos 17.2 / ventas 3047.3. |
| Arrendamientos como deuda (conversor, Damodaran) | Input sheet B33 |  | 2,00 | 1,98 | Ventas/capital con el capital arrendado: 1/(1/2 + 0.0056), con VP de arrendamientos 17.2 / ventas 3047.3. |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C45 |  | 0,110 | 0,111 | Margen en base ajustada por arrendamientos: + 0.09 pp (ajuste del EBIT 2.8 / ventas 3047.3). |
| Arrendamientos como deuda (conversor, Damodaran) | Valuation output C47 |  | 0,210 | 0,211 | Margen en base ajustada por arrendamientos: + 0.09 pp (ajuste del EBIT 2.8 / ventas 3047.3). |
| Margen objetivo Base de la hoja enlazado al de Input sheet | Valuation output C46 |  | 0,170 | ='Input sheet'!B30 | Margen objetivo Base enlazado a 'Input sheet'!B30: el valor escrito a mano no seguía a B30 (ajuste por arrendamientos de Damodaran y revisiones del 30-sep-2026), y el DCF de la hoja mezclaba un margen inicial ajustado con un objetivo sin ajustar. |
| Flujos LTM | Cash Flow Statement L40 | Net Change in Cash | -14,00 | 17,90 | LTM = ejercicio -350.2 + acumulado al 2026-06-30 93.1 − acumulado del año anterior -275.0 (CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect). Antes -14. |
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

- No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

## Dictamen

El valor intrínseco principal es el DCF Base: US$18,41 (antes US$22,22). El DCF esperado de las cuatro historias, complementario, es US$14,21 (antes US$18,53); precio con margen de seguridad sobre el esperado US$9,24. Las correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.

Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.
