---
schema: "jmr-analisis-damodaran-v1"
ticker: "PYPL"
analysis_date: "2026-09-30"
---

# PayPal Holdings, Inc. (PYPL) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Escenarios e historias unificados:** A, B, C y D son los cuatro escenarios DCF activos. La cifra principal es el valor intrínseco esperado US$95,01; la historia central A vale US$110,08 y el rango es US$48,40–138,29. El MOS 35% se aplica al esperado: US$61,76. El antiguo caso Base de la hoja (US$105,85) se conserva solo como calibración técnica; no es el DCF de la historia central A. Los múltiplos y su mezcla son lecturas auxiliares con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos operativos fuera de la deuda, capital invertido operativo, conversor de i+d alineado al ltm, eps básico, flujos ltm, roic terminal (criterio damodaran) (11 celdas, con respaldo). Valor esperado US$91,54 → US$95,01. Salvedades abiertas: La API XBRL de la SEC solo publica hasta mar-2026 para PayPal: se conservaron los flujos LTM a jun-2026 de la hoja. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de US$105,85 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

PayPal es una red de pagos digitales de dos lados: 439 millones de cuentas activas, US$1,79 billones de volumen en 2025 y un botón de pago (checkout de marca) que durante veinte años fue sinónimo de pagar en línea. Ese botón, su negocio de mayor margen, crece solo ~2% sin divisas y pierde terreno frente a las billeteras integradas en el dispositivo o la plataforma (Apple Pay, Shop Pay, Google Pay); el volumen lo aportan Braintree (procesamiento de bajo margen) y Venmo, que todavía monetiza poco. Las finanzas son sólidas: flujo libre ajustado de US$6.400 millones en 2025 y recompras que bajaron las acciones de 1.172 millones (2020) a 920 millones. En 2026 llegó un nuevo CEO (Enrique Lores) y una reorganización. La historia de cinco años es si PayPal defiende el checkout y monetiza Venmo, o si se convierte en un procesador de bajo margen.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~4% anual cinco años | Sí | Sí: +4-7% en 2023-2025 | Probable |
| El checkout de marca vuelve a crecer ≥ 5% | Sí | Poco: ~2% sin divisas y en baja de participación | Baja-media |
| El margen operativo llega a 19,5% | Sí | Sí: 18,3% en 2025 por disciplina de costos y mezcla | Media |
| Venmo se vuelve un negocio rentable grande | Sí | Sí: creció a doble dígito en ingresos; parte de una base de ~US$3.000 millones | Media |


### Visión externa: tasas base

