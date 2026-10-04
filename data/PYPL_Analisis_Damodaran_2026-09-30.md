---
schema: "jmr-analisis-damodaran-v1"
ticker: "PYPL"
analysis_date: "2026-09-30"
---

# PayPal Holdings, Inc. (PYPL) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$109,90 por acción** (Base · Se estabiliza con márgenes estables).

**Complemento · DCF esperado por probabilidades: US$94,91.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$48,34–138,07. El MOS 35% se aplica al esperado: US$61,69. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), capital invertido operativo, conversor de i+d alineado al ltm, deuda de balance sin arrendamientos operativos, eps básico, flujos ltm, roic terminal (criterio damodaran) (22 celdas, con respaldo). DCF esperado US$91,54 → US$97,97. Salvedades abiertas: La API XBRL de la SEC solo publica hasta mar-2026 para PayPal: se conservaron los flujos LTM a jun-2026 de la hoja. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (bloque Base de 'Valuation output': US$109,90 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja calcula estos cuatro DCF en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


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
| Base · Se estabiliza con márgenes estables | 4,9% | 54% |
| Conservadora · El botón PayPal pierde frente a las billeteras nativas | 1,6% | 73% |
| Disrupción · Deterioro de los fundamentales: Pierde el checkout y compite por precio | −1,1% | 83% |
| Optimista · Reactivación: Fastlane, Venmo y publicidad | 6,8% | 40% |

En dólares de 2015 la empresa está en el tramo de US$12.000-25.000 millones: crecer 4,9% anual cinco años (Base) lo logró ~54% de las empresas de ese tamaño; 6,8% (Optimista), ~40%. La hoja (~3,6%) es modesta. El valor de PayPal depende de la mezcla (cuánto margen de checkout de marca conserva), no del crecimiento total.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: el botón crece poco; Venmo, más.** PayPal es una red de pagos de dos lados: 439 millones de cuentas y US$1,79 billones de volumen en 2025. Su negocio de mayor margen, el botón de pago (checkout de marca), crece solo ~2% sin divisas y pierde terreno frente a las billeteras integradas en el dispositivo (Apple Pay, Shop Pay, Google Pay); el volumen lo aportan Braintree, procesamiento de bajo margen, y Venmo, que todavía monetiza poco. La Base supone que el checkout de marca y Braintree crecen 3-4%, Venmo 10-15% y los servicios de valor agregado 5%: 4,5% el primer año y 4,9% compuesto, algo que lograron ~54% de las empresas de su tamaño. Es la estabilización con el nuevo CEO (Enrique Lores, 2026). La Conservadora (1,6%) es la pérdida continua del checkout; la Disrupción (−1,1%), PayPal convertido en procesador de bajo margen; la Optimista (6,8%), una reactivación con Fastlane, Venmo en comercios y publicidad. Si el checkout de marca deja de crecer, la Base se cae.

**Margen: la mezcla manda.** El margen operativo fue 16,7-18,3% y la Base supone 19,2% (con el I+D capitalizado y los arrendamientos como deuda). Lo que mueve el margen es la mezcla: cada punto que el checkout de marca cede a Braintree lo baja, porque Braintree cobra mucho menos por transacción. Por eso la Conservadora usa 16,2% y la Disrupción 13,2%, mientras la Optimista llega a 22,2%. Dos puntos de margen mueven la Base a US$99,38 (−10%) o US$120,43 (+10%). Un margen operativo de 16% o menos invalidaría la Base.

**Reinversión: el flujo libre va a recompras.** PayPal necesita poco capital físico (capex de US$620-850 millones) y la hoja usa un ventas/capital de 2,48×. El capital de trabajo incluye carteras de crédito de «compra ahora y paga después», que PayPal vende a terceros. El flujo libre (US$6.400 millones ajustado en 2025) va a recompras, que bajaron las acciones de 1.172 millones en 2020 a ~855,5 millones: es la palanca principal del valor por acción, pero no se modela hacia adelante. La red de dos lados es una ventaja que se desvanece, así que el ROIC después del año 10 es 15,0%, el punto medio entre el costo de capital y su ROIC actual (Damodaran no publica un promedio útil para su industria). Sin ventaja, la Base valdría US$88,46 (−20%).

**Descuento.** La hoja usa una beta de 0,97. La bottom-up desapalancada de servicios financieros no sirve para una red de pagos con saldos de clientes y carteras de crédito; como en las financieras, la referencia sectorial es la beta del patrimonio (~0,97), con la que el DCF técnico sube. La Base, con la beta de la hoja, queda del lado prudente. El costo de capital va de 8,87% a 9,38%; un punto menos lleva la Base a US$141,65 (+29%). El crecimiento perpetuo es 5,29% y el terminal explica 60,6% del valor operativo.

**Probabilidades y lectura del resultado.** La Base pesa 45%, la Conservadora 30% —casi tanto, porque el checkout de marca pierde captura desde hace años sin señales de reactivación—, la Disrupción 10% y la Optimista 15%. El DCF Base es US$109,90 y el esperado US$94,91, frente a un precio de US$52,80: el mercado paga algo cercano a la Disrupción (US$48,34). O el mercado ve a PayPal como un procesador de bajo margen, o descuenta un riesgo que las historias no capturan. Como en INTU y LULU, esa distancia merece una explicación antes de cualquier decisión.

**Vida útil de I+D.** La hoja capitaliza el I+D (US$3.247 millones en el último año) y lo amortiza en 3 años. Mecanismo: el I+D crea activos que rinden varios años; capitalizarlo mueve el gasto del EBIT al capital invertido. La vida elegida es una convención del modelo (tabla de Damodaran por sector), no un dato reportado: una vida más larga eleva el activo y reduce el ROIC medido; una más corta hace lo contrario, y cambia también el EBIT ajustado. No se recalcula aquí porque modifica la hoja de conversión, no un input del DCF; queda provisional hasta contrastarla con la duración de los beneficios de los productos.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$34.128 millones. Con el crecimiento de la Base llegan a US$43.273 millones en el año 5 y a US$55.623 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 17,4% en el año 1 a 19,2% al final, y se descuentan impuestos (16,4% al principio y 25,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$5.201 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$707 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$4.494 millones el primer año. Cada flujo se trae a hoy con el costo de capital (8,87% al principio, 9,38% al final): los diez años suman US$36.583 millones. Después del año 10 se supone que la empresa crece 5,29% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 15,0%; esa perpetuidad vale hoy US$56.187 millones, 61% del total. Flujos más terminal dan el valor de las operaciones, US$92.769 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$11.256 millones, más activos no operativos por US$4.009 millones, menos deuda por US$14.013 millones (incluye los arrendamientos capitalizados). Queda un patrimonio de US$94.021 millones que, repartido entre 855,5 millones de acciones, da US$109,90 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 13,70× (peso 33% dentro de los múltiplos); EV/FCFF 19,31× (peso 17% dentro de los múltiplos); P/E 18,57× (peso 33% dentro de los múltiplos); P/FCFE 18,19× (peso 8% dentro de los múltiplos); P/OCF 15,48× (peso 8% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (9,3%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$109,90; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$99,38 | −9,6% |
| Margen objetivo +2 pp | US$120,43 | +9,6% |
| Crecimiento años 1–5 −2 pp | US$99,64 | −9,3% |
| Crecimiento años 1–5 +2 pp | US$121,29 | +10,4% |
| Ventas/capital −20% | US$108,23 | −1,5% |
| Ventas/capital +20% | US$111,02 | +1,0% |
| WACC +1 pp | US$90,43 | −17,7% |
| WACC −1 pp | US$141,65 | +28,9% |
| Crecimiento terminal −0,5 pp | US$104,72 | −4,7% |
| Crecimiento terminal +0,5 pp | US$116,44 | +5,9% |
| ROIC terminal = costo de capital | US$88,46 | −19,5% |
| Acciones +5% | US$104,67 | −4,8% |


### Piezas del valor

**Crecimiento.** Ingresos de US$29.771 millones (2023, +8,2%), US$31.797 millones (2024, +6,8%) y US$33.172 millones (2025, +4,3%); LTM US$34.128 millones. El 89,8% de los ingresos de 2025 fueron transacciones y el 10,2% otros servicios de valor agregado. La división de las historias entre checkout de marca, Braintree, Venmo y otros es una estimación propia: PayPal no publica ingresos por producto.

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 29.771 | 31.797 | 33.172 | 34.128 |
| Crecimiento | +8,2% | +6,8% | +4,3% | — |
| Margen operativo | 16,9% | 16,7% | 18,3% | 17,4% |
| FCFF (hoja) | 5.899 | 2.643 | 4.154 | — |

**Márgenes.** El margen operativo fue 16,7-18,3% y la hoja supone ~17,3% el próximo año y 19,5% de objetivo. La mezcla manda: cada punto que el checkout de marca pierde frente a Braintree baja el margen, porque Braintree cobra mucho menos por transacción. Las historias van de 13% a 22%.

**Reinversión y retorno.** Poco capital físico (capex de US$620-850 millones) y sales-to-capital de 2,6 en la hoja. El capital de trabajo incluye carteras de crédito (compra ahora y paga después) que PayPal vende a terceros. El flujo libre va a recompras: es la palanca principal del valor por acción. Ventaja que se desvanece: red de dos lados de comercios y usuarios, pero el checkout de marca pierde participación frente a Apple Pay y las billeteras nativas. El ROIC después del año 10 es 15,0%, el punto medio entre el costo de capital terminal (9,0%) y su ROIC actual (17,8%), porque Damodaran no publica un promedio útil para su industria.

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$619 millones, compromisos del 10-Q al 2026-03-31) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$58 millones, +0,17 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,02 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usa una beta de 0,97 (desde el 3-oct-2026; antes 1,29). Regla de la cartera (prompt v4, paso 2): beta del patrimonio del sector (0,97) = 0,97. La de regresión queda como referencia. Red de pagos con saldos de clientes y crédito: se parte de la beta del patrimonio del sector (0,97). El efecto de cada beta en el DCF Base está en la tabla.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 0,97 | 10,0% | 8,9% | US$109,70 |
| Bottom-up del sector (Financial Svcs. (Non-bank & Insurance), reapalancada) | 0,40 | 7,2% | 6,7% | US$123,94 |


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja que se desvanece | 20,9% | No disponible | 9,4% | 15,0% | US$109,90 | US$88,32 |

Fuentes de ventaja: Red de dos lados (comercios y usuarios) y marca en el checkout. Evidencia: ROIC 13-25% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$109,90 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$94,91. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$34.128 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 14.500 + 11.000 + 3.300 + 5.328 = 34.128. |
| Margen inicial del DCF | 17,4% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 6 (Input sheet B31). |
| Impuesto | 16,39% en años 1–5; 25,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 8,87% → 9,38% | Tasa libre de riesgo 5,29%, beta 0,97, ERP 4,87%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 2,48x en años 1–5; 2,48x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 5,29%; Disrupción: 0,00% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: parte de su crecimiento del año 5 (−0,5%) y converge a 0,00% en el año 10 (piso de 0% nominal: el negocio residual deja de achicarse, lo que en términos reales sigue siendo contracción). Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Optimista: 15,00%; Conservadora/Disrupción: 9,38% (= WACC terminal) | Criterio de ventaja competitiva (ventaja que se desvanece). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 11.256; deuda 14.013; activos no operativos 4.009; acciones 855,5 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 14.500 × 1,03 + 11.000 × 1,03 + 3.300 × 1,15 + 5.328 × 1,05 = US$35.654,40 millones. Frente a 34.128, el crecimiento consolidado es 4,47%. En los años 2–5 es 4,91%, 5,09%, 4,90%, 4,94%; las ventas del año 5 son US$43.272,80 millones. El 4,9% de la tabla es el crecimiento anual compuesto de los cinco años: (43.272,80 / 34.128)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 35.654,40 × 17,45% × (1 − 16,39%) = US$5.201,16 millones. La reinversión es US$707,10 millones y el FCFF es US$4.494,05 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,38%. Reinversión terminal sobre el NOPAT: Base, 35,3% (5,29% / 15,00%); Conservadora, 56,4% (5,29% / 9,38%); Disrupción, 0,0% (0,00% / 9,38%); Optimista, 35,3% (5,29% / 15,00%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · Se estabiliza con márgenes estables** — probabilidad 45%; valor terminal 133.265 (VP 56.187); DCF US$109,90 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 35.654 | 4,5% | 17,4% | 5.201 | 707 | 4.494 | 8,9% | 4.128 |
| 2 | 37.405 | 4,9% | 18,0% | 5.636 | 769 | 4.867 | 8,9% | 4.106 |
| 3 | 39.309 | 5,1% | 18,3% | 6.017 | 779 | 5.239 | 8,9% | 4.060 |
| 4 | 41.236 | 4,9% | 18,6% | 6.411 | 823 | 5.588 | 8,9% | 3.978 |
| 5 | 43.273 | 4,9% | 18,9% | 6.832 | 876 | 5.956 | 8,9% | 3.895 |
| 6 | 45.441 | 5,0% | 19,2% | 7.133 | 933 | 6.200 | 9,0% | 3.721 |
| 7 | 47.749 | 5,1% | 19,2% | 7.338 | 993 | 6.344 | 9,1% | 3.491 |
| 8 | 50.208 | 5,1% | 19,2% | 7.550 | 1.059 | 6.491 | 9,2% | 3.271 |
| 9 | 52.828 | 5,2% | 19,2% | 7.770 | 1.129 | 6.641 | 9,3% | 3.062 |
| 10 | 55.623 | 5,3% | 19,2% | 7.997 | 1.189 | 6.808 | 9,4% | 2.870 |
| Terminal | 58.566 | 5,3% | 19,2% | 8.420 | 2.969 | 5.451 | 9,4% | — |

**Conservadora · El botón PayPal pierde frente a las billeteras nativas** — probabilidad 30%; valor terminal 60.228 (VP 25.393); DCF US$66,35 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 34.895 | 2,2% | 17,4% | 5.090 | 240 | 4.850 | 8,9% | 4.455 |
| 2 | 35.489 | 1,7% | 17,0% | 5.051 | 197 | 4.854 | 8,9% | 4.095 |
| 3 | 35.976 | 1,4% | 16,8% | 5.056 | 180 | 4.876 | 8,9% | 3.779 |
| 4 | 36.422 | 1,2% | 16,6% | 5.054 | 194 | 4.860 | 8,9% | 3.460 |
| 5 | 36.903 | 1,3% | 16,4% | 5.055 | 315 | 4.740 | 8,9% | 3.099 |
| 6 | 37.682 | 2,1% | 16,2% | 4.989 | 443 | 4.547 | 9,0% | 2.729 |
| 7 | 38.778 | 2,9% | 16,2% | 5.027 | 580 | 4.447 | 9,1% | 2.446 |
| 8 | 40.213 | 3,7% | 16,2% | 5.101 | 730 | 4.370 | 9,2% | 2.202 |
| 9 | 42.021 | 4,5% | 16,2% | 5.213 | 898 | 4.315 | 9,3% | 1.990 |
| 10 | 44.244 | 5,3% | 16,2% | 5.366 | 946 | 4.420 | 9,4% | 1.864 |
| Terminal | 46.585 | 5,3% | 16,2% | 5.649 | 3.186 | 2.463 | 9,4% | — |

**Disrupción · Deterioro de los fundamentales: Pierde el checkout y compite por precio** — probabilidad 10%; valor terminal 33.730 (VP 14.221); DCF US$48,34 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 33.858 | −0,8% | 17,4% | 4.939 | -214 | 5.153 | 8,9% | 4.734 |
| 2 | 33.328 | −1,6% | 16,0% | 4.464 | -196 | 4.661 | 8,9% | 3.933 |
| 3 | 32.842 | −1,5% | 15,3% | 4.204 | -128 | 4.331 | 8,9% | 3.357 |
| 4 | 32.525 | −1,0% | 14,6% | 3.969 | -67 | 4.036 | 8,9% | 2.873 |
| 5 | 32.360 | −0,5% | 13,9% | 3.756 | -53 | 3.809 | 8,9% | 2.491 |
| 6 | 32.229 | −0,4% | 13,2% | 3.476 | -40 | 3.515 | 9,0% | 2.109 |
| 7 | 32.131 | −0,3% | 13,2% | 3.392 | -26 | 3.418 | 9,1% | 1.881 |
| 8 | 32.065 | −0,2% | 13,2% | 3.313 | -13 | 3.326 | 9,2% | 1.676 |
| 9 | 32.033 | −0,1% | 13,2% | 3.237 | 0 | 3.237 | 9,3% | 1.493 |
| 10 | 32.033 | 0,0% | 13,2% | 3.164 | 0 | 3.164 | 9,4% | 1.334 |
| Terminal | 32.033 | 0,0% | 13,2% | 3.164 | 0 | 3.164 | 9,4% | — |

**Optimista · Reactivación: Fastlane, Venmo y publicidad** — probabilidad 15%; valor terminal 173.234 (VP 73.038); DCF US$138,07 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 36.634 | 7,3% | 17,4% | 5.344 | 1.080 | 4.264 | 8,9% | 3.917 |
| 2 | 39.307 | 7,3% | 19,0% | 6.251 | 1.124 | 5.127 | 8,9% | 4.326 |
| 3 | 42.089 | 7,1% | 19,8% | 6.971 | 1.084 | 5.887 | 8,9% | 4.563 |
| 4 | 44.771 | 6,4% | 20,6% | 7.709 | 1.114 | 6.596 | 8,9% | 4.695 |
| 5 | 47.528 | 6,2% | 21,4% | 8.497 | 1.149 | 7.348 | 8,9% | 4.805 |
| 6 | 50.372 | 6,0% | 22,2% | 9.145 | 1.183 | 7.962 | 9,0% | 4.778 |
| 7 | 53.299 | 5,8% | 22,2% | 9.473 | 1.214 | 8.259 | 9,1% | 4.544 |
| 8 | 56.304 | 5,6% | 22,2% | 9.792 | 1.243 | 8.549 | 9,2% | 4.308 |
| 9 | 59.380 | 5,5% | 22,2% | 10.100 | 1.269 | 8.831 | 9,3% | 4.072 |
| 10 | 62.521 | 5,3% | 22,2% | 10.395 | 1.336 | 9.059 | 9,4% | 3.819 |
| Terminal | 65.828 | 5,3% | 22,2% | 10.945 | 3.860 | 7.085 | 9,4% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 36.582,60 | 56.186,55 | 92.769,15 | 94.020,81 | 109,90 |
| Conservadora | 30.118,83 | 25.392,82 | 55.511,66 | 56.763,32 | 66,35 |
| Disrupción | 25.879,74 | 14.221,18 | 40.100,92 | 41.352,58 | 48,34 |
| Optimista | 43.827,87 | 73.038,06 | 116.865,93 | 118.117,59 | 138,07 |

Ejemplo Base: (36.582,60 + 56.186,55 + 11.256 + 4.009 − 14.013) / 855,5 = US$109,90 por acción. El terminal representa 60,6% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 45% / 30% / 10% / 15% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,45 × 109,901593 + 0,30 × 66,351048 + 0,10 × 48,337324 + 0,15 × 138,068487 = US$94,905036 ≈ US$94,91. Los aportes son US$49,46 + US$19,91 + US$4,83 + US$20,71 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 94,905036 × 0,65 = US$61,688274 ≈ US$61,69. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$109,90, es el valor intrínseco principal. El DCF esperado de US$94,91 combina las cuatro tesis con sus probabilidades y se presenta como complemento. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: Se estabiliza con márgenes estables

**Qué plantea.** Es la estabilización con Lores: crecimiento de un dígito medio y margen de ~19%.

**Traducción al modelo.** Checkout de marca crece 3%, 3%, 4%, 4%, 4%; Procesamiento no de marca (Braintree) crece 3%, 4%, 4%, 4%, 4%; Venmo y P2P crece 15%, 15%, 12%, 10%, 10%; Otros servicios de valor agregado crece 5%, 5%, 5%, 5%, 5%. El crecimiento anual compuesto de cinco años es 4,9%; el margen operativo objetivo es 19,2%. El ROIC terminal es 15,0%. El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 45%; DCF: US$109,90 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (checkout de marca (TPV sin divisas): ~+2%; margen de transacción (US$): Creciendo; ingresos de Venmo: Doble dígito). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: El botón PayPal pierde frente a las billeteras nativas

**Qué plantea.** Es la pérdida continua del checkout de marca.

**Traducción al modelo.** Checkout de marca crece 0%, -1%, -2%, -2%, -2%; Procesamiento no de marca (Braintree) crece 3%, 3%, 3%, 3%, 3%; Venmo y P2P crece 10%, 8%, 8%, 6%, 6%; Otros servicios de valor agregado crece 2%, 2%, 2%, 2%, 2%. El crecimiento anual compuesto de cinco años es 1,6%; el margen operativo objetivo es 16,2%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 30%; DCF: US$66,35 por acción.

**Cómo contrastarla.** La apoyarían: checkout de marca (TPV sin divisas): ≤ 0%; margen de transacción (US$): en caída; ingresos de Venmo: < +8%; margen operativo: ≤ 16%.


#### Disrupción · Deterioro de los fundamentales: Pierde el checkout y compite por precio

**Qué plantea.** Es PayPal convertido en procesador de bajo margen.

**Traducción al modelo.** Checkout de marca crece -3%, -5%, -5%, -4%, -3%; Procesamiento no de marca (Braintree) crece 0%, 0%, 0%, 0%, 0%; Venmo y P2P crece 5%, 5%, 5%, 5%, 5%; Otros servicios de valor agregado crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es −1,1%; el margen operativo objetivo es 13,2%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 0,00%: los años 6–10 pasan de −0,5% a ese nivel, sin recuperación. Probabilidad: 10%; DCF: US$48,34 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: checkout de marca (TPV sin divisas): ≤ 0%; margen de transacción (US$): en caída; ingresos de Venmo: < +8%; margen operativo: ≤ 16%.


#### Optimista: Reactivación: Fastlane, Venmo y publicidad

**Qué plantea.** Es una reactivación (Fastlane, Venmo en comercios, publicidad).

**Traducción al modelo.** Checkout de marca crece 6%, 6%, 6%, 5%, 5%; Procesamiento no de marca (Braintree) crece 5%, 5%, 5%, 5%, 5%; Venmo y P2P crece 20%, 18%, 15%, 12%, 10%; Otros servicios de valor agregado crece 8%, 8%, 8%, 8%, 8%. El crecimiento anual compuesto de cinco años es 6,8%; el margen operativo objetivo es 22,2%. El ROIC terminal es 15,0%. El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 15%; DCF: US$138,07 por acción.

**Cómo contrastarla.** La confirmarían: checkout de marca (TPV sin divisas): ≥ +5%; margen de transacción (US$): ≥ +4%; ingresos de Venmo: ≥ +15%; margen operativo: ≥ 19%.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 5,29%; Disrupción: 0,00%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 0,97) | Valor/acción (beta 0,40) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| **Base · Se estabiliza con márgenes estables** | 45% | Checkout de marca: 3%, 3%, 4%, 4%, 4%; Procesamiento no de marca (Braintree): 3%, 4%, 4%, 4%, 4%; Venmo y P2P: 15%, 15%, 12%, 10%, 10%; Otros servicios de valor agregado: 5%, 5%, 5%, 5%, 5% | 4,9% | 19,2% | 2,5 | 15,0% | 5,29% | US$109,90 | US$124,18 |
| **Conservadora · El botón PayPal pierde frente a las billeteras nativas** | 30% | Checkout de marca: 0%, -1%, -2%, -2%, -2%; Procesamiento no de marca (Braintree): 3%, 3%, 3%, 3%, 3%; Venmo y P2P: 10%, 8%, 8%, 6%, 6%; Otros servicios de valor agregado: 2%, 2%, 2%, 2%, 2% | 1,6% | 16,2% | 2,5 | = costo de capital | 5,29% | US$66,35 | US$74,08 |
| **Disrupción · Deterioro de los fundamentales: Pierde el checkout y compite por precio** | 10% | Checkout de marca: -3%, -5%, -5%, -4%, -3%; Procesamiento no de marca (Braintree): 0%, 0%, 0%, 0%, 0%; Venmo y P2P: 5%, 5%, 5%, 5%, 5%; Otros servicios de valor agregado: 0%, 0%, 0%, 0%, 0% | −1,1% | 13,2% | 2,5 | = costo de capital | 0,00% | US$48,34 | US$53,44 |
| **Optimista · Reactivación: Fastlane, Venmo y publicidad** | 15% | Checkout de marca: 6%, 6%, 6%, 5%, 5%; Procesamiento no de marca (Braintree): 5%, 5%, 5%, 5%, 5%; Venmo y P2P: 20%, 18%, 15%, 12%, 10%; Otros servicios de valor agregado: 8%, 8%, 8%, 8%, 8% | 6,8% | 22,2% | 2,5 | 15,0% | 5,29% | US$138,07 | US$156,44 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  |  | **US$94,91** | **US$106,91** |

Base (45%) es la estabilización con Lores: crecimiento de un dígito medio y margen de ~19%. Conservadora (30%) es la pérdida continua del checkout de marca. Disrupción (10%) es PayPal convertido en procesador de bajo margen. Optimista (15%) es una reactivación (Fastlane, Venmo en comercios, publicidad). En las historias de erosión (Conservadora y Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 0,97; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.

| Crecimiento \ Margen | 15,7% | 17,7% | 19,7% | 21,7% | 23,7% |
|---|---:|---:|---:|---:|---:|
| 0,9% | 76,10 | 84,28 | 92,46 | 100,64 | 108,82 |
| 2,9% | 83,41 | 92,69 | 101,97 | 111,25 | 120,53 |
| 4,9% | 91,50 | 102,02 | 112,53 | 123,05 | 133,56 |
| 6,9% | 100,48 | 112,37 | 124,26 | 136,15 | 148,04 |
| 8,9% | 110,41 | 123,84 | 137,26 | 150,69 | 164,11 |


### Pre-mortem

1. Apple Pay, Shop Pay y los checkouts de plataforma siguen quitando participación al botón PayPal.
2. Braintree renegocia con grandes comercios y el volumen crece sin margen.
3. La reorganización y el cambio de CEO distraen y retrasan productos.
4. Pérdidas de crédito en «compra ahora y paga después» en una recesión.
5. Regulación (tarifas, competencia de billeteras) limita la monetización de Venmo.

**Evidencia en contra de la historia más probable:** el checkout de marca crece ~2% y pierde tasa de captura desde hace varios años; sin evidencia de reactivación, Conservadora pesa casi tanto como Base.


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

Precio de referencia de la valoración guardada: **US$52,80**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 15% | Margen 18% | Margen 20% |
|---|---:|---:|---:|
| Beta 0,97 | −6,9% (95% de las empresas) | −9,4% (96% de las empresas) | ninguno entre −10% y 60% |
| Beta 0,40 | −9,3% (96% de las empresas) | ninguno entre −10% y 60% | ninguno entre −10% y 60% |

Frente al DCF Base (US$109,90), el valor intrínseco principal, el precio está por debajo en 52%.

Frente al DCF esperado de las historias (US$94,91 con la beta de la hoja; US$106,91 con la propuesta), el precio está por debajo en 44% y por debajo en 51%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Red de pagos rentable cuyo botón de marca pierde frente a las billeteras nativas |  |
| Probabilidades | Base 45% / Conservadora 30% / Disrupción 10% / Optimista 15% |  |
| DCF Base hoy (valor intrínseco principal) | US$109,90 |  |
| DCF esperado por probabilidades (complemento) (beta de la hoja / propuesta) | US$94,91 / US$106,91 |  |
| Precio con MOS sobre el DCF esperado | US$61,69 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$48,34 a US$156,44 |  |
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
