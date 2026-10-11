---
schema: "jmr-valoracion-v4"
ticker: "NU"
company: "Nu Holdings Ltd."
analysis_date: "2026-10-11"
information_cutoff: "2026-09-30"
currency: "USD"
---

# Nu Holdings Ltd. (NU) — Valoración Modelo JMR desde cero (prompt v4)

> Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación. Hoja: [Modelo JMR - NU (desde cero 2026-10-11)](https://docs.google.com/spreadsheets/d/1FIghcohETa7UiyRciIKiDCmFeEjN7XwlaN4TBCeWO6Q/edit), copia nueva de la plantilla maestra (19PRUFiYsNavUcN6WwHBVlp-VRMozp3rNSE2R1zt7N-g) en la carpeta «NU» de Análisis. Primera valoración de NU en el Modelo JMR: no hay hoja anterior ni nada heredado de otra empresa. Corte común de la cartera: 30-sep-2026.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$12,88 por acción** (historia «Base · Líder digital de Brasil que escala México»).

**Complemento · DCF esperado por probabilidades: US$10,41 por acción.**

| Historia activa | Probabilidad | ROE años 1-5 | ROE después del año 10 | DCF hoy por acción |
|---|---:|---:|---:|---:|
| Base · Líder digital de Brasil que escala México | 45% | 32% | 18,8% (industria) | US$12,88 |
| Conservadora · Crédito, impuestos y competencia comprimen el retorno | 25% | 24% | 10,93% (= Ke) | US$5,03 |
| Disrupción · Deterioro de los fundamentales: ciclo de crédito y regulación en Brasil | 10% | 15% | 10,93% (= Ke) | US$3,29 |
| Optimista · Banco digital de América Latina con opción global | 20% | 35% | 18,8% (industria) | US$15,14 |
| DCF esperado (complemento) | 100% | | | US$10,41 |
| Precio con margen de seguridad (35% sobre el esperado) | | | | US$6,77 |

NU es un banco (depósitos de US$45.300 millones, cartera de crédito de US$39.400 millones, licencias bancarias en México y en proceso en Brasil), así que se valora por la **rama financiera del prompt v4**: DCF de flujos al accionista (FCFE) con utilidad = ROE × patrimonio contable, reinversión = aumento del patrimonio que exige crecer, descuento al costo del patrimonio (Ke 10,93%) y sin restar depósitos ni sumar caja. La hoja calcula el FCFE en «DCF FCFE financiero» (Base B42 = US$12,88) y las cuatro historias en «Escenarios e historias» (H5:H8 y esperado H10); el motor del Modelo JMR las reproduce al centavo (diferencia 0,00). 'Valuation output' (FCFF industrial) queda como referencia técnica y no gobierna ningún resultado.

Precio relativo (secundario): solo el P/E aplica a un banco en la plantilla (EV/EBITDA, EV/FCFF, P/FCFE y P/OCF no aplican; ver sección 6). P/E al presente US$20,55 (Base) / US$11,35 (Conservador) / US$27,34 (Optimista) y a 3 años sin descontar US$31,08 / US$15,97 / US$42,48. Ponderado DCF + P/E (40%/60%, categoría «Financiera») al presente US$17,48 / US$8,82 / US$22,46 y a 3 años sin descontar US$25,68 / US$12,32 / US$33,76.

## 2. Historia y visión externa

**La historia.** Nu Holdings (Nubank) es el banco digital más grande de América Latina: 138,9 millones de clientes al 2T26 (casi 118 millones en Brasil, 15,8 en México y más de 5 en Colombia), con 83,5% activos cada mes, un ingreso medio de ~US$17 por cliente activo al mes y un costo de servir de ~US$1 ([Nu Holdings, comunicado del 2T26, 13-ago-2026](https://www.sec.gov/Archives/edgar/data/1691493/000129281426004222/nupr2q26_6k.htm)). En cinco a diez años, Brasil madura (crece por productos por cliente, clientes de mayor ingreso y pymes), México se convierte en un segundo Brasil más pequeño con licencia bancaria (opera como banco desde el 6-ago-2026) y Colombia, EE.UU. y Nu Global son opciones de bajo peso. El ROE sostenible baja del ~36% actual sobre el patrimonio de inicio a ~32% en los años 1-5 por la CSLL más alta en Brasil, la inversión internacional y la acumulación de capital, y converge al ROE de la industria (18,8%) en los años 6-10. Hay que retener patrimonio al ritmo del crecimiento (regulación de capital), y el riesgo central es el crédito no garantizado en Brasil (mora 90+ de 6,9%).

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~19% anual cinco años (en dólares) | Sí | Sí: +37% en 2025 y +52% interanual en 1S26 en dólares; el consenso espera +45% en 2026 y +24% en 2027 | Probable |
| El ROE promedia ~32% sobre el patrimonio inicial cinco años | Sí | Sí: 30,8% (2024) y 37,5% (2025) sobre el patrimonio de inicio; 33% anualizado en el 2T26 | Probable |
| México llega a 60-70% del tamaño de Brasil en el largo plazo | Sí | Plausible: caso base de la gerencia en la llamada del 2T26; hoy es 7% de los ingresos de clientes | Posible a 10+ años |
| Un ciclo de crédito en Brasil eleva la mora y baja el ROE a ~15% | Sí | Sí: la mora 90+ subió a 6,9% y la expansión a segmentos de más riesgo es deliberada | Baja-media |

**Tasas base.** Con US$19.340 millones de ingresos UDM (US$13.684 millones en dólares de 2015), NU está en el tramo de US$12.000-25.000 millones de *The Base Rate Book* (Mauboussin & Callahan, 2016, Exhibit 4): media de 3,3% real anual a cinco años, mediana 2,9%. Crecer 18,8% nominal (Base) lo logra ~6% de las empresas de ese tamaño; 22,1% (Optimista) ~4%; 11,5% (Conservadora) ~19%. La Base se aparta de la tasa base con evidencia específica: crecimiento orgánico (sin compras materiales desde 2022), México y Colombia en fase de adquisición de clientes, consenso de +24% en 2027 y ~4% de inflación brasileña dentro de la cifra en dólares.

**Descomposición del crecimiento.** Ingresos NIIF por país (ingresos de clientes del 1S26, nota 34 del 6-K del 2T26; el rendimiento de tesorería se reparte en la misma proporción, estimación propia): Brasil US$17.584 millones (90,9%), México US$1.401 millones (7,2%), Colombia y otros US$355 millones (1,8%). Base: Brasil 24% → 10% en el año 5; México 50% → 26%; Colombia y otros 60% → 30%. Todo orgánico. No se publica sell-through (no aplica a un banco); los motores observables son clientes (+13% interanual), ARPAC (+22% FXN) y cartera de crédito (+37% interanual).

**Márgenes y retorno.** En un banco el margen relevante es el ROE. NIIF: utilidad de la controladora UDM US$3.607 millones sobre un patrimonio de US$13.250 millones (30-jun-2026). No hay cargos de una vez materiales en el UDM; en 2022 la terminación del CSA (US$355,6 millones) explica parte de la pérdida. Comparable maduro del mismo negocio: Itaú Unibanco, con ROE de ~21% (yfinance, 30-sep-2026) tras décadas de liderazgo en Brasil, y el ROE de la industria de Damodaran (Financial Svcs., global, ene-2026) de 18,8%, que es el ROE terminal de la Base.

**Reinversión.** Orgánica: el patrimonio debe crecer con el negocio (CET1 del conglomerado de Brasil 11,9% al 30-jun-2026, frente a 13,0% en dic-25; mínimo total requerido US$3.749,6 millones y exceso de US$1.848 millones). Capex bajo (US$288 millones UDM, sobre todo software). Comprado: no material (Easynvest 2021 y Olivia 2022; Banco Porto Real en 2026 es una licencia, sin precio material divulgado).

## 3. Datos

- Hoja: [Modelo JMR - NU (desde cero 2026-10-11)](https://docs.google.com/spreadsheets/d/1FIghcohETa7UiyRciIKiDCmFeEjN7XwlaN4TBCeWO6Q/edit). Fecha de corte 30-sep-2026; precio de cierre US$12,66 (Yahoo Finance, `auto_adjust=False`); Treasury a 10 años 5,29% (FRED DGS10) y prima madura de Damodaran 3,70% (ERPOct26.xlsx, misma fecha).
- Estados: NIIF consolidados en dólares. 2023-2025 del [20-F 2025](https://www.sec.gov/Archives/edgar/data/1691493/000129281426002166/nuform20f_2025.htm) (8-abr-2026); 2021-2022 del [20-F 2023](https://www.sec.gov/Archives/edgar/data/1691493/000129281424001464/nuform20f_2023.htm); UDM y balance al 30-jun-2026 del [6-K de estados del 2T26](https://www.sec.gov/Archives/edgar/data/1691493/000129281426004225/nufs2q26_6k.htm) (13-ago-2026, no auditados, revisión de KPMG). UDM = 2025 + 1S26 − 1S25 (mismas normas y perímetro).
- El importador de la SEC lee us-gaap; NU presenta en ifrs-full y la SEC todavía no publica en companyfacts el XBRL del 20-F 2025. Por eso los estados se transcribieron a `reference/desde_cero/NU/estados_fuente_2026-10-11.json` (con fuente por bloque y cuadres aritméticos verificados) y se cargaron con el importador mediante `scripts/nu_datos_niif.py`.

| Concepto (US$ millones) | Hoja | Fuente | Estado |
|---|---:|---|---|
| Ingresos totales UDM | 19.339,8 | 15.774,7 + 10.481,2 − 6.916,2 | Conciliado |
| Utilidad antes de impuestos UDM | 4.384,6 | 3.868,4 + 2.190,6 − 1.674,4 | Conciliado |
| Utilidad de la controladora UDM | 3.607,1 | 2.868,9 + 1.932,3 − 1.194,0 | Conciliado |
| Patrimonio de la controladora 30-jun-2026 | 13.249,7 | Estado de situación del 6-K 2T26 | Conciliado |
| Minoritarios | 2,1 | 13.251,7 − 13.249,7 | Conciliado |
| Depósitos | 45.328,4 | 6-K 2T26 | Materia prima: no se resta |
| Préstamos y financiación (deuda de la hoja) | 4.682,3 | 6-K 2T26 | Solo en el FCFF técnico |
| Acciones en circulación (clase A + B) | 4.830,69 M | Nota 31 del 6-K 2T26 (netas de 40,66 M en tesorería) | Conciliado |
| Acciones diluidas del modelo | 4.882,87 M | + 52,18 M de RSU y opciones (diluido − básico del 1S26, nota 9) | Cálculo |
| Preferentes y convertibles | 0 | 6-K 2T26 | No hay |

## 4. Supuestos del DCF y costo de capital

| Supuesto | Valor | Celda | Procedencia | A favor | En contra |
|---|---|---|---|---|---|
| ROE años 1-5 (Base) | 32% | «Escenarios e historias»!D5 → «DCF FCFE financiero»!D5 | Juicio: ~36% hoy sobre el patrimonio de inicio menos CSLL, inversión internacional y patrimonio creciente | 33% anualizado en el 2T26; 37,5% en 2025 | Mora en alza; CSLL de 15% en 2028 |
| ROE Conservadora / Disrupción / Optimista | 24% / 15% / 35% | D6 / D7 / D8 | Juicio por historia | Rango 21-38% en 2023-2026 | — |
| Crecimiento años 1-5 (Base, grupo) | 26,5%, 22,0%, 18,1%, 15,2%, 13,0% | «Escenarios e historias» fila 29 | Suma de países | Consenso +45% (2026) y +24% (2027) | Tasa base: ~6% lo logra |
| Crecimiento años 6-10 | Converge linealmente a 5,29% | Fila 29 | Regla de la plantilla | — | — |
| ROE después del año 10 | 18,8% Base y Optimista; Ke en Conservadora y Disrupción | «DCF FCFE financiero»!B11; G5:G8 | Ventaja durable: ROE de la industria (Damodaran) | ROE > Ke tres años; costo y escala | Competencia y regulación |
| Crecimiento terminal | 5,29% | «DCF FCFE financiero»!B5 = 'Valuation output'!M4 | Tasa libre (tope de Damodaran) | — | Brasil en dólares podría crecer menos |
| Patrimonio inicial | US$13.249,7 M | «DCF FCFE financiero»!B12 | 6-K 2T26 | — | Incluye US$3.649 M de impuestos diferidos |
| Acciones | 4.882,87 M | 'Input sheet'!B22 | 6-K 2T26 + dilución | — | Recompras futuras no se suponen |

**Costo de capital.** Ke = Rf 5,29% + beta 0,82 × prima 6,88% = **10,93%**, constante hasta el año 10 y en perpetuidad (el riesgo soberano de Brasil es estructural). Beta bottom-up: la del patrimonio de Financial Svcs. (Non-bank & Insurance) en la tabla global de Damodaran (ene-2026), sin desapalancar ni reapalancar porque en un banco los depósitos no son deuda financiera; tabla global porque >98% de los ingresos de clientes está fuera de EE.UU. Beta de regresión de NU (Yahoo, 5 años mensual): 0,955; beta de Bank (Money Center) global: 0,70. Prima por países ponderada por los ingresos de clientes del 1S26: Brasil 6,94% × 90,9% + México 6,16% × 7,2% + Colombia 6,55% × 1,8% = 6,88%. Kd (solo FCFF técnico): 5,29% + diferencial de Brasil 2,13% = 7,42%; peso del patrimonio 94,2%; WACC técnico 10,62%. No hay primas por riesgos propios: van en las historias Conservadora y Disrupción.

## 5. Historias, probabilidades y valor esperado

| Historia | Probabilidad | Brasil | México | Colombia y otros | CAGR del grupo 1-5 | ROE 1-5 | ROE terminal | DCF/acción |
|---|---:|---|---|---|---:|---:|---:|---:|
| **Base** · Líder digital de Brasil que escala México | 45% | 24, 19, 15, 12, 10% | 50, 45, 38, 32, 26% | 60, 50, 40, 35, 30% | 18,8% | 32% | 18,8% | **US$12,88** |
| Conservadora · Crédito, impuestos y competencia comprimen el retorno | 25% | 15, 12, 10, 8, 7% | 30, 25, 20, 18, 15% | 30, 25, 20, 15, 12% | 11,5% | 24% | 10,93% | US$5,03 |
| Disrupción · Deterioro de los fundamentales | 10% | 3, 2, 4, 5, 5% | 12, 10, 10, 8, 8% | 10, 10, 8, 8, 8% | 4,4% | 15% | 10,93% | US$3,29 |
| Optimista · Banco digital de América Latina con opción global | 20% | 27, 22, 18, 14, 12% | 60, 50, 42, 35, 30% | 80, 65, 50, 40, 35% | 22,1% | 35% | 18,8% | US$15,14 |
| **DCF esperado** | 100% | | | | | | | **US$10,41** |

DCF esperado = 0,45 × 12,88 + 0,25 × 5,03 + 0,10 × 3,29 + 0,20 × 15,14 = US$10,41. Precio con MOS (35% sobre el esperado) = US$6,77. La Disrupción se estabiliza (crecimiento terminal = su crecimiento del año 5, 5,3%, sin superar el de la hoja) con ROE terminal = Ke: no hay recuperación forzada. Las probabilidades son juicio del analista: el 35% asignado a historias de erosión refleja que la mora 90+ está subiendo y que el crédito no garantizado en Brasil ya tuvo ciclos duros (2015-2016).

**Puente de la Base (US$ millones).** VP del FCFE de los años 1-10: 22.986; VP del valor terminal (patrimonio₁₀ de 46.892 × (18,8% − 5,29%)/(10,93% − 5,29%) = 112.564, descontado): 39.899; patrimonio: 62.885; ÷ 4.882,87 M de acciones = US$12,88. Año 1: utilidad 4.240 (32% × 13.250), reinversión 3.517 (13.250 × 26,5%), FCFE 723. Modelo de rendimientos en exceso: patrimonio de hoy 13.250 + VP de (ROE − Ke) × patrimonio 49.636 = 62.885 (igual que el FCFE). El valor terminal pesa 63% del valor de la Base.

**Sensibilidad del DCF Base** (DCF completos, un supuesto a la vez): ROE 1-5 ±2 pp → US$12,44 / US$13,32; crecimiento 1-5 ±2 pp → US$12,00 / US$13,84; Ke ±1 pp → US$15,85 / US$10,81; crecimiento terminal ±0,5 pp → US$13,42 / US$12,42; acciones +5% → US$12,27; ROE terminal = Ke (sin ventaja) → US$7,32; ROE terminal 15% → US$10,18; 22% → US$15,11; ROE 1-5 de 28% / 36% → US$12,00 / US$13,75.

| Crecimiento 1-5 \ ROE 1-5 | 28% | 30% | 32% | 34% | 36% |
|---|---:|---:|---:|---:|---:|
| 14,9% | 10,84 | 11,22 | 11,60 | 11,98 | 12,36 |
| 16,9% | 11,65 | 12,05 | 12,45 | 12,86 | 13,26 |
| 18,9% | 12,54 | 12,97 | 13,40 | 13,82 | 14,25 |
| 20,9% | 13,53 | 13,98 | 14,43 | 14,88 | 15,33 |
| 22,9% | 14,60 | 15,08 | 15,56 | 16,04 | 16,51 |

(Crecimiento constante en los años 1-5; por eso el centro, US$13,40, difiere de la Base con su trayectoria decreciente.)

**Pre-mortem** (si en tres años la Base falló): (1) un ciclo de crédito en Brasil lleva la mora 90+ por encima de 8%; (2) un tope a las tasas de la tarjeta o del crédito personal, o el crédito vía Pix, recorta el margen; (3) la CSLL y otros impuestos a las fintechs bajan la utilidad más de lo previsto; (4) México no llega a escala rentable; (5) una compra grande diluye (la especulación sobre Monzo de sep-2026 fue desmentida por la empresa); (6) el real y el peso se deprecian. Evidencia en contra hoy: la mora 90+ sube y el crecimiento depende de segmentos de más riesgo.

**Indicadores** (mover 5-10 pp de probabilidad por trimestre; los valores de cada historia solo cambian si cambia un supuesto): ROE anualizado 33% (≥ 30% / < 25%); mora 15-90 4,8% (≤ 5% / > 5,5%); mora 90+ 6,9% (≤ 7% / > 8%); NIM ajustado por riesgo 12,4% (≥ 11% / < 9%); clientes en México 16 M (≥ 20 M en 2027 / estancado); eficiencia 19,5% (≤ 22% / > 28%); CET1 de Brasil 11,9% (≥ 11% / < 10%); costo de los depósitos 88% de la interbancaria (≤ 90% / > 100%).

## 6. Múltiplos (precio relativo)

| Método | Aplicabilidad | Ancla A (historia) | Ancla B (peers) | Ancla C (justificado) | Conservador | Base | Optimista |
|---|---|---|---|---|---:|---:|---:|
| P/E | Aplicable | Mediana de dic-24, dic-25 y UDM = 25,9× (dic-24 25,3×; dic-25 28,3×; UDM 17,1×); se excluyen 2021-2022 (pérdidas) y dic-23 (39,7×, primer año con utilidad) | Mediana 12,4× (ITUB, BBD, BSBR, INTR, BAP, COF; sin SOFI) × 1,5 = 17,8× | 17,9× / 27,7× / 36,6× | 18,7× | **23,3×** | 27,5× |
| EV/EBITDA | No aplica | — | — | — | — | — | — |
| EV/FCFF | No aplica | — | — | — | — | — | — |
| P/FCFE | No aplica | — | — | — | — | — | — |
| P/OCF | No aplica | — | — | — | — | — | — |

Regla: Base = (1 − λ) × promedio(A, B) + λ × C con λ = 0,25 (la NU de FY+3 gana un ROE parecido al de hoy con menor crecimiento; el justificado usa el ROE de FY+3 sobre el patrimonio de hoy y lo sobrestima, así que pesa poco). Ajuste de peers +50%: ROE de ~30% frente a ~16% de mediana y crecimiento de ~15% en FY+3 frente a 5-10%; con Ke ~11% y g ~5% el P/E justificado ((1 − g/ROE)(1 + g)/(Ke − g)) es ~50% mayor con ese ROE. Conservador y Optimista por las dispersiones P25/P75 de cada ancla. **No aplican**: EV/EBITDA y EV/FCFF (en un banco los depósitos son materia prima y el valor empresa no tiene sentido); P/FCFE y P/OCF (el flujo de caja contable de NU y de los peers incluye la variación de cartera y depósitos: flujo operativo de −US$1.382 millones UDM en NU y P/FCF de 0,6× en Itaú y Santander Brasil). Damodaran usa P/BV y P/E en financieras; la plantilla no tiene P/BV y se informa como lectura: P/BV de hoy 4,6× (US$12,66 / US$2,74 de patrimonio por acción en circulación); el justificado de la Base, (ROE − g)/(Ke − g) con ROE 32% y g a largo plazo de 5,29%, sería ~4,7×, pero supone el ROE de 32% para siempre.

**Chequeo de independencia (6.4).** El P/E al presente (US$20,55) supera al DCF Base (US$12,88) en 60%, fuera de ±25%. Ningún múltiplo se derivó del DCF ni se movió para acercarlo. **Crecimiento implícito (6.5):** el P/E Base de 23,3× en FY+3 equivale a un crecimiento perpetuo de 7,0% con la misma fórmula; el múltiplo que implica el DCF en FY+3 es 13,2× (3,7%). Alerta: diferencia de 3,3 pp y 77% en valor. Decisión: no se sube el crecimiento del DCF porque la Base ya está cerca del consenso de ingresos y el ROE de 32% en los años 1-5 es generoso; la brecha está en el largo plazo (el DCF lleva el ROE a 18,8% en los años 6-10; el ancla histórica de 2024-2025 supone que el mercado pagará 26-28× por una utilidad que todavía crece 30%). Para un banco, el DCF (ROE frente al Ke con convergencia explícita) es más confiable; el P/E de mercado de hoy (17,1× UDM; 14,6× la utilidad Base del año 1) está más cerca del DCF que el ancla histórica.

**Múltiplos históricos normalizados (lectura independiente).** P/E: tres cierres válidos (dic-23 39,7×, dic-24 25,9×, dic-25 28,4×; mediana 28,4×, P25 27,1×); hoy 17,0×, 40% por debajo de la mediana y en el percentil 0 de su corta historia. Aplicada a la utilidad Base de FY+3 y traída a hoy, la mediana da US$27,70 (lectura de reversión a la media, no valor intrínseco). **Barato frente a su historia no equivale a infravalorado intrínsecamente.** afecta_dcf = false; afecta_ponderado = false.

## 7. Resultados

**Tabla 1 · Valor por acción descontado al presente (30-sep-2026).** Promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); NU no paga dividendos.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$12,88 | US$5,03 | US$15,14 |
| P/E | 23,3× / 18,7× / 27,5× | 60% | 100% | US$20,55 | US$11,35 | US$27,34 |
| EV/EBITDA, EV/FCFF, P/FCFE, P/OCF | No aplican | 0% | 0% | — | — | — |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$20,55 | US$11,35 | US$27,34 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$17,48 | US$8,82 | US$22,46 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Sin dividendos (NU no tiene política de dividendos; la recompra no se proyecta).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones (DCF × 1,1093³) | — | 40% | — | US$17,58 | US$6,86 | US$20,67 |
| P/E | 23,3× / 18,7× / 27,5× | 60% | 100% | US$31,08 | US$15,97 | US$42,48 |
| **Ponderado de múltiplos solos a 3 años sin descontar** | — | 60% | 100% | US$31,08 | US$15,97 | US$42,48 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$25,68 | US$12,32 | US$33,76 |

Pesos: categoría «Financiera» (DCF 40%, P/E 35%, P/FCFE 20%, P/OCF 5%); con P/FCFE y P/OCF sin aplicar, el peso de múltiplos (60%) queda todo en el P/E. Ponderado DCF + múltiplos = 0,40 × DCF + 0,60 × P/E.

| P/E | Escenario | Utilidad FY+1 / FY+2 / FY+3 (US$ M) | Precio FY+1 / FY+2 / FY+3 | VP 1 / 2 / 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---|---|---|---:|---|
| P/E | Base | 4.240 / 5.365 / 6.543 | US$20,14 / US$25,49 / US$31,08 | US$18,16 / US$20,71 / US$22,77 | US$20,55 | OK |
| P/E | Conservador | 3.180 / 3.700 / 4.193 | US$12,11 / US$14,09 / US$15,97 | US$10,92 / US$11,45 / US$11,70 | US$11,35 | OK |
| P/E | Optimista | 4.637 / 6.045 / 7.592 | US$25,95 / US$33,83 / US$42,48 | US$23,39 / US$27,49 / US$31,12 | US$27,34 | OK |

La utilidad de FY+1 a FY+3 de cada escenario es la de su historia FCFE (ROE × patrimonio; 'Financials Multiples' filas 15/54/94 enlazadas a «Escenarios e historias»), dividida por 4.908,8 M de acciones diluidas promedio (constantes, sin recompras). Ke de descuento 10,93%.

## 8. DCF frente a múltiplos

El DCF Base (US$12,88) y el P/E (US$20,55 hoy) cuentan historias distintas sobre la duración del retorno excedente. Ambos parten de la misma utilidad de los años 1-3 (la de la historia Base); la diferencia está en lo que se paga por ella en FY+3. El P/E de 23,3× supone que en 2029 el mercado seguirá pagando por NU como por una empresa de alto crecimiento con ROE de ~30%; el DCF, en cambio, explicita que el ROE baja de 32% a 18,8% en los años 6-10 y que el crecimiento converge a 5,29%, lo que implica un P/E de 13,2× en FY+3. Para un banco con crédito no garantizado, regulación cambiante y competencia que se adapta, la convergencia explícita del DCF es más defendible que extrapolar el múltiplo de 2024-2025. Por eso el DCF es el método más confiable aquí; el P/E se informa como lectura de cuánto paga el mercado por bancos con ROE alto y crecimiento.

## 9. Sensibilidad

| Variación | DCF Base | Cambio |
|---|---:|---:|
| Crecimiento años 1-5 −2 pp / +2 pp | US$12,00 / US$13,84 | −6,8% / +7,4% |
| ROE años 1-5 −2 pp / +2 pp | US$12,44 / US$13,32 | −3,4% / +3,4% |
| ROE años 1-5 −4 pp / +4 pp (28% / 36%) | US$12,00 / US$13,75 | −6,8% / +6,8% |
| Ke −1 pp / +1 pp | US$15,85 / US$10,81 | +23,0% / −16,1% |
| Beta de regresión 0,955 (Ke 11,86%) | US$10,93 | −15,1% |
| Beta de Bank (Money Center) global 0,70 (Ke 10,10%) | US$15,24 | +18,3% |
| Crecimiento terminal −0,5 pp / +0,5 pp | US$12,42 / US$13,42 | −3,5% / +4,2% |
| Crecimiento terminal 3,0% | US$11,26 | −12,6% |
| ROE terminal = Ke (sin ventaja) | US$7,32 | −43,2% |
| ROE terminal 15% / 22% | US$10,18 / US$15,11 | −21,0% / +17,3% |
| Acciones +5% | US$12,27 | −4,8% |
| Múltiplos ±20% (P/E Base hoy) | US$16,44 / US$24,66 | ±20% |

La variable que más mueve el valor es el ROE de largo plazo (años 6-10 y perpetuidad), seguida del costo del patrimonio; el ROE de los años 1-5 pesa menos porque el patrimonio todavía es pequeño frente al de los años 6-10.

## 10. Log de cambios en la hoja

Respaldo de cada celda en `reference/backups/nu_desde_cero_2026-10-11.json`; notas en las celdas.

| Cambio | Antes | Después | Motivo |
|---|---|---|---|
| Copia nueva de la plantilla maestra | — | Hoja 1FIghcohETa7… en Análisis › NU | Empresa nueva (aislamiento) |
| Estados (Income, Balance, Cash Flow) | Vacíos | NIIF 2021-2025 + UDM jun-26 | `scripts/nu_datos_niif.py` (20-F y 6-K) |
| Balance columna L | Repetía dic-25 | Saldos al 30-jun-2026 | Balance UDM = último informe |
| 'Income Statement'!G22:L22 | Utilidad consolidada | Utilidad de la controladora | Clean surplus con el patrimonio de la controladora |
| 'Cash Flow Statement'!B40:H40 | Serie de relleno de la plantilla | Vacío (sin dato) | Error de la plantilla |
| 'Input sheet'!B4, D1, B23 | 14-sep-2026 / GOOGLEFINANCE | 30-sep-2026 / US$12,66 / =D1 | Corte común (`aplicar_corte.py`) |
| 'Input sheet'!B17, B18, B38 | Yes / No / No | No / No / No | Sin I+D; NIIF 16; RSU en las acciones diluidas |
| 'Input sheet'!B21, B22 | 0 / L27 | Minoritarios / L27 + 52,178 | Puente patrimonial |
| 'Cost of capital worksheet'!B22:B23, B26:B27, B34:B35 | Single Business(Global) / Country of Incorporation / Actual rating | Direct Input 0,82 / prima por países / Direct Input | Banco: beta del patrimonio; exposición por ingresos |
| Pestaña «DCF FCFE financiero» | No existía | FCFE con ROE terminal (B11) | Rama financiera del prompt v4 |
| 'Valuation output'!C45:C48 | ROE de las historias | 'Input sheet'!B30 (margen técnico) | El FCFF técnico no debe usar el ROE como margen EBIT |
| 'Financials Multiples' filas 15/29, 54/68, 94/108 (E:H) | EBIT × (1 − t) y FCFE industrial | Utilidad y FCFE de las historias FCFE | Excepción financiera (`scripts/financieras.py`) |
| 'Descuento de múltiplos'!C38:E38 | 'Valuation output' B86/B35/B137 | «Escenarios e historias» H6/H5/H8 | DCF de hoy = FCFE de las historias |
| 'Resumen de Valoración'!G3, F7:F11 | Genérico / vacío | Financiera / «No» en EV/EBITDA, EV/FCFF, P/FCFE, P/OCF | Ciclo de vida y aplicabilidad |
| PE!J8/J19/J30 | Plantilla | 18,7× / 23,3× / 27,5× | Tres anclas (paso 6) |

Cambios de código (aplican a la cartera, sin cambiar resultados de otras empresas): el motor del Modelo JMR (`docs/jmr_engine.js`) acepta un ROE terminal propio en las financieras ('DCF FCFE financiero'!B11; sin él, el ROE converge al Ke como antes: PAGS da exactamente los mismos valores, verificado con el motor); `build_story_sheet.py` y `damodaran_stories.py` llevan ese ROE terminal por historia y corrigen el modelo de rendimientos en exceso; la lista de financieras vive en `scripts/financieras.py` (PAGS y NU).

## 11. El precio al final

Precio de referencia: **US$12,66** (cierre del 30-sep-2026). Frente al DCF Base (US$12,88) el precio está 2% por debajo; frente al DCF esperado (US$10,41), 22% por encima; frente al precio con MOS (US$6,77), 87% por encima.

**DCF inverso** (crecimiento anual de los años 1-5 que justifica US$12,66, con la trayectoria de convergencia de la hoja):

| | ROE 24% | ROE 32% | ROE 35% |
|---|---:|---:|---:|
| Beta 0,82 (Ke 10,93%) | 21,0% | 17,4% | 16,1% |
| Beta 0,955 (Ke 11,86%) | 26,6% | 22,4% | 20,8% |
| Beta 0,70 (Ke 10,10%) | 16,1% | 12,9% | 11,8% |

Con la beta del modelo y el ROE de la Base, el precio pide ~17,4% de crecimiento anual en cinco años (lo logra ~7% de las empresas de ese tamaño), algo menos que el 18,8% de la Base. El precio necesita, en esencia, la historia Base completa, incluida la ventaja durable: sin rendimiento excedente después del año 10, el DCF Base sería US$7,32. ¿Qué sabe el mercado que yo no? Probablemente valora más la opcionalidad de México, EE.UU. y Nu Global y un ROE de largo plazo más alto (como Itaú) que el 18,8% de la industria; o usa un costo del patrimonio más bajo. **Hechos posteriores al corte** (no entran en la valoración): el precio subió a US$16,12 al 9-oct-2026, tras el desmentido sobre Monzo (6-K del 30-sep) y la primera vuelta electoral en Brasil del 4-oct.

Crecimiento implícito de los múltiplos: P/E Base 23,3× → 7,0% perpetuo con el ROE de FY+3 (el DCF implica 3,7%).

## 12. Registro de decisión

| Campo | Propuesta | Tu estimación |
|---|---|---|
| Fecha | 30-sep-2026 (corte); informe del 11-oct-2026 | |
| Historia en una frase | El banco digital dominante de Brasil que replica su modelo en México: el valor depende de cuánto tiempo sostenga un ROE muy superior al costo del patrimonio | |
| Probabilidades | Base 45% / Conservadora 25% / Disrupción 10% / Optimista 20% | |
| DCF Base hoy (valor intrínseco principal) | US$12,88 | |
| DCF esperado (complemento) | US$10,41 | |
| Rango | US$3,29 a US$15,14 | |
| Precio con MOS (35% sobre el esperado) | US$6,77 | |
| Confianza | Media: el ROE es alto y verificable, pero crédito, país y regulación dominan el resultado | |
| Qué cambiaría la opinión | ROE, mora 90+, NIM ajustado por riesgo, CSLL y escala de México | |
| Revisión | Resultados del 3T26 (nov-2026) e Investor Day del 8-dic-2026 | |

La decisión (comprar, mantener o vender) la registras tú en la app; este análisis no la toma por ti.

## 13. Fuentes

Primarias:
- Nu Holdings, [Form 20-F 2025](https://www.sec.gov/Archives/edgar/data/1691493/000129281426002166/nuform20f_2025.htm), 8-abr-2026.
- Nu Holdings, [Form 20-F 2023](https://www.sec.gov/Archives/edgar/data/1691493/000129281424001464/nuform20f_2023.htm), 19-abr-2024.
- Nu Holdings, [6-K estados financieros del 2T26](https://www.sec.gov/Archives/edgar/data/1691493/000129281426004225/nufs2q26_6k.htm), 13-ago-2026.
- Nu Holdings, [6-K comunicado de resultados del 2T26](https://www.sec.gov/Archives/edgar/data/1691493/000129281426004222/nupr2q26_6k.htm), 13-ago-2026.
- Nu Holdings, 6-K del [1-jun-2026 (nuevo CFO)](https://www.sec.gov/Archives/edgar/data/1691493/000129281426003267/nu20260601_6k.htm), [4-jun-2026 (recompra de US$1.000 M)](https://www.sec.gov/Archives/edgar/data/1691493/000129281426003326/nu20260604_6k.htm), [10-jul-2026 (banco en México)](https://www.sec.gov/Archives/edgar/data/1691493/000129281426003723/nu20260710_6k.htm), [20-jul-2026 (Banco Porto Real)](https://www.sec.gov/Archives/edgar/data/1691493/000129281426003814/nu20260720_6k.htm), [2-sep-2026 (Investor Day)](https://www.sec.gov/Archives/edgar/data/1691493/000129281426004456/nu20260831_6k.htm), [10-sep-2026 (EE.UU. y Nu Global)](https://www.sec.gov/Archives/edgar/data/1691493/000129281426004518/nu20260909_6k.htm) y [30-sep-2026 (Monzo)](https://www.sec.gov/Archives/edgar/data/1691493/000129281426004752/nu20260930_6k.htm).
- FRED, DGS10 al 30-sep-2026; Damodaran, [ERPOct26.xlsx](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx) y [datos por industria, ene-2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html).

Secundarias:
- Yahoo Finance / yfinance: precios al 30-sep-2026, beta de regresión, consenso de utilidades e ingresos (consultado el 11-oct-2026) y múltiplos de los peers.
- [Zacks / Yahoo Finance, resumen de la llamada del 2T26](https://finance.yahoo.com/markets/stocks/articles/nu-q2-earnings-call-focuses-140000993.html), ago-2026 (guía de eficiencia ~20% y NIM ajustado ~12,4%; no hay transcripción primaria en la SEC).
- Mauboussin & Callahan, [The Base Rate Book](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf), 2016.
- Benzinga / FX Leaders (28-29-sep-2026) sobre la caída por los reportes de Monzo; StocksToTrade (5-oct-2026) sobre el alza posterior. Solo contexto de precio.

## 14. Control de calidad

| Control | Sí/No |
|---|---|
| Hoja nueva desde la plantilla maestra; nada heredado de otra empresa (AISLAMIENTO = OK) | Sí |
| Historia escrita antes de los números; filtro posible/plausible/probable | Sí |
| Tasas base del tamaño reportadas | Sí |
| Orgánico frente a comprado separado | Sí |
| ROE (margen de un banco) anclado en un maduro (Itaú) y en la industria (Damodaran) | Sí |
| Beta bottom-up documentada (patrimonio del sector, tabla global) con regresión y alternativa | Sí |
| Cuatro historias activas con probabilidades que suman 100% y valor esperado | Sí |
| Hoja = motor en las cuatro historias y el esperado (diferencia 0,00) | Sí |
| Pre-mortem e indicadores | Sí |
| Múltiplos con tres anclas, no derivados del DCF; métodos no aplicables documentados | Sí |
| Crecimiento implícito (6.5) corrido; alerta del P/E explicada | Sí |
| Ambos horizontes con múltiplos solos y DCF + múltiplos | Sí |
| El precio aparece recién en la sección 11 (salvo la nota de hechos posteriores) | Sí |
| Estados conciliados con el 20-F 2025 y el 6-K 2T26 (UDM y balance) | Sí |
| Capital regulatorio conciliado con el patrimonio contable | Cobertura parcial: se informan CET1 por entidad y las diferencias principales; no hay estados de la matriz por separado |
| DCF inverso de `implied_growth.py` | No disponible para financieras (limitación conocida del script); se informa el de `damodaran_stories.py` |