Con ventas LTM de US$34.128 millones (US$24.147 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **$12,000-25,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 3,3% y una mediana de 2,9% (desviación estándar 8,9%); sumando una inflación de 2,5%, la mediana nominal ronda 5,4%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| A · Se estabiliza con márgenes estables | 4,9% | 54% |
| B · El botón PayPal pierde frente a las billeteras nativas | 1,6% | 73% |
| C · Tesis de disrupción · Deterioro de los fundamentales | -1,1% | 83% |
| D · Reactivación: Fastlane, Venmo y publicidad | 6,8% | 40% |

En dólares de 2015 la empresa está en el tramo de US$12.000-25.000 millones: crecer 4,9% anual cinco años (historia A) lo logró ~54% de las empresas de ese tamaño; 6,8% (historia D), ~40%. La hoja (~3,6%) es modesta. El valor de PayPal depende de la mezcla (cuánto margen de checkout de marca conserva), no del crecimiento total.


### Piezas del valor

**Crecimiento.** Ingresos de US$29.771 millones (2023, +8,2%), US$31.797 millones (2024, +6,8%) y US$33.172 millones (2025, +4,3%); LTM US$34.128 millones. El 89,8% de los ingresos de 2025 fueron transacciones y el 10,2% otros servicios de valor agregado. La división de las historias entre checkout de marca, Braintree, Venmo y otros es una estimación propia: PayPal no publica ingresos por producto.

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 29.771 | 31.797 | 33.172 | 34.128 |
| Crecimiento | +8,2% | +6,8% | +4,3% | — |
| Margen operativo | 16,9% | 16,7% | 18,3% | 17,4% |
| FCFF (hoja) | 5.899 | 2.643 | 4.154 | — |

**Márgenes.** El margen operativo fue 16,7-18,3% y la hoja supone ~17,3% el próximo año y 19,5% de objetivo. La mezcla manda: cada punto que el checkout de marca pierde frente a Braintree baja el margen, porque Braintree cobra mucho menos por transacción. Las historias van de 13% a 22%.

**Reinversión y retorno.** Poco capital físico (capex de US$620-850 millones) y sales-to-capital de 2,6 en la hoja. El capital de trabajo incluye carteras de crédito (compra ahora y paga después) que PayPal vende a terceros. El flujo libre va a recompras: es la palanca principal del valor por acción. Ventaja que se desvanece: red de dos lados de comercios y usuarios, pero el checkout de marca pierde participación frente a Apple Pay y las billeteras nativas. El ROIC después del año 10 es 15,2%, el punto medio entre el costo de capital terminal (9,0%) y su ROIC actual (17,8%), porque Damodaran no publica un promedio útil para su industria.

**Riesgo.** La hoja usa una beta de 1,29. La bottom-up desapalancada de Financial Services (0,40 reapalancada) no sirve para una red de pagos con saldos de clientes y carteras de crédito; como en las financieras, se usa la beta del patrimonio del sector (0,97). El DCF técnico anterior sube de US$101,16 a US$107,30.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF técnico anterior por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,29 | 10,5% | 9,3% | US$105,85 |
| Bottom-up del sector (Financial Svcs. (Non-bank & Insurance), reapalancada) | 0,39 | 6,7% | 6,2% | US$125,28 |
| Propuesta (sector ajustado por riesgo propio) | 0,97 | 9,2% | 8,2% | US$112,33 |


### Calibración técnica anterior C/B/O (referencia auxiliar)

| Supuesto | Conservador | Base | Optimista |
|---|---:|---:|---:|
| Crecimiento año 1 | 2,0% | 4,0% | 5,2% |
| Crecimiento años 2–5 | 2,0% | 3,5% | 5,2% |
| Margen año 1 (base ajustada del modelo) | 17,3% | 17,3% | 17,3% |
| Margen objetivo | 17,3% | 19,5% | 23,9% |

Ventas/capital: 2,6x en años 1–5 y 2,6x en 6–10. WACC: 9,3%. Ke: 10,5%. Impuesto efectivo: 16,4%. Convergencia: 6 años. Estos parámetros son escenarios del analista, no cifras reportadas. Los casos Conservador, Base y Optimista de la hoja ya no son escenarios activos: sirven de calibración y de supuestos auxiliares de múltiplos. No confundir el antiguo Base con la historia A.


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF técnico anterior | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja que se desvanece | 21,3% | No disponible | 9,0% | 15,2% | US$105,85 | US$85,49 |

Fuentes de ventaja: Red de dos lados (comercios y usuarios) y marca en el checkout. Evidencia: ROIC 13-25% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor principal de US$95,01 se obtiene ejecutando cuatro DCF completos de diez años más valor terminal y ponderándolos por sus probabilidades. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. No se obtiene aplicando descuentos al antiguo Base de US$105,85 ni mezclando el DCF con múltiplos. La historia central A vale US$110,08; «central» y «esperado» son conceptos distintos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$34.128 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 14.500 + 11.000 + 3.300 + 5.328 = 34.128. |
| Margen inicial del DCF | 17,3% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 6 (Input sheet B31). |
| Impuesto | 16,39% en años 1–5; 25,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 9,26% → 9,05% | Tasa libre de riesgo 4,96%, beta 1,29, ERP 4,32%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 2,60x en años 1–5; 2,60x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | A/B/D: 4,96%; C: 0,00% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. C se estabiliza sin recuperarse: parte de su crecimiento del año 5 (-0,5%) y converge a 0,00% en el año 10 (piso de 0% nominal: el negocio residual deja de achicarse, lo que en términos reales sigue siendo contracción). Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | A/D: 15,20%; B/C: 9,05% (= WACC terminal) | Criterio de ventaja competitiva (ventaja que se desvanece). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 11.256; deuda 13.400; activos no operativos 4.009; acciones 855,5 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo A, año 1: 14.500 × 1,03 + 11.000 × 1,03 + 3.300 × 1,15 + 5.328 × 1,05 = US$35.654,40 millones. Frente a 34.128, el crecimiento consolidado es 4,47%. En los años 2–5 es 4,91%, 5,09%, 4,90%, 4,94%; las ventas del año 5 son US$43.272,80 millones. El 4,9% de la tabla es el crecimiento anual compuesto de los cinco años: (43.272,80 / 34.128)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En A, año 1: NOPAT = 35.654,40 × 17,28% × (1 − 16,39%) = US$5.149,82 millones. La reinversión es US$673,16 millones y el FCFF es US$4.476,65 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,05%. Reinversión terminal sobre el NOPAT: A, 32,6% (4,96% / 15,20%); B, 54,8% (4,96% / 9,05%); C, 0,0% (0,00% / 9,05%); D, 32,6% (4,96% / 15,20%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en «Escenarios e historias»: ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**A · Se estabiliza con márgenes estables** — probabilidad 45%; valor terminal 135.749 (VP 56.313); DCF US$110,08 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 35.654 | 4,5% | 17,3% | 5.150 | 673 | 4.477 | 9,3% | 4.097 |
| 2 | 37.405 | 4,9% | 17,9% | 5.582 | 732 | 4.850 | 9,3% | 4.063 |
| 3 | 39.309 | 5,1% | 18,1% | 5.961 | 741 | 5.220 | 9,3% | 4.002 |
| 4 | 41.236 | 4,9% | 18,4% | 6.352 | 783 | 5.569 | 9,3% | 3.908 |
| 5 | 43.273 | 4,9% | 18,7% | 6.770 | 823 | 5.947 | 9,3% | 3.820 |
| 6 | 45.412 | 4,9% | 19,0% | 7.066 | 864 | 6.201 | 9,2% | 3.646 |
| 7 | 47.659 | 4,9% | 19,0% | 7.259 | 908 | 6.351 | 9,2% | 3.421 |
| 8 | 50.019 | 5,0% | 19,0% | 7.455 | 953 | 6.502 | 9,1% | 3.209 |
| 9 | 52.498 | 5,0% | 19,0% | 7.653 | 1.001 | 6.651 | 9,1% | 3.009 |
| 10 | 55.102 | 5,0% | 19,0% | 7.852 | 1.051 | 6.801 | 9,1% | 2.821 |
| Terminal | 57.835 | 5,0% | 19,0% | 8.241 | 2.689 | 5.552 | 9,0% | — |

**B · El botón PayPal pierde frente a las billeteras nativas** — probabilidad 30%; valor terminal 60.993 (VP 25.302); DCF US$66,30 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 34.895 | 2,2% | 17,3% | 5.040 | 228 | 4.812 | 9,3% | 4.404 |
| 2 | 35.489 | 1,7% | 16,9% | 5.000 | 187 | 4.812 | 9,3% | 4.031 |
| 3 | 35.976 | 1,4% | 16,6% | 5.005 | 172 | 4.833 | 9,3% | 3.705 |
| 4 | 36.422 | 1,2% | 16,4% | 5.002 | 185 | 4.817 | 9,3% | 3.380 |
| 5 | 36.903 | 1,3% | 16,2% | 5.002 | 291 | 4.712 | 9,3% | 3.026 |
| 6 | 37.658 | 2,0% | 16,0% | 4.934 | 402 | 4.532 | 9,2% | 2.665 |
| 7 | 38.703 | 2,8% | 16,0% | 4.964 | 522 | 4.443 | 9,2% | 2.393 |
| 8 | 40.059 | 3,5% | 16,0% | 5.028 | 652 | 4.376 | 9,1% | 2.160 |
| 9 | 41.754 | 4,2% | 16,0% | 5.126 | 797 | 4.329 | 9,1% | 1.958 |
| 10 | 43.825 | 5,0% | 16,0% | 5.259 | 836 | 4.423 | 9,1% | 1.835 |
| Terminal | 45.999 | 5,0% | 16,0% | 5.520 | 3.025 | 2.495 | 9,0% | — |

**C · Tesis de disrupción · Deterioro de los fundamentales: Pierde el checkout y compite por precio** — probabilidad 10%; valor terminal 34.511 (VP 14.316); DCF US$48,40 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 33.858 | -0,8% | 17,3% | 4.890 | -204 | 5.094 | 9,3% | 4.662 |
| 2 | 33.328 | -1,6% | 15,9% | 4.417 | -187 | 4.604 | 9,3% | 3.856 |
| 3 | 32.842 | -1,5% | 15,1% | 4.157 | -122 | 4.278 | 9,3% | 3.280 |
| 4 | 32.525 | -1,0% | 14,4% | 3.923 | -63 | 3.986 | 9,3% | 2.797 |
| 5 | 32.360 | -0,5% | 13,7% | 3.710 | -51 | 3.761 | 9,3% | 2.415 |
| 6 | 32.229 | -0,4% | 13,0% | 3.431 | -38 | 3.469 | 9,2% | 2.040 |
| 7 | 32.131 | -0,3% | 13,0% | 3.349 | -25 | 3.374 | 9,2% | 1.817 |
| 8 | 32.065 | -0,2% | 13,0% | 3.270 | -13 | 3.282 | 9,1% | 1.620 |
| 9 | 32.033 | -0,1% | 13,0% | 3.195 | 0 | 3.195 | 9,1% | 1.445 |
| 10 | 32.033 | 0,0% | 13,0% | 3.123 | 0 | 3.123 | 9,1% | 1.296 |
| Terminal | 32.033 | 0,0% | 13,0% | 3.123 | 0 | 3.123 | 9,0% | — |

**D · Reactivación: Fastlane, Venmo y publicidad** — probabilidad 15%; valor terminal 176.680 (VP 73.293); DCF US$138,29 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 36.634 | 7,3% | 17,3% | 5.291 | 1.028 | 4.263 | 9,3% | 3.902 |
| 2 | 39.307 | 7,3% | 18,9% | 6.195 | 1.070 | 5.125 | 9,3% | 4.293 |
| 3 | 42.089 | 7,1% | 19,6% | 6.911 | 1.032 | 5.879 | 9,3% | 4.507 |
| 4 | 44.771 | 6,4% | 20,4% | 7.646 | 1.060 | 6.585 | 9,3% | 4.621 |
| 5 | 47.528 | 6,2% | 21,2% | 8.429 | 1.082 | 7.348 | 9,3% | 4.719 |
| 6 | 50.341 | 5,9% | 22,0% | 9.069 | 1.100 | 7.970 | 9,2% | 4.686 |
| 7 | 53.200 | 5,7% | 22,0% | 9.383 | 1.113 | 8.270 | 9,2% | 4.454 |
| 8 | 56.093 | 5,4% | 22,0% | 9.680 | 1.122 | 8.559 | 9,1% | 4.224 |
| 9 | 59.010 | 5,2% | 22,0% | 9.960 | 1.126 | 8.834 | 9,1% | 3.996 |
| 10 | 61.937 | 5,0% | 22,0% | 10.220 | 1.182 | 9.038 | 9,1% | 3.749 |
| Terminal | 65.009 | 5,0% | 22,0% | 10.726 | 3.500 | 7.226 | 9,0% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| A | 35.995,10 | 56.313,18 | 92.308,27 | 94.173,27 | 110,08 |
| B | 29.556,47 | 25.302,14 | 54.858,61 | 56.723,61 | 66,30 |
| C | 25.228,56 | 14.316,16 | 39.544,72 | 41.409,72 | 48,40 |
| D | 43.151,51 | 73.293,11 | 116.444,62 | 118.309,62 | 138,29 |

Ejemplo A: (35.995,10 + 56.313,18 + 11.256 + 4.009 − 13.400) / 855,5 = US$110,08 por acción. El terminal representa 61,0% del valor operativo de A: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. Valor esperado, probabilidades y margen de seguridad

Las probabilidades 45% / 30% / 10% / 15% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

Valor esperado = 0,45 × 110,079805 + 0,30 × 66,304630 + 0,10 × 48,404113 + 0,15 × 138,292947 = US$95,011654 ≈ US$95,01. Los aportes son US$49,54 + US$19,89 + US$4,84 + US$20,74 por acción.

Precio con MOS = valor esperado × (1 − 35%) = 95,011654 × 0,65 = US$61,757575 ≈ US$61,76. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. No se aplica al antiguo Base ni a la historia central A.

Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; central H11; rango H12:H13; MOS H14. Los DCF completos empiezan en las filas 22 (A), 46 (B), 70 (C) y 94 (D); sus valores por acción están en B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: base, conservadora, disrupción y optimista

Estas etiquetas describen las historias A–D activas. La tesis base es A, con un DCF de US$110,08; el valor esperado de US$95,01 combina las cuatro tesis con sus probabilidades. La antigua calibración C/B/O de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### A · Tesis base: Se estabiliza con márgenes estables

**Qué plantea.** Es la estabilización con Lores: crecimiento de un dígito medio y margen de ~19%.

**Traducción al modelo.** Checkout de marca crece 3%, 3%, 4%, 4%, 4%; Procesamiento no de marca (Braintree) crece 3%, 4%, 4%, 4%, 4%; Venmo y P2P crece 15%, 15%, 12%, 10%, 10%; Otros servicios de valor agregado crece 5%, 5%, 5%, 5%, 5%. El crecimiento anual compuesto de cinco años es 4,9%; el margen operativo objetivo es 19,0%. El ROIC terminal es 15,2%. El crecimiento terminal es 4,96%, el de la hoja. Probabilidad: 45%; DCF: US$110,08 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (checkout de marca (TPV sin divisas): ~+2%; margen de transacción (US$): Creciendo; ingresos de Venmo: Doble dígito). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### B · Tesis conservadora: El botón PayPal pierde frente a las billeteras nativas

**Qué plantea.** Es la pérdida continua del checkout de marca.

**Traducción al modelo.** Checkout de marca crece 0%, -1%, -2%, -2%, -2%; Procesamiento no de marca (Braintree) crece 3%, 3%, 3%, 3%, 3%; Venmo y P2P crece 10%, 8%, 8%, 6%, 6%; Otros servicios de valor agregado crece 2%, 2%, 2%, 2%, 2%. El crecimiento anual compuesto de cinco años es 1,6%; el margen operativo objetivo es 16,0%. El ROIC terminal es el costo de capital (9,05%). El crecimiento terminal es 4,96%, el de la hoja. Probabilidad: 30%; DCF: US$66,30 por acción.

**Cómo contrastarla.** La apoyarían: checkout de marca (TPV sin divisas): ≤ 0%; margen de transacción (US$): en caída; ingresos de Venmo: < +8%; margen operativo: ≤ 16%.


#### C · Tesis de disrupción · Deterioro de los fundamentales: Pierde el checkout y compite por precio

**Qué plantea.** Es PayPal convertido en procesador de bajo margen.

**Traducción al modelo.** Checkout de marca crece -3%, -5%, -5%, -4%, -3%; Procesamiento no de marca (Braintree) crece 0%, 0%, 0%, 0%, 0%; Venmo y P2P crece 5%, 5%, 5%, 5%, 5%; Otros servicios de valor agregado crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es -1,1%; el margen operativo objetivo es 13,0%. El ROIC terminal es el costo de capital (9,05%). El crecimiento terminal es 0,00%: los años 6–10 pasan de -0,5% a ese nivel, sin recuperación. Probabilidad: 10%; DCF: US$48,40 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que B: checkout de marca (TPV sin divisas): ≤ 0%; margen de transacción (US$): en caída; ingresos de Venmo: < +8%; margen operativo: ≤ 16%.


#### D · Tesis optimista: Reactivación: Fastlane, Venmo y publicidad

**Qué plantea.** Es una reactivación (Fastlane, Venmo en comercios, publicidad).

**Traducción al modelo.** Checkout de marca crece 6%, 6%, 6%, 5%, 5%; Procesamiento no de marca (Braintree) crece 5%, 5%, 5%, 5%, 5%; Venmo y P2P crece 20%, 18%, 15%, 12%, 10%; Otros servicios de valor agregado crece 8%, 8%, 8%, 8%, 8%. El crecimiento anual compuesto de cinco años es 6,8%; el margen operativo objetivo es 22,0%. El ROIC terminal es 15,2%. El crecimiento terminal es 4,96%, el de la hoja. Probabilidad: 15%; DCF: US$138,29 por acción.

**Cómo contrastarla.** La confirmarían: checkout de marca (TPV sin divisas): ≥ +5%; margen de transacción (US$): ≥ +4%; ingresos de Venmo: ≥ +15%; margen operativo: ≥ 19%.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: A/B/D: 4,96%; C: 0,00%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas y valor esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,29) | Valor/acción (beta 0,97) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| **A · Se estabiliza con márgenes estables** | 45% | Checkout de marca: 3%, 3%, 4%, 4%, 4%; Procesamiento no de marca (Braintree): 3%, 4%, 4%, 4%, 4%; Venmo y P2P: 15%, 15%, 12%, 10%, 10%; Otros servicios de valor agregado: 5%, 5%, 5%, 5%, 5% | 4,9% | 19% | 2,6 | 15,2% | 4,96% | US$110,08 | US$116,89 |
| **B · El botón PayPal pierde frente a las billeteras nativas** | 30% | Checkout de marca: 0%, -1%, -2%, -2%, -2%; Procesamiento no de marca (Braintree): 3%, 3%, 3%, 3%, 3%; Venmo y P2P: 10%, 8%, 8%, 6%, 6%; Otros servicios de valor agregado: 2%, 2%, 2%, 2%, 2% | 1,6% | 16% | 2,6 | = costo de capital | 4,96% | US$66,30 | US$69,97 |
| **C · Tesis de disrupción · Deterioro de los fundamentales: Pierde el checkout y compite por precio** | 10% | Checkout de marca: -3%, -5%, -5%, -4%, -3%; Procesamiento no de marca (Braintree): 0%, 0%, 0%, 0%, 0%; Venmo y P2P: 5%, 5%, 5%, 5%, 5%; Otros servicios de valor agregado: 0%, 0%, 0%, 0%, 0% | -1,1% | 13% | 2,6 | = costo de capital | 0,00% | US$48,40 | US$50,83 |
| **D · Reactivación: Fastlane, Venmo y publicidad** | 15% | Checkout de marca: 6%, 6%, 6%, 5%, 5%; Procesamiento no de marca (Braintree): 5%, 5%, 5%, 5%, 5%; Venmo y P2P: 20%, 18%, 15%, 12%, 10%; Otros servicios de valor agregado: 8%, 8%, 8%, 8%, 8% | 6,8% | 22% | 2,6 | 15,2% | 4,96% | US$138,29 | US$147,06 |
| **Valor esperado** | 100% |  |  |  |  |  |  | **US$95,01** | **US$100,73** |

A (45%) es la estabilización con Lores: crecimiento de un dígito medio y margen de ~19%. B (30%) es la pérdida continua del checkout de marca. C (10%) es PayPal convertido en procesador de bajo margen. D (15%) es una reactivación (Fastlane, Venmo en comercios, publicidad). En las historias de erosión (B y C) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF técnico anterior (beta 1,29; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF técnico anterior de la hoja.

| Crecimiento \ Margen | 15,5% | 17,5% | 19,5% | 21,5% | 23,5% |
|---|---:|---:|---:|---:|---:|
| -0,4% | 71,92 | 79,47 | 87,01 | 94,56 | 102,10 |
| 1,6% | 78,80 | 87,37 | 95,94 | 104,52 | 113,09 |
| 3,6% | 86,43 | 96,15 | 105,87 | 115,60 | 125,32 |
| 5,6% | 94,89 | 105,90 | 116,91 | 127,92 | 138,93 |
| 7,6% | 104,27 | 116,72 | 129,16 | 141,61 | 154,05 |


### Pre-mortem

1. Apple Pay, Shop Pay y los checkouts de plataforma siguen quitando participación al botón PayPal.
2. Braintree renegocia con grandes comercios y el volumen crece sin margen.
3. La reorganización y el cambio de CEO distraen y retrasan productos.
4. Pérdidas de crédito en «compra ahora y paga después» en una recesión.
5. Regulación (tarifas, competencia de billeteras) limita la monetización de Venmo.

**Evidencia en contra de la historia más probable:** el checkout de marca crece ~2% y pierde tasa de captura desde hace varios años; sin evidencia de reactivación, B pesa casi tanto como A.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Checkout de marca (TPV sin divisas) | ~+2% | ≥ +5% | ≤ 0% |
| Margen de transacción (US$) | Creciendo | ≥ +4% | En caída |
| Ingresos de Venmo | Doble dígito | ≥ +15% | < +8% |
| Margen operativo | ~18% | ≥ 19% | ≤ 16% |
| Recompras / acciones en circulación | En baja | −5% anual | Se detienen |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$52,68**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 15% | Margen 18% | Margen 20% |
|---|---:|---:|---:|
| Beta 1,29 | -6,9% (95% de las empresas) | -9,4% (96% de las empresas) | ninguno entre −10% y 60% |
| Beta 0,97 | -8,1% (96% de las empresas) | ninguno entre −10% y 60% | ninguno entre −10% y 60% |

Frente al valor esperado de las historias (US$95,01 con la beta de la hoja; US$100,73 con la propuesta), el precio está por debajo en 45% y por debajo en 48%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Red de pagos rentable cuyo botón de marca pierde frente a las billeteras nativas |  |
| Probabilidades | A 45% / B 30% / C 10% / D 15% |  |
| Valor esperado (valor principal) (beta de la hoja / propuesta) | US$95,01 / US$100,73 |  |
| DCF base hoy (historia A) | US$110,08 |  |
| Precio con MOS sobre el valor esperado | US$61,76 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$48,40 a US$147,06 |  |
| Confianza | Media: finanzas sólidas; la mezcla de ingresos es la incógnita |  |
| Qué cambiaría la opinión | Crecimiento del checkout de marca y margen de transacción |  |
| Revisión | Resultados del 3T26 (oct-2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [PayPal, resultados del 4T y año 2025](https://newsroom.paypal-corp.com/2026-02-03-PayPal-Reports-Fourth-Quarter-and-Full-Year-2025-Results)
- [PayPal, Form 10-K 2025](https://www.sec.gov/Archives/edgar/data/1633917/000163391726000024/pypl-20251231.htm)
- [PayPal, nombramiento de Enrique Lores como CEO](https://newsroom.paypal-corp.com/2026-02-03-PayPal-Appoints-Enrique-Lores-as-Chief-Executive-Officer-and-David-W-Dorman-as-Independent-Board-Chair)
- [PayPal, reorganización estratégica (abr-2026)](https://newsroom.paypal-corp.com/2026-04-29-PayPal-Announces-Strategic-Reorganization-to-Accelerate-Growth)
- [Yahoo Finance, resultados del 2T 2026](https://finance.yahoo.com/markets/stocks/articles/paypal-holdings-inc-pypl-q2-190110631.html)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
