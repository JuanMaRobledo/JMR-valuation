---
schema: "jmr-analisis-damodaran-v1"
ticker: "BSX"
analysis_date: "2026-09-30"
---

# Boston Scientific Corporation (BSX) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$35,22 por acción** (Base · La cartera diversificada sostiene ~7%).

**Complemento · DCF esperado por probabilidades: US$33,91.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$21,86–42,59. El MOS 35% se aplica al esperado: US$22,04. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), balance del último 10-q, capital invertido operativo, deuda de balance sin arrendamientos operativos, eps básico, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet (28 celdas, con respaldo). DCF esperado US$33,95 → US$33,91. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (bloque Base de 'Valuation output': US$35,22 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja calcula estos cuatro DCF en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

Boston Scientific vende dispositivos de un solo uso para procedimientos mínimamente invasivos, sobre todo cardiovasculares. En 2023-2025 creció 12-20% al año gracias a dos productos excepcionales: la ablación por campo pulsado (FARAPULSE) y el cierre de orejuela Watchman. En 2026 ambos frenaron en EE.UU. (+3% en el 2T) al llegar la competencia de Medtronic y Johnson & Johnson, el crecimiento orgánico bajó a 7%. La historia de los próximos cinco años es la de una cartera amplia (dos tercios cardiovascular, un tercio MedSurg) en mercados que crecen por envejecimiento: ¿cuánto de su crecimiento dependía de productos que ahora se vuelven competidos? En agosto un ciberataque paró durante semanas parte de la fabricación y de los despachos; la empresa dijo que no cumplirá la guía de ventas de 2026 y que no espera un efecto material de largo plazo (8-K del 8-sep-2026). La compra pendiente de Penumbra (~US$14.500 millones) no está en esta valoración.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~6% anual cinco años | Sí | Sí: orgánico de 7% en el 2T26 con cartera diversificada; 2026 más bajo por la guía y el ciberataque | Probable |
| Electrofisiología vuelve a crecer a doble dígito | Sí | Sí fuera de EE.UU.; en EE.UU. hay tres competidores en campo pulsado | Incierto |
| El margen operativo GAAP sube de ~20% a 24% | Sí | Sí: el ajustado ya es mayor; la amortización de compras pesa ~4,5 pp | Probable si baja la actividad de compras |
| Penumbra crea valor al precio pagado | Sí | Depende de la trombectomía; se paga un múltiplo alto | Incierto |


### Visión externa: tasas base

Con ventas LTM de US$20.996 millones (US$14.856 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **$12,000-25,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 3,3% y una mediana de 2,9% (desviación estándar 8,9%); sumando una inflación de 2,5%, la mediana nominal ronda 5,4%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · La cartera diversificada sostiene ~7% | 6,1% | 46% |
| Conservadora · El campo pulsado se vuelve commodity | 3,7% | 61% |
| Disrupción · Deterioro de los fundamentales: Pierde participación y precio | 1,8% | 72% |
| Optimista · Electrofisiología y Watchman vuelven a doble dígito | 7,9% | 34% |

En dólares de 2015 la empresa está en el tramo de US$12.000-25.000 millones: crecer 6,1% anual cinco años (Base) lo logró ~46% de las empresas de ese tamaño; 7,9% (Optimista), ~34%. La Base está por encima de la mediana nominal (~5,4%) pero es razonable por el envejecimiento y la cartera de productos; su primer año es bajo por la guía de julio y el ciberataque. El crecimiento de 2023-2025 (12-20%, con compras) no es una tasa base útil: fue un ciclo de producto.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: una cartera amplia después de un ciclo de producto excepcional.** Entre 2023 y 2025 Boston Scientific creció 12-20% al año, pero eso fue un ciclo de producto (la ablación por campo pulsado FARAPULSE y el cierre de orejuela Watchman) más compras. En el 2T26 ambos productos frenaron en EE.UU. a +3% al llegar Medtronic y Johnson & Johnson, y el orgánico total bajó a 7%. La Base parte de ahí. El primer año (jul-2026 a jun-2027) sigue la guía de julio (+3-5% en el 3T26 y ~2-3% en el segundo semestre) y el ciberataque del 25-ago-2026, que la empresa ya dijo que le hará incumplir esa guía: Electrofisiología 6%, Watchman 4% y el resto 3,5%. El segundo año rebota contra esa base deprimida (Electrofisiología 11%, Watchman 10%, el resto 6,5%) y desde el tercero Electrofisiología crece 9% y baja a 8%, Watchman entre 8% y 9% y el resto de Cardiovascular y MedSurg entre 5% y 6%. Es un desfase de un año, no una historia más pobre: el ciberataque no cambia los mercados ni la cartera. El resultado es 4,0% el primer año y 6,1% compuesto. No extrapolamos el 20% de 2025 porque no es una tasa base útil: fue un producto nuevo sin competencia. Tampoco suponemos que la desaceleración siga, porque la cartera es amplia y los mercados crecen por envejecimiento. La visión externa dice que ~46% de las empresas de su tamaño lo lograron. La Conservadora (3,7%) es el campo pulsado convertido en commodity; la Disrupción (1,8%), un tropiezo clínico que hace caer Electrofisiología; la Optimista (7,9%), que 2026 fue un ajuste temporal. Si EE.UU. repite ~3% en el 3T y el 4T, la Conservadora debería pesar más que la Base. La compra pendiente de Penumbra (~US$14.500 millones) no está en esta valoración.

**Margen: lo que dejan la amortización y las compras.** El margen GAAP subió de 4,9% en 2016 a 19,8% LTM, pero sigue cargado por ~US$930 millones al año de amortización de intangibles, litigios y reestructuración. La Base usa 24,2%. En el 2T26 el margen GAAP fue 21,6% y el ajustado 28,4%: la amortización resta 4,3 pp y compras, reestructuración y litigios ~2,4 pp. Sin compras nuevas, la amortización de las pasadas pesa menos cada año; reestructuraciones y litigios siguen (hay un plan nuevo de US$700-800 millones hasta 2029, con ~US$500 millones de ahorro anual en buena parte reinvertido). Eso deja el objetivo entre el GAAP y el ajustado. El rango de las historias —20,2% a 26,2%— refleja una pregunta concreta: si la empresa deja de comprar, la amortización baja y el margen sube; si sigue comprando (Penumbra y otras), el margen GAAP se queda cerca de 20%. Restar dos puntos al objetivo lleva la Base a US$31,62 (−10%); sumarlos, a US$38,82 (+10%). Lo invalidaría un margen GAAP por debajo de 18% en 2027.

**Reinversión: el crecimiento se compra, y eso decide el ROIC.** La reinversión es alta: I+D de ~10% de las ventas, capex de US$700-900 millones y compras frecuentes (Axonics, Bolt, Nalu y ahora Penumbra). La Base crece con los segmentos (5-10%), sin compras, y la hoja usa un ventas/capital de 1,26× y 1,17×: cada dólar de ventas nuevas exige ~US$0,79 de capital, entre lo que pide hoy con el crédito mercantil de las compras (~US$1,67) y el promedio del sector (~US$0,68). Si Boston Scientific sigue comprando, hay que sumar a la vez los ingresos y el precio de cada compra. Incluida la plusvalía de esas compras, el ROIC fue 4-9% en 2021-2025, por debajo del costo de capital. Por eso la Base no conserva retornos excedentes después del año 10: el ROIC terminal es el costo de capital (9,0%). Es el supuesto por defecto de Damodaran cuando no hay una ventaja demostrada: el crecimiento posterior no suma ni resta valor. Se probó un ROIC terminal de 11,1% y se revirtió el 30-sep-2026 por no cumplir la regla. Con Penumbra el capital invertido sube ~US$14.500 millones; el retorno de esa compra dirá si el crecimiento de los próximos años crea valor.

**Descuento y terminal.** El costo de capital empieza en 8,91% y termina en 8,99%, con beta 0,98; la bottom-up de Healthcare Products reapalancada da 0,98, prácticamente igual. El riesgo de esta empresa no está en la tasa sino en la competencia en Electrofisiología, y por eso va en las historias. El crecimiento perpetuo es 5,29% y el valor terminal explica 58,6% del valor operativo de la Base. Como el ROIC terminal ya es el costo de capital, mover el crecimiento terminal casi no cambia el valor (US$34,89 (−0,9%) y US$35,55 (+1,0%)): crecer a perpetuidad sin retorno excedente no crea valor.

**Probabilidades y lectura del resultado.** La Base pesa 45% porque es lo que muestra el 2T26; la Conservadora 30% es el riesgo real, con tres competidores bajando precio en campo pulsado; la Disrupción solo 5%, un tropiezo clínico o de producto; la Optimista 20%, la lectura de que la caída de 2026 fue de inventario y adopción. El DCF Base es US$35,22 y el esperado US$33,91, con el precio en US$43,65. Los arrendamientos son pequeños aquí (+0,25 pp de margen) y no cambian la lectura. Las acciones se fijan en 1.449,2 millones; la emisión o la deuda para Penumbra no están modeladas.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$20.996 millones. Con el crecimiento de la Base llegan a US$28.210 millones en el año 5 y a US$36.903 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 20,2% en el año 1 a 24,2% al final, y se descuentan impuestos (17,8% al principio y 19,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$3.633 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$1.320 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$2.313 millones el primer año. Cada flujo se trae a hoy con el costo de capital (8,91% al principio, 8,99% al final): los diez años suman US$25.544 millones. Después del año 10 se supone que la empresa crece 5,29% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 9,0%; esa perpetuidad vale hoy US$36.087 millones, 59% del total. Flujos más terminal dan el valor de las operaciones, US$61.631 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$539 millones, más activos no operativos por US$2.245 millones, menos deuda por US$13.137 millones (incluye los arrendamientos capitalizados), menos minoritarios por US$242 millones. Queda un patrimonio de US$51.036 millones que, repartido entre 1.449,2 millones de acciones, da US$35,22 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 12,00× (peso 25% dentro de los múltiplos); EV/FCFF 18,19× (peso 38% dentro de los múltiplos); P/E 20,79× (peso 12% dentro de los múltiplos); P/FCFE 15,95× (peso 12% dentro de los múltiplos); P/OCF 12,72× (peso 12% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (9,6%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$35,22; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$31,62 | −10,2% |
| Margen objetivo +2 pp | US$38,82 | +10,2% |
| Crecimiento años 1–5 −2 pp | US$31,75 | −9,8% |
| Crecimiento años 1–5 +2 pp | US$39,03 | +10,8% |
| Ventas/capital −20% | US$33,69 | −4,3% |
| Ventas/capital +20% | US$36,24 | +2,9% |
| WACC +1 pp | US$29,91 | −15,1% |
| WACC −1 pp | US$41,97 | +19,2% |
| Crecimiento terminal −0,5 pp | US$34,89 | −0,9% |
| Crecimiento terminal +0,5 pp | US$35,55 | +1,0% |
| Acciones +5% | US$33,54 | −4,8% |


### Piezas del valor

**Crecimiento.** Ventas de US$14.240 millones (2023), US$16.747 millones (2024, +17,6%) y US$20.074 millones (2025, +19,9% con compras); US$10.646 millones en el 1S26 (+9,5%) y orgánico de 7% en el 2T. En el 1S26, Cardiovascular facturó US$7.126 millones (+10,8%): Electrofisiología US$1.821 millones (+16%), ICVT US$2.577 millones (+11,9%) y Watchman US$1.014 millones (+11,3%); MedSurg, ~US$3.520 millones. La división LTM de las historias usa esos pesos (EP ~17%, Watchman ~10%, resto de Cardiovascular ~40%, MedSurg ~33%). Guía del 29-jul-2026: ventas del 3T26 +3-5% y de 2026 +5,5-6,5% reportadas (+5-6% orgánicas), es decir, ~2-3% en el segundo semestre; el 25-ago-2026 un ciberataque interrumpió la fabricación, el procesamiento de pedidos y los despachos, y el 8-sep la empresa informó que probablemente no cumplirá esa guía, que recuperará parte de las ventas perdidas y que dará una guía nueva el 28-oct-2026.

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 14.240 | 16.747 | 20.074 | 20.996 |
| Crecimiento | +12,3% | +17,6% | +19,9% | — |
| Margen operativo GAAP | 16,5% | 15,5% | 18,0% | 19,8% |
| FCFF (hoja) | 2.166 | 1.947 | 3.775 | — |

**Márgenes.** El margen GAAP subió de 4,9% (2016) a 19,8% LTM, pero sigue cargado por amortización de intangibles (~US$930 millones al año), litigios y reestructuración. La hoja supone 20% el próximo año y 24% de objetivo. Si la empresa deja de comprar, la amortización baja y el margen sube; si compra Penumbra y otras, el GAAP se queda cerca de 20%. Por eso las historias van de 20% a 26%. La tasa efectiva de los años 1-5 es 17,8% (promedio 2023-2025); la del LTM, 5%, refleja beneficios fiscales de una vez. En el 2T26 el margen GAAP fue 21,6% y el ajustado 28,4% (comunicado del 29-jul-2026): la amortización de intangibles resta 4,3 pp y compras, reestructuración y litigios otros ~2,4 pp. El 24% de objetivo supone que la amortización de las compras pasadas pesa menos al crecer las ventas sin compras nuevas y que reestructuraciones y litigios siguen restando ~1,5 pp. El plan de reestructuración de 2026 (8-K del 27-jul-2026) costará US$700-800 millones antes de impuestos hasta 2029 y ahorrará ~US$500 millones al año, en buena parte reinvertidos.

**Reinversión y retorno.** La reinversión es alta: I+D de ~10% de las ventas, capex de US$700-900 millones y compras frecuentes (Axonics, Bolt, Nalu y ahora Penumbra). La hoja usa un ventas/capital de 1,26 (años 1-5) y 1,17 (años 6-10): la Base crece con los segmentos, sin compras; queda entre el de hoy (0,60, con el crédito mercantil) y el del sector (1,48). Con margen objetivo de 24,2% e impuesto marginal de 19%, el capital nuevo rinde ~25% y ~23% (revisión del 5-oct-2026: se quitó el tope de la auditoría del 4-oct, que lo comparaba con un ROIC actual cargado de crédito mercantil). Con Penumbra, el capital invertido sube ~US$14.500 millones: el retorno de esa compra decide si el crecimiento crea valor. El ROIC después del año 10 es igual al costo de capital: incluida la plusvalía de las compras, el ROIC estuvo por debajo del costo de capital hasta 2025, así que no cumple la regla del ROIC terminal (se aplicó 11,1% y se revirtió el 30-sep-2026). Sin ventaja defendible: el crecimiento se compra y el ROIC con la plusvalía de las compras (4-9% en 2021-2025) no superó el costo de capital de forma sostenida. El ROIC después del año 10 es igual al costo de capital, el supuesto por defecto de Damodaran: el crecimiento posterior no suma valor.

**Ventas/capital: las referencias de Damodaran.** Damodaran elige el ventas/capital mirando el de la empresa hoy, el marginal de los últimos años y el promedio del sector, y comprueba que el rendimiento que implica sobre el capital nuevo sea creíble frente a lo que gana la empresa o su sector (Investment Valuation, cap. 11, p. 44-46). El marginal es volátil: recompras de acciones y adquisiciones mueven el capital contable. El usado está dentro del rango de las referencias.

| Referencia | Ventas/capital | Detalle |
|---|---:|---|
| Empresa hoy | 0,60 | ventas LTM 20.996,0 / capital invertido 35.283,4 millones |
| Marginal, último año | 2,01 | Δventas 3.327,0 / Δcapital 1.653,0 millones (Dec '24 → Dec '25) |
| Marginal, últimos tres años | 0,87 | Δventas 7.392,0 / Δcapital 8.462,0 millones (Dec '22 → Dec '25) |
| Sector (Damodaran, enero de 2026) | 1,48 | Healthcare Products |
| Usado en la hoja | 1,26 / 1,17 | años 1-5 / 6-10; rinde ~25% / ~23% sobre el capital nuevo (ROIC actual 9,8%) |

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$519 millones, compromisos del 10-K al 2025-12-31) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$52 millones, +0,25 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,02 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usa una beta de 0,98 (desde el 3-oct-2026; antes 1,00). Regla de la cartera (prompt v4, paso 2): bottom-up de Healthcare Products (Damodaran, ene-2026: 0,86 desapalancada y corregida por caja) reapalancada con la D/E de mercado 0,17 = 0,98 = 0,98. La de regresión queda como referencia. El efecto de cada beta en el DCF Base está en la tabla.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 0,98 | 9,6% | 8,9% | US$35,22 |
| Bottom-up del sector (Healthcare Products, reapalancada) | 0,98 | 9,5% | 8,9% | US$35,25 |


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Sin ventaja defendible | 9,8% | 17,0% | 9,0% | = costo de capital | US$35,22 | US$35,22 |

Fuentes de ventaja: Patentes y relación con médicos, pero el crecimiento se compra. Evidencia: ROIC (con plusvalía) 4-9% en 2021-2025, bajo el costo de capital hasta 2025. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$35,22 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$33,91. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$20.996 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 3.590 + 2.000 + 8.470 + 6.936 = 20.996. |
| Margen inicial del DCF | 20,2% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 17,80% en años 1–5; 19,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 8,91% → 8,99% | Tasa libre de riesgo 5,29%, beta 0,98, ERP 4,35%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 1,26x en años 1–5; 1,17x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 5,29%; Disrupción: 2,76% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (2,76%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Conservadora/Disrupción/Optimista: 8,99% (= WACC terminal) | Criterio de ventaja competitiva (sin ventaja defendible). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 539; deuda 13.137; activos no operativos 2.245; minoritarios 242; acciones 1.449,2 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 3.590 × 1,06 + 2.000 × 1,04 + 8.470 × 1,03 + 6.936 × 1,03 = US$21.830,61 millones. Frente a 20.996, el crecimiento consolidado es 3,98%. En los años 2–5 es 7,62%, 6,83%, 6,17%, 5,86%; las ventas del año 5 son US$28.209,89 millones. El 6,1% de la tabla es el crecimiento anual compuesto de los cinco años: (28.209,89 / 20.996)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 21.830,61 × 20,25% × (1 − 17,80%) = US$3.633,47 millones. La reinversión es US$1.320,39 millones y el FCFF es US$2.313,08 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 8,99%. Reinversión terminal sobre el NOPAT: Base, 58,8% (5,29% / 8,99%); Conservadora, 58,8% (5,29% / 8,99%); Disrupción, 30,7% (2,76% / 8,99%); Optimista, 58,8% (5,29% / 8,99%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · La cartera diversificada sostiene ~7%** — probabilidad 45%; valor terminal 84.888 (VP 36.087); DCF US$35,22 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 21.831 | 4,0% | 20,2% | 3.633 | 1.320 | 2.313 | 8,9% | 2.124 |
| 2 | 23.494 | 7,6% | 21,8% | 4.219 | 1.274 | 2.945 | 8,9% | 2.483 |
| 3 | 25.099 | 6,8% | 22,6% | 4.673 | 1.230 | 3.443 | 8,9% | 2.665 |
| 4 | 26.648 | 6,2% | 23,4% | 5.136 | 1.240 | 3.896 | 8,9% | 2.769 |
| 5 | 28.210 | 5,9% | 24,2% | 5.623 | 1.288 | 4.335 | 8,9% | 2.830 |
| 6 | 29.832 | 5,7% | 24,2% | 5.929 | 1.442 | 4.487 | 8,9% | 2.689 |
| 7 | 31.512 | 5,6% | 24,2% | 6.244 | 1.492 | 4.752 | 8,9% | 2.614 |
| 8 | 33.251 | 5,5% | 24,2% | 6.570 | 1.542 | 5.028 | 9,0% | 2.538 |
| 9 | 35.049 | 5,4% | 24,2% | 6.904 | 1.591 | 5.313 | 9,0% | 2.462 |
| 10 | 36.903 | 5,3% | 24,2% | 7.248 | 1.675 | 5.573 | 9,0% | 2.369 |
| Terminal | 38.855 | 5,3% | 24,2% | 7.631 | 4.491 | 3.141 | 9,0% | — |

**Conservadora · El campo pulsado se vuelve commodity** — probabilidad 30%; valor terminal 67.011 (VP 28.487); DCF US$28,19 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 21.401 | 1,9% | 20,2% | 3.562 | 839 | 2.723 | 8,9% | 2.500 |
| 2 | 22.458 | 4,9% | 21,0% | 3.886 | 743 | 3.142 | 8,9% | 2.649 |
| 3 | 23.395 | 4,2% | 21,4% | 4.125 | 713 | 3.412 | 8,9% | 2.641 |
| 4 | 24.292 | 3,8% | 21,8% | 4.363 | 740 | 3.622 | 8,9% | 2.575 |
| 5 | 25.225 | 3,8% | 22,2% | 4.613 | 827 | 3.786 | 8,9% | 2.471 |
| 6 | 26.266 | 4,1% | 22,2% | 4.790 | 996 | 3.794 | 8,9% | 2.273 |
| 7 | 27.427 | 4,4% | 22,2% | 4.987 | 1.108 | 3.878 | 8,9% | 2.133 |
| 8 | 28.719 | 4,7% | 22,2% | 5.206 | 1.232 | 3.974 | 9,0% | 2.006 |
| 9 | 30.154 | 5,0% | 22,2% | 5.450 | 1.369 | 4.081 | 9,0% | 1.891 |
| 10 | 31.750 | 5,3% | 22,2% | 5.722 | 1.441 | 4.280 | 9,0% | 1.820 |
| Terminal | 33.429 | 5,3% | 22,2% | 6.024 | 3.545 | 2.479 | 9,0% | — |

**Disrupción · Deterioro de los fundamentales: Pierde participación y precio** — probabilidad 5%; valor terminal 49.254 (VP 20.938); DCF US$21,86 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 20.823 | −0,8% | 20,2% | 3.466 | 292 | 3.174 | 8,9% | 2.914 |
| 2 | 21.191 | 1,8% | 20,2% | 3.527 | 413 | 3.114 | 8,9% | 2.626 |
| 3 | 21.711 | 2,5% | 20,2% | 3.613 | 476 | 3.138 | 8,9% | 2.429 |
| 4 | 22.310 | 2,8% | 20,2% | 3.713 | 489 | 3.224 | 8,9% | 2.292 |
| 5 | 22.926 | 2,8% | 20,2% | 3.816 | 503 | 3.313 | 8,9% | 2.163 |
| 6 | 23.559 | 2,8% | 20,2% | 3.910 | 558 | 3.351 | 8,9% | 2.008 |
| 7 | 24.210 | 2,8% | 20,2% | 4.006 | 574 | 3.432 | 8,9% | 1.888 |
| 8 | 24.879 | 2,8% | 20,2% | 4.105 | 590 | 3.515 | 9,0% | 1.775 |
| 9 | 25.566 | 2,8% | 20,2% | 4.205 | 606 | 3.600 | 9,0% | 1.668 |
| 10 | 26.272 | 2,8% | 20,2% | 4.309 | 623 | 3.686 | 9,0% | 1.567 |
| Terminal | 26.998 | 2,8% | 20,2% | 4.428 | 1.360 | 3.067 | 9,0% | — |

**Optimista · Electrofisiología y Watchman vuelven a doble dígito** — probabilidad 20%; valor terminal 102.889 (VP 43.739); DCF US$42,59 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 22.228 | 5,9% | 20,2% | 3.700 | 1.896 | 1.803 | 8,9% | 1.656 |
| 2 | 24.617 | 10,7% | 22,6% | 4.583 | 1.626 | 2.957 | 8,9% | 2.493 |
| 3 | 26.665 | 8,3% | 23,8% | 5.227 | 1.609 | 3.618 | 8,9% | 2.801 |
| 4 | 28.691 | 7,6% | 25,0% | 5.907 | 1.651 | 4.256 | 8,9% | 3.026 |
| 5 | 30.771 | 7,2% | 26,2% | 6.639 | 1.675 | 4.964 | 8,9% | 3.240 |
| 6 | 32.882 | 6,9% | 26,2% | 7.074 | 1.824 | 5.250 | 8,9% | 3.146 |
| 7 | 35.008 | 6,5% | 26,2% | 7.509 | 1.825 | 5.685 | 8,9% | 3.127 |
| 8 | 37.134 | 6,1% | 26,2% | 7.942 | 1.810 | 6.131 | 9,0% | 3.096 |
| 9 | 39.244 | 5,7% | 26,2% | 8.368 | 1.781 | 6.587 | 9,0% | 3.052 |
| 10 | 41.320 | 5,3% | 26,2% | 8.785 | 1.876 | 6.909 | 9,0% | 2.937 |
| Terminal | 43.506 | 5,3% | 26,2% | 9.250 | 5.443 | 3.807 | 9,0% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 25.544,03 | 36.086,95 | 61.630,97 | 51.035,54 | 35,22 |
| Conservadora | 22.961,59 | 28.486,96 | 51.448,55 | 40.853,11 | 28,19 |
| Disrupción | 21.329,78 | 20.938,31 | 42.268,10 | 31.672,66 | 21,86 |
| Optimista | 28.573,99 | 43.739,50 | 72.313,49 | 61.718,06 | 42,59 |

Ejemplo Base: (25.544,03 + 36.086,95 + 539 + 2.245 − 13.137 − 242) / 1.449,2 = US$35,22 por acción. El terminal representa 58,6% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 45% / 30% / 5% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,45 × 35,216352 + 0,30 × 28,190114 + 0,05 × 21,855272 + 0,20 × 42,587673 = US$33,914691 ≈ US$33,91. Los aportes son US$15,85 + US$8,46 + US$1,09 + US$8,52 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 33,914691 × 0,65 = US$22,044549 ≈ US$22,04. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$35,22, es el valor intrínseco principal. El DCF esperado de US$33,91 combina las cuatro tesis con sus probabilidades y se presenta como complemento. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: La cartera diversificada sostiene ~7%

**Qué plantea.** Es lo que muestra el 2T26: orgánico de 7% con Electrofisiología desacelerando pero todavía creciendo.

**Traducción al modelo.** Electrofisiología crece 6%, 11%, 9%, 8%, 8%; Watchman crece 4%, 10%, 9%, 8%, 8%; Resto de Cardiovascular crece 4%, 6%, 6%, 5%, 5%; MedSurg crece 4%, 6%, 6%, 6%, 5%. El crecimiento anual compuesto de cinco años es 6,1%; el margen operativo objetivo es 24,2%. El ROIC terminal es el costo de capital (8,99%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 45%; DCF: US$35,22 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (crecimiento orgánico total: 7,0% (2T26); recuperación tras el ciberataque: Fabricación y despachos casi normales (8-sep-2026); electrofisiología EE.UU.: +3% (2T26)). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: El campo pulsado se vuelve commodity

**Qué plantea.** Es el riesgo real: tres competidores en campo pulsado bajan precio y participación en EE.UU.

**Traducción al modelo.** Electrofisiología crece 0%, 3%, 3%, 3%, 3%; Watchman crece 1%, 4%, 4%, 4%, 4%; Resto de Cardiovascular crece 2%, 6%, 4%, 4%, 4%; MedSurg crece 2%, 6%, 5%, 4%, 4%. El crecimiento anual compuesto de cinco años es 3,7%; el margen operativo objetivo es 22,2%. El ROIC terminal es el costo de capital (8,99%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 30%; DCF: US$28,19 por acción.

**Cómo contrastarla.** La apoyarían: crecimiento orgánico total: < 5% dos trimestres; recuperación tras el ciberataque: pérdida de clientes o multas; electrofisiología EE.UU.: ≤ 0%; watchman EE.UU.: ≤ 0%.


#### Disrupción · Deterioro de los fundamentales: Pierde participación y precio

**Qué plantea.** Es un tropiezo clínico o de producto.

**Traducción al modelo.** Electrofisiología crece -8%, -3%, 0%, 2%, 2%; Watchman crece -2%, 0%, 2%, 2%, 2%; Resto de Cardiovascular crece 1%, 3%, 3%, 3%, 3%; MedSurg crece 1%, 3%, 3%, 3%, 3%. El crecimiento anual compuesto de cinco años es 1,8%; el margen operativo objetivo es 20,2%. El ROIC terminal es el costo de capital (8,99%). El crecimiento terminal es 2,76%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 5%; DCF: US$21,86 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: crecimiento orgánico total: < 5% dos trimestres; recuperación tras el ciberataque: pérdida de clientes o multas; electrofisiología EE.UU.: ≤ 0%; watchman EE.UU.: ≤ 0%.


#### Optimista: Electrofisiología y Watchman vuelven a doble dígito

**Qué plantea.** Supone que la caída de 2026 fue un ajuste temporal (inventario, adopción de nuevos catéteres).

**Traducción al modelo.** Electrofisiología crece 10%, 17%, 13%, 12%, 10%; Watchman crece 9%, 16%, 12%, 10%, 10%; Resto de Cardiovascular crece 4%, 8%, 7%, 6%, 6%; MedSurg crece 4%, 8%, 6%, 6%, 6%. El crecimiento anual compuesto de cinco años es 7,9%; el margen operativo objetivo es 26,2%. El ROIC terminal es el costo de capital (8,99%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 20%; DCF: US$42,59 por acción.

**Cómo contrastarla.** La confirmarían: crecimiento orgánico total: ≥ 7%; recuperación tras el ciberataque: ventas del 4T26 ≥ +5% y guía 2027 sin recortes; electrofisiología EE.UU.: ≥ +8% en 2027; watchman EE.UU.: ≥ +8%.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 5,29%; Disrupción: 2,76%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | Crecimiento terminal | Valor/acción (beta 0,98) |
|---|---:|---|---:|---:|---:|---:|---:|
| **Base · La cartera diversificada sostiene ~7%** | 45% | Electrofisiología: 6%, 11%, 9%, 8%, 8%; Watchman: 4%, 10%, 9%, 8%, 8%; Resto de Cardiovascular: 4%, 6%, 6%, 5%, 5%; MedSurg: 4%, 6%, 6%, 6%, 5% | 6,1% | 24,2% | 1,3 | 5,29% | US$35,22 |
| **Conservadora · El campo pulsado se vuelve commodity** | 30% | Electrofisiología: 0%, 3%, 3%, 3%, 3%; Watchman: 1%, 4%, 4%, 4%, 4%; Resto de Cardiovascular: 2%, 6%, 4%, 4%, 4%; MedSurg: 2%, 6%, 5%, 4%, 4% | 3,7% | 22,2% | 1,3 | 5,29% | US$28,19 |
| **Disrupción · Deterioro de los fundamentales: Pierde participación y precio** | 5% | Electrofisiología: -8%, -3%, 0%, 2%, 2%; Watchman: -2%, 0%, 2%, 2%, 2%; Resto de Cardiovascular: 1%, 3%, 3%, 3%, 3%; MedSurg: 1%, 3%, 3%, 3%, 3% | 1,8% | 20,2% | 1,3 | 2,76% | US$21,86 |
| **Optimista · Electrofisiología y Watchman vuelven a doble dígito** | 20% | Electrofisiología: 10%, 17%, 13%, 12%, 10%; Watchman: 9%, 16%, 12%, 10%, 10%; Resto de Cardiovascular: 4%, 8%, 7%, 6%, 6%; MedSurg: 4%, 8%, 6%, 6%, 6% | 7,9% | 26,2% | 1,3 | 5,29% | US$42,59 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  | **US$33,91** |

Base (45%) es lo que muestra el 2T26: orgánico de 7% con Electrofisiología desacelerando pero todavía creciendo. Conservadora (30%) es el riesgo real: tres competidores en campo pulsado bajan precio y participación en EE.UU. Disrupción (5%) es un tropiezo clínico o de producto. Optimista (20%) supone que la caída de 2026 fue un ajuste temporal (inventario, adopción de nuevos catéteres). En las historias de erosión (Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 0,98; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.

| Crecimiento \ Margen | 20,2% | 22,2% | 24,2% | 26,2% | 28,2% |
|---|---:|---:|---:|---:|---:|
| 2,1% | 23,30 | 26,14 | 28,97 | 31,80 | 34,64 |
| 4,1% | 25,71 | 28,91 | 32,12 | 35,32 | 38,52 |
| 6,1% | 28,36 | 31,98 | 35,59 | 39,20 | 42,82 |
| 8,1% | 31,28 | 35,35 | 39,42 | 43,49 | 47,56 |
| 10,1% | 34,48 | 39,06 | 43,64 | 48,22 | 52,80 |


### Pre-mortem

1. Medtronic y Johnson & Johnson ganan participación en campo pulsado y Electrofisiología en EE.UU. crece a un dígito bajo por años.
2. Watchman pierde frente a nuevos anticoagulantes o por evidencia clínica comparativa desfavorable.
3. Penumbra se paga caro, genera deterioro de goodwill y la deuda limita la flexibilidad.
4. La demanda colectiva por la guía de Electrofisiología revela problemas de gestión o de transparencia.
5. Presión de precios en ICVT y reembolsos de Medicare más bajos reducen el margen.
6. El ciberataque deja pérdidas permanentes de participación con hospitales, multas o costos de remediación mayores que los previstos.

**Evidencia en contra de la historia más probable:** el freno en EE.UU. fue brusco (de doble dígito alto a +3% en un trimestre) y coincidió con la llegada de competencia directa. Si el 3T y el 4T repiten ~3% en EE.UU., la historia Conservadora debe pesar más que Base.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Crecimiento orgánico total | 7,0% (2T26) | ≥ 7% | < 5% dos trimestres |
| Recuperación tras el ciberataque | Fabricación y despachos casi normales (8-sep-2026) | Ventas del 4T26 ≥ +5% y guía 2027 sin recortes | Pérdida de clientes o multas |
| Electrofisiología EE.UU. | +3% (2T26) | ≥ +8% en 2027 | ≤ 0% |
| Watchman EE.UU. | +3% (2T26) | ≥ +8% | ≤ 0% |
| Margen operativo GAAP | 19,8% LTM | ≥ 21% en 2027 | ≤ 18% |
| Penumbra (antimonopolio y retorno) | Pendiente | Cierre y crecimiento de trombectomía ≥ 15% | Remedios o deterioro |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$43,65**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 22% | Margen 24% | Margen 26% |
|---|---:|---:|---:|
| Beta 0,98 | 12,3% (16% de las empresas) | 10,1% (25% de las empresas) | 8,2% (33% de las empresas) |

Frente al DCF Base (US$35,22), el valor intrínseco principal, el precio está por encima en 24%.

Frente al DCF esperado de las historias (US$33,91), el complemento, el precio está por encima en 29%. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Cartera cardiovascular diversificada que pierde su ciclo de producto excepcional |  |
| Probabilidades | Base 45% / Conservadora 30% / Disrupción 5% / Optimista 20% |  |
| DCF Base hoy (valor intrínseco principal) | US$35,22 |  |
| DCF esperado por probabilidades (complemento) | US$33,91 |  |
| Precio con MOS sobre el DCF esperado | US$22,04 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$21,86 a US$42,63 |  |
| Confianza | Media: la diversificación da piso; la duración de la competencia en campo pulsado es incierta |  |
| Qué cambiaría la opinión | Electrofisiología y Watchman en EE.UU. en los próximos dos trimestres; recuperación tras el ciberataque; cierre y precio de Penumbra |  |
| Revisión | Resultados del 3T26 y guía nueva (28-oct-2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [Boston Scientific, comunicado de resultados del 2T 2026 (29-jul-2026)](https://www.sec.gov/Archives/edgar/data/885725/000088572526000051/q22026earningsrelease.htm)
- [Boston Scientific, 8-K del 26-ago-2026 (ciberataque)](https://www.sec.gov/Archives/edgar/data/885725/000088572526000056/bsx-20260826.htm)
- [Boston Scientific, 8-K del 8-sep-2026 (efecto material en 2026)](https://www.sec.gov/Archives/edgar/data/885725/000088572526000059/bsx-20260907.htm)
- [Boston Scientific, 8-K del 27-jul-2026 (plan de reestructuración de 2026)](https://www.sec.gov/Archives/edgar/data/885725/000088572526000049/bsx-20260721.htm)
- [Boston Scientific, Form 10-Q del 2T 2026](https://www.sec.gov/Archives/edgar/data/885725/000088572526000053/bsx-20260630.htm)
- [Boston Scientific, Form 10-Q del 1T 2026](https://www.sec.gov/Archives/edgar/data/885725/000088572526000033/bsx-20260331.htm)
- [Boston Scientific, Form 10-K 2025](https://www.sec.gov/Archives/edgar/data/885725/000088572526000010/bsx-20251231.htm)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
