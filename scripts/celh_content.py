"""Contenido cualitativo de la valoración de CELH desde cero (1-oct-2026; pasos 3 y 10 del prompt v4).
Las cifras de resultado son fórmulas vivas contra el modelo y la pestaña «Escenarios e historias»."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: 10-Q del 2T26 de Celsius Holdings (6-ago-2026) y 10-K 2025 (2-mar-2026), SEC EDGAR; comunicados de resultados "
    "del 4T25 (26-feb-2026) y del 2T26 (6-ago-2026); 8-K de la segunda enmienda del crédito (15-jul-2026) y de cambios en la "
    "gerencia (10-ago-2026); proxy 2026 (14-abr-2026); Beverage Industry con datos de Circana (10-jul-2026); resumen de la "
    "llamada del 2T26 (Yahoo Finance, 6-ago-2026); investigación del fiscal de Texas (4-jun-2026); demanda colectiva (SBS, "
    "29-sep-2026); Monster Beverage, XBRL de la SEC; Damodaran (betas y márgenes por industria, ene-2026; ERP sep-2026); "
    "UST 10 años al 30-sep-2026; precio de cierre del 30-sep-2026."
)

CUALITATIVO = {
    "B5": "Celsius Holdings, Inc.",
    "B6": "John Fieldly (presidente del directorio y CEO). CFO: Jarrod Langhans. Tyler Bohannon, director comercial desde el 10-ago-2026.",
    "B7": "Bebidas energéticas y funcionales (Damodaran: Beverage (Soft))",
    "B8": "https://www.celsiusholdingsinc.com  |  IR: https://ir.celsiusholdingsinc.com",
    "B11": "Descripción",
    "B12": ("Portafolio de tres marcas de bebidas energéticas: CELSIUS, Alani Nu (comprada en abril de 2025) y Rockstar (EE.UU. y "
            "Canadá, agosto de 2025). Ventas LTM a jun-2026 de US$3.047M, ~20% de la categoría en EE.UU. Fabrica con terceros y "
            "distribuye en EE.UU. a través de PepsiCo, que es parte relacionada (60% de las ventas del 2T26) y tenedor de las "
            "preferentes. 1.497 empleados a dic-2025."),
    "A13": "CELSIUS",
    "B13": ("~US$1.425M LTM. Cayó 11,7% en el 2T26 (−2% al consumidor) por promociones, inventario y la poda de presentaciones, "
            "que la gerencia admitió fue demasiado profunda. 9,5% de participación en EE.UU.; espera volver a crecer al cierre de 2026."),
    "A14": "Alani Nu",
    "B14": ("~US$1.433M LTM. Ventas al consumidor +55,7% en el 2T26 y 8,7% de participación; facturación +21% por el paso a "
            "distribución directa de PepsiCo, que aumenta las bonificaciones. Bajo investigación del fiscal de Texas (jun-2026)."),
    "A15": "Rockstar y exterior",
    "B15": ("Rockstar ~US$189M en diez meses (US$66,5M en el 2T26), −13% al consumidor. Exterior US$62,5M en el 1S26 (+32%): "
            "Nórdicos, Reino Unido, Irlanda, Francia, Australia; meta de más de 15% de las ventas en cinco años."),
    "A16": "Distribución",
    "B16": ("PepsiCo distribuye las tres marcas en EE.UU. como capitán de la categoría energía (acuerdo de ~17 años desde "
            "ago-2025). Celsius pagó por la capitanía con preferentes y reconoce el pago implícito como menor ingreso."),
    "B21": "Argumento",
    "A22": "Categoría en crecimiento y escala",
    "B22": ("Las bebidas energéticas crecieron 15,2% en EE.UU. en 52 semanas a abr-2026 (Circana). El portafolio vendió +31% al "
            "consumidor en el 2T26 y aportó ~30% del crecimiento del segmento sin azúcar."),
    "A23": "Margen normalizado y caja",
    "B23": ("Sin cargos de una vez el margen operativo LTM es ~20,6%; EBITDA ajustado 23,7% en el 1S26. Flujo operativo de "
            "US$296M en el 1S26, caja de US$631M y deuda neta baja (~US$64M)."),
    "A24": "PepsiCo alineado",
    "B24": ("PepsiCo es socio, distribuidor y tenedor de preferentes: tiene incentivos para priorizar el portafolio. Las tres "
            "marcas ya están integradas a su sistema (sep-2026)."),
    "B27": "Riesgo",
    "A28": "La marca CELSIUS pierde participación",
    "B28": "Facturación −11,7% en el 2T26 y tres trimestres cediendo participación; la recuperación depende de recuperar espacio en refrigeradores.",
    "A29": "Moda y regulación de la cafeína",
    "B29": ("Investigación del fiscal de Texas sobre Alani Nu (200 mg de cafeína por lata) y demandas colectivas (período "
            "feb-2025 a jun-2026). Una restricción por edad golpearía a la marca que hoy crece."),
    "A30": "Margen bruto y dependencia",
    "B30": ("Margen bruto de 48,1% (51,5% un año antes) por promociones, mezcla y aluminio. Más de la mitad de las ventas pasa "
            "por un solo distribuidor."),
    "A32": SOURCES,
    "A35": "Periodo del Reporte: 1 de julio de 2026 – 30 de septiembre de 2026",
    "B38": "Titular",
    "A39": "Resultados",
    "B39": "2T26: ventas +10,6%, CELSIUS −11,7%, margen bruto 48,1%",
    "D39": "Ventas de US$817,9M frente a ~US$886M esperados; EBITDA ajustado US$184,2M (22,5%); recompras de US$100,4M.",
    "A40": "Guía",
    "B40": "3T26 parecido al 2T26; CELSIUS vuelve a crecer al cierre del año",
    "D40": "Margen bruto «en la parte alta de los 40» por el aluminio; sin metas formales de largo plazo.",
    "A41": "Gestión",
    "B41": "Sale el presidente y COO Eric Hanson; Bohannon, director comercial",
    "D41": "8-K del 10-ago-2026; Tony Guilfoyle, director de transformación desde el 1-jul-2026.",
    "A42": "Deuda",
    "B42": "Segunda refinanciación: −0,25 pp de tasa",
    "D42": "Nuevo préstamo de US$694,75M (15-jul-2026) a SOFR + 2,25%, vence en 2032.",
    "A43": "Legal",
    "B43": "Demandas colectivas por la seguridad de Alani Nu",
    "D43": "Período de clase feb-2025 a jun-2026; fecha límite para el demandante principal: 3-nov-2026. El CEO compró acciones el 10-sep-2026.",
    "B46": "Análisis e impacto en la valoración",
    "A47": "EBIT normalizado",
    "B47": ("El EBIT GAAP LTM (US$160,3M) incluye US$466,2M de cargos de una vez, sobre todo la terminación de distribuidores de "
            "Alani Nu (en su mayoría reembolsada por PepsiCo). El modelo usa el EBIT normalizado (US$626,5M, 20,6%)."),
    "A48": "Preferentes de PepsiCo",
    "B48": ("Se restan por su valor de liquidación (US$1.135M), no por el contable (US$1.760M): la conversión solo ocurre a "
            "opción de Celsius o por encima de US$25 (Serie A) y US$51,75 (Serie B). Se incluyen en el capital invertido."),
    "A49": "Historias",
    "B49": ("Cuatro historias activas: Base (45%), Conservadora (25%), Disrupción (15%) y Optimista (15%). Los casos "
            "Conservador/Base/Optimista de la plantilla quedan como referencia técnica."),
    "A50": "Riesgo en el descuento",
    "B50": ("Beta 1,0: la del sector (0,63 reapalancada) corresponde a refrescos diversificados; Celsius depende de una "
            "categoría, de un distribuidor y de marcas jóvenes. Regresión: 1,55 (5 años) y 0,83 (2 años)."),
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
    "E12": "='Resumen de Valoración'!D12",
    "E20": "='Balance Sheet'!L5", "E23": "='Input sheet'!B13/'Income Statement'!L16",
    "H4": "=('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1",
    "H5": "=('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1",
    "H6": "=('Income Statement'!K3/'Income Statement'!B3)^(1/9)-1",
    "H12": "=(3380/2515,3)-1",   # consenso de ingresos 2026 (~US$3.380M, 17 analistas) frente a 2025
    "H18": 0, "H19": 0, "H20": 0, "H21": "—", "H22": "—", "H23": "—", "H24": "—",
}

STORIES = {
    "A3": "Celsius: de una marca en hipercrecimiento a un portafolio de tres marcas que crece con la categoría",
    "A4": ("Celsius vende ~US$3.047M al año y ~20% de las bebidas energéticas de EE.UU., pero la mitad de sus ventas ya no es la "
           "marca CELSIUS sino Alani Nu, y todo pasa por PepsiCo. El margen normalizado es ~20,6%, por debajo del 29% de Monster. "
           "La historia Base: el portafolio crece con la categoría (~6% compuesto), CELSIUS se estabiliza, Alani Nu se modera, "
           "Rockstar cae y el margen llega a 21%. Sin una ventaja defendible propia, el retorno después del año 10 vuelve al costo "
           "de capital."),
    "G10": "Año 1 +7,8% (3T26 ≈ 2T26 y Rockstar con un año completo); años 2-5 5,5% compuesto con la categoría.",
    "G11": "Año 1 20% (normalizado del 2T26); objetivo 21% en 5 años, por escala; no recupera todo el margen bruto.",
    "G12": "Tasa efectiva del 1S26 (20,1%) que converge a la marginal de 25%.",
    "G13": "2,0 en los años 1-5 y 1,7 (promedio global Beverage (Soft)) en los años 6-10: incluye compras ocasionales.",
    "G14": "ROIC normalizado ~16,5% con el preferente en el capital; terminal = costo de capital (sin ventaja defendible).",
    "G15": "Ke 9,38% (rf 5,29% + beta 1,0 × ERP 4,09%); Kd 6,5% (SOFR + 2,25%); WACC ~8,9%.",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": 0.078, "D6": "3T26 similar al 2T26 (guía del 6-ago-2026), Rockstar con un año completo y el 1S27 con la categoría.",
    "C7": 0.20, "D7": "Margen normalizado del 2T26: EBITDA ajustado 22,5% − D&A 1,2% − compensación en acciones 1,3%.",
    "C8": 0.055, "D8": "Historia Base: categoría ~6-7% nominal; Alani Nu 7-10%, CELSIUS 3-4%, Rockstar −3 a −6%.",
    "C9": 0.211, "D9": "21% reportado + 0,09 pp de arrendamientos; Monster 29% como techo de largo plazo con distribución propia.",
    "C10": 5, "D10": "La mejora de margen es de escala y compras, no un cambio de modelo.",
    "C11": 2.0, "D11": "Entre la industria (1,54-1,68) y la intensidad orgánica (capex ≈ D&A).",
    "C12": 1.7, "D12": "Promedio global de Beverage (Soft) (1,68).",
}

MULTIPLOS_EVALUACION = (
    "Evaluación CELH (1-oct-2026): los múltiplos Base salen de tres anclas (historia desde FY2024 sin FY2025 ni LTM, peers sin KDP "
    "con −15% y el justificado, λ = 0,5). Valen ~55% más que el DCF Base de las historias. No es un problema de crecimiento sino de "
    "ventaja competitiva: los peers (Coca-Cola, Monster) cotizan con retornos excedentes duraderos y el DCF supone que Celsius no los "
    "conserva después del año 10. El DCF es el valor intrínseco; los múltiplos son precio relativo."
)

VO, INP, COC, RES, ESC = ("'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'",
                          "'Escenarios e historias'")

TESIS_ROWS: list[list] = [
    ["CELH (Celsius Holdings, Inc.) — Tesis de Inversión: De la Historia a los Números (análisis desde cero, 1-oct-2026)"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al 30-sep-2026: US$"&TEXT({RES}!C3;"0.00")&" | WACC inicial: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["Celsius dejó de ser una marca única en hipercrecimiento y pasó a ser un portafolio de tres marcas de bebidas energéticas "
     "distribuido por PepsiCo. Las ventas de 2025 crecieron 85,5%, casi todo por compras; la marca CELSIUS cae al facturar y "
     "apenas cae al consumidor, mientras Alani Nu crece más de 50% al consumidor. El margen GAAP (5,3% LTM) está deprimido por "
     "US$466M de cargos de una vez; el normalizado es ~20,6%. La tensión: si el portafolio puede crecer con la categoría y "
     "sostener ~21% de margen sin una ventaja propia, o si Alani Nu es una moda y CELSIUS sigue perdiendo espacio."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["Portafolio +31% al consumidor en el 2T26 y ~20% de la categoría en EE.UU.; Alani Nu +55,7%.",
     "CELSIUS −11,7% al facturar en el 2T26; la gerencia admitió que la poda de presentaciones fue demasiado profunda."],
    ["Margen normalizado ~20,6% y EBITDA ajustado de 23,7% en el 1S26; caja de US$631M frente a deuda de US$695M.",
     "Margen bruto de 48,1% (−3,4 pp en un año) por promociones, mezcla y aluminio."],
    ["PepsiCo es socio, distribuidor y tenedor de preferentes: incentivos alineados para dar espacio al portafolio.",
     "Más de la mitad de las ventas pasa por PepsiCo; Celsius no controla su distribución."],
    ["Exterior +32% en el 1S26 y meta de más de 15% de las ventas en cinco años.",
     "Investigación del fiscal de Texas sobre Alani Nu y demandas colectivas por la seguridad del producto."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — CASO BASE DE LA HOJA (= historia Base; fórmulas vivas)"],
    ["Supuesto", "Conservador técnico", "Base", "Optimista técnico", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={INP}!B27", f"={VO}!C106",
     "Base +7,8%: 3T26 similar al 2T26 (guía del 6-ago-2026), un año completo de Rockstar y el 1S27 con la categoría."],
    ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={INP}!B29", f"={VO}!D106",
     "Base 5,5%: categoría ~6-7% nominal; Alani Nu 7-10%, CELSIUS 3-4% y Rockstar en declive (historia Base por marca)."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "20%: margen normalizado del 2T26 (EBITDA ajustado 22,5% − D&A 1,2% − compensación en acciones 1,3%)."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 21,1% (21% + arrendamientos): escala en gastos generales; Monster (29,2%) es el techo con distribución propia."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31", "5 años."],
    ["Sales-to-Capital (años 1-5)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "2,0 (1,7 en los años 6-10): entre la industria y la intensidad orgánica, para cubrir compras ocasionales."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "rf 5,29% (UST 10 años, 30-sep-2026) + beta 1,0 × ERP 4,09% (Damodaran, sep-2026) = Ke 9,38%; Kd 6,5% (SOFR + 2,25%)."],
    ["Referencia: margen base normalizado (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "EBIT GAAP LTM US$160,3M + US$466,2M de cargos de una vez = US$626,5M (+ arrendamientos)."],
    [],
    ["3. HISTORIAS ACTIVAS Y RESULTADO (DCF Base = valor intrínseco principal; esperado = complemento)"],
    ["Historia", "Probabilidad", "DCF hoy / acción", "Margen objetivo", "CAGR ingresos 1-5"],
    [f"={ESC}!A5", f"={ESC}!B5", f"={ESC}!H5", f"={ESC}!D5", f"={ESC}!C5"],
    [f"={ESC}!A6", f"={ESC}!B6", f"={ESC}!H6", f"={ESC}!D6", f"={ESC}!C6"],
    [f"={ESC}!A7", f"={ESC}!B7", f"={ESC}!H7", f"={ESC}!D7", f"={ESC}!C7"],
    [f"={ESC}!A8", f"={ESC}!B8", f"={ESC}!H8", f"={ESC}!D8", f"={ESC}!C8"],
    ["DCF esperado por probabilidades (complemento)", f"={ESC}!B10", f"={ESC}!H10", "Precio con MOS sobre el esperado", f"={ESC}!H14"],
    ["Múltiplos consolidados hoy (precio relativo, Base)", "", "='Descuento de múltiplos'!D39", "Precio al 30-sep-2026", f"={RES}!C3"],
    [],
    ["4. LOG DE CORRECCIONES Y AJUSTES (respaldo de cada celda en reference/backups/celh_desde_cero_2026-10-01.json del repo JMR-valuation)"],
    ["#", "Celda / componente", "Antes", "Después", "Razón"],
    [1, "Balance Sheet columna L", "Saldos de dic-2025 (salvo la caja)", "Balance al 30-jun-2026 (10-Q 2T26)", "El pipeline repetía el cierre anual."],
    [2, "Input sheet!B13 (EBIT base)", "=L12 (US$160,3M)", "=L12 + 466,2 (US$626,5M)", "Terminación de distribuidores, integración, litigio y ajuste de inventario (comunicados 4T25 y 2T26)."],
    [3, "Input sheet!B15 (patrimonio en libros)", "=L35 (US$1.199,6M)", "=L35 + 1.759,975", "El capital invertido incluye el preferente que financió Rockstar y la capitanía."],
    [4, "Input sheet!B16 (deuda)", "Neta de costos de emisión + arrendamientos", "US$694,75M nominal", "Valor razonable ≈ principal (10-Q); arrendamientos por el conversor."],
    [5, "Input sheet!B17 / B18", "I+D Yes · arrendamientos No", "No · Yes", "I+D inmaterial; arrendamientos como deuda (Damodaran)."],
    [6, "Input sheet!B22 / B24 / B38-B42", "253,0M · 8,8% · sin opciones", "255,1M (con RSU) · 20,1% · 2,313M opciones a US$6,28", "10-Q 2T26 y 10-K 2025."],
    [7, "Input sheet!B76 y Valuation output!B33/B84/B135", "Sin preferentes", "US$1.135M restados en los tres casos", "Valor de liquidación de las Series A y B (10-Q 2T26)."],
    [8, "Cost of capital worksheet", "Beta del sector · rating A1/A+ · ERP de enero", "Beta 1,0 directa · Kd 6,5% directo · ERP 4,09%", "Riesgo propio; deuda real a tasa variable; ERP de sep-2026."],
    [9, "Input sheet!B4 / D1 / B35", "Fecha y precio de la corrida", "30-sep-2026 · US$27,35 · 5,29%", "Fecha de corte de la valoración."],
    [10, "Descuento de múltiplos fila 38 / 43", "DCF técnico · MOS sobre el ponderado", "Historias · MOS sobre el esperado", "Presentación vigente (1-oct-2026)."],
    [],
    ["5. CONCLUSIÓN"],
    [f'="El DCF Base de las historias es US$"&TEXT({ESC}!H5;"0.00")&" y el esperado US$"&TEXT({ESC}!H10;"0.00")&"; el precio del 30-sep-2026 (US$"&TEXT({RES}!C3;"0.00")&") está "&TEXT({RES}!C3/{ESC}!H5-1;"+0%;-0%")&" frente a la Base. Los múltiplos (US$"&TEXT(\'Descuento de múltiplos\'!D39;"0.00")&") valen más porque los peers cotizan con ventajas duraderas que el DCF no le reconoce a Celsius. El DCF es la lectura más confiable: el valor depende del margen y de la duración de Alani Nu, no de un múltiplo de mercado."'],
    ["Variable clave a monitorear: las ventas al consumidor de CELSIUS y de Alani Nu (Circana) y el margen bruto. Si CELSIUS vuelve a crecer y el margen bruto se recupera a 50%, el caso se mueve hacia la Optimista; si Alani Nu se desacelera a un dígito o llega una restricción regulatoria, hacia la Conservadora o la Disrupción."],
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
