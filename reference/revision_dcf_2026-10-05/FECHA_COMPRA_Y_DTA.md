# Fecha del análisis, posición en cartera e impuestos diferidos · 6-oct-2026

## Fecha del análisis y posición en cartera

Primero (6-oct-2026, mañana) la fecha y el precio del análisis se pusieron en la primera compra. A pedido del usuario se
revirtió el mismo día: la fecha y el precio del análisis son los REALES (el corte de la valoración: 30-sep-2026; LULU, NKE y
ONON 1-oct-2026) y la posición va aparte (`scripts/posicion_cartera.py`).

- 'Input sheet'!B4 = fecha del corte; 'Resumen de Valoración'!C25 = B3 = 'Input sheet'!D1 (cierre de ese día). B23 (precio de
  mercado del modelo: peso del patrimonio, opciones, precio/valor) = D1 en las 22; en DUOL, PLTR y UBER era un GOOGLEFINANCE a
  la fecha de B4 y en ADBE, AFYA, MSFT, NVO y PYPL apuntaba a C25.
- 'Resumen de Valoración'!A50:E60 «Mi posición en cartera» (fuente: hoja «Seguimiento de cartera» de Drive, IBKR y Hapi,
  `reference/cartera_compras_2026-10-06.json`): acciones, costo promedio, primera compra; precio de hoy (GOOGLEFINANCE en vivo)
  y del análisis con la ganancia sobre el costo; y la ganancia potencial hasta el DCF Base, el DCF esperado y el ponderado,
  desde el precio de hoy y desde el precio de compra, en % y en US$ de la posición.
- App (Modelo-JMR, visor): sección «Tu posición», con el precio en vivo si hay clave de mercado; el registro guardado lleva el
  campo `posicion`.
- Verificación: DCF Base, esperado, costo de capital y precio de mercado iguales en las 22; consistencia 16/16; integridad 0
  hallazgos; fórmula única 0 celdas.

| Empresa | Primera compra | Precio ese día | Costo promedio de la posición | Acciones | Otras compras |
|---|---|---:|---:|---:|---|
| ADBE | 2025-12-03 | US$324,63 | US$264,13 | 7.98426 | 2026-01-09, 2026-01-14, 2026-01-22, 2026-02-20, 2026-03-13, 2026-07-01 |
| AFYA | 2026-02-25 | US$13,75 | US$13,77 | 20 | — |
| BSX | 2026-08-07 | US$49,50 | US$49,56 | 12 | — |
| CELH | 2026-03-06 | US$42,00 | US$32,95 | 30 | 2026-03-23, 2026-03-25, 2026-07-09, 2026-08-06 |
| CMG | 2026-03-27 | US$30,91 | US$30,95 | 10 | — |
| DPZ | 2026-07-29 | US$363,66 | US$364,01 | 1 | — |
| DUOL | 2026-02-17 | US$113,37 | US$107,93 | 7.44245 | 2026-02-20, 2026-02-27 |
| EPAM | 2026-04-07 | US$135,93 | US$110,61 | 4 | 2026-07-01 |
| GOOG | — | — | — | 0 | sin posición al 5-oct-2026 (última operación 2026-01-08 venta); queda el corte del 30-sep-2026 |
| INTU | 2026-07-29 | US$331,29 | US$331,64 | 1 | — |
| LULU | 2026-03-06 | US$170,04 | US$145,05 | 4 | 2026-03-27, 2026-08-07 |
| MSFT | 2026-04-07 | US$370,14 | US$363,18 | 2 | 2026-06-25 |
| NKE | 2026-04-01 | US$47,29 | US$47,33 | 8 | — |
| NVDA | — | — | — | 0 | sin posición al 5-oct-2026 (sin operaciones); queda el corte del 30-sep-2026 |
| NVO | 2026-02-25 | US$38,00 | US$37,99 | 20.4 | 2026-03-11, 2026-03-13, 2026-03-23 |
| ONON | 2026-08-12 | US$30,75 | US$30,77 | 15 | — |
| PAGS | 2026-04-07 | US$10,34 | US$10,36 | 20 | — |
| PLTR | — | — | — | 0 | sin posición al 5-oct-2026 (última operación 2026-08-07 compra); queda el corte del 30-sep-2026 |
| PYPL | 2026-02-25 | US$47,68 | US$46,95 | 11 | 2026-03-06, 2026-03-13 |
| SHAK | 2026-07-10 | US$59,19 | US$59,25 | 6 | — |
| UBER | 2026-01-20 | US$83,44 | US$76,52 | 6 | 2026-07-24 |
| ZTS | 2026-08-07 | US$72,52 | US$72,59 | 5 | — |

## Impuestos diferidos activos en el capital invertido (revisión de las 19 restantes)

Criterio (el mismo de UBER, NVDA y DUOL): se excluyen del capital invertido los impuestos diferidos activos que no son capital operativo, como los creados de una vez al liberar una reserva de valuación. Los que nacen de diferencias temporales de la operación (provisiones, I+D capitalizado para impuestos, arrendamientos, utilidades no realizadas entre filiales) son parte del capital y se quedan.

| Empresa | Impuestos diferidos activos / capital invertido | Evolución (SEC XBRL) | Decisión |
|---|---:|---|---|
| NVO | ~31% | Estable o creciendo con el negocio (DKK 13.400 millones en 2022 → 23.600 millones en 2025) | Sin liberación de reserva: se queda |
| SHAK | ~28% | Estable desde 2022 (US$314-347 millones); reserva de valuación casi nula desde 2023 | Sin liberación reciente: se queda; con ROIC terminal = costo de capital no cambia el valor |
| NKE | ~15% | Creciendo gradualmente (US$1.800 → 2.600 millones en FY2023-FY2026) | Se queda |
| BSX | ~11% | Estable (US$3.700-3.950 millones) | Se queda |
| ONON | ~11% | Creciendo con el negocio (CHF 70 → 176 millones) | Se queda |
| EPAM | ~10% | Estable (US$235-296 millones) | Se queda |
| ADBE | ~9% | Estable (US$1.900-2.200 millones) | Se queda |
| Resto (AFYA, CELH, CMG, DPZ, GOOG, INTU, LULU, MSFT, PAGS, PLTR, PYPL, ZTS) | < 5% o sin datos | — | Se queda |

Ninguna de las 19 tuvo una liberación de reserva de valuación reciente como DUOL (3T25), UBER (2024-2025) o NVDA.
