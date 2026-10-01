---
schema: "jmr-analisis-damodaran-v1"
ticker: "INTU"
analysis_date: "2026-09-30"
---

# Intuit Inc. (INTU) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$512,91 por acción** (Base · La IA es palanca de monetización).

**Complemento · DCF esperado por probabilidades: US$443,09.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$208,71–631,38. El MOS 35% se aplica al esperado: US$288,01. El antiguo caso técnico de la hoja (US$499,36) se conserva solo como calibración; no es el DCF Base. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), capital invertido operativo, deuda de balance sin arrendamientos operativos, eps básico, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet, roic terminal (criterio damodaran) (23 celdas, con respaldo). DCF esperado US$440,79 → US$443,09. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de US$499,36 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

Intuit es el sistema financiero de la pequeña empresa y del contribuyente estadounidense: QuickBooks, nómina, pagos y Mailchimp para la pyme; TurboTax y Credit Karma para el consumidor. Cobra suscripciones, tarifas por declaración y comisiones, con márgenes de segmento de 73-77% y casi sin capital. En FY2026 (cerrado en julio) facturó US$21.448 millones (+14%), con Global Business Solutions +16% y el Online Ecosystem +19%. El mercado, sin embargo, bajó el múltiplo por miedo a que la IA generativa abarate la contabilidad básica y la preparación de impuestos. La historia de cinco años depende de si Intuit usa la IA para cobrar más a su base (servicios asistidos, mid-market, agentes) o si la IA y la declaración gratuita del Estado le quitan clientes en el extremo simple.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~9-10% anual cinco años | Sí | Sí: +13-16% anual en FY24-FY26 | Probable |
| La IA sustituye a TurboTax en declaraciones simples | Sí | Sí en el extremo gratuito; los asistidos (Live) crecen | Posible, parcial |
| QuickBooks sigue subiendo precio sin perder clientes | Sí | Sí: QBO Accounting +23% en FY26 por precio, clientes y mezcla | Probable |
| El margen GAAP llega a 32% | Sí | Sí: 22,3% → 27,4% en dos años; SBC de ~10% de los ingresos | Probable |


### Visión externa: tasas base

