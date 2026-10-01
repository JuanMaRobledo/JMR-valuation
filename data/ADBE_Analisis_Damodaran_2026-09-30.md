---
schema: "jmr-analisis-damodaran-v1"
ticker: "ADBE"
analysis_date: "2026-09-30"
---

# Adobe Inc. (ADBE) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Escenarios e historias unificados:** A, B, C y D son los cuatro escenarios DCF activos. La cifra principal es el valor intrínseco esperado US$364,82; la historia central A vale US$466,29 y el rango es US$172,96–584,46. El MOS 35% se aplica al esperado: US$237,13. El antiguo caso Base de la hoja (US$537,02) se conserva solo como calibración técnica; no es el DCF de la historia central A. Los múltiplos y su mezcla son lecturas auxiliares con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), capital invertido operativo, deuda de balance sin arrendamientos operativos (14 celdas, con respaldo). Valor esperado US$364,33 → US$364,82. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de US$537,02 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

Adobe es la suite de referencia de la creatividad profesional y de los documentos (PDF), vendida por suscripción: ~US$27.500 millones de ARR, margen operativo GAAP de ~36% y flujo libre de ~41% de las ventas. Los próximos cinco años dependen de una pregunta: si la IA generativa es una función que Adobe cobra dentro de sus suscripciones (Firefly, Acrobat AI Assistant, GenStudio) o una tecnología que abarata crear contenido y deja entrar a herramientas más baratas (Figma, Canva y los modelos generales de OpenAI o Google). Por ahora los datos apoyan la primera lectura: en el 3T FY26 las ventas crecieron 13%, la guía subió y el ARR «AI-first» pasó de US$650 millones (+150%). Pero la IA todavía es ~2,4% del ARR, y entre equipos de diseño la adopción de Figma (59%) ya supera a la de Adobe (42%). A esto se suma el cambio de CEO del 1-dic-2026.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Adobe crece ~8% anual cinco años más | Sí | Sí: +10-11% anual en FY23-FY25 y guía FY26 de ~+12% | Probable, desacelerando |
| La IA suma crecimiento sobre la base actual | Sí | Sí: ARR AI-first +150%, aunque solo ~2,4% del total | Incierto |
| El margen operativo sube a 40% y se sostiene | Sí | Sí: 36,6% en FY25 con capex ~1% de las ventas; la IA encarece el cómputo | Probable si no hay guerra de precios |
| Creative Cloud pierde poder de precio frente a Figma y Canva | Sí | Sí: Figma ya supera a Adobe en adopción entre equipos de diseño | Posible, gradual |


### Visión externa: tasas base

