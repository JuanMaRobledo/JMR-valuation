---
schema: "jmr-analisis-damodaran-v1"
ticker: "MSFT"
analysis_date: "2026-09-30"
---

# Microsoft Corporation (MSFT) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Escenarios e historias unificados:** A, B, C y D son los cuatro escenarios DCF activos. La cifra principal es el valor intrínseco esperado US$395,33; la historia central A vale US$446,95 y el rango es US$192,69–585,53. El MOS 35% se aplica al esperado: US$256,96. El antiguo caso Base de la hoja (US$455,44) se conserva solo como calibración técnica; no es el DCF de la historia central A. Los múltiplos y su mezcla son lecturas auxiliares con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: balance del último 10-q, capital invertido operativo, conversor de i+d alineado al ltm, roic terminal (criterio damodaran) (7 celdas, con respaldo). Valor esperado US$406,69 → US$395,33. Salvedades abiertas: Arrendamientos operativos: la deuda del DCF incluye 16.532,0 millones de arrendamientos operativos mientras el EBIT ya descuenta el alquiler (conversor de arrendamientos desactivado). Con el criterio de Damodaran o se convierten (deuda y EBIT ajustado) o se excluyen; excluirlos subiría el DCF en ~US$2,23 por acción. Es una decisión de método pendiente; no se cambió en esta auditoría. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de US$455,44 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

Microsoft vende el software y la infraestructura sobre los que operan casi todas las empresas: Microsoft 365, Dynamics y LinkedIn (Productivity and Business Processes, margen ~58%), Azure y servidores (Intelligent Cloud, ~42%) y Windows, Xbox y dispositivos (More Personal Computing). En FY2026 (cerrado en junio) facturó US$331.839 millones (+17,8%) con margen operativo de 46,8%, impulsada por Azure (~+30%) y la adopción de Copilot. El cambio de régimen está en el capital: el capex pasó de US$44.477 millones (FY24) a US$115.948 millones (FY26) y el flujo libre de la hoja cayó de US$73.144 millones a US$30.557 millones. La historia de cinco años es si esa inversión en IA rinde como rindió la nube en 2015-2022 o si Microsoft está sobreinvirtiendo en capacidad con demanda concentrada en pocos clientes (OpenAI).

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~13% anual cinco años | Sí | Sí: +15-18% anual en FY24-FY26 | Probable, desacelerando |
| Azure sigue creciendo más de 20% anual | Sí | Sí: ~30% en FY26 con capacidad limitada por oferta | Probable 2-3 años |
| El capex de IA rinde por encima del costo de capital | Sí | Sí si la demanda de inferencia sigue; hoy depende en parte de OpenAI | Incierto |
| El margen operativo se mantiene en ~45% | Sí | Sí: 44,6% → 46,8%, pero la depreciación del capex crece rápido | Probable |


### Visión externa: tasas base

