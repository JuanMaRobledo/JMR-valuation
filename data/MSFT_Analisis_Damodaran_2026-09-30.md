---
schema: "jmr-analisis-damodaran-v1"
ticker: "MSFT"
analysis_date: "2026-09-30"
---

# Microsoft Corporation (MSFT) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
**Valor intrínseco principal · DCF Base hoy: US$388,50 por acción** (Base · Azure y Copilot sostienen el doble dígito).

**Complemento · DCF esperado por probabilidades: US$342,95.** Los cuatro escenarios DCF activos son Base, Conservadora, Disrupción y Optimista; su rango es US$168,69–504,17. El MOS 35% se aplica al esperado: US$222,92. La hoja calcula las cuatro en 'Valuation output'. Los múltiplos individuales, consolidados y ponderados son lecturas secundarias con sus propios supuestos.

**Auditoría, 2026-10-01:** se contrastaron los estados de la hoja con la SEC (último 10-Q) y se verificaron las historias y sus textos. Correcciones: arrendamientos como deuda (conversor, damodaran), balance del último 10-q, capital invertido operativo, conversor de i+d alineado al ltm, deuda de balance sin arrendamientos operativos, roic terminal (criterio damodaran) (22 celdas, con respaldo). DCF esperado US$406,69 → US$342,95. La coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.

Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Cada historia es un DCF completo con el motor del Modelo JMR, que reproduce la hoja (bloque Base de 'Valuation output': US$388,50 por acción): solo cambian el crecimiento de cada año, el margen objetivo, la reinversión, el crecimiento terminal y el ROIC después del año 10 de la historia; la tasa de descuento es la misma en todas, porque el riesgo va en los flujos. El valor esperado es el promedio de las historias ponderado por su probabilidad. La hoja calcula estos cuatro DCF en 'Valuation output' (bloques Base, Conservador, Optimista y Disrupción) y los resume en «Escenarios e historias». Los múltiplos son precio relativo y se comentan en otras secciones.


### La historia en un párrafo

Microsoft vende el software y la infraestructura sobre los que operan casi todas las empresas: Microsoft 365, Dynamics y LinkedIn (Productivity and Business Processes, margen ~58%), Azure y servidores (Intelligent Cloud, ~42%) y Windows, Xbox y dispositivos (More Personal Computing). En FY2026 (cerrado en junio) facturó US$331.839 millones (+17,8%) con margen operativo de 46,8%, impulsada por Azure (~+30%) y la adopción de Copilot. El cambio de régimen está en el capital: el capex pasó de US$44.477 millones (FY24) a US$115.948 millones (FY26) y el flujo libre de la hoja cayó de US$73.144 millones a US$30.557 millones. La historia de cinco años es si esa inversión en IA rinde como rindió la nube en 2015-2022 o si Microsoft está sobreinvirtiendo en capacidad con demanda concentrada en pocos clientes (OpenAI).

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Los ingresos crecen ~13% anual cinco años | Sí | Sí: +15-18% anual en FY24-FY26 | Probable, desacelerando |
| Azure sigue creciendo más de 20% anual | Sí | Sí: ~30% en FY26 con capacidad limitada por oferta | Probable 2-3 años |
| El capex de IA rinde por encima del costo de capital | Sí | Sí si la demanda de inferencia sigue; hoy depende en parte de OpenAI | Incierto |
| El margen operativo se mantiene en ~45% | Sí | Sí: 44,6% → 46,8%, pero la depreciación del capex crece rápido | Probable |


### Visión externa: tasas base

Con ventas LTM de US$331.839 millones (US$234.795 millones en dólares de 2015, deflactadas con el IPC-U: × 237,017 / 334,980), la empresa está en el tramo **>$50,000 Mn** de las tasas base de crecimiento de ventas a 5 años (Mauboussin & Callahan, *The Base Rate Book*, 2016, Exhibit 4, 1950-2015). En ese tramo el crecimiento real anual tuvo una media de 1,0% y una mediana de 1,5% (desviación estándar 8,3%); sumando una inflación de 2,5%, la mediana nominal ronda 4,0%.

| Historia | Crecimiento anual de ingresos (5 años) | Empresas de este tamaño que lo lograron |
|---|---:|---:|
| Base · Azure y Copilot sostienen el doble dígito | 13,0% | 10% |
| Conservadora · El capex de IA rinde menos de lo esperado | 8,0% | 25% |
| Disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige | 5,0% | 44% |
| Optimista · Microsoft gana la plataforma empresarial de IA | 17,5% | 3% |

En dólares de 2015 la empresa está en el tramo de más de US$50.000 millones: crecer 13,0% anual cinco años (Base) lo logró ~10% de las empresas de ese tamaño; 17,5% (Optimista), ~3%. Microsoft es la excepción que confirma la regla: hace cinco años que crece a doble dígito con más de US$150.000 millones de ventas. Aun así, la visión externa pide no extrapolar el 17,8% de FY26.


### Justificación de los supuestos

Cada párrafo explica un supuesto material de la tesis Base —el valor intrínseco principal—: qué cifra se usa y con qué trayectoria, qué evidencia la respalda (fuente y fecha), el mecanismo económico, por qué se eligió frente a las alternativas, cómo cambia entre escenarios, qué observación obligaría a cambiarla y cuánto mueve el valor. Las sensibilidades son DCF completos de la Base con un solo supuesto cambiado. Donde falta soporte, el supuesto se declara provisional: un valor heredado de la hoja no queda validado por reproducirse aritméticamente.

