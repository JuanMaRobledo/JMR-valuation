---
schema: "jmr-analisis-damodaran-v1"
ticker: "EPAM"
analysis_date: "2026-09-30"
---

# EPAM Systems, Inc. (EPAM) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$176,10 por acción** (Base · La IA compensa lo que quita: crecimiento moderado).

**Complemento · DCF esperado por probabilidades: US$157,00.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$85,29–231,70. El MOS 35% se aplica al esperado: US$102,05. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), balance del último 10-q, capital invertido operativo, deuda de balance sin arrendamientos operativos, eps básico, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet, roic terminal (criterio damodaran) (27 celdas, con respaldo). DCF esperado US$148,68 → US$157,00. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (bloque Base de 'Valuation output': US$176,10 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja calcula estos cuatro DCF en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

EPAM vende ingeniería de software, datos, nube e IA a grandes empresas, con equipos en Europa Central y del Este, Asia y América Latina, y cobra casi todo por tiempo y materiales. Fue una de las mejores historias de crecimiento de servicios de TI hasta 2021 (la acción llegó a US$668). Después vinieron la guerra en Ucrania (reubicación de miles de ingenieros), la caída del gasto discrecional y la IA generativa, que amenaza con reducir las horas de programación que EPAM factura. Los ingresos se estancaron en 2023-2024, repuntaron en 2025 con compras (+15,4%) y en el 1S26 crecen 6% (4,5% en el 2T). La historia de cinco años es si la IA es una deflación de horas o una nueva ola de proyectos de ingeniería (datos, agentes, modernización) en la que EPAM está bien posicionada.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~5% anual cinco años | Sí | Sí: +6% en el 1S26 con Europa +10% | Probable |
| La IA reduce las horas facturables netas | Sí | Sí: la programación rutinaria se automatiza; EPAM está en el segmento de mayor valor | Posible, gradual |
| El margen GAAP sube de ~10% a 12,5% | Sí | Poco: el margen cae desde 2021 (compresión de tarifas y reubicación) | Media-baja |
| EPAM vuelve a crecer a doble dígito orgánico | Sí | Solo si la IA genera una ola de proyectos grandes | Baja |


### Visión externa: tasas base

Con ventas LTM de US$5.617 millones (US$3.974 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **$3,000-4,500 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 5,4% y una mediana de 4,7% (desviación estándar 8,5%); sumando una inflación de 2,5%, la mediana nominal ronda 7,2%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · La IA compensa lo que quita: crecimiento moderado | 5,5% | 60% |
| Conservadora · Deflación de horas por IA | 2,1% | 80% |
| Disrupción · Deterioro de los fundamentales: Los servicios se comoditizan | −1,1% | 90% |
| Optimista · La IA crea demanda de ingeniería | 8,6% | 42% |

En dólares de 2015 la empresa está en el tramo de US$3.000-4.500 millones: crecer 5,5% anual cinco años (Base) lo logró ~60% de las empresas de ese tamaño; 8,6% (Optimista), ~42%. La hoja (5%) es modesta. El valor de EPAM depende menos del crecimiento que del margen, que la hoja espera recuperar (de ~10% a 12,5%).


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: modesto, porque la pregunta es la IA.** EPAM vende ingeniería de software, datos, nube e IA a grandes empresas y cobra casi todo por tiempo y materiales: gana por hora facturada. Fue una de las mejores historias de servicios de TI hasta 2021; después vinieron la guerra en Ucrania (reubicación de miles de ingenieros), la caída del gasto discrecional y la IA generativa, que puede reducir las horas que EPAM factura. Los ingresos se estancaron en 2023-2024, saltaron 15,4% en 2025 por compras (Neoris, First Derivative) y en el 2T26 crecieron 4,5%, con Europa +10%. La Base sigue lo que se ve: Norteamérica de 4% a 5%, Europa de 8% bajando a 6%; 5,6% el primer año y 5,5% compuesto, una cifra que lograron ~60% de las empresas de su tamaño. No extrapolamos 2025 porque fue comprado. La Conservadora (2,1%) es la deflación de horas: los clientes producen el mismo software con menos horas; la Disrupción (−1,1%), la comoditización con ingresos en caída; la Optimista (8,6%), que la IA dispare proyectos de datos y modernización. Dos trimestres de crecimiento orgánico negativo invalidarían la Base.

**Margen: la pieza más frágil.** El margen operativo GAAP pasó de ~14% en 2021 a 9,5% en 2025 y 10,0% LTM: menos utilización de ingenieros, tarifas presionadas, costos de reubicación y de integración. La Base supone que se recupera a 12% (en el modelo 12,5%, con el ajuste por arrendamientos). Es la apuesta más discutible de la Base, porque si la IA reduce las horas difícilmente sube el margen: una empresa que cobra por hora gana menos si cada proyecto necesita menos horas, salvo que suba la tarifa. Por eso el margen pesa más que el crecimiento: dos puntos de margen mueven la Base a US$150,48 (−15%) o US$201,73 (+15%), más que dos puntos de crecimiento. Lo invalidaría un margen GAAP por debajo de 9%. El rango de las historias va de 8,5% a 14,5%.

**Reinversión: personas, no fábricas.** EPAM casi no necesita capital físico (capex de ~US$30-40 millones al año) y tiene caja neta de ~US$680 millones. La hoja usa un ventas/capital de 3,27× y 2,83×: ~US$0,31 de capital por dólar de ventas nuevas. La reinversión real es en personas (formación en IA) y en compras; en los últimos doce meses recompró US$715 millones (las acciones bajaron de 57 a 52 millones). El ROIC cayó de 47% a ~15% en cinco años: la ventaja existe —costos de cambio moderados con clientes grandes— pero se está desvaneciendo. Por eso el ROIC después del año 10 es 12,0%, el punto medio entre el costo de capital y la industria, limitado al ROIC actual. Si la ventaja desapareciera del todo, la Base valdría US$151,98 (−14%); la Conservadora y la Disrupción ya usan el costo de capital.

**Descuento: la beta de regresión cuenta la guerra.** La hoja usa una beta de 1,30; la bottom-up de servicios de computación da 0,98, con la que el DCF técnico sube de forma notable. La diferencia refleja que la regresión de EPAM incorpora el shock geopolítico de 2022. El criterio de Damodaran prefiere la bottom-up, pero la entrega desde Europa del Este justifica algo por encima del sector, así que la Base se queda con la de la hoja, del lado prudente. El costo de capital va de 10,62% a 9,00%; un punto menos lleva la Base a US$225,88 (+28%). El crecimiento perpetuo es 4,99% y el terminal explica 62,2% del valor operativo.

**Probabilidades y lectura del resultado.** La Base pesa 45%; la Conservadora 30%, el riesgo que el mercado más teme; la Disrupción 10%; la Optimista 15%. El DCF Base es US$176,10 y el esperado US$157,00, frente a un precio de US$108,29: el mercado valora algo más cercano a la Conservadora (US$114,90). La evidencia en contra de la Base es que el margen cae desde 2021 y Norteamérica crece a un dígito bajo; si 2027 no muestra recuperación, la Conservadora se vuelve la central. Las acciones se fijan en 51,6 millones; las recompras no se modelan.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$5.617 millones. Con el crecimiento de la Base llegan a US$7.355 millones en el año 5 y a US$9.459 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 11,0% en el año 1 a 12,5% al final, y se descuentan impuestos (26,8% al principio y 24,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$479 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$106 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$373 millones el primer año. Cada flujo se trae a hoy con el costo de capital (10,62% al principio, 9,00% al final): los diez años suman US$3.189 millones. Después del año 10 se supone que la empresa crece 4,99% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 12,0%; esa perpetuidad vale hoy US$5.246 millones, 62% del total. Flujos más terminal dan el valor de las operaciones, US$8.435 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$789 millones, menos deuda por US$138 millones (incluye los arrendamientos capitalizados). Queda un patrimonio de US$9.087 millones que, repartido entre 51,6 millones de acciones, da US$176,10 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 9,19× (peso 33% dentro de los múltiplos); EV/FCFF 12,51× (peso 17% dentro de los múltiplos); P/E 13,71× (peso 33% dentro de los múltiplos); P/FCFE 12,56× (peso 8% dentro de los múltiplos); P/OCF 11,46× (peso 8% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (10,8%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$176,10; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$150,48 | −14,6% |
| Margen objetivo +2 pp | US$201,73 | +14,6% |
| Crecimiento años 1–5 −2 pp | US$161,39 | −8,4% |
| Crecimiento años 1–5 +2 pp | US$192,40 | +9,3% |
| Ventas/capital −20% | US$172,41 | −2,1% |
| Ventas/capital +20% | US$178,57 | +1,4% |
| WACC +1 pp | US$145,92 | −17,1% |
| WACC −1 pp | US$225,88 | +28,3% |
| Crecimiento terminal −0,5 pp | US$169,79 | −3,6% |
| Crecimiento terminal +0,5 pp | US$184,03 | +4,5% |
| ROIC terminal = costo de capital | US$151,98 | −13,7% |
| Acciones +5% | US$167,72 | −4,8% |


### Piezas del valor

**Crecimiento.** Ingresos de US$4.691 millones (2023, −2,8%), US$4.728 millones (2024, +0,8%) y US$5.457 millones (2025, +15,4% con compras como Neoris y First Derivative); LTM US$5.617 millones. En el 2T26 facturó US$1.414,8 millones (+4,5%), con Europa +10%. La división de las historias (Norteamérica ~57%, Europa ~40%, otros ~3%) es una aproximación: la empresa reporta por geografía de clientes y la diferencia entre el total y Europa la calcula el informe.

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 4.691 | 4.728 | 5.457 | 5.617 |
| Crecimiento | −2,8% | +0,8% | +15,4% | — |
| Margen operativo GAAP | 10,7% | 11,5% | 9,5% | 10,0% |
| FCFF (hoja) | 437 | 513 | 527 | — |

**Márgenes.** El margen operativo GAAP pasó de ~14% en 2021 a 9,5% en 2025 y 10,0% LTM: menos utilización, tarifas presionadas, reubicación desde Ucrania y Belarús y costos de integración. La hoja supone 10,5% el próximo año y 12,5% de objetivo. Es la pieza más frágil: si la IA baja las horas, el margen difícilmente sube. Las historias van de 8% a 14%.

**Reinversión y retorno.** Casi no necesita capital físico (capex de ~US$30-40 millones al año) y tiene caja neta de ~US$680 millones. La hoja usa un sales-to-capital de 3,5 y 3. La reinversión real es en personas (formación en IA) y compras; en los últimos doce meses recompró US$715 millones (las acciones bajaron de 57 a 52 millones). Ventaja que se desvanece: costos de cambio moderados en servicios de ingeniería, pero con un ROIC que bajó de 47% a 15% en cinco años y deflación de horas por la IA. El ROIC después del año 10 es 12,0%, el punto medio entre el costo de capital terminal (9,0%) y el promedio de su industria según Damodaran (26,4%), limitado a su ROIC actual (13,8%).

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$113 millones, compromisos del 10-K al 2025-12-31) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$30 millones, +0,53 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,02 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usa una beta de 1,30. La beta bottom-up de Computer Services (64 empresas, 0,96 desapalancada y corregida por caja) sin deuda relevante da 0,97, y el DCF Base sube de US$178,25 a US$191,69. La diferencia refleja que la beta de regresión de EPAM incorpora el shock geopolítico de 2022; con criterio Damodaran conviene la bottom-up, pero el riesgo operativo de Europa del Este justifica algo por encima del sector.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,30 | 10,8% | 10,6% | US$178,14 |
| Bottom-up del sector (Computer Services, reapalancada) | 0,98 | 9,4% | 9,2% | US$191,58 |


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja que se desvanece | 15,1% | 26,4% | 9,0% | 12,0% | US$176,10 | US$153,55 |

Fuentes de ventaja: Servicios de ingeniería con costos de cambio moderados. Evidencia: ROIC 47% → 15% en cinco años, acercándose al costo de capital. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$176,10 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$157,00. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$5.617 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 3.200 + 2.250 + 167 = 5.617. |
| Margen inicial del DCF | 11,0% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 26,79% en años 1–5; 24,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 10,62% → 9,00% | Tasa libre de riesgo 4,99%, beta 1,30, ERP 4,46%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 3,27x en años 1–5; 2,83x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 4,99%; Disrupción: 0,97% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (0,97%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Optimista: 12,00%; Conservadora/Disrupción: 9,00% (= WACC terminal) | Criterio de ventaja competitiva (ventaja que se desvanece). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 789; deuda 138; acciones 51,6 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 3.200 × 1,04 + 2.250 × 1,08 + 167 × 1,05 = US$5.933,03 millones. Frente a 5.617, el crecimiento consolidado es 5,63%. En los años 2–5 es 5,82%, 5,41%, 5,42%, 5,42%; las ventas del año 5 son US$7.354,71 millones. El 5,5% de la tabla es el crecimiento anual compuesto de los cinco años: (7.354,71 / 5.617)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 5.933,03 × 11,03% × (1 − 26,79%) = US$479,02 millones. La reinversión es US$105,56 millones y el FCFF es US$373,46 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,00%. Reinversión terminal sobre el NOPAT: Base, 41,6% (4,99% / 12,00%); Conservadora, 55,4% (4,99% / 9,00%); Disrupción, 10,8% (0,97% / 9,00%); Optimista, 41,6% (4,99% / 12,00%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · La IA compensa lo que quita: crecimiento moderado** — probabilidad 45%; valor terminal 13.775,1 (VP 5.245,9); DCF US$176,10 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5.933,0 | 5,6% | 11,0% | 479,0 | 105,6 | 373,5 | 10,6% | 337,6 |
| 2 | 6.278,3 | 5,8% | 11,6% | 534,5 | 103,9 | 430,5 | 10,6% | 351,8 |
| 3 | 6.618,2 | 5,4% | 11,9% | 577,9 | 109,6 | 468,3 | 10,6% | 345,9 |
| 4 | 6.976,7 | 5,4% | 12,2% | 624,6 | 115,6 | 509,0 | 10,6% | 339,9 |
| 5 | 7.354,7 | 5,4% | 12,5% | 674,6 | 119,9 | 554,6 | 10,6% | 334,8 |
| 6 | 7.746,9 | 5,3% | 12,5% | 716,0 | 143,6 | 572,3 | 10,3% | 313,2 |
| 7 | 8.153,4 | 5,2% | 12,5% | 759,2 | 148,7 | 610,5 | 10,0% | 303,8 |
| 8 | 8.574,3 | 5,2% | 12,5% | 804,4 | 153,8 | 650,6 | 9,6% | 295,3 |
| 9 | 9.009,5 | 5,1% | 12,5% | 851,5 | 158,9 | 692,7 | 9,3% | 287,5 |
| 10 | 9.459,1 | 5,0% | 12,5% | 900,6 | 166,8 | 733,8 | 9,0% | 279,5 |
| Terminal | 9.931,1 | 5,0% | 12,5% | 945,6 | 393,2 | 552,4 | 9,0% | — |

**Conservadora · Deflación de horas por IA** — probabilidad 30%; valor terminal 7.054,1 (VP 2.686,4); DCF US$114,90 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5.706,7 | 1,6% | 11,0% | 460,7 | 31,2 | 429,5 | 10,6% | 388,3 |
| 2 | 5.808,9 | 1,8% | 10,8% | 460,5 | 41,9 | 418,6 | 10,6% | 342,1 |
| 3 | 5.945,8 | 2,4% | 10,7% | 467,0 | 42,9 | 424,1 | 10,6% | 313,2 |
| 4 | 6.086,2 | 2,4% | 10,6% | 473,6 | 44,0 | 429,6 | 10,6% | 286,8 |
| 5 | 6.230,2 | 2,4% | 10,5% | 480,2 | 55,1 | 425,2 | 10,6% | 256,6 |
| 6 | 6.410,2 | 2,9% | 10,5% | 497,9 | 77,4 | 420,5 | 10,3% | 230,1 |
| 7 | 6.629,2 | 3,4% | 10,5% | 518,8 | 92,3 | 426,4 | 10,0% | 212,2 |
| 8 | 6.890,4 | 3,9% | 10,5% | 543,2 | 108,7 | 434,5 | 9,6% | 197,2 |
| 9 | 7.198,0 | 4,5% | 10,5% | 571,7 | 126,9 | 444,8 | 9,3% | 184,6 |
| 10 | 7.557,2 | 5,0% | 10,5% | 604,7 | 133,3 | 471,4 | 9,0% | 179,5 |
| Terminal | 7.934,3 | 5,0% | 10,5% | 634,9 | 352,0 | 282,9 | 9,0% | — |

**Disrupción · Deterioro de los fundamentales: Los servicios se comoditizan** — probabilidad 10%; valor terminal 4.047,6 (VP 1.541,4); DCF US$85,29 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5.456,7 | −2,8% | 11,0% | 440,6 | -50,9 | 491,5 | 10,6% | 444,3 |
| 2 | 5.290,1 | −3,1% | 10,0% | 388,4 | -17,8 | 406,2 | 10,6% | 331,9 |
| 3 | 5.231,8 | −1,1% | 9,5% | 365,0 | 6,7 | 358,2 | 10,6% | 264,6 |
| 4 | 5.253,8 | 0,4% | 9,0% | 347,3 | 15,6 | 331,7 | 10,6% | 221,5 |
| 5 | 5.304,7 | 1,0% | 8,5% | 331,2 | 15,7 | 315,5 | 10,6% | 190,4 |
| 6 | 5.356,0 | 1,0% | 8,5% | 337,0 | 18,3 | 318,6 | 10,3% | 174,4 |
| 7 | 5.407,9 | 1,0% | 8,5% | 342,8 | 18,5 | 324,3 | 10,0% | 161,4 |
| 8 | 5.460,2 | 1,0% | 8,5% | 348,7 | 18,7 | 330,0 | 9,6% | 149,8 |
| 9 | 5.513,1 | 1,0% | 8,5% | 354,7 | 18,9 | 335,8 | 9,3% | 139,4 |
| 10 | 5.566,5 | 1,0% | 8,5% | 360,8 | 19,0 | 341,7 | 9,0% | 130,1 |
| Terminal | 5.620,4 | 1,0% | 8,5% | 364,3 | 39,2 | 325,1 | 9,0% | — |

**Optimista · La IA crea demanda de ingeniería** — probabilidad 15%; valor terminal 19.373 (VP 7.378); DCF US$231,70 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 6.111 | 8,8% | 11,0% | 493 | 175 | 318 | 10,6% | 288 |
| 2 | 6.684 | 9,4% | 12,4% | 608 | 183 | 425 | 10,6% | 347 |
| 3 | 7.284 | 9,0% | 13,1% | 700 | 178 | 522 | 10,6% | 385 |
| 4 | 7.866 | 8,0% | 13,8% | 796 | 192 | 604 | 10,6% | 403 |
| 5 | 8.496 | 8,0% | 14,5% | 904 | 192 | 711 | 10,6% | 429 |
| 6 | 9.124 | 7,4% | 14,5% | 978 | 219 | 759 | 10,3% | 415 |
| 7 | 9.744 | 6,8% | 14,5% | 1.052 | 213 | 839 | 10,0% | 417 |
| 8 | 10.348 | 6,2% | 14,5% | 1.126 | 204 | 921 | 9,6% | 418 |
| 9 | 10.926 | 5,6% | 14,5% | 1.198 | 193 | 1.005 | 9,3% | 417 |
| 10 | 11.472 | 5,0% | 14,5% | 1.267 | 202 | 1.064 | 9,0% | 405 |
| Terminal | 12.044 | 5,0% | 14,5% | 1.330 | 553 | 777 | 9,0% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 3.189,21 | 5.245,88 | 8.435,10 | 9.086,87 | 176,10 |
| Conservadora | 2.590,67 | 2.686,35 | 5.277,02 | 5.928,79 | 114,90 |
| Disrupción | 2.207,81 | 1.541,44 | 3.749,25 | 4.401,02 | 85,29 |
| Optimista | 3.926,15 | 7.377,61 | 11.303,76 | 11.955,54 | 231,70 |

Ejemplo Base: (3.189,21 + 5.245,88 + 789 − 138) / 51,6 = US$176,10 por acción. El terminal representa 62,2% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 45% / 30% / 10% / 15% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,45 × 176,102205 + 0,30 × 114,899112 + 0,10 × 85,291159 + 0,15 × 231,696439 = US$156,999308 ≈ US$157,00. Los aportes son US$79,25 + US$34,47 + US$8,53 + US$34,75 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 156,999308 × 0,65 = US$102,049550 ≈ US$102,05. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$176,10, es el valor intrínseco principal. El DCF esperado de US$157,00 combina las cuatro tesis con sus probabilidades y se presenta como complemento. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: La IA compensa lo que quita: crecimiento moderado

**Qué plantea.** Es lo que muestra 2026: un dígito medio con Europa más fuerte.

**Traducción al modelo.** Norteamérica crece 4%, 5%, 5%, 5%, 5%; Europa crece 8%, 7%, 6%, 6%, 6%; Otros mercados crece 5%, 5%, 5%, 5%, 5%. El crecimiento anual compuesto de cinco años es 5,5%; el margen operativo objetivo es 12,5%. El ROIC terminal es 12,0%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 45%; DCF: US$176,10 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (crecimiento de ingresos (orgánico, sin divisas): +4,5% (2T26); margen operativo GAAP: 10,0% LTM; norteamérica (interanual): Bajo un dígito). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: Deflación de horas por IA

**Qué plantea.** Es la deflación de horas por IA, el riesgo que el mercado más teme.

**Traducción al modelo.** Norteamérica crece 0%, 1%, 2%, 2%, 2%; Europa crece 4%, 3%, 3%, 3%, 3%; Otros mercados crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 2,1%; el margen operativo objetivo es 10,5%. El ROIC terminal es el costo de capital (9,00%). El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 30%; DCF: US$114,90 por acción.

**Cómo contrastarla.** La apoyarían: crecimiento de ingresos (orgánico, sin divisas): negativo dos trimestres; margen operativo GAAP: < 9%; norteamérica (interanual): negativo; utilización de ingenieros: en baja.


#### Disrupción · Deterioro de los fundamentales: Los servicios se comoditizan

**Qué plantea.** Es la comoditización con ingresos en caída.

**Traducción al modelo.** Norteamérica crece -5%, -4%, -2%, 0%, 1%; Europa crece 0%, -2%, 0%, 1%, 1%; Otros mercados crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es −1,1%; el margen operativo objetivo es 8,5%. El ROIC terminal es el costo de capital (9,00%). El crecimiento terminal es 0,97%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 10%; DCF: US$85,29 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: crecimiento de ingresos (orgánico, sin divisas): negativo dos trimestres; margen operativo GAAP: < 9%; norteamérica (interanual): negativo; utilización de ingenieros: en baja.


#### Optimista: La IA crea demanda de ingeniería

**Qué plantea.** Supone que la IA dispara proyectos de datos y modernización.

**Traducción al modelo.** Norteamérica crece 8%, 9%, 9%, 8%, 8%; Europa crece 10%, 10%, 9%, 8%, 8%; Otros mercados crece 8%, 8%, 8%, 8%, 8%. El crecimiento anual compuesto de cinco años es 8,6%; el margen operativo objetivo es 14,5%. El ROIC terminal es 12,0%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 15%; DCF: US$231,70 por acción.

**Cómo contrastarla.** La confirmarían: crecimiento de ingresos (orgánico, sin divisas): ≥ +6%; margen operativo GAAP: ≥ 11%; norteamérica (interanual): ≥ +5%; utilización de ingenieros: en alza.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 4,99%; Disrupción: 0,97%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,30) | Valor/acción (beta 0,98) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| **Base · La IA compensa lo que quita: crecimiento moderado** | 45% | Norteamérica: 4%, 5%, 5%, 5%, 5%; Europa: 8%, 7%, 6%, 6%, 6%; Otros mercados: 5%, 5%, 5%, 5%, 5% | 5,5% | 12,5% | 3,3 | 12,0% | 4,99% | US$176,10 | US$189,34 |
| **Conservadora · Deflación de horas por IA** | 30% | Norteamérica: 0%, 1%, 2%, 2%, 2%; Europa: 4%, 3%, 3%, 3%, 3%; Otros mercados: 0%, 0%, 0%, 0%, 0% | 2,1% | 10,5% | 3,3 | = costo de capital | 4,99% | US$114,90 | US$122,55 |
| **Disrupción · Deterioro de los fundamentales: Los servicios se comoditizan** | 10% | Norteamérica: -5%, -4%, -2%, 0%, 1%; Europa: 0%, -2%, 0%, 1%, 1%; Otros mercados: 0%, 0%, 0%, 0%, 0% | −1,1% | 8,5% | 3,3 | = costo de capital | 0,97% | US$85,29 | US$90,28 |
| **Optimista · La IA crea demanda de ingeniería** | 15% | Norteamérica: 8%, 9%, 9%, 8%, 8%; Europa: 10%, 10%, 9%, 8%, 8%; Otros mercados: 8%, 8%, 8%, 8%, 8% | 8,6% | 14,5% | 3,3 | 12,0% | 4,99% | US$231,70 | US$249,99 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  |  | **US$157,00** | **US$168,49** |

Base (45%) es lo que muestra 2026: un dígito medio con Europa más fuerte. Conservadora (30%) es la deflación de horas por IA, el riesgo que el mercado más teme. Disrupción (10%) es la comoditización con ingresos en caída. Optimista (15%) supone que la IA dispara proyectos de datos y modernización. En las historias de erosión (Conservadora y Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 1,30; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.

| Crecimiento \ Margen | 9,0% | 11,0% | 13,0% | 15,0% | 17,0% |
|---|---:|---:|---:|---:|---:|
| 1,5% | 113,16 | 133,20 | 153,24 | 173,29 | 193,33 |
| 3,5% | 121,80 | 144,49 | 167,19 | 189,89 | 212,59 |
| 5,5% | 131,33 | 157,00 | 182,67 | 208,34 | 234,01 |
| 7,5% | 141,86 | 170,84 | 199,82 | 228,80 | 257,78 |
| 9,5% | 153,48 | 186,15 | 218,82 | 251,49 | 284,16 |


### Pre-mortem

1. Los clientes usan IA para producir el mismo software con 20-30% menos horas y renegocian contratos.
2. La competencia de India (TCS, Infosys) y de las consultoras con IA baja las tarifas.
3. El margen sigue cayendo por baja utilización y costos de reubicación.
4. Un nuevo shock geopolítico en Europa del Este afecta la entrega.
5. Las compras recientes no se integran bien y generan deterioro.

**Evidencia en contra de la historia más probable:** el margen cae desde 2021 y el crecimiento orgánico es de un dígito bajo en Norteamérica; si 2027 no muestra recuperación, la historia Conservadora se vuelve la central.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Crecimiento de ingresos (orgánico, sin divisas) | +4,5% (2T26) | ≥ +6% | Negativo dos trimestres |
| Margen operativo GAAP | 10,0% LTM | ≥ 11% | < 9% |
| Norteamérica (interanual) | Bajo un dígito | ≥ +5% | Negativo |
| Utilización de ingenieros | Estable | En alza | En baja |
| Ingresos de proyectos de IA y datos | En aumento | Más de 20% de los ingresos | Estancados |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$108,29**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 10% | Margen 11% | Margen 13% |
|---|---:|---:|---:|
| Beta 1,30 | −0,8% (89% de las empresas) | −3,8% (95% de las empresas) | −6,9% (97% de las empresas) |
| Beta 0,98 | −2,5% (94% de las empresas) | −5,4% (96% de las empresas) | −8,4% (98% de las empresas) |

Frente al DCF Base (US$176,10), el valor intrínseco principal, el precio está por debajo en 39%.

Frente al DCF esperado de las historias (US$157,00 con la beta de la hoja; US$168,49 con la propuesta), el precio está por debajo en 31% y por debajo en 36%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Ingeniería de software de alta calidad frente a la deflación de horas por IA |  |
| Probabilidades | Base 45% / Conservadora 30% / Disrupción 10% / Optimista 15% |  |
| DCF Base hoy (valor intrínseco principal) | US$176,10 |  |
| DCF esperado por probabilidades (complemento) (beta de la hoja / propuesta) | US$157,00 / US$168,49 |  |
| Precio con MOS sobre el DCF esperado | US$102,05 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$85,29 a US$249,99 |  |
| Confianza | Media-baja: el efecto neto de la IA sobre las horas facturables es el gran desconocido |  |
| Qué cambiaría la opinión | Crecimiento orgánico en Norteamérica y margen operativo en 2027 |  |
| Revisión | Resultados del 3T26 (nov-2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [EPAM, Form 10-Q del 2T 2026](https://www.sec.gov/Archives/edgar/data/1352010/000135201026000046/epam-20260630.htm)
- [EPAM, Form 10-Q del 1T 2026](https://www.sec.gov/Archives/edgar/data/1352010/000135201026000029/epam-20260331.htm)
- [EPAM, Form 10-K 2025](https://www.sec.gov/Archives/edgar/data/1352010/000135201026000015/epam-20251231.htm)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
