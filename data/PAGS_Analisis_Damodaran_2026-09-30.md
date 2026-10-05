---
schema: "jmr-analisis-damodaran-v1"
ticker: "PAGS"
analysis_date: "2026-09-30"
---

# PagSeguro Digital Ltd. (PAGS) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$12,06 por acción** (Base · Banco digital estable con ROAE de ~15%).

**Complemento · DCF esperado por probabilidades: US$11,49.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$9,21–13,10. El MOS 35% se aplica al esperado: US$7,47. El antiguo caso técnico de la hoja (US$12,08) se conserva solo como calibración; no es el DCF Base. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: balance del último 10-q, capital invertido operativo, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet (12 celdas, con respaldo). DCF esperado US$11,60 → US$11,49. Salvedades abiertas: Arrendamientos: bajo NIIF 16 todos los arrendamientos están en el balance y el EBIT ya excluye su costo financiero, así que su pasivo es deuda; se conserva en la deuda del DCF. Financiera (DCF de flujo al accionista): balance y flujos LTM actualizados con el 20-F 2025 y el 6-K del 1S26 (convertidos a los tipos implícitos de la hoja); no afectan al valor, que depende de utilidad, ROE y costo del patrimonio. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de US$12,08 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


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

**Crecimiento: la adquirencia cae, el banco crece.** La Base supone que las transacciones caen 3% y se estabilizan mientras los ingresos financieros y de banca crecen 8-10%: el total crece 4,8% el primer año y 5,6% compuesto, una cifra que lograron ~63% de las empresas de su tamaño. El crecimiento que mueve el valor es el de la utilidad, que la hoja supone en 5% el primer año y 6% después. La Conservadora (1,4%) es la erosión por el PIX y por Nubank, Mercado Pago y Stone; la Disrupción (−0,4%), una crisis de crédito; la Optimista (9,0%), un banco que crece a doble dígito. Si el volumen de pagos entra en caída, la Base pierde sustento. El crecimiento casi no mueve el valor (±2 puntos: US$11,94 (−1,0%) y US$12,18 (+1%)), porque crecer exige retener capital: en un banco, crecer con un ROE apenas por encima del costo del patrimonio crea poco valor.

**ROE: el supuesto central.** La Base usa un ROE de 15,6%, el ROAE ajustado del 2T26 (comunicado del 11-ago-2026), que después del año 5 converge al costo del patrimonio terminal: ningún banco sostiene para siempre un retorno por encima de su costo de capital sin una ventaja, y PagBank no tiene una barrera durable frente al PIX y los bancos digitales. La Conservadora usa 13,0%, la Disrupción 10,0% y la Optimista 17,0%. La utilidad es ROE × patrimonio contable del año anterior y lo que se retiene para crecer es el aumento del patrimonio; el resto es el flujo del accionista. El índice de Basilea de 22,5% muestra holgura de capital, pero no se suma como valor extra porque no hay evidencia de que sea distribuible. Un ROAE por debajo de 12% invalidaría la Base; dos puntos de ROE la mueven a US$11,01 (−9%) o US$13,11 (+9%).

**Descuento: Brasil cuesta caro.** El costo del patrimonio empieza en 11,30% (beta 0,82, prima de riesgo 7,33%, que incluye el riesgo país) y converge a 12,30%. Es el supuesto que más mueve el valor: un punto más lo lleva a US$11,48 (−5%); uno menos, a US$12,68 (+5%). La beta es la del patrimonio de las financieras no bancarias en la tabla global; el riesgo de Brasil ya está en la prima y no se cuenta otra vez en la beta. La regresión (0,80-1,42 contra el S&P 500) queda como referencia. El crecimiento perpetuo en dólares es 3,00% y el terminal explica 43,6% del valor.

**Probabilidades y lectura del resultado.** La Base pesa 45%, la Conservadora 30%, la Disrupción 10% y la Optimista 15%. Las cuatro historias están cerca (US$9,21 a US$13,10) porque, con el ROE convergiendo al costo del patrimonio, ninguna crea mucho valor por crecer: la diferencia está en cuánto rinde el capital que ya tiene. El DCF Base es US$12,06 y el esperado US$11,49, frente a un precio de US$8,90: el mercado paga menos que la Disrupción, es decir, descuenta un ROE o un riesgo país peor que el de cualquier historia, o desconfía de la calidad de la cartera de crédito. Las acciones se fijan en 279,5 millones; el real frente al dólar es un riesgo que este DCF en dólares no aísla.

