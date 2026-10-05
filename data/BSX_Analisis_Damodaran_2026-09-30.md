---
schema: "jmr-analisis-damodaran-v1"
ticker: "BSX"
analysis_date: "2026-09-30"
---

# Boston Scientific Corporation (BSX) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$31,61 por acción** (Base · La cartera diversificada sostiene ~7%).

**Complemento · DCF esperado por probabilidades: US$30,48.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$20,33–37,86. El MOS 35% se aplica al esperado: US$19,81. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), balance del último 10-q, capital invertido operativo, deuda de balance sin arrendamientos operativos, eps básico, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet (28 celdas, con respaldo). DCF esperado US$33,95 → US$30,48. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (bloque Base de 'Valuation output': US$31,61 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja calcula estos cuatro DCF en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

Boston Scientific vende dispositivos de un solo uso para procedimientos mínimamente invasivos, sobre todo cardiovasculares. En 2023-2025 creció 12-20% al año gracias a dos productos excepcionales: la ablación por campo pulsado (FARAPULSE) y el cierre de orejuela Watchman. En 2026 ambos frenaron en EE.UU. (+3% en el 2T) al llegar la competencia de Medtronic y Johnson & Johnson, el crecimiento orgánico bajó a 7%. La historia de los próximos cinco años es la de una cartera amplia (dos tercios cardiovascular, un tercio MedSurg) en mercados que crecen por envejecimiento: ¿cuánto de su crecimiento dependía de productos que ahora se vuelven competidos? La compra pendiente de Penumbra (~US$14.500 millones) no está en esta valoración.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~7% anual cinco años | Sí | Sí: orgánico de 7% en el 2T26 con cartera diversificada | Probable |
| Electrofisiología vuelve a crecer a doble dígito | Sí | Sí fuera de EE.UU.; en EE.UU. hay tres competidores en campo pulsado | Incierto |
| El margen operativo GAAP sube de ~20% a 24% | Sí | Sí: el ajustado ya es mayor; la amortización de compras pesa ~4,5 pp | Probable si baja la actividad de compras |
| Penumbra crea valor al precio pagado | Sí | Depende de la trombectomía; se paga un múltiplo alto | Incierto |


### Visión externa: tasas base

Con ventas LTM de US$20.996 millones (US$14.856 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **$12,000-25,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 3,3% y una mediana de 2,9% (desviación estándar 8,9%); sumando una inflación de 2,5%, la mediana nominal ronda 5,4%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · La cartera diversificada sostiene ~7% | 6,5% | 42% |
| Conservadora · El campo pulsado se vuelve commodity | 4,1% | 58% |
| Disrupción · Deterioro de los fundamentales: Pierde participación y precio | 2,2% | 71% |
| Optimista · Electrofisiología y Watchman vuelven a doble dígito | 8,3% | 33% |

En dólares de 2015 la empresa está en el tramo de US$12.000-25.000 millones: crecer 6,5% anual cinco años (Base) lo logró ~42% de las empresas de ese tamaño; 8,3% (Optimista), ~33%. La hoja (7%) está por encima de la mediana nominal (~5,4%) pero es razonable por el envejecimiento y la cartera de productos. El crecimiento de 2023-2025 (12-20%, con compras) no es una tasa base útil: fue un ciclo de producto.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: una cartera amplia después de un ciclo de producto excepcional.** Entre 2023 y 2025 Boston Scientific creció 12-20% al año, pero eso fue un ciclo de producto (la ablación por campo pulsado FARAPULSE y el cierre de orejuela Watchman) más compras. En el 2T26 ambos productos frenaron en EE.UU. a +3% al llegar Medtronic y Johnson & Johnson, y el orgánico total bajó a 7%. La Base parte de ahí: Electrofisiología crece 10% y baja a 8%, Watchman entre 8% y 9%, el resto de Cardiovascular y MedSurg entre 5% y 6%. El resultado es 6,9% el primer año y 6,5% compuesto. No extrapolamos el 20% de 2025 porque no es una tasa base útil: fue un producto nuevo sin competencia. Tampoco suponemos que la desaceleración siga, porque la cartera es amplia y los mercados crecen por envejecimiento. La visión externa dice que ~42% de las empresas de su tamaño lo lograron. La Conservadora (4,1%) es el campo pulsado convertido en commodity; la Disrupción (2,2%), un tropiezo clínico que hace caer Electrofisiología; la Optimista (8,3%), que 2026 fue un ajuste temporal. Si EE.UU. repite ~3% en el 3T y el 4T, la Conservadora debería pesar más que la Base. La compra pendiente de Penumbra (~US$14.500 millones) no está en esta valoración.

**Margen: lo que dejan la amortización y las compras.** El margen GAAP subió de 4,9% en 2016 a 19,8% LTM, pero sigue cargado por ~US$930 millones al año de amortización de intangibles, litigios y reestructuración. La Base usa 24,2%: supone que parte de esos cargos se diluye con la escala. El rango de las historias —20,2% a 26,2%— refleja una pregunta concreta: si la empresa deja de comprar, la amortización baja y el margen sube; si sigue comprando (Penumbra y otras), el margen GAAP se queda cerca de 20%. Restar dos puntos al objetivo lleva la Base a US$28,10 (−11%); sumarlos, a US$35,11 (+11%). Lo invalidaría un margen GAAP por debajo de 18% en 2027.

**Reinversión: el crecimiento se compra, y eso decide el ROIC.** La reinversión es alta: I+D de ~10% de las ventas, capex de US$700-900 millones y compras frecuentes (Axonics, Bolt, Nalu y ahora Penumbra). La hoja usa un ventas/capital de 0,86× y 0,86×, que ya supone que parte del crecimiento se compra: cada dólar de ventas nuevas exige ~US$1,16 de capital. Incluida la plusvalía de esas compras, el ROIC fue 4-9% en 2021-2025, por debajo del costo de capital. Por eso la Base no conserva retornos excedentes después del año 10: el ROIC terminal es el costo de capital (9,4%). Es el supuesto por defecto de Damodaran cuando no hay una ventaja demostrada: el crecimiento posterior no suma ni resta valor. Se probó un ROIC terminal de 11,1% y se revirtió el 30-sep-2026 por no cumplir la regla. Con Penumbra el capital invertido sube ~US$14.500 millones; el retorno de esa compra dirá si el crecimiento de los próximos años crea valor.

**Descuento y terminal.** El costo de capital empieza en 9,22% y termina en 9,38%, con beta 0,98; la bottom-up de Healthcare Products reapalancada da 0,98, prácticamente igual. El riesgo de esta empresa no está en la tasa sino en la competencia en Electrofisiología, y por eso va en las historias. El crecimiento perpetuo es 5,29% y el valor terminal explica 60,8% del valor operativo de la Base. Como el ROIC terminal ya es el costo de capital, mover el crecimiento terminal casi no cambia el valor (US$31,37 (−0,7%) y US$31,84 (+0,7%)): crecer a perpetuidad sin retorno excedente no crea valor.

**Probabilidades y lectura del resultado.** La Base pesa 45% porque es lo que muestra el 2T26; la Conservadora 30% es el riesgo real, con tres competidores bajando precio en campo pulsado; la Disrupción solo 5%, un tropiezo clínico o de producto; la Optimista 20%, la lectura de que la caída de 2026 fue de inventario y adopción. El DCF Base es US$31,61 y el esperado US$30,48, con el precio en US$42,60. Los arrendamientos son pequeños aquí (+0,25 pp de margen) y no cambian la lectura. Las acciones se fijan en 1.449,2 millones; la emisión o la deuda para Penumbra no están modeladas.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$20.996 millones. Con el crecimiento de la Base llegan a US$28.832 millones en el año 5 y a US$37.721 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 20,2% en el año 1 a 24,2% al final, y se descuentan impuestos (17,8% al principio y 19,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$3.735 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$1.825 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$1.910 millones el primer año. Cada flujo se trae a hoy con el costo de capital (9,22% al principio, 9,38% al final): los diez años suman US$22.116 millones. Después del año 10 se supone que la empresa crece 5,29% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 9,4%; esa perpetuidad vale hoy US$34.282 millones, 61% del total. Flujos más terminal dan el valor de las operaciones, US$56.398 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$539 millones, más activos no operativos por US$2.245 millones, menos deuda por US$13.137 millones (incluye los arrendamientos capitalizados), menos minoritarios por US$242 millones. Queda un patrimonio de US$45.802 millones que, repartido entre 1.449,2 millones de acciones, da US$31,61 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 12,00× (peso 25% dentro de los múltiplos); EV/FCFF 18,19× (peso 38% dentro de los múltiplos); P/E 20,79× (peso 12% dentro de los múltiplos); P/FCFE 15,95× (peso 12% dentro de los múltiplos); P/OCF 12,72× (peso 12% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (9,9%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$31,61; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$28,10 | −11,1% |
| Margen objetivo +2 pp | US$35,11 | +11,1% |
| Crecimiento años 1–5 −2 pp | US$29,05 | −8,1% |
| Crecimiento años 1–5 +2 pp | US$34,40 | +8,8% |
| Ventas/capital −20% | US$29,44 | −6,8% |
| Ventas/capital +20% | US$33,05 | +4,6% |
| WACC +1 pp | US$26,71 | −15,5% |
| WACC −1 pp | US$37,79 | +19,6% |
| Crecimiento terminal −0,5 pp | US$31,37 | −0,7% |
| Crecimiento terminal +0,5 pp | US$31,84 | +0,7% |
| Acciones +5% | US$30,10 | −4,8% |


### Piezas del valor

**Crecimiento.** Ventas de US$14.240 millones (2023), US$16.747 millones (2024, +17,6%) y US$20.074 millones (2025, +19,9% con compras); US$10.646 millones en el 1S26 (+9,5%) y orgánico de 7% en el 2T. En el 1S26, Cardiovascular facturó US$7.126 millones (+10,8%): Electrofisiología US$1.821 millones (+16%), ICVT US$2.577 millones (+11,9%) y Watchman US$1.014 millones (+11,3%); MedSurg, ~US$3.520 millones. La división LTM de las historias usa esos pesos (EP ~17%, Watchman ~10%, resto de Cardiovascular ~40%, MedSurg ~33%).

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 14.240 | 16.747 | 20.074 | 20.996 |
| Crecimiento | +12,3% | +17,6% | +19,9% | — |
| Margen operativo GAAP | 16,5% | 15,5% | 18,0% | 19,8% |
| FCFF (hoja) | 2.166 | 1.947 | 3.775 | — |

**Márgenes.** El margen GAAP subió de 4,9% (2016) a 19,8% LTM, pero sigue cargado por amortización de intangibles (~US$930 millones al año), litigios y reestructuración. La hoja supone 20% el próximo año y 24% de objetivo. Si la empresa deja de comprar, la amortización baja y el margen sube; si compra Penumbra y otras, el GAAP se queda cerca de 20%. Por eso las historias van de 20% a 26%. La tasa efectiva de los años 1-5 es 17,8% (promedio 2023-2025); la del LTM, 5%, refleja beneficios fiscales de una vez.

**Reinversión y retorno.** La reinversión es alta: I+D de ~10% de las ventas, capex de US$700-900 millones y compras frecuentes (Axonics, Bolt, Nalu y ahora Penumbra). La hoja usa un ventas/capital de 0,86 (años 1-5) y 0,86 (años 6-10): con margen objetivo de 24,2% e impuesto marginal de 19%, cada dólar de capital nuevo rinde ~17% y ~17%, sin superar el mayor entre su ROIC actual (9,8%) y el de su industria (17,0%) (Damodaran, Investment Valuation cap. 11, p. 45; revisión del 4-oct-2026). Antes 1,26 y 1,17, que implicaban ~25% y ~23% sobre el capital nuevo. Con Penumbra, el capital invertido sube ~US$14.500 millones: el retorno de esa compra decide si el crecimiento crea valor. El ROIC después del año 10 es igual al costo de capital: incluida la plusvalía de las compras, el ROIC estuvo por debajo del costo de capital hasta 2025, así que no cumple la regla del ROIC terminal (se aplicó 11,1% y se revirtió el 30-sep-2026). Sin ventaja defendible: el crecimiento se compra y el ROIC con la plusvalía de las compras (4-9% en 2021-2025) no superó el costo de capital de forma sostenida. El ROIC después del año 10 es igual al costo de capital, el supuesto por defecto de Damodaran: el crecimiento posterior no suma valor.

**Ventas/capital: las referencias de Damodaran.** Damodaran elige el ventas/capital mirando el de la empresa hoy, el marginal de los últimos años y el promedio del sector, y comprueba que el rendimiento que implica sobre el capital nuevo sea creíble frente a lo que gana la empresa o su sector (Investment Valuation, cap. 11, p. 44-46). El capital de cada cierre se arma como el del modelo (patrimonio, incluido el preferente, + deuda y arrendamientos − caja e inversiones, + I+D capitalizado). El marginal es volátil: recompras, deterioros y moneda mueven el capital contable. El usado está dentro del rango de las referencias.

| Referencia | Ventas/capital | Detalle |
|---|---:|---|
| Empresa hoy | 0,60 | ventas LTM 20.996,0 / capital invertido 35.283,4 millones |
| Marginal, últimos tres años | 0,87 | Δventas 7.392,0 / Δcapital 8.462,0 millones (Dec '22 → Dec '25; capital 25.927,0 → 34.389,0) |
| Marginal, últimos cinco años | 0,87 | Δventas 10.161,0 / Δcapital 11.654,0 millones (Dec '20 → Dec '25; capital 22.735,0 → 34.389,0) |
| Sector (Damodaran, enero de 2026) | 1,48 | Healthcare Products |
| Usado en la hoja | 0,86 / 0,86 | años 1-5 / 6-10; rinde ~17% / ~17% sobre el capital nuevo (ROIC actual 9,8%) |

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$519 millones, compromisos del 10-K al 2025-12-31) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$52 millones, +0,25 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,02 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usa una beta de 0,98 (desde el 3-oct-2026; antes 1,00). Regla de la cartera (prompt v4, paso 2): bottom-up de Healthcare Products (Damodaran, ene-2026: 0,86 desapalancada y corregida por caja) reapalancada con la D/E de mercado 0,17 = 0,98 = 0,98. La de regresión queda como referencia. El efecto de cada beta en el DCF Base está en la tabla.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 0,98 | 9,9% | 9,2% | US$32,27 |
| Bottom-up del sector (Healthcare Products, reapalancada) | 0,98 | 9,9% | 9,2% | US$32,28 |


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Sin ventaja defendible | 9,8% | 17,0% | 9,4% | = costo de capital | US$31,61 | US$32,27 |

Fuentes de ventaja: Patentes y relación con médicos, pero el crecimiento se compra. Evidencia: ROIC (con plusvalía) 4-9% en 2021-2025, bajo el costo de capital hasta 2025. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$31,61 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$30,48. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$20.996 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 3.590 + 2.000 + 8.470 + 6.936 = 20.996. |
| Margen inicial del DCF | 20,2% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 17,80% en años 1–5; 19,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 9,22% → 9,38% | Tasa libre de riesgo 5,29%, beta 0,98, ERP 4,74%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 0,86x en años 1–5; 0,86x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 5,29%; Disrupción: 2,76% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (2,76%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Conservadora/Disrupción/Optimista: 9,38% (= WACC terminal) | Criterio de ventaja competitiva (sin ventaja defendible). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 539; deuda 13.137; activos no operativos 2.245; minoritarios 242; acciones 1.449,2 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 3.590 × 1,10 + 2.000 × 1,08 + 8.470 × 1,06 + 6.936 × 1,06 = US$22.439,36 millones. Frente a 20.996, el crecimiento consolidado es 6,87%. En los años 2–5 es 6,99%, 6,84%, 6,18%, 5,87%; las ventas del año 5 son US$28.832,34 millones. El 6,5% de la tabla es el crecimiento anual compuesto de los cinco años: (28.832,34 / 20.996)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 22.439,36 × 20,25% × (1 − 17,80%) = US$3.734,79 millones. La reinversión es US$1.824,56 millones y el FCFF es US$1.910,23 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,38%. Reinversión terminal sobre el NOPAT: Base, 56,4% (5,29% / 9,38%); Conservadora, 56,4% (5,29% / 9,38%); Disrupción, 29,4% (2,76% / 9,38%); Optimista, 56,4% (5,29% / 9,38%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · La cartera diversificada sostiene ~7%** — probabilidad 45%; valor terminal 83.163 (VP 34.282); DCF US$31,61 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 22.439 | 6,9% | 20,2% | 3.735 | 1.825 | 1.910 | 9,2% | 1.749 |
| 2 | 24.008 | 7,0% | 21,8% | 4.312 | 1.909 | 2.403 | 9,2% | 2.015 |
| 3 | 25.650 | 6,8% | 22,6% | 4.775 | 1.842 | 2.933 | 9,2% | 2.251 |
| 4 | 27.234 | 6,2% | 23,4% | 5.249 | 1.858 | 3.391 | 9,2% | 2.383 |
| 5 | 28.832 | 5,9% | 24,2% | 5.747 | 1.929 | 3.818 | 9,2% | 2.457 |
| 6 | 30.491 | 5,8% | 24,2% | 6.060 | 1.999 | 4.061 | 9,3% | 2.392 |
| 7 | 32.210 | 5,6% | 24,2% | 6.383 | 2.068 | 4.315 | 9,3% | 2.325 |
| 8 | 33.988 | 5,5% | 24,2% | 6.715 | 2.136 | 4.579 | 9,3% | 2.258 |
| 9 | 35.826 | 5,4% | 24,2% | 7.057 | 2.204 | 4.854 | 9,3% | 2.188 |
| 10 | 37.721 | 5,3% | 24,2% | 7.409 | 2.320 | 5.088 | 9,4% | 2.098 |
| Terminal | 39.716 | 5,3% | 24,2% | 7.801 | 4.399 | 3.401 | 9,4% | — |

**Conservadora · El campo pulsado se vuelve commodity** — probabilidad 30%; valor terminal 65.485 (VP 26.995); DCF US$25,57 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 21.898 | 4,3% | 20,2% | 3.645 | 1.164 | 2.481 | 9,2% | 2.271 |
| 2 | 22.899 | 4,6% | 21,0% | 3.962 | 1.110 | 2.852 | 9,2% | 2.391 |
| 3 | 23.854 | 4,2% | 21,4% | 4.206 | 1.064 | 3.141 | 9,2% | 2.411 |
| 4 | 24.769 | 3,8% | 21,8% | 4.448 | 1.106 | 3.343 | 9,2% | 2.349 |
| 5 | 25.720 | 3,8% | 22,2% | 4.704 | 1.235 | 3.469 | 9,2% | 2.232 |
| 6 | 26.782 | 4,1% | 22,2% | 4.884 | 1.376 | 3.507 | 9,3% | 2.066 |
| 7 | 27.965 | 4,4% | 22,2% | 5.084 | 1.531 | 3.553 | 9,3% | 1.915 |
| 8 | 29.282 | 4,7% | 22,2% | 5.308 | 1.702 | 3.606 | 9,3% | 1.778 |
| 9 | 30.746 | 5,0% | 22,2% | 5.557 | 1.891 | 3.666 | 9,3% | 1.653 |
| 10 | 32.373 | 5,3% | 22,2% | 5.834 | 1.991 | 3.843 | 9,4% | 1.584 |
| Terminal | 34.085 | 5,3% | 22,2% | 6.143 | 3.464 | 2.678 | 9,4% | — |

**Disrupción · Deterioro de los fundamentales: Pierde participación y precio** — probabilidad 5%; valor terminal 48.227 (VP 19.880); DCF US$20,33 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 21.279 | 1,3% | 20,2% | 3.542 | 435 | 3.107 | 9,2% | 2.845 |
| 2 | 21.652 | 1,8% | 20,2% | 3.604 | 617 | 2.987 | 9,2% | 2.504 |
| 3 | 22.183 | 2,4% | 20,2% | 3.692 | 712 | 2.980 | 9,2% | 2.288 |
| 4 | 22.795 | 2,8% | 20,2% | 3.794 | 732 | 3.062 | 9,2% | 2.152 |
| 5 | 23.424 | 2,8% | 20,2% | 3.899 | 752 | 3.147 | 9,2% | 2.025 |
| 6 | 24.071 | 2,8% | 20,2% | 3.995 | 773 | 3.222 | 9,3% | 1.898 |
| 7 | 24.735 | 2,8% | 20,2% | 4.093 | 794 | 3.299 | 9,3% | 1.778 |
| 8 | 25.418 | 2,8% | 20,2% | 4.194 | 816 | 3.378 | 9,3% | 1.665 |
| 9 | 26.120 | 2,8% | 20,2% | 4.297 | 838 | 3.458 | 9,3% | 1.559 |
| 10 | 26.841 | 2,8% | 20,2% | 4.402 | 862 | 3.541 | 9,4% | 1.460 |
| Terminal | 27.582 | 2,8% | 20,2% | 4.524 | 1.331 | 3.192 | 9,4% | — |

**Optimista · Electrofisiología y Watchman vuelven a doble dígito** — probabilidad 20%; valor terminal 100.169 (VP 41.292); DCF US$37,86 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 22.893 | 9,0% | 20,2% | 3.810 | 2.433 | 1.377 | 9,2% | 1.261 |
| 2 | 24.985 | 9,1% | 22,6% | 4.651 | 2.424 | 2.228 | 9,2% | 1.868 |
| 3 | 27.070 | 8,3% | 23,8% | 5.307 | 2.398 | 2.908 | 9,2% | 2.232 |
| 4 | 29.132 | 7,6% | 25,0% | 5.998 | 2.461 | 3.537 | 9,2% | 2.486 |
| 5 | 31.249 | 7,3% | 26,2% | 6.742 | 2.496 | 4.246 | 9,2% | 2.732 |
| 6 | 33.395 | 6,9% | 26,2% | 7.184 | 2.514 | 4.670 | 9,3% | 2.751 |
| 7 | 35.558 | 6,5% | 26,2% | 7.627 | 2.514 | 5.113 | 9,3% | 2.756 |
| 8 | 37.719 | 6,1% | 26,2% | 8.067 | 2.493 | 5.574 | 9,3% | 2.748 |
| 9 | 39.864 | 5,7% | 26,2% | 8.501 | 2.452 | 6.048 | 9,3% | 2.727 |
| 10 | 41.973 | 5,3% | 26,2% | 8.924 | 2.582 | 6.342 | 9,4% | 2.614 |
| Terminal | 44.193 | 5,3% | 26,2% | 9.396 | 5.299 | 4.097 | 9,4% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 22.115,84 | 34.281,74 | 56.397,58 | 45.802,15 | 31,61 |
| Conservadora | 20.650,21 | 26.994,71 | 47.644,92 | 37.049,48 | 25,57 |
| Disrupción | 20.173,42 | 19.880,39 | 40.053,81 | 29.458,37 | 20,33 |
| Optimista | 24.175,18 | 41.292,17 | 65.467,35 | 54.871,91 | 37,86 |

Ejemplo Base: (22.115,84 + 34.281,74 + 539 + 2.245 − 13.137 − 242) / 1.449,2 = US$31,61 por acción. El terminal representa 60,8% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 45% / 30% / 5% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,45 × 31,605126 + 0,30 × 25,565472 + 0,05 × 20,327335 + 0,20 × 37,863590 = US$30,481033 ≈ US$30,48. Los aportes son US$14,22 + US$7,67 + US$1,02 + US$7,57 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 30,481033 × 0,65 = US$19,812672 ≈ US$19,81. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$31,61, es el valor intrínseco principal. El DCF esperado de US$30,48 combina las cuatro tesis con sus probabilidades y se presenta como complemento. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: La cartera diversificada sostiene ~7%

**Qué plantea.** Es lo que muestra el 2T26: orgánico de 7% con Electrofisiología desacelerando pero todavía creciendo.

**Traducción al modelo.** Electrofisiología crece 10%, 10%, 9%, 8%, 8%; Watchman crece 8%, 9%, 9%, 8%, 8%; Resto de Cardiovascular crece 6%, 6%, 6%, 5%, 5%; MedSurg crece 6%, 6%, 6%, 6%, 5%. El crecimiento anual compuesto de cinco años es 6,5%; el margen operativo objetivo es 24,2%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 45%; DCF: US$31,61 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (crecimiento orgánico total: 7,0% (2T26); electrofisiología EE.UU.: +3% (2T26); watchman EE.UU.: +3% (2T26)). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: El campo pulsado se vuelve commodity

**Qué plantea.** Es el riesgo real: tres competidores en campo pulsado bajan precio y participación en EE.UU.

**Traducción al modelo.** Electrofisiología crece 2%, 3%, 3%, 3%, 3%; Watchman crece 3%, 4%, 4%, 4%, 4%; Resto de Cardiovascular crece 5%, 5%, 4%, 4%, 4%; MedSurg crece 5%, 5%, 5%, 4%, 4%. El crecimiento anual compuesto de cinco años es 4,1%; el margen operativo objetivo es 22,2%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 30%; DCF: US$25,57 por acción.

**Cómo contrastarla.** La apoyarían: crecimiento orgánico total: < 5% dos trimestres; electrofisiología EE.UU.: ≤ 0%; watchman EE.UU.: ≤ 0%; margen operativo GAAP: ≤ 18%.


#### Disrupción · Deterioro de los fundamentales: Pierde participación y precio

**Qué plantea.** Es un tropiezo clínico o de producto.

**Traducción al modelo.** Electrofisiología crece -5%, -3%, 0%, 2%, 2%; Watchman crece 0%, 0%, 2%, 2%, 2%; Resto de Cardiovascular crece 3%, 3%, 3%, 3%, 3%; MedSurg crece 3%, 3%, 3%, 3%, 3%. El crecimiento anual compuesto de cinco años es 2,2%; el margen operativo objetivo es 20,2%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 2,76%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 5%; DCF: US$20,33 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: crecimiento orgánico total: < 5% dos trimestres; electrofisiología EE.UU.: ≤ 0%; watchman EE.UU.: ≤ 0%; margen operativo GAAP: ≤ 18%.


#### Optimista: Electrofisiología y Watchman vuelven a doble dígito

**Qué plantea.** Supone que la caída de 2026 fue un ajuste temporal (inventario, adopción de nuevos catéteres).

**Traducción al modelo.** Electrofisiología crece 15%, 15%, 13%, 12%, 10%; Watchman crece 14%, 14%, 12%, 10%, 10%; Resto de Cardiovascular crece 7%, 7%, 7%, 6%, 6%; MedSurg crece 7%, 7%, 6%, 6%, 6%. El crecimiento anual compuesto de cinco años es 8,3%; el margen operativo objetivo es 26,2%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 20%; DCF: US$37,86 por acción.

**Cómo contrastarla.** La confirmarían: crecimiento orgánico total: ≥ 7%; electrofisiología EE.UU.: ≥ +8% en 2027; watchman EE.UU.: ≥ +8%; margen operativo GAAP: ≥ 21% en 2027.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 5,29%; Disrupción: 2,76%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | Crecimiento terminal | Valor/acción (beta 0,98) |
|---|---:|---|---:|---:|---:|---:|---:|
| **Base · La cartera diversificada sostiene ~7%** | 45% | Electrofisiología: 10%, 10%, 9%, 8%, 8%; Watchman: 8%, 9%, 9%, 8%, 8%; Resto de Cardiovascular: 6%, 6%, 6%, 5%, 5%; MedSurg: 6%, 6%, 6%, 6%, 5% | 6,5% | 24,2% | 0,9 | 5,29% | US$31,61 |
| **Conservadora · El campo pulsado se vuelve commodity** | 30% | Electrofisiología: 2%, 3%, 3%, 3%, 3%; Watchman: 3%, 4%, 4%, 4%, 4%; Resto de Cardiovascular: 5%, 5%, 4%, 4%, 4%; MedSurg: 5%, 5%, 5%, 4%, 4% | 4,1% | 22,2% | 0,9 | 5,29% | US$25,57 |
| **Disrupción · Deterioro de los fundamentales: Pierde participación y precio** | 5% | Electrofisiología: -5%, -3%, 0%, 2%, 2%; Watchman: 0%, 0%, 2%, 2%, 2%; Resto de Cardiovascular: 3%, 3%, 3%, 3%, 3%; MedSurg: 3%, 3%, 3%, 3%, 3% | 2,2% | 20,2% | 0,9 | 2,76% | US$20,33 |
| **Optimista · Electrofisiología y Watchman vuelven a doble dígito** | 20% | Electrofisiología: 15%, 15%, 13%, 12%, 10%; Watchman: 14%, 14%, 12%, 10%, 10%; Resto de Cardiovascular: 7%, 7%, 7%, 6%, 6%; MedSurg: 7%, 7%, 6%, 6%, 6% | 8,3% | 26,2% | 0,9 | 5,29% | US$37,86 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  | **US$30,48** |

Base (45%) es lo que muestra el 2T26: orgánico de 7% con Electrofisiología desacelerando pero todavía creciendo. Conservadora (30%) es el riesgo real: tres competidores en campo pulsado bajan precio y participación en EE.UU. Disrupción (5%) es un tropiezo clínico o de producto. Optimista (20%) supone que la caída de 2026 fue un ajuste temporal (inventario, adopción de nuevos catéteres). En las historias de erosión (Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 0,98; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.

| Crecimiento \ Margen | 20,2% | 22,2% | 24,2% | 26,2% | 28,2% |
|---|---:|---:|---:|---:|---:|
| 2,5% | 21,24 | 24,02 | 26,79 | 29,57 | 32,35 |
| 4,5% | 22,87 | 26,00 | 29,14 | 32,28 | 35,41 |
| 6,5% | 24,64 | 28,18 | 31,71 | 35,25 | 38,78 |
| 8,5% | 26,57 | 30,55 | 34,53 | 38,51 | 42,49 |
| 10,5% | 28,67 | 33,15 | 37,62 | 42,09 | 46,57 |


### Pre-mortem

1. Medtronic y Johnson & Johnson ganan participación en campo pulsado y Electrofisiología en EE.UU. crece a un dígito bajo por años.
2. Watchman pierde frente a nuevos anticoagulantes o por evidencia clínica comparativa desfavorable.
3. Penumbra se paga caro, genera deterioro de goodwill y la deuda limita la flexibilidad.
4. La demanda colectiva por la guía de Electrofisiología revela problemas de gestión o de transparencia.
5. Presión de precios en ICVT y reembolsos de Medicare más bajos reducen el margen.

**Evidencia en contra de la historia más probable:** el freno en EE.UU. fue brusco (de doble dígito alto a +3% en un trimestre) y coincidió con la llegada de competencia directa. Si el 3T y el 4T repiten ~3% en EE.UU., la historia Conservadora debe pesar más que Base.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Crecimiento orgánico total | 7,0% (2T26) | ≥ 7% | < 5% dos trimestres |
| Electrofisiología EE.UU. | +3% (2T26) | ≥ +8% en 2027 | ≤ 0% |
| Watchman EE.UU. | +3% (2T26) | ≥ +8% | ≤ 0% |
| Margen operativo GAAP | 19,8% LTM | ≥ 21% en 2027 | ≤ 18% |
| Penumbra (antimonopolio y retorno) | Pendiente | Cierre y crecimiento de trombectomía ≥ 15% | Remedios o deterioro |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$42,60**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 22% | Margen 24% | Margen 26% |
|---|---:|---:|---:|
| Beta 0,98 | 16,6% (8% de las empresas) | 13,4% (13% de las empresas) | 10,8% (22% de las empresas) |
| Beta 0,98 | 16,6% (8% de las empresas) | 13,4% (13% de las empresas) | 10,8% (22% de las empresas) |

Frente al DCF Base (US$31,61), el valor intrínseco principal, el precio está por encima en 35%.

Frente al DCF esperado de las historias (US$30,48), el complemento, el precio está por encima en 40%. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Cartera cardiovascular diversificada que pierde su ciclo de producto excepcional |  |
| Probabilidades | Base 45% / Conservadora 30% / Disrupción 5% / Optimista 20% |  |
| DCF Base hoy (valor intrínseco principal) | US$31,61 |  |
| DCF esperado por probabilidades (complemento) | US$30,48 |  |
| Precio con MOS sobre el DCF esperado | US$19,81 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$20,33 a US$37,87 |  |
| Confianza | Media: la diversificación da piso; la duración de la competencia en campo pulsado es incierta |  |
| Qué cambiaría la opinión | Electrofisiología y Watchman en EE.UU. en los próximos dos trimestres; cierre y precio de Penumbra |  |
| Revisión | Resultados del 3T26 (oct-2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [Boston Scientific, Form 10-Q del 2T 2026](https://www.sec.gov/Archives/edgar/data/885725/000088572526000053/bsx-20260630.htm)
- [Boston Scientific, Form 10-Q del 1T 2026](https://www.sec.gov/Archives/edgar/data/885725/000088572526000033/bsx-20260331.htm)
- [Boston Scientific, Form 10-K 2025](https://www.sec.gov/Archives/edgar/data/885725/000088572526000010/bsx-20251231.htm)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
