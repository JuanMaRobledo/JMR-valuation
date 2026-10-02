"""Contenido cualitativo de la valoración de ONON desde cero (2-oct-2026; pasos 3 y 10 del prompt v4).
Las cifras de resultado son fórmulas vivas contra el modelo y la pestaña «Escenarios e historias»."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: 20-F 2025 de On Holding AG (3-mar-2026) y estados intermedios del 1S26 (6-K del 11-ago-2026), SEC EDGAR; comunicado "
    "del 2T26 (11-ago-2026); Investor Day 2026 (22-sep-2026); comunicado de los cofundadores como co-CEO (25-mar-2026); tipos de "
    "cambio CHF/USD de yfinance; Damodaran (betas y márgenes por industria, ene-2026; ERP sep-2026); UST 10 años y precio del 1-oct-2026."
)

CUALITATIVO = {
    "B5": "On Holding AG",
    "B6": "David Allemann y Caspar Coppetti (cofundadores, co-CEO desde el 1-may-2026). CFO: Frank Sluis. Presidente y COO: Scott Maguire.",
    "B7": "Calzado y ropa deportiva premium (Damodaran: Shoe)",
    "B8": "https://www.on.com  |  IR: https://investors.on-running.com",
    "B11": "Descripción",
    "B12": ("Marca suiza de calzado de running premium (CloudTec, LightSpray), con ropa y accesorios en crecimiento. Ventas LTM a jun-2026 "
            "de CHF 3.220M (US$4.060M): calzado ~92%, ropa ~6%, accesorios ~2%. Mayoristas ~57% y venta directa ~43%. Presente en más de "
            "90 países; ~4.000 empleados. Reporta en francos suizos bajo NIIF."),
    "A13": "Mayoristas",
    "B13": "CHF 1.834M LTM. +12,7% en moneda constante en el 2T26; la gerencia contiene los envíos para proteger el precio lleno. El mayor cliente es 11,6% de las ventas.",
    "A14": "Directo al consumidor",
    "B14": "CHF 1.386M LTM. +34,3% en moneda constante en el 2T26; 45,7% de las ventas del trimestre, con tiendas propias muy rentables.",
    "A15": "Regiones y categorías",
    "B15": "Américas ~54% de las ventas (+13% en moneda constante), EMEA ~26% (+20,5%), Asia-Pacífico ~20% (+54,7%). Ropa +56%.",
    "A16": "Estrategia",
    "B16": ("«Premium Playbook»: innovación, validación con atletas, experiencias propias y precio lleno. Metas 2026-2029: crecimiento de un "
            "dígito alto en los «teens», margen bruto ≥ 65%, EBITDA ajustado ≥ 22% en 2029; fútbol y golf como nuevas categorías."),
    "B21": "Argumento",
    "A22": "Crecimiento con precio lleno",
    "B22": "Ventas +21,6% en moneda constante con margen bruto de 65,4% en el 2T26: crece sin rebajas.",
    "A23": "Venta directa y Asia",
    "B23": "La venta directa crece al triple que los mayoristas y Asia-Pacífico crece >50%: más margen y más mercado por delante.",
    "A24": "Balance y recompras",
    "B24": "Caja de CHF 1.206M (US$1.493M), sin deuda bancaria; recompra de hasta US$1.000M aprobada hasta 2029.",
    "B27": "Riesgo",
    "A28": "Moda",
    "B28": "Marca de 16 años: el running premium puede enfriarse como otras modas deportivas; los mayoristas ya se contienen.",
    "A29": "Moneda y aranceles",
    "B29": "Reporta en francos con ventas en dólares y euros; absorbe aranceles de EE.UU. sin devoluciones en la guía.",
    "A30": "Gobierno",
    "B30": "Cofundadores con acciones Clase B de voto múltiple; co-CEO desde mayo de 2026 y CFO nuevo en 2026.",
    "A32": SOURCES,
    "A35": "Periodo del Reporte: 1 de julio de 2026 – 1 de octubre de 2026",
    "B38": "Titular",
    "A39": "Resultados",
    "B39": "2T26: ventas +13,5% (+21,6% en moneda constante), margen bruto 65,4%, EBITDA ajustado 19,8%",
    "D39": "Venta directa +34,3% y Asia-Pacífico +54,7% en moneda constante; utilidad neta CHF 105M.",
    "A40": "Guía",
    "B40": "2026: crecimiento ~20% en moneda constante (CHF 3.470-3.560M), margen bruto ≥ 65%, EBITDA ajustado 19,5-20%",
    "D40": "Sin devoluciones de aranceles; contención deliberada de los envíos a mayoristas en el 2S26.",
    "A41": "Investor Day",
    "B41": "Metas 2029: ventas ≥ CHF 5.600M, margen bruto ≥ 65%, EBITDA ajustado ≥ 22%; recompra de US$1.000M",
    "D41": "Fútbol y golf como nuevas categorías; Laura Miele, directora independiente líder (22-sep-2026).",
    "A42": "Gestión",
    "B42": "Los cofundadores Allemann y Coppetti, co-CEO desde el 1-may-2026; Martin Hoffmann dejó el cargo",
    "D42": "Frank Sluis, CFO nuevo (su primer trimestre fue el 2T26).",
    "A43": "Mercado",
    "B43": "La acción cayó de US$50,63 (ene-2026) a ~US$30",
    "D43": "Mínimo de 52 semanas de US$26,76 el 15-sep-2026.",
    "B46": "Análisis e impacto en la valoración",
    "A47": "Moneda",
    "B47": ("Los estados NIIF en francos se convierten a dólares al tipo de cambio de cada período (flujos al promedio, saldos al cierre). "
            "LTM: CHF 3.220M de ventas y CHF 444M de resultado operativo a 1,2608 US$/CHF."),
    "A48": "Arrendamientos y acciones",
    "B48": ("NIIF 16: los arrendamientos (US$696M) son la única deuda y el resultado operativo ya excluye su interés. Acciones económicas = "
            "Clase A + Clase B / 10 (336,1M con premios dilutivos)."),
    "A49": "Historias",
    "B49": ("Cuatro historias activas: Base (45%), Conservadora (25%), Disrupción (10%) y Optimista (20%). Los casos "
            "Conservador/Base/Optimista de la plantilla quedan como referencia técnica."),
    "A50": "Ventaja competitiva",
    "B50": "Sin ventaja defendible probada: la marca tiene 16 años. ROIC terminal = costo de capital.",
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 3963,
    "B12": "='Income Statement'!L30", "B13": "='Input sheet'!B13/'Input sheet'!B12",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "='Valuation output'!B42", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12",
    "E20": "='Balance Sheet'!L5", "E23": "='Input sheet'!B13/'Input sheet'!B14",
    "H4": "=('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1",
    "H5": "=('Income Statement'!K3/'Income Statement'!G3)^(1/4)-1",
    "H6": "=('Income Statement'!K3/'Income Statement'!G3)^(1/4)-1",
    "H12": 0.20,    # guía 2026: crecimiento ~20% en moneda constante
    "H18": 0, "H19": 0, "H20": 0, "H21": "—", "H22": "—", "H23": "—", "H24": "—",
}

STORIES = {
    "A3": "On: una marca premium de running que se vuelve marca deportiva global, sin ventaja todavía probada",
    "A4": ("On vende ~US$4.060M al año, crece ~20% en moneda constante y gana un margen bruto de 65% con precio lleno. La historia Base: "
           "~17,5% el primer año y ~14% anual después, con la venta directa y Asia como motores, y un margen operativo que sube de 14% a "
           "16,5%. La marca tiene 16 años: sin un ciclo completo probado, el retorno después del año 10 vuelve al costo de capital."),
    "G10": "Año 1 +17,5% (guía 2026, mayoristas contenidos); años 2-5 ~14% (venta directa 14-24%, mayoristas 8-10%).",
    "G11": "Año 1 14% (margen NIIF del 1S26); objetivo 16,5% en 5 años (meta de EBITDA ajustado ≥ 22% en 2029).",
    "G12": "20% (normalizada; LTM 7,9% por impuestos diferidos), que converge a 23% marginal.",
    "G13": "2,3 en los años 1-5 y 2,1 (Shoe) en los años 6-10; On rota hoy ~2,6.",
    "G14": "ROIC ~28,5% LTM; terminal = costo de capital (sin ventaja defendible probada).",
    "G15": "Ke 10,56% (rf 5,24% + beta 1,30 × ERP 4,09%); arrendamientos al 6%; WACC ~10,2%.",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": 0.175, "D6": "Guía 2026 (~20% en moneda constante) con mayoristas contenidos; venta directa +30%.",
    "C7": 0.14, "D7": "Margen operativo NIIF del 1S26 (14,1%).",
    "C8": 0.14, "D8": "Historia Base: venta directa 14-24%, mayoristas 8-10%.",
    "C9": 0.165, "D9": "Meta de EBITDA ajustado ≥ 22% en 2029 ≈ 15,5% operativo, con algo más de escala.",
    "C10": 5, "D10": "Escala en gastos en cinco años.",
    "C11": 2.3, "D11": "Rotación propia ~2,6; más tiendas y nuevas categorías.",
    "C12": 2.1, "D12": "Promedio global de Shoe.",
}

MULTIPLOS_EVALUACION = (
    "Evaluación ONON (2-oct-2026): los múltiplos Base salen de tres anclas (historia desde Dec '23, peers con +25% por crecimiento y el "
    "justificado, λ = 0,5). Valen ~40% más que el DCF Base: el justificado supone que el ROE de FY+3 dura para siempre y la historia de On "
    "refleja la etapa de hipercrecimiento, mientras el DCF lleva el ROIC al costo de capital después del año 10. El DCF es el valor "
    "intrínseco; los múltiplos son precio relativo."
)

VO, INP, COC, RES, ESC = ("'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'",
                          "'Escenarios e historias'")

TESIS_ROWS: list[list] = [
    ["ONON (On Holding AG) — Tesis de Inversión: De la Historia a los Números (análisis desde cero, 2-oct-2026)"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al 1-oct-2026: US$"&TEXT({RES}!B3;"0.00")&" | WACC inicial: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["On pasó en 16 años de una zapatilla suiza de nicho a una marca de running premium global que factura ~US$4.000 millones, crece "
     "~20% en moneda constante y gana un margen bruto de 65% sin rebajas. Vende cada vez más directo al consumidor y crece rápido en Asia "
     "y en ropa. La acción cayó ~40% desde enero de 2026 por el enfriamiento del sector y la contención de los mayoristas. La tensión: si "
     "On se vuelve una marca deportiva global duradera o si es una moda que se enfría, como otras antes."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["Crecimiento de 21,6% en moneda constante con margen bruto de 65,4% en el 2T26.",
     "Mayoristas +4,8% en francos en el 2T26: la gerencia frena los envíos en un mercado con rebajas."],
    ["Venta directa +34% y Asia-Pacífico +55%: más margen y más mercado.",
     "Marca de 16 años sin un ciclo de moda completo superado."],
    ["Metas 2029 creíbles (la gerencia superó las de 2026) y recompra de US$1.000M.",
     "Cambio de liderazgo (co-CEO fundadores, CFO nuevo) en pleno crecimiento."],
    ["Caja de US$1.493M, sin deuda bancaria; capex de ~3% de las ventas.",
     "Franco fuerte y aranceles de EE.UU. presionan el margen."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — CASO BASE DE LA HOJA (= historia Base; fórmulas vivas)"],
    ["Supuesto", "Conservador técnico", "Base", "Optimista técnico", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={INP}!B27", f"={VO}!C106",
     "Base +17,5%: guía 2026 (~20% en moneda constante) con mayoristas contenidos (comunicado del 11-ago-2026)."],
    ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={INP}!B29", f"={VO}!D106",
     "Base ~14%: venta directa 14-24% y mayoristas 8-10%; algo por debajo de la meta 2029 de la gerencia."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "14%: margen operativo NIIF del 1S26 (14,1%)."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 16,5%: meta de EBITDA ajustado ≥ 22% en 2029 menos D&A y pagos en acciones."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31", "5 años."],
    ["Sales-to-Capital (años 1-5)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "2,3 (2,1 en los años 6-10): rotación propia ~2,6 y promedio de Shoe."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "rf 5,24% (UST 10 años, 1-oct-2026) + beta 1,30 × ERP 4,09% (Damodaran, sep-2026); arrendamientos al 6%."],
    ["Referencia: margen base (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "Resultado operativo NIIF LTM CHF 444M (US$560M a 1,2608), 13,8% de las ventas."],
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
    ["4. LOG DE CORRECCIONES Y AJUSTES (respaldo de cada celda en reference/backups/onon_desde_cero_2026-10-02.json del repo JMR-valuation)"],
    ["#", "Celda / componente", "Antes", "Después", "Razón"],
    [1, "Estados financieros (todas las pestañas)", "Sin datos: el pipeline solo lee 10-K", "Serie NIIF 2021-2025 + LTM desde 'ifrs-full', en US$", "On presenta 20-F y 6-K en francos (scripts/run_onon_cero.py)."],
    [2, "Balance Sheet columna L", "—", "Balance al 30-jun-2026 a 1,2382 US$/CHF", "6-K del 1S26."],
    [3, "Income Statement fila 15", "Gasto financiero con signo negativo", "Gasto bruto en positivo", "La fila 16 lo restaba dos veces."],
    [4, "Balance Sheet fila 20 (2021-2025)", "Arrendamientos corrientes duplicados como deuda", "0", "Sin deuda bancaria; arrendamientos en la fila 21."],
    [5, "Input sheet!B17 / B18", "I+D Yes · arrendamientos No", "No · No", "I+D inmaterial; NIIF 16 ya pone los arrendamientos en el balance."],
    [6, "Input sheet!B22", "—", "336,1M (Clase A + Clase B / 10 + premios)", "Nota 4.5 del 6-K."],
    [7, "Input sheet!B24 / B25", "7,9% · 25%", "20% · 23%", "Tasa normalizada; LTM distorsionado por impuestos diferidos."],
    [8, "Cost of capital worksheet", "ERP de enero", "Beta 1,30 · Kd 6% · ERP 4,09%", "Entre industria y regresión; ERP de sep-2026."],
    [9, "Input sheet!B4 / D1 / B35 / B49", "Fecha y precio de la corrida", "1-oct-2026 · US$30,20 · 5,24% · ROIC terminal = WACC", "Fecha de corte; sin ventaja defendible."],
    [10, "Descuento de múltiplos fila 38 / 43", "DCF técnico · MOS sobre el ponderado", "Historias · MOS sobre el esperado", "Presentación vigente (1-oct-2026)."],
    [],
    ["5. CONCLUSIÓN"],
    [f'="El DCF Base de las historias es US$"&TEXT({ESC}!H5;"0.00")&" y el esperado US$"&TEXT({ESC}!H10;"0.00")&"; el precio del 1-oct-2026 (US$"&TEXT({RES}!B3;"0.00")&") está "&TEXT({RES}!B3/{ESC}!H5-1;"+0%;-0%")&" frente a la Base. Los múltiplos (US$"&TEXT(\'Descuento de múltiplos\'!D39;"0.00")&") valen más porque suponen retornos excedentes duraderos que el DCF no le reconoce a una marca de 16 años."'],
    ["Variable clave a monitorear: el crecimiento de los mayoristas y el margen bruto. Si los mayoristas vuelven a crecer >10% con margen bruto ≥ 65%, el caso se mueve hacia la Optimista; si caen dos trimestres seguidos o el margen bruto baja de 62%, hacia la Conservadora o la Disrupción."],
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