**Del supuesto al valor: cómo se calcula la Base.** El punto de partida es la utilidad del último año, US$407 millones. Cada año es el ROE de la Base por el patrimonio contable del año anterior: US$530 millones en el año 5 y US$526 millones en el año 10, cuando el ROE ya bajó al costo del patrimonio. No toda esa utilidad se puede repartir: para crecer, un banco o una financiera tiene que aumentar su patrimonio al mismo ritmo, y esa parte se retiene. Lo que queda es el flujo del accionista (FCFE): US$296 millones el primer año. Esos flujos se traen a hoy con el costo del patrimonio, que empieza en 11,30% y baja a 12,30%; suman US$1.902 millones. Después del año 10 se supone un crecimiento perpetuo de 3,00%: el valor de esa perpetuidad, traído a hoy, es US$1.469 millones. La suma es el valor del patrimonio, US$3.370 millones; dividido entre 279,5 millones de acciones da US$12,06 por acción. Aquí no se resta deuda: en una financiera la deuda es materia prima del negocio y ya está dentro del flujo del accionista.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 2,70× (peso 0% dentro de los múltiplos); EV/FCFF 2,25× (peso 0% dentro de los múltiplos); P/E 10,38× (peso 64% dentro de los múltiplos); P/FCFE 9,62× (peso 36% dentro de los múltiplos); P/OCF 4,93× (peso 0% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (11,3%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$12,06; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| ROE −2 pp | US$11,01 | −8,7% |
| ROE +2 pp | US$13,11 | +8,7% |
| Crecimiento años 1–5 −2 pp | US$11,94 | −1,0% |
| Crecimiento años 1–5 +2 pp | US$12,18 | +1,0% |
| Ke +1 pp | US$11,48 | −4,8% |
| Ke −1 pp | US$12,68 | +5,2% |
| Crecimiento terminal −0,5 pp | US$12,06 | −0,0% |
| Crecimiento terminal +0,5 pp | US$12,06 | +0,0% |
| Acciones +5% | US$11,49 | −4,8% |


### Piezas del valor

**Crecimiento.** En dólares (hoja): US$3.193 millones (2023), US$3.495 millones (2024, +9,4%) y US$3.653 millones (2025, +4,5%); LTM US$3.892 millones. En reales, ingresos y rendimientos de R$20.411 millones en 2025 (+8,5%); transacciones R$8.159 millones (en baja) y el resto ingresos financieros. La división de las historias (~40% transacciones, ~60% financieros y banca) es un cálculo propio.

| US$ millones | 2023 | 2024 | 2025 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 3.193 | 3.495 | 3.653 | 3.892 |
| Crecimiento | +7,5% | +9,4% | +4,5% | — |
| Margen (utilidad antes de impuestos) | 12,6% | 12,7% | 12,5% | 12,6% |
| FCFF (hoja) | −845 | −333 | 703 | — |

**Márgenes.** Para PagBank la rentabilidad relevante es el ROE, no el margen EBIT. Siguiendo a Damodaran para bancos, la utilidad de cada año es ROE × patrimonio contable del año anterior: parte del patrimonio de US$2.742 millones del 2T26 (utilidad LTM de US$406,6 millones, ROE de 14,8% sobre ese patrimonio) y de 279,5 millones de acciones diluidas. ROE Base de 15,6% (ROAE ajustado del comunicado del 2T de 11-ago-2026); 13% y 17% delimitan Conservadora y Optimista, y 10% la Disrupción. En los años 6-10 el ROE converge al costo del patrimonio terminal de 12% y la utilidad baja con él; crecimiento estable en dólares de 3%. Son supuestos del analista, no guía. Lectura del precio: la acción cotiza a ~0,92 veces el valor en libros; con Ke de 13,4% y g de 3%, eso implica un ROE de largo plazo de ~12,5% (g + P/VL × (Ke − g)), por debajo del costo del patrimonio: el mercado no cree que PagBank sostenga el 15%.

**Reinversión y retorno.** La reinversión patrimonial es el aumento del patrimonio contable que exige crecer (patrimonio del año anterior × crecimiento); el FCFE es utilidad menos esa retención. Se descuenta al Ke de 13,4% (beta 1,12), que converge a 12% en el año 10. Con ROE = Ke en perpetuidad, el valor terminal es el patrimonio contable del año 10: crecer después no suma valor. No se suma la liquidez bancaria ni se restan depósitos. El 22,5% de Basilea reportado en 2T muestra holgura, pero no identifica por sí solo capital distribuible: no se agrega un valor por exceso de capital no comprobado. La aproximación requiere que crecimiento de ingresos y beneficios sea comparable; la sensibilidad debe revisarse si cambia el riesgo de crédito o el capital regulatorio. Sin ventaja defendible: no tiene una barrera durable frente a Pix y los bancos digitales, y su ROIC apenas supera el costo de capital. El ROIC después del año 10 es igual al costo de capital, el supuesto por defecto de Damodaran: el crecimiento posterior no suma valor.

**Riesgo.** La hoja usa una beta de 0,82: la del patrimonio de «Financial Svcs. (Non-bank & Insurance)» en la tabla global de Damodaran (1.138 empresas, ene-2026). En una financiera se usa la beta del patrimonio, no la desapalancada; tabla global porque PagSeguro vende 100% en Brasil, y el riesgo de Brasil va en la prima de mercado (7,33%), no en la beta. Hasta el 5-oct-2026 se usaba 1,12 = 0,97 (tabla de EE.UU.) + 0,15 por empresa pequeña; la prima por tamaño es riesgo diversificable y Damodaran no la usa. La regresión semanal contra el S&P 500 da 0,80 a dos años y 1,42 a cinco, y contra el índice de Brasil ~1,2, como StoneCo, XP e Inter; queda como referencia. El efecto de cada beta en el DCF técnico anterior está en la tabla.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF técnico anterior por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 0,82 | 11,3% | 11,3% | US$12,06 |
| Bottom-up del sector (Financial Svcs. (Non-bank & Insurance), reapalancada) | 0,33 | 7,7% | 7,7% | US$14,48 |


### DCF financiero: supuestos y limitaciones

Para PagBank la rentabilidad relevante es el ROE, no el margen EBIT. Siguiendo a Damodaran para bancos, la utilidad de cada año es ROE × patrimonio contable del año anterior: parte del patrimonio de US$2.742 millones del 2T26 (utilidad LTM de US$406,6 millones, ROE de 14,8% sobre ese patrimonio) y de 279,5 millones de acciones diluidas. ROE Base de 15,6% (ROAE ajustado del comunicado del 2T de 11-ago-2026); 13% y 17% delimitan Conservadora y Optimista, y 10% la Disrupción. En los años 6-10 el ROE converge al costo del patrimonio terminal de 12% y la utilidad baja con él; crecimiento estable en dólares de 3%. Son supuestos del analista, no guía. Lectura del precio: la acción cotiza a ~0,92 veces el valor en libros; con Ke de 13,4% y g de 3%, eso implica un ROE de largo plazo de ~12,5% (g + P/VL × (Ke − g)), por debajo del costo del patrimonio: el mercado no cree que PagBank sostenga el 15%. La reinversión patrimonial es el aumento del patrimonio contable que exige crecer (patrimonio del año anterior × crecimiento); el FCFE es utilidad menos esa retención. Se descuenta al Ke de 13,4% (beta 1,12), que converge a 12% en el año 10. Con ROE = Ke en perpetuidad, el valor terminal es el patrimonio contable del año 10: crecer después no suma valor. No se suma la liquidez bancaria ni se restan depósitos. El 22,5% de Basilea reportado en 2T muestra holgura, pero no identifica por sí solo capital distribuible: no se agrega un valor por exceso de capital no comprobado. La aproximación requiere que crecimiento de ingresos y beneficios sea comparable; la sensibilidad debe revisarse si cambia el riesgo de crédito o el capital regulatorio. Sin ventaja defendible: no tiene una barrera durable frente a Pix y los bancos digitales, y su ROIC apenas supera el costo de capital. El ROIC después del año 10 es igual al costo de capital, el supuesto por defecto de Damodaran: el crecimiento posterior no suma valor.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$12,06 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$11,49. Cada historia tiene su propia trayectoria de beneficios, ROE objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene aplicando descuentos al antiguo caso técnico de la hoja (US$12,08) ni mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Utilidad neta base | US$407 millones | «DCF FCFE financiero» B3: utilidad LTM del año base. |
| ROE objetivo | Base: 15,6%; Conservadora: 13,0%; Disrupción: 10,0%; Optimista: 17,0% | Años 1–5 al ROE de la historia; converge al Ke terminal en los años 6–10. |
| Descuento | Ke 11,30% → 12,30% | Costo del patrimonio de la hoja; tasa libre de riesgo 5,29%, beta 0,82, ERP 7,33%. Igual en las cuatro historias. |
| Crecimiento perpetuo | Base/Conservadora/Disrupción/Optimista: 3,00% | Terminal de la hoja («DCF FCFE financiero» B5) en las historias que no lo cambian. |
| Acciones | 279,5 millones | Valuation output B34. En FCFE no se resta deuda: el flujo ya es del accionista. |


#### 2. De la utilidad al flujo del accionista

Utilidadₜ = ROEₜ × patrimonio contableₜ₋₁ (Damodaran, bancos). Reinversión patrimonial = patrimonioₜ₋₁ × crecimientoₜ (crecer exige más capital); FCFE = utilidad − reinversión. En la Base, año 1: utilidad US$427,75 millones, reinversión US$131,65 millones y FCFE US$296,10 millones. Se descuenta al costo del patrimonio; en perpetuidad el ROE es el Ke terminal, utilidad₁₁ = Ke terminal × patrimonio₁₀, FCFE₁₁ = utilidad₁₁ × (1 − g / Ke terminal) y valor terminal = FCFE₁₁ / (Ke terminal − g) = patrimonio₁₀. No se resta deuda.


#### 3. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en «Escenarios e historias»: utilidad, crecimiento, ROE, reinversión patrimonial, flujo al accionista (FCFE), costo del patrimonio y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · Banco digital estable con ROAE de ~15%** — probabilidad 45%; valor terminal 4.400,7 (VP 1.468,5); DCF US$12,06 por acción.

| Año | Utilidad | Crecimiento | ROE | Reinversión | FCFE | Ke | VP del FCFE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 427,8 | 4,8% | 15,6% | 131,7 | 296,1 | 11,3% | 266,0 |
| 2 | 448,3 | 5,6% | 15,6% | 159,7 | 288,6 | 11,3% | 232,9 |
| 3 | 473,2 | 5,9% | 15,6% | 179,2 | 294,0 | 11,3% | 213,2 |
| 4 | 501,2 | 5,7% | 15,6% | 184,0 | 317,1 | 11,3% | 206,6 |
| 5 | 529,9 | 5,8% | 15,6% | 198,0 | 331,8 | 11,3% | 194,3 |
| 6 | 537,0 | 5,3% | 14,9% | 189,2 | 347,8 | 11,5% | 182,6 |
| 7 | 540,3 | 4,7% | 14,3% | 177,8 | 362,6 | 11,7% | 170,4 |
| 8 | 539,6 | 4,1% | 13,6% | 163,7 | 375,9 | 11,9% | 157,9 |
| 9 | 534,6 | 3,6% | 13,0% | 147,1 | 387,5 | 12,1% | 145,2 |
| 10 | 525,5 | 3,0% | 12,3% | 128,2 | 397,3 | 12,3% | 132,6 |
| Terminal | 541,3 | 3,0% | 12,3% | 132,0 | 409,3 | 12,3% | — |

Modelo de rendimientos en exceso (Damodaran, bancos): patrimonio contable de hoy 2.742,0 + VP de los rendimientos en exceso 628,5 = 3.370,5 millones; entre 279,46 millones de acciones da US$12,06 por acción, igual que el FCFE (US$12,06). En perpetuidad el ROE es el costo del patrimonio: no hay rendimiento en exceso y crecer no suma valor.

| Año | Patrimonio inicial | ROE | Utilidad | Ke | Costo del patrimonio | Rendimiento en exceso | VP |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2.742,0 | 15,6% | 427,8 | 11,3% | 309,9 | 117,9 | 105,9 |
| 2 | 2.873,7 | 15,6% | 448,3 | 11,3% | 324,7 | 123,5 | 99,7 |
| 3 | 3.033,4 | 15,6% | 473,2 | 11,3% | 342,8 | 130,4 | 94,6 |
| 4 | 3.212,6 | 15,6% | 501,2 | 11,3% | 363,0 | 138,1 | 90,0 |
| 5 | 3.396,6 | 15,6% | 529,9 | 11,3% | 383,8 | 146,0 | 85,5 |
| 6 | 3.594,7 | 14,9% | 537,0 | 11,5% | 413,4 | 123,6 | 64,9 |
| 7 | 3.783,9 | 14,3% | 540,3 | 11,7% | 442,7 | 97,6 | 45,9 |
| 8 | 3.961,7 | 13,6% | 539,6 | 11,9% | 471,4 | 68,1 | 28,6 |
| 9 | 4.125,4 | 13,0% | 534,6 | 12,1% | 499,2 | 35,5 | 13,3 |
| 10 | 4.272,5 | 12,3% | 525,5 | 12,3% | 525,5 | 0,0 | 0,0 |
| Terminal | 4.400,7 | 12,3% | 541,3 | 12,3% | 541,3 | 0,0 | 0 |

**Conservadora · El PIX y la competencia erosionan** — probabilidad 30%; valor terminal 3.386,4 (VP 1.130,1); DCF US$10,61 por acción.

| Año | Utilidad | Crecimiento | ROE | Reinversión | FCFE | Ke | VP del FCFE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 356,5 | −0,2% | 13,0% | 0,0 | 356,5 | 11,3% | 320,3 |
| 2 | 356,5 | 0,9% | 13,0% | 25,9 | 330,5 | 11,3% | 266,8 |
| 3 | 359,8 | 1,6% | 13,0% | 43,4 | 316,4 | 11,3% | 229,5 |
| 4 | 365,5 | 2,1% | 13,0% | 59,3 | 306,1 | 11,3% | 199,5 |
| 5 | 373,2 | 2,6% | 13,0% | 74,2 | 299,0 | 11,3% | 175,0 |
| 6 | 378,7 | 2,7% | 12,9% | 78,6 | 300,1 | 11,5% | 157,6 |
| 7 | 384,6 | 2,8% | 12,7% | 83,2 | 301,4 | 11,7% | 141,7 |
| 8 | 390,8 | 2,8% | 12,6% | 88,0 | 302,8 | 11,9% | 127,2 |
| 9 | 397,4 | 2,9% | 12,4% | 93,2 | 304,2 | 12,1% | 114,0 |
| 10 | 404,4 | 3,0% | 12,3% | 98,6 | 305,8 | 12,3% | 102,0 |
| Terminal | 416,5 | 3,0% | 12,3% | 101,6 | 314,9 | 12,3% | — |

Modelo de rendimientos en exceso (Damodaran, bancos): patrimonio contable de hoy 2.742,0 + VP de los rendimientos en exceso 221,7 = 2.963,7 millones; entre 279,46 millones de acciones da US$10,61 por acción, igual que el FCFE (US$10,61). En perpetuidad el ROE es el costo del patrimonio: no hay rendimiento en exceso y crecer no suma valor.

| Año | Patrimonio inicial | ROE | Utilidad | Ke | Costo del patrimonio | Rendimiento en exceso | VP |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2.742,0 | 13,0% | 356,5 | 11,3% | 309,9 | 46,6 | 41,9 |
| 2 | 2.742,0 | 13,0% | 356,5 | 11,3% | 309,9 | 46,6 | 37,6 |
| 3 | 2.767,9 | 13,0% | 359,8 | 11,3% | 312,8 | 47,0 | 34,1 |
| 4 | 2.811,3 | 13,0% | 365,5 | 11,3% | 317,7 | 47,8 | 31,1 |
| 5 | 2.870,6 | 13,0% | 373,2 | 11,3% | 324,4 | 48,8 | 28,6 |
| 6 | 2.944,8 | 12,9% | 378,7 | 11,5% | 338,7 | 40,0 | 21,0 |
| 7 | 3.023,4 | 12,7% | 384,6 | 11,7% | 353,7 | 30,8 | 14,5 |
| 8 | 3.106,6 | 12,6% | 390,8 | 11,9% | 369,7 | 21,1 | 8,9 |
| 9 | 3.194,6 | 12,4% | 397,4 | 12,1% | 386,6 | 10,9 | 4,1 |
| 10 | 3.287,8 | 12,3% | 404,4 | 12,3% | 404,4 | 0,0 | 0,0 |
| Terminal | 3.386,4 | 12,3% | 416,5 | 12,3% | 416,5 | 0,0 | 0 |

**Disrupción · Deterioro de los fundamentales: Crisis de crédito en Brasil** — probabilidad 10%; valor terminal 3.429,0 (VP 1.144,3); DCF US$9,21 por acción.

| Año | Utilidad | Crecimiento | ROE | Reinversión | FCFE | Ke | VP del FCFE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 274,2 | −7,0% | 10,0% | 0,0 | 274,2 | 11,3% | 246,4 |
| 2 | 274,2 | −1,9% | 10,0% | 0,0 | 274,2 | 11,3% | 221,3 |
| 3 | 274,2 | 0,8% | 10,0% | 20,6 | 253,6 | 11,3% | 183,9 |
| 4 | 276,3 | 3,2% | 10,0% | 88,3 | 188,0 | 11,3% | 122,5 |
| 5 | 285,1 | 3,3% | 10,0% | 92,7 | 192,4 | 11,3% | 112,6 |
| 6 | 307,9 | 3,2% | 10,5% | 94,2 | 213,7 | 11,5% | 112,2 |
| 7 | 331,7 | 3,2% | 10,9% | 95,7 | 236,0 | 11,7% | 110,9 |
| 8 | 356,6 | 3,1% | 11,4% | 97,2 | 259,4 | 11,9% | 109,0 |
| 9 | 382,5 | 3,1% | 11,8% | 98,5 | 284,0 | 12,1% | 106,4 |
| 10 | 409,5 | 3,0% | 12,3% | 99,9 | 309,6 | 12,3% | 103,3 |
| Terminal | 421,8 | 3,0% | 12,3% | 102,9 | 318,9 | 12,3% | — |

Modelo de rendimientos en exceso (Damodaran, bancos): patrimonio contable de hoy 2.742,0 + VP de los rendimientos en exceso -169,0 = 2.573,0 millones; entre 279,46 millones de acciones da US$9,21 por acción, igual que el FCFE (US$9,21). En perpetuidad el ROE es el costo del patrimonio: no hay rendimiento en exceso y crecer no suma valor.

| Año | Patrimonio inicial | ROE | Utilidad | Ke | Costo del patrimonio | Rendimiento en exceso | VP |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2.742,0 | 10,0% | 274,2 | 11,3% | 309,9 | -35,7 | -32,0 |
| 2 | 2.742,0 | 10,0% | 274,2 | 11,3% | 309,9 | -35,7 | -28,8 |
| 3 | 2.742,0 | 10,0% | 274,2 | 11,3% | 309,9 | -35,7 | -25,9 |
| 4 | 2.762,6 | 10,0% | 276,3 | 11,3% | 312,2 | -35,9 | -23,4 |
| 5 | 2.850,9 | 10,0% | 285,1 | 11,3% | 322,2 | -37,1 | -21,7 |
| 6 | 2.943,5 | 10,5% | 307,9 | 11,5% | 338,5 | -30,6 | -16,1 |
| 7 | 3.037,8 | 10,9% | 331,7 | 11,7% | 355,4 | -23,7 | -11,1 |
| 8 | 3.133,5 | 11,4% | 356,6 | 11,9% | 372,9 | -16,3 | -6,8 |
| 9 | 3.230,6 | 11,8% | 382,5 | 12,1% | 390,9 | -8,4 | -3,1 |
| 10 | 3.329,2 | 12,3% | 409,5 | 12,3% | 409,5 | 0,0 | 0,0 |
| Terminal | 3.429,0 | 12,3% | 421,8 | 12,3% | 421,8 | 0,0 | 0 |

**Optimista · Crece el banco: crédito y depósitos** — probabilidad 15%; valor terminal 5.378,0 (VP 1.794,7); DCF US$13,10 por acción.

| Año | Utilidad | Crecimiento | ROE | Reinversión | FCFE | Ke | VP del FCFE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 466,1 | 9,0% | 17,0% | 246,8 | 219,3 | 11,3% | 197,0 |
| 2 | 508,1 | 9,6% | 17,0% | 286,9 | 221,2 | 11,3% | 178,6 |
| 3 | 556,9 | 9,6% | 17,0% | 314,0 | 242,9 | 11,3% | 176,2 |
| 4 | 610,2 | 9,1% | 17,0% | 327,1 | 283,2 | 11,3% | 184,5 |
| 5 | 665,8 | 7,9% | 17,0% | 308,6 | 357,2 | 11,3% | 209,2 |
| 6 | 678,6 | 6,9% | 16,1% | 291,7 | 386,9 | 11,5% | 203,2 |
| 7 | 683,0 | 5,9% | 15,1% | 267,8 | 415,2 | 11,7% | 195,2 |
| 8 | 678,5 | 5,0% | 14,2% | 236,9 | 441,6 | 11,9% | 185,5 |
| 9 | 664,9 | 4,0% | 13,2% | 199,7 | 465,2 | 12,1% | 174,3 |
| 10 | 642,2 | 3,0% | 12,3% | 156,6 | 485,6 | 12,3% | 162,0 |
| Terminal | 661,5 | 3,0% | 12,3% | 161,3 | 500,2 | 12,3% | — |

Modelo de rendimientos en exceso (Damodaran, bancos): patrimonio contable de hoy 2.742,0 + VP de los rendimientos en exceso 918,4 = 3.660,4 millones; entre 279,46 millones de acciones da US$13,10 por acción, igual que el FCFE (US$13,10). En perpetuidad el ROE es el costo del patrimonio: no hay rendimiento en exceso y crecer no suma valor.

| Año | Patrimonio inicial | ROE | Utilidad | Ke | Costo del patrimonio | Rendimiento en exceso | VP |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2.742,0 | 17,0% | 466,1 | 11,3% | 309,9 | 156,3 | 140,4 |
| 2 | 2.988,8 | 17,0% | 508,1 | 11,3% | 337,8 | 170,3 | 137,5 |
| 3 | 3.275,7 | 17,0% | 556,9 | 11,3% | 370,2 | 186,7 | 135,4 |
| 4 | 3.589,7 | 17,0% | 610,2 | 11,3% | 405,7 | 204,6 | 133,3 |
| 5 | 3.916,7 | 17,0% | 665,8 | 11,3% | 442,6 | 223,2 | 130,7 |
| 6 | 4.225,4 | 16,1% | 678,6 | 11,5% | 485,9 | 192,7 | 101,2 |
| 7 | 4.517,1 | 15,1% | 683,0 | 11,7% | 528,5 | 154,5 | 72,6 |
| 8 | 4.784,8 | 14,2% | 678,5 | 11,9% | 569,4 | 109,1 | 45,8 |
| 9 | 5.021,7 | 13,2% | 664,9 | 12,1% | 607,6 | 57,2 | 21,5 |
| 10 | 5.221,4 | 12,3% | 642,2 | 12,3% | 642,2 | 0,0 | 0,0 |
| Terminal | 5.378,0 | 12,3% | 661,5 | 12,3% | 661,5 | 0,0 | 0 |


#### 4. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFE años 1–10 | VP terminal | Patrimonio | DCF/acción |
|---|---:|---:|---:|---:|
| Base | 1.901,95 | 1.468,52 | 3.370,47 | 12,06 |
| Conservadora | 1.833,67 | 1.130,07 | 2.963,75 | 10,61 |
| Disrupción | 1.428,67 | 1.144,29 | 2.572,96 | 9,21 |
| Optimista | 1.865,71 | 1.794,69 | 3.660,40 | 13,10 |

Ejemplo Base: (1.901,95 + 1.468,52) / 279,5 = US$12,06 por acción.


#### 5. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 45% / 30% / 10% / 15% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,45 × 12,060665 + 0,30 × 10,605261 + 0,10 × 9,206897 + 0,15 × 13,098103 = US$11,494282 ≈ US$11,49. Los aportes son US$5,43 + US$3,18 + US$0,92 + US$1,96 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 11,494282 × 0,65 = US$7,471284 ≈ US$7,47. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base ni al antiguo caso técnico de la hoja: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Los DCF completos empiezan en las filas 22 (Base), 46 (Conservadora), 70 (Disrupción) y 94 (Optimista); sus valores por acción están en B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$12,06, es el valor intrínseco principal. El DCF esperado de US$11,49 combina las cuatro tesis con sus probabilidades y se presenta como complemento. La antigua calibración técnica Conservador/Base/Optimista de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: Banco digital estable con ROAE de ~15%

**Qué plantea.** Es lo que muestra 2025-2026: adquirencia estancada, banco creciendo, ROAE ~15%.

**Traducción al modelo.** Transacciones (adquirencia) crece -3%, -2%, 0%, 1%, 1%; Ingresos financieros y banca crece 10%, 10%, 9%, 8%, 8%. El crecimiento anual compuesto de cinco años es 5,6%; el ROE objetivo es 15,6%. El crecimiento terminal es 3,00%, el de la hoja. Probabilidad: 45%; DCF: US$12,06 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (ROAE: 15,6% (2T26); volumen de pagos (TPV): Estable; depósitos y cartera de crédito: Creciendo). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: El PIX y la competencia erosionan

**Qué plantea.** Es la erosión por el PIX y la competencia de Nubank, Mercado Pago y Stone.

**Traducción al modelo.** Transacciones (adquirencia) crece -8%, -6%, -5%, -4%, -3%; Ingresos financieros y banca crece 5%, 5%, 5%, 5%, 5%. El crecimiento anual compuesto de cinco años es 1,4%; el ROE objetivo es 13,0%. El crecimiento terminal es 3,00%, el de la hoja. Probabilidad: 30%; DCF: US$10,61 por acción.

**Cómo contrastarla.** La apoyarían: ROAE: < 12%; volumen de pagos (TPV): en caída; depósitos y cartera de crédito: estancados; morosidad (90 días): en alza dos trimestres.


#### Disrupción · Deterioro de los fundamentales: Crisis de crédito en Brasil

**Qué plantea.** Es una crisis de crédito con morosidad en alza.

**Traducción al modelo.** Transacciones (adquirencia) crece -10%, -5%, -3%, 0%, 0%; Ingresos financieros y banca crece -5%, 0%, 3%, 5%, 5%. El crecimiento anual compuesto de cinco años es −0,4%; el ROE objetivo es 10,0%. El crecimiento terminal es 3,00%, el de la hoja. Probabilidad: 10%; DCF: US$9,21 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: ROAE: < 12%; volumen de pagos (TPV): en caída; depósitos y cartera de crédito: estancados; morosidad (90 días): en alza dos trimestres.


#### Optimista: Crece el banco: crédito y depósitos

**Qué plantea.** Es un banco digital que crece a doble dígito.

**Traducción al modelo.** Transacciones (adquirencia) crece 0%, 2%, 3%, 3%, 3%; Ingresos financieros y banca crece 15%, 14%, 13%, 12%, 10%. El crecimiento anual compuesto de cinco años es 9,0%; el ROE objetivo es 17,0%. El crecimiento terminal es 3,00%, el de la hoja. Probabilidad: 15%; DCF: US$13,10 por acción.

**Cómo contrastarla.** La confirmarían: ROAE: ≥ 15%; volumen de pagos (TPV): creciendo ≥ 5%; depósitos y cartera de crédito: ≥ +15%; morosidad (90 días): estable.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento. Crecimiento terminal: Base/Conservadora/Disrupción/Optimista: 3,00%. Las diferencias proceden de beneficios, ROE y crecimiento terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | ROE objetivo | Reinversión patrimonial | Crecimiento terminal | Valor/acción (beta 0,82) | Valor/acción (beta 0,33) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **Base · Banco digital estable con ROAE de ~15%** | 45% | Transacciones (adquirencia): -3%, -2%, 0%, 1%, 1%; Ingresos financieros y banca: 10%, 10%, 9%, 8%, 8% | 5,6% | 15,6% | 1,4 | 3,00% | US$12,06 | US$14,48 |
| **Conservadora · El PIX y la competencia erosionan** | 30% | Transacciones (adquirencia): -8%, -6%, -5%, -4%, -3%; Ingresos financieros y banca: 5%, 5%, 5%, 5%, 5% | 1,4% | 13,0% | 1,4 | 3,00% | US$10,61 | US$12,59 |
| **Disrupción · Deterioro de los fundamentales: Crisis de crédito en Brasil** | 10% | Transacciones (adquirencia): -10%, -5%, -3%, 0%, 0%; Ingresos financieros y banca: -5%, 0%, 3%, 5%, 5% | −0,4% | 10,0% | 1,4 | 3,00% | US$9,21 | US$11,01 |
| **Optimista · Crece el banco: crédito y depósitos** | 15% | Transacciones (adquirencia): 0%, 2%, 3%, 3%, 3%; Ingresos financieros y banca: 15%, 14%, 13%, 12%, 10% | 9,0% | 17,0% | 1,4 | 3,00% | US$13,10 | US$15,89 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  | **US$11,49** | **US$13,78** |

Base (45%) es lo que muestra 2025-2026: adquirencia estancada, banco creciendo, ROAE ~15%. Conservadora (30%) es la erosión por el PIX y la competencia de Nubank, Mercado Pago y Stone. Disrupción (10%) es una crisis de crédito con morosidad en alza. Optimista (15%) es un banco digital que crece a doble dígito. En las historias de erosión (Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF técnico anterior (beta 0,82; US$ por acción; filas = crecimiento de los años 1-5, columnas = ROE objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF técnico anterior de la hoja.

| Crecimiento \ Margen | 11,6% | 13,6% | 15,6% | 17,6% | 19,6% |
|---|---:|---:|---:|---:|---:|
| 1,8% | 9,95 | 10,90 | 11,85 | 12,80 | 13,75 |
| 3,8% | 9,96 | 10,96 | 11,96 | 12,97 | 13,97 |
| 5,8% | 9,97 | 11,03 | 12,08 | 13,14 | 14,19 |
| 7,8% | 9,98 | 11,09 | 12,21 | 13,32 | 14,43 |
| 9,8% | 9,99 | 11,16 | 12,34 | 13,51 | 14,69 |


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

Precio de referencia de la valoración guardada: **US$8,90**.

DCF inverso: crecimiento anual de beneficios en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 13% | Margen 16% | Margen 17% |
|---|---:|---:|---:|
| Beta 0,82 | ninguno entre −10% y 60% | ninguno entre −10% y 60% | ninguno entre −10% y 60% |
| Beta 0,33 | ninguno entre −10% y 60% | ninguno entre −10% y 60% | ninguno entre −10% y 60% |

Frente al DCF Base (US$12,06), el valor intrínseco principal, el precio está por debajo en 26%.

Frente al DCF esperado de las historias (US$11,49 con la beta de la hoja; US$13,78 con la propuesta), el precio está por debajo en 23% y por debajo en 35%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Adquirente en declive que se convierte en banco digital rentable en Brasil |  |
| Probabilidades | Base 45% / Conservadora 30% / Disrupción 10% / Optimista 15% |  |
| DCF Base hoy (valor intrínseco principal) | US$12,06 |  |
| DCF esperado por probabilidades (complemento) (beta de la hoja / propuesta) | US$11,49 / US$13,78 |  |
| Precio con MOS sobre el DCF esperado | US$7,47 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$9,21 a US$15,89 |  |
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