**Crecimiento: doble dígito, con la nube y Copilot.** Microsoft facturó US$331.839 millones en FY2026 (+17,8%), impulsada por Azure (~+30%). La Base desacelera cada segmento: Productivity (Microsoft 365, Dynamics, LinkedIn) de 14% a 9%, Intelligent Cloud (Azure) de 25% a 13% y More Personal Computing (Windows, Xbox) casi plano. El total es 16,3% el primer año y 13,0% compuesto. Solo ~10% de las empresas de este tamaño lo lograron, pero Microsoft lleva cinco años creciendo a doble dígito con más de US$150.000 millones de ventas: es la excepción que confirma la regla. Aun así no extrapolamos el 17,8% de FY26. La Conservadora (8,0%) es un capex que rinde menos; la Disrupción (5,0%), una corrección de la demanda de cómputo para IA; la Optimista (17,5%), Microsoft como plataforma empresarial de IA. Si Azure baja a ~18% de crecimiento, la Base se cae.

**Margen: el capex todavía no está en la depreciación.** El margen operativo subió a 46,8% pese al capex, porque la depreciación todavía no refleja toda la inversión (los centros de datos se deprecian en 5-6 años). La Base usa 45% en base reportada (46,2% en el modelo, que capitaliza I+D con vida de 3 años y trata los arrendamientos como deuda): un poco menos que hoy, porque la depreciación de la IA y su menor margen frente al software empujan hacia abajo, y Copilot y el precio de Microsoft 365 empujan hacia arriba. El rango va de 38,2% a 49,2%. Por la escala de Microsoft, el margen mueve menos el valor que el crecimiento o la tasa: dos puntos llevan la Base a US$371,27 (−4%) o US$405,72 (+4%).

**Reinversión: el cambio de régimen.** Este es el punto donde Microsoft dejó de ser una empresa de software puro. El capex pasó de US$44.477 millones (FY24) a US$115.948 millones (FY26), y el flujo libre cayó a menos de la mitad. La hoja usa un ventas/capital de 0,62× en los años 1–5 y 0,70× después: cada dólar de ventas nuevas exige ~US$1,60 de capital, cuando antes bastaba una fracción. La Optimista lo baja a 0,58× porque crecer más exige todavía más centros de datos. El valor depende de que el retorno de ese capital supere el costo de capital de ~10%, y la evidencia aún es incompleta: la demanda está concentrada en pocos clientes (OpenAI). Después del año 10 la Base conserva un ROIC de 20,6%, limitado a su ROIC actual: costos de cambio y efectos de red en Office, Azure y Windows sostuvieron un ROIC de 30-72% en 2021-2026. Si el capex no rinde y el ROIC terminal cae al costo de capital, la Base vale US$270,92 (−30%): es el riesgo central de la tesis.

**Descuento y terminal.** La hoja usa una beta de 1,36; la bottom-up de software reapalancada da 1,27, una diferencia pequeña frente a la que producen las historias. El costo de capital va de 11,83% a 9,38%. El crecimiento perpetuo es 5,29%, igual a la tasa libre de riesgo, y el terminal explica 72,9% del valor operativo: tres cuartas partes del valor están más allá del año 10. Por eso la tasa pesa tanto: un punto más lleva la Base a US$307,53 (−21%), uno menos a US$522,16 (+34%).

**Probabilidades y lectura del resultado.** La Base pesa 45%, la Conservadora 25%, la Disrupción 10% y la Optimista 20%. El DCF Base es US$388,50 y el esperado US$342,95, frente a un precio de US$517,53: el mercado paga algo entre la Base y la Optimista (US$504,17). La evidencia en contra de la Base es que el flujo libre cayó a la mitad mientras el capex se triplicaba; si Azure baja a ~20% antes de que el capex se modere, la Conservadora se vuelve la central. Las acciones se fijan en 7.427,0 millones.

**Vida útil de I+D.** La hoja capitaliza el I+D (US$35.562 millones en el último año) y lo amortiza en 3 años. Mecanismo: el I+D crea activos que rinden varios años; capitalizarlo mueve el gasto del EBIT al capital invertido. La vida elegida es una convención del modelo (tabla de Damodaran por sector), no un dato reportado: una vida más larga eleva el activo y reduce el ROIC medido; una más corta hace lo contrario, y cambia también el EBIT ajustado. No se recalcula aquí porque modifica la hoja de conversión, no un input del DCF; queda provisional hasta contrastarla con la duración de los beneficios de los productos.

**Del supuesto al valor: cómo se calcula la Base.** Se parte de ventas de los últimos doce meses por US$331.839 millones. Con el crecimiento de la Base llegan a US$610.544 millones en el año 5 y a US$867.804 millones en el año 10. A esas ventas se les aplica el margen operativo, que pasa de 47,5% en el año 1 a 46,2% al final, y se descuentan impuestos (19,4% al principio y 21,0% a largo plazo): el resultado es el beneficio operativo después de impuestos (NOPAT), US$147.799 millones el primer año. Crecer no es gratis: cada dólar de ventas nuevas exige capital, y esa reinversión (+US$86.828 millones el primer año) se resta del NOPAT. Lo que queda es el flujo de caja libre de la empresa (FCFF), US$60.970 millones el primer año. Cada flujo se trae a hoy con el costo de capital (11,83% al principio, 9,38% al final): los diez años suman US$784.879 millones. Después del año 10 se supone que la empresa crece 5,29% para siempre y reinvierte lo justo para ese crecimiento con un retorno de 20,6%; esa perpetuidad vale hoy US$2.114.975 millones, 73% del total. Flujos más terminal dan el valor de las operaciones, US$2.899.854 millones. Para llegar al accionista se suma y se resta lo que no es operativo: más caja por US$76.843 millones, más activos no operativos por US$36.348 millones, menos deuda por US$127.658 millones (incluye los arrendamientos capitalizados). Queda un patrimonio de US$2.885.387 millones que, repartido entre 7.427,0 millones de acciones, da US$388,50 por acción. Las otras tres historias siguen exactamente el mismo camino con sus propios supuestos; el DCF esperado es su promedio ponderado por probabilidad.

