# Alphabet Inc., clase C (GOOG) — Valoración Modelo JMR (Damodaran + 5 múltiplos)

- **Hoja del modelo:** [Modelo JMR - Alphabet (GOOG)](https://docs.google.com/spreadsheets/d/1yt2zqdGz1JWEqV3SYqqL-nHarO7C1Oud1lvR3pY9i0U/edit). Copia limpia hecha a mano en Drive de la plantilla maestra ya auditada (ver `scripts/reset_from_master.py`), no una valoración de otra empresa reutilizada.
- **Ticker:** GOOG (clase C, sin voto). Alphabet cotiza en tres clases con los mismos derechos económicos (A con voto, B con 10 votos —no lista—, C sin voto): el valor por acción de este modelo aplica igual a las tres.
- **Fecha y precio del análisis:** 14-sep-2026, **US$345,71**.
- **WACC:** 9,61%: Ke 10,02% (rf 4,99% + beta 1,05 × ERP 4,46% de EE.UU.), Kd después de impuestos 4,66% (calificación real Aa2/AA), deuda financiera neta prácticamente nula (~US$5.376M sobre una capitalización de ~US$4,2 billones).
- **Tipo de empresa (ponderación):** Madura: DCF 40%, EV/EBITDA 20%, P/E 20%, EV/FCFF 10%, P/FCFE 5% y P/OCF 5%.
- **Script reproducible:** `scripts/run_google.py` + `scripts/google_content.py`. Cada celda pisada tiene respaldo en `reference/backups/google_formula_backup.json`.

## Resultado

| Escenario | DCF hoy / acción | DCF vs. precio | Precio objetivo ponderado (3 años) | CAGR a 3 años |
|---|---|---|---|---|
| Conservador | US$155,28 | −55,1% | US$178,35 | −19,8% |
| **Base** | **US$174,28** | **−49,6%** | **US$208,05** | **−15,6%** |
| Optimista | US$292,40 | −15,4% | US$319,24 | −2,6% |

Valores por método en US$ por acción (Conservador / Base / Optimista):

| Método | Conservador | Base | Optimista |
|---|---|---|---|
| DCF | 204,84 | 229,91 | 385,72 |
| EV/EBITDA | 173,03 | 208,02 | 295,74 |
| EV/FCFF | 79,62 | 96,13 | 132,49 |
| P/E | 207,90 | 250,51 | 358,84 |
| P/FCFE | 107,58 | 130,59 | 190,31 |
| P/OCF | 137,82 | 164,77 | 225,41 |

Zonas de compra (sobre el Base): Value US$135,23–145,64; Deep Value US$114,43–124,83; Valoración histórica US$93,62–104,03.

**Lectura.** En el caso Base, deliberadamente conservador (crecimiento y margen sin apostar a una aceleración adicional de Cloud/IA), el modelo da a Alphabet por debajo de su precio de mercado en las 6 metodologías. Solo el escenario Optimista —Google Cloud y la monetización de IA generativa acelerando más rápido que la continuidad simple del negocio actual— se acerca al precio de hoy. El mercado ya está pagando por un ritmo de crecimiento más cercano al caso alcista que al Base. El múltiplo EV/FCFF es un caso aparte: el FCFF reportado se desplomó en los últimos 2 cierres fiscales por el ciclo de capex de infraestructura de IA (centros de datos, TPUs), así que su precio implícito (US$96,13 en el Base) es un piso muy conservador, no una lectura central — se explica en detalle en la hoja «Supuestos de los Múltiplos».

## Supuestos por escenario

| Supuesto | Conservador | Base | Optimista | Ancla |
|---|---|---|---|---|
| Crecimiento Año 1 | 6,0% | 11,0% | 16,0% | Base en línea con el crecimiento LTM real (10,7%); Conservador asume que Cloud no compensa la desaceleración de Búsqueda; Optimista, que Cloud/IA aceleran el consolidado |
| Crecimiento años 2-5 | 6,0% | 7,0% | 16,0% | Converge hacia el crecimiento nominal de EE.UU. más una prima moderada de Cloud/IA |
| Margen EBIT Año 1 | 32,5% | 32,5% | 32,5% | Levemente por debajo del EBIT LTM real (33,1%) por la depreciación creciente del capex de IA |
| Margen objetivo | 32,5% | 33,5% | 37,0% | Expansión moderada, no el ~36% del promedio histórico completo (incluye años de mucho menor inversión) |
| Años de convergencia | 5 | 5 | 5 | Horizonte estándar del modelo |
| Sales-to-capital | 2,5x / 2,0x | 2,5x / 2,0x | 2,5x / 2,0x | Negocio de software/servicios; algo más de intensidad de capital en años 6-10 por Cloud/IA |
| Tasa de impuestos marginal | 16% | | | Corporativa de EE.UU. (21%) neta de la tasa efectiva real más baja por ingresos en el exterior |

## Particularidades del armado

- **Datos:** SEC EDGAR (`us-gaap`, CIK 0001652044), historia completa de 10 años vía el loader genérico del repo (mismo pipeline que NKE/PYPL, sin ajustes manuales al loader).
- **Acciones:** 12.230M combinadas de las 3 clases (A+B+C). Como las tres tienen derechos económicos idénticos, el EPS y el valor por acción del modelo se calculan sobre el total combinado — no hace falta prorratear por clase.
- **Beta:** la canasta de industria «Software (Internet)» de Damodaran da 1,34 desapalancada, dominada por empresas mucho más chicas y de un solo producto (Snap, Pinterest, Match); se sobreestimaría el riesgo de una empresa tan diversificada y estable como Alphabet. Se usó beta observado directo de 1,05.
- **Calificación crediticia:** se corrigió el A1/A+ genérico de la plantilla a la calificación real de Alphabet (Aa2/AA), con vencimiento promedio de deuda de 10 años.
- **Categoría de empresa:** «Madura», igual criterio que MSFT (mega-cap diversificada, con dividendo reciente y bajo apalancamiento).
- **EV/FCFF distorsionado:** el capex de infraestructura de IA (TPUs, centros de datos) creció mucho más rápido que los ingresos en los últimos 2 cierres fiscales, desplomando el FCFF reportado (el múltiplo trailing llegó a superar 250x en el año más reciente). El mínimo positivo de 4 años (que fija el múltiplo Base, ~15x) queda del cierre más antiguo del rango, previo al capex-supercycle — el precio resultante por este método es un piso conservador, no comparable en peso con los otros 5.
