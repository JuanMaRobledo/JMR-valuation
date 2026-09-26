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
| Margen de seguridad | Se aplicaba al promedio de DCF presente y objetivos FY+3. | Se aplica al DCF Base de hoy. Los pesos por tipo de empresa y su promedio siguen disponibles como criterio exploratorio propio del Modelo JMR, **no** como parámetro de Damodaran. |

## De dónde salen los supuestos

* Estados financieros: SEC EDGAR, transformados por `sec_edgar_loader.py`. La cobertura y clasificación de los hechos XBRL requieren revisión para cada caso.
* Precio, beta y comparables: Yahoo Finance; precio con fecha de negociación. La beta no es la beta bottom-up por industria de Damodaran y su ventana debe validarse antes de tomar una decisión.
* Prima de mercado: hoja oficial [ERPSept26.xlsx](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPSept26.xlsx), C45, con Treasury sin ajuste; valores y corte en `reference/SOURCES.md`.
* Referencias de crecimiento, margen y ventas/capital por industria: CSV heredados del Excel original; **no tienen fecha demostrable**. El set de pares, la mezcla historia/industria, los rangos de escenarios, pesos por método y 35 % de margen son decisiones del Modelo JMR, no cifras prescritas por Damodaran.
* Crecimiento terminal y reinversión: regla de estado estable `g = tasa libre de riesgo` y `reinversión = g/ROIC`, descrita en [Damodaran, terminal value](https://pages.stern.nyu.edu/~adamodar/pdfiles/papers/termvalue.pdf). Se debe verificar que moneda, tasa y rentabilidad de estado estable sean coherentes.

## Prueba de dirección, no valoración actual de Adobe

El archivo `data/example_adbe.csv` es una muestra estática con precio **USD 276,27**, sin corte verificable del mercado. Con los cambios anteriores, su DCF Base pasa de **USD 366,36 a USD 370,50**. El promedio mixto pasa de **USD 410,69 a USD 446,88**: usar ingresos LTM aumenta la proyección de esta muestra, aun después de corregir el puente de EV. El precio con margen de seguridad del 35 % pasa de **USD 266,95** (aplicado antes al promedio mixto) a **USD 240,82** (aplicado al DCF Base). La dirección neta no permite llamar al modelo universalmente estricto ni laxo.

En la misma muestra, DCF Base = USD 370,50. Una variación de **±1 punto porcentual del WACC inicial** da aproximadamente **USD 391,56 / USD 350,83**; una variación de **±2 puntos del crecimiento de ingresos del primer año** da **USD 363,96 / USD 377,04**. El valor terminal representa alrededor del **57 %** del valor de activos operativos. Son pruebas de sensibilidad sobre entradas de ejemplo, no precios objetivo actuales.

## Límite pendiente antes de considerar el modelo validado

Falta fechar y cotejar los CSV de industrias y volver a exportar las primas por país. La exposición geográfica real, el tratamiento de I+D, arrendamientos, opciones, NOL, impuestos y acciones diluidas deben revisarse por compañía. La hoja Excel/Google Sheets original aún requiere auditoría de fórmulas y recálculo: los cambios de este repositorio Python no cambian por sí solos esa hoja. No existe un backtest representativo que demuestre sesgo general de exigencia o laxitud.