**Múltiplos (lectura secundaria).** Caso Base de los múltiplos: EV/EBITDA 20,12× (peso 25% dentro de los múltiplos); EV/FCFF 42,41× (peso 38% dentro de los múltiplos); P/E 27,08× (peso 12% dentro de los múltiplos); P/FCFE 43,39× (peso 12% dentro de los múltiplos); P/OCF 20,67× (peso 12% dentro de los múltiplos). Cada múltiplo se elige con tres anclas documentadas en la hoja (historia depurada de la empresa, peers ajustados y múltiplo justificado por crecimiento, riesgo y retorno); el precio resultante a FY+1..FY+3, más dividendos, se trae a hoy con el costo del patrimonio (12,0%). Son precio relativo, no valor intrínseco: si el mercado entero está caro, también lo estará el múltiplo. Solo hay tres casos auxiliares (Conservador, Base y Optimista); no se inventa un resultado de Disrupción. La tabla por método está en la valoración vigente.

Sensibilidad del DCF Base (US$388,50; cada fila es un DCF completo con un solo supuesto cambiado):

| Supuesto cambiado | DCF Base | Variación |
|---|---:|---:|
| Margen objetivo −2 pp | US$371,27 | −4,4% |
| Margen objetivo +2 pp | US$405,72 | +4,4% |
| Crecimiento años 1–5 −2 pp | US$353,74 | −8,9% |
| Crecimiento años 1–5 +2 pp | US$426,95 | +9,9% |
| Ventas/capital −20% | US$372,45 | −4,1% |
| Ventas/capital +20% | US$399,20 | +2,8% |
| WACC +1 pp | US$307,53 | −20,8% |
| WACC −1 pp | US$522,16 | +34,4% |
| Crecimiento terminal −0,5 pp | US$361,74 | −6,9% |
| Crecimiento terminal +0,5 pp | US$422,63 | +8,8% |
| ROIC terminal = costo de capital | US$270,92 | −30,3% |
| Acciones +5% | US$370,00 | −4,8% |


### Piezas del valor

**Crecimiento.** Ingresos de US$245.122 millones (FY24, +15,7%), US$281.724 millones (FY25, +14,9%) y US$331.839 millones (FY26, +17,8%). En FY25: Productivity US$120.810 millones (+12%), Intelligent Cloud US$106.265 millones (+20%) y More Personal Computing US$54.649 millones (+5%). En FY26, según los trimestres publicados, ~+16%, ~+30% y ~−1%. La división FY26 de las historias aplica esos crecimientos a FY25 (estimación propia).

| US$ millones | FY24 | FY25 | FY26 |
|---|---:|---:|---:|
| Ingresos | 245.122 | 281.724 | 331.839 |
| Crecimiento | +15,7% | +14,9% | +17,8% |
| Margen operativo | 44,6% | 45,6% | 46,8% |
| Capex | 44.477 | 64.551 | 115.948 |
| FCFF (hoja) | 73.144 | 66.125 | 30.557 |

**Márgenes.** El margen operativo subió a 46,8% pese al capex porque la depreciación todavía no refleja toda la inversión. La hoja supone 46,3% el próximo año y 45% de objetivo. La depreciación de los centros de datos de IA (vidas útiles de 5-6 años) y los márgenes menores de la infraestructura de IA frente al software empujan hacia abajo; Copilot y el precio de Microsoft 365 empujan hacia arriba. Las historias van de 37% a 48%.

**Reinversión y retorno.** La hoja usa un ventas/capital de 0,62 (años 1-5) y 0,70 (años 6-10): con margen objetivo de 46,2% e impuesto marginal de 21%, cada dólar de capital nuevo rinde ~23% y ~26%, sin superar el mayor entre su ROIC actual (25,4%) y el de su industria (20,6%) (Damodaran, Investment Valuation cap. 11, p. 45; revisión del 4-oct-2026). Antes 0,62 y 0,94, que implicaban ~23% y ~34% sobre el capital nuevo. En la historia Optimista se baja a 0,6. El valor depende de que el retorno de ese capital (ROIC incremental) supere el costo de capital de ~10%. Ventaja durable: costos de cambio y efectos de red (Office, Azure, Windows, LinkedIn), con ROIC de 30-72% en 2021-2026. El ROIC después del año 10 es 25,4%, el promedio de su industria según Damodaran (29,3%), limitado a su ROIC actual. Es el criterio de Damodaran para ventajas sostenibles; el riesgo de perderla está en las historias de erosión.

**Ventas/capital: las referencias de Damodaran.** Damodaran elige el ventas/capital mirando el de la empresa hoy, el marginal de los últimos años y el promedio del sector, y comprueba que el rendimiento que implica sobre el capital nuevo sea creíble frente a lo que gana la empresa o su sector (Investment Valuation, cap. 11, p. 44-46). El capital de cada cierre se arma como el del modelo (patrimonio, incluido el preferente, + deuda y arrendamientos − caja e inversiones, + I+D capitalizado). El marginal es volátil: recompras, deterioros y moneda mueven el capital contable. El usado está dentro del rango de las referencias.

| Referencia | Ventas/capital | Detalle |
|---|---:|---|
| Empresa hoy | 0,63 | ventas LTM 331.839,0 / capital invertido 523.911,1 millones (con I+D capitalizado a 3 años) |
| Marginal, últimos tres años | 0,47 | Δventas 119.924,0 / Δcapital 257.590,7 millones (Jun '23 → Jun '26; capital 195.488,7 → 453.079,3) |
| Marginal, últimos cinco años | 0,48 | Δventas 163.751,0 / Δcapital 340.447,0 millones (Jun '21 → Jun '26; capital 112.632,3 → 453.079,3) |
| Sector (Damodaran, enero de 2026) | 1,54 | Software (System & Application) |
| Usado en la hoja | 0,62 / 0,70 | años 1-5 / 6-10; rinde ~23% / ~26% sobre el capital nuevo (ROIC actual 25,4%) |

