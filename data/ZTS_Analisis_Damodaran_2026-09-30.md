---
schema: "jmr-analisis-damodaran-v1"
ticker: "ZTS"
analysis_date: "2026-09-30"
---

# Zoetis Inc. (ZTS) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$114,23 por acción** (Base · Tropiezo temporal; vuelve a crecer con innovación).

**Complemento · DCF esperado por probabilidades: US$92,09.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$44,80–132,05. El MOS 35% se aplica al esperado: US$59,86. El antiguo caso técnico de la hoja (US$114,13) se conserva solo como calibración; no es el DCF Base. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), balance del último 10-q, capital invertido operativo, deuda de balance sin arrendamientos operativos, eps básico, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet (28 celdas, con respaldo). DCF esperado US$95,15 → US$91,98. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de US$114,13 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

Zoetis es la mayor empresa de salud animal del mundo: medicamentos, vacunas y diagnósticos para mascotas (~2/3 de las ventas) y animales de producción. Durante una década fue un compuesto casi perfecto: crecimiento de un dígito alto, margen operativo de ~37% y franquicias crónicas (dermatología con Apoquel y Cytopoint, dolor con Librela y Solensia, parasiticidas con Simparica) que se renuevan cada mes. En 2026 varias franquicias se debilitaron a la vez: en el 2T las ventas cayeron 0,2% y mascotas en EE.UU. 11%, por demanda más débil, competencia en dermatología y parasiticidas, genéricos de Cerenia y Convenia y menores ventas de Librela. Mientras tanto, la empresa se endeudó para recomprar acciones. La historia de cinco años es si este es un tropiezo temporal de un líder o el fin de su poder de precio en mascotas.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Las ventas vuelven a crecer ~5% anual desde 2027 | Sí | Sí: la salud animal crece a un dígito medio y Zoetis tiene cartera nueva | Media |
| El margen operativo se mantiene en ~36% | Sí | Sí: 36-38% en 2023-2025 incluso con ventas planas | Probable |
| Las franquicias de dermatología y dolor pierden participación de forma duradera | Sí | Sí: competidores nuevos y dudas sobre Librela | Media |
| El dueño de mascotas deja de pagar precios altos | Sí | Parcialmente: el 10-Q habla de sensibilidad de precio por la macro | Media-baja |


### Visión externa: tasas base