Con ventas LTM de US$21.448 millones (US$15.176 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **$12,000-25,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 3,3% y una mediana de 2,9% (desviación estándar 8,9%); sumando una inflación de 2,5%, la mediana nominal ronda 5,4%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · La IA es palanca de monetización | 9,8% | 26% |
| Conservadora · La IA erosiona impuestos y contabilidad básica | 4,9% | 54% |
| Disrupción · Deterioro de los fundamentales: Recesión y declaración gratuita del Estado | 2,5% | 69% |
| Optimista · Plataforma financiera de la pyme | 12,2% | 16% |

En dólares de 2015 la empresa está en el tramo de US$12.000-25.000 millones: crecer 9,8% anual cinco años (Base) lo logró ~26% de las empresas de ese tamaño; 12,2% (Optimista), ~16%. Intuit lleva años en ese grupo, pero la tasa base recuerda que pocas empresas sostienen doble dígito cuando ya facturan más de US$20.000 millones.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: la pyme crece a doble dígito; el consumidor, a un dígito.** Intuit es el sistema financiero de la pequeña empresa (QuickBooks, nómina, pagos, Mailchimp) y del contribuyente estadounidense (TurboTax, Credit Karma). En FY2026, cerrado en julio, facturó US$21.448 millones (+13,9%): Global Business Solutions +16% y QuickBooks Online +23%. La Base supone que la pyme crece de 14% a 10%, el consumidor de 7% a 5% y Credit Karma de 10% a 6%: 11,5% el primer año y 9,8% compuesto. Solo ~26% de las empresas de su tamaño lo lograron, pero Intuit lleva años en ese grupo y la Base ya supone que desacelera. El mercado bajó el múltiplo por miedo a que la IA abarate la contabilidad básica y la preparación de impuestos; esa es la Conservadora (4,9%), con el consumidor cayendo. La Disrupción (2,5%) combina recesión (Credit Karma) y la declaración gratuita del Estado; la Optimista (12,2%), Intuit como plataforma financiera completa de la pyme. Si las unidades de TurboTax caen en la temporada 2027, la Conservadora gana peso.

**Margen: el salto depende de la compensación en acciones.** El margen operativo GAAP subió de 22,3% a 27,4% en dos años. La Base supone ~32% (32,2% en el modelo) desde el próximo año, un salto rápido que exige que la compensación en acciones (US$2.056 millones, ~10% de los ingresos) crezca menos que las ventas. Los márgenes de segmento son de 73-77%, así que el espacio existe; la duda es si la empresa lo deja llegar al resultado o lo reinvierte en IA. El rango va de 26,2% a 35,2%; dos puntos mueven la Base a US$481,82 (−6%) o US$543,99 (+6%). Un margen GAAP de 26% o menos en FY27 invalidaría la Base.

**Reinversión: casi sin capital, con compras grandes.** El capex es mínimo (US$175 millones en FY26) frente a un flujo operativo de US$8.838 millones. La hoja usa un ventas/capital de 2,31× y 1,88× (~US$0,43 de capital por dólar de ventas nuevas), que incorpora que parte del crecimiento se compra: Credit Karma y Mailchimp costaron ~US$20.000 millones. El flujo libre va a recompras (US$5.412 millones) y dividendos. El ROIC, incluida la plusvalía de esas compras, siempre estuvo por encima del costo de capital (12-22%), y los costos de cambio son reales: una pyme no cambia de contabilidad con facilidad. Por eso la Base conserva un ROIC de 22,6% después del año 10, limitado al actual y por debajo del de la industria. Sin esa ventaja, la Base valdría US$361,81 (−29%).

**Descuento.** La hoja usa una beta de 1,20; la bottom-up de Software reapalancada da 1,34, y con ella el DCF técnico baja algo. Credit Karma añade ciclicidad (depende del crédito al consumidor), lo que apoya una beta algo mayor que la de la hoja; la Base, calculada con la de la hoja, queda del lado optimista en este punto. El costo de capital va de 9,83% a 9,00%; un punto más lleva la Base a US$410,10 (−20%). El crecimiento perpetuo es 4,99% y el terminal explica 68,3% del valor operativo.

**Probabilidades y lectura del resultado.** La Base pesa 45%, la Conservadora 25%, la Disrupción 10% y la Optimista 20%. El DCF Base es US$512,91 y el esperado US$443,09; el precio, US$274,77, está apenas por encima de la Conservadora (US$260,52): el mercado está descontando algo muy cercano a la sustitución por IA de esa historia, o una tasa mucho mayor. Esa distancia merece una explicación antes de cualquier decisión. La compensación en acciones (~10% de los ingresos) diluye, y no está modelada: las acciones se fijan en 267,2 millones.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$21.448 millones. Con el crecimiento de la Base llegan a US$34.271 millones en el año 5 y a US$46.556 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 32,0% en el año 1 a 32,2% al final, y se descuentan impuestos (24,1% al principio y 23,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$5.813 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$1.086 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$4.727 millones el primer año. Cada flujo se trae a hoy con el costo de capital (9,83% al principio, 9,00% al final): los diez años suman US$43.691 millones. Después del año 10 se supone que la empresa crece 4,99% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 22,6%; esa perpetuidad vale hoy US$94.291 millones, 68% del total. Flujos más terminal dan el valor de las operaciones, US$137.982 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$7.200 millones, más activos no operativos por US$248 millones, menos deuda por US$8.381 millones (incluye los arrendamientos capitalizados). Queda un patrimonio de US$137.049 millones que, repartido entre 267,2 millones de acciones, da US$512,91 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 16,99× (peso 25% dentro de los múltiplos); EV/FCFF 17,21× (peso 38% dentro de los múltiplos); P/E 20,30× (peso 12% dentro de los múltiplos); P/FCFE 15,43× (peso 12% dentro de los múltiplos); P/OCF 15,56× (peso 12% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (10,3%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$512,91; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$481,82 | −6,1% |
| Margen objetivo +2 pp | US$543,99 | +6,1% |
| Crecimiento años 1–5 −2 pp | US$460,49 | −10,2% |
| Crecimiento años 1–5 +2 pp | US$571,08 | +11,3% |
| Ventas/capital −20% | US$506,02 | −1,3% |
| Ventas/capital +20% | US$517,50 | +0,9% |
| WACC +1 pp | US$410,10 | −20,0% |
| WACC −1 pp | US$683,71 | +33,3% |
| Crecimiento terminal −0,5 pp | US$476,89 | −7,0% |
| Crecimiento terminal +0,5 pp | US$558,94 | +9,0% |
| ROIC terminal = costo de capital | US$361,81 | −29,5% |
| Acciones +5% | US$488,48 | −4,8% |


### Piezas del valor

**Crecimiento.** Ingresos de US$16.285 millones (FY24, +13,3%), US$18.831 millones (FY25, +15,6%) y US$21.448 millones (FY26, +13,9%). Global Business Solutions creció 16% y el Online Ecosystem 19%; QuickBooks Online Accounting, 23%. La división de las historias (GBS ~US$12.650 millones, Consumer ~US$6.000 millones, Credit Karma ~US$2.800 millones) es una estimación propia: desde agosto de 2025 Consumer, Credit Karma y ProTax se reportan juntos y desde agosto de 2026 Mailchimp va aparte.

| US$ millones | FY24 | FY25 | FY26 |
|---|---:|---:|---:|
| Ingresos | 16.285 | 18.831 | 21.448 |
| Crecimiento | +13,3% | +15,6% | +13,9% |
| Margen operativo GAAP | 22,3% | 26,1% | 27,4% |
| FCFF (hoja) | 2.974 | 3.936 | 4.950 |

**Márgenes.** El margen operativo GAAP subió de 22,3% a 27,4% en dos años; la hoja supone ~32% desde el próximo año, un salto rápido que exige que la compensación en acciones (US$2.056 millones, ~10% de los ingresos) crezca menos que las ventas. Las historias van de 26% (recesión y regulación) a 35% (plataforma financiera de la pyme).

**Reinversión y retorno.** Capex mínimo (US$175 millones en FY26) y flujo operativo de US$8.838 millones. La hoja usa un sales-to-capital de 2,5 y 2, que incorpora compras (Credit Karma y Mailchimp costaron ~US$20.000 millones). El flujo libre va a recompras (US$5.412 millones) y dividendos (US$1.347 millones). Ventaja durable: costos de cambio y datos del cliente en QuickBooks y TurboTax, con ROIC siempre por encima del costo de capital (12-22%). El ROIC después del año 10 es 22,6%, el promedio de su industria según Damodaran (29,3%), limitado a su ROIC actual. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$712 millones, compromisos del 10-K al 2026-07-31) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$40 millones, +0,19 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,03 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usa una beta de 1,20. La bottom-up de Software (System & Application) reapalancada con la deuda de Intuit da 1,34; el DCF técnico anterior baja de US$499,36 a US$482,93. Credit Karma añade ciclicidad (depende del crédito al consumidor), lo que apoya una beta algo mayor que la de la hoja.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF técnico anterior por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,20 | 10,3% | 9,8% | US$499,36 |
| Bottom-up del sector (Software (System & Application), reapalancada) | 1,34 | 11,0% | 10,4% | US$482,93 |


### Calibración técnica anterior Conservador/Base/Optimista (referencia auxiliar)

| Supuesto | Conservador | Base | Optimista |
|---|---:|---:|---:|
| Crecimiento año 1 | 6,0% | 9,1% | 14,0% |
| Crecimiento años 2–5 | 6,0% | 9,0% | 14,0% |
| Margen año 1 (base ajustada del modelo) | 32,0% | 32,0% | 32,0% |
| Margen objetivo | 28,2% | 32,2% | 36,2% |

Ventas/capital: 2,3x en años 1–5 y 1,9x en 6–10. WACC: 9,8%. Ke: 10,3%. Impuesto efectivo: 24,1%. Convergencia: 5 años. Estos parámetros son escenarios del analista, no cifras reportadas. Los casos Conservador, Base y Optimista de la hoja ya no son escenarios activos: sirven de calibración y de supuestos auxiliares de múltiplos. No confundir el antiguo caso técnico Base con la tesis Base.


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF técnico anterior | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 22,6% | 29,3% | 9,0% | 22,6% | US$499,36 | US$351,90 |

Fuentes de ventaja: Costos de cambio y datos del cliente (QuickBooks, TurboTax), escala en pyme. Evidencia: ROIC 12-22%, siempre por encima del costo de capital. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$512,91 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$443,09. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene aplicando descuentos al antiguo caso técnico de la hoja (US$499,36) ni mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$21.448 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 12.649 + 5.999 + 2.800 = 21.448. |
| Margen inicial del DCF | 32,0% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 24,12% en años 1–5; 23,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 9,83% → 9,00% | Tasa libre de riesgo 4,99%, beta 1,20, ERP 4,46%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 2,31x en años 1–5; 1,88x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 4,99%; Disrupción: 3,65% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (3,65%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Optimista: 22,60%; Conservadora/Disrupción: 9,00% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 7.200; deuda 8.381; activos no operativos 248; acciones 267,2 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 12.649 × 1,14 + 5.999 × 1,07 + 2.800 × 1,10 = US$23.918,77 millones. Frente a 21.448, el crecimiento consolidado es 11,52%. En los años 2–5 es 10,48%, 9,83%, 9,02%, 8,32%; las ventas del año 5 son US$34.271,34 millones. El 9,8% de la tabla es el crecimiento anual compuesto de los cinco años: (34.271,34 / 21.448)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 23.918,77 × 32,03% × (1 − 24,12%) = US$5.812,81 millones. La reinversión es US$1.085,64 millones y el FCFF es US$4.727,17 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,00%. Reinversión terminal sobre el NOPAT: Base, 22,1% (4,99% / 22,60%); Conservadora, 55,4% (4,99% / 9,00%); Disrupción, 40,6% (3,65% / 9,00%); Optimista, 22,1% (4,99% / 22,60%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en «Escenarios e historias»: ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · La IA es palanca de monetización** — probabilidad 45%; valor terminal 235.403 (VP 94.291); DCF US$512,91 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 23.919 | 11,5% | 32,0% | 5.813 | 1.086 | 4.727 | 9,8% | 4.304 |
| 2 | 26.425 | 10,5% | 32,1% | 6.435 | 1.125 | 5.310 | 9,8% | 4.402 |
| 3 | 29.021 | 9,8% | 32,1% | 7.074 | 1.134 | 5.940 | 9,8% | 4.484 |
| 4 | 31.638 | 9,0% | 32,2% | 7.720 | 1.141 | 6.579 | 9,8% | 4.522 |
| 5 | 34.271 | 8,3% | 32,2% | 8.370 | 1.137 | 7.234 | 9,8% | 4.527 |
| 6 | 36.895 | 7,7% | 32,2% | 9.038 | 1.375 | 7.663 | 9,7% | 4.372 |
| 7 | 39.474 | 7,0% | 32,2% | 9.698 | 1.331 | 8.367 | 9,5% | 4.360 |
| 8 | 41.969 | 6,3% | 32,2% | 10.341 | 1.266 | 9.076 | 9,3% | 4.326 |
| 9 | 44.343 | 5,7% | 32,2% | 10.958 | 1.180 | 9.779 | 9,2% | 4.269 |
| 10 | 46.556 | 5,0% | 32,2% | 11.539 | 1.239 | 10.300 | 9,0% | 4.126 |
| Terminal | 48.879 | 5,0% | 32,2% | 12.115 | 2.675 | 9.440 | 9,0% | — |

**Conservadora · La IA erosiona impuestos y contabilidad básica** — probabilidad 25%; valor terminal 88.973 (VP 35.638); DCF US$260,52 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 22.973 | 7,1% | 32,0% | 5.583 | 533 | 5.050 | 9,8% | 4.598 |
| 2 | 24.204 | 5,4% | 30,9% | 5.673 | 456 | 5.218 | 9,8% | 4.326 |
| 3 | 25.255 | 4,3% | 30,3% | 5.811 | 407 | 5.404 | 9,8% | 4.079 |
| 4 | 26.195 | 3,7% | 29,8% | 5.915 | 435 | 5.480 | 9,8% | 3.766 |
| 5 | 27.199 | 3,8% | 29,2% | 6.024 | 479 | 5.545 | 9,8% | 3.470 |
| 6 | 28.304 | 4,1% | 29,2% | 6.287 | 648 | 5.639 | 9,7% | 3.218 |
| 7 | 29.519 | 4,3% | 29,2% | 6.576 | 712 | 5.864 | 9,5% | 3.056 |
| 8 | 30.855 | 4,5% | 29,2% | 6.894 | 783 | 6.111 | 9,3% | 2.913 |
| 9 | 32.323 | 4,8% | 29,2% | 7.243 | 860 | 6.383 | 9,2% | 2.787 |
| 10 | 33.936 | 5,0% | 29,2% | 7.627 | 903 | 6.724 | 9,0% | 2.693 |
| Terminal | 35.629 | 5,0% | 29,2% | 8.008 | 4.440 | 3.568 | 9,0% | — |

**Disrupción · Deterioro de los fundamentales: Recesión y declaración gratuita del Estado** — probabilidad 10%; valor terminal 67.533 (VP 27.050); DCF US$208,71 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 21.747 | 1,4% | 32,0% | 5.285 | 164 | 5.121 | 9,8% | 4.662 |
| 2 | 22.126 | 1,7% | 29,7% | 4.985 | 266 | 4.719 | 9,8% | 3.912 |
| 3 | 22.740 | 2,8% | 28,5% | 4.922 | 307 | 4.614 | 9,8% | 3.483 |
| 4 | 23.450 | 3,1% | 27,4% | 4.868 | 371 | 4.497 | 9,8% | 3.090 |
| 5 | 24.306 | 3,7% | 26,2% | 4.830 | 384 | 4.445 | 9,8% | 2.782 |
| 6 | 25.194 | 3,7% | 26,2% | 5.021 | 490 | 4.531 | 9,7% | 2.585 |
| 7 | 26.113 | 3,7% | 26,2% | 5.220 | 508 | 4.711 | 9,5% | 2.455 |
| 8 | 27.067 | 3,7% | 26,2% | 5.426 | 527 | 4.899 | 9,3% | 2.335 |
| 9 | 28.055 | 3,7% | 26,2% | 5.641 | 546 | 5.095 | 9,2% | 2.224 |
| 10 | 29.080 | 3,7% | 26,2% | 5.864 | 566 | 5.298 | 9,0% | 2.122 |
| Terminal | 30.142 | 3,7% | 26,2% | 6.078 | 2.466 | 3.612 | 9,0% | — |

**Optimista · Plataforma financiera de la pyme** — probabilidad 20%; valor terminal 296.113 (VP 118.608); DCF US$631,38 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 24.414 | 13,8% | 32,0% | 5.933 | 1.386 | 4.547 | 9,8% | 4.140 |
| 2 | 27.614 | 13,1% | 33,3% | 6.976 | 1.477 | 5.499 | 9,8% | 4.558 |
| 3 | 31.024 | 12,3% | 33,9% | 7.986 | 1.556 | 6.430 | 9,8% | 4.853 |
| 4 | 34.615 | 11,6% | 34,6% | 9.076 | 1.520 | 7.556 | 9,8% | 5.193 |
| 5 | 38.125 | 10,1% | 35,2% | 10.179 | 1.504 | 8.675 | 9,8% | 5.428 |
| 6 | 41.597 | 9,1% | 35,2% | 11.139 | 1.792 | 9.348 | 9,7% | 5.334 |
| 7 | 44.958 | 8,1% | 35,2% | 12.075 | 1.690 | 10.385 | 9,5% | 5.412 |
| 8 | 48.127 | 7,0% | 35,2% | 12.964 | 1.545 | 11.419 | 9,3% | 5.443 |
| 9 | 51.024 | 6,0% | 35,2% | 13.784 | 1.358 | 12.427 | 9,2% | 5.426 |
| 10 | 53.570 | 5,0% | 35,2% | 14.515 | 1.425 | 13.089 | 9,0% | 5.243 |
| Terminal | 56.243 | 5,0% | 35,2% | 15.239 | 3.365 | 11.874 | 9,0% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 43.691,05 | 94.290,80 | 137.981,85 | 137.048,90 | 512,91 |
| Conservadora | 34.904,72 | 35.638,28 | 70.543,01 | 69.610,05 | 260,52 |
| Disrupción | 29.651,01 | 27.050,21 | 56.701,21 | 55.768,26 | 208,71 |
| Optimista | 51.029,69 | 118.608,21 | 169.637,91 | 168.704,95 | 631,38 |

Ejemplo Base: (43.691,05 + 94.290,80 + 7.200 + 248 − 8.381) / 267,2 = US$512,91 por acción. El terminal representa 68,3% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 45% / 25% / 10% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,45 × 512,907543 + 0,25 × 260,516663 + 0,10 × 208,713550 + 0,20 × 631,380820 = US$443,085079 ≈ US$443,09. Los aportes son US$230,81 + US$65,13 + US$20,87 + US$126,28 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 443,085079 × 0,65 = US$288,005301 ≈ US$288,01. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base ni al antiguo caso técnico de la hoja: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Los DCF completos empiezan en las filas 22 (Base), 46 (Conservadora), 70 (Disrupción) y 94 (Optimista); sus valores por acción están en B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$512,91, es el valor intrínseco principal. El DCF esperado de US$443,09 combina las cuatro tesis con sus probabilidades y se presenta como complemento. La antigua calibración técnica Conservador/Base/Optimista de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: La IA es palanca de monetización

**Qué plantea.** Es la continuación de FY24-FY26: la pyme crece a doble dígito y el consumidor a un dígito medio.

**Traducción al modelo.** Global Business Solutions crece 14%, 13%, 12%, 11%, 10%; Consumer (TurboTax y ProTax) crece 7%, 6%, 6%, 5%, 5%; Credit Karma crece 10%, 8%, 7%, 7%, 6%. El crecimiento anual compuesto de cinco años es 9,8%; el margen operativo objetivo es 32,2%. El ROIC terminal es 22,6%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 45%; DCF: US$512,91 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (online Ecosystem (interanual): +19% (FY26); unidades y precio de TurboTax: Estables; credit Karma: Creciendo). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: La IA erosiona impuestos y contabilidad básica

**Qué plantea.** Es la sustitución parcial por IA en impuestos y contabilidad simples.

**Traducción al modelo.** Global Business Solutions crece 10%, 8%, 7%, 6%, 6%; Consumer (TurboTax y ProTax) crece 2%, 0%, -2%, -2%, -2%; Credit Karma crece 5%, 4%, 4%, 3%, 3%. El crecimiento anual compuesto de cinco años es 4,9%; el margen operativo objetivo es 29,2%. El ROIC terminal es el costo de capital (9,00%). El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 25%; DCF: US$260,52 por acción.

**Cómo contrastarla.** La apoyarían: online Ecosystem (interanual): ≤ +10%; unidades y precio de TurboTax: caída de unidades con precio a la baja; credit Karma: caída anual; margen operativo GAAP: ≤ 26%.


#### Disrupción · Deterioro de los fundamentales: Recesión y declaración gratuita del Estado

**Qué plantea.** Combina recesión (Credit Karma) y expansión de la declaración gratuita del Estado.

**Traducción al modelo.** Global Business Solutions crece 6%, 5%, 5%, 5%, 5%; Consumer (TurboTax y ProTax) crece -3%, -5%, -3%, -2%, 0%; Credit Karma crece -10%, 0%, 3%, 3%, 3%. El crecimiento anual compuesto de cinco años es 2,5%; el margen operativo objetivo es 26,2%. El ROIC terminal es el costo de capital (9,00%). El crecimiento terminal es 3,65%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 10%; DCF: US$208,71 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: online Ecosystem (interanual): ≤ +10%; unidades y precio de TurboTax: caída de unidades con precio a la baja; credit Karma: caída anual; margen operativo GAAP: ≤ 26%.


#### Optimista: Plataforma financiera de la pyme

**Qué plantea.** Es Intuit como plataforma financiera completa de la pyme (pagos, nómina, capital, mid-market).

**Traducción al modelo.** Global Business Solutions crece 17%, 16%, 15%, 14%, 12%; Consumer (TurboTax y ProTax) crece 8%, 8%, 7%, 7%, 6%; Credit Karma crece 12%, 10%, 10%, 8%, 8%. El crecimiento anual compuesto de cinco años es 12,2%; el margen operativo objetivo es 35,2%. El ROIC terminal es 22,6%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 20%; DCF: US$631,38 por acción.

**Cómo contrastarla.** La confirmarían: online Ecosystem (interanual): ≥ +15%; unidades y precio de TurboTax: unidades estables y asistido en alza; credit Karma: ≥ +8%; margen operativo GAAP: ≥ 29% en FY27.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 4,99%; Disrupción: 3,65%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,20) | Valor/acción (beta 1,34) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| **Base · La IA es palanca de monetización** | 45% | Global Business Solutions: 14%, 13%, 12%, 11%, 10%; Consumer (TurboTax y ProTax): 7%, 6%, 6%, 5%, 5%; Credit Karma: 10%, 8%, 7%, 7%, 6% | 9,8% | 32,2% | 2,3 | 22,6% | 4,99% | US$512,91 | US$496,03 |
| **Conservadora · La IA erosiona impuestos y contabilidad básica** | 25% | Global Business Solutions: 10%, 8%, 7%, 6%, 6%; Consumer (TurboTax y ProTax): 2%, 0%, -2%, -2%, -2%; Credit Karma: 5%, 4%, 4%, 3%, 3% | 4,9% | 29,2% | 2,3 | = costo de capital | 4,99% | US$260,52 | US$252,67 |
| **Disrupción · Deterioro de los fundamentales: Recesión y declaración gratuita del Estado** | 10% | Global Business Solutions: 6%, 5%, 5%, 5%, 5%; Consumer (TurboTax y ProTax): -3%, -5%, -3%, -2%, 0%; Credit Karma: -10%, 0%, 3%, 3%, 3% | 2,5% | 26,2% | 2,3 | = costo de capital | 3,65% | US$208,71 | US$202,58 |
| **Optimista · Plataforma financiera de la pyme** | 20% | Global Business Solutions: 17%, 16%, 15%, 14%, 12%; Consumer (TurboTax y ProTax): 8%, 8%, 7%, 7%, 6%; Credit Karma: 12%, 10%, 10%, 8%, 8% | 12,2% | 35,2% | 2,3 | 22,6% | 4,99% | US$631,38 | US$610,34 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  |  | **US$443,09** | **US$428,71** |

Base (45%) es la continuación de FY24-FY26: la pyme crece a doble dígito y el consumidor a un dígito medio. Conservadora (25%) es la sustitución parcial por IA en impuestos y contabilidad simples. Disrupción (10%) combina recesión (Credit Karma) y expansión de la declaración gratuita del Estado. Optimista (20%) es Intuit como plataforma financiera completa de la pyme (pagos, nómina, capital, mid-market). En las historias de erosión (Conservadora y Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF técnico anterior (beta 1,20; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF técnico anterior de la hoja.

| Crecimiento \ Margen | 28,2% | 30,2% | 32,2% | 34,2% | 36,2% |
|---|---:|---:|---:|---:|---:|
| 5,0% | 354,53 | 378,21 | 401,90 | 425,58 | 449,26 |
| 7,0% | 394,49 | 421,28 | 448,08 | 474,88 | 501,68 |
| 9,0% | 438,87 | 469,14 | 499,42 | 529,70 | 559,97 |
| 11,0% | 488,12 | 522,26 | 556,41 | 590,56 | 624,71 |
| 13,0% | 542,70 | 581,15 | 619,61 | 658,06 | 696,52 |


### Pre-mortem

1. Los asistentes de IA preparan declaraciones simples gratis y TurboTax pierde unidades en el extremo bajo.
2. Bancos, fintech y ERPs ligeros integran contabilidad y pagos gratis y QuickBooks pierde pymes nuevas.
3. Una recesión reduce el crédito al consumidor y Credit Karma cae 20-30%.
4. La regulación amplía la declaración gratuita del IRS o de los estados.
5. La compensación en acciones sigue en ~10% de los ingresos y diluye el valor por acción.

**Evidencia en contra de la historia más probable:** la compresión del múltiplo muestra que el mercado ya ve riesgo de sustitución, y Credit Karma sigue siendo cíclico. Si las unidades de TurboTax caen en la temporada 2027, Conservadora gana peso.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Online Ecosystem (interanual) | +19% (FY26) | ≥ +15% | ≤ +10% |
| Unidades y precio de TurboTax | Estables | Unidades estables y asistido en alza | Caída de unidades con precio a la baja |
| Credit Karma | Creciendo | ≥ +8% | Caída anual |
| Margen operativo GAAP | 27,4% | ≥ 29% en FY27 | ≤ 26% |
| SBC / ingresos | ~9,6% | ≤ 8% | ≥ 11% |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$274,77**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 28% | Margen 32% | Margen 35% |
|---|---:|---:|---:|
| Beta 1,20 | 0,2% (78% de las empresas) | −2,0% (87% de las empresas) | −3,4% (90% de las empresas) |
| Beta 1,34 | 0,8% (76% de las empresas) | −1,4% (85% de las empresas) | −2,8% (90% de las empresas) |

Frente al DCF Base (US$512,91), el valor intrínseco principal, el precio está por debajo en 46%.

Frente al DCF esperado de las historias (US$443,09 con la beta de la hoja; US$428,71 con la propuesta), el precio está por debajo en 38% y por debajo en 36%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Sistema financiero de la pyme y del contribuyente que usa la IA para cobrar más |  |
| Probabilidades | Base 45% / Conservadora 25% / Disrupción 10% / Optimista 20% |  |
| DCF Base hoy (valor intrínseco principal) | US$512,91 |  |
| DCF esperado por probabilidades (complemento) (beta de la hoja / propuesta) | US$443,09 / US$428,71 |  |
| Precio con MOS sobre el DCF esperado | US$288,01 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$202,58 a US$631,38 |  |
| Confianza | Media-alta en GBS; media en Consumer por IA y regulación |  |
| Qué cambiaría la opinión | Unidades de TurboTax en la temporada 2027 y crecimiento del Online Ecosystem |  |
| Revisión | Resultados del 1T FY27 (nov-2026) y temporada de impuestos 2027 |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [Intuit, Form 10-K FY2026](https://www.sec.gov/Archives/edgar/data/896878/000089687826000037/intu-20260731.htm)
- [Intuit, Form 10-Q del 3T FY2026](https://www.sec.gov/Archives/edgar/data/896878/000089687826000025/intu-20260430.htm)
- [Intuit, Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/896878/000089687825000035/intu-20250731.htm)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
