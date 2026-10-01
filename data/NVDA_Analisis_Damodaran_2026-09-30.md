---
schema: "jmr-analisis-damodaran-v1"
ticker: "NVDA"
analysis_date: "2026-09-30"
---

# NVIDIA Corporation (NVDA) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Escenarios e historias unificados:** A, B, C y D son los cuatro escenarios DCF activos. La cifra principal es el valor intrínseco esperado US$186,04; la historia central A vale US$204,91 y el rango es US$50,24–313,47. El MOS 35% se aplica al esperado: US$120,93. El antiguo caso Base de la hoja (US$259,30) se conserva solo como calibración técnica; no es el DCF de la historia central A. Los múltiplos y su mezcla son lecturas auxiliares con sus propios supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (DCF técnico anterior de US$259,30 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja incluye estos cuatro DCF en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

NVIDIA pasó de vender tarjetas gráficas a ser el proveedor dominante de la infraestructura de IA: GPUs, sistemas completos, redes (Mellanox) y CUDA, el software que es estándar de la industria desde hace casi veinte años. Diseña pero no fabrica (TSMC produce sus chips). Los números son de otro planeta: ingresos de US$60.922 millones (FY24), US$130.497 millones (FY25) y US$215.938 millones (FY26), margen operativo de ~60% y, en el 2T FY27, US$96.220 millones en un trimestre, más de 90% de Data Center (+117%). La historia de cinco años no es si NVIDIA es buena empresa, sino cuánto dura el ciclo de inversión en IA de los hiperescaladores, si la inferencia sostiene la demanda cuando el entrenamiento madure y cuánto terreno ceden sus márgenes frente a los chips propios de Google, Amazon y Microsoft y frente a AMD.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~50% el próximo año | Sí | Sí: la empresa habla de crecimiento limitado por la oferta y guía muy alta | Probable |
| La demanda de IA sigue creciendo cinco años sin corrección | Sí | Posible con la inferencia y la IA soberana, pero los semiconductores siempre fueron cíclicos | Incierto |
| El margen operativo se mantiene en ~58-60% | Sí | Sí mientras domine CUDA; los chips propios de los clientes presionan | Media |
| Los chips propios de los clientes (TPU, Trainium) reemplazan a NVIDIA | Sí | Parcialmente: ganan en inferencia interna, no en el mercado abierto | Baja a cinco años |


### Visión externa: tasas base

Con ventas LTM de US$302.970 millones, la empresa está en el tramo **>$50,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 1,0% y una mediana de 1,5% (desviación estándar 8,3%); sumando una inflación de 2,5%, la mediana nominal ronda 4,0%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| A · Ciclo de IA largo que desacelera con la escala | 17,1% | 4% |
| B · Ciclo de semiconductores: el capex se corrige | 7,0% | 30% |
| C · Tesis de disrupción · Deterioro de los fundamentales | -1,3% | 79% |
| D · La IA es infraestructura permanente | 25,3% | 1% |

Para empresas de más de US$50.000 millones, crecer 17% anual cinco años (historia A) lo logró ~4%; 25% (historia D), ~1%. NVIDIA ya rompió todas las tasas base en 2024-2026, pero la visión externa es clara: sostener crecimientos así desde US$300.000 millones de ventas casi no tiene precedentes, y en semiconductores los ciclos de sobreinversión terminan en correcciones.


### Piezas del valor

**Crecimiento.** Ingresos de US$60.922 millones (FY24, +126%), US$130.497 millones (FY25, +114%) y US$215.938 millones (FY26, +65%); LTM US$302.970 millones. En el 2T FY27 (jul-2026) facturó US$96.220 millones, con Data Center en US$89.000 millones (+117%). La hoja supone +50% el próximo año y 14% en los años 2-5. Cada historia se valora con su crecimiento año a año por segmentos; el CAGR a cinco años es descriptivo y no reemplaza la trayectoria de flujos.

