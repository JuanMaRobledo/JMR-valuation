"""Contenido cualitativo de la valoración de LULU desde cero (2-oct-2026; pasos 3 y 10 del prompt v4).
Las cifras de resultado son fórmulas vivas contra el modelo y la pestaña «Escenarios e historias»."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: 10-Q del 2T26 de lululemon athletica inc. (2-ago-2026, presentado el 3-sep-2026), 10-Q del 1T26 y 10-K 2025 "
    "(1-feb-2026), SEC EDGAR; comunicado de resultados del 2T26 (3-sep-2026); 8-K del nombramiento de Heidi O'Neill (22-abr-2026), "
    "del acuerdo de cooperación con Chip Wilson (27-may-2026), de la junta anual (24-jun-2026) y del directorio (8-sep-2026); "
    "Damodaran (betas y márgenes por industria, ene-2026; ERP sep-2026); UST 10 años y precio de cierre del 1-oct-2026."
)

CUALITATIVO = {
    "B5": "lululemon athletica inc.",
    "B6": "Heidi O'Neill (CEO desde el 8-sep-2026; antes en Nike). CFO: Meghan Frank. Presidenta ejecutiva del directorio: Marti Morfitt.",
    "B7": "Ropa deportiva técnica premium (Damodaran: Apparel)",
    "B8": "https://shop.lululemon.com  |  IR: https://corporate.lululemon.com/investors",
    "B11": "Descripción",
    "B12": ("Marca de ropa deportiva técnica (yoga, running, entrenamiento) para mujeres (~63% de las ventas) y hombres (~24%), con "
            "accesorios y calzado (~13%). Ventas LTM a jul-2026 de US$11.094M: tiendas propias ~45%, e-commerce ~44% y otros canales. "
            "825 tiendas propias y ~39.000 empleados. Sin deuda financiera."),
    "A13": "Américas",
    "B13": ("US$7.652M LTM (69%). Ventas −8% y comparables −12% en el 2T26 por menos tráfico, conversión y ticket. Margen del segmento "
            "32,6% en 2025 (38,0% en 2024)."),
    "A14": "China continental",
    "B14": ("US$1.879M LTM (17%). +29% en 2025 (comparables +20%); +4% en el 2T26 (−2% en moneda constante). Margen del segmento 40,0% "
            "en 2025, el más alto de la empresa."),
    "A15": "Resto del mundo",
    "B15": "US$1.563M LTM (14%): APAC y EMEA. +16% en 2025; +5% en el 2T26. Margen del segmento 23,0% en 2025.",
    "A16": "Estrategia",
    "B16": ("Plan de recuperación de Américas en tres pilares (creación de producto, activación de producto y habilitación de la empresa), "
            "más ventas a precio lleno y menos rebajas; expansión internacional con tiendas propias."),
    "B21": "Argumento",
    "A22": "Marca premium y rentable",
    "B22": "Margen de segmento de 23-40% y ROIC de la hoja de 27% LTM aun en la caída; margen bruto de ~55-59%.",
    "A23": "Crecimiento internacional",
    "B23": "China continental y el resto del mundo crecieron 29% y 16% en 2025 y ya son 31% de las ventas; 25 tiendas nuevas en un año.",
    "A24": "Balance y recompras",
    "B24": "Caja de US$1.390M, sin deuda financiera; US$1.158M de recompras en los últimos doce meses (~11% de la capitalización).",
    "B27": "Riesgo",
    "A28": "Américas pierde clientes",
    "B28": "Comparables −12% en el 2T26; Alo Yoga, Vuori, Nike y Adidas compiten por el mismo cliente.",
    "A29": "Aranceles y de minimis",
    "B29": ("Pagó US$230M de aranceles IEEPA (recuperó US$134,5M); los aranceles nuevos y el fin de la exención de minimis encarecen el "
            "e-commerce de EE.UU., que se despacha desde Canadá."),
    "A30": "Gobierno y transición",
    "B30": "CEO nueva desde sep-2026 tras ocho meses de co-CEO interinos; disputa por poderes con el fundador Chip Wilson resuelta con un acuerdo.",
    "A32": SOURCES,
    "A35": "Periodo del Reporte: 1 de julio de 2026 – 1 de octubre de 2026",
    "B38": "Titular",
    "A39": "Resultados",
    "B39": "2T26: ventas −4%, comparables −9% (Américas −12%), BPA US$2,92",
    "D39": "Incluye US$134,5M de devolución de aranceles (+560 pb de margen bruto y US$0,86 de BPA); gastos de venta y administración 41,7% de las ventas.",
    "A40": "Guía",
    "B40": "2026: ventas −5% a −7% y BPA US$9,48-9,73; 3T26: ventas −10% a −11%",
    "D40": "La guía incluye US$0,86 de la devolución de aranceles y no supone recompras futuras; tasa de impuestos ~30%.",
    "A41": "Gestión",
    "B41": "Heidi O'Neill asume como CEO (8-sep-2026); sale el director de IA y tecnología (13-ago-2026)",
    "D41": "Meghan Frank y André Maestrini dejan de ser co-CEO interinos; O'Neill se suma al directorio.",
    "A42": "Gobierno",
    "B42": "Acuerdo de cooperación con Chip Wilson (26-may-2026): dos directores nuevos y uno más con experiencia en ropa",
    "D42": "Laura Gentile y Marc Maurer entran al directorio tras la junta del 25-jun-2026.",
    "A43": "Capital",
    "B43": "Recompra de 2,7 millones de acciones por US$330M en el 2T26",
    "D43": "Autorización total de US$4.000M; acciones comunes e intercambiables de 110,7 millones al 28-ago-2026.",
    "B46": "Análisis e impacto en la valoración",
    "A47": "EBIT normalizado",
    "B47": ("El EBIT GAAP LTM (US$1.979M) incluye US$134,5M de devolución de aranceles y US$40M de costos de una vez (disputa por "
            "poderes y transición del CEO). El modelo usa el EBIT normalizado (US$1.884M, 17,0%)."),
    "A48": "Arrendamientos y acciones",
    "B48": ("Arrendamientos operativos como deuda (VP US$1.717M; +US$161M al EBIT). Las acciones incluyen 5,1 millones de acciones "
            "intercambiables de Lulu Canadian Holding que el pipeline omitía."),
    "A49": "Historias",
    "B49": ("Cuatro historias activas: Base (45%), Conservadora (30%), Disrupción (10%) y Optimista (15%). Los casos "
            "Conservador/Base/Optimista de la plantilla quedan como referencia técnica."),
    "A50": "Ventaja competitiva",
    "B50": ("Ventaja que se desvanece: marca de 28 años muy rentable, con Américas en caída. ROIC terminal 12,6% (punto medio entre el "
            "costo de capital terminal y el ROIC de la industria)."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 39000,
    "B12": "='Income Statement'!L30", "B13": "='Input sheet'!B13/'Input sheet'!B12",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "='Valuation output'!B42", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12",
    "E20": "='Balance Sheet'!L5", "E23": "—",
    "H4": "=('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1",
    "H5": "=('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1",
    "H6": "=('Income Statement'!K3/'Income Statement'!B3)^(1/9)-1",
    "H12": -0.06,   # guía 2026: ventas −5% a −7% (punto medio)
    "H18": 0, "H19": 0, "H20": 0, "H21": "—", "H22": "—", "H23": "—", "H24": "—",
}

STORIES = {
    "A3": "lululemon: una marca premium que deja de crecer en Américas y se apoya en lo internacional",
    "A4": ("lululemon vende ~US$11.100M al año con un margen operativo normalizado de ~17%, pero Américas (69% de las ventas) cae y la "
           "guía de 2026 implica un margen de ~13%. La historia Base: un año más de caída en Américas, estabilización desde 2027, "
           "crecimiento de 6-8% en China y el resto del mundo y un margen que sube a 17% en cinco años, sin volver al 20-24% de "
           "2022-2025. La marca gana muy por encima de su costo de capital, pero la ventaja se desvanece: ROIC terminal de 12,6%."),
    "G10": "Año 1 −6,5% (guía 2026 y Américas −11%); años 2-5 ~3,9% con lo internacional.",
    "G11": "Año 1 12,5% (guía 2026 sin la devolución de aranceles); objetivo 17% (18,45% con arrendamientos) en 5 años.",
    "G12": "30% (tasa efectiva de 2025 y guía de 2026), que se mantiene en el largo plazo.",
    "G13": "1,8 en los años 1-10: entre la industria (1,5) y la rotación propia (~2,2).",
    "G14": "ROIC de la hoja 27% LTM; terminal 12,6%: ventaja que se desvanece.",
    "G15": "Ke 9,94% (rf 5,24% + beta 1,15 × ERP 4,09%); sin deuda financiera; arrendamientos al 5,9%; WACC ~9,18%.",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": -0.065, "D6": "Guía 2026 (ventas −5% a −7%; 3T26 −10% a −11%) y Américas −11% en los próximos doce meses.",
    "C7": 0.125, "D7": "Guía 2026 sin la devolución de aranceles: BPA ~US$8,7 → margen operativo ~13%.",
    "C8": 0.039, "D8": "Historia Base: Américas 0-3%, China continental y resto del mundo 6-8%.",
    "C9": 0.1845, "D9": "17% reportado + 1,45 pp de arrendamientos; 2022-2025 fue 20-24%.",
    "C10": 5, "D10": "Recuperación de precio lleno y gastos en cinco años.",
    "C11": 1.8, "D11": "Entre Apparel (1,5) y la rotación propia (~2,2).",
    "C12": 1.8, "D12": "Igual que los años 1-5.",
}

MULTIPLOS_EVALUACION = (
    "Evaluación LULU (2-oct-2026): los múltiplos Base salen de tres anclas (historia desde Feb '25, la etapa de caída de Américas; "
    "peers sin Under Armour, sin ajuste; y el justificado, λ = 0,5). Quedan ~21% por debajo del DCF Base: la propia historia reciente "
    "de lululemon (7× EBITDA en Feb '26) y los peers deprimidos tiran hacia abajo. El DCF es el valor intrínseco; los múltiplos son "
    "precio relativo."
)

VO, INP, COC, RES, ESC = ("'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'",
                          "'Escenarios e historias'")

TESIS_ROWS: list[list] = [
    ["LULU (lululemon athletica inc.) — Tesis de Inversión: De la Historia a los Números (análisis desde cero, 2-oct-2026)"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al 1-oct-2026: US$"&TEXT({RES}!B3;"0.00")&" | WACC inicial: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["lululemon construyó en 25 años una marca premium de ropa deportiva con márgenes de 20-24%, pero desde 2025 pierde clientes en "
     "Américas (comparables −12% en el 2T26) frente a Alo Yoga, Vuori, Nike y Adidas, mientras crece en China y el resto del mundo. "
     "Los aranceles y el fin de la exención de minimis bajaron el margen, y la guía de 2026 implica ~13% sin la devolución de "
     "aranceles. Una CEO nueva (ex-Nike) asumió en septiembre de 2026. La tensión: si Américas se estabiliza y el margen vuelve a "
     "~17%, o si la marca perdió la novedad de forma permanente."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["Marca muy rentable: margen de segmento de 23-40% y ROIC de 27% aun en la caída.",
     "Comparables de Américas −12% en el 2T26 y guía de ventas −10% a −11% en el 3T26."],
    ["China continental y el resto del mundo crecen y ya son 31% de las ventas.",
     "Margen operativo de 23,7% (2024) a ~13% (guía 2026 sin aranceles devueltos)."],
    ["Sin deuda, caja de US$1.390M y recompras de ~11% de la capitalización en doce meses.",
     "Competencia de marcas de nicho (Alo, Vuori) que crecen con el mismo cliente."],
    ["La acción cotiza a ~8 veces las utilidades LTM y ~1 vez las ventas.",
     "Transición de CEO, disputa con el fundador y salida del director de tecnología."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — CASO BASE DE LA HOJA (= historia Base; fórmulas vivas)"],
    ["Supuesto", "Conservador técnico", "Base", "Optimista técnico", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={INP}!B27", f"={VO}!C106",
     "Base −6,5%: guía 2026 (comunicado del 3-sep-2026) y Américas −11%; por segmento, historia Base."],
    ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={INP}!B29", f"={VO}!D106",
     "Base ~3,9%: Américas 0-3%, China continental y resto del mundo 6-8%."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "12,5%: guía 2026 sin la devolución de aranceles (BPA ~US$8,7)."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 18,45% (17% + arrendamientos): precio lleno y gastos, sin volver al 20-24% de 2022-2025."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31", "5 años."],
    ["Sales-to-Capital (años 1-5)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "1,8 (también en los años 6-10): entre Apparel (1,5) y la rotación propia (~2,2)."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "rf 5,24% (UST 10 años, 1-oct-2026) + beta 1,15 (regresión 2 y 5 años) × ERP 4,09% (Damodaran, sep-2026); arrendamientos al 5,9%."],
    ["Referencia: margen base normalizado (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "EBIT GAAP LTM US$1.979M − US$134,5M de aranceles devueltos + US$40M de costos de una vez = US$1.884M (+ arrendamientos)."],
    [],
    ["3. HISTORIAS ACTIVAS Y RESULTADO (DCF Base = valor intrínseco principal; esperado = complemento)"],
    ["Historia", "Probabilidad", "DCF hoy / acción", "Margen objetivo", "CAGR ingresos 1-5"],
    [f"={ESC}!A5", f"={ESC}!B5", f"={ESC}!H5", f"={ESC}!D5", f"={ESC}!C5"],
    [f"={ESC}!A6", f"={ESC}!B6", f"={ESC}!H6", f"={ESC}!D6", f"={ESC}!C6"],
    [f"={ESC}!A7", f"={ESC}!B7", f"={ESC}!H7", f"={ESC}!D7", f"={ESC}!C7"],
    [f"={ESC}!A8", f"={ESC}!B8", f"={ESC}!H8", f"={ESC}!D8", f"={ESC}!C8"],
    ["DCF esperado por probabilidades (complemento)", f"={ESC}!B10", f"={ESC}!H10", "Precio con MOS sobre el esperado", f"={ESC}!H14"],
    ["Múltiplos consolidados hoy (precio relativo, Base)", "", "='Descuento de múltiplos'!D39", "Precio al 1-oct-2026", f"={RES}!B3"],
    [],
    ["4. LOG DE CORRECCIONES Y AJUSTES (respaldo de cada celda en reference/backups/lulu_desde_cero_2026-10-02.json del repo JMR-valuation)"],
    ["#", "Celda / componente", "Antes", "Después", "Razón"],
    [1, "Balance Sheet columna L", "Saldos de feb-2026 (salvo la caja)", "Balance al 2-ago-2026 (10-Q 2T26)", "El pipeline repetía el cierre anual."],
    [2, "Balance Sheet filas 21-23 (feb-2026 y LTM)", "Arrendamientos y tarjetas de regalo en otros pasivos", "Separados", "10-K 2025 y 10-Q 2T26."],
    [3, "Input sheet!B13 (EBIT base)", "=L12 (US$1.979M)", "=L12 − 134,5 + 40 (US$1.884M)", "Devolución de aranceles, disputa por poderes y transición del CEO."],
    [4, "Input sheet!B16 (deuda)", "US$1.500M (arrendamientos contables)", "0 (sin deuda financiera)", "Los arrendamientos entran por el conversor (B18 = Yes)."],
    [5, "Input sheet!B17 / B18", "I+D Yes · arrendamientos No", "No · Yes", "Sin I+D informado; arrendamientos como deuda (Damodaran)."],
    [6, "Input sheet!B22 / Income Statement!L27", "105,6M (solo comunes)", "111,8M (comunes + intercambiables + RSU/PSU)", "Portada y nota 6 del 10-Q del 2T26."],
    [7, "Input sheet!B24 / B38-B42 / B60", "29,4% · sin opciones · converge a 25%", "30% fijo · 1,525M opciones a US$258,81", "Guía de tasa ~30%; 10-Q del 2T26."],
    [8, "Cost of capital worksheet", "Beta 1,20 directa · ERP de enero", "Beta 1,15 · Kd 5,9% · ERP 4,09%", "Regresión 2 y 5 años; ERP de sep-2026."],
    [9, "Input sheet!B4 / D1 / B35 / B49-B50", "Fecha y precio de la corrida", "1-oct-2026 · US$95,86 · 5,24% · ROIC terminal 12,6%", "Fecha de corte; criterio de ventaja que se desvanece."],
    [10, "Descuento de múltiplos fila 38 / 43", "DCF técnico · MOS sobre el ponderado", "Historias · MOS sobre el esperado", "Presentación vigente (1-oct-2026)."],
    [],
    ["5. CONCLUSIÓN"],
    [f'="El DCF Base de las historias es US$"&TEXT({ESC}!H5;"0.00")&" y el esperado US$"&TEXT({ESC}!H10;"0.00")&"; el precio del 1-oct-2026 (US$"&TEXT({RES}!B3;"0.00")&") está "&TEXT({RES}!B3/{ESC}!H5-1;"+0%;-0%")&" frente a la Base. Los múltiplos (US$"&TEXT(\'Descuento de múltiplos\'!D39;"0.00")&") quedan por debajo del DCF. El precio se parece al de la Conservadora o la Disrupción: el mercado descuenta que Américas no se recupera."'],
    ["Variable clave a monitorear: los comparables de Américas, el margen bruto sin devoluciones de aranceles y la ejecución de la nueva CEO. Si Américas vuelve a 0% en 2027 con margen bruto ≥ 57%, el caso se mueve hacia la Base u Optimista; si los comparables siguen en −8% o peor, hacia la Conservadora o la Disrupción."],
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
        {"range": "H4:H12", "format": pct},
    ])


def write_tesis(sh, backup_path) -> None:
    pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
    cur = {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}
    ms.write_tesis(
        sh, TESIS_ROWS, backup_path, text_rows=range(34, 44),
        merges=[f"A{r}:E{r}" for r in (1, 2, 5, 33, 47, 48, 50)] + [f"B{r}:E{r}" for r in range(7, 12)],
        bold_rows=(4, 13, 24, 33, 46), head_rows=(7, 14, 25, 34),
        formats=[
            {"range": "B15:D18", "format": pct}, {"range": "B22:D22", "format": pct},
            {"range": "B19:D19", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0"}}},
            {"range": "B20:D20", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}},
            {"range": "B21:D21", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0.00%"}}},
            {"range": "B26:B30", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0%"}}},
            {"range": "C26:C31", "format": cur}, {"range": "D26:E29", "format": pct},
            {"range": "E30:E31", "format": cur},
        ])
