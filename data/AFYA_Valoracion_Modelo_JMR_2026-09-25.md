# AFYA (Afya Limited) — Valoración Modelo JMR (Damodaran + 5 múltiplos)

- **Hoja del modelo:** [Modelo JMR - AFYA](https://docs.google.com/spreadsheets/d/1_CXhy_5n-V4rwfOSl8xI8455hywS5W92VBed_FCylvQ/edit) (AAA Finanzas › Análisis › AFYA). La hoja era una copia de LULU con el nombre AFYA: se reemplazó por la plantilla maestra auditada (respaldo en `reference/backups/afya_pre_reset.json.gz`).
- **Fecha de corte de los datos:** 6-K del 2T26 (30-jun-2026, publicado el 13-ago-2026). LTM = jul-2025 a jun-2026.
- **Fecha y precio del análisis:** 25-sep-2026, **US$13,00** (cierre en Nasdaq).
- **WACC:** 11,22%: Ke 13,99% (rf 5,18% + beta 1,20 × ERP 7,33% de Brasil), Kd después de impuestos 7,39%, D/(D+E) 42%. El WACC terminal es 11% y conserva el riesgo país.
- **Tipo de empresa (ponderación):** Madura: DCF 40%, EV/EBITDA 20%, P/E 20%, EV/FCFF 10%, P/FCFE 5% y P/OCF 5%.
- **Research cualitativo (prompt v1, 21 secciones):** `data/AFYA_Research_Fundamental_Modelo_JMR_2026-09-26.md`. También está publicado en Modelo-JMR-datos (`analisis/`), vinculado a la valoración del visor (`valoraciones/AFYA-1790444060961.json`).
- **Script reproducible:** `scripts/run_afya.py` + `scripts/afya_steps.py` + `scripts/afya_content.py`. Cada celda pisada tiene respaldo en `reference/backups/afya_formula_backup.json`.

## Resultado

| Escenario | DCF hoy / acción | DCF vs. precio | Precio objetivo ponderado (3 años) | CAGR a 3 años |
|---|---|---|---|---|
| Conservador | US$17,65 | +35,8% | US$20,04 | 15,5% |
| **Base** | **US$22,43** | **+72,5%** | **US$25,27** | **24,8%** |
| Optimista | US$27,23 | +109,5% | US$30,60 | 33,0% |
| **Valor de la relación de canje con Yduqs** (6,408347 × YDUQ3 ÷ R$ por US$, 25-sep-2026) | **US$13,71** | +5,5% | — | — |

Valores por método en US$ por acción (Conservador / Base / Optimista), todos a 3 años:

| Método | Conservador | Base | Optimista |
|---|---|---|---|
| DCF | 26,14 | 33,21 | 40,33 |
| EV/EBITDA | 16,51 | 21,11 | 25,88 |
| EV/FCFF | 16,65 | 21,69 | 26,88 |
| P/E | 15,61 | 19,01 | 22,54 |
| P/FCFE | 13,05 | 15,68 | 18,39 |
| P/OCF | 16,91 | 20,14 | 23,48 |

Zonas de compra (sobre el Base): Value US$16,42–17,69; Deep Value US$13,90–15,16; Valoración histórica US$11,37–12,63.

**Lectura.** El negocio standalone vale bastante más que el precio: el DCF Base da US$22,43 y hasta el Conservador supera el precio en 36%. El mercado paga ~5x EBITDA LTM por un negocio con margen EBIT de 33% que crece con la inflación. Pero desde el 23-sep-2026 la acción ya no sigue al valor standalone sino a la relación de canje con Yduqs (hoy US$13,71): la diferencia entre ambos valores es lo que el accionista de Afya cede en la fusión. La cede salvo que las sinergias (R$2.000-2.200M de valor presente, según las empresas) y la revalorización de la empresa combinada la compensen. Si la fusión fracasa (CADE o asambleas), vuelve a mandar el valor standalone.

## Supuestos por escenario (US$)

| Supuesto | Conservador | Base | Optimista | Ancla |
|---|---|---|---|---|
| Crecimiento Año 1 | 3,5% | 6,0% | 7,0% | Guía 2026 R$3.950-4.100M (+7% a +11%); H1 +7% → ~7,5% en R$, menos ~1,5pp de diferencial de inflación |
| Crecimiento años 2-5 | 3,5% | 5,0% | 7,0% | Cuota neta ~inflación + maduración de plazas, sin compras (~6,5% en R$) |
| Margen EBIT Año 1 | 31,5% | 31,5% | 31,5% | LTM 32,6% menos el ciclo de inversión (EBITDA ajustado −190pb en el H1) |
| Margen objetivo | 29,0% | 33,0% | 36,0% | FY2025 32,8%; pares de B3 17-26%, Laureate 36% |
| Años de convergencia | 5 | 5 | 5 | |
| Sales-to-capital | 1,5x / 1,2x | 1,5x / 1,2x | 1,5x / 1,2x | FCFF del Año 1 (~US$190M) ≈ FCFF real LTM |
| Tasa de impuestos | 10,6% → 15% | | | PROUNI hoy; mínimo del Pilar Dos a largo plazo (grupo Bertelsmann) |

## Particularidades del armado

- **Datos:** 20-F (IFRS, R$) desde el XBRL `ifrs-full` de SEC EDGAR (FY2019-FY2025), más el 2T26 para el LTM y el balance al 30-jun-2026.
- **Moneda:** cada año se convierte a su propio tipo de cambio (flujos al promedio del año, saldos al cierre), porque el real se movió de 3,94 a 6,18 por dólar.
- **Flujo operativo:** Afya reporta el OCF antes de intereses; el del libro resta los intereses pagados (R$445M en 2025).
- **Deuda:** incluye préstamos, cuentas por pagar a vendedores de empresas compradas y arrendamientos IFRS 16. Acciones: 88,92M (en circulación al 30-jun-2026 más dilución).
- **Múltiplo Base:** el mínimo positivo de los últimos 4 cierres cae en dic-2025 (P/E 10,4x, EV/EBITDA 6,5x). Son los múltiplos post-derrumbe del sector.