Con ventas LTM de US$25.970 millones (US$18.375 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **$12,000-25,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 3,3% y una mediana de 2,9% (desviación estándar 8,9%); sumando una inflación de 2,5%, la mediana nominal ronda 5,4%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| A · La IA se cobra dentro de la suscripción | 8,1% | 34% |
| B · Erosión gradual frente a Figma y Canva | 5,4% | 50% |
| C · Tesis de disrupción · Deterioro de los fundamentales | 0,9% | 76% |
| D · La IA amplía el mercado de Adobe | 11,0% | 21% |

En dólares de 2015 la empresa está en el tramo de US$12.000-25.000 millones: crecer 8,1% anual cinco años (historia A) lo logró ~34% de las empresas de ese tamaño; 11,0% (historia D), ~21%. Adobe tiene razones para estar arriba de la mediana: suscripción con alta retención, subidas de precio y venta cruzada de IA. Aun así, el DCF de la hoja (10,4% anual en los años 1-5) ya supone un resultado del cuartil superior, y la visión externa pide descontar esa confianza.


### Piezas del valor

**Crecimiento.** Las ventas crecieron 10,8% en FY24 y 10,5% en FY25; la guía FY26 (US$26.576-26.626 millones) implica ~12%. En el 3T FY26, Creative & Marketing Professionals facturó US$4.700 millones (+13%) y Business Professionals & Consumers US$1.900 millones (+16%). La reorganización de segmentos de 2026 no deja comparar series largas por segmento: la división LTM de las historias es una estimación propia con el peso del 3T (≈70% / 28% / 2%).

| US$ millones | FY23 | FY24 | FY25 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 19.409 | 21.505 | 23.769 | 25.970 |
| Crecimiento | +10,2% | +10,8% | +10,5% | — |
| Margen operativo GAAP | 34,3% | 31,3% | 36,6% | 35,7% |
| FCFF (hoja) | 6.102 | 6.749 | 8.702 | — |

**Márgenes.** El margen de FY24 (31,3%) está deprimido por el cargo de US$1.000 millones por la ruptura del acuerdo con Figma; sin él, la serie va de ~34% a ~36-37%. La hoja supone 38,5% el próximo año y 40% como objetivo. Es alcanzable por escala, pero la IA suma costo de cómputo (entrenar e inferir Firefly) y la competencia empuja a regalar créditos de IA. Por eso las historias van de 32% (comoditización) a 43% (la IA amplía el mercado).

**Reinversión y retorno.** Adobe casi no necesita capital para crecer: el capex de FY25 fue US$179 millones (~0,8% de las ventas) y el FCFF, ~US$8.700 millones. La hoja usa un sales-to-capital de 4 (años 1-5) y 4,5 (años 6-10), razonable para software. El riesgo está en las compras: si para defenderse de la IA Adobe vuelve a comprar (como intentó con Figma por US$20.000 millones), la reinversión real sería mucho mayor que la del DCF. Ventaja durable: costos de cambio y estándar de la industria creativa y documental, con ROIC en alza (38% → 59%). El ROIC después del año 10 es 29,3%, el promedio de su industria según Damodaran. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$403 millones, compromisos del 10-K al 2025-11-28) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$25 millones, +0,10 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,02 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usa una beta de 1,39. La beta bottom-up del sector (Software System & Application, 309 empresas, desapalancada y corregida por caja 1,25) reapalancada con la estructura de Adobe da 1,31, casi igual. El riesgo de Adobe no está en la tasa de descuento sino en los flujos (precio y retención de Creative Cloud), y eso se trata en las historias, no subiendo la beta.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF técnico anterior por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,39 | 11,2% | 10,8% | US$537,02 |
| Bottom-up del sector (Software (System & Application), reapalancada) | 1,31 | 10,8% | 10,4% | US$547,97 |


### Calibración técnica anterior C/B/O (referencia auxiliar)

| Supuesto | Conservador | Base | Optimista |
|---|---:|---:|---:|
| Crecimiento año 1 | 6,0% | 12,0% | 16,0% |
| Crecimiento años 2–5 | 6,0% | 10,0% | 16,0% |
| Margen año 1 (base ajustada del modelo) | 38,6% | 38,6% | 38,6% |
| Margen objetivo | 39,3% | 40,1% | 45,1% |

Ventas/capital: 3,8x en años 1–5 y 4,2x en 6–10. WACC: 10,8%. Ke: 11,2%. Impuesto efectivo: 21,5%. Convergencia: 3 años. Estos parámetros son escenarios del analista, no cifras reportadas. Los casos Conservador, Base y Optimista de la hoja ya no son escenarios activos: sirven de calibración y de supuestos auxiliares de múltiplos. No confundir el antiguo Base con la historia A.


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF técnico anterior | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 36,9% | 29,3% | 9,2% | 29,3% | US$537,02 | US$378,09 |

