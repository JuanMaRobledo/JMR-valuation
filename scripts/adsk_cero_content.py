"""Contenido de las hojas de texto de la valoración de ADSK desde cero (7-oct-2026; pasos 3 y 10 del prompt v4).
Las cifras de resultado son fórmulas vivas contra el modelo y la pestaña «Escenarios e historias»; las demás salen de
las fuentes citadas (corte de información: 30-sep-2026; hechos posteriores al balance del 31-jul-2026 incluidos)."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: 10-Q del 2T FY27 de Autodesk (28-ago-2026) y 10-K FY26 (3-mar-2026), SEC EDGAR; comunicados del 4T FY26 "
    "(26-feb-2026), 1T FY27 (28-may-2026) y 2T FY27 (27-ago-2026); 8-K de la reestructuración (22-ene-2026), de MaintainX "
    "(28-may y 3-ago-2026), del préstamo puente (15-jun-2026), del papel comercial (13-jul-2026) y de los bonos 2029/2033 "
    "(10-sep-2026); transcripción de la llamada del 2T FY27 (The Motley Fool); Trefis (10-sep-2026); Damodaran (betas, "
    "márgenes, ROIC y ventas/capital por industria, ene-2026; ERP oct-2026); UST 10 años y cierre del 30-sep-2026."
)

CUALITATIVO = {
    "B5": "Autodesk, Inc.",
    "B6": "Andrew Anagnost (presidente y CEO desde 2017). CFO: Janesh Moorjani. Presidente del directorio: Stacy J. Smith.",
    "B7": "Software de diseño, ingeniería, construcción y manufactura (Damodaran: Software (System & Application))",
    "B8": "https://www.autodesk.com  |  IR: https://investors.autodesk.com",
    "B11": "Descripción",
    "A12": "Visión General de la Empresa",
    "B12": ("Software de diseño y gestión de proyectos para arquitectura, ingeniería, construcción y operación (AECO), "
            "manufactura y medios. Ventas LTM a jul-2026 de US$7.790M (97% recurrentes), margen operativo GAAP de 26,2% y "
            "~14.300 empleados (31-ene-2026). Vende por suscripción, directo y a través de revendedores."),
    "A13": "AECO",
    "B13": ("US$3.895M LTM (50%): Revit, Civil 3D, Autodesk Construction Cloud, Forma y Tandem. +17% en el 2T FY27 (+15% en "
            "moneda constante) con la construcción creciendo más de 20%."),
    "A14": "AutoCAD y AutoCAD LT",
    "B14": ("US$1.910M LTM (25%): la herramienta de dibujo estándar (formato DWG). +14% en el 2T FY27 (+11% en moneda "
            "constante), sobre todo por precio."),
    "A15": "Manufactura, M&E y otros",
    "B15": ("Manufactura US$1.488M LTM (Fusion, Inventor; +15% en el 2T FY27); medios y entretenimiento (Maya, 3ds Max, Flow) "
            "y otros US$497M."),
    "A16": "MaintainX (desde ago-2026)",
    "B16": ("Software de mantenimiento y operación de activos comprado el 3-ago-2026 por US$3.530M netos de caja; ARR de más de "
            "US$135M a dic-2026 creciendo más de 50%; sin utilidades. Aporta ~US$60M de ingresos en el 2S FY27."),
    "B21": "Argumento",
    "A22": "Sistema de registro con costos de cambio",
    "B22": ("DWG y Revit son el estándar de intercambio de planos y modelos; los clientes guardan años de proyectos en ellos. "
            "Ingresos 97% recurrentes y retención neta en el extremo alto de 100-110%."),
    "A23": "Precio y margen",
    "B23": ("Fin de los descuentos plurianuales, nuevo modelo de transacción y compensación en acciones en baja (11% → 9% de las "
            "ventas): meta de 41% de margen no GAAP en FY29 frente a ~39% en FY27."),
    "A24": "Caja y recompras",
    "B24": ("Flujo libre de US$2.409M en FY26 y guía de US$2.725-2.750M en FY27; recompra ~50% del flujo libre (US$901M en el "
            "1S FY27)."),
    "B27": "Riesgo",
    "A28": "IA y puestos",
    "B28": ("El mercado teme que la IA generativa reduzca los puestos que compran los estudios y constructoras; la acción cayó "
            "16,6% del 1 al 9-sep-2026 junto con PTC y Bentley pese a subir la guía."),
    "A29": "MaintainX",
    "B29": ("~26 veces el ARR por un negocio sin utilidades, financiado con caja, papel comercial y bonos: diluye el margen de "
            "FY27 y necesita crecer más de 40% varios años para rendir su costo de capital."),
    "A30": "Reorganización comercial",
    "B30": ("Plan de enero de 2026 (~1.000 empleados, US$135-160M de cargos) que cierra la optimización de ventas; Europa "
            "occidental va atrasada en productividad comercial."),
    "A32": SOURCES,
    "A35": "Periodo del Reporte: 1 de julio de 2026 – 30 de septiembre de 2026",
    "B38": "Titular",
    "A39": "Resultados",
    "B39": "2T FY27: ingresos +16% (+14% en moneda constante) a US$2.046M",
    "D39": "Margen GAAP 29% y no GAAP 41%; BPA diluido US$2,33; flujo libre US$561M; RPO corriente +12% (comunicado del 27-ago-2026).",
    "A40": "Guía",
    "B40": "FY27: ingresos US$8.295-8.345M, margen no GAAP ~39%, flujo libre US$2.725-2.750M",
    "D40": "Incluye MaintainX (~US$60M de ingresos en el 2S); el nuevo modelo de transacción suma ~1,5 pp al crecimiento de FY27 y no se repite en FY28.",
    "A41": "MaintainX",
    "B41": "Cierre de la compra el 3-ago-2026",
    "D41": "US$3.530M netos de caja: préstamo de US$1.000M (4,58%), papel comercial y caja (10-Q 2T FY27, nota 19; 8-K del 3-ago-2026).",
    "A42": "Deuda",
    "B42": "Bonos por US$1.000M (5,050% 2029 y 5,650% 2033)",
    "D42": "Colocados el 8-sep-2026 para repagar el préstamo puente (8-K del 10-sep-2026); deuda nominal pro forma US$4.500M.",
    "A43": "Mercado",
    "B43": "La acción cae 16,6% del 1 al 9-sep-2026",
    "D43": "Con PTC (−15,7%) y Bentley (−10,1%): temor a la IA y crecimiento de FY28 sin el nuevo modelo de transacción (Trefis, 10-sep-2026).",
    "B46": "Análisis e impacto en la valoración",
    "A47": "MaintainX pro forma",
    "B47": ("Ventas LTM +US$90M y EBIT −US$80M (estimaciones), caja −US$3.530M y deuda +US$1.000M: el valor de la compra vuelve "
            "por sus ventas en las historias."),
    "A48": "I+D y arrendamientos",
    "B48": ("I+D capitalizado a 3 años (EBIT +US$221M; margen base 27,7%); arrendamientos operativos con el conversor (VP "
            "US$234M; +0,24 pp de margen)."),
    "A49": "Historias",
    "B49": ("Cuatro historias activas: Base (45%), Conservadora (25%), Disrupción (15%) y Optimista (15%); 'Valuation output' "
            "calcula las cuatro con la estructura de Damodaran."),
    "A50": "Riesgo en el descuento",
    "B50": ("Beta 1,43 bottom-up: Software (System & Application) global 1,33 reapalancada con la D/E de mercado (~10%). Prima "
            "3,70% (oct-2026) ponderada por regiones: 4,77%. Kd 5,65% (bonos 2033). WACC 11,40%."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 14300,
    "B12": "='Income Statement'!L30", "B13": "='Input sheet'!B13/'Input sheet'!B12",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "='Valuation output'!B42", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12", "E13": "—", "E14": "—", "E15": "—", "E16": "—", "E17": "—",
    "E20": "='Balance Sheet'!L5", "E23": "='Input sheet'!B13/'Input sheet'!B14",
    "H4": "=('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1",
    "H5": "=('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1",
    "H6": "=('Income Statement'!K3/'Income Statement'!B3)^(1/9)-1",
    "H7": "—", "H8": "—", "H9": "—", "H10": "—",
    "H11": "=('Income Statement'!K27/'Income Statement'!F27)^(1/5)-1",
    "H12": "—", "H13": "—", "H14": "—", "H15": "—",
    "H18": 0, "H19": 0, "H20": 0, "H21": "—", "H22": "—", "H23": "—", "H24": "—",
}

STORIES = {
    "A3": "Autodesk: sistema de registro del diseño y la obra que crece ~10% sin el impulso contable de FY27",
    "A4": ("Autodesk cobra suscripciones por el software donde estudios, constructoras y fabricantes guardan sus modelos y "
           "planos: US$7.790M de ventas LTM, 97% recurrentes, con un margen GAAP de 26%. La historia Base: el crecimiento "
           "orgánico baja de ~14% reportado a ~11% el primer año (sin el nuevo modelo de transacción ni el dólar) y a ~7% en el "
           "año 5; MaintainX crece de 55% a 20%; el margen sube a ~31% GAAP (34% con el I+D como inversión) cuando terminan la "
           "reorganización y la dilución de la compra. Costos de cambio y estándares de archivo sostienen una ventaja durable: "
           "el ROIC después del año 10 es 17,9% (el de la industria topado en el actual)."),
    "G10": "Año 1 11,1% (AECO +12%, AutoCAD +9%, manufactura +10%, M&E +7%, MaintainX +55%); CAGR 1-5 ~9,2%.",
    "G11": "Año 1 28,2% (guía FY27 en base del modelo + arrendamientos); objetivo 34,2% en 5 años (meta de 41% no GAAP − compensación en acciones).",
    "G12": "Tasa efectiva LTM 22% que converge a la marginal de 25%.",
    "G13": "1,205 en los años 1-10 (1,25 sin arrendamientos): el capital nuevo rinde ~31%, con compras recurrentes.",
    "G14": "ROIC actual pro forma 17,9%; terminal 17,9% (industria 20,6% topada en el actual: ventaja durable).",
    "G15": "Ke 12,12% (rf 5,29% + beta 1,43 × ERP por regiones 4,77%); Kd 5,65%; WACC 11,40%; terminal 8,99%.",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": 0.1107, "D6": "Suma por familia: AECO +12%, AutoCAD +9%, manufactura +10%, M&E y otros +7%, MaintainX +55%.",
    "C7": 0.2824, "D7": "Guía FY27 25-27% GAAP en la base del modelo (I+D capitalizado) + 0,24 pp de arrendamientos.",
    "C8": 0.0877, "D8": "Años 2-5 de la Base: 10,3%, 9,3%, 8,3% y 7,3%.",
    "C9": 0.3424, "D9": "34% en la base del modelo (~31% GAAP) + 0,24 pp de arrendamientos.",
    "C10": 5, "D10": "La meta de margen de la gerencia es a FY29-FY30.",
    "C11": 1.2053, "D11": "Rendimiento sobre el capital nuevo ~31% (34,2% × 75% × 1,205), entre el ROIC actual y el orgánico.",
    "C12": 1.2053, "D12": "Igual que los años 1-5: I+D y compras recurrentes.",
}

MULTIPLOS_EVALUACION = (
    "Evaluación ADSK (7-oct-2026, desde cero): los múltiplos Base salen de tres anclas (etapa actual desde FY2026 por la "
    "re-valoración del software con tasas de 5,3%, peers PTC, Bentley y Dassault al cierre del 30-sep-2026 con +5% y el "
    "justificado, λ = 0,25). Los consolidados hoy valen ~8% menos que el DCF Base: no se movió ningún múltiplo para "
    "acercarlos. El chequeo de crecimiento implícito marca EV/FCFF, P/FCFE y P/OCF por debajo del DCF en FY+3: el flujo de "
    "caja de los peers suma la compensación en acciones, que el DCF trata como costo, y el justificado tampoco cierra la "
    "brecha. EV/EBITDA y P/E son coherentes con el DCF. El DCF es el valor intrínseco; los múltiplos son precio relativo."
)

VO, INP, COC, RES, ESC = ("'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'",
                          "'Escenarios e historias'")

TESIS_ROWS: list[list] = [
    ["ADSK (Autodesk, Inc.) — Tesis de Inversión: De la Historia a los Números (análisis desde cero, 7-oct-2026)"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al 30-sep-2026: US$"&TEXT({RES}!B3;"0.00")&" | WACC inicial: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["Autodesk es el sistema de registro del diseño y la obra: sus clientes guardan años de modelos y planos en DWG y Revit, "
     "pagan por suscripción y renuevan casi siempre. La tensión: si la IA es un producto más que Autodesk cobra dentro de la "
     "suscripción y por consumo, o si abarata el diseño y reduce los puestos que pagan. A eso se suma la compra de MaintainX "
     "(US$3.530M por un negocio sin utilidades) y el fin del impulso contable del nuevo modelo de transacción en FY28."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["Ingresos +16% en el 2T FY27, RPO corriente +12% y retención neta en el extremo alto de 100-110%.",
     "~2 pp del crecimiento de FY27 son contables (nuevo modelo de transacción) y ~2 pp del dólar; FY28 vuelve a ~10%."],
    ["Meta de 41% de margen no GAAP en FY29 y compensación en acciones en baja (11% → 9% de las ventas).",
     "La IA generativa puede reducir puestos de dibujo y modelado; AutoCAD LT es el producto más expuesto."],
    ["Flujo libre de ~US$2.700M al año y recompras de ~50% de él.",
     "MaintainX costó ~26 veces su ARR y se pagó con deuda: diluye el margen y rinde poco sobre lo pagado."],
    ["Datos de proyectos y modelos 3D propios para cobrar la IA por consumo (Flex).",
     "La reorganización comercial aún no termina y Europa occidental va atrasada."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — HISTORIAS EN 'VALUATION OUTPUT' (fórmulas vivas)"],
    ["Supuesto", "Conservadora", "Base", "Optimista", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={VO}!C4", f"={VO}!C106",
     "Base 11,1%: facturación orgánica ~10-11% sin el nuevo modelo de transacción ni el dólar, más MaintainX (2T FY27, llamada del 27-ago-2026)."],
    ["Crecimiento de ingresos — Año 2", f"={VO}!D55", f"={VO}!D4", f"={VO}!D106",
     "Base 10,3%; años 3-5 9,3%, 8,3% y 7,3%: cada familia converge al crecimiento de su mercado."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "28,2%: guía FY27 (25-27% GAAP) con el I+D capitalizado + 0,24 pp de arrendamientos."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 34,2% (~31% GAAP): meta de 41% no GAAP en FY29 menos compensación en acciones y amortización de compras."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31", "5 años (la meta de la gerencia es a FY29)."],
    ["Sales-to-Capital (años 1-5)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "1,205 (también en los años 6-10): ~31% sobre el capital nuevo, con I+D y compras recurrentes."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "rf 5,29% (UST 10 años, 30-sep-2026) + beta 1,43 × ERP por regiones 4,77% (Damodaran, oct-2026) = Ke 12,12%; Kd 5,65%."],
    ["Referencia: margen base (B6, con I+D y arrendamientos)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "EBIT GAAP LTM US$2.041M − 80 de MaintainX + 221 de I+D + 19 de arrendamientos; la reestructuración queda como costo."],
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
    ["4. LOG DE CORRECCIONES Y AJUSTES (respaldo de cada celda en reference/backups/adsk_desde_cero_2026-10-07.json del repo JMR-valuation)"],
    ["#", "Celda / componente", "Antes", "Después", "Razón"],
    [1, "Balance Sheet columna L", "Partidas del 31-ene-2026", "Balance al 31-jul-2026 (10-Q 2T FY27)", "El importador repetía el cierre anual."],
    [2, "Income Statement L8 y L11", "SG&A anual (3.066) · otros 79", "SG&A LTM 3.161 · otros −16", "El importador repetía el SG&A anual; el EBIT LTM (2.041) no cambia."],
    [3, "Income Statement fila 23 y Cash Flow (cambio de caja)", "BPA básico y cambio de caja del importador", "Cifras del XBRL", "auditar_estados_sec.py (25 cambios)."],
    [4, "Input sheet!B12 / B13", "Ventas y EBIT LTM", "+90 y −80 de MaintainX pro forma", "Compra del 3-ago-2026, después del balance (estimaciones con nota)."],
    [5, "Input sheet!B16 / B19", "Deuda 3.478 · caja 4.155", "Deuda nominal 4.500 · caja 1.625", "Pago de MaintainX (3.530) y préstamo de 1.000 refinanciado con bonos (8-K)."],
    [6, "Input sheet!B18 y conversor", "Arrendamientos No", "Yes (VP 234)", "Arrendamientos operativos como deuda (Damodaran)."],
    [7, "Input sheet!B22 / B38", "209 M · sin opciones", "214,4 M (con 5,4 M de RSU/PSU)", "Portada y nota de acciones del 10-Q 2T FY27."],
    [8, "Cost of capital worksheet", "País de registro · rating A1/A+ heredado", "Beta global · prima por regiones · Kd 5,65%", "65% de las ventas fuera de EE.UU.; rendimiento de los bonos 2033."],
    [9, "Input sheet!B4 / D1 · Resumen C25", "Fecha y precio de la corrida", "30-sep-2026 · US$209,00", "Fecha de corte común de la cartera."],
    [10, "Input sheet!B49 / B50", "ROIC terminal = costo de capital", "17,9% (industria topada en el actual)", "Ventaja durable: costos de cambio y estándares de archivo, sin erosión visible."],
    [11, "Descuento de múltiplos fila 38 / 43", "DCF de 'Valuation output' · MOS sobre el ponderado", "Historias · MOS sobre el esperado", "Presentación vigente."],
    [],
    ["5. CONCLUSIÓN"],
    [f'="El DCF Base de las historias es US$"&TEXT({ESC}!H5;"0.00")&" y el esperado US$"&TEXT({ESC}!H10;"0.00")&"; el precio del 30-sep-2026 (US$"&TEXT({RES}!B3;"0.00")&") está "&TEXT({RES}!B3/{ESC}!H5-1;"+0%;-0%")&" frente a la Base. Los múltiplos (US$"&TEXT(\'Descuento de múltiplos\'!D39;"0.00")&") quedan ~8% por debajo del DCF. El DCF es la lectura más confiable: el valor depende de cuánto crece Autodesk sin el impulso contable de FY27 y de si el margen GAAP llega a ~31%, no de un múltiplo de mercado."'],
    ["Variable clave a monitorear: la facturación orgánica y la retención neta de FY28, el margen no GAAP y el ARR de MaintainX. Si la facturación orgánica supera 12% con ingresos por consumo de IA visibles, el caso se mueve hacia la Optimista; si la retención baja de 100%, hacia la Conservadora o la Disrupción."],
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
