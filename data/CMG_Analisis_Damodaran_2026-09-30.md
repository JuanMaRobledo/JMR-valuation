---
schema: "jmr-analisis-damodaran-v1"
ticker: "CMG"
analysis_date: "2026-09-30"
---

# Chipotle Mexican Grill, Inc. (CMG) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$23,05 por acción** (Base · Crece por aperturas con comparables bajas).

**Complemento · DCF esperado por probabilidades: US$22,05.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$8,91–30,76. El MOS 35% se aplica al esperado: US$14,34. El antiguo caso técnico de la hoja (US$26,02) se conserva solo como calibración; no es el DCF Base. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), capital invertido operativo, eps básico, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet, roic terminal (criterio damodaran), ventas/capital contrastado con la historia y la industria (23 celdas, con respaldo). DCF esperado US$24,28 → US$22,05. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de US$26,02 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

Chipotle es una cadena de comida mexicana rápida-casual con 4.186 locales propios al 30 de junio de 2026 (4.074 en EE.UU.) y 15 de socios en el exterior, sin franquicias en EE.UU. y sin deuda financiera. Su crecimiento tiene dos motores: aperturas (~8% más unidades al año, con Chipotlanes de alto retorno) y ventas comparables (ticket y tráfico). El primer motor sigue intacto; el segundo se debilitó: en el 2T26 las comparables fueron +2,2%, con tráfico de solo +1,0%, y el margen operativo bajó de 16,9% (2024) a 14,7% LTM por alimentos, aranceles y salarios. En agosto de 2026 un brote de salmonella ligado a jalapeños de un proveedor mexicano, que también afectó a Qdoba, recordó el riesgo que definió la crisis de 2015-2016. La pregunta es si Chipotle es todavía una historia de crecimiento de doble dígito o ya una cadena madura que crece por aperturas con márgenes normales de restaurante.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Las ventas crecen ~8% anual cinco años | Sí | Sí: ~8% de unidades nuevas al año más comparables de 1-3% | Probable |
| El margen operativo vuelve a 17% | Sí | Sí: fue 16,9% en 2024; hoy lo frenan costos y tráfico débil | Incierto |
| El tráfico vuelve a crecer 3-4% anual | Sí | Poco: el consumidor de ingresos medios está presionado | Baja-media |
| Chipotle llega a 7.000 locales en Norteamérica | Sí | Sí: es la meta de la empresa y el ritmo es ~350 aperturas al año | Probable a largo plazo |


### Visión externa: tasas base

