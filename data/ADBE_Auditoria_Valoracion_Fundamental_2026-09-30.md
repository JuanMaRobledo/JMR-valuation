---
schema: "jmr-audit-v1"
ticker: "ADBE"
company: "Adobe Inc."
analysis_date: "2026-09-30"
information_cutoff: "2026-09-30"
currency: "USD"
language: "es"
---

# Auditoría de la valoración y del análisis fundamental de Adobe

El cálculo guardado del DCF coincide con la hoja y con el motor JMR. La revisión encuentra errores contables y documentales, una base estimada de ingresos por grupos y deficiencias de soporte económico. Los errores verificables se corrigieron; el análisis fundamental no recibe una aprobación integral del prompt v5.

Se revisaron la hoja nativa vinculada, los JSON de valoración y research, las referencias de historias/múltiplos y los prompts de valoración v4 y research v5. Se conservaron la estructura del motor y los supuestos discrecionales que no pueden sustituirse por una cifra reportada. El corte del informe anterior era 27-sep-2026; esta auditoría usa información pública hasta 30-sep-2026.

## Resultados vigentes, con horizonte explícito

| Concepto | Conservador | Base | Optimista |
|---|---:|---:|---:|
| DCF por acción hoy | 408,85 | 536,48 | 823,06 |
| Múltiplos consolidados hoy | 318,83 | 486,87 | 812,69 |
| Mezcla ponderada hoy, secundaria | 354,84 | 506,71 | 816,83 |
| Objetivo ponderado FY+3, otro horizonte | 475,99 | 698,88 | 1.197,71 |

| Historias, con la beta de la hoja | Probabilidad del analista | Valor anterior | Valor corregido |
|---|---:|---:|---:|
| A · IA dentro de la suscripción | 40% | 467,38 | 465,71 |
| B · Erosión gradual | 35% | 268,58 | 267,97 |
| C · Comoditización | 15% | 187,86 | 187,85 |
| D · Ampliación del mercado | 10% | 586,71 | 583,92 |
| Valor esperado de historias | 100% | 367,80 | 366,64 |
| Umbral tras MOS del 35% | — | 239,07 | 238,32 |

El valor esperado es la suma de DCF completos ponderados por probabilidades; no es el escenario Base ni la mezcla DCF/múltiplos. La corrección del valor esperado procede de reconciliar la mezcla de ingresos, manteniendo las probabilidades y las tasas de crecimiento por historia. Los escenarios B/C pierden el exceso de retorno terminal; A/D lo conservan.

Precio observado en el caché de GOOGLEFINANCE durante la lectura: US$239,94. No se verificó hora de negociación ni tipo de sesión; se identifica como referencia de la hoja, no como cotización en tiempo real. El WACC todavía utiliza el precio del análisis, US$265,60, en su estructura de capital. Esa convención se documenta y no se cambia silenciosamente.

## Hallazgos y correcciones

| Hallazgo | Estado y actuación | Prioridad |
|---|---|---|
| Flujo de inversión LTM de −1.665M y financiación de −8.830M | Incongruencia confirmada: corregidos a −2.054M y −9.369M. | Alta |
| Cambio de caja LTM −14M | Incongruencia confirmada: −623M, con efecto cambiario −6M. | Alta |
| Ceros y vacíos en movimientos de capital de trabajo/inversiones | Reconstruidas las partidas identificadas para FY23–FY25 y LTM; conciliadas las sumas. No se interpreta cero importado como inexistencia. | Alta |
| Flujo de endeudamiento tomado de variación de saldos | Sustituido en FY23–FY25/LTM por emisión menos repago reportados. Diferencias de saldo no son flujos de caja. | Alta |
| EPS básico copiado del diluido | FY23/FY24/FY25: corregido a 11,87 / 12,43 / 16,73. | Media |
| Variación del WACC descrita como 4 pb | 10,7998%→10,8037% es +0,0039 puntos porcentuales = +0,39 pb. Texto corregido. | Baja |
| Deuda neta de aproximadamente 488M | Texto actualizado a 1.123M incluyendo arrendamientos; convención consistente con los ajustes del modelo. | Alta |
| Dos grupos comerciales presentados como segmentos y Digital Experience sumado aparte | Un único segmento reportable; Experience forma parte del grupo profesional. Retirado el doble conteo conceptual. | Alta |
| Grupos de historias estimados en 18.050M/7.300M/620M | Base reconciliada: 17.819M/7.263M/888M; suma 25.970M. | Media |
| Tasas base clasificadas por ingresos nominales | Dólares de 2015: 25.970 × 237,017 / 334,980; cohorte 12.000–25.000M. Corregida la cohorte y sus fracciones. | Media |
| Origen de los Supuestos afirma que múltiplos vienen del DCF o del mínimo histórico | Corregida la descripción para reflejar el protocolo de tres anclas activo. | Alta |
| Margen LTM de 36,1% y objetivo 40% tratado como comparable GAAP | GAAP LTM 35,70%; inicio ajustado por I+D 38,74%. El 40% es supuesto ajustado del modelo, no guía GAAP/no-GAAP. | Alta |
| Adopción Figma 59%/Adobe 42,4% usada como pérdida de cuota | Muestra y serie no verificadas; retirado su uso como prueba de cuota total o erosión visible. | Alta |
| Filosofías de inversión favorables basadas en objetivos de distinto horizonte | Reescritas como evaluaciones económicas; retirada la conclusión de descuento frente a “valor intrínseco” basada en la mezcla ponderada. | Media |
| Control de calidad marcado íntegramente “Sí” | Sustituido por alcance y salvedades reales; presencia de 18 secciones no equivale a cumplimiento completo. | Alta |

