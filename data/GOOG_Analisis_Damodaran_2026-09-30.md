---
schema: "jmr-analisis-damodaran-v1"
ticker: "GOOG"
analysis_date: "2026-09-30"
---

# Alphabet Inc. (GOOG) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$322,31 por acción** (Base · Search resiste y Cloud es el segundo motor).

**Complemento · DCF esperado por probabilidades: US$274,11.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$131,60–424,32. El MOS 35% se aplica al esperado: US$178,17. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), balance del último 10-q, capital invertido operativo, deuda de balance sin arrendamientos operativos, eps básico, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet, roic terminal (criterio damodaran) (32 celdas, con respaldo). DCF esperado US$251,35 → US$274,11. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (bloque Base de 'Valuation output': US$322,31 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja calcula estos cuatro DCF en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

Alphabet tiene dos negocios distintos bajo un mismo techo. Google Services (Búsqueda, YouTube, Android, suscripciones) es una máquina publicitaria madura y enormemente rentable que genera ~80% de los ingresos. Google Cloud (infraestructura, Vertex AI, TPUs, Workspace) es el nuevo motor: creció 82% en el 2T26, hasta US$24.800 millones en el trimestre, empujado por la demanda de cómputo para IA. En medio está la pregunta de la década: ¿la IA conversacional (Gemini, AI Overviews, agentes) refuerza a la Búsqueda o la canibaliza? Y alrededor, el costo: el capex pasó de US$32.000 millones (2023) a US$91.000 millones (2025), el flujo libre se desplomó y dos juicios antimonopolio (búsqueda y ad tech) siguen en apelación.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Google Services crece ~7-10% anual cinco años | Sí | Sí: +15% en el 2T26 (Search +17%) pese a la IA conversacional | Probable a corto plazo; incierto después |
| Google Cloud sigue creciendo más de 20% anual por años | Sí | Sí: +82% en el 2T26 y ganando participación frente a AWS y Azure | Probable, desacelerando |
| El capex de IA rinde por encima del costo de capital | Sí | Sí en Cloud (demanda visible); incierto en consumo | Incierto |
| Los remedios antimonopolio rompen el negocio de Search | Sí | Poco: los remedios del tribunal de distrito fueron limitados | Baja-media |


### Visión externa: tasas base

Con ventas LTM de US$445.866 millones (US$315.475 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **>$50,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 1,0% y una mediana de 1,5% (desviación estándar 8,3%); sumando una inflación de 2,5%, la mediana nominal ronda 4,0%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · Search resiste y Cloud es el segundo motor | 11,7% | 13% |
| Conservadora · La IA conversacional erosiona Search | 6,6% | 33% |
| Disrupción · Deterioro de los fundamentales: Remedios antimonopolio y guerra de precios en IA | 3,7% | 53% |
| Optimista · Gemini y Cloud dominan la plataforma de IA | 16,1% | 5% |

En dólares de 2015 la empresa está en el tramo de más de US$50.000 millones: crecer 11,7% anual cinco años (Base) lo logró ~13% de las empresas de ese tamaño; 16,1% (Optimista), ~5%. Alphabet es una excepción probada (creció 14-15% en 2024-2025 y 24% en el 2T26 con ~US$450.000 millones de ventas), pero la visión externa recuerda lo raro que es sostenerlo cinco años más.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: una máquina madura y un segundo motor.** Alphabet son dos negocios. Google Services (Búsqueda, YouTube, Android) genera ~80% de los ingresos y es una máquina publicitaria madura; Google Cloud creció 82% en el 2T26 (US$24.800 millones en el trimestre) por la demanda de cómputo para IA. La Base les da trayectorias distintas: Services de 10% bajando a 6%, Cloud de 45% bajando a 15%. El total es 16,3% el primer año y 11,7% compuesto. Es una cifra exigente para una empresa de ~US$450.000 millones de ventas —solo ~13% de las empresas de ese tamaño lo lograron—, pero Alphabet es una excepción probada: creció 14-15% en 2024-2025 y 24% en el 2T26. Antes de la revisión del 30-sep-2026 la hoja suponía mucho menos (11% y 7%), por debajo del ritmo real. La Conservadora (6,6%) es la Búsqueda erosionada por la IA conversacional; la Disrupción (3,7%), remedios antimonopolio y una guerra de precios en IA; la Optimista (16,1%), Alphabet como plataforma dominante de IA. Si Search crece 3% o menos, la Base deja de sostenerse.

**Margen: escala de Cloud contra depreciación de la IA.** El margen operativo subió de 27,4% (2023) a ~33% y fue 34% en el 2T26, con Cloud ya rentable. La Base usa 34,3%. Se cruzan dos fuerzas: la escala de Cloud sube el margen, y la depreciación del capex de IA y el costo de servir respuestas generativas en la Búsqueda lo bajan. La Base supone que se compensan con una mejora leve; el rango de las historias va de 27,3% (remedios y guerra de precios) a 37,3%. Dos puntos de margen mueven la Base a US$304,54 (−6%) o US$340,09 (+6%).

**Reinversión: el supuesto que más cambió.** El capex se triplicó en dos años (US$91.447 millones en 2025) y el flujo libre cayó de US$71.236 millones a US$14.612 millones; para 2026 la guía es de US$195-205 mil millones. Por eso la hoja pasó a un ventas/capital de 1,15× en los años 1–5 y 1,43× después: cada dólar de ventas nuevas exige ~US$0,87 de capital, el triple que antes. La versión anterior (2,5 y 2) suponía una reinversión que era una fracción del gasto real. La Optimista usa 0,97× porque crecer tanto en Cloud exige aún más centros de datos. Todo depende de que ese capital rinda por encima del costo de capital; la demanda de Cloud (+82%) es la mejor evidencia a favor, y un capex que sube sin que aceleren los ingresos sería la señal en contra. Después del año 10 la Base conserva un ROIC de 29,3%, el promedio de la industria: escala y efectos de red en búsqueda, YouTube y Android sostuvieron un ROIC de 24-31% durante años. Si esa ventaja se perdiera, la Base caería a US$220,50 (−32%).

**Descuento.** La beta de la hoja es 1,07. La bottom-up de Software (Internet) da 1,62, pero ese grupo son 29 empresas pequeñas y volátiles que no representan a Alphabet; ponderando publicidad (~82% de ingresos) y software sale ~1,07, la que usa la hoja. El riesgo de Alphabet está en los flujos —IA y regulación—, no en la tasa. El costo de capital va de 9,65% a 9,00%. El crecimiento perpetuo es 4,99% y el terminal explica 72,6% del valor operativo; un punto más de tasa lleva la Base a US$258,89 (−20%).

**Probabilidades y lectura del resultado.** La Base pesa 40%, la Conservadora 25%, la Disrupción 15% y la Optimista 20%. El DCF Base es US$322,31, cerca del precio (US$340,35); el esperado, US$274,11, es menor porque la Conservadora y la Disrupción suman 40% y en ambas la ventaja se pierde. La evidencia en contra de la Base es el capex: crece más rápido que los ingresos y el flujo libre cayó ~80% en 2025. Si la demanda de IA se enfría, la Base se sostiene en ingresos pero no en retorno sobre el capital. Los dos juicios antimonopolio siguen en apelación. Las acciones se fijan en 12.230,0 millones; las recompras no se modelan. En 2026 Alphabet emitió US$19.063 millones en acciones preferentes convertibles (6,25%; 19 millones a US$1.000 de liquidación, según el 10-Q del 2T26): se restan del patrimonio como un derecho separado de US$19.000 millones, sin sumarlas a las acciones. Es un tratamiento provisional hasta modelar la conversión de 2029 y los capped calls.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$445.866 millones. Con el crecimiento de la Base llegan a US$774.191 millones en el año 5 y a US$1.061.580 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 32,8% en el año 1 a 34,3% al final, y se descuentan impuestos (18,4% al principio y 16,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$138.694 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$58.317 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$80.378 millones el primer año. Cada flujo se trae a hoy con el costo de capital (9,65% al principio, 9,00% al final): los diez años suman US$1.012.708 millones. Después del año 10 se supone que la empresa crece 4,99% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 29,3%; esa perpetuidad vale hoy US$2.689.318 millones, 73% del total. Flujos más terminal dan el valor de las operaciones, US$3.702.026 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$242.474 millones, más activos no operativos por US$131.461 millones, menos deuda por US$115.088 millones (incluye los arrendamientos capitalizados), menos acciones preferentes por US$19.000 millones. Queda un patrimonio de US$3.941.872 millones que, repartido entre 12.230,0 millones de acciones, da US$322,31 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 17,90× (peso 33% dentro de los múltiplos); EV/FCFF 36,63× (peso 17% dentro de los múltiplos); P/E 26,77× (peso 33% dentro de los múltiplos); P/FCFE 34,67× (peso 8% dentro de los múltiplos); P/OCF 19,53× (peso 8% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (9,8%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$322,31; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$304,54 | −5,5% |
| Margen objetivo +2 pp | US$340,09 | +5,5% |
| Crecimiento años 1–5 −2 pp | US$292,45 | −9,3% |
| Crecimiento años 1–5 +2 pp | US$355,45 | +10,3% |
| Ventas/capital −20% | US$316,04 | −1,9% |
| Ventas/capital +20% | US$326,49 | +1,3% |
| WACC +1 pp | US$258,89 | −19,7% |
| WACC −1 pp | US$428,09 | +32,8% |
| Crecimiento terminal −0,5 pp | US$298,44 | −7,4% |
| Crecimiento terminal +0,5 pp | US$352,93 | +9,5% |
| ROIC terminal = costo de capital | US$220,50 | −31,6% |
| Acciones +5% | US$306,96 | −4,8% |


### Piezas del valor

**Crecimiento.** Ingresos de US$307.394 millones (2023, +8,7%), US$350.018 millones (2024, +13,9%) y US$402.836 millones (2025, +15,1%); LTM US$445.866 millones. En el 2T26 los ingresos crecieron 24% (US$119.800 millones): Google Services +15% (US$94.500 millones; Search +17%, YouTube +13%) y Google Cloud +82% (US$24.800 millones). Tras la revisión del 30-sep-2026, la hoja supone 18% el próximo año y 11% en los años 2-5 (antes 11% y 7%, muy por debajo del ritmo actual). La división LTM de las historias (Services ~US$364.000 millones, Cloud ~US$80.000 millones) es una estimación propia.

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 307.394 | 350.018 | 402.836 | 445.866 |
| Crecimiento | +8,7% | +13,9% | +15,1% | — |
| Margen operativo | 27,4% | 32,1% | 32,0% | 33,1% |
| Capex | 32.251 | 52.535 | 91.447 | — |
| FCFF (hoja) | 59.212 | 71.236 | 14.612 | — |

**Márgenes.** El margen operativo subió de 27,4% (2023) a ~33% y fue 34% en el 2T26, con Cloud ya rentable. La hoja supone 32,5% el próximo año y 35% de objetivo (antes 33,5%). Dos fuerzas se cruzan: la escala de Cloud sube el margen, y la depreciación del capex de IA y el costo de servir respuestas generativas en Search lo bajan. Las historias van de 27% (remedios y guerra de precios) a 37% (plataforma de IA dominante).

**Reinversión y retorno.** Esta es la pieza que más cambió. El capex se triplicó en dos años (US$91.447 millones en 2025) y el FCFF cayó de US$71.236 millones a US$14.612 millones. Con un capex 2026 de US$195-205 mil millones, la hoja pasó a un sales-to-capital de 1,2 (años 1-5) y 1,5 (años 6-10), antes 2,5 y 2: la reinversión anterior (~US$14.000 millones al año) era una fracción del gasto real. En la historia Optimista se baja a 1,0 porque crecer tanto en Cloud exige aún más centros de datos. El valor depende de que ese capital rinda por encima del costo de capital: la demanda de Cloud (+82%) es la mejor evidencia a favor. Ventaja durable: escala y efectos de red en búsqueda, YouTube y Android, con ROIC estable de 24-31% y la Búsqueda todavía creciendo. El ROIC después del año 10 es 29,3%, el promedio de su industria según Damodaran (29,3%), limitado a su ROIC actual. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$14.924 millones, compromisos del 10-K al 2025-12-31) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$1.213 millones, +0,27 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,03 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usa ahora una beta de 1,07 (antes 1,05). La bottom-up de Software (Internet) da 1,61, pero ese grupo (29 empresas pequeñas y volátiles) no representa a Alphabet. Ponderando por ingresos Advertising (1,01, ~82%) y Software System & Application (1,25, ~18%) y reapalancando con la poca deuda sale 1,07, la que ahora usa la hoja: el riesgo de Alphabet está en los flujos (IA, regulación), no en la tasa.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,07 | 9,8% | 9,7% | US$363,77 |
| Bottom-up del sector (Software (Internet), reapalancada) | 1,62 | 12,2% | 12,1% | US$318,28 |
| Propuesta (sector ajustado por riesgo propio) | 1,07 | 9,8% | 9,7% | US$363,77 |


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 31,8% | 29,3% | 9,0% | 29,3% | US$322,31 | US$243,84 |

Fuentes de ventaja: Escala y efectos de red en búsqueda, YouTube y Android; datos. Evidencia: ROIC 24-31% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$322,31 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$274,11. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$445.866 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 364.000 + 80.000 + 1.866 = 445.866. |
| Margen inicial del DCF | 32,8% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 18,40% en años 1–5; 16,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 9,65% → 9,00% | Tasa libre de riesgo 4,99%, beta 1,07, ERP 4,46%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 1,15x en años 1–5; 1,43x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. Optimista usa 0,97x en años 1–5. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 4,99%; Disrupción: 2,83% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (2,83%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Optimista: 29,30%; Conservadora/Disrupción: 9,00% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 242.474; deuda 115.088; activos no operativos 131.461; acciones preferentes 19.000; acciones 12.230,0 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 364.000 × 1,10 + 80.000 × 1,45 + 1.866 × 1,20 = US$518.639,20 millones. Frente a 445.866, el crecimiento consolidado es 16,32%. En los años 2–5 es 12,97%, 10,92%, 9,47%, 8,82%; las ventas del año 5 son US$774.190,87 millones. El 11,7% de la tabla es el crecimiento anual compuesto de los cinco años: (774.190,87 / 445.866)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 518.639,20 × 32,77% × (1 − 18,40%) = US$138.694,25 millones. La reinversión es US$58.316,58 millones y el FCFF es US$80.377,66 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,00%. Reinversión terminal sobre el NOPAT: Base, 17,0% (4,99% / 29,30%); Conservadora, 55,4% (4,99% / 9,00%); Disrupción, 31,5% (2,83% / 9,00%); Optimista, 17,0% (4,99% / 29,30%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · Search resiste y Cloud es el segundo motor** — probabilidad 40%; valor terminal 6.638.847 (VP 2.689.318); DCF US$322,31 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 518.639 | 16,3% | 32,8% | 138.694 | 58.317 | 80.378 | 9,7% | 73.301 |
| 2 | 585.919 | 13,0% | 33,4% | 159.555 | 55.460 | 104.095 | 9,7% | 86.573 |
| 3 | 649.903 | 10,9% | 33,7% | 178.570 | 53.326 | 125.243 | 9,7% | 94.991 |
| 4 | 711.425 | 9,5% | 34,0% | 197.216 | 54.404 | 142.812 | 9,7% | 98.780 |
| 5 | 774.191 | 8,8% | 34,3% | 216.510 | 54.060 | 162.450 | 9,7% | 102.471 |
| 6 | 836.560 | 8,1% | 34,3% | 235.328 | 42.695 | 192.634 | 9,5% | 110.945 |
| 7 | 897.541 | 7,3% | 34,3% | 253.959 | 40.990 | 212.969 | 9,4% | 112.126 |
| 8 | 956.087 | 6,5% | 34,3% | 272.098 | 38.533 | 233.564 | 9,3% | 112.546 |
| 9 | 1.011.124 | 5,8% | 34,3% | 289.424 | 35.325 | 254.099 | 9,1% | 112.196 |
| 10 | 1.061.580 | 5,0% | 34,3% | 305.613 | 37.088 | 268.525 | 9,0% | 108.776 |
| Terminal | 1.114.552 | 5,0% | 34,3% | 320.863 | 54.645 | 266.218 | 9,0% | — |

**Conservadora · La IA conversacional erosiona Search** — probabilidad 25%; valor terminal 2.299.432 (VP 931.473); DCF US$162,33 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 495.893 | 11,2% | 32,8% | 132.611 | 30.806 | 101.806 | 9,7% | 92.843 |
| 2 | 531.433 | 7,2% | 31,8% | 137.779 | 25.358 | 112.421 | 9,7% | 93.498 |
| 3 | 560.689 | 5,5% | 31,3% | 143.076 | 24.465 | 118.612 | 9,7% | 89.961 |
| 4 | 588.914 | 5,0% | 30,8% | 147.876 | 22.375 | 125.501 | 9,7% | 86.807 |
| 5 | 614.728 | 4,4% | 30,3% | 151.850 | 24.002 | 127.848 | 9,7% | 80.645 |
| 6 | 642.419 | 4,5% | 30,3% | 159.624 | 20.807 | 138.817 | 9,5% | 79.950 |
| 7 | 672.137 | 4,6% | 30,3% | 167.984 | 22.340 | 145.644 | 9,4% | 76.680 |
| 8 | 704.045 | 4,7% | 30,3% | 176.982 | 23.999 | 152.983 | 9,3% | 73.717 |
| 9 | 738.323 | 4,9% | 30,3% | 186.672 | 25.795 | 160.877 | 9,1% | 71.035 |
| 10 | 775.165 | 5,0% | 30,3% | 197.113 | 27.082 | 170.031 | 9,0% | 68.878 |
| Terminal | 813.846 | 5,0% | 30,3% | 206.949 | 114.742 | 92.207 | 9,0% | — |

**Disrupción · Deterioro de los fundamentales: Remedios antimonopolio y guerra de precios en IA** — probabilidad 15%; valor terminal 1.612.009 (VP 653.006); DCF US$131,60 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 480.426 | 7,8% | 32,8% | 128.475 | 16.283 | 112.192 | 9,7% | 102.315 |
| 2 | 499.212 | 3,9% | 30,6% | 124.537 | 9.968 | 114.569 | 9,7% | 95.284 |
| 3 | 510.712 | 2,3% | 29,5% | 122.822 | 8.772 | 114.050 | 9,7% | 86.502 |
| 4 | 520.832 | 2,0% | 28,4% | 120.581 | 12.788 | 107.793 | 9,7% | 74.558 |
| 5 | 535.585 | 2,8% | 27,3% | 119.189 | 13.150 | 106.039 | 9,7% | 66.888 |
| 6 | 550.756 | 2,8% | 27,3% | 123.286 | 10.923 | 112.363 | 9,5% | 64.715 |
| 7 | 566.356 | 2,8% | 27,3% | 127.520 | 11.232 | 116.288 | 9,4% | 61.224 |
| 8 | 582.399 | 2,8% | 27,3% | 131.894 | 11.550 | 120.344 | 9,3% | 57.989 |
| 9 | 598.896 | 2,8% | 27,3% | 136.414 | 11.877 | 124.537 | 9,1% | 54.989 |
| 10 | 615.860 | 2,8% | 27,3% | 141.084 | 12.214 | 128.871 | 9,0% | 52.204 |
| Terminal | 633.305 | 2,8% | 27,3% | 145.081 | 45.662 | 99.419 | 9,0% | — |

**Optimista · Gemini y Cloud dominan la plataforma de IA** — probabilidad 20%; valor terminal 9.348.791 (VP 3.787.084); DCF US$424,32 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 537.932 | 20,6% | 32,8% | 143.854 | 99.100 | 44.754 | 9,7% | 40.814 |
| 2 | 633.823 | 17,8% | 34,6% | 178.806 | 102.520 | 76.286 | 9,7% | 63.445 |
| 3 | 733.022 | 15,7% | 35,5% | 212.174 | 107.138 | 105.036 | 9,7% | 79.665 |
| 4 | 836.690 | 14,1% | 36,4% | 248.326 | 106.532 | 141.795 | 9,7% | 98.077 |
| 5 | 939.771 | 12,3% | 37,3% | 285.822 | 105.418 | 180.404 | 9,7% | 113.796 |
| 6 | 1.041.775 | 10,9% | 37,3% | 318.709 | 68.475 | 250.234 | 9,5% | 144.120 |
| 7 | 1.139.577 | 9,4% | 37,3% | 350.668 | 63.206 | 287.462 | 9,4% | 151.346 |
| 8 | 1.229.855 | 7,9% | 37,3% | 380.649 | 55.590 | 325.058 | 9,3% | 156.633 |
| 9 | 1.309.255 | 6,5% | 37,3% | 407.566 | 45.741 | 361.825 | 9,1% | 159.762 |
| 10 | 1.374.587 | 5,0% | 37,3% | 430.363 | 48.023 | 382.339 | 9,0% | 154.881 |
| Terminal | 1.443.178 | 5,0% | 37,3% | 451.838 | 76.951 | 374.887 | 9,0% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 1.012.707,57 | 2.689.318,34 | 3.702.025,90 | 3.941.872,48 | 322,31 |
| Conservadora | 814.013,39 | 931.472,60 | 1.745.486,00 | 1.985.332,57 | 162,33 |
| Disrupción | 716.668,60 | 653.005,56 | 1.369.674,16 | 1.609.520,74 | 131,60 |
| Optimista | 1.162.539,85 | 3.787.084,40 | 4.949.624,24 | 5.189.470,82 | 424,32 |

Ejemplo Base: (1.012.707,57 + 2.689.318,34 + 242.474 + 131.461 − 115.088 − 19.000) / 12.230,0 = US$322,31 por acción. El terminal representa 72,6% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 40% / 25% / 15% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,40 × 322,311732 + 0,25 × 162,332998 + 0,15 × 131,604312 + 0,20 × 424,323043 = US$274,113198 ≈ US$274,11. Los aportes son US$128,92 + US$40,58 + US$19,74 + US$84,86 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 274,113198 × 0,65 = US$178,173579 ≈ US$178,17. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$322,31, es el valor intrínseco principal. El DCF esperado de US$274,11 combina las cuatro tesis con sus probabilidades y se presenta como complemento. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: Search resiste y Cloud es el segundo motor

**Qué plantea.** Es lo que muestra 2026: Search sigue creciendo y Cloud se vuelve un segundo motor que desacelera con la escala.

**Traducción al modelo.** Google Services crece 10%, 8%, 7%, 6%, 6%; Google Cloud crece 45%, 30%, 22%, 18%, 15%; Other Bets crece 20%, 20%, 20%, 20%, 20%. El crecimiento anual compuesto de cinco años es 11,7%; el margen operativo objetivo es 34,3%. El ROIC terminal es 29,3%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 40%; DCF: US$322,31 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (search & other (interanual): +17% (2T26); google Cloud (interanual): +82% (2T26); margen operativo de Cloud: En alza). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: La IA conversacional erosiona Search

**Qué plantea.** Es la erosión de la Búsqueda por la IA conversacional (competencia de OpenAI, cambios en el comportamiento).

**Traducción al modelo.** Google Services crece 6%, 3%, 2%, 2%, 2%; Google Cloud crece 35%, 22%, 16%, 13%, 10%; Other Bets crece 10%, 10%, 10%, 10%, 10%. El crecimiento anual compuesto de cinco años es 6,6%; el margen operativo objetivo es 30,3%. El ROIC terminal es el costo de capital (9,00%). El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 25%; DCF: US$162,33 por acción.

**Cómo contrastarla.** La apoyarían: search & other (interanual): ≤ +3%; google Cloud (interanual): ≤ +20%; margen operativo de Cloud: cae con el capex; capex / ingresos: sube sin aceleración de ingresos.


#### Disrupción · Deterioro de los fundamentales: Remedios antimonopolio y guerra de precios en IA

**Qué plantea.** Combina remedios antimonopolio más duros y una guerra de precios en IA que baja márgenes.

**Traducción al modelo.** Google Services crece 4%, 1%, 0%, 0%, 1%; Google Cloud crece 25%, 15%, 10%, 8%, 8%; Other Bets crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 3,7%; el margen operativo objetivo es 27,3%. El ROIC terminal es el costo de capital (9,00%). El crecimiento terminal es 2,83%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 15%; DCF: US$131,60 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: search & other (interanual): ≤ +3%; google Cloud (interanual): ≤ +20%; margen operativo de Cloud: cae con el capex; capex / ingresos: sube sin aceleración de ingresos.


#### Optimista: Gemini y Cloud dominan la plataforma de IA

**Qué plantea.** Es Alphabet como plataforma dominante de IA (modelos, chips y nube).

**Traducción al modelo.** Google Services crece 13%, 11%, 10%, 9%, 8%; Google Cloud crece 55%, 40%, 30%, 25%, 20%; Other Bets crece 40%, 40%, 40%, 40%, 40%. El crecimiento anual compuesto de cinco años es 16,1%; el margen operativo objetivo es 37,3%. El ROIC terminal es 29,3%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 20%; DCF: US$424,32 por acción.

**Cómo contrastarla.** La confirmarían: search & other (interanual): ≥ +8%; google Cloud (interanual): ≥ +30% en 2027; margen operativo de Cloud: ≥ 25%; capex / ingresos: baja a ≤ 20% con ingresos creciendo.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 4,99%; Disrupción: 2,83%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,07) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **Base · Search resiste y Cloud es el segundo motor** | 40% | Google Services: 10%, 8%, 7%, 6%, 6%; Google Cloud: 45%, 30%, 22%, 18%, 15%; Other Bets: 20%, 20%, 20%, 20%, 20% | 11,7% | 34,3% | 1,2 | 29,3% | 4,99% | US$322,31 |
| **Conservadora · La IA conversacional erosiona Search** | 25% | Google Services: 6%, 3%, 2%, 2%, 2%; Google Cloud: 35%, 22%, 16%, 13%, 10%; Other Bets: 10%, 10%, 10%, 10%, 10% | 6,6% | 30,3% | 1,2 | = costo de capital | 4,99% | US$162,33 |
| **Disrupción · Deterioro de los fundamentales: Remedios antimonopolio y guerra de precios en IA** | 15% | Google Services: 4%, 1%, 0%, 0%, 1%; Google Cloud: 25%, 15%, 10%, 8%, 8%; Other Bets: 0%, 0%, 0%, 0%, 0% | 3,7% | 27,3% | 1,2 | = costo de capital | 2,83% | US$131,60 |
| **Optimista · Gemini y Cloud dominan la plataforma de IA** | 20% | Google Services: 13%, 11%, 10%, 9%, 8%; Google Cloud: 55%, 40%, 30%, 25%, 20%; Other Bets: 40%, 40%, 40%, 40%, 40% | 16,1% | 37,3% | 1,0 | 29,3% | 4,99% | US$424,32 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  |  | **US$274,11** |

Base (40%) es lo que muestra 2026: Search sigue creciendo y Cloud se vuelve un segundo motor que desacelera con la escala. Conservadora (25%) es la erosión de la Búsqueda por la IA conversacional (competencia de OpenAI, cambios en el comportamiento). Disrupción (15%) combina remedios antimonopolio más duros y una guerra de precios en IA que baja márgenes. Optimista (20%) es Alphabet como plataforma dominante de IA (modelos, chips y nube). En las historias de erosión (Conservadora y Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 1,07; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.

| Crecimiento \ Margen | 31,3% | 33,3% | 35,3% | 37,3% | 39,3% |
|---|---:|---:|---:|---:|---:|
| 7,7% | 251,07 | 265,66 | 280,26 | 294,85 | 309,44 |
| 9,7% | 276,32 | 292,81 | 309,30 | 325,78 | 342,27 |
| 11,7% | 304,37 | 322,96 | 341,56 | 360,15 | 378,74 |
| 13,7% | 335,48 | 356,41 | 377,35 | 398,28 | 419,22 |
| 15,7% | 369,94 | 393,47 | 417,01 | 440,54 | 464,08 |


### Pre-mortem

1. Las respuestas generativas reducen los clics y el precio por consulta: Search deja de crecer aunque las búsquedas suban.
2. El capex de IA sobreinvierte: hay exceso de capacidad, precios de cómputo en caída y deterioro de activos.
3. Las apelaciones terminan en remedios más duros (fin de acuerdos por defecto con Apple, venta del ad exchange).
4. OpenAI, Anthropic, Meta o Microsoft capturan a los usuarios de asistentes y a los desarrolladores.
5. La desaceleración de Cloud llega antes: los clientes de IA construyen su propia infraestructura.

**Evidencia en contra de la historia más probable:** el capex crece más rápido que los ingresos y el flujo libre cayó ~80% en 2025. Si la demanda de IA se enfría, la historia Base se sostiene en ingresos pero no en retorno sobre el capital.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Search & other (interanual) | +17% (2T26) | ≥ +8% | ≤ +3% |
| Google Cloud (interanual) | +82% (2T26) | ≥ +30% en 2027 | ≤ +20% |
| Margen operativo de Cloud | En alza | ≥ 25% | Cae con el capex |
| Capex / ingresos | ~23% (2025) | Baja a ≤ 20% con ingresos creciendo | Sube sin aceleración de ingresos |
| Remedios antimonopolio (búsqueda y ad tech) | En apelación | Remedios conductuales | Desinversiones o fin de acuerdos por defecto |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$340,35**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 30% | Margen 34% | Margen 37% |
|---|---:|---:|---:|
| Beta 1,07 | 14,7% (7% de las empresas) | 12,5% (10% de las empresas) | 10,6% (17% de las empresas) |

Frente al DCF Base (US$322,31), el valor intrínseco principal, el precio está por encima en 6%.

Frente al DCF esperado de las historias (US$274,11), el complemento, el precio está por encima en 24%. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Máquina publicitaria madura con un segundo motor de IA en la nube, financiado con capex récord |  |
| Probabilidades | Base 40% / Conservadora 25% / Disrupción 15% / Optimista 20% |  |
| DCF Base hoy (valor intrínseco principal) | US$322,31 |  |
| DCF esperado por probabilidades (complemento) | US$274,11 |  |
| Precio con MOS sobre el DCF esperado | US$178,17 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$131,60 a US$424,32 |  |
| Confianza | Media: el negocio es excepcional; el retorno del capex de IA y el futuro de Search son inciertos |  |
| Qué cambiaría la opinión | Crecimiento de Search y de Cloud; retorno del capex; remedios antimonopolio |  |
| Revisión | Resultados del 3T26 (oct-2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [Alphabet, resultados del 2T 2026 (Form 8-K, ex. 99.1)](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm)
- [Alphabet, proxy statement 2026 (DEF 14A)](https://www.sec.gov/Archives/edgar/data/0001652044/000130817926000342/goog-20260424.htm)
- [Synergy Research, participación en la nube de los tres grandes](https://www.srgresearch.com/articles/cloud-market-share-trends-big-three-together-hold-63-while-oracle-and-the-neoclouds-inch-higher)
- [Tech Insider, Google Cloud +82% frente a AWS (2026)](https://tech-insider.org/google-cloud-82-percent-growth-aws-earnings-2026/)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
