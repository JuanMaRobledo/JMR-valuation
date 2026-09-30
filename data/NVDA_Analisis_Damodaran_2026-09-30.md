---
schema: "jmr-analisis-damodaran-v1"
ticker: "NVDA"
analysis_date: "2026-09-30"
---

# NVIDIA Corporation (NVDA) — Valor con criterio Damodaran

> Sección 12 del análisis fundamental (prompt v5). Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.
Esta sección sigue el orden de Damodaran y Mauboussin para no anclarse en el precio: historia, visión externa, piezas del valor, historias cuantificadas y, recién al final, el precio. Los valores se calculan con el motor del Modelo JMR calibrado para que el escenario Base reproduzca el DCF de la hoja (US$259,29 por acción); la hoja no se modifica. El valor intrínseco es el DCF; los múltiplos son precio relativo y se comentan en otras secciones.


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
| C · La IA es infraestructura permanente | 25,3% | 1% |
| D · Chips propios de los clientes y corrección fuerte | -1,3% | 79% |

Para empresas de más de US$50.000 millones, crecer 17% anual cinco años (historia A) lo logró ~4%; 25% (historia C), ~1%. NVIDIA ya rompió todas las tasas base en 2024-2026, pero la visión externa es clara: sostener crecimientos así desde US$300.000 millones de ventas casi no tiene precedentes, y en semiconductores los ciclos de sobreinversión terminan en correcciones.


### Piezas del valor

**Crecimiento.** Ingresos de US$60.922 millones (FY24, +126%), US$130.497 millones (FY25, +114%) y US$215.938 millones (FY26, +65%); LTM US$302.970 millones. En el 2T FY27 (jul-2026) facturó US$96.220 millones, con Data Center en US$89.000 millones (+117%). La hoja supone +50% el próximo año y 14% en los años 2-5. Nota de método: el motor usa el crecimiento anual compuesto de los años 1-5, así que una historia con un año muy fuerte y una corrección posterior se valora por su promedio.

| US$ millones | FY24 | FY25 | FY26 | LTM |
|---|---:|---:|---:|---:|
| Ingresos | 60.922 | 130.497 | 215.938 | 302.970 |
| Crecimiento | +126% | +114% | +65% | — |
| Margen operativo | 54,1% | 62,4% | 60,4% | 65,2% |
| FCFF (hoja) | 17.211 | 46.706 | 83.173 | — |

**Márgenes.** El margen operativo (54-65%) es de monopolio temporal: precio altísimo por escasez, poco capital (fabless) y software propio. La hoja supone 60% el próximo año y 58% de objetivo. Las fuerzas en contra son la competencia (AMD MI400, TPU, Trainium) y el poder de negociación de cinco clientes enormes; a favor, la escala y el ecosistema CUDA. Las historias van de 40% (corrección fuerte) a 60%.

**Reinversión y retorno.** Como fabless, NVIDIA casi no invierte en activos fijos; su reinversión es I+D (US$18.497 millones en FY26), compromisos de capacidad con TSMC y capital de trabajo. La hoja usa un sales-to-capital de 3 y 2,5. En 2026 la empresa subió el dividendo 25 veces y aprobó recompras por US$80.000 millones: señal de que genera más caja de la que puede reinvertir. Desde la revisión del 30-sep-2026, el ROIC después del año 10 es 27,2% (el de Semiconductor; el actual supera 100%); antes era igual al costo de capital.

**Riesgo.** La hoja usaba una beta de regresión de 1,90 (costo del patrimonio 13,5%). Tras la revisión del 30-sep-2026 usa la bottom-up de Semiconductor (66 empresas, 1,50 desapalancada y corregida por caja; 1,51 sin deuda relevante), con costo del patrimonio de 11,7%: el DCF Base pasó de US$162,65 a US$178,38. La ciclicidad del negocio se modela en las historias (B y D), no en la tasa.

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja (regresión o la cargada en el libro) | 1,51 | 11,7% | 11,7% | US$259,29 |
| Bottom-up del sector (Semiconductor, reapalancada) | 1,51 | 11,7% | 11,7% | US$259,57 |


### Historias cuantificadas y valor esperado

