---
schema: "jmr-analisis-damodaran-v1"
ticker: "NVO"
analysis_date: "2026-09-30"
---

# Novo Nordisk A/S (NVO) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$39,27 por acción** (Base · El volumen compensa la caída de precio).

**Complemento · DCF esperado por probabilidades: US$35,92.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$22,71–46,89. El MOS 35% se aplica al esperado: US$23,35. El antiguo caso técnico de la hoja (US$42,27) se conserva solo como calibración; no es el DCF Base. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: capital invertido operativo, conversor de i+d alineado al ltm, flujos ltm (7 celdas, con respaldo). DCF esperado US$35,63 → US$35,92. Salvedades abiertas: Arrendamientos: bajo NIIF 16 todos los arrendamientos están en el balance y el EBIT ya excluye su costo financiero, así que su pasivo es deuda; se conserva en la deuda del DCF. Emisor extranjero (NIIF) sin XBRL trimestral en la SEC: flujos LTM y EPS no se contrastaron de forma automática; el balance se revisó con el informe semestral. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de US$42,27 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


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

**Margen: bajar de 44% a 40%.** El margen operativo bajó de 44% a ~41% por precios, reestructuración y la integración de las plantas de Catalent. El modelo capitaliza el I+D (vida de 5 años), por eso el margen del primer año es 45,7%. La Base supone que converge a 40,0% en 7 años: el segmento de obesidad y diabetes todavía tiene ~52% de margen, pero el precio en EE.UU. baja. La Conservadora usa 35,0% y la Disrupción 30,0%. Bajo NIIF 16 los arrendamientos ya están en la deuda y no hay ajuste adicional. Dos puntos de margen mueven la Base a US$37,49 (−5%) o US$41,06 (+5%). Un margen de 36% o menos invalidaría la Base.

**Reinversión: capacidad comprada para una demanda que cambió de precio.** Novo invirtió fuerte en capacidad: capex de US$9.210 millones en 2025 y la compra de tres plantas de llenado por US$11.700 millones. La hoja usa un ventas/capital de 0,45× en los años 1–5 —cada dólar de ventas nuevas exige ~US$2,22 de capital, muy intensivo— y 1,10× después. Si el precio sigue cayendo, esa capacidad rinde menos de lo planeado: es el mayor riesgo de destrucción de valor. El ROIC bajó de 87% a ~25%: la ventaja (patentes y escala de manufactura) se desvanece, así que después del año 10 la Base usa 13,1%, el punto medio entre el costo de capital y la industria. Sin ventaja, la Base valdría US$35,89 (−9%).

**Descuento.** La hoja usa una beta de 1,09; la bottom-up de farmacéuticas reapalancada da 1,00, una diferencia menor: el riesgo está en el precio de los GLP-1, no en la tasa. El costo de capital va de 9,03% a 9,20%. El crecimiento perpetuo es 3,50% y el terminal explica 51,6% del valor operativo. Un punto más de tasa lleva la Base a US$33,49 (−15%).

**Probabilidades y lectura del resultado.** La Base pesa 40%, la Conservadora 30%, la Disrupción 10% y la Optimista 20%. El DCF Base es US$39,27 y el esperado US$35,92, frente a un precio de US$38,14: el mercado paga casi lo mismo que la Base. La evidencia en contra es que en el 1S26 el precio cayó más rápido que el aumento del volumen y China y los emergentes están planos o en baja. Los datos de CagriSema y amicretin frente a tirzepatida son el evento que más puede mover las probabilidades. Las acciones se fijan en 4.420,8 millones.

