---
schema: "jmr-analisis-damodaran-v1"
ticker: "MSFT"
analysis_date: "2026-09-30"
---

# Microsoft Corporation (MSFT) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Escenarios e historias unificados:** A, B, C y D son los cuatro escenarios DCF activos. La cifra principal es el valor intrínseco esperado US$405,29; la historia central A vale US$458,42 y el rango es US$197,86–599,73. El MOS 35% se aplica al esperado: US$263,44. El antiguo caso Base de la hoja (US$467,13) se conserva solo como calibración técnica; no es el DCF de la historia central A. Los múltiplos y su mezcla son lecturas auxiliares con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), balance del último 10-q, capital invertido operativo, conversor de i+d alineado al ltm, deuda de balance sin arrendamientos operativos, roic terminal (criterio damodaran) (22 celdas, con respaldo). Valor esperado US$406,69 → US$405,29. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de US$467,13 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


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

**Reinversión y retorno.** La hoja usa un sales-to-capital de 0,65 en los años 1-5 (cada dólar de ingreso nuevo exige ~US$1,5 de capital) y 1 después: refleja el ciclo de capex de IA, muy distinto del Microsoft de software puro. En la historia D se baja a 0,6. El valor depende de que el retorno de ese capital (ROIC incremental) supere el costo de capital de ~10%. Ventaja durable: costos de cambio y efectos de red (Office, Azure, Windows, LinkedIn), con ROIC de 30-72% en 2021-2026. El ROIC después del año 10 es 25,4%, el promedio de su industria según Damodaran (29,3%), limitado a su ROIC actual. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$20.770 millones, compromisos del 10-K al 2026-06-30) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$4.001 millones, +1,21 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,06 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usa una beta de 1,34. La bottom-up de Software (System & Application) reapalancada da 1,27; el DCF técnico anterior sube de US$467,13 a US$477,29. La diferencia es pequeña frente a la que producen las historias; el riesgo real está en el retorno del capex, no en la tasa.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF técnico anterior por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,36 | 10,3% | 10,2% | US$467,13 |
| Bottom-up del sector (Software (System & Application), reapalancada) | 1,27 | 9,9% | 9,8% | US$477,29 |


### Calibración técnica anterior C/B/O (referencia auxiliar)

| Supuesto | Conservador | Base | Optimista |
|---|---:|---:|---:|
| Crecimiento año 1 | 14,0% | 16,5% | 19,0% |
| Crecimiento años 2–5 | 8,0% | 12,0% | 14,0% |
| Margen año 1 (base ajustada del modelo) | 45,0% | 47,5% | 47,5% |
| Margen objetivo | 43,2% | 46,2% | 49,2% |

Ventas/capital: 0,6x en años 1–5 y 0,9x en 6–10. WACC: 10,2%. Ke: 10,3%. Impuesto efectivo: 19,4%. Convergencia: 7 años. Estos parámetros son escenarios del analista, no cifras reportadas. Los casos Conservador, Base y Optimista de la hoja ya no son escenarios activos: sirven de calibración y de supuestos auxiliares de múltiplos. No confundir el antiguo Base con la historia A.


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF técnico anterior | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 25,4% | 29,3% | 8,5% | 25,4% | US$467,13 | US$327,68 |