Fuentes de ventaja: Costos de cambio y estándar de la industria creativa y documental. Evidencia: ROIC 37-60% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor principal de US$364,82 se obtiene ejecutando cuatro DCF completos de diez años más valor terminal y ponderándolos por sus probabilidades. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. No se obtiene aplicando descuentos al antiguo Base de US$537,02 ni mezclando el DCF con múltiplos. La historia central A vale US$466,29; «central» y «esperado» son conceptos distintos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$25.970 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 17.819 + 7.263 + 888 = 25.970. |
| Margen inicial del DCF | 38,6% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 3 (Input sheet B31). |
| Impuesto | 21,52% en años 1–5; 25,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 10,80% → 9,22% | Tasa libre de riesgo 4,99%, beta 1,39, ERP 4,46%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 3,77x en años 1–5; 4,21x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | A/B/D: 4,99%; C: 0,00% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. C se estabiliza sin recuperarse: parte de su crecimiento del año 5 (-1,3%) y converge a 0,00% en el año 10 (piso de 0% nominal: el negocio residual deja de achicarse, lo que en términos reales sigue siendo contracción). Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | A/D: 29,30%; B/C: 9,22% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 5.639; deuda 6.766; acciones 389,2 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo A, año 1: 17.819 × 1,10 + 7.263 × 1,14 + 888 × 1,00 = US$28.768,72 millones. Frente a 25.970, el crecimiento consolidado es 10,78%. En los años 2–5 es 8,90%, 7,69%, 6,75%, 6,47%; las ventas del año 5 son US$38.346,75 millones. El 8,1% de la tabla es el crecimiento anual compuesto de los cinco años: (38.346,75 / 25.970)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En A, año 1: NOPAT = 28.768,72 × 38,60% × (1 − 21,52%) = US$8.714,27 millones. La reinversión es US$680,20 millones y el FCFF es US$8.034,07 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,22%. Reinversión terminal sobre el NOPAT: A, 17,0% (4,99% / 29,30%); B, 54,1% (4,99% / 9,22%); C, 0,0% (0,00% / 9,22%); D, 17,0% (4,99% / 29,30%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en «Escenarios e historias»: ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**A · La IA se cobra dentro de la suscripción** — probabilidad 40%; valor terminal 311.557 (VP 116.638); DCF US$466,29 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 28.769 | 10,8% | 38,6% | 8.714 | 680 | 8.034 | 10,8% | 7.251 |
| 2 | 31.330 | 8,9% | 39,6% | 9.736 | 640 | 9.096 | 10,8% | 7.410 |
| 3 | 33.740 | 7,7% | 40,1% | 10.617 | 605 | 10.013 | 10,8% | 7.361 |
| 4 | 36.017 | 6,7% | 40,1% | 11.334 | 619 | 10.715 | 10,8% | 7.110 |
| 5 | 38.347 | 6,5% | 40,1% | 12.067 | 629 | 11.438 | 10,8% | 6.850 |
| 6 | 40.714 | 6,2% | 40,1% | 12.698 | 569 | 12.129 | 10,5% | 6.574 |
| 7 | 43.107 | 5,9% | 40,1% | 13.324 | 572 | 12.752 | 10,2% | 6.274 |
| 8 | 45.513 | 5,6% | 40,1% | 13.941 | 572 | 13.369 | 9,9% | 5.988 |
| 9 | 47.919 | 5,3% | 40,1% | 14.544 | 569 | 13.975 | 9,5% | 5.714 |
| 10 | 50.310 | 5,0% | 40,1% | 15.129 | 597 | 14.532 | 9,2% | 5.440 |
| Terminal | 52.821 | 5,0% | 40,1% | 15.884 | 2.705 | 13.179 | 9,2% | — |

**B · Erosión gradual frente a Figma y Canva** — probabilidad 35%; valor terminal 132.626 (VP 49.651); DCF US$268,32 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 28.267 | 8,8% | 38,6% | 8.562 | 450 | 8.112 | 10,8% | 7.322 |
| 2 | 29.961 | 6,0% | 37,6% | 8.840 | 379 | 8.461 | 10,8% | 6.892 |
| 3 | 31.390 | 4,8% | 37,1% | 9.139 | 319 | 8.820 | 10,8% | 6.484 |
| 4 | 32.590 | 3,8% | 37,1% | 9.488 | 306 | 9.182 | 10,8% | 6.093 |
| 5 | 33.742 | 3,5% | 37,1% | 9.824 | 343 | 9.481 | 10,8% | 5.678 |
| 6 | 35.033 | 3,8% | 37,1% | 10.109 | 343 | 9.766 | 10,5% | 5.293 |
| 7 | 36.476 | 4,1% | 37,1% | 10.431 | 382 | 10.049 | 10,2% | 4.944 |
| 8 | 38.084 | 4,4% | 37,1% | 10.792 | 425 | 10.367 | 9,9% | 4.643 |
| 9 | 39.873 | 4,7% | 37,1% | 11.196 | 473 | 10.723 | 9,5% | 4.385 |
| 10 | 41.863 | 5,0% | 37,1% | 11.647 | 497 | 11.150 | 9,2% | 4.174 |
| Terminal | 43.952 | 5,0% | 37,1% | 12.228 | 6.618 | 5.610 | 9,2% | — |

**C · Tesis de disrupción · Deterioro de los fundamentales: La IA generativa comoditiza la creatividad** — probabilidad 15%; valor terminal 69.207 (VP 25.909); DCF US$172,96 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 27.515 | 5,9% | 38,6% | 8.334 | 155 | 8.180 | 10,8% | 7.382 |
| 2 | 28.098 | 2,1% | 34,3% | 7.555 | -34 | 7.590 | 10,8% | 6.182 |
| 3 | 27.969 | -0,5% | 32,1% | 7.045 | -102 | 7.147 | 10,8% | 5.254 |
| 4 | 27.585 | -1,4% | 32,1% | 6.948 | -97 | 7.045 | 10,8% | 4.675 |
| 5 | 27.220 | -1,3% | 32,1% | 6.857 | -76 | 6.933 | 10,8% | 4.152 |
| 6 | 26.933 | -1,1% | 32,1% | 6.724 | -51 | 6.775 | 10,5% | 3.672 |
| 7 | 26.719 | -0,8% | 32,1% | 6.611 | -34 | 6.645 | 10,2% | 3.269 |
| 8 | 26.578 | -0,5% | 32,1% | 6.517 | -17 | 6.533 | 9,9% | 2.926 |
| 9 | 26.508 | -0,3% | 32,1% | 6.440 | 0 | 6.440 | 9,5% | 2.633 |
| 10 | 26.508 | -0,0% | 32,1% | 6.381 | 0 | 6.381 | 9,2% | 2.389 |
| Terminal | 26.508 | 0,0% | 32,1% | 6.381 | 0 | 6.381 | 9,2% | — |

**D · La IA amplía el mercado de Adobe** — probabilidad 10%; valor terminal 401.548 (VP 150.328); DCF US$584,46 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 29.270 | 12,7% | 38,6% | 8.866 | 949 | 7.917 | 10,8% | 7.145 |
| 2 | 32.845 | 12,2% | 41,6% | 10.722 | 959 | 9.763 | 10,8% | 7.953 |
| 3 | 36.456 | 11,0% | 43,1% | 12.330 | 973 | 11.357 | 10,8% | 8.350 |
| 4 | 40.120 | 10,1% | 43,1% | 13.570 | 969 | 12.600 | 10,8% | 8.361 |
| 5 | 43.771 | 9,1% | 43,1% | 14.804 | 962 | 13.842 | 10,8% | 8.289 |
| 6 | 47.394 | 8,3% | 43,1% | 15.887 | 840 | 15.047 | 10,5% | 8.156 |
| 7 | 50.927 | 7,5% | 43,1% | 16.919 | 803 | 16.116 | 10,2% | 7.929 |
| 8 | 54.305 | 6,6% | 43,1% | 17.878 | 750 | 17.128 | 9,9% | 7.671 |
| 9 | 57.461 | 5,8% | 43,1% | 18.745 | 682 | 18.063 | 9,5% | 7.386 |
| 10 | 60.328 | 5,0% | 43,1% | 19.499 | 716 | 18.783 | 9,2% | 7.032 |
| Terminal | 63.339 | 5,0% | 43,1% | 20.472 | 3.487 | 16.985 | 9,2% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| A | 65.971,79 | 116.637,55 | 182.609,34 | 181.481,98 | 466,29 |
| B | 55.907,59 | 49.651,07 | 105.558,66 | 104.431,29 | 268,32 |
| C | 42.534,93 | 25.909,18 | 68.444,10 | 67.316,74 | 172,96 |
| D | 78.271,94 | 150.327,50 | 228.599,44 | 227.472,07 | 584,46 |

Ejemplo A: (65.971,79 + 116.637,55 + 5.639 − 6.766) / 389,2 = US$466,29 por acción. El terminal representa 63,9% del valor operativo de A: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. Valor esperado, probabilidades y margen de seguridad

Las probabilidades 40% / 35% / 15% / 10% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

Valor esperado = 0,40 × 466,294910 + 0,35 × 268,322954 + 0,15 × 172,961822 + 0,10 × 584,460623 = US$364,821333 ≈ US$364,82. Los aportes son US$186,52 + US$93,91 + US$25,94 + US$58,45 por acción.

Precio con MOS = valor esperado × (1 − 35%) = 364,821333 × 0,65 = US$237,133867 ≈ US$237,13. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. No se aplica al antiguo Base ni a la historia central A.

Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; central H11; rango H12:H13; MOS H14. Los DCF completos empiezan en las filas 22 (A), 46 (B), 70 (C) y 94 (D); sus valores por acción están en B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: base, conservadora, disrupción y optimista

Estas etiquetas describen las historias A–D activas. La tesis base es A, con un DCF de US$466,29; el valor esperado de US$364,82 combina las cuatro tesis con sus probabilidades. La antigua calibración C/B/O de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### A · Tesis base: Adobe monetiza la IA y conserva su posición

**Qué tiene que ocurrir.** Adobe mantiene el papel de sus herramientas en los flujos profesionales y cobra las funciones de IA mediante suscripciones, créditos o planes superiores. La IA ayuda a defender la retención y el gasto por cliente, pero no provoca una aceleración permanente. La competencia limita el crecimiento sin deshacer la ventaja comercial.

**Traducción al modelo.** Creative & Marketing Professionals crece 10%, 8%, 7%, 6%, 6%; Business Professionals & Consumers crece 14%, 12%, 10%, 9%, 8%; Otros crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 8,1%; el margen operativo objetivo es 40,1%. El ROIC terminal es 29,3%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 40%; DCF: US$466,29 por acción.

**Cómo contrastarla.** La confirmarían renovaciones y precio realizado estables, monetización de IA que aporte ventas y márgenes compatibles con el coste de cómputo. Perdería fuerza si el crecimiento solo se sostiene con descuentos, si empeora la retención o si la IA aumenta el coste sin elevar el gasto del cliente.


#### B · Tesis conservadora: Adobe sigue siendo rentable, pero pierde poder de precio

**Qué tiene que ocurrir.** Figma, Canva y otras herramientas capturan parte de los nuevos clientes y de los trabajos sencillos. Adobe conserva los flujos profesionales más difíciles de sustituir, pero necesita conceder más valor dentro de sus planes y tiene menos capacidad para subir precios. El negocio crece más lentamente y su ventaja se erosiona de forma gradual.

**Traducción al modelo.** Creative & Marketing Professionals crece 8%, 5%, 4%, 3%, 3%; Business Professionals & Consumers crece 12%, 9%, 7%, 6%, 5%; Otros crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 5,4%; el margen operativo objetivo es 37,1%. El ROIC terminal es el costo de capital (9,22%). El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 35%; DCF: US$268,32 por acción.

**Cómo contrastarla.** La apoyarían una desaceleración persistente, menor gasto por cliente o presión de descuentos con caja todavía sólida. Se debilitaría si Adobe mantiene la retención y monetiza la IA sin sacrificar precios ni margen. No hay una serie comparable verificada de adopción que demuestre que esta erosión ya esté ocurriendo.


#### C · Tesis de disrupción · Deterioro de los fundamentales: La IA generativa comoditiza la creatividad

**Qué tiene que ocurrir.** Para una parte relevante de los usuarios, producir contenido con herramientas de IA más baratas resulta suficiente y reduce la necesidad de pagar por la suite de Adobe. La presión afecta tanto a nuevos clientes como al gasto de la base instalada. Adobe conserva productos útiles y un negocio rentable, pero pierde una parte sustancial de su poder de precio y de sus retornos extraordinarios.

**Traducción al modelo.** Creative & Marketing Professionals crece 5%, 1%, -2%, -3%, -3%; Business Professionals & Consumers crece 9%, 5%, 3%, 2%, 2%; Otros crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 0,9%; el margen operativo objetivo es 32,1%. El ROIC terminal es el costo de capital (9,22%). El crecimiento terminal es 0,00%: los años 6–10 pasan de -1,3% a ese nivel, sin recuperación. Probabilidad: 15%; DCF: US$172,96 por acción.

**Cómo contrastarla.** La apoyarían deterioro sostenido de renovaciones, contracción de ingresos profesionales y necesidad de regalar funcionalidades de IA para retener usuarios. Se debilitaría si las herramientas complementan la suite y Adobe conserva el gasto de sus clientes. Es una hipótesis adversa severa; no es un caso de quiebra ni el peor resultado posible.


#### D · Tesis optimista: La IA amplía el mercado y Adobe captura el crecimiento

**Qué tiene que ocurrir.** La IA permite que más personas y empresas creen y distribuyan contenido, aumenta el volumen de trabajo y el gasto por cliente, y Adobe captura una parte relevante de esa expansión con Firefly, Acrobat y GenStudio. Los ingresos adicionales compensan el coste de cómputo y sostienen la ventaja competitiva.

**Traducción al modelo.** Creative & Marketing Professionals crece 12%, 12%, 11%, 10%, 9%; Business Professionals & Consumers crece 16%, 14%, 12%, 11%, 10%; Otros crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 11,0%; el margen operativo objetivo es 43,1%. El ROIC terminal es 29,3%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 10%; DCF: US$584,46 por acción.

**Cómo contrastarla.** La confirmarían expansión de clientes y gasto, monetización de IA que aporte crecimiento adicional y mejora de margen con retención sólida. Se debilitaría si el ARR de IA solo sustituye ingresos existentes o si aumenta su uso sin una contribución económica suficiente.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: A/B/D: 4,99%; C: 0,00%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas y valor esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,39) | Valor/acción (beta 1,31) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| **A · La IA se cobra dentro de la suscripción** | 40% | Creative & Marketing Professionals: 10%, 8%, 7%, 6%, 6%; Business Professionals & Consumers: 14%, 12%, 10%, 9%, 8%; Otros: 0%, 0%, 0%, 0%, 0% | 8,1% | 40,1% | 3,8 | 29,3% | 4,99% | US$466,29 | US$475,66 |
| **B · Erosión gradual frente a Figma y Canva** | 35% | Creative & Marketing Professionals: 8%, 5%, 4%, 3%, 3%; Business Professionals & Consumers: 12%, 9%, 7%, 6%, 5%; Otros: 0%, 0%, 0%, 0%, 0% | 5,4% | 37,1% | 3,8 | = costo de capital | 4,99% | US$268,32 | US$273,29 |
| **C · Tesis de disrupción · Deterioro de los fundamentales: La IA generativa comoditiza la creatividad** | 15% | Creative & Marketing Professionals: 5%, 1%, -2%, -3%, -3%; Business Professionals & Consumers: 9%, 5%, 3%, 2%, 2%; Otros: 0%, 0%, 0%, 0%, 0% | 0,9% | 32,1% | 3,8 | = costo de capital | 0,00% | US$172,96 | US$175,92 |
| **D · La IA amplía el mercado de Adobe** | 10% | Creative & Marketing Professionals: 12%, 12%, 11%, 10%, 9%; Business Professionals & Consumers: 16%, 14%, 12%, 11%, 10%; Otros: 0%, 0%, 0%, 0%, 0% | 11,0% | 43,1% | 3,8 | 29,3% | 4,99% | US$584,46 | US$596,39 |
| **Valor esperado** | 100% |  |  |  |  |  |  | **US$364,82** | **US$371,94** |