**Arrendamientos (criterio Damodaran).** Los arrendamientos operativos son deuda: su valor presente (US$20.770 millones, compromisos del 10-Q al 2026-06-30) se suma a la deuda y al peso de la deuda del WACC, y el alquiler deja de ser gasto operativo: el EBIT suma el gasto de arrendamiento y resta la depreciación del activo arrendado (US$4.001 millones, +1,21 pp de margen). Por eso los márgenes del modelo y de las historias están en base ajustada (el margen reportado del texto más ese ajuste), y el ventas/capital incluye el capital arrendado (cada dólar de ventas exige además 0,06 dólares de activo arrendado). Fuente: Damodaran, *Leases, Debt and Value* y *Dealing with Operating Leases in Valuation*.

**Riesgo.** La hoja usa una beta de 1,34. La bottom-up de Software (System & Application) reapalancada da 1,27; el DCF Base sube de US$467,13 a US$477,29. La diferencia es pequeña frente a la que producen las historias; el riesgo real está en el retorno del capex, no en la tasa.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,36 | 12,0% | 11,8% | US$427,38 |
| Bottom-up del sector (Software (System & Application), reapalancada) | 1,27 | 11,6% | 11,4% | US$437,67 |


### Ventaja competitiva y ROIC terminal: comprobación

| Ventaja (criterio Damodaran) | ROIC actual (modelo) | ROIC de la industria (Damodaran) | Costo de capital terminal | ROIC terminal usado | DCF Base de la hoja | DCF con ROIC terminal = costo de capital |
|---|---:|---:|---:|---:|---:|---:|
| Ventaja durable | 25,4% | 20,6% | 9,4% | 20,6% | US$388,50 | US$292,69 |

Fuentes de ventaja: Costos de cambio y efectos de red (Office, Azure, Windows, LinkedIn). Evidencia: ROIC 30-72% en 2021-2026. Criterio (Damodaran, *Investment Valuation*, cap. 12): sin ventaja defendible, el ROIC en crecimiento estable es el costo de capital; con una ventaja durable, el promedio de la industria, sin superar el ROIC actual; si la ventaja se desvanece de forma visible, el punto medio entre ambos. El riesgo de perder la ventaja va en las historias de erosión, que usan el costo de capital. El ROIC actual del motor y el histórico GAAP pueden diferir por I+D, arrendamientos y plusvalía.


### De dónde sale el cálculo: de la historia al valor por acción

El valor intrínseco principal es el DCF Base: US$388,50 por acción, un DCF completo de diez años más valor terminal con la trayectoria central defendida. Como complemento se ejecutan otros tres DCF completos (Conservadora, Disrupción y Optimista) y se ponderan las cuatro historias por sus probabilidades: el DCF esperado es US$342,95. Cada historia tiene su propia trayectoria de ventas, margen objetivo, crecimiento terminal y retorno terminal. Ninguna cifra se obtiene mezclando el DCF con múltiplos. «Base» y «esperado» son conceptos distintos: la Base es la historia central; el esperado, un promedio de desenlaces con pesos subjetivos.


#### 1. Datos de partida y origen de los supuestos

| Entrada | Valor usado | Origen y tratamiento |
|---|---|---|
| Ingresos LTM | US$331.839 millones | Input sheet B12: últimos doce meses de los estados financieros (ver fuentes). Por segmentos: 140.116 + 138.116 + 53.606 = 331.839. |
| Margen inicial del DCF | 47,5% en año 1 | Valuation output C6 (base ajustada del modelo). Converge al margen objetivo de cada historia en el año 7 (Input sheet B31). |
| Impuesto | 19,40% en años 1–5; 21,00% en terminal | Tasa efectiva y marginal de la hoja; la efectiva converge linealmente a la marginal en los años 6–10. No hay pérdidas fiscales iniciales. |
| Descuento | WACC 11,83% → 9,38% | Tasa libre de riesgo 5,29%, beta 1,36, ERP 4,96%. Constante en años 1–5 y converge linealmente en los años 6–10. Es la misma en las cuatro historias. |
| Ventas/capital | 0,62x en años 1–5; 0,70x en años 6–10 | Input sheet B32/B33: hipótesis del analista, no datos reportados. Optimista usa 0,58x en años 1–5. |
| Crecimiento perpetuo | Base/Conservadora/Optimista: 5,29%; Disrupción: 4,80% | Terminal de la hoja (Valuation output M4, igual a la tasa libre de riesgo) en las historias que no lo cambian. Disrupción se estabiliza sin recuperarse: mantiene su crecimiento del año 5 (4,80%) en los años 6–10 y en perpetuidad, en lugar de subir al terminal de la hoja. Es criterio del analista (Damodaran, *The Stable Growth Rate*: el crecimiento estable puede ser menor que la economía), no guía de la empresa. |
| ROIC terminal | Base/Optimista: 20,56%; Conservadora/Disrupción: 9,38% (= WACC terminal) | Criterio de ventaja competitiva (ventaja durable). Las historias de erosión igualan el retorno al costo de capital: una ventaja que se pierde no deja retornos excedentes para siempre. |
| Puente al patrimonio | Caja 76.843; deuda 127.658; activos no operativos 36.348; acciones 7.427,0 millones | Valuation output B29/B27/B30/B28/B32/B34. Acciones fijas: no se proyecta recompra ni dilución. |


#### 2. Cómo se convierte cada historia en ingresos

Para cada segmento: ingreso del año t = ingreso del año anterior × (1 + crecimiento de ese segmento). Se suman los segmentos para obtener las ventas de la empresa. Las tasas de la tabla «Historias cuantificadas» son hipótesis del analista; los informes de la empresa aportan el punto de partida, no estas cuatro trayectorias. En los años 6–10 el crecimiento converge linealmente al terminal de cada historia.

