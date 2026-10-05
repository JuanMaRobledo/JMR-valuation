# Prima de mercado de octubre y revisión de DUOL, MSFT y BSX · 5-oct-2026

## Prima de mercado

Las hojas tienen corte al 30-sep-2026 con la tasa libre de riesgo de ese día (UST 10 años, 5,29%), pero usaban la prima
implícita de Damodaran de septiembre (4,09%), calculada el 1-sep con una tasa de 4,75%. La de octubre (ERPOct26.xlsx,
3,70%) se calculó con la misma tasa y los precios del 30-sep, así que es la coherente con el corte
(`scripts/prima_mercado_octubre.py`).

- 'Country equity risk premiums'!B2 = 3,70% en las 22 hojas; las primas por país y región se recalculan (madura + riesgo país).
- Costo de capital terminal (tasa libre + prima madura): 9,38% → 8,99%. AFYA 11,11% → 10,72% y PAGS (Ke terminal) 12,30% →
  11,91%, porque conservan la prima de Brasil.
- ROIC terminal de punto medio (ventaja que se desvanece) recalculado con 8,99%: EPAM 12,0% → 12,1%, LULU 12,6% → 12,4% y
  NKE 12,3% → 12,1% (`scripts/roic_punto_medio_octubre.py`).
- Textos de tasa de las hojas (`scripts/textos_tasa_s2c.py`), especificaciones de las historias, criterios
  (`reference/criterios_damodaran_2026-10-04.md`) y regla de ventaja (`reference/moat_2026-09-30.json`) al día.

## DUOL, MSFT y BSX (revisión cuidadosa, sin ser excesivamente conservador)

- **BSX.** El análisis no incluía el ciberataque del 25-ago-2026 (8-K del 26-ago y 8-K, ítem 1.05, del 8-sep: efecto
  material en el 3T26 y en 2026, no en el largo plazo) ni la guía del 29-jul (3T26 +3-5%; 2026 +5,5-6,5%), que ya
  implicaba ~2-3% en el segundo semestre. El primer año de la Base (6,9%) era optimista frente a esa evidencia: pasa a ~4%
  con un rebote en el segundo (~7,6%); desde el tercero no cambia. Es un desfase, no una historia más pobre. El margen
  objetivo (24%) se mantiene: en el 2T26 el GAAP fue 21,6% y el ajustado 28,4% (amortización 4,3 pp). La regla de ventaja
  sigue dando ROIC terminal = costo de capital (ROIC con plusvalía 4-9% en 2021-2025).
- **DUOL.** Los usuarios activos diarios aceleraron a ~27% en agosto (8-K del 18-ago-2026, dato preliminar), lo contrario
  de lo que mostraría la sustitución por IA: la Disrupción baja de 10% a 5% y la Base sube de 40% a 45% (regla de 5-10 pp
  por trimestre). Texto de la beta corregido (1,35 es la bottom-up global de Software (Internet)).
- **MSFT.** El texto decía ROIC terminal 25,4% «limitado al actual»; la hoja usa 20,6% (promedio de la industria en la
  base del modelo con I+D capitalizado). Corregido; mismo error en PLTR (decía 29,3%) y en NVO (decía 13,1%; la hoja usa
  el costo de capital). Se anotó el cambio de segmentos desde FY2027 (8-K del 2-sep-2026), que no cambia el valor.

## Efecto (frente a main antes de este cambio)

| Empresa | DCF Base (antes → ahora) | Esperado (antes → ahora) | Precio de corte |
|---|---|---|---|
| ADBE | 410,79 → 454,78 | 326,48 → 355,49 | 239,94 |
| AFYA | 22,89 → 24,38 | 20,13 → 21,39 | 12,04 |
| BSX | 34,11 → 35,22 | 32,79 → 33,91 | 43,65 |
| CELH | 23,06 → 24,24 | 20,52 → 21,55 | 27,35 |
| CMG | 23,60 → 26,38 | 22,58 → 25,22 | 31,95 |
| DPZ | 336,72 → 381,29 | 294,73 → 331,17 | 299,61 |
| DUOL | 104,84 → 109,60 | 99,60 → 106,58 | 142,40 |
| EPAM | 174,72 → 190,89 | 156,31 → 168,79 | 108,36 |
| GOOG | 299,68 → 330,86 | 255,10 → 278,78 | 340,74 |
| INTU | 477,89 → 531,76 | 413,26 → 455,43 | 275,71 |
| LULU | 176,18 → 191,62 | 155,86 → 168,01 | 95,86 |
| MSFT | 403,20 → 450,52 | 356,20 → 394,50 | 512,90 |
| NKE | 31,38 → 34,28 | 28,44 → 30,84 | 35,15 |
| NVDA | 200,24 → 222,09 | 182,14 → 201,88 | 228,38 |
| NVO | 31,78 → 33,17 | 30,01 → 31,29 | 37,91 |
| ONON | 33,10 → 34,90 | 30,60 → 32,22 | 30,20 |
| PAGS | 12,06 → 12,26 | 11,49 → 11,68 | 8,90 |
| PLTR | 68,36 → 75,36 | 62,37 → 68,70 | 187,05 |
| PYPL | 109,94 → 119,70 | 94,94 → 102,20 | 52,53 |
| SHAK | 22,30 → 24,68 | 18,22 → 20,23 | 58,68 |
| UBER | 77,14 → 81,56 | 70,04 → 73,99 | 68,51 |
| ZTS | 101,03 → 112,58 | 81,55 → 89,61 | 69,83 |

Controles: 22 de 22 con consistencia 16/16 e integridad 0 hallazgos; fórmula única en seco 0 celdas; hoja = app =
resultado en las 22; 52/52 archivos subidos a Drive.
