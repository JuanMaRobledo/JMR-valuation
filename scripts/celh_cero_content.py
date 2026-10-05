"""Contenido de las hojas de texto de la valoración de CELH desde cero (5-oct-2026; pasos 3 y 10 del prompt v4).
Las cifras de resultado son fórmulas vivas contra el modelo y la pestaña «Escenarios e historias»; las demás salen de
las fuentes citadas (corte de información: 30-sep-2026)."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: 10-Q del 2T26 de Celsius Holdings (6-ago-2026) y 10-K 2025 (2-mar-2026), SEC EDGAR; comunicados de resultados "
    "del 4T25 (26-feb-2026) y del 2T26 (6-ago-2026); 8-K de la segunda enmienda del crédito (15-jul-2026) y de cambios en la "
    "gerencia (10-ago-2026); Forms 4 del CEO y de dos directores (10 al 16-sep-2026); resumen de la llamada del 2T26 (Yahoo "
    "Finance, 6-ago-2026); Monster Beverage, comunicado del 2T26 y datos NielsenIQ al 25-jul-2026 (8-K del 6-ago-2026); "
    "investigación del fiscal de Texas (14 News, 4-jun-2026); aviso de la demanda colectiva (GlobeNewswire, 10-sep-2026); "
    "Damodaran (betas, márgenes y ventas/capital por industria, ene-2026; ERP sep-2026); UST 10 años y precio de cierre del "
    "30-sep-2026."
)

CUALITATIVO = {
    "B5": "Celsius Holdings, Inc.",
    "B6": "John Fieldly (presidente del directorio y CEO). CFO: Jarrod Langhans. Tyler Bohannon, director comercial desde el 10-ago-2026.",
    "B7": "Bebidas energéticas y funcionales (Damodaran: Beverage (Soft))",
    "B8": "https://www.celsiusholdingsinc.com  |  IR: https://ir.celsiusholdingsinc.com",
    "B11": "Descripción",
    "A12": "Visión General de la Empresa",
    "B12": ("Portafolio de tres marcas de bebidas energéticas: CELSIUS, Alani Nu (comprada en abril de 2025 por US$2.055,6M) y "
            "Rockstar (EE.UU. y Canadá, agosto de 2025). Ventas LTM a jun-2026 de US$3.047M y ~20% de la categoría en EE.UU. "
            "Fabrica con terceros y distribuye a través de PepsiCo, parte relacionada que compra ~60% de las ventas (1S26) y es "
            "tenedora de las preferentes. 1.497 empleados a dic-2025."),
    "A13": "CELSIUS",
    "B13": ("~US$1.425M LTM. Facturación −11,7% en el 2T26 (−2% al consumidor; −7,2% en conveniencia en julio) por promociones, "
            "inventario y una poda de presentaciones que la gerencia admitió fue demasiado profunda. 9,5% de la categoría."),
    "A14": "Alani Nu",
    "B14": ("~US$1.433M LTM y ya la marca más grande. Ventas al consumidor +55,7% en el 2T26 (+74% en conveniencia en julio) y 8,7% "
            "de la categoría; facturación +21% por el paso a la red de PepsiCo. Bajo investigación del fiscal de Texas (jun-2026)."),
    "A15": "Rockstar y exterior",
    "B15": ("Rockstar US$188,7M en diez meses (US$66,5M en el 2T26), −13% al consumidor. Exterior US$62,5M en el 1S26 (+32%): "
            "Nórdicos, Reino Unido, Irlanda, Francia, Australia; meta de más de 15% de las ventas en cinco años."),
    "A16": "Distribución",
    "B16": ("PepsiCo distribuye las tres marcas en EE.UU. como capitán de la categoría energía (acuerdo de ~17 años desde "
            "ago-2025). Celsius pagó la capitanía con preferentes (pago implícito de US$598,8M que reduce el ingreso)."),
    "B21": "Argumento",
    "A22": "Alani Nu y escala",
    "B22": ("Alani Nu crece a más de 50% al consumidor y atrae a consumidoras nuevas en la categoría. El portafolio vendió +31% al "
            "consumidor en el 2T26 y aportó ~30% del crecimiento del segmento sin azúcar."),
    "A23": "Margen normalizado y caja",
    "B23": ("Sin cargos de una vez el margen operativo LTM es ~19,8% (con los costos legales como recurrentes); flujo operativo "
            "de US$296M en el 1S26, caja de US$631M y deuda de US$695M. Recompras de US$125,5M en el 1S26."),
    "A24": "PepsiCo alineado e internos comprando",
    "B24": ("PepsiCo es socio, distribuidor y tenedor de preferentes. El CEO y dos directores compraron acciones a US$27-28 entre "
            "el 10 y el 16-sep-2026 (Forms 4)."),
    "B27": "Riesgo",
    "A28": "La marca CELSIUS pierde participación",
    "B28": "Tres trimestres de caída al facturar y −7,2% en conveniencia en julio; la recuperación depende de recuperar espacio en refrigeradores.",
    "A29": "Regulación de la cafeína y litigios",
    "B29": ("Investigación del fiscal de Texas sobre Alani Nu (200 mg de cafeína por lata), demanda por muerte de una adolescente y "
            "demandas colectivas de accionistas (período feb-2025 a jun-2026). Una restricción por edad golpearía a la marca que crece."),
    "A30": "Categoría que se enfría y margen bruto",
    "B30": ("La categoría pasó de +15,2% (52 semanas a abril, Circana) a +7,1% (13 semanas al 25-jul-2026, NielsenIQ). Margen bruto de 48,1% (51,5% un año antes) "
            "por promociones, mezcla y aluminio; más de la mitad de las ventas pasa por un solo distribuidor."),
    "A32": SOURCES,
    "A35": "Periodo del Reporte: 1 de julio de 2026 – 30 de septiembre de 2026",
    "B38": "Titular",
    "A39": "Resultados",
    "B39": "2T26: ventas +10,6%, CELSIUS −11,7%, margen bruto 48,1%",
    "D39": "Ventas de US$817,9M; EBITDA ajustado US$184,2M (22,5%); recompras de US$100,4M en el trimestre.",
    "A40": "Guía",
    "B40": "3T26 parecido al 2T26; CELSIUS vuelve a crecer al cierre del año",
    "D40": "Margen bruto ~48% en el 3T26 por el aluminio; el 4T26 de Alani Nu enfrenta la base alta del llenado de inventario de 2025.",
    "A41": "Gestión",
    "B41": "Sale el presidente y COO Eric Hanson; Bohannon, director comercial",
    "D41": "8-K del 10-ago-2026; Tony Guilfoyle, director de transformación desde el 1-jul-2026.",
    "A42": "Internos y acciones",
    "B42": "El CEO y dos directores compran ~US$1,8M en acciones",
    "D42": "Fieldly 18.000 a US$27,44 (10-sep); DeSantis 36.000 a US$27,65-27,95; Kravitz 12.000 a US$28,00. El 1-oct se liberó un tercio de las acciones de los vendedores de Alani Nu.",
    "A43": "Legal",
    "B43": "Demanda colectiva por la seguridad de Alani Nu",
    "D43": "Período de clase 21-feb-2025 a 3-jun-2026; fecha límite para el demandante principal: 3-nov-2026 (GlobeNewswire, 10-sep-2026).",
    "B46": "Análisis e impacto en la valoración",
    "A47": "EBIT normalizado",
    "B47": ("El EBIT GAAP LTM (US$160,3M) incluye US$466,2M de cargos; el modelo suma US$441,6M (terminación de distribuidores, "
            "integración, inventario) y deja como costo el acuerdo legal de US$24,6M: EBIT normalizado US$601,9M (19,8%)."),
    "A48": "Preferentes de PepsiCo",
    "B48": ("Se restan por su valor de liquidación (US$1.135M), no por el contable (US$1.760M): no se convierten antes de "
            "ago-2031/2032 y solo por encima de US$25 (Serie A) y US$51,75 (Serie B). Se incluyen en el capital invertido."),
    "A49": "Historias",
    "B49": ("Cuatro historias activas: Base (45%), Conservadora (25%), Disrupción (15%) y Optimista (15%); 'Valuation output' "
            "calcula las cuatro con la estructura de Damodaran."),
    "A50": "Riesgo en el descuento",
    "B50": ("Beta 1,0: la del sector (0,62 reapalancada) corresponde a refrescos diversificados; Celsius depende de una categoría "
            "y de un distribuidor. Prima de mercado por regiones (4,13%). Regresión: 0,83 (2 años) y 1,55 (5 años)."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 1497,
    "B12": "='Income Statement'!L30", "B13": "='Input sheet'!B13/'Input sheet'!B12",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "='Valuation output'!B42", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12", "E13": "—", "E14": "—", "E15": "—", "E16": "—", "E17": "—",
    "E20": "='Balance Sheet'!L5", "E23": "='Input sheet'!B13/'Income Statement'!L16",
    "H4": "=('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1",
    "H5": "=('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1",
    "H6": "=('Income Statement'!K3/'Income Statement'!B3)^(1/9)-1",
    "H7": "—", "H8": "—", "H9": "—", "H10": "—",
    "H11": "=('Income Statement'!K27/'Income Statement'!F27)^(1/5)-1",
    "H12": "—", "H13": "—", "H14": "—", "H15": "—",
    "H18": 0, "H19": 0, "H20": 0, "H21": "—", "H22": "—", "H23": "—", "H24": "—",
}

STORIES = {
    "A3": "Celsius: Alani Nu sostiene un portafolio de tres marcas mientras la marca CELSIUS cede",
    "A4": ("Celsius vende ~US$3.047M al año y ~20% de las bebidas energéticas de EE.UU., pero la mitad de sus ventas ya es Alani Nu "
           "y todo pasa por PepsiCo. El margen normalizado es ~19,8%, nueve puntos por debajo del de Monster. La historia Base: el "
           "portafolio crece ~5% compuesto (algo menos que la categoría), Alani Nu se modera, CELSIUS deja de caer y crece poco, "
           "Rockstar declina y el margen llega a 20%. Sin una ventaja defendible propia, el retorno después del año 10 vuelve al "
           "costo de capital."),
    "G10": "Año 1 +5,9% (CELSIUS −3%, Alani Nu +12%, Rockstar con un año completo); años 2-5 ~4,5% por marca.",
    "G11": "Año 1 19,6% (normalizado del 2T26); objetivo 20% en 5 años: escala en gastos contra promociones más altas.",
    "G12": "Tasa efectiva del 1S26 (20,1%) que converge a la marginal de 25%.",
    "G13": "1,8 en los años 1-5 y 1,6 en los años 6-10: el capital nuevo rinde ~27% y ~24%, bajo el ROIC de la industria (29%).",
    "G14": "ROIC normalizado ~15,9% con el preferente en el capital; terminal = costo de capital (sin ventaja defendible).",
    "G15": "Ke 9,42% (rf 5,29% + beta 1,0 × ERP por regiones 4,13%); Kd 6,5% (SOFR + 2,25%); WACC ~9,0%.",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": 0.059, "D6": "Suma por marca: CELSIUS −3% (3T26 como el 2T26), Alani Nu +12%, Rockstar +27% por anualización.",
    "C7": 0.196, "D7": "Margen normalizado del 2T26 (EBIT 75,3 + terminación 80,9 + integración 3,8 sobre ventas 817,9).",
    "C8": 0.045, "D8": "Historia Base por marca: Alani Nu 10% → 5%, CELSIUS 2-3%, Rockstar −4 a −8%; categoría 4-7%.",
    "C9": 0.201, "D9": "20% reportado + 0,09 pp de arrendamientos; Monster (29%) no es el ancla: distribución propia y escala.",
    "C10": 5, "D10": "La mejora de margen es de escala en gastos generales, no un cambio de modelo.",
    "C11": 1.8, "D11": "Rendimiento sobre el capital nuevo ~27% (margen 20% × 75% × 1,8): bajo el ROIC de la industria (29%).",
    "C12": 1.6, "D12": "~24% sobre el capital nuevo; industria Beverage (Soft) 1,54; actual 1,0 por las compras.",
}

MULTIPLOS_EVALUACION = (
    "Evaluación CELH (5-oct-2026, desde cero): los múltiplos Base salen de tres anclas (historia solo de FY2024, peers sin KDP con "
    "−20% y el justificado, λ = 0,5). Valen más que el DCF Base de las historias. No es un problema de crecimiento sino de ventaja "
    "competitiva: los peers (Coca-Cola, Monster) cotizan con retornos excedentes duraderos y el DCF supone que Celsius no los conserva "
    "después del año 10. El DCF es el valor intrínseco; los múltiplos son precio relativo."
)

VO, INP, COC, RES, ESC = ("'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'",
                          "'Escenarios e historias'")

TESIS_ROWS: list[list] = [
    ["CELH (Celsius Holdings, Inc.) — Tesis de Inversión: De la Historia a los Números (análisis desde cero, 5-oct-2026)"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al 30-sep-2026: US$"&TEXT({RES}!B3;"0.00")&" | WACC inicial: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["Celsius dejó de ser una marca única en hipercrecimiento y pasó a ser un portafolio de tres marcas de bebidas energéticas "
     "distribuido por PepsiCo, en el que Alani Nu ya vende más que CELSIUS. Las ventas de 2025 crecieron 85,5%, casi todo por compras; "
     "la marca CELSIUS cae al facturar y en julio también al consumidor, mientras Alani Nu crece más de 50%. El margen GAAP (5,3% LTM) "
     "está deprimido por cargos de una vez; el normalizado es ~19,8%. La tensión: si Alani Nu sostiene el crecimiento bajo el "
     "escrutinio de la cafeína mientras CELSIUS se estabiliza, o si la categoría enfriándose y la regulación dejan al portafolio "
     "sin motor."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["Alani Nu +55,7% al consumidor en el 2T26 (+74% en conveniencia en julio); portafolio ~20% de la categoría.",
     "CELSIUS −11,7% al facturar en el 2T26 y −7,2% al consumidor en conveniencia en julio."],
    ["Margen normalizado ~19,8% y EBITDA ajustado de 23,7% en el 1S26; flujo operativo de US$296M en el semestre.",
     "Margen bruto de 48,1% (−3,4 pp en un año) y más promociones anunciadas para el 4T26."],
    ["PepsiCo es socio, distribuidor y tenedor de preferentes; el CEO y dos directores compraron acciones en septiembre.",
     "Investigación del fiscal de Texas y demandas por la cafeína de Alani Nu; la categoría se desaceleró a ~5-7%."],
    ["Exterior +32% en el 1S26 y meta de más de 15% de las ventas en cinco años.",
     "Las compras (Alani Nu US$2.056M, capitanía US$936M) rinden poco más que el costo de capital."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — HISTORIAS EN 'VALUATION OUTPUT' (fórmulas vivas)"],
    ["Supuesto", "Conservadora", "Base", "Optimista", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={VO}!C4", f"={VO}!C106",
     "Base +5,9%: CELSIUS −3% (3T26 similar al 2T26), Alani Nu +12% y Rockstar con un año completo (comunicado del 2T26)."],
    ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={VO}!D4", f"={VO}!D106",
     "Base ~4,5%: Alani Nu 10% → 5%, CELSIUS 2-3%, Rockstar en declive; la categoría creció 7,1% en 13 semanas a julio."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "19,6%: margen normalizado del 2T26 (sin terminación de distribuidores ni integración)."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 20,1% (20% + arrendamientos): escala en gastos generales contra más promociones; Monster (29,2%) es el techo."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31", "5 años."],
    ["Sales-to-Capital (años 1-5)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "1,8 (1,6 en los años 6-10): ~27% y ~24% sobre el capital nuevo, bajo el ROIC de la industria (29%)."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "rf 5,29% (UST 10 años, 30-sep-2026) + beta 1,0 × ERP por regiones 4,13% (Damodaran, sep-2026) = Ke 9,42%; Kd 6,5%."],
    ["Referencia: margen base normalizado (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "EBIT GAAP LTM US$160,3M + US$441,6M de cargos de una vez = US$601,9M (+ arrendamientos); el litigio queda como costo."],
    [],
    ["3. HISTORIAS ACTIVAS Y RESULTADO (DCF Base = valor intrínseco principal; esperado = complemento)"],
    ["Historia", "Probabilidad", "DCF hoy / acción", "Margen objetivo", "CAGR ingresos 1-5"],
    [f"={ESC}!A5", f"={ESC}!B5", f"={ESC}!H5", f"={ESC}!D5", f"={ESC}!C5"],
    [f"={ESC}!A6", f"={ESC}!B6", f"={ESC}!H6", f"={ESC}!D6", f"={ESC}!C6"],
    [f"={ESC}!A7", f"={ESC}!B7", f"={ESC}!H7", f"={ESC}!D7", f"={ESC}!C7"],
    [f"={ESC}!A8", f"={ESC}!B8", f"={ESC}!H8", f"={ESC}!D8", f"={ESC}!C8"],
    ["DCF esperado por probabilidades (complemento)", f"={ESC}!B10", f"={ESC}!H10", "Precio con MOS sobre el esperado", f"={ESC}!H14"],
    ["Múltiplos consolidados hoy (precio relativo, Base)", "", "='Descuento de múltiplos'!D39", "Precio al 30-sep-2026", f"={RES}!B3"],
    [],
    ["4. LOG DE CORRECCIONES Y AJUSTES (respaldo de cada celda en reference/backups/celh_desde_cero_2026-10-05.json del repo JMR-valuation)"],
    ["#", "Celda / componente", "Antes", "Después", "Razón"],
    [1, "Balance Sheet columna L", "Saldos de dic-2025", "Balance al 30-jun-2026 (10-Q 2T26)", "El importador repetía el cierre anual."],
    [2, "Income Statement filas 23-27 (2016-2022)", "Acciones y BPA sin ajustar", "Acciones ×3, BPA ÷3", "Split 3 por 1 del 15-nov-2023."],
    [3, "BPA 2023 y cambio neto de caja", "Escala o etiqueta del importador", "XBRL de la SEC", "Auditoría de estados contra la SEC (12 celdas)."],
    [4, "Input sheet!B13 (EBIT base)", "=L12 (US$160,3M)", "=L12 + 441,6 (US$601,9M)", "Terminación de distribuidores, integración e inventario; el litigio queda como costo recurrente."],
    [5, "Input sheet!B15 (patrimonio en libros)", "=L35 (US$1.199,6M)", "=L35 + 1.759,975", "El capital invertido incluye el preferente que financió Rockstar y la capitanía."],
    [6, "Input sheet!B16 (deuda)", "Neta de costos + arrendamientos", "L20 + L25 + 19,9 = US$694,75M nominal", "Valor razonable ≈ principal (10-Q); arrendamientos por el conversor."],
    [7, "Input sheet!B17 / B18", "I+D Yes · arrendamientos No", "No · Yes", "I+D inmaterial; arrendamientos como deuda (Damodaran)."],
    [8, "Input sheet!B22 / B24 / B38-B42", "253,0M · tasa LTM 8,8% · sin opciones", "255,1M (con RSU) · 20,1% · 2,313M opciones a US$6,28", "10-Q 2T26 y 10-K 2025."],
    [9, "Input sheet!B76", "Sin preferentes", "US$1.135M (liquidación)", "Series A y B de PepsiCo (10-Q 2T26)."],
    [10, "Cost of capital worksheet", "Beta del sector · rating · país de registro", "Beta 1,0 · Kd 6,5% directo · prima por regiones", "Riesgo propio; deuda real a tasa variable; ventas por región del 10-K."],
    [11, "Input sheet!B4 / D1 · Trailing L3", "Fecha y precio de la corrida", "30-sep-2026 · US$27,35", "Fecha de corte común de la cartera."],
    [12, "Descuento de múltiplos fila 38 / 43", "DCF de 'Valuation output' · MOS sobre el ponderado", "Historias · MOS sobre el esperado", "Presentación vigente."],
    [],
    ["5. CONCLUSIÓN"],
    [f'="El DCF Base de las historias es US$"&TEXT({ESC}!H5;"0.00")&" y el esperado US$"&TEXT({ESC}!H10;"0.00")&"; el precio del 30-sep-2026 (US$"&TEXT({RES}!B3;"0.00")&") está "&TEXT({RES}!B3/{ESC}!H5-1;"+0%;-0%")&" frente a la Base. Los múltiplos (US$"&TEXT(\'Descuento de múltiplos\'!D39;"0.00")&") valen más porque los peers cotizan con ventajas duraderas que el DCF no le reconoce a Celsius. El DCF es la lectura más confiable: el valor depende del margen y de cuánto dura el crecimiento de Alani Nu, no de un múltiplo de mercado."'],
    ["Variable clave a monitorear: las ventas al consumidor de CELSIUS y de Alani Nu (Circana/NielsenIQ), el margen bruto y la investigación de Texas. Si CELSIUS vuelve a crecer y el margen bruto se recupera a 50%, el caso se mueve hacia la Optimista; si Alani Nu se desacelera a un dígito o llega una restricción por edad, hacia la Conservadora o la Disrupción."],
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
        {"range": "E4:E9", "format": mult}, {"range": "E12", "format": cur},
        {"range": "E20", "format": num}, {"range": "E23", "format": mult},
        {"range": "H4:H15", "format": pct},
    ])


def write_tesis(sh, backup_path) -> None:
    pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
    cur = {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}
    ms.write_tesis(
        sh, TESIS_ROWS, backup_path, text_rows=range(34, 46),
        merges=[f"A{r}:E{r}" for r in (1, 2, 5, 33, 49, 50, 52)] + [f"B{r}:E{r}" for r in range(7, 12)],
        bold_rows=(4, 13, 24, 33, 48), head_rows=(7, 14, 25, 34),
        formats=[
            {"range": "B15:D18", "format": pct}, {"range": "B22:D22", "format": pct},
            {"range": "B19:D19", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0"}}},
            {"range": "B20:D20", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}},
            {"range": "B21:D21", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0.00%"}}},
            {"range": "B26:B30", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0%"}}},
            {"range": "C26:C31", "format": cur}, {"range": "D26:E29", "format": pct},
            {"range": "E30:E31", "format": cur},
        ])
