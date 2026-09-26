# Auditoría de supuestos y consistencia (26 de septiembre de 2026)

## Qué se corrigió

| Ruta | Inconsistencia | Tratamiento |
| --- | --- | --- |
| DCF y múltiplos | El crecimiento operativo `reinversión × ROIC` se mezclaba con el crecimiento de ingresos. | Solo se informa como diagnóstico del EBIT; los ingresos proceden de su historia y referencia sectorial. |
| Valor terminal | `g ≥ WACC` producía valores matemáticamente inválidos. | La corrida falla con mensaje explícito. |
| Primas por país | El CSV exportado del Excel contiene fórmulas sin evaluar. | La consulta se rechaza; no se inventa un valor. La tabla requiere exportación de cifras calculadas y fecha. |
| ERP en USD | El archivo local no coincidía con el corte de septiembre. | `mature_market_erp.txt` usa **4,093700355 % sobre el Treasury** de `ERPSept26.xlsx`, hoja `Impl premium calculator`, C45 (septiembre de 2026). La celda C44, 4,313700355 %, presupone tasa libre de riesgo ajustada por default. |
| Múltiplos EV | EV/EBITDA y EV/FCFF se dividían por acciones como si EV fuese patrimonio. | Se descuenta deuda, minoritarios y opciones; se suman caja y activos no operativos antes de dividir por acciones proyectadas. |
| Horizonte | El DCF proyectaba desde LTM y los múltiplos desde el último FY cerrado. | Ambas proyecciones usan ingresos LTM; los múltiplos muestran explícitamente su objetivo FY+3. |
| Pares Yahoo | `EV/freeCashflow` se llamaba EV/FCFF y `P/FCF` se usaba como P/FCFE. | El primero suma interés después de impuestos cuando hay datos; de lo contrario se omite. P/FCFE se omite del pipeline de pares si falta endeudamiento neto comparable. |
| Precio de mercado | Se mostraba sin día verificable. | La obtención automática exige `regularMarketTime` y escribe la fecha del precio. |
| Margen de seguridad | La mezcla de DCF presente y múltiplos FY+3 no se distinguía al interpretarla. | Por elección del usuario, el umbral principal se calcula desde el **ponderado Base**. Se muestran aparte el MOS y el precio de compra de cada método. Los pesos y el descuento son reglas del Modelo JMR, **no** parámetros de Damodaran. La mezcla conserva un límite de comparabilidad temporal. |

## De dónde salen los supuestos

* Estados financieros: SEC EDGAR, transformados por `sec_edgar_loader.py`. La cobertura y clasificación de los hechos XBRL requieren revisión para cada caso.
* Precio, beta y comparables: Yahoo Finance; precio con fecha de negociación. La beta no es la beta bottom-up por industria de Damodaran y su ventana debe validarse antes de tomar una decisión.
* Prima de mercado: hoja oficial [ERPSept26.xlsx](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPSept26.xlsx), C45, con Treasury sin ajuste; valores y corte en `reference/SOURCES.md`.
* Referencias de crecimiento, margen y ventas/capital por industria: CSV heredados del Excel original; **no tienen fecha demostrable**. El set de pares, la mezcla historia/industria, los rangos de escenarios, pesos por método y 35 % de margen son decisiones del Modelo JMR, no cifras prescritas por Damodaran.
* Crecimiento terminal y reinversión: regla de estado estable `g = tasa libre de riesgo` y `reinversión = g/ROIC`, descrita en [Damodaran, terminal value](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/termvalue.pdf). Se debe verificar que moneda, tasa y rentabilidad de estado estable sean coherentes.

## Prueba de dirección, no valoración actual de Adobe

El archivo `data/example_adbe.csv` es una muestra estática con precio **USD 276,27**, sin corte verificable del mercado. Con los cambios anteriores, su DCF Base pasa de **USD 366,36 a USD 370,50**. El promedio mixto pasa de **USD 410,69 a USD 446,88**: usar ingresos LTM aumenta la proyección de esta muestra, aun después de corregir el puente de EV. Con el criterio solicitado de ponderado Base, el precio de compra con margen del 35 % sería **USD 290,47** (446,88 × 0,65), frente a **USD 240,82** si se usara solo el DCF Base. El valor anterior del modelo era **USD 266,95** sobre el promedio mixto antiguo. Esta comparación muestra cómo los múltiplos FY+3 pueden elevar el umbral frente al DCF presente; no demuestra un sesgo universal del modelo.

