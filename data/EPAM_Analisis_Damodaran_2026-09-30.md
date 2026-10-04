---
schema: "jmr-analisis-damodaran-v1"
ticker: "EPAM"
analysis_date: "2026-09-30"
---

# EPAM Systems, Inc. (EPAM) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$172,32 por acción** (Base · La IA compensa lo que quita: crecimiento moderado).

**Complemento · DCF esperado por probabilidades: US$154,35.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$85,80–225,79. El MOS 35% se aplica al esperado: US$100,33. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), balance del último 10-q, capital invertido operativo, deuda de balance sin arrendamientos operativos, eps básico, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet, roic terminal (criterio damodaran) (27 celdas, con respaldo). DCF esperado US$148,68 → US$156,31. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (bloque Base de 'Valuation output': US$172,32 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja calcula estos cuatro DCF en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


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

**Margen: la pieza más frágil.** El margen operativo GAAP pasó de ~14% en 2021 a 9,5% en 2025 y 10,0% LTM: menos utilización de ingenieros, tarifas presionadas, costos de reubicación y de integración. La Base supone que se recupera a 12% (en el modelo 12,6%, con el ajuste por arrendamientos). Es la apuesta más discutible de la Base, porque si la IA reduce las horas difícilmente sube el margen: una empresa que cobra por hora gana menos si cada proyecto necesita menos horas, salvo que suba la tarifa. Por eso el margen pesa más que el crecimiento: dos puntos de margen mueven la Base a US$146,90 (−15%) o US$197,74 (+15%), más que dos puntos de crecimiento. Lo invalidaría un margen GAAP por debajo de 9%. El rango de las historias va de 8,6% a 14,6%.

**Reinversión: personas, no fábricas.** EPAM casi no necesita capital físico (capex de ~US$30-40 millones al año) y tiene caja neta de ~US$680 millones. La hoja usa un ventas/capital de 2,65× y 2,65×: ~US$0,38 de capital por dólar de ventas nuevas. La reinversión real es en personas (formación en IA) y en compras; en los últimos doce meses recompró US$715 millones (las acciones bajaron de 57 a 52 millones). El ROIC cayó de 47% a ~15% en cinco años: la ventaja existe —costos de cambio moderados con clientes grandes— pero se está desvaneciendo. Por eso el ROIC después del año 10 es 12,0%, el punto medio entre el costo de capital y la industria, limitado al ROIC actual. Si la ventaja desapareciera del todo, la Base valdría US$150,50 (−13%); la Conservadora y la Disrupción ya usan el costo de capital.

**Descuento: la beta de regresión cuenta la guerra.** La hoja usa una beta de 0,98; la bottom-up de servicios de computación da 0,98, con la que el DCF técnico sube de forma notable. La diferencia refleja que la regresión de EPAM incorpora el shock geopolítico de 2022. El criterio de Damodaran prefiere la bottom-up, pero la entrega desde Europa del Este justifica algo por encima del sector, así que la Base se queda con la de la hoja, del lado prudente. El costo de capital va de 10,09% a 9,38%; un punto menos lleva la Base a US$220,02 (+28%). El crecimiento perpetuo es 5,29% y el terminal explica 62,0% del valor operativo.

**Probabilidades y lectura del resultado.** La Base pesa 45%; la Conservadora 30%, el riesgo que el mercado más teme; la Disrupción 10%; la Optimista 15%. El DCF Base es US$172,32 y el esperado US$154,35, frente a un precio de US$108,29: el mercado valora algo más cercano a la Conservadora (US$114,53). La evidencia en contra de la Base es que el margen cae desde 2021 y Norteamérica crece a un dígito bajo; si 2027 no muestra recuperación, la Conservadora se vuelve la central. Las acciones se fijan en 51,6 millones; las recompras no se modelan.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$5.617 millones. Con el crecimiento de la Base llegan a US$7.355 millones en el año 5 y a US$9.540 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 11,1% en el año 1 a 12,6% al final, y se descuentan impuestos (26,8% al principio y 24,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$481 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$130 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$350 millones el primer año. Cada flujo se trae a hoy con el costo de capital (10,09% al principio, 9,38% al final): los diez años suman US$3.133 millones. Después del año 10 se supone que la empresa crece 5,29% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 12,0%; esa perpetuidad vale hoy US$5.114 millones, 62% del total. Flujos más terminal dan el valor de las operaciones, US$8.247 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$789 millones, menos deuda por US$145 millones (incluye los arrendamientos capitalizados). Queda un patrimonio de US$8.892 millones que, repartido entre 51,6 millones de acciones, da US$172,32 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 8,47× (peso 33% dentro de los múltiplos); EV/FCFF 13,16× (peso 17% dentro de los múltiplos); P/E 14,35× (peso 33% dentro de los múltiplos); P/FCFE 13,39× (peso 8% dentro de los múltiplos); P/OCF 12,10× (peso 8% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (10,2%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$172,32; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$146,90 | −14,8% |
| Margen objetivo +2 pp | US$197,74 | +14,8% |
| Crecimiento años 1–5 −2 pp | US$158,70 | −7,9% |
| Crecimiento años 1–5 +2 pp | US$187,40 | +8,7% |
| Ventas/capital −20% | US$167,87 | −2,6% |
| Ventas/capital +20% | US$175,29 | +1,7% |
| WACC +1 pp | US$143,10 | −17,0% |
| WACC −1 pp | US$220,02 | +27,7% |
| Crecimiento terminal −0,5 pp | US$166,71 | −3,3% |
| Crecimiento terminal +0,5 pp | US$179,31 | +4,1% |
| ROIC terminal = costo de capital | US$150,50 | −12,7% |
| Acciones +5% | US$164,12 | −4,8% |


### Piezas del valor

**Crecimiento.** Ingresos de US$4.691 millones (2023, −2,8%), US$4.728 millones (2024, +0,8%) y US$5.457 millones (2025, +15,4% con compras como Neoris y First Derivative); LTM US$5.617 millones. En el 2T26 facturó US$1.414,8 millones (+4,5%), con Europa +10%. La división de las historias (Norteamérica ~57%, Europa ~40%, otros ~3%) es una aproximación: la empresa reporta por geografía de clientes y la diferencia entre el total y Europa la calcula el informe.

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 4.691 | 4.728 | 5.457 | 5.617 |
| Crecimiento | −2,8% | +0,8% | +15,4% | — |
| Margen operativo GAAP | 10,7% | 11,5% | 9,5% | 10,0% |
| FCFF (hoja) | 437 | 513 | 527 | — |

**Márgenes.** El margen operativo GAAP pasó de ~14% en 2021 a 9,5% en 2025 y 10,0% LTM: menos utilización, tarifas presionadas, reubicación desde Ucrania y Belarús y costos de integración. La hoja supone 10,5% el próximo año y 12,5% de objetivo. Es la pieza más frágil: si la IA baja las horas, el margen difícilmente sube. Las historias van de 8% a 14%.

**Reinversión y retorno.** Casi no necesita capital físico (capex de ~US$30-40 millones al año) y tiene caja neta de ~US$680 millones. La hoja usa un ventas/capital de 2,65 (años 1-5) y 2,65 (años 6-10): con margen objetivo de 13,1% e impuesto marginal de 24%, cada dólar de capital nuevo rinde ~26% y ~26%, sin superar el mayor entre su ROIC actual (15,2%) y el de su industria (26,4%) (Damodaran, Investment Valuation cap. 11, p. 45; revisión del 4-oct-2026). Antes 3,27 y 2,83, que implicaban ~32% y ~28% sobre el capital nuevo. La reinversión real es en personas (formación en IA) y compras; en los últimos doce meses recompró US$715 millones (las acciones bajaron de 57 a 52 millones). Ventaja que se desvanece: costos de cambio moderados en servicios de ingeniería, pero con un ROIC que bajó de 47% a 15% en cinco años y deflación de horas por la IA. El ROIC después del año 10 es 12,0%, el punto medio entre el costo de capital terminal (9,0%) y el promedio de su industria según Damodaran (26,4%), limitado a su ROIC actual (13,8%).

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$121 millones, compromisos del 10-Q al 2026-06-30) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$32 millones, +0,57 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,02 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usa una beta de 0,98 (desde el 3-oct-2026; antes 1,30). Regla de la cartera (prompt v4, paso 2): bottom-up de Computer Services (Damodaran, ene-2026: 0,96 desapalancada y corregida por caja) reapalancada con la D/E de mercado 0,03 = 0,98 = 0,98. La de regresión queda como referencia. El riesgo de la entrega desde Europa del Este va en la prima de mercado ponderada por operaciones, no en la beta. El efecto de cada beta en el DCF Base está en la tabla.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 0,98 | 10,2% | 10,1% | US$174,18 |
| Bottom-up del sector (Computer Services, reapalancada) | 0,98 | 10,2% | 10,1% | US$174,18 |


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja que se desvanece | 15,1% | 26,4% | 9,4% | 12,0% | US$172,32 | US$151,94 |

Fuentes de ventaja: Servicios de ingeniería con costos de cambio moderados. Evidencia: ROIC 47% → 15% en cinco años, acercándose al costo de capital. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$172,32 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$154,35. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$5.617 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 3.200 + 2.250 + 167 = 5.617. |
| Margen inicial del DCF | 11,1% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 26,79% en años 1–5; 24,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 10,09% → 9,38% | Tasa libre de riesgo 5,29%, beta 0,98, ERP 5,05%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 2,65x en años 1–5; 2,65x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 5,29%; Disrupción: 0,97% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (0,97%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Optimista: 12,00%; Conservadora/Disrupción: 9,38% (= WACC terminal) | Criterio de ventaja competitiva (ventaja que se desvanece). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 789; deuda 145; acciones 51,6 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 3.200 × 1,04 + 2.250 × 1,08 + 167 × 1,05 = US$5.933,03 millones. Frente a 5.617, el crecimiento consolidado es 5,63%. En los años 2–5 es 5,82%, 5,41%, 5,42%, 5,42%; las ventas del año 5 son US$7.354,71 millones. El 5,5% de la tabla es el crecimiento anual compuesto de los cinco años: (7.354,71 / 5.617)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 5.933,03 × 11,07% × (1 − 26,79%) = US$480,65 millones. La reinversión es US$130,28 millones y el FCFF es US$350,37 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,38%. Reinversión terminal sobre el NOPAT: Base, 44,1% (5,29% / 12,00%); Conservadora, 56,4% (5,29% / 9,38%); Disrupción, 10,3% (0,97% / 9,38%); Optimista, 44,1% (5,29% / 12,00%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · La IA compensa lo que quita: crecimiento moderado** — probabilidad 45%; valor terminal 13.115,2 (VP 5.114,1); DCF US$172,32 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5.933,0 | 5,6% | 11,1% | 480,7 | 130,3 | 350,4 | 10,1% | 318,3 |
| 2 | 6.278,3 | 5,8% | 11,7% | 536,2 | 128,3 | 407,9 | 10,1% | 336,6 |
| 3 | 6.618,2 | 5,4% | 12,0% | 579,8 | 135,3 | 444,5 | 10,1% | 333,2 |
| 4 | 6.976,7 | 5,4% | 12,3% | 626,5 | 142,7 | 483,8 | 10,1% | 329,4 |
| 5 | 7.354,7 | 5,4% | 12,6% | 676,6 | 149,7 | 526,9 | 10,1% | 325,9 |
| 6 | 7.751,3 | 5,4% | 12,6% | 718,5 | 157,0 | 561,5 | 9,9% | 315,9 |
| 7 | 8.167,4 | 5,4% | 12,6% | 762,8 | 164,6 | 598,2 | 9,8% | 306,4 |
| 8 | 8.603,6 | 5,3% | 12,6% | 809,6 | 172,6 | 637,0 | 9,7% | 297,6 |
| 9 | 9.061,0 | 5,3% | 12,6% | 859,0 | 180,9 | 678,1 | 9,5% | 289,2 |
| 10 | 9.540,3 | 5,3% | 12,6% | 911,1 | 190,4 | 720,7 | 9,4% | 281,0 |
| Terminal | 10.045,0 | 5,3% | 12,6% | 959,3 | 422,9 | 536,4 | 9,4% | — |

**Conservadora · Deflación de horas por IA** — probabilidad 30%; valor terminal 6.870,8 (VP 2.679,2); DCF US$114,53 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5.706,7 | 1,6% | 11,1% | 462,3 | 38,6 | 423,8 | 10,1% | 384,9 |
| 2 | 5.808,9 | 1,8% | 10,9% | 462,1 | 51,7 | 410,4 | 10,1% | 338,6 |
| 3 | 5.945,8 | 2,4% | 10,8% | 468,6 | 53,0 | 415,6 | 10,1% | 311,5 |
| 4 | 6.086,2 | 2,4% | 10,7% | 475,2 | 54,3 | 420,9 | 10,1% | 286,6 |
| 5 | 6.230,2 | 2,4% | 10,6% | 481,9 | 69,4 | 412,6 | 10,1% | 255,1 |
| 6 | 6.414,0 | 3,0% | 10,6% | 499,9 | 85,6 | 414,4 | 9,9% | 233,1 |
| 7 | 6.640,7 | 3,5% | 10,6% | 521,5 | 103,2 | 418,3 | 9,8% | 214,3 |
| 8 | 6.914,3 | 4,1% | 10,6% | 547,1 | 122,8 | 424,3 | 9,7% | 198,2 |
| 9 | 7.239,7 | 4,7% | 10,6% | 577,1 | 144,5 | 432,6 | 9,5% | 184,5 |
| 10 | 7.622,6 | 5,3% | 10,6% | 612,1 | 152,2 | 459,9 | 9,4% | 179,3 |
| Terminal | 8.025,9 | 5,3% | 10,6% | 644,5 | 363,5 | 281,0 | 9,4% | — |

**Disrupción · Deterioro de los fundamentales: Los servicios se comoditizan** — probabilidad 10%; valor terminal 3.900,8 (VP 1.521,1); DCF US$85,80 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5.456,7 | −2,8% | 11,1% | 442,1 | -62,9 | 504,9 | 10,1% | 458,7 |
| 2 | 5.290,1 | −3,1% | 10,1% | 389,8 | -22,0 | 411,9 | 10,1% | 339,8 |
| 3 | 5.231,8 | −1,1% | 9,6% | 366,4 | 8,3 | 358,1 | 10,1% | 268,4 |
| 4 | 5.253,8 | 0,4% | 9,1% | 348,7 | 19,2 | 329,5 | 10,1% | 224,3 |
| 5 | 5.304,7 | 1,0% | 8,6% | 332,7 | 19,4 | 313,3 | 10,1% | 193,7 |
| 6 | 5.356,0 | 1,0% | 8,6% | 338,4 | 19,6 | 318,9 | 9,9% | 179,4 |
| 7 | 5.407,9 | 1,0% | 8,6% | 344,3 | 19,8 | 324,5 | 9,8% | 166,3 |
| 8 | 5.460,2 | 1,0% | 8,6% | 350,2 | 19,9 | 330,3 | 9,7% | 154,3 |
| 9 | 5.513,1 | 1,0% | 8,6% | 356,3 | 20,1 | 336,1 | 9,5% | 143,4 |
| 10 | 5.566,5 | 1,0% | 8,6% | 362,4 | 20,3 | 342,0 | 9,4% | 133,4 |
| Terminal | 5.620,4 | 1,0% | 8,6% | 365,9 | 37,8 | 328,1 | 9,4% | — |

**Optimista · La IA crea demanda de ingeniería** — probabilidad 15%; valor terminal 18.436 (VP 7.189); DCF US$225,79 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 6.111 | 8,8% | 11,1% | 495 | 216 | 279 | 10,1% | 253 |
| 2 | 6.684 | 9,4% | 12,5% | 610 | 226 | 384 | 10,1% | 317 |
| 3 | 7.284 | 9,0% | 13,2% | 702 | 220 | 482 | 10,1% | 361 |
| 4 | 7.866 | 8,0% | 13,9% | 799 | 237 | 561 | 10,1% | 382 |
| 5 | 8.496 | 8,0% | 14,6% | 906 | 239 | 667 | 10,1% | 412 |
| 6 | 9.129 | 7,5% | 14,6% | 981 | 238 | 743 | 9,9% | 418 |
| 7 | 9.761 | 6,9% | 14,6% | 1.057 | 235 | 822 | 9,8% | 421 |
| 8 | 10.383 | 6,4% | 14,6% | 1.132 | 228 | 904 | 9,7% | 422 |
| 9 | 10.988 | 5,8% | 14,6% | 1.207 | 219 | 988 | 9,5% | 421 |
| 10 | 11.569 | 5,3% | 14,6% | 1.281 | 231 | 1.050 | 9,4% | 409 |
| Terminal | 12.181 | 5,3% | 14,6% | 1.348 | 594 | 754 | 9,4% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 3.133,36 | 5.114,10 | 8.247,46 | 8.891,90 | 172,32 |
| Conservadora | 2.586,19 | 2.679,19 | 5.265,38 | 5.909,82 | 114,53 |
| Disrupción | 2.261,60 | 1.521,05 | 3.782,65 | 4.427,09 | 85,80 |
| Optimista | 3.817,57 | 7.188,92 | 11.006,50 | 11.650,94 | 225,79 |

Ejemplo Base: (3.133,36 + 5.114,10 + 789 − 145) / 51,6 = US$172,32 por acción. El terminal representa 62,0% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 45% / 30% / 10% / 15% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,45 × 172,323635 + 0,30 × 114,531457 + 0,10 × 85,796267 + 0,15 × 225,793386 = US$154,353708 ≈ US$154,35. Los aportes son US$77,55 + US$34,36 + US$8,58 + US$33,87 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 154,353708 × 0,65 = US$100,329910 ≈ US$100,33. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$172,32, es el valor intrínseco principal. El DCF esperado de US$154,35 combina las cuatro tesis con sus probabilidades y se presenta como complemento. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: La IA compensa lo que quita: crecimiento moderado

**Qué plantea.** Es lo que muestra 2026: un dígito medio con Europa más fuerte.

**Traducción al modelo.** Norteamérica crece 4%, 5%, 5%, 5%, 5%; Europa crece 8%, 7%, 6%, 6%, 6%; Otros mercados crece 5%, 5%, 5%, 5%, 5%. El crecimiento anual compuesto de cinco años es 5,5%; el margen operativo objetivo es 12,6%. El ROIC terminal es 12,0%. El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 45%; DCF: US$172,32 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (crecimiento de ingresos (orgánico, sin divisas): +4,5% (2T26); margen operativo GAAP: 10,0% LTM; norteamérica (interanual): Bajo un dígito). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: Deflación de horas por IA

**Qué plantea.** Es la deflación de horas por IA, el riesgo que el mercado más teme.

**Traducción al modelo.** Norteamérica crece 0%, 1%, 2%, 2%, 2%; Europa crece 4%, 3%, 3%, 3%, 3%; Otros mercados crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 2,1%; el margen operativo objetivo es 10,6%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 30%; DCF: US$114,53 por acción.

**Cómo contrastarla.** La apoyarían: crecimiento de ingresos (orgánico, sin divisas): negativo dos trimestres; margen operativo GAAP: < 9%; norteamérica (interanual): negativo; utilización de ingenieros: en baja.


#### Disrupción · Deterioro de los fundamentales: Los servicios se comoditizan

**Qué plantea.** Es la comoditización con ingresos en caída.

**Traducción al modelo.** Norteamérica crece -5%, -4%, -2%, 0%, 1%; Europa crece 0%, -2%, 0%, 1%, 1%; Otros mercados crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es −1,1%; el margen operativo objetivo es 8,6%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 0,97%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 10%; DCF: US$85,80 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: crecimiento de ingresos (orgánico, sin divisas): negativo dos trimestres; margen operativo GAAP: < 9%; norteamérica (interanual): negativo; utilización de ingenieros: en baja.


#### Optimista: La IA crea demanda de ingeniería

**Qué plantea.** Supone que la IA dispara proyectos de datos y modernización.

**Traducción al modelo.** Norteamérica crece 8%, 9%, 9%, 8%, 8%; Europa crece 10%, 10%, 9%, 8%, 8%; Otros mercados crece 8%, 8%, 8%, 8%, 8%. El crecimiento anual compuesto de cinco años es 8,6%; el margen operativo objetivo es 14,6%. El ROIC terminal es 12,0%. El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 15%; DCF: US$225,79 por acción.

**Cómo contrastarla.** La confirmarían: crecimiento de ingresos (orgánico, sin divisas): ≥ +6%; margen operativo GAAP: ≥ 11%; norteamérica (interanual): ≥ +5%; utilización de ingenieros: en alza.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 5,29%; Disrupción: 0,97%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 0,98) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **Base · La IA compensa lo que quita: crecimiento moderado** | 45% | Norteamérica: 4%, 5%, 5%, 5%, 5%; Europa: 8%, 7%, 6%, 6%, 6%; Otros mercados: 5%, 5%, 5%, 5%, 5% | 5,5% | 12,6% | 2,6 | 12,0% | 5,29% | US$172,32 |
| **Conservadora · Deflación de horas por IA** | 30% | Norteamérica: 0%, 1%, 2%, 2%, 2%; Europa: 4%, 3%, 3%, 3%, 3%; Otros mercados: 0%, 0%, 0%, 0%, 0% | 2,1% | 10,6% | 2,6 | = costo de capital | 5,29% | US$114,53 |
| **Disrupción · Deterioro de los fundamentales: Los servicios se comoditizan** | 10% | Norteamérica: -5%, -4%, -2%, 0%, 1%; Europa: 0%, -2%, 0%, 1%, 1%; Otros mercados: 0%, 0%, 0%, 0%, 0% | −1,1% | 8,6% | 2,6 | = costo de capital | 0,97% | US$85,80 |
| **Optimista · La IA crea demanda de ingeniería** | 15% | Norteamérica: 8%, 9%, 9%, 8%, 8%; Europa: 10%, 10%, 9%, 8%, 8%; Otros mercados: 8%, 8%, 8%, 8%, 8% | 8,6% | 14,6% | 2,6 | 12,0% | 5,29% | US$225,79 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  |  | **US$154,35** |

Base (45%) es lo que muestra 2026: un dígito medio con Europa más fuerte. Conservadora (30%) es la deflación de horas por IA, el riesgo que el mercado más teme. Disrupción (10%) es la comoditización con ingresos en caída. Optimista (15%) supone que la IA dispara proyectos de datos y modernización. En las historias de erosión (Conservadora y Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 0,98; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.

| Crecimiento \ Margen | 9,1% | 11,1% | 13,1% | 15,1% | 17,1% |
|---|---:|---:|---:|---:|---:|
| 1,5% | 111,68 | 131,57 | 151,47 | 171,36 | 191,25 |
| 3,5% | 119,39 | 141,92 | 164,44 | 186,96 | 209,49 |
| 5,5% | 127,89 | 153,36 | 178,82 | 204,28 | 229,74 |
| 7,5% | 137,26 | 166,00 | 194,74 | 223,48 | 252,22 |
| 9,5% | 147,58 | 179,97 | 212,36 | 244,74 | 277,13 |


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
| Beta 0,98 | −0,7% (88% de las empresas) | −3,9% (95% de las empresas) | −7,2% (97% de las empresas) |
| Beta 0,98 | −0,7% (88% de las empresas) | −3,9% (95% de las empresas) | −7,2% (97% de las empresas) |

Frente al DCF Base (US$172,32), el valor intrínseco principal, el precio está por debajo en 37%.

Frente al DCF esperado de las historias (US$154,35), el complemento, el precio está por debajo en 30%. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Ingeniería de software de alta calidad frente a la deflación de horas por IA |  |
| Probabilidades | Base 45% / Conservadora 30% / Disrupción 10% / Optimista 15% |  |
| DCF Base hoy (valor intrínseco principal) | US$172,32 |  |
| DCF esperado por probabilidades (complemento) | US$154,35 |  |
| Precio con MOS sobre el DCF esperado | US$100,33 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$85,80 a US$225,79 |  |
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
