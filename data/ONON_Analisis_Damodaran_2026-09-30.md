---
schema: "jmr-analisis-damodaran-v1"
ticker: "ONON"
analysis_date: "2026-10-01"
---

# On Holding AG (ONON) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$34,90 por acción** (Base · Marca premium global que crece ~15% con margen de 16,5%).

**Complemento · DCF esperado por probabilidades: US$32,22.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$12,91–49,00. El MOS 35% se aplica al esperado: US$20,94. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: balance del último 10-q, capital invertido operativo, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet, ventas/capital contrastado con la historia y la industria (10 celdas, con respaldo). DCF esperado US$34,38 → US$30,60. Salvedades abiertas: Arrendamientos: bajo NIIF 16 todos los arrendamientos están en el balance y el EBIT ya excluye su costo financiero, así que su pasivo es deuda; se conserva en la deuda del DCF. Emisor extranjero (NIIF) sin XBRL trimestral en la SEC: flujos LTM y EPS no se contrastaron de forma automática; el balance se revisó con el informe semestral. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (bloque Base de 'Valuation output': US$34,90 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja calcula estos cuatro DCF en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

En cinco a diez años On es una de las cuatro o cinco marcas deportivas globales, con ventas de US$9.000-10.000 millones, liderada por el running premium y con ropa, tenis, fútbol y calzado de estilo de vida como segundas patas. Crece más rápido que el mercado porque todavía tiene poca participación fuera de Norteamérica y de Europa central, y porque vende cada vez más directo al consumidor, con un margen bruto de ~65% que ninguna marca grande tiene. El margen operativo sube de ~14% a ~16-17% por escala en gastos, pero no llega al de las marcas de lujo porque On debe seguir invirtiendo en atletas, tiendas e innovación para sostener la novedad. Reinvierte poco capital (fabrica con terceros) y empieza a devolver caja. El riesgo es de moda: una marca de 16 años que todavía no atravesó un ciclo completo de pérdida de favor del consumidor.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| On crece ~15% anual hasta 2031 | Sí | Sí: +21,6% en moneda constante en el 2T26 y meta de crecimiento de un dígito alto-teens hasta 2029 ([On, Investor Day 2026, 22-sep-2026](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000021/exhibit991oninvestorday202.htm)) | Probable, desacelerando |
| El margen bruto se sostiene en ~65% | Sí | Sí: 65,4% en el 2T26 con más venta directa y sin rebajas ([On, comunicado del 2T26, 11-ago-2026](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm)) | Probable |
| El margen operativo llega a ~16-17% | Sí | Sí: la meta de EBITDA ajustado ≥ 22% en 2029 equivale a ~15,5% operativo | Probable en el caso central |
| On llega al margen de Deckers o Birkenstock (23-29%) | Sí | Poco: On reinvierte en marca, tiendas y nuevas categorías | Baja |


### Visión externa: tasas base

Con ventas LTM de US$4.060 millones (US$2.873 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **$2,000-3,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 6,2% y una mediana de 5,1% (desviación estándar 8,9%); sumando una inflación de 2,5%, la mediana nominal ronda 7,6%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · Marca premium global que crece ~15% con margen de 16,5% | 14,7% | 18% |
| Conservadora · El ciclo de moda se enfría | 8,1% | 47% |
| Disrupción · Deterioro de los fundamentales: pasa la moda y las ventas caen como en Under Armour | 0,1% | 88% |
| Optimista · On se vuelve una marca deportiva global de primera línea | 18,1% | 11% |

On está en el tramo de ventas de US$2.000-3.000 millones de dólares de 2015 de The Base Rate Book. La Base (14,7% nominal compuesto en cinco años) está en la cola alta de ese tramo: pocas empresas sostienen crecimientos así cinco años, y por eso la Base queda algo por debajo de la meta de la gerencia.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: ~17,5% el primer año y ~14% después.** La Base crece 17,5% el primer año, en línea con la guía de 2026 (~20% en moneda constante, con mayoristas contenidos), y 14,7% compuesto en cinco años. La venta directa crece 14-30% y los mayoristas 8-10%. Queda algo por debajo de la meta de la gerencia (un dígito alto en los «teens» hasta 2029) porque pocas empresas sostienen ese ritmo: ~18% de las empresas de su tamaño lo lograron. Sensibilidad: ±2 puntos de crecimiento en los años 1-5 llevan el DCF Base a US$32,12 (−8%) y US$37,96 (+9%). Obligaría a revisarlo que los mayoristas caigan (hacia la Conservadora, 8,1%) o que On supere su meta (hacia la Optimista, 18,1%).

**Margen: de 14% a 16,5% con escala.** La Base parte de 14,0% el primer año (el margen NIIF del 1S26) y llega a 16,5% en 5 años. Supone margen bruto de ~65% y algo de escala en gastos, en línea con la meta de EBITDA ajustado de 22% en 2029 (≈ 15,5% operativo). Los arrendamientos ya están en el balance (NIIF 16), sin ajuste adicional. Sensibilidad: ±2 puntos de margen dan US$30,59 (−12%) y US$39,22 (+12%). La Conservadora (13,0%) supone más marketing para crecer; la Disrupción (9,0%), rebajas; la Optimista (20,0%), escala de marca global.

**Reinversión: liviana.** El ventas/capital es 2,30 en los años 1-5 (~US$0,43 de capital por dólar de ventas nuevas) y 2,10 en los años 6-10. On rota hoy su capital ~2,6 veces; se usa algo menos por las tiendas propias y las nuevas categorías. Con ±20% en el ventas/capital el DCF Base va de US$33,30 (−5%) a US$35,97 (+3%).

**Descuento y largo plazo: beta del sector y sin ventaja defendible.** El costo de capital inicial es 9,81% (tasa libre de riesgo 5,29% al 30-sep-2026, prima de mercado 4,63% de Damodaran de octubre, beta 1,05, sin deuda bancaria; los arrendamientos pesan ~6%) y el terminal 8,99%. Después del año 10 el crecimiento es 5,29% y el ROIC terminal es el costo de capital (9,0%): On gana hoy muy por encima de su costo de capital, pero su marca tiene 16 años y no atravesó todavía un ciclo de moda completo, así que no cuenta como ventaja probada. El terminal pesa 63,7% del valor operativo. ±1 punto de tasa da US$40,43 (+16%) y US$30,56 (−12%).

**Acciones, moneda y caja.** Se usan 336,1 millones de acciones económicas: 301,7 millones Clase A y 325,0 millones Clase B (cada una con 1/10 de los derechos económicos) al 30-jun-2026, más 1,9 millones de premios con efecto dilutivo. Las cifras en francos se convierten a dólares al tipo de cambio de cada período. La caja es US$1.493 millones y no hay deuda bancaria. Una dilución adicional de 5% llevaría el DCF Base a US$33,24 (−5%).

**Probabilidades y lectura del resultado.** Con 45% para la Base, 25% para la Conservadora, 10% para la Disrupción y 20% para la Optimista, el DCF esperado es US$32,22 frente a un DCF Base de US$34,90. Con el margen de seguridad de 35%, el precio de compra con margen es US$20,94.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$4.060 millones. Con el crecimiento de la Base llegan a US$8.067 millones en el año 5 y a US$11.673 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 14,0% en el año 1 a 16,5% al final, y se descuentan impuestos (20,0% al principio y 23,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$534 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$346 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$189 millones el primer año. Cada flujo se trae a hoy con el costo de capital (9,81% al principio, 8,99% al final): los diez años suman US$3.968 millones. Después del año 10 se supone que la empresa crece 5,29% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 9,0%; esa perpetuidad vale hoy US$6.966 millones, 64% del total. Flujos más terminal dan el valor de las operaciones, US$10.934 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$1.493 millones, menos deuda por US$696 millones. Queda un patrimonio de US$11.730 millones que, repartido entre 336,1 millones de acciones, da US$34,90 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 16,43× (peso 25% dentro de los múltiplos); EV/FCFF 28,53× (peso 38% dentro de los múltiplos); P/E 31,23× (peso 12% dentro de los múltiplos); P/FCFE 29,44× (peso 12% dentro de los múltiplos); P/OCF 26,03× (peso 12% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (10,6%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$34,90; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$30,59 | −12,4% |
| Margen objetivo +2 pp | US$39,22 | +12,4% |
| Crecimiento años 1–5 −2 pp | US$32,12 | −8,0% |
| Crecimiento años 1–5 +2 pp | US$37,96 | +8,8% |
| Ventas/capital −20% | US$33,30 | −4,6% |
| Ventas/capital +20% | US$35,97 | +3,1% |
| WACC +1 pp | US$30,56 | −12,4% |
| WACC −1 pp | US$40,43 | +15,8% |
| Crecimiento terminal −0,5 pp | US$34,61 | −0,8% |
| Crecimiento terminal +0,5 pp | US$35,20 | +0,9% |
| Acciones +5% | US$33,24 | −4,8% |


### Piezas del valor

**Crecimiento.** Las ventas de los últimos doce meses (julio 2025-junio 2026) suman CHF 3.220 millones, US$4.060 millones al tipo de cambio promedio de esos meses (cálculo propio: 2025 − 1S25 + 1S26, [On, 20-F 2025, 3-mar-2026](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000008/onholdingag-20251231.htm) y [On, estados intermedios del 1S26 (6-K), 11-ago-2026](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/onholdingag-20260630_d2.htm)). Mayoristas CHF 1.834 millones y directo al consumidor CHF 1.386 millones. En 2025 las ventas crecieron 30% (CHF 3.014 millones). En el 2T26 crecieron 13,5% en francos y 21,6% en moneda constante: directo al consumidor +34,3%, mayoristas +12,7%; Asia-Pacífico +54,7%, EMEA +20,5% y Américas +13,0% en moneda constante; ropa +56% ([On, comunicado del 2T26, 11-ago-2026](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm)). La guía de 2026 es un crecimiento de ~20% en moneda constante (CHF 3.470-3.560 millones) y la meta 2026-2029 es un crecimiento de un dígito alto en los «teens» hasta al menos CHF 5.600 millones en 2029 ([On, Investor Day 2026, 22-sep-2026](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000021/exhibit991oninvestorday202.htm)).

| CHF millones | 2024 | 2025 | LTM jun-26 (cálculo propio) | 2T26 vs 2T25 (moneda constante) |
|---|---:|---:|---:|---:|
| Mayoristas | 1.375 | 1.753 | 1.834 | +12,7% |
| Directo al consumidor | 943 | 1.261 | 1.386 | +34,3% |
| Total | 2.318 | 3.014 | 3.220 | +21,6% |
| Total en US$ (al promedio de cada período) | 2.635 | 3.636 | 4.060 | — |

**Márgenes.** El resultado operativo NIIF de los últimos doce meses es CHF 444 millones, 13,8% de las ventas (14,1% en el 1S26); ya descuenta los pagos en acciones (~2% de las ventas) y la depreciación de los derechos de uso. El margen bruto subió de 59,6% en 2023 a 62,8% en 2025 y 65,4% en el 2T26 por más venta directa y precio lleno, aun absorbiendo los aranceles de EE.UU. ([On, comunicado del 2T26, 11-ago-2026](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm)). La guía de 2026 es EBITDA ajustado de 19,5-20% y la meta de 2029, ≥ 22% con margen bruto ≥ 65% ([On, Investor Day 2026, 22-sep-2026](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000021/exhibit991oninvestorday202.htm)). Comparables: Deckers ganó 23% y Birkenstock ~29% en su último ejercicio, con margen bruto parecido pero menos inversión en crecimiento; Nike ~7% normalizado.

**Reinversión y retorno.** On fabrica con terceros: el capex fue CHF 79 millones en 2025 (2,6% de las ventas). El capital invertido (patrimonio + arrendamientos − caja) es ~US$1.570 millones al 30-jun-2026: rota ~2,6 veces las ventas. Se usa 2,3 en los años 1-5 (más tiendas propias, ropa y nuevas categorías) y el promedio de Shoe (2,1) en los años 6-10.

| Concepto (CHF millones) | 2024 | 2025 | LTM jun-26 |
|---|---:|---:|---:|
| Capex | 65 | 79 | 96 |
| Inventarios | 419 | 420 | 473 |
| Flujo operativo (después de intereses) | 495 | 338 | 501 |

**Ventas/capital: las referencias de Damodaran.** Damodaran elige el ventas/capital mirando el de la empresa hoy, el marginal de los últimos años y el promedio del sector, y comprueba que el rendimiento que implica sobre el capital nuevo sea creíble frente a lo que gana la empresa o su sector (Investment Valuation, cap. 11, p. 44-46). El marginal es volátil: recompras de acciones y adquisiciones mueven el capital contable. El usado está por debajo de todas las referencias: es prudente (más reinversión por dólar de crecimiento); la nota de la hoja (Input sheet B32-B33) explica por qué.

| Referencia | Ventas/capital | Detalle |
|---|---:|---|
| Empresa hoy | 2,59 | ventas LTM 4.060,3 / capital invertido 1.570,3 millones |
| Marginal, último año | 1,89 | Δventas 1.001,2 / Δcapital 530,0 millones (Dec '24 → Dec '25) |
| Marginal, últimos tres años | 3,86 | Δventas 2.355,5 / Δcapital 610,0 millones (Dec '22 → Dec '25) |
| Sector (Damodaran, enero de 2026) | 2,62 | Shoe |
| Usado en la hoja | 2,30 / 2,10 | años 1-5 / 6-10; rinde ~29% / ~27% sobre el capital nuevo (ROIC actual 28,5%) |

**Riesgo.** Beta bottom-up (Damodaran, 5-oct-2026): la desapalancada de Shoe en EE.UU., corregida por caja (1,00, enero de 2026), reapalancada con la D/E de mercado de On (arrendamientos incluidos, ~0,07) da ~1,05. Tabla de EE.UU. porque 57% de las ventas está en América (51% en Norteamérica). Ya no se suma la prima de 0,15 por moda (antes 1,20): el riesgo de que pase la moda está en las historias Conservadora y Disrupción, y sumarlo a la tasa lo contaría dos veces. La regresión semanal contra el S&P 500 da 1,78 desde la salida a bolsa y 1,58 a dos años; para una acción con cinco años de historia su error estándar es alto, por eso Damodaran prefiere la del sector.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,05 | 10,2% | 9,8% | US$34,90 |
| Bottom-up del sector (Shoe, reapalancada) | 1,05 | 10,2% | 9,8% | US$34,90 |


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Sin ventaja defendible | 28,5% | 20,9% | 9,4% | = costo de capital | US$34,90 | US$34,90 |

Fuentes de ventaja: Marca y tecnología (CloudTec, LightSpray) de 16 años, con venta directa creciente; sin historia de un ciclo completo. Evidencia: ROIC después de impuestos ~28,5% LTM (resultado operativo de US$560 millones sobre capital invertido de ~US$1.570 millones con arrendamientos); margen operativo de 12-14% desde 2023 y margen bruto de 65%. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$34,90 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$32,22. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$4.060 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 2.313 + 1.748 = 4.060. |
| Margen inicial del DCF | 14,0% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 20,00% en años 1–5; 23,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 9,81% → 8,99% | Tasa libre de riesgo 5,29%, beta 1,05, ERP 4,63%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 2,30x en años 1–5; 2,10x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 5,29%; Disrupción: 2,49% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (2,49%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Conservadora/Disrupción/Optimista: 8,99% (= WACC terminal) | Criterio de ventaja competitiva (sin ventaja defendible). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 1.493; deuda 696; acciones 336,1 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 2.313 × 1,08 + 1.748 × 1,30 = US$4.769,58 millones. Frente a 4.060, el crecimiento consolidado es 17,47%. En los años 2–5 es 16,67%, 15,06%, 13,22%, 11,27%; las ventas del año 5 son US$8.066,70 millones. El 14,7% de la tabla es el crecimiento anual compuesto de los cinco años: (8.066,70 / 4.060)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 4.769,58 × 14,00% × (1 − 20,00%) = US$534,19 millones. La reinversión es US$345,66 millones y el FCFF es US$188,54 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 8,99%. Reinversión terminal sobre el NOPAT: Base, 58,8% (5,29% / 8,99%); Conservadora, 58,8% (5,29% / 8,99%); Disrupción, 27,7% (2,49% / 8,99%); Optimista, 58,8% (5,29% / 8,99%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · Marca premium global que crece ~15% con margen de 16,5%** — probabilidad 45%; valor terminal 17.369 (VP 6.966); DCF US$34,90 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4.770 | 17,5% | 14,0% | 534 | 346 | 189 | 9,8% | 172 |
| 2 | 5.565 | 16,7% | 15,0% | 668 | 364 | 303 | 9,8% | 252 |
| 3 | 6.403 | 15,1% | 15,5% | 794 | 368 | 426 | 9,8% | 322 |
| 4 | 7.249 | 13,2% | 16,0% | 928 | 355 | 573 | 9,8% | 394 |
| 5 | 8.067 | 11,3% | 16,5% | 1.065 | 353 | 711 | 9,8% | 445 |
| 6 | 8.880 | 10,1% | 16,5% | 1.163 | 375 | 788 | 9,6% | 450 |
| 7 | 9.668 | 8,9% | 16,5% | 1.257 | 354 | 903 | 9,5% | 471 |
| 8 | 10.411 | 7,7% | 16,5% | 1.343 | 322 | 1.022 | 9,3% | 488 |
| 9 | 11.086 | 6,5% | 16,5% | 1.419 | 279 | 1.140 | 9,2% | 498 |
| 10 | 11.673 | 5,3% | 16,5% | 1.483 | 294 | 1.189 | 9,0% | 477 |
| Terminal | 12.290 | 5,3% | 16,5% | 1.561 | 919 | 643 | 9,0% | — |

**Conservadora · El ciclo de moda se enfría** — probabilidad 25%; valor terminal 9.232,2 (VP 3.702,7); DCF US$21,70 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4.502,3 | 10,9% | 14,0% | 504,3 | 169,5 | 334,8 | 9,8% | 304,9 |
| 2 | 4.892,1 | 8,7% | 13,6% | 532,3 | 168,2 | 364,0 | 9,8% | 301,9 |
| 3 | 5.279,1 | 7,9% | 13,4% | 565,9 | 161,7 | 404,3 | 9,8% | 305,3 |
| 4 | 5.650,9 | 7,0% | 13,2% | 596,7 | 149,5 | 447,2 | 9,8% | 307,5 |
| 5 | 5.994,7 | 6,1% | 13,0% | 623,4 | 154,5 | 469,0 | 9,8% | 293,7 |
| 6 | 6.349,9 | 5,9% | 13,0% | 655,4 | 174,4 | 481,1 | 9,6% | 274,7 |
| 7 | 6.716,1 | 5,8% | 13,0% | 688,0 | 179,4 | 508,7 | 9,5% | 265,3 |
| 8 | 7.092,8 | 5,6% | 13,0% | 721,1 | 184,0 | 537,0 | 9,3% | 256,2 |
| 9 | 7.479,3 | 5,4% | 13,0% | 754,5 | 188,4 | 566,1 | 9,2% | 247,5 |
| 10 | 7.874,9 | 5,3% | 13,0% | 788,3 | 198,4 | 589,9 | 9,0% | 236,6 |
| Terminal | 8.291,5 | 5,3% | 13,0% | 830,0 | 488,4 | 341,6 | 9,0% | — |

**Disrupción · Deterioro de los fundamentales: pasa la moda y las ventas caen como en Under Armour** — probabilidad 10%; valor terminal 3.646,9 (VP 1.462,6); DCF US$12,91 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4.235,1 | 4,3% | 14,0% | 474,3 | -80,4 | 554,8 | 9,8% | 505,2 |
| 2 | 4.050,0 | −4,4% | 12,0% | 388,8 | -46,3 | 435,1 | 9,8% | 360,8 |
| 3 | 3.943,6 | −2,6% | 11,0% | 347,0 | 16,7 | 330,3 | 9,8% | 249,4 |
| 4 | 3.982,1 | 1,0% | 10,0% | 318,6 | 43,2 | 275,4 | 9,8% | 189,4 |
| 5 | 4.081,3 | 2,5% | 9,0% | 293,9 | 44,2 | 249,6 | 9,8% | 156,3 |
| 6 | 4.183,1 | 2,5% | 9,0% | 298,9 | 49,6 | 249,3 | 9,6% | 142,4 |
| 7 | 4.287,3 | 2,5% | 9,0% | 304,1 | 50,9 | 253,2 | 9,5% | 132,1 |
| 8 | 4.394,2 | 2,5% | 9,0% | 309,3 | 52,2 | 257,1 | 9,3% | 122,7 |
| 9 | 4.503,7 | 2,5% | 9,0% | 314,5 | 53,5 | 261,1 | 9,2% | 114,1 |
| 10 | 4.616,0 | 2,5% | 9,0% | 319,9 | 54,8 | 265,1 | 9,0% | 106,3 |
| Terminal | 4.731,0 | 2,5% | 9,0% | 327,9 | 90,9 | 237,0 | 9,0% | — |

**Optimista · On se vuelve una marca deportiva global de primera línea** — probabilidad 20%; valor terminal 25.501 (VP 10.228); DCF US$49,00 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 4.932 | 21,5% | 14,0% | 552 | 443 | 110 | 9,8% | 100 |
| 2 | 5.950 | 20,6% | 16,4% | 781 | 480 | 301 | 9,8% | 250 |
| 3 | 7.054 | 18,5% | 17,6% | 993 | 497 | 496 | 9,8% | 374 |
| 4 | 8.197 | 16,2% | 18,8% | 1.233 | 492 | 741 | 9,8% | 509 |
| 5 | 9.329 | 13,8% | 20,0% | 1.493 | 491 | 1.002 | 9,8% | 627 |
| 6 | 10.459 | 12,1% | 20,0% | 1.661 | 518 | 1.143 | 9,6% | 653 |
| 7 | 11.546 | 10,4% | 20,0% | 1.820 | 478 | 1.342 | 9,5% | 700 |
| 8 | 12.551 | 8,7% | 20,0% | 1.963 | 418 | 1.545 | 9,3% | 737 |
| 9 | 13.428 | 7,0% | 20,0% | 2.084 | 338 | 1.746 | 9,2% | 763 |
| 10 | 14.139 | 5,3% | 20,0% | 2.177 | 356 | 1.821 | 9,0% | 730 |
| Terminal | 14.887 | 5,3% | 20,0% | 2.293 | 1.349 | 944 | 9,0% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 3.967,83 | 6.966,06 | 10.933,89 | 11.730,29 | 34,90 |
| Conservadora | 2.793,52 | 3.702,72 | 6.496,25 | 7.292,65 | 21,70 |
| Disrupción | 2.078,63 | 1.462,65 | 3.541,28 | 4.337,68 | 12,91 |
| Optimista | 5.443,54 | 10.227,58 | 15.671,13 | 16.467,53 | 49,00 |

Ejemplo Base: (3.967,83 + 6.966,06 + 1.493 − 696) / 336,1 = US$34,90 por acción. El terminal representa 63,7% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 45% / 25% / 10% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,45 × 34,901184 + 0,25 × 21,697847 + 0,10 × 12,905924 + 0,20 × 48,995912 = US$32,219770 ≈ US$32,22. Los aportes son US$15,71 + US$5,42 + US$1,29 + US$9,80 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 32,219770 × 0,65 = US$20,942850 ≈ US$20,94. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$34,90, es el valor intrínseco principal. El DCF esperado de US$32,22 combina las cuatro tesis con sus probabilidades y se presenta como complemento. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: Marca premium global que crece ~15% con margen de 16,5%

**Qué tiene que ocurrir.** On crece ~17,5% en los próximos doce meses (guía de 2026 con mayoristas contenidos) y ~14% anual en los años 2-5: venta directa +14-24% y mayoristas +8-10%, con Asia y la ropa como motores. El margen operativo sube de 14% a 16,5% en cinco años por escala en gastos, un poco más que la meta de 2029 de la gerencia.

**Traducción al modelo.** Mayoristas crece 8%, 10%, 10%, 9%, 8%; Directo al consumidor crece 30%, 24%, 20%, 17%, 14%. El crecimiento anual compuesto de cinco años es 14,7%; el margen operativo objetivo es 16,5%. El ROIC terminal es el costo de capital (8,99%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 45%; DCF: US$34,90 por acción.

**Cómo contrastarla.** Crecimiento en moneda constante ≥ 15% en 2027 con margen bruto ≥ 64%.


#### Conservadora: El ciclo de moda se enfría

**Qué tiene que ocurrir.** La moda del running premium se desacelera: los mayoristas compran menos, crecen las marcas nuevas y On necesita más marketing para crecer 8-10% anual; el margen operativo se queda en 13%.

**Traducción al modelo.** Mayoristas crece 4%, 4%, 4%, 4%, 4%; Directo al consumidor crece 20%, 14%, 12%, 10%, 8%. El crecimiento anual compuesto de cinco años es 8,1%; el margen operativo objetivo es 13,0%. El ROIC terminal es el costo de capital (8,99%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 25%; DCF: US$21,70 por acción.

**Cómo contrastarla.** Mayoristas negativos dos trimestres seguidos o margen bruto ≤ 62%.


#### Disrupción · Deterioro de los fundamentales: pasa la moda y las ventas caen como en Under Armour

**Qué tiene que ocurrir.** On repite la historia de marcas que pasaron de moda (Under Armour, Crocs en 2008): las ventas a mayoristas caen, se acumula inventario, llegan las rebajas y el margen operativo baja a 9%.

**Traducción al modelo.** Mayoristas crece 0%, -8%, -5%, 0%, 2%; Directo al consumidor crece 10%, 0%, 0%, 2%, 3%. El crecimiento anual compuesto de cinco años es 0,1%; el margen operativo objetivo es 9,0%. El ROIC terminal es el costo de capital (8,99%). El crecimiento terminal es 2,49%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 10%; DCF: US$12,91 por acción.

**Cómo contrastarla.** Crecimiento total ≤ 0% en 2027 o inventario creciendo más que las ventas dos trimestres.


#### Optimista: On se vuelve una marca deportiva global de primera línea

**Qué tiene que ocurrir.** On supera su meta de 2029: ropa, fútbol (con atletas como Mbappé) y Asia crecen al doble, la venta directa pasa de la mitad de las ventas y el margen operativo llega a 20%.

**Traducción al modelo.** Mayoristas crece 12%, 14%, 13%, 12%, 10%; Directo al consumidor crece 34%, 28%, 24%, 20%, 17%. El crecimiento anual compuesto de cinco años es 18,1%; el margen operativo objetivo es 20,0%. El ROIC terminal es el costo de capital (8,99%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 20%; DCF: US$49,00 por acción.

**Cómo contrastarla.** Crecimiento en moneda constante ≥ 20% en 2027 con EBITDA ajustado ≥ 21%.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 5,29%; Disrupción: 2,49%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | Crecimiento terminal | Valor/acción (beta 1,05) |
|---|---:|---|---:|---:|---:|---:|---:|
| **Base · Marca premium global que crece ~15% con margen de 16,5%** | 45% | Mayoristas: 8%, 10%, 10%, 9%, 8%; Directo al consumidor: 30%, 24%, 20%, 17%, 14% | 14,7% | 16,5% | 2,3 | 5,29% | US$34,90 |
| **Conservadora · El ciclo de moda se enfría** | 25% | Mayoristas: 4%, 4%, 4%, 4%, 4%; Directo al consumidor: 20%, 14%, 12%, 10%, 8% | 8,1% | 13,0% | 2,3 | 5,29% | US$21,70 |
| **Disrupción · Deterioro de los fundamentales: pasa la moda y las ventas caen como en Under Armour** | 10% | Mayoristas: 0%, -8%, -5%, 0%, 2%; Directo al consumidor: 10%, 0%, 0%, 2%, 3% | 0,1% | 9,0% | 2,3 | 2,49% | US$12,91 |
| **Optimista · On se vuelve una marca deportiva global de primera línea** | 20% | Mayoristas: 12%, 14%, 13%, 12%, 10%; Directo al consumidor: 34%, 28%, 24%, 20%, 17% | 18,1% | 20,0% | 2,3 | 5,29% | US$49,00 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  | **US$32,22** |

La Base pesa 45%: es la guía de 2026 y algo menos que la meta de 2029, que la gerencia viene superando. La Conservadora pesa 25% porque las marcas de moda deportiva se desaceleran sin aviso y los mayoristas ya se contienen. La Disrupción pesa 10%: On no muestra señales de inventario o rebajas, pero la marca tiene apenas 16 años. La Optimista pesa 20% porque On viene superando sus metas y suma categorías. Son juicio del analista, no frecuencias publicadas; el lector debe poner las suyas. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 1,05; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.

| Crecimiento \ Margen | 12,5% | 14,5% | 16,5% | 18,5% | 20,5% |
|---|---:|---:|---:|---:|---:|
| 10,7% | 23,12 | 26,72 | 30,31 | 33,91 | 37,51 |
| 12,7% | 24,88 | 28,92 | 32,95 | 36,99 | 41,03 |
| 14,7% | 26,81 | 31,34 | 35,86 | 40,39 | 44,91 |
| 16,7% | 28,93 | 34,00 | 39,06 | 44,13 | 49,19 |
| 18,7% | 31,25 | 36,92 | 42,58 | 48,24 | 53,90 |


### Pre-mortem

1. El running premium se satura: Hoka, Nike y las marcas chinas recuperan participación y los mayoristas reducen pedidos.
2. La expansión a ropa, fútbol y golf diluye la marca y el margen sin crear volumen.
3. Un cambio de gusto del consumidor joven (la Cloudtilt pierde atractivo) deja inventario y obliga a rebajar.
4. La estructura con co-CEO fundadores y un CFO nuevo pierde disciplina de costos.
5. Los aranceles y un franco suizo fuerte comprimen el margen bruto por debajo de 62%.

**Evidencia en contra de la historia más probable:** los mayoristas crecieron solo 4,8% en francos en el 2T26 y la gerencia los está conteniendo «para proteger el precio lleno» en un mercado con muchas rebajas; la acción cayó de US$50,63 (ene-2026) a US$30,20 ([On, comunicado del 2T26, 11-ago-2026](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm)).


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Crecimiento en moneda constante | +21,6% (2T26) | ≥ 18% | ≤ 10% |
| Mayoristas (moneda constante) | +12,7% (2T26) | ≥ +10% | ≤ 0% |
| Directo al consumidor (participación) | 45,7% de las ventas (2T26) | ≥ 48% | Cae |
| Margen bruto | 65,4% (2T26) | ≥ 65% | ≤ 62% |
| EBITDA ajustado | 19,8% (2T26) | ≥ 21% | ≤ 17% |
| Inventario / ventas | ~15% (jun-26) | Estable | Crece más que las ventas |
| Asia-Pacífico | +54,7% (2T26) | ≥ +30% | ≤ +10% |
| Recompras (programa de US$1.000M) | Aprobado en sep-2026 | Ejecución gradual | Suspendido |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$30,20**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 13% | Margen 16% | Margen 20% |
|---|---:|---:|---:|
| Beta 1,05 | 16,7% (14% de las empresas) | 10,6% (34% de las empresas) | 6,3% (58% de las empresas) |

Frente al DCF Base (US$34,90), el valor intrínseco principal, el precio está por debajo en 13%.

Frente al DCF esperado de las historias (US$32,22), el complemento, el precio está por debajo en 6%. El precio de US$30,20 queda ~9% por debajo de la Base y casi igual al esperado: el mercado paga por un crecimiento alto, pero no por la meta completa de la gerencia; con el margen de la Base, el DCF inverso pide ~12% anual en los años 1-5. ¿Qué sabe el mercado que yo no? Puede estar pesando más la Conservadora por la contención de los mayoristas y el enfriamiento del sector, o descontando un margen menor por la inversión en nuevas categorías.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-10-01 |  |
| Historia en una frase | Marca premium de running que crece ~15% con margen bruto de 65%; sin ventaja defendible probada a largo plazo |  |
| Probabilidades | Base 45% / Conservadora 25% / Disrupción 10% / Optimista 20% |  |
| DCF Base hoy (valor intrínseco principal) | US$34,90 |  |
| DCF esperado por probabilidades (complemento) | US$32,22 |  |
| Precio con MOS sobre el DCF esperado | US$20,94 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$12,91 a US$49,00 |  |
| Confianza | Media: el crecimiento y el margen bruto están bien documentados; la duración de la moda no |  |
| Qué cambiaría la opinión | El crecimiento de los mayoristas, el margen bruto y la ejecución de las nuevas categorías |  |
| Revisión | Resultados del 3T26 (noviembre de 2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [On, comunicado del 2T26 (11-ago-2026)](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm)
- [On, estados intermedios del 1S26 (6-K, 11-ago-2026)](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/onholdingag-20260630_d2.htm)
- [On, 20-F 2025 (3-mar-2026)](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000008/onholdingag-20251231.htm)
- [On, Investor Day 2026 (22-sep-2026)](https://www.sec.gov/Archives/edgar/data/1858985/000185898526000021/exhibit991oninvestorday202.htm)
- [On, cofundadores como co-CEO (25-mar-2026)](https://www.sec.gov/Archives/edgar/data/1858985/000095010326004606/dp244091_ex9901.htm)
- [Damodaran, ERP implícita de octubre de 2026 (con la tasa y los precios del 30-sep)](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx)
- [Damodaran, Betas by Sector (global), enero de 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
- [Mauboussin y Callahan, The Base Rate Book (2016)](https://www.credit-suisse.com/media/assets/corporate/docs/about-us/research/publications/the-base-rate-book-integrating-the-past-to-better-anticipate-the-future.pdf)