Las correcciones contables se respaldan en el 10-K FY25 y el 10-Q Q3 FY26. La identidad LTM utilizada es FY25 + nueve meses FY26 − nueve meses FY25; se aplica a flujos, nunca a balances. Se verificaron las sumas de operación, inversión y financiación de los cuatro períodos. Los respaldos incluyen los valores y fórmulas anteriores.

## Soporte económico de la valoración

| Supuesto activo | Qué demuestra el archivo | Juicio de auditoría |
|---|---|---|
| Crecimiento 12% año 1; 10% años 2–5 | Input B27/B29 activos; escenarios ordenados 6%/12%/16% y 6%/10%/16%. | Compatible con crecimiento reciente; no es una guía de Adobe para cinco años. Requiere retención, precio/volumen y puente orgánico/adquirido. |
| Margen inicial 38,5%; objetivo 40% en año 3 | Base ajustada por capitalización de I+D, no margen GAAP. | Falta puente homogéneo contra peers maduros, costo incremental de IA y SBC. La guía no-GAAP no basta. |
| Ventas/capital 4x y 4,5x | Inputs manuales activos B32/B33. | Capex bajo no justifica esos ratios. Falta conciliar I+D, capital de trabajo, goodwill y compras. |
| WACC 10,8004%; Ke 11,2023% | Beta activa bottom-up global 1,33 desapalancada y 1,3929 apalancada; rating activo A2/A+. | No es beta de regresión. La propuesta US 1,3082 es contraste alternativo. Falta verificar actualización de tablas y rating al corte. |
| ROIC terminal 29,3%; crecimiento terminal 4,99%; WACC terminal 9,22% | Override ROIC activo; criterio de moat aplicado. | Decisión muy material: DCF Base sin exceso de ROIC terminal ≈377,94 frente a 536,48 vigente. Falta serie homogénea de cinco años que pruebe retornos excedentes y comparabilidad sectorial. |
| Opciones “No”, valor de opciones cero y recompras futuras cero | Selectores y parámetros activos. | “No opciones” no equivale a “sin compensación/dilución”. Debe reconciliarse RSU, premios y acciones proyectadas sin doble conteo. |
| Impuesto efectivo 21,52%→marginal 25% | Activo; el marginal es manual. | Exige justificación jurisdiccional y puente GAAP. La guía no-GAAP 18% no sustituye la tasa económica. |
| Múltiplos de salida y pesos 40%/60% | Historial, peers y ancla justificada; quince valores consolidados coinciden con el cálculo. | Coincidencia aritmética no valida las cotizaciones/definiciones de los peers ni la elección discrecional de λ y ajustes. No se fuerza coincidencia con DCF. |
| Probabilidades 40%/35%/15%/10%; MOS 35% | Suman 100%; el MOS se aplica al valor esperado. | Son juicio del analista; deben revisarse con métricas operativas, no moviendo cifras para obtener un precio deseado. |

## Evaluación del análisis fundamental

La evidencia respalda recurrencia, generación de caja y costos de cambio en flujos profesionales. La sostenibilidad futura depende de retener clientes de pago, monetizar IA sin deteriorar margen y lograr retornos sobre el capital económico completo. No se deduce moat de un margen elevado ni comoditización de una encuesta sin universo verificable.

El informe infravaloraba inversión intangible y capital comprado. Se incorporó Semrush, completada el 28-abr-2026 por 1.874M, como parte del perímetro y de la revisión de capital. El retorno sobre el precio pagado no queda demostrado por el crecimiento consolidado. La geografía y el desglose comercial sí estaban disponibles en fuentes primarias; ya no se presentan como datos inexistentes.

Continúan estas salvedades documentadas:

