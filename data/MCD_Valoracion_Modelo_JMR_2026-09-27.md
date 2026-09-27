# McDonald's Corporation (MCD) — Valoración Modelo JMR (Damodaran + 5 múltiplos)

- **Hoja del modelo:** [Modelo JMR — MCD (hoja provista por el usuario, carpeta de Drive «MCD»)](https://docs.google.com/spreadsheets/d/1USPRKTTdnXcWAEoAQoVq9CJXH1ENPLQkP1k_SW0Rnp8/edit). Era una copia recién hecha de la plantilla vigente. Se comparó celda por celda contra la plantilla maestra del repo: coincidía salvo mejoras más nuevas (precio del análisis tomado del cierre histórico de `Input sheet!B4` y columnas MOS en el Resumen). Por eso no se reinició con `reset_from_master.py`, que la habría dejado en la versión anterior.
- **Prompt usado:** «JMR - PROMPT Valoracion (VIGENTE v2).md» (carpeta Prompts de Drive).
- **Ticker:** NYSE:MCD. Franquiciador global: ~95% de los más de 46.000 locales los operan franquiciados.
- **Fecha y precio del análisis:** cierre del 25-sep-2026, **US$236,50**. Estados financieros al 30-jun-2026 (10-Q del 2T2026; LTM = FY2025 − 1S2025 + 1S2026).
- **WACC:** 7,93%. Ke 8,46% (UST 10 años 5,18% + beta 0,76 × ERP 4,32%). La beta es la desapalancada global de Restaurant/Dining de Damodaran (0,66), reapalancada con la D/E de mercado. Kd antes de impuestos 7,02% con el rating real Baa1/BBB+; después de impuestos, 5,26%. Pesos: 83% equity y 17% deuda (valor de mercado).
- **Tipo de empresa (ponderación):** Defensiva: DCF 30%, P/E 25%, EV/EBITDA 20%, EV/FCFF 10%, P/FCFE 10%, P/OCF 5%. MOS de 25% (hipótesis Estándar).
- **Script reproducible:** `scripts/run_mcd.py` + `scripts/mcd_content.py`. Cada celda que se pisó tiene su respaldo en `reference/backups/mcd_formula_backup.json`.

## Resultado

| Escenario | DCF hoy / acción | DCF vs. precio | Precio objetivo ponderado (3 años) | CAGR a 3 años |
|---|---|---|---|---|
| Conservador | US$178,87 | −24,4% | US$238,12 | +0,2% |
| **Base** | **US$225,92** | **−4,5%** | **US$298,69** | **+8,1%** |
| Optimista | US$257,66 | +8,9% | US$348,59 | +13,8% |

Valores por método a 3 años, en US$ por acción. El DCF se lleva a 3 años con × (1 + Ke)³; los múltiplos incluyen los dividendos. Orden: Conservador / Base / Optimista.

| Método | Peso | Conservador | Base | Optimista |
|---|---|---|---|---|
| DCF | 30% | 228,20 | 288,24 | 328,74 |
| EV/EBITDA | 20% | 228,17 | 288,74 | 342,82 |
| EV/FCFF | 10% | 247,80 | 318,34 | 380,59 |
| P/E | 25% | 250,28 | 304,89 | 353,29 |
| P/FCFE | 10% | 237,19 | 307,87 | 370,07 |
| P/OCF | 5% | 259,18 | 312,49 | 360,22 |
| **Ponderado** | 100% | **238,12** | **298,69** | **348,59** |

Zonas de compra (sobre el Base): Value US$194,15–209,08; Deep Value US$164,28–179,21; Valoración histórica US$134,41–149,34. Precio con MOS de 25%: US$224,02.

**Lectura.** El DCF Base, US$225,92, queda apenas por debajo del precio (−4,5%). El precio objetivo ponderado Base a 3 años da un retorno anual de ~8,1% con dividendos: ~3% viene del dividendo y el resto de un EBIT que crece ~4% anual. En el Base no se supone que la acción vuelva a los múltiplos de 2022-2025. El mercado ya castigó el tráfico débil en EE.UU. y el costo del plan NEXT: la acción cae ~23% en el año, cotiza a un P/E LTM de 19,2x y a un EV/EBITDA de 13,9x, contra medianas de 10 años de ~25,6x y ~18,2x. No es una ganga absoluta, pero sí la valoración más baja en años para un negocio de muy bajo riesgo. El precio actual está por encima de la zona Value, así que aún no hay margen de seguridad para una primera entrada.

## Supuestos por escenario

| Supuesto | Conservador | Base | Optimista | Ancla |
|---|---|---|---|---|
| Crecimiento de ingresos Año 1 | −3,5% | −2,0% | −1,0% | Las ventas del sistema crecen +4-5% (nuevas unidades ~2,5% + comparables), pero el refranquiciamiento de ~95% a ~98% a fines de 2028 (Investor Day, 23-sep-2026) resta: ~60% de los US$9.690M de ventas de locales propios pasan a cobrarse como renta + regalías |
| Crecimiento de ingresos años 2-5 | 0,5% | 2,0% | 3,0% | 2028 sigue refranquiciando (~−4%); 2029-30 vuelve a ~+4,5% |
| Margen operativo Año 1 | 47,5% | 47,5% | 47,5% | LTM 46,2%; guía 2026 «mid-to-high 40%»; el G&A empieza a bajar en 2027 |
| Margen objetivo (año 5) | 47,5% | 53,0% | 56,0% | Guía de «low-to-mid 50%» a 2030, menos la amortización (~10 años) del apoyo a franquiciados; el Optimista toma el tope del rango |
| Sales-to-capital | 1,0x / 1,2x | 1,0x / 1,2x | 1,0x / 1,2x | Capex base de ~US$3.000M/año + US$1.500-2.000M de apoyo NEXT 2027-30, contra D&A de ~US$2.300M |
| Tasa impositiva | 21,4% → 25% | ídem | ídem | Tasa efectiva LTM → marginal de EE.UU. (convención de Damodaran) |
| Perpetuidad | g 5,18% (rf), WACC 8,25%, ROIC 12% | ídem | ídem | Ver el log (corrección 6) |

Cifras de la guía (8-K del 23-sep-2026, Exhibit 99.1):

- Margen operativo «low-to-mid 50%» a 2030.
- G&A de ~1,9% de las ventas del sistema en 2030 (2,2% en 2026).
- Capex de ~US$3.000M/año más US$1.500-2.000M acumulados de apoyo entre 2027 y 2030.
- Conversión de FCF «mid-to-high 80%» a 2030.
- US$8.500M de apoyo a franquiciados hasta 2036, de los que ~US$5.000M llegan a 2030.
- +1,5 pp de cuota en pollo y en bebidas a 2030.

## Log de correcciones (antes → después)

1. **D&A (datos SEC).** El loader tomaba `DepreciationDepletionAndAmortization`, que en MCD es una partida parcial (US$301-466M desde 2020). Se reemplazó por `DepreciationAndAmortization` del flujo de caja (US$1.751M en 2020 → US$2.199M en 2025; LTM US$2.266M). El EBITDA LTM pasa de US$13.271M a US$15.071M y el EV/EBITDA de 2025, de 20,3x a 17,9x.
2. **Acciones y EPS (datos SEC).** Desde 2023 MCD reporta en XBRL las acciones promedio en millones (732,3). El loader las dejaba en 0, el EPS 2023-LTM salía en millones (11.564.659) y los múltiplos de 2023-2025 daban 0,0x. Se reescalaron: EPS diluido 2025 = US$11,95 (coincide con el 10-K) y P/E 2025 = 25,6x.
3. **Precio del análisis.** `refresh_native_model` pisa `Resumen!C25` con un valor fijo. Se restauró la fórmula `=$B$3` de la plantilla vigente, que toma el cierre histórico de `Input!B4` por GOOGLEFINANCE.
4. **Escenarios.**
   - `C55/D55`: `MIN(B27;B29) − 1,5pp` → `B27 − 1,5pp` y `B29 − 1,5pp`. La regla original aplicaba −3,5% a los 5 años.
   - `C106/D106`: `MAX(...) + 1pp` → +1pp por tramo.
   - `C45`: margen del Año 0 → margen del Año 1. El refranquiciamiento sube el margen solo por mezcla.
   - `C47`: Base + 5pp → Base + 3pp, el tope del rango guiado.
5. **Múltiplos objetivo.** `J19` (Base) pasa del mínimo positivo de 4 cierres (P/E 25,5x, EV/EBITDA 17,9x) a 0,78 × la mediana de 4 cierres, la regla de la Calculadora del Paso 5: P/E 20,0x, EV/EBITDA 14,2x, EV/FCFF 24,6x, P/FCFE 20,0x, P/OCF 16,7x. El mínimo de 4 años exigía volver a múltiplos que hoy el mercado no paga (P/E 19,2x) y que están por encima de la mediana de los peers (~18x). Con la regla nativa, el ponderado Base sería ~20% más alto.
6. **Perpetuidad.** WACC terminal: rf + ERP (9,27%) → 8,25%. ROIC terminal: igual al WACC → 12%. Con los valores por defecto el DCF Base daba US$147,38, porque trata a MCD como una empresa de riesgo promedio sin ventaja competitiva. Su beta desapalancada es 0,66 y su ROIC actual ~25%, gracias al modelo de renta + regalías.
7. **Otros ajustes.**
   - I+D (`Input!B17`): Yes → No, porque MCD no reporta I+D.
   - UST 10 años: 4,99% → 5,18% (25-sep-2026).
   - ERP maduro: 4,23% (ene-2026) → 4,09% (Damodaran, 1-sep-2026).
   - Rating: A1/A+ genérico → Baa1/BBB+ real.
   - Vencimiento de la deuda: 3 → 10 años (aproximado).
   - Tipo de empresa: Genérico → Defensiva.
   - MOS: 35% → 25%.
   - Se completó la hoja «Control de valoración», que queda LISTO PARA REVISIÓN.

**Nota sobre arrendamientos:** los ~US$14.700M de pasivos por arrendamientos operativos (ASC 842) no se suman a la deuda, porque su costo ya está restado en el EBIT (tratamiento consistente). Sí se incluyen los US$2.329M de arrendamientos financieros.

Barrido de errores: 0 celdas con #DIV/0!, #REF!, #VALUE! o #N/A en las hojas de cálculo. El orden Conservador < Base < Optimista se cumple en crecimiento, margen objetivo, DCF y precio ponderado (chequeo vivo en la Tesis).

## Conclusión

A US$236,50, MCD cotiza cerca de su valor intrínseco Base (US$225,92). Su precio objetivo ponderado a 3 años (US$298,69) implica un retorno de ~8% anual con dividendos. El riesgo a la baja parece acotado (Conservador a 3 años ≈ precio actual) porque el negocio de renta y regalías es muy estable. El potencial al alza depende de que el tráfico en EE.UU. vuelva a crecer.

**Variables a monitorear:**
- Comparables y tráfico de clientes en EE.UU. trimestre a trimestre (+0,8% en el 2T2026; ¿vuelven a +3%?).
- El margen operativo ajustado frente a la senda de «low-to-mid 50%» a 2030, neto de la amortización del apoyo a franquiciados.