Fuentes de ventaja: Costos de cambio y efectos de red (Office, Azure, Windows, LinkedIn). Evidencia: ROIC 30-72% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor principal de US$405,29 se obtiene ejecutando cuatro DCF completos de diez años más valor terminal y ponderándolos por sus probabilidades. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. No se obtiene aplicando descuentos al antiguo Base de US$467,13 ni mezclando el DCF con múltiplos. La historia central A vale US$458,42; «central» y «esperado» son conceptos distintos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$331.839 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 140.116 + 138.116 + 53.606 = 331.839. |
| Margen inicial del DCF | 47,5% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 7 (Input sheet B31). |
| Impuesto | 19,40% en años 1–5; 21,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 10,15% → 8,48% | Tasa libre de riesgo 4,25%, beta 1,36, ERP 4,46%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 0,62x en años 1–5; 0,94x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. D usa 0,58x en años 1–5. |
| Crecimiento perpetuo | A/B/C/D: 4,25% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. |
| ROIC terminal | A/D: 25,40%; B/C: 8,48% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 76.843; deuda 127.658; activos no operativos 36.348; acciones 7.427,0 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo A, año 1: 140.116 × 1,14 + 138.116 × 1,25 + 53.606 × 1,00 = US$385.984,36 millones. Frente a 331.839, el crecimiento consolidado es 16,32%. En los años 2–5 es 14,05%, 12,72%, 11,55%, 10,30%; las ventas del año 5 son US$610.544,46 millones. El 13,0% de la tabla es el crecimiento anual compuesto de los cinco años: (610.544,46 / 331.839)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En A, año 1: NOPAT = 385.984,36 × 47,51% × (1 − 19,40%) = US$147.798,69 millones. La reinversión es US$86.828,46 millones y el FCFF es US$60.970,24 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 8,48%. Reinversión terminal sobre el NOPAT: A, 16,7% (4,25% / 25,40%); B, 50,1% (4,25% / 8,48%); C, 50,1% (4,25% / 8,48%); D, 16,7% (4,25% / 25,40%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en «Escenarios e historias»: ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**A · Azure y Copilot sostienen el doble dígito** — probabilidad 45%; valor terminal 6.312.486 (VP 2.512.694); DCF US$458,42 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 385.984 | 16,3% | 47,5% | 147.799 | 86.828 | 60.970 | 10,2% | 55.351 |
| 2 | 440.217 | 14,1% | 47,1% | 167.247 | 89.628 | 77.619 | 10,2% | 63.970 |
| 3 | 496.199 | 12,7% | 46,9% | 187.773 | 91.773 | 96.000 | 10,2% | 71.826 |
| 4 | 553.521 | 11,6% | 46,8% | 208.636 | 91.297 | 117.340 | 10,2% | 79.700 |
| 5 | 610.544 | 10,3% | 46,6% | 229.216 | 88.870 | 140.346 | 10,2% | 86.541 |
| 6 | 666.053 | 9,1% | 46,4% | 248.067 | 55.778 | 192.289 | 9,8% | 107.969 |
| 7 | 718.546 | 7,9% | 46,2% | 265.482 | 50.933 | 214.549 | 9,5% | 110.033 |
| 8 | 766.479 | 6,7% | 46,2% | 282.056 | 44.472 | 237.583 | 9,1% | 111.633 |
| 9 | 808.332 | 5,5% | 46,2% | 296.259 | 36.504 | 259.755 | 8,8% | 112.164 |
| 10 | 842.686 | 4,3% | 46,2% | 307.601 | 38.056 | 269.546 | 8,5% | 107.293 |
| Terminal | 878.500 | 4,2% | 46,2% | 320.674 | 53.656 | 267.018 | 8,5% | — |

**B · El capex de IA rinde menos de lo esperado** — probabilidad 25%; valor terminal 2.503.346 (VP 996.460); DCF US$237,05 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 369.639 | 11,4% | 47,5% | 141.540 | 51.053 | 90.487 | 10,2% | 82.147 |
| 2 | 401.527 | 8,6% | 45,7% | 147.925 | 47.879 | 100.045 | 10,2% | 82.452 |
| 3 | 431.432 | 7,4% | 44,8% | 155.812 | 43.668 | 112.144 | 10,2% | 83.905 |
| 4 | 458.707 | 6,3% | 43,9% | 162.335 | 46.760 | 115.575 | 10,2% | 78.502 |
| 5 | 487.914 | 6,4% | 43,0% | 169.131 | 46.430 | 122.701 | 10,2% | 75.661 |
| 6 | 516.914 | 5,9% | 42,1% | 174.736 | 30.321 | 144.415 | 9,8% | 81.088 |
| 7 | 545.449 | 5,5% | 41,2% | 179.720 | 29.541 | 150.179 | 9,5% | 77.020 |
| 8 | 573.250 | 5,1% | 41,2% | 188.122 | 28.467 | 159.655 | 9,1% | 75.017 |
| 9 | 600.040 | 4,7% | 41,2% | 196.121 | 27.098 | 169.023 | 8,8% | 72.985 |
| 10 | 625.542 | 4,2% | 41,2% | 203.629 | 28.249 | 175.380 | 8,5% | 69.810 |
| Terminal | 652.128 | 4,2% | 41,2% | 212.284 | 106.392 | 105.892 | 8,5% | — |

**C · Tesis de disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige** — probabilidad 10%; valor terminal 1.953.566 (VP 777.620); DCF US$197,86 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 355.252 | 7,1% | 47,5% | 136.031 | 22.601 | 113.430 | 10,2% | 102.975 |
| 2 | 369.368 | 4,0% | 44,8% | 133.525 | 25.489 | 108.036 | 10,2% | 89.038 |
| 3 | 385.289 | 4,3% | 43,5% | 135.154 | 29.420 | 105.735 | 10,2% | 79.110 |
| 4 | 403.665 | 4,8% | 42,2% | 137.278 | 31.050 | 106.227 | 10,2% | 72.153 |
| 5 | 423.058 | 4,8% | 40,9% | 139.343 | 31.791 | 107.552 | 10,2% | 66.319 |
| 6 | 442.915 | 4,7% | 39,5% | 140.578 | 21.568 | 119.010 | 9,8% | 66.824 |
| 7 | 463.212 | 4,6% | 38,2% | 141.512 | 22.010 | 119.502 | 9,5% | 61.287 |
| 8 | 483.926 | 4,5% | 38,2% | 147.247 | 22.424 | 124.823 | 9,1% | 58.650 |
| 9 | 505.030 | 4,4% | 38,2% | 153.049 | 22.807 | 130.242 | 8,8% | 56.239 |
| 10 | 526.494 | 4,3% | 38,2% | 158.909 | 23.776 | 135.132 | 8,5% | 53.790 |
| Terminal | 548.870 | 4,2% | 38,2% | 165.662 | 83.027 | 82.636 | 8,5% | — |

**D · Microsoft gana la plataforma empresarial de IA** — probabilidad 20%; valor terminal 8.747.273 (VP 3.481.865); DCF US$599,73 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 400.928 | 20,8% | 47,5% | 153.521 | 136.469 | 17.052 | 10,2% | 15.480 |
| 2 | 479.846 | 19,7% | 48,0% | 185.618 | 149.099 | 36.520 | 10,2% | 30.098 |
| 3 | 566.067 | 18,0% | 48,2% | 220.079 | 152.250 | 67.829 | 10,2% | 50.749 |
| 4 | 654.111 | 15,6% | 48,5% | 255.590 | 156.460 | 99.130 | 10,2% | 67.332 |
| 5 | 744.589 | 13,8% | 48,7% | 292.401 | 153.426 | 138.975 | 10,2% | 85.695 |
| 6 | 833.312 | 11,9% | 49,0% | 327.565 | 88.541 | 239.025 | 9,8% | 134.211 |
| 7 | 916.638 | 10,0% | 49,2% | 360.660 | 78.728 | 281.932 | 9,5% | 144.591 |
| 8 | 990.729 | 8,1% | 49,2% | 388.248 | 64.916 | 323.332 | 9,1% | 151.923 |
| 9 | 1.051.821 | 6,2% | 49,2% | 410.529 | 47.500 | 363.029 | 8,8% | 156.758 |
| 10 | 1.096.524 | 4,3% | 49,2% | 426.246 | 49.519 | 376.727 | 8,5% | 149.957 |
| Terminal | 1.143.126 | 4,2% | 49,2% | 444.361 | 74.352 | 370.010 | 8,5% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| A | 906.480,01 | 2.512.694,36 | 3.419.174,37 | 3.404.707,55 | 458,42 |
| B | 778.588,39 | 996.460,41 | 1.775.048,81 | 1.760.581,99 | 237,05 |
| C | 706.384,87 | 777.619,97 | 1.484.004,85 | 1.469.538,04 | 197,86 |
| D | 986.794,44 | 3.481.865,09 | 4.468.659,53 | 4.454.192,71 | 599,73 |

Ejemplo A: (906.480,01 + 2.512.694,36 + 76.843 + 36.348 − 127.658) / 7.427,0 = US$458,42 por acción. El terminal representa 73,5% del valor operativo de A: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. Valor esperado, probabilidades y margen de seguridad

Las probabilidades 45% / 25% / 10% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

Valor esperado = 0,45 × 458,422991 + 0,25 × 237,051568 + 0,10 × 197,864284 + 0,20 × 599,729731 = US$405,285613 ≈ US$405,29. Los aportes son US$206,29 + US$59,26 + US$19,79 + US$119,95 por acción.

Precio con MOS = valor esperado × (1 − 35%) = 405,285613 × 0,65 = US$263,435648 ≈ US$263,44. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. No se aplica al antiguo Base ni a la historia central A.

Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; central H11; rango H12:H13; MOS H14. Los DCF completos empiezan en las filas 22 (A), 46 (B), 70 (C) y 94 (D); sus valores por acción están en B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: base, conservadora, disrupción y optimista

Estas etiquetas describen las historias A–D activas. La tesis base es A, con un DCF de US$458,42; el valor esperado de US$405,29 combina las cuatro tesis con sus probabilidades. La antigua calibración C/B/O de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### A · Tesis base: Azure y Copilot sostienen el doble dígito

**Qué plantea.** Es la continuación de FY24-FY26 con desaceleración gradual.

**Traducción al modelo.** Productivity and Business Processes crece 14%, 12%, 11%, 10%, 9%; Intelligent Cloud crece 25%, 20%, 17%, 15%, 13%; More Personal Computing crece 0%, 1%, 2%, 2%, 2%. El crecimiento anual compuesto de cinco años es 13,0%; el margen operativo objetivo es 46,2%. El ROIC terminal es 25,4%. El crecimiento terminal es 4,25%, el de la hoja. Probabilidad: 45%; DCF: US$458,42 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (azure y otros servicios de nube (interanual): ~+30% (FY26); microsoft 365 comercial / Copilot: En alza; capex / ingresos: ~35% (FY26)). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### B · Tesis conservadora: El capex de IA rinde menos de lo esperado

**Qué plantea.** Es un capex que rinde menos: precios de cómputo en baja y menor dependencia de OpenAI.

**Traducción al modelo.** Productivity and Business Processes crece 10%, 8%, 7%, 6%, 6%; Intelligent Cloud crece 18%, 12%, 10%, 8%, 8%; More Personal Computing crece -2%, 0%, 0%, 1%, 1%. El crecimiento anual compuesto de cinco años es 8,0%; el margen operativo objetivo es 41,2%. El ROIC terminal es el costo de capital (8,48%). El crecimiento terminal es 4,25%, el de la hoja. Probabilidad: 25%; DCF: US$237,05 por acción.

**Cómo contrastarla.** La apoyarían: azure y otros servicios de nube (interanual): ≤ +18%; microsoft 365 comercial / Copilot: asientos de Copilot estancados; capex / ingresos: sube sin aceleración de Azure; margen operativo: ≤ 42%.


#### C · Tesis de disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige

**Qué plantea.** Es una corrección de la demanda de cómputo.

**Traducción al modelo.** Productivity and Business Processes crece 8%, 6%, 5%, 5%, 5%; Intelligent Cloud crece 10%, 4%, 5%, 6%, 6%; More Personal Computing crece -3%, -2%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 5,0%; el margen operativo objetivo es 38,2%. El ROIC terminal es el costo de capital (8,48%). El crecimiento terminal es 4,25%, el de la hoja. Probabilidad: 10%; DCF: US$197,86 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que B: azure y otros servicios de nube (interanual): ≤ +18%; microsoft 365 comercial / Copilot: asientos de Copilot estancados; capex / ingresos: sube sin aceleración de Azure; margen operativo: ≤ 42%.


#### D · Tesis optimista: Microsoft gana la plataforma empresarial de IA

**Qué plantea.** Es Microsoft como plataforma empresarial de IA (Copilot en cada asiento, Azure como infraestructura dominante).

**Traducción al modelo.** Productivity and Business Processes crece 17%, 16%, 15%, 13%, 12%; Intelligent Cloud crece 32%, 28%, 24%, 20%, 17%; More Personal Computing crece 2%, 3%, 3%, 3%, 3%. El crecimiento anual compuesto de cinco años es 17,5%; el margen operativo objetivo es 49,2%. El ROIC terminal es 25,4%. El crecimiento terminal es 4,25%, el de la hoja. Probabilidad: 20%; DCF: US$599,73 por acción.

**Cómo contrastarla.** La confirmarían: azure y otros servicios de nube (interanual): ≥ +25%; microsoft 365 comercial / Copilot: ARPU creciendo ≥ 8%; capex / ingresos: estable o bajando con ingresos creciendo; margen operativo: ≥ 45%.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: A/B/C/D: 4,25%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas y valor esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,36) | Valor/acción (beta 1,27) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| **A · Azure y Copilot sostienen el doble dígito** | 45% | Productivity and Business Processes: 14%, 12%, 11%, 10%, 9%; Intelligent Cloud: 25%, 20%, 17%, 15%, 13%; More Personal Computing: 0%, 1%, 2%, 2%, 2% | 13,0% | 46,2% | 0,6 | 25,4% | 4,25% | US$458,42 | US$468,38 |
| **B · El capex de IA rinde menos de lo esperado** | 25% | Productivity and Business Processes: 10%, 8%, 7%, 6%, 6%; Intelligent Cloud: 18%, 12%, 10%, 8%, 8%; More Personal Computing: -2%, 0%, 0%, 1%, 1% | 8,0% | 41,2% | 0,6 | = costo de capital | 4,25% | US$237,05 | US$241,79 |
| **C · Tesis de disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige** | 10% | Productivity and Business Processes: 8%, 6%, 5%, 5%, 5%; Intelligent Cloud: 10%, 4%, 5%, 6%, 6%; More Personal Computing: -3%, -2%, 0%, 0%, 0% | 5,0% | 38,2% | 0,6 | = costo de capital | 4,25% | US$197,86 | US$201,66 |
| **D · Microsoft gana la plataforma empresarial de IA** | 20% | Productivity and Business Processes: 17%, 16%, 15%, 13%, 12%; Intelligent Cloud: 32%, 28%, 24%, 20%, 17%; More Personal Computing: 2%, 3%, 3%, 3%, 3% | 17,5% | 49,2% | 0,6 | 25,4% | 4,25% | US$599,73 | US$613,17 |
| **Valor esperado** | 100% |  |  |  |  |  |  | **US$405,29** | **US$414,02** |

