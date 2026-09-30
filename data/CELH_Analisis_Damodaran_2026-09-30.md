---
schema: "jmr-analisis-narrativa-v1"
title: "Celsius Holdings (CELH) — Valor con criterio Damodaran: historia, tasas base y escenarios"
ticker: "CELH"
analysis_date: "2026-09-30"
base: "Análisis fundamental del 28-sep-2026 (Modelo-JMR-datos/analisis/CELH-research-…json) y Modelo JMR - CELH"
---

# Celsius Holdings (CELH) — Valor con criterio Damodaran

> **Cómo leer este documento.** Sigue el orden que usan Damodaran y Mauboussin para no contaminarse con el precio:
> primero la historia, después la visión externa (tasas base), luego cada pieza del valor (crecimiento, margen,
> reinversión y riesgo), cuatro historias con probabilidades y, **recién en la sección 10, el precio**. Si quieres
> formarte tu propia opinión sin ancla, detente al final de la sección 9 y anota tu valor antes de seguir.
>
> No cambia nada del modelo: la hoja, el visor y la bitácora siguen igual. Los valores de las secciones 6 y 7 se
> calcularon aparte con el motor del Modelo JMR (`docs/jmr_engine.js`), calibrado para que el escenario Base de la
> hoja dé exactamente sus US$18,11 por acción. "Cálculo propio" marca cifras derivadas de datos públicos.
> Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación.

---

## 1. La historia en un párrafo

Celsius dejó de ser una marca de hipercrecimiento orgánico (2020-2023) y pasó a ser un **portafolio de bebidas
energéticas distribuido por PepsiCo**. Su marca original, Celsius, ya no crece: el mercado de energéticas "fitness"
se llenó de competidores y la marca pasa por un ajuste de inventario y de surtido. El crecimiento viene de
**Alani Nu**, una marca comprada en abril de 2025 que le habla a un consumidor más joven y femenino, y que está
entrando a la red de PepsiCo. Rockstar, comprada en agosto de 2025, es una marca madura en declive que aporta
escala y sobre todo la alineación con PepsiCo como "category captain". El valor depende de tres preguntas:
**(1) ¿cuánto y por cuánto tiempo crece Alani Nu?, (2) ¿la marca Celsius se estabiliza o sigue cediendo? y
(3) ¿qué margen es sostenible con más promociones y una mezcla de marcas menos rentable?**

**Filtro de Damodaran (posible · plausible · probable):**

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Alani Nu sigue creciendo a doble dígito 2-3 años más | Sí | Sí: ventas al consumidor +100% (1T26) y +55,7% (2T26) | Sí, desacelerando |
| La marca Celsius vuelve a crecer | Sí | Sí: al consumidor solo cae 2% (2T26); la caída reportada es mayormente inventario | Incierto (50/50) |
| El grupo crece más de 15% al año por cinco años | Sí | Poco: exige Alani muy fuerte, Celsius creciendo y quizá más compras | Baja (ver sección 2) |
| El margen operativo llega al de Monster (~29%) | Sí | Poco: el margen bruto es 7-8 pp menor y la escala, tres veces menor | Baja |

---

## 2. Visión externa: qué dicen las tasas base