| Historia | Probabilidad | Crecimiento por segmento (años 1-5) | Crecimiento anual del grupo | Margen objetivo | Sales-to-capital | Valor/acción (beta 1,51) |
|---|---:|---|---:|---:|---:|---:|
| **A · Ciclo de IA largo que desacelera con la escala** | 40% | Data Center: 50%, 20%, 10%, 8%, 6%; Gaming, visualización y automotriz: 10%, 8%, 7%, 6%, 6% | 17,1% | 58% | 3,0 | US$207,92 |
| **B · Ciclo de semiconductores: el capex se corrige** | 30% | Data Center: 35%, -10%, 0%, 8%, 8%; Gaming, visualización y automotriz: 5%, 5%, 5%, 5%, 5% | 7,0% | 50% | 3,0 | US$105,33 |
| **C · La IA es infraestructura permanente** | 20% | Data Center: 60%, 30%, 20%, 15%, 12%; Gaming, visualización y automotriz: 12%, 12%, 10%, 10%, 8% | 25,3% | 60% | 3,0 | US$331,78 |
| **D · Chips propios de los clientes y corrección fuerte** | 10% | Data Center: 25%, -25%, -10%, 5%, 5%; Gaming, visualización y automotriz: 0%, 0%, 0%, 0%, 0% | -1,3% | 40% | 3,0 | US$55,56 |
| **Valor esperado** | 100% |  |  |  |  | **US$186,68** |

A (40%) es un ciclo de IA largo que desacelera con la escala. B (30%) es la historia clásica de semiconductores: sobreinversión y corrección en 2028. C (20%) trata la IA como infraestructura permanente (inferencia masiva, IA soberana, robótica). D (10%) combina corrección fuerte y pérdida de participación frente a chips propios. **Son probabilidades del analista, no datos: asigna las tuyas antes de leer el precio.**

Sensibilidad del DCF Base (beta 1,51; US$ por acción; filas = crecimiento de los años 1-5, columnas = margen operativo objetivo):

| Crecimiento \ Margen | 54,0% | 56,0% | 58,0% | 60,0% | 62,0% |
|---|---:|---:|---:|---:|---:|
| 17,2% | 195,76 | 202,65 | 209,55 | 216,44 | 223,33 |
| 19,2% | 217,74 | 225,47 | 233,19 | 240,92 | 248,64 |
| 21,2% | 242,00 | 250,65 | 259,29 | 267,94 | 276,58 |
| 23,2% | 268,75 | 278,41 | 288,07 | 297,74 | 307,40 |
| 25,2% | 298,21 | 308,99 | 319,77 | 330,55 | 341,33 |


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

Precio de referencia de la valoración guardada: **US$228,86**.

DCF inverso: crecimiento anual de ingresos en los años 1-5 que justifica ese precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 50% | Margen 58% | Margen 62% |
|---|---:|---:|---:|
| Beta 1,51 | 21,6% (1% de las empresas) | 19,0% (3% de las empresas) | 17,8% (3% de las empresas) |
| Beta 1,51 | 21,6% (1% de las empresas) | 19,0% (3% de las empresas) | 17,8% (3% de las empresas) |

Frente al valor esperado de las historias (US$186,68), el precio está por encima en 23%. Con el ROIC terminal revisado (30-sep-2026), el precio (US$228,86) queda 23% por encima del valor esperado de las historias (US$186,68) pero por debajo del DCF Base (US$259,30). El DCF inverso pide 18-22% anual en los años 1-5, algo que logró ~1-3% de las empresas de este tamaño. ¿Qué sabe el mercado que yo no? Paga por algo entre las historias A y C. Aquí el mayor error posible es doble: subestimar el ciclo (como quien vendió en 2023) o sobreestimar su duración (como en 2000 con Cisco). Las historias ponen ese dilema en números.


### Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 |  |
| Historia en una frase | Proveedor dominante de la infraestructura de IA en la cima de un ciclo de inversión |  |
| Probabilidades | A 40% / B 30% / C 20% / D 10% |  |
| Valor esperado | US$186,68 |  |
| Rango (historia más débil a más fuerte) | US$55,56 a US$332,13 |  |
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
