---
schema: "jmr-analisis-damodaran-v1"
ticker: "DPZ"
analysis_date: "2026-09-30"
---

# Domino's Pizza, Inc. (DPZ) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$323,13 por acción** (Base · Crece por tiendas con ventas mismas tiendas bajas).

**Complemento · DCF esperado por probabilidades: US$282,25.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$93,61–387,75. El MOS 35% se aplica al esperado: US$183,46. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), balance del último 10-q, capital invertido operativo, eps básico, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet (29 celdas, con respaldo). DCF esperado US$308,75 → US$293,85. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (bloque Base de 'Valuation output': US$323,13 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja calcula estos cuatro DCF en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

Domino's es la mayor cadena de pizza del mundo y casi todas sus tiendas son franquiciadas. Gana dinero de dos formas: regalías sobre las ventas del sistema (alto margen, casi sin capital) y la venta de insumos a los franquiciados de EE.UU. y Canadá (~60% de los ingresos, margen bajo). Es un negocio de muy poco capital, con retornos altísimos y patrimonio negativo por recompras con deuda titulizada (~US$4.900 millones). Su ventaja histórica fue la conveniencia del delivery propio; los agregadores (DoorDash, Uber Eats) la estrecharon y en el 2T26 las ventas mismas tiendas fueron +0,1% en EE.UU. y −0,1% internacional, con ventas minoristas globales de +3% por aperturas. La historia de cinco años es la de un compuesto maduro que crece por tiendas nuevas; la pregunta es si las ventas por tienda vuelven a crecer.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~4,5% anual cinco años | Sí | Sí: +5% en 2024 y 2025, +3,9% en el 1S26 | Probable |
| Las ventas mismas tiendas de EE.UU. vuelven a +3% | Sí | Poco: planas en 2026 pese a promociones y a entrar en Uber Eats/DoorDash | Baja-media |
| El margen operativo llega a 20% | Sí | Sí: 18,3% → 19,3% en dos años con escala en regalías | Probable |
| La deuda titulizada se vuelve un problema | Sí | Poco: flujo estable y refinanciaciones ordenadas | Baja salvo recesión fuerte |


### Visión externa: tasas base

Con ventas LTM de US$5.028 millones (US$3.557 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **$3,000-4,500 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 5,4% y una mediana de 4,7% (desviación estándar 8,5%); sumando una inflación de 2,5%, la mediana nominal ronda 7,2%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · Crece por tiendas con ventas mismas tiendas bajas | 4,5% | 67% |
| Conservadora · Los agregadores erosionan la ventaja | 2,5% | 79% |
| Disrupción · Deterioro de los fundamentales: El sistema de franquicias se debilita | 0,7% | 84% |
| Optimista · Agregadores e internacional aceleran | 6,2% | 56% |

En dólares de 2015 la empresa está en el tramo de US$3.000-4.500 millones: crecer 4,5% anual cinco años (Base) lo logró ~67% de las empresas de ese tamaño; 6,2% (Optimista), ~56%. La hoja es realista y cercana a la mediana nominal (~6,6%). Domino's no necesita crecer mucho para valer lo que dice el DCF; su valor depende más de la duración y de los márgenes que del crecimiento.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: tiendas nuevas, ventas por tienda planas.** Domino's es casi todo franquicia: gana regalías sobre las ventas del sistema (margen alto, casi sin capital) y vende insumos a los franquiciados de EE.UU. y Canadá (~60% de los ingresos, margen bajo). En el 2T26 las ventas minoristas globales crecieron 3% sin efecto cambiario, pero las ventas mismas tiendas fueron +0,1% en EE.UU. y −0,1% internacional: todo el crecimiento viene de tiendas nuevas. La Base supone exactamente eso: 4-5% al año en ambas partes del negocio, 4,5% compuesto, cerca de la mediana nominal de empresas de su tamaño (~67% lo lograron). No pedimos más porque los agregadores (DoorDash, Uber Eats) estrecharon la ventaja del delivery propio y la entrada de Domino's en esas plataformas todavía no movió las ventas por tienda. La Conservadora (2,5%) es que los agregadores sigan quitando pedidos; la Disrupción (0,7%), un sistema de franquicias que se debilita con cierres internacionales; la Optimista (6,2%), que agregadores e internacional aceleren. Domino's no necesita crecer mucho para valer lo que dice el DCF: su valor depende más de la duración de los retornos que del crecimiento.

**Margen: un paso pequeño y creíble.** El margen sube despacio (18,3% → 19,3%) porque la cadena de suministro, que vende insumos casi al costo, diluye el margen de las regalías. La Base usa 20,3%, apenas un punto más, porque no hay un motor evidente para más: el riesgo está en la rentabilidad de los franquiciados, y si sus márgenes caen Domino's tiene que subsidiar promociones o bajar el precio de los insumos. El rango va de 17,3% a 21,3%. Aun así el margen pesa: dos puntos llevan la Base a US$278,97 (−14%) o US$367,28 (+14%), porque cada punto se aplica sobre todas las ventas del sistema y casi no hay capital que lo diluya. Lo invalidaría un margen por debajo de 18%.

**Reinversión: el capital lo ponen los franquiciados.** Domino's casi no necesita capital: capex de ~US$105-120 millones al año (~2,5% de las ventas); las tiendas las pagan los franquiciados. La hoja usa un ventas/capital de 2,64× (cada dólar de ventas nuevas exige ~US$0,38), y el ROIC actual es altísimo (~81% en el modelo, 65-78% en 2021-2026). El flujo libre (~US$670 millones en 2025) va a dividendos y recompras financiadas en parte con deuda titulizada (~US$4.900 millones), por eso el patrimonio contable es negativo. Después del año 10 la Base no conserva ese 81%: usa 18,4%, el promedio de la industria, porque Damodaran limita el ROIC terminal de una ventaja duradera al de su sector; suponer que un ROIC de 80% dura para siempre sería extrapolar. Si la ventaja desapareciera (ROIC terminal igual al costo de capital) la Base caería a US$206,47 (−36%); por eso la Conservadora y la Disrupción usan el costo de capital.

**Descuento: una empresa muy apalancada.** El costo de capital empieza bajo (8,42%) porque la deuda pesa mucho en la estructura y es más barata que el patrimonio, y converge a 9,38%. La beta de la hoja es 1,17; la bottom-up de restaurantes reapalancada con la deuda de Domino's da 1,07, más coherente con un patrimonio tan apalancado, y con ella el DCF técnico baja algo. Es el punto donde más se apoya el valor: un punto más de tasa lleva la Base a US$234,99 (−27%); uno menos, a US$467,47 (+45%). El crecimiento perpetuo es 5,29% y el terminal explica 63,7% del valor operativo. La refinanciación de la deuda titulizada con tasas altas es un riesgo que no está en la tasa y que conviene vigilar (deuda/EBITDA ~4,5×; por encima de 5,5× cambiaría la lectura).

**Probabilidades y lectura del resultado.** La Base pesa 50%, más que en otras empresas, porque es la continuación de lo que se ve desde 2024; la Conservadora 25%, los agregadores; la Disrupción 5%; la Optimista 20%. El DCF Base es US$323,13 y el esperado US$282,25, frente a un precio de US$297,62. La distancia entre la Base y la Conservadora (US$153,81) es grande porque la Conservadora además pierde el ROIC excedente: no solo crece menos, sino que su crecimiento deja de crear valor. Las acciones se fijan en 33,1 millones; las recompras no se modelan.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$5.028 millones. Con el crecimiento de la Base llegan a US$6.254 millones en el año 5 y a US$8.002 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 19,3% en el año 1 a 20,3% al final, y se descuentan impuestos (21,9% al principio y 23,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$788 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$83 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$705 millones el primer año. Cada flujo se trae a hoy con el costo de capital (8,42% al principio, 9,38% al final): los diez años suman US$5.663 millones. Después del año 10 se supone que la empresa crece 5,29% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 18,4%; esa perpetuidad vale hoy US$9.952 millones, 64% del total. Flujos más terminal dan el valor de las operaciones, US$15.615 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$165 millones, más activos no operativos por US$28 millones, menos deuda por US$5.112 millones (incluye los arrendamientos capitalizados). Queda un patrimonio de US$10.695 millones que, repartido entre 33,1 millones de acciones, da US$323,13 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 17,57× (peso 33% dentro de los múltiplos); EV/FCFF 27,89× (peso 17% dentro de los múltiplos); P/E 22,85× (peso 33% dentro de los múltiplos); P/FCFE 25,23× (peso 8% dentro de los múltiplos); P/OCF 19,76× (peso 8% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (10,2%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$323,13; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$278,97 | −13,7% |
| Margen objetivo +2 pp | US$367,28 | +13,7% |
| Crecimiento años 1–5 −2 pp | US$276,38 | −14,5% |
| Crecimiento años 1–5 +2 pp | US$375,12 | +16,1% |
| Ventas/capital −20% | US$317,41 | −1,8% |
| Ventas/capital +20% | US$326,94 | +1,2% |
| WACC +1 pp | US$234,99 | −27,3% |
| WACC −1 pp | US$467,47 | +44,7% |
| Crecimiento terminal −0,5 pp | US$295,69 | −8,5% |
| Crecimiento terminal +0,5 pp | US$357,89 | +10,8% |
| ROIC terminal = costo de capital | US$206,47 | −36,1% |
| Acciones +5% | US$307,74 | −4,8% |


### Piezas del valor

**Crecimiento.** Ingresos de US$4.479 millones (2023, −1,3%), US$4.706 millones (2024, +5,1%) y US$4.940 millones (2025, +5,0%); US$2.345 millones en el 1S26 (+3,9%). En el 2T26, las ventas minoristas globales sin efecto cambiario crecieron 3,0%, con ventas mismas tiendas de +0,1% en EE.UU. y −0,1% internacional: el crecimiento viene de tiendas nuevas. La división de las historias entre cadena de suministro (~60%) y el resto (~40%) es una aproximación con el peso del costo de suministro del 1S26.

| US$ millones | 2023 | 2024 | 2025 |
|---|---:|---:|---:|
| Ingresos | 4.479 | 4.706 | 4.940 |
| Crecimiento | −1,3% | +5,1% | +5,0% |
| Margen operativo | 18,3% | 18,7% | 19,3% |
| FCFF (hoja) | 664 | 642 | 737 |

**Márgenes.** El margen operativo sube lento (18,3% → 19,3%) porque la cadena de suministro diluye el margen de las regalías. La hoja supone 19% el próximo año y 20% de objetivo, un paso pequeño y creíble. El riesgo está en la rentabilidad de los franquiciados: si sus márgenes caen, Domino's tiene que subsidiar promociones o bajar el precio de los insumos. Las historias van de 17% a 21%.

**Reinversión y retorno.** Casi no necesita capital: capex de ~US$105-120 millones al año (~2,5% de las ventas); las tiendas las pagan los franquiciados. La hoja usa un sales-to-capital de 3. El flujo libre (~US$670 millones en 2025) va a dividendos (US$237 millones) y recompras (US$358 millones). Con tan poco capital, el ROIC actual es ~99%. Ventaja durable: marca probada de más de 60 años y escala logística en reparto, con ROIC de 65-78% en 2021-2026. El ROIC después del año 10 es 18,4%, el promedio de su industria según Damodaran. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$231 millones, compromisos del 10-Q al 2026-06-14) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$14 millones, +0,29 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,05 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usa una beta de 1,17 (desde el 3-oct-2026; antes 0,90). Regla de la cartera (prompt v4, paso 2): bottom-up de Restaurant/Dining (Damodaran, ene-2026: 0,78 desapalancada y corregida por caja) reapalancada con la D/E de mercado 0,48 = 1,07 + 0,10 por un solo concepto (pizza a domicilio) = 1,17. La de regresión queda como referencia. La D/E alta (recapitalización con deuda) explica que la beta reapalancada supere a la del sector. El efecto de cada beta en el DCF Base está en la tabla.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,17 | 10,1% | 8,4% | US$315,02 |
| Bottom-up del sector (Restaurant/Dining, reapalancada) | 1,07 | 9,6% | 8,1% | US$322,67 |


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 81,2% | 18,4% | 9,4% | 18,4% | US$323,13 | US$201,12 |

Fuentes de ventaja: Marca probada (más de 60 años, se recuperó de la crisis de 2008-2010) y densidad y escala logística en reparto; franquicias con muy poco capital. Evidencia: ROIC 65-78% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$323,13 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$282,25. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$5.028 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 3.013 + 2.015 = 5.028. |
| Margen inicial del DCF | 19,3% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 21,89% en años 1–5; 23,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 8,42% → 9,38% | Tasa libre de riesgo 5,29%, beta 1,17, ERP 4,09%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 2,64x en años 1–5; 2,64x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 5,29%; Disrupción: 1,00% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (1,00%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Optimista: 18,40%; Conservadora/Disrupción: 9,38% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 165; deuda 5.112; activos no operativos 28; acciones 33,1 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 3.013 × 1,04 + 2.015 × 1,04 = US$5.228,92 millones. Frente a 5.028, el crecimiento consolidado es 4,00%. En los años 2–5 es 4,20%, 4,70%, 4,70%, 4,70%; las ventas del año 5 son US$6.253,76 millones. El 4,5% de la tabla es el crecimiento anual compuesto de los cinco años: (6.253,76 / 5.028)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 5.228,92 × 19,29% × (1 − 21,89%) = US$787,81 millones. La reinversión es US$83,15 millones y el FCFF es US$704,66 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,38%. Reinversión terminal sobre el NOPAT: Base, 28,8% (5,29% / 18,40%); Conservadora, 56,4% (5,29% / 9,38%); Disrupción, 10,7% (1,00% / 9,38%); Optimista, 28,8% (5,29% / 18,40%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · Crece por tiendas con ventas mismas tiendas bajas** — probabilidad 50%; valor terminal 22.930,4 (VP 9.951,5); DCF US$323,13 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5.228,9 | 4,0% | 19,3% | 787,8 | 83,1 | 704,7 | 8,4% | 649,9 |
| 2 | 5.448,6 | 4,2% | 19,7% | 837,9 | 97,0 | 741,0 | 8,4% | 630,4 |
| 3 | 5.704,7 | 4,7% | 19,9% | 886,2 | 101,5 | 784,7 | 8,4% | 615,7 |
| 4 | 5.972,9 | 4,7% | 20,1% | 937,2 | 106,3 | 830,9 | 8,4% | 601,4 |
| 5 | 6.253,8 | 4,7% | 20,3% | 991,1 | 114,1 | 877,0 | 8,4% | 585,4 |
| 6 | 6.555,2 | 4,8% | 20,3% | 1.035,9 | 122,5 | 913,4 | 8,6% | 561,4 |
| 7 | 6.878,8 | 4,9% | 20,3% | 1.083,9 | 131,6 | 952,3 | 8,8% | 538,0 |
| 8 | 7.226,5 | 5,1% | 20,3% | 1.135,5 | 141,5 | 994,0 | 9,0% | 515,2 |
| 9 | 7.600,3 | 5,2% | 20,3% | 1.190,8 | 152,2 | 1.038,6 | 9,2% | 493,0 |
| 10 | 8.002,4 | 5,3% | 20,3% | 1.250,2 | 160,3 | 1.089,9 | 9,4% | 473,0 |
| Terminal | 8.425,7 | 5,3% | 20,3% | 1.316,3 | 378,4 | 937,9 | 9,4% | — |

**Conservadora · Los agregadores erosionan la ventaja** — probabilidad 25%; valor terminal 11.399,7 (VP 4.947,3); DCF US$153,81 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5.138,4 | 2,2% | 19,3% | 774,2 | 46,7 | 727,4 | 8,4% | 671,0 |
| 2 | 5.261,9 | 2,4% | 19,1% | 784,6 | 53,8 | 730,7 | 8,4% | 621,7 |
| 3 | 5.404,1 | 2,7% | 19,0% | 801,5 | 55,3 | 746,2 | 8,4% | 585,6 |
| 4 | 5.550,1 | 2,7% | 18,9% | 818,9 | 56,8 | 762,1 | 8,4% | 551,6 |
| 5 | 5.700,1 | 2,7% | 18,8% | 836,5 | 69,5 | 767,0 | 8,4% | 512,1 |
| 6 | 5.883,7 | 3,2% | 18,8% | 861,0 | 83,3 | 777,8 | 8,6% | 478,1 |
| 7 | 6.103,7 | 3,7% | 18,8% | 890,7 | 98,3 | 792,3 | 8,8% | 447,6 |
| 8 | 6.363,4 | 4,3% | 18,8% | 925,9 | 115,0 | 810,9 | 9,0% | 420,3 |
| 9 | 6.667,1 | 4,8% | 18,8% | 967,3 | 133,5 | 833,8 | 9,2% | 395,8 |
| 10 | 7.019,8 | 5,3% | 18,8% | 1.015,6 | 140,6 | 875,0 | 9,4% | 379,7 |
| Terminal | 7.391,1 | 5,3% | 18,8% | 1.069,3 | 603,0 | 466,2 | 9,4% | — |

**Disrupción · Deterioro de los fundamentales: El sistema de franquicias se debilita** — probabilidad 5%; valor terminal 7.835,3 (VP 3.400,4); DCF US$93,61 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5.027,8 | 0,0% | 19,3% | 757,5 | 7,6 | 749,9 | 8,4% | 691,7 |
| 2 | 5.048,0 | 0,4% | 18,5% | 729,0 | 19,1 | 709,9 | 8,4% | 603,9 |
| 3 | 5.098,4 | 1,0% | 18,1% | 720,4 | 19,3 | 701,1 | 8,4% | 550,1 |
| 4 | 5.149,4 | 1,0% | 17,7% | 711,5 | 19,5 | 692,0 | 8,4% | 500,8 |
| 5 | 5.200,9 | 1,0% | 17,3% | 702,3 | 19,7 | 682,7 | 8,4% | 455,7 |
| 6 | 5.252,9 | 1,0% | 17,3% | 707,3 | 19,9 | 687,5 | 8,6% | 422,6 |
| 7 | 5.305,5 | 1,0% | 17,3% | 712,4 | 20,1 | 692,3 | 8,8% | 391,1 |
| 8 | 5.358,5 | 1,0% | 17,3% | 717,5 | 20,3 | 697,2 | 9,0% | 361,3 |
| 9 | 5.412,1 | 1,0% | 17,3% | 722,5 | 20,5 | 702,1 | 9,2% | 333,3 |
| 10 | 5.466,2 | 1,0% | 17,3% | 727,7 | 20,7 | 707,0 | 9,4% | 306,8 |
| Terminal | 5.520,9 | 1,0% | 17,3% | 735,0 | 78,4 | 656,6 | 9,4% | — |

**Optimista · Agregadores e internacional aceleran** — probabilidad 20%; valor terminal 26.589,2 (VP 11.539,4); DCF US$387,75 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5.349,6 | 6,4% | 19,3% | 806,0 | 129,7 | 676,3 | 8,4% | 623,8 |
| 2 | 5.692,2 | 6,4% | 20,1% | 893,2 | 138,0 | 755,1 | 8,4% | 642,4 |
| 3 | 6.056,8 | 6,4% | 20,5% | 969,3 | 135,5 | 833,8 | 8,4% | 654,3 |
| 4 | 6.414,6 | 5,9% | 20,9% | 1.046,6 | 138,5 | 908,1 | 8,4% | 657,2 |
| 5 | 6.780,5 | 5,7% | 21,3% | 1.127,5 | 144,3 | 983,2 | 8,4% | 656,4 |
| 6 | 7.161,7 | 5,6% | 21,3% | 1.187,5 | 150,2 | 1.037,3 | 8,6% | 637,6 |
| 7 | 7.558,4 | 5,5% | 21,3% | 1.249,7 | 156,1 | 1.093,6 | 8,8% | 617,8 |
| 8 | 7.970,8 | 5,5% | 21,3% | 1.314,1 | 162,1 | 1.152,0 | 9,0% | 597,1 |
| 9 | 8.399,1 | 5,4% | 21,3% | 1.380,8 | 168,2 | 1.212,6 | 9,2% | 575,6 |
| 10 | 8.843,4 | 5,3% | 21,3% | 1.449,6 | 177,1 | 1.272,5 | 9,4% | 552,3 |
| Terminal | 9.311,2 | 5,3% | 21,3% | 1.526,3 | 438,8 | 1.087,5 | 9,4% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 5.663,42 | 9.951,50 | 15.614,93 | 10.695,47 | 323,13 |
| Conservadora | 5.063,36 | 4.947,34 | 10.010,70 | 5.091,25 | 153,81 |
| Disrupción | 4.617,36 | 3.400,44 | 8.017,80 | 3.098,35 | 93,61 |
| Optimista | 6.214,52 | 11.539,40 | 17.753,92 | 12.834,46 | 387,75 |

Ejemplo Base: (5.663,42 + 9.951,50 + 165 + 28 − 5.112) / 33,1 = US$323,13 por acción. El terminal representa 63,7% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 50% / 25% / 5% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,50 × 323,126047 + 0,25 × 153,814135 + 0,05 × 93,605596 + 0,20 × 387,748111 = US$282,246459 ≈ US$282,25. Los aportes son US$161,56 + US$38,45 + US$4,68 + US$77,55 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 282,246459 × 0,65 = US$183,460199 ≈ US$183,46. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$323,13, es el valor intrínseco principal. El DCF esperado de US$282,25 combina las cuatro tesis con sus probabilidades y se presenta como complemento. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: Crece por tiendas con ventas mismas tiendas bajas

**Qué plantea.** Es la continuación de 2024-2026: crecimiento de tiendas y ventas por tienda planas.

**Traducción al modelo.** Cadena de suministro crece 4%, 4%, 4%, 4%, 4%; Regalías, tiendas propias y fondo de publicidad crece 4%, 4%, 5%, 5%, 5%. El crecimiento anual compuesto de cinco años es 4,5%; el margen operativo objetivo es 20,3%. El ROIC terminal es 18,4%. El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 50%; DCF: US$323,13 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (ventas mismas tiendas EE.UU.: +0,1% (2T26); ventas mismas tiendas internacionales: −0,1%; aperturas netas globales: Positivas). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: Los agregadores erosionan la ventaja

**Qué plantea.** Es el riesgo de que los agregadores sigan quitando pedidos.

**Traducción al modelo.** Cadena de suministro crece 2%, 2%, 2%, 2%, 2%; Regalías, tiendas propias y fondo de publicidad crece 2%, 3%, 3%, 3%, 3%. El crecimiento anual compuesto de cinco años es 2,5%; el margen operativo objetivo es 18,8%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 25%; DCF: US$153,81 por acción.

**Cómo contrastarla.** La apoyarían: ventas mismas tiendas EE.UU.: negativas dos trimestres; ventas mismas tiendas internacionales: ≤ −2%; aperturas netas globales: cierres netos internacionales; margen operativo: ≤ 18%.


#### Disrupción · Deterioro de los fundamentales: El sistema de franquicias se debilita

**Qué plantea.** Es un problema en el sistema de franquicias (cierres internacionales, franquiciados en dificultades).

**Traducción al modelo.** Cadena de suministro crece 0%, 0%, 1%, 1%, 1%; Regalías, tiendas propias y fondo de publicidad crece 0%, 1%, 1%, 1%, 1%. El crecimiento anual compuesto de cinco años es 0,7%; el margen operativo objetivo es 17,3%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 1,00%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 5%; DCF: US$93,61 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: ventas mismas tiendas EE.UU.: negativas dos trimestres; ventas mismas tiendas internacionales: ≤ −2%; aperturas netas globales: cierres netos internacionales; margen operativo: ≤ 18%.


#### Optimista: Agregadores e internacional aceleran

**Qué plantea.** Supone que la entrada en los agregadores y el ritmo de aperturas internacionales sumen crecimiento.

**Traducción al modelo.** Cadena de suministro crece 6%, 6%, 6%, 6%, 6%; Regalías, tiendas propias y fondo de publicidad crece 7%, 7%, 7%, 6%, 6%. El crecimiento anual compuesto de cinco años es 6,2%; el margen operativo objetivo es 21,3%. El ROIC terminal es 18,4%. El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 20%; DCF: US$387,75 por acción.

**Cómo contrastarla.** La confirmarían: ventas mismas tiendas EE.UU.: ≥ +2%; ventas mismas tiendas internacionales: ≥ +2%; aperturas netas globales: ≥ 700 al año; margen operativo: ≥ 19,5%.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 5,29%; Disrupción: 1,00%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,17) | Valor/acción (beta 1,07) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| **Base · Crece por tiendas con ventas mismas tiendas bajas** | 50% | Cadena de suministro: 4%, 4%, 4%, 4%, 4%; Regalías, tiendas propias y fondo de publicidad: 4%, 4%, 5%, 5%, 5% | 4,5% | 20,3% | 2,6 | 18,4% | 5,29% | US$323,13 | US$330,93 |
| **Conservadora · Los agregadores erosionan la ventaja** | 25% | Cadena de suministro: 2%, 2%, 2%, 2%, 2%; Regalías, tiendas propias y fondo de publicidad: 2%, 3%, 3%, 3%, 3% | 2,5% | 18,8% | 2,6 | = costo de capital | 5,29% | US$153,81 | US$158,46 |
| **Disrupción · Deterioro de los fundamentales: El sistema de franquicias se debilita** | 5% | Cadena de suministro: 0%, 0%, 1%, 1%, 1%; Regalías, tiendas propias y fondo de publicidad: 0%, 1%, 1%, 1%, 1% | 0,7% | 17,3% | 2,6 | = costo de capital | 1,00% | US$93,61 | US$97,15 |
| **Optimista · Agregadores e internacional aceleran** | 20% | Cadena de suministro: 6%, 6%, 6%, 6%, 6%; Regalías, tiendas propias y fondo de publicidad: 7%, 7%, 7%, 6%, 6% | 6,2% | 21,3% | 2,6 | 18,4% | 5,29% | US$387,75 | US$396,73 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  |  | **US$282,25** | **US$289,28** |

Base (50%) es la continuación de 2024-2026: crecimiento de tiendas y ventas por tienda planas. Conservadora (25%) es el riesgo de que los agregadores sigan quitando pedidos. Disrupción (5%) es un problema en el sistema de franquicias (cierres internacionales, franquiciados en dificultades). Optimista (20%) supone que la entrada en los agregadores y el ritmo de aperturas internacionales sumen crecimiento. En las historias de erosión (Conservadora y Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 1,17; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.

| Crecimiento \ Margen | 16,3% | 18,3% | 20,3% | 22,3% | 24,3% |
|---|---:|---:|---:|---:|---:|
| 0,5% | 165,43 | 199,63 | 233,83 | 268,03 | 302,23 |
| 2,5% | 198,02 | 236,85 | 275,68 | 314,50 | 353,33 |
| 4,5% | 234,26 | 278,27 | 322,27 | 366,27 | 410,28 |
| 6,5% | 274,51 | 324,30 | 374,09 | 423,88 | 473,66 |
| 8,5% | 319,18 | 375,42 | 431,66 | 487,90 | 544,14 |


### Pre-mortem

1. Las ventas mismas tiendas de EE.UU. son negativas varios trimestres: los agregadores hacen irrelevante la logística propia.
2. Grandes franquiciados internacionales (como Domino's Pizza Enterprises o Jubilant) cierran tiendas o reducen aperturas.
3. La inflación de insumos y salarios comprime a los franquiciados y frena la apertura de tiendas.
4. Una recesión con tasas altas encarece la refinanciación de la deuda titulizada.
5. Las promociones permanentes bajan el ticket y el margen del sistema.

**Evidencia en contra de la historia más probable:** las ventas mismas tiendas están planas en EE.UU. y levemente negativas afuera pese a promociones y a la entrada en agregadores. Si esto sigue en 2027, Conservadora gana peso.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Ventas mismas tiendas EE.UU. | +0,1% (2T26) | ≥ +2% | Negativas dos trimestres |
| Ventas mismas tiendas internacionales | −0,1% | ≥ +2% | ≤ −2% |
| Aperturas netas globales | Positivas | ≥ 700 al año | Cierres netos internacionales |
| Margen operativo | 19,3% (2025) | ≥ 19,5% | ≤ 18% |
| Deuda / EBITDA | ~4,5x | ≤ 5x | > 5,5x |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$297,62**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 19% | Margen 20% | Margen 21% |
|---|---:|---:|---:|
| Beta 1,17 | 4,3% (68% de las empresas) | 3,4% (73% de las empresas) | 2,6% (79% de las empresas) |
| Beta 1,07 | 4,0% (70% de las empresas) | 3,1% (75% de las empresas) | 2,3% (80% de las empresas) |

Frente al DCF Base (US$323,13), el valor intrínseco principal, el precio está por debajo en 8%.

Frente al DCF esperado de las historias (US$282,25 con la beta de la hoja; US$289,28 con la propuesta), el precio está por encima en 5% y por encima en 3%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Compuesto de franquicias maduro que crece por tiendas nuevas, con ventas por tienda planas |  |
| Probabilidades | Base 50% / Conservadora 25% / Disrupción 5% / Optimista 20% |  |
| DCF Base hoy (valor intrínseco principal) | US$323,13 |  |
| DCF esperado por probabilidades (complemento) (beta de la hoja / propuesta) | US$282,25 / US$289,28 |  |
| Precio con MOS sobre el DCF esperado | US$183,46 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$93,61 a US$396,73 |  |
| Confianza | Media-alta en el negocio; media en el crecimiento por tienda |  |
| Qué cambiaría la opinión | Ventas mismas tiendas en EE.UU. y aperturas internacionales netas |  |
| Revisión | Resultados del 3T26 (oct-2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [Domino's, Form 10-Q del 2T 2026](https://www.sec.gov/Archives/edgar/data/1286681/000128668126000035/dpz-20260614.htm)
- [Domino's, Form 10-Q del 1T 2026](https://www.sec.gov/Archives/edgar/data/1286681/000128668126000025/dpz-20260322.htm)
- [Domino's, Form 10-K 2025](https://www.sec.gov/Archives/edgar/data/1286681/000119312526062321/dpz-20251228.htm)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
