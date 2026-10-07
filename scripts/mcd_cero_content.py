"""Contenido de las hojas de texto de la valoración de MCD desde cero (6-oct-2026; pasos 3 y 10 del prompt v4).
Las cifras de resultado son fórmulas vivas contra el modelo y la pestaña «Escenarios e historias»; las demás salen de
las fuentes citadas (corte de información: 30-sep-2026)."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: 10-Q del 2T26 de McDonald's (7-ago-2026) y 10-K 2025 (24-feb-2026), SEC EDGAR; comunicado e información "
    "complementaria del 2T26 (8-K del 4-ago-2026); 8-K del nombramiento de Skye Anderson (4-ago-2026); 8-K del Investor Day "
    "(23-sep-2026) y su transcripción (Stock Analysis); Restaurant Dive (comparables de 18 cadenas, 27-ago-2026; plan NEXT, "
    "28-sep-2026); Damodaran (betas, márgenes, ROIC y ventas/capital por industria, ene-2026; ERP oct-2026); UST 10 años y "
    "precio de cierre del 30-sep-2026."
)

CUALITATIVO = {
    "B5": "McDonald's Corporation",
    "B6": ("Chris Kempczinski (presidente del directorio y CEO). CFO: Ian Borden. Skye Anderson, presidenta de McDonald's USA "
           "desde el 4-ago-2026 (reemplaza a Joe Erlinger)."),
    "B7": "Restaurantes de comida rápida, franquiciador (Damodaran: Restaurant/Dining)",
    "B8": "https://corporate.mcdonalds.com  |  IR: https://investor.mcdonalds.com",
    "B11": "Descripción",
    "A12": "Visión General de la Empresa",
    "B12": ("Mayor cadena de comida rápida del mundo: más de 46.000 locales en más de 100 países, ~95% operados por franquiciados. "
            "Ingresos LTM a jun-2026 de US$27.702M (61,6% rentas, regalías y cuotas de franquicias) sobre ventas del sistema de "
            "~US$139.400M (2025). Es dueña o arrendataria de largo plazo del terreno y el edificio de casi todos los locales."),
    "A13": "EE.UU.",
    "B13": ("13.769 locales (95% franquiciados) y ingresos de US$10.825M en 2025. Comparables +0,8% en el 2T26 (ticket y mezcla, "
            "tráfico negativo) y guía de 3T26 levemente negativa."),
    "A14": "International Operated Markets",
    "B14": ("10.918 locales en Francia, Canadá, Reino Unido, Alemania, Australia, Italia, España, Polonia y otros (89% "
            "franquiciados); ingresos de US$13.633M en 2025 y comparables +1,5% en el 2T26."),
    "A15": "Developmental Licensed y corporativo",
    "B15": ("~99% licenciados: China y Japón (afiliadas con participación), Latinoamérica, Medio Oriente y otros; regalías y "
            "cuotas por US$2.427M en 2025; comparables +1,9% en el 2T26 (Japón positivo, China negativo)."),
    "A16": "Modelo de ingresos",
    "B16": ("Franquicias: renta (~US$10.442M en 2025) y regalías (~US$6.018M) sobre la venta de cada local; restaurantes propios "
            "(US$9.690M en 2025) con margen de ~15%; otros ingresos (tecnología cobrada a franquiciados, licencias)."),
    "B21": "Argumento",
    "A22": "Renta y regalías indexadas a ventas",
    "B22": ("~90% del margen de restaurantes viene de franquicias; la renta tiene mínimos contractuales (US$31.451M de pagos "
            "mínimos futuros) y la regalía crece con la venta del sistema."),
    "A23": "Escala, marca y datos",
    "B23": ("~220 millones de usuarios activos de fidelización y US$40.000M de ventas a miembros en 12 meses; 17 productos que "
            "venden más de US$1.000M al año; ~2.600 aperturas previstas en 2026."),
    "A24": "Margen y caja",
    "B24": ("Margen operativo no GAAP de 46,9% en el 2T26, guía de «low-to-mid 50%» a 2030 con refranquiciamiento a ~98%; "
            "dividendo de US$7,44 anual (49 años seguidos de aumentos) y recompras de US$1.251M en el 1S26."),
    "B27": "Riesgo",
    "A28": "Tráfico de EE.UU.",
    "B28": ("Comparables de +0,8% en el 2T26 con tráfico negativo; el CEO admitió que cambiar ofertas digitales por el menú de "
            "precios fijos fue un mal canje y solo 60-65% del sistema adoptó los precios sugeridos."),
    "A29": "Costo del plan NEXT",
    "B29": ("US$8.500M de apoyo a franquiciados hasta 2036 (US$5.000M a 2030) en rentas y capital; la acción cayó 4,8% el "
            "23-sep-2026. El apoyo de rentas se amortiza ~10 años contra el resultado."),
    "A30": "Competencia por valor y costo laboral",
    "B30": ("Burger King (+8,5%) y Taco Bell (+7%) ganaron comparables en el 2T26 mientras McDonald's creció +0,8%; salarios "
            "mínimos de comida rápida y medicamentos GLP-1 presionan la frecuencia y la economía del franquiciado."),
    "A32": SOURCES,
    "A35": "Periodo del Reporte: 1 de julio de 2026 – 30 de septiembre de 2026",
    "B38": "Titular",
    "A39": "Resultados",
    "B39": "2T26: ingresos +4%, comparables globales +1,3% (EE.UU. +0,8%)",
    "D39": "Ingresos US$7.099M; EBIT US$3.338M; BPA diluido US$3,32 (+6%); ventas del sistema +5% (+4% a moneda constante).",
    "A40": "Guía",
    "B40": "Margen 2026 «mid-to-high 40%»; capex US$3.700-3.900M; ~2.600 aperturas",
    "D40": "Gasto general ~2,2% de las ventas del sistema; tasa efectiva 21-23%; conversión de flujo libre «low-to-mid 80%» (anexo 99.2).",
    "A41": "Gestión",
    "B41": "Skye Anderson reemplaza a Joe Erlinger al frente de EE.UU.",
    "D41": "8-K del 4-ago-2026; Erlinger asesora la transición hasta comienzos de 2027.",
    "A42": "Investor Day",
    "B42": "Plan NEXT: margen «low-to-mid 50%» a 2030 y US$8.500M de apoyo",
    "D42": "Refranquiciamiento a ~98% a fines de 2028; gasto general 1,9% a 2030; +1,5 pp de participación en pollo y bebidas (8-K del 23-sep-2026).",
    "A43": "Mercado",
    "B43": "La acción cae 4,8% el día del Investor Day",
    "D43": "Peor día desde marzo de 2020; recortes de precio objetivo de JPMorgan, TD Cowen, Evercore y BMO (24-sep-2026).",
    "B46": "Análisis e impacto en la valoración",
    "A47": "Refranquiciamiento",
    "B47": ("Baja los ingresos reportados en los años 1-2 (las ventas de restaurantes propios caen ~50% hasta 2028) y sube el "
            "margen; las ventas del sistema siguen creciendo ~5%."),
    "A48": "Arrendamientos",
    "B48": ("Operativos capitalizados con el conversor (VP US$10.020M a la tasa de la deuda): EBIT +US$963M y margen +3,48 pp; "
            "los financieros (US$2.329M) ya están en la deuda."),
    "A49": "Historias",
    "B49": ("Cuatro historias activas: Base (50%), Conservadora (25%), Disrupción (10%) y Optimista (15%); 'Valuation output' "
            "calcula las cuatro con la estructura de Damodaran."),
    "A50": "Riesgo en el descuento",
    "B50": ("Beta 0,79 bottom-up: Restaurant/Dining global 0,66 reapalancada con la D/E de mercado (~25%). Prima de mercado "
            "3,70% (oct-2026) ponderada por regiones: 4,33%. Kd 7,13% con la calificación Baa1/BBB+."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 150000,
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
    "A3": "McDonald's: arrendador y franquiciador que refranquicia a 98% mientras defiende el tráfico de EE.UU.",
    "A4": ("McDonald's cobra renta y regalías sobre ~US$139.400M de ventas del sistema y reporta US$27.702M de ingresos LTM con un "
           "margen operativo de ~46%. La historia Base: las ventas del sistema crecen ~5% (aperturas ~2,5% y comparables de "
           "2-3%), el refranquiciamiento a ~98% baja los ingresos reportados dos años y sube el margen a 52% en cinco años, y el "
           "capital nuevo (inmuebles) rinde lo mismo que hoy (~21%). Con una marca probada y escala sin par, el ROIC después del "
           "año 10 es el promedio de la industria (18,4%)."),
    "G10": "Año 1 −0,9% (franquicias +7%, restaurantes propios −15% por refranquiciamiento, otros +8%); CAGR 1-5 ~1,0%.",
    "G11": "Año 1 49,7% (LTM con arrendamientos); objetivo 55,5% (52% reportado + 3,48 pp) en 5 años: mezcla y gasto general.",
    "G12": "Tasa efectiva 22% (guía 21-23%) que converge a la marginal de 25%.",
    "G13": "0,5 en los años 1-10: el capital nuevo rinde ~21%, igual al ROIC actual con arrendamientos.",
    "G14": "ROIC con arrendamientos ~21%; terminal 18,4% (promedio de Restaurant/Dining, ventaja durable).",
    "G15": "Ke 8,69% (rf 5,29% + beta 0,79 × ERP por regiones 4,33%); Kd 7,13% (Baa1/BBB+); WACC 8,02%.",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": -0.0087, "D6": "Suma por fuente: franquicias +7%, restaurantes propios −15% (refranquiciamiento), otros +8%.",
    "C7": 0.497, "D7": "Margen LTM en base ajustada por arrendamientos (12.805 + 963) / 27.702.",
    "C8": 0.0146, "D8": "Años 2-5 de la Base: −4,7% (2028, fin del refranquiciamiento), +1,6%, +4,6%, +4,6%.",
    "C9": 0.5548, "D9": "52% reportado (tramo bajo-medio de la guía «low-to-mid 50%» a 2030) + 3,48 pp de arrendamientos.",
    "C10": 5, "D10": "La guía llega a 2030; la mejora es de mezcla y gasto general.",
    "C11": 0.5, "D11": "Rendimiento sobre el capital nuevo ~21% (55,5% × 75% × 0,5) = ROIC actual con arrendamientos.",
    "C12": 0.5, "D12": "Igual que los años 1-5: el modelo de renta exige inmuebles por cada local nuevo.",
}

MULTIPLOS_EVALUACION = (
    "Evaluación MCD (6-oct-2026, desde cero): los múltiplos Base salen de tres anclas (historia de cinco cierres, peers Yum!, "
    "RBI y Domino's con +5% y el justificado, λ = 0,25; P/E sin justificado por el patrimonio negativo). Los consolidados hoy "
    "valen ~25% más que el DCF Base: la historia de cinco años (P/E 25,6×) se formó con más crecimiento del BPA que el que hoy "
    "muestra el negocio. El chequeo de crecimiento implícito no da alertas (los cinco Base cuentan la historia del DCF en FY+3). "
    "El DCF es el valor intrínseco; los múltiplos son precio relativo."
)

VO, INP, COC, RES, ESC = ("'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'",
                          "'Escenarios e historias'")

TESIS_ROWS: list[list] = [
    ["MCD (McDonald's Corporation) — Tesis de Inversión: De la Historia a los Números (análisis desde cero, 6-oct-2026)"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al 30-sep-2026: US$"&TEXT({RES}!B3;"0.00")&" | WACC inicial: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["McDonald's es un arrendador y franquiciador: cobra renta y regalías sobre la venta de más de 46.000 locales y es dueño o "
     "arrendatario de largo plazo de sus inmuebles. El refranquiciamiento a ~98% a fines de 2028 baja los ingresos reportados y "
     "sube el margen, mientras las ventas del sistema crecen ~5%. La tensión: si el plan NEXT (US$8.500M de apoyo a "
     "franquiciados) recupera el tráfico de EE.UU. y lleva el margen a «low-to-mid 50%», o si la competencia por valor, el "
     "costo laboral y el GLP-1 obligan a resignar renta de forma permanente."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["Ventas del sistema +4% a moneda constante en el 2T26 con aperturas que aportan ~2,5%; ~220 millones de usuarios de fidelización.",
     "Comparables de EE.UU. +0,8% en el 2T26 con tráfico negativo; guía de 3T26 levemente negativa."],
    ["Margen no GAAP de 46,9% y guía de «low-to-mid 50%» a 2030 por refranquiciamiento y gasto general.",
     "US$8.500M de apoyo a franquiciados hasta 2036; el apoyo de rentas se amortiza contra el resultado."],
    ["Renta con pagos mínimos contractuales de US$31.451M y regalías indexadas a ventas: flujo estable y beta baja.",
     "Burger King (+8,5%) y Taco Bell (+7%) ganaron comparables en el 2T26; Wendy's (−7%) muestra la guerra de precios."],
    ["49 años seguidos de aumentos de dividendo; payout guiado de 50-60% más recompras.",
     "Patrimonio contable negativo y deuda de US$39.863M: las recompras se financiaron con deuda."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — HISTORIAS EN 'VALUATION OUTPUT' (fórmulas vivas)"],
    ["Supuesto", "Conservadora", "Base", "Optimista", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={VO}!C4", f"={VO}!C106",
     "Base −0,9%: franquicias +7%, restaurantes propios −15% (refranquiciamiento), otros +8% (10-K 2025, 2T26, Investor Day)."],
    ["Crecimiento de ingresos — Año 2", f"={VO}!D55", f"={VO}!D4", f"={VO}!D106",
     "Base −4,7%: 2028 concentra el refranquiciamiento (restaurantes propios −30%); años 3-5 +1,6%, +4,6%, +4,6%."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "49,7%: margen LTM (46,2%) + 3,48 pp del ajuste de arrendamientos."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 55,5% (52% + arrendamientos): tramo bajo-medio de la guía de «low-to-mid 50%» a 2030 (8-K del 23-sep-2026)."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31", "5 años (la guía llega a 2030)."],
    ["Sales-to-Capital (años 1-5)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "0,5 (también en los años 6-10): ~21% sobre el capital nuevo, igual al ROIC actual con arrendamientos."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "rf 5,29% (UST 10 años, 30-sep-2026) + beta 0,79 × ERP por regiones 4,33% (Damodaran, oct-2026) = Ke 8,69%; Kd 7,13%."],
    ["Referencia: margen base (B6, con arrendamientos)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "EBIT GAAP LTM US$12.805M (la reestructuración se repite desde 2023 y queda como costo) + US$963M de arrendamientos."],
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
    ["4. LOG DE CORRECCIONES Y AJUSTES (respaldo de cada celda en reference/backups/mcd_desde_cero_2026-10-06.json del repo JMR-valuation)"],
    ["#", "Celda / componente", "Antes", "Después", "Razón"],
    [1, "Balance Sheet columna L", "Saldos de dic-2025", "Balance al 30-jun-2026 (10-Q 2T26)", "El importador repetía el cierre anual."],
    [2, "Income Statement fila 9 y Cash Flow fila 4 (2020-LTM)", "D&A corporativa (301-466)", "D&A total (1.751-2.266)", "El importador usaba DepreciationDepletionAndAmortization; EBITDA corregido."],
    [3, "Income Statement filas 23-27 (2023-LTM)", "BPA en millones y acciones en 0", "BPA y acciones del XBRL", "MCD etiqueta las acciones en millones desde 2023."],
    [4, "Income Statement fila 8 (2020-2021)", "SG&A en 0", "SG&A del 10-K 2021 sin su D&A", "No etiquetado en el XBRL."],
    [5, "Balance Sheet filas 20, 26 y 27", "Deuda corriente duplicada y arrendamientos operativos 2019-2022 en «Leases»", "Deuda corriente dentro del LP; operativos en otros pasivos", "10-K 2025: vencimientos clasificados como largo plazo; deuda comparable para los múltiplos históricos."],
    [6, "Input sheet!B17 / B18", "I+D Yes · arrendamientos No", "No · Yes", "Sin I+D; arrendamientos operativos como deuda (Damodaran)."],
    [7, "Input sheet!B22 / B24 / B38-B42", "707,6M · tasa LTM · sin opciones", "708,8M (con RSU) · 22% · 8,8M opciones a US$228,19", "10-Q 2T26, 10-K 2025 y guía 2026."],
    [8, "Cost of capital worksheet y ERP (B2)", "Prima 4,09% · país de registro · rating genérico", "Prima 3,70% · por regiones · Baa1/BBB+", "Tasas comunes de la cartera al 30-sep-2026; ~60% de las ventas fuera de EE.UU."],
    [9, "Input sheet!B4 / D1 · Resumen C25", "Fecha y precio de la corrida", "30-sep-2026 · US$230,94", "Fecha de corte común de la cartera."],
    [10, "Input sheet!B49 / B50", "ROIC terminal = costo de capital", "18,4% (Restaurant/Dining)", "Ventaja durable: ROIC ~21% sostenido, marca de 70 años, sin erosión visible."],
    [11, "Descuento de múltiplos fila 38 / 43", "DCF de 'Valuation output' · MOS sobre el ponderado", "Historias · MOS sobre el esperado", "Presentación vigente."],
    [],
    ["5. CONCLUSIÓN"],
    [f'="El DCF Base de las historias es US$"&TEXT({ESC}!H5;"0.00")&" y el esperado US$"&TEXT({ESC}!H10;"0.00")&"; el precio del 30-sep-2026 (US$"&TEXT({RES}!B3;"0.00")&") está "&TEXT({RES}!B3/{ESC}!H5-1;"+0%;-0%")&" frente a la Base. Los múltiplos (US$"&TEXT(\'Descuento de múltiplos\'!D39;"0.00")&") valen más porque la historia de cinco años se formó con más crecimiento del BPA. El DCF es la lectura más confiable: el valor depende del margen después del refranquiciamiento y de cuánto recupera el tráfico, no de un múltiplo de mercado."'],
    ["Variable clave a monitorear: las comparables y el tráfico de EE.UU., el ritmo del refranquiciamiento y la amortización del apoyo de rentas. Si las comparables vuelven a 3% y el margen ajustado supera 48% en 2027, el caso se mueve hacia la Optimista; si EE.UU. sigue en ~0% y el apoyo crece, hacia la Conservadora."],
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
        sh, TESIS_ROWS, backup_path, text_rows=range(34, 45),
        merges=[f"A{r}:E{r}" for r in (1, 2, 5, 33, 48, 49, 51)] + [f"B{r}:E{r}" for r in range(7, 12)],
        bold_rows=(4, 13, 24, 33, 47), head_rows=(7, 14, 25, 34),
        formats=[
            {"range": "B15:D18", "format": pct}, {"range": "B22:D22", "format": pct},
            {"range": "B19:D19", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0"}}},
            {"range": "B20:D20", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}},
            {"range": "B21:D21", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0.00%"}}},
            {"range": "B26:B30", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0%"}}},
            {"range": "C26:C31", "format": cur}, {"range": "D26:E29", "format": pct},
            {"range": "E30:E31", "format": cur},
        ])