Ejemplo Base, año 1: 140.116 × 1,14 + 138.116 × 1,25 + 53.606 × 1,00 = US$385.984,36 millones. Frente a 331.839, el crecimiento consolidado es 16,32%. En los años 2–5 es 14,05%, 12,72%, 11,55%, 10,30%; las ventas del año 5 son US$610.544,46 millones. El 13,0% de la tabla es el crecimiento anual compuesto de los cinco años: (610.544,46 / 331.839)^(1/5) − 1; no se usa como tasa constante.


#### 3. Del ingreso al flujo libre y su valor presente

NOPATₜ = ventasₜ × margen operativoₜ × (1 − impuestoₜ). La reinversión explícita es (ventasₜ₊₁ − ventasₜ) / ventas-capital: financia el crecimiento del año siguiente. FCFFₜ = NOPATₜ − reinversiónₜ. No se resta además el capex como una segunda reinversión.

En la Base, año 1: NOPAT = 385.984,36 × 47,51% × (1 − 19,40%) = US$147.798,69 millones. La reinversión es US$86.828,46 millones y el FCFF es US$60.970,24 millones. Cada FCFF se descuenta con el producto de las tasas de cada año: VP(FCFFₜ) = FCFFₜ / [(1 + WACC₁) × … × (1 + WACCₜ)].

En perpetuidad: reinversión terminal = NOPAT₁₁ × g / ROIC terminal; valor terminal al final del año 10 = FCFF₁₁ / (WACC terminal − g), con WACC terminal 9,38%. Reinversión terminal sobre el NOPAT: Base, 25,7% (5,29% / 20,56%); Conservadora, 56,4% (5,29% / 9,38%); Disrupción, 51,2% (4,80% / 9,38%); Optimista, 25,7% (5,29% / 20,56%). Una reinversión neta nula no significa gasto bruto cero: es mantener el capital económico en estado estable.


#### 4. Trayectoria anual de cada historia

Cada historia es un DCF completo. Estas tablas muestran, año por año, lo que la hoja calcula en los bloques de 'Valuation output': ingresos, crecimiento, margen operativo, NOPAT, reinversión, flujo libre (FCFF), WACC y su valor presente. Importes en millones; la fila «Terminal» es el primer año de la perpetuidad (su valor terminal se descuenta con el factor del año 10).

**Base · Azure y Copilot sostienen el doble dígito** — probabilidad 45%; valor terminal 6.056.525 (VP 2.114.975); DCF US$388,50 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 385.984 | 16,3% | 47,5% | 147.799 | 86.828 | 60.970 | 11,8% | 54.518 |
| 2 | 440.217 | 14,1% | 47,1% | 167.247 | 89.628 | 77.619 | 11,8% | 62.061 |
| 3 | 496.199 | 12,7% | 46,9% | 187.773 | 91.773 | 96.000 | 11,8% | 68.635 |
| 4 | 553.521 | 11,6% | 46,8% | 208.636 | 91.297 | 117.340 | 11,8% | 75.015 |
| 5 | 610.544 | 10,3% | 46,6% | 229.216 | 90.904 | 138.312 | 11,8% | 79.066 |
| 6 | 667.323 | 9,3% | 46,4% | 248.540 | 79.099 | 169.441 | 11,3% | 86.993 |
| 7 | 722.692 | 8,3% | 46,2% | 267.014 | 75.313 | 191.701 | 10,9% | 88.786 |
| 8 | 775.411 | 7,3% | 46,2% | 285.343 | 69.703 | 215.640 | 10,4% | 90.496 |
| 9 | 824.203 | 6,3% | 46,2% | 302.076 | 62.286 | 239.790 | 9,9% | 91.591 |
| 10 | 867.804 | 5,3% | 46,2% | 316.770 | 65.581 | 251.189 | 9,4% | 87.717 |
| Terminal | 913.710 | 5,3% | 46,2% | 333.527 | 85.815 | 247.712 | 9,4% | — |

**Conservadora · El capex de IA rinde menos de lo esperado** — probabilidad 25%; valor terminal 2.354.539 (VP 822.219); DCF US$201,69 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 369.639 | 11,4% | 47,5% | 141.540 | 51.053 | 90.487 | 11,8% | 80.912 |
| 2 | 401.527 | 8,6% | 45,7% | 147.925 | 47.879 | 100.045 | 11,8% | 79.992 |
| 3 | 431.432 | 7,4% | 44,8% | 155.812 | 43.668 | 112.144 | 11,8% | 80.178 |
| 4 | 458.707 | 6,3% | 43,9% | 162.335 | 46.760 | 115.575 | 11,8% | 73.887 |
| 5 | 487.914 | 6,4% | 43,0% | 169.131 | 48.055 | 121.077 | 11,8% | 69.213 |
| 6 | 517.929 | 6,2% | 42,1% | 175.079 | 43.922 | 131.157 | 11,3% | 67.337 |
| 7 | 548.675 | 5,9% | 41,2% | 180.783 | 44.841 | 135.941 | 10,9% | 62.961 |
| 8 | 580.064 | 5,7% | 41,2% | 190.358 | 45.621 | 144.737 | 10,4% | 60.741 |
| 9 | 611.999 | 5,5% | 41,2% | 200.030 | 46.250 | 153.780 | 9,9% | 58.738 |
| 10 | 644.373 | 5,3% | 41,2% | 209.759 | 48.696 | 161.063 | 9,4% | 56.244 |
| Terminal | 678.461 | 5,3% | 41,2% | 220.856 | 124.555 | 96.301 | 9,4% | — |

**Disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige** — probabilidad 10%; valor terminal 1.803.978 (VP 629.960); DCF US$168,69 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 355.252 | 7,1% | 47,5% | 136.031 | 22.601 | 113.430 | 11,8% | 101.427 |
| 2 | 369.368 | 4,0% | 44,8% | 133.525 | 25.489 | 108.036 | 11,8% | 86.381 |
| 3 | 385.289 | 4,3% | 43,5% | 135.154 | 29.420 | 105.735 | 11,8% | 75.595 |
| 4 | 403.665 | 4,8% | 42,2% | 137.278 | 31.050 | 106.227 | 11,8% | 67.911 |
| 5 | 423.058 | 4,8% | 40,9% | 139.343 | 32.542 | 106.801 | 11,8% | 61.052 |
| 6 | 443.384 | 4,8% | 39,5% | 140.727 | 30.432 | 110.295 | 11,3% | 56.627 |
| 7 | 464.686 | 4,8% | 38,2% | 141.962 | 31.894 | 110.068 | 10,9% | 50.978 |
| 8 | 487.012 | 4,8% | 38,2% | 148.186 | 33.426 | 114.760 | 10,4% | 48.161 |
| 9 | 510.410 | 4,8% | 38,2% | 154.680 | 35.032 | 119.648 | 9,9% | 45.701 |
| 10 | 534.933 | 4,8% | 38,2% | 161.456 | 36.715 | 124.741 | 9,4% | 43.560 |
| Terminal | 560.634 | 4,8% | 38,2% | 169.213 | 86.671 | 82.542 | 9,4% | — |

**Optimista · Microsoft gana la plataforma empresarial de IA** — probabilidad 20%; valor terminal 8.390.488 (VP 2.930.009); DCF US$504,17 por acción.

| Año | Ingresos | Crecimiento | Margen | NOPAT | Reinversión | FCFF | WACC | VP del FCFF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 400.928 | 20,8% | 47,5% | 153.521 | 136.469 | 17.052 | 11,8% | 15.247 |
| 2 | 479.846 | 19,7% | 48,0% | 185.618 | 149.099 | 36.520 | 11,8% | 29.200 |
| 3 | 566.067 | 18,0% | 48,2% | 220.079 | 152.250 | 67.829 | 11,8% | 48.495 |
| 4 | 654.111 | 15,6% | 48,5% | 255.590 | 156.460 | 99.130 | 11,8% | 63.374 |
| 5 | 744.589 | 13,8% | 48,7% | 292.401 | 156.104 | 136.297 | 11,8% | 77.914 |
| 6 | 834.861 | 12,1% | 49,0% | 328.174 | 124.219 | 203.955 | 11,3% | 104.713 |
| 7 | 921.815 | 10,4% | 49,2% | 362.697 | 114.659 | 248.038 | 10,9% | 114.878 |
| 8 | 1.002.076 | 8,7% | 49,2% | 392.695 | 100.185 | 292.510 | 10,4% | 122.756 |
| 9 | 1.072.206 | 7,0% | 49,2% | 418.485 | 81.028 | 337.457 | 9,9% | 128.896 |
| 10 | 1.128.925 | 5,3% | 49,2% | 438.841 | 85.314 | 353.527 | 9,4% | 123.454 |
| Terminal | 1.188.645 | 5,3% | 49,2% | 462.056 | 118.885 | 343.171 | 9,4% | — |


#### 5. Puente numérico de los cuatro DCF

Importes en US$ millones salvo el DCF por acción. Se calcula con precisión completa y se redondea solo al presentar.

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja y deuda | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 784.878,73 | 2.114.974,84 | 2.899.853,57 | 2.885.386,75 | 388,50 |
| Conservadora | 690.203,48 | 822.219,05 | 1.512.422,53 | 1.497.955,72 | 201,69 |
| Disrupción | 637.393,38 | 629.959,80 | 1.267.353,18 | 1.252.886,37 | 168,69 |
| Optimista | 828.924,94 | 2.930.008,57 | 3.758.933,51 | 3.744.466,70 | 504,17 |

Ejemplo Base: (784.878,73 + 2.114.974,84 + 76.843 + 36.348 − 127.658) / 7.427,0 = US$388,50 por acción. El terminal representa 72,9% del valor operativo de la Base: el resultado depende materialmente del crecimiento perpetuo, del WACC terminal y de la duración del retorno excedente.


#### 6. DCF esperado (complemento), probabilidades y margen de seguridad

Las probabilidades 45% / 25% / 10% / 20% son juicio del analista (ver «Historias cuantificadas»): no se estimaron con un modelo estadístico ni se deducen de las tasas base. Deben leerse como pesos discutibles y revisables, no como precisión empírica.

DCF esperado = 0,45 × 388,499630 + 0,25 × 201,690551 + 0,10 × 168,693465 + 0,20 × 504,169476 = US$342,950713 ≈ US$342,95. Los aportes son US$174,82 + US$50,42 + US$16,87 + US$100,83 por acción.

Precio con MOS = DCF esperado × (1 − 35%) = 342,950713 × 0,65 = US$222,917963 ≈ US$222,92. El 35% es la política de margen de seguridad del analista para este tipo de empresa; no lo estima el DCF. Se aplica al esperado, no al DCF Base: la jerarquía de presentación (Base primero) no cambia esa fórmula.

Trazabilidad: la hoja calcula cada historia en 'Valuation output' con la estructura de Damodaran: Base en las filas 2–42 (valor por acción B35), Conservadora 53–93 (B86), Optimista 104–144 (B137) y Disrupción 157–197 (B190). La pestaña «Escenarios e historias» guarda los supuestos de cada historia y resume los resultados: A5:J8; esperado H10; Base H11; rango H12:H13; MOS H14. Las fórmulas de la hoja y el motor del Modelo JMR dan los mismos cuatro resultados; esa concordancia verifica la aritmética, no la validez económica de los supuestos.


### Las cuatro tesis: Base, Conservadora, Disrupción y Optimista

La tesis Base es la trayectoria central defendida y su DCF, US$388,50, es el valor intrínseco principal. El DCF esperado de US$342,95 combina las cuatro tesis con sus probabilidades y se presenta como complemento. Disrupción describe un deterioro estructural del negocio; no presupone IA ni quiebra.


#### Base: Azure y Copilot sostienen el doble dígito

**Qué plantea.** Es la continuación de FY24-FY26 con desaceleración gradual.

