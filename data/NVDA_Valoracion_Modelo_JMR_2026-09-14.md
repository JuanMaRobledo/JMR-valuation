# NVIDIA Corporation (NVDA) — Valoración Modelo JMR (Damodaran + 5 múltiplos)

- **Hoja del modelo:** [Modelo JMR - Alphabet/NVDA — hoja provista por el usuario](https://docs.google.com/spreadsheets/d/1eEsuWSHXWQrBa2Dt5l_9Fbx24M4pug15Rx_Gj-CCkMg/edit). Antes de valorar se ejecutó `scripts/reset_from_master.py --sheet-id ...` para asegurar que tuviera la plantilla maestra auditada vigente (0 hojas nuevas necesarias, 45/45 ya coincidían), en línea con el protocolo obligatorio del repo (nunca reusar una hoja de otra empresa, siempre partir de la plantilla ya corregida).
- **Ticker:** NVDA. Empresa fabless (diseña, no fabrica: TSMC produce los chips).
- **Fecha y precio del análisis:** 14-sep-2026, **US$210,96** (precio congelado por el script al día del análisis; precio de mercado al momento de escribir este resumen: US$225,07).
- **WACC:** 13,42%: Ke ~14,45% (rf 4,99% + beta 1,90 × ERP 4,46% de EE.UU.; beta observado Direct Input, no el de la canasta de industria "Semiconductor" de Damodaran), Kd después de impuestos ~4,94% (calificación real Aa1/AA), posición de caja neta positiva (US$22.443M de caja e inversiones vs. US$11.040M de deuda financiera total).
- **Tipo de empresa (ponderación):** Madura: DCF 40%, EV/EBITDA 20%, P/E 20%, EV/FCFF 10%, P/FCFE 5% y P/OCF 5%.
- **Script reproducible:** `scripts/run_nvidia.py` + `scripts/nvidia_content.py`. Cada celda pisada tiene respaldo en `reference/backups/nvidia_formula_backup.json`.

## Resultado

| Escenario | DCF hoy / acción | DCF vs. precio | Precio objetivo ponderado (3 años) | CAGR a 3 años |
|---|---|---|---|---|
| Conservador | US$106,09 | −49,7% | US$55,76 | −35,8% |
| **Base** | **US$237,60** | **+12,6%** | **US$120,41** | **−17,0%** |
| Optimista | US$301,14 | +42,7% | US$147,94 | −11,2% |

Valores por método en US$ por acción (Conservador / Base / Optimista):

| Método | Conservador | Base | Optimista |
|---|---|---|---|
| DCF | 106,09 | 237,60 | 301,14 |
| EV/EBITDA | 24,71 | 47,55 | 51,99 |
| EV/FCFF | 18,80 | 34,03 | 35,65 |
| P/E | 23,73 | 46,17 | 50,61 |
| P/FCFE | 18,37 | 33,87 | 35,73 |
| P/OCF | 16,75 | 30,67 | 32,23 |

Zonas de compra (sobre el Base): Value US$78,27–84,29; Deep Value US$66,23–72,25; Valoración histórica US$54,19–60,21.

**Lectura — atención al peso de los múltiplos.** El DCF Base (US$237,60) queda apenas por encima del precio del análisis, pero el precio objetivo ponderado Base (US$120,41) queda muy por debajo, porque el 60% del peso recae en 5 métodos de múltiplos que usan como múltiplo objetivo el **mínimo positivo de los últimos 4 cierres fiscales**: para NVDA ese mínimo cae en el cierre de enero-2024 (EV/EBITDA 4,46x, P/E 5,05x), un año atípico donde la utilidad creció mucho más rápido que la revalorización de la acción en ese momento puntual (EBITDA +6,0x interanual). Los cierres siguientes (FY2025 y FY2026) muestran múltiplos mucho más altos (EV/EBITDA 41,9x/34,2x; P/E 47,9x/38,0x), así que ese mínimo no es representativo del rango. **Para NVDA, el DCF es la lectura más confiable de las 6 metodologías**; el precio objetivo ponderado tiene un sesgo a la baja estructural que no refleja necesariamente sobrevaloración. Ver el detalle completo en la hoja «Supuestos de los Múltiplos».

## Supuestos por escenario

| Supuesto | Conservador | Base | Optimista | Ancla |
|---|---|---|---|---|
| Crecimiento Año 1 | 30% | 50% | 68% | Base: desaceleración deliberada frente al crecimiento reciente de Data Center (+117% i.a.) y frente a la mitad de la guía propia de la compañía para el próximo año fiscal (~70%, "limitado por la oferta"); Conservador: los ASICs propios de los hiperescaladores restan cuota de forma material; Optimista: la demanda de cómputo de IA sigue superando a la oferta, en línea con la guía de la compañía |
| Crecimiento años 2-5 | 6% | 14% | 22% | Base: la demanda de cómputo de IA se mantiene fuerte pero los ASICs propios empiezan a restar crecimiento incremental de forma gradual |
| Margen operativo Año 1 | 60% | 60% | 60% | En línea con el margen GAAP LTM real (65,2%), sin asumir mayor expansión en el Año 1 |
| Margen objetivo | 50% | 58% | 65% | Base: leve compresión desde el margen LTM real (65,2%) por presión de precio de los ASICs propios de los hiperescaladores y mezcla de producto |
| Años de convergencia | 5 | 5 | 5 | Horizonte estándar del modelo |
| Sales-to-capital | 3,0x / 2,5x | 3,0x / 2,5x | 3,0x / 2,5x | Diseño fabless de chips (TSMC fabrica): relativamente liviano en capital fijo propio |
| Tasa de impuestos marginal | 16% | | | Corporativa de EE.UU. (21%) neta de la tasa efectiva histórica más baja de Nvidia |

## Particularidades del armado

- **Datos:** SEC EDGAR (`us-gaap`, CIK 0001045810), historia completa de 10 años vía el loader genérico del repo (mismo pipeline que NKE/PYPL/GOOG, sin ajustes manuales al loader). LTM: ingresos US$302.970M (+40,3% i.a.), margen operativo 65,2%, margen EBITDA 66,4%, utilidad neta US$192.880M.
- **Beta:** la canasta de industria "Semiconductor" de Damodaran promedia decenas de fabricantes mucho más diversificados y de menor crecimiento que Nvidia, subestimando su riesgo idiosincrático específico (concentración de ingresos en la narrativa de IA y en un puñado de clientes hiperescaladores). Se usó beta observado directo de 1,90 (fuentes de mercado citan un rango de 1,7-2,2 según ventana/frecuencia de cálculo).
- **Calificación crediticia:** se corrigió el A1/A+ genérico de la plantilla a la calificación real de Nvidia (Aa1 Moody's / AA S&P, set-2026), con vencimiento promedio de deuda de 10 años.
- **Categoría de empresa:** "Madura" (utilidad positiva y creciente desde hace varios años, sin el patrón de signo cambiante de una empresa en transición a la rentabilidad), igual criterio que MSFT/GOOG/ADBE.
- **Multiplos distorsionados a la baja (los 5 métodos, no solo uno):** el mínimo positivo de 4 años cae en un cierre atípico (ene-2024) donde el crecimiento de utilidad superó a la revalorización de mercado de ese momento puntual. Ver la sección "Resultado" arriba para el detalle cuantitativo.