Antes de mirar a Celsius, Mauboussin propone preguntar **qué les pasa a las empresas de su tamaño**. En su estudio de
tasas base, las empresas estadounidenses que empiezan con **US$2.000-5.000 millones de ventas** (Celsius tiene
US$3.047M LTM) crecieron en promedio **6,9% nominal al año durante cinco años, con una desviación estándar de
11,1%** (1950-2025, ~19.300 observaciones) ([Mauboussin, *Bayes and Base Rates 2.0*](https://www.morganstanley.com/im/publication/insights/articles/article_bayesandbaserates2_ltr.pdf)).

Con una aproximación normal (la distribución real tiene colas más gruesas; úsalo como orden de magnitud):

| Crecimiento anual de ingresos a 5 años | Fracción aproximada de empresas que lo logran |
|---|---:|
| ≥ 4,1% | ~60% |
| ≥ 8,6% | ~44% |
| ≥ 10,2% | ~38% |
| ≥ 12,2% | ~32% |
| ≥ 15,2% | ~23% |
| ≤ −1,9% (se achica) | ~21% |

**Lectura.** La tasa base es el punto de partida (~7%); te alejas de ella solo con evidencia específica. Para
Celsius hay evidencia a favor de estar algo por encima (categoría creciendo, Alani al alza, distribución de PepsiCo)
y evidencia en contra (marca original estancada, ciclos de moda en energéticas). El pasado de 68% de CAGR **no**
es evidencia útil: mezcla hipercrecimiento orgánico de una marca pequeña con compras, y el crecimiento alto
persiste poco en todas las tasas base.

---

## 3. Descomposición del crecimiento

### 3.1 Orgánico frente a comprado

| US$ millones | 2024 | 2025 | LTM jun-26 (cálculo propio) | Comentario |
|---|---:|---:|---:|---|
| Celsius (marca) | 1.355,6 | ~1.457,8 (+7,5%) | ~1.425,5 | 2025 = total − Alani − Rockstar |
| Alani Nu | (595 antes de la compra) | 1.001,9 (abr-dic) | ~1.433,1 | 2025 incluye la carga inicial de inventario de PepsiCo |
| Rockstar | — | 55,6 (sep-dic) | ~188,7 | Ventas al consumidor −13% |
| **Total** | **1.355,6** | **2.515,3 (+85,5%)** | **3.047,3** | El +85,5% es casi todo comprado |

Fuente: 10-K 2025 y resultados 1T/2T 2026. El LTM por marca es cálculo propio: Alani = (1.001,9 − 2T25 ≈ 301,2) +
732,4 del 1S26; Rockstar = 55,6 + 133,1; Celsius = total − ambas.

**Conclusión:** el crecimiento orgánico de la marca Celsius fue +3% (2024), ~+7,5% (2025) y ~−4% en el 1S26. El
motor es Alani Nu, que hoy pesa casi la mitad de las ventas.

### 3.2 Lo que se vende al consumidor frente a lo que se factura

Esta es la evidencia más importante para la historia, porque separa demanda real de movimientos de inventario:

| 2T 2026 (13 semanas a 28-jun, Circana) | Ingresos reportados | Ventas al consumidor | Lectura |
|---|---:|---:|---|
| Celsius | −11,7% | **−2%** | La caída facturada es sobre todo inventario y surtido (SKU) de los distribuidores |
| Alani Nu | +21,0% | **+55,7%** | La demanda crece mucho más de lo que muestra la factura (la base 2T25 incluía la carga inicial) |
| Rockstar | sin comparable | −13% | Marca en declive |
| Portafolio | +10,6% | +31,0% | |

En el 1T26: Alani al consumidor **+100%**; Celsius facturó +6%. Fuentes: [resultados 2T26](https://www.sec.gov/Archives/edgar/data/0001341766/000134176626000047/ex9912q2026.htm) y [resultados 1T26](https://www.sec.gov/Archives/edgar/data/0001341766/000134176626000035/ex9911q2026.htm).

**Implicación:** esto responde en parte la pregunta abierta del análisis fundamental ("¿cuánto de la caída de Celsius
es inventario?"): con −2% al consumidor, la marca no se está desplomando, se está estancando. Y Alani está
creciendo de verdad, no solo por llenar la red de PepsiCo.

### 3.3 Participación y categoría

| Participación en dólares, energéticas EE.UU. (Circana) | 1T 2026 | 2T 2026 |
|---|---:|---:|
| Portafolio Celsius | 20,9% | 20,1% |
| Celsius | 9,9% | 9,5% |
| Alani Nu | 9,0% | 8,7% |
| Rockstar | 2,0% | 1,9% |
| Parte del crecimiento de la categoría sin azúcar que aporta el portafolio | 45% de US$800M | 30% de US$640M |

La categoría de energéticas en EE.UU. vende ~US$28.100M al consumidor y creció ~15% en las 52 semanas a abril
([BevIndustry, 2026 State of the Beverage Industry](https://www.bevindustry.com/articles/98511-2026-state-of-the-beverage-industry-energy-drinks-shots-market-embraces-innovation-functionality)).

**Señales mixtas:** la participación bajó de un trimestre a otro en las tres marcas (puede ser estacional) y el
portafolio capturó menos del crecimiento del segmento sin azúcar (45% → 30%). Es el primer dato a vigilar: si Alani
crece +55% al consumidor pero su participación baja, la categoría crece aún más rápido y otros ganan más.

### 3.4 Alani Nu: evidencia a favor y en contra

| A favor | En contra |
|---|---|
| Ventas al consumidor +100% (1T26) y +55,7% (2T26) | La tasa se desacelera rápido (100% → 56% en un trimestre) |
| Entra a la red de PepsiCo: más puntos de venta por delante | Parte del crecimiento es distribución nueva, que se agota cuando la red está completa |
| Innovación de sabores con éxito (lanzamientos por tiempo limitado) | Depende de moda y redes sociales; las energéticas tienen ciclos (Bang, Rockstar) |
| Consumidor distinto al de Celsius: amplía el portafolio | Participación 9,0% → 8,7% entre 1T y 2T |

---

## 4. Márgenes: GAAP frente a normalizado

El margen operativo GAAP de 5,3% LTM **no es representativo**: incluye US$85,3M de terminación de distribuidores en
el 1S26, US$24,6M de un acuerdo legal en el 1T26, integración y amortización de intangibles.

| Medida | Valor | Fuente |
|---|---:|---|
| Margen operativo 2T26 sin la terminación de distribuidores | (75,3 + 80,9) / 817,9 = **19,1%** | Cálculo propio con resultados 2T26 |
| Margen operativo 2T25 | 143,0 / 739,3 = **19,3%** | Resultados 2T26 (comparativo) |
| EBITDA ajustado 1S26 / ingresos | 379,6 / 1.600,5 = **23,7%** | Resultados 2T26 |
| Margen bruto | 48,1% (2T26) vs 51,5% (2T25) | Promociones y mezcla con marcas compradas |
| Monster 2025 (referencia madura, 3× la escala) | Bruto **55,8%**, operativo **29,2%**, ventas US$8.290M (+10,7%) | [Monster, resultados 2025](https://www.sec.gov/Archives/edgar/data/865752/000110465926020831/mnst-20251231x10k.htm) |

**Lectura:** el margen normalizado de hoy ya está en ~19%. El 17% objetivo del Base de la hoja está **por debajo**
del normalizado actual, y el 12% del año 1 es conservador. El techo lógico no es Monster: la brecha de margen bruto
(~8 pp) y de escala hace poco probable superar ~22-24% sin cambiar de modelo. Rango razonable: **12% (moda que se
desgasta) a 22% (plataforma con escala)**, con 16-19% en las historias centrales.

---

## 5. Reinversión y retorno: el crecimiento no es gratis

**Orgánico:** muy liviano en capital. El capex LTM es US$46M y el flujo libre, ~US$463M. El sales-to-capital de 2,5
de la hoja es razonable (hasta conservador) para crecimiento orgánico.

**Comprado:** es otra historia.

| Compra | Precio | Ventas | Retorno sobre lo pagado (cálculo propio) |
|---|---:|---:|---|
| Alani Nu (abr-25) | US$1.650M netos (US$1.800M con US$150M de activos tributarios) | 595 (2024); ~1.433 LTM | Con margen 16-19% y 24% de impuestos: NOPAT 174-207 → **10,5-12,5%** sobre lo pagado, similar al costo de capital |
| Rockstar (ago-25) | US$585M (y PepsiCo suscribió US$585M en preferentes) | ~189 LTM (~266 anualizado 2T26) | Con margen ~10%: **~3,5%**; solo se justifica por el valor de la alianza con PepsiCo |

Fuentes: [compra de Alani Nu](https://www.businesswire.com/news/home/20250401253612/en/Celsius-Holdings-Completes-Acquisition-of-Alani-Nu); [transacciones con PepsiCo y Rockstar](https://www.fooddive.com/news/pepsico-ups-stake-in-energy-drink-company-celsius-with-585m-deal/758933/).

**Lectura:** Alani se compró a <3× ventas de 2024 y creció mucho, así que hoy rinde más o menos su costo de capital
(ni crea ni destruye mucho valor). Rockstar rinde bastante menos. Damodaran diría: las compras movieron el
crecimiento, no el valor por acción; el valor se crea si Alani sigue creciendo con poca inversión adicional.

**Hallazgo en la hoja:** el capital invertido base (US$1.241M = patrimonio contable + deuda − caja) **no incluye las
preferentes de PepsiCo (~US$1.135M)**, que financiaron parte de las compras. Por eso el ROIC del DCF (24-34%) se ve
más alto de lo que es. El valor por acción no cambia (las preferentes se cuentan como convertidas: 286,5M de
acciones), pero el ROIC se debería leer con capital completo.

---

## 6. Riesgo: ¿qué beta usar?

| Enfoque | Beta | Costo del patrimonio | WACC inicial | DCF Base por acción |
|---|---:|---:|---:|---:|
| Hoja: beta de regresión | 1,50 | 11,7% | 11,1% | **US$18,11** |
| Intermedio: sector ajustado por riesgo de marca | 1,00 | 9,5% | 9,1% | US$20,36 |
| Bottom-up puro: bebidas no alcohólicas (Damodaran, ene-2026) | 0,62 | 7,8% | 7,5% | US$22,28 |

Damodaran calcula la beta **bottom-up**: parte de la beta desapalancada del sector, que para bebidas no alcohólicas
es 0,58 corregida por caja (27 empresas, [Damodaran, Betas by Sector, ene-2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)),
y la reapalanca con la deuda de la empresa (~0,62 para Celsius). Una beta de regresión de 1,5 refleja sobre todo la
volatilidad de la acción en su auge y caída, no el riesgo del negocio. Pero Celsius es más riesgosa que el promedio
del sector: una sola categoría, moda y un distribuidor que concentra casi toda la venta. Una beta de **~1,0** es
defendible como punto medio. El valor cambia menos de lo que parece (US$18 → 20-22) porque el costo de capital
terminal de la hoja ya está fijo en 9%.

---

## 7. Cuatro historias, cuantificadas

Cada historia proyecta las tres marcas por separado (años 1-5), desde las ventas LTM por marca de la sección 3.1.
Después de cinco años, todas convergen a la perpetuidad como el DCF de la hoja.

| Historia | Probabilidad | Celsius (años 1-5) | Alani Nu (años 1-5) | Rockstar | Crecimiento anual del grupo | Ventas año 5 | Margen objetivo | Sales-to-capital | Valor/acción (beta 1,5) | Valor/acción (beta 1,0) |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|
| **A · Alani lidera y Celsius se estabiliza** | 40% | 0%, 2%, 3%, 3%, 3% | 25%, 18%, 14%, 10%, 8% | −5%/año | 8,6% | US$4.598M | 19% | 2,5 | **US$22,87** | US$25,75 |
| **B · Alani crece, Celsius sigue cediendo** | 35% | −6%, −4%, −2%, 0%, 0% | 18%, 12%, 9%, 7%, 6% | −8%/año | 4,1% | US$3.727M | 16% | 2,5 | **US$15,41** | US$17,29 |
| **C · La moda se desgasta** | 15% | −10%, −8%, −5%, −3%, −2% | 8%, 3%, 0%, 0%, 0% | −10%/año | −1,9% | US$2.772M | 12% | 2,5 | **US$8,97** | US$9,97 |
| **D · Plataforma multimarca** | 10% | 3%, 5%, 5%, 4%, 4% | 35%, 25%, 18%, 12%, 10% | −3%/año | 12,2% | US$5.429M | 22% | 1,5 (con más compras) | **US$29,49** | US$33,40 |
| **Valor esperado** | 100% | | | | | | | | **US$18,84** | **US$21,19** |

**Por qué estas probabilidades.** A es la más probable (40%) porque los datos al consumidor del 2T26 la respaldan:
Celsius −2% y Alani +55,7%. B (35%) es la continuación de lo que muestra la factura. C (15%) recoge la tasa base de
~21% de empresas que se achican en cinco años y los ciclos conocidos de marcas de energía. D (10%) exige un
crecimiento que solo ~32% de las empresas de este tamaño logra, un margen cercano al techo lógico y más compras.
**Son mis probabilidades, no datos:** conviene que asignes las tuyas antes de la sección 10.

**Comparación con la tasa base:** A (8,6%) está algo por encima de la media (~44% de las empresas lo logran); B
(4,1%) algo por debajo; C cae en el quintil inferior; D, en el tercio superior. El portafolio de historias está
centrado cerca de la tasa base, con sesgo positivo por Alani.

**Sensibilidad del DCF Base (beta 1,5; sales-to-capital 2,5). US$ por acción:**

| Crecimiento años 1-5 \ Margen objetivo | 12% | 15% | 17% | 19% | 21% |
|---|---:|---:|---:|---:|---:|
| 4% | 11,37 | 14,35 | 16,33 | 18,31 | 20,30 |
| 6% | 12,36 | 15,71 | 17,94 | 20,18 | 22,41 |
| 8% | 13,45 | 17,21 | 19,73 | 22,24 | 24,75 |
| 10% | 14,65 | 18,88 | 21,70 | 24,52 | 27,34 |
| 12% | 15,97 | 20,71 | 23,88 | 27,04 | 30,20 |

**El margen pesa tanto como el crecimiento:** desde el Base (6% y 17%), subir el margen objetivo 2 pp (a 19%)
agrega ~US$2,2 por acción; subir el crecimiento anual 2 pp (a 8%) agrega ~US$1,8. Como el margen de hoy es más fácil
de verificar que la duración del crecimiento de Alani, la pregunta más valiosa no es solo "¿cuánto crece Alani?"
sino "¿con qué margen?".

---

## 8. Pre-mortem: si en 2029 la tesis falló, ¿por qué?

1. **Alani fue una moda.** Las ventas al consumidor pasaron de +100% a +56% en un trimestre; si siguen cayendo a un
   dígito en 2027 y la participación retrocede, el motor se apaga (historia C).
2. **Las promociones se volvieron permanentes.** El margen bruto no vuelve a 50%+ y el operativo se queda en 12-15%:
   aun creciendo, el valor cae a la zona de US$12-16.
3. **PepsiCo prioriza lo suyo.** El distribuidor y accionista cambia condiciones, prioriza marcas propias o
   convierte las preferentes en un momento desfavorable.
4. **Celsius no se estabiliza.** La marca original pasa de −2% a −10% al consumidor y arrastra al grupo.
5. **Más compras caras.** El crecimiento se sigue comprando a retornos cercanos o por debajo del costo de capital.

**Evidencia en contra de mi propia historia central (A):** la desaceleración rápida de Alani y la caída de
participación del 1T al 2T son exactamente lo que se vería al principio de B o C.

---

## 9. Qué vigilar y cómo mover las probabilidades

| Indicador (trimestral, próxima fecha ~nov-2026) | Hoy | Refuerza A/D si… | Refuerza B/C si… |
|---|---|---|---|
| Ventas al consumidor Celsius (Circana) | −2% | ≥ 0% | ≤ −8% |
| Ventas al consumidor Alani Nu | +55,7% | ≥ +25% | ≤ +10% |
| Participación del portafolio | 20,1% | ≥ 21% | ≤ 19% |
| Parte del crecimiento sin azúcar que captura | 30% | ≥ 40% | ≤ 20% |
| Margen bruto | 48,1% | ≥ 50% | ≤ 46% |
| Margen operativo sin cargos | ~19% | ≥ 20% | ≤ 16% |
| Cargos de terminación de distribuidores | US$85M en 1S26 | Terminan en 2026 | Se repiten en 2027 |
| Ventas Rockstar al consumidor | −13% | ≥ −5% | ≤ −15% |

**Regla bayesiana simple:** cada trimestre, mueve 5-10 pp de probabilidad entre historias según cuántos indicadores
apunten a un lado. No cambies el valor de cada historia salvo que cambie un supuesto (crecimiento, margen,
reinversión o riesgo).

> **Pausa sugerida.** Si quieres valorar sin ancla, anota aquí tu probabilidad para A, B, C y D, tu valor esperado
> y tu nivel de confianza **antes de leer la sección 10.**

---

## 10. Recién ahora: el precio

**Precio de referencia de la hoja: US$27,71 (US$28,00 en la valoración guardada).**

**DCF inverso: ¿qué crecimiento anual de ingresos en los años 1-5 justifica ese precio?**

| | Margen 17% | Margen 19% | Margen 22% |
|---|---:|---:|---:|
| Beta 1,5 (hoja) | 15,2% | 12,6% | 9,4% |
| Beta 1,0 | 12,6% | 10,2% | 7,0% |

**Lectura:**
- Con los supuestos de la hoja (beta 1,5 y margen 17%), el precio exige **15,2% al año por cinco años**. Solo ~23%
  de las empresas de este tamaño lo logra (sección 2), y está por encima incluso de la historia D.
- Con un riesgo más cercano al sector (beta 1,0) y el margen normalizado de hoy (19%), el precio exige **~10% al
  año**: entre la historia A (8,6%) y la D (12,2%). Es exigente pero no imposible (~38% de las empresas de este tamaño).
- Frente al valor esperado de las cuatro historias (US$18,84 con beta 1,5; US$21,19 con beta 1,0), el precio está
  **31-47% por encima**. El mercado le asigna más probabilidad que yo a A y D, o un margen más alto, o un riesgo menor.

**¿Qué sabe el mercado que yo no?** Posibles respuestas: (1) ve los datos al consumidor de Alani y confía en que el
crecimiento dure; (2) asume que el margen vuelve a ~22% al terminar los cargos y la integración; (3) usa un costo de
capital más bajo que el de la hoja. Si ninguna de las tres te convence con evidencia, el valor no se ajusta al
precio: el precio queda como una apuesta por las historias A y D.

---

## 11. Registro de decisión (para llenar antes de mirar el precio)

| Campo | Mi propuesta (esta nota) | Tu estimación |
|---|---|---|
| Fecha | 30-sep-2026 | |
| Historia en una frase | Portafolio liderado por Alani Nu; la marca Celsius se estanca | |
| Probabilidades A / B / C / D | 40% / 35% / 15% / 10% | |
| Valor esperado (beta 1,5 / 1,0) | US$18,84 / US$21,19 | |
| Rango (C a D) | US$9-33 | |
| Confianza (baja/media/alta) | Media-baja: el margen y la duración de Alani son muy inciertos | |
| Qué me haría cambiar | Indicadores de la sección 9 | |
| Revisión | Resultados 3T26 (nov-2026) | |

---

## 12. Qué cambiaría en el modelo si decides (no aplicado)

Nada de esto se ha cambiado; son decisiones pendientes para cuando termines de evaluar:

1. **Proyectar por marca** (Celsius, Alani, Rockstar) en lugar de un solo crecimiento agregado.
2. **Margen:** revisar el objetivo Base (17% hoy, por debajo del normalizado de ~19%) y el año 1 (12% hoy, muy por
   debajo del ~19% trimestral sin cargos).
3. **Beta:** pasar de la regresión (1,5) a una bottom-up ajustada (~1,0), documentando el porqué.
4. **Capital invertido:** incluir las preferentes de PepsiCo para leer bien el ROIC.
5. **Sales-to-capital:** mantener 2,5 si el crecimiento es orgánico; bajarlo si la historia incluye más compras.
6. **Múltiplos:** con lo anterior, el P/E Base de 29x (que supone ~9% de crecimiento perpetuo) sigue siendo alto
   frente a cualquiera de las cuatro historias; el chequeo de crecimiento implícito lo seguirá marcando.

---

## Fuentes

- Celsius Holdings, [resultados del 2T 2026](https://www.sec.gov/Archives/edgar/data/0001341766/000134176626000047/ex9912q2026.htm) (6-ago-2026) y [del 1T 2026](https://www.sec.gov/Archives/edgar/data/0001341766/000134176626000035/ex9911q2026.htm) (7-may-2026).
- Celsius Holdings, [Form 10-K 2025](https://www.sec.gov/Archives/edgar/data/1341766/000134176626000024/celh-20251231.htm) (2-mar-2026).
- [Celsius completa la compra de Alani Nu](https://www.businesswire.com/news/home/20250401253612/en/Celsius-Holdings-Completes-Acquisition-of-Alani-Nu) (1-abr-2025); [anuncio de la compra](https://www.businesswire.com/news/home/20250220357704/en/Celsius-Holdings-to-Acquire-Alani-Nu-Creating-a-Leading-Better-For-You-Functional-Lifestyle-Platform) (20-feb-2025).
- [PepsiCo sube su participación en Celsius con una operación de US$585M](https://www.fooddive.com/news/pepsico-ups-stake-in-energy-drink-company-celsius-with-585m-deal/758933/) (Food Dive).
- Monster Beverage, [Form 10-K 2025](https://www.sec.gov/Archives/edgar/data/865752/000110465926020831/mnst-20251231x10k.htm).
- Michael Mauboussin, [*Bayes and Base Rates 2.0*](https://www.morganstanley.com/im/publication/insights/articles/article_bayesandbaserates2_ltr.pdf) (Morgan Stanley Counterpoint Global).
- Aswath Damodaran, [Betas by Sector (US), enero 2026](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html).
- BevIndustry, [2026 State of the Beverage Industry: Energy drinks](https://www.bevindustry.com/articles/98511-2026-state-of-the-beverage-industry-energy-drinks-shots-market-embraces-innovation-functionality).
- Análisis fundamental de CELH del 28-sep-2026 y Modelo JMR - CELH (hoja del usuario).
