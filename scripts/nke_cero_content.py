"""Contenido cualitativo de la valoración de NKE desde cero (2-oct-2026; pasos 3 y 10 del prompt v4).
Las cifras de resultado son fórmulas vivas contra el modelo y la pestaña «Escenarios e historias»."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: 10-K FY2026 de NIKE, Inc. (31-may-2026, presentado el 15-jul-2026), SEC EDGAR; comunicado de resultados del "
    "1T FY2027 (1-oct-2026) y del 3T FY2026; 8-K de la junta anual (8-sep-2026) y de cambios en la gerencia (ago-sep-2026); "
    "Bloomberg Línea y Tradingpedia (salida de Mbappé a On, recorte de precio objetivo de UBS, sep-2026); Damodaran (betas y "
    "márgenes por industria, ene-2026; ERP sep-2026); UST 10 años y precio de cierre del 1-oct-2026."
)

CUALITATIVO = {
    "B5": "NIKE, Inc.",
    "B6": "Elliott Hill (presidente y CEO desde oct-2024). CFO: Dave Denton (desde el 17-ago-2026). Presidente ejecutivo del directorio: Mark Parker.",
    "B7": "Calzado, ropa y equipamiento deportivo (Damodaran: Shoe)",
    "B8": "https://about.nike.com  |  IR: https://investors.nike.com",
    "B11": "Descripción",
    "B12": ("La marca deportiva más grande del mundo: NIKE, Jordan y Converse. Ventas LTM a ago-2026 de US$45.891M: calzado ~63%, "
            "ropa ~31%, equipamiento ~6%. Diseña y comercializa; fabrica con terceros en Vietnam, Indonesia y China. Vende a "
            "mayoristas (~61%) y directo (NIKE Direct, ~39%). ~73.000 empleados a may-2026."),
    "A13": "Norteamérica",
    "B13": ("US$20.618M LTM (45%). Única región que crece: +2% en el 1T FY27 con mayoristas +9% y NIKE Direct −6%. EBIT de "
            "US$5.376M en FY2026 (26% de margen), incluye la devolución de aranceles IEEPA."),
    "A14": "EMEA y APLA",
    "B14": ("EMEA US$12.417M LTM (−5% en el 1T FY27; calzado −11%, ropa +5%). APLA US$6.216M (−2%, plano sin efecto cambiario). "
            "Desde FY2028 Nike se reorganiza en tres geografías (programa Pace)."),
    "A15": "Gran China y Converse",
    "B15": ("Gran China US$5.515M LTM, −22% en el 1T FY27 (−26% sin efecto cambiario) y EBIT −34%: competencia local (Anta, "
            "Li-Ning) y reposicionamiento. Converse US$1.174M en FY2026 (−31%) y −28% en el 1T FY27; EBIT casi nulo."),
    "A16": "Estrategia",
    "B16": ("«Sport Offense»: equipos por deporte (running, fútbol, básquet), vuelta a los mayoristas y limpieza de franquicias "
            "clásicas (Air Force 1, Dunk, Jordan 1). Pace: ahorro de US$2.500M brutos a FY2031 con ~US$1.000M de cargos."),
    "B21": "Argumento",
    "A22": "Marca y escala",
    "B22": ("La marca deportiva más valiosa, con el mayor presupuesto de marketing del sector (demand creation US$1.252M solo en el "
            "1T FY27) y la red de distribución más grande. Ya salió de crisis parecidas en 1998 y 2016-2017."),
    "A23": "Margen deprimido con palancas visibles",
    "B23": ("Margen normalizado de ~6,9% frente a 12-16% en FY2017-FY2024; margen bruto +60 pb en el 1T FY27 y gastos generales "
            "−6%. Pace apunta a US$2.500M de ahorros."),
    "A24": "Balance sólido",
    "B24": ("Caja e inversiones de US$8.368M frente a deuda de US$7.893M; calificación A2/A+; dividendo de US$0,41 por trimestre "
            "(~4,7% de rendimiento al precio actual)."),
    "B27": "Riesgo",
    "A28": "Pérdida de participación y relevancia",
    "B28": "On, Hoka, Adidas y marcas chinas crecen más; Mbappé dejó Nike por On (sep-2026). NIKE Direct digital −13% en el 1T FY27.",
    "A29": "Gran China",
    "B29": "−22% en el 1T FY27 y la gerencia la está reposicionando: puede ser una pérdida estructural, no cíclica.",
    "A30": "Aranceles y márgenes",
    "B30": ("La devolución de los aranceles IEEPA (US$986M) fue de una vez; aranceles nuevos (secciones 232/301) podrían quitar "
            "1-2 pp de margen bruto. Más ventas por mayoristas implica menos margen que la venta directa."),
    "A32": SOURCES,
    "A35": "Periodo del Reporte: 1 de julio de 2026 – 1 de octubre de 2026",
    "B38": "Titular",
    "A39": "Resultados",
    "B39": "1T FY27: ventas −4%, margen bruto 42,8% (+60 pb), BPA US$0,48",
    "D39": "Ventas de US$11.213M frente a ~US$11.320M esperados; BPA por encima del consenso (US$0,43); Gran China −22%, Converse −28%.",
    "A40": "Guía",
    "B40": "FY2027: ventas con caída de un dígito alto; BPA ajustado US$1,15-1,35",
    "D40": "Tasa efectiva ~25%; excluye ~US$0,15 por acción de cargos de Pace; la gerencia anticipa más despidos en 2027.",
    "A41": "Gestión",
    "B41": "Dave Denton, CFO desde el 17-ago-2026; Alexandre Arnault entra al directorio",
    "D41": "Arnault se sumó el 16-sep-2026; Mark Parker sigue como presidente ejecutivo.",
    "A42": "Mercado",
    "B42": "Sale del S&P 100 (21-sep-2026); UBS baja el precio objetivo a US$42",
    "D42": "La acción tocó un mínimo de 52 semanas de US$35,15 el 1-oct-2026 (máximo US$72,94 en sep-2025).",
    "A43": "Atletas",
    "B43": "Kylian Mbappé deja Nike por On (sep-2026)",
    "D43": "Señal de la competencia por atletas en fútbol, una de las categorías prioritarias de la Sport Offense.",
    "B46": "Análisis e impacto en la valoración",
    "A47": "EBIT normalizado",
    "B47": ("El EBIT GAAP LTM (US$3.758M) incluye la devolución de una vez de aranceles IEEPA (US$986M) y las indemnizaciones de "
            "FY2026 (US$385M). El modelo usa el EBIT normalizado (US$3.157M, 6,9%)."),
    "A48": "Arrendamientos y deuda",
    "B48": ("Arrendamientos operativos como deuda (VP US$2.869M; +US$283M al EBIT). Deuda financiera a valor nominal (US$7.893M); "
            "la plantilla sumaba los arrendamientos contables a la deuda."),
    "A49": "Historias",
    "B49": ("Cuatro historias activas: Base (45%), Conservadora (25%), Disrupción (10%) y Optimista (20%). Los casos "
            "Conservador/Base/Optimista de la plantilla quedan como referencia técnica."),
    "A50": "Ventaja competitiva",
    "B50": ("Ventaja que se desvanece: marca probada que gana sobre su costo de capital, pero con el ROIC en caída. ROIC terminal "
            "12,3% (punto medio entre el costo de capital terminal y el ROIC actual)."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 73000,
    "B12": "='Income Statement'!L30", "B13": "='Input sheet'!B13/'Input sheet'!B12",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "='Valuation output'!B42", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12",
    "E20": "='Balance Sheet'!L5", "E23": "='Input sheet'!B13/'Input sheet'!B14",
    "H4": "=('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1",
    "H5": "=('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1",
    "H6": "=('Income Statement'!K3/'Income Statement'!B3)^(1/9)-1",
    "H12": -0.08,   # guía FY2027: caída de un dígito alto (punto medio)
    "H18": 0, "H19": 0, "H20": 0, "H21": "—", "H22": "—", "H23": "—", "H24": "—",
}

STORIES = {
    "A3": "Nike: la marca deportiva más grande en una reestructuración que devuelve el crecimiento lento con margen de dos dígitos bajos",
    "A4": ("Nike vende ~US$45.900M al año, pero las ventas caen desde FY2024 y el margen normalizado es ~6,9%, frente a 12-16% en "
           "FY2017-FY2024. La historia Base: un año más de caída mientras limpia el mercado (guía de FY2027), crecimiento de 3-4% "
           "desde FY2028 liderado por Norteamérica, Gran China que se estabiliza y un margen que sube a 11% con los ahorros de Pace. "
           "La marca gana sobre su costo de capital, pero la ventaja se desvanece: ROIC terminal de 12,3%."),
    "G10": "Año 1 −6,6% (guía FY2027: caída de un dígito alto); años 2-5 ~3,4% con Norteamérica y la estabilización de China.",
    "G11": "Año 1 ~6% (guía FY2027); objetivo 11% (11,6% con arrendamientos) en 6 años con Pace y menos descuentos.",
    "G12": "22% (LTM 20,7%, guía FY2027 ~25%) que converge a la marginal de 25%.",
    "G13": "2,1 en los años 1-10: promedio global de Shoe; Nike rota hoy su capital ~2,6 veces.",
    "G14": "ROIC actual ~15%; terminal 12,3%: ventaja que se desvanece (punto medio con el costo de capital terminal).",
    "G15": "Ke 9,37% (rf 5,24% + beta 1,01 × ERP 4,09%); Kd 6,02% (A2/A); WACC ~8,65%.",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": -0.066, "D6": "Guía FY2027 (1-oct-2026): caída de un dígito alto; Gran China, Converse, NIKE Sportswear y Jordan a la baja.",
    "C7": 0.06, "D7": "Guía FY2027: BPA ajustado US$1,15-1,35 con impuestos ~25% sobre ventas ~8% menores.",
    "C8": 0.034, "D8": "Historia Base: Norteamérica ~4%, EMEA y APLA ~3,5%, Gran China se estabiliza, Converse plano.",
    "C9": 0.116, "D9": "11% reportado + 0,6 pp de arrendamientos; FY2017-FY2024 fue 12-16% con más venta directa.",
    "C10": 6, "D10": "Los ahorros de Pace (US$2.500M brutos) se completan en FY2031.",
    "C11": 2.1, "D11": "Promedio global de Shoe (2,12); Nike rota su capital ~2,6 veces.",
    "C12": 2.1, "D12": "Promedio global de Shoe (2,12).",
}

MULTIPLOS_EVALUACION = (
    "Evaluación NKE (2-oct-2026): los múltiplos Base salen de tres anclas (historia desde FY2025, la etapa de reestructuración; peers "
    "sin Under Armour con −5%; y el justificado, λ = 0,5). Los peers cotizan hoy a múltiplos bajos (Lululemon y Deckers a 8-11 veces "
    "utilidades) y la historia de Nike a múltiplos de la era de crecimiento: el promedio queda cerca del DCF Base. El DCF es el valor "
    "intrínseco; los múltiplos son precio relativo."
)

VO, INP, COC, RES, ESC = ("'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'",
                          "'Escenarios e historias'")

TESIS_ROWS: list[list] = [
    ["NKE (NIKE, Inc.) — Tesis de Inversión: De la Historia a los Números (análisis desde cero, 2-oct-2026)"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al 1-oct-2026: US$"&TEXT({RES}!B3;"0.00")&" | WACC inicial: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["Nike es la marca deportiva más grande del mundo, pero lleva dos años de reestructuración: ventas −10% en FY2025, planas en "
     "FY2026 y con una caída de un dígito alto esperada en FY2027 mientras limpia el mercado de franquicias clásicas y vuelve a los "
     "mayoristas. El margen normalizado (~6,9%) es la mitad del histórico. Norteamérica ya crece; Gran China y Converse siguen "
     "cayendo. La tensión: si la Sport Offense y Pace devuelven a Nike a crecer con márgenes de dos dígitos, o si la marca perdió "
     "relevancia frente a On, Hoka y las marcas chinas de forma permanente."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["Norteamérica +2% con mayoristas +9% en el 1T FY27; el rendimiento deportivo (running, fútbol, básquet) gana tracción.",
     "Guía FY2027: ventas con caída de un dígito alto; Gran China −22% y Converse −28% en el 1T FY27."],
    ["Margen bruto +60 pb y gastos generales −6% en el 1T FY27; Pace apunta a US$2.500M de ahorros brutos a FY2031.",
     "Margen normalizado ~6,9% frente a 12-16% histórico; más mayoristas implica menos margen que la venta directa."],
    ["Balance sólido: caja de US$8.368M, calificación A2/A+, dividendo de ~4,7%.",
     "Pérdida de atletas (Mbappé a On) y de participación en running frente a On y Hoka; NIKE Direct digital −13%."],
    ["La marca ya salió de crisis parecidas (1998, 2016-2017) con innovación y marketing.",
     "Sale del S&P 100 y la acción toca mínimos de 52 semanas; la gerencia anticipa más despidos en 2027."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — CASO BASE DE LA HOJA (= historia Base; fórmulas vivas)"],
    ["Supuesto", "Conservador técnico", "Base", "Optimista técnico", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={INP}!B27", f"={VO}!C106",
     "Base −6,6%: guía FY2027 de caída de un dígito alto (comunicado del 1-oct-2026); por región, historia Base."],
    ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={INP}!B29", f"={VO}!D106",
     "Base ~3,4%: Norteamérica ~4%, EMEA y APLA ~3,5%, Gran China se estabiliza y Converse queda plano."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "~6%: guía FY2027 (BPA ajustado US$1,15-1,35 con impuestos ~25% sobre ventas ~8% menores)."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 11,6% (11% + arrendamientos): Pace y menos descuentos, sin volver al 12-16% de la era de venta directa."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31", "6 años: los ahorros de Pace se completan en FY2031."],
    ["Sales-to-Capital (años 1-5)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "2,1 (también en los años 6-10): promedio global de Shoe; Nike rota hoy su capital ~2,6 veces."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "rf 5,24% (UST 10 años, 1-oct-2026) + beta 1,01 (Shoe global reapalancada) × ERP 4,09% (Damodaran, sep-2026); Kd 6,02% (A2/A)."],
    ["Referencia: margen base normalizado (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "EBIT GAAP LTM US$3.758M − US$986M de aranceles devueltos + US$385M de indemnizaciones = US$3.157M (+ arrendamientos)."],
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
    ["4. LOG DE CORRECCIONES Y AJUSTES (respaldo de cada celda en reference/backups/nke_desde_cero_2026-10-02.json del repo JMR-valuation)"],
    ["#", "Celda / componente", "Antes", "Después", "Razón"],
    [1, "Income Statement y Balance Sheet columna L", "Copia de FY2026 (may-2026)", "LTM a ago-2026 y balance al 31-ago-2026", "El pipeline repetía el cierre anual; se suma el 1T FY27 (comunicado del 1-oct-2026)."],
    [2, "Income Statement filas 15 y 17", "Gasto por intereses 0; el ingreso como gasto", "Gasto bruto (US$228M en FY2026)", "Ingreso por intereses − neto (10-K); otros ingresos sin el gasto."],
    [3, "Input sheet!B13 (EBIT base)", "=L12 (US$3.797M de FY2026)", "=L12 − 986 + 385 (US$3.157M)", "Devolución de una vez de aranceles IEEPA e indemnizaciones de FY2026 (10-K)."],
    [4, "Input sheet!B16 (deuda)", "US$10.555M con arrendamientos contables", "US$7.893M nominal", "Los arrendamientos entran por el conversor (B18 = Yes)."],
    [5, "Input sheet!B17 / B18", "I+D Yes · arrendamientos No", "No · Yes", "Nike no reporta I+D; arrendamientos como deuda (Damodaran)."],
    [6, "Input sheet!B22 / B24 / B38-B42", "1.481,0M (promedio diluido) · 20,3% · sin opciones", "1.496,0M (con RSU) · 22% · 76,8M opciones a US$96,44", "Portada y notas del 10-K FY2026; guía de tasa de FY2027."],
    [7, "Operating lease converter", "Plantilla", "Costo US$693M y compromisos al 31-may-2026", "10-K FY2026, nota de arrendamientos."],
    [8, "Cost of capital worksheet", "ERP de enero", "Beta Shoe global · rating A2/A · ERP 4,09%", "ERP de sep-2026; rating real (Moody's A2, S&P A+)."],
    [9, "Input sheet!B4 / D1 / B35 / B49-B50", "Fecha y precio de la corrida", "1-oct-2026 · US$35,15 · 5,24% · ROIC terminal 12,3%", "Fecha de corte; criterio de ventaja que se desvanece."],
    [10, "Descuento de múltiplos fila 38 / 43", "DCF técnico · MOS sobre el ponderado", "Historias · MOS sobre el esperado", "Presentación vigente (1-oct-2026)."],
    [],
    ["5. CONCLUSIÓN"],
    [f'="El DCF Base de las historias es US$"&TEXT({ESC}!H5;"0.00")&" y el esperado US$"&TEXT({ESC}!H10;"0.00")&"; el precio del 1-oct-2026 (US$"&TEXT({RES}!B3;"0.00")&") está "&TEXT({RES}!B3/{ESC}!H5-1;"+0%;-0%")&" frente a la Base. Los múltiplos (US$"&TEXT(\'Descuento de múltiplos\'!D39;"0.00")&") quedan cerca del DCF. El valor depende del margen al que vuelva Nike y de cuánto dure la caída, no de un múltiplo de mercado."'],
    ["Variable clave a monitorear: el crecimiento de Norteamérica, el margen bruto y Gran China. Si las ventas vuelven a crecer en FY2028 con margen bruto de 44% o más, el caso se mueve hacia la Optimista; si FY2028 vuelve a caer o el margen bruto baja de 41%, hacia la Conservadora o la Disrupción."],
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
