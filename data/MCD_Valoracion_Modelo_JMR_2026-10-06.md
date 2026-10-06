---
schema: "jmr-valoracion-v4"
ticker: "MCD"
company: "McDonald's Corporation"
analysis_date: "2026-10-06"
information_cutoff: "2026-09-30"
currency: "USD"
---

# McDonald's Corporation (MCD) — Valoración Modelo JMR desde cero (prompt v4)

> Estimación condicionada a supuestos; no es asesoría financiera ni una recomendación. Hoja: [Modelo JMR - MCD (desde cero 2026-10-06)](https://docs.google.com/spreadsheets/d/1D44qNMrcbmbDbWuGO4EdFJdWdg9xE6cYg_pDCwLb30M/edit), copia nueva de la plantilla maestra con la fórmula única, en la carpeta «MCD» de Análisis; la hoja del 27-sep-2026 («Plantilla maestra reutilizable (vigente)», misma carpeta) queda sin cambios como referencia. Cifras en US$ millones salvo valores por acción.

## 1. Resumen

**Valor intrínseco principal · DCF Base hoy: US$224,12 por acción** (historia «Base · Refranquiciamiento a 98% y comparables de 2-3%»).

**Complemento · DCF esperado por probabilidades: US$203,96 por acción.**

| Historia activa | Probabilidad | DCF hoy por acción |
|---|---:|---:|
| Base · Refranquiciamiento a 98% y comparables de 2-3% | 50% | US$224,12 |
| Conservadora · El tráfico de EE.UU. no vuelve y el valor cuesta margen | 25% | US$185,42 |
| Disrupción · Deterioro de los fundamentales: los franquiciados pierden rentabilidad y la renta deja de crecer | 10% | US$75,44 |
| Optimista · NEXT recupera el tráfico y la escala se nota en el margen | 15% | US$253,34 |
| DCF esperado (complemento) | 100% | US$203,96 |
| Precio con margen de seguridad (35% sobre el esperado) | | US$132,57 |

'Valuation output' calcula las cuatro historias con la estructura de Damodaran (Base B35, Conservadora B86, Optimista B137, Disrupción B190) y «Escenarios e historias» las resume; el motor del Modelo JMR las reproduce al centavo (diferencia 0,00 en las cuatro).

Precio relativo (secundario; Base / Conservador / Optimista): múltiplos solos al presente US$279,64 / US$251,29 / US$301,64 y a 3 años sin descontar US$320,92 / US$280,77 / US$352,95; ponderado DCF + múltiplos (40%/60%, categoría «Madura» por su etapa del ciclo de vida de Damodaran) al presente US$257,43 / US$224,94 / US$282,32 y a 3 años sin descontar US$307,67 / US$263,70 / US$341,89, con el DCF capitalizado a FY+3 (US$287,78 / US$238,09 / US$325,31). Ninguno es valor intrínseco; las dos tablas completas están en «Resultados».

**Qué cambió frente al análisis del 27-sep-2026** (DCF Base US$225,92 con el prompt v2, sin historias): la hoja nueva usa la fórmula única de la maestra y las cuatro historias activas; los datos se corrigieron contra la SEC (D&A total en lugar de la corporativa, balance al 30-jun-2026, deuda corriente sin duplicar); los arrendamientos operativos pasan a ser deuda con el conversor (antes se excluían); la prima de mercado es la de octubre (3,70%, antes 4,09%) ponderada por regiones; el costo de capital terminal es el de la regla de la cartera (8,99%, antes 8,25% escrito a mano) y el ROIC terminal es el promedio de la industria (18,4%, antes 12%) por el criterio de ventaja durable; los múltiplos salen de tres anclas en lugar de 0,78 × la mediana histórica.

## 2. Historia y visión externa

**La historia.** En cinco a diez años McDonald's es, todavía más que hoy, un dueño de inmuebles y de una marca que cobra renta y regalías sobre las ventas de ~50.000 restaurantes operados por terceros. El refranquiciamiento lleva la mezcla de ~95% a ~98% de locales franquiciados a fines de 2028, así que los ingresos reportados bajan dos años aunque las ventas del sistema sigan creciendo ~5% (aperturas ~2,5% y comparables de 2-3%). El margen operativo sube de ~46% a ~52% por esa mezcla y por un gasto general que baja de 2,2% a 1,9% de las ventas del sistema, sin llegar al tope de la guía porque el apoyo de rentas del plan NEXT se amortiza contra el resultado. Reinvierte mucho capital por dólar de ventas nuevas (terrenos y edificios), con un rendimiento parecido al actual (~21% con arrendamientos). El riesgo no es financiero: es de tráfico en EE.UU., de la salud de los franquiciados y del costo de defender el valor percibido.

| Afirmación | ¿Posible? | ¿Plausible? | ¿Probable? |
|---|---|---|---|
| Las ventas del sistema crecen ~5% anual hasta 2030 | Sí | Sí: +4% a moneda constante en el 2T26 con aperturas que aportan ~2,5% ([comunicado del 2T26, 4-ago-2026](https://www.sec.gov/Archives/edgar/data/63908/000006390826000067/exhibit991-6302026.htm); [anexo 99.2 del 2T26](https://www.sec.gov/Archives/edgar/data/63908/000006390826000067/exhibit992-6302026.htm)) | Probable con comparables de 2-3%; el 3-4% de la gerencia exige tráfico positivo en EE.UU. |
| Refranquiciamiento de ~95% a ~98% a fines de 2028 | Sí | Sí: meta del CFO en el Investor Day ([transcripción, 23-sep-2026](https://stockanalysis.com/stocks/mcd/transcripts/746101-investor-day-2026/)) | Probable; depende de compradores en los mercados propios de IOM |
| Margen operativo de 52% o más en 2030 | Sí | Sí: guía de «low-to-mid 50%» ajustado ([8-K del Investor Day, 23-sep-2026](https://www.sec.gov/Archives/edgar/data/63908/000006390826000076/exhibit991-investorupdate2.htm)) | Plausible: el apoyo de rentas se amortiza ~10 años contra el resultado |
| NEXT recupera el tráfico de EE.UU. | Sí | Débil: comparables +0,8% en el 2T26 y guía de 3T26 levemente negativa | Incierto |

**Tasas base.** Con ingresos LTM de US$27.702 millones (US$19.601 millones de 2015), McDonald's está en el tramo de US$12.000-25.000 millones de *The Base Rate Book* (Mauboussin y Callahan, 2016, Exhibit 4): mediana real a 5 años de 2,9% y media de 3,3% (~5,4% nominal con 2,5% de inflación). Lograron al menos el crecimiento de la Base (1,0% nominal) ~75% de las empresas de ese tamaño; el de la Optimista (2,1%), ~71%; el de la Conservadora (−0,4%), ~81%. La Base queda por debajo de la mediana por una razón contable, no de demanda: el refranquiciamiento cambia ventas de restaurantes propios por rentas y regalías de ~15% de esas ventas.

**Crecimiento por piezas.** Ingresos LTM (2025 + 1S26 − 1S25): franquicias US$17.073 millones (rentas ~10,4% y regalías ~6% de la venta de los locales franquiciados), restaurantes propios US$9.942 millones y otros US$688 millones ([10-K 2025, 24-feb-2026](https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm); [comunicado del 2T26](https://www.sec.gov/Archives/edgar/data/63908/000006390826000067/exhibit991-6302026.htm)). Todo el crecimiento es orgánico: no hay compras relevantes. Las ventas del sistema fueron US$139.400 millones en 2025 (+5% a moneda constante); en el 2T26 las comparables crecieron 1,3% (EE.UU. +0,8% por ticket y mezcla con tráfico negativo, IOM +1,5%, IDL +1,9%).

**Márgenes normalizados.** Margen GAAP LTM 46,2%. Los cargos de reestructuración de Accelerating the Organization (US$219 millones LTM) no se excluyen: se repiten desde 2023 (US$362, 291 y 229 millones). La fuente del margen es la mezcla: franquicias ~84% después de la ocupación, restaurantes propios ~15%. Comparables: Yum! (casi 100% franquiciada) ~33% y Domino's ~19%; ninguno es dueño de sus inmuebles, de ahí la diferencia.

**Reinversión y retorno.** Capex 2025 US$3.365 millones (1,5 veces la D&A) y guía 2026 de US$3.700-3.900 millones; 2027-2030 ~US$3.000 millones al año más US$1.500-2.000 millones de apoyo de capital ([8-K del Investor Day](https://www.sec.gov/Archives/edgar/data/63908/000006390826000076/exhibit991-investorupdate2.htm)). Capital invertido con arrendamientos ~US$50.400 millones y ROIC después de impuestos ~21% ('Valuation output'!B41:B42).

## 3. Datos

- Hoja: [Modelo JMR - MCD (desde cero 2026-10-06)](https://docs.google.com/spreadsheets/d/1D44qNMrcbmbDbWuGO4EdFJdWdg9xE6cYg_pDCwLb30M/edit). Fecha de corte: 30 de septiembre de 2026 (la de las tasas comunes de la cartera). Último reporte: 10-Q del 2T26 (7 de agosto de 2026).
- Conciliación: ingresos LTM 26.885 − 12.799 + 13.616 = 27.702; EBIT GAAP LTM 12.393 − 5.880 + 6.292 = 12.805; D&A LTM 2.199 − 1.064 + 1.131 = 2.266 (EBITDA 15.071); caja US$822 millones; deuda de largo plazo US$39.863 millones (incluye vencimientos corrientes y papel comercial); arrendamientos financieros US$2.329 millones (10-K 2025) y operativos US$14.729 millones en el balance (por el conversor, VP de compromisos US$10.020 millones a la tasa de la deuda); patrimonio −US$1.023 millones; 707,6 millones de acciones al 30-jun-2026 + 1,164 millones de RSU; 8,8 millones de opciones a US$228,19; sin minoritarios ni preferentes ([10-Q del 2T26, 7-ago-2026](https://www.sec.gov/Archives/edgar/data/63908/000006390826000073/mcd-20260630.htm); [10-K 2025, 24-feb-2026](https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm)).
- Estados financieros: SEC EDGAR (XBRL) con el importador del repositorio y correcciones documentadas (D&A total 2020-LTM, SG&A 2020-2021, BPA y acciones 2023-LTM, balance al 30-jun-2026, deuda corriente y arrendamientos comparables); respaldo de cada celda en `reference/backups/mcd_desde_cero_2026-10-06.json`; script reproducible `scripts/run_mcd_cero.py`.

## 4. Supuestos del DCF y costo de capital

| Supuesto (Base) | Valor | Celda | Procedencia | A favor | En contra |
|---|---:|---|---|---|---|
| Crecimiento año 1 | −0,9% | «Escenarios e historias» / Input B27 | Franquicias +7%, restaurantes propios −15%, otros +8% | Ventas del sistema +4-5% | Comparables de EE.UU. negativas en el 3T26 |
| Crecimiento años 2-5 | −4,7%, +1,6%, +4,6%, +4,6% (1,5% compuesto) | «Escenarios e historias» / Input B29 | Refranquiciamiento hasta 2028; después ventas del sistema ~5% | Guía de aperturas de ~2,5% | Apoyo de rentas resta ~1 punto |
| Margen año 1 | 49,7% | Input B28 | LTM 46,2% + 3,48 pp de arrendamientos | Guía 2026 «mid-to-high 40%» | Reestructuración recurrente |
| Margen objetivo | 55,5% (52% + 3,48 pp de arrendamientos) | «Escenarios e historias» D5 | Tramo bajo-medio de la guía a 2030 | Mezcla de 98% y gasto general de 1,9% | Amortización del apoyo de rentas |
| Convergencia | 5 años | Input B31 | La guía llega a 2030 | — | — |
| Ventas/capital | 0,5 (años 1-10) | Input B32/B33 | Rendimiento del capital nuevo ~21% = ROIC actual | Modelo de renta con inmuebles propios | En los años 1-2 libera ~US$2.600 M por la caída de ingresos |
| Tasa efectiva → marginal | 22% → 25% | Input B24/B25 | Guía 2026: 21-23% | — | — |
| ROIC después del año 10 | 18,4% (promedio de Restaurant/Dining) | Input B49 = Yes / B50 | Ventaja durable | ROIC ~21% sostenido, marca de 70 años | Tráfico débil en EE.UU. |

**Costo de capital.** Tasa libre de riesgo 5,29% (UST 10 años al 30-sep-2026); prima de mercado 3,70% (Damodaran, octubre de 2026) ponderada por las ventas de cada región: 4,33% (EE.UU. y Canadá ~46%, Europa ~43%, Australia ~5%, IDL ~9% con la prima global sin desglose; reparto de IOM por número de locales, estimación); beta 0,79: la bottom-up de Restaurant/Dining global (0,66 desapalancada) reapalancada con la D/E de mercado (~25%), elegida porque ~60% de las ventas está fuera de EE.UU.; con la tabla de EE.UU. (0,78 corregida por caja) sería 0,93. Ke 8,69%; Kd 7,13% antes de impuestos (calificación real Baa1/BBB+), 5,35% después; peso del patrimonio 79,9% (deuda con los arrendamientos capitalizados); WACC inicial 8,02% y terminal 8,99% (tasa libre + prima madura). Efecto en el DCF Base: US$224,12 con la beta usada y US$216,02 con la de EE.UU. El tráfico, el costo laboral y la salud de los franquiciados son riesgos propios y diversificables: van en las historias Conservadora y Disrupción, no en la tasa.

## 5. Historias, probabilidades y valor esperado

| Historia | Probabilidad | Crecimiento por fuente de ingresos (años 1-5) | CAGR de ingresos (años 1–5) | Margen objetivo (ajustado) | Sales-to-capital | ROIC terminal | Crecimiento terminal | Valor/acción (beta 0,79) |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **Base · Refranquiciamiento a 98% y comparables de 2-3%** | 50% | Franquicias 7%, 6,5%, 5%, 5%, 5%; propios −15%, −30%, −10%, 3%, 3%; otros 8%, 7%, 6%, 5%, 5% | 1,0% | 55,5% | 0,5 | 18,4% | 5,29% | US$224,12 |
| **Conservadora · El tráfico de EE.UU. no vuelve y el valor cuesta margen** | 25% | Franquicias 5%, 5%, 3,5%, 3,5%, 3,5%; propios −15%, −30%, −10%, 1%, 1%; otros 5%, 4%, 4%, 3%, 3% | −0,4% | 51,5% | 0,5 | 18,4% | 5,29% | US$185,42 |
| **Disrupción · Deterioro de los fundamentales: los franquiciados pierden rentabilidad y la renta deja de crecer** | 10% | Franquicias 3%, 2%, 0,5%, 0%, 0%; propios −17%, −30%, −12%, −2%, −2%; otros 2%, 0%, 0%, 0%, 0% | −3,1% | 46,5% | 0,5 | = costo de capital (8,99%) | 0,00% | US$75,44 |
| **Optimista · NEXT recupera el tráfico y la escala se nota en el margen** | 15% | Franquicias 8%, 8%, 6,5%, 6,5%, 6%; propios −15%, −30%, −10%, 4%, 4%; otros 10%, 9%, 8%, 7%, 6% | 2,1% | 58,0% | 0,5 | 18,4% | 5,29% | US$253,34 |
| **DCF esperado (complemento)** | 100% | | | | | | | **US$203,96** |

DCF esperado = 0,50 × 224,12 + 0,25 × 185,42 + 0,10 × 75,44 + 0,15 × 253,34 = US$203,96. Las probabilidades son juicio del analista: la Base extrapola las ventas del sistema de los últimos años con comparables algo menores que la guía; la Conservadora es lo que hoy muestran EE.UU. y la reacción del mercado al plan NEXT; la Disrupción pesa 10% porque el negocio superó crisis peores, pero el GLP-1 y el costo laboral son amenazas nuevas; la Optimista exige a la vez tráfico positivo y el tope de la guía. Los márgenes de la tabla están en base ajustada por arrendamientos (reportados: 52%, 48%, 43% y 54,5%). La Disrupción se estabiliza sin recuperación (crecimiento terminal 0%) y su ROIC terminal es el costo de capital.

Puente de los cuatro DCF (US$ millones):

| Historia | VP FCFF años 1–10 | VP terminal | Activos operativos | Patrimonio, tras caja, deuda y opciones | DCF/acción |
|---|---:|---:|---:|---:|---:|
| Base | 69.627,03 | 141.137,98 | 210.765,01 | 158.846,77 | 224,12 |
| Conservadora | 64.998,33 | 118.337,48 | 183.335,81 | 131.417,57 | 185,42 |
| Disrupción | 64.522,20 | 40.861,76 | 105.383,97 | 53.465,73 | 75,44 |
| Optimista | 72.783,98 | 158.694,87 | 231.478,85 | 179.560,61 | 253,34 |

Ejemplo Base: (69.627,03 + 141.137,98 + 822 − 52.212 − 528) / 708,8 = US$224,12 por acción (la deuda incluye US$10.020 millones de arrendamientos capitalizados). El terminal representa 67,0% del valor operativo: el resultado depende materialmente del WACC terminal, del crecimiento perpetuo y de la duración del retorno excedente.

Sensibilidad crecimiento × margen del DCF Base (crecimiento constante en los años 1-5; US$ por acción):

| Crecimiento \ Margen | 51,5% | 53,5% | 55,5% | 57,5% | 59,5% |
|---|---:|---:|---:|---:|---:|
| −2,9% | 152,18 | 159,80 | 167,43 | 175,05 | 182,68 |
| −0,9% | 173,18 | 181,87 | 190,55 | 199,24 | 207,93 |
| 1,1% | 196,53 | 206,41 | 216,29 | 226,17 | 236,05 |
| 3,1% | 222,47 | 233,69 | 244,91 | 256,13 | 267,35 |
| 5,1% | 251,28 | 264,00 | 276,72 | 289,44 | 302,15 |

**Pre-mortem.** (1) El valor no recupera el tráfico: los franquiciados no adoptan los precios sugeridos (60-65% lo hizo en el 2T26) y las comparables de EE.UU. siguen en ~0%; (2) el apoyo de rentas se vuelve permanente y la renta efectiva baja; (3) el refranquiciamiento se demora o se vende barato en IOM y la mejora de margen llega tarde; (4) el GLP-1 y la regulación laboral reducen la frecuencia y el flujo del franquiciado; (5) un dólar más fuerte recorta 1-2 puntos el crecimiento reportado. Evidencia en contra de la Base: comparables de EE.UU. de +0,8% con tráfico negativo, un 3T26 guiado levemente negativo y la caída de 4,8% de la acción el día del Investor Day.

**Indicadores.** Comparables de EE.UU. (+0,8% en el 2T26; favorable ≥ +2% desde el 1T27, desfavorable ≤ 0% dos trimestres más), comparables globales (+1,3%; ≥ +3% / ≤ 0%), ventas del sistema a moneda constante (+4%; ≥ +5% / ≤ +3%), mezcla franquiciada (~95%; ~98% a fines de 2028 / demora), margen ajustado (46,9%; ≥ 48% en 2027 / ≤ 45%), gasto general sobre ventas del sistema (~2,2%; ≤ 2,0% en 2028 / ≥ 2,3%), usuarios activos de fidelización (~220 millones; ≥ +10% anual / estancamiento) y acciones en circulación (707,6 millones; bajan ~1% anual / suben). Regla: mover 5-10 pp de probabilidad por trimestre sin cambiar el valor de cada historia salvo que cambie un supuesto.

## 6. Múltiplos (precio relativo)

| Método | Ancla historia | Ancla peers (ajustada) | Ancla justificado Base/Cons/Opt | Base | Conservador | Optimista |
|---|---|---|---|---:|---:|---:|
| EV/EBITDA | mediana FY2021-FY2025 + LTM = 18,3x | 14,4x (n=3: YUM 16,3x, QSR 13,8x, DPZ 14,5x) × 1,05 = 15,2x | 16,6x / 15,7x / 17,0x | **16,7x** | 15,6x | 17,4x |
| EV/FCFF | mediana = 31,0x (EV/FCF × 0,87 = FCF después de intereses ÷ FCFF) | 19,9x (n=3: YUM 24,0x, QSR 19,9x, DPZ 18,3x) × 1,05 = 20,9x | 31,5x / 27,5x / 34,9x | **27,4x** | 25,0x | 30,6x |
| P/E | mediana = 25,6x | 17,2x (n=3: YUM 17,3x, QSR 17,6x, DPZ 16,9x) × 1,05 = 18,1x | no se calcula (patrimonio negativo) | **21,9x** | 21,2x | 22,5x |
| P/FCFE | mediana = 30,2x | 19,6x (n=3: YUM 22,3x, QSR 19,6x, DPZ 15,0x) × 1,05 = 20,6x | 29,2x / 25,7x / 32,1x | **26,4x** | 23,5x | 28,9x |
| P/OCF | mediana = 22,1x | 16,8x (n=3: YUM 17,9x, QSR 16,8x, DPZ 12,6x) × 1,05 = 17,6x | 22,9x / 19,2x / 26,4x | **20,6x** | 17,8x | 22,5x |

Regla: Base = (1 − λ) × promedio(historia, peers) + λ × justificado, dentro del rango de las tres anclas; Conservador y Optimista = Base × la dispersión promedio de las anclas (P25/mediana y P75/mediana de historia y peers; justificado Conservador/Base y Optimista/Base). Justificado: g = punto medio entre el crecimiento de los años 4-10 del escenario y el de perpetuidad; EV/FCFF = (1+g)/(WACC−g), P/FCFE = (1+g)/(Ke−g), EV/EBITDA y P/OCF convertidos con FCFF/EBITDA y FCFE/OCF de FY+3.

**Decisiones.** Ancla A: franquiciador maduro sin cambio de etapa; mediana de FY2021-FY2025 y LTM. El LTM (P/E 18,8×, EV/EBITDA 13,6×) es el más bajo de la década y refleja la caída de la acción en 2026, no un cambio de etapa. Ancla B: Yum!, Restaurant Brands y Domino's (yfinance, consultado el 6-oct-2026); se excluyen Wendy's (seis trimestres de comparables negativas; P/OCF 3×), Papa John's (ingresos −8,8%) y Chipotle (opera sus locales). Ajuste +5%: −5% por crecimiento reportado menor por el refranquiciamiento, +5% por margen y +5% por riesgo menor (Baa1/BBB+ frente a grado especulativo de Yum! y RBI; inmuebles propios). λ = 0,25: la empresa de FY+3 se parece a la de hoy. P/E no tiene justificado porque el patrimonio contable es negativo (−US$1.023 millones por US$80.527 millones de recompras acumuladas): el ROE no tiene sentido y su Base es el promedio de A y B.

**Por método.** EV/EBITDA (peso 20%) es el más usado para franquiciadores maduros, pero ignora la reinversión en inmuebles (capex 1,5 veces la D&A). EV/FCFF (10%) es el más consistente con el DCF. P/E (20%) depende de la deuda (intereses de US$1.625 millones LTM) y de la tasa efectiva. P/FCFE (5%) y P/OCF (5%) muestran saltos entre FY+1 y FY+2 porque la plantilla proyecta el endeudamiento neto y el capital de trabajo proporcionales al cambio de ventas, que es negativo por el refranquiciamiento: por eso sus VP a 1 año son mucho mayores que a 2 y 3 años (US$447 y US$407 frente a ~US$252). Es una limitación mecánica conocida; pesan 10% entre los dos.

**Chequeo de independencia (6.4).** Los múltiplos consolidados Base hoy (US$279,64) están 25% por encima del DCF Base (US$224,12), en el límite del ±25%. No se movió ningún múltiplo. La causa es de crecimiento del BPA: la historia de cinco años (P/E 25,6×) se formó cuando el BPA crecía ~8-10% al año, mientras la Base del DCF supone ingresos casi planos por el refranquiciamiento y un margen que sube poco a poco. El chequeo de crecimiento implícito (6.5) no da alertas: los cinco Base difieren menos de 1 pp del crecimiento que implica el DCF en FY+3.

## 7. Resultados

**Tabla 1 · Valor por acción descontado al presente (2026-09-30).** Cada método usa el promedio simple de los VP a 1, 2 y 3 años (criterio vigente de la hoja); cada dividendo se descuenta en su año de pago.

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF de las historias al presente | — | 40% | — | US$224,12 | US$185,42 | US$253,34 |
| EV/EBITDA | 16,7× / 15,6× / 17,4× | 20% | 33% | US$269,57 | US$234,71 | US$292,75 |
| EV/FCFF | 27,4× / 25,0× / 30,6× | 10% | 17% | US$299,74 | US$276,43 | US$329,03 |
| P/E | 21,9× / 21,2× / 22,5× | 20% | 33% | US$263,26 | US$243,81 | US$279,45 |
| P/FCFE | 26,4× / 23,5× / 28,9× | 5% | 8% | US$306,94 | US$268,12 | US$336,32 |
| P/OCF | 20,6× / 17,8× / 22,5× | 5% | 8% | US$317,91 | US$280,42 | US$336,50 |
| **Ponderado de múltiplos solos al presente** | — | 60% | 100% | US$279,64 | US$251,29 | US$301,64 |
| **Ponderado DCF + múltiplos al presente** | — | 100% | — | US$257,43 | US$224,94 | US$282,32 |

**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 más los dividendos por acción de FY+1 a FY+3 (US$25,58).

| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |
|---|---|---:|---:|---:|---:|---:|
| DCF capitalizado a FY+3 antes de distribuciones | — | 40% | — | US$287,78 | US$238,09 | US$325,31 |
| EV/EBITDA (total con dividendos) | 16,7× / 15,6× / 17,4× | 20% | 33% | US$334,42 | US$281,67 | US$372,13 |
| EV/FCFF (total con dividendos) | 27,4× / 25,0× / 30,6× | 10% | 17% | US$282,21 | US$255,28 | US$313,50 |
| P/E (total con dividendos) | 21,9× / 21,2× / 22,5× | 20% | 33% | US$326,35 | US$293,29 | US$354,09 |
| P/FCFE (total con dividendos) | 26,4× / 23,5× / 28,9× | 5% | 8% | US$321,79 | US$277,13 | US$360,58 |
| P/OCF (total con dividendos) | 20,6× / 17,8× / 22,5× | 5% | 8% | US$321,79 | US$281,71 | US$342,93 |
| **Ponderado de múltiplos solos a 3 años sin descontar** (total) | — | 60% | 100% | US$320,92 | US$280,77 | US$352,95 |
| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | US$25,58 | US$25,58 | US$25,58 |
| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | US$295,34 | US$255,19 | US$327,37 |
| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | US$307,67 | US$263,70 | US$341,89 |

Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ (1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias × (1 + Ke)^3: riqueza capitalizada antes de distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción existe solo en el DCF (US$75,44) y no se inventa para ellos.

Detalle del valor presente por horizonte (Ke 8,69%; consolidado por método: promedio 1-3 años):

| Método | Escenario | VP 1 año | VP 2 años | VP 3 años | Consolidado hoy | VP3 < FY+3 |
|---|---|---:|---:|---:|---:|---|
| EV/EBITDA | Base | US$281,87 | US$264,71 | US$262,13 | US$269,57 | OK |
| EV/EBITDA | Conservador | US$254,54 | US$228,53 | US$221,05 | US$234,71 | OK |
| EV/EBITDA | Optimista | US$297,97 | US$288,78 | US$291,50 | US$292,75 | OK |
| EV/FCFF | Base | US$407,85 | US$269,91 | US$221,47 | US$299,74 | OK |
| EV/FCFF | Conservador | US$383,78 | US$245,00 | US$200,50 | US$276,43 | OK |
| EV/FCFF | Optimista | US$443,05 | US$298,20 | US$245,84 | US$329,03 | OK |
| P/E | Base | US$274,40 | US$259,54 | US$255,84 | US$263,26 | OK |
| P/E | Conservador | US$262,68 | US$238,66 | US$230,10 | US$243,81 | OK |
| P/E | Optimista | US$284,31 | US$276,59 | US$277,45 | US$279,45 | OK |
| P/FCFE | Base | US$447,31 | US$221,21 | US$252,29 | US$306,94 | OK |
| P/FCFE | Conservador | US$397,77 | US$189,08 | US$217,52 | US$268,12 | OK |
| P/FCFE | Optimista | US$480,24 | US$246,23 | US$282,51 | US$336,32 | OK |
| P/OCF | Base | US$407,43 | US$294,01 | US$252,29 | US$317,91 | OK |
| P/OCF | Conservador | US$363,18 | US$256,99 | US$221,09 | US$280,42 | OK |
| P/OCF | Optimista | US$428,49 | US$312,24 | US$268,76 | US$336,50 | OK |

Lectura: los VP a 1 año de EV/FCFF, P/FCFE y P/OCF son mucho mayores que los de 2 y 3 años porque el flujo de FY+1 incluye la liberación de capital del refranquiciamiento (ver 6. «Por método»). Los métodos sobre resultados (EV/EBITDA, P/E) no tienen ese salto. Chequeo VP a 3 años < FY+3 sin descontar: OK en los tres escenarios. MOS 35% sobre el DCF esperado: US$132,57.

## 8. DCF frente a múltiplos

Los múltiplos dicen cuánto pagaría el mercado por McDonald's si se valorara como su propia historia y como sus pares franquiciadores; el DCF dice cuánto valen sus flujos con la historia Base. La brecha de +25% no viene de una diferencia de ventaja competitiva (el DCF ya le reconoce un ROIC terminal de 18,4%, el de la industria), sino de crecimiento: la historia de cinco años se formó con un BPA que crecía ~8-10% al año y recompras financiadas con deuda, y la Base supone ingresos casi planos hasta 2028 y un BPA que crece por margen, no por volumen. Los peers sin ajustar (EV/EBITDA 14,4×, P/E 17,2×) están por debajo de la historia de McDonald's y cerca de su LTM: el mercado de 2026 ya paga por McDonald's algo parecido a lo que paga por Yum! y RBI. Para esta empresa el DCF es más confiable porque captura el cambio de mezcla (refranquiciamiento) y el apoyo a franquiciados, que un múltiplo histórico no ve; los múltiplos sirven para leer cuánto de la historia de 2021-2025 sigue en el precio.

Crecimiento implícito (paso 6.5): cada múltiplo Base frente al múltiplo que implica el DCF en FY+3 (US$287,78 por acción), ambos por la misma fórmula:

| Múltiplo Base FY+3 | Múltiplo | Múltiplo que implica el DCF | Diferencia de valor | Crecimiento implícito | Crecimiento implícito del DCF | Diferencia | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| EV/EBITDA | 16,7x | 14,0x | +16% | 5,1% | 4,5% | +0,6 pp | Coherente con el DCF |
| EV/FCFF | 27,4x | 26,6x | −2% | 4,6% | 4,5% | +0,1 pp | Coherente con el DCF |
| P/E | 21,9x | 19,1x | +13% | — | — | — | Coherente en valor (sin ROE: patrimonio negativo) |
| P/FCFE | 26,4x | 23,3x | +12% | 4,7% | 4,2% | +0,5 pp | Coherente con el DCF |
| P/OCF | 20,6x | 18,3x | +12% | 4,7% | 4,2% | +0,5 pp | Coherente con el DCF |

**DCF inverso de `implied_growth.py` (corregido el 6-oct-2026).** La primera corrida informó −3,4%: el script calibraba el motor con el crecimiento del año 2 de la hoja ('Valuation output'!D4 = −4,7%, el año del refranquiciamiento) como si fuera el de los años 2-5. Desde la corrección calibra con la trayectoria real de los años 1-5 y da 2,1%, igual que el motor de historias (sección 11). El efecto en el resto de la cartera, medido sin escribir, está en `reference/revision_dcf_2026-10-06/implied_growth_calibracion.json`.

## 9. Sensibilidad

| Supuesto (DCF Base de la historia, US$224,12) | Bajo | Alto |
|---|---:|---:|
| Crecimiento años 1-5 ±2 pp | US$197,12 | US$254,15 |
| Margen objetivo ±2 pp | US$213,74 | US$234,50 |
| WACC ±1 pp | US$163,74 (+1 pp) | US$328,95 (−1 pp) |
| Crecimiento terminal ±0,5 pp | US$204,41 | US$249,94 |
| Beta: EE.UU. bottom-up (0,93) / global usada (0,79) | US$216,02 | US$224,12 |
| Ventas/capital ±20% | US$219,46 | US$227,23 |
| ROIC terminal = costo de capital (sin ventaja) | US$140,01 | — |
| Acciones +5% | US$213,45 | — |
| Múltiplos ±20% (ponderado DCF + múltiplos Base hoy, US$257,43) | US$221,90 | US$292,96 |

El valor es mucho más sensible al costo de capital y al ROIC terminal que al crecimiento o al margen: con un spread de solo 3,7 puntos entre el WACC terminal (8,99%) y el crecimiento perpetuo (5,29%), el terminal pesa 67% del valor operativo. Con un ROIC terminal igual al costo de capital (es decir, si la ventaja no durara) el DCF Base caería 38%.

## 10. Log de cambios en la hoja

Respaldo de cada celda en `reference/backups/mcd_desde_cero_2026-10-06.json` (repositorio JMR-valuation); script reproducible `scripts/run_mcd_cero.py` (pasos refresh, fix, datos, costo, supuestos, presentacion, content).

| # | Componente | Antes | Después | Motivo |
|---|---|---|---|---|
| 1 | Copia nueva de la plantilla maestra | — | «Modelo JMR - MCD (desde cero 2026-10-06)» en la carpeta MCD | Análisis desde cero con la fórmula única; la copia del 27-sep queda como referencia |
| 2 | Balance Sheet columna L | Dic-2025 | 30-jun-2026 | El importador repetía el cierre anual |
| 3 | D&A (Income Statement fila 9, Cash Flow fila 4), 2020-LTM | D&A corporativa (301-466) | D&A total (1.751-2.266) | El importador usaba DepreciationDepletionAndAmortization; EBITDA y flujos libres corregidos |
| 4 | SG&A 2018-LTM y 2020-2021 | Con D&A corporativa; 0 en 2020-2021 | Sin su D&A; 10-K 2021 para 2020-2021 | Evitar doble conteo; datos no etiquetados en XBRL |
| 5 | BPA y acciones 2023-LTM | BPA en millones y acciones en 0 | XBRL (en millones desde 2023) | Múltiplos históricos de 2023-2025 corregidos |
| 6 | Balance Sheet filas 20, 23, 26 y 27 | Deuda corriente de dic-2025 duplicada; arrendamientos operativos 2019-2022 en «Leases» | Deuda corriente dentro del LP; operativos en otros pasivos; financieros 2023 = 1.575,5 | Deuda comparable en la historia de los múltiplos EV |
| 7 | Input B17, B18, B20, B22, B24, B38-B42 | Plantilla | I+D No; arrendamientos Yes; afiliadas 0; 708,8M acciones (con RSU); 22%; 8,8M opciones a US$228,19 | 10-Q 2T26, 10-K 2025, guía 2026 |
| 8 | Operating lease converter | Datos de otra empresa | Gasto 1.631 y compromisos operativos del 10-K 2025 | Arrendamientos como deuda (Damodaran) |
| 9 | Prima madura y costo de capital | 4,09%, beta global, país de registro, rating genérico | 3,70% (octubre), «Single Business(Global)», prima por regiones, Baa1/BBB+, vencimiento 12 años | Tasas comunes de la cartera; ventas por región |
| 10 | Input B27-B33, B49/B50; Resumen G3 | Valores automáticos | Historia Base; ROIC terminal 18,4%; «Madura» | Supuestos anclados; ventaja durable |
| 11 | «Escenarios e historias» | No existía | Cuatro DCF por fórmulas | Contrato de escenarios |
| 12 | Múltiplos J8/J19/J30 | Plantilla | Tres anclas, λ = 0,25 | Pasos 6.2-6.5 |
| 13 | Input D1, B4; Resumen C25 | Precio y fecha de la corrida (14-sep) | US$230,94 al 30-sep-2026 | Fecha de corte |
| 14 | Filas 38 y 43 de «Descuento de múltiplos» | DCF de 'Valuation output' y MOS sobre el ponderado | Historias y MOS sobre el esperado | Presentación vigente |
| 15 | Textos (Cualitativo, Estadísticas, Stories to Numbers, Supuestos Recomendados, Supuestos de los Múltiplos, Tesis) | Plantilla | Contenido de MCD con fórmulas vivas | Paso 10 |
| 16 | BPA básico 2016-2022 y cambio neto de caja 2016-LTM (18 celdas) | BPA copiado del diluido; serie de relleno de la plantilla | XBRL de la SEC | `auditar_estados_sec.py` + `aplicar_cambios_celdas.py` (6-oct-2026); no cambian el DCF |

Controles: fórmula única verificada (`apply_canonical_formulas.py` en seco: 0 celdas pendientes); el motor reproduce el DCF de la hoja (US$224,12) y la pestaña «Escenarios e historias» reproduce las cuatro historias y el esperado (diferencia 0,00); el escaneo de integridad (`integridad_hojas.py`) da 0 hallazgos (la fecha de valoración fija al corte se reconoce como entrada desde el 6-oct-2026) y la consistencia de la app 16 de 16. Sin celdas con error en las pestañas de la valoración. Datos enlazados con ajuste y nota: B22 de la Input sheet (+RSU). Supuestos escritos a mano: B24, B27-B33, B49/B50, opciones, beta (enfoque), regiones, rating, J8/J19/J30.

## 11. El precio al final

Precio de referencia: **US$230,94** (cierre del 30 de septiembre de 2026, NYSE).

DCF inverso: crecimiento anual de ingresos de los años 1-5 que justifica el precio (entre paréntesis, la fracción de empresas de este tamaño que lo logró):

|  | Margen 51,5% | Margen 55,5% (Base) | Margen 58,0% |
|---|---:|---:|---:|
| Beta 0,79 (usada: bottom-up global) | 3,7% (62%) | 2,1% (71%) | 1,2% (74%) |
| Beta 0,93 (bottom-up de EE.UU.) | 4,3% (58%) | 2,7% (68%) | 1,8% (72%) |

Frente al DCF Base (US$224,12), el precio está 3% por encima; frente al esperado (US$203,96), 13% por encima; el precio con margen de seguridad (US$132,57) queda 43% por debajo del precio. Con la beta y el margen de la Base, el precio pide crecer ~2,1% anual en los años 1-5 frente al 1,0% de la Base: una historia entre la Base y la Optimista, alcanzable para ~71% de las empresas de su tamaño. ¿Qué sabe el mercado que yo no? Puede estar pagando por la estabilidad de un flujo de renta y regalías indexado a ventas, con pagos mínimos contractuales de US$31.451 millones, más de lo que la tasa del modelo reconoce, o por un ROIC terminal mayor que el promedio de la industria. En sentido contrario, la caída de ~24% de la acción en 2026 (de US$305,63 al cierre de 2025 a US$230,94) ya descuenta buena parte de la Conservadora.

## 12. Registro de decisión

| Campo | Propuesta del análisis | Tu estimación |
|---|---|---|
| Fecha | 2026-09-30 (corte); análisis del 2026-10-06 | |
| Historia en una frase | Arrendador y franquiciador de ~50.000 locales: refranquicia a 98%, las ventas del sistema crecen ~5% y el margen sube a ~52% | |
| Probabilidades | Base 50% / Conservadora 25% / Disrupción 10% / Optimista 15% | |
| DCF Base hoy | US$224,12 | |
| DCF esperado | US$203,96 | |
| Rango | US$75,44 a US$253,34 | |
| Confianza | Media-alta: el modelo de renta y regalías es estable y está documentado; el tráfico de EE.UU. y el costo real del plan NEXT no | |
| Qué cambiaría la opinión | Comparables y tráfico de EE.UU., ritmo del refranquiciamiento, amortización del apoyo de rentas | |
| Revisión | Resultados del 3T26 (fines de octubre o noviembre de 2026) | |

La decisión (comprar, mantener o vender) la registra el usuario en la app.

## 13. Fuentes

- [McDonald's, 10-Q del 2T26 (7-ago-2026)](https://www.sec.gov/Archives/edgar/data/63908/000006390826000073/mcd-20260630.htm)
- [McDonald's, 10-K 2025 (24-feb-2026)](https://www.sec.gov/Archives/edgar/data/63908/000006390826000035/mcd-20251231.htm)
- [McDonald's, comunicado del 2T26 (4-ago-2026)](https://www.sec.gov/Archives/edgar/data/63908/000006390826000067/exhibit991-6302026.htm)
- [McDonald's, información complementaria del 2T26, anexo 99.2 (4-ago-2026)](https://www.sec.gov/Archives/edgar/data/63908/000006390826000067/exhibit992-6302026.htm)
- [McDonald's, 8-K del Investor Day, anexo 99.1 (23-sep-2026)](https://www.sec.gov/Archives/edgar/data/63908/000006390826000076/exhibit991-investorupdate2.htm)
- [McDonald's, 8-K del nombramiento de Skye Anderson (4-ago-2026)](https://www.sec.gov/Archives/edgar/data/63908/000006390826000069/exhibitpressrelease.htm)
- [McDonald's, 10-K 2021 (SG&A 2020-2021)](https://www.sec.gov/Archives/edgar/data/63908/000006390822000011/mcd-20211231.htm)
- [Stock Analysis, transcripción del Investor Day (23-sep-2026)](https://stockanalysis.com/stocks/mcd/transcripts/746101-investor-day-2026/)
- [Restaurant Dive, ventas comparables de 18 cadenas (27-ago-2026)](https://www.restaurantdive.com/news/tracking-same-store-sales-18-major-restaurant-chains/742371/)
- [Restaurant Dive, tres cifras del plan NEXT (28-sep-2026)](https://www.restaurantdive.com/news/mcdonalds-next-franchisee-rent-relief-store-productivity-investment/831377/)
- [The Crypto Basic, caída de la acción y payback del plan NEXT (24-sep-2026)](https://thecryptobasic.com/2026/09/24/mcdonalds-stock-fell-4-8-amid-investor-day-cfo-puts-next-company-payback-at-5-6-years/)
- [Damodaran, ERP implícita de octubre de 2026](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPOct26.xlsx) y [betas por industria (enero de 2026)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/Betas.html)
- [Mauboussin y Callahan, The Base Rate Book (2016)](https://www.credit-suisse.com/media/assets/corporate/docs/about-us/research/publications/the-base-rate-book-integrating-the-past-to-better-anticipate-the-future.pdf)
- Peers y precios: Yahoo Finance vía yfinance, consultado el 6-oct-2026 (cierre de MCD del 30-sep-2026; peers YUM, QSR, DPZ, WEN, PZZA y CMG).

## 14. Control de calidad

| Comprobación | ¿Verificado? |
|---|---|
| Historia escrita antes de los números | Sí |
| Tasas base del tamaño reportadas | Sí |
| Orgánico frente a comprado separado (sin compras relevantes; refranquiciamiento separado) | Sí |
| Margen anclado en la guía y en comparables (Yum!, Domino's), con la brecha explicada | Sí |
| Beta bottom-up documentada (global usada, EE.UU. como sensibilidad) | Sí, con limitación: no se calculó una beta de regresión propia |
| Cuatro historias activas con probabilidades y valor esperado | Sí |
| Pre-mortem e indicadores | Sí |
| Cuadre con la SEC (ingresos, EBIT, D&A, caja, deuda, arrendamientos, acciones, opciones, RSU, minoritarios) | Sí |
| Ninguna celda con error en las pestañas de la valoración; auditoría de estados contra la SEC aplicada | Sí |
| Motor = hoja (US$224,12) y pestaña de historias = motor (esperado US$203,96) | Sí |
| Múltiplos con tres anclas, independientes del DCF; chequeo de crecimiento implícito aplicado | Sí (0 alertas) |
| Chequeo VP a 3 años < FY+3 | Sí |
| Fórmula única (0 celdas pendientes frente a la maestra) | Sí |
| Dos tablas de horizontes (presente y FY+3): métodos, múltiplos solos y DCF + múltiplos; reproducen la hoja y la app | Sí |
| El precio no aparece antes de la sección 11 (salvo la referencia de la hoja en «Datos») | Sí |
| Estado | Verificado, con salvedades: reparto de IOM por región estimado por número de locales; arrendamientos financieros al 30-jun-2026 no publicados (se usa dic-2025); la liberación de capital del refranquiciamiento en los años 1-2 depende del ventas/capital; ingresos de 2018-2019 reexpresados en la SEC (se informan, no se corrigen) |