A (45%) es la continuación de FY24-FY26 con desaceleración gradual. B (25%) es un capex que rinde menos: precios de cómputo en baja y menor dependencia de OpenAI. C (10%) es una corrección de la demanda de cómputo. D (20%) es Microsoft como plataforma empresarial de IA (Copilot en cada asiento, Azure como infraestructura dominante). En las historias de erosión (B y C) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF técnico anterior (beta 1,36; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF técnico anterior de la hoja.

| Crecimiento \ Margen | 42,2% | 44,2% | 46,2% | 48,2% | 50,2% |
|---|---:|---:|---:|---:|---:|
| 8,9% | 352,50 | 368,78 | 385,07 | 401,35 | 417,64 |
| 10,9% | 388,34 | 406,74 | 425,14 | 443,53 | 461,93 |
| 12,9% | 428,08 | 448,83 | 469,58 | 490,33 | 511,08 |
| 14,9% | 472,10 | 495,47 | 518,84 | 542,20 | 565,57 |
| 16,9% | 520,82 | 547,09 | 573,36 | 599,63 | 625,89 |


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

|  | Margen 41% | Margen 46% | Margen 49% |
|---|---:|---:|---:|
| Beta 1,36 | 17,3% (4% de las empresas) | 14,9% (7% de las empresas) | 13,6% (9% de las empresas) |
| Beta 1,27 | 16,9% (4% de las empresas) | 14,4% (8% de las empresas) | 13,2% (9% de las empresas) |

Frente al valor esperado de las historias (US$405,29 con la beta de la hoja; US$414,02 con la propuesta), el precio está por encima en 28% y por encima en 25%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Plataforma de software empresarial que apuesta su capital a la infraestructura de IA |  |
| Probabilidades | A 45% / B 25% / C 10% / D 20% |  |
| Valor esperado (valor principal) (beta de la hoja / propuesta) | US$405,29 / US$414,02 |  |
| DCF base hoy (historia A) | US$458,42 |  |
| Precio con MOS sobre el valor esperado | US$263,44 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$197,86 a US$613,17 |  |
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