**Traducción al modelo.** Productivity and Business Processes crece 14%, 12%, 11%, 10%, 9%; Intelligent Cloud crece 25%, 20%, 17%, 15%, 13%; More Personal Computing crece 0%, 1%, 2%, 2%, 2%. El crecimiento anual compuesto de cinco años es 13,0%; el margen operativo objetivo es 46,2%. El ROIC terminal es 20,6%. El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 45%; DCF: US$388,50 por acción.

**Cómo contrastarla.** Se sostiene mientras los indicadores sigan cerca de sus niveles de hoy (azure y otros servicios de nube (interanual): ~+30% (FY26); microsoft 365 comercial / Copilot: En alza; capex / ingresos: ~35% (FY26)). Pierde peso si cruzan cualquiera de los umbrales de la tabla de indicadores.


#### Conservadora: El capex de IA rinde menos de lo esperado

**Qué plantea.** Es un capex que rinde menos: precios de cómputo en baja y menor dependencia de OpenAI.

**Traducción al modelo.** Productivity and Business Processes crece 10%, 8%, 7%, 6%, 6%; Intelligent Cloud crece 18%, 12%, 10%, 8%, 8%; More Personal Computing crece -2%, 0%, 0%, 1%, 1%. El crecimiento anual compuesto de cinco años es 8,0%; el margen operativo objetivo es 41,2%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 25%; DCF: US$201,69 por acción.

**Cómo contrastarla.** La apoyarían: azure y otros servicios de nube (interanual): ≤ +18%; microsoft 365 comercial / Copilot: asientos de Copilot estancados; capex / ingresos: sube sin aceleración de Azure; margen operativo: ≤ 42%.


#### Disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige

**Qué plantea.** Es una corrección de la demanda de cómputo.

**Traducción al modelo.** Productivity and Business Processes crece 8%, 6%, 5%, 5%, 5%; Intelligent Cloud crece 10%, 4%, 5%, 6%, 6%; More Personal Computing crece -3%, -2%, 0%, 0%, 0%. El crecimiento anual compuesto de cinco años es 5,0%; el margen operativo objetivo es 38,2%. El ROIC terminal es el costo de capital (9,38%). El crecimiento terminal es 4,80%: se mantiene el crecimiento del año 5, sin recuperación. Probabilidad: 10%; DCF: US$168,69 por acción.

**Cómo contrastarla.** La apoyaría, con más intensidad y duración que la Conservadora: azure y otros servicios de nube (interanual): ≤ +18%; microsoft 365 comercial / Copilot: asientos de Copilot estancados; capex / ingresos: sube sin aceleración de Azure; margen operativo: ≤ 42%.


#### Optimista: Microsoft gana la plataforma empresarial de IA

**Qué plantea.** Es Microsoft como plataforma empresarial de IA (Copilot en cada asiento, Azure como infraestructura dominante).

**Traducción al modelo.** Productivity and Business Processes crece 17%, 16%, 15%, 13%, 12%; Intelligent Cloud crece 32%, 28%, 24%, 20%, 17%; More Personal Computing crece 2%, 3%, 3%, 3%, 3%. El crecimiento anual compuesto de cinco años es 17,5%; el margen operativo objetivo es 49,2%. El ROIC terminal es 20,6%. El crecimiento terminal es 5,29%, el de la hoja. Probabilidad: 20%; DCF: US$504,17 por acción.

**Cómo contrastarla.** La confirmarían: azure y otros servicios de nube (interanual): ≥ +25%; microsoft 365 comercial / Copilot: ARPU creciendo ≥ 8%; capex / ingresos: estable o bajando con ingresos creciendo; margen operativo: ≥ 45%.

**Reglas comunes.** Los cuatro DCF usan la misma tasa de descuento y la misma estructura de impuestos y deuda. Crecimiento terminal: Base/Conservadora/Optimista: 5,29%; Disrupción: 4,80%. Las diferencias proceden de ventas, margen, crecimiento terminal y ROIC terminal. Las probabilidades son juicio del analista y suman 100%; no son datos publicados por la empresa. La tesis de disrupción se separa de la conservadora porque plantea una pérdida estructural de la ventaja; la conservadora, una erosión gradual.


### Historias cuantificadas: DCF Base y DCF esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | CAGR de ingresos del grupo (años 1–5) | Margen objetivo | Sales-to-capital | ROIC después del año 10 | Crecimiento terminal | Valor/acción (beta 1,36) | Valor/acción (beta 1,27) |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|
| **Base · Azure y Copilot sostienen el doble dígito** | 45% | Productivity and Business Processes: 14%, 12%, 11%, 10%, 9%; Intelligent Cloud: 25%, 20%, 17%, 15%, 13%; More Personal Computing: 0%, 1%, 2%, 2%, 2% | 13,0% | 46,2% | 0,6 | 20,6% | 5,29% | US$388,50 | US$397,71 |
| **Conservadora · El capex de IA rinde menos de lo esperado** | 25% | Productivity and Business Processes: 10%, 8%, 7%, 6%, 6%; Intelligent Cloud: 18%, 12%, 10%, 8%, 8%; More Personal Computing: -2%, 0%, 0%, 1%, 1% | 8,0% | 41,2% | 0,6 | = costo de capital | 5,29% | US$201,69 | US$206,04 |
| **Disrupción · Deterioro de los fundamentales: La demanda de cómputo para IA se corrige** | 10% | Productivity and Business Processes: 8%, 6%, 5%, 5%, 5%; Intelligent Cloud: 10%, 4%, 5%, 6%, 6%; More Personal Computing: -3%, -2%, 0%, 0%, 0% | 5,0% | 38,2% | 0,6 | = costo de capital | 4,80% | US$168,69 | US$172,16 |
| **Optimista · Microsoft gana la plataforma empresarial de IA** | 20% | Productivity and Business Processes: 17%, 16%, 15%, 13%, 12%; Intelligent Cloud: 32%, 28%, 24%, 20%, 17%; More Personal Computing: 2%, 3%, 3%, 3%, 3% | 17,5% | 49,2% | 0,6 | 20,6% | 5,29% | US$504,17 | US$516,55 |
| **DCF esperado (complemento)** | 100% |  |  |  |  |  |  | **US$342,95** | **US$351,00** |

