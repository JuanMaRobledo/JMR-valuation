"""Contenido de las hojas de texto de la valoración de NU desde cero (11-oct-2026; pasos 3 y 10 del prompt v4).
La plantilla maestra trae textos y números de ejemplo de otras empresas en «Cualitativo», «Estadísticas», «Stories to
Numbers» y «Supuestos Recomendados»: aquí se reemplazan todos. Las cifras de resultado son fórmulas vivas contra el modelo
y la pestaña «Escenarios e historias»; las demás salen de las fuentes citadas (corte de información: 30-sep-2026)."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: Nu Holdings, Form 20-F 2025 (8-abr-2026) y 20-F 2023 (19-abr-2024); 6-K de estados financieros y comunicado "
    "del 2T26 (13-ago-2026); 6-K del 1-jun (CFO), 4-jun (recompra), 10-jul (banco en México), 20-jul (Banco Porto Real), "
    "2-sep (Investor Day), 10-sep (EE.UU. y Nu Global) y 30-sep-2026 (Monzo), SEC EDGAR; resumen de la llamada del 2T26 "
    "(Zacks/Yahoo Finance, ago-2026); Damodaran (betas, ROE y costo del capital por industria, ene-2026; ERP oct-2026); "
    "UST 10 años y precio de cierre del 30-sep-2026."
)

CUALITATIVO = {
    "B5": "Nu Holdings Ltd. (Islas Caimán; operación principal en Brasil). Acciones clase A en la NYSE (NU).",
    "B6": "David Vélez (fundador, presidente del directorio y CEO; 74,3% del voto). CFO: Rob Livingston desde el 13-jul-2026.",
    "B7": "Banco digital (Damodaran: Financial Svcs. (Non-bank & Insurance), tabla global)",
    "B8": "https://international.nubank.com.br  |  IR: https://www.investidores.nu",
    "B11": "Descripción",
    "A12": "Visión General de la Empresa",
    "B12": ("Banco digital más grande de América Latina: 138,9 millones de clientes al 2T26 (83,5% activos), sin sucursales. "
            "Ingresos NIIF UDM a jun-2026 de US$19.340M y utilidad de la controladora de US$3.607M (ROE ~29% sobre el "
            "patrimonio medio). 10.027 empleados a dic-2025."),
    "A13": "Brasil",
    "B13": ("~118 millones de clientes (86% activos), 90,9% de los ingresos de clientes del 1S26 (US$7.577M, +53% en dólares). "
            "Tarjetas, préstamos, cuenta con rendimiento (100% del CDI), inversiones, seguros y pymes (6,8 millones)."),
    "A14": "México",
    "B14": ("15,8 millones de clientes al 2T26 (16 millones en julio), 7,2% de los ingresos de clientes (US$604M, +87%). Opera "
            "como banco múltiple desde el 6-ago-2026 (autorización de la CNBV del 9-jul-2026)."),
    "A15": "Colombia, EE.UU. y Nu Global",
    "B15": ("Colombia: más de 5 millones de clientes. EE.UU.: cuentas y tarjeta desde el 10-sep-2026 con Lead Bank (licencia "
            "nacional con aprobación condicional de la OCC). Nu Global: cuenta multimoneda con stablecoins. 1,8% de los ingresos."),
    "A16": "Fondeo y distribución",
    "B16": ("Depósitos de US$45.328M al 30-jun-2026 a 88% de la tasa interbancaria; adquisición orgánica de clientes (marketing "
            "1,8% de los ingresos); costo de servir ~US$1 por cliente activo al mes."),
    "B21": "Argumento",
    "A22": "ROE alto con crecimiento",
    "B22": ("ROE de 18% (2023) a 29% (UDM) sobre el patrimonio medio mientras el patrimonio crecía 48% en 2025; utilidad "
            "trimestral récord de US$1.061M en el 2T26 (ROE anualizado 33%)."),
    "A23": "Ventaja de costos y datos",
    "B23": ("Costo de servir de ~US$1 frente a un ingreso de ~US$17 por cliente activo; eficiencia de 19,5%; modelos de crédito "
            "propios (NuFormer); la mora de clientes con Nu como banco principal es ~la mitad del promedio."),
    "A24": "México como segundo motor",
    "B24": ("Banco desde ago-2026; ARPAC de US$12,3 frente a US$5,6 en Brasil a la misma edad; la gerencia plantea un México de "
            "60-70% del tamaño de Brasil en el largo plazo."),
    "B27": "Riesgo",
    "A28": "Ciclo de crédito en Brasil",
    "B28": ("Mora 90+ de 6,9% en el 2T26 (+35 pb) y expansión deliberada a segmentos de más riesgo; la pérdida esperada consume "
            "28% de los ingresos."),
    "A29": "Impuestos y regulación",
    "B29": ("La CSLL de las instituciones de pago sube de 9% a 12% (2026-2027) y 15% (2028); riesgo de topes a tasas de tarjeta y "
            "crédito personal y de crédito vía Pix que sustituya a la tarjeta."),
    "A30": "Competencia y gobierno",
    "B30": ("Itaú, Bradesco, Mercado Pago, Inter y PicPay digitalizan; el fundador controla el voto y aprueba compras grandes "
            "(reportes sobre Monzo en sep-2026, desmentidos por la empresa)."),
    "A32": SOURCES,
    "A35": "Periodo del Reporte: 1 de julio de 2026 – 30 de septiembre de 2026",
    "A38": "Categoría / Tema", "B38": "Titular", "D38": "Detalle Corto",
    "A39": "Resultados", "B39": "2T26: utilidad récord de US$1.061M, ROE 33%",
    "D39": "Ingresos gerenciales US$5.876M (+39% FXN); NIM ajustado 12,4%; mora 15-90 4,8% y 90+ 6,9%; depósitos US$45.300M.",
    "A40": "Regulatorio", "B40": "Nubank México empieza a operar como banco (6-ago-2026)",
    "D40": "Autorización de la CNBV del 9-jul-2026; compra de Banco Porto Real para la licencia bancaria en Brasil (20-jul-2026).",
    "A41": "Estrategia", "B41": "Lanzamiento en EE.UU. y de Nu Global (10-sep-2026)",
    "D41": "Cuenta con 3,50% APY y tarjeta con 1,5% de reembolso vía Lead Bank; Nu Global con USDC y EURC.",
    "A42": "M&A / Capital", "B42": "Nu desmiente que persiga a Monzo (30-sep-2026)",
    "D42": "La acción cayó ~10% el 28-sep tras reportes de una compra de hasta £10.000M; marco de asignación de capital sin cambios.",
    "A43": "Gestión", "B43": "Investor Day el 8-dic-2026; nuevo CFO desde el 13-jul",
    "D43": "Rob Livingston (ex-Visa) reemplaza a Guilherme Lago; primer Investor Day en Nueva York.",
    "B46": "Análisis e impacto en la valoración",
    "A47": "Rama financiera (FCFE)",
    "B47": ("NU se valora como banco: utilidad = ROE × patrimonio contable, reinversión = aumento del patrimonio, descuento al Ke "
            "(10,93%); no se restan depósitos ni se suma caja. Pestaña «DCF FCFE financiero»."),
    "A48": "ROE y ventaja",
    "B48": ("ROE Base de 32% en los años 1-5 y de 18,8% (industria, Damodaran) después del año 10 por ventaja durable; las "
            "historias de erosión llevan el ROE al Ke."),
    "A49": "Historias",
    "B49": ("Cuatro historias activas: Base (45%), Conservadora (25%), Disrupción (10%) y Optimista (20%), calculadas en "
            "«Escenarios e historias» y en «DCF FCFE financiero»."),
    "A50": "Riesgo en el descuento",
    "B50": ("Beta 0,82: la del patrimonio de Financial Svcs. (global, ene-2026), sin reapalancar. Prima por países ponderada por "
            "ingresos (Brasil 90,9%, México 7,2%, Colombia 1,8%): 6,88%. Regresión 0,955 y Bank (Money Center) 0,70 como sensibilidad."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "—", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 10027,
    "B12": "—", "B13": "='Income Statement'!L13",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "—",
    "B20": "—", "B21": "='DCF FCFE financiero'!B10", "B22": "—", "B23": "—",
    "E4": "='Input sheet'!D1/('Income Statement'!L22/'Income Statement'!L26)",
    "E5": "='Input sheet'!D1*'Income Statement'!L27/'Balance Sheet'!L34",
    "E6": "—", "E7": "—", "E8": "—", "E9": "—",
    "E12": "='Resumen de Valoración'!D12", "E13": "—", "E14": "—", "E15": "—", "E16": "—", "E17": "—",
    "E20": "='Balance Sheet'!L3", "E21": "—", "E22": "—", "E23": "—",
    "H4": "=('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1",
    "H5": "=('Income Statement'!K3/'Income Statement'!G3)^(1/4)-1",
    "H6": "—", "H7": "—", "H8": "—", "H9": "—", "H10": "—",
    "H11": "=('Income Statement'!K27/'Income Statement'!G27)^(1/4)-1",
    "H12": "—", "H13": "—", "H14": "—", "H15": "—",
    "H18": 0, "H19": 0, "H20": 0, "H21": "—", "H22": "—", "H23": "—", "H24": "—",
}

ESTADISTICAS_NOTAS = {
    "B5": "Banco: el valor de empresa no aplica (los depósitos son materia prima).",
    "B21": "ROE = utilidad de la controladora UDM / patrimonio medio (dic-25 y jun-26), «DCF FCFE financiero»!B10.",
    "E4": "P/E = precio del corte / utilidad por acción diluida UDM.",
    "E5": "P/B = capitalización del corte (acciones en circulación) / patrimonio de la controladora al 30-jun-2026.",
    "H5": "Solo hay cinco ejercicios (2021-2025): crecimiento compuesto de 4 años desde 2021.",
    "H11": "Acciones en circulación dic-21 → dic-25 (4 años).",
    "E20": "Caja y equivalentes al 30-jun-2026 (sin títulos). En un banco la deuda neta y la cobertura de intereses no aplican.",
}

STORIES = {
    "A3": "Nu Holdings: el banco digital dominante de Brasil que replica su modelo en México",
    "A4": ("Nu tiene 139 millones de clientes y gana un ROE de ~30% con un costo de servir de ~US$1 por cliente. La historia "
           "Base: Brasil madura y crece por productos por cliente, México se vuelve un segundo mercado con licencia bancaria y "
           "el ROE baja de ~36% sobre el patrimonio de inicio a 32% (CSLL, inversión internacional) y a 18,8% después del año "
           "10 por ventaja durable. El banco debe retener patrimonio al ritmo del crecimiento; el riesgo central es el crédito "
           "no garantizado en Brasil. Valor por FCFE (pestaña «DCF FCFE financiero»): las filas de abajo son la plantilla "
           "industrial y quedan como referencia técnica."),
    "G10": "Base año 1 +26,5% (Brasil +24%, México +50%, Colombia y otros +60%); CAGR de 5 años 18,8%.",
    "G11": "Banco: la rentabilidad relevante es el ROE (32% en años 1-5; 18,8% después del año 10), no el margen EBIT.",
    "G12": "Tasa efectiva contable UDM 17,7% (con impuestos diferidos); la gerencial del 2T26 es ~35%; la CSLL sube a 2028.",
    "G13": "No aplica a un banco: la reinversión es el aumento del patrimonio (patrimonio × crecimiento).",
    "G14": "ROE terminal 18,8% (Financial Svcs., Damodaran ene-2026) por ventaja durable; Ke 10,93%.",
    "G15": "Ke 10,93% = rf 5,29% + beta 0,82 × prima por países 6,88%; el FCFE se descuenta al Ke, no al WACC.",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": 0.265, "D6": "Año 1 de la historia Base: Brasil +24%, México +50%, Colombia y otros +60% (FCFE, no FCFF).",
    "C7": "No aplica", "D7": "Banco: la rentabilidad es el ROE (32% en años 1-5), no el margen operativo del FCFF.",
    "C8": 0.18, "D8": "Años 2-5 de la Base: 22,0%, 18,1%, 15,2% y 13,0%.",
    "C9": "No aplica", "D9": "ROE de largo plazo 18,8% (industria, Damodaran) en la pestaña «DCF FCFE financiero».",
    "C10": "No aplica", "D10": "El ROE converge linealmente en los años 6-10.",
    "C11": "No aplica", "D11": "Reinversión = patrimonio del año anterior × crecimiento (regulación de capital).",
    "C12": "No aplica", "D12": "Ídem.",
}

VO, INP, COC, RES, ESC, F = ("'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'",
                             "'Escenarios e historias'", "'DCF FCFE financiero'")

TESIS_ROWS: list[list] = [
    ["NU (Nu Holdings Ltd.) — Tesis de Inversión: De la Historia a los Números (análisis desde cero, 11-oct-2026)"],
    [f'="Metodología Damodaran (NYU Stern), rama financiera (FCFE) | Precio al 30-sep-2026: US$"&TEXT({RES}!B3;"0.00")&" | Ke: "&TEXT({COC}!B63;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["Nu Holdings es el banco digital más grande de América Latina: 139 millones de clientes, un costo de servir de ~US$1 por "
     "cliente activo al mes y un ROE de ~30% en los doce meses a junio de 2026. Crece por clientes en México y por productos "
     "por cliente en Brasil, y financia el crédito con depósitos baratos. La tensión: si la ventaja de costos y datos sostiene "
     "un ROE muy superior al costo del patrimonio mientras la compañía se expande a segmentos de más riesgo, la CSLL sube y "
     "los incumbentes se digitalizan, o si un ciclo de crédito y la regulación llevan el retorno hacia el de un banco común."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["ROE de 18% (2023) a 29% (UDM) con el patrimonio creciendo 48% en 2025; utilidad trimestral récord de US$1.061M.",
     "Mora 90+ de 6,9% (+35 pb en el trimestre) y expansión deliberada a segmentos de más riesgo."],
    ["Costo de servir de ~US$1 y eficiencia de 19,5%; depósitos a 88% de la tasa interbancaria.",
     "CSLL de 9% a 15% en 2028 para instituciones de pago; riesgo de topes a tasas y de crédito vía Pix."],
    ["México banco desde ago-2026, 16 millones de clientes y monetización más rápida que Brasil a la misma edad.",
     "Itaú, Mercado Pago, Inter y PicPay compiten por los mismos clientes y depósitos."],
    ["Recompra de US$1.000M (US$500M ejecutados) con capital excedente.",
     "El fundador controla 74,3% del voto; los reportes sobre Monzo mostraron el riesgo de una compra grande."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — HISTORIAS FCFE (fórmulas vivas)"],
    ["Supuesto", "Conservadora", "Base", "Optimista", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos y patrimonio — Año 1", f"={ESC}!C53", f"={ESC}!C29", f"={ESC}!C101",
     "Base +26,5%: Brasil +24%, México +50%, Colombia y otros +60% (ingresos de clientes del 1S26, nota 34 del 6-K 2T26)."],
    ["Crecimiento — Años 2-5 (promedio)", f"=AVERAGE({ESC}!D53:G53)", f"=AVERAGE({ESC}!D29:G29)", f"=AVERAGE({ESC}!D101:G101)",
     "Base 22,0% → 13,0%: Brasil madura; México sigue en fase de adquisición de clientes; consenso +24% en 2027."],
    ["ROE años 1-5", f"={F}!C5", f"={F}!D5", f"={F}!E5",
     "Base 32%: hoy ~36% sobre el patrimonio de inicio; baja por la CSLL, la inversión internacional y el patrimonio retenido."],
    ["ROE después del año 10", f"={ESC}!G6", f"={ESC}!G5", f"={ESC}!G8",
     "Ventaja durable: ROE de la industria (Financial Svcs., Damodaran ene-2026, 18,8%); la Conservadora vuelve al Ke."],
    ["Patrimonio contable inicial (US$ M)", f"={F}!B12", f"={F}!B12", f"={F}!B12", "Controladora al 30-jun-2026 (6-K 2T26)."],
    ["Crecimiento estable (g)", f"={F}!B5", f"={F}!B5", f"={F}!B5", "Tasa libre en dólares (tope de Damodaran)."],
    ["Costo del patrimonio (Ke)", f"={COC}!B63", f"={COC}!B63", f"={COC}!B63",
     "rf 5,29% (UST 10 años, 30-sep-2026) + beta 0,82 × prima por países 6,88% (Damodaran, oct-2026); constante en perpetuidad."],
    ["Referencia: ROE actual (UDM / patrimonio medio)", f"={F}!B10", f"={F}!B10", f"={F}!B10",
     "Utilidad de la controladora UDM US$3.607M sobre el patrimonio medio de dic-25 y jun-26."],
    [],
    ["3. HISTORIAS ACTIVAS Y RESULTADO (DCF Base = valor intrínseco principal; esperado = complemento)"],
    ["Historia", "Probabilidad", "DCF hoy / acción", "ROE años 1-5", "CAGR ingresos 1-5"],
    [f"={ESC}!A5", f"={ESC}!B5", f"={ESC}!H5", f"={ESC}!D5", f"={ESC}!C5"],
    [f"={ESC}!A6", f"={ESC}!B6", f"={ESC}!H6", f"={ESC}!D6", f"={ESC}!C6"],
    [f"={ESC}!A7", f"={ESC}!B7", f"={ESC}!H7", f"={ESC}!D7", f"={ESC}!C7"],
    [f"={ESC}!A8", f"={ESC}!B8", f"={ESC}!H8", f"={ESC}!D8", f"={ESC}!C8"],
    ["DCF esperado por probabilidades (complemento)", f"={ESC}!B10", f"={ESC}!H10", "Precio con MOS sobre el esperado", f"={ESC}!H14"],
    ["Múltiplos consolidados hoy (precio relativo, Base: P/E)", "", "='Descuento de múltiplos'!D39", "Precio al 30-sep-2026", f"={RES}!B3"],
    [],
    ["4. LOG DE CORRECCIONES Y AJUSTES (respaldo de cada celda en reference/backups/nu_desde_cero_2026-10-11.json del repo JMR-valuation)"],
    ["#", "Celda / componente", "Antes", "Después", "Razón"],
    [1, "Income Statement / Balance Sheet / Cash Flow", "Vacíos (el importador no lee NIIF)", "NIIF 2021-2025 + UDM jun-26", "scripts/nu_datos_niif.py con 20-F 2023 y 2025 y 6-K 2T26."],
    [2, "Balance Sheet columna L", "Saldos de dic-2025", "Saldos al 30-jun-2026", "Balance UDM = último informe."],
    [3, "Income Statement fila 22", "Utilidad consolidada", "Utilidad de la controladora", "Coherencia con el patrimonio de la controladora."],
    [4, "Input sheet B17, B18, B21, B22, D12", "I+D Yes; minoritarios 0; acciones L27; D12 vacío", "No; 2,1; L27 + 52,178; fórmula", "Banco NIIF; puente patrimonial; dilución RSU."],
    [5, "Cost of capital worksheet", "Beta reapalancada; país de registro; rating", "Beta del patrimonio 0,82; prima por países; Kd directo", "Damodaran para bancos; exposición por ingresos."],
    [6, "Pestaña «DCF FCFE financiero»", "No existía", "FCFE con ROE terminal (B11)", "Rama financiera del prompt v4."],
    [7, "Valuation output C45:C48", "ROE de las historias", "Input sheet!B30 (margen técnico)", "El FCFF técnico no usa el ROE como margen."],
    [8, "Financials Multiples (utilidad y FCFE)", "EBIT × (1 − t)", "Utilidad y FCFE de las historias", "Excepción financiera (scripts/financieras.py)."],
    [9, "Descuento de múltiplos C38:E38", "Valuation output", "Escenarios e historias H6/H5/H8", "DCF de hoy = FCFE de las historias."],
    [10, "Resumen G3 y F7:F11", "Genérico", "Financiera; No en EV/EBITDA, EV/FCFF, P/FCFE, P/OCF", "Ciclo de vida y aplicabilidad."],
    [11, "Cualitativo, Estadísticas, Stories, Supuestos Recomendados", "Textos y números de ejemplo de otras empresas", "Contenido de NU", "Aislamiento por empresa."],
    [],
    ["5. CONCLUSIÓN"],
    [f'="El DCF Base (FCFE) es US$"&TEXT({ESC}!H5;"0.00")&" y el esperado US$"&TEXT({ESC}!H10;"0.00")&"; el precio del 30-sep-2026 (US$"&TEXT({RES}!B3;"0.00")&") está "&TEXT(ABS({RES}!B3/{ESC}!H5-1);"0%")&IF({RES}!B3<{ESC}!H5;" por debajo";" por encima")&" del DCF Base. El P/E (precio relativo) da US$"&TEXT(\'Descuento de múltiplos\'!D39;"0.00")&": supone que el ROE alto dura más que en el DCF."'],
    ["Variable clave a monitorear: el ROE trimestral, la mora 90+ y la tasa efectiva con la CSLL. Para un banco, el DCF de flujos al accionista (ROE frente al Ke con convergencia explícita) es más confiable que extrapolar el P/E de 2024-2025."],
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
        {"range": "E20", "format": num}, {"range": "H4:H15", "format": pct},
    ])


def write_tesis(sh, backup_path) -> None:
    pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
    cur = {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}
    ms.write_tesis(
        sh, TESIS_ROWS, backup_path, text_rows=range(34, 45),
        merges=[f"A{r}:E{r}" for r in (1, 2, 5, 33, 48, 49, 51)] + [f"B{r}:E{r}" for r in range(7, 12)],
        bold_rows=(4, 13, 24, 33, 47), head_rows=(7, 14, 25, 34),
        formats=[
            {"range": "B15:D18", "format": pct}, {"range": "B20:D22", "format": pct},
            {"range": "B19:D19", "format": {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}}},
            {"range": "B26:B30", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0%"}}},
            {"range": "C26:C31", "format": cur}, {"range": "D26:E29", "format": pct},
            {"range": "E30:E31", "format": cur},
        ])