A (40%) continúa lo que muestran los últimos trimestres: crecimiento de doble dígito bajo que desacelera y margen de 40%. B (35%) pesa casi lo mismo porque la adopción de Figma crece más rápido que la de Adobe. C (15%) es la disrupción: poco probable en cinco años por el costo de cambiar flujos profesionales, pero no despreciable. D (10%) exige que la IA agrande el mercado y no solo defienda la base. En las historias de erosión (B y C) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF técnico anterior (beta 1,39; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF técnico anterior de la hoja.

| Crecimiento \ Margen | 36,1% | 38,1% | 40,1% | 42,1% | 44,1% |
|---|---:|---:|---:|---:|---:|
| 6,4% | 390,14 | 410,95 | 431,75 | 452,56 | 473,36 |
| 8,4% | 435,75 | 459,19 | 482,63 | 506,07 | 529,52 |
| 10,4% | 486,41 | 512,79 | 539,17 | 565,54 | 591,92 |
| 12,4% | 542,63 | 572,27 | 601,91 | 631,54 | 661,18 |
| 14,4% | 604,93 | 638,19 | 671,44 | 704,70 | 737,96 |


### Pre-mortem

1. El ARR «AI-first» se estanca antes de llegar a 5% del total y la IA termina regalada dentro de los planes para no perder usuarios.
2. Figma y Canva capturan a los nuevos diseñadores y equipos de marketing; Creative Cloud crece solo por precio y la retención cae.
3. El nuevo CEO (1-dic-2026) cambia la estrategia o salen ejecutivos clave en medio del giro a la IA.
4. Adobe hace una compra grande para defenderse y destruye valor (precio alto, retorno bajo).
5. El costo de cómputo de la IA baja el margen a 32-34% en lugar de subirlo a 40%.

**Evidencia en contra de la historia más probable:** la adopción relativa se mueve en contra (Figma 59% frente a 42% de Adobe en equipos de diseño) y el consenso (~40 analistas en «Hold») no cree la guía. Si Creative & Marketing Professionals baja de ~13% a un dígito bajo en 2027, la historia A pierde peso a favor de B.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Crecimiento de ingresos (interanual) | +13% (3T FY26) | ≥ +9% en FY27 | ≤ +6% |
| ARR «AI-first» | >US$650M, +150% | > 5% del ARR total en 2027 | Crece < 60% antes de llegar a 5% |
| Creative & Marketing Professionals | +13% | ≥ +8% | ≤ +4% |
| Margen operativo GAAP | 35,7% LTM | ≥ 37% | ≤ 33% |
| Adopción Figma frente a Adobe (equipos de diseño) | 59% vs 42% | Brecha estable o cerrándose | Brecha y gasto por cliente a favor de Figma |
| Transición de CEO | 1-dic-2026 | Sin cambios bruscos de estrategia | Salida de ejecutivos clave |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$239,94**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 35% | Margen 38% | Margen 40% |
|---|---:|---:|---:|
| Beta 1,39 | -1,9% (87% de las empresas) | -3,2% (90% de las empresas) | -4,0% (91% de las empresas) |
| Beta 1,31 | -2,2% (88% de las empresas) | -3,5% (90% de las empresas) | -4,3% (91% de las empresas) |

Frente al valor esperado de las historias (US$364,82 con la beta de la hoja; US$371,94 con la propuesta), el precio está por debajo en 34% y por debajo en 35%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Suite creativa y documental por suscripción que defiende su precio con IA frente a Figma y Canva |  |
| Probabilidades | A 40% / B 35% / C 15% / D 10% |  |
| Valor esperado (valor principal) (beta de la hoja / propuesta) | US$364,82 / US$371,94 |  |
| DCF base hoy (historia A) | US$466,29 |  |
| Precio con MOS sobre el valor esperado | US$237,13 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$172,96 a US$596,39 |  |
| Confianza | Media: la base es muy rentable y recurrente; lo incierto es el precio de Creative Cloud en la era de la IA |  |
| Qué cambiaría la opinión | Crecimiento de Creative & Marketing Professionals, peso del ARR «AI-first» y adopción frente a Figma |  |
| Revisión | Resultados del 4T FY26 (dic-2026) y primeros meses del nuevo CEO |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Antecedentes de revisiones anteriores

Notas de revisiones previas, con las cifras de su fecha; las cifras vigentes son las de esta sección.

**Dictamen de auditoría del 30-sep-2026 (cifras de esa fecha).** DCF técnico anterior US$536,48, condicionado a ROIC terminal 29,3%; contraste sin retorno excedente terminal US$377,94 (−29,55%). Valor esperado de cuatro historias US$364,33; MOS 35% US$236,81. El ROIC excedente no es incorrecto por definición: requiere evidencia de duración de la ventaja. Falta una serie homogénea que incluya I+D, goodwill y adquisiciones, así como soporte de ventas/capital 4x–4,5x. La coincidencia del cálculo con la hoja no certifica esos supuestos ni el cumplimiento integral de los prompts v4/v5.

**Corrección de la historia C, 30-sep-2026.** La convergencia automática a 4,99% introducía una recuperación no explicada por la tesis. Se sustituye por estabilización nominal del negocio residual: crecimiento años 6–10 de −1,06%, −0,79%, −0,53%, −0,26% y 0%; perpetuidad 0%, margen 32% y ROIC igual a WACC. El 0% es juicio del analista aceptado por el usuario, no una cifra de Adobe. El ingreso del año 10 y terminal es US$26.508,16 millones. La reinversión negativa de algunos años representa liberación de capital y sigue siendo una salvedad económica por validar; no debe interpretarse como recuperación automática de todo el capital intangible. Damodaran, The Stable Growth Rate, consultado 30-sep-2026, permite crecimiento estable menor o negativo, pero no determina el 0% elegido.


### Fuentes de esta sección

- [Adobe, resultados del 3T FY2026 (Form 8-K, ex. 99.1)](https://www.sec.gov/Archives/edgar/data/796343/000079634326000147/adbeex991q326.htm)
- [Adobe, anuncio de Anil Chakravarthy como CEO (sep-2026)](https://news.adobe.com/news/2026/09/adobe-announces-anil-chakravarthy-to-become-president-and-ceo)
- [Yahoo Finance, «Adobe Valuation Questioned As Figma AI Credits Challenge Creative Cloud»](https://finance.yahoo.com/news/adobe-valuation-questioned-figma-ai-031116166.html)
- [Benzinga, revisiones de analistas tras el 3T FY26](https://www.benzinga.com/analyst-stock-ratings/price-target/26/09/61739763/these-analysts-revise-their-forecasts-on-adobe-following-q3-results)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