Base (45%) es la continuación de FY24-FY26 con desaceleración gradual. Conservadora (25%) es un capex que rinde menos: precios de cómputo en baja y menor dependencia de OpenAI. Disrupción (10%) es una corrección de la demanda de cómputo. Optimista (20%) es Microsoft como plataforma empresarial de IA (Copilot en cada asiento, Azure como infraestructura dominante). En las historias de erosión (Conservadora y Disrupción) el ROIC después del año 10 es el costo de capital. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 1,36; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

Cada celda ejecuta un DCF completo, sin reescalar el resultado. Aquí el crecimiento es constante en años 1–5; si la hoja tiene un año 1 distinto de años 2–5, el centro puede diferir del DCF Base de la hoja.

| Crecimiento \ Margen | 42,2% | 44,2% | 46,2% | 48,2% | 50,2% |
|---|---:|---:|---:|---:|---:|
| 9,0% | 301,18 | 315,30 | 329,42 | 343,54 | 357,66 |
| 11,0% | 330,21 | 346,15 | 362,09 | 378,03 | 393,97 |
| 13,0% | 362,32 | 380,29 | 398,26 | 416,23 | 434,19 |
| 15,0% | 397,83 | 418,04 | 438,26 | 458,48 | 478,69 |
| 17,0% | 437,03 | 459,75 | 482,46 | 505,17 | 527,89 |


### Pre-mortem

1. OpenAI diversifica proveedores de cómputo y Azure pierde su cliente de IA más grande.
2. Copilot no convence: la adopción pagada se estanca y Microsoft 365 crece solo por precio.
3. Exceso de capacidad de centros de datos en 2028: precios de GPU en la nube bajan y hay deterioro de activos.
4. Falta energía o chips y Microsoft no puede entregar la capacidad vendida.
5. Regulación (competencia en la nube y en IA) limita la venta atada de productos.

**Evidencia en contra de la historia más probable:** el FCFF cayó a menos de la mitad en dos años mientras el capex se triplicó; si el crecimiento de Azure baja a ~20% antes de que el capex se modere, la historia Conservadora se vuelve la central.


### Indicadores y actualización de probabilidades

| Indicador | Hoy | Refuerza historias favorables si… | Refuerza historias desfavorables si… |
|---|---|---|---|
| Azure y otros servicios de nube (interanual) | ~+30% (FY26) | ≥ +25% | ≤ +18% |
| Microsoft 365 comercial / Copilot | En alza | ARPU creciendo ≥ 8% | Asientos de Copilot estancados |
| Capex / ingresos | ~35% (FY26) | Estable o bajando con ingresos creciendo | Sube sin aceleración de Azure |
| Margen operativo | 46,8% | ≥ 45% | ≤ 42% |
| Dependencia de OpenAI | Alta | Base de clientes de IA diversificada | Pérdida de cargas de OpenAI |

Cada trimestre, mueve 5-10 pp de probabilidad entre historias según hacia dónde apunten los indicadores; no cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen, reinversión o riesgo).


### El precio al final

Precio de referencia de la valoración guardada: **US$517,53**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 41% | Margen 46% | Margen 49% |
|---|---:|---:|---:|
| Beta 1,36 | 21,1% (2% de las empresas) | 18,4% (3% de las empresas) | 17,0% (4% de las empresas) |
| Beta 1,27 | 20,6% (2% de las empresas) | 17,9% (3% de las empresas) | 16,5% (5% de las empresas) |

Frente al DCF Base (US$388,50), el valor intrínseco principal, el precio está por encima en 33%.

Frente al DCF esperado de las historias (US$342,95 con la beta de la hoja; US$351,00 con la propuesta), el precio está por encima en 51% y por encima en 47%, respectivamente. La comparación es condicional a las historias y a su probabilidad. La diferencia frente al precio no constituye una recomendación. Revisar primero las métricas operativas y los supuestos de reinversión si el mercado exige una historia distinta.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Plataforma de software empresarial que apuesta su capital a la infraestructura de IA |  |
| Probabilidades | Base 45% / Conservadora 25% / Disrupción 10% / Optimista 20% |  |
| DCF Base hoy (valor intrínseco principal) | US$388,50 |  |
| DCF esperado por probabilidades (complemento) (beta de la hoja / propuesta) | US$342,95 / US$351,00 |  |
| Precio con MOS sobre el DCF esperado | US$222,92 (MOS 35%) |  |
| Rango (historia más débil a más fuerte) | US$168,69 a US$516,55 |  |
| Confianza | Media: el negocio es excepcional; el retorno del capex de IA no está probado |  |
| Qué cambiaría la opinión | Crecimiento de Azure frente al capex; adopción pagada de Copilot |  |
| Revisión | Resultados del 1T FY27 (oct-2026) |  |

La decisión (comprar, mantener o vender) la registras tú con el selector «Mi decisión» de la app; este análisis no la toma por ti.


### Fuentes de esta sección

- [Microsoft, resultados del 4T FY2026](https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast)
- [Microsoft, ingresos por segmento del 4T FY2025](https://www.microsoft.com/en-us/investor/earnings/fy-2025-q4/segment-revenues)
- [Digital Applied, resultados FY26 Q4 y ARR de Copilot](https://www.digitalapplied.com/blog/microsoft-fy26-q4-earnings-copilot-arr)
- [CNBC, resultados de AWS del 2T 2026](https://www.cnbc.com/2026/07/30/aws-earnings-q2-2026.html)
- [Mauboussin & Callahan, The Base Rate Book (2016)](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf)
- [Damodaran, Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
