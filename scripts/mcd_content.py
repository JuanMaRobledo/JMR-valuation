"""Contenido cualitativo de la valoracion de McDonald's Corporation (MCD).
Las cifras de resultado de la Tesis son formulas vivas contra el modelo;
las cifras de negocio salen de los estados financieros de la hoja (SEC
EDGAR, XBRL, CIK 0000063908), del comunicado del 2T2026 (8-K, 4-ago-2026)
y del comunicado del Investor Day (8-K, Exhibit 99.1, 23-sep-2026)."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: estados financieros del modelo (SEC EDGAR, XBRL, 10-K FY2025 y 10-Q 2T2026 de McDonald's Corp, "
    "CIK 0000063908); comunicado de resultados del 2T2026 (8-K, 4-ago-2026); comunicado 'McDonald's advances "
    "NEXT strategy' del Investor Day (8-K, Exhibit 99.1, 23-sep-2026) y transcripción del Investor Day; "
    "comunicado de resultados del 4T2025 (guía 2026); Moody's (Baa1, jul-2025) y S&P (BBB+, abr-2025); "
    "Damodaran Online (industria 'Restaurant/Dining'; ERP de mercado maduro 1-sep-2026); UST 10 años y precio "
    "de MCD vía yfinance (cierre del 25-sep-2026). Las estimaciones de analistas (BMO, Evercore, consenso de "
    "precio objetivo) se citan de prensa financiera y no se usan como supuesto del modelo."
)

CUALITATIVO = {
    "B5": "McDonald's Corporation",
    "B6": "Chris Kempczinski — Presidente del Directorio y CEO (CEO desde nov-2019). CFO: Ian Borden.",
    "B7": "Restaurantes de servicio rápido — franquiciador global (Damodaran: Restaurant/Dining)",
    "B8": "https://corporate.mcdonalds.com  |  IR: https://investor.mcdonalds.com",
    "B11": "Descripción",
    "B12": ("McDonald's es la mayor cadena de restaurantes del mundo: más de 46.000 locales en más de 100 países, "
            "~95% operados por franquiciados independientes. Su negocio real es inmobiliario y de marca: es dueña o "
            "arrendataria de largo plazo del terreno y el local, y cobra al franquiciado renta y regalías como "
            "porcentaje de sus ventas. Ingresos 2025: US$26.885M (US$16.548M de ingresos por franquicias y "
            "US$9.690M de ventas de locales propios); LTM a jun-2026: US$27.702M con margen operativo de 46,2%. "
            "Ventas del sistema del 2T2026: US$37.000M en el trimestre."),
    "A13": "Estados Unidos",
    "B13": ("El mercado más grande y el más rentable (US$7.371M de ingresos por franquicias en 2025). Es también "
            "el foco del problema actual: ventas comparables de solo +0,8% en el 2T2026, con menos tráfico de "
            "clientes de bajos ingresos, presión de precios de la competencia y una estrategia de valor "
            "(McValue) que no logró recuperar visitas."),
    "A14": "Mercados Internacionales Operados (IOM)",
    "B14": ("Reino Unido, Alemania, Francia, Canadá, Australia, Japón y otros mercados donde McDonald's opera o "
            "franquicia directamente (US$7.279M de ingresos por franquicias en 2025). Comparables +1,5% en el "
            "2T2026. Aquí se concentra la mayoría de los locales propios que se van a refranquiciar."),
    "A15": "Mercados de Licencia para el Desarrollo (IDL)",
    "B15": ("China, Medio Oriente, Latinoamérica (Arcos Dorados) y otros, operados por licenciatarios que ponen "
            "el capital y pagan regalías (US$1.898M de ingresos en 2025). Comparables +1,9% en el 2T2026. Es el "
            "motor de nuevas aperturas con poca inversión propia."),
    "A16": "Estrategia: McDonald's > NEXT (Investor Day 23-sep-2026)",
    "B16": ("Cuatro pilares (Menu, Consumer, Restaurant y People > NEXT): ganar 1,5pp de cuota en pollo y "
            "bebidas a 2030, ~250pb de eficiencia a nivel restaurante (~US$100.000 de caja anual por local en "
            "EE.UU.), subir la mezcla franquiciada de ~95% a ~98% a fines de 2028 y llevar el margen operativo "
            "ajustado a 'low-to-mid 50%' en 2030. Lo financia con ~US$8.500M de apoyo a franquiciados hasta 2036 "
            "(~US$5.000M a 2030) en rebajas de renta y capital."),
    "B21": "Argumento",
    "A22": "Modelo de franquicia + inmueble propio",
    "B22": ("McDonald's cobra renta y regalías sobre las ventas del sistema, no sobre su propia operación: margen "
            "operativo de 46,2% (LTM) y flujo de caja libre de US$7.761M con un capex de US$3.586M. El inmueble "
            "le da control sobre la ubicación y un flujo parecido al de un REIT con reajuste por inflación."),
    "A23": "Escala y datos imposibles de replicar",
    "B23": ("Más de 70 millones de clientes al día, 17 productos que venden más de US$1.000M cada uno y cerca "
            "de 220 millones de miembros activos de su programa de lealtad en 70 mercados. Esa escala abarata "
            "compras, publicidad y tecnología frente a cualquier competidor."),
    "A24": "Palancas propias para crecer el margen",
    "B24": ("Refranquiciar (98% a fines de 2028), bajar el G&A de 2,2% a ~1,9% de las ventas del sistema en 2030 "
            "con IA (ArchIQ) y 2.100 aperturas netas previstas en 2026: el margen puede subir aunque las ventas "
            "comparables crezcan poco. Dividendo creciente 50 años seguidos, con payout objetivo de 50-60%."),
    "B27": "Riesgo",
    "A28": "Tráfico débil en EE.UU. y consumidor de menores ingresos",
    "B28": ("Las comparables globales bajaron de +3,8% en el 1T2026 a +1,3% en el 2T2026 (EE.UU. +0,8%). La "
            "gerencia advirtió que el tráfico puede quedar plano si la inflación sigue alta. A esto se suman la "
            "guerra de precios del sector y el efecto de los fármacos GLP-1 en la frecuencia de visita."),
    "A29": "Costo del apoyo a franquiciados",
    "B29": ("US$8.500M de rebajas de renta y capital hasta 2036 (US$5.000M a 2030). Se amortiza en ~10 años "
            "(plazo restante de cada contrato), así que el golpe al resultado es gradual, pero BMO estima una "
            "baja del EPS de ~1% en 2027-28 y de 2-3% en 2030, y el capex sube US$600-900M por año en 2027-28."),
    "A30": "Apalancamiento y patrimonio negativo",
    "B30": ("Deuda financiera de US$43.027M (incluye arrendamientos financieros) contra caja de US$822M, más "
            "~US$14.700M de pasivos por arrendamientos operativos; patrimonio contable negativo (US$-1.791M) por "
            "décadas de recompras financiadas con deuda. Deuda neta/EBITDA de 2,8x (sin arrendamientos "
            "operativos), en la zona de cautela de la metodología."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": "N/D",
    "B12": "='Income Statement'!L30", "B13": "='Income Statement'!L13",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "N/D (patrimonio negativo)", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "N/D (patrimonio negativo)", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12",
    "E13": "=PE!F19", "E14": "=E4/('Input sheet'!B29*100)",
    "E16": "=IFERROR('Trailing Valuation'!L6/'Financials Multiples'!E57;\"\")",
    "E20": "='Balance Sheet'!L5", "E23": "='Income Statement'!L12/'Income Statement'!L16",
    "H4": "=IFERROR(('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1;\"\")",
    "H5": "=IFERROR(('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1;\"\")",
    "H6": "=IFERROR(('Income Statement'!K3/'Income Statement'!B3)^(1/9)-1;\"\")",
    "H7": "=IFERROR(('Income Statement'!K24/'Income Statement'!H24)^(1/3)-1;\"\")",
    "H8": "=IFERROR(('Income Statement'!K24/'Income Statement'!F24)^(1/5)-1;\"\")",
    "H9": "=IFERROR(('Income Statement'!K24/'Income Statement'!B24)^(1/9)-1;\"\")",
    "H10": "=IFERROR(('Cash Flow Statement'!K36/'Cash Flow Statement'!F36)^(1/5)-1;\"\")",
    "H11": "=IFERROR(('Income Statement'!K26/'Income Statement'!F26)^(1/5)-1;\"\")",
    "H12": "N/D (sin guía de ingresos; el refranquiciamiento 2027-28 baja los ingresos contables)",
    "H13": "N/D (sin guía de EBITDA)",
    "H14": "N/D (sin guía de EPS; BMO estima -1% de EPS en 2027-28 por el apoyo a franquiciados)",
    "H15": "N/D (sin guía de EPS de largo plazo)",
    "H18": "='Trailing Valuation'!L7",
    "H19": "=-'Cash Flow Statement'!L32/'Income Statement'!L22",
    "H20": "=-'Cash Flow Statement'!L32/'Income Statement'!L26",
    "H21": "=IFERROR(((-'Cash Flow Statement'!K32/'Income Statement'!K26)/(-'Cash Flow Statement'!H32/'Income Statement'!H26))^(1/3)-1;\"\")",
    "H22": "=IFERROR(((-'Cash Flow Statement'!K32/'Income Statement'!K26)/(-'Cash Flow Statement'!F32/'Income Statement'!F26))^(1/5)-1;\"\")",
    "H23": "=IFERROR(((-'Cash Flow Statement'!K32/'Income Statement'!K26)/(-'Cash Flow Statement'!B32/'Income Statement'!B26))^(1/9)-1;\"\")",
    "H24": "N/D (payout objetivo 50-60% del EPS, Investor Day)",
}

STORIES = {
    "A3": "McDonald's: un dueño de inmuebles y marca que sacrifica crecimiento contable de corto plazo para recuperar tráfico y subir el margen a 2030",
    "A4": ("McDonald's genera US$27.702M de ingresos LTM con un margen operativo de 46,2% porque cobra renta y "
           "regalías sobre ~US$140.000M de ventas del sistema. La acción cayó de US$305,63 (cierre 2025) a "
           "US$236,50 por tráfico débil en EE.UU. (comparables +0,8% en el 2T2026) y por el costo del plan NEXT "
           "anunciado en el Investor Day del 23-sep-2026: US$8.500M de apoyo a franquiciados hasta 2036. La "
           "historia Base: los ingresos contables caen en 2027-28 porque refranquicia el ~60% de sus locales "
           "propios (95% a 98% de mezcla franquiciada), el margen sube a 53% (algo por debajo del rango "
           "'low-to-mid 50%' que guió la empresa, por la amortización del apoyo) y el EBIT crece ~4% anual, en "
           "línea con ventas del sistema de +4-5% (unidades ~2,5% + comparables bajas)."),
    "G10": "Año 1 Base -2%: ventas del sistema +4-5% menos la baja contable del refranquiciamiento (ventas de locales propios que pasan a renta + regalías). Años 2-5 +2%: 2028 todavía refranquicia, 2029-30 ~+4,5%.",
    "G11": "Margen Año 1 47,5% (LTM 46,2%, guía 2026 'mid-to-high 40%') que converge a 53% en 5 años: mezcla 98% franquiciada + G&A de 2,2% a 1,9% de las ventas del sistema, menos la amortización del apoyo a franquiciados.",
    "G12": "Tasa efectiva LTM 21,4% que converge a la marginal de 25% (EE.UU. federal + estatal, convención de Damodaran).",
    "G13": "1,0x (años 1-5): capex ~US$3.000M/año + US$1.500-2.000M de apoyo NEXT frente a D&A ~US$2.300M. 1,2x (años 6-10): termina el capex extraordinario.",
    "G14": "ROIC ~25% hoy (NOPAT US$10.060M). Perpetuidad con ROIC de 12%: el moat de marca e inmueble se desvanece a la mitad, pero sigue por encima del costo de capital.",
    "G15": "WACC 7,9%: beta desapalancada global de Restaurant/Dining (0,66) reapalancada, ERP maduro 4,09%, UST 5,18%, deuda Baa1/BBB+. WACC terminal 8,25% (no rf + ERP = 9,27%: MCD ya es una empresa madura de bajo riesgo).",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": -0.02, "D6": "Ventas del sistema +4-5% (unidades ~2,5% + comparables ~1,5-2%) menos la baja contable del refranquiciamiento de 95% a 98% a fines de 2028.",
    "C7": 0.475, "D7": "LTM 46,2%; guía 2026 'mid-to-high 40%'; el G&A empieza a bajar en 2027 (Investor Day).",
    "C8": 0.02, "D8": "2028 todavía refranquicia (~-4%); 2029-2030 vuelve a ~+4,5% (unidades + comparables).",
    "C9": 0.53, "D9": "Rango 'low-to-mid 50%' a 2030 (Investor Day), menos la amortización del apoyo a franquiciados (~10 años por contrato).",
    "C10": 5, "D10": "La meta de margen es a 2030.",
    "C11": 1.0, "D11": "Capex ~US$3.000M/año + US$1.500-2.000M de apoyo NEXT 2027-2030 frente a D&A de ~US$2.300M.",
    "C12": 1.2, "D12": "Termina el capex extraordinario de NEXT; el crecimiento vuelve a venir de aperturas financiadas en parte por licenciatarios.",
}

MULTIPLOS_EVALUACION = (
    "Evaluación MCD: los 4 últimos cierres (2022-2025) dieron múltiplos positivos, pero la regla nativa (mínimo "
    "positivo de 4 cierres) fijaba el Base en P/E 25,5x y EV/EBITDA 17,9x, muy por encima de lo que el mercado "
    "paga hoy (P/E LTM 19,2x; EV/EBITDA LTM 13,9x) y de la mediana de los peers (YUM, QSR, DPZ, CMG, WEN, SBUX: "
    "P/E ~18x, EV/EBITDA ~15x). Usarla suponía que la acción vuelve a los múltiplos de 2022-2025, justo cuando "
    "el crecimiento de tráfico se frenó y el plan NEXT recorta el EPS de 2027-2030. Por eso se fijó a mano "
    "(J19 de cada hoja) la regla de la Calculadora del Paso 5: Base = 0,78 × mediana de los 4 cierres (misma "
    "definición de cada hoja): P/E 20,0x, EV/EBITDA 14,2x, EV/FCFF 24,6x, P/FCFE 20,0x, P/OCF 16,7x, cerca de "
    "los múltiplos actuales. Conservador y Optimista quedan en ×0,9 y ×1,1. Con la regla nativa el precio "
    "objetivo ponderado Base sería ~20% más alto."
)

VO, INP, COC, RES = "'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'"

TESIS_ROWS: list[list] = [
    ["MCD (McDonald's Corporation) — Tesis de Inversión: De la Historia a los Números"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al día del análisis: US$"&TEXT({RES}!C25;"0.00")&" | WACC: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["McDonald's es, en el fondo, un dueño de inmuebles y de una marca global que cobra renta y regalías sobre "
     "~US$140.000M de ventas del sistema. La acción cayó ~23% en 2026 (de US$305,63 a US$236,50) porque el "
     "tráfico se frenó (comparables globales de +3,8% en el 1T a +1,3% en el 2T2026; EE.UU. +0,8%) y porque el "
     "Investor Day del 23-sep-2026 puso precio a la recuperación: US$8.500M de apoyo a franquiciados hasta 2036. "
     "La tensión de la tesis: la empresa cambia EPS de corto plazo (rebajas de renta, más capex, refranquiciar el "
     "~60% de sus locales propios) por un sistema más sano y un margen operativo de 'low-to-mid 50%' en 2030. Si "
     "el tráfico vuelve, el EBIT crece ~4-5% anual con un negocio de muy bajo riesgo; si no, el mercado pagará "
     "menos que los ~25x de utilidad que pagó entre 2022 y 2025."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["Modelo de franquicia + inmueble: margen operativo LTM 46,2% y flujo de caja libre de US$7.761M; 50 años "
     "seguidos subiendo el dividendo, con payout objetivo de 50-60%.",
     "Tráfico débil: comparables de EE.UU. de solo +0,8% en el 2T2026 y la gerencia advierte que el tráfico puede "
     "quedar plano si la inflación sigue alta; competencia de precios y fármacos GLP-1."],
    ["Palancas propias de margen: mezcla franquiciada de 95% a 98% a fines de 2028 y G&A de 2,2% a ~1,9% de las "
     "ventas del sistema en 2030; meta de margen 'low-to-mid 50%' (Investor Day).",
     "Costo de NEXT: US$5.000M de apoyo a franquiciados a 2030 (US$8.500M a 2036) y capex US$600-900M más alto "
     "por año en 2027-28; BMO estima -1% de EPS en 2027-28 y -2/3% en 2030."],
    ["Crecimiento de unidades con poco capital: ~2.100 aperturas netas en 2026 y ~2,5% de aporte de nuevas "
     "unidades a las ventas del sistema en 2027, buena parte financiada por licenciatarios (IDL).",
     "Deuda financiera de US$43.027M (2,8x deuda neta/EBITDA) más ~US$14.700M de arrendamientos operativos y "
     "patrimonio contable negativo: poco margen para recompras mientras dure NEXT."],
    ["Valoración ya comprimida: P/E LTM 19,2x y EV/EBITDA 13,9x contra una mediana de 10 años de ~25,6x y ~18,2x; "
     "rendimiento por dividendo de 3,1%.",
     "Los ingresos contables caen en 2027-28 por el refranquiciamiento: los múltiplos sobre ventas y el "
     "crecimiento reportado se verán débiles aunque el EBIT aguante."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — LOS TRES ESCENARIOS (fórmulas vivas del modelo)"],
    ["Supuesto", "Conservador", "Base", "Optimista", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={INP}!B27", f"={VO}!C106",
     "Base -2%: ventas del sistema +4-5% menos la baja contable del refranquiciamiento (de 95% a 98% a fines de "
     "2028; las ventas de locales propios, US$9.690M en 2025, pasan a renta + regalías). Conservador -3,5%: el "
     "tráfico no se recupera. Optimista -1%: comparables se recuperan y el refranquiciamiento es más lento."],
    ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={INP}!B29", f"={VO}!D106",
     "Base 2%: 2028 todavía refranquicia (~-4%); 2029-2030 ~+4,5% (unidades ~2-2,5% + comparables). Conservador "
     "0,5% y Optimista 3% (±1,5pp/+1pp por tramo: la regla MIN(Año 1; 2-5) de la plantilla hubiera aplicado el "
     "-3,5% del Año 1 a los 5 años)."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "47,5%: LTM 46,2% ('Valuation output'!B6) y guía 2026 'mid-to-high 40%'; el G&A empieza a bajar en 2027."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 53%: rango 'low-to-mid 50%' a 2030 menos la amortización del apoyo a franquiciados. Conservador 47,5%: "
     "solo el efecto mezcla del refranquiciamiento, sin eficiencias. Optimista 56%: se cumplen los ~250pb de "
     "eficiencia y el tope del rango guiado."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31",
     "5 años: la meta de margen de la empresa es a 2030."],
    ["Sales-to-Capital (años 1-5 / 6-10)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "1,0x (años 1-5): capex ~US$3.000M/año + US$1.500-2.000M de apoyo NEXT 2027-30 contra D&A ~US$2.300M. 1,2x "
     "(años 6-10): termina el capex extraordinario."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "Beta desapalancada global Restaurant/Dining 0,66 reapalancada con D/E de mercado; UST 10 años 5,18% "
     "(25-sep-2026); ERP maduro 4,09% (Damodaran, 1-sep-2026); deuda Baa1/BBB+ (rating real). Perpetuidad: WACC "
     "8,25% (en vez de rf + ERP = 9,27%) y ROIC 12% (en vez de ROIC = WACC), ver log."],
    ["Referencia: margen base (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "Margen operativo GAAP LTM: US$12.805M sobre ingresos de US$27.702M (46,2%)."],
    [],
    ["3. RESULTADO DEL DCF POR ESCENARIO"],
    ["Escenario", "Valor DCF / acción", "Precio Objetivo Ponderado*", "DCF vs. precio del análisis", "Ponderado vs. precio del análisis"],
    ["Conservador", f"={VO}!B86", f"={RES}!C12", f"=B26/{RES}!$C$25-1", f"=C26/{RES}!$C$25-1"],
    ["Base", f"={VO}!B35", f"={RES}!D12", f"=B27/{RES}!$C$25-1", f"=C27/{RES}!$C$25-1"],
    ["Optimista", f"={VO}!B137", f"={RES}!E12", f"=B28/{RES}!$C$25-1", f"=C28/{RES}!$C$25-1"],
    ["Precio del análisis (cierre 25-sep-2026)", f"={RES}!C25"],
    [f'=IF(AND(B26<B27;B27<B28;C26<C27;C27<C28;{VO}!C55<{INP}!B27;{INP}!B27<{VO}!C106;{VO}!C45<{VO}!C46;{VO}!C46<{VO}!C47);"✔ Orden verificado: Conservador < Base < Optimista en crecimiento, margen objetivo, valor DCF y precio ponderado";"✖ REVISAR: el orden Conservador < Base < Optimista no se cumple")'],
    ["*El Precio Objetivo Ponderado es a 3 años: DCF llevado a 3 años con el costo del equity (30%) y 5 múltiplos "
     "a FY+3 más dividendos (P/E 25%, EV/EBITDA 20%, EV/FCFF 10%, P/FCFE 10%, P/OCF 5%), categoría 'Defensiva'. "
     "El valor DCF de la columna B es el valor intrínseco de hoy."],
    [],
    ["4. CONCLUSIÓN"],
    [f'="A US$"&TEXT({RES}!C25;"0.00")&", McDonald\'s cotiza "&IF({VO}!B35>{RES}!C25;"por DEBAJO";"por ENCIMA")&" de su DCF Base (US$"&TEXT({VO}!B35;"0.00")&", "&TEXT({VO}!B35/{RES}!C25-1;"+0%;-0%")&") y "&IF({RES}!D12>{RES}!C25;"por DEBAJO";"por ENCIMA")&" del precio objetivo ponderado Base a 3 años (US$"&TEXT({RES}!D12;"0.00")&", CAGR "&TEXT({RES}!D13;"0.0%")&" con dividendos). El precio ya descuenta un tráfico débil y el costo de NEXT: el retorno esperado viene del dividendo (~3%) y de un EBIT que crece ~4% anual, no de volver a los múltiplos de 2022-2025. No es una ganga en términos absolutos, pero es la valoración más baja en años para un negocio de muy bajo riesgo."'],
    ["Variable clave a monitorear: las ventas comparables y el tráfico de clientes en EE.UU. trimestre a trimestre "
     "(¿vuelven a +3% o más?) y el margen operativo ajustado frente a la senda 'low-to-mid 50%' a 2030, "
     "incluida la amortización del apoyo a franquiciados."],
    [],
    ["5. LOG DE CORRECCIONES (antes → después; respaldo en JMR-valuation/reference/backups/mcd_formula_backup.json)"],
    ["Datos SEC: D&A 2020-LTM tomaba DepreciationDepletionAndAmortization (US$301-466M, partida parcial) → "
     "DepreciationAndAmortization del flujo de caja (US$1.751-2.266M). EBITDA LTM de US$13.271M → US$15.071M."],
    ["Datos SEC: desde 2023 MCD reporta las acciones promedio en millones (732,3); el loader las dejaba en 0 y el "
     "EPS 2023-LTM salía en millones (11.564.659) → acciones reescaladas; EPS diluido 2025 US$11,95 (10-K) y "
     "múltiplos P/E/EV 2023-2025 corregidos (P/E 2025 de 0,0x → 25,6x)."],
    ["Precio del análisis ('Resumen de Valoración'!C25): el refresh lo pisaba con un valor fijo → se restauró la fórmula =$B$3 de la "
     "plantilla vigente (cierre histórico de 'Input sheet'!B4 vía GOOGLEFINANCE)."],
    ["Escenarios: C55/D55 = MIN(B27;B29)-1,5pp → B27-1,5pp y B29-1,5pp; C106/D106 = MAX(...)+1pp → +1pp por "
     "tramo; C45 = margen Año 0 → margen Año 1 (el refranquiciamiento sube el margen por mezcla); C47 = Base+5pp → "
     "Base+3pp (tope del rango guiado)."],
    ["Múltiplos: J19 (Base) = mínimo positivo de 4 cierres → 0,78 × mediana de 4 cierres en las 5 hojas (ver "
     "'Supuestos de los Múltiplos')."],
    ["Perpetuidad: WACC terminal rf + ERP (9,27%) → 8,25%; ROIC terminal = WACC → 12%. Con los valores por "
     "defecto de la plantilla, el DCF Base era US$147,38 por acción (hoy US$225,92)."],
    ["I+D: 'Input sheet'!B17 Yes → No (MCD no reporta I+D). Tipo de empresa Genérico → Defensiva. MOS 35% → 25% "
     "(hipótesis Estándar: moat claro, deuda investment grade)."],
    [],
    [SOURCES],
]

LOG_ROWS = range(37, 44)  # indices 0-based de las filas del log (texto literal)


def format_estadisticas(sh) -> None:
    est = sh.worksheet("Estadísticas")
    pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
    num = {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}
    mult = {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}
    cur = {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}
    est.batch_format([
        {"range": "B4:B8", "format": num}, {"range": "B11:B16", "format": pct}, {"range": "B19:B23", "format": pct},
        {"range": "E4:E9", "format": mult}, {"range": "E13:E17", "format": mult}, {"range": "E12", "format": cur},
        {"range": "E20:E21", "format": num}, {"range": "E22:E23", "format": mult},
        {"range": "H4:H15", "format": pct}, {"range": "H18:H19", "format": pct}, {"range": "H20", "format": cur},
        {"range": "H21:H23", "format": pct},
    ])


def write_tesis(sh, backup_path) -> None:
    pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
    ms.write_tesis(
        sh, TESIS_ROWS, backup_path, text_rows=LOG_ROWS,
        merges=[f"A{r}:E{r}" for r in (1, 2, 5, 13, 24, 31, 33, 34, 35, *range(37, 45), 46)]
        + [f"B{r}:E{r}" for r in range(7, 12)],
        bold_rows=(4, 13, 24, 33, 37), head_rows=(7, 14, 25),
        formats=[
            {"range": "B15:D18", "format": pct}, {"range": "B22:D22", "format": pct},
            {"range": "B19:D19", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0"}}},
            {"range": "B20:D20", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}},
            {"range": "B21:D21", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0.00%"}}},
            {"range": "B26:C28", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
            {"range": "B29", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
            {"range": "D26:E28", "format": {"numberFormat": {"type": "PERCENT", "pattern": "+0.0%;-0.0%"}}},
        ])