| US$ millones | FY24 | FY25 | FY26 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 60.922 | 130.497 | 215.938 | 302.970 |
| Crecimiento | +126% | +114% | +65% | — |
| Margen operativo | 54,1% | 62,4% | 60,4% | 65,2% |
| FCFF (hoja) | 17.211 | 46.706 | 83.173 | — |

**Márgenes.** El margen operativo (54-65%) es de monopolio temporal: precio altísimo por escasez, poco capital (fabless) y software propio. La hoja supone 60% el próximo año y 58% de objetivo. Las fuerzas en contra son la competencia (AMD MI400, TPU, Trainium) y el poder de negociación de cinco clientes enormes; a favor, la escala y el ecosistema CUDA. Las historias van de 40% (corrección fuerte) a 60%.

**Reinversión y retorno.** Como fabless, NVIDIA casi no invierte en activos fijos; su reinversión es I+D (US$18.497 millones en FY26), compromisos de capacidad con TSMC y capital de trabajo. La hoja usa un sales-to-capital de 3 y 2,5. En 2026 la empresa subió el dividendo 25 veces y aprobó recompras por US$80.000 millones: señal de que genera más caja de la que puede reinvertir. Ventaja durable: ecosistema CUDA (costos de cambio) y escala en cómputo acelerado, con ROIC de 13-111%. El ROIC después del año 10 es 27,2%, el promedio de su industria según Damodaran. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Riesgo.** La hoja usaba una beta de regresión de 1,90 (costo del patrimonio 13,5%). Tras la revisión del 30-sep-2026 usa la bottom-up de Semiconductor (66 empresas, 1,50 desapalancada y corregida por caja; 1,51 sin deuda relevante), con costo del patrimonio de 11,7%: el DCF técnico anterior pasó de US$162,65 a US$178,38. La ciclicidad del negocio se modela en las historias (B y C), no en la tasa.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF técnico anterior por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,51 | 11,7% | 11,7% | US$259,30 |
| Bottom-up del sector (Semiconductor, reapalancada) | 1,51 | 11,7% | 11,7% | US$259,56 |


### Calibración técnica anterior C/B/O (referencia auxiliar)

| Supuesto | Conservador | Base | Optimista |
|---|---:|---:|---:|
| Crecimiento año 1 | 32,5% | 50,0% | 56,0% |
| Crecimiento años 2–5 | 6,0% | 14,0% | 22,0% |
| Margen año 1 (base ajustada del modelo) | 60,0% | 60,0% | 60,0% |
| Margen objetivo | 50,0% | 58,0% | 65,0% |

Ventas/capital: 3,0x en años 1–5 y 2,5x en 6–10. WACC: 11,7%. Ke: 11,7%. Impuesto efectivo: 16,1%. Convergencia: 5 años. Estos parámetros son escenarios del analista, no cifras reportadas. Los casos Conservador, Base y Optimista de la hoja ya no son escenarios activos: sirven de calibración y de supuestos auxiliares de múltiplos. No confundir el antiguo Base con la historia A.


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF técnico anterior | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 113,7% | 27,2% | 9,0% | 27,2% | US$259,30 | US$178,38 |

