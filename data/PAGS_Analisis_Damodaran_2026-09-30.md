---
schema: "jmr-analisis-damodaran-v1"
ticker: "PAGS"
analysis_date: "2026-09-30"
---

# PagSeguro Digital Ltd. (PAGS) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$11,89 por acción** (Base · Banco digital estable con ROAE de ~15%).

**Complemento · DCF esperado por probabilidades: US$11,60.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$9,99–12,73. El MOS 35% se aplica al esperado: US$7,54. El antiguo caso técnico de la hoja (US$11,92) se conserva solo como calibración; no es el DCF Base. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: balance del último 10-q, capital invertido operativo, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet (12 celdas, con respaldo). DCF esperado US$11,60 → US$11,60. Salvedades abiertas: Arrendamientos: bajo NIIF 16 todos los arrendamientos están en el balance y el EBIT ya excluye su costo financiero, así que su pasivo es deuda; se conserva en la deuda del DCF. Financiera (DCF de flujo al accionista): balance y flujos LTM actualizados con el 20-F 2025 y el 6-K del 1S26 (convertidos a los tipos implícitos de la hoja); no afectan al valor, que depende de utilidad, ROE y costo del patrimonio. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de US$11,92 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

PagSeguro (PagBank) nació procesando pagos con tarjeta para microcomercios en Brasil y se está convirtiendo en un banco digital: cuentas, depósitos, crédito e inversiones que financian su propia operación. La adquirencia es un negocio maduro y deflacionario (el PIX, pago instantáneo gratuito, reemplaza a la tarjeta de débito; los ingresos por transacciones cayeron de R$9.183 millones en 2024 a R$8.159 millones en 2025), mientras el banco reduce el costo de fondeo y sostiene utilidades: R$2.118 millones en 2025, ROAE de 15,6% y Basilea de 22,5% en el 2T26. La acción cotiza a ~6 veces utilidades y por debajo del valor en libros. La historia de cinco años es si PagBank es un banco digital rentable y estable o un adquirente en declive con un banco que no alcanza a compensar.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~6% anual cinco años | Sí | Sí: +8,5% en 2025 en reales; la adquirencia cae y el banco crece | Media |
| El ROAE se mantiene en ~15% | Sí | Sí: estable en 15-16% con capital holgado | Probable |
| El PIX destruye la adquirencia | Sí | Parcialmente: el débito cae; el crédito y la anticipación resisten | Posible, gradual |
| Una crisis de crédito en Brasil golpea la cartera | Sí | Sí con tasas altas; la cartera es pequeña y conservadora | Baja-media |


### Visión externa: tasas base