En la misma muestra, DCF Base = USD 370,50. Una variación de **±1 punto porcentual del WACC inicial** da aproximadamente **USD 391,56 / USD 350,83**; una variación de **±2 puntos del crecimiento de ingresos del primer año** da **USD 363,96 / USD 377,04**. El valor terminal representa alrededor del **57 %** del valor de activos operativos. Son pruebas de sensibilidad sobre entradas de ejemplo, no precios objetivo actuales.

## Hojas de LULU y UNH revisadas

La fecha del análisis se toma de `Input sheet!B4`; `Input sheet!B23` consulta el último cierre disponible hasta esa fecha y `Input sheet!D1` mantiene la cotización actual. En `Resumen de Valoración!F5:H12` aparecen el MOS frente al cierre del análisis, el MOS frente a la cotización actual y el precio de compra por método. La fila 12, y el umbral de `B19`, usan el ponderado Base. LULU: cierre de análisis USD 95,98 (16-sep-2026) y precio actual observado USD 101,30; UNH: USD 371,29 (23-sep-2026) y USD 376,59. Son lecturas observadas al revisar las hojas, no promesas de cotización futura.

Las pestañas `Tesis de Inversión y Supuestos`, `Supuestos Recomendados`, `Origen de los Supuestos` y `Supuestos de los Múltiplos` distinguen datos observados, hipótesis del analista y fórmulas del libro. Se corrigieron sus encabezados de fecha/precio y los WACC impresos; ahora remiten a `Input sheet!B4`, `B23` y `B36`. Las explicaciones de múltiplos se generan desde las celdas del histórico y del sector, e indican cuando falta un comparable, para que no sobrevivan cifras copiadas de otra versión. Las referencias de sector aún carecen de pares y fecha comprobados.

| Empresa | Crecimiento Base | Margen EBIT Base | Múltiplos Base | Justificación y límites |
| --- | --- | --- | --- | --- |
| LULU | Año 1 −6 %; años 2–5 +4 % | Año 1 14 %; objetivo 18,5 % en año 6 | EV/FCFF 18×, P/OCF 12×, P/E 15×, P/FCFE 15×, EV/EBITDA 8× | El −6 % está dentro de la [guía FY2026 de lululemon](https://corporate.lululemon.com/newsroom/press-releases/2026/09-03-2026-210528733) de US$10.350–10.500 M; el 4 % posterior y ambos márgenes son hipótesis. La compañía indicó que el margen del trimestre recibió un beneficio no recurrente de devoluciones arancelarias. Los múltiplos son descuentos manuales frente a los históricos en la hoja, no objetivos publicados por Damodaran. |
| UNH | Año 1 +4 %; años 2–5 +6 % | Año 1 5,8 %; objetivo 6,5 % en año 6 | EV/FCFF 14×, P/OCF 13×, P/E 18×, P/FCFE 16×, EV/EBITDA 10× | Son hipótesis de recuperación desde el LTM Q2 2026: US$450.129 M × 1,04 ≈ US$468.134 M y × 5,8 % ≈ US$27.152 M de EBIT, con calendarios distintos a la [guía FY2026 de UnitedHealth](https://www.unitedhealthgroup.com/newsroom/2026/2026-07-16-uhg-reports-second-quarter-2026-results.html). EV/FCFF y EV/EBITDA tienen peso cero para la categoría financiera; los demás múltiplos son manuales y sus pares sectoriales incompletos. |

En las dos hojas, `Resumen de Valoración!D12` es el ponderado Base y `G4` fija el descuento de compra en 30 %; `F12` y `G12` comparan ese valor con el precio del análisis y el actual. Para LULU, USD 172,00 Base, MOS 44,2 % / 41,1 %, compra a USD 120,40; para UNH, USD 415,97 Base, MOS 10,7 % / 9,5 %, compra a USD 291,18. Los pesos de LULU (DCF 40 %, EV/EBITDA 25 %, EV/FCFF 15 %, P/E 5 %, P/FCFE 10 %, P/OCF 5 %) y UNH (DCF 40 %, EV 0 %, P/E 35 %, P/FCFE 20 %, P/OCF 5 %) son ajustes específicos de estas hojas. No coinciden necesariamente con los valores predeterminados por tipo de empresa en el repositorio Python.

## Límite pendiente antes de considerar el modelo validado

Falta fechar y cotejar los CSV de industrias y volver a exportar las primas por país. La exposición geográfica real, el tratamiento de I+D, arrendamientos, opciones, NOL, impuestos y acciones diluidas deben revisarse por compañía. Se corrigieron fecha/precio y se añadió la comparación de MOS en las hojas LULU y UNH; la plantilla maestra UBER y otras fórmulas del libro aún requieren auditoría y recálculo integral. Los cambios del repositorio Python no se sincronizan automáticamente con las hojas. No existe un backtest representativo que demuestre sesgo general de exigencia o laxitud.