Fuentes de ventaja: Ecosistema CUDA (costos de cambio) y escala en cómputo acelerado. Evidencia: ROIC 13-111%, siempre por encima del costo de capital. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor principal de US$186,04 se obtiene ejecutando cuatro DCF completos de diez años más valor terminal y ponderándolos por sus probabilidades. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. No se obtiene aplicando descuentos al antiguo Base de US$259,30 ni mezclando el DCF con múltiplos. La historia central A vale US$204,91; «central» y «esperado» son conceptos distintos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$302.970 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 278.000 + 24.970 = 302.970. |
| Margen inicial del DCF | 60,0% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 5 (Input sheet B31). |
| Impuesto | 16,05% en años 1–5; 16,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 11,69% → 9,00% | Tasa libre de riesgo 4,99%, beta 1,51, ERP 4,46%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 3,00x en años 1–5; 2,50x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. |
| Crecimiento perpetuo | A/B/D: 4,99%; C: 4,54% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. C se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (4,54%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | A/B/D: 27,20%; C: 9,00% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 22.443; deuda 11.040; acciones 24.100,0 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo A, año 1: 278.000 × 1,50 + 24.970 × 1,10 = US$444.467,00 millones. Frente a 302.970, el crecimiento consolidado es 46,70%. En los años 2–5 es 19,26%, 9,83%, 7,89%, 6,00%; las ventas del año 5 son US$665.807,75 millones. El 17,1% de la tabla es el crecimiento anual compuesto de los cinco años: (665.807,75 / 302.970)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En A, año 1: NOPAT = 444.467,00 × 60,00% × (1 − 16,05%) = US$223.878,03 millones. La reinversión es US$28.532,45 millones y el FCFF es US$195.345,57 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,00%. Reinversión terminal sobre el NOPAT: A, 18,3% (4,99% / 27,20%); B, 18,3% (4,99% / 27,20%); C, 50,4% (4,54% / 9,00%); D, 18,3% (4,99% / 27,20%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| A | 1.716.549,95 | 3.210.409,83 | 4.926.959,77 | 4.938.362,77 | 204,91 |
| B | 1.079.386,23 | 1.830.151,69 | 2.909.537,92 | 2.920.940,92 | 121,20 |
| C | 707.504,51 | 491.929,82 | 1.199.434,33 | 1.210.837,33 | 50,24 |
| D | 2.347.181,94 | 5.196.116,40 | 7.543.298,33 | 7.554.701,33 | 313,47 |

Ejemplo A: (1.716.549,95 + 3.210.409,83 + 22.443 − 11.040) / 24.100,0 = US$204,91 por acción. El terminal representa 65,2% del valor operativo de A: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 5. Valor esperado, probabilidades y margen de seguridad

Las probabilidades 40% / 30% / 10% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

Valor esperado = 0,40 × 204,911318 + 0,30 × 121,200868 + 0,10 × 50,242213 + 0,20 × 313,473084 = US$186,043626 ≈ US$186,04. Los aportes son US$81,96 + US$36,36 + US$5,02 + US$62,69 por acción.

Precio con MOS = valor esperado × (1 − 35%) = 186,043626 × 0,65 = US$120,928357 ≈ US$120,93. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. No se aplica al antiguo Base ni a la historia central A.

Trazabilidad: hoja «Escenarios e historias»: entradas y resultados A5:J8; esperado H10; central H11; rango H12:H13; MOS H14. Los DCF completos empiezan en las filas 22 (A), 46 (B), 70 (C) y 94 (D); sus valores por acción están en B44/B68/B92/B116. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: base, conservadora, disrupción y optimista

Estas etiquetas describen las historias A–D activas. La tesis base es A, con un DCF de US$204,91; el valor esperado de US$186,04 combina las cuatro tesis con sus probabilidades. La antigua calibración C/B/O de la hoja no define estas tesis. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### A · Tesis base: Ciclo de IA largo que desacelera con la escala

**Qué plantea.** Es un ciclo de IA largo que desacelera con la escala.

**Traducción al modelo.** Data Center crece 50%, 20%, 10%, 8%, 6%; Gaming, visualización y automotriz crece 10%, 8%, 7%, 6%, 6%. El crecimiento anual compuesto de cinco años es 17,1%; el margen operativo objetivo es 58,0%. El ROIC terminal es 27,2%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 40%; DCF: US$204,91 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (data Center (interanual): +117% (2T FY27); capex de los hiperescaladores: Récord; margen bruto: ~70-75%). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### B · Tesis conservadora: Ciclo de semiconductores: el capex se corrige

**Qué plantea.** Es la historia clásica de semiconductores: sobreinversión y corrección en 2028.

**Traducción al modelo.** Data Center crece 35%, -10%, 0%, 8%, 8%; Gaming, visualización y automotriz crece 5%, 5%, 5%, 5%, 5%. El crecimiento anual compuesto de cinco años es 7,0%; el margen operativo objetivo es 50,0%. El ROIC terminal es 27,2%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 30%; DCF: US$121,20 por acción.

**Cómo contrastarla.** La apoyarían: data Center (interanual): caída trimestral secuencial; capex de los hiperescaladores: recortes anunciados; margen bruto: ≤ 65%; participación de chips propios y AMD en inferencia: pérdida de clientes grandes.


#### C · Tesis de disrupción · Deterioro de los fundamentales: Chips propios de los clientes y corrección fuerte

**Qué plantea.** Combina corrección fuerte y pérdida de participación frente a chips propios.

**Traducción al modelo.** Data Center crece 25%, -25%, -10%, 5%, 5%; Gaming, visualización y automotriz crece 0%, 0%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es -1,3%; el margen operativo objetivo es 40,0%. El ROIC terminal es el costo de capital (9,00%). El crecimiento terminal es 4,54%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 10%; DCF: US$50,24 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que B: data Center (interanual): caída trimestral secuencial; capex de los hiperescaladores: recortes anunciados; margen bruto: ≤ 65%; participación de chips propios y AMD en inferencia: pérdida de clientes grandes.


#### D · Tesis optimista: La IA es infraestructura permanente

**Qué plantea.** Trata la IA como infraestructura permanente (inferencia masiva, IA soberana, robótica).

**Traducción al modelo.** Data Center crece 60%, 30%, 20%, 15%, 12%; Gaming, visualización y automotriz crece 12%, 12%, 10%, 10%, 8%. El crecimiento anual compuesto de cinco años es 25,3%; el margen operativo objetivo es 60,0%. El ROIC terminal es 27,2%. El crecimiento terminal es 4,99%, el de la hoja. Probabilidad: 20%; DCF: US$313,47 por acción.

**Cómo contrastarla.** La confirmarían: data Center (interanual): ≥ +30% en FY28; capex de los hiperescaladores: sigue creciendo en 2027-2028; margen bruto: ≥ 70%; participación de chips propios y AMD en inferencia: NVIDIA ≥ 70% del mercado abierto.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: A/B/D: 4,99%; C: 4,54%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas y valor esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,51) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **A · Ciclo de IA largo que desacelera con la escala** | 40% | Data Center: 50%, 20%, 10%, 8%, 6%; Gaming, visualización y automotriz: 10%, 8%, 7%, 6%, 6% | 17,1% | 58% | 3,0 | 27,2% | 4,99% | US$204,91 |
| **B · Ciclo de semiconductores: el capex se corrige** | 30% | Data Center: 35%, -10%, 0%, 8%, 8%; Gaming, visualización y automotriz: 5%, 5%, 5%, 5%, 5% | 7,0% | 50% | 3,0 | 27,2% | 4,99% | US$121,20 |
| **C · Tesis de disrupción · Deterioro de los fundamentales: Chips propios de los clientes y corrección fuerte** | 10% | Data Center: 25%, -25%, -10%, 5%, 5%; Gaming, visualización y automotriz: 0%, 0%, 0%, 0%, 0% | -1,3% | 40% | 3,0 | = costo de capital | 4,54% | US$50,24 |
| **D · La IA es infraestructura permanente** | 20% | Data Center: 60%, 30%, 20%, 15%, 12%; Gaming, visualización y automotriz: 12%, 12%, 10%, 10%, 8% | 25,3% | 60% | 3,0 | 27,2% | 4,99% | US$313,47 |
| **Valor esperado** | 100% |  |  |  |  |  |  | **US$186,04** |

A (40%) es un ciclo de IA largo que desacelera con la escala. B (30%) es la historia clásica de semiconductores: sobreinversión y corrección en 2028. C (10%) combina corrección fuerte y pérdida de participación frente a chips propios. D (20%) trata la IA como infraestructura permanente (inferencia masiva, IA soberana, robótica). En las historias de erosión (C) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF técnico anterior (beta 1,51; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF técnico anterior de la hoja.

| Crecimiento \ Margen | 54,0% | 56,0% | 58,0% | 60,0% | 62,0% |
|---|---:|---:|---:|---:|---:|
| 17,2% | 218,92 | 226,70 | 234,47 | 242,24 | 250,01 |
| 19,2% | 243,58 | 252,29 | 261,00 | 269,71 | 278,42 |
| 21,2% | 270,80 | 280,54 | 290,29 | 300,04 | 309,78 |
| 23,2% | 300,80 | 311,69 | 322,58 | 333,47 | 344,37 |
| 25,2% | 333,84 | 346,00 | 358,15 | 370,30 | 382,46 |


### Pre-mortem

1. Los hiperescaladores recortan capex en 2028 porque la monetización de la IA no alcanza para pagar la inversión.
2. Los chips propios (TPU, Trainium, Maia) y AMD capturan la inferencia, que es la mayor parte de la demanda futura.
3. Controles de exportación más duros o un conflicto en Taiwán cortan ventas o producción.
4. Los clientes negocian precios a la baja y el margen cae de ~60% a ~45%.
5. Aparecen métodos de IA mucho más eficientes que reducen la necesidad de cómputo.

**Evidencia en contra de la historia más probable:** la concentración de clientes (pocos hiperescaladores) y la historia de los semiconductores: todos los ciclos de escasez terminaron en exceso de capacidad. Una desaceleración del capex de los hiperescaladores sube el peso de B.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Data Center (interanual) | +117% (2T FY27) | ≥ +30% en FY28 | Caída trimestral secuencial |
| Capex de los hiperescaladores | Récord | Sigue creciendo en 2027-2028 | Recortes anunciados |
| Margen bruto | ~70-75% | ≥ 70% | ≤ 65% |
| Participación de chips propios y AMD en inferencia | Creciendo | NVIDIA ≥ 70% del mercado abierto | Pérdida de clientes grandes |
| Restricciones de exportación | Vigentes para China | Sin nuevas restricciones | Nuevas restricciones o problemas en Taiwán |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$230,67**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 50% | Margen 58% | Margen 62% |
|---|---:|---:|---:|
| Beta 1,51 | 19,6% (2% de las empresas) | 16,9% (4% de las empresas) | 15,7% (6% de las empresas) |
| Beta 1,51 | 19,6% (2% de las empresas) | 16,9% (4% de las empresas) | 15,7% (6% de las empresas) |

Frente al valor esperado de las historias (US$186,04), el precio está por encima en 24%. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Proveedor dominante de la infraestructura de IA en la cima de un ciclo de inversión |  |
| Probabilidades | A 40% / B 30% / C 10% / D 20% |  |
| Valor esperado (valor principal) | US$186,04 |  |
| DCF base hoy (historia A) | US$204,91 |  |
| Precio con MOS sobre el valor esperado | US$120,93 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$50,24 a US$313,79 |  |
| Confianza | Baja: el valor depende de la duración del ciclo, que nadie puede prever |  |
| Qué cambiaría la opinión | Capex de los hiperescaladores y participación de NVIDIA en inferencia |  |
| Revisión | Resultados del 3T FY27 (nov-2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [NVIDIA, resultados del 4T y año FY2026](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026)
- [NVIDIA, Form 10-K FY2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- [Investing.com, presentación del 2T FY27](https://www.investing.com/news/company-news/nvidia-q2-fy27-slides-revenue-doubles-to-96b-data-center-surges-93CH-4878041)
- [CNBC, resultados del 2T FY27](https://www.cnbc.com/2026/08/26/nvidia-nvda-earnings-report-q2-2027-live-updates.html)
- [IBTimes, NVIDIA frente a AMD en centros de datos (2026)](https://www.ibtimes.com.au/nvidia-vs-amd-2026-ai-chip-showdown-who-dominates-data-centers-blackwell-mi400-battle-1866177)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
