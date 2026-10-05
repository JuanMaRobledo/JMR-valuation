---
schema: "jmr-analisis-damodaran-v1"
ticker: "AFYA"
analysis_date: "2026-09-30"
---

# Afya Limited (AFYA) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$24,38 por acción** (Base · La escasez de plazas sostiene precio y margen).

**Complemento · DCF esperado por probabilidades: US$21,39.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$11,82–28,26. El MOS 35% se aplica al esperado: US$13,90. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: capital invertido operativo, flujos ltm, roic terminal (criterio damodaran) (4 celdas, con respaldo). DCF esperado US$22,83 → US$21,39. Salvedades abiertas: Arrendamientos: bajo NIIF 16 todos los arrendamientos están en el balance y el EBIT ya excluye su costo financiero, así que su pasivo es deuda; se conserva en la deuda del DCF. Emisor extranjero (NIIF) sin XBRL trimestral en la SEC: flujos LTM y EPS no se contrastaron de forma automática; el balance se revisó con el informe semestral. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (bloque Base de 'Valuation output': US$24,38 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja calcula estos cuatro DCF en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

Afya es el mayor grupo de educación médica de Brasil. Su negocio es la escasez: el Ministerio de Educación limita las plazas de Medicina, y cada plaza autorizada es un flujo de matrículas de seis años con precio alto y demanda que excede la oferta. Por eso el grado en Medicina es ~88% de los ingresos y sostiene márgenes EBIT de ~32%. La educación continua y las soluciones digitales para médicos son pequeñas y crecen poco. En el 1S26 los ingresos crecieron ~7% en reales, en el rango bajo de la guía (7-11%), y el EBITDA ajustado perdió 190 pb por un ciclo de inversión. Sobre todo esto cae la fusión anunciada con Yduqs (sep-2026), que cambia la historia si se cierra: esta sección valora a Afya sola (standalone), que es lo que vuelve a mandar si CADE o las asambleas la frenan.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~6% anual en dólares cinco años | Sí | Sí: +7,8% en 2025 y ~+7% en reales en el 1S26; el real puede restar | Probable en reales; incierto en dólares |
| El margen EBIT se mantiene en ~33% | Sí | Sí: 30,6% (2024) → 32,8% (2025); el 1S26 muestra compresión por inversión | Probable |
| La regulación libera muchas plazas nuevas de Medicina | Sí | Poco: el programa Mais Médicos ya abrió plazas y la política se endureció | Baja |
| La fusión con Yduqs se cierra sin condiciones severas | Sí | Sí, pero 17% del mercado de escuelas médicas atrae a CADE | Incierto |


### Visión externa: tasas base

Con ventas LTM de US$723 millones (US$512 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **$325-700 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 9,2% y una mediana de 7,3% (desviación estándar 10,8%); sumando una inflación de 2,5%, la mediana nominal ronda 9,8%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · La escasez de plazas sostiene precio y margen | 5,8% | 66% |
| Conservadora · Madurez: precio real plano | 3,5% | 77% |
| Disrupción · Deterioro de los fundamentales: Se liberan plazas y cae el precio | 0,3% | 85% |
| Optimista · Maduran los campus y crece lo digital | 7,4% | 59% |

En dólares de 2015 la empresa está en el tramo de US$325-700 millones: crecer 5,8% anual cinco años (Base) lo logró ~66% de las empresas de ese tamaño; 7,4% (Optimista), ~59%. La hoja no pide nada extraordinario. El riesgo no está en el crecimiento sino en el país (real, tasas, política educativa), que ya entra por el costo del patrimonio de ~14%.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: una escasez regulada, no una apuesta de expansión.** Afya vive de que el Ministerio de Educación limita las plazas de Medicina en Brasil: cada plaza autorizada es una matrícula de seis años con precio alto y más demanda que oferta, y el grado en Medicina explica ~88% de los ingresos. Por eso la Base no supone un salto, sino que el negocio siga como en 2024-2026: el grado crece 7% el primer año y baja a 5% en el quinto, la educación continua de 6% a 5% y las soluciones digitales para médicos entre 5% y 8%. El resultado es 6,8% el primer año y 5,8% anual compuesto en cinco años. La evidencia está en el 1S26 (6-K): grado +7% y Medicina +6,5% en reales, en el piso de la guía de 7-11%. Elegimos el piso y no el centro de la guía porque el primer semestre ya mostró que el rango alto no se está cumpliendo; tampoco extrapolamos el +27,6% de 2023, que fue comprado. La visión externa respalda que no es una cifra heroica: ~66% de las empresas de su tamaño crecieron al menos eso en cinco años. La Conservadora (3,5%) supone que el precio real de la matrícula deja de subir; la Disrupción (0,3%) que el gobierno abre plazas y el precio cae; la Optimista (7,4%) que los campus nuevos maduran y lo digital despega. Si en 2027 el grado en Medicina crece 4% o menos en reales, la Base pierde sustento. Un punto que esta valoración deja fuera a propósito: la fusión anunciada con Yduqs (sep-2026). Se valora Afya sola, que es lo que vuelve a importar si CADE o las asambleas la frenan.

**Margen: el nivel de hoy, no uno mejor.** El margen EBIT subió de 26,7% a 32,8% en dos años porque las plazas compradas maduraron: una plaza nueva tiene pocos alumnos los primeros años y los costos del campus ya están. La Base usa 33,0% de objetivo, prácticamente el margen actual; no supone una mejora adicional porque la mezcla empuja en contra (educación continua y digital, que crecen más, tienen menos margen) y porque el 1S26 trajo 190 pb menos de EBITDA ajustado por inversión en producto. Si esa compresión fuera permanente, la Conservadora (30,0%) se vuelve más probable; la Disrupción (26,0%) es la caída de precio que traería una apertura masiva de plazas, y la Optimista (35,0%) los campus maduros sin la presión de mezcla. Restar dos puntos al margen objetivo lleva la Base a US$22,70 (−7%).

**Reinversión y retorno: crecer con las plazas que ya tiene cuesta poco capital.** Afya creció comprando escuelas y plazas de Medicina: por eso hoy vende solo ~0,5 veces su capital, que incluye el sobreprecio de esas compras. La Base no supone compras nuevas: crece con plazas ya autorizadas que maduran, la educación continua y las soluciones digitales, y ese crecimiento orgánico pide poco capital (el capex, de US$49-73 millones al año, apenas supera la depreciación y amortización, que incluye la de intangibles comprados). La hoja usa un ventas/capital de 1,50× en los años 1–5: con él, el flujo libre del primer año coincide con el real de los últimos doce meses, así que la reinversión del modelo es la que Afya hace hoy; cada dólar de ventas nuevas exige ~US$0,67 y el capital nuevo rinde ~33% (con la tasa marginal de 34%), más que el ROIC actual, que paga el sobreprecio de las compras. En los años 6–10 usa 1,20×, cerca del sector educación en la tabla global (1,16), porque crecer exigirá plazas nuevas. Si Afya vuelve a comprar plazas, hay que sumar a la vez los ingresos y el precio de la compra. Después del año 10 la Base conserva un ROIC de 14,8%: las licencias de Medicina son una barrera real (el regulador decide cuántas plazas hay), y el ROIC ha estado en 12-16% desde 2022. Si el ROIC terminal fuera igual al costo de capital —lo que pasaría si se liberan plazas— la Base caería a US$21,33 (−12%). Un ventas/capital 20% menor la deja en US$23,72 (−3%).

**Descuento: el riesgo es Brasil, y ya está en la tasa.** El costo de capital empieza en 9,88% y termina en 10,72%. Es alto porque incluye la prima de riesgo país de Brasil: tasa libre de riesgo 5,29%, beta 1,13 y prima de riesgo 6,94%. La beta bottom-up del sector educación reapalancada con la deuda de Afya da 1,09, casi igual, así que la tasa no es el punto débil. Lo que no hacemos es contar el riesgo dos veces: si el real se deprecia o cambian las tasas, eso ya está en el costo de capital, y las historias no recortan además los flujos por el mismo motivo. Un punto más de tasa lleva la Base a US$20,43 (−16%); un punto menos, a US$30,01 (+23%). El crecimiento perpetuo es 5,29%, igual a la tasa libre de riesgo de la hoja, y el valor terminal explica 48,5% del valor operativo de la Base.

**Probabilidades y lectura del resultado.** La Base pesa 45% porque es la continuación de lo que se ve; la Conservadora 30% porque el precio real de la matrícula no puede subir para siempre y el 1S26 ya estuvo en el piso de la guía; la Disrupción 15% es el riesgo regulatorio, poco probable pero el único que rompe la tesis; la Optimista 10% exige que la madurez de los campus y lo digital aceleren. El DCF Base es US$24,38 y el esperado US$21,39; la diferencia entre ambos mide cuánto pesan los desenlaces malos. Las acciones se mantienen en 88,9 millones en todas las historias. La salvedad mayor no está en el modelo sino fuera de él: si la fusión con Yduqs se cierra, el valor relevante pasa a ser el del canje, y esta valoración standalone deja de ser la referencia.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$723 millones. Con el crecimiento de la Base llegan a US$960 millones en el año 5 y a US$1.237 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 31,5% en el año 1 a 33,0% al final, y se descuentan impuestos (10,6% al principio y 34,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$218 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$31 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$186 millones el primer año. Cada flujo se trae a hoy con el costo de capital (9,88% al principio, 10,72% al final): los diez años suman US$1.361 millones. Después del año 10 se supone que la empresa crece 5,29% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 14,8%; esa perpetuidad vale hoy US$1.279 millones, 48% del total. Flujos más terminal dan el valor de las operaciones, US$2.640 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$194 millones, más activos no operativos por US$11 millones, menos deuda por US$670 millones, menos minoritarios por US$8 millones. Queda un patrimonio de US$2.167 millones que, repartido entre 88,9 millones de acciones, da US$24,38 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 7,71× (peso 33% dentro de los múltiplos); EV/FCFF 11,30× (peso 17% dentro de los múltiplos); P/E 8,96× (peso 33% dentro de los múltiplos); P/FCFE 9,17× (peso 8% dentro de los múltiplos); P/OCF 6,56× (peso 8% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (13,1%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$24,38; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$22,70 | −6,9% |
| Margen objetivo +2 pp | US$26,05 | +6,9% |
| Crecimiento años 1–5 −2 pp | US$21,92 | −10,1% |
| Crecimiento años 1–5 +2 pp | US$27,08 | +11,1% |
| Ventas/capital −20% | US$23,72 | −2,7% |
| Ventas/capital +20% | US$24,81 | +1,8% |
| WACC +1 pp | US$20,43 | −16,2% |
| WACC −1 pp | US$30,01 | +23,1% |
| Crecimiento terminal −0,5 pp | US$23,65 | −3,0% |
| Crecimiento terminal +0,5 pp | US$25,23 | +3,5% |
| ROIC terminal = costo de capital | US$21,33 | −12,5% |
| Acciones +5% | US$23,21 | −4,8% |


### Piezas del valor

**Crecimiento.** Ingresos de US$575,9 millones (2023, +27,6% por compras), US$613,9 millones (2024, +6,6%) y US$661,7 millones (2025, +7,8%); LTM US$723,1 millones. En el 1S26 (reales): grado R$1.762 millones (+7%), Medicina R$1.499 millones (+6,5%), educación continua R$143,9 millones (+4,6%) y soluciones para la práctica médica R$85,3 millones (+1,5%). La división LTM en dólares de las historias usa ese peso del 1S26 (≈88% / 7% / 4%).

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 575,9 | 613,9 | 661,7 | 723,1 |
| Crecimiento | +27,6% | +6,6% | +7,8% | — |
| Margen EBIT | 26,7% | 30,6% | 32,8% | 32,6% |
| FCFF (hoja) | 135,4 | 181,3 | 187,5 | — |

**Márgenes.** El margen EBIT subió de 26,7% a 32,8% en dos años al madurar las plazas compradas. La hoja supone 31,5% el próximo año y 33% de objetivo, prácticamente el nivel actual. El piso lo pone la mezcla: más peso de educación continua y digital (menor margen) y la inversión en producto del 2026. Las historias van de 26% (caída de precio) a 35% (campus maduros). Impuestos: la tasa efectiva de ~11% (beneficio de ProUni) se mantiene en los años 1-5 y converge en los años 6-10 a la tasa legal de 34% (IRPJ y CSLL), que es la que rige a perpetuidad: Damodaran (Investment Valuation cap. 10, p. 4) advierte que los beneficios fiscales rara vez son perpetuos. Si ProUni se renovara indefinidamente, el valor subiría ~20%.

**Reinversión y retorno.** Crecer exige capital: campus, hospitales-escuela y compras de plazas (con earn-outs). El capex fue US$49-73 millones al año (~10% de las ventas) y sus ventas son solo ~0,5 veces su capital invertido, porque crece comprando plazas (intangibles de US$1.076 millones). La hoja usa un ventas/capital de 0,75 (años 1-5) y 0,75 (años 6-10): con margen objetivo de 33,0% e impuesto marginal de 34%, cada dólar de capital nuevo rinde ~16% y ~16%, sin superar el mayor entre su ROIC actual (14,9%) y el de su industria (15,9%) (Damodaran, Investment Valuation cap. 11, p. 45; revisión del 4-oct-2026). Antes 0,75 y 0,75, que implicaban ~16% y ~16% sobre el capital nuevo. El valor anterior (1,5 y 1,2) implicaba ~42% sobre el capital nuevo, incoherente con el ROIC de 14,8% del valor terminal (revisión del 4-oct-2026). Si el crecimiento viene de comprar plazas, cada punto cuesta más. Ventaja durable: licencias reguladas de Medicina con plazas limitadas, con ROIC por encima del costo de capital desde 2022 (12-16%). El ROIC después del año 10 es 14,8%, el promedio de su industria según Damodaran (15,9%), limitado a su ROIC actual. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Ventas/capital: las referencias de Damodaran.** Damodaran elige el ventas/capital mirando el de la empresa hoy, el marginal de los últimos años y el promedio del sector, y comprueba que el rendimiento que implica sobre el capital nuevo sea creíble frente a lo que gana la empresa o su sector (Investment Valuation, cap. 11, p. 44-46). El marginal es volátil: recompras de acciones y adquisiciones mueven el capital contable. El usado está dentro del rango de las referencias.

| Referencia | Ventas/capital | Detalle |
|---|---:|---|
| Empresa hoy | 0,51 | ventas LTM 723,1 / capital invertido 1.416,2 millones |
| Marginal, último año | 0,25 | Δventas 47,8 / Δcapital 188,4 millones (Dec '24 → Dec '25) |
| Marginal, últimos tres años | 0,64 | Δventas 210,5 / Δcapital 329,5 millones (Dec '22 → Dec '25) |
| Sector (Damodaran, enero de 2026) | 1,63 | Education |
| Usado en la hoja | 1,50 / 1,20 | años 1-5 / 6-10; rinde ~33% / ~26% sobre el capital nuevo (ROIC actual 14,9%) |

**Riesgo.** La hoja usa la beta bottom-up de Education en la tabla global de Damodaran (281 empresas, ene-2026: 0,74 desapalancada y corregida por caja), reapalancada por la hoja con la deuda de Afya (42% de la estructura, arrendamientos incluidos): ~1,10. Tabla global porque Afya vende 100% en Brasil; el riesgo de Brasil va en la prima de mercado (7,33%). La regresión semanal contra el S&P 500 da 0,44 a dos años y 0,72 a cinco y queda como referencia. El riesgo relevante es el país y la moneda, y ya está en la tasa; no conviene sumarlo otra vez recortando los flujos.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,13 | 13,1% | 9,9% | US$24,38 |
| Bottom-up del sector (Education, reapalancada) | 1,09 | 12,9% | 9,7% | US$24,60 |


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 14,9% | 15,9% | 11,1% | 14,8% | US$24,38 | US$21,33 |

Fuentes de ventaja: Licencias reguladas de Medicina (plazas limitadas). Evidencia: ROIC 12-16%, apenas 1-5 pp sobre el costo de capital desde 2022. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$24,38 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$21,39. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$723 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 640 + 52 + 31 = 723. |
| Margen inicial del DCF | 31,5% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 10,61% en años 1–5; 34,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 9,88% → 10,72% | Tasa libre de riesgo 5,29%, beta 1,13, ERP 6,94%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 1,50x en años 1–5; 1,20x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 5,29%; Disrupción: 0,89% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (0,89%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Conservadora/Optimista: 14,80%; Disrupción: 10,72% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 194; deuda 670; activos no operativos 11; minoritarios 8; acciones 88,9 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 640 × 1,07 + 52 × 1,06 + 31 × 1,05 = US$772,58 millones. Frente a 723, el crecimiento consolidado es 6,84%. En los años 2–5 es 6,08%, 6,01%, 5,13%, 5,09%; las ventas del año 5 son US$959,95 millones. El 5,8% de la tabla es el crecimiento anual compuesto de los cinco años: (959,95 / 723)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 772,58 × 31,50% × (1 − 10,61%) = US$217,54 millones. La reinversión es US$31,34 millones y el FCFF es US$186,20 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 10,72%. Reinversión terminal sobre el NOPAT: Base, 35,7% (5,29% / 14,80%); Conservadora, 35,7% (5,29% / 14,80%); Disrupción, 8,3% (0,89% / 10,72%); Optimista, 35,7% (5,29% / 14,80%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · La escasez de plazas sostiene precio y margen** — probabilidad 45%; valor terminal 3.358,1 (VP 1.279,1); DCF US$24,38 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 772,6 | 6,8% | 31,5% | 217,5 | 31,3 | 186,2 | 9,9% | 169,5 |
| 2 | 819,6 | 6,1% | 32,1% | 235,2 | 32,9 | 202,3 | 9,9% | 167,6 |
| 3 | 868,9 | 6,0% | 32,4% | 251,6 | 29,7 | 221,9 | 9,9% | 167,3 |
| 4 | 913,5 | 5,1% | 32,7% | 267,0 | 31,0 | 236,0 | 9,9% | 161,9 |
| 5 | 960,0 | 5,1% | 33,0% | 283,2 | 32,8 | 250,3 | 9,9% | 156,3 |
| 6 | 1.009,2 | 5,1% | 33,0% | 282,1 | 43,5 | 238,6 | 10,1% | 135,4 |
| 7 | 1.061,4 | 5,2% | 33,0% | 280,3 | 46,1 | 234,2 | 10,2% | 120,6 |
| 8 | 1.116,7 | 5,2% | 33,0% | 277,7 | 48,9 | 228,8 | 10,4% | 106,7 |
| 9 | 1.175,3 | 5,2% | 33,0% | 274,1 | 51,8 | 222,3 | 10,6% | 93,8 |
| 10 | 1.237,5 | 5,3% | 33,0% | 269,5 | 54,6 | 215,0 | 10,7% | 81,9 |
| Terminal | 1.302,9 | 5,3% | 33,0% | 283,8 | 101,4 | 182,3 | 10,7% | — |

**Conservadora · Madurez: precio real plano** — probabilidad 30%; valor terminal 2.620,6 (VP 998,2); DCF US$19,40 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 757,3 | 4,7% | 31,5% | 213,2 | 19,4 | 193,8 | 9,9% | 176,4 |
| 2 | 786,4 | 3,8% | 30,9% | 217,2 | 15,5 | 201,7 | 9,9% | 167,1 |
| 3 | 809,7 | 3,0% | 30,6% | 221,5 | 16,0 | 205,5 | 9,9% | 154,9 |
| 4 | 833,6 | 3,0% | 30,3% | 225,8 | 16,4 | 209,3 | 9,9% | 143,6 |
| 5 | 858,3 | 3,0% | 30,0% | 230,2 | 19,6 | 210,6 | 9,9% | 131,4 |
| 6 | 887,7 | 3,4% | 30,0% | 225,6 | 28,8 | 196,8 | 10,1% | 111,6 |
| 7 | 922,3 | 3,9% | 30,0% | 221,4 | 33,5 | 187,9 | 10,2% | 96,7 |
| 8 | 962,5 | 4,4% | 30,0% | 217,6 | 38,7 | 178,9 | 10,4% | 83,4 |
| 9 | 1.008,9 | 4,8% | 30,0% | 213,9 | 44,5 | 169,4 | 10,6% | 71,5 |
| 10 | 1.062,3 | 5,3% | 30,0% | 210,3 | 46,8 | 163,5 | 10,7% | 62,3 |
| Terminal | 1.118,4 | 5,3% | 30,0% | 221,5 | 79,2 | 142,3 | 10,7% | — |

**Disrupción · Deterioro de los fundamentales: Se liberan plazas y cae el precio** — probabilidad 15%; valor terminal 1.241,9 (VP 473,0); DCF US$11,82 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 735,9 | 1,8% | 31,5% | 207,2 | 0,0 | 207,2 | 9,9% | 188,6 |
| 2 | 735,9 | 0,0% | 29,3% | 192,7 | -4,4 | 197,1 | 9,9% | 163,2 |
| 3 | 729,4 | −0,9% | 28,2% | 183,9 | 0,0 | 183,9 | 9,9% | 138,6 |
| 4 | 729,4 | 0,0% | 27,1% | 176,7 | 4,3 | 172,4 | 9,9% | 118,2 |
| 5 | 735,8 | 0,9% | 26,0% | 171,0 | 4,3 | 166,7 | 9,9% | 104,0 |
| 6 | 742,4 | 0,9% | 26,0% | 163,5 | 5,5 | 158,0 | 10,1% | 89,6 |
| 7 | 748,9 | 0,9% | 26,0% | 155,8 | 5,5 | 150,3 | 10,2% | 77,4 |
| 8 | 755,6 | 0,9% | 26,0% | 148,0 | 5,6 | 142,5 | 10,4% | 66,4 |
| 9 | 762,3 | 0,9% | 26,0% | 140,1 | 5,6 | 134,4 | 10,6% | 56,7 |
| 10 | 769,0 | 0,9% | 26,0% | 132,0 | 5,7 | 126,3 | 10,7% | 48,1 |
| Terminal | 775,8 | 0,9% | 26,0% | 133,1 | 11,0 | 122,1 | 10,7% | — |

**Optimista · Maduran los campus y crece lo digital** — probabilidad 10%; valor terminal 3.917,9 (VP 1.492,3); DCF US$28,26 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 788,6 | 9,1% | 31,5% | 222,0 | 43,0 | 179,1 | 9,9% | 163,0 |
| 2 | 853,1 | 8,2% | 32,9% | 250,9 | 41,0 | 209,9 | 9,9% | 173,8 |
| 3 | 914,6 | 7,2% | 33,6% | 274,7 | 38,6 | 236,1 | 9,9% | 177,9 |
| 4 | 972,4 | 6,3% | 34,3% | 298,2 | 40,5 | 257,7 | 9,9% | 176,8 |
| 5 | 1.033,2 | 6,2% | 35,0% | 323,2 | 41,7 | 281,6 | 9,9% | 175,8 |
| 6 | 1.095,7 | 6,1% | 35,0% | 324,9 | 53,5 | 271,3 | 10,1% | 153,9 |
| 7 | 1.159,9 | 5,9% | 35,0% | 324,9 | 54,8 | 270,1 | 10,2% | 139,0 |
| 8 | 1.225,7 | 5,7% | 35,0% | 323,3 | 56,0 | 267,3 | 10,4% | 124,6 |
| 9 | 1.292,8 | 5,5% | 35,0% | 319,8 | 57,0 | 262,8 | 10,6% | 110,8 |
| 10 | 1.361,2 | 5,3% | 35,0% | 314,4 | 60,0 | 254,4 | 10,7% | 96,9 |
| Terminal | 1.433,2 | 5,3% | 35,0% | 331,1 | 118,3 | 212,7 | 10,7% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 1.360,68 | 1.279,08 | 2.639,76 | 2.166,96 | 24,38 |
| Conservadora | 1.198,87 | 998,16 | 2.197,03 | 1.724,23 | 19,40 |
| Disrupción | 1.050,88 | 473,04 | 1.523,92 | 1.051,12 | 11,82 |
| Optimista | 1.492,53 | 1.492,29 | 2.984,82 | 2.512,02 | 28,26 |

Ejemplo Base: (1.360,68 + 1.279,08 + 194 + 11 − 670 − 8) / 88,9 = US$24,38 por acción. El terminal representa 48,5% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 45% / 30% / 15% / 10% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,45 × 24,375201 + 0,30 × 19,395129 + 0,15 × 11,823616 + 0,10 × 28,256701 = US$21,386592 ≈ US$21,39. Los aportes son US$10,97 + US$5,82 + US$1,77 + US$2,83 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 21,386592 × 0,65 = US$13,901284 ≈ US$13,90. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$24,38, es el valor intrínseco principal. El DCF esperado de US$21,39 combina las cuatro tesis con sus probabilidades y se presenta como complemento. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: La escasez de plazas sostiene precio y margen

**Qué plantea.** Es la continuación de 2024-2026: crecimiento de un dígito medio y margen estable.

**Traducción al modelo.** Grado (Medicina) crece 7%, 6%, 6%, 5%, 5%; Educación continua crece 6%, 6%, 5%, 5%, 5%; Soluciones para la práctica médica crece 5%, 8%, 8%, 8%, 7%. El crecimiento anual compuesto de cinco años es 5,8%; el margen operativo objetivo es 33,0%. El ROIC terminal es 14,8%. El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 45%; DCF: US$24,38 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (ingresos de grado en Medicina (reales): +6,5% (1S26); margen EBITDA ajustado: −190 pb (1S26); estado de la fusión con Yduqs (CADE, asambleas): Anunciada (sep-2026)). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: Madurez: precio real plano

**Qué plantea.** Refleja que el precio real de la matrícula no puede subir para siempre y que el 1S26 ya estuvo en el rango bajo de la guía.

**Traducción al modelo.** Grado (Medicina) crece 5%, 4%, 3%, 3%, 3%; Educación continua crece 3%, 3%, 3%, 3%, 3%; Soluciones para la práctica médica crece 2%, 2%, 2%, 2%, 2%. El crecimiento anual compuesto de cinco años es 3,5%; el margen operativo objetivo es 30,0%. El ROIC terminal es 14,8%. El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 30%; DCF: US$19,40 por acción.

**Cómo contrastarla.** La apoyarían: ingresos de grado en Medicina (reales): ≤ +4%; margen EBITDA ajustado: nueva compresión; estado de la fusión con Yduqs (CADE, asambleas): remedios estructurales o rechazo; plazas nuevas de Medicina autorizadas (MEC): nueva apertura masiva.


#### Disrupción · Deterioro de los fundamentales: Se liberan plazas y cae el precio

**Qué plantea.** Es el riesgo regulatorio: poco probable, pero es el que rompe la tesis.

**Traducción al modelo.** Grado (Medicina) crece 2%, 0%, -1%, 0%, 1%; Educación continua crece 0%, 0%, 0%, 0%, 0%; Soluciones para la práctica médica crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 0,3%; el margen operativo objetivo es 26,0%. El ROIC terminal es el costo de capital (10,72%). El crecimiento terminal es 0,89%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 15%; DCF: US$11,82 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: ingresos de grado en Medicina (reales): ≤ +4%; margen EBITDA ajustado: nueva compresión; estado de la fusión con Yduqs (CADE, asambleas): remedios estructurales o rechazo; plazas nuevas de Medicina autorizadas (MEC): nueva apertura masiva.


#### Optimista: Maduran los campus y crece lo digital

**Qué plantea.** Necesita que la madurez de los campus nuevos y lo digital aceleren.

**Traducción al modelo.** Grado (Medicina) crece 9%, 8%, 7%, 6%, 6%; Educación continua crece 8%, 8%, 8%, 8%, 8%; Soluciones para la práctica médica crece 12%, 12%, 10%, 10%, 8%. El crecimiento anual compuesto de cinco años es 7,4%; el margen operativo objetivo es 35,0%. El ROIC terminal es 14,8%. El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 10%; DCF: US$28,26 por acción.

**Cómo contrastarla.** La confirmarían: ingresos de grado en Medicina (reales): ≥ +7%; margen EBITDA ajustado: recupera en 2027; estado de la fusión con Yduqs (CADE, asambleas): aprobada sin remedios severos; plazas nuevas de Medicina autorizadas (MEC): sin cambios.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 5,29%; Disrupción: 0,89%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,13) | Valor/acción (beta 1,09) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| **Base · La escasez de plazas sostiene precio y margen** | 45% | Grado (Medicina): 7%, 6%, 6%, 5%, 5%; Educación continua: 6%, 6%, 5%, 5%, 5%; Soluciones para la práctica médica: 5%, 8%, 8%, 8%, 7% | 5,8% | 33,0% | 1,5 | 14,8% | 5,29% | US$24,38 | US$24,60 |
| **Conservadora · Madurez: precio real plano** | 30% | Grado (Medicina): 5%, 4%, 3%, 3%, 3%; Educación continua: 3%, 3%, 3%, 3%, 3%; Soluciones para la práctica médica: 2%, 2%, 2%, 2%, 2% | 3,5% | 30,0% | 1,5 | 14,8% | 5,29% | US$19,40 | US$19,57 |
| **Disrupción · Deterioro de los fundamentales: Se liberan plazas y cae el precio** | 15% | Grado (Medicina): 2%, 0%, -1%, 0%, 1%; Educación continua: 0%, 0%, 0%, 0%, 0%; Soluciones para la práctica médica: 0%, 0%, 0%, 0%, 0% | 0,3% | 26,0% | 1,5 | = costo de capital | 0,89% | US$11,82 | US$11,93 |
| **Optimista · Maduran los campus y crece lo digital** | 10% | Grado (Medicina): 9%, 8%, 7%, 6%, 6%; Educación continua: 8%, 8%, 8%, 8%, 8%; Soluciones para la práctica médica: 12%, 12%, 10%, 10%, 8% | 7,4% | 35,0% | 1,5 | 14,8% | 5,29% | US$28,26 | US$28,51 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  |  | **US$21,39** | **US$21,58** |

Base (45%) es la continuación de 2024-2026: crecimiento de un dígito medio y margen estable. Conservadora (30%) refleja que el precio real de la matrícula no puede subir para siempre y que el 1S26 ya estuvo en el rango bajo de la guía. Disrupción (15%) es el riesgo regulatorio: poco probable, pero es el que rompe la tesis. Optimista (10%) necesita que la madurez de los campus nuevos y lo digital aceleren. En las historias de erosión (Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 1,13; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.

| Crecimiento \ Margen | 29,0% | 31,0% | 33,0% | 35,0% | 37,0% |
|---|---:|---:|---:|---:|---:|
| 1,8% | 17,07 | 18,40 | 19,73 | 21,06 | 22,39 |
| 3,8% | 18,98 | 20,48 | 21,97 | 23,47 | 24,97 |
| 5,8% | 21,08 | 22,76 | 24,45 | 26,14 | 27,82 |
| 7,8% | 23,38 | 25,28 | 27,17 | 29,07 | 30,96 |
| 9,8% | 25,92 | 28,04 | 30,17 | 32,30 | 34,42 |


### Pre-mortem

1. CADE bloquea o condiciona la fusión y la acción queda atrapada entre el valor de canje y el standalone durante meses.
2. Un cambio de política (o una nueva ronda de Mais Médicos) abre plazas y baja el precio de la matrícula.
3. El real se deprecia otra vez: el negocio va bien en reales pero el valor en dólares cae.
4. La compresión de margen del 1S26 no es temporal: la inversión en producto digital no da retorno.
5. La integración con Yduqs (si se cierra) distrae y destruye valor en el negocio más rentable.
6. Cambia la ley de ProUni o la reforma tributaria elimina la exención: la tasa sube hacia 34% y el valor cae ~20%.

**Evidencia en contra de la historia más probable:** el crecimiento del 1S26 (~7%) estuvo en el piso de la guía, el EBITDA ajustado perdió 190 pb y educación continua y digital crecen 1-5%. Si 2027 se parece, la historia Conservadora sube de peso.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Ingresos de grado en Medicina (reales) | +6,5% (1S26) | ≥ +7% | ≤ +4% |
| Margen EBITDA ajustado | −190 pb (1S26) | Recupera en 2027 | Nueva compresión |
| Estado de la fusión con Yduqs (CADE, asambleas) | Anunciada (sep-2026) | Aprobada sin remedios severos | Remedios estructurales o rechazo |
| Plazas nuevas de Medicina autorizadas (MEC) | Política restrictiva | Sin cambios | Nueva apertura masiva |
| Tipo de cambio R$/US$ | ~6,2 (según el modelo) | Estable o apreciación | Nueva depreciación fuerte |
| Beneficio fiscal de ProUni (tasa efectiva) | ~11% efectiva | Programa renovado sin cambios | Recorte o fin del beneficio |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$12,04**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 26% | Margen 30% | Margen 33% |
|---|---:|---:|---:|
| Beta 1,13 | −2,4% (88% de las empresas) | −5,2% (90% de las empresas) | −7,0% (90% de las empresas) |
| Beta 1,09 | −2,6% (89% de las empresas) | −5,4% (90% de las empresas) | −7,2% (90% de las empresas) |

Frente al DCF Base (US$24,38), el valor intrínseco principal, el precio está por debajo en 51%.

Frente al DCF esperado de las historias (US$21,39 con la beta de la hoja; US$21,58 con la propuesta), el precio está por debajo en 44% y por debajo en 44%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Escasez regulada de plazas de Medicina en Brasil; la fusión con Yduqs está por decidirse |  |
| Probabilidades | Base 45% / Conservadora 30% / Disrupción 15% / Optimista 10% |  |
| DCF Base hoy (valor intrínseco principal) | US$24,38 |  |
| DCF esperado por probabilidades (complemento) (beta de la hoja / propuesta) | US$21,39 / US$21,58 |  |
| Precio con MOS sobre el DCF esperado | US$13,90 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$11,82 a US$28,51 |  |
| Confianza | Media: el negocio standalone es claro; la fusión y la moneda dominan el resultado |  |
| Qué cambiaría la opinión | Resolución de CADE y asambleas sobre la fusión; crecimiento de grado y margen en 2027 |  |
| Revisión | Resultados del 3T26 (nov-2026) y cada hito de la fusión |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [Afya, resultados del 2T y 1S 2026 (Form 6-K)](https://www.sec.gov/Archives/edgar/data/0001771007/000129281426004218/ex99-1.htm)
- [MarketBeat, puntos clave de la llamada del 2T26 de Afya](https://www.marketbeat.com/instant-alerts/afya-q2-earnings-call-highlights-2026-08-13/)
- [Dealroom, «Afya and Yduqs merge to form US$2.3B Brazilian education giant»](https://dealroom.co/news/155883-afya-and-yduqs-merge-to-form-r-9b-brazilian-education-giant/)
- [StockTitan, Schedule 13D/A de Bertelsmann sobre Afya](https://www.stocktitan.net/sec-filings/AFYA/schedule-13d-a-afya-ltd-amended-major-shareholder-report-a6e236382a7b.html)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
