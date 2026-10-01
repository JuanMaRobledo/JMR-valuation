---
schema: "jmr-analisis-damodaran-v1"
ticker: "GOOG"
analysis_date: "2026-09-30"
---

# Alphabet Inc. (GOOG) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Escenarios e historias unificados:** A, B, C y D son los cuatro escenarios DCF activos. La cifra principal es el valor intrínseco esperado US$251,35; la historia central A vale US$298,81 y el rango es US$110,41–399,94. El MOS 35% se aplica al esperado: US$163,37. El antiguo caso Base de la hoja (US$311,57) se conserva solo como calibración técnica; no es el DCF de la historia central A. Los múltiplos y su mezcla son lecturas auxiliares con sus propios supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de US$311,57 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

Alphabet tiene dos negocios distintos bajo un mismo techo. Google Services (Búsqueda, YouTube, Android, suscripciones) es una máquina publicitaria madura y enormemente rentable que genera ~80% de los ingresos. Google Cloud (infraestructura, Vertex AI, TPUs, Workspace) es el nuevo motor: creció 82% en el 2T26, hasta US$24.800 millones en el trimestre, empujado por la demanda de cómputo para IA. En medio está la pregunta de la década: ¿la IA conversacional (Gemini, AI Overviews, agentes) refuerza a la Búsqueda o la canibaliza? Y alrededor, el costo: el capex pasó de US$32.000 millones (2023) a US$91.000 millones (2025), el flujo libre se desplomó y dos juicios antimonopolio (búsqueda y ad tech) siguen en apelación.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Google Services crece ~7-10% anual cinco años | Sí | Sí: +15% en el 2T26 (Search +17%) pese a la IA conversacional | Probable a corto plazo; incierto después |
| Google Cloud sigue creciendo más de 20% anual por años | Sí | Sí: +82% en el 2T26 y ganando participación frente a AWS y Azure | Probable, desacelerando |
| El capex de IA rinde por encima del costo de capital | Sí | Sí en Cloud (demanda visible); incierto en consumo | Incierto |
| Los remedios antimonopolio rompen el negocio de Search | Sí | Poco: los remedios del tribunal de distrito fueron limitados | Baja-media |


### Visión externa: tasas base

Con ventas LTM de US$445.866 millones, la empresa está en el tramo **>$50,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 1,0% y una mediana de 1,5% (desviación estándar 8,3%); sumando una inflación de 2,5%, la mediana nominal ronda 4,0%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| A · Search resiste y Cloud es el segundo motor | 11,7% | 13% |
| B · La IA conversacional erosiona Search | 6,6% | 33% |
| C · Tesis de disrupción · Deterioro de los fundamentales | 3,7% | 53% |
| D · Gemini y Cloud dominan la plataforma de IA | 16,1% | 5% |

Para empresas de más de US$50.000 millones, la mediana de crecimiento real a cinco años es 1,5% (≈4% nominal). Crecer 11,7% anual (historia A) lo logró ~13%; 16% (historia D), ~5%. Alphabet es una excepción probada (creció 14-15% en 2024-2025 y 24% en el 2T26 con ~US$450.000 millones de ventas), pero la visión externa recuerda lo raro que es sostenerlo cinco años más.


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

**Reinversión y retorno.** Esta es la pieza que más cambió. El capex se triplicó en dos años (US$91.447 millones en 2025) y el FCFF cayó de US$71.236 millones a US$14.612 millones. Con un capex 2026 de US$195-205 mil millones, la hoja pasó a un sales-to-capital de 1,2 (años 1-5) y 1,5 (años 6-10), antes 2,5 y 2: la reinversión anterior (~US$14.000 millones al año) era una fracción del gasto real. En la historia D se baja a 1,0 porque crecer tanto en Cloud exige aún más centros de datos. El valor depende de que ese capital rinda por encima del costo de capital: la demanda de Cloud (+82%) es la mejor evidencia a favor. Ventaja durable: escala y efectos de red en búsqueda, YouTube y Android, con ROIC estable de 24-31% y la Búsqueda todavía creciendo. El ROIC después del año 10 es 28,6%, el promedio de su industria según Damodaran (29,3%), limitado a su ROIC actual. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Riesgo.** La hoja usa ahora una beta de 1,07 (antes 1,05). La bottom-up de Software (Internet) da 1,61, pero ese grupo (29 empresas pequeñas y volátiles) no representa a Alphabet. Ponderando por ingresos Advertising (1,01, ~82%) y Software System & Application (1,25, ~18%) y reapalancando con la poca deuda sale 1,07, la que ahora usa la hoja: el riesgo de Alphabet está en los flujos (IA, regulación), no en la tasa.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF técnico anterior por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,07 | 9,8% | 9,7% | US$311,57 |
| Bottom-up del sector (Software (Internet), reapalancada) | 1,61 | 12,2% | 12,1% | US$271,31 |
| Propuesta (sector ajustado por riesgo propio) | 1,07 | 9,8% | 9,7% | US$311,57 |