Con ventas LTM de US$12.424 millones (US$8.791 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **$7,000-12,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 3,9% y una mediana de 3,5% (desviación estándar 8,3%); sumando una inflación de 2,5%, la mediana nominal ronda 6,0%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · Crece por aperturas con comparables bajas | 7,2% | 43% |
| Conservadora · Tráfico débil y margen presionado | 5,0% | 57% |
| Disrupción · Deterioro de los fundamentales: Crisis de marca o saturación: el tráfico cae | 2,6% | 72% |
| Optimista · Vuelve el tráfico | 10,2% | 28% |

En dólares de 2015 la empresa está en el tramo de US$7.000-12.000 millones: crecer 7,2% anual cinco años (Base) lo logró ~43% de las empresas de ese tamaño; 10,2% (Optimista), ~28%. El crecimiento por aperturas le da a Chipotle una ventaja sobre la tasa base, pero el precio pide algo muy distinto (ver «El precio al final»).


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: las aperturas siguen; el tráfico es la duda.** Chipotle crece por dos motores. El primero son las aperturas: ~8% más locales al año, la mayoría con Chipotlane (ventanilla para pedidos digitales), y ese motor sigue intacto (guía de 350-370 aperturas en 2026). El segundo son las ventas comparables, y ahí está el problema: en el 2T26 fueron +2,2%, con tráfico de solo +1,0%, y la guía del 3T26 es ~+1%, antes del brote de salmonella de agosto. La Base suma ambos: 8% el primer año bajando a 6% en el quinto (7,2% compuesto). Es, en esencia, aperturas más comparables casi planas. No usamos el 14% de 2023-2024 porque se apoyaba en comparables que ya no existen. La visión externa da ~43% de empresas de su tamaño con ese crecimiento: plausible justamente porque las aperturas son un motor que muchas empresas no tienen. La Conservadora (5,0%) extiende la debilidad del consumidor; la Disrupción (2,6%) es una caída del tráfico por saturación o por una crisis sanitaria como la de 2015-2016; la Optimista (10,2%) es el regreso del tráfico. Si las comparables del 3T26 y el 4T26 son negativas, la Conservadora pasa a ser la más probable.

**Margen: volver al máximo de 2024, con arrendamientos dentro.** El margen operativo reportado (con el alquiler como gasto) pasó de 15,8% a 16,9% en 2024 y bajó a 14,7% LTM por alimentos, aranceles y salarios. La Base supone volver a 16% en base reportada; en el modelo eso es 17,3%, porque desde el 1-oct-2026 los arrendamientos se tratan como deuda y el alquiler deja de restar del EBIT (+1,29 pp). Volver al máximo es posible con apalancamiento operativo si vuelve el tráfico; sin tráfico, subir precios choca con la elasticidad del cliente. Por eso el rango es amplio: 13,3% en la Disrupción, 15,3% en la Conservadora y 19,3% en la Optimista. Es el supuesto que más mueve la Base después de la tasa: dos puntos de margen la llevan a US$19,89 (−14%) o US$26,21 (+14%). Lo invalidaría un margen a nivel restaurante por debajo de 24%.

**Reinversión: cada local se paga con caja, y los locales se alquilan.** Chipotle no franquicia en EE.UU.: cada local nuevo se paga con caja propia (capex de US$560-670 millones al año) y además se alquila. Al tratar los arrendamientos como deuda (~US$5.044 millones de valor presente), el capital incluye también los locales alquilados: un restaurante nuevo necesita su local aunque sea alquilado. Revisión del 1-oct-2026: la conversión había dejado el ventas/capital en 1,26/1,16, por debajo de la propia historia (1,56 en 2023-2025, con capex neto y locales arrendados nuevos) y del promedio de restaurantes según Damodaran (1,51). Ahora usa 1,51×: cada dólar de ventas nuevas exige ~US$0,66 de capital propio y arrendado. El retorno sigue siendo alto —los locales se pagan en 2-3 años, ~60% cash-on-cash al segundo año—, por eso el crecimiento crea valor. Después del año 10 la Base conserva un ROIC de 18,4%, el promedio de la industria (por debajo del ROIC actual de ~23%), porque la marca demostró que sobrevive a una crisis sanitaria. Si se perdiera esa ventaja, la Base bajaría a US$15,79 (−31%): es el supuesto con más efecto después de la tasa.

**Descuento, terminal y el peso de la perpetuidad.** El costo de capital va de 9,29% a 9,00%, con beta 1,10. La bottom-up de restaurantes reapalancada con la deuda por arrendamientos da 0,85, menor; la de la hoja es prudente y defendible para una cadena con ~US$5.000 millones de pasivo por alquileres. El crecimiento perpetuo es 4,99% y el terminal explica 70,6% del valor operativo: la mayor parte del valor de Chipotle está más allá del año 10, lo que es lógico para un negocio que todavía abre locales pero hace al resultado muy sensible a la tasa (un punto más la lleva a US$17,64 (−23%); uno menos, a US$32,05 (+39%)).

**Probabilidades y lectura del resultado.** La Base pesa 40%; la Conservadora 35%, cinco puntos más que antes, porque la guía del 3T26 quedó en el piso de la Base y el brote de agosto añade presión; la Disrupción solo 5%, porque el brote vino de un proveedor compartido con Qdoba y la CDC no ve riesgo en curso; la Optimista 20%. El DCF Base es US$23,05 y el esperado US$22,05, frente a un precio de US$31,90. La diferencia con el precio es grande y es la pregunta central: el mercado está pagando por algo más cercano a la Optimista. Las recompras (US$2.783 millones LTM) no se modelan: las acciones se fijan en 1.265,4 millones.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$12.424 millones. Con el crecimiento de la Base llegan a US$17.586 millones en el año 5 y a US$22.869 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 16,3% en el año 1 a 17,3% al final, y se descuentan impuestos (24,1% al principio y 24,5% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$1.659 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$711 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$948 millones el primer año. Cada flujo se trae a hoy con el costo de capital (9,29% al principio, 9,00% al final): los diez años suman US$9.813 millones. Después del año 10 se supone que la empresa crece 4,99% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 18,4%; esa perpetuidad vale hoy US$23.620 millones, 71% del total. Flujos más terminal dan el valor de las operaciones, US$33.433 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$678 millones, más activos no operativos por US$97 millones, menos deuda por US$5.044 millones (incluye los arrendamientos capitalizados). Queda un patrimonio de US$29.163 millones que, repartido entre 1.265,4 millones de acciones, da US$23,05 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 18,59× (peso 25% dentro de los múltiplos); EV/FCFF 30,23× (peso 38% dentro de los múltiplos); P/E 26,72× (peso 12% dentro de los múltiplos); P/FCFE 27,08× (peso 12% dentro de los múltiplos); P/OCF 18,11× (peso 12% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (9,9%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$23,05; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$19,89 | −13,7% |
| Margen objetivo +2 pp | US$26,21 | +13,7% |
| Crecimiento años 1–5 −2 pp | US$20,75 | −10,0% |
| Crecimiento años 1–5 +2 pp | US$25,59 | +11,1% |
| Ventas/capital −20% | US$22,17 | −3,8% |
| Ventas/capital +20% | US$23,63 | +2,5% |
| WACC +1 pp | US$17,64 | −23,5% |
| WACC −1 pp | US$32,05 | +39,1% |
| Crecimiento terminal −0,5 pp | US$21,35 | −7,4% |
| Crecimiento terminal +0,5 pp | US$25,22 | +9,4% |
| ROIC terminal = costo de capital | US$15,79 | −31,5% |
| Acciones +5% | US$21,95 | −4,8% |


### Piezas del valor

**Crecimiento.** Ventas de US$9.872 millones (2023, +14,3%), US$11.314 millones (2024, +14,6%) y US$11.926 millones (2025, +5,4%); LTM US$12.424 millones. En el 2T26 los ingresos crecieron 9,3% (US$3.349 millones) con comparables de +2,2% (+1,2% ticket, +1,0% tráfico) y 38,3% de ventas digitales. El salto de 2025 hacia abajo viene de comparables planas o negativas; las aperturas sostuvieron el crecimiento. Para 2026 la empresa espera comparables de un dígito bajo y 350-370 aperturas; para el 3T26 anticipó comparables de ~+1%, con ~200 pb de freno por preocupaciones sanitarias de la industria, antes del brote de agosto.

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 9.872 | 11.314 | 11.926 | 12.424 |
| Crecimiento | +14,3% | +14,6% | +5,4% | — |
| Margen operativo | 15,8% | 16,9% | 16,2% | 14,7% |
| FCFF (hoja) | 265 | 1.370 | 1.109 | — |

**Márgenes.** El margen operativo (con el alquiler dentro del EBIT, como lo reporta la empresa) pasó de 15,8% a 16,9% y bajó a 14,7% LTM. La hoja supone 15% el próximo año y 17% de objetivo, es decir, volver al máximo de 2024. Es posible con apalancamiento operativo si vuelve el tráfico; sin tráfico, los aumentos de precio compiten con la elasticidad del consumidor. Las historias van de 12% a 18%.

**Reinversión y retorno.** Todo el crecimiento es propio: cada local nuevo se paga con caja (capex de US$560-670 millones al año). La hoja usa un sales-to-capital de 1,51 con los arrendamientos incluidos: la historia 2023-2025 da 1,56 (capex neto más locales arrendados nuevos) y el promedio de Restaurant/Dining según Damodaran es 1,51. El retorno sobre el capital es alto (los locales se pagan en 2-3 años), así que el crecimiento crea valor mientras la economía unitaria se sostenga. La empresa además recompró US$2.783 millones LTM. Ventaja durable: marca probada de 30 años que superó la crisis sanitaria de 2015-2016, con ROIC (con arrendamientos) de 15-22%. El ROIC después del año 10 es 18,4%, el promedio de su industria según Damodaran. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$5.044 millones, compromisos del 10-K al 2025-12-31) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$160 millones, +1,29 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,41 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usa una beta de 1,10. La beta bottom-up de Restaurant/Dining (64 empresas, 0,78 desapalancada y corregida por caja) reapalancada con la deuda por arrendamientos (que ahora el modelo trata como deuda, criterio Damodaran) da 0,85, y el DCF técnico anterior sube de US$26,02 a US$27,78. Una cadena con un pasivo por arrendamientos de ~US$5.000 millones tiene apalancamiento operativo real; la beta de la hoja, algo mayor que la bottom-up, es prudente y defendible.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF técnico anterior por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,10 | 9,9% | 9,3% | US$26,02 |
| Bottom-up del sector (Restaurant/Dining, reapalancada) | 0,85 | 8,8% | 8,3% | US$27,78 |


### Calibración técnica anterior Conservador/Base/Optimista (referencia auxiliar)

| Supuesto | Conservador | Base | Optimista |
|---|---:|---:|---:|
| Crecimiento año 1 | 5,0% | 8,0% | 11,0% |
| Crecimiento años 2–5 | 5,0% | 8,0% | 11,0% |
| Margen año 1 (base ajustada del modelo) | 16,3% | 16,3% | 16,3% |
| Margen objetivo | 15,3% | 18,3% | 21,3% |

Ventas/capital: 1,5x en años 1–5 y 1,5x en 6–10. WACC: 9,3%. Ke: 9,9%. Impuesto efectivo: 24,1%. Convergencia: 5 años. Estos parámetros son escenarios del analista, no cifras reportadas. Los casos Conservador, Base y Optimista de la hoja ya no son escenarios activos: sirven de calibración y de supuestos auxiliares de múltiplos. No confundir el antiguo caso técnico Base con la tesis Base.


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF técnico anterior | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 23,2% | 18,4% | 9,0% | 18,4% | US$26,02 | US$17,75 |

Fuentes de ventaja: Marca probada (30 años; se recuperó de la crisis de seguridad alimentaria de 2015-2018) con economía por local superior. Evidencia: ROIC 15-22% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$23,05 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$22,05. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene aplicando descuentos al antiguo caso técnico de la hoja (US$26,02) ni mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$12.424 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). |
| Margen inicial del DCF | 16,3% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 24,08% en años 1–5; 24,50% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 9,29% → 9,00% | Tasa libre de riesgo 4,99%, beta 1,10, ERP 4,46%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 1,51x en años 1–5; 1,51x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 4,99%; Disrupción: 2,00% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (2,00%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Conservadora/Optimista: 18,40%; Disrupción: 9,00% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 678; deuda 5.044; activos no operativos 97; acciones 1.265,4 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 12.424 × 1,08 = US$13.417,70 millones. Frente a 12.424, el crecimiento consolidado es 8,00%. En los años 2–5 es 8,00%, 7,00%, 7,00%, 6,00%; las ventas del año 5 son US$17.586,34 millones. El 7,2% de la tabla es el crecimiento anual compuesto de los cinco años: (17.586,34 / 12.424)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 13.417,70 × 16,29% × (1 − 24,08%) = US$1.659,19 millones. La reinversión es US$710,87 millones y el FCFF es US$948,32 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,00%. Reinversión terminal sobre el NOPAT: Base, 27,1% (4,99% / 18,40%); Conservadora, 27,1% (4,99% / 18,40%); Disrupción, 22,2% (2,00% / 9,00%); Optimista, 27,1% (4,99% / 18,40%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en «Escenarios e historias»: ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · Crece por aperturas con comparables bajas** — probabilidad 40%; valor terminal 56.957 (VP 23.620); DCF US$23,05 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 13.418 | 8,0% | 16,3% | 1.659 | 711 | 948 | 9,3% | 868 |
| 2 | 14.491 | 8,0% | 16,7% | 1.836 | 672 | 1.164 | 9,3% | 975 |
| 3 | 15.505 | 7,0% | 16,9% | 1.988 | 719 | 1.269 | 9,3% | 972 |
| 4 | 16.591 | 7,0% | 17,1% | 2.152 | 659 | 1.493 | 9,3% | 1.047 |
| 5 | 17.586 | 6,0% | 17,3% | 2.308 | 675 | 1.633 | 9,3% | 1.047 |
| 6 | 18.606 | 5,8% | 17,3% | 2.439 | 690 | 1.750 | 9,2% | 1.028 |
| 7 | 19.647 | 5,6% | 17,3% | 2.573 | 702 | 1.871 | 9,2% | 1.006 |
| 8 | 20.707 | 5,4% | 17,3% | 2.709 | 712 | 1.997 | 9,1% | 984 |
| 9 | 21.782 | 5,2% | 17,3% | 2.846 | 720 | 2.126 | 9,1% | 961 |
| 10 | 22.869 | 5,0% | 17,3% | 2.985 | 756 | 2.229 | 9,0% | 924 |
| Terminal | 24.010 | 5,0% | 17,3% | 3.134 | 850 | 2.284 | 9,0% | — |

**Conservadora · Tráfico débil y margen presionado** — probabilidad 35%; valor terminal 43.711 (VP 18.127); DCF US$17,82 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 13.169 | 6,0% | 16,3% | 1.628 | 436 | 1.192 | 9,3% | 1.091 |
| 2 | 13.828 | 5,0% | 15,9% | 1.668 | 458 | 1.210 | 9,3% | 1.013 |
| 3 | 14.519 | 5,0% | 15,7% | 1.729 | 481 | 1.248 | 9,3% | 956 |
| 4 | 15.245 | 5,0% | 15,5% | 1.793 | 404 | 1.389 | 9,3% | 973 |
| 5 | 15.855 | 4,0% | 15,3% | 1.840 | 441 | 1.399 | 9,3% | 898 |
| 6 | 16.520 | 4,2% | 15,3% | 1.915 | 481 | 1.434 | 9,2% | 842 |
| 7 | 17.247 | 4,4% | 15,3% | 1.997 | 525 | 1.473 | 9,2% | 792 |
| 8 | 18.039 | 4,6% | 15,3% | 2.087 | 572 | 1.514 | 9,1% | 746 |
| 9 | 18.903 | 4,8% | 15,3% | 2.184 | 625 | 1.560 | 9,1% | 705 |
| 10 | 19.847 | 5,0% | 15,3% | 2.291 | 656 | 1.635 | 9,0% | 678 |
| Terminal | 20.837 | 5,0% | 15,3% | 2.405 | 652 | 1.753 | 9,0% | — |

**Disrupción · Deterioro de los fundamentales: Crisis de marca o saturación: el tráfico cae** — probabilidad 5%; valor terminal 17.731 (VP 7.353); DCF US$8,91 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 12.797 | 3,0% | 16,3% | 1.582 | 254 | 1.328 | 9,3% | 1.215 |
| 2 | 13.180 | 3,0% | 15,1% | 1.510 | 262 | 1.248 | 9,3% | 1.045 |
| 3 | 13.576 | 3,0% | 14,5% | 1.493 | 180 | 1.313 | 9,3% | 1.006 |
| 4 | 13.847 | 2,0% | 13,9% | 1.460 | 183 | 1.277 | 9,3% | 895 |
| 5 | 14.124 | 2,0% | 13,3% | 1.425 | 187 | 1.238 | 9,3% | 794 |
| 6 | 14.407 | 2,0% | 13,3% | 1.452 | 191 | 1.261 | 9,2% | 740 |
| 7 | 14.695 | 2,0% | 13,3% | 1.479 | 195 | 1.285 | 9,2% | 691 |
| 8 | 14.989 | 2,0% | 13,3% | 1.507 | 199 | 1.309 | 9,1% | 645 |
| 9 | 15.289 | 2,0% | 13,3% | 1.536 | 202 | 1.333 | 9,1% | 603 |
| 10 | 15.594 | 2,0% | 13,3% | 1.564 | 207 | 1.358 | 9,0% | 563 |
| Terminal | 15.906 | 2,0% | 13,3% | 1.596 | 355 | 1.241 | 9,0% | — |

**Optimista · Vuelve el tráfico** — probabilidad 20%; valor terminal 77.179 (VP 32.006); DCF US$30,76 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 13.790 | 11,0% | 16,3% | 1.705 | 1.005 | 701 | 9,3% | 641 |
| 2 | 15.307 | 11,0% | 17,5% | 2.032 | 1.014 | 1.019 | 9,3% | 853 |
| 3 | 16.838 | 10,0% | 18,1% | 2.312 | 1.115 | 1.197 | 9,3% | 917 |
| 4 | 18.522 | 10,0% | 18,7% | 2.628 | 1.104 | 1.524 | 9,3% | 1.068 |
| 5 | 20.189 | 9,0% | 19,3% | 2.956 | 1.096 | 1.860 | 9,3% | 1.193 |
| 6 | 21.844 | 8,2% | 19,3% | 3.195 | 1.070 | 2.125 | 9,2% | 1.248 |
| 7 | 23.460 | 7,4% | 19,3% | 3.428 | 1.024 | 2.403 | 9,2% | 1.293 |
| 8 | 25.006 | 6,6% | 19,3% | 3.650 | 959 | 2.690 | 9,1% | 1.326 |
| 9 | 26.455 | 5,8% | 19,3% | 3.857 | 874 | 2.982 | 9,1% | 1.348 |
| 10 | 27.775 | 5,0% | 19,3% | 4.045 | 918 | 3.127 | 9,0% | 1.297 |
| Terminal | 29.161 | 5,0% | 19,3% | 4.246 | 1.152 | 3.095 | 9,0% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 9.812,79 | 23.619,90 | 33.432,68 | 29.163,40 | 23,05 |
| Conservadora | 8.695,62 | 18.126,92 | 26.822,54 | 22.553,26 | 17,82 |
| Disrupción | 8.197,31 | 7.352,84 | 15.550,14 | 11.280,86 | 8,91 |
| Optimista | 11.184,31 | 32.005,69 | 43.190,01 | 38.920,73 | 30,76 |

Ejemplo Base: (9.812,79 + 23.619,90 + 678 + 97 − 5.044) / 1.265,4 = US$23,05 por acción. El terminal representa 70,6% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 40% / 35% / 5% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,40 × 23,046787 + 0,35 × 17,823029 + 0,05 × 8,914861 + 0,20 × 30,757648 = US$22,054047 ≈ US$22,05. Los aportes son US$9,22 + US$6,24 + US$0,45 + US$6,15 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 22,054047 × 0,65 = US$14,335131 ≈ US$14,34. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base ni al antiguo caso técnico de la hoja: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Los DCF completos empiezan en las filas 22 (Base), 46 (Conservadora), 70 (Disrupción) y 94 (Optimista); sus valores por acción están en B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$23,05, es el valor intrínseco principal. El DCF esperado de US$22,05 combina las cuatro tesis con sus probabilidades y se presenta como complemento. La antigua calibración técnica Conservador/Base/Optimista de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: Crece por aperturas con comparables bajas

**Qué plantea.** Es lo que muestran 2025-2026: unidades nuevas y comparables de 1-3%.

**Traducción al modelo.** Crece 8%, 8%, 7%, 7%, 6%. El crecimiento anual compuesto de cinco años es 7,2%; el margen operativo objetivo es 17,3%. El ROIC terminal es 18,4%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 40%; DCF: US$23,05 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (ventas comparables: +2,2% (2T26); guía 3T26 ~+1%; tráfico (transacciones): +1,0% (2T26); margen a nivel restaurante: 25,2% (2T26; 27,4% un año antes)). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: Tráfico débil y margen presionado

**Qué plantea.** Extiende la debilidad del consumidor y los costos; gana 5 pp porque la guía del 3T26 (~+1%) quedó en el piso de Base y el brote de salmonella de agosto, no incluido en esa guía, añade presión al tráfico de corto plazo.

**Traducción al modelo.** Crece 6%, 5%, 5%, 5%, 4%. El crecimiento anual compuesto de cinco años es 5,0%; el margen operativo objetivo es 15,3%. El ROIC terminal es 18,4%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 35%; DCF: US$17,82 por acción.

**Cómo contrastarla.** La apoyarían: ventas comparables: negativas dos trimestres; tráfico (transacciones): negativo; margen a nivel restaurante: ≤ 24%; margen operativo: ≤ 13%.


#### Disrupción · Deterioro de los fundamentales: Crisis de marca o saturación: el tráfico cae

**Qué plantea.** Es una caída del tráfico por saturación (canibalización) o por una crisis de seguridad alimentaria que dañe la marca como en 2015-2016; el brote de 2026 vino de un proveedor compartido con Qdoba y la CDC no ve riesgo en curso, por eso Disrupción no sube.

**Traducción al modelo.** Crece 3%, 3%, 3%, 2%, 2%. El crecimiento anual compuesto de cinco años es 2,6%; el margen operativo objetivo es 13,3%. El ROIC terminal es el costo de capital (9,00%). El crecimiento terminal es 2,00%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 5%; DCF: US$8,91 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: ventas comparables: negativas dos trimestres; tráfico (transacciones): negativo; margen a nivel restaurante: ≤ 24%; margen operativo: ≤ 13%.


#### Optimista: Vuelve el tráfico

**Qué plantea.** Es el regreso del tráfico por nuevas proteínas, velocidad de servicio y Chipotlanes.

**Traducción al modelo.** Crece 11%, 11%, 10%, 10%, 9%. El crecimiento anual compuesto de cinco años es 10,2%; el margen operativo objetivo es 19,3%. El ROIC terminal es 18,4%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 20%; DCF: US$30,76 por acción.

**Cómo contrastarla.** La confirmarían: ventas comparables: ≥ +3%; tráfico (transacciones): ≥ +2%; margen a nivel restaurante: ≥ 26,5%; margen operativo: ≥ 16%.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 4,99%; Disrupción: 2,00%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,10) | Valor/acción (beta 0,85) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| **Base · Crece por aperturas con comparables bajas** | 40% | 8%, 8%, 7%, 7%, 6% | 7,2% | 17,3% | 1,5 | 18,4% | 4,99% | US$23,05 | US$24,61 |
| **Conservadora · Tráfico débil y margen presionado** | 35% | 6%, 5%, 5%, 5%, 4% | 5,0% | 15,3% | 1,5 | 18,4% | 4,99% | US$17,82 | US$19,04 |
| **Disrupción · Deterioro de los fundamentales: Crisis de marca o saturación: el tráfico cae** | 5% | 3%, 3%, 3%, 2%, 2% | 2,6% | 13,3% | 1,5 | = costo de capital | 2,00% | US$8,91 | US$9,55 |
| **Optimista · Vuelve el tráfico** | 20% | 11%, 11%, 10%, 10%, 9% | 10,2% | 19,3% | 1,5 | 18,4% | 4,99% | US$30,76 | US$32,83 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  |  | **US$22,05** | **US$23,55** |

Base (40%) es lo que muestran 2025-2026: unidades nuevas y comparables de 1-3%. Conservadora (35%) extiende la debilidad del consumidor y los costos; gana 5 pp porque la guía del 3T26 (~+1%) quedó en el piso de Base y el brote de salmonella de agosto, no incluido en esa guía, añade presión al tráfico de corto plazo. Disrupción (5%) es una caída del tráfico por saturación (canibalización) o por una crisis de seguridad alimentaria que dañe la marca como en 2015-2016; el brote de 2026 vino de un proveedor compartido con Qdoba y la CDC no ve riesgo en curso, por eso Disrupción no sube. Optimista (20%) es el regreso del tráfico por nuevas proteínas, velocidad de servicio y Chipotlanes. En las historias de erosión (Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF técnico anterior (beta 1,10; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF técnico anterior de la hoja.

| Crecimiento \ Margen | 14,3% | 16,3% | 18,3% | 20,3% | 22,3% |
|---|---:|---:|---:|---:|---:|
| 4,0% | 15,74 | 18,38 | 21,02 | 23,66 | 26,30 |
| 6,0% | 17,41 | 20,40 | 23,39 | 26,38 | 29,37 |
| 8,0% | 19,26 | 22,64 | 26,02 | 29,40 | 32,78 |
| 10,0% | 21,31 | 25,13 | 28,94 | 32,75 | 36,56 |
| 12,0% | 23,58 | 27,87 | 32,17 | 36,46 | 40,76 |


### Pre-mortem

1. Las comparables siguen planas o negativas: la marca perdió frescura frente a Cava, Sweetgreen y cadenas más baratas.
2. El margen no vuelve: alimentos, aranceles y salarios suben más rápido que el precio que el cliente acepta.
3. Las aperturas canibalizan a los locales existentes y bajan el retorno por unidad.
4. El brote de salmonella de agosto de 2026 (431 casos en 32 estados al 19 de agosto) deja demandas y una percepción de riesgo que frena el tráfico durante varios trimestres, como en 2015-2016.
5. La expansión internacional (socios en Oriente Medio, Asia, Latinoamérica) consume atención sin aportar.

**Evidencia en contra de la historia más probable:** el tráfico del 2T26 (+1,0%), la guía de ~+1% para el 3T26 y la caída del margen muestran que ni siquiera la historia Base está garantizada; si las comparables del 3T26 y el 4T26 son negativas por el brote, Conservadora pasa a ser la más probable.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Ventas comparables | +2,2% (2T26); guía 3T26 ~+1% | ≥ +3% | Negativas dos trimestres |
| Tráfico (transacciones) | +1,0% (2T26) | ≥ +2% | Negativo |
| Margen a nivel restaurante | 25,2% (2T26; 27,4% un año antes) | ≥ 26,5% | ≤ 24% |
| Margen operativo | 14,7% LTM | ≥ 16% | ≤ 13% |
| Aperturas al año (80% con Chipotlane) | 350-370 guía 2026 | ≥ 350 con productividad ≥ 80% | < 250 o productividad < 75% |
| Retorno de locales nuevos | ~60% cash-on-cash al año 2; productividad ~80% | Estable o en alza | Caída |
| Seguridad alimentaria y demandas | Brote de salmonella de agosto de 2026; CDC sin riesgo en curso | Sin nuevos brotes ni caída del tráfico por el caso | Nuevo brote o tráfico negativo atribuido al caso |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$31,90**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 16% | Margen 18% | Margen 20% |
|---|---:|---:|---:|
| Beta 1,10 | 14,6% (13% de las empresas) | 11,8% (20% de las empresas) | 9,5% (31% de las empresas) |
| Beta 0,85 | 13,3% (16% de las empresas) | 10,6% (26% de las empresas) | 8,3% (37% de las empresas) |

Frente al DCF Base (US$23,05), el valor intrínseco principal, el precio está por encima en 38%.

Frente al DCF esperado de las historias (US$22,05 con la beta de la hoja; US$23,55 con la propuesta), el precio está por encima en 45% y por encima en 35%, respectivamente. El precio de referencia de la valoración (US$31,90, hoja de Google al 30 de septiembre de 2026; cierre de ese día US$31,76) queda 34% por encima del DCF técnico anterior (US$23,86) y por encima de la historia Optimista (US$30,77), la más optimista. Con los arrendamientos como deuda (márgenes en base ajustada, +1,3 pp), el DCF inverso pide 8-15% de crecimiento anual en los años 1-5 con márgenes de 16-20%, algo que lograron 13-37% de las empresas de este tamaño; con el margen objetivo de la hoja (18,3% ajustado) y su beta pide 11,8%, bastante más que el 8% de la hoja. ¿Qué sabe el mercado que yo no? Paga por la calidad del negocio (retornos por local, sin deuda financiera, recompras) y por una pista de aperturas de muchos años. Es un argumento de duración: si crees que crecerá 7-8% durante quince años y no cinco, el valor cierra buena parte de la brecha. El brote de agosto pesó en la acción: cayó 9,7% el 4 de agosto (de US$37,46 a US$33,82) y terminó septiembre cerca de US$32, por debajo del salto posterior a los resultados (US$38,52 el 30 de julio).


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Cadena de restaurantes propios con gran economía unitaria y tráfico débil |  |
| Probabilidades | Base 40% / Conservadora 35% / Disrupción 5% / Optimista 20% |  |
| DCF Base hoy (valor intrínseco principal) | US$23,05 |  |
| DCF esperado por probabilidades (complemento) (beta de la hoja / propuesta) | US$22,05 / US$23,55 |  |
| Precio con MOS sobre el DCF esperado | US$14,34 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$8,91 a US$32,83 |  |
| Confianza | Media: las aperturas son predecibles; el tráfico y el margen no |  |
| Qué cambiaría la opinión | Comparables y tráfico de los próximos dos trimestres; margen operativo |  |
| Revisión | Resultados del 3T26 (fines de octubre de 2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [Chipotle, Form 10-Q del 2T 2026](https://www.sec.gov/Archives/edgar/data/1058090/000105809026000066/cmg-20260630.htm)
- [Chipotle, comunicado de resultados del 2T 2026 (8-K, 29 de julio de 2026)](https://www.sec.gov/Archives/edgar/data/1058090/000105809026000063/cmg-20260729xex991.htm)
- [Chipotle, 8-K sobre la investigación de salmonella (5 de agosto de 2026)](https://www.sec.gov/Archives/edgar/data/1058090/000105809026000069/cmg-20260804.htm)
- [CDC, Investigation Update: Salmonella Outbreak, August 2026](https://www.cdc.gov/salmonella/outbreaks/javiana-08-26/investigation.html)
- [Chipotle, transcripción de la llamada del 2T 2026 (The Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/08/07/chipotle-cmg-q2-2026-earnings-call-transcript/)
- [Chipotle, Form 10-K 2025](https://www.sec.gov/Archives/edgar/data/1058090/000105809026000009/cmg-20251231.htm)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