**Vida útil de I+D.** La hoja capitaliza el I+D (US$7.930 millones en el último año) y lo amortiza en 5 años. Mecanismo: el I+D crea activos que rinden varios años; capitalizarlo mueve el gasto del EBIT al capital invertido. La vida elegida es una convención del modelo (tabla de Damodaran por sector), no un dato reportado: una vida más larga eleva el activo y reduce el ROIC medido; una más corta hace lo contrario, y cambia también el EBIT ajustado. No se recalcula aquí porque modifica la hoja de conversión, no un input del DCF; queda provisional hasta contrastarla con la duración de los beneficios de los productos.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$46.353 millones. Con el crecimiento de la Base llegan a US$48.323 millones en el año 5 y a US$55.663 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 45,7% en el año 1 a 40,0% al final, y se descuentan impuestos (21,7% al principio y 22,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$16.029 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$1.208 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$14.821 millones el primer año. Cada flujo se trae a hoy con el costo de capital (9,03% al principio, 9,20% al final): los diez años suman US$90.972 millones. Después del año 10 se supone que la empresa crece 3,50% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 13,1%; esa perpetuidad vale hoy US$96.869 millones, 52% del total. Flujos más terminal dan el valor de las operaciones, US$187.841 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$6.889 millones, más activos no operativos por US$357 millones, menos deuda por US$21.460 millones. Queda un patrimonio de US$173.626 millones que, repartido entre 4.420,8 millones de acciones, da US$39,27 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 10,60× (peso 33% dentro de los múltiplos); EV/FCFF 21,03× (peso 17% dentro de los múltiplos); P/E 16,91× (peso 33% dentro de los múltiplos); P/FCFE 19,30× (peso 8% dentro de los múltiplos); P/OCF 12,54× (peso 8% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (9,6%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$39,27; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$37,49 | −4,5% |
| Margen objetivo +2 pp | US$41,06 | +4,5% |
| Crecimiento años 1–5 −2 pp | US$36,50 | −7,1% |
| Crecimiento años 1–5 +2 pp | US$42,34 | +7,8% |
| Ventas/capital −20% | US$38,62 | −1,7% |
| Ventas/capital +20% | US$39,71 | +1,1% |
| WACC +1 pp | US$33,49 | −14,7% |
| WACC −1 pp | US$47,45 | +20,8% |
| Crecimiento terminal −0,5 pp | US$38,21 | −2,7% |
| Crecimiento terminal +0,5 pp | US$40,51 | +3,2% |
| ROIC terminal = costo de capital | US$35,89 | −8,6% |
| Acciones +5% | US$37,40 | −4,8% |


### Piezas del valor

**Crecimiento.** En dólares (hoja): US$35.570 millones (2023, +31%), US$44.474 millones (2024, +25%) y US$47.332 millones (2025, +6%); LTM US$46.353 millones. En coronas, 2025 fue DKK 309.064 millones (+10% a tipo de cambio constante): obesidad DKK 82.347 millones, GLP-1 para diabetes DKK 152.202 millones y enfermedades raras DKK 19.608 millones; EE.UU. aportó 56%. En el 1S26 las ventas ajustadas crecieron 2% a tipo de cambio constante (EUCAN +20%, China 0%, emergentes −7%). La división LTM en dólares de las historias usa el peso de 2025.

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 35.570 | 44.474 | 47.332 | 46.353 |
| Crecimiento | +31,3% | +25,0% | +6,4% | — |
| Margen operativo | 44,2% | 44,2% | 41,3% | 40,2% |
| Capex | 3.952 | 7.223 | 9.210 | — |
| FCFF (hoja) | 12.618 | 12.028 | 6.712 | — |

**Márgenes.** El margen operativo bajó de 44% a ~41% por precios, costos de reestructuración y la integración de las plantas de Catalent. La hoja supone 44% el próximo año y 40% de objetivo. El segmento Obesidad y Diabetes aún tiene 52,4% de margen; lo que pesa es el precio en EE.UU. Las historias van de 30% (pérdida de relevancia) a 43%.

**Reinversión y retorno.** Novo invirtió fuerte en capacidad: capex de US$9.210 millones en 2025 y compra de tres plantas de llenado a Novo Holdings por US$11.700 millones. La hoja usa un sales-to-capital de 0,45 en los años 1-5 (muy intensivo en capital) y 1,1 después. Si el precio sigue cayendo, esa capacidad rinde menos de lo planeado: ese es el mayor riesgo de destrucción de valor. Ventaja que se desvanece: patentes y escala en diabetes y obesidad, pero pierde participación frente a Lilly, recorta precios y su ROIC bajó de 87% a 36%. El ROIC después del año 10 es 13,1%, el punto medio entre el costo de capital terminal (9,2%) y el promedio de su industria según Damodaran (17,0%).

**Riesgo.** La hoja usa una beta de 1,09. La bottom-up de Drugs (Pharmaceutical) (228 empresas, 0,92 desapalancada y corregida por caja) reapalancada da 1,00; el DCF técnico anterior sube de US$42,27 a US$43,06. Diferencia menor: el riesgo está en el precio de los GLP-1.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF técnico anterior por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,09 | 9,6% | 9,0% | US$42,27 |
| Bottom-up del sector (Drugs (Pharmaceutical), reapalancada) | 1,00 | 9,2% | 8,7% | US$43,06 |


### Calibración técnica anterior Conservador/Base/Optimista (referencia auxiliar)

| Supuesto | Conservador | Base | Optimista |
|---|---:|---:|---:|
| Crecimiento año 1 | −7,0% | −3,0% | −1,0% |
| Crecimiento años 2–5 | 1,0% | 4,5% | 7,0% |
| Margen año 1 (base ajustada del modelo) | 45,7% | 45,7% | 45,7% |
| Margen objetivo | 35,0% | 40,0% | 45,0% |

Ventas/capital: 0,5x en años 1–5 y 1,1x en 6–10. WACC: 9,0%. Ke: 9,6%. Impuesto efectivo: 21,7%. Convergencia: 7 años. Estos parámetros son escenarios del analista, no cifras reportadas. Los casos Conservador, Base y Optimista de la hoja ya no son escenarios activos: sirven de calibración y de supuestos auxiliares de múltiplos. No confundir el antiguo caso técnico Base con la tesis Base.


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF técnico anterior | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja que se desvanece | 25,2% | 17,0% | 9,2% | 13,1% | US$42,27 | US$38,32 |

Fuentes de ventaja: Patentes y escala de manufactura en diabetes y obesidad. Evidencia: ROIC 36-87% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$39,27 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$35,92. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene aplicando descuentos al antiguo caso técnico de la hoja (US$42,27) ni mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$46.353 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 12.350 + 22.800 + 8.280 + 2.923 = 46.353. |
| Margen inicial del DCF | 45,7% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 7 (Input sheet B31). |
| Impuesto | 21,72% en años 1–5; 22,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 9,03% → 9,20% | Tasa libre de riesgo 5,11%, beta 1,09, ERP 4,09%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 0,45x en años 1–5; 1,10x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 3,50%; Disrupción: 0,00% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: parte de su crecimiento del año 5 (−2,9%) y converge a 0,00% en el año 10 (piso de 0% nominal: el negocio residual deja de achicarse, lo que en términos reales sigue siendo contracción). Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Optimista: 13,10%; Conservadora/Disrupción: 9,20% (= WACC terminal) | Criterio de ventaja competitiva (ventaja que se desvanece). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 6.889; deuda 21.460; activos no operativos 357; acciones 4.420,8 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 12.350 × 1,05 + 22.800 × 0,92 + 8.280 × 0,95 + 2.923 × 1,02 = US$44.790,96 millones. Frente a 46.353, el crecimiento consolidado es −3,37%. En los años 2–5 es 1,21%, 2,46%, 2,07%, 1,92%; las ventas del año 5 son US$48.322,76 millones. El 0,8% de la tabla es el crecimiento anual compuesto de los cinco años: (48.322,76 / 46.353)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 44.790,96 × 45,71% × (1 − 21,72%) = US$16.028,67 millones. La reinversión es US$1.207,91 millones y el FCFF es US$14.820,76 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,20%. Reinversión terminal sobre el NOPAT: Base, 26,7% (3,50% / 13,10%); Conservadora, 38,0% (3,50% / 9,20%); Disrupción, 0,0% (0,00% / 9,20%); Optimista, 26,7% (3,50% / 13,10%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en «Escenarios e historias»: ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · El volumen compensa la caída de precio** — probabilidad 40%; valor terminal 231.094 (VP 96.869); DCF US$39,27 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 44.791 | −3,4% | 45,7% | 16.029 | 1.208 | 14.821 | 9,0% | 13.593 |
| 2 | 45.335 | 1,2% | 44,1% | 15.644 | 2.475 | 13.169 | 9,0% | 11.077 |
| 3 | 46.448 | 2,5% | 43,3% | 15.731 | 2.139 | 13.593 | 9,0% | 10.486 |
| 4 | 47.410 | 2,1% | 42,4% | 15.754 | 2.027 | 13.727 | 9,0% | 9.712 |
| 5 | 48.323 | 1,9% | 41,6% | 15.748 | 2.405 | 13.344 | 9,0% | 8.659 |
| 6 | 49.405 | 2,2% | 40,8% | 15.774 | 1.147 | 14.627 | 9,1% | 8.702 |
| 7 | 50.667 | 2,6% | 40,0% | 15.842 | 1.322 | 14.520 | 9,1% | 7.918 |
| 8 | 52.121 | 2,9% | 40,0% | 16.285 | 1.509 | 14.776 | 9,1% | 7.384 |
| 9 | 53.781 | 3,2% | 40,0% | 16.792 | 1.711 | 15.080 | 9,2% | 6.903 |
| 10 | 55.663 | 3,5% | 40,0% | 17.367 | 1.771 | 15.596 | 9,2% | 6.537 |
| Terminal | 57.611 | 3,5% | 40,0% | 17.975 | 4.802 | 13.172 | 9,2% | — |

**Conservadora · Guerra de precios con Lilly y genéricos** — probabilidad 30%; valor terminal 134.108 (VP 56.215); DCF US$28,52 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 42.790 | −7,7% | 45,7% | 15.313 | -2.797 | 18.110 | 9,0% | 16.609 |
| 2 | 41.532 | −2,9% | 42,7% | 13.867 | -1.392 | 15.259 | 9,0% | 12.835 |
| 3 | 40.905 | −1,5% | 41,1% | 13.168 | -775 | 13.942 | 9,0% | 10.756 |
| 4 | 40.557 | −0,9% | 39,6% | 12.570 | -901 | 13.470 | 9,0% | 9.531 |
| 5 | 40.151 | −1,0% | 38,1% | 11.963 | -89 | 12.052 | 9,0% | 7.821 |
| 6 | 40.111 | −0,1% | 36,5% | 11.462 | 292 | 11.170 | 9,1% | 6.646 |
| 7 | 40.432 | 0,8% | 35,0% | 11.062 | 625 | 10.437 | 9,1% | 5.692 |
| 8 | 41.120 | 1,7% | 35,0% | 11.242 | 972 | 10.270 | 9,1% | 5.132 |
| 9 | 42.189 | 2,6% | 35,0% | 11.526 | 1.342 | 10.183 | 9,2% | 4.661 |
| 10 | 43.666 | 3,5% | 35,0% | 11.921 | 1.389 | 10.531 | 9,2% | 4.414 |
| Terminal | 45.194 | 3,5% | 35,0% | 12.338 | 4.694 | 7.644 | 9,2% | — |

**Disrupción · Deterioro de los fundamentales: Novo pierde relevancia frente a Lilly** — probabilidad 10%; valor terminal 81.792 (VP 34.285); DCF US$22,71 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 41.283 | −10,9% | 45,7% | 14.773 | -6.923 | 21.697 | 9,0% | 19.899 |
| 2 | 38.167 | −7,5% | 41,2% | 12.317 | -4.347 | 16.664 | 9,0% | 14.017 |
| 3 | 36.211 | −5,1% | 39,0% | 11.049 | -2.449 | 13.499 | 9,0% | 10.414 |
| 4 | 35.109 | −3,0% | 36,7% | 10.096 | -2.259 | 12.355 | 9,0% | 8.742 |
| 5 | 34.092 | −2,9% | 34,5% | 9.204 | -1.755 | 10.959 | 9,0% | 7.112 |
| 6 | 33.303 | −2,3% | 32,2% | 8.400 | -526 | 8.926 | 9,1% | 5.311 |
| 7 | 32.724 | −1,7% | 30,0% | 7.674 | -345 | 8.018 | 9,1% | 4.373 |
| 8 | 32.345 | −1,2% | 30,0% | 7.580 | -170 | 7.750 | 9,1% | 3.873 |
| 9 | 32.158 | −0,6% | 30,0% | 7.530 | 0 | 7.530 | 9,2% | 3.447 |
| 10 | 32.158 | −0,0% | 30,0% | 7.525 | 0 | 7.525 | 9,2% | 3.154 |
| Terminal | 32.158 | 0,0% | 30,0% | 7.525 | 0 | 7.525 | 9,2% | — |

**Optimista · La nueva generación recupera el liderazgo** — probabilidad 20%; valor terminal 298.734 (VP 125.221); DCF US$46,89 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 46.432 | 0,2% | 45,7% | 16.616 | 4.022 | 12.594 | 9,0% | 11.550 |
| 2 | 48.243 | 3,9% | 44,9% | 16.971 | 5.709 | 11.262 | 9,0% | 9.473 |
| 3 | 50.812 | 5,3% | 44,6% | 17.720 | 5.345 | 12.375 | 9,0% | 9.547 |
| 4 | 53.217 | 4,7% | 44,2% | 18.398 | 5.078 | 13.320 | 9,0% | 9.424 |
| 5 | 55.502 | 4,3% | 43,8% | 19.019 | 5.100 | 13.919 | 9,0% | 9.032 |
| 6 | 57.797 | 4,1% | 43,4% | 19.616 | 2.089 | 17.527 | 9,1% | 10.428 |
| 7 | 60.095 | 4,0% | 43,0% | 20.199 | 2.086 | 18.114 | 9,1% | 9.878 |
| 8 | 62.389 | 3,8% | 43,0% | 20.955 | 2.075 | 18.880 | 9,1% | 9.434 |
| 9 | 64.672 | 3,7% | 43,0% | 21.707 | 2.058 | 19.649 | 9,2% | 8.994 |
| 10 | 66.935 | 3,5% | 43,0% | 22.450 | 2.130 | 20.320 | 9,2% | 8.518 |
| Terminal | 69.278 | 3,5% | 43,0% | 23.236 | 6.208 | 17.028 | 9,2% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 90.972,05 | 96.868,52 | 187.840,57 | 173.626,37 | 39,27 |
| Conservadora | 84.097,10 | 56.214,59 | 140.311,69 | 126.097,49 | 28,52 |
| Disrupción | 80.339,54 | 34.285,23 | 114.624,77 | 100.410,57 | 22,71 |
| Optimista | 96.279,13 | 125.221,46 | 221.500,60 | 207.286,40 | 46,89 |

Ejemplo Base: (90.972,05 + 96.868,52 + 6.889 + 357 − 21.460) / 4.420,8 = US$39,27 por acción. El terminal representa 51,6% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 40% / 30% / 10% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,40 × 39,274875 + 0,30 × 28,523681 + 0,10 × 22,713212 + 0,20 × 46,888888 = US$35,916153 ≈ US$35,92. Los aportes son US$15,71 + US$8,56 + US$2,27 + US$9,38 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 35,916153 × 0,65 = US$23,345499 ≈ US$23,35. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base ni al antiguo caso técnico de la hoja: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Los DCF completos empiezan en las filas 22 (Base), 46 (Conservadora), 70 (Disrupción) y 94 (Optimista); sus valores por acción están en B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$39,27, es el valor intrínseco principal. El DCF esperado de US$35,92 combina las cuatro tesis con sus probabilidades y se presenta como complemento. La antigua calibración técnica Conservador/Base/Optimista de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: El volumen compensa la caída de precio

**Qué plantea.** Es lo que muestra 2026: volumen creciendo y precio cayendo, con ventas casi planas y margen de ~40%.

**Traducción al modelo.** Obesidad (Wegovy, Saxenda) crece 5%, 10%, 10%, 8%, 7%; Diabetes GLP-1 (Ozempic, Rybelsus) crece -8%, -2%, 0%, 0%, 0%; Insulinas y otros de diabetes crece -5%, -5%, -5%, -5%, -5%; Enfermedades raras crece 2%, 2%, 2%, 2%, 2%. El crecimiento anual compuesto de cinco años es 0,8%; el margen operativo objetivo es 40,0%. El ROIC terminal es 13,1%. El crecimiento terminal es 3,50%, el de la hoja. Probabilidad: 40%; DCF: US$39,27 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (ventas a tipo de cambio constante: +2% (1S26); participación de Novo en prescripciones de obesidad (EE.UU.): Detrás de Lilly; precio realizado de Wegovy/Ozempic en EE.UU.: En fuerte baja). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: Guerra de precios con Lilly y genéricos

**Qué plantea.** Es una guerra de precios con Lilly y genéricos que se aceleran.

**Traducción al modelo.** Obesidad (Wegovy, Saxenda) crece -2%, 4%, 5%, 5%, 4%; Diabetes GLP-1 (Ozempic, Rybelsus) crece -12%, -6%, -4%, -3%, -3%; Insulinas y otros de diabetes crece -7%, -7%, -7%, -7%, -7%; Enfermedades raras crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es −2,8%; el margen operativo objetivo es 35,0%. El ROIC terminal es el costo de capital (9,20%). El crecimiento terminal es 3,50%, el de la hoja. Probabilidad: 30%; DCF: US$28,52 por acción.

**Cómo contrastarla.** La apoyarían: ventas a tipo de cambio constante: negativas; participación de Novo en prescripciones de obesidad (EE.UU.): sigue cayendo; precio realizado de Wegovy/Ozempic en EE.UU.: baja > 15% anual; resultados de CagriSema y amicretin: datos débiles.


#### Disrupción · Deterioro de los fundamentales: Novo pierde relevancia frente a Lilly

**Qué plantea.** Es la pérdida de relevancia frente a Lilly y los orales.

**Traducción al modelo.** Obesidad (Wegovy, Saxenda) crece -8%, -5%, 0%, 2%, 2%; Diabetes GLP-1 (Ozempic, Rybelsus) crece -15%, -10%, -8%, -5%, -5%; Insulinas y otros de diabetes crece -8%, -8%, -8%, -8%, -8%; Enfermedades raras crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es −6,0%; el margen operativo objetivo es 30,0%. El ROIC terminal es el costo de capital (9,20%). El crecimiento terminal es 0,00%: los años 6–10 pasan de −2,9% a ese nivel, sin recuperación. Probabilidad: 10%; DCF: US$22,71 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: ventas a tipo de cambio constante: negativas; participación de Novo en prescripciones de obesidad (EE.UU.): sigue cayendo; precio realizado de Wegovy/Ozempic en EE.UU.: baja > 15% anual; resultados de CagriSema y amicretin: datos débiles.


#### Optimista: La nueva generación recupera el liderazgo

**Qué plantea.** Es la próxima generación de Novo (CagriSema, amicretin, Wegovy pill) recuperando participación.

**Traducción al modelo.** Obesidad (Wegovy, Saxenda) crece 10%, 15%, 15%, 12%, 10%; Diabetes GLP-1 (Ozempic, Rybelsus) crece -4%, 0%, 2%, 2%, 2%; Insulinas y otros de diabetes crece -4%, -4%, -4%, -4%, -4%; Enfermedades raras crece 3%, 3%, 3%, 3%, 3%. El crecimiento anual compuesto de cinco años es 3,7%; el margen operativo objetivo es 43,0%. El ROIC terminal es 13,1%. El crecimiento terminal es 3,50%, el de la hoja. Probabilidad: 20%; DCF: US$46,89 por acción.

**Cómo contrastarla.** La confirmarían: ventas a tipo de cambio constante: ≥ +5% en 2027; participación de Novo en prescripciones de obesidad (EE.UU.): estabiliza; precio realizado de Wegovy/Ozempic en EE.UU.: baja < 10% anual; resultados de CagriSema y amicretin: superioridad o no inferioridad frente a tirzepatida.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 3,50%; Disrupción: 0,00%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,09) | Valor/acción (beta 1,00) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| **Base · El volumen compensa la caída de precio** | 40% | Obesidad (Wegovy, Saxenda): 5%, 10%, 10%, 8%, 7%; Diabetes GLP-1 (Ozempic, Rybelsus): -8%, -2%, 0%, 0%, 0%; Insulinas y otros de diabetes: -5%, -5%, -5%, -5%, -5%; Enfermedades raras: 2%, 2%, 2%, 2%, 2% | 0,8% | 40,0% | 0,5 | 13,1% | 3,50% | US$39,27 | US$39,98 |
| **Conservadora · Guerra de precios con Lilly y genéricos** | 30% | Obesidad (Wegovy, Saxenda): -2%, 4%, 5%, 5%, 4%; Diabetes GLP-1 (Ozempic, Rybelsus): -12%, -6%, -4%, -3%, -3%; Insulinas y otros de diabetes: -7%, -7%, -7%, -7%, -7%; Enfermedades raras: 0%, 0%, 0%, 0%, 0% | −2,8% | 35,0% | 0,5 | = costo de capital | 3,50% | US$28,52 | US$29,00 |
| **Disrupción · Deterioro de los fundamentales: Novo pierde relevancia frente a Lilly** | 10% | Obesidad (Wegovy, Saxenda): -8%, -5%, 0%, 2%, 2%; Diabetes GLP-1 (Ozempic, Rybelsus): -15%, -10%, -8%, -5%, -5%; Insulinas y otros de diabetes: -8%, -8%, -8%, -8%, -8%; Enfermedades raras: 0%, 0%, 0%, 0%, 0% | −6,0% | 30,0% | 0,5 | = costo de capital | 0,00% | US$22,71 | US$23,06 |
| **Optimista · La nueva generación recupera el liderazgo** | 20% | Obesidad (Wegovy, Saxenda): 10%, 15%, 15%, 12%, 10%; Diabetes GLP-1 (Ozempic, Rybelsus): -4%, 0%, 2%, 2%, 2%; Insulinas y otros de diabetes: -4%, -4%, -4%, -4%, -4%; Enfermedades raras: 3%, 3%, 3%, 3%, 3% | 3,7% | 43,0% | 0,5 | 13,1% | 3,50% | US$46,89 | US$47,77 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  |  | **US$35,92** | **US$36,55** |

Base (40%) es lo que muestra 2026: volumen creciendo y precio cayendo, con ventas casi planas y margen de ~40%. Conservadora (30%) es una guerra de precios con Lilly y genéricos que se aceleran. Disrupción (10%) es la pérdida de relevancia frente a Lilly y los orales. Optimista (20%) es la próxima generación de Novo (CagriSema, amicretin, Wegovy pill) recuperando participación. En las historias de erosión (Conservadora y Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF técnico anterior (beta 1,09; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF técnico anterior de la hoja.

| Crecimiento \ Margen | 36,0% | 38,0% | 40,0% | 42,0% | 44,0% |
|---|---:|---:|---:|---:|---:|
| −1,0% | 34,38 | 35,94 | 37,50 | 39,06 | 40,62 |
| 1,0% | 36,70 | 38,48 | 40,25 | 42,03 | 43,80 |
| 3,0% | 39,26 | 41,28 | 43,29 | 45,31 | 47,32 |
| 5,0% | 42,09 | 44,38 | 46,66 | 48,94 | 51,22 |
| 7,0% | 45,22 | 47,80 | 50,38 | 52,96 | 55,54 |


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

Precio de referencia de la valoración guardada: **US$38,14**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 35% | Margen 40% | Margen 44% |
|---|---:|---:|---:|
| Beta 1,09 | 2,9% (62% de las empresas) | −0,5% (77% de las empresas) | −2,7% (86% de las empresas) |
| Beta 1,00 | 2,4% (65% de las empresas) | −1,0% (79% de las empresas) | −3,2% (87% de las empresas) |

Frente al DCF Base (US$39,27), el valor intrínseco principal, el precio está por debajo en 3%.

Frente al DCF esperado de las historias (US$35,92 con la beta de la hoja; US$36,55 con la propuesta), el precio está por encima en 6% y por encima en 4%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Pionera de los GLP-1 en transición: volumen en alza, precio en baja y Lilly adelante |  |
| Probabilidades | Base 40% / Conservadora 30% / Disrupción 10% / Optimista 20% |  |
| DCF Base hoy (valor intrínseco principal) | US$39,27 |  |
| DCF esperado por probabilidades (complemento) (beta de la hoja / propuesta) | US$35,92 / US$36,55 |  |
| Precio con MOS sobre el DCF esperado | US$23,35 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$22,71 a US$47,77 |  |
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
