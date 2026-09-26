# ADSK (Autodesk, Inc.) — Valoración Modelo JMR (Damodaran + 5 múltiplos)

- **Hoja del modelo:** [Modelo_JMR_ADSK](https://docs.google.com/spreadsheets/d/17eku40NKWd72OBZEQ85diKEaNNSH1zuJrnhG6ucmJok/edit) (copia nueva de la plantilla maestra, en AAA Finanzas › Análisis › ADSK)
- **Fecha de corte de los datos:** 10-Q del Q2 FY2027 (31-jul-2026, presentado el 28-ago-2026). LTM = ago-2025 a jul-2026.
- **Fecha y precio de cotización del análisis:** 25-sep-2026, **US$209,40** (cierre)
- **WACC:** 10,79% (Ke 11,23%, Kd después de impuestos 4,63%, D/(D+E) 6,6%)
- **Tipo de empresa (ponderación):** Software — DCF 60%, EV/FCFF 15%, EV/EBITDA 10%, P/E 5%, P/FCFE 5%, P/OCF 5%
- **Script reproducible:** `scripts/run_adsk.py` + `scripts/adsk_content.py` (repo JMR-valuation); backup de cada celda pisada en `reference/backups/adsk_formula_backup.json`

## Resultado

| Escenario | Valor DCF / acción | DCF vs. precio | Precio objetivo ponderado | Ponderado vs. precio |
|---|---|---|---|---|
| Conservador | US$151,65 | −27,6% | US$215,17 | +2,8% |
| **Base** | **US$196,76** | **−6,0%** | **US$279,04** | **+33,3%** |
| Optimista | US$259,57 | +24,0% | US$361,81 | +72,8% |

Orden verificado: Conservador < Base < Optimista en crecimiento, margen objetivo, valor DCF y precio ponderado.

**Lectura:** a US$209,40 Autodesk cotiza un 6% por encima de su DCF Base, entre el Conservador y el Optimista. No hay margen de seguridad en el DCF, pero el precio tampoco exige un escenario heroico. El precio ponderado Base (US$279) es mayor solo porque los múltiplos se anclan a 2023-2026 (P/E GAAP de ~48-60x contra ~24x hoy): hay que leerlos como el techo si vuelve la valuación histórica, no como el valor central.

## La historia

Autodesk es el estándar del diseño técnico y de la construcción (AutoCAD/DWG, Revit). Crece 14-16%, tiene margen bruto de 91% y una meta explícita de 41% de margen non-GAAP para FY2029. La acción cayó a ~17x la utilidad non-GAAP proyectada por dos motivos: el temor a que la IA reduzca los usuarios que pagan (−8% el 4-sep-2026 en la venta de todo el software) y un UST 10 años de 5,17%. En agosto pagó US$3.530M por MaintainX y pasó de caja neta a una deuda neta de ~US$3.100M.

## Supuestos por escenario

| Supuesto | Conservador | Base | Optimista | Ancla |
|---|---|---|---|---|
| Crecimiento Año 1 | 8,5% | 13,0% | 14,0% | Guía FY2027 (+15-16%) ⇒ ~14% en el H2 con MaintainX (~12% orgánico); billings +10-11% |
| Crecimiento años 2-5 | 8,5% | 10,0% | 14,0% | Billings y cRPO +10-12%; el empuje del cambio de modelo de transacción se agota |
| Margen Año 1 (ajustado por I+D) | 29,5% | 29,5% | 29,5% | Base ajustada 29,0% ('Valuation output'!B6; GAAP LTM 26,2%) + mejora − dilución de MaintainX |
| Margen objetivo | 29,0% | 33,5% | 36,5% | 41% non-GAAP FY2029 − SBC ~8,5% − amortización ~1,5% ≈ 31% GAAP + ~2,5pp por I+D; comparables Adobe ~36%, Cadence y PTC ~30% |
| Años de convergencia | 5 | 5 | 5 | Meta de la empresa a FY2029, más plazo por MaintainX e IA |
| Sales-to-capital | 1,5x | 1,5x | 1,5x | Bottom-up FY2022-FY2026 con adquisiciones (~1,3x) |
| ROIC en perpetuidad | 15% | 15% | 15% | Foso de estándar; ROIC actual ~36% (sin el override, DCF Base ≈ US$152) |
| WACC | 10,79% | 10,79% | 10,79% | UST 5,17% (25-sep-2026), beta 1,40 (Software global desapalancada 1,33), ERP 4,32%, Kd 6,17% (A3/BBB+) |

## Balance pro forma (MaintainX)

MaintainX se pagó el 3-ago-2026, después del cierre del Q2. El 10-Q todavía muestra la caja antes del pago:

- Caja y títulos de corto plazo al 31-jul-2026: US$4.155M. **Menos el pago de US$3.530M: caja pro forma de US$625M** (Input!B19)
- Deuda: notas US$2.484M + préstamo puente US$994M + arrendamientos US$227M = **US$3.705M**. Las notas de sep-2026 (US$500M al 5,05% a 2029 y US$500M al 5,65% a 2033) repagan el préstamo, así que no cambian la deuda.
- Activos no operativos: US$594M (títulos negociables de largo plazo por US$202M + inversiones estratégicas por US$392M)

## Log de correcciones (antes → después)

| # | Celda / componente | Antes | Después | Razón |
|---|---|---|---|---|
| 1 | Hoja del modelo | — | Copia nueva `Modelo_JMR_ADSK` en Análisis › ADSK | Pedido: hoja nueva y carpeta propia; la plantilla maestra no se tocó |
| 2 | Balance Sheet, columna L (LTM) | Cierre de ene-2026 (salvo la caja) | Balance real al 31-jul-2026 | El pipeline solo actualiza la caja LTM |
| 3 | Balance Sheet L20/L21/K21 | 0 / vacío | 1.493 (préstamo 994 + notas 2027 499) / 52 | Deuda y arrendamientos corrientes sin tag en el pipeline |
| 4 | Income Statement filas 15-16 (intereses) | Fila 16 = ingreso + gasto (FY2026: 163); FY2017-FY2022 en 0 | Gasto bruto: FY2026 80, LTM 86 (Q2 estimado); FY2017-FY2022 = intereses pagados | Input!B14 tomaba ingreso como gasto |
| 5 | Income Statement L8/L11 (SG&A LTM) | 3.066 (= FY2026) / 79 | 3.161 / −16 | SG&A LTM = FY2026 + H1 FY2027 − H1 FY2026 |
| 6 | Input!B19 (caja) | 4.155 | 625 | Pro forma de MaintainX |
| 7 | Input!B20 (activos no operativos) | 0 | 594 | Autodesk no usa el tag LongTermInvestments |
| 8 | Input!B4 / Resumen C25 | 14-sep-2026 / US$228,93 (fecha heredada) | 25-sep-2026 / US$209,40 | Fecha real del análisis |
| 9 | Input!B27-B33 | Fórmulas por defecto (8,1% LTM · B6−2pp · 8,1% · 33,0% · 5 · 1,54 · 1,54) | 13% · 29,5% · 10% · 33,5% · 5 · 1,5 · 1,5 | Anclados a la guía, la meta de margen y datos bottom-up |
| 10 | Input!B49/B50 (ROIC terminal) | No (ROIC = WACC) → DCF Base ~US$152 | Sí, 15% → DCF Base ~US$197 | Foso de estándar; ROIC actual ~36% |
| 11 | Cost of capital worksheet | Rating A1/A+ heredado · rf 4,99% · ERP 4,23% · vencimiento 3 | Direct Input rf+1,0% = 6,17% · 5,17% · 4,09% · 5 años | Rating partido A3/BBB+; datos de mercado de sep-2026 |
| 12 | Valuation output!C45 (margen Conservador) | =B6 | =MIN(B6; Input!B28) | Se estanca en el margen actual |
| 13 | Valuation output!C47 (margen Optimista) | =B30+5pp (38,5%) | =B30+3pp (36,5%) | Nivel de Adobe, el comparable maduro más rentable |
| 14 | Resumen G3 (tipo de empresa) | Genérico | Software | Utilidades GAAP deprimidas por SBC: más peso a DCF y flujo |
| 15 | Estadísticas E20/E21 | Caja de US$4.155M / deuda neta de −US$450M | US$625M / US$3.080M | Pro forma de MaintainX |
| 16 | Barrido de errores | 12 #DIV/0! en 'Industry Averages(US)' | Sin cambios | Preexistentes del dataset de Damodaran |

Los fixes genéricos de la plantilla (TICKER, tasa efectiva LTM, IFERROR de Option value, beta, NWC) ya venían en la plantilla maestra: no hubo que volver a aplicarlos.

## Múltiplos (paso 6)

Los cinco múltiplos fueron positivos los 4 años (ene-2023 a ene-2026), así que el MIN nativo no se rompe por cambios de signo y se dejó el mecanismo nativo. El problema es el régimen: el P/E GAAP de 2023-2026 fue de 48-60x y el EV/EBITDA de 30-44x, contra ~24x y ~20x hoy. Por eso dan precios muy superiores al DCF (P/E Base ~US$557, EV/EBITDA ~US$489). La categoría Software les da solo 40% del peso.

## Variable clave a monitorear

El crecimiento de billings y cRPO (10% y 12% en el Q2 FY2027):

- Si se sostienen en doble dígito mientras la IA se monetiza sin caída de usuarios, el caso se mueve hacia el Optimista.
- Si caen a un dígito medio, confirman el Conservador.

Próximo dato: resultados del Q3 FY2027, a fines de nov-2026 (guía de ingresos de US$2.125-2.140M).

## Fuentes

10-K FY2026 y 10-Q Q2 FY2027 (SEC EDGAR, XBRL); comunicado del Q2 FY2027 (27-ago-2026); 8-K de la emisión de notas (10-sep-2026); Bloomberg, Construction Dive y AEC Magazine (MaintainX); CG Channel (despidos de ene-2026); TIKR (caída del 4-sep-2026 y consenso de 36 analistas, precio objetivo medio de ~US$315-321); Investor Day 2025 de Autodesk (41% non-GAAP en FY2029); Damodaran Online (indname.xls ene-2026, ERP sep-2026); CNBC (UST 10 años al 25-sep-2026: 5,17%).
