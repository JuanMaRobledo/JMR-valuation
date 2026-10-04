---
schema: "jmr-analisis-damodaran-v1"
ticker: "PAGS"
analysis_date: "2026-09-30"
---

# PagSeguro Digital Ltd. (PAGS) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$10,83 por acción** (Base · Banco digital estable con ROAE de ~15%).

**Complemento · DCF esperado por probabilidades: US$10,34.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$8,29–11,69. El MOS 35% se aplica al esperado: US$6,72. El antiguo caso técnico de la hoja (US$10,84) se conserva solo como calibración; no es el DCF Base. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: balance del último 10-q, capital invertido operativo, flujos ltm, margen objetivo base de la hoja enlazado al de input sheet (12 celdas, con respaldo). DCF esperado US$11,60 → US$10,41. Salvedades abiertas: Arrendamientos: bajo NIIF 16 todos los arrendamientos están en el balance y el EBIT ya excluye su costo financiero, así que su pasivo es deuda; se conserva en la deuda del DCF. Financiera (DCF de flujo al accionista): balance y flujos LTM actualizados con el 20-F 2025 y el 6-K del 1S26 (convertidos a los tipos implícitos de la hoja); no afectan al valor, que depende de utilidad, ROE y costo del patrimonio. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de US$10,84 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


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

**Crecimiento: la adquirencia cae, el banco crece.** La Base supone que las transacciones caen 3% y se estabilizan mientras los ingresos financieros y de banca crecen 8-10%: el total crece 4,8% el primer año y 5,6% compuesto, una cifra que lograron ~63% de las empresas de su tamaño. El crecimiento que mueve el valor es el de la utilidad, que la hoja supone en 5% el primer año y 6% después. La Conservadora (1,4%) es la erosión por el PIX y por Nubank, Mercado Pago y Stone; la Disrupción (−0,4%), una crisis de crédito; la Optimista (9,0%), un banco que crece a doble dígito. Si el volumen de pagos entra en caída, la Base pierde sustento. El crecimiento casi no mueve el valor (±2 puntos: US$10,78 (−0,5%) y US$10,89 (+0,5%)), porque crecer exige retener capital: en un banco, crecer con un ROE apenas por encima del costo del patrimonio crea poco valor.

**ROE: el supuesto central.** La Base usa un ROE de 15,6%, el ROAE ajustado del 2T26 (comunicado del 11-ago-2026), que después del año 5 converge al costo del patrimonio terminal: ningún banco sostiene para siempre un retorno por encima de su costo de capital sin una ventaja, y PagBank no tiene una barrera durable frente al PIX y los bancos digitales. La Conservadora usa 13,0%, la Disrupción 10,0% y la Optimista 17,0%. La utilidad es ROE × patrimonio contable del año anterior y lo que se retiene para crecer es el aumento del patrimonio; el resto es el flujo del accionista. El índice de Basilea de 22,5% muestra holgura de capital, pero no se suma como valor extra porque no hay evidencia de que sea distribuible. Un ROAE por debajo de 12% invalidaría la Base; dos puntos de ROE la mueven a US$9,86 (−9%) o US$11,81 (+9%).

**Descuento: Brasil cuesta caro.** El costo del patrimonio empieza en 13,50% (beta 1,12, prima de riesgo 7,33%, que incluye el riesgo país) y converge a 12,30%. Es el supuesto que más mueve el valor: un punto más lo lleva a US$10,33 (−5%); uno menos, a US$11,37 (+5%). Una beta sectorial menor (~0,97) se considera solo como sensibilidad, porque el riesgo de un banco en Brasil no es el de una financiera promedio de EE.UU. El crecimiento perpetuo en dólares es 3,00% y el terminal explica 42,3% del valor.

**Probabilidades y lectura del resultado.** La Base pesa 45%, la Conservadora 30%, la Disrupción 10% y la Optimista 15%. Las cuatro historias están cerca (US$8,29 a US$11,69) porque, con el ROE convergiendo al costo del patrimonio, ninguna crea mucho valor por crecer: la diferencia está en cuánto rinde el capital que ya tiene. El DCF Base es US$10,83 y el esperado US$10,34, frente a un precio de US$9,02: el mercado paga menos que la Disrupción, es decir, descuenta un ROE o un riesgo país peor que el de cualquier historia, o desconfía de la calidad de la cartera de crédito. Las acciones se fijan en 279,5 millones; el real frente al dólar es un riesgo que este DCF en dólares no aísla.

