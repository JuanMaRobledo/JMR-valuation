---
schema: "jmr-analisis-damodaran-v1"
ticker: "ADBE"
analysis_date: "2026-09-30"
---

# Adobe Inc. (ADBE) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$454,78 por acción** (Base · La IA se cobra dentro de la suscripción).

**Complemento · DCF esperado por probabilidades: US$355,49.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$174,89–566,58. El MOS 35% se aplica al esperado: US$231,07. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), capital invertido operativo, deuda de balance sin arrendamientos operativos (14 celdas, con respaldo). DCF esperado US$364,33 → US$355,49. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (bloque Base de 'Valuation output': US$454,78 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja calcula estos cuatro DCF en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


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
| Base · La IA se cobra dentro de la suscripción | 8,1% | 34% |
| Conservadora · Erosión gradual frente a Figma y Canva | 5,4% | 50% |
| Disrupción · Deterioro de los fundamentales: La IA generativa comoditiza la creatividad | 0,9% | 76% |
| Optimista · La IA amplía el mercado de Adobe | 11,0% | 21% |

En dólares de 2015 la empresa está en el tramo de US$12.000-25.000 millones: crecer 8,1% anual cinco años (Base) lo logró ~34% de las empresas de ese tamaño; 11,0% (Optimista), ~21%. Adobe tiene razones para estar arriba de la mediana: suscripción con alta retención, subidas de precio y venta cruzada de IA. Aun así, el DCF de la hoja (10,4% anual en los años 1-5) ya supone un resultado del cuartil superior, y la visión externa pide descontar esa confianza.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: por qué la Base desacelera.** La trayectoria parte del negocio recurrente y del desglose de clientes conciliado con el último 10-Q, no de aplicar un porcentaje idéntico a todas las ventas. El grupo profesional aumenta 10% en el primer año y termina creciendo 6% en el quinto; documentos y consumidores pasan de 14% a 8%. El mecanismo supuesto es que las funciones de IA sostengan renovaciones y permitan aumentar el ingreso por cliente, mientras la mayor escala y las alternativas competitivas moderan la expansión. Esta elección produce 10,8% consolidado en el primer año y 8,1% de CAGR a cinco años. El CAGR resume esa trayectoria; no es una tasa constante. Una Base con crecimiento perpetuamente igual al ritmo reciente exigiría demostrar que Adobe puede mantener ganancias de clientes y monetización a una escala mucho mayor. Los porcentajes son juicio del analista, no una guía publicada por Adobe. La contribución de adquisiciones debe separarse antes de calificar todo el crecimiento como orgánico.

**Margen: por qué 40,1% y qué podría impedirlo.** El objetivo de 40,1% (40,0% antes del ajuste por arrendamientos) es un margen operativo ajustado por capitalización de I+D; no se compara directamente con el margen GAAP LTM de 35,70%. La hipótesis de la Base es que la escala de las suscripciones y una mezcla más favorable compensen el cómputo adicional y la inversión comercial de la IA. Por eso se usa una mejora moderada frente al margen ajustado inicial, en vez de extrapolar el máximo de la Optimista. La Conservadora queda en 37,1% porque defender clientes puede exigir descuentos y producto adicional sin cobrarlo íntegramente; la Disrupción cae a 32,1% por menor poder de precio y costos que no se ajustan tan rápido como las ventas. La Optimista exige 43,1% y crecimiento mayor a la vez: solo tiene sentido si la monetización supera los costos incrementales. Ninguno de estos márgenes es una promesa de Adobe. Revisaría la Base si el ingreso por cliente aumenta menos que el costo de prestar funciones de IA.

**Reinversión y ventas/capital: una hipótesis todavía incompleta.** El modelo usa 1,23× en los años 1-5 y 1,23× en los años 6-10, con el capital arrendado y el I+D capitalizado: cada dólar de ventas nuevas exige ~US$0,81 de capital. Es el ventas/capital de Adobe hoy (1,20 con I+D capitalizado) y rinde ~37% sobre el capital nuevo con el margen objetivo, igual a su ROIC actual (37%) y por encima del de su industria (20,6%): el capital nuevo rinde lo mismo que el existente, ni más ni menos (Damodaran, Investment Valuation, cap. 11, p. 44-46). El marginal de tres años (13×) no sirve de referencia porque las recompras reducen el capital contable. El del sector (1,54) no incluye el I+D capitalizado. Si para defenderse de la IA Adobe vuelve a comprar (como intentó con Figma), la reinversión real sería mayor. Con ±20% en el ventas/capital el DCF Base va de US$447,16 (−2%) a US$459,86 (+1%). En Disrupción, la reinversión negativa supone recuperar capital al contraerse las ventas, un beneficio que puede exagerarse si los intangibles no son recuperables.

**I+D: por qué la vida útil importa.** Capitalizar I+D reconoce que una parte del gasto genera beneficios durante varios años. La vida útil de tres años es una convención del modelo, no un dato reportado ni evidencia de que todo desarrollo tenga ese plazo. En productos expuestos a cambios rápidos de IA, parte del desarrollo puede quedar obsoleto antes; plataformas e integraciones pueden durar más. La vida elegida modifica tanto la amortización y el EBIT ajustado como el activo económico y el ROIC, por lo que deben evaluarse conjuntamente. La corrección aritmética de I+D no valida su vida útil. Falta contrastar plazos alternativos con la persistencia de los beneficios, conservando definiciones homogéneas.

**Descuento y valor terminal: dónde se concentra el juicio.** Se mantiene el WACC de la hoja, aproximadamente 10,93% al inicio y 8,99% al final, para que las diferencias entre historias provengan de sus flujos. Esa convergencia supone que el riesgo y la estructura financiera se normalicen; no es una consecuencia automática de ser una empresa grande. Base y Optimista conservan ROIC terminal de 20,6% como ancla sectorial condicionada a una ventaja duradera, mientras Conservadora y Disrupción convergen al costo de capital. El 20,6% no es un ROIC futuro observado de Adobe. El crecimiento terminal de 5,29% en Base, Conservadora y Optimista es exigente y requiere moneda, inflación y crecimiento económico de largo plazo compatibles; la Conservadora incluso vuelve a acelerar desde 3,54% en el año 5, una recuperación que necesita soporte adicional. Disrupción se estabiliza en 0,00% nominal. Como el terminal explica 67,7% del valor operativo de la Base, estos supuestos pesan mucho en US$454,78 y deben seguir señalados como condicionados, no plenamente auditados.

**Acciones y probabilidades: límites del valor por acción.** Las cuatro historias conservan 389,2 millones de acciones y no proyectan recompras ni dilución adicional. Esta elección facilita compararlas, pero no demuestra que la compensación en acciones carezca de costo. Más acciones, manteniendo el mismo patrimonio, reducen el DCF por acción; una recompra también consume caja y debe modelarse de forma consistente. La Base es la trayectoria central defendida; el esperado de US$355,49 combina desenlaces distintos y pesos subjetivos. Cambiar esos pesos modifica el esperado y el MOS, sin cambiar por sí solo el DCF de la Base. La política vigente mantiene MOS de 35% sobre el esperado: US$231,07.

**Fuentes y alcance.** Punto de partida contable: [Adobe 10-Q, cierre 28-ago-2026](https://www.sec.gov/Archives/edgar/data/796343/000079634326000156/adbe-20260828.htm). Límite conceptual del crecimiento perpetuo: [Damodaran, The Stable Growth Rate](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/valquestions/stablegrowthrate.htm), revisado 1-oct-2026. Los porcentajes de escenarios y elecciones de capital son hipótesis del modelo. Esta ampliación explica la selección y sus límites; no declara resueltos los controles económicos pendientes.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$25.970 millones. Con el crecimiento de la Base llegan a US$38.347 millones en el año 5 y a US$50.741 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 38,6% en el año 1 a 40,1% al final, y se descuentan impuestos (21,5% al principio y 25,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$8.712 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$2.083 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$6.630 millones el primer año. Cada flujo se trae a hoy con el costo de capital (10,93% al principio, 8,99% al final): los diez años suman US$57.597 millones. Después del año 10 se supone que la empresa crece 5,29% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 20,6%; esa perpetuidad vale hoy US$120.491 millones, 68% del total. Flujos más terminal dan el valor de las operaciones, US$178.088 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$5.639 millones, menos deuda por US$6.727 millones (incluye los arrendamientos capitalizados). Queda un patrimonio de US$177.000 millones que, repartido entre 389,2 millones de acciones, da US$454,78 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 18,34× (peso 33% dentro de los múltiplos); EV/FCFF 19,75× (peso 17% dentro de los múltiplos); P/E 23,87× (peso 33% dentro de los múltiplos); P/FCFE 18,52× (peso 8% dentro de los múltiplos); P/OCF 18,26× (peso 8% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (11,4%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$454,78; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$431,76 | −5,1% |
| Margen objetivo +2 pp | US$477,79 | +5,1% |
| Crecimiento años 1–5 −2 pp | US$410,10 | −9,8% |
| Crecimiento años 1–5 +2 pp | US$504,38 | +10,9% |
| Ventas/capital −20% | US$447,16 | −1,7% |
| Ventas/capital +20% | US$459,86 | +1,1% |
| WACC +1 pp | US$361,08 | −20,6% |
| WACC −1 pp | US$617,18 | +35,7% |
| Crecimiento terminal −0,5 pp | US$421,96 | −7,2% |
| Crecimiento terminal +0,5 pp | US$497,63 | +9,4% |
| ROIC terminal = costo de capital | US$316,75 | −30,4% |
| Acciones +5% | US$433,12 | −4,8% |


### Piezas del valor

**Crecimiento.** Las ventas crecieron 10,8% en FY24 y 10,5% en FY25; la guía FY26 (US$26.576-26.626 millones) implica ~12%. En el 3T FY26, Creative & Marketing Professionals facturó US$4.700 millones (+13%) y Business Professionals & Consumers US$1.900 millones (+16%). La reorganización de segmentos de 2026 no deja comparar series largas por segmento: la división LTM de las historias es una estimación propia con el peso del 3T (≈70% / 28% / 2%).

| US$ millones | FY23 | FY24 | FY25 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 19.409 | 21.505 | 23.769 | 25.970 |
| Crecimiento | +10,2% | +10,8% | +10,5% | — |
| Margen operativo GAAP | 34,3% | 31,3% | 36,6% | 35,7% |
| FCFF (hoja) | 6.102 | 6.749 | 8.702 | — |

**Márgenes.** El margen de FY24 (31,3%) está deprimido por el cargo de US$1.000 millones por la ruptura del acuerdo con Figma; sin él, la serie va de ~34% a ~36-37%. La hoja supone 38,5% el próximo año y 40% como objetivo. Es alcanzable por escala, pero la IA suma costo de cómputo (entrenar e inferir Firefly) y la competencia empuja a regalar créditos de IA. Por eso las historias van de 32% (comoditización) a 43% (la IA amplía el mercado).

**Reinversión y retorno.** Adobe casi no necesita capital para crecer: el capex de FY25 fue US$179 millones (~0,8% de las ventas) y el FCFF, ~US$8.700 millones. La hoja usa un ventas/capital de 1,23 (años 1-5) y 1,23 (años 6-10): con margen objetivo de 40,1% e impuesto marginal de 25%, cada dólar de capital nuevo rinde ~37% y ~37%, sin superar el mayor entre su ROIC actual (37,0%) y el de su industria (20,6%) (Damodaran, Investment Valuation cap. 11, p. 45; revisión del 4-oct-2026). Antes 3,77 y 4,21, que implicaban ~113% y ~126% sobre el capital nuevo. El riesgo está en las compras: si para defenderse de la IA Adobe vuelve a comprar (como intentó con Figma por US$20.000 millones), la reinversión real sería mucho mayor que la del DCF. Ventaja durable: costos de cambio y estándar de la industria creativa y documental, con ROIC en alza (38% → 59%). El ROIC después del año 10 es 20,6%, el promedio de su industria según Damodaran llevado a la base con I+D capitalizado. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Ventas/capital: las referencias de Damodaran.** Damodaran elige el ventas/capital mirando el de la empresa hoy, el marginal de los últimos años y el promedio del sector, y comprueba que el rendimiento que implica sobre el capital nuevo sea creíble frente a lo que gana la empresa o su sector (Investment Valuation, cap. 11, p. 44-46). El marginal es volátil: recompras de acciones y adquisiciones mueven el capital contable. El usado está dentro del rango de las referencias.

| Referencia | Ventas/capital | Detalle |
|---|---:|---|
| Empresa hoy | 1,20 | ventas LTM 25.970,0 / capital invertido 21.620,8 millones (con I+D capitalizado a 3 años) |
| Marginal, último año | — | Δventas 2.264,0 / Δcapital -125,0 millones (Nov '24 → Nov '25): el capital o las ventas no crecieron (recompras, venta de negocios o caída de ventas), no hay inversión que medir |
| Marginal, últimos tres años | 13,33 | Δventas 6.163,0 / Δcapital 462,3 millones (Dec '22 → Nov '25) |
| Sector (Damodaran, enero de 2026) | 1,54 | Software (System & Application) |
| Usado en la hoja | 1,23 / 1,23 | años 1-5 / 6-10; rinde ~37% / ~37% sobre el capital nuevo (ROIC actual 37,0%) |

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$367 millones, compromisos del 10-Q al 2026-08-28) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$23 millones, +0,09 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,01 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** Beta bottom-up (Damodaran, 5-oct-2026): la desapalancada de Software (System & Application) en EE.UU., corregida por caja (1,25; 309 empresas, enero de 2026), reapalancada con la D/E de mercado de Adobe (~6%) da 1,31. Se usa la tabla de EE.UU. porque Adobe vende 53% en EE.UU. y 60% en América; antes la hoja usaba la global (1,33 → 1,39), con más software de menor escala. La regresión semanal contra el S&P 500 da 1,39 a cinco años y 0,97 a dos. El riesgo de Adobe no está en la tasa sino en los flujos (precio y retención de Creative Cloud), y eso se trata en las historias.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,31 | 11,4% | 10,9% | US$454,78 |
| Bottom-up del sector (Software (System & Application), reapalancada) | 1,31 | 11,4% | 10,9% | US$454,57 |


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 36,9% | 20,6% | 9,4% | 20,6% | US$454,78 | US$316,75 |

Fuentes de ventaja: Costos de cambio y estándar de la industria creativa y documental. Evidencia: ROIC 37-60% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$454,78 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$355,49. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$25.970 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 17.819 + 7.263 + 888 = 25.970. |
| Margen inicial del DCF | 38,6% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 3 (Input sheet B31). |
| Impuesto | 21,52% en años 1–5; 25,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 10,93% → 8,99% | Tasa libre de riesgo 5,29%, beta 1,31, ERP 4,63%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 1,23x en años 1–5; 1,23x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 5,29%; Disrupción: 0,00% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: parte de su crecimiento del año 5 (−1,3%) y converge a 0,00% en el año 10 (piso de 0% nominal: el negocio residual deja de achicarse, lo que en términos reales sigue siendo contracción). Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Optimista: 20,56%; Conservadora/Disrupción: 8,99% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 5.639; deuda 6.727; acciones 389,2 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 17.819 × 1,10 + 7.263 × 1,14 + 888 × 1,00 = US$28.768,72 millones. Frente a 25.970, el crecimiento consolidado es 10,78%. En los años 2–5 es 8,90%, 7,69%, 6,75%, 6,47%; las ventas del año 5 son US$38.346,75 millones. El 8,1% de la tabla es el crecimiento anual compuesto de los cinco años: (38.346,75 / 25.970)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 28.768,72 × 38,59% × (1 − 21,52%) = US$8.712,36 millones. La reinversión es US$2.082,64 millones y el FCFF es US$6.629,71 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 8,99%. Reinversión terminal sobre el NOPAT: Base, 25,7% (5,29% / 20,56%); Conservadora, 58,8% (5,29% / 8,99%); Disrupción, 0,0% (0,00% / 8,99%); Optimista, 25,7% (5,29% / 20,56%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · La IA se cobra dentro de la suscripción** — probabilidad 40%; valor terminal 322.424 (VP 120.491); DCF US$454,78 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 28.769 | 10,8% | 38,6% | 8.712 | 2.083 | 6.630 | 10,9% | 5.977 |
| 2 | 31.330 | 8,9% | 39,6% | 9.734 | 1.959 | 7.775 | 10,9% | 6.319 |
| 3 | 33.740 | 7,7% | 40,1% | 10.615 | 1.851 | 8.764 | 10,9% | 6.421 |
| 4 | 36.017 | 6,7% | 40,1% | 11.331 | 1.894 | 9.437 | 10,9% | 6.233 |
| 5 | 38.347 | 6,5% | 40,1% | 12.064 | 1.943 | 10.121 | 10,9% | 6.026 |
| 6 | 40.737 | 6,2% | 40,1% | 12.703 | 1.986 | 10.716 | 10,5% | 5.772 |
| 7 | 43.180 | 6,0% | 40,1% | 13.344 | 2.023 | 11.321 | 10,2% | 5.536 |
| 8 | 45.668 | 5,8% | 40,1% | 13.985 | 2.052 | 11.934 | 9,8% | 5.316 |
| 9 | 48.192 | 5,5% | 40,1% | 14.624 | 2.073 | 12.551 | 9,4% | 5.112 |
| 10 | 50.741 | 5,3% | 40,1% | 15.255 | 2.182 | 13.073 | 9,0% | 4.885 |
| Terminal | 53.426 | 5,3% | 40,1% | 16.062 | 4.133 | 11.930 | 9,0% | — |

**Conservadora · Erosión gradual frente a Figma y Canva** — probabilidad 35%; valor terminal 137.553 (VP 51.404); DCF US$259,10 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 28.267 | 8,8% | 38,6% | 8.560 | 1.378 | 7.183 | 10,9% | 6.475 |
| 2 | 29.961 | 6,0% | 37,6% | 8.838 | 1.162 | 7.677 | 10,9% | 6.239 |
| 3 | 31.390 | 4,8% | 37,1% | 9.137 | 975 | 8.161 | 10,9% | 5.979 |
| 4 | 32.590 | 3,8% | 37,1% | 9.486 | 937 | 8.549 | 10,9% | 5.646 |
| 5 | 33.742 | 3,5% | 37,1% | 9.821 | 1.066 | 8.755 | 10,9% | 5.213 |
| 6 | 35.054 | 3,9% | 37,1% | 10.112 | 1.208 | 8.905 | 10,5% | 4.797 |
| 7 | 36.539 | 4,2% | 37,1% | 10.447 | 1.363 | 9.084 | 10,2% | 4.442 |
| 8 | 38.215 | 4,6% | 37,1% | 10.827 | 1.535 | 9.293 | 9,8% | 4.140 |
| 9 | 40.103 | 4,9% | 37,1% | 11.258 | 1.725 | 9.534 | 9,4% | 3.883 |
| 10 | 42.224 | 5,3% | 37,1% | 11.745 | 1.816 | 9.929 | 9,0% | 3.710 |
| Terminal | 44.458 | 5,3% | 37,1% | 12.366 | 7.277 | 5.089 | 9,0% | — |

**Disrupción · Deterioro de los fundamentales: La IA generativa comoditiza la creatividad** — probabilidad 15%; valor terminal 70.959 (VP 26.518); DCF US$174,89 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 27.515 | 5,9% | 38,6% | 8.333 | 474 | 7.859 | 10,9% | 7.085 |
| 2 | 28.098 | 2,1% | 34,3% | 7.554 | -105 | 7.658 | 10,9% | 6.224 |
| 3 | 27.969 | −0,5% | 32,1% | 7.043 | -312 | 7.356 | 10,9% | 5.389 |
| 4 | 27.585 | −1,4% | 32,1% | 6.947 | -296 | 7.243 | 10,9% | 4.784 |
| 5 | 27.220 | −1,3% | 32,1% | 6.855 | -234 | 7.089 | 10,9% | 4.221 |
| 6 | 26.933 | −1,1% | 32,1% | 6.722 | -173 | 6.896 | 10,5% | 3.714 |
| 7 | 26.719 | −0,8% | 32,1% | 6.609 | -115 | 6.724 | 10,2% | 3.288 |
| 8 | 26.578 | −0,5% | 32,1% | 6.515 | -57 | 6.572 | 9,8% | 2.928 |
| 9 | 26.508 | −0,3% | 32,1% | 6.438 | 0 | 6.438 | 9,4% | 2.622 |
| 10 | 26.508 | −0,0% | 32,1% | 6.379 | 0 | 6.379 | 9,0% | 2.384 |
| Terminal | 26.508 | 0,0% | 32,1% | 6.379 | 0 | 6.379 | 9,0% | — |

**Optimista · La IA amplía el mercado de Adobe** — probabilidad 10%; valor terminal 415.536 (VP 155.287); DCF US$566,58 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 29.270 | 12,7% | 38,6% | 8.864 | 2.906 | 5.958 | 10,9% | 5.371 |
| 2 | 32.845 | 12,2% | 41,6% | 10.720 | 2.936 | 7.784 | 10,9% | 6.326 |
| 3 | 36.456 | 11,0% | 43,1% | 12.328 | 2.979 | 9.349 | 10,9% | 6.849 |
| 4 | 40.120 | 10,1% | 43,1% | 13.567 | 2.968 | 10.599 | 10,9% | 7.001 |
| 5 | 43.771 | 9,1% | 43,1% | 14.801 | 2.967 | 11.835 | 10,9% | 7.046 |
| 6 | 47.420 | 8,3% | 43,1% | 15.893 | 2.920 | 12.973 | 10,5% | 6.988 |
| 7 | 51.012 | 7,6% | 43,1% | 16.944 | 2.826 | 14.118 | 10,2% | 6.904 |
| 8 | 54.487 | 6,8% | 43,1% | 17.935 | 2.681 | 15.254 | 9,8% | 6.796 |
| 9 | 57.785 | 6,1% | 43,1% | 18.847 | 2.485 | 16.361 | 9,4% | 6.664 |
| 10 | 60.842 | 5,3% | 43,1% | 19.661 | 2.617 | 17.044 | 9,0% | 6.370 |
| Terminal | 64.060 | 5,3% | 43,1% | 20.701 | 5.326 | 15.375 | 9,0% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 57.597,13 | 120.490,72 | 178.087,84 | 176.999,71 | 454,78 |
| Conservadora | 50.524,35 | 51.404,13 | 101.928,49 | 100.840,35 | 259,10 |
| Disrupción | 42.637,88 | 26.517,68 | 69.155,56 | 68.067,43 | 174,89 |
| Optimista | 66.314,04 | 155.287,27 | 221.601,31 | 220.513,18 | 566,58 |

Ejemplo Base: (57.597,13 + 120.490,72 + 5.639 − 6.727) / 389,2 = US$454,78 por acción. El terminal representa 67,7% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 40% / 35% / 15% / 10% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,40 × 454,778289 + 0,35 × 259,096485 + 0,15 × 174,890620 + 0,10 × 566,580620 = US$355,486740 ≈ US$355,49. Los aportes son US$181,91 + US$90,68 + US$26,23 + US$56,66 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 355,486740 × 0,65 = US$231,066381 ≈ US$231,07. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$454,78, es el valor intrínseco principal. El DCF esperado de US$355,49 combina las cuatro tesis con sus probabilidades y se presenta como complemento. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: Adobe monetiza la IA y conserva su posición

**Qué tiene que ocurrir.** Adobe mantiene el papel de sus herramientas en los flujos profesionales y cobra las funciones de IA mediante suscripciones, créditos o planes superiores. La IA ayuda a defender la retención y el gasto por cliente, pero no provoca una aceleración permanente. La competencia limita el crecimiento sin deshacer la ventaja comercial.

**Traducción al modelo.** Creative & Marketing Professionals crece 10%, 8%, 7%, 6%, 6%; Business Professionals & Consumers crece 14%, 12%, 10%, 9%, 8%; Otros crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 8,1%; el margen operativo objetivo es 40,1%. El ROIC terminal es 20,6%. El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 40%; DCF: US$454,78 por acción.

**Cómo contrastarla.** La confirmarían renovaciones y precio realizado estables, monetización de IA que aporte ventas y márgenes compatibles con el coste de cómputo. Perdería fuerza si el crecimiento solo se sostiene con descuentos, si empeora la retención o si la IA aumenta el coste sin elevar el gasto del cliente.


#### Conservadora: Adobe sigue siendo rentable, pero pierde poder de precio

**Qué tiene que ocurrir.** Figma, Canva y otras herramientas capturan parte de los nuevos clientes y de los trabajos sencillos. Adobe conserva los flujos profesionales más difíciles de sustituir, pero necesita conceder más valor dentro de sus planes y tiene menos capacidad para subir precios. El negocio crece más lentamente y su ventaja se erosiona de forma gradual.

**Traducción al modelo.** Creative & Marketing Professionals crece 8%, 5%, 4%, 3%, 3%; Business Professionals & Consumers crece 12%, 9%, 7%, 6%, 5%; Otros crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 5,4%; el margen operativo objetivo es 37,1%. El ROIC terminal es el costo de capital (8,99%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 35%; DCF: US$259,10 por acción.

**Cómo contrastarla.** La apoyarían una desaceleración persistente, menor gasto por cliente o presión de descuentos con caja todavía sólida. Se debilitaría si Adobe mantiene la retención y monetiza la IA sin sacrificar precios ni margen. No hay una serie comparable verificada de adopción que demuestre que esta erosión ya esté ocurriendo.


#### Disrupción · Deterioro de los fundamentales: La IA generativa comoditiza la creatividad

**Qué tiene que ocurrir.** Para una parte relevante de los usuarios, producir contenido con herramientas de IA más baratas resulta suficiente y reduce la necesidad de pagar por la suite de Adobe. La presión afecta tanto a nuevos clientes como al gasto de la base instalada. Adobe conserva productos útiles y un negocio rentable, pero pierde una parte sustancial de su poder de precio y de sus retornos extraordinarios.

**Traducción al modelo.** Creative & Marketing Professionals crece 5%, 1%, -2%, -3%, -3%; Business Professionals & Consumers crece 9%, 5%, 3%, 2%, 2%; Otros crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 0,9%; el margen operativo objetivo es 32,1%. El ROIC terminal es el costo de capital (8,99%). El crecimiento terminal es 0,00%: los años 6–10 pasan de −1,3% a ese nivel, sin recuperación. Probabilidad: 15%; DCF: US$174,89 por acción.

**Cómo contrastarla.** La apoyarían deterioro sostenido de renovaciones, contracción de ingresos profesionales y necesidad de regalar funcionalidades de IA para retener usuarios. Se debilitaría si las herramientas complementan la suite y Adobe conserva el gasto de sus clientes. Es una hipótesis adversa severa; no es un caso de quiebra ni el peor resultado posible.


#### Optimista: La IA amplía el mercado y Adobe captura el crecimiento

**Qué tiene que ocurrir.** La IA permite que más personas y empresas creen y distribuyan contenido, aumenta el volumen de trabajo y el gasto por cliente, y Adobe captura una parte relevante de esa expansión con Firefly, Acrobat y GenStudio. Los ingresos adicionales compensan el coste de cómputo y sostienen la ventaja competitiva.

**Traducción al modelo.** Creative & Marketing Professionals crece 12%, 12%, 11%, 10%, 9%; Business Professionals & Consumers crece 16%, 14%, 12%, 11%, 10%; Otros crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 11,0%; el margen operativo objetivo es 43,1%. El ROIC terminal es 20,6%. El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 10%; DCF: US$566,58 por acción.

**Cómo contrastarla.** La confirmarían expansión de clientes y gasto, monetización de IA que aporte crecimiento adicional y mejora de margen con retención sólida. Se debilitaría si el ARR de IA solo sustituye ingresos existentes o si aumenta su uso sin una contribución económica suficiente.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 5,29%; Disrupción: 0,00%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,31) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **Base · La IA se cobra dentro de la suscripción** | 40% | Creative & Marketing Professionals: 10%, 8%, 7%, 6%, 6%; Business Professionals & Consumers: 14%, 12%, 10%, 9%, 8%; Otros: 0%, 0%, 0%, 0%, 0% | 8,1% | 40,1% | 1,2 | 20,6% | 5,29% | US$454,78 |
| **Conservadora · Erosión gradual frente a Figma y Canva** | 35% | Creative & Marketing Professionals: 8%, 5%, 4%, 3%, 3%; Business Professionals & Consumers: 12%, 9%, 7%, 6%, 5%; Otros: 0%, 0%, 0%, 0%, 0% | 5,4% | 37,1% | 1,2 | = costo de capital | 5,29% | US$259,10 |
| **Disrupción · Deterioro de los fundamentales: La IA generativa comoditiza la creatividad** | 15% | Creative & Marketing Professionals: 5%, 1%, -2%, -3%, -3%; Business Professionals & Consumers: 9%, 5%, 3%, 2%, 2%; Otros: 0%, 0%, 0%, 0%, 0% | 0,9% | 32,1% | 1,2 | = costo de capital | 0,00% | US$174,89 |
| **Optimista · La IA amplía el mercado de Adobe** | 10% | Creative & Marketing Professionals: 12%, 12%, 11%, 10%, 9%; Business Professionals & Consumers: 16%, 14%, 12%, 11%, 10%; Otros: 0%, 0%, 0%, 0%, 0% | 11,0% | 43,1% | 1,2 | 20,6% | 5,29% | US$566,58 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  |  | **US$355,49** |

Base (40%) continúa lo que muestran los últimos trimestres: crecimiento de doble dígito bajo que desacelera y margen de 40%. Conservadora (35%) pesa casi lo mismo porque la adopción de Figma crece más rápido que la de Adobe. Disrupción (15%) es la disrupción: poco probable en cinco años por el costo de cambiar flujos profesionales, pero no despreciable. Optimista (10%) exige que la IA agrande el mercado y no solo defienda la base. En las historias de erosión (Conservadora y Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 1,31; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.

| Crecimiento \ Margen | 36,1% | 38,1% | 40,1% | 42,1% | 44,1% |
|---|---:|---:|---:|---:|---:|
| 4,1% | 338,08 | 356,59 | 375,09 | 393,59 | 412,10 |
| 6,1% | 374,49 | 395,38 | 416,26 | 437,15 | 458,04 |
| 8,1% | 414,93 | 438,48 | 462,03 | 485,58 | 509,12 |
| 10,1% | 459,83 | 486,34 | 512,84 | 539,35 | 565,86 |
| 12,1% | 509,61 | 539,40 | 569,20 | 599,00 | 628,79 |


### Pre-mortem

1. El ARR «AI-first» se estanca antes de llegar a 5% del total y la IA termina regalada dentro de los planes para no perder usuarios.
2. Figma y Canva capturan a los nuevos diseñadores y equipos de marketing; Creative Cloud crece solo por precio y la retención cae.
3. El nuevo CEO (1-dic-2026) cambia la estrategia o salen ejecutivos clave en medio del giro a la IA.
4. Adobe hace una compra grande para defenderse y destruye valor (precio alto, retorno bajo).
5. El costo de cómputo de la IA baja el margen a 32-34% en lugar de subirlo a 40%.

**Evidencia en contra de la historia más probable:** la adopción relativa se mueve en contra (Figma 59% frente a 42% de Adobe en equipos de diseño) y el consenso (~40 analistas en «Hold») no cree la guía. Si Creative & Marketing Professionals baja de ~13% a un dígito bajo en 2027, la historia Base pierde peso a favor de Conservadora.


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
| Beta 1,31 | −2,2% (88% de las empresas) | −3,6% (91% de las empresas) | −4,6% (92% de las empresas) |

Frente al DCF Base (US$454,78), el valor intrínseco principal, el precio está por debajo en 47%.

Frente al DCF esperado de las historias (US$355,49), el complemento, el precio está por debajo en 33%. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Suite creativa y documental por suscripción que defiende su precio con IA frente a Figma y Canva |  |
| Probabilidades | Base 40% / Conservadora 35% / Disrupción 15% / Optimista 10% |  |
| DCF Base hoy (valor intrínseco principal) | US$454,78 |  |
| DCF esperado por probabilidades (complemento) | US$355,49 |  |
| Precio con MOS sobre el DCF esperado | US$231,07 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$174,82 a US$566,58 |  |
| Confianza | Media: la base es muy rentable y recurrente; lo incierto es el precio de Creative Cloud en la era de la IA |  |
| Qué cambiaría la opinión | Crecimiento de Creative & Marketing Professionals, peso del ARR «AI-first» y adopción frente a Figma |  |
| Revisión | Resultados del 4T FY26 (dic-2026) y primeros meses del nuevo CEO |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Antecedentes de revisiones anteriores

Notas de revisiones previas, con las cifras de su fecha; las cifras vigentes son las de esta sección.

**Dictamen de auditoría del 30-sep-2026 (cifras de esa fecha).** DCF técnico anterior US$536,48, condicionado a ROIC terminal 29,3%; contraste sin retorno excedente terminal US$377,94 (−29,55%). Valor esperado de cuatro historias US$364,33; MOS 35% US$236,81. El ROIC excedente no es incorrecto por definición: requiere evidencia de duración de la ventaja. Falta una serie homogénea que incluya I+D, goodwill y adquisiciones, así como soporte de ventas/capital 4x–4,5x. La coincidencia del cálculo con la hoja no certifica esos supuestos ni el cumplimiento integral de los prompts v4/v5.

**Corrección de la historia Disrupción, 30-sep-2026.** La convergencia automática a 4,99% introducía una recuperación no explicada por la tesis. Se sustituye por estabilización nominal del negocio residual: crecimiento años 6–10 de −1,06%, −0,79%, −0,53%, −0,26% y 0%; perpetuidad 0%, margen 32% y ROIC igual a WACC. El 0% es juicio del analista aceptado por el usuario, no una cifra de Adobe. El ingreso del año 10 y terminal es US$26.508,16 millones. La reinversión negativa de algunos años representa liberación de capital y sigue siendo una salvedad económica por validar; no debe interpretarse como recuperación automática de todo el capital intangible. Damodaran, The Stable Growth Rate, consultado 30-sep-2026, permite crecimiento estable menor o negativo, pero no determina el 0% elegido.


### Fuentes de esta sección

- [Adobe, resultados del 3T FY2026 (Form 8-K, ex. 99.1)](https://www.sec.gov/Archives/edgar/data/796343/000079634326000147/adbeex991q326.htm)
- [Adobe, anuncio de Anil Chakravarthy como CEO (sep-2026)](https://news.adobe.com/news/2026/09/adobe-announces-anil-chakravarthy-to-become-president-and-ceo)
- [Yahoo Finance, «Adobe Valuation Questioned As Figma AI Credits Challenge Creative Cloud»](https://finance.yahoo.com/news/adobe-valuation-questioned-figma-ai-031116166.html)
- [Benzinga, revisiones de analistas tras el 3T FY26](https://www.benzinga.com/analyst-stock-ratings/price-target/26/09/61739763/these-analysts-revise-their-forecasts-on-adobe-following-q3-results)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
