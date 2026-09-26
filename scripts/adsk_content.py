"""Contenido cualitativo de la valoracion de ADSK (pasos 3 y 9). Las cifras
de resultado de la Tesis son formulas vivas contra el modelo."""
from __future__ import annotations

import model_steps as ms
from nke_content import format_estadisticas  # noqa: F401  (mismo layout de la plantilla)

SOURCES = (
    "Fuentes: 10-K FY2026 y 10-Q Q2 FY2027 de Autodesk (SEC EDGAR, XBRL, cierre 31-jul-2026); comunicado de "
    "resultados Q2 FY2027 (27-ago-2026); 8-K de la emisión de notas (10-sep-2026); Bloomberg, Construction Dive y "
    "AEC Magazine (MaintainX, may-ago 2026); CG Channel (despidos, ene-2026); TIKR (caída del 4-sep-2026 y consenso "
    "de 36 analistas); Investor Day 2025 de Autodesk (meta de margen FY2029); Damodaran Online (indname.xls ene-2026, "
    "ERP sep-2026); CNBC (UST 10 años al 25-sep-2026)."
)

CUALITATIVO = {
    "B5": "Autodesk, Inc.",
    "B6": "Andrew Anagnost (CEO desde 2017). CFO: Janesh Moorjani.",
    "B7": "Software de diseño e ingeniería (Damodaran: Software (System & Application))",
    "B8": "https://www.autodesk.com  |  IR: https://investors.autodesk.com",
    "B11": "Descripción",
    "B12": ("Líder mundial en software de diseño y construcción (AutoCAD, Revit, Fusion, Maya). Ingresos FY2026 (a "
            "ene-2026) de US$7.206M (+18%) y LTM a jul-2026 de US$7.790M, casi todo por suscripción, con margen "
            "bruto de 91%. ~14.300 empleados. En ago-2026 compró MaintainX (mantenimiento y operaciones) por "
            "US$3.530M, su mayor adquisición."),
    "A13": "AECO (arquitectura, ingeniería, construcción y operaciones)",
    "B13": ("US$1.029M en el Q2 FY2027 (+17%), el 50% de los ingresos. Revit, Civil 3D, Autodesk Construction Cloud "
            "y ahora MaintainX: la apuesta es conectar diseño, obra y operación del activo en una sola plataforma."),
    "A14": "AutoCAD / AutoCAD LT y Manufactura (MFG)",
    "B14": ("AutoCAD US$500M (+14%) y MFG US$385M (+15%) en el Q2 FY2027. AutoCAD/DWG es el estándar de dibujo "
            "técnico; en manufactura Fusion (nube) compite con Dassault, PTC y Siemens. Make (Fusion, Build, Flow) "
            "crece 26%."),
    "A15": "Medios y Entretenimiento (M&E) y Otros",
    "B15": ("M&E US$92M (+15%; Maya, 3ds Max, Flow) y Otros US$40M en el Q2 FY2027. Por geografía: Américas "
            "US$898M (+14%), EMEA US$804M (+19%) y APAC US$344M (+14%)."),
    "A16": "Estrategia de Distribución\ny Comercialización",
    "B16": ("Pasó al 'nuevo modelo de transacción' (venta directa y facturación anual en lugar de multianual por "
            "canales), que infló el crecimiento reportado de FY2025-FY2026. En ene-2026 reorganizó ventas y "
            "despidió ~1.000 personas (7%) para redirigir gasto a IA y a la nube de industria."),
    "B21": "Argumento",
    "A22": "Estándar de la industria y crecimiento de doble dígito",
    "B22": ("Ingresos del Q2 FY2027 +16% (+14% sin efecto cambiario), billings +10%, cRPO +12% y FCF del Q2 +24%. "
            "Guía FY2027 elevada: ingresos US$8.295-8.345M (+15-16%) y FCF de US$2.725-2.750M."),
    "A23": "Expansión de márgenes con meta explícita",
    "B23": ("Margen operativo non-GAAP de 41% en el Q2 (+2pp) y ~39% guiado para FY2027. Meta del Investor Day: 41% "
            "non-GAAP en FY2029. Margen GAAP del Q2 de 29% (+4pp)."),
    "A24": "Valuación en mínimos de varios años",
    "B24": ("A ~US$209, cotiza a ~17x la utilidad non-GAAP proyectada (promedio histórico ~28x) y a ~15x el FCF "
            "LTM. 36 analistas: 30 compra, 6 mantener y ningún vender; precio objetivo medio de ~US$315-321."),
    "B27": "Riesgo",
    "A28": "IA generativa y el modelo por usuario (seat)",
    "B28": ("Si la IA reduce la cantidad de diseñadores o dibujantes, el cobro por usuario pierde base. El 4-sep-2026 "
            "la acción cayó 8% (a US$218) en una venta del sector software tras el cambio de CEO de Adobe."),
    "A29": "MaintainX: precio alto y dilución",
    "B29": ("US$3.530M por ~US$135M de ARR (~26x ingresos), financiado con caja y US$2.000M de deuda nueva. Diluye el "
            "margen FY2027 y deja la deuda neta en ~US$3.100M (antes, caja neta)."),
    "A30": "Desaceleración subyacente y tasas altas",
    "B30": ("Billings +10% contra ingresos +16%: el empuje del cambio de modelo de transacción se agota y el RPO "
            "total crece solo 2%. La guía del Q3 quedó debajo del consenso de EPS. UST 10 años de 5,17%, máximo "
            "desde 2007, que castiga a los múltiplos de crecimiento."),
    "A32": SOURCES,
    "A35": "Periodo del Reporte: 28 de mayo de 2026 – 25 de septiembre de 2026",
    "B38": "Titular",
    "A39": "M&A / Estratégico",
    "B39": "Compra de MaintainX por US$3.530M (cerrada el 3-ago-2026)",
    "D39": "Anunciada el 28-may; la mayor adquisición de su historia. Suma ~US$135M de ARR que crece >50%.",
    "A40": "Resultados",
    "B40": "Q2 FY2027: ingresos +16% y guía FY2027 elevada",
    "D40": "Ingresos US$2.046M, margen non-GAAP 41%, EPS non-GAAP US$3,30 (consenso US$3,12). FY2027: ingresos de US$8.295-8.345M.",
    "A41": "Financiamiento",
    "B41": "Emisión de US$1.000M en notas para repagar el préstamo puente",
    "D41": "10-sep-2026: US$500M al 5,05% (2029) y US$500M al 5,65% (2033). Ratings A3 (Moody's) / BBB+ (S&P).",
    "A42": "Mercado / Sector",
    "B42": "Caída de 8% el 4-sep por el temor a la IA en el software",
    "D42": "La venta del sector siguió al cambio de CEO de Adobe; ADSK cerró en US$218 y llegó a US$209 el 25-sep.",
    "A43": "Análisis de Wall St.",
    "B43": "Consenso de compra con precio objetivo ~50% arriba",
    "D43": "36 analistas (24 compra, 6 sobreponderar, 6 mantener); precio objetivo medio de US$315-321 (rango US$276-355).",
    "B46": "Análisis e impacto en la valoración",
    "A47": "MaintainX cambia el balance",
    "B47": ("El pago de US$3.530M se hizo el 3-ago, después del cierre del Q2 (31-jul): el balance del 10-Q todavía "
            "muestra US$4.098M de caja. Impacto: el modelo usa caja pro forma de US$625M (Input!B19) y deuda de "
            "US$3.705M (notas, préstamo puente y arrendamientos). Los ingresos de MaintainX entran en el crecimiento "
            "del Año 1."),
    "A48": "Guía FY2027 y Año 1 del modelo",
    "B48": ("La guía implica +14% en el segundo semestre FY2027 con MaintainX (~+12% orgánico). Con billings "
            "creciendo 10-11%, el Base usa +13% para los próximos 12 meses (≈11% orgánico + ~2pp de MaintainX) y "
            "10% anual en los años 2-5."),
    "A49": "Margen: la meta de 41% non-GAAP",
    "B49": ("41% non-GAAP en FY2029 menos compensación en acciones (~8,5% de ingresos) y amortización de "
            "intangibles (~1,5%, más con MaintainX) da ~31% GAAP, más ~2,5pp del ajuste por capitalizar I+D: margen "
            "objetivo Base de 33,5% en 5 años. Año 1 de 29,5%: la mejora subyacente compensa la dilución de MaintainX."),
    "A50": "IA y tasas: el castigo del múltiplo",
    "B50": ("El mercado paga ~17x la utilidad non-GAAP proyectada por temor a que la IA erosione el cobro por "
            "usuario, con el UST 10 años en 5,17%. Los múltiplos históricos del modelo (P/E ~48-60x GAAP en "
            "2023-2026) son de otro régimen: el DCF es la lectura principal."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 14300,
    "B12": "='Income Statement'!L30", "B13": "='Income Statement'!L13",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "='Eficiencia de capital'!L5", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12",
    # EPS non-GAAP NTM ~US$12,8 (17x forward a US$218, TIKR 4-sep-2026; guía FY2027 US$12,52-12,60)
    "E13": "='Input sheet'!D1/12,8", "E14": "=E13/15",
    "E16": "=IFERROR('Trailing Valuation'!L6/'Financials Multiples'!E57;\"\")",
    # Pro forma MaintainX (pagado el 3-ago-2026, despues del balance del 31-jul)
    "E20": "='Input sheet'!B19", "E21": "='Input sheet'!B16-'Input sheet'!B19", "E23": "='Income Statement'!L12/'Income Statement'!L16",
    "H4": "=('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1",
    "H5": "=('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1",
    "H6": "=('Income Statement'!K3/'Income Statement'!B3)^(1/9)-1",
    "H7": "=('Income Statement'!K24/'Income Statement'!H24)^(1/3)-1",
    "H8": "=('Income Statement'!K24/'Income Statement'!F24)^(1/5)-1",
    "H9": "—",  # EPS FY2017 negativo
    "H10": "=('Cash Flow Statement'!K36/'Cash Flow Statement'!F36)^(1/5)-1",
    "H11": "=('Income Statement'!K26/'Income Statement'!F26)^(1/5)-1",
    "H12": "=('Valuation output'!D5/'Valuation output'!B5)^(1/2)-1",   # modelo Base (13% y 10%)
    "H13": "=('Financials Multiples'!F57/'Income Statement'!K28)^(1/2)-1",
    "H14": 0.19,   # guía original FY2027: EPS non-GAAP +18-20%
    "H15": "—",
    "H18": "—", "H19": "—", "H20": "—", "H21": "—", "H22": "—", "H23": "—", "H24": "—",
}

STORIES = {
    "A3": "Autodesk: el estándar del diseño y la construcción que el mercado castiga por miedo a la IA",
    "A4": ("Autodesk vende US$7.800M por año con margen bruto de 91%, crece 14-16% y tiene una meta explícita de 41% de "
           "margen non-GAAP en FY2029. Acaba de pagar US$3.530M por MaintainX para extender la plataforma de diseño y "
           "obra a la operación de los activos. El mercado la valora a ~17x la utilidad non-GAAP proyectada por temor a "
           "que la IA reduzca los usuarios que pagan y con tasas de 5,17%. La tesis Base: +13% el próximo año (incluye "
           "MaintainX), 10% anual en los años 2-5, margen GAAP ajustado que sube de 29% a 33,5% en 5 años, ROIC "
           "perpetuo de 15% y costo de capital de 10,8%."),
    "G10": "Guía FY2027 (+15-16%) implica ~14% en el H2 con MaintainX; billings +10-11% -> Año 1 13%, años 2-5 10%.",
    "G11": "Año 1 29,5% (base ajustada 29,0%): mejora subyacente menos dilución de MaintainX. Converge a 33,5% (meta 41% non-GAAP FY2029).",
    "G12": "Tasa efectiva LTM de 22% que converge a la marginal de 25%.",
    "G13": "1,5x: bottom-up FY2022-FY2026 con adquisiciones (~1,3x) y orgánico muy superior (poco capex, capital de trabajo negativo).",
    "G14": "ROIC actual ~36% (ajustado por I+D); en perpetuidad 15%, por encima del costo de capital por el foso de estándar (DWG/Revit).",
    "G15": "10,8%: beta global de Software desapalancada 1,33 (1,40 reapalancada), UST 5,17%, ERP 4,32%, Kd 6,17% (A3/BBB+).",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": 0.13, "D6": "Guía FY2027 (+15-16%, con MaintainX) implica ~14% en el H2 FY2027; billings +10-11% anticipan desaceleración.",
    "C7": 0.295, "D7": "Base ajustada por I+D de 29,0% ('Valuation output'!B6); margen GAAP del Q2 de 29% (+4pp) menos la dilución de MaintainX.",
    "C8": 0.10, "D8": "Billings y cRPO crecen 10-12%; el empuje del cambio de modelo de transacción se agota.",
    "C9": 0.335, "D9": "Meta de 41% non-GAAP FY2029 − SBC (~8,5%) − amortización (~1,5%) ≈ 31% GAAP + ~2,5pp de ajuste por I+D. Comparables: Adobe ~36%, Cadence ~30%, PTC ~30% (GAAP).",
    "C10": 5, "D10": "La meta de la empresa es a FY2029 (~2,5 años); se da más plazo por MaintainX y la inversión en IA.",
    "C11": 1.5, "D11": "Bottom-up FY2022-FY2026 incluyendo adquisiciones (~1,3x); el crecimiento orgánico requiere mucho menos capital.",
    "C12": 1.5, "D12": "Se mantiene: las adquisiciones siguen siendo parte del crecimiento.",
}

MULTIPLOS_EVALUACION = (
    "Evaluación ADSK: P/E, EV/EBITDA, EV/FCFF, P/FCFE y P/OCF fueron positivos los 4 años (ene-2023 a ene-2026), así que "
    "el mecanismo nativo (MIN de 4 años) no se rompe por cambios de signo. PERO esos años son de otro régimen de "
    "valuación: P/E GAAP de 48-60x y EV/EBITDA de 30-44x, contra ~24x y ~20x hoy. Por eso los múltiplos dan precios muy "
    "superiores al DCF (P/E Base ~US$557) y se leen como techo si vuelve la valuación histórica. La categoría 'Software' "
    "les da solo 40% del peso (DCF 60%). Además, el EV de 'Trailing Valuation' usa la caja del 31-jul, antes del pago de "
    "MaintainX."
)

VO, INP, COC, RES = "'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'"

TESIS_ROWS: list[list] = [
    ["ADSK (Autodesk, Inc.) — Tesis de Inversión: De la Historia a los Números"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al día del análisis: US$"&TEXT({RES}!C25;"0.00")&" (25-sep-2026) | WACC: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["Autodesk es el estándar del diseño técnico y de la construcción (AutoCAD, Revit) y sigue creciendo 14-16% con "
     "margen bruto de 91%. Pero la acción cayó a ~US$209, cerca de 17x la utilidad non-GAAP proyectada, porque el "
     "mercado teme que la IA reduzca la cantidad de usuarios que pagan y porque el UST 10 años llegó a 5,17%. En "
     "agosto pagó US$3.530M por MaintainX: pasa de caja neta a deuda neta de ~US$3.100M. La pregunta es si el foso "
     "del estándar sostiene crecimiento de doble dígito y la meta de 41% de margen non-GAAP. Con 13% el próximo año, "
     "10% en los años 2-5 y margen que converge a 33,5%, el DCF Base queda cerca del precio actual: la acción no está "
     "cara, pero el DCF tampoco da margen de seguridad."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["Ingresos del Q2 FY2027 +16% (+14% sin efecto cambiario), cRPO +12% y FCF +24%; guía FY2027 elevada a +15-16%.",
     "Billings +10% contra ingresos +16%: el empuje del cambio de modelo de transacción se agota; RPO total +2%."],
    ["Meta de 41% de margen non-GAAP en FY2029 (41% ya en el Q2) y margen GAAP del Q2 de 29% (+4pp).",
     "La IA puede reducir usuarios por proyecto: el 4-sep-2026 la acción cayó 8% en una venta de todo el software."],
    ["MaintainX (~US$135M de ARR creciendo >50%) extiende la plataforma a la operación y mantenimiento de activos.",
     "MaintainX costó ~26x ingresos, diluye márgenes y dejó deuda neta de ~US$3.100M; los despidos de ene-2026 (7%) muestran presión en ventas."],
    ["Valuación en mínimos: ~17x la utilidad non-GAAP proyectada (promedio ~28x); consenso de 36 analistas sin ventas y precio objetivo de ~US$315-321.",
     "UST 10 años en 5,17% (máximo desde 2007): castiga a los múltiplos de crecimiento y encarece la deuda nueva (5,05-5,65%)."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — LOS TRES ESCENARIOS (fórmulas vivas del modelo)"],
    ["Supuesto", "Conservador", "Base", "Optimista", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={INP}!B27", f"={VO}!C106",
     "Base 13%: guía FY2027 (+15-16%) implica ~14% en el H2 con MaintainX (~12% orgánico); billings +10-11%. Conservador 8,5%: la IA frena usuarios (MIN(Base) − 1,5pp). Optimista 14%: la guía se sostiene (MAX(Base) + 1pp)."],
    ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={INP}!B29", f"={VO}!D106",
     "Base 10%: billings y cRPO crecen 10-12% y el cambio de modelo de transacción ya no suma. Desde el año 6 convergen a la tasa libre de riesgo (5,17%)."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "29,5% contra una base ajustada por I+D de 29,0% ('Valuation output'!B6; GAAP LTM 26,2%): la mejora subyacente (Q2 GAAP 29%) compensa la dilución de MaintainX y la amortización de sus intangibles."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 33,5%: meta de 41% non-GAAP FY2029 − SBC (~8,5%) − amortización (~1,5%) ≈ 31% GAAP + ~2,5pp de ajuste por I+D; comparables Adobe ~36%, Cadence y PTC ~30% GAAP. Conservador: se estanca en el margen actual. Optimista: +3pp (nivel Adobe)."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31",
     "5 años: la meta de la empresa es FY2029 (~2,5 años); se da más plazo por MaintainX y la inversión en IA."],
    ["Sales-to-Capital (años 1-5 / 6-10)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "1,5x: bottom-up FY2022-FY2026 con adquisiciones (~1,3x); el crecimiento orgánico casi no requiere capital (capex ~1% de ingresos, capital de trabajo negativo)."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "UST 10 años 5,17% (25-sep-2026) + beta 1,40 (Damodaran Software global desapalancada 1,33) × ERP 4,32% (1-sep-2026) = Ke 11,2%. Kd 6,17% (rating A3/BBB+; notas 2033 al 5,65%). D/(D+E) 6,6%. ROIC perpetuo 15%."],
    ["Referencia: margen base ajustado (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "EBIT LTM US$2.041M + ajuste por capitalizar I+D (US$221M) = US$2.262M sobre ingresos de US$7.790M."],
    [],
    ["3. RESULTADO DEL DCF POR ESCENARIO"],
    ["Escenario", "Valor DCF / acción", "Precio Objetivo Ponderado*", "DCF vs. precio actual", "Ponderado vs. precio actual"],
    ["Conservador", f"={VO}!B86", f"={RES}!C12", f"=B26/{INP}!$B$23-1", f"=C26/{INP}!$B$23-1"],
    ["Base", f"={VO}!B35", f"={RES}!D12", f"=B27/{INP}!$B$23-1", f"=C27/{INP}!$B$23-1"],
    ["Optimista", f"={VO}!B137", f"={RES}!E12", f"=B28/{INP}!$B$23-1", f"=C28/{INP}!$B$23-1"],
    ["Precio actual (GOOGLEFINANCE)", f"={INP}!B23", "Precio al día del análisis", f"={RES}!C25"],
    [f'=IF(AND(B26<B27;B27<B28;C26<C27;C27<C28;{VO}!C55<{INP}!B27;{INP}!B27<{VO}!C106;{VO}!C45<{VO}!C46;{VO}!C46<{VO}!C47);"✔ Orden verificado: Conservador < Base < Optimista en crecimiento, margen objetivo, valor DCF y precio ponderado";"✖ REVISAR: el orden Conservador < Base < Optimista no se cumple")'],
    ["*El Precio Objetivo Ponderado combina el DCF (60%) con 5 múltiplos (EV/FCFF 15%, EV/EBITDA 10%, P/E 5%, P/FCFE 5%, P/OCF 5%) según la categoría 'Software'. Los múltiplos dan precios muy superiores al DCF porque su ancla (MIN de 4 años, ene-2023 a ene-2026) es de antes de la caída del software: P/E GAAP de ~48x contra ~24x hoy. Tomar el DCF como la lectura principal y los múltiplos como techo si vuelve la valuación histórica."],
    [],
    ["4. LOG DE CORRECCIONES ESTRUCTURALES Y AJUSTES (backup de cada fórmula en reference/backups/adsk_formula_backup.json del repo JMR-valuation)"],
    ["#", "Celda / componente", "Antes", "Después", "Razón"],
    [1, "Copia nueva de la plantilla maestra", "—", "Modelo_JMR_ADSK en AAA Finanzas › Análisis › ADSK", "Pedido del usuario: hoja nueva y carpeta propia (la plantilla maestra no se tocó)."],
    [2, "Balance Sheet columna L (LTM)", "Cierre de ene-2026 (salvo la caja)", "Balance real al 31-jul-2026 (10-Q Q2 FY2027)", "El pipeline solo actualiza la caja en la columna LTM."],
    [3, "Balance Sheet L20/L21/K21 (deuda y arrendamientos corrientes)", "0 / vacío", "1.493 (préstamo puente 994 + notas 2027 499) / 52", "Deuda de corto plazo y arrendamientos corrientes no taggeados en los tags del pipeline."],
    [4, "Income Statement filas 15-16 (intereses)", "Fila 16 = ingreso + gasto (FY2026: 163); FY2017-FY2022 en 0", "Gasto bruto: FY2026 80, LTM 86 (Q2 estimado); FY2017-FY2022 = intereses pagados", "Input!B14 tomaba el ingreso por intereses como gasto."],
    [5, "Income Statement L8 / L11 (SG&A LTM)", "3.066 (= FY2026) / 79", "3.161 / −16", "SG&A LTM = FY2026 + H1 FY2027 − H1 FY2026."],
    [6, "Input sheet!B19 (caja)", "=L5 -> 4.155 (31-jul-2026)", "=L5 − 3.530 -> 625", "Pro forma: MaintainX se pagó el 3-ago-2026, después del cierre del Q2."],
    [7, "Input sheet!B20 (activos no operativos)", "0", "594 (títulos negociables LP 202 + inversiones estratégicas 392)", "Autodesk no usa el tag 'LongTermInvestments'."],
    [8, "Input sheet!B4 y Resumen C25 (fecha y precio del análisis)", "14-sep-2026 · US$228,93 (fecha heredada de la plantilla)", "25-sep-2026 · US$209,40", "La fecha de la plantilla no era la del análisis."],
    [9, "Input sheet!B27-B33 (supuestos Base)", "Fórmulas por defecto: 8,1% LTM · B6−2pp · 8,1% · 33,0% · 5 · 1,54 · 1,54", "13% · 29,5% · 10% · 33,5% · 5 · 1,5 · 1,5", "Anclados a la guía FY2027, a la meta de margen FY2029 y a datos bottom-up (paso 4)."],
    [10, "Input sheet!B49/B50 (ROIC en crecimiento estable)", "No (ROIC = WACC 9,3%) -> DCF Base ~US$152", "Sí, 15% -> DCF Base ~US$197", "Foso de estándar (DWG/Revit) y ROIC actual ~36%: sigue por encima del costo de capital en perpetuidad."],
    [11, "Cost of capital worksheet", "Rating A1/A+ heredado · rf 4,99% · ERP 4,23% · vencimiento 3", "Direct Input rf + 1,0% = 6,17% · 5,17% · 4,09% · 5 años", "Rating partido A3/BBB+ (sin fila exacta en la tabla); datos de mercado de sep-2026."],
    [12, "Valuation output!C45 (margen Conservador)", "=B6", "=MIN(B6; Input!B28)", "El Conservador se estanca en el margen actual; nunca por encima del Año 1."],
    [13, "Valuation output!C47 (margen Optimista)", "=B30 + 5pp (38,5%)", "=B30 + 3pp (36,5%)", "Nivel de Adobe (~36% GAAP), el comparable maduro más rentable."],
    [14, "Resumen de Valoración!G3 (tipo de empresa)", "Genérico", "Software (DCF 60%)", "Utilidades GAAP deprimidas por SBC: más peso a DCF y flujo de caja."],
    [15, "Barrido de errores (paso 8)", "12 #DIV/0! en 'Industry Averages(US)'", "Sin cambios", "Preexistentes del dataset de Damodaran (industrias chicas); no dependen de ADSK."],
    [f'="Resultado: DCF Base US$"&TEXT({VO}!B35;"0.00")&" (Conservador US$"&TEXT({VO}!B86;"0.00")&", Optimista US$"&TEXT({VO}!B137;"0.00")&"); precio ponderado Base US$"&TEXT({RES}!D12;"0.00")&"."'],
    [],
    ["5. CONCLUSIÓN"],
    [f'="A US$"&TEXT({INP}!B23;"0.00")&", Autodesk cotiza "&TEXT({INP}!B23/{VO}!B35-1;"+0%;-0%")&" contra su DCF Base (US$"&TEXT({VO}!B35;"0.00")&"), entre el Conservador (US$"&TEXT({VO}!B86;"0.00")&") y el Optimista (US$"&TEXT({VO}!B137;"0.00")&"). El precio ya descuenta un escenario cercano al Base: no hay margen de seguridad en el DCF, pero tampoco un castigo exagerado considerando tasas de 5,17% y la deuda de MaintainX. El precio ponderado Base (US$"&TEXT({RES}!D12;"0.00")&") es mayor solo por los múltiplos históricos de 2023-2026."'],
    ["Variable clave a monitorear: el crecimiento de billings y de cRPO (10% y 12% en el Q2 FY2027). Si se sostienen en doble dígito mientras la IA se monetiza (sin caída de usuarios), el caso se mueve hacia el Optimista; si caen a un dígito medio, confirman el Conservador. Próximo dato: resultados del Q3 FY2027 (fines de nov-2026)."],
    [],
    [SOURCES],
]


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