- El informe original carecía de las viñetas exigidas en el resumen y de tablas de modelo de negocio; la auditoría registra el incumplimiento editorial y no certifica una reescritura integral.
- El análisis histórico era superficial y omitía ratios aplicables. Existe una década importada; se conciliaron partidas del último año/LTM y flujos FY23–FY25, no cada cifra de la década. Promedios de ratios deben declarar definición y número de observaciones.
- Las acciones promedio LTM guardadas son básicas 400,2M y diluidas 400,0M: requieren reconstrucción con períodos homogéneos. Las 389,2M acciones al cierre usadas en DCF tienen otra fecha/definición. No se arregla EPS LTM con una suma simple de EPS acumulados.
- “Total Revenues %Chg” LTM 9,26% divide LTM por FY25. Es variación frente al período mostrado anterior, no crecimiento LTM interanual. No se utiliza como prueba de desaceleración.
- Faltan fuentes reproducibles para todos los múltiplos de peers, referencias de ROIC, consenso y ajustes discrecionales. Algunas fuentes secundarias no pudieron reabrirse; su contenido no se declara validado.
- Las preguntas abiertas deben excluir asuntos ya contestados por reportes, y el seguimiento debe distinguir umbrales del analista de guía empresarial. Se ampliaron los indicadores a ocho; se mantuvo la alerta de cobertura del informe.

## Fuentes y trazabilidad

1. [Adobe, 10-Q cerrado el 28-ago-2026](https://www.sec.gov/Archives/edgar/data/796343/000079634326000156/adbe-20260828.htm): flujos acumulados, balance, geografía, reporting y adquisiciones.
2. [Adobe, 10-K FY2025](https://www.adobe.com/cc-shared/assets/investor-relations/pdfs/adbe-10k-fy25-final.pdf): flujos FY2023–FY2025 y EPS básico/diluido, nota 15.
3. [Adobe, datasheet Q3 FY2026, 10-sep-2026](https://www.adobe.com/cc-shared/assets/investor-relations/pdfs/01906202/b75st5a4rwea.pdf): series comparables de grupos, geografía y resultados GAAP.
4. [Adobe, comunicado Q3 FY2026, 10-sep-2026](https://www.sec.gov/Archives/edgar/data/796343/000079634326000147/adbeex991q326.htm): resultados, guía y conciliaciones.
5. [Adobe, transición de CEO](https://news.adobe.com/news/2026/09/adobe-announces-anil-chakravarthy-to-become-president-and-ceo): el cambio anunciado tiene vigencia 1-dic-2026.
6. [DOJ, acuerdo de suscripciones, 13-mar-2026](https://www.justice.gov/opa/pr/adobe-agrees-150-million-settlement-and-injunction-resolve-alleged-violations-restore-online): distinción entre penalidad y servicios.
7. [Base Rate Book, septiembre 2016](https://sorfis.com/wp-content/uploads/2021/09/The-Base-Rate-Book-Integrating-the-Past-to-Better-Anticipate-the-Future-September-2016.pdf): distribución histórica real por tamaño; no probabilidades específicas del emisor.
8. [BLS, CPI-U agosto 2026, 11-sep-2026](https://www.bls.gov/news.release/cpi.t01.htm) y [promedio 2015](https://www.bls.gov/news.release/archives/cesan_08292017.pdf): deflactor de tamaño.
9. [Adobe proxy 2026](https://www.sec.gov/Archives/edgar/data/796343/000079634326000043/adbe-20260227.htm): identidad de documento verificada; no se certifica revisión exhaustiva de incentivos.
10. [Hoja nativa ADBE](https://docs.google.com/spreadsheets/d/19WcSOKymo4gR6lnKiLB1gAitYFFwfI3xl08E4BDzLDw/edit): valores, fórmulas y selectores leídos en rangos acotados el 30-sep-2026.

Los estados “conciliado” y “requiere aclaración” se refieren al alcance concreto indicado. Esta auditoría no emite decisión de comprar, mantener ni vender.

## Dictamen de revisión y publicación

La auditoría mantiene el DCF como valor intrínseco principal. El DCF Base de US$536,48 es condicionado: el contraste de US$377,94, con ROIC terminal igual al costo de capital, baja 29,55%. No se cambia el ROIC por una probabilidad de erosión futura ya incorporada en las historias. El principal pendiente es demostrar su duración con capital económico homogéneo, no forzar coincidencia con múltiplos. El valor esperado corregido es US$366,64 y su umbral con MOS 35% US$238,32.

Se corrige además la etiqueta de beta: la hoja utiliza bottom-up global, no regresión. El riesgo sistemático está en el WACC; los riesgos específicos se recogen en los flujos e historias. Las cifras no verificadas de adopción no sustentan pérdida de cuota. La auditoría revisó resultados, tablas y soporte material; no certifica cumplimiento editorial completo del informe v5 ni toda la década importada.