Con ventas LTM de US$331.839 millones (US$234.795 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **>$50,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 1,0% y una mediana de 1,5% (desviación estándar 8,3%); sumando una inflación de 2,5%, la mediana nominal ronda 4,0%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| A · Azure y Copilot sostienen el doble dígito | 13,0% | 10% |
| B · El capex de IA rinde menos de lo esperado | 8,0% | 25% |
| C · Tesis de disrupción · Deterioro de los fundamentales | 5,0% | 44% |
| D · Microsoft gana la plataforma empresarial de IA | 17,5% | 3% |

En dólares de 2015 la empresa está en el tramo de más de US$50.000 millones: crecer 13,0% anual cinco años (historia A) lo logró ~10% de las empresas de ese tamaño; 17,5% (historia D), ~3%. Microsoft es la excepción que confirma la regla: hace cinco años que crece a doble dígito con más de US$150.000 millones de ventas. Aun así, la visión externa pide no extrapolar el 17,8% de FY26.


### Piezas del valor

**Crecimiento.** Ingresos de US$245.122 millones (FY24, +15,7%), US$281.724 millones (FY25, +14,9%) y US$331.839 millones (FY26, +17,8%). En FY25: Productivity US$120.810 millones (+12%), Intelligent Cloud US$106.265 millones (+20%) y More Personal Computing US$54.649 millones (+5%). En FY26, según los trimestres publicados, ~+16%, ~+30% y ~−1%. La división FY26 de las historias aplica esos crecimientos a FY25 (estimación propia).

| US$ millones | FY24 | FY25 | FY26 |
|---|---:|---:|---:|
| Ingresos | 245.122 | 281.724 | 331.839 |
| Crecimiento | +15,7% | +14,9% | +17,8% |
| Margen operativo | 44,6% | 45,6% | 46,8% |
| Capex | 44.477 | 64.551 | 115.948 |
| FCFF (hoja) | 73.144 | 66.125 | 30.557 |

**Márgenes.** El margen operativo subió a 46,8% pese al capex porque la depreciación todavía no refleja toda la inversión. La hoja supone 46,3% el próximo año y 45% de objetivo. La depreciación de los centros de datos de IA (vidas útiles de 5-6 años) y los márgenes menores de la infraestructura de IA frente al software empujan hacia abajo; Copilot y el precio de Microsoft 365 empujan hacia arriba. Las historias van de 37% a 48%.

**Reinversión y retorno.** La hoja usa un sales-to-capital de 0,65 en los años 1-5 (cada dólar de ingreso nuevo exige ~US$1,5 de capital) y 1 después: refleja el ciclo de capex de IA, muy distinto del Microsoft de software puro. En la historia D se baja a 0,6. El valor depende de que el retorno de ese capital (ROIC incremental) supere el costo de capital de ~10%. Ventaja durable: costos de cambio y efectos de red (Office, Azure, Windows, LinkedIn), con ROIC de 30-72% en 2021-2026. El ROIC después del año 10 es 25,0%, el promedio de su industria según Damodaran (29,3%), limitado a su ROIC actual. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Riesgo.** La hoja usa una beta de 1,34. La bottom-up de Software (System & Application) reapalancada da 1,26; el DCF técnico anterior sube de US$455,44 a US$465,33 La diferencia es pequeña frente a la que producen las historias; el riesgo real está en el retorno del capex, no en la tasa.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF técnico anterior por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,35 | 10,3% | 10,2% | US$455,44 |
| Bottom-up del sector (Software (System & Application), reapalancada) | 1,27 | 9,9% | 9,8% | US$465,33 |


### Calibración técnica anterior C/B/O (referencia auxiliar)

| Supuesto | Conservador | Base | Optimista |
|---|---:|---:|---:|
| Crecimiento año 1 | 14,0% | 16,5% | 19,0% |
| Crecimiento años 2–5 | 8,0% | 12,0% | 14,0% |
| Margen año 1 (base ajustada del modelo) | 45,0% | 46,3% | 47,5% |
| Margen objetivo | 42,0% | 45,0% | 48,0% |

Ventas/capital: 0,7x en años 1–5 y 1,0x en 6–10. WACC: 10,2%. Ke: 10,3%. Impuesto efectivo: 19,4%. Convergencia: 7 años. Estos parámetros son escenarios del analista, no cifras reportadas. Los casos Conservador, Base y Optimista de la hoja ya no son escenarios activos: sirven de calibración y de supuestos auxiliares de múltiplos. No confundir el antiguo Base con la historia A.


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF técnico anterior | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 25,0% | 29,3% | 8,5% | 25,0% | US$455,44 | US$320,75 |

Fuentes de ventaja: Costos de cambio y efectos de red (Office, Azure, Windows, LinkedIn). Evidencia: ROIC 30-72% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor principal de US$395,33 se obtiene ejecutando cuatro DCF completos de diez años más valor terminal y ponderándolos por sus probabilidades. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. No se obtiene aplicando descuentos al antiguo Base de US$455,44 ni mezclando el DCF con múltiplos. La historia central A vale US$446,95; «central» y «esperado» son conceptos distintos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$331.839 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 140.116 + 138.116 + 53.606 = 331.839. |
| Margen inicial del DCF | 46,3% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 7 (Input sheet B31). |
| Impuesto | 19,40% en años 1–5; 21,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 10,16% → 8,48% | Tasa libre de riesgo 4,25%, beta 1,35, ERP 4,46%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 0,65x en años 1–5; 1,00x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. D usa 0,60x en años 1–5. |
| Crecimiento perpetuo | A/B/C/D: 4,25% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. |
| ROIC terminal | A/D: 25,00%; B/C: 8,48% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 76.843; deuda 123.420; activos no operativos 36.348; acciones 7.427,0 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo A, año 1: 140.116 × 1,14 + 138.116 × 1,25 + 53.606 × 1,00 = US$385.984,36 millones. Frente a 331.839, el crecimiento consolidado es 16,32%. En los años 2–5 es 14,05%, 12,72%, 11,55%, 10,30%; las ventas del año 5 son US$610.544,46 millones. El 13,0% de la tabla es el crecimiento anual compuesto de los cinco años: (610.544,46 / 331.839)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En A, año 1: NOPAT = 385.984,36 × 46,30% × (1 − 19,40%) = US$144.047,55 millones. La reinversión es US$83.435,47 millones y el FCFF es US$60.612,08 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 8,48%. Reinversión terminal sobre el NOPAT: A, 17,0% (4,25% / 25,00%); B, 50,1% (4,25% / 8,48%); C, 50,1% (4,25% / 8,48%); D, 17,0% (4,25% / 25,00%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en «Escenarios e historias»: ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**A · Azure y Copilot sostienen el doble dígito** — probabilidad 45%; valor terminal 6.128.005 (VP 2.438.724); DCF US$446,95 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 385.984 | 16,3% | 46,3% | 144.048 | 83.435 | 60.612 | 10,2% | 55.024 |
| 2 | 440.217 | 14,1% | 45,9% | 162.969 | 86.125 | 76.844 | 10,2% | 63.327 |
| 3 | 496.199 | 12,7% | 45,7% | 182.951 | 88.187 | 94.764 | 10,2% | 70.895 |
| 4 | 553.521 | 11,6% | 45,6% | 203.257 | 87.729 | 115.528 | 10,2% | 78.460 |
| 5 | 610.544 | 10,3% | 45,4% | 223.283 | 85.398 | 137.885 | 10,2% | 85.010 |
| 6 | 666.053 | 9,1% | 45,2% | 241.620 | 52.493 | 189.127 | 9,8% | 106.175 |
| 7 | 718.546 | 7,9% | 45,0% | 258.554 | 47.933 | 210.622 | 9,5% | 107.997 |
| 8 | 766.479 | 6,7% | 45,0% | 274.696 | 41.853 | 232.843 | 9,2% | 109.382 |
| 9 | 808.332 | 5,5% | 45,0% | 288.529 | 34.354 | 254.175 | 8,8% | 109.730 |
| 10 | 842.686 | 4,3% | 45,0% | 299.575 | 35.814 | 263.761 | 8,5% | 104.967 |
| Terminal | 878.500 | 4,2% | 45,0% | 312.307 | 53.092 | 259.215 | 8,5% | — |

**B · El capex de IA rinde menos de lo esperado** — probabilidad 25%; valor terminal 2.430.098 (VP 967.091); DCF US$231,30 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 369.639 | 11,4% | 46,3% | 137.948 | 49.058 | 88.890 | 10,2% | 80.694 |
| 2 | 401.527 | 8,6% | 44,5% | 144.022 | 46.009 | 98.014 | 10,2% | 80.773 |
| 3 | 431.432 | 7,4% | 43,6% | 151.619 | 41.962 | 109.658 | 10,2% | 82.037 |
| 4 | 458.707 | 6,3% | 42,7% | 157.877 | 44.933 | 112.944 | 10,2% | 76.705 |
| 5 | 487.914 | 6,4% | 41,8% | 164.390 | 44.616 | 119.774 | 10,2% | 73.844 |
| 6 | 516.914 | 5,9% | 40,9% | 169.733 | 28.535 | 141.197 | 9,8% | 79.267 |
| 7 | 545.449 | 5,5% | 40,0% | 174.461 | 27.801 | 146.661 | 9,5% | 75.201 |
| 8 | 573.250 | 5,1% | 40,0% | 182.618 | 26.790 | 155.828 | 9,2% | 73.203 |
| 9 | 600.040 | 4,7% | 40,0% | 190.383 | 25.502 | 164.881 | 8,8% | 71.181 |
| 10 | 625.542 | 4,2% | 40,0% | 197.671 | 26.586 | 171.086 | 8,5% | 68.086 |
| Terminal | 652.128 | 4,2% | 40,0% | 206.072 | 103.279 | 102.793 | 8,5% | — |

**C · Tesis de disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige** — probabilidad 10%; valor terminal 1.891.917 (VP 752.914); DCF US$192,69 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 355.252 | 7,1% | 46,3% | 132.578 | 21.718 | 110.860 | 10,2% | 100.639 |
| 2 | 369.368 | 4,0% | 43,6% | 129.936 | 24.493 | 105.442 | 10,2% | 86.895 |
| 3 | 385.289 | 4,3% | 42,3% | 131.410 | 28.270 | 103.140 | 10,2% | 77.161 |
| 4 | 403.665 | 4,8% | 41,0% | 133.355 | 29.837 | 103.518 | 10,2% | 70.304 |
| 5 | 423.058 | 4,8% | 39,7% | 135.231 | 30.549 | 104.683 | 10,2% | 64.540 |
| 6 | 442.915 | 4,7% | 38,3% | 136.291 | 20.297 | 115.993 | 9,8% | 65.118 |
| 7 | 463.212 | 4,6% | 37,0% | 137.046 | 20.714 | 116.332 | 9,5% | 59.650 |
| 8 | 483.926 | 4,5% | 37,0% | 142.600 | 21.104 | 121.497 | 9,2% | 57.075 |
| 9 | 505.030 | 4,4% | 37,0% | 148.220 | 21.464 | 126.756 | 8,8% | 54.722 |
| 10 | 526.494 | 4,3% | 37,0% | 153.894 | 22.376 | 131.518 | 8,5% | 52.339 |
| Terminal | 548.870 | 4,2% | 37,0% | 160.435 | 80.406 | 80.028 | 8,5% | — |

**D · Microsoft gana la plataforma empresarial de IA** — probabilidad 20%; valor terminal 8.505.507 (VP 3.384.884); DCF US$585,53 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 400.928 | 20,8% | 46,3% | 149.624 | 131.530 | 18.095 | 10,2% | 16.426 |
| 2 | 479.846 | 19,7% | 46,8% | 180.955 | 143.702 | 37.253 | 10,2% | 30.700 |
| 3 | 566.067 | 18,0% | 47,0% | 214.578 | 146.739 | 67.838 | 10,2% | 50.751 |
| 4 | 654.111 | 15,6% | 47,3% | 249.233 | 150.797 | 98.436 | 10,2% | 66.852 |
| 5 | 744.589 | 13,8% | 47,5% | 285.165 | 147.872 | 137.292 | 10,2% | 84.644 |
| 6 | 833.312 | 11,9% | 47,8% | 319.499 | 83.326 | 236.173 | 9,8% | 132.586 |
| 7 | 916.638 | 10,0% | 48,0% | 351.823 | 74.091 | 277.732 | 9,5% | 142.408 |
| 8 | 990.729 | 8,1% | 48,0% | 378.735 | 61.093 | 317.642 | 9,2% | 149.218 |
| 9 | 1.051.821 | 6,2% | 48,0% | 400.470 | 44.702 | 355.768 | 8,8% | 153.589 |
| 10 | 1.096.524 | 4,3% | 48,0% | 415.802 | 46.602 | 369.200 | 8,5% | 146.928 |
| Terminal | 1.143.126 | 4,2% | 48,0% | 433.473 | 73.690 | 359.783 | 8,5% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| A | 890.966,32 | 2.438.724,13 | 3.329.690,46 | 3.319.461,46 | 446,95 |
| B | 760.991,90 | 967.091,11 | 1.728.083,01 | 1.717.854,01 | 231,30 |
| C | 688.443,12 | 752.914,47 | 1.441.357,59 | 1.431.128,59 | 192,69 |
| D | 974.103,97 | 3.384.884,05 | 4.358.988,02 | 4.348.759,02 | 585,53 |

Ejemplo A: (890.966,32 + 2.438.724,13 + 76.843 + 36.348 − 123.420) / 7.427,0 = US$446,95 por acción. El terminal representa 73,2% del valor operativo de A: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. Valor esperado, probabilidades y margen de seguridad

Las probabilidades 45% / 25% / 10% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

Valor esperado = 0,45 × 446,945127 + 0,25 × 231,298507 + 0,10 × 192,692687 + 0,20 × 585,533731 = US$395,325949 ≈ US$395,33. Los aportes son US$201,13 + US$57,82 + US$19,27 + US$117,11 por acción.

Precio con MOS = valor esperado × (1 − 35%) = 395,325949 × 0,65 = US$256,961867 ≈ US$256,96. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. No se aplica al antiguo Base ni a la historia central A.

Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; central H11; rango H12:H13; MOS H14. Los DCF completos empiezan en las filas 22 (A), 46 (B), 70 (C) y 94 (D); sus valores por acción están en B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: base, conservadora, disrupción y optimista

Estas etiquetas describen las historias A–D activas. La tesis base es A, con un DCF de US$446,95; el valor esperado de US$395,33 combina las cuatro tesis con sus probabilidades. La antigua calibración C/B/O de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### A · Tesis base: Azure y Copilot sostienen el doble dígito

**Qué plantea.** Es la continuación de FY24-FY26 con desaceleración gradual.

**Traducción al modelo.** Productivity and Business Processes crece 14%, 12%, 11%, 10%, 9%; Intelligent Cloud crece 25%, 20%, 17%, 15%, 13%; More Personal Computing crece 0%, 1%, 2%, 2%, 2%. El crecimiento anual compuesto de cinco años es 13,0%; el margen operativo objetivo es 45,0%. El ROIC terminal es 25,0%. El crecimiento terminal es 4,25%, el de la hoja. Probabilidad: 45%; DCF: US$446,95 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (azure y otros servicios de nube (interanual): ~+30% (FY26); microsoft 365 comercial / Copilot: En alza; capex / ingresos: ~35% (FY26)). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### B · Tesis conservadora: El capex de IA rinde menos de lo esperado

**Qué plantea.** Es un capex que rinde menos: precios de cómputo en baja y menor dependencia de OpenAI.

**Traducción al modelo.** Productivity and Business Processes crece 10%, 8%, 7%, 6%, 6%; Intelligent Cloud crece 18%, 12%, 10%, 8%, 8%; More Personal Computing crece -2%, 0%, 0%, 1%, 1%. El crecimiento anual compuesto de cinco años es 8,0%; el margen operativo objetivo es 40,0%. El ROIC terminal es el costo de capital (8,48%). El crecimiento terminal es 4,25%, el de la hoja. Probabilidad: 25%; DCF: US$231,30 por acción.

**Cómo contrastarla.** La apoyarían: azure y otros servicios de nube (interanual): ≤ +18%; microsoft 365 comercial / Copilot: asientos de Copilot estancados; capex / ingresos: sube sin aceleración de Azure; margen operativo: ≤ 42%.


#### C · Tesis de disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige

**Qué plantea.** Es una corrección de la demanda de cómputo.

**Traducción al modelo.** Productivity and Business Processes crece 8%, 6%, 5%, 5%, 5%; Intelligent Cloud crece 10%, 4%, 5%, 6%, 6%; More Personal Computing crece -3%, -2%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 5,0%; el margen operativo objetivo es 37,0%. El ROIC terminal es el costo de capital (8,48%). El crecimiento terminal es 4,25%, el de la hoja. Probabilidad: 10%; DCF: US$192,69 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que B: azure y otros servicios de nube (interanual): ≤ +18%; microsoft 365 comercial / Copilot: asientos de Copilot estancados; capex / ingresos: sube sin aceleración de Azure; margen operativo: ≤ 42%.


#### D · Tesis optimista: Microsoft gana la plataforma empresarial de IA

**Qué plantea.** Es Microsoft como plataforma empresarial de IA (Copilot en cada asiento, Azure como infraestructura dominante).

**Traducción al modelo.** Productivity and Business Processes crece 17%, 16%, 15%, 13%, 12%; Intelligent Cloud crece 32%, 28%, 24%, 20%, 17%; More Personal Computing crece 2%, 3%, 3%, 3%, 3%. El crecimiento anual compuesto de cinco años es 17,5%; el margen operativo objetivo es 48,0%. El ROIC terminal es 25,0%. El crecimiento terminal es 4,25%, el de la hoja. Probabilidad: 20%; DCF: US$585,53 por acción.

**Cómo contrastarla.** La confirmarían: azure y otros servicios de nube (interanual): ≥ +25%; microsoft 365 comercial / Copilot: ARPU creciendo ≥ 8%; capex / ingresos: estable o bajando con ingresos creciendo; margen operativo: ≥ 45%.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: A/B/C/D: 4,25%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas y valor esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,35) | Valor/acción (beta 1,27) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| **A · Azure y Copilot sostienen el doble dígito** | 45% | Productivity and Business Processes: 14%, 12%, 11%, 10%, 9%; Intelligent Cloud: 25%, 20%, 17%, 15%, 13%; More Personal Computing: 0%, 1%, 2%, 2%, 2% | 13,0% | 45% | 0,7 | 25,0% | 4,25% | US$446,95 | US$456,64 |
| **B · El capex de IA rinde menos de lo esperado** | 25% | Productivity and Business Processes: 10%, 8%, 7%, 6%, 6%; Intelligent Cloud: 18%, 12%, 10%, 8%, 8%; More Personal Computing: -2%, 0%, 0%, 1%, 1% | 8,0% | 40% | 0,7 | = costo de capital | 4,25% | US$231,30 | US$235,91 |
| **C · Tesis de disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige** | 10% | Productivity and Business Processes: 8%, 6%, 5%, 5%, 5%; Intelligent Cloud: 10%, 4%, 5%, 6%, 6%; More Personal Computing: -3%, -2%, 0%, 0%, 0% | 5,0% | 37% | 0,7 | = costo de capital | 4,25% | US$192,69 | US$196,38 |
| **D · Microsoft gana la plataforma empresarial de IA** | 20% | Productivity and Business Processes: 17%, 16%, 15%, 13%, 12%; Intelligent Cloud: 32%, 28%, 24%, 20%, 17%; More Personal Computing: 2%, 3%, 3%, 3%, 3% | 17,5% | 48% | 0,6 | 25,0% | 4,25% | US$585,53 | US$598,64 |
| **Valor esperado** | 100% |  |  |  |  |  |  | **US$395,33** | **US$403,83** |

A (45%) es la continuación de FY24-FY26 con desaceleración gradual. B (25%) es un capex que rinde menos: precios de cómputo en baja y menor dependencia de OpenAI. C (10%) es una corrección de la demanda de cómputo. D (20%) es Microsoft como plataforma empresarial de IA (Copilot en cada asiento, Azure como infraestructura dominante). En las historias de erosión (B y C) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF técnico anterior (beta 1,35; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF técnico anterior de la hoja.

| Crecimiento \ Margen | 41,0% | 43,0% | 45,0% | 47,0% | 49,0% |
|---|---:|---:|---:|---:|---:|
| 8,9% | 342,91 | 359,16 | 375,40 | 391,65 | 407,89 |
| 10,9% | 377,79 | 396,15 | 414,50 | 432,85 | 451,20 |
| 12,9% | 416,47 | 437,17 | 457,87 | 478,56 | 499,26 |
| 14,9% | 459,32 | 482,62 | 505,93 | 529,23 | 552,54 |
| 16,9% | 506,74 | 532,94 | 559,14 | 585,34 | 611,53 |


### Pre-mortem

1. OpenAI diversifica proveedores de cómputo y Azure pierde su cliente de IA más grande.
2. Copilot no convence: la adopción pagada se estanca y Microsoft 365 crece solo por precio.
3. Exceso de capacidad de centros de datos en 2028: precios de GPU en la nube bajan y hay deterioro de activos.
4. Falta energía o chips y Microsoft no puede entregar la capacidad vendida.
5. Regulación (competencia en la nube y en IA) limita la venta atada de productos.

**Evidencia en contra de la historia más probable:** el FCFF cayó a menos de la mitad en dos años mientras el capex se triplicó; si el crecimiento de Azure baja a ~20% antes de que el capex se modere, la historia B se vuelve la central.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Azure y otros servicios de nube (interanual) | ~+30% (FY26) | ≥ +25% | ≤ +18% |
| Microsoft 365 comercial / Copilot | En alza | ARPU creciendo ≥ 8% | Asientos de Copilot estancados |
| Capex / ingresos | ~35% (FY26) | Estable o bajando con ingresos creciendo | Sube sin aceleración de Azure |
| Margen operativo | 46,8% | ≥ 45% | ≤ 42% |
| Dependencia de OpenAI | Alta | Base de clientes de IA diversificada | Pérdida de cargas de OpenAI |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$518,46**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 40% | Margen 45% | Margen 48% |
|---|---:|---:|---:|
| Beta 1,35 | 17,9% (3% de las empresas) | 15,4% (6% de las empresas) | 14,1% (8% de las empresas) |
| Beta 1,27 | 17,4% (3% de las empresas) | 15,0% (7% de las empresas) | 13,6% (9% de las empresas) |

Frente al valor esperado de las historias (US$395,33 con la beta de la hoja; US$403,83 con la propuesta), el precio está por encima en 31% y por encima en 28%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Plataforma de software empresarial que apuesta su capital a la infraestructura de IA |  |
| Probabilidades | A 45% / B 25% / C 10% / D 20% |  |
| Valor esperado (valor principal) (beta de la hoja / propuesta) | US$395,33 / US$403,83 |  |
| DCF base hoy (historia A) | US$446,95 |  |
| Precio con MOS sobre el valor esperado | US$256,96 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$192,69 a US$598,64 |  |
| Confianza | Media: el negocio es excepcional; el retorno del capex de IA no está probado |  |
| Qué cambiaría la opinión | Crecimiento de Azure frente al capex; adopción pagada de Copilot |  |
| Revisión | Resultados del 1T FY27 (oct-2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [Microsoft, resultados del 4T FY2026](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast)
- [Microsoft, ingresos por segmento del 4T FY2025](https://www.microsoft.com/en-us/investor/earnings/fy-2025-q4/segment-revenues)
- [Digital Applied, resultados FY26 Q4 y ARR de Copilot](https://www.digitalapplied.com/blog/microsoft-fy26-q4-earnings-copilot-arr)
- [CNBC, resultados de AWS del 2T 2026](https://www.cnbc.com/2026/07/30/aws-earnings-q2-2026.html)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