Con ventas LTM de US$9.517 millones (US$6.734 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **$4,500-7,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 5,0% y una mediana de 4,1% (desviación estándar 8,7%); sumando una inflación de 2,5%, la mediana nominal ronda 6,6%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · Tropiezo temporal; vuelve a crecer con innovación | 4,5% | 64% |
| Conservadora · Erosión prolongada de franquicias clave | 1,5% | 80% |
| Disrupción · Deterioro de los fundamentales: Genéricos y competencia generalizada | −0,7% | 87% |
| Optimista · Recuperación fuerte con nuevos productos | 6,0% | 54% |

En dólares de 2015 la empresa está en el tramo de US$4.500-7.000 millones: crecer 4,5% anual cinco años (Base) lo logró ~64% de las empresas de ese tamaño; 6,0% (Optimista), ~54%. La hoja pide algo común. El valor de Zoetis depende de sostener un margen de 36%, que es excepcional para cualquier empresa, más que del crecimiento.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: un tropiezo o el fin del poder de precio.** Zoetis es la mayor empresa de salud animal del mundo: medicamentos, vacunas y diagnósticos para mascotas (~2/3 de las ventas) y animales de producción. Durante una década fue un compuesto casi perfecto, con franquicias crónicas que se renuevan cada mes (dermatología con Apoquel y Cytopoint, dolor con Librela y Solensia, parasiticidas con Simparica). En 2026 varias franquicias se debilitaron a la vez: en el 2T26 las ventas cayeron 0,2% y mascotas en EE.UU. 11%, por demanda más débil, competencia, genéricos de Cerenia y Convenia y menores ventas de Librela. La Base es la tesis de la empresa: 2026 es transición y la cartera nueva devuelve el crecimiento (mascotas de 1% a 6%, producción 3-4%): 1,7% el primer año y 4,5% compuesto, algo común (~64% de empresas de su tamaño lo lograron). La Conservadora (1,5%) es una erosión prolongada de las franquicias; la Disrupción (−0,7%), genéricos y competencia generalizados; la Optimista (6,0%), una recuperación fuerte. La caída simultánea en varias franquicias apunta a un problema competitivo más que a un mal año; si mascotas EE.UU. sigue cayendo en el 3T y el 4T, la Conservadora gana peso.

**Margen: excepcional, y por eso frágil.** El margen operativo se mantuvo en 36-38% con ventas planas: poder de precio y costos flexibles. La Base lo mantiene (36,4%). Es un margen excepcional para cualquier empresa, y la mezcla lo hace frágil: las mascotas son el negocio más rentable, así que si la competencia obliga a bajar precios ahí, el margen cae rápido. La Conservadora usa 33,4%, la Disrupción 29,4% y la Optimista 38,4%. Dos puntos de margen mueven la Base a US$107,40 (−6%) o US$121,06 (+6%). Un margen de 33% o menos invalidaría la Base.

**Reinversión y ventaja.** Zoetis invierte US$620-730 millones al año (plantas de biológicos) y US$722 millones en I+D; la hoja usa un ventas/capital de 1,91× (~US$0,52 por dólar de ventas nuevas). En los últimos doce meses recompró US$3.644 millones y pagó US$889 millones de dividendos, con la deuda subiendo a US$9.042 millones: una apuesta de la gerencia a que el tropiezo es temporal. La ventaja —patentes que se renuevan, relación con los veterinarios, escala— sostuvo un ROIC de 26-29%, así que la Base conserva 16,9% después del año 10, el promedio de la industria (menor que el actual). Si la ventaja se perdiera, la Base valdría US$83,36 (−27%); por eso la Conservadora y la Disrupción usan el costo de capital, y explican la distancia entre la Base y el esperado.

**Descuento.** La hoja usa una beta de 1,11; la bottom-up farmacéutica reapalancada con la deuda de Zoetis da 1,11. La salud animal suele ser menos riesgosa que la farmacéutica humana (menos riesgo de ensayos y de reembolsos), así que la beta de la hoja es defendible, pero la deuda creciente apoya subirla algo: la Base queda del lado optimista en ese punto. El costo de capital va de 8,91% a 9,00%; un punto más lleva la Base a US$89,36 (−22%). El crecimiento perpetuo es 4,99% y el terminal explica 63,3% del valor operativo.

**Probabilidades y lectura del resultado.** La Base pesa 40% y la Conservadora 35%, casi lo mismo, por la caída simultánea de varias franquicias. La Disrupción pesa 10% y la Optimista 15%. El DCF Base es US$114,23 y el esperado US$92,09, frente a un precio de US$69,69: el mercado paga algo apenas por encima de la Conservadora (US$63,17), es decir, ya descuenta una erosión prolongada. Las acciones se fijan en 413,2 millones; las recompras no se modelan.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$9.517 millones. Con el crecimiento de la Base llegan a US$11.837 millones en el año 5 y a US$15.203 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 36,4% en el año 1 a 36,4% al final, y se descuentan impuestos (20,1% al principio y 20,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$2.815 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$237 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$2.578 millones el primer año. Cada flujo se trae a hoy con el costo de capital (8,91% al principio, 9,00% al final): los diez años suman US$20.113 millones. Después del año 10 se supone que la empresa crece 4,99% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 16,9%; esa perpetuidad vale hoy US$34.684 millones, 63% del total. Flujos más terminal dan el valor de las operaciones, US$54.798 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$1.676 millones, menos deuda por US$9.272 millones (incluye los arrendamientos capitalizados). Queda un patrimonio de US$47.202 millones que, repartido entre 413,2 millones de acciones, da US$114,23 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 13,54× (peso 33% dentro de los múltiplos); EV/FCFF 22,46× (peso 17% dentro de los múltiplos); P/E 21,71× (peso 33% dentro de los múltiplos); P/FCFE 20,66× (peso 8% dentro de los múltiplos); P/OCF 16,22× (peso 8% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (9,9%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$114,23; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$107,40 | −6,0% |
| Margen objetivo +2 pp | US$121,06 | +6,0% |
| Crecimiento años 1–5 −2 pp | US$100,69 | −11,9% |
| Crecimiento años 1–5 +2 pp | US$129,31 | +13,2% |
| Ventas/capital −20% | US$112,99 | −1,1% |
| Ventas/capital +20% | US$115,06 | +0,7% |
| WACC +1 pp | US$89,36 | −21,8% |
| WACC −1 pp | US$155,34 | +36,0% |
| Crecimiento terminal −0,5 pp | US$106,62 | −6,7% |
| Crecimiento terminal +0,5 pp | US$123,90 | +8,5% |
| ROIC terminal = costo de capital | US$83,36 | −27,0% |
| Acciones +5% | US$108,79 | −4,8% |


### Piezas del valor

**Crecimiento.** Ingresos de US$8.544 millones (2023, +5,7%), US$9.256 millones (2024, +8,3%) y US$9.467 millones (2025, +2,3%); LTM US$9.517 millones. En el 2T26 las ventas cayeron 0,2% y mascotas en EE.UU. 11%. La hoja supone 2% el próximo año y 5% en los años 2-5. La división de las historias (compañía ~2/3, producción ~1/3) es una aproximación.

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 8.544 | 9.256 | 9.467 | 9.517 |
| Crecimiento | +5,7% | +8,3% | +2,3% | — |
| Margen operativo | 37,2% | 36,3% | 37,8% | 36,9% |
| FCFF (hoja) | 1.984 | 2.993 | 2.432 | — |

**Márgenes.** El margen operativo se mantuvo en 36-38% con ventas planas: es un negocio con poder de precio y costos flexibles. La hoja supone 36% estable. Si la competencia obliga a bajar precios en mascotas, el margen cae rápido porque la mezcla de mascotas es la más rentable. Las historias van de 29% a 38%.

**Reinversión y retorno.** Capex de US$620-730 millones al año (plantas de biológicos) e I+D de US$722 millones LTM. La hoja usa un sales-to-capital de 2. En los últimos doce meses recompró US$3.644 millones y pagó US$889 millones de dividendos, con deuda en aumento (US$9.042 millones): una apuesta de la gerencia a que el tropiezo es temporal. Ventaja durable: patentes que se renuevan, relación con los veterinarios y escala en salud animal, con ROIC estable de 26-29%. El ROIC después del año 10 es 16,9%, el promedio de su industria según Damodaran. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$224 millones, compromisos del 10-Q al 2026-06-30) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$37 millones, +0,39 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,02 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usa una beta de 1,11 (desde el 3-oct-2026; antes 0,90). Regla de la cartera (prompt v4, paso 2): bottom-up de Drugs (Pharmaceutical) (Damodaran, ene-2026: 0,92 desapalancada y corregida por caja) reapalancada con la D/E de mercado 0,25 = 1,11 = 1,11. La de regresión queda como referencia. El efecto de cada beta en el DCF técnico anterior está en la tabla.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF técnico anterior por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,11 | 9,9% | 8,9% | US$110,96 |
| Bottom-up del sector (Drugs (Pharmaceutical), reapalancada) | 1,11 | 9,9% | 8,9% | US$111,02 |


### Calibración técnica anterior Conservador/Base/Optimista (referencia auxiliar)

| Supuesto | Conservador | Base | Optimista |
|---|---:|---:|---:|
| Crecimiento año 1 | −2,0% | 1,7% | 4,0% |
| Crecimiento años 2–5 | 1,0% | 4,7% | 6,7% |
| Margen año 1 (base ajustada del modelo) | 36,4% | 36,4% | 36,4% |
| Margen objetivo | 33,4% | 36,4% | 38,4% |

Ventas/capital: 1,9x en años 1–5 y 1,9x en 6–10. WACC: 8,9%. Ke: 9,9%. Impuesto efectivo: 20,1%. Convergencia: 5 años. Estos parámetros son escenarios del analista, no cifras reportadas. Los casos Conservador, Base y Optimista de la hoja ya no son escenarios activos: sirven de calibración y de supuestos auxiliares de múltiplos. No confundir el antiguo caso técnico Base con la tesis Base.


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF técnico anterior | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 26,4% | 17,0% | 9,0% | 16,9% | US$114,13 | US$81,09 |

Fuentes de ventaja: Cartera de patentes que se renueva, relación con veterinarios (costos de cambio) y escala en salud animal. Evidencia: ROIC 26-29% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$114,23 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$92,09. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene aplicando descuentos al antiguo caso técnico de la hoja (US$114,13) ni mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$9.517 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 6.350 + 3.167 = 9.517. |
| Margen inicial del DCF | 36,4% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 20,05% en años 1–5; 20,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 8,91% → 9,00% | Tasa libre de riesgo 4,99%, beta 1,11, ERP 4,46%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 1,91x en años 1–5; 1,91x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 4,99%; Disrupción: 2,00% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (2,00%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Optimista: 16,90%; Conservadora/Disrupción: 9,00% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 1.676; deuda 9.272; acciones 413,2 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 6.350 × 1,01 + 3.167 × 1,03 = US$9.675,51 millones. Frente a 9.517, el crecimiento consolidado es 1,67%. En los años 2–5 es 4,66%, 5,33%, 5,34%, 5,35%; las ventas del año 5 son US$11.836,60 millones. El 4,5% de la tabla es el crecimiento anual compuesto de los cinco años: (11.836,60 / 9.517)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 9.675,51 × 36,39% × (1 − 20,05%) = US$2.814,87 millones. La reinversión es US$236,54 millones y el FCFF es US$2.578,32 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,00%. Reinversión terminal sobre el NOPAT: Base, 29,5% (4,99% / 16,90%); Conservadora, 55,4% (4,99% / 9,00%); Disrupción, 22,2% (2,00% / 9,00%); Optimista, 29,5% (4,99% / 16,90%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · Tropiezo temporal; vuelve a crecer con innovación** — probabilidad 40%; valor terminal 81.658 (VP 34.684); DCF US$114,23 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 9.676 | 1,7% | 36,4% | 2.815 | 237 | 2.578 | 8,9% | 2.367 |
| 2 | 10.127 | 4,7% | 36,4% | 2.946 | 283 | 2.663 | 8,9% | 2.245 |
| 3 | 10.666 | 5,3% | 36,4% | 3.103 | 299 | 2.805 | 8,9% | 2.171 |
| 4 | 11.236 | 5,3% | 36,4% | 3.269 | 315 | 2.954 | 8,9% | 2.099 |
| 5 | 11.837 | 5,3% | 36,4% | 3.444 | 327 | 3.116 | 8,9% | 2.033 |
| 6 | 12.461 | 5,3% | 36,4% | 3.626 | 340 | 3.286 | 8,9% | 1.968 |
| 7 | 13.110 | 5,2% | 36,4% | 3.815 | 353 | 3.462 | 8,9% | 1.903 |
| 8 | 13.782 | 5,1% | 36,4% | 4.011 | 366 | 3.645 | 9,0% | 1.839 |
| 9 | 14.480 | 5,1% | 36,4% | 4.215 | 379 | 3.836 | 9,0% | 1.776 |
| 10 | 15.203 | 5,0% | 36,4% | 4.426 | 398 | 4.028 | 9,0% | 1.711 |
| Terminal | 15.961 | 5,0% | 36,4% | 4.646 | 1.372 | 3.274 | 9,0% | — |

**Conservadora · Erosión prolongada de franquicias clave** — probabilidad 35%; valor terminal 39.152 (VP 16.630); DCF US$63,17 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 9.326 | −2,0% | 36,4% | 2.713 | 51 | 2.662 | 8,9% | 2.445 |
| 2 | 9.423 | 1,0% | 35,2% | 2.651 | 116 | 2.535 | 8,9% | 2.137 |
| 3 | 9.645 | 2,4% | 34,6% | 2.667 | 152 | 2.515 | 8,9% | 1.947 |
| 4 | 9.934 | 3,0% | 34,0% | 2.700 | 156 | 2.543 | 8,9% | 1.807 |
| 5 | 10.232 | 3,0% | 33,4% | 2.731 | 182 | 2.549 | 8,9% | 1.663 |
| 6 | 10.580 | 3,4% | 33,4% | 2.825 | 211 | 2.614 | 8,9% | 1.566 |
| 7 | 10.982 | 3,8% | 33,4% | 2.932 | 241 | 2.691 | 8,9% | 1.479 |
| 8 | 11.442 | 4,2% | 33,4% | 3.056 | 275 | 2.780 | 9,0% | 1.403 |
| 9 | 11.968 | 4,6% | 33,4% | 3.196 | 313 | 2.883 | 9,0% | 1.335 |
| 10 | 12.565 | 5,0% | 33,4% | 3.356 | 329 | 3.027 | 9,0% | 1.286 |
| Terminal | 13.192 | 5,0% | 33,4% | 3.524 | 1.954 | 1.570 | 9,0% | — |

**Disrupción · Deterioro de los fundamentales: Genéricos y competencia generalizada** — probabilidad 10%; valor terminal 27.082 (VP 11.503); DCF US$44,80 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 9.009 | −5,3% | 36,4% | 2.621 | -89 | 2.710 | 8,9% | 2.488 |
| 2 | 8.839 | −1,9% | 33,6% | 2.374 | 34 | 2.340 | 8,9% | 1.972 |
| 3 | 8.903 | 0,7% | 32,2% | 2.291 | 64 | 2.227 | 8,9% | 1.724 |
| 4 | 9.025 | 1,4% | 30,8% | 2.222 | 95 | 2.127 | 8,9% | 1.512 |
| 5 | 9.206 | 2,0% | 29,4% | 2.163 | 97 | 2.066 | 8,9% | 1.348 |
| 6 | 9.390 | 2,0% | 29,4% | 2.207 | 98 | 2.108 | 8,9% | 1.263 |
| 7 | 9.578 | 2,0% | 29,4% | 2.251 | 100 | 2.151 | 8,9% | 1.182 |
| 8 | 9.769 | 2,0% | 29,4% | 2.296 | 102 | 2.194 | 9,0% | 1.107 |
| 9 | 9.965 | 2,0% | 29,4% | 2.342 | 104 | 2.238 | 9,0% | 1.036 |
| 10 | 10.164 | 2,0% | 29,4% | 2.390 | 107 | 2.283 | 9,0% | 970 |
| Terminal | 10.367 | 2,0% | 29,4% | 2.437 | 542 | 1.896 | 9,0% | — |

**Optimista · Recuperación fuerte con nuevos productos** — probabilidad 15%; valor terminal 94.120 (VP 39.977); DCF US$132,05 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 9.898 | 4,0% | 36,4% | 2.880 | 346 | 2.533 | 8,9% | 2.326 |
| 2 | 10.558 | 6,7% | 37,2% | 3.139 | 371 | 2.768 | 8,9% | 2.334 |
| 3 | 11.265 | 6,7% | 37,6% | 3.385 | 398 | 2.988 | 8,9% | 2.312 |
| 4 | 12.024 | 6,7% | 38,0% | 3.652 | 383 | 3.269 | 8,9% | 2.323 |
| 5 | 12.755 | 6,1% | 38,4% | 3.915 | 392 | 3.523 | 8,9% | 2.299 |
| 6 | 13.502 | 5,9% | 38,4% | 4.144 | 399 | 3.745 | 8,9% | 2.243 |
| 7 | 14.264 | 5,6% | 38,4% | 4.379 | 406 | 3.973 | 8,9% | 2.184 |
| 8 | 15.037 | 5,4% | 38,4% | 4.617 | 411 | 4.206 | 9,0% | 2.122 |
| 9 | 15.820 | 5,2% | 38,4% | 4.858 | 414 | 4.444 | 9,0% | 2.057 |
| 10 | 16.610 | 5,0% | 38,4% | 5.101 | 435 | 4.666 | 9,0% | 1.982 |
| Terminal | 17.438 | 5,0% | 38,4% | 5.356 | 1.581 | 3.774 | 9,0% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 20.113,37 | 34.684,35 | 54.797,72 | 47.201,61 | 114,23 |
| Conservadora | 17.067,88 | 16.629,73 | 33.697,61 | 26.101,50 | 63,17 |
| Disrupción | 14.602,58 | 11.503,25 | 26.105,83 | 18.509,72 | 44,80 |
| Optimista | 22.183,57 | 39.977,47 | 62.161,04 | 54.564,93 | 132,05 |

Ejemplo Base: (20.113,37 + 34.684,35 + 1.676 − 9.272) / 413,2 = US$114,23 por acción. El terminal representa 63,3% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 40% / 35% / 10% / 15% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,40 × 114,234290 + 0,35 × 63,169173 + 0,10 × 44,796034 + 0,15 × 132,054529 = US$92,090709 ≈ US$92,09. Los aportes son US$45,69 + US$22,11 + US$4,48 + US$19,81 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 92,090709 × 0,65 = US$59,858961 ≈ US$59,86. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base ni al antiguo caso técnico de la hoja: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$114,23, es el valor intrínseco principal. El DCF esperado de US$92,09 combina las cuatro tesis con sus probabilidades y se presenta como complemento. La antigua calibración técnica Conservador/Base/Optimista de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: Tropiezo temporal; vuelve a crecer con innovación

**Qué plantea.** Es la tesis de la empresa: 2026 es un año de transición y la cartera nueva devuelve el crecimiento.

**Traducción al modelo.** Animales de compañía crece 1%, 5%, 6%, 6%, 6%; Animales de producción crece 3%, 4%, 4%, 4%, 4%. El crecimiento anual compuesto de cinco años es 4,5%; el margen operativo objetivo es 36,4%. El ROIC terminal es 16,9%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 40%; DCF: US$114,23 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (mascotas EE.UU. (interanual): −11% (2T26); ventas totales (orgánicas): −0,2% (2T26); franquicia de dermatología (Apoquel, Cytopoint): En baja). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: Erosión prolongada de franquicias clave

**Qué plantea.** Es una erosión prolongada de dermatología, dolor y parasiticidas: la caída simultánea en varias franquicias y los genéricos de Cerenia y Convenia la hacen casi tan probable como Base.

**Traducción al modelo.** Animales de compañía crece -4%, 0%, 2%, 3%, 3%; Animales de producción crece 2%, 3%, 3%, 3%, 3%. El crecimiento anual compuesto de cinco años es 1,5%; el margen operativo objetivo es 33,4%. El ROIC terminal es el costo de capital (9,00%). El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 35%; DCF: US$63,17 por acción.

**Cómo contrastarla.** La apoyarían: mascotas EE.UU. (interanual): caídas > 10% tres trimestres más; ventas totales (orgánicas): negativas; franquicia de dermatología (Apoquel, Cytopoint): caída de doble dígito; margen operativo: ≤ 33%.


#### Disrupción · Deterioro de los fundamentales: Genéricos y competencia generalizada

**Qué plantea.** Es competencia y genéricos generalizados.

**Traducción al modelo.** Animales de compañía crece -8%, -4%, 0%, 1%, 2%; Animales de producción crece 0%, 2%, 2%, 2%, 2%. El crecimiento anual compuesto de cinco años es −0,7%; el margen operativo objetivo es 29,4%. El ROIC terminal es el costo de capital (9,00%). El crecimiento terminal es 2,00%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 10%; DCF: US$44,80 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: mascotas EE.UU. (interanual): caídas > 10% tres trimestres más; ventas totales (orgánicas): negativas; franquicia de dermatología (Apoquel, Cytopoint): caída de doble dígito; margen operativo: ≤ 33%.


#### Optimista: Recuperación fuerte con nuevos productos

**Qué plantea.** Es una recuperación fuerte con nuevos productos.

**Traducción al modelo.** Animales de compañía crece 4%, 8%, 8%, 8%, 7%; Animales de producción crece 4%, 4%, 4%, 4%, 4%. El crecimiento anual compuesto de cinco años es 6,0%; el margen operativo objetivo es 38,4%. El ROIC terminal es 16,9%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 15%; DCF: US$132,05 por acción.

**Cómo contrastarla.** La confirmarían: mascotas EE.UU. (interanual): ≥ 0% en 2027; ventas totales (orgánicas): ≥ +4% en 2027; franquicia de dermatología (Apoquel, Cytopoint): estable; margen operativo: ≥ 36%.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 4,99%; Disrupción: 2,00%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,11) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **Base · Tropiezo temporal; vuelve a crecer con innovación** | 40% | Animales de compañía: 1%, 5%, 6%, 6%, 6%; Animales de producción: 3%, 4%, 4%, 4%, 4% | 4,5% | 36,4% | 1,9 | 16,9% | 4,99% | US$114,23 |
| **Conservadora · Erosión prolongada de franquicias clave** | 35% | Animales de compañía: -4%, 0%, 2%, 3%, 3%; Animales de producción: 2%, 3%, 3%, 3%, 3% | 1,5% | 33,4% | 1,9 | = costo de capital | 4,99% | US$63,17 |
| **Disrupción · Deterioro de los fundamentales: Genéricos y competencia generalizada** | 10% | Animales de compañía: -8%, -4%, 0%, 1%, 2%; Animales de producción: 0%, 2%, 2%, 2%, 2% | −0,7% | 29,4% | 1,9 | = costo de capital | 2,00% | US$44,80 |
| **Optimista · Recuperación fuerte con nuevos productos** | 15% | Animales de compañía: 4%, 8%, 8%, 8%, 7%; Animales de producción: 4%, 4%, 4%, 4%, 4% | 6,0% | 38,4% | 1,9 | 16,9% | 4,99% | US$132,05 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  |  | **US$92,09** |

Base (40%) es la tesis de la empresa: 2026 es un año de transición y la cartera nueva devuelve el crecimiento. Conservadora (35%) es una erosión prolongada de dermatología, dolor y parasiticidas: la caída simultánea en varias franquicias y los genéricos de Cerenia y Convenia la hacen casi tan probable como Base. Disrupción (10%) es competencia y genéricos generalizados. Optimista (15%) es una recuperación fuerte con nuevos productos. En las historias de erosión (Conservadora y Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF técnico anterior (beta 1,11; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF técnico anterior de la hoja.

| Crecimiento \ Margen | 32,4% | 34,4% | 36,4% | 38,4% | 40,4% |
|---|---:|---:|---:|---:|---:|
| 0,5% | 77,62 | 82,87 | 88,11 | 93,35 | 98,60 |
| 2,5% | 88,21 | 94,17 | 100,12 | 106,07 | 112,03 |
| 4,5% | 100,00 | 106,75 | 113,50 | 120,25 | 127,00 |
| 6,5% | 113,12 | 120,75 | 128,39 | 136,02 | 143,66 |
| 8,5% | 127,69 | 136,31 | 144,94 | 153,56 | 162,19 |


### Pre-mortem

1. Los competidores en dermatología (nuevos inhibidores de JAK y anticuerpos) le quitan participación a Apoquel y Cytopoint.
2. Las dudas de seguridad sobre Librela reducen su uso de forma permanente.
3. Los genéricos de Cerenia y Convenia y los parasiticidas de la competencia bajan precios.
4. El dueño de mascotas, presionado por la macro, visita menos al veterinario.
5. La deuda para recompras limita la flexibilidad si el flujo cae.

**Evidencia en contra de la historia más probable:** la caída es simultánea en varias franquicias (no un solo producto), lo que apunta a un problema competitivo más que a un año malo; si mascotas EE.UU. sigue cayendo en el 3T y 4T, Conservadora gana peso.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Mascotas EE.UU. (interanual) | −11% (2T26) | ≥ 0% en 2027 | Caídas > 10% tres trimestres más |
| Ventas totales (orgánicas) | −0,2% (2T26) | ≥ +4% en 2027 | Negativas |
| Franquicia de dermatología (Apoquel, Cytopoint) | En baja | Estable | Caída de doble dígito |
| Margen operativo | ~37% | ≥ 36% | ≤ 33% |
| Deuda neta / EBITDA | En alza | ≤ 2x | > 2,5x |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$69,69**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 32% | Margen 36% | Margen 38% |
|---|---:|---:|---:|
| Beta 1,11 | −1,2% (89% de las empresas) | −3,1% (93% de las empresas) | −4,0% (94% de las empresas) |
| Beta 1,11 | −1,2% (89% de las empresas) | −3,1% (93% de las empresas) | −4,0% (94% de las empresas) |

Frente al DCF Base (US$114,23), el valor intrínseco principal, el precio está por debajo en 39%.

Frente al DCF esperado de las historias (US$92,09), el complemento, el precio está por debajo en 24%. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Líder de salud animal con márgenes excepcionales y varias franquicias bajo presión a la vez |  |
| Probabilidades | Base 40% / Conservadora 35% / Disrupción 10% / Optimista 15% |  |
| DCF Base hoy (valor intrínseco principal) | US$114,23 |  |
| DCF esperado por probabilidades (complemento) | US$92,09 |  |
| Precio con MOS sobre el DCF esperado | US$59,86 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$44,80 a US$132,14 |  |
| Confianza | Media: la calidad del negocio es alta; la duración de la presión competitiva no |  |
| Qué cambiaría la opinión | Ventas de mascotas en EE.UU. y de dermatología en los próximos dos trimestres |  |
| Revisión | Resultados del 3T26 (nov-2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [Zoetis, Form 10-Q del 2T 2026](https://www.sec.gov/Archives/edgar/data/1555280/000155528026000040/zts-20260630.htm)
- [Zoetis, Form 10-Q del 1T 2026](https://www.sec.gov/Archives/edgar/data/1555280/000155528026000024/zts-20260331.htm)
- [Zoetis, Form 10-K 2025](https://www.sec.gov/Archives/edgar/data/1555280/000155528026000011/zts-20251231.htm)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
