---
schema: "jmr-analisis-damodaran-v1"
ticker: "NVDA"
analysis_date: "2026-09-30"
---

# NVIDIA Corporation (NVDA) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$209,39 por acción** (Base · Ciclo de IA largo que desacelera con la escala).

**Complemento · DCF esperado por probabilidades: US$190,50.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$54,53–318,06. El MOS 35% se aplica al esperado: US$123,83. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), balance del último 10-q, capital invertido operativo, deuda de balance sin arrendamientos operativos, eps básico, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet (29 celdas, con respaldo). DCF esperado US$186,04 → US$190,57. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (bloque Base de 'Valuation output': US$209,38 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja calcula estos cuatro DCF en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

NVIDIA pasó de vender tarjetas gráficas a ser el proveedor dominante de la infraestructura de IA: GPUs, sistemas completos, redes (Mellanox) y CUDA, el software que es estándar de la industria desde hace casi veinte años. Diseña pero no fabrica (TSMC produce sus chips). Los números son de otro planeta: ingresos de US$60.922 millones (FY24), US$130.497 millones (FY25) y US$215.938 millones (FY26), margen operativo de ~60% y, en el 2T FY27, US$96.220 millones en un trimestre, más de 90% de Data Center (+117%). La historia de cinco años no es si NVIDIA es buena empresa, sino cuánto dura el ciclo de inversión en IA de los hiperescaladores, si la inferencia sostiene la demanda cuando el entrenamiento madure y cuánto terreno ceden sus márgenes frente a los chips propios de Google, Amazon y Microsoft y frente a AMD.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~50% el próximo año | Sí | Sí: la empresa habla de crecimiento limitado por la oferta y guía muy alta | Probable |
| La demanda de IA sigue creciendo cinco años sin corrección | Sí | Posible con la inferencia y la IA soberana, pero los semiconductores siempre fueron cíclicos | Incierto |
| El margen operativo se mantiene en ~58-60% | Sí | Sí mientras domine CUDA; los chips propios de los clientes presionan | Media |
| Los chips propios de los clientes (TPU, Trainium) reemplazan a NVIDIA | Sí | Parcialmente: ganan en inferencia interna, no en el mercado abierto | Baja a cinco años |


### Visión externa: tasas base

Con ventas LTM de US$302.970 millones (US$214.368 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **>$50,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 1,0% y una mediana de 1,5% (desviación estándar 8,3%); sumando una inflación de 2,5%, la mediana nominal ronda 4,0%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · Ciclo de IA largo que desacelera con la escala | 17,1% | 4% |
| Conservadora · Ciclo de semiconductores: el capex se corrige | 7,0% | 30% |
| Disrupción · Deterioro de los fundamentales: Chips propios de los clientes y corrección fuerte | −1,3% | 79% |
| Optimista · La IA es infraestructura permanente | 25,3% | 1% |

En dólares de 2015 la empresa está en el tramo de más de US$50.000 millones: crecer 17,1% anual cinco años (Base) lo logró ~4% de las empresas de ese tamaño; 25,3% (Optimista), ~1%. NVIDIA ya rompió todas las tasas base en 2024-2026, pero la visión externa es clara: sostener crecimientos así desde US$300.000 millones de ventas casi no tiene precedentes, y en semiconductores los ciclos de sobreinversión terminan en correcciones.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: cuánto dura el ciclo.** NVIDIA pasó de vender tarjetas gráficas a ser el proveedor dominante de la infraestructura de IA: GPUs, sistemas completos, redes y CUDA, el software estándar de la industria. Los ingresos fueron US$60.922 millones en FY24, US$130.497 millones en FY25 y US$215.938 millones en FY26, y en el 2T FY27 facturó US$96.220 millones en un solo trimestre (Data Center +117%). La pregunta no es si es buena empresa, sino cuánto dura el ciclo de inversión de los hiperescaladores. La Base supone que Data Center crece 50% el primer año y luego se desacelera rápido (20%, 10%, 8%, 6%): 46,7% el primer año y 17,1% compuesto. La desaceleración es deliberada: sostener crecimientos así desde US$300.000 millones de ventas casi no tiene precedentes (~4% de las empresas de ese tamaño lo lograron), y en semiconductores todos los ciclos de escasez terminaron en exceso de capacidad. La Conservadora (7,0%) es justamente eso: una corrección del capex en el año 2; la Disrupción (−1,3%), corrección fuerte más chips propios de los clientes; la Optimista (25,3%), la IA como infraestructura permanente. Una caída secuencial de Data Center sería la primera señal contra la Base.

**Margen: de monopolio temporal.** El margen operativo de 54-65% es el de un monopolio temporal: precio altísimo por escasez, poco capital (NVIDIA diseña pero no fabrica) y software propio. La Base usa 58,1%, apenas por debajo del actual, porque CUDA y la escala sostienen el precio mientras la escasez dure. Las fuerzas en contra son la competencia (AMD, los TPU de Google, Trainium de Amazon) y el poder de negociación de cinco clientes enormes. La Conservadora baja a 50,1%, la Disrupción a 40,1%. Curiosamente, el margen es de los supuestos que menos mueven la Base (dos puntos: US$202,84 (−3%) o US$215,94 (+3%)), porque lo que domina el valor es cuánto dura el crecimiento. Un margen bruto por debajo de 65% invalidaría la Base.

**Reinversión: genera más caja de la que puede usar.** Como no fabrica, NVIDIA casi no invierte en activos fijos: su reinversión es I+D (US$18.497 millones en FY26), compromisos de capacidad con TSMC y capital de trabajo. La hoja usa un ventas/capital de 2,92× y 2,44×, y el supuesto casi no mueve el valor. En 2026 la empresa subió el dividendo 25 veces y aprobó recompras por US$80.000 millones: genera más caja de la que puede reinvertir. El ROIC actual es altísimo; después del año 10 la Base usa 27,2%, el promedio de semiconductores, no el actual, porque Damodaran limita el retorno de una ventaja duradera al de su industria. La ventaja (los costos de cambio de CUDA) es real; si se perdiera, la Base valdría US$148,73 (−29%).

**Descuento: la ciclicidad va en las historias.** Hasta el 30-sep-2026 la hoja usaba una beta de regresión de 1,90; hoy usa la bottom-up de semiconductores, 1,51, con un costo de capital de 11,67% que converge a 9,00%. La ciclicidad del negocio no se sumó a la tasa: está en la Conservadora y la Disrupción, que es donde Damodaran recomienda ponerla. Un punto más de tasa lleva la Base a US$170,33 (−19%). El crecimiento perpetuo es 4,99% y el terminal explica 65,2% del valor operativo.

**Probabilidades y lectura del resultado.** La Base pesa 40%, la Conservadora 30% —alta, porque es la historia clásica del sector—, la Disrupción 10% y la Optimista 20%. El DCF Base es US$209,39 y el esperado US$190,50, frente a un precio de US$233,95: el mercado paga algo entre la Base y la Optimista. El antiguo DCF técnico de la hoja (US$209,38) es más alto que la Base porque suponía un crecimiento más largo; la Base se apoya en la visión externa. Las acciones se fijan en 24.100,0 millones; las recompras no se modelan.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$302.970 millones. Con el crecimiento de la Base llegan a US$665.808 millones en el año 5 y a US$865.805 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 60,1% en el año 1 a 58,1% al final, y se descuentan impuestos (16,1% al principio y 16,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$224.070 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$29.323 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$194.747 millones el primer año. Cada flujo se trae a hoy con el costo de capital (11,67% al principio, 9,00% al final): los diez años suman US$1.716.968 millones. Después del año 10 se supone que la empresa crece 4,99% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 27,2%; esa perpetuidad vale hoy US$3.217.393 millones, 65% del total. Flujos más terminal dan el valor de las operaciones, US$4.934.361 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$99.369 millones, más activos no operativos por US$51.157 millones, menos deuda por US$38.591 millones (incluye los arrendamientos capitalizados). Queda un patrimonio de US$5.046.296 millones que, repartido entre 24.100,0 millones de acciones, da US$209,39 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 31,19× (peso 33% dentro de los múltiplos); EV/FCFF 43,65× (peso 17% dentro de los múltiplos); P/E 37,63× (peso 33% dentro de los múltiplos); P/FCFE 40,19× (peso 8% dentro de los múltiplos); P/OCF 37,52× (peso 8% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (11,7%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$209,39; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$202,84 | −3,1% |
| Margen objetivo +2 pp | US$215,94 | +3,1% |
| Crecimiento años 1–5 −2 pp | US$188,94 | −9,8% |
| Crecimiento años 1–5 +2 pp | US$232,01 | +10,8% |
| Ventas/capital −20% | US$208,31 | −0,5% |
| Ventas/capital +20% | US$210,11 | +0,3% |
| WACC +1 pp | US$170,33 | −18,7% |
| WACC −1 pp | US$274,08 | +30,9% |
| Crecimiento terminal −0,5 pp | US$194,88 | −6,9% |
| Crecimiento terminal +0,5 pp | US$227,92 | +8,9% |
| ROIC terminal = costo de capital | US$148,73 | −29,0% |
| Acciones +5% | US$199,42 | −4,8% |


### Piezas del valor

**Crecimiento.** Ingresos de US$60.922 millones (FY24, +126%), US$130.497 millones (FY25, +114%) y US$215.938 millones (FY26, +65%); LTM US$302.970 millones. En el 2T FY27 (jul-2026) facturó US$96.220 millones, con Data Center en US$89.000 millones (+117%). La hoja supone +50% el próximo año y 14% en los años 2-5. Cada historia se valora con su crecimiento año a año por segmentos; el CAGR a cinco años es descriptivo y no reemplaza la trayectoria de flujos.

| US$ millones | FY24 | FY25 | FY26 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 60.922 | 130.497 | 215.938 | 302.970 |
| Crecimiento | +126% | +114% | +65% | — |
| Margen operativo | 54,1% | 62,4% | 60,4% | 65,2% |
| FCFF (hoja) | 17.211 | 46.706 | 83.173 | — |

**Márgenes.** El margen operativo (54-65%) es de monopolio temporal: precio altísimo por escasez, poco capital (fabless) y software propio. La hoja supone 60% el próximo año y 58% de objetivo. Las fuerzas en contra son la competencia (AMD MI400, TPU, Trainium) y el poder de negociación de cinco clientes enormes; a favor, la escala y el ecosistema CUDA. Las historias van de 40% (corrección fuerte) a 60%.

**Reinversión y retorno.** Como fabless, NVIDIA casi no invierte en activos fijos; su reinversión es I+D (US$18.497 millones en FY26), compromisos de capacidad con TSMC y capital de trabajo. La hoja usa un sales-to-capital de 3 y 2,5. En 2026 la empresa subió el dividendo 25 veces y aprobó recompras por US$80.000 millones: señal de que genera más caja de la que puede reinvertir. Ventaja durable: ecosistema CUDA (costos de cambio) y escala en cómputo acelerado, con ROIC de 13-111%. El ROIC después del año 10 es 27,2%, el promedio de su industria según Damodaran. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$5.225 millones, compromisos del 10-Q al 2026-07-26) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$156 millones, +0,05 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,02 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usaba una beta de regresión de 1,90 (costo del patrimonio 13,5%). Tras la revisión del 30-sep-2026 usa la bottom-up de Semiconductor (66 empresas, 1,50 desapalancada y corregida por caja; 1,51 sin deuda relevante), con costo del patrimonio de 11,7%: el DCF Base pasó de US$162,65 a US$178,38. La ciclicidad del negocio se modela en las historias (Conservadora y Disrupción), no en la tasa.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,51 | 11,7% | 11,7% | US$326,54 |
| Bottom-up del sector (Semiconductor, reapalancada) | 1,51 | 11,7% | 11,7% | US$326,56 |


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 140,8% | 27,2% | 9,0% | 27,2% | US$209,38 | US$222,20 |

Fuentes de ventaja: Ecosistema CUDA (costos de cambio) y escala en cómputo acelerado. Evidencia: ROIC 13-111%, siempre por encima del costo de capital. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$209,39 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$190,50. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$302.970 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 278.000 + 24.970 = 302.970. |
| Margen inicial del DCF | 60,1% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 16,05% en años 1–5; 16,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 11,67% → 9,00% | Tasa libre de riesgo 4,99%, beta 1,51, ERP 4,46%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 2,92x en años 1–5; 2,44x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 4,99%; Disrupción: 4,54% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (4,54%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Conservadora/Optimista: 27,20%; Disrupción: 9,00% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 99.369; deuda 38.591; activos no operativos 51.157; acciones 24.100,0 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 278.000 × 1,50 + 24.970 × 1,10 = US$444.467,00 millones. Frente a 302.970, el crecimiento consolidado es 46,70%. En los años 2–5 es 19,26%, 9,83%, 7,89%, 6,00%; las ventas del año 5 son US$665.807,75 millones. El 17,1% de la tabla es el crecimiento anual compuesto de los cinco años: (665.807,75 / 302.970)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 444.467,00 × 60,05% × (1 − 16,05%) = US$224.070,19 millones. La reinversión es US$29.323,20 millones y el FCFF es US$194.746,99 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,00%. Reinversión terminal sobre el NOPAT: Base, 18,3% (4,99% / 27,20%); Conservadora, 18,3% (4,99% / 27,20%); Disrupción, 50,4% (4,54% / 9,00%); Optimista, 18,3% (4,99% / 27,20%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · Ciclo de IA largo que desacelera con la escala** — probabilidad 40%; valor terminal 9.026.019 (VP 3.217.393); DCF US$209,39 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 444.467 | 46,7% | 60,1% | 224.070 | 29.323 | 194.747 | 11,7% | 174.392 |
| 2 | 530.064 | 19,3% | 59,3% | 263.663 | 17.854 | 245.809 | 11,7% | 197.110 |
| 3 | 582.181 | 9,8% | 58,9% | 287.631 | 15.738 | 271.894 | 11,7% | 195.239 |
| 4 | 628.121 | 7,9% | 58,5% | 308.219 | 12.911 | 295.308 | 11,7% | 189.888 |
| 5 | 665.808 | 6,0% | 58,1% | 324.476 | 13.224 | 311.252 | 11,7% | 179.221 |
| 6 | 704.411 | 5,8% | 58,1% | 343.330 | 16.131 | 327.199 | 11,1% | 169.523 |
| 7 | 743.830 | 5,6% | 58,1% | 362.586 | 16.419 | 346.167 | 10,6% | 162.157 |
| 8 | 783.952 | 5,4% | 58,1% | 382.190 | 16.657 | 365.533 | 10,1% | 155.565 |
| 9 | 824.655 | 5,2% | 58,1% | 402.081 | 16.840 | 385.241 | 9,5% | 149.681 |
| 10 | 865.805 | 5,0% | 58,1% | 422.195 | 17.680 | 404.515 | 9,0% | 144.192 |
| Terminal | 909.009 | 5,0% | 58,1% | 443.262 | 81.319 | 361.943 | 9,0% | — |

**Conservadora · Ciclo de semiconductores: el capex se corrige** — probabilidad 30%; valor terminal 5.146.175 (VP 1.834.393); DCF US$125,59 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 401.518 | 32,5% | 60,1% | 202.418 | -12.408 | 214.826 | 11,7% | 192.372 |
| 2 | 365.299 | −9,0% | 56,1% | 171.893 | 472 | 171.421 | 11,7% | 137.460 |
| 3 | 366.676 | 0,4% | 54,1% | 166.384 | 9.752 | 156.632 | 11,7% | 112.473 |
| 4 | 395.143 | 7,8% | 52,1% | 172.666 | 10.517 | 162.149 | 11,7% | 104.265 |
| 5 | 425.844 | 7,8% | 50,1% | 178.932 | 10.523 | 168.409 | 11,7% | 96.971 |
| 6 | 456.563 | 7,2% | 50,1% | 191.862 | 12.439 | 179.423 | 11,1% | 92.960 |
| 7 | 486.959 | 6,7% | 50,1% | 204.660 | 12.160 | 192.501 | 10,6% | 90.174 |
| 8 | 516.673 | 6,1% | 50,1% | 217.174 | 11.726 | 205.448 | 10,1% | 87.435 |
| 9 | 545.327 | 5,5% | 50,1% | 229.246 | 11.136 | 218.110 | 9,5% | 84.744 |
| 10 | 572.539 | 5,0% | 50,1% | 240.714 | 11.692 | 229.022 | 9,0% | 81.637 |
| Terminal | 601.108 | 5,0% | 50,1% | 252.726 | 46.364 | 206.362 | 9,0% | — |

**Disrupción · Deterioro de los fundamentales: Chips propios de los clientes y corrección fuerte** — probabilidad 10%; valor terminal 1.383.606 (VP 493.197); DCF US$54,53 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 372.470 | 22,9% | 60,1% | 187.774 | -29.761 | 217.535 | 11,7% | 194.798 |
| 2 | 285.595 | −23,3% | 52,1% | 124.797 | -8.928 | 133.725 | 11,7% | 107.232 |
| 3 | 259.532 | −9,1% | 48,1% | 104.693 | 4.018 | 100.676 | 11,7% | 72.292 |
| 4 | 271.261 | 4,5% | 44,1% | 100.316 | 4.219 | 96.097 | 11,7% | 61.792 |
| 5 | 283.575 | 4,5% | 40,1% | 95.347 | 4.410 | 90.937 | 11,7% | 52.362 |
| 6 | 296.449 | 4,5% | 40,1% | 99.688 | 5.507 | 94.180 | 11,1% | 48.795 |
| 7 | 309.907 | 4,5% | 40,1% | 104.225 | 5.757 | 98.468 | 10,6% | 46.126 |
| 8 | 323.976 | 4,5% | 40,1% | 108.970 | 6.019 | 102.951 | 10,1% | 43.814 |
| 9 | 338.683 | 4,5% | 40,1% | 113.931 | 6.292 | 107.638 | 9,5% | 41.822 |
| 10 | 354.059 | 4,5% | 40,1% | 119.117 | 6.578 | 112.539 | 9,0% | 40.115 |
| Terminal | 370.132 | 4,5% | 40,1% | 124.524 | 62.812 | 61.712 | 9,0% | — |

**Optimista · La IA es infraestructura permanente** — probabilidad 20%; valor terminal 14.608.372 (VP 5.207.264); DCF US$318,06 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 472.766 | 56,0% | 60,1% | 238.337 | 46.862 | 191.474 | 11,7% | 171.461 |
| 2 | 609.562 | 28,9% | 60,1% | 307.300 | 40.691 | 266.609 | 11,7% | 213.790 |
| 3 | 728.343 | 19,5% | 60,1% | 367.181 | 36.836 | 330.345 | 11,7% | 237.211 |
| 4 | 835.871 | 14,8% | 60,1% | 421.390 | 33.842 | 387.548 | 11,7% | 249.200 |
| 5 | 934.660 | 11,8% | 60,1% | 471.192 | 33.469 | 437.723 | 11,7% | 252.045 |
| 6 | 1.032.359 | 10,5% | 60,1% | 520.508 | 38.391 | 482.117 | 11,1% | 249.786 |
| 7 | 1.126.171 | 9,1% | 60,1% | 567.875 | 35.586 | 532.289 | 10,6% | 249.343 |
| 8 | 1.213.128 | 7,7% | 60,1% | 611.796 | 31.553 | 580.243 | 10,1% | 246.942 |
| 9 | 1.290.231 | 6,4% | 60,1% | 650.757 | 26.347 | 624.410 | 9,5% | 242.607 |
| 10 | 1.354.614 | 5,0% | 60,1% | 683.311 | 27.662 | 655.649 | 9,0% | 233.711 |
| Terminal | 1.422.209 | 5,0% | 60,1% | 717.409 | 131.613 | 585.796 | 9,0% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 1.716.968,25 | 3.217.392,69 | 4.934.360,95 | 5.046.296,31 | 209,39 |
| Conservadora | 1.080.490,40 | 1.834.392,75 | 2.914.883,15 | 3.026.818,51 | 125,59 |
| Disrupción | 709.149,18 | 493.196,62 | 1.202.345,80 | 1.314.281,16 | 54,53 |
| Optimista | 2.346.095,57 | 5.207.264,32 | 7.553.359,89 | 7.665.295,25 | 318,06 |

Ejemplo Base: (1.716.968,25 + 3.217.392,69 + 99.369 + 51.157 − 38.591) / 24.100,0 = US$209,39 por acción. El terminal representa 65,2% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 40% / 30% / 10% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,40 × 209,389888 + 0,30 × 125,594129 + 0,10 × 54,534488 + 0,20 × 318,062043 = US$190,500052 ≈ US$190,50. Los aportes son US$83,76 + US$37,68 + US$5,45 + US$63,61 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 190,500052 × 0,65 = US$123,825034 ≈ US$123,83. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$209,39, es el valor intrínseco principal. El DCF esperado de US$190,50 combina las cuatro tesis con sus probabilidades y se presenta como complemento. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: Ciclo de IA largo que desacelera con la escala

**Qué plantea.** Es un ciclo de IA largo que desacelera con la escala.

**Traducción al modelo.** Data Center crece 50%, 20%, 10%, 8%, 6%; Gaming, visualización y automotriz crece 10%, 8%, 7%, 6%, 6%. El crecimiento anual compuesto de cinco años es 17,1%; el margen operativo objetivo es 58,1%. El ROIC terminal es 27,2%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 40%; DCF: US$209,39 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (data Center (interanual): +117% (2T FY27); capex de los hiperescaladores: Récord; margen bruto: ~70-75%). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: Ciclo de semiconductores: el capex se corrige

**Qué plantea.** Es la historia clásica de semiconductores: sobreinversión y corrección en 2028.

**Traducción al modelo.** Data Center crece 35%, -10%, 0%, 8%, 8%; Gaming, visualización y automotriz crece 5%, 5%, 5%, 5%, 5%. El crecimiento anual compuesto de cinco años es 7,0%; el margen operativo objetivo es 50,1%. El ROIC terminal es 27,2%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 30%; DCF: US$125,59 por acción.

**Cómo contrastarla.** La apoyarían: data Center (interanual): caída trimestral secuencial; capex de los hiperescaladores: recortes anunciados; margen bruto: ≤ 65%; participación de chips propios y AMD en inferencia: pérdida de clientes grandes.


#### Disrupción · Deterioro de los fundamentales: Chips propios de los clientes y corrección fuerte

**Qué plantea.** Combina corrección fuerte y pérdida de participación frente a chips propios.

**Traducción al modelo.** Data Center crece 25%, -25%, -10%, 5%, 5%; Gaming, visualización y automotriz crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es −1,3%; el margen operativo objetivo es 40,1%. El ROIC terminal es el costo de capital (9,00%). El crecimiento terminal es 4,54%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 10%; DCF: US$54,53 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: data Center (interanual): caída trimestral secuencial; capex de los hiperescaladores: recortes anunciados; margen bruto: ≤ 65%; participación de chips propios y AMD en inferencia: pérdida de clientes grandes.


#### Optimista: La IA es infraestructura permanente

**Qué plantea.** Trata la IA como infraestructura permanente (inferencia masiva, IA soberana, robótica).

**Traducción al modelo.** Data Center crece 60%, 30%, 20%, 15%, 12%; Gaming, visualización y automotriz crece 12%, 12%, 10%, 10%, 8%. El crecimiento anual compuesto de cinco años es 25,3%; el margen operativo objetivo es 60,1%. El ROIC terminal es 27,2%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 20%; DCF: US$318,06 por acción.

**Cómo contrastarla.** La confirmarían: data Center (interanual): ≥ +30% en FY28; capex de los hiperescaladores: sigue creciendo en 2027-2028; margen bruto: ≥ 70%; participación de chips propios y AMD en inferencia: NVIDIA ≥ 70% del mercado abierto.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 4,99%; Disrupción: 4,54%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,51) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **Base · Ciclo de IA largo que desacelera con la escala** | 40% | Data Center: 50%, 20%, 10%, 8%, 6%; Gaming, visualización y automotriz: 10%, 8%, 7%, 6%, 6% | 17,1% | 58,1% | 2,9 | 27,2% | 4,99% | US$209,39 |
| **Conservadora · Ciclo de semiconductores: el capex se corrige** | 30% | Data Center: 35%, -10%, 0%, 8%, 8%; Gaming, visualización y automotriz: 5%, 5%, 5%, 5%, 5% | 7,0% | 50,1% | 2,9 | 27,2% | 4,99% | US$125,59 |
| **Disrupción · Deterioro de los fundamentales: Chips propios de los clientes y corrección fuerte** | 10% | Data Center: 25%, -25%, -10%, 5%, 5%; Gaming, visualización y automotriz: 0%, 0%, 0%, 0%, 0% | −1,3% | 40,1% | 2,9 | = costo de capital | 4,54% | US$54,53 |
| **Optimista · La IA es infraestructura permanente** | 20% | Data Center: 60%, 30%, 20%, 15%, 12%; Gaming, visualización y automotriz: 12%, 12%, 10%, 10%, 8% | 25,3% | 60,1% | 2,9 | 27,2% | 4,99% | US$318,06 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  |  | **US$190,50** |

Base (40%) es un ciclo de IA largo que desacelera con la escala. Conservadora (30%) es la historia clásica de semiconductores: sobreinversión y corrección en 2028. Disrupción (10%) combina corrección fuerte y pérdida de participación frente a chips propios. Optimista (20%) trata la IA como infraestructura permanente (inferencia masiva, IA soberana, robótica). En las historias de erosión (Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 1,51; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.

| Crecimiento \ Margen | 54,1% | 56,1% | 58,1% | 60,1% | 62,1% |
|---|---:|---:|---:|---:|---:|
| 13,9% | 188,07 | 194,51 | 200,95 | 207,39 | 213,83 |
| 15,9% | 209,03 | 216,26 | 223,50 | 230,73 | 237,97 |
| 17,9% | 232,20 | 240,32 | 248,44 | 256,55 | 264,67 |
| 19,9% | 257,80 | 266,89 | 275,98 | 285,07 | 294,16 |
| 21,9% | 286,05 | 296,21 | 306,38 | 316,55 | 326,72 |


### Pre-mortem

1. Los hiperescaladores recortan capex en 2028 porque la monetización de la IA no alcanza para pagar la inversión.
2. Los chips propios (TPU, Trainium, Maia) y AMD capturan la inferencia, que es la mayor parte de la demanda futura.
3. Controles de exportación más duros o un conflicto en Taiwán cortan ventas o producción.
4. Los clientes negocian precios a la baja y el margen cae de ~60% a ~45%.
5. Aparecen métodos de IA mucho más eficientes que reducen la necesidad de cómputo.

**Evidencia en contra de la historia más probable:** la concentración de clientes (pocos hiperescaladores) y la historia de los semiconductores: todos los ciclos de escasez terminaron en exceso de capacidad. Una desaceleración del capex de los hiperescaladores sube el peso de Conservadora.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Data Center (interanual) | +117% (2T FY27) | ≥ +30% en FY28 | Caída trimestral secuencial |
| Capex de los hiperescaladores | Récord | Sigue creciendo en 2027-2028 | Recortes anunciados |
| Margen bruto | ~70-75% | ≥ 70% | ≤ 65% |
| Participación de chips propios y AMD en inferencia | Creciendo | NVIDIA ≥ 70% del mercado abierto | Pérdida de clientes grandes |
| Restricciones de exportación | Vigentes para China | Sin nuevas restricciones | Nuevas restricciones o problemas en Taiwán |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$233,95**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 50% | Margen 58% | Margen 62% |
|---|---:|---:|---:|
| Beta 1,51 | 19,5% (2% de las empresas) | 16,8% (4% de las empresas) | 15,6% (6% de las empresas) |
| Beta 1,51 | 19,5% (2% de las empresas) | 16,8% (4% de las empresas) | 15,6% (6% de las empresas) |

Frente al DCF Base (US$209,39), el valor intrínseco principal, el precio está por encima en 12%.

Frente al DCF esperado de las historias (US$190,50), el complemento, el precio está por encima en 23%. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Proveedor dominante de la infraestructura de IA en la cima de un ciclo de inversión |  |
| Probabilidades | Base 40% / Conservadora 30% / Disrupción 10% / Optimista 20% |  |
| DCF Base hoy (valor intrínseco principal) | US$209,39 |  |
| DCF esperado por probabilidades (complemento) | US$190,50 |  |
| Precio con MOS sobre el DCF esperado | US$123,83 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$54,53 a US$318,08 |  |
| Confianza | Baja: el valor depende de la duración del ciclo, que nadie puede prever |  |
| Qué cambiaría la opinión | Capex de los hiperescaladores y participación de NVIDIA en inferencia |  |
| Revisión | Resultados del 3T FY27 (nov-2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [NVIDIA, resultados del 4T y año FY2026](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026)
- [NVIDIA, Form 10-K FY2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- [Investing.com, presentación del 2T FY27](https://www.investing.com/news/company-news/nvidia-q2-fy27-slides-revenue-doubles-to-96b-data-center-surges-93CH-4878041)
- [CNBC, resultados del 2T FY27](https://www.cnbc.com/2026/08/26/nvidia-nvda-earnings-report-q2-2027-live-updates.html)
- [IBTimes, NVIDIA frente a AMD en centros de datos (2026)](https://www.ibtimes.com.au/nvidia-vs-amd-2026-ai-chip-showdown-who-dominates-data-centers-blackwell-mi400-battle-1866177)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
