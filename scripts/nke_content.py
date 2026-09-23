"""Contenido cualitativo de la valoracion de NKE (pasos 3 y 9). Las cifras
de resultado de la Tesis son formulas vivas contra el modelo."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: 10-K FY2026 de NIKE (SEC EDGAR, XBRL, cierre 31-may-2026); comunicado de resultados Q4 FY2026 "
    "(30-jun-2026) y llamada con inversores; CNBC, Yahoo Finance, Motley Fool, ad-hoc-news e Investing.com "
    "(jun-sep 2026); Moody's (baja a A2, nov-2025); Damodaran Online (indname.xls ene-2026, ERPbymonth "
    "sep-2026); UST 10 años al 22-sep-2026; consenso de analistas vía yfinance (22-sep-2026)."
)

CUALITATIVO = {
    "B5": "NIKE, Inc.",
    "B6": "Elliott Hill (CEO desde oct-2024). CFO: David Denton desde el 17-ago-2026 (reemplazó a Matthew Friend).",
    "B7": "Calzado e indumentaria deportiva (Damodaran: Shoe)",
    "B8": "https://about.nike.com  |  IR: https://investors.nike.com",
    "B11": "Descripción",
    "B12": ("La mayor marca deportiva del mundo: ingresos FY2026 (a may-2026) de US$46.400M, planos (−2% sin efecto "
            "cambiario). Vende calzado, indumentaria y equipamiento bajo NIKE, Jordan y Converse, a través de "
            "mayoristas (US$27.500M, +6%) y de venta directa NIKE Direct (US$17.700M, −6%). Tiene ~73.000 empleados."),
    "A13": "NIKE Brand (calzado, indumentaria, Jordan)",
    "B13": ("US$45.200M en FY2026 (+1%, −1% sin efecto cambiario), el 97% de los ingresos. El plan \"Win Now\" de "
            "Hill reorienta la marca al deporte (running, básquet, fútbol) después de años de depender de "
            "franquicias de estilo de vida (Dunk, Air Force 1) que se saturaron."),
    "A14": "Converse",
    "B14": ("US$1.200M en FY2026 (−31%; −32% sin efecto cambiario); en el Q4 cayó 32%. Es la marca en peor "
            "momento del grupo y un candidato natural a reestructuración o venta."),
    "A15": "Geografías",
    "B15": ("Norteamérica es la región que crece. Greater China cayó 12% en el Q4 FY2026 y EMEA también está en "
            "baja. Las ventas internacionales tardan más en recuperarse de lo previsto."),
    "A16": "Estrategia de Distribución\ny Comercialización",
    "B16": ("Revierte la apuesta de 2020-2023 por la venta directa: vuelve al canal mayorista (Foot Locker, Dick's, "
            "JD), que crece 6% mientras NIKE Direct cae 6% y el digital 12%. Menos promociones y liquidación de "
            "inventario antiguo (inventario de US$7.500M, plano)."),
    "B21": "Argumento",
    "A22": "El reseteo mayorista funciona",
    "B22": ("Mayoristas +6% en FY2026 (+4% sin efecto cambiario) y +4% en el Q4; Norteamérica creciendo. La "
            "empresa espera que el margen bruto empiece a expandirse desde el Q1 FY2027, antes de lo previsto, "
            "por acciones de costos en la cadena de suministro."),
    "A23": "Balance y dividendo",
    "B23": ("Caja e inversiones de corto plazo de US$9.000M y deuda de US$7.900M; rating A2 (Moody's) / A+ "
            "(S&P). Dividendo de US$1,64 por año (~4,5% de rendimiento) que sigue creciendo (+5% en FY2026)."),
    "A24": "Valuación deprimida",
    "B24": ("Cotiza cerca de mínimos de 12 años, ~45% debajo del máximo de 52 semanas (más de US$64). A ~17x la "
            "utilidad LTM, contra 22-62x históricos. Si el margen vuelve al 13-15% de FY2021-FY2024, la acción "
            "tiene recorrido."),
    "B27": "Riesgo",
    "A28": "Pérdida de relevancia frente a nuevas marcas",
    "B28": ("On, Hoka (Deckers) y otras le ganan cuota en running. En sep-2026 Kylian Mbappé dejó Nike por On "
            "tras 20 años. NIKE Direct −8% y digital −12% sin efecto cambiario en FY2026."),
    "A29": "Márgenes subyacentes en caída",
    "B29": ("Sin el reembolso único de aranceles de US$986M, el margen bruto FY2026 fue 40,8% (−190pb) y el EPS "
            "US$1,58 (−27%). FCF de US$2.180M (−33%). Los aranceles pasan de 10% a 15% desde agosto de 2026."),
    "A30": "Guía débil y presión de mercado",
    "B30": ("Guía H1 FY2027: ingresos con caída de un dígito bajo a medio y utilidades planas. En sep-2026, "
            "bajas de recomendación de Baird (a Neutral, precio objetivo de US$70 a US$44), UBS (US$42), Telsey "
            "(US$44) y Stifel (US$40); salida del S&P 100 el 21-sep-2026."),
    "A32": SOURCES,
    "A35": "Periodo del Reporte: 30 de junio de 2026 – 22 de septiembre de 2026",
    "B38": "Titular",
    "A39": "Resultados",
    "B39": "Q4 FY2026: ingresos −1% y reembolso de aranceles de US$986M",
    "D39": "Ingresos de US$11.000M (−4% sin efecto cambiario); margen bruto de 49,2% con +900pb del reembolso IEEPA; EPS de US$0,72 (US$0,20 sin el reembolso).",
    "A40": "Guía",
    "B40": "H1 FY2027: ingresos con caída de un dígito bajo a medio",
    "D40": "Utilidades planas en el H1; margen bruto levemente positivo en el Q1; aranceles de 15% desde agosto. Resultados del Q1 FY2027 el 1-oct-2026.",
    "A41": "Gestión",
    "B41": "Cambio de CFO: David Denton reemplaza a Matthew Friend",
    "D41": "Efectivo desde el 17-ago-2026.",
    "A42": "Marketing / Deportes",
    "B42": "Kylian Mbappé deja Nike y firma con On",
    "D42": "Fin de una relación de 20 años (sep-2026); una señal de la competencia de las marcas nuevas en fútbol y running.",
    "A43": "Mercado / Wall St.",
    "B43": "Salida del S&P 100 y ola de bajas de recomendación",
    "D43": "Salió del S&P 100 el 21-sep-2026 (sigue en el S&P 500). Baird, UBS, Telsey y Stifel recortaron; el consenso es Mantener con precio objetivo de ~US$48.",
    "B46": "Análisis e impacto en la valoración",
    "A47": "El reembolso de aranceles distorsiona FY2026",
    "B47": ("Los US$986M de recupero de aranceles IEEPA se registraron en el Q4 FY2026 y explican casi todo el "
            "EBIT reportado de más: sin ellos, el EBIT es ~US$2.811M (6,1%) contra US$3.797M (8,2%). Al 31-may "
            "se habían cobrado solo US$302M. Impacto: el modelo usa el EBIT normalizado como base (Input!B13) y "
            "suma los US$684M pendientes como activo no operativo."),
    "A48": "Guía FY2027 y aranceles",
    "B48": ("La empresa espera que los ingresos caigan un dígito bajo a medio en el H1 FY2027, con utilidades "
            "planas. Asume aranceles incrementales de 10% hasta julio y 15% después, y adelantó la expansión del "
            "margen bruto al Q1 por ahorros en la cadena de suministro. El consenso FY2027 es de ingresos −1,9% "
            "(US$45.500M) y EPS de US$1,69. Es el ancla del Año 1 del Base (−2%, margen 6,5%)."),
    "A49": "Competencia y marca",
    "B49": ("La salida de Mbappé a On (sep-2026) simboliza la pérdida de relevancia frente a marcas nuevas. "
            "NIKE Direct y el digital siguen cayendo (−8% y −12% sin efecto cambiario) y Converse −32%. El "
            "reseteo mayorista compensa en volumen pero con menor margen: ancla del margen objetivo Base (11%), "
            "por debajo del promedio histórico."),
    "A50": "Presión de mercado",
    "B50": ("La acción perdió ~45% desde su máximo de 52 semanas, salió del S&P 100 y recibió 4 bajas de "
            "precio objetivo la semana del 18-sep antes del Q1 FY2027 (1-oct). El consenso de 36 analistas es "
            "Mantener, con precio objetivo medio de US$47,7 (rango US$23-94)."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 73000,
    "B12": "='Income Statement'!L30", "B13": "='Income Statement'!L13",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "='Eficiencia de capital'!L5", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12",
    # Consenso EPS (yfinance, 22-sep-2026): FY27 US$1,69 / FY28 US$2,14 -> NTM ~US$1,84
    "E13": "='Input sheet'!D1/1,84", "E14": "=E13/16,4",
    "E16": "=IFERROR('Trailing Valuation'!L6/'Financials Multiples'!E57;\"\")",
    "E20": "='Balance Sheet'!L5", "E23": "='Income Statement'!L12/'Income Statement'!L16",
    "H4": "=('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1",
    "H5": "=('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1",
    "H6": "=('Income Statement'!K3/'Income Statement'!B3)^(1/9)-1",
    "H7": "=('Income Statement'!K24/'Income Statement'!H24)^(1/3)-1",
    "H8": "=('Income Statement'!K24/'Income Statement'!F24)^(1/5)-1",
    "H9": "=('Income Statement'!K24/'Income Statement'!B24)^(1/9)-1",
    "H10": "=('Cash Flow Statement'!K36/'Cash Flow Statement'!F36)^(1/5)-1",
    "H11": "=('Income Statement'!K26/'Income Statement'!F26)^(1/5)-1",
    "H12": "=(47134/46398)^(1/2)-1",   # consenso ingresos FY2028 vs FY2026
    "H13": "=('Financials Multiples'!F57/'Income Statement'!K28)^(1/2)-1",
    "H14": "=(2,14/1,58)^(1/2)-1",      # consenso EPS FY2028 vs EPS subyacente FY2026 (sin aranceles)
    "H15": 0.164,
    "H18": "=1,64/'Input sheet'!D1", "H19": "=1,64/'Income Statement'!L24", "H20": 1.64,
    "H21": "=(1,64/1,18)^(1/3)-1", "H22": "=(1,64/0,98)^(1/5)-1", "H23": "—", "H24": "—",
}

STORIES = {
    "A3": "Nike: la marca más grande del deporte en medio de un reseteo que el mercado todavía no sabe si funciona",
    "A4": ("Nike vende US$46.400M por año, pero sus ingresos no crecen desde FY2023 y su margen operativo subyacente cayó "
           "de ~13% a ~6% (sin el reembolso de aranceles de FY2026). El nuevo CEO revirtió la estrategia de venta directa, "
           "volvió a los mayoristas y reorientó la marca al deporte, mientras On y Hoka le ganan cuota y los aranceles "
           "suben. La tesis Base: un FY2027 todavía en caída (−2%), una recuperación gradual (3,5% por año) y un margen "
           "que sube a 11% en 7 años, por debajo de su historia por aranceles y competencia, con costo de capital de 8,6%."),
    "G10": "Guía H1 FY2027 con caída de un dígito bajo a medio; consenso FY2027 −1,9% y FY2028 +3,5% -> Año 1 −2%, años 2-5 +3,5%.",
    "G11": "Año 1 6,5% (subyacente FY2026 6,1% + expansión de margen bruto guiada desde el Q1). Converge a 11% en 7 años.",
    "G12": "Tasa efectiva FY2026 de 20,3% que converge a la marginal de 25%.",
    "G13": "2,1x: relación marginal FY2020-FY2026 (ΔIngresos US$9.000M / ΔCapital invertido US$4.400M).",
    "G14": "ROIC actual ~17% (sobre el EBIT normalizado); la marca sostiene retornos sobre el costo de capital.",
    "G15": "8,6%: beta de industria Shoe (desapalancada 0,89, relevered ~1,0), rating A2/A, ERP de 4,09% (sep-2026).",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": -0.02, "D6": "Consenso FY2027 −1,9% y guía H1 FY2027 de caída de un dígito bajo a medio.",
    "C7": 0.065, "D7": "EBIT subyacente FY2026 6,1% (sin los US$986M de aranceles) + expansión de margen bruto guiada desde el Q1 FY2027.",
    "C8": 0.035, "D8": "Consenso FY2028 +3,5%; CAGR de 10 años de Nike 3,4%.",
    "C9": 0.11, "D9": "Por debajo del promedio FY2017-FY2024 (12,5%) por aranceles de 15% y más competencia; comparables: Lululemon 13%, Deckers 15%, Adidas ~8,5%.",
    "C10": 7, "D10": "El turnaround recién empieza y la mejora de margen no está demostrada.",
    "C11": 2.1, "D11": "Bottom-up FY2020-FY2026: ΔIngresos / ΔCapital invertido.",
    "C12": 2.1, "D12": "Modelo con activos propios (tiendas y centros de distribución) estable.",
}

MULTIPLOS_EVALUACION = (
    "Evaluación NKE: P/E, EV/EBITDA, EV/FCFF y P/OCF fueron positivos los 4 años, así que el mecanismo nativo (MIN de 4 "
    "años) funciona. OJO: esos 4 años (may-2023 a may-2026) son ANTERIORES al derrumbe de 2026, así que el MIN (P/E 22x, "
    "EV/EBITDA 15,5x) queda por encima del múltiplo de hoy (P/E LTM 17x, EV/EBITDA 12x) y los múltiplos dan precios "
    "mayores que el DCF. P/FCFE: el FCFE de FY2026 fue NEGATIVO (−US$734M) y el MIN de 4 años daba −93x -> se reemplazó "
    "(J8/J19/J30 de la hoja PFCFE) por el múltiplo implícito del DCF de cada escenario (equity / FCFE FY+1). Además, el "
    "NWC proyectado de 'Financials Multiples' se recalculó con intensidad de NWC (ver log de la Tesis)."
)

VO, INP, COC, RES = "'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'"

TESIS_ROWS: list[list] = [
    ["NKE (NIKE, Inc.) — Tesis de Inversión: De la Historia a los Números"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al día del análisis: US$"&TEXT({RES}!C25;"0.00")&" (22-sep-2026) | WACC: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["Nike está en el peor momento de su historia reciente: ingresos planos por 3 años, margen operativo subyacente de ~6% "
     "(contra 13-15% en FY2021-FY2024), la acción en mínimos de 12 años y fuera del S&P 100. La pregunta es si el reseteo "
     "de Elliott Hill (volver a los mayoristas, al deporte y a menos promociones) recupera márgenes cerca de su historia, o "
     "si aranceles de 15% y marcas como On y Hoka dejaron a Nike en un nivel estructuralmente más bajo. El reembolso único "
     "de aranceles de US$986M hace que FY2026 parezca mejor de lo que fue: el modelo parte del EBIT normalizado (6,1%). "
     "Con una recuperación gradual a 11%, el DCF vale menos que el precio actual: el mercado ya descuenta una recuperación "
     "más fuerte que la del caso Base."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["Mayoristas +6% en FY2026 (+4% sin efecto cambiario) y +4% en el Q4, con Norteamérica creciendo: el reseteo con los retailers funciona.",
     "NIKE Direct −8% y digital −12% sin efecto cambiario (FY2026); Greater China −12% y Converse −32% en el Q4."],
    ["Expansión de margen bruto adelantada al Q1 FY2027 por ahorros en la cadena de suministro (guía del 30-jun-2026).",
     "Sin el reembolso de aranceles: margen bruto FY2026 de 40,8% (−190pb), EPS de US$1,58 (−27%) y FCF de US$2.180M (−33%). Los aranceles suben a 15% desde agosto."],
    ["Balance sólido (caja e inversiones de corto plazo de US$9.000M, A2/A+) y dividendo de US$1,64 (~4,5%) que sigue creciendo.",
     "Guía H1 FY2027: ingresos con caída de un dígito bajo a medio y utilidades planas. On y Hoka ganan cuota; Mbappé se fue a On (sep-2026)."],
    ["Acción ~45% debajo del máximo de 52 semanas y a ~17x la utilidad LTM, contra 22-62x históricos: si vuelve el margen de 13%, hay recorrido.",
     "Bajas de Baird, UBS, Telsey y Stifel (sep-2026) antes del Q1 FY2027 (1-oct) y salida del S&P 100: el mercado desconfía del ritmo del turnaround."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — LOS TRES ESCENARIOS (fórmulas vivas del modelo)"],
    ["Supuesto", "Conservador", "Base", "Optimista", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={INP}!B27", f"={VO}!C106",
     "Base −2%: consenso FY2027 −1,9% y guía H1 FY2027 de caída de un dígito bajo a medio. Conservador −3%: la caída del H1 se extiende. Optimista +4,5%: recuperación inmediata (CAGR Base +1pp)."],
    ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={INP}!B29", f"={VO}!D106",
     "Base 3,5%: consenso FY2028 +3,5% y CAGR de 10 años de Nike (3,4%). No desacelera respecto del Año 1 porque el Año 1 es de contracción (turnaround). Desde el año 6 convergen a la tasa libre de riesgo."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "6,5% contra una base normalizada de 6,1% ('Valuation output'!B6, EBIT FY2026 sin los US$986M de aranceles): la guía adelanta la expansión de margen bruto al Q1 FY2027."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 11%: por debajo del promedio FY2017-FY2024 (12,5%) por aranceles de 15% y más competencia; comparables Lululemon 13%, Deckers 15%, Adidas ~8,5%. Conservador: se estanca en el Año 1 (6,5%). Optimista: vuelve al promedio FY2021-FY2024 (13,4%)."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31",
     "7 años: el turnaround recién empieza y la mejora todavía no se ve en los resultados."],
    ["Sales-to-Capital (años 1-5 / 6-10)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "2,1x bottom-up: ΔIngresos FY2020-FY2026 (+US$9.000M) / ΔCapital invertido (+US$4.400M)."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "Tasa libre de riesgo 4,96% (UST 10 años, 22-sep-2026) + beta ~1,0 (Damodaran Shoe desapalancada 0,89 relevered; comparables 0,76-2,0, mediana 1,06) x ERP 4,32% (1-sep-2026) = Ke 9,3%. Kd 5,74% (A2/A). D/(D+E) 13%."],
    ["Referencia: margen base normalizado (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "EBIT FY2026 reportado US$3.797M − reembolso único de aranceles US$986M = US$2.811M."],
    [],
    ["3. RESULTADO DEL DCF POR ESCENARIO"],
    ["Escenario", "Valor DCF / acción", "Precio Objetivo Ponderado*", "DCF vs. precio actual", "Ponderado vs. precio actual"],
    ["Conservador", f"={VO}!B86", f"={RES}!C12", f"=B26/{INP}!$B$23-1", f"=C26/{INP}!$B$23-1"],
    ["Base", f"={VO}!B35", f"={RES}!D12", f"=B27/{INP}!$B$23-1", f"=C27/{INP}!$B$23-1"],
    ["Optimista", f"={VO}!B137", f"={RES}!E12", f"=B28/{INP}!$B$23-1", f"=C28/{INP}!$B$23-1"],
    ["Precio actual (GOOGLEFINANCE)", f"={INP}!B23", "Precio al día del análisis", f"={RES}!C25"],
    [f'=IF(AND(B26<B27;B27<B28;C26<C27;C27<C28;{VO}!C55<{INP}!B27;{INP}!B27<{VO}!C106;{VO}!C45<{VO}!C46;{VO}!C46<{VO}!C47);"✔ Orden verificado: Conservador < Base < Optimista en crecimiento, margen objetivo, valor DCF y precio ponderado";"✖ REVISAR: el orden Conservador < Base < Optimista no se cumple")'],
    ["*El Precio Objetivo Ponderado combina el DCF (40%) con 5 múltiplos (EV/EBITDA 20%, P/E 20%, EV/FCFF 10%, P/FCFE 5%, P/OCF 5%) según la categoría 'Madura'. Los múltiplos dan precios muy superiores al DCF porque su ancla (MIN de 4 años) es de may-2023 a may-2026, antes del derrumbe de la acción: P/E 22x contra 17x hoy. Tomar el DCF como la lectura más confiable y los múltiplos como techo si vuelve la valuación histórica."],
    [],
    ["4. LOG DE CORRECCIONES ESTRUCTURALES Y AJUSTES (backup de cada fórmula en reference/backups/nke_formula_backup.json del repo JMR-valuation)"],
    ["#", "Celda / componente", "Antes", "Después", "Razón"],
    [1, "Loader SEC: EBIT", "0 (Nike nunca taggea OperatingIncomeLoss)", "Gross Profit − SG&A: FY2026 US$3.797M", "Arreglado en el loader antes de esta hoja (PR #2)."],
    [2, "Loader SEC: pasivos totales (Balance Sheet fila 29)", "0 y 'Otros pasivos LP' negativos", "(Pasivo + Patrimonio) − Patrimonio: US$23.545M", "Nike no taggea 'Liabilities'."],
    [3, "Loader SEC: D&A FY2017-FY2022", "0 (EBITDA = EBIT)", "706 … 717 (tag 'Depreciation')", "El tag combinado de D&A recién existe desde FY2023."],
    [4, "Loader SEC: inversiones de corto plazo", "0", "US$1.464M (títulos de deuda disponibles para la venta, corrientes)", "Nike no usa 'ShortTermInvestments'."],
    [5, "Income Statement filas 15-16 (intereses)", "El INGRESO por intereses (278) figuraba como gasto", "Gasto bruto = ingreso − neto: FY2026 US$228M", "Nike solo taggea el ingreso y el neto."],
    [6, "Input sheet!B13 (EBIT base)", "=L12 (US$3.797M, 8,2%)", "=L12 − 986 (US$2.811M, 6,1%)", "Reembolso único de aranceles IEEPA registrado en el Q4 FY2026."],
    [7, "Input sheet!B20 (activos no operativos)", "=L14+L15 -> 8.512 (activos LP operativos)", "=L14 + 684 (reembolso de aranceles por cobrar)", "Other LT Assets es operativo; los US$684M se cobran en FY2027."],
    [8, "Input sheet!B24 / B1 / B17", "Tasa efectiva de Dec '23 · TICKER vacío · I+D = Yes", "LTM 20,3% · =A1 · No", "Bugs de la plantilla; Nike no reporta I+D por separado."],
    [9, "Valuation output!C106 (crecimiento Optimista)", "=B27×1,3 -> −2,6% (MENOR que el Base −2%)", "=B29+1pp -> 4,5%", "Bug #11 del apéndice: con crecimiento negativo, multiplicar por 1,3 lo empeora."],
    [10, "Valuation output!C55 (crecimiento Conservador)", "=PROMEDIO(B27;rf) -> +1,5% (MAYOR que el Base)", "=B27−1pp -> −3%", "Bug #10 del apéndice."],
    [11, "Valuation output!C45 / C47 (márgenes de escenario)", "=B6 (8,2% con el reembolso) / =B30+5%", "=B28 (6,5%) / =PROMEDIO(FY2021-FY2024) 13,4%", "Anclas reales: estancamiento en el Año 1 / regreso a márgenes previos al deterioro."],
    [12, "Financials Multiples: NWC proyectado (filas 22/61/101)", "PROMEDIO(ΔNWC/ΔIngresos): con FY2026 casi plano (+US$89M) el ratio daba 21x -> NWC +US$11.000M/año; H42/H82 vacías", "Intensidad de NWC (NWC/Ingresos, promedio de 3 años) × ΔIngresos", "FCFF/FCFE/OCF proyectados daban negativos y precios objetivo de −US$130 a +US$924."],
    [13, "PFCFE!J8/J19/J30", "MIN de 4 años = −93x (FCFE FY2026 −US$734M)", "Implícito del DCF: equity / FCFE FY+1 (13,6x / 25,4x / 38,1x)", "Paso 6: el múltiplo cambia de signo."],
    [14, "Cost of capital worksheet", "Rating A1/A+ · rf 4,99% · ERP 4,23% · vencimiento 3", "A2/A · 4,96% · 4,09% · 9 años", "Moody's bajó a A2 (nov-2025); datos de mercado de sep-2026."],
    [15, "Option value / Cost of capital B24 / Financials Multiples", "#DIV/0! (bug #5 y tablas vacías)", "IFERROR", "Barrido de errores (paso 8)."],
    [f'="Resultado: DCF Base US$"&TEXT({VO}!B35;"0.00")&" (Conservador US$"&TEXT({VO}!B86;"0.00")&", Optimista US$"&TEXT({VO}!B137;"0.00")&"); precio ponderado Base US$"&TEXT({RES}!D12;"0.00")&"."'],
    [],
    ["5. CONCLUSIÓN"],
    [f'="A US$"&TEXT({INP}!B23;"0.00")&", Nike cotiza por ENCIMA de su DCF Base (US$"&TEXT({VO}!B35;"0.00")&", "&TEXT({VO}!B35/{INP}!B23-1;"+0%;-0%")&") y cerca del Optimista (US$"&TEXT({VO}!B137;"0.00")&"): el mercado ya paga por una recuperación del margen hacia ~13%. El precio ponderado Base (US$"&TEXT({RES}!D12;"0.00")&") es mayor solo porque los múltiplos históricos son de antes del derrumbe. No hay margen de seguridad en el DCF: la tesis alcista necesita que el turnaround sea más rápido y profundo que el caso Base."'],
    ["Variable clave a monitorear: el margen bruto sin aranceles extraordinarios (40,8% en FY2026). Si el Q1 FY2027 (1-oct-2026) confirma la expansión guiada y NIKE Direct deja de caer, el caso se mueve hacia el Optimista (margen de 13%); si el margen bruto sigue bajo presión por aranceles de 15% y promociones, se mueve al Conservador (margen de ~6,5% permanente)."],
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
        sh, TESIS_ROWS, backup_path, text_rows=range(34, 49),
        merges=[f"A{r}:E{r}" for r in (1, 2, 5, 30, 31, 33, 50, 53, 54, 56)] + [f"B{r}:E{r}" for r in range(7, 12)],
        bold_rows=(4, 13, 24, 33, 52), head_rows=(7, 14, 25, 34),
        formats=[
            {"range": "B15:D18", "format": pct}, {"range": "B22:D22", "format": pct},
            {"range": "B19:D19", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0"}}},
            {"range": "B20:D20", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}},
            {"range": "B21:D21", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0.00%"}}},
            {"range": "B26:C29", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
            {"range": "D29", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
            {"range": "D26:E28", "format": {"numberFormat": {"type": "PERCENT", "pattern": "+0.0%;-0.0%"}}},
            {"range": "A30", "format": {"textFormat": {"bold": True}}},
        ])
