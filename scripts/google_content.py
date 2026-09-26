"""Contenido cualitativo de la valoracion de Alphabet Inc., clase C sin
voto (GOOG). Las cifras de resultado de la Tesis son formulas vivas
contra el modelo; las cifras de negocio citadas en el texto salen de los
propios estados financieros de la hoja (SEC EDGAR, CIK 0001652044), no
de memoria, salvo los hechos generales marcados como tales (segmentos,
CEO, estructura accionaria, litigios antimonopolio)."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: estados financieros del modelo (SEC EDGAR, XBRL, 10-K y 10-Q de Alphabet Inc., "
    "CIK 0001652044); Damodaran Online (indname.xls, industria 'Software (Internet)'; ERPbymonth; "
    "Country equity risk premiums); UST 10 años y precio de GOOG vía yfinance (fecha del análisis). "
    "No se citan titulares de prensa de trimestres específicos por no tener una fuente verificada al "
    "momento de escribir esta hoja -- actualizar en la próxima revisión con los datos del trimestre "
    "más reciente."
)

CUALITATIVO = {
    "B5": "Alphabet Inc.",
    "B6": "Sundar Pichai (CEO de Alphabet y Google desde 2015/2019). Presidente: John Hennessy.",
    "B7": "Software / Internet — publicidad digital, nube y otras apuestas (Damodaran: Software (Internet))",
    "B8": "https://abc.xyz  |  IR: https://abc.xyz/investor",
    "B11": "Descripción",
    "B12": ("Alphabet es la matriz de Google. Reporta en tres segmentos: Google Services (Búsqueda, YouTube "
            "ads, Google Network, Play, dispositivos y suscripciones), Google Cloud (infraestructura, "
            "plataforma de datos e IA para empresas) y Other Bets (Waymo, Verily y otras apuestas de etapa "
            "temprana). Ingresos LTM de US$445.866M con un margen operativo de 33,1%."),
    "A13": "Google Services (Search, YouTube, Network, Play, dispositivos)",
    "B13": ("El negocio principal: la publicidad de Búsqueda y YouTube financia casi todo el resto del grupo. "
            "Genera la enorme mayoría del EBIT consolidado; su moat es la escala de datos y distribución "
            "(acuerdos con fabricantes de dispositivos y navegadores) que sostiene su participación en "
            "búsqueda, además de los efectos de red de YouTube como la plataforma de video más grande."),
    "A14": "Google Cloud",
    "B14": ("El segmento de mayor crecimiento: infraestructura (Compute, Storage), plataforma de datos y, cada "
            "vez más, servicios de IA generativa (modelos Gemini, Vertex AI) para empresas. Compite "
            "directamente con AWS y Azure; a diferencia de esos dos rivales, llegó más tarde a la escala "
            "rentable, pero ya aporta una porción relevante y creciente del EBIT del grupo."),
    "A15": "Other Bets",
    "B15": ("Apuestas de etapa temprana fuera del negocio central, la más conocida Waymo (conducción autónoma). "
            "Consumen capital sin ingresos materiales todavía; son opcionalidad de largo plazo, no un "
            "impulsor de la valoración de corto/mediano plazo del modelo."),
    "A16": "Estructura accionaria (3 clases)",
    "B16": ("Alphabet cotiza en tres clases: A (GOOGL, 1 voto), B (10 votos, en manos de los fundadores e "
            "insiders, no cotiza) y C (GOOG, sin voto, ticker de esta valoración). Las tres clases tienen "
            "los MISMOS derechos económicos (utilidad y dividendo por acción idénticos): el valor por acción "
            "del DCF y de los múltiplos aplica igual a las tres; la única diferencia de precio entre A y C en "
            "el mercado es la prima/descuento por el voto, no por el negocio."),
    "B21": "Argumento",
    "A22": "Cloud como segundo motor de crecimiento",
    "B22": ("Google Cloud pasó de ser una apuesta deficitaria a un negocio con escala rentable, compitiendo de "
            "igual a igual con AWS y Azure en la ola de infraestructura de IA generativa (Gemini, TPUs propios, "
            "Vertex AI). Es la principal fuente de crecimiento incremental fuera de la publicidad."),
    "A23": "Balance excepcional y recompras",
    "B23": (f"Caja e inversiones de US$55.911M contra una deuda financiera de US$61.287M (deuda neta prácticamente "
            "nula, calificación real Aa2/AA): financia el capex de IA casi sin apalancamiento. Recompra acciones "
            "de forma sostenida (el conteo combinado de las 3 clases bajó de acciones más viejas) y paga dividendo "
            "desde 2024 (payout todavía bajo, ~4-8% de la utilidad)."),
    "A24": "TPUs propios (ventaja de costo en IA)",
    "B24": ("A diferencia de la mayoría de sus competidores, que dependen casi enteramente de GPUs de Nvidia, "
            "Alphabet diseña sus propios aceleradores de IA (TPU) para entrenar e inferir sus modelos Gemini, lo "
            "que le da una ventaja de costo estructural en la carrera de infraestructura de IA."),
    "B27": "Riesgo",
    "A28": "Capex de IA presiona el flujo de caja libre",
    "B28": ("El capex (centros de datos, TPUs, redes) creció mucho más rápido que los ingresos en los últimos "
            "años, comprimiendo el FCFF y el FCFE reportados (ver 'Supuestos de los Múltiplos' para el detalle "
            "del impacto en el múltiplo EV/FCFF). El caso de inversión depende de que ese capex empiece a "
            "traducirse en ingresos de Cloud e IA antes de que el mercado pierda paciencia."),
    "A29": "Riesgo antimonopolio (EE.UU. y UE)",
    "B29": ("Alphabet enfrenta litigios antimonopolio en EE.UU. sobre distribución de Búsqueda (acuerdos de "
            "posición por defecto con fabricantes de dispositivos y navegadores) y sobre su negocio de "
            "tecnología publicitaria (ad-tech), además de escrutinio regulatorio en la Unión Europea (Digital "
            "Markets Act). Un remedio estructural (separar activos, prohibir ciertos acuerdos de distribución) "
            "es el riesgo de cola más citado sobre la tesis."),
    "A30": "Competencia en IA generativa",
    "B30": ("OpenAI/Microsoft, Anthropic y otros compiten directamente por la sustitución de la búsqueda "
            "tradicional con asistentes de IA generativa. Alphabet responde integrando IA (AI Overviews, modo IA) "
            "dentro de Búsqueda, pero el riesgo de que un cambio de hábito de los usuarios erosione el modelo de "
            "negocio publicitario central sigue siendo el argumento bajista de más largo plazo."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 190000,  # empleados a tiempo completo (10-K mas reciente)
    "B12": "='Income Statement'!L30", "B13": "='Income Statement'!L13",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "='Eficiencia de capital'!L5", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12",
    "E13": "=PE!F19", "E14": "=E4/('Input sheet'!B29*100)",
    "E16": "=IFERROR('Trailing Valuation'!L6/'Financials Multiples'!E57;\"\")",
    "E20": "='Balance Sheet'!L5", "E23": "='Income Statement'!L12/'Income Statement'!L16",
    "H4": "=IF('Income Statement'!H3<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1;\"\"))",
    "H5": "=IF('Income Statement'!F3<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1;\"\"))",
    "H6": "=IF('Income Statement'!B3<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K3/'Income Statement'!B3)^(1/9)-1;\"\"))",
    "H7": "=IF('Income Statement'!H24<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K24/'Income Statement'!H24)^(1/3)-1;\"\"))",
    "H8": "=IF('Income Statement'!F24<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K24/'Income Statement'!F24)^(1/5)-1;\"\"))",
    "H9": "=IF('Income Statement'!B24<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K24/'Income Statement'!B24)^(1/9)-1;\"\"))",
    "H10": "=IF('Cash Flow Statement'!F36<0;\"N/A (base negativa)\";IFERROR(('Cash Flow Statement'!K36/'Cash Flow Statement'!F36)^(1/5)-1;\"\"))",
    "H11": "=IF('Income Statement'!F26<0;\"N/A (base negativa)\";IFERROR(('Income Statement'!K26/'Income Statement'!F26)^(1/5)-1;\"\"))",
    "H12": "N/D (guía externa; sin dato verificado para esta empresa)",
    "H13": "N/D (guía externa; sin dato verificado para esta empresa)",
    "H14": "N/D (guía externa; sin dato verificado para esta empresa)",
    "H15": "N/D (guía externa; sin dato verificado para esta empresa)",
    "H18": "=IFERROR(Dividendos!L4/'Input sheet'!D1;\"\")", "H19": "=Dividendos!L5", "H20": "=Dividendos!L4",
    "H21": "=IFERROR(MIN(MAX((Dividendos!$K$4/Dividendos!$J$4)^(1/1)-1;0);2);\"N/D (2 años de historia)\")",
    "H22": "N/D (menos de 5 años de historia de dividendo)", "H23": "N/D (menos de 10 años de historia de dividendo)",
}

STORIES = {
    "A3": "Alphabet: el negocio publicitario más rentable del mundo, financiando una carrera de infraestructura de IA sin apalancarse",
    "A4": ("Alphabet genera US$445.866M de ingresos LTM con un margen operativo de 33,1%, casi sin deuda "
           "financiera neta. El negocio central (Búsqueda + YouTube) sostiene un capex de IA que creció mucho "
           "más rápido que los ingresos, comprimiendo el flujo de caja libre reportado en los últimos ejercicios "
           "(ver 'Supuestos de los Múltiplos'). La tesis Base asume que ese capex se traduce gradualmente en "
           "crecimiento de Cloud e IA (11% el Año 1, convergiendo a 7%) con una expansión de margen moderada "
           "(32,5% a 33,5%), sin apostar a que la operación de la nube alcance la escala rentable de forma "
           "acelerada. Riesgo antimonopolio en EE.UU. y UE, y la sustitución de la búsqueda tradicional por "
           "asistentes de IA generativa, son los dos riesgos estructurales de más largo plazo."),
    "G10": "Año 1 en línea con el crecimiento LTM real (10,7%); años 2-5 convergen hacia el crecimiento nominal de EE.UU. más una prima de Cloud/IA.",
    "G11": "Margen Año 1 apenas por debajo del LTM real (33,1%) por la presión de depreciación del capex de IA; converge a una expansión moderada, no al 36% que sale del promedio histórico (incluye años de menor inversión).",
    "G12": "Tasa marginal de largo plazo 16%: corporativa de EE.UU. (21%) neta de la tasa efectiva real más baja por ingresos en el exterior.",
    "G13": "2,5x: negocio de software/servicios, requiere relativamente poco capital nuevo por dólar de ingreso incremental frente a un negocio intensivo en activos físicos.",
    "G14": "ROIC muy por encima del costo de capital: el negocio de Búsqueda/YouTube genera retornos excepcionales sobre el capital operativo.",
    "G15": "9,6%: beta observado ~1,05 (Directo, no la canasta de industria 'Software (Internet)' de Damodaran, dominada por empresas mucho más chicas y de un solo producto) x ERP de mercado maduro de EE.UU., calificación real Aa2/AA, deuda financiera neta casi nula.",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": 0.11, "D6": "En línea con el crecimiento LTM real (10,7%): Búsqueda y YouTube maduros, Cloud como motor incremental.",
    "C7": 0.325, "D7": "Levemente por debajo del EBIT LTM real (33,1%) por la depreciación creciente del capex de IA.",
    "C8": 0.07, "D8": "Converge hacia el crecimiento nominal de EE.UU. más una prima moderada de Cloud/IA.",
    "C9": 0.335, "D9": "Expansión moderada sobre el margen Año 1, no el ~36% que sale de promediar la historia completa (incluye años de mucho menor inversión en capex).",
    "C10": 5, "D10": "Horizonte estándar de convergencia del modelo.",
    "C11": 2.5, "D11": "Negocio de software/servicios: relativamente poco capital nuevo por dólar de ingreso incremental.",
    "C12": 2.0, "D12": "Años 6-10: algo más de intensidad de capital por la maduración de Cloud e infraestructura de IA propia.",
}

MULTIPLOS_EVALUACION = (
    "Evaluación GOOG: los 4 últimos cierres fiscales dieron múltiplos positivos en las 5 hojas, así que el "
    "mecanismo nativo (mínimo positivo de 4 años) se aplicó sin ajuste manual. OJO con EV/FCFF: el FCFF "
    "reportado se desplomó en los últimos 2 cierres porque el capex de infraestructura de IA (centros de datos, "
    "TPUs) creció mucho más rápido que los ingresos -- el múltiplo trailing de EV/FCFF llegó a superar 250x en el "
    "año más reciente. El mínimo de 4 años (~15x, del cierre más antiguo del rango, previo al capex-supercycle) "
    "termina siendo la base del múltiplo, y el precio resultante por EV/FCFF queda muy por debajo de los otros "
    "5 métodos (DCF, EV/EBITDA, P/E, P/FCFE, P/OCF). Esto refleja una distorsión real y conocida (el FCF de "
    "Alphabet está genuinamente comprimido por el ciclo de inversión en IA), no un error del modelo: conviene "
    "leer el precio de EV/FCFF como un piso muy conservador y no promediarlo con el mismo peso que el resto."
)

VO, INP, COC, RES = "'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'"

TESIS_ROWS: list[list] = [
    ["GOOG (Alphabet Inc., clase C) — Tesis de Inversión: De la Historia a los Números"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al día del análisis: US$"&TEXT({RES}!C25;"0.00")&" | WACC: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["Alphabet combina el negocio de publicidad digital más rentable del mundo (Búsqueda y YouTube) con una "
     "carrera de infraestructura de IA que está consumiendo capital a un ritmo sin precedentes en la historia "
     "de la empresa. El negocio central sigue creciendo a doble dígito bajo y financia ese capex casi sin "
     "apalancarse (deuda neta prácticamente nula, calificación real Aa2/AA). La pregunta de la tesis es si ese "
     "capex se traduce en un segundo motor de crecimiento rentable (Google Cloud, servicios de IA generativa "
     "para empresas) antes de que el mercado deje de tolerar la compresión del flujo de caja libre que produce "
     "mientras tanto. El caso Base asume una continuidad conservadora sin apostar a una aceleración adicional; "
     "el Optimista sí incorpora que Cloud alcance escala rentable más rápido."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["Google Cloud como segundo motor de crecimiento, compitiendo de igual a igual con AWS y Azure en la ola de "
     "infraestructura de IA generativa (modelos Gemini, TPUs propios, Vertex AI).",
     "El capex de IA (centros de datos, TPUs, redes) creció mucho más rápido que los ingresos, comprimiendo el "
     "flujo de caja libre reportado en los últimos ejercicios."],
    ["Ventaja de costo estructural en IA: a diferencia de la mayoría de sus competidores, Alphabet diseña sus "
     "propios aceleradores (TPU) en vez de depender casi enteramente de GPUs de Nvidia.",
     "Litigios antimonopolio en curso en EE.UU. (distribución de Búsqueda, tecnología publicitaria) y escrutinio "
     "regulatorio en la Unión Europea (Digital Markets Act): un remedio estructural es el riesgo de cola más "
     "citado sobre la tesis."],
    ["Balance excepcional (deuda neta casi nula, calificación Aa2/AA) y recompras sostenidas de acciones, con "
     "dividendo desde 2024 todavía con payout muy bajo (margen para crecer).",
     "Competencia directa de OpenAI/Microsoft, Anthropic y otros por la sustitución de la búsqueda tradicional "
     "con asistentes de IA generativa: el riesgo bajista de más largo plazo para el negocio central."],
    ["Estructura de tres clases de acciones (A, B, C) con derechos económicos idénticos: el valor por acción del "
     "modelo aplica igual a GOOG (clase C, sin voto) que a GOOGL.",
     "El FCFF y el FCFE reportados cayeron fuertemente en los últimos 2 cierres fiscales por el ciclo de "
     "inversión en IA, distorsionando el múltiplo EV/FCFF muy por debajo de los otros métodos (ver 'Supuestos "
     "de los Múltiplos')."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — LOS TRES ESCENARIOS (fórmulas vivas del modelo)"],
    ["Supuesto", "Conservador", "Base", "Optimista", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={INP}!B27", f"={VO}!C106",
     "Base 11%: en línea con el crecimiento LTM real (10,7%). Conservador 6%: la desaceleración de Búsqueda no "
     "se compensa con Cloud. Optimista 16%: Cloud e IA aceleran el crecimiento consolidado."],
    ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={INP}!B29", f"={VO}!D106",
     "Base 7%: converge hacia el crecimiento nominal de EE.UU. más una prima moderada de Cloud/IA, sin asumir "
     "una reaceleración adicional."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "Levemente por debajo del EBIT LTM real (33,1%, 'Valuation output'!B6) por la depreciación creciente del "
     "capex de IA en los próximos ejercicios."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 33,5%: expansión moderada, no el ~36% que sale de promediar la historia completa (incluye años con "
     "mucho menor inversión en capex, antes del ciclo de IA). Conservador: se estanca en el margen LTM real. "
     "Optimista 37%: la escala de Cloud compensa el capex de IA con apalancamiento operativo."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31",
     "5 años: horizonte estándar del modelo para una empresa madura."],
    ["Sales-to-Capital (años 1-5 / 6-10)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "2,5x (años 1-5): negocio de software/servicios, poco capital nuevo por dólar de ingreso incremental. 2,0x "
     "(años 6-10): algo más de intensidad de capital por la maduración de Cloud e infraestructura de IA propia."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "Beta observado ~1,05 (Direct Input; la canasta de industria 'Software (Internet)' de Damodaran da 1,34 "
     "desapalancada, sobreestimando el riesgo de una empresa tan diversificada y estable como Alphabet) x ERP de "
     "mercado maduro de EE.UU. Costo de deuda con calificación real Aa2/AA (no el A1/A+ genérico de la "
     "plantilla), vencimiento promedio 10 años. Deuda financiera neta prácticamente nula."],
    ["Referencia: margen base (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "EBIT LTM real: US$147.628M sobre ingresos de US$445.866M (33,1%)."],
    [],
    ["3. RESULTADO DEL DCF POR ESCENARIO"],
    ["Escenario", "Valor DCF / acción", "Precio Objetivo Ponderado*", "DCF vs. precio del análisis", "Ponderado vs. precio del análisis"],
    ["Conservador", f"={VO}!B86", f"={RES}!C12", f"=B26/{RES}!$C$25-1", f"=C26/{RES}!$C$25-1"],
    ["Base", f"={VO}!B35", f"={RES}!D12", f"=B27/{RES}!$C$25-1", f"=C27/{RES}!$C$25-1"],
    ["Optimista", f"={VO}!B137", f"={RES}!E12", f"=B28/{RES}!$C$25-1", f"=C28/{RES}!$C$25-1"],
    ["Precio del análisis (GOOGLEFINANCE)", f"={RES}!C25"],
    [f'=IF(AND(B26<B27;B27<B28;C26<C27;C27<C28;{VO}!C55<{INP}!B27;{INP}!B27<{VO}!C106;{VO}!C45<{VO}!C46;{VO}!C46<{VO}!C47);"✔ Orden verificado: Conservador < Base < Optimista en crecimiento, margen objetivo, valor DCF y precio ponderado";"✖ REVISAR: el orden Conservador < Base < Optimista no se cumple")'],
    ["*El Precio Objetivo Ponderado combina el DCF (40%) con 5 múltiplos (EV/EBITDA 20%, P/E 20%, EV/FCFF 10%, "
     "P/FCFE 5%, P/OCF 5%) según la categoría 'Madura'. El múltiplo EV/FCFF está distorsionado a la baja por el "
     "ciclo de capex de IA (ver 'Supuestos de los Múltiplos'): tomarlo como un piso conservador, no como una "
     "lectura central. En el caso Base, el DCF y el precio ponderado quedan por debajo del precio del análisis; "
     "solo el escenario Optimista se acerca al precio de mercado -- el mercado ya está pagando por un ritmo de "
     "crecimiento y expansión de margen más cercano al caso alcista que al Base."],
    [],
    ["4. CONCLUSIÓN"],
    [f'="A US$"&TEXT({RES}!C25;"0.00")&", Alphabet cotiza por ENCIMA de su DCF Base (US$"&TEXT({VO}!B35;"0.00")&", "&TEXT({VO}!B35/{RES}!C25-1;"+0%;-0%")&") y del precio objetivo ponderado Base (US$"&TEXT({RES}!D12;"0.00")&"): el caso Base de este modelo, deliberadamente conservador (sin apostar a una aceleración adicional de Cloud/IA), no justifica el precio actual por sí solo. El escenario Optimista (US$"&TEXT({VO}!B137;"0.00")&") sí se acerca al precio de mercado: la tesis alcista necesita que Google Cloud y la monetización de IA generativa aceleren más rápido que el caso Base, no solo que se sostengan."'],
    ["Variable clave a monitorear: el crecimiento y el margen operativo de Google Cloud trimestre a trimestre, y "
     "si el capex de infraestructura de IA empieza a estabilizarse como % de los ingresos (lo que liberaría "
     "flujo de caja libre) o sigue creciendo por encima de los ingresos. El resultado del litigio antimonopolio "
     "en EE.UU. (remedios) es el segundo catalizador a monitorear."],
    [],
    [SOURCES],
]


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
        {"range": "H21:H22", "format": pct},
    ])


def write_tesis(sh, backup_path) -> None:
    pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
    ms.write_tesis(
        sh, TESIS_ROWS, backup_path, text_rows=(),
        merges=[f"A{r}:E{r}" for r in (1, 2, 5, 13, 24, 31, 33, 34, 35, 37)] + [f"B{r}:E{r}" for r in range(7, 12)],
        bold_rows=(4, 13, 24, 33), head_rows=(7, 14, 25),
        formats=[
            {"range": "B15:D18", "format": pct}, {"range": "B22:D22", "format": pct},
            {"range": "B19:D19", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0"}}},
            {"range": "B20:D20", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}},
            {"range": "B21:D21", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0.00%"}}},
            {"range": "B26:C28", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
            {"range": "B29", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
            {"range": "D26:E28", "format": {"numberFormat": {"type": "PERCENT", "pattern": "+0.0%;-0.0%"}}},
        ])