Con ventas LTM de US$3.892 millones (US$2.753 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **$2,000-3,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 6,2% y una mediana de 5,1% (desviación estándar 8,9%); sumando una inflación de 2,5%, la mediana nominal ronda 7,6%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · Banco digital estable con ROAE de ~15% | 5,6% | 63% |
| Conservadora · El PIX y la competencia erosionan | 1,4% | 85% |
| Disrupción · Deterioro de los fundamentales: Crisis de crédito en Brasil | −0,4% | 89% |
| Optimista · Crece el banco: crédito y depósitos | 9,0% | 42% |

En dólares de 2015 la empresa está en el tramo de US$2.000-3.000 millones: crecer 5,6% anual cinco años (Base) lo logró ~63% de las empresas de ese tamaño; 9,0% (Optimista), ~42%. La hoja (6%) es normal. En una financiera, el valor depende más del retorno sobre el patrimonio frente al costo del patrimonio (~12-15% en Brasil) que del crecimiento.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Qué se valora: un banco, no un procesador.** PagSeguro nació procesando pagos con tarjeta para microcomercios en Brasil y se está convirtiendo en un banco digital (PagBank): cuentas, depósitos, crédito e inversiones que financian su propia operación. Por eso se valora con un DCF de flujos al accionista (FCFE), como una financiera: en un banco la deuda y los depósitos son materia prima del negocio, no financiamiento que haya que restar, y lo que importa es cuánto rinde el patrimonio (ROE) frente a lo que cuesta (el costo del patrimonio). La adquirencia es un negocio maduro y deflacionario: el PIX, pago instantáneo gratuito, reemplaza a la tarjeta de débito, y los ingresos por transacciones cayeron de R$9.183 millones en 2024 a R$8.159 millones en 2025. El banco compensa: utilidad de R$2.118 millones en 2025 y ROAE de 15,6% en el 2T26.

**Crecimiento: la adquirencia cae, el banco crece.** La Base supone que las transacciones caen 3% y se estabilizan mientras los ingresos financieros y de banca crecen 8-10%: el total crece 4,8% el primer año y 5,6% compuesto, una cifra que lograron ~63% de las empresas de su tamaño. El crecimiento que mueve el valor es el de la utilidad, que la hoja supone en 5% el primer año y 6% después. La Conservadora (1,4%) es la erosión por el PIX y por Nubank, Mercado Pago y Stone; la Disrupción (−0,4%), una crisis de crédito; la Optimista (9,0%), un banco que crece a doble dígito. Si el volumen de pagos entra en caída, la Base pierde sustento. El crecimiento casi no mueve el valor (±2 puntos: US$11,60 (−2%) y US$12,18 (+2%)), porque crecer exige retener capital: en un banco, crecer con un ROE apenas por encima del costo del patrimonio crea poco valor.

**ROE: el supuesto central.** La Base usa un ROE de 15,6%, el ROAE ajustado del 2T26 (comunicado del 11-ago-2026), que después del año 5 converge al costo del patrimonio terminal: ningún banco sostiene para siempre un retorno por encima de su costo de capital sin una ventaja, y PagBank no tiene una barrera durable frente al PIX y los bancos digitales. La Conservadora usa 13,0%, la Disrupción 10,0% y la Optimista 17,0%. La parte de la utilidad que se retiene para crecer es utilidad × crecimiento / ROE; el resto es el flujo del accionista. El índice de Basilea de 22,5% muestra holgura de capital, pero no se suma como valor extra porque no hay evidencia de que sea distribuible. Un ROAE por debajo de 12% invalidaría la Base; dos puntos de ROE la mueven a US$11,51 (−3%) o US$12,19 (+3%).

**Descuento: Brasil cuesta caro.** El costo del patrimonio empieza en 14,70% (beta 1,30, prima de riesgo 7,47%, que incluye el riesgo país) y converge a 12,00%. Es el supuesto que más mueve el valor: un punto más lo lleva a US$10,82 (−9%); uno menos, a US$13,18 (+11%). Una beta sectorial menor (~0,97) se considera solo como sensibilidad, porque el riesgo de un banco en Brasil no es el de una financiera promedio de EE.UU. El crecimiento perpetuo en dólares es 3,00% y el terminal explica 46,5% del valor.

**Probabilidades y lectura del resultado.** La Base pesa 45%, la Conservadora 30%, la Disrupción 10% y la Optimista 15%. Las cuatro historias están cerca (US$9,99 a US$12,73) porque, con el ROE convergiendo al costo del patrimonio, ninguna crea mucho valor por crecer: la diferencia está en cuánto rinde el capital que ya tiene. El DCF Base es US$11,89 y el esperado US$11,60, frente a un precio de US$8,96: el mercado paga menos que la Disrupción, es decir, descuenta un ROE o un riesgo país peor que el de cualquier historia, o desconfía de la calidad de la cartera de crédito. Las acciones se fijan en 276,0 millones; el real frente al dólar es un riesgo que este DCF en dólares no aísla.

**Del supuesto al valor: cómo se calcula la Base.** El punto de partida es la utilidad del último año, US$407 millones. Cada año crece con la trayectoria de la Base y llega a US$533 millones en el año 5 y US$653 millones en el año 10. No toda esa utilidad se puede repartir: para crecer, un banco o una financiera tiene que retener capital, y la parte retenida es utilidad × crecimiento / ROE. Lo que queda es el flujo del accionista (FCFE): US$295 millones el primer año. Esos flujos se traen a hoy con el costo del patrimonio, que empieza en 14,70% y baja a 12,00%; suman US$1.756 millones. Después del año 10 se supone un crecimiento perpetuo de 3,00%: el valor de esa perpetuidad, traído a hoy, es US$1.526 millones. La suma es el valor del patrimonio, US$3.282 millones; dividido entre 276,0 millones de acciones da US$11,89 por acción. Aquí no se resta deuda: en una financiera la deuda es materia prima del negocio y ya está dentro del flujo del accionista.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 3,01× (peso 0% dentro de los múltiplos); EV/FCFF 2,51× (peso 0% dentro de los múltiplos); P/E 9,25× (peso 58% dentro de los múltiplos); P/FCFE 7,88× (peso 33% dentro de los múltiplos); P/OCF 3,27× (peso 8% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (14,7%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$11,89; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| ROE −2 pp | US$11,51 | −3,2% |
| ROE +2 pp | US$12,19 | +2,5% |
| Crecimiento años 1–5 −2 pp | US$11,60 | −2,5% |
| Crecimiento años 1–5 +2 pp | US$12,18 | +2,4% |
| Ke +1 pp | US$10,82 | −9,0% |
| Ke −1 pp | US$13,18 | +10,8% |
| Crecimiento terminal −0,5 pp | US$11,85 | −0,3% |
| Crecimiento terminal +0,5 pp | US$11,93 | +0,3% |
| Acciones +5% | US$11,33 | −4,8% |


### Piezas del valor

**Crecimiento.** En dólares (hoja): US$3.193 millones (2023), US$3.495 millones (2024, +9,4%) y US$3.653 millones (2025, +4,5%); LTM US$3.892 millones. En reales, ingresos y rendimientos de R$20.411 millones en 2025 (+8,5%); transacciones R$8.159 millones (en baja) y el resto ingresos financieros. La división de las historias (~40% transacciones, ~60% financieros y banca) es un cálculo propio.

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 3.193 | 3.495 | 3.653 | 3.892 |
| Crecimiento | +7,5% | +9,4% | +4,5% | — |
| Margen (utilidad antes de impuestos) | 12,6% | 12,7% | 12,5% | 12,6% |
| FCFF (hoja) | −845 | −333 | 703 | — |

**Márgenes.** Para PagBank la rentabilidad relevante es el ROE, no el margen EBIT. El DCF de flujos al accionista parte de utilidad LTM de US$406,6 millones, 276 millones de acciones, ROE Base de 15,6%, crecimiento de beneficios de 5% el primer año y 6% en años 2-5. El ROE se desvanece al costo del patrimonio terminal de 12%; crecimiento estable en dólares de 3%. ROE de 13%/17% delimitan los escenarios. Son supuestos del analista, no guía; la cifra de ROAE ajustado de 15,6% procede del comunicado 2T de 11-ago-2026.

**Reinversión y retorno.** La reinversión patrimonial se estima como utilidad × crecimiento / ROE; el FCFE es utilidad menos esa retención. Se descuenta al Ke de 14,7%, que converge a 12%. No se suma la liquidez bancaria ni se restan depósitos. El 22,5% de Basilea reportado en 2T muestra holgura, pero no identifica por sí solo capital distribuible: no se agrega un valor por exceso de capital no comprobado. La aproximación requiere que crecimiento de ingresos y beneficios sea comparable; la sensibilidad debe revisarse si cambia el riesgo de crédito o el capital regulatorio. Sin ventaja defendible: no tiene una barrera durable frente a Pix y los bancos digitales, y su ROIC apenas supera el costo de capital. El ROIC después del año 10 es igual al costo de capital, el supuesto por defecto de Damodaran: el crecimiento posterior no suma valor.

**Riesgo.** La beta de la hoja es 1,30; el Ke inicial es 14,7%. La beta sectorial propuesta de 0,97 se evalúa como sensibilidad al costo del patrimonio. Se usa FCFE financiero y el ROE converge al Ke terminal; los depósitos y la caja operativa bancaria no son deuda y caja excedente de una industrial.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF técnico anterior por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,30 | 14,7% | 14,7% | US$11,92 |
| Bottom-up del sector (Financial Svcs. (Non-bank & Insurance), reapalancada) | 0,33 | 7,5% | 7,5% | US$17,34 |
| Propuesta (sector ajustado por riesgo propio) | 0,97 | 12,2% | 12,2% | US$13,49 |


### DCF financiero: supuestos y limitaciones

Para PagBank la rentabilidad relevante es el ROE, no el margen EBIT. El DCF de flujos al accionista parte de utilidad LTM de US$406,6 millones, 276 millones de acciones, ROE Base de 15,6%, crecimiento de beneficios de 5% el primer año y 6% en años 2-5. El ROE se desvanece al costo del patrimonio terminal de 12%; crecimiento estable en dólares de 3%. ROE de 13%/17% delimitan los escenarios. Son supuestos del analista, no guía; la cifra de ROAE ajustado de 15,6% procede del comunicado 2T de 11-ago-2026. La reinversión patrimonial se estima como utilidad × crecimiento / ROE; el FCFE es utilidad menos esa retención. Se descuenta al Ke de 14,7%, que converge a 12%. No se suma la liquidez bancaria ni se restan depósitos. El 22,5% de Basilea reportado en 2T muestra holgura, pero no identifica por sí solo capital distribuible: no se agrega un valor por exceso de capital no comprobado. La aproximación requiere que crecimiento de ingresos y beneficios sea comparable; la sensibilidad debe revisarse si cambia el riesgo de crédito o el capital regulatorio. Sin ventaja defendible: no tiene una barrera durable frente a Pix y los bancos digitales, y su ROIC apenas supera el costo de capital. El ROIC después del año 10 es igual al costo de capital, el supuesto por defecto de Damodaran: el crecimiento posterior no suma valor.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$11,89 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$11,60. Cada historia tiene su propia trayectoria de beneficios, ROE objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene aplicando descuentos al antiguo caso técnico de la hoja (US$11,92) ni mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Utilidad neta base | US$407 millones | «DCF FCFE financiero» B3: utilidad LTM del año base. |
| ROE objetivo | Base: 15,6%; Conservadora: 13,0%; Disrupción: 10,0%; Optimista: 17,0% | Años 1–5 al ROE de la historia; converge al Ke terminal en los años 6–10. |
| Descuento | Ke 14,70% → 12,00% | Costo del patrimonio de la hoja; tasa libre de riesgo 4,99%, beta 1,30, ERP 7,47%. Igual en las cuatro historias. |
| Crecimiento perpetuo | Base/Conservadora/Disrupción/Optimista: 3,00% | Terminal de la hoja («DCF FCFE financiero» B5) en las historias que no lo cambian. |
| Acciones | 276,0 millones | Valuation output B34. En FCFE no se resta deuda: el flujo ya es del accionista. |


#### 2. De la utilidad al flujo del accionista

Utilidadₜ = utilidadₜ₋₁ × (1 + crecimientoₜ). Reinversión patrimonial = utilidad × crecimiento / ROE; FCFE = utilidad − reinversión. En la Base, año 1: utilidad US$426,12 millones, reinversión US$131,15 millones y FCFE US$294,97 millones. Se descuenta al costo del patrimonio; en perpetuidad, FCFE₁₁ = utilidad₁₁ × (1 − g / Ke terminal) y valor terminal = FCFE₁₁ / (Ke terminal − g). No se resta deuda.


#### 3. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en «Escenarios e historias»: utilidad, crecimiento, ROE, reinversión patrimonial, flujo al accionista (FCFE), costo del patrimonio y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · Banco digital estable con ROAE de ~15%** — probabilidad 45%; valor terminal 5.601,1 (VP 1.526,0); DCF US$11,89 por acción.

| Año | Utilidad | Crecimiento | ROE | Reinversión | FCFE | Ke | VP del FCFE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 426,1 | 4,8% | 15,6% | 131,2 | 295,0 | 14,7% | 257,2 |
| 2 | 449,8 | 5,6% | 15,6% | 160,3 | 289,5 | 14,7% | 220,1 |
| 3 | 476,4 | 5,9% | 15,6% | 180,4 | 296,0 | 14,7% | 196,1 |
| 4 | 503,7 | 5,7% | 15,6% | 185,0 | 318,7 | 14,7% | 184,1 |
| 5 | 533,0 | 5,8% | 15,6% | 199,2 | 333,8 | 14,7% | 168,1 |
| 6 | 561,1 | 5,3% | 14,9% | 198,5 | 362,6 | 14,2% | 160,0 |
| 7 | 587,5 | 4,7% | 14,2% | 194,9 | 392,5 | 13,6% | 152,4 |
| 8 | 611,7 | 4,1% | 13,4% | 188,1 | 423,7 | 13,1% | 145,5 |
| 9 | 633,5 | 3,6% | 12,7% | 177,6 | 455,9 | 12,5% | 139,1 |
| 10 | 652,6 | 3,0% | 12,0% | 163,1 | 489,4 | 12,0% | 133,3 |
| Terminal | 672,1 | 3,0% | 12,0% | 168,0 | 504,1 | 12,0% | — |

**Conservadora · El PIX y la competencia erosionan** — probabilidad 30%; valor terminal 4.301,6 (VP 1.172,0); DCF US$11,14 por acción.

| Año | Utilidad | Crecimiento | ROE | Reinversión | FCFE | Ke | VP del FCFE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 405,8 | −0,2% | 13,0% | 0,0 | 405,8 | 14,7% | 353,8 |
| 2 | 409,6 | 0,9% | 13,0% | 29,8 | 379,9 | 14,7% | 288,7 |
| 3 | 416,0 | 1,6% | 13,0% | 50,2 | 365,9 | 14,7% | 242,5 |
| 4 | 424,8 | 2,1% | 13,0% | 69,0 | 355,9 | 14,7% | 205,6 |
| 5 | 435,8 | 2,6% | 13,0% | 86,7 | 349,1 | 14,7% | 175,9 |
| 6 | 447,4 | 2,7% | 12,8% | 93,3 | 354,2 | 14,2% | 156,3 |
| 7 | 459,7 | 2,8% | 12,6% | 100,4 | 359,4 | 13,6% | 139,5 |
| 8 | 472,8 | 2,8% | 12,4% | 108,1 | 364,7 | 13,1% | 125,2 |
| 9 | 486,6 | 2,9% | 12,2% | 116,3 | 370,2 | 12,5% | 113,0 |
| 10 | 501,2 | 3,0% | 12,0% | 125,3 | 375,9 | 12,0% | 102,4 |
| Terminal | 516,2 | 3,0% | 12,0% | 129,0 | 387,1 | 12,0% | — |

**Disrupción · Deterioro de los fundamentales: Crisis de crédito en Brasil** — probabilidad 10%; valor terminal 3.980,4 (VP 1.084,4); DCF US$9,99 por acción.

| Año | Utilidad | Crecimiento | ROE | Reinversión | FCFE | Ke | VP del FCFE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 378,1 | −7,0% | 10,0% | 0,0 | 378,1 | 14,7% | 329,7 |
| 2 | 370,8 | −1,9% | 10,0% | 0,0 | 370,8 | 14,7% | 281,9 |
| 3 | 373,6 | 0,8% | 10,0% | 28,0 | 345,6 | 14,7% | 229,0 |
| 4 | 385,5 | 3,2% | 10,0% | 123,2 | 262,4 | 14,7% | 151,6 |
| 5 | 398,1 | 3,3% | 10,0% | 129,4 | 268,7 | 14,7% | 135,3 |
| 6 | 410,8 | 3,2% | 10,4% | 126,4 | 284,4 | 14,2% | 125,5 |
| 7 | 423,8 | 3,2% | 10,8% | 123,6 | 300,1 | 13,6% | 116,6 |
| 8 | 436,9 | 3,1% | 11,2% | 120,9 | 316,0 | 13,1% | 108,5 |
| 9 | 450,2 | 3,1% | 11,6% | 118,4 | 331,8 | 12,5% | 101,3 |
| 10 | 463,7 | 3,0% | 12,0% | 115,9 | 347,8 | 12,0% | 94,8 |
| Terminal | 477,6 | 3,0% | 12,0% | 119,4 | 358,2 | 12,0% | — |

**Optimista · Crece el banco: crédito y depósitos** — probabilidad 15%; valor terminal 6.845,1 (VP 1.864,9); DCF US$12,73 por acción.

| Año | Utilidad | Crecimiento | ROE | Reinversión | FCFE | Ke | VP del FCFE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 443,2 | 9,0% | 17,0% | 234,7 | 208,5 | 14,7% | 181,8 |
| 2 | 485,7 | 9,6% | 17,0% | 274,2 | 211,5 | 14,7% | 160,8 |
| 3 | 532,3 | 9,6% | 17,0% | 300,1 | 232,2 | 14,7% | 153,8 |
| 4 | 580,8 | 9,1% | 17,0% | 311,3 | 269,5 | 14,7% | 155,7 |
| 5 | 626,6 | 7,9% | 17,0% | 290,4 | 336,2 | 14,7% | 169,3 |
| 6 | 669,8 | 6,9% | 16,0% | 289,0 | 380,8 | 14,2% | 168,0 |
| 7 | 709,5 | 5,9% | 15,0% | 280,4 | 429,1 | 13,6% | 166,6 |
| 8 | 744,7 | 5,0% | 14,0% | 263,4 | 481,3 | 13,1% | 165,3 |
| 9 | 774,3 | 4,0% | 13,0% | 236,8 | 537,5 | 12,5% | 164,0 |
| 10 | 797,5 | 3,0% | 12,0% | 199,4 | 598,1 | 12,0% | 163,0 |
| Terminal | 821,4 | 3,0% | 12,0% | 205,4 | 616,1 | 12,0% | — |


#### 4. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFE años 1–10 | VP terminal | Patrimonio | DCF/acción |
|---|---:|---:|---:|---:|
| Base | 1.756,01 | 1.525,98 | 3.281,99 | 11,89 |
| Conservadora | 1.902,86 | 1.171,96 | 3.074,82 | 11,14 |
| Disrupción | 1.673,96 | 1.084,44 | 2.758,39 | 9,99 |
| Optimista | 1.648,31 | 1.864,91 | 3.513,22 | 12,73 |

Ejemplo Base: (1.756,01 + 1.525,98) / 276,0 = US$11,89 por acción.


#### 5. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 45% / 30% / 10% / 15% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,45 × 11,891268 + 0,30 × 11,140644 + 0,10 × 9,994179 + 0,15 × 12,729057 = US$11,602040 ≈ US$11,60. Los aportes son US$5,35 + US$3,34 + US$1,00 + US$1,91 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 11,602040 × 0,65 = US$7,541326 ≈ US$7,54. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base ni al antiguo caso técnico de la hoja: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Los DCF completos empiezan en las filas 22 (Base), 46 (Conservadora), 70 (Disrupción) y 94 (Optimista); sus valores por acción están en B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$11,89, es el valor intrínseco principal. El DCF esperado de US$11,60 combina las cuatro tesis con sus probabilidades y se presenta como complemento. La antigua calibración técnica Conservador/Base/Optimista de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: Banco digital estable con ROAE de ~15%

**Qué plantea.** Es lo que muestra 2025-2026: adquirencia estancada, banco creciendo, ROAE ~15%.

**Traducción al modelo.** Transacciones (adquirencia) crece -3%, -2%, 0%, 1%, 1%; Ingresos financieros y banca crece 10%, 10%, 9%, 8%, 8%. El crecimiento anual compuesto de cinco años es 5,6%; el ROE objetivo es 15,6%. El crecimiento terminal es 3,00%, el de la hoja. Probabilidad: 45%; DCF: US$11,89 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (ROAE: 15,6% (2T26); volumen de pagos (TPV): Estable; depósitos y cartera de crédito: Creciendo). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: El PIX y la competencia erosionan

**Qué plantea.** Es la erosión por el PIX y la competencia de Nubank, Mercado Pago y Stone.

**Traducción al modelo.** Transacciones (adquirencia) crece -8%, -6%, -5%, -4%, -3%; Ingresos financieros y banca crece 5%, 5%, 5%, 5%, 5%. El crecimiento anual compuesto de cinco años es 1,4%; el ROE objetivo es 13,0%. El crecimiento terminal es 3,00%, el de la hoja. Probabilidad: 30%; DCF: US$11,14 por acción.

**Cómo contrastarla.** La apoyarían: ROAE: < 12%; volumen de pagos (TPV): en caída; depósitos y cartera de crédito: estancados; morosidad (90 días): en alza dos trimestres.


#### Disrupción · Deterioro de los fundamentales: Crisis de crédito en Brasil

**Qué plantea.** Es una crisis de crédito con morosidad en alza.

**Traducción al modelo.** Transacciones (adquirencia) crece -10%, -5%, -3%, 0%, 0%; Ingresos financieros y banca crece -5%, 0%, 3%, 5%, 5%. El crecimiento anual compuesto de cinco años es −0,4%; el ROE objetivo es 10,0%. El crecimiento terminal es 3,00%, el de la hoja. Probabilidad: 10%; DCF: US$9,99 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: ROAE: < 12%; volumen de pagos (TPV): en caída; depósitos y cartera de crédito: estancados; morosidad (90 días): en alza dos trimestres.


#### Optimista: Crece el banco: crédito y depósitos

**Qué plantea.** Es un banco digital que crece a doble dígito.

**Traducción al modelo.** Transacciones (adquirencia) crece 0%, 2%, 3%, 3%, 3%; Ingresos financieros y banca crece 15%, 14%, 13%, 12%, 10%. El crecimiento anual compuesto de cinco años es 9,0%; el ROE objetivo es 17,0%. El crecimiento terminal es 3,00%, el de la hoja. Probabilidad: 15%; DCF: US$12,73 por acción.

**Cómo contrastarla.** La confirmarían: ROAE: ≥ 15%; volumen de pagos (TPV): creciendo ≥ 5%; depósitos y cartera de crédito: ≥ +15%; morosidad (90 días): estable.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento. Crecimiento terminal: Base/Conservadora/Disrupción/Optimista: 3,00%. Las diferencias proceden de beneficios, ROE y crecimiento terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | ROE objetivo | Reinversión patrimonial | Crecimiento terminal | Valor/acción (beta 1,30) | Valor/acción (beta 0,97) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **Base · Banco digital estable con ROAE de ~15%** | 45% | Transacciones (adquirencia): -3%, -2%, 0%, 1%, 1%; Ingresos financieros y banca: 10%, 10%, 9%, 8%, 8% | 5,6% | 15,6% | 1,4 | 3,00% | US$11,89 | US$13,44 |
| **Conservadora · El PIX y la competencia erosionan** | 30% | Transacciones (adquirencia): -8%, -6%, -5%, -4%, -3%; Ingresos financieros y banca: 5%, 5%, 5%, 5%, 5% | 1,4% | 13,0% | 1,4 | 3,00% | US$11,14 | US$12,47 |
| **Disrupción · Deterioro de los fundamentales: Crisis de crédito en Brasil** | 10% | Transacciones (adquirencia): -10%, -5%, -3%, 0%, 0%; Ingresos financieros y banca: -5%, 0%, 3%, 5%, 5% | −0,4% | 10,0% | 1,4 | 3,00% | US$9,99 | US$11,18 |
| **Optimista · Crece el banco: crédito y depósitos** | 15% | Transacciones (adquirencia): 0%, 2%, 3%, 3%, 3%; Ingresos financieros y banca: 15%, 14%, 13%, 12%, 10% | 9,0% | 17,0% | 1,4 | 3,00% | US$12,73 | US$14,50 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  | **US$11,60** | **US$13,08** |

Base (45%) es lo que muestra 2025-2026: adquirencia estancada, banco creciendo, ROAE ~15%. Conservadora (30%) es la erosión por el PIX y la competencia de Nubank, Mercado Pago y Stone. Disrupción (10%) es una crisis de crédito con morosidad en alza. Optimista (15%) es un banco digital que crece a doble dígito. En las historias de erosión (Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF técnico anterior (beta 1,30; US$ por acción; filas = crecimiento de los años 1-5, columnas = ROE objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF técnico anterior de la hoja.

| Crecimiento \ Margen | 11,6% | 13,6% | 15,6% | 17,6% | 19,6% |
|---|---:|---:|---:|---:|---:|
| 1,8% | 11,06 | 11,21 | 11,34 | 11,43 | 11,51 |
| 3,8% | 11,04 | 11,38 | 11,63 | 11,83 | 11,99 |
| 5,8% | 10,99 | 11,52 | 11,92 | 12,24 | 12,50 |
| 7,8% | 10,88 | 11,64 | 12,21 | 12,66 | 13,02 |
| 9,8% | 10,72 | 11,73 | 12,49 | 13,08 | 13,57 |


### Pre-mortem

1. El PIX con crédito (PIX parcelado) reemplaza también a la tarjeta de crédito y la adquirencia se derrumba.
2. Nubank y Mercado Pago capturan a los microcomercios con cuentas y crédito gratis.
3. Las tasas altas en Brasil elevan la morosidad y obligan a más provisiones.
4. El real se deprecia y el valor en dólares cae aunque el negocio vaya bien en reales.
5. Cambios regulatorios (tarifas de intercambio, anticipación) bajan la rentabilidad.

**Evidencia en contra de la historia más probable:** los ingresos por transacciones caen y el crecimiento en dólares bajó a 4,5%; si el banco no acelera, Conservadora se vuelve la historia central.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| ROAE | 15,6% (2T26) | ≥ 15% | < 12% |
| Volumen de pagos (TPV) | Estable | Creciendo ≥ 5% | En caída |
| Depósitos y cartera de crédito | Creciendo | ≥ +15% | Estancados |
| Morosidad (90 días) | Controlada | Estable | En alza dos trimestres |
| Índice de Basilea | 22,5% | ≥ 18% con dividendos | < 16% |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$8,96**.

DCF inverso: crecimiento anual de beneficios en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 13% | Margen 16% | Margen 17% |
|---|---:|---:|---:|
| Beta 1,30 | −4,6% (96% de las empresas) | −4,6% (96% de las empresas) | −4,6% (96% de las empresas) |
| Beta 0,97 | −6,7% (97% de las empresas) | −6,7% (97% de las empresas) | −6,7% (97% de las empresas) |

Frente al DCF Base (US$11,89), el valor intrínseco principal, el precio está por debajo en 25%.

Frente al DCF esperado de las historias (US$11,60 con la beta de la hoja; US$13,08 con la propuesta), el precio está por debajo en 23% y por debajo en 32%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Adquirente en declive que se convierte en banco digital rentable en Brasil |  |
| Probabilidades | Base 45% / Conservadora 30% / Disrupción 10% / Optimista 15% |  |
| DCF Base hoy (valor intrínseco principal) | US$11,89 |  |
| DCF esperado por probabilidades (complemento) (beta de la hoja / propuesta) | US$11,60 / US$13,08 |  |
| Precio con MOS sobre el DCF esperado | US$7,54 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$9,99 a US$14,50 |  |
| Confianza | Media-baja: país, tasas y competencia dominan el resultado |  |
| Qué cambiaría la opinión | ROAE, morosidad y crecimiento de depósitos y crédito |  |
| Revisión | Resultados del 3T26 (nov-2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [PagSeguro, comunicado de resultados del 2T 2026 (6-K)](https://www.sec.gov/Archives/edgar/data/1712807/000155485526001793/MainDocument.htm)
- [PagSeguro, 6-K sobre dividendos 2027-2028 (sep-2026)](https://www.sec.gov/Archives/edgar/data/1712807/000155485526001939/MainDocument.htm)
- [PagSeguro, Form 20-F 2025](https://www.sec.gov/Archives/edgar/data/1712807/000155485526000826/pags-20251231.htm)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
