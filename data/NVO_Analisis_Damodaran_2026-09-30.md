---
schema: "jmr-analisis-damodaran-v1"
ticker: "NVO"
analysis_date: "2026-09-30"
---

# Novo Nordisk A/S (NVO) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$31,21 por acción** (Base · El volumen compensa la caída de precio).

**Complemento · DCF esperado por probabilidades: US$29,48.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$20,37–37,65. El MOS 35% se aplica al esperado: US$19,16. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: capital invertido operativo, conversor de i+d alineado al ltm, flujos ltm, ventas/capital contrastado con la historia y la industria (8 celdas, con respaldo). DCF esperado US$35,63 → US$29,48. Salvedades abiertas: Arrendamientos: bajo NIIF 16 todos los arrendamientos están en el balance y el EBIT ya excluye su costo financiero, así que su pasivo es deuda; se conserva en la deuda del DCF. Emisor extranjero (NIIF) sin XBRL trimestral en la SEC: flujos LTM y EPS no se contrastaron de forma automática; el balance se revisó con el informe semestral. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (bloque Base de 'Valuation output': US$31,21 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja calcula estos cuatro DCF en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

Novo Nordisk creó el mercado de los GLP-1 para diabetes y obesidad (Ozempic, Wegovy, Rybelsus) y entre 2022 y 2024 creció 25-31% al año con márgenes operativos de ~44%. Ahora vive una transición: Eli Lilly (tirzepatida) le quitó el liderazgo en obesidad en EE.UU., el precio realizado cae más rápido de lo que crece el volumen (canal de autopago a US$149-299 por mes, Medicare desde julio de 2026), la semaglutida enfrenta genéricos fuera de EE.UU. desde 2026 y las insulinas declinan. En el 1S26 las ventas ajustadas subieron solo 2% a tipo de cambio constante, aunque el volumen sigue creciendo y la guía subió dos veces. La historia de cinco años depende de si el volumen global de obesidad (Wegovy pill, dosis altas, nuevos mercados) compensa la caída de precio, y de si su próxima generación (CagriSema, amicretin) recupera terreno frente a Lilly.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Las ventas vuelven a crecer ~4% anual desde 2027 | Sí | Sí: el volumen crece; el precio es la incógnita | Media |
| El margen operativo se mantiene en ~40% | Sí | Sí: 41-44% hoy con precios en baja; la escala de producción ayuda | Probable |
| Novo recupera el liderazgo en obesidad | Sí | Poco: Lilly lidera en eficacia y en nuevos lanzamientos | Baja-media |
| La semaglutida pierde valor por genéricos antes de 2032 en EE.UU. | Sí | Fuera de EE.UU. sí desde 2026; en EE.UU. la patente llega a 2032 | Parcial |


### Visión externa: tasas base

Con ventas LTM de US$46.353 millones (US$32.797 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **>$25,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 2,1% y una mediana de 2,0% (desviación estándar 8,6%); sumando una inflación de 2,5%, la mediana nominal ronda 4,5%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · El volumen compensa la caída de precio | 0,8% | 71% |
| Conservadora · Guerra de precios con Lilly y genéricos | −2,8% | 86% |
| Disrupción · Deterioro de los fundamentales: Novo pierde relevancia frente a Lilly | −6,0% | 91% |
| Optimista · La nueva generación recupera el liderazgo | 3,7% | 57% |

En dólares de 2015 la empresa está en el tramo de más de US$25.000 millones: crecer 0,8% anual cinco años (Base) lo logró ~71% de las empresas de ese tamaño; 3,7% (Optimista), ~57%. La hoja (3%) no pide nada extraordinario. El riesgo de Novo no es de crecimiento sino de precio: en farmacéuticas, la erosión de precio por competencia y genéricos suele ser más rápida de lo que el volumen compensa.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: el volumen sube, el precio baja.** Novo Nordisk creó el mercado de los GLP-1 (Ozempic, Wegovy, Rybelsus) y entre 2022 y 2024 creció 25-31% al año. Ahora vive una transición: Eli Lilly le quitó el liderazgo en obesidad en EE.UU., el precio realizado cae más rápido de lo que crece el volumen (autopago a US$149-299 al mes, Medicare desde julio de 2026), la semaglutida enfrenta genéricos fuera de EE.UU. y las insulinas declinan. En el 1S26 las ventas ajustadas crecieron solo 2% a tipo de cambio constante. La Base supone que la obesidad sigue creciendo (5% y luego 7-10%), que los GLP-1 para diabetes caen 8% el primer año y se estabilizan, y que las insulinas bajan 5% al año: −3,4% el primer año y 0,8% compuesto, ventas casi planas. No es una cifra exigente (~71% de empresas de su tamaño lo lograron): el riesgo de Novo no es de crecimiento sino de precio. La Conservadora (−2,8%) es una guerra de precios con Lilly y genéricos; la Disrupción (−6,0%), la pérdida de relevancia frente a Lilly y los orales; la Optimista (3,7%), que la próxima generación (CagriSema, amicretin, Wegovy en pastilla) recupere participación. Si 2027 no crece a tipo constante, la Conservadora pasa a ser la central.

**Margen: bajar de 44% a 40%.** El margen operativo bajó de 44% a ~41% por precios, reestructuración y la integración de las plantas de Catalent. El modelo capitaliza el I+D (vida de 10 años), por eso el margen del primer año es 48,4%. La Base supone que converge a 40,0% en 7 años: el segmento de obesidad y diabetes todavía tiene ~52% de margen, pero el precio en EE.UU. baja. La Conservadora usa 35,0% y la Disrupción 30,0%. Bajo NIIF 16 los arrendamientos ya están en la deuda y no hay ajuste adicional. Dos puntos de margen mueven la Base a US$29,96 (−4%) o US$32,46 (+4%). Un margen de 36% o menos invalidaría la Base.

**Reinversión: capacidad comprada para una demanda que cambió de precio.** Novo invirtió fuerte en capacidad: capex de US$9.210 millones en 2025 y la compra de tres plantas de llenado por US$11.700 millones. La hoja usa un ventas/capital de 0,57× en los años 1–5 —cada dólar de ventas nuevas exige ~US$1,75 de capital, muy intensivo— y 0,76× después. Revisión del 1-oct-2026: antes era 0,45, más exigente que la propia historia (0,57 en 2023-2025, con capex, intangibles y compras); el promedio de farmacéuticas según Damodaran es 1,11. Si el precio sigue cayendo, esa capacidad rinde menos de lo planeado: es el mayor riesgo de destrucción de valor. El ROIC bajó de 87% a ~25%: la ventaja (patentes y escala de manufactura) se desvanece, así que después del año 10 la Base usa 9,4%, el punto medio entre el costo de capital y la industria. Sin ventaja, la Base valdría US$31,21 (+0,0%).

**Descuento.** La hoja usa una beta de 1,09; la bottom-up de farmacéuticas reapalancada da 1,00, una diferencia menor: el riesgo está en el precio de los GLP-1, no en la tasa. El costo de capital va de 10,03% a 9,38%. El crecimiento perpetuo es 3,50% y el terminal explica 38,6% del valor operativo. Un punto más de tasa lleva la Base a US$28,03 (−10%).

**Probabilidades y lectura del resultado.** La Base pesa 40%, la Conservadora 30%, la Disrupción 10% y la Optimista 20%. El DCF Base es US$31,21 y el esperado US$29,48, frente a un precio de US$37,32: el mercado paga casi lo mismo que la Base. La evidencia en contra es que en el 1S26 el precio cayó más rápido que el aumento del volumen y China y los emergentes están planos o en baja. Los datos de CagriSema y amicretin frente a tirzepatida son el evento que más puede mover las probabilidades. Las acciones se fijan en 4.420,8 millones.

**Vida útil de I+D.** La hoja capitaliza el I+D (US$7.930 millones en el último año) y lo amortiza en 10 años. Mecanismo: el I+D crea activos que rinden varios años; capitalizarlo mueve el gasto del EBIT al capital invertido. La vida elegida es una convención del modelo (tabla de Damodaran por sector), no un dato reportado: una vida más larga eleva el activo y reduce el ROIC medido; una más corta hace lo contrario, y cambia también el EBIT ajustado. No se recalcula aquí porque modifica la hoja de conversión, no un input del DCF; queda provisional hasta contrastarla con la duración de los beneficios de los productos.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$46.353 millones. Con el crecimiento de la Base llegan a US$48.323 millones en el año 5 y a US$43.576 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 48,4% en el año 1 a 40,0% al final, y se descuentan impuestos (21,7% al principio y 22,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$16.967 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$954 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$16.013 millones el primer año. Cada flujo se trae a hoy con el costo de capital (10,03% al principio, 9,38% al final): los diez años suman US$93.468 millones. Después del año 10 se supone que la empresa crece 3,50% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 9,4%; esa perpetuidad vale hoy US$58.712 millones, 39% del total. Flujos más terminal dan el valor de las operaciones, US$152.180 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$6.889 millones, más activos no operativos por US$357 millones, menos deuda por US$21.460 millones. Queda un patrimonio de US$137.965 millones que, repartido entre 4.420,8 millones de acciones, da US$31,21 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 10,36× (peso 33% dentro de los múltiplos); EV/FCFF 19,16× (peso 17% dentro de los múltiplos); P/E 15,45× (peso 33% dentro de los múltiplos); P/FCFE 17,51× (peso 8% dentro de los múltiplos); P/OCF 11,74× (peso 8% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (10,6%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$31,21; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$29,96 | −4,0% |
| Margen objetivo +2 pp | US$32,46 | +4,0% |
| Crecimiento años 1–5 −2 pp | US$31,68 | +1,5% |
| Crecimiento años 1–5 +2 pp | US$36,69 | +17,6% |
| Ventas/capital −20% | US$31,13 | −0,2% |
| Ventas/capital +20% | US$31,26 | +0,2% |
| WACC +1 pp | US$28,03 | −10,2% |
| WACC −1 pp | US$35,13 | +12,6% |
| Crecimiento terminal −0,5 pp | US$31,17 | −0,1% |
| Crecimiento terminal +0,5 pp | US$31,25 | +0,1% |
| Acciones +5% | US$29,72 | −4,8% |


### Piezas del valor

**Crecimiento.** En dólares (hoja): US$35.570 millones (2023, +31%), US$44.474 millones (2024, +25%) y US$47.332 millones (2025, +6%); LTM US$46.353 millones. En coronas, 2025 fue DKK 309.064 millones (+10% a tipo de cambio constante): obesidad DKK 82.347 millones, GLP-1 para diabetes DKK 152.202 millones y enfermedades raras DKK 19.608 millones; EE.UU. aportó 56%. En el 1S26 las ventas ajustadas crecieron 2% a tipo de cambio constante (EUCAN +20%, China 0%, emergentes −7%). La división LTM en dólares de las historias usa el peso de 2025. Guía de la empresa (6-K del 4-ago-2026): ventas ajustadas de 2026 entre 0% y −6% a tipo de cambio constante (antes −4% a −12%), por más volumen de GLP-1 que compensa precios más bajos (acuerdo MFN en EE.UU. y pérdida de exclusividad de la semaglutida en Canadá, China, Brasil e India). Con +2% en el 1S26, la guía implica un 2S26 de alrededor de −5% a −10%. El LTM excluye la reversión de la provisión 340B (DKK 26.800 millones en el 1T26, sin efecto en caja; US$4.098 millones en la hoja). La exclusividad de la semaglutida vence en Europa en marzo de 2031, en EE.UU. entre diciembre de 2031 y octubre de 2032 y en Japón en 2033: cae en los años 5-7 del modelo. Siguiendo a Damodaran, el vencimiento se modela de forma explícita en los años 6-10 de cada historia, en lugar de la convergencia lineal al crecimiento terminal: Base −4%, −6%, −3%, +1% y +2% (los genéricos de semaglutida en EE.UU., Europa y Japón, compensados en parte por CagriSema, amicretina y la Wegovy oral); Conservadora −8%, −10%, −5%, +1% y +2% (erosión rápida, poca renovación); Disrupción −10%, −12%, −6%, −2% y 0%; Optimista −2%, −3%, 0%, +3% y +3,5% (la nueva generación reemplaza casi toda la semaglutida). Después del año 10, Base, Conservadora y Optimista crecen al 3,5% terminal.

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 35.570 | 44.474 | 47.332 | 46.353 |
| Crecimiento | +31,3% | +25,0% | +6,4% | — |
| Margen operativo | 44,2% | 44,2% | 41,3% | 40,2% |
| Capex | 3.952 | 7.223 | 9.210 | — |
| FCFF (hoja) | 12.618 | 12.028 | 6.712 | — |

**Márgenes.** El margen operativo bajó de 44% a ~41% por precios, costos de reestructuración y la integración de las plantas de Catalent. La hoja supone 44% el próximo año y 40% de objetivo. El segmento Obesidad y Diabetes aún tiene 52,4% de margen; lo que pesa es el precio en EE.UU. Las historias van de 30% (pérdida de relevancia) a 43%.

**Reinversión y retorno.** Novo invirtió fuerte en capacidad: capex de US$9.210 millones en 2025 y compra de tres plantas de llenado a Novo Holdings por US$11.700 millones. La hoja usa un ventas/capital de 0,57 (años 1-5) y 0,76 (años 6-10): con margen objetivo de 40,0% e impuesto marginal de 22%, cada dólar de capital nuevo rinde ~18% y ~24%, sin superar el mayor entre su ROIC actual (23,9%) y el de su industria (9,2%) (Damodaran, Investment Valuation cap. 11, p. 45; revisión del 4-oct-2026). Antes 0,57 y 1,10, que implicaban ~18% y ~34% sobre el capital nuevo. Si el precio sigue cayendo, esa capacidad rinde menos de lo planeado: ese es el mayor riesgo de destrucción de valor. Ventaja que se desvanece: patentes y escala en diabetes y obesidad, pero pierde participación frente a Lilly, recorta precios y su ROIC bajó de 87% a 36%. El ROIC después del año 10 es 13,1%, el punto medio entre el costo de capital terminal (9,2%) y el promedio de su industria según Damodaran (17,0%). El I+D se capitaliza con una vida de 10 años (antes 5): en farmacéuticas el paso de la investigación al producto es largo por la aprobación de fármacos (Damodaran, Investment Valuation cap. 9, p. 6-7; revisión del 4-oct-2026).

**Ventas/capital: las referencias de Damodaran.** Damodaran elige el ventas/capital mirando el de la empresa hoy, el marginal de los últimos años y el promedio del sector, y comprueba que el rendimiento que implica sobre el capital nuevo sea creíble frente a lo que gana la empresa o su sector (Investment Valuation, cap. 11, p. 44-46). El marginal es volátil: recompras de acciones y adquisiciones mueven el capital contable. El usado está dentro del rango de las referencias.

| Referencia | Ventas/capital | Detalle |
|---|---:|---|
| Empresa hoy | 0,61 | ventas LTM 46.353,0 / capital invertido 75.862,6 millones (con I+D capitalizado a 10 años) |
| Marginal, último año | 0,17 | Δventas 2.857,8 / Δcapital 17.016,2 millones (Dec '24 → Dec '25) |
| Marginal, últimos tres años | 0,47 | Δventas 20.232,1 / Δcapital 43.339,1 millones (Dec '22 → Dec '25) |
| Sector (Damodaran, enero de 2026) | 1,11 | Drugs (Pharmaceutical) |
| Usado en la hoja | 0,57 / 0,76 | años 1-5 / 6-10; rinde ~18% / ~24% sobre el capital nuevo (ROIC actual 23,9%) |

**Riesgo.** La hoja usa una beta de 1,09. La bottom-up de Drugs (Pharmaceutical) (228 empresas, 0,92 desapalancada y corregida por caja) reapalancada da 1,00; el DCF Base sube de US$43,16 a US$43,96. Diferencia menor: el riesgo está en el precio de los GLP-1.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,09 | 10,6% | 10,0% | US$33,48 |
| Bottom-up del sector (Drugs (Pharmaceutical), reapalancada) | 1,00 | 10,2% | 9,7% | US$34,18 |


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja que se desvanece | 25,2% | 9,2% | 9,4% | 9,2% | US$31,21 | US$33,48 |

Fuentes de ventaja: Patentes y escala de manufactura en diabetes y obesidad. Evidencia: ROIC 36-87% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$31,21 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$29,48. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$46.353 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 12.350 + 22.800 + 8.280 + 2.923 = 46.353. |
| Margen inicial del DCF | 48,4% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 7 (Input sheet B31). |
| Impuesto | 21,72% en años 1–5; 22,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 10,03% → 9,38% | Tasa libre de riesgo 5,29%, beta 1,09, ERP 4,93%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 0,57x en años 1–5; 0,76x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 3,50%; Disrupción: 0,00% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: parte de su crecimiento del año 5 (−2,9%) y converge a 0,00% en el año 10 (piso de 0% nominal: el negocio residual deja de achicarse, lo que en términos reales sigue siendo contracción). Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Conservadora/Disrupción/Optimista: 9,38% (= WACC terminal) | Criterio de ventaja competitiva (ventaja que se desvanece). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 6.889; deuda 21.460; activos no operativos 357; acciones 4.420,8 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 12.350 × 1,05 + 22.800 × 0,92 + 8.280 × 0,95 + 2.923 × 1,02 = US$44.790,96 millones. Frente a 46.353, el crecimiento consolidado es −3,37%. En los años 2–5 es 1,21%, 2,46%, 2,07%, 1,92%; las ventas del año 5 son US$48.322,76 millones. El 0,8% de la tabla es el crecimiento anual compuesto de los cinco años: (48.322,76 / 46.353)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 44.790,96 × 48,39% × (1 − 21,72%) = US$16.966,94 millones. La reinversión es US$953,61 millones y el FCFF es US$16.013,33 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,38%. Reinversión terminal sobre el NOPAT: Base, 37,3% (3,50% / 9,38%); Conservadora, 37,3% (3,50% / 9,38%); Disrupción, 0,0% (0,00% / 9,38%); Optimista, 37,3% (3,50% / 9,38%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · El volumen compensa la caída de precio** — probabilidad 40%; valor terminal 150.016 (VP 58.712); DCF US$31,21 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 44.791 | −3,4% | 48,4% | 16.967 | 954 | 16.013 | 10,0% | 14.554 |
| 2 | 45.335 | 1,2% | 46,0% | 16.322 | 1.954 | 14.368 | 10,0% | 11.868 |
| 3 | 46.448 | 2,5% | 44,8% | 16.287 | 1.688 | 14.599 | 10,0% | 10.959 |
| 4 | 47.410 | 2,1% | 43,6% | 16.180 | 1.601 | 14.579 | 10,0% | 9.947 |
| 5 | 48.323 | 1,9% | 42,4% | 16.038 | -3.391 | 19.429 | 10,0% | 12.047 |
| 6 | 46.390 | −4,0% | 41,2% | 14.950 | -3.662 | 18.613 | 9,9% | 10.501 |
| 7 | 43.606 | −6,0% | 40,0% | 13.635 | -1.721 | 15.356 | 9,8% | 7.893 |
| 8 | 42.298 | −3,0% | 40,0% | 13.216 | 557 | 12.659 | 9,6% | 5.935 |
| 9 | 42.721 | 1,0% | 40,0% | 13.339 | 1.124 | 12.214 | 9,5% | 5.229 |
| 10 | 43.576 | 2,0% | 40,0% | 13.596 | 2.007 | 11.589 | 9,4% | 4.536 |
| Terminal | 45.101 | 3,5% | 40,0% | 14.071 | 5.251 | 8.821 | 9,4% | — |

**Conservadora · Guerra de precios con Lilly y genéricos** — probabilidad 30%; valor terminal 98.011 (VP 38.359); DCF US$24,77 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 42.790 | −7,7% | 48,4% | 16.209 | -2.208 | 18.417 | 10,0% | 16.739 |
| 2 | 41.532 | −2,9% | 44,6% | 14.488 | -1.099 | 15.587 | 10,0% | 12.875 |
| 3 | 40.905 | −1,5% | 42,7% | 13.657 | -611 | 14.269 | 10,0% | 10.712 |
| 4 | 40.557 | −0,9% | 40,7% | 12.934 | -711 | 13.645 | 10,0% | 9.309 |
| 5 | 40.151 | −1,0% | 38,8% | 12.203 | -5.635 | 17.838 | 10,0% | 11.061 |
| 6 | 36.939 | −8,0% | 36,9% | 10.666 | -4.860 | 15.527 | 9,9% | 8.760 |
| 7 | 33.245 | −10,0% | 35,0% | 9.096 | -2.187 | 11.283 | 9,8% | 5.799 |
| 8 | 31.583 | −5,0% | 35,0% | 8.635 | 416 | 8.219 | 9,6% | 3.853 |
| 9 | 31.899 | 1,0% | 35,0% | 8.715 | 839 | 7.875 | 9,5% | 3.371 |
| 10 | 32.537 | 2,0% | 35,0% | 8.883 | 1.498 | 7.384 | 9,4% | 2.890 |
| Terminal | 33.676 | 3,5% | 35,0% | 9.193 | 3.430 | 5.763 | 9,4% | — |

**Disrupción · Deterioro de los fundamentales: Novo pierde relevancia frente a Lilly** — probabilidad 10%; valor terminal 62.051 (VP 24.285); DCF US$20,37 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 41.283 | −10,9% | 48,4% | 15.638 | -5.466 | 21.104 | 10,0% | 19.180 |
| 2 | 38.167 | −7,5% | 43,1% | 12.888 | -3.432 | 16.320 | 10,0% | 13.480 |
| 3 | 36.211 | −5,1% | 40,5% | 11.483 | -1.934 | 13.416 | 10,0% | 10.072 |
| 4 | 35.109 | −3,0% | 37,9% | 10.411 | -1.783 | 12.195 | 10,0% | 8.320 |
| 5 | 34.092 | −2,9% | 35,3% | 9.409 | -5.981 | 15.390 | 10,0% | 9.543 |
| 6 | 30.683 | −10,0% | 32,6% | 7.831 | -4.845 | 12.676 | 9,9% | 7.152 |
| 7 | 27.001 | −12,0% | 30,0% | 6.332 | -2.132 | 8.464 | 9,8% | 4.350 |
| 8 | 25.381 | −6,0% | 30,0% | 5.948 | -668 | 6.616 | 9,6% | 3.101 |
| 9 | 24.873 | −2,0% | 30,0% | 5.825 | 0 | 5.825 | 9,5% | 2.493 |
| 10 | 24.873 | 0,0% | 30,0% | 5.820 | 0 | 5.820 | 9,4% | 2.278 |
| Terminal | 24.873 | 0,0% | 30,0% | 5.820 | 0 | 5.820 | 9,4% | — |

**Optimista · La nueva generación recupera el liderazgo** — probabilidad 20%; valor terminal 208.153 (VP 81.465); DCF US$37,65 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 46.432 | 0,2% | 48,4% | 17.589 | 3.176 | 14.413 | 10,0% | 13.099 |
| 2 | 48.243 | 3,9% | 46,9% | 17.693 | 4.507 | 13.186 | 10,0% | 10.891 |
| 3 | 50.812 | 5,3% | 46,1% | 18.329 | 4.220 | 14.109 | 10,0% | 10.591 |
| 4 | 53.217 | 4,7% | 45,3% | 18.875 | 4.009 | 14.867 | 10,0% | 10.143 |
| 5 | 55.502 | 4,3% | 44,5% | 19.351 | -1.947 | 21.299 | 10,0% | 13.207 |
| 6 | 54.392 | −2,0% | 43,8% | 18.623 | -2.147 | 20.770 | 9,9% | 11.719 |
| 7 | 52.760 | −3,0% | 43,0% | 17.734 | 0 | 17.734 | 9,8% | 9.115 |
| 8 | 52.760 | 0,0% | 43,0% | 17.721 | 2.083 | 15.639 | 9,6% | 7.331 |
| 9 | 54.343 | 3,0% | 43,0% | 18.240 | 2.503 | 15.737 | 9,5% | 6.737 |
| 10 | 56.245 | 3,5% | 43,0% | 18.865 | 2.590 | 16.274 | 9,4% | 6.369 |
| Terminal | 58.213 | 3,5% | 43,0% | 19.525 | 7.285 | 12.239 | 9,4% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 93.467,71 | 58.711,92 | 152.179,63 | 137.965,43 | 31,21 |
| Conservadora | 85.368,85 | 38.358,92 | 123.727,77 | 109.513,57 | 24,77 |
| Disrupción | 79.968,18 | 24.285,00 | 104.253,18 | 90.038,98 | 20,37 |
| Optimista | 99.202,27 | 81.465,50 | 180.667,76 | 166.453,56 | 37,65 |

Ejemplo Base: (93.467,71 + 58.711,92 + 6.889 + 357 − 21.460) / 4.420,8 = US$31,21 por acción. El terminal representa 38,6% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 40% / 30% / 10% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,40 × 31,208249 + 0,30 × 24,772343 + 0,10 × 20,367123 + 0,20 × 37,652362 = US$29,482187 ≈ US$29,48. Los aportes son US$12,48 + US$7,43 + US$2,04 + US$7,53 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 29,482187 × 0,65 = US$19,163422 ≈ US$19,16. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$31,21, es el valor intrínseco principal. El DCF esperado de US$29,48 combina las cuatro tesis con sus probabilidades y se presenta como complemento. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: El volumen compensa la caída de precio

**Qué plantea.** Es lo que muestra 2026: volumen creciendo y precio cayendo, con ventas casi planas y margen de ~40%.

**Traducción al modelo.** Obesidad (Wegovy, Saxenda) crece 5%, 10%, 10%, 8%, 7%; Diabetes GLP-1 (Ozempic, Rybelsus) crece -8%, -2%, 0%, 0%, 0%; Insulinas y otros de diabetes crece -5%, -5%, -5%, -5%, -5%; Enfermedades raras crece 2%, 2%, 2%, 2%, 2%. El crecimiento anual compuesto de cinco años es 0,8%; el margen operativo objetivo es 40,0%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 3,50%, el de la hoja. Probabilidad: 40%; DCF: US$31,21 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (ventas a tipo de cambio constante: +2% (1S26); participación de Novo en prescripciones de obesidad (EE.UU.): Detrás de Lilly; precio realizado de Wegovy/Ozempic en EE.UU.: En fuerte baja). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: Guerra de precios con Lilly y genéricos

**Qué plantea.** Es una guerra de precios con Lilly y genéricos que se aceleran.

**Traducción al modelo.** Obesidad (Wegovy, Saxenda) crece -2%, 4%, 5%, 5%, 4%; Diabetes GLP-1 (Ozempic, Rybelsus) crece -12%, -6%, -4%, -3%, -3%; Insulinas y otros de diabetes crece -7%, -7%, -7%, -7%, -7%; Enfermedades raras crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es −2,8%; el margen operativo objetivo es 35,0%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 3,50%, el de la hoja. Probabilidad: 30%; DCF: US$24,77 por acción.

**Cómo contrastarla.** La apoyarían: ventas a tipo de cambio constante: negativas; participación de Novo en prescripciones de obesidad (EE.UU.): sigue cayendo; precio realizado de Wegovy/Ozempic en EE.UU.: baja > 15% anual; resultados de CagriSema y amicretin: datos débiles.


#### Disrupción · Deterioro de los fundamentales: Novo pierde relevancia frente a Lilly

**Qué plantea.** Es la pérdida de relevancia frente a Lilly y los orales.

**Traducción al modelo.** Obesidad (Wegovy, Saxenda) crece -8%, -5%, 0%, 2%, 2%; Diabetes GLP-1 (Ozempic, Rybelsus) crece -15%, -10%, -8%, -5%, -5%; Insulinas y otros de diabetes crece -8%, -8%, -8%, -8%, -8%; Enfermedades raras crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es −6,0%; el margen operativo objetivo es 30,0%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 0,00%: los años 6–10 pasan de −2,9% a ese nivel, sin recuperación. Probabilidad: 10%; DCF: US$20,37 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: ventas a tipo de cambio constante: negativas; participación de Novo en prescripciones de obesidad (EE.UU.): sigue cayendo; precio realizado de Wegovy/Ozempic en EE.UU.: baja > 15% anual; resultados de CagriSema y amicretin: datos débiles.


#### Optimista: La nueva generación recupera el liderazgo

**Qué plantea.** Es la próxima generación de Novo (CagriSema, amicretin, Wegovy pill) recuperando participación.

**Traducción al modelo.** Obesidad (Wegovy, Saxenda) crece 10%, 15%, 15%, 12%, 10%; Diabetes GLP-1 (Ozempic, Rybelsus) crece -4%, 0%, 2%, 2%, 2%; Insulinas y otros de diabetes crece -4%, -4%, -4%, -4%, -4%; Enfermedades raras crece 3%, 3%, 3%, 3%, 3%. El crecimiento anual compuesto de cinco años es 3,7%; el margen operativo objetivo es 43,0%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 3,50%, el de la hoja. Probabilidad: 20%; DCF: US$37,65 por acción.

**Cómo contrastarla.** La confirmarían: ventas a tipo de cambio constante: ≥ +5% en 2027; participación de Novo en prescripciones de obesidad (EE.UU.): estabiliza; precio realizado de Wegovy/Ozempic en EE.UU.: baja < 10% anual; resultados de CagriSema y amicretin: superioridad o no inferioridad frente a tirzepatida.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 3,50%; Disrupción: 0,00%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | Crecimiento terminal | Valor/acción (beta 1,09) | Valor/acción (beta 1,00) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **Base · El volumen compensa la caída de precio** | 40% | Obesidad (Wegovy, Saxenda): 5%, 10%, 10%, 8%, 7%; Diabetes GLP-1 (Ozempic, Rybelsus): -8%, -2%, 0%, 0%, 0%; Insulinas y otros de diabetes: -5%, -5%, -5%, -5%, -5%; Enfermedades raras: 2%, 2%, 2%, 2%, 2% | 0,8% | 40,0% | 0,6 | 3,50% | US$31,21 | US$31,84 |
| **Conservadora · Guerra de precios con Lilly y genéricos** | 30% | Obesidad (Wegovy, Saxenda): -2%, 4%, 5%, 5%, 4%; Diabetes GLP-1 (Ozempic, Rybelsus): -12%, -6%, -4%, -3%, -3%; Insulinas y otros de diabetes: -7%, -7%, -7%, -7%, -7%; Enfermedades raras: 0%, 0%, 0%, 0%, 0% | −2,8% | 35,0% | 0,6 | 3,50% | US$24,77 | US$25,24 |
| **Disrupción · Deterioro de los fundamentales: Novo pierde relevancia frente a Lilly** | 10% | Obesidad (Wegovy, Saxenda): -8%, -5%, 0%, 2%, 2%; Diabetes GLP-1 (Ozempic, Rybelsus): -15%, -10%, -8%, -5%, -5%; Insulinas y otros de diabetes: -8%, -8%, -8%, -8%, -8%; Enfermedades raras: 0%, 0%, 0%, 0%, 0% | −6,0% | 30,0% | 0,6 | 0,00% | US$20,37 | US$20,72 |
| **Optimista · La nueva generación recupera el liderazgo** | 20% | Obesidad (Wegovy, Saxenda): 10%, 15%, 15%, 12%, 10%; Diabetes GLP-1 (Ozempic, Rybelsus): -4%, 0%, 2%, 2%, 2%; Insulinas y otros de diabetes: -4%, -4%, -4%, -4%, -4%; Enfermedades raras: 3%, 3%, 3%, 3%, 3% | 3,7% | 43,0% | 0,6 | 3,50% | US$37,65 | US$38,45 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  | **US$29,48** | **US$30,07** |

Base (40%) es lo que muestra 2026: volumen creciendo y precio cayendo, con ventas casi planas y margen de ~40%. Conservadora (30%) es una guerra de precios con Lilly y genéricos que se aceleran. Disrupción (10%) es la pérdida de relevancia frente a Lilly y los orales. Optimista (20%) es la próxima generación de Novo (CagriSema, amicretin, Wegovy pill) recuperando participación. En las historias de erosión (Conservadora y Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 1,09; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.

| Crecimiento \ Margen | 36,0% | 38,0% | 40,0% | 42,0% | 44,0% |
|---|---:|---:|---:|---:|---:|
| −3,1% | 27,98 | 29,13 | 30,27 | 31,42 | 32,57 |
| −1,1% | 29,81 | 31,12 | 32,43 | 33,73 | 35,04 |
| 0,9% | 31,82 | 33,30 | 34,78 | 36,27 | 37,75 |
| 2,9% | 34,01 | 35,69 | 37,37 | 39,05 | 40,73 |
| 4,9% | 36,41 | 38,31 | 40,21 | 42,11 | 44,01 |


### Pre-mortem

1. Lilly (tirzepatida y orforglipron oral) gana también fuera de EE.UU. y Novo queda como segundo jugador con precio más bajo.
2. CagriSema decepciona frente a la competencia y la cartera nueva no llega a tiempo.
3. Los genéricos de semaglutida fuera de EE.UU. bajan el precio más rápido de lo previsto.
4. Medicare y el autopago fijan un precio de referencia bajo que se extiende a todo el mercado estadounidense.
5. La nueva capacidad de producción queda ociosa y se deteriora.

**Evidencia en contra de la historia más probable:** en el 1S26 el precio cayó más rápido que el aumento del volumen y China y los emergentes están planos o en baja; si 2027 no muestra crecimiento en moneda constante, Conservadora pasa a ser la historia central.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Ventas a tipo de cambio constante | +2% (1S26) | ≥ +5% en 2027 | Negativas |
| Participación de Novo en prescripciones de obesidad (EE.UU.) | Detrás de Lilly | Estabiliza | Sigue cayendo |
| Precio realizado de Wegovy/Ozempic en EE.UU. | En fuerte baja | Baja < 10% anual | Baja > 15% anual |
| Resultados de CagriSema y amicretin | En desarrollo | Superioridad o no inferioridad frente a tirzepatida | Datos débiles |
| Margen operativo | ~40% | ≥ 40% | ≤ 36% |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$37,32**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 35% | Margen 40% | Margen 44% |
|---|---:|---:|---:|
| Beta 1,09 | 6,4% (39% de las empresas) | 2,8% (62% de las empresas) | 0,6% (73% de las empresas) |
| Beta 1,00 | 5,7% (43% de las empresas) | 2,2% (65% de las empresas) | 0,0% (75% de las empresas) |

Frente al DCF Base (US$31,21), el valor intrínseco principal, el precio está por encima en 20%.

Frente al DCF esperado de las historias (US$29,48 con la beta de la hoja; US$30,07 con la propuesta), el precio está por encima en 27% y por encima en 24%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Pionera de los GLP-1 en transición: volumen en alza, precio en baja y Lilly adelante |  |
| Probabilidades | Base 40% / Conservadora 30% / Disrupción 10% / Optimista 20% |  |
| DCF Base hoy (valor intrínseco principal) | US$31,21 |  |
| DCF esperado por probabilidades (complemento) (beta de la hoja / propuesta) | US$29,48 / US$30,07 |  |
| Precio con MOS sobre el DCF esperado | US$19,16 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$20,37 a US$38,45 |  |
| Confianza | Media: el mercado de obesidad crecerá; la participación y el precio de Novo son inciertos |  |
| Qué cambiaría la opinión | Ventas a tipo de cambio constante, participación frente a Lilly y datos de CagriSema |  |
| Revisión | Resultados de 9M26 (nov-2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [Novo Nordisk, informe del 1S 2026 (Form 6-K)](https://www.sec.gov/Archives/edgar/data/0000353278/000035327826000023/caq22026.htm)
- [Novo Nordisk, informe financiero 2025 (Form 6-K)](https://www.sec.gov/Archives/edgar/data/353278/000035327826000006/caq42025.htm)
- [Novo Nordisk, Form 20-F 2025](https://www.sec.gov/Archives/edgar/data/353278/000035327826000012/nvo-20251231.htm)
- [Eli Lilly, resultados del 2T 2026](https://www.sec.gov/Archives/edgar/data/0000059478/000005947826000077/q226lillysalesandearningsp.htm)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