### Calibración técnica anterior C/B/O (referencia auxiliar)

| Supuesto | Conservador | Base | Optimista |
|---|---:|---:|---:|
| Crecimiento año 1 | 9,0% | 18,0% | 20,6% |
| Crecimiento años 2–5 | 9,0% | 11,0% | 16,0% |
| Margen año 1 (base ajustada del modelo) | 32,5% | 32,5% | 32,5% |
| Margen objetivo | 31,0% | 33,5% | 38,0% |

Ventas/capital: 1,2x en años 1–5 y 1,5x en 6–10. WACC: 9,7%. Ke: 9,8%. Impuesto efectivo: 18,4%. Convergencia: 5 años. Estos parámetros son escenarios del analista, no cifras reportadas. Los casos Conservador, Base y Optimista de la hoja ya no son escenarios activos: sirven de calibración y de supuestos auxiliares de múltiplos. No confundir el antiguo Base con la historia A.


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF técnico anterior | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 28,6% | 29,3% | 9,0% | 28,6% | US$311,57 | US$206,14 |

Fuentes de ventaja: Escala y efectos de red en búsqueda, YouTube y Android; datos. Evidencia: ROIC 24-31% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor principal de US$251,35 se obtiene ejecutando cuatro DCF completos de diez años más valor terminal y ponderándolos por sus probabilidades. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. No se obtiene aplicando descuentos al antiguo Base de US$311,57 ni mezclando el DCF con múltiplos. La historia central A vale US$298,81; «central» y «esperado» son conceptos distintos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$445.866 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 364.000 + 80.000 + 1.866 = 445.866. |
| Margen inicial del DCF | 32,5% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 18,40% en años 1–5; 16,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 9,70% → 9,00% | Tasa libre de riesgo 4,99%, beta 1,07, ERP 4,46%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 1,20x en años 1–5; 1,50x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. D usa 1,00x en años 1–5. |
| Crecimiento perpetuo | A/B/D: 4,99%; C: 2,83% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. C se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (2,83%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | A/D: 28,60%; B/C: 9,00% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 55.911; deuda 61.287; acciones 12.230,0 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo A, año 1: 364.000 × 1,10 + 80.000 × 1,45 + 1.866 × 1,20 = US$518.639,20 millones. Frente a 445.866, el crecimiento consolidado es 16,32%. En los años 2–5 es 12,97%, 10,92%, 9,47%, 8,82%; las ventas del año 5 son US$774.190,87 millones. El 11,7% de la tabla es el crecimiento anual compuesto de los cinco años: (774.190,87 / 445.866)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En A, año 1: NOPAT = 518.639,20 × 32,50% × (1 − 18,40%) = US$137.543,12 millones. La reinversión es US$56.066,53 millones y el FCFF es US$81.476,58 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,00%. Reinversión terminal sobre el NOPAT: A, 17,4% (4,99% / 28,60%); B, 55,4% (4,99% / 9,00%); C, 31,5% (2,83% / 9,00%); D, 17,4% (4,99% / 28,60%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| A | 1.012.767,49 | 2.647.005,34 | 3.659.772,83 | 3.654.396,83 | 298,81 |
| B | 810.509,86 | 920.472,20 | 1.730.982,06 | 1.725.606,06 | 141,10 |
| C | 711.077,35 | 644.650,08 | 1.355.727,43 | 1.350.351,43 | 110,41 |
| D | 1.166.719,10 | 3.729.900,00 | 4.896.619,10 | 4.891.243,10 | 399,94 |

Ejemplo A: (1.012.767,49 + 2.647.005,34 + 55.911 − 61.287) / 12.230,0 = US$298,81 por acción. El terminal representa 72,3% del valor operativo de A: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 5. Valor esperado, probabilidades y margen de seguridad

Las probabilidades 40% / 25% / 15% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

Valor esperado = 0,40 × 298,805955 + 0,25 × 141,096162 + 0,15 × 110,413036 + 0,20 × 399,938111 = US$251,346000 ≈ US$251,35. Los aportes son US$119,52 + US$35,27 + US$16,56 + US$79,99 por acción.

Precio con MOS = valor esperado × (1 − 35%) = 251,346000 × 0,65 = US$163,374900 ≈ US$163,37. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. No se aplica al antiguo Base ni a la historia central A.

Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; central H11; rango H12:H13; MOS H14. Los DCF completos empiezan en las filas 22 (A), 46 (B), 70 (C) y 94 (D); sus valores por acción están en B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: base, conservadora, disrupción y optimista

Estas etiquetas describen las historias A–D activas. La tesis base es A, con un DCF de US$298,81; el valor esperado de US$251,35 combina las cuatro tesis con sus probabilidades. La antigua calibración C/B/O de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### A · Tesis base: Search resiste y Cloud es el segundo motor

**Qué plantea.** Es lo que muestra 2026: Search sigue creciendo y Cloud se vuelve un segundo motor que desacelera con la escala.

**Traducción al modelo.** Google Services crece 10%, 8%, 7%, 6%, 6%; Google Cloud crece 45%, 30%, 22%, 18%, 15%; Other Bets crece 20%, 20%, 20%, 20%, 20%. El crecimiento anual compuesto de cinco años es 11,7%; el margen operativo objetivo es 34,0%. El ROIC terminal es 28,6%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 40%; DCF: US$298,81 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (search & other (interanual): +17% (2T26); google Cloud (interanual): +82% (2T26); margen operativo de Cloud: En alza). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### B · Tesis conservadora: La IA conversacional erosiona Search

**Qué plantea.** Es la erosión de la Búsqueda por la IA conversacional (competencia de OpenAI, cambios en el comportamiento).

**Traducción al modelo.** Google Services crece 6%, 3%, 2%, 2%, 2%; Google Cloud crece 35%, 22%, 16%, 13%, 10%; Other Bets crece 10%, 10%, 10%, 10%, 10%. El crecimiento anual compuesto de cinco años es 6,6%; el margen operativo objetivo es 30,0%. El ROIC terminal es el costo de capital (9,00%). El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 25%; DCF: US$141,10 por acción.

**Cómo contrastarla.** La apoyarían: search & other (interanual): ≤ +3%; google Cloud (interanual): ≤ +20%; margen operativo de Cloud: cae con el capex; capex / ingresos: sube sin aceleración de ingresos.


#### C · Tesis de disrupción · Deterioro de los fundamentales: Remedios antimonopolio y guerra de precios en IA

**Qué plantea.** Combina remedios antimonopolio más duros y una guerra de precios en IA que baja márgenes.

**Traducción al modelo.** Google Services crece 4%, 1%, 0%, 0%, 1%; Google Cloud crece 25%, 15%, 10%, 8%, 8%; Other Bets crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 3,7%; el margen operativo objetivo es 27,0%. El ROIC terminal es el costo de capital (9,00%). El crecimiento terminal es 2,83%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 15%; DCF: US$110,41 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que B: search & other (interanual): ≤ +3%; google Cloud (interanual): ≤ +20%; margen operativo de Cloud: cae con el capex; capex / ingresos: sube sin aceleración de ingresos.


#### D · Tesis optimista: Gemini y Cloud dominan la plataforma de IA

**Qué plantea.** Es Alphabet como plataforma dominante de IA (modelos, chips y nube).

**Traducción al modelo.** Google Services crece 13%, 11%, 10%, 9%, 8%; Google Cloud crece 55%, 40%, 30%, 25%, 20%; Other Bets crece 40%, 40%, 40%, 40%, 40%. El crecimiento anual compuesto de cinco años es 16,1%; el margen operativo objetivo es 37,0%. El ROIC terminal es 28,6%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 20%; DCF: US$399,94 por acción.

**Cómo contrastarla.** La confirmarían: search & other (interanual): ≥ +8%; google Cloud (interanual): ≥ +30% en 2027; margen operativo de Cloud: ≥ 25%; capex / ingresos: baja a ≤ 20% con ingresos creciendo.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: A/B/D: 4,99%; C: 2,83%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas y valor esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,07) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **A · Search resiste y Cloud es el segundo motor** | 40% | Google Services: 10%, 8%, 7%, 6%, 6%; Google Cloud: 45%, 30%, 22%, 18%, 15%; Other Bets: 20%, 20%, 20%, 20%, 20% | 11,7% | 34% | 1,2 | 28,6% | 4,99% | US$298,81 |
| **B · La IA conversacional erosiona Search** | 25% | Google Services: 6%, 3%, 2%, 2%, 2%; Google Cloud: 35%, 22%, 16%, 13%, 10%; Other Bets: 10%, 10%, 10%, 10%, 10% | 6,6% | 30% | 1,2 | = costo de capital | 4,99% | US$141,10 |
| **C · Tesis de disrupción · Deterioro de los fundamentales: Remedios antimonopolio y guerra de precios en IA** | 15% | Google Services: 4%, 1%, 0%, 0%, 1%; Google Cloud: 25%, 15%, 10%, 8%, 8%; Other Bets: 0%, 0%, 0%, 0%, 0% | 3,7% | 27% | 1,2 | = costo de capital | 2,83% | US$110,41 |
| **D · Gemini y Cloud dominan la plataforma de IA** | 20% | Google Services: 13%, 11%, 10%, 9%, 8%; Google Cloud: 55%, 40%, 30%, 25%, 20%; Other Bets: 40%, 40%, 40%, 40%, 40% | 16,1% | 37% | 1,0 | 28,6% | 4,99% | US$399,94 |
| **Valor esperado** | 100% |  |  |  |  |  |  | **US$251,35** |

A (40%) es lo que muestra 2026: Search sigue creciendo y Cloud se vuelve un segundo motor que desacelera con la escala. B (25%) es la erosión de la Búsqueda por la IA conversacional (competencia de OpenAI, cambios en el comportamiento). C (15%) combina remedios antimonopolio más duros y una guerra de precios en IA que baja márgenes. D (20%) es Alphabet como plataforma dominante de IA (modelos, chips y nube). En las historias de erosión (B y C) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF técnico anterior (beta 1,07; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF técnico anterior de la hoja.

| Crecimiento \ Margen | 31,0% | 33,0% | 35,0% | 37,0% | 39,0% |
|---|---:|---:|---:|---:|---:|
| 8,4% | 236,63 | 251,77 | 266,90 | 282,04 | 297,18 |
| 10,4% | 262,58 | 279,67 | 296,76 | 313,85 | 330,94 |
| 12,4% | 291,39 | 310,65 | 329,91 | 349,17 | 368,43 |
| 14,4% | 323,33 | 345,00 | 366,68 | 388,35 | 410,02 |
| 16,4% | 358,70 | 383,05 | 407,40 | 431,75 | 456,11 |


### Pre-mortem

1. Las respuestas generativas reducen los clics y el precio por consulta: Search deja de crecer aunque las búsquedas suban.
2. El capex de IA sobreinvierte: hay exceso de capacidad, precios de cómputo en caída y deterioro de activos.
3. Las apelaciones terminan en remedios más duros (fin de acuerdos por defecto con Apple, venta del ad exchange).
4. OpenAI, Anthropic, Meta o Microsoft capturan a los usuarios de asistentes y a los desarrolladores.
5. La desaceleración de Cloud llega antes: los clientes de IA construyen su propia infraestructura.

**Evidencia en contra de la historia más probable:** el capex crece más rápido que los ingresos y el flujo libre cayó ~80% en 2025. Si la demanda de IA se enfría, la historia A se sostiene en ingresos pero no en retorno sobre el capital.


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

Precio de referencia de la valoración guardada: **US$346,22**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 30% | Margen 34% | Margen 37% |
|---|---:|---:|---:|
| Beta 1,07 | 16,4% (5% de las empresas) | 14,2% (8% de las empresas) | 12,2% (11% de las empresas) |

Frente al valor esperado de las historias (US$251,35), el precio está por encima en 38%. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Máquina publicitaria madura con un segundo motor de IA en la nube, financiado con capex récord |  |
| Probabilidades | A 40% / B 25% / C 15% / D 20% |  |
| Valor esperado (valor principal) | US$251,35 |  |
| DCF base hoy (historia A) | US$298,81 |  |
| Precio con MOS sobre el valor esperado | US$163,37 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$110,41 a US$399,94 |  |
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
