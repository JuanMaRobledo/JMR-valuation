"""Contenido cualitativo de la valoracion de NVO (pasos 3 y 9). Las cifras
de resultado de la Tesis son formulas vivas contra el modelo."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: 20-F 2019-2025 de Novo Nordisk (SEC EDGAR, XBRL ifrs-full); 6-K del 4-ago-2026 (informe financiero H1 "
    "2026) y del 4-feb-2026 (resultados 2025 y guía 2026); comunicados del Capital Markets Day (21-sep-2026); Rio Times, "
    "24/7 Wall St., Yahoo Finance, Investing.com, TipRanks y BioSpace (ago-sep 2026); S&P (AA, may-2025) y Moody's "
    "(Aa3, ene-2025); Damodaran Online (indname ene-2026, ERP sep-2026); UST 10 años y DKK/USD al 23-sep-2026; consenso "
    "de analistas vía yfinance (23-sep-2026). Cifras en DKK convertidas a US$ a 6,5297 DKK/US$."
)

CUALITATIVO = {
    "B5": "Novo Nordisk A/S (ADR NVO en NYSE; acciones B en Nasdaq Copenhague)",
    "B6": "Mike Doustdar (CEO desde ago-2025). CFO: Karsten Munk Knudsen.",
    "B7": "Farmacéutica: diabetes, obesidad y enfermedades raras (Damodaran: Drugs (Pharmaceutical))",
    "B8": "https://www.novonordisk.com  |  IR: https://www.novonordisk.com/investors.html",
    "B11": "Descripción",
    "B12": ("Líder mundial en GLP-1 (semaglutida: Ozempic, Wegovy, Rybelsus) e insulinas. Ventas 2025 de DKK 309.100M "
            "(US$47.300M, +10% a tipo de cambio constante) con margen operativo de 41%. En el H1 2026 las ventas "
            "ajustadas (sin la reversión 340B) crecieron 2% a tipo de cambio constante. 68.794 empleados a dic-2025 "
            "(−10% tras el recorte de ~9.000 puestos de sep-2025)."),
    "A13": "Obesidad (Wegovy inyectable, Wegovy pill, Wegovy HD)",
    "B13": ("DKK 44.100M en el H1 2026 (+19% a tipo de cambio constante), 30% de las ventas ajustadas. Wegovy pill "
            "(lanzada en EE.UU. el 5-ene-2026) facturó DKK 5.500M en el semestre y superó 265.000 recetas "
            "semanales: el mejor lanzamiento de un GLP-1 en volumen. Wegovy HD (7,2 mg) se lanzó en EE.UU. en abril."),
    "A14": "Diabetes (Ozempic, Rybelsus/Ozempic pill, insulinas)",
    "B14": ("DKK 95.400M en el H1 2026 (−5% a tipo de cambio constante), 64% de las ventas ajustadas. Ozempic "
            "DKK 59.200M (−2%), Rybelsus DKK 9.800M (−9%). Presión de precios en EE.UU. (acuerdo MFN) y "
            "genéricos de semaglutida en Canadá, China y otros mercados internacionales desde 2026."),
    "A15": "Enfermedades raras y geografías",
    "B15": ("Enfermedades raras (hemofilia, hormona de crecimiento): DKK 9.100M en el H1 2026 (+2%). Por geografía, "
            "EE.UU. cae 4% (ajustado) y las Operaciones Internacionales crecen 8% (EUCAN +20%, China 0%)."),
    "A16": "Estrategia de Distribución\ny Comercialización",
    "B16": ("Bajar el precio para ganar volumen: en EE.UU., acuerdo \"Most Favoured Nations\" con el gobierno "
            "(nov-2025), cobertura de Medicare para obesidad vía el programa Bridge (desde el 1-jul-2026), canal de "
            "autopago (NovoCare Pharmacy, telemedicina) a US$149-299 por mes, y recorte del precio de lista (WAC) de "
            "Wegovy y Ozempic desde el 1-ene-2027. Fuera de EE.UU., lanzamientos de Wegovy en ~60 países."),
    "B21": "Argumento",
    "A22": "Wegovy pill y el volumen de GLP-1",
    "B22": ("Más de 5 millones de recetas de Wegovy pill desde enero. El Q2 2026 mostró reaceleración: ventas "
            "ajustadas +7% y EBIT ajustado +11% (a tipo de cambio constante), y la guía 2026 se subió dos veces "
            "(de −5%/−13% en feb a 0%/−6% en ago)."),
    "A23": "Caja y retorno al accionista",
    "B23": ("Flujo de caja libre guiado de DKK 45.000-55.000M en 2026 con un capex récord (~DKK 55.000M) que la "
            "empresa espera que baje en los próximos años. Dividendo de ~US$1,85 por ADR (~4,9%) y recompra de "
            "hasta DKK 15.000M. Rating AA (S&P) / Aa3 (Moody's)."),
    "A24": "Valuación deprimida",
    "B24": ("A US$38 el ADR cotiza a ~11x la utilidad estimada y ~7,6x EV/EBITDA LTM, contra 25-36x P/E en "
            "2022-2024 y ~15x-25x de sus pares. Está ~40% debajo del máximo de 52 semanas (US$64)."),
    "B27": "Riesgo",
    "A28": "Pérdida de cuota frente a Eli Lilly",
    "B28": ("Lilly (tirzepatida: Mounjaro/Zepbound, y orforglipron oral) tenía ~61% del mercado de obesidad contra "
            "39% de Novo en el Q2 2026. CagriSema solo fue no inferior a tirzepatida en peso (REIMAGINE 4) y no "
            "en HbA1c."),
    "A29": "Precios y expiración de patentes",
    "B29": ("Precio realizado en baja (MFN, WAC más bajo desde 2027, cobertura Medicaid reducida). La patente de "
            "semaglutida vence en 2032 en EE.UU. (más de la mitad de las ventas) y ya venció en Canadá, China, "
            "Brasil e India. Margen bruto ajustado H1 2026: 79,3% contra 83,1%."),
    "A30": "Crecimiento solo \"en línea con los pares\"",
    "B30": ("En el Capital Markets Day (21-sep-2026) la empresa apuntó a un crecimiento 2026-2030 en línea con 14 "
            "grandes farmacéuticas y a un margen \"ampliamente estable\": la acción cayó 7,9%. Fracasos recientes: "
            "ZEUS (ziltivekimab) y deterioros de DKK 6.300M (monlunabant) en el Q2 2026."),
    "A32": SOURCES,
    "A35": "Periodo del Reporte: 4 de agosto de 2026 – 23 de septiembre de 2026",
    "B38": "Titular",
    "A39": "Resultados",
    "B39": "H1 2026: ventas ajustadas +2% y EBIT ajustado +2% (tipo de cambio constante)",
    "D39": ("Q2: ventas DKK 78.500M (+7% ajustado) y EBIT ajustado DKK 33.400M (+11%). Reportado H1: ventas "
            "DKK 175.300M y EBIT DKK 86.700M, inflados por la reversión 340B de DKK 26.800M (Q1, sin caja)."),
    "A40": "Guía",
    "B40": "Guía 2026 mejorada: ventas y EBIT ajustados de 0% a −6% (tipo de cambio constante)",
    "D40": "Antes −4%/−12%. FCF DKK 45.000-55.000M, capex ~DKK 55.000M, tasa efectiva 21-23%. El efecto cambiario resta ~1-2pp en DKK.",
    "A41": "Estrategia",
    "B41": "Capital Markets Day: metas 2030 decepcionan",
    "D41": "Crecimiento 2026-30 en línea con los pares, margen estable, >5 lanzamientos multi-blockbuster y >DKK 150.000M de ventas de pipeline (ajustadas por riesgo) a 2035.",
    "A42": "Pipeline / Legal",
    "B42": "ZEUS falla; demanda contra Lilly por publicidad; ANDA de Cipla",
    "D42": "ZEUS (ziltivekimab) sin el objetivo primario (posible deterioro en Q3); Novo demandó a Lilly por publicidad engañosa (21-jul); Cipla pidió un genérico de Ozempic (Paragraph IV).",
    "A43": "Mercado / Wall St.",
    "B43": "Caída de 7,9% en el CMD y bajas de recomendación",
    "D43": "Deutsche Bank pasó de Mantener a Vender el 27-ago-2026 (objetivo DKK 265; ya había bajado de Comprar a Mantener el 23-feb tras REDEFINE 4). Consenso (yfinance): 3 Comprar / 10 Mantener / 1 Vender, objetivo medio US$46.",
    "B46": "Análisis e impacto en la valoración",
    "A47": "La reversión 340B distorsiona el LTM",
    "B47": ("La reversión de la provisión 340B (US$4.200M = DKK 26.800M, Q1 2026) es no recurrente y sin caja; "
            "además hubo DKK 6.300M de deterioros en el Q2. Impacto: el modelo usa como base las ventas y el EBIT "
            "\"ajustados\" de la propia empresa (Input!B12/B13): US$46.353M de ventas y 40,2% de margen LTM."),
    "A48": "Guía 2026-2027 y precio",
    "B48": ("La guía de ago-2026 (0% a −6% en ventas y EBIT ajustados) y el consenso (ventas 2026 DKK 300.200M, "
            "−2,9%; 2027 DKK 304.100M, +1,3%) anclan el Año 1 del Base en −3%. El recorte de WAC de ene-2027 y el "
            "MFN pesan sobre el precio; el volumen (Wegovy pill, Medicare Bridge) compensa."),
    "A49": "Metas 2030 y patente 2032",
    "B49": ("El CMD fija el techo del Base: crecimiento en línea con los pares (años 2-5 de 4,5%, debajo del ~5-6% "
            "del grupo) y margen estable hasta 2030. La expiración de semaglutida en EE.UU. (2032) justifica "
            "converger a 40% (basis ajustado por I+D) en 7 años y un crecimiento perpetuo de 3,5%."),
    "A50": "Presión de mercado",
    "B50": ("El ADR cayó de US$43,24 (18-sep) a US$38,17 (23-sep): −12% en tres ruedas. El consenso de 14 analistas "
            "es Mantener, con precio objetivo medio de US$46,3 (rango US$39,7-62,8)."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 68794,
    "B12": "='Income Statement'!L30", "B13": "='Income Statement'!L13",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "='Eficiencia de capital'!L5", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12",
    # Consenso EPS (yfinance, 23-sep-2026, DKK): 2026 22,75 / 2027 22,04 -> NTM ~22,2 = US$3,40
    "E13": "='Input sheet'!D1/(22,2/6,5297)", "E14": "—",
    "E16": "=IFERROR('Trailing Valuation'!L6/'Financials Multiples'!E57;\"\")",
    "E20": "='Balance Sheet'!L5", "E21": "='Input sheet'!B16-'Input sheet'!B19",
    "E22": "='Input sheet'!B16/'Input sheet'!B15", "E23": "='Income Statement'!L12/'Income Statement'!L16",
    "H4": "=('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1",
    "H5": "=('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1",
    "H6": "=('Income Statement'!K3/'Income Statement'!E3)^(1/6)-1",   # 6 años (XBRL IFRS desde 2019)
    "H7": "=('Income Statement'!K24/'Income Statement'!H24)^(1/3)-1",
    "H8": "=('Income Statement'!K24/'Income Statement'!F24)^(1/5)-1",
    "H9": "=('Income Statement'!K24/'Income Statement'!E24)^(1/6)-1",
    "H10": "=('Cash Flow Statement'!K36/'Cash Flow Statement'!F36)^(1/5)-1",
    "H11": "=('Income Statement'!K26/'Income Statement'!F26)^(1/5)-1",
    "H12": "=(304116/309064)^(1/2)-1",   # consenso ventas 2027 vs 2025 (DKK M)
    "H13": "=('Financials Multiples'!F57/'Income Statement'!K28)^(1/2)-1",
    "H14": "=(22,04/23,03)^(1/2)-1",      # consenso EPS 2027 vs EPS 2025 (DKK)
    "H15": "—",
    "H18": "=1,854/'Input sheet'!D1", "H19": "=Dividendos!L5", "H20": 1.854,
    "H21": "=(Dividendos!K4/Dividendos!H4)^(1/3)-1", "H22": "=(Dividendos!K4/Dividendos!F4)^(1/5)-1",
    "H23": "—", "H24": "—",
}

STORIES = {
    "A3": "Novo Nordisk: el pionero de los GLP-1 pasa del hipercrecimiento a crecer como una farmacéutica más",
    "A4": ("Novo creó el mercado de GLP-1 y triplicó sus ventas entre 2019 y 2025, pero en 2026 perdió el liderazgo en "
           "obesidad frente a Lilly, baja precios en EE.UU. (MFN, WAC desde 2027) y enfrenta genéricos de semaglutida "
           "fuera de EE.UU. El CMD de sep-2026 reseteó la ambición: crecer en línea con los pares con margen estable. "
           "La tesis Base: un Año 1 en caída (−3%), 4,5% anual en los años 2-5 (Wegovy pill/HD, CagriSema, "
           "zenagamtide) y un margen que baja de 45,8% a 40% (basis ajustado por I+D) hacia la expiración de la "
           "patente de semaglutida en EE.UU. (2032), con un costo de capital de 9,0%."),
    "G10": "Guía 2026 0% a −6% (tipo de cambio constante, −1pp FX) y consenso 2027 +1,3% -> Año 1 −3%; CMD \"en línea con pares\" -> años 2-5 4,5%.",
    "G11": "Año 1 = base ajustada −1,5pp (más I+D y promoción en el 2S26, WAC más bajo en 2027). Converge a 40% en 7 años (patente 2032).",
    "G12": "Tasa efectiva LTM 21,7% (guía 21-23%) que converge a la corporativa danesa de 22%.",
    "G13": "0,45x (años 1-5): capex guiado ~DKK 55.000M en 2026 y en baja; con 0,45x el FCFF del Año 1 (~US$11.100M) queda entre el FCF de FY2025 (US$9.000M) y el LTM (US$11.600M). 1,1x (años 6-10): capacidad ya construida, industria 1,07x.",
    "G14": "ROIC actual ~24% (basis ajustado por I+D); converge al costo de capital después del año 10.",
    "G15": "9,0%: rf 5,11% (UST, 23-sep-2026) + beta desapalancada 1,00 de farma global (relevered 1,09) x ERP 4,09% = Ke 9,55%; Kd 5,66% (AA); D/(D+E) 10% a valor de mercado.",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": -0.03, "D6": "Guía 2026 (ago): ventas ajustadas 0% a −6% a tipo de cambio constante (~−1pp FX); consenso 2026 −2,9% y 2027 +1,3%.",
    "C7": "='Valuation output'!B6-0,015", "D7": "Base ajustada por I+D ('Valuation output'!B6) −1,5pp: guía de más I+D y promoción en el 2S26 y WAC más bajo desde ene-2027.",
    "C8": 0.045, "D8": "CMD 21-sep-2026: CAGR 2026-30 en línea con 14 grandes farmacéuticas (~5-6%), con descuento por la erosión de semaglutida.",
    "C9": 0.40, "D9": "Basis ajustado por I+D. Premium sobre big pharma madura (Novartis/Amgen ~35% GAAP) tras la expiración de semaglutida; el promedio de Damodaran (23%) incluye empresas chicas.",
    "C10": 7, "D10": "Hasta 2032-33, la expiración de la patente de semaglutida en EE.UU.",
    "C11": 0.45, "D11": "Anclado al flujo de caja real: con 0,45x el FCFF del Año 1 (~US$11.100M) queda entre el FCF de FY2025 (US$9.000M) y el LTM (US$11.600M); la guía 2026 es DKK 45.000-55.000M (US$6.900-8.400M) con capex de ~DKK 55.000M. El marginal histórico 2020-25 (0,7x) subestimaba la reinversión con un crecimiento más bajo.",
    "C12": 1.1, "D12": "La empresa guía capex en baja; promedio de la industria 1,07x.",
}

MULTIPLOS_EVALUACION = (
    "Evaluación NVO: P/E, EV/EBITDA, P/OCF y P/FCFE fueron positivos todos los años (sin cambios de signo), así que el "
    "mecanismo nativo funciona; el ancla Base es el MIN de los 4 cierres dic-22 a dic-25 (J19 =MIN(B19:E19)), que cae en dic-2025 (dic-2024 en P/FCFE), después del derrumbe de 2025, así que el múltiplo Base "
    "ya es el deprimido (P/E 14,4x, EV/EBITDA 11,1x, P/OCF 13,9x) y no el de la burbuja 2022-24 (P/E 36x). EV/FCFF: el FCFF "
    "está deprimido por el capex récord (17% de ventas contra D&A 4,5%) y el múltiplo histórico era 30-36x -> se reemplazó "
    "(J8/J19/J30 de EVFCFF) por el múltiplo implícito del DCF de cada escenario (EV / FCFF FY+1). Además, 'Financials "
    "Multiples' proyectaba el EBIT contable con el margen ajustado por I+D del DCF (5,6pp más alto): se corrigió (bug #14)."
)

VO, INP, COC, RES = "'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'"

HISTORIA = (
    "Novo Nordisk pasó de ser la acción de crecimiento de Europa (P/E de 36x en 2023) a cotizar a ~11x utilidades: la "
    "competencia de Lilly, los recortes de precio en EE.UU. y los genéricos de semaglutida fuera de EE.UU. frenaron las "
    "ventas, y el Capital Markets Day de sep-2026 confirmó que la empresa ya no promete crecer más que sus pares. La "
    "pregunta es si el volumen (Wegovy pill, Medicare, nuevos mercados) y el pipeline (CagriSema, zenagamtide) compensan "
    "la caída de precio y la expiración de la patente de semaglutida en EE.UU. en 2032. El modelo parte de la base "
    "\"ajustada\" de la propia empresa (sin la reversión 340B ni los deterioros) y valúa en US$ al ADR."
)

BULL = [
    "Wegovy pill: >5 millones de recetas desde enero y >265.000 por semana; Q2 2026 con ventas ajustadas +7% y EBIT +11% (a tipo de cambio constante).",
    "Guía 2026 subida dos veces (de −5%/−13% a 0%/−6%); FCF de DKK 45.000-55.000M con capex en su pico.",
    "Balance AA/Aa3, dividendo de ~US$1,85 por ADR (~4,9%) y recompra de hasta DKK 15.000M.",
    "~11x utilidades y ~7,6x EV/EBITDA: el precio ya descuenta un crecimiento bajo y márgenes en caída.",
]
BEAR = [
    "Lilly con ~61% del mercado de obesidad (Q2 2026); CagriSema no superó a tirzepatida (REIMAGINE 4).",
    "Precio en baja: MFN, WAC más bajo desde 2027, genéricos de semaglutida en Canadá, China, Brasil e India.",
    "Patente de semaglutida en EE.UU. en 2032, más de la mitad de las ventas en EE.UU.; ZEUS falló y hubo DKK 6.300M de deterioros.",
    "CMD 2030: crecimiento \"en línea con pares\" y margen estable; Deutsche Bank pasó a Vender (27-ago-2026, objetivo DKK 265).",
]

LOG = [
    ["Loader SEC (sec_edgar_loader.py)", "Solo lee us-gaap: NVO (20-F, IFRS) daba \"sin ingresos anuales\"", "Serie armada desde ifrs-full en scripts/run_nvo.py (FY2019-FY2025)", "Emisor extranjero; sin XBRL antes de 2019 (columnas B-D con \"—\")."],
    ["Moneda (todo el libro)", "Plantilla en US$; estados de NVO en DKK", "DKK / 6,5297 (spot 23-sep-2026) para todos los años", "Precio del ADR (1 ADR = 1 acción B) y UST en US$; conserva crecimientos y márgenes de DKK."],
    ["Columna LTM (Income/Cash Flow)", "Sin 10-Q: LTM no disponible en XBRL", "FY2025 + H1 2026 − H1 2025 (6-K del 4-ago-2026)", "D&A del H1 2025 aproximado como la mitad de FY2025."],
    ["Balance Sheet columna L", "Repetía dic-2025", "Balance al 30-jun-2026 (Appendix 3 del 6-K)", "Caja US$6.812M, deuda US$21.460M, patrimonio US$33.888M."],
    ["Acciones 2019-2020", "Pre-split (2.400M)", "×2 (split 2:1 de sep-2023)", "Los 20-F viejos no están re-expresados."],
    ["Input sheet!B12 / B13 (base)", "=L3 (US$50.451M) / =L12 (US$21.762M, 43,1%)", "=L3 − 340B / =L12 − 340B + deterioros -> US$46.353M / US$18.633M (40,2%)", "Definición \"adjusted\" de Novo: reversión 340B de DKK 26.760M (sin caja) y deterioros de DKK 6.328M."],
    ["R& D converter F7 / F8 / B15:B16", "3 años; I+D LTM con deterioros", "5 años; I+D LTM sin el deterioro de DKK 6.328M", "El deterioro ya se sumó en B13 (evita doble cuenta)."],
    ["Input sheet!B25 / B68:B69", "25% / perpetuidad = rf (5,11%)", "22% / override 3,5%", "Tasa danesa; cliff de patentes de GLP-1 después de 2032."],
    ["Valuation output!C45 / C47 (márgenes)", "=B6 (45,8%) / =B30+5%", "35% / =B30+5% (45%)", "Conservador: big pharma madura (Novartis/Amgen ~35%). Optimista: margen estable del CMD."],
    ["Valuation output!C55:D55 / C106:D106 (crecimiento)", "=MIN(B27;B29)−1,5pp / =MAX(B27;B29)+1pp (todos los años)", "−7% y +1% / −1% y +7%", "Piso y techo de la guía 2026 (−1pp FX); luego erosión vs. crecimiento de pares con Lilly."],
    ["Financials Multiples filas 8/47/87 (bug #14)", "Margen del DCF ajustado por I+D (44,3%) aplicado al EBIT contable", "Margen DCF − ajuste de I+D / ventas (38,7%)", "Inflaba utilidad, EBITDA y OCF proyectados ~13% y los precios de P/E, EV/EBITDA, P/OCF y P/FCFE."],
    ["Dividendos (hoja vacía)", "DPS = 0 en los 5 múltiplos", "Dividendos pagados / acciones promedio (2019-LTM)", "US$1,79 por acción LTM, payout 45%."],
    ["EVFCFF!J8/J19/J30", "Mediana de 5 años (29,8x): FCFF deprimido por el capex récord", "Implícito del DCF de cada escenario (EV / FCFF FY+1)", "Paso 6."],
    ["Sector fila 2 (NVO)", "EV/EBITDA 1,5x y P/OCF 1,3x (yfinance mezcla US$ y DKK)", "Fórmulas contra las cifras LTM del libro (7,6x / 8,4x)", "Solo referencia visual."],
    ["Cost of capital worksheet", "A1/A+ · vencimiento 3 · ERP 4,23% (ene-2026) · rf 4,99%", "Aa2/AA · 7 años · 4,09% (sep-2026) · 5,11%", "S&P AA / Moody's Aa3; UST al 23-sep-2026."],
    ["Income Statement!B30:D30 / Valuation output!B52", "#DIV/0! (años sin dato) -> cascada en Crecimiento y Márgenes", "IFERROR", "Barrido de errores (paso 8). Industry Averages(US) F/S/Y/Z 19/30/79 son preexistentes de la plantilla."],
    ["Input sheet!B32 (auditoría 24-sep)", "0,7x (marginal 2020-25): FCFF Año 1 US$12.700M, sobre el FCF real", "0,45x: FCFF Año 1 US$11.100M", "FCF real: FY2025 US$9.000M, LTM US$11.600M, guía 2026 US$6.900-8.400M; el capex sigue en ~DKK 55.000M."],
    ["EVEBITDA / EVFCFF filas 10/21/32 (bug #15)", "Precio = múltiplo EV × métrica / acciones (valor de EMPRESA por acción)", "(EV implícito − deuda neta) / acciones", "Sobrevaluaba US$3,3 por acción (deuda neta US$14.571M)."],
    ["Financials Multiples filas 35/74/114 + 5 hojas de múltiplos filas 11/22/33 (bug #16)", "DPS = DPS previo + tasa de crecimiento; \"Dividendos acumulados\" a FY+3 = un solo año de dividendo", "DPS × (1 + crecimiento); acumulado = SUMA de FY+1..FY+n", "Subestimaba ~US$3,6 por acción el precio a FY+3 de cada múltiplo."],
    ["Resumen de Valoración!C25", "yfinance devolvió NaN para el cierre del 23-sep", "US$38,17 (cierre real, −3,12% vs. US$39,40)", "Precio congelado del día del análisis."],
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


def tesis_rows() -> tuple[list[list], dict]:
    rows: list[list] = [
        ["NVO (Novo Nordisk A/S) — Tesis de Inversión: De la Historia a los Números"],
        [f'="Metodología Damodaran (NYU Stern) | Precio al día del análisis: US$"&TEXT({RES}!C25;"0.00")&" (23-sep-2026, ADR NYSE) | WACC: "&TEXT({COC}!B14;"0.00%")&" | Cifras en US$ (DKK/6,5297)"'],
        [],
        ["1. LA HISTORIA"],
        [HISTORIA],
        [],
        ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ]
    idx: dict = {"bull_start": len(rows) + 1}
    rows += [[b, s] for b, s in zip(BULL, BEAR)]
    idx["bull_end"] = len(rows)
    rows += [[], ["2. DE LA HISTORIA A LOS NÚMEROS — LOS TRES ESCENARIOS (fórmulas vivas del modelo)"]]
    idx["sec2"] = len(rows)
    rows.append(["Supuesto", "Conservador", "Base", "Optimista", "Justificación y fuente (dato real)"])
    idx["head2"] = len(rows)
    rows += [
        ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={INP}!B27", f"={VO}!C106",
         "Base −3%: guía 2026 de ventas ajustadas 0% a −6% a tipo de cambio constante (~−1pp FX en DKK) y consenso 2027 +1,3%; el recorte de WAC de ene-2027 cae dentro del Año 1. Conservador −7%: piso de la guía. Optimista −1%: techo de la guía."],
        ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={INP}!B29", f"={VO}!D106",
         "Base 4,5%: CMD (21-sep-2026) con CAGR 2026-30 en línea con 14 grandes farmacéuticas (~5-6%), con descuento por la pérdida de cuota y los genéricos. Conservador 1%: erosión de semaglutida. Optimista 7%: Wegovy pill/HD, CagriSema y zenagamtide cumplen. Desde el año 6 convergen al 3,5% perpetuo."],
        ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
         "Base ajustada por I+D ('Valuation output'!B6 = 45,8%; 40,2% sin capitalizar I+D) −1,5pp: la empresa guía más I+D y promoción en el 2S26 y el WAC baja en 2027."],
        ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
         "Base 40% (basis ajustado por I+D): premium sobre big pharma madura tras la patente 2032; comparables GAAP: Lilly 54%, Amgen 36%, Novartis 35%, AstraZeneca 24%, Sanofi 21%. Conservador 35% (Novartis/Amgen). Optimista 45%: el margen \"estable\" del CMD se sostiene."],
        ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31",
         "7 años: hasta 2032-33, la expiración de la patente de semaglutida en EE.UU."],
        ["Sales-to-Capital (años 1-5 / 6-10)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
         "0,45x en los años 1-5, anclado al FCF: con 0,7x (marginal 2020-25) el FCFF del Año 1 daba US$12.700M, por encima del FCF de FY2025 (US$9.000M), del LTM (US$11.600M) y de la guía 2026 (US$6.900-8.400M), porque el capex sigue en ~DKK 55.000M con un crecimiento mucho menor. 1,1x en los años 6-10 (capex en baja; industria 1,07x)."],
        ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
         "rf 5,11% (UST 10 años, 23-sep-2026) + beta 1,09 (Damodaran Drugs (Pharmaceutical) global desapalancada 1,00, D/E 11% a mercado) x ERP 4,09% (Damodaran, 1-sep-2026; Dinamarca Aaa sin prima país) = Ke 9,55%. Kd 5,66% (AA). D/(D+E) 10%."],
        ["Referencia: margen base ajustado (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
         "EBIT LTM reportado US$21.762M − reversión 340B US$4.098M + deterioros US$969M = US$18.633M, + ajuste de I+D capitalizado US$2.590M."],
    ]
    idx["assump_end"] = len(rows)
    rows += [[], ["3. RESULTADO DEL DCF POR ESCENARIO"]]
    idx["sec3"] = len(rows)
    rows.append(["Escenario", "Valor DCF / acción", "Precio Objetivo Ponderado*", "DCF vs. precio actual", "Ponderado vs. precio actual"])
    idx["head3"] = len(rows)
    r0 = len(rows) + 1
    rows += [
        ["Conservador", f"={VO}!B86", f"={RES}!C12", f"=B{r0}/{INP}!$B$23-1", f"=C{r0}/{INP}!$B$23-1"],
        ["Base", f"={VO}!B35", f"={RES}!D12", f"=B{r0 + 1}/{INP}!$B$23-1", f"=C{r0 + 1}/{INP}!$B$23-1"],
        ["Optimista", f"={VO}!B137", f"={RES}!E12", f"=B{r0 + 2}/{INP}!$B$23-1", f"=C{r0 + 2}/{INP}!$B$23-1"],
        ["Precio actual (GOOGLEFINANCE)", f"={INP}!B23", "Precio al día del análisis", f"={RES}!C25"],
        [f'=IF(AND(B{r0}<B{r0 + 1};B{r0 + 1}<B{r0 + 2};C{r0}<C{r0 + 1};C{r0 + 1}<C{r0 + 2};{VO}!C55<{INP}!B27;{INP}!B27<{VO}!C106;{VO}!D55<{INP}!B29;{INP}!B29<{VO}!D106;{VO}!C45<{VO}!C46;{VO}!C46<{VO}!C47);"✔ Orden verificado: Conservador < Base < Optimista en crecimiento, margen objetivo, valor DCF y precio ponderado";"✖ REVISAR: el orden Conservador < Base < Optimista no se cumple")'],
        ["*El Precio Objetivo Ponderado combina el DCF (40%) con 5 múltiplos (EV/EBITDA 20%, P/E 20%, EV/FCFF 10%, P/FCFE 5%, P/OCF 5%) según la categoría 'Madura': utilidades y EBITDA positivos y estables todos los años, así que P/E y EV/EBITDA son confiables. Se descartó 'Biotech/Farma' porque carga 30% en FCFF/FCFE, que hoy están deprimidos por el capex récord. Los múltiplos Base son los de dic-2025 (post-derrumbe), no los de la burbuja 2022-24."],
    ]
    idx["res_rows"] = (r0, r0 + 3)
    idx["check"] = len(rows) - 1
    idx["note"] = len(rows)
    rows += [[], ["4. LOG DE CORRECCIONES ESTRUCTURALES Y AJUSTES (backup de cada fórmula en reference/backups/nvo_formula_backup.json del repo JMR-valuation)"]]
    idx["sec4"] = len(rows)
    rows.append(["#", "Celda / componente", "Antes", "Después", "Razón"])
    idx["head4"] = len(rows)
    idx["log_start"] = len(rows)  # 0-based index de la primera fila del log
    rows += [[i + 1, *row] for i, row in enumerate(LOG)]
    idx["log_end"] = len(rows)
    rows.append([f'="Resultado: DCF Base US$"&TEXT({VO}!B35;"0.00")&" (Conservador US$"&TEXT({VO}!B86;"0.00")&", Optimista US$"&TEXT({VO}!B137;"0.00")&"); precio ponderado Base US$"&TEXT({RES}!D12;"0.00")&"."'])
    idx["result"] = len(rows)
    rows += [[], ["5. CONCLUSIÓN"]]
    idx["sec5"] = len(rows)
    rows.append([f'="A US$"&TEXT({INP}!B23;"0.00")&", el ADR de Novo cotiza cerca de su DCF Base (US$"&TEXT({VO}!B35;"0.00")&", "&TEXT({VO}!B35/{INP}!B23-1;"+0%;-0%")&"), entre el Conservador (US$"&TEXT({VO}!B86;"0.00")&") y el Optimista (US$"&TEXT({VO}!B137;"0.00")&"): el mercado ya descuenta el reseteo del CMD (crecimiento de pares y margen a la baja hacia 2032). El precio ponderado Base (US$"&TEXT({RES}!D12;"0.00")&") queda arriba porque los múltiplos de dic-2025 todavía reflejan más crecimiento. Con el DCF casi en el precio no hay margen de seguridad amplio: el retorno depende del dividendo (~4,9%) y de que el volumen compense el precio."'])
    idx["concl"] = len(rows)
    rows.append(["Variable clave a monitorear: el precio realizado neto en EE.UU. contra el volumen de Wegovy pill y Medicare Bridge. Si las ventas ajustadas vuelven a crecer en 2027 pese al recorte de WAC (consenso +1,3%) y CagriSema se aprueba, el caso se mueve al Optimista; si Lilly (orforglipron) sigue ganando cuota y el precio cae más rápido que el volumen, se mueve al Conservador (margen de 35%)."])
    idx["monitor"] = len(rows)
    rows += [[], [SOURCES]]
    idx["sources"] = len(rows)
    return rows, idx


def write_tesis(sh, backup_path) -> None:
    rows, i = tesis_rows()
    pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
    a0, a1 = i["head2"] + 1, i["assump_end"]
    r0, r1 = i["res_rows"]
    ms.write_tesis(
        sh, rows, backup_path, text_rows=range(i["log_start"], i["log_end"]),
        merges=[f"A{r}:E{r}" for r in (1, 2, 5, i["check"], i["note"], i["sec4"], i["result"], i["concl"],
                                       i["monitor"], i["sources"])]
        + [f"B{r}:E{r}" for r in range(i["bull_start"] - 1, i["bull_end"] + 1)],
        bold_rows=(4, i["sec2"], i["sec3"], i["sec4"], i["sec5"]),
        head_rows=(i["bull_start"] - 1, i["head2"], i["head3"], i["head4"]),
        formats=[
            {"range": f"B{a0}:D{a0 + 3}", "format": pct}, {"range": f"B{a1}:D{a1}", "format": pct},
            {"range": f"B{a0 + 4}:D{a0 + 4}", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0"}}},
            {"range": f"B{a0 + 5}:D{a0 + 5}", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}},
            {"range": f"B{a0 + 6}:D{a0 + 6}", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0.00%"}}},
            {"range": f"B{r0}:C{r1}", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
            {"range": f"D{r1}", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
            {"range": f"D{r0}:E{r1 - 1}", "format": {"numberFormat": {"type": "PERCENT", "pattern": "+0.0%;-0.0%"}}},
            {"range": f"A{i['check']}", "format": {"textFormat": {"bold": True}}},
        ])