**Del supuesto al valor: cómo se calcula la Base.** El punto de partida es la utilidad del último año, US$407 millones. Cada año es el ROE de la Base por el patrimonio contable del año anterior: US$530 millones en el año 5 y US$526 millones en el año 10, cuando el ROE ya bajó al costo del patrimonio. No toda esa utilidad se puede repartir: para crecer, un banco o una financiera tiene que aumentar su patrimonio al mismo ritmo, y esa parte se retiene. Lo que queda es el flujo del accionista (FCFE): US$296 millones el primer año. Esos flujos se traen a hoy con el costo del patrimonio, que empieza en 13,50% y baja a 12,30%; suman US$1.747 millones. Después del año 10 se supone un crecimiento perpetuo de 3,00%: el valor de esa perpetuidad, traído a hoy, es US$1.281 millones. La suma es el valor del patrimonio, US$3.028 millones; dividido entre 279,5 millones de acciones da US$10,83 por acción. Aquí no se resta deuda: en una financiera la deuda es materia prima del negocio y ya está dentro del flujo del accionista.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 2,75× (peso 0% dentro de los múltiplos); EV/FCFF 2,29× (peso 0% dentro de los múltiplos); P/E 9,55× (peso 64% dentro de los múltiplos); P/FCFE 8,34× (peso 36% dentro de los múltiplos); P/OCF 4,34× (peso 0% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (13,4%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$10,83; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| ROE −2 pp | US$9,86 | −9,0% |
| ROE +2 pp | US$11,81 | +9,0% |
| Crecimiento años 1–5 −2 pp | US$10,78 | −0,5% |
| Crecimiento años 1–5 +2 pp | US$10,89 | +0,5% |
| Ke +1 pp | US$10,33 | −4,7% |
| Ke −1 pp | US$11,37 | +5,0% |
| Crecimiento terminal −0,5 pp | US$10,83 | −0,0% |
| Crecimiento terminal +0,5 pp | US$10,83 | +0,0% |
| Acciones +5% | US$10,32 | −4,8% |


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

**Riesgo.** La hoja usa una beta de 1,12 (desde el 3-oct-2026; antes 1,30). Regla de la cartera (prompt v4, paso 2): beta del patrimonio del sector (0,97) + 0,15 por empresa pequeña = 1,12. La de regresión queda como referencia. Banco digital: se parte de la beta del patrimonio del sector financiero (0,97), no de la desapalancada; el riesgo de Brasil va en la prima de mercado. El efecto de cada beta en el DCF técnico anterior está en la tabla.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF técnico anterior por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,12 | 13,5% | 13,5% | US$10,84 |
| Bottom-up del sector (Financial Svcs. (Non-bank & Insurance), reapalancada) | 0,33 | 7,7% | 7,7% | US$14,51 |


### DCF financiero: supuestos y limitaciones

Para PagBank la rentabilidad relevante es el ROE, no el margen EBIT. Siguiendo a Damodaran para bancos, la utilidad de cada año es ROE × patrimonio contable del año anterior: parte del patrimonio de US$2.742 millones del 2T26 (utilidad LTM de US$406,6 millones, ROE de 14,8% sobre ese patrimonio) y de 279,5 millones de acciones diluidas. ROE Base de 15,6% (ROAE ajustado del comunicado del 2T de 11-ago-2026); 13% y 17% delimitan Conservadora y Optimista, y 10% la Disrupción. En los años 6-10 el ROE converge al costo del patrimonio terminal de 12% y la utilidad baja con él; crecimiento estable en dólares de 3%. Son supuestos del analista, no guía. Lectura del precio: la acción cotiza a ~0,92 veces el valor en libros; con Ke de 13,4% y g de 3%, eso implica un ROE de largo plazo de ~12,5% (g + P/VL × (Ke − g)), por debajo del costo del patrimonio: el mercado no cree que PagBank sostenga el 15%. La reinversión patrimonial es el aumento del patrimonio contable que exige crecer (patrimonio del año anterior × crecimiento); el FCFE es utilidad menos esa retención. Se descuenta al Ke de 13,4% (beta 1,12), que converge a 12% en el año 10. Con ROE = Ke en perpetuidad, el valor terminal es el patrimonio contable del año 10: crecer después no suma valor. No se suma la liquidez bancaria ni se restan depósitos. El 22,5% de Basilea reportado en 2T muestra holgura, pero no identifica por sí solo capital distribuible: no se agrega un valor por exceso de capital no comprobado. La aproximación requiere que crecimiento de ingresos y beneficios sea comparable; la sensibilidad debe revisarse si cambia el riesgo de crédito o el capital regulatorio. Sin ventaja defendible: no tiene una barrera durable frente a Pix y los bancos digitales, y su ROIC apenas supera el costo de capital. El ROIC después del año 10 es igual al costo de capital, el supuesto por defecto de Damodaran: el crecimiento posterior no suma valor.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$10,83 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$10,34. Cada historia tiene su propia trayectoria de beneficios, ROE objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene aplicando descuentos al antiguo caso técnico de la hoja (US$10,84) ni mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Utilidad neta base | US$407 millones | «DCF FCFE financiero» B3: utilidad LTM del año base. |
| ROE objetivo | Base: 15,6%; Conservadora: 13,0%; Disrupción: 10,0%; Optimista: 17,0% | Años 1–5 al ROE de la historia; converge al Ke terminal en los años 6–10. |
| Descuento | Ke 13,50% → 12,30% | Costo del patrimonio de la hoja; tasa libre de riesgo 5,29%, beta 1,12, ERP 7,33%. Igual en las cuatro historias. |
| Crecimiento perpetuo | Base/Conservadora/Disrupción/Optimista: 3,00% | Terminal de la hoja («DCF FCFE financiero» B5) en las historias que no lo cambian. |
| Acciones | 279,5 millones | Valuation output B34. En FCFE no se resta deuda: el flujo ya es del accionista. |


#### 2. De la utilidad al flujo del accionista

Utilidadₜ = ROEₜ × patrimonio contableₜ₋₁ (Damodaran, bancos). Reinversión patrimonial = patrimonioₜ₋₁ × crecimientoₜ (crecer exige más capital); FCFE = utilidad − reinversión. En la Base, año 1: utilidad US$427,75 millones, reinversión US$131,65 millones y FCFE US$296,10 millones. Se descuenta al costo del patrimonio; en perpetuidad el ROE es el Ke terminal, utilidad₁₁ = Ke terminal × patrimonio₁₀, FCFE₁₁ = utilidad₁₁ × (1 − g / Ke terminal) y valor terminal = FCFE₁₁ / (Ke terminal − g) = patrimonio₁₀. No se resta deuda.


#### 3. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en «Escenarios e historias»: utilidad, crecimiento, ROE, reinversión patrimonial, flujo al accionista (FCFE), costo del patrimonio y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · Banco digital estable con ROAE de ~15%** — probabilidad 45%; valor terminal 4.400,7 (VP 1.280,6); DCF US$10,83 por acción.

| Año | Utilidad | Crecimiento | ROE | Reinversión | FCFE | Ke | VP del FCFE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 427,8 | 4,8% | 15,6% | 131,7 | 296,1 | 13,5% | 260,9 |
| 2 | 448,3 | 5,6% | 15,6% | 159,7 | 288,6 | 13,5% | 224,0 |
| 3 | 473,2 | 5,9% | 15,6% | 179,2 | 294,0 | 13,5% | 201,1 |
| 4 | 501,2 | 5,7% | 15,6% | 184,0 | 317,1 | 13,5% | 191,1 |
| 5 | 529,9 | 5,8% | 15,6% | 198,0 | 331,8 | 13,5% | 176,2 |
| 6 | 537,0 | 5,3% | 14,9% | 189,2 | 347,8 | 13,3% | 163,0 |
| 7 | 540,3 | 4,7% | 14,3% | 177,8 | 362,6 | 13,0% | 150,4 |
| 8 | 539,6 | 4,1% | 13,6% | 163,7 | 375,9 | 12,8% | 138,2 |
| 9 | 534,6 | 3,6% | 13,0% | 147,1 | 387,5 | 12,5% | 126,6 |
| 10 | 525,5 | 3,0% | 12,3% | 128,2 | 397,3 | 12,3% | 115,6 |
| Terminal | 541,3 | 3,0% | 12,3% | 132,0 | 409,3 | 12,3% | — |

Modelo de rendimientos en exceso (Damodaran, bancos): patrimonio contable de hoy 2.742,0 + VP de los rendimientos en exceso 285,7 = 3.027,7 millones; entre 279,46 millones de acciones da US$10,83 por acción, igual que el FCFE (US$10,83). En perpetuidad el ROE es el costo del patrimonio: no hay rendimiento en exceso y crecer no suma valor.

| Año | Patrimonio inicial | ROE | Utilidad | Ke | Costo del patrimonio | Rendimiento en exceso | VP |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2.742,0 | 15,6% | 427,8 | 13,5% | 370,2 | 57,6 | 50,7 |
| 2 | 2.873,7 | 15,6% | 448,3 | 13,5% | 387,9 | 60,4 | 46,9 |
| 3 | 3.033,4 | 15,6% | 473,2 | 13,5% | 409,5 | 63,7 | 43,6 |
| 4 | 3.212,6 | 15,6% | 501,2 | 13,5% | 433,7 | 67,5 | 40,7 |
| 5 | 3.396,6 | 15,6% | 529,9 | 13,5% | 458,5 | 71,3 | 37,9 |
| 6 | 3.594,7 | 14,9% | 537,0 | 13,3% | 476,6 | 60,4 | 28,3 |
| 7 | 3.783,9 | 14,3% | 540,3 | 13,0% | 492,7 | 47,7 | 19,8 |
| 8 | 3.961,7 | 13,6% | 539,6 | 12,8% | 506,3 | 33,3 | 12,2 |
| 9 | 4.125,4 | 13,0% | 534,6 | 12,5% | 517,3 | 17,3 | 5,7 |
| 10 | 4.272,5 | 12,3% | 525,5 | 12,3% | 525,5 | 0,0 | 0,0 |
| Terminal | 4.400,7 | 12,3% | 541,3 | 12,3% | 541,3 | 0,0 | 0 |

**Conservadora · El PIX y la competencia erosionan** — probabilidad 30%; valor terminal 3.386,4 (VP 985,4); DCF US$9,59 por acción.

| Año | Utilidad | Crecimiento | ROE | Reinversión | FCFE | Ke | VP del FCFE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 356,5 | −0,2% | 13,0% | 0,0 | 356,5 | 13,5% | 314,1 |
| 2 | 356,5 | 0,9% | 13,0% | 25,9 | 330,5 | 13,5% | 256,6 |
| 3 | 359,8 | 1,6% | 13,0% | 43,4 | 316,4 | 13,5% | 216,4 |
| 4 | 365,5 | 2,1% | 13,0% | 59,3 | 306,1 | 13,5% | 184,5 |
| 5 | 373,2 | 2,6% | 13,0% | 74,2 | 299,0 | 13,5% | 158,7 |
| 6 | 378,7 | 2,7% | 12,9% | 78,6 | 300,1 | 13,3% | 140,7 |
| 7 | 384,6 | 2,8% | 12,7% | 83,2 | 301,4 | 13,0% | 125,0 |
| 8 | 390,8 | 2,8% | 12,6% | 88,0 | 302,8 | 12,8% | 111,3 |
| 9 | 397,4 | 2,9% | 12,4% | 93,2 | 304,2 | 12,5% | 99,4 |
| 10 | 404,4 | 3,0% | 12,3% | 98,6 | 305,8 | 12,3% | 89,0 |
| Terminal | 416,5 | 3,0% | 12,3% | 101,6 | 314,9 | 12,3% | — |

Modelo de rendimientos en exceso (Damodaran, bancos): patrimonio contable de hoy 2.742,0 + VP de los rendimientos en exceso -60,8 = 2.681,2 millones; entre 279,46 millones de acciones da US$9,59 por acción, igual que el FCFE (US$9,59). En perpetuidad el ROE es el costo del patrimonio: no hay rendimiento en exceso y crecer no suma valor.

| Año | Patrimonio inicial | ROE | Utilidad | Ke | Costo del patrimonio | Rendimiento en exceso | VP |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2.742,0 | 13,0% | 356,5 | 13,5% | 370,2 | -13,7 | -12,1 |
| 2 | 2.742,0 | 13,0% | 356,5 | 13,5% | 370,2 | -13,7 | -10,6 |
| 3 | 2.767,9 | 13,0% | 359,8 | 13,5% | 373,7 | -13,8 | -9,5 |
| 4 | 2.811,3 | 13,0% | 365,5 | 13,5% | 379,5 | -14,0 | -8,5 |
| 5 | 2.870,6 | 13,0% | 373,2 | 13,5% | 387,5 | -14,3 | -7,6 |
| 6 | 2.944,8 | 12,9% | 378,7 | 13,3% | 390,5 | -11,8 | -5,5 |
| 7 | 3.023,4 | 12,7% | 384,6 | 13,0% | 393,6 | -9,1 | -3,8 |
| 8 | 3.106,6 | 12,6% | 390,8 | 12,8% | 397,0 | -6,2 | -2,3 |
| 9 | 3.194,6 | 12,4% | 397,4 | 12,5% | 400,6 | -3,2 | -1,0 |
| 10 | 3.287,8 | 12,3% | 404,4 | 12,3% | 404,4 | 0,0 | 0,0 |
| Terminal | 3.386,4 | 12,3% | 416,5 | 12,3% | 416,5 | 0,0 | 0 |

**Disrupción · Deterioro de los fundamentales: Crisis de crédito en Brasil** — probabilidad 10%; valor terminal 3.429,0 (VP 997,8); DCF US$8,29 por acción.

| Año | Utilidad | Crecimiento | ROE | Reinversión | FCFE | Ke | VP del FCFE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 274,2 | −7,0% | 10,0% | 0,0 | 274,2 | 13,5% | 241,6 |
| 2 | 274,2 | −1,9% | 10,0% | 0,0 | 274,2 | 13,5% | 212,9 |
| 3 | 274,2 | 0,8% | 10,0% | 20,6 | 253,6 | 13,5% | 173,5 |
| 4 | 276,3 | 3,2% | 10,0% | 88,3 | 188,0 | 13,5% | 113,3 |
| 5 | 285,1 | 3,3% | 10,0% | 92,7 | 192,4 | 13,5% | 102,1 |
| 6 | 307,9 | 3,2% | 10,5% | 94,2 | 213,7 | 13,3% | 100,2 |
| 7 | 331,7 | 3,2% | 10,9% | 95,7 | 236,0 | 13,0% | 97,9 |
| 8 | 356,6 | 3,1% | 11,4% | 97,2 | 259,4 | 12,8% | 95,4 |
| 9 | 382,5 | 3,1% | 11,8% | 98,5 | 284,0 | 12,5% | 92,8 |
| 10 | 409,5 | 3,0% | 12,3% | 99,9 | 309,6 | 12,3% | 90,1 |
| Terminal | 421,8 | 3,0% | 12,3% | 102,9 | 318,9 | 12,3% | — |

Modelo de rendimientos en exceso (Damodaran, bancos): patrimonio contable de hoy 2.742,0 + VP de los rendimientos en exceso -424,5 = 2.317,5 millones; entre 279,46 millones de acciones da US$8,29 por acción, igual que el FCFE (US$8,29). En perpetuidad el ROE es el costo del patrimonio: no hay rendimiento en exceso y crecer no suma valor.

| Año | Patrimonio inicial | ROE | Utilidad | Ke | Costo del patrimonio | Rendimiento en exceso | VP |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2.742,0 | 10,0% | 274,2 | 13,5% | 370,2 | -96,0 | -84,5 |
| 2 | 2.742,0 | 10,0% | 274,2 | 13,5% | 370,2 | -96,0 | -74,5 |
| 3 | 2.742,0 | 10,0% | 274,2 | 13,5% | 370,2 | -96,0 | -65,6 |
| 4 | 2.762,6 | 10,0% | 276,3 | 13,5% | 372,9 | -96,7 | -58,3 |
| 5 | 2.850,9 | 10,0% | 285,1 | 13,5% | 384,9 | -99,8 | -53,0 |
| 6 | 2.943,5 | 10,5% | 307,9 | 13,3% | 390,3 | -82,4 | -38,6 |
| 7 | 3.037,8 | 10,9% | 331,7 | 13,0% | 395,5 | -63,8 | -26,5 |
| 8 | 3.133,5 | 11,4% | 356,6 | 12,8% | 400,5 | -43,9 | -16,1 |
| 9 | 3.230,6 | 11,8% | 382,5 | 12,5% | 405,1 | -22,6 | -7,4 |
| 10 | 3.329,2 | 12,3% | 409,5 | 12,3% | 409,5 | 0,0 | 0,0 |
| Terminal | 3.429,0 | 12,3% | 421,8 | 12,3% | 421,8 | 0,0 | 0 |

**Optimista · Crece el banco: crédito y depósitos** — probabilidad 15%; valor terminal 5.378,0 (VP 1.565,0); DCF US$11,69 por acción.

| Año | Utilidad | Crecimiento | ROE | Reinversión | FCFE | Ke | VP del FCFE |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 466,1 | 9,0% | 17,0% | 246,8 | 219,3 | 13,5% | 193,2 |
| 2 | 508,1 | 9,6% | 17,0% | 286,9 | 221,2 | 13,5% | 171,7 |
| 3 | 556,9 | 9,6% | 17,0% | 314,0 | 242,9 | 13,5% | 166,1 |
| 4 | 610,2 | 9,1% | 17,0% | 327,1 | 283,2 | 13,5% | 170,6 |
| 5 | 665,8 | 7,9% | 17,0% | 308,6 | 357,2 | 13,5% | 189,7 |
| 6 | 678,6 | 6,9% | 16,1% | 291,7 | 386,9 | 13,3% | 181,4 |
| 7 | 683,0 | 5,9% | 15,1% | 267,8 | 415,2 | 13,0% | 172,2 |
| 8 | 678,5 | 5,0% | 14,2% | 236,9 | 441,6 | 12,8% | 162,4 |
| 9 | 664,9 | 4,0% | 13,2% | 199,7 | 465,2 | 12,5% | 152,0 |
| 10 | 642,2 | 3,0% | 12,3% | 156,6 | 485,6 | 12,3% | 141,3 |
| Terminal | 661,5 | 3,0% | 12,3% | 161,3 | 500,2 | 12,3% | — |

Modelo de rendimientos en exceso (Damodaran, bancos): patrimonio contable de hoy 2.742,0 + VP de los rendimientos en exceso 523,6 = 3.265,6 millones; entre 279,46 millones de acciones da US$11,69 por acción, igual que el FCFE (US$11,69). En perpetuidad el ROE es el costo del patrimonio: no hay rendimiento en exceso y crecer no suma valor.

| Año | Patrimonio inicial | ROE | Utilidad | Ke | Costo del patrimonio | Rendimiento en exceso | VP |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2.742,0 | 17,0% | 466,1 | 13,5% | 370,2 | 96,0 | 84,6 |
| 2 | 2.988,8 | 17,0% | 508,1 | 13,5% | 403,5 | 104,6 | 81,2 |
| 3 | 3.275,7 | 17,0% | 556,9 | 13,5% | 442,2 | 114,7 | 78,4 |
| 4 | 3.589,7 | 17,0% | 610,2 | 13,5% | 484,6 | 125,7 | 75,7 |
| 5 | 3.916,7 | 17,0% | 665,8 | 13,5% | 528,7 | 137,1 | 72,8 |
| 6 | 4.225,4 | 16,1% | 678,6 | 13,3% | 560,3 | 118,3 | 55,5 |
| 7 | 4.517,1 | 15,1% | 683,0 | 13,0% | 588,1 | 94,9 | 39,3 |
| 8 | 4.784,8 | 14,2% | 678,5 | 12,8% | 611,5 | 67,0 | 24,6 |
| 9 | 5.021,7 | 13,2% | 664,9 | 12,5% | 629,7 | 35,2 | 11,5 |
| 10 | 5.221,4 | 12,3% | 642,2 | 12,3% | 642,2 | 0,0 | 0,0 |
| Terminal | 5.378,0 | 12,3% | 661,5 | 12,3% | 661,5 | 0,0 | 0 |


#### 4. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFE años 1–10 | VP terminal | Patrimonio | DCF/acción |
|---|---:|---:|---:|---:|
| Base | 1.747,15 | 1.280,55 | 3.027,71 | 10,83 |
| Conservadora | 1.695,73 | 985,42 | 2.681,16 | 9,59 |
| Disrupción | 1.319,68 | 997,82 | 2.317,50 | 8,29 |
| Optimista | 1.700,68 | 1.564,97 | 3.265,65 | 11,69 |

Ejemplo Base: (1.747,15 + 1.280,55) / 279,5 = US$10,83 por acción.


#### 5. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 45% / 30% / 10% / 15% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,45 × 10,834134 + 0,30 × 9,594068 + 0,10 × 8,292780 + 0,15 × 11,685565 = US$10,335694 ≈ US$10,34. Los aportes son US$4,88 + US$2,88 + US$0,83 + US$1,75 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 10,335694 × 0,65 = US$6,718201 ≈ US$6,72. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base ni al antiguo caso técnico de la hoja: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Los DCF completos empiezan en las filas 22 (Base), 46 (Conservadora), 70 (Disrupción) y 94 (Optimista); sus valores por acción están en B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$10,83, es el valor intrínseco principal. El DCF esperado de US$10,34 combina las cuatro tesis con sus probabilidades y se presenta como complemento. La antigua calibración técnica Conservador/Base/Optimista de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: Banco digital estable con ROAE de ~15%

**Qué plantea.** Es lo que muestra 2025-2026: adquirencia estancada, banco creciendo, ROAE ~15%.

**Traducción al modelo.** Transacciones (adquirencia) crece -3%, -2%, 0%, 1%, 1%; Ingresos financieros y banca crece 10%, 10%, 9%, 8%, 8%. El crecimiento anual compuesto de cinco años es 5,6%; el ROE objetivo es 15,6%. El crecimiento terminal es 3,00%, el de la hoja. Probabilidad: 45%; DCF: US$10,83 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (ROAE: 15,6% (2T26); volumen de pagos (TPV): Estable; depósitos y cartera de crédito: Creciendo). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: El PIX y la competencia erosionan

**Qué plantea.** Es la erosión por el PIX y la competencia de Nubank, Mercado Pago y Stone.

**Traducción al modelo.** Transacciones (adquirencia) crece -8%, -6%, -5%, -4%, -3%; Ingresos financieros y banca crece 5%, 5%, 5%, 5%, 5%. El crecimiento anual compuesto de cinco años es 1,4%; el ROE objetivo es 13,0%. El crecimiento terminal es 3,00%, el de la hoja. Probabilidad: 30%; DCF: US$9,59 por acción.

**Cómo contrastarla.** La apoyarían: ROAE: < 12%; volumen de pagos (TPV): en caída; depósitos y cartera de crédito: estancados; morosidad (90 días): en alza dos trimestres.


#### Disrupción · Deterioro de los fundamentales: Crisis de crédito en Brasil

**Qué plantea.** Es una crisis de crédito con morosidad en alza.

**Traducción al modelo.** Transacciones (adquirencia) crece -10%, -5%, -3%, 0%, 0%; Ingresos financieros y banca crece -5%, 0%, 3%, 5%, 5%. El crecimiento anual compuesto de cinco años es −0,4%; el ROE objetivo es 10,0%. El crecimiento terminal es 3,00%, el de la hoja. Probabilidad: 10%; DCF: US$8,29 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: ROAE: < 12%; volumen de pagos (TPV): en caída; depósitos y cartera de crédito: estancados; morosidad (90 días): en alza dos trimestres.


#### Optimista: Crece el banco: crédito y depósitos

**Qué plantea.** Es un banco digital que crece a doble dígito.

**Traducción al modelo.** Transacciones (adquirencia) crece 0%, 2%, 3%, 3%, 3%; Ingresos financieros y banca crece 15%, 14%, 13%, 12%, 10%. El crecimiento anual compuesto de cinco años es 9,0%; el ROE objetivo es 17,0%. El crecimiento terminal es 3,00%, el de la hoja. Probabilidad: 15%; DCF: US$11,69 por acción.

**Cómo contrastarla.** La confirmarían: ROAE: ≥ 15%; volumen de pagos (TPV): creciendo ≥ 5%; depósitos y cartera de crédito: ≥ +15%; morosidad (90 días): estable.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento. Crecimiento terminal: Base/Conservadora/Disrupción/Optimista: 3,00%. Las diferencias proceden de beneficios, ROE y crecimiento terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | ROE objetivo | Reinversión patrimonial | Crecimiento terminal | Valor/acción (beta 1,12) | Valor/acción (beta 0,33) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **Base · Banco digital estable con ROAE de ~15%** | 45% | Transacciones (adquirencia): -3%, -2%, 0%, 1%, 1%; Ingresos financieros y banca: 10%, 10%, 9%, 8%, 8% | 5,6% | 15,6% | 1,4 | 3,00% | US$10,83 | US$14,48 |
| **Conservadora · El PIX y la competencia erosionan** | 30% | Transacciones (adquirencia): -8%, -6%, -5%, -4%, -3%; Ingresos financieros y banca: 5%, 5%, 5%, 5%, 5% | 1,4% | 13,0% | 1,4 | 3,00% | US$9,59 | US$12,59 |
| **Disrupción · Deterioro de los fundamentales: Crisis de crédito en Brasil** | 10% | Transacciones (adquirencia): -10%, -5%, -3%, 0%, 0%; Ingresos financieros y banca: -5%, 0%, 3%, 5%, 5% | −0,4% | 10,0% | 1,4 | 3,00% | US$8,29 | US$11,01 |
| **Optimista · Crece el banco: crédito y depósitos** | 15% | Transacciones (adquirencia): 0%, 2%, 3%, 3%, 3%; Ingresos financieros y banca: 15%, 14%, 13%, 12%, 10% | 9,0% | 17,0% | 1,4 | 3,00% | US$11,69 | US$15,89 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  | **US$10,34** | **US$13,78** |

Base (45%) es lo que muestra 2025-2026: adquirencia estancada, banco creciendo, ROAE ~15%. Conservadora (30%) es la erosión por el PIX y la competencia de Nubank, Mercado Pago y Stone. Disrupción (10%) es una crisis de crédito con morosidad en alza. Optimista (15%) es un banco digital que crece a doble dígito. En las historias de erosión (Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF técnico anterior (beta 1,12; US$ por acción; filas = crecimiento de los años 1-5, columnas = ROE objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF técnico anterior de la hoja.

| Crecimiento \ Margen | 11,6% | 13,6% | 15,6% | 17,6% | 19,6% |
|---|---:|---:|---:|---:|---:|
| 1,8% | 8,97 | 9,86 | 10,74 | 11,63 | 12,52 |
| 3,8% | 8,93 | 9,86 | 10,79 | 11,72 | 12,66 |
| 5,8% | 8,88 | 9,86 | 10,84 | 11,83 | 12,81 |
| 7,8% | 8,83 | 9,86 | 10,90 | 11,93 | 12,97 |
| 9,8% | 8,78 | 9,87 | 10,96 | 12,05 | 13,14 |


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

Precio de referencia de la valoración guardada: **US$9,02**.

DCF inverso: crecimiento anual de beneficios en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 13% | Margen 16% | Margen 17% |
|---|---:|---:|---:|
| Beta 1,12 | 48,2% (0% de las empresas) | ninguno entre −10% y 60% | ninguno entre −10% y 60% |
| Beta 0,33 | ninguno entre −10% y 60% | ninguno entre −10% y 60% | ninguno entre −10% y 60% |

Frente al DCF Base (US$10,83), el valor intrínseco principal, el precio está por debajo en 17%.

Frente al DCF esperado de las historias (US$10,34 con la beta de la hoja; US$13,78 con la propuesta), el precio está por debajo en 13% y por debajo en 35%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Adquirente en declive que se convierte en banco digital rentable en Brasil |  |
| Probabilidades | Base 45% / Conservadora 30% / Disrupción 10% / Optimista 15% |  |
| DCF Base hoy (valor intrínseco principal) | US$10,83 |  |
| DCF esperado por probabilidades (complemento) (beta de la hoja / propuesta) | US$10,34 / US$13,78 |  |
| Precio con MOS sobre el DCF esperado | US$6,72 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$8,29 a US$15,89 |  |
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
