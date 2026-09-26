"""Contenido cualitativo de la valoracion de AFYA (pasos 3 y 9). Las cifras
de resultado de la Tesis son formulas vivas contra el modelo. El detalle y
las fuentes están en data/AFYA_Research_Fundamental_Modelo_JMR_2026-09-26.md."""
from __future__ import annotations

import model_steps as ms

SOURCES = (
    "Fuentes: 20-F 2025 de Afya (SEC EDGAR, 31-mar-2026) y XBRL ifrs-full; 6-K de resultados 2T26 y estados financieros "
    "al 30-jun-2026 (13-ago-2026); 6-K de la fusión con Yduqs (23-sep-2026) y de las conversaciones (24-ago-2026); MEC "
    "(ENAMED, ene/mar-2026); APM y Agencia Brasil (plazas de medicina); Bloomberg Línea, Exame y Brazil Journal (23/24-sep-2026); "
    "Damodaran Online (Education, ene-2026; ERP y prima país de Brasil, sep-2026); UST 10 años y cotizaciones de AFYA, "
    "YDUQ3 y BRL=X al 25-sep-2026 (yfinance)."
)

CUALITATIVO = {
    "B5": "Afya Limited (Nasdaq: AFYA; B3: A2FY34)",
    "B6": "Virgilio Gibbon (CEO desde 2016). CFO: Luis André Blanco. Controlador: Bertelsmann (84% de los votos).",
    "B7": "Educación médica y soluciones para médicos en Brasil (Damodaran: Education)",
    "B8": "https://www.afya.com.br  |  IR: https://ir.afya.com.br",
    "B11": "Descripción",
    "B12": ("Mayor grupo de educación médica de Brasil: 3.785 plazas de medicina aprobadas (18-sep-2026), 62 campus y "
            "ocupación cercana a 100%. Ingresos 2025 de R$3.697M (+11,9%) y LTM a jun-2026 de R$3.826M; 9.395 "
            "empleados. Fusión con Yduqs firmada el 23-sep-2026 (Afya se incorpora a Yduqs y sale de Nasdaq)."),
    "A13": "Undergraduate (medicina y salud)",
    "B13": ("R$1.762M en el H1 2026 (+7,4%), el 89% de los ingresos. Medicina R$1.499M (+6,5%): 26.421 alumnos (+2,7%) y "
            "cuota neta de R$9.443/mes (+3,9%). Otras carreras de salud +12,9%."),
    "A14": "Continuing Education",
    "B14": ("R$144M en el H1 2026 (+4,6%): preparación para la residencia, posgrados y cursos cortos; alumnos +23,6% "
            "(56.237) con una cuota promedio menor."),
    "A15": "Medical Practice Solutions",
    "B15": ("R$85M en el H1 2026 (+1,5%): Afya Whitebook (decisión clínica) e iClinic (gestión de consultorios). "
            "Pagadores planos (200.547) y usuarios activos −7,9%: el ciclo de inversión de 2026 todavía no rinde."),
    "A16": "Estrategia de Distribución\ny Comercialización",
    "B16": ("Escuelas de medicina en ciudades medianas del Norte y Nordeste con pocas alternativas; costo de adquisición "
            "de R$1.190 por alumno (2025). Dejó de comprar escuelas a gran escala (R$144M en 2025) y devuelve caja: "
            "R$448M en el H1 2026 (106% del flujo de caja libre para el accionista)."),
    "B21": "Argumento",
    "A22": "Activo escaso y regulado",
    "B22": ("La plaza de medicina requiere autorización del MEC; ocupación ~100% y alumnos cautivos 6 años. Margen EBIT "
            "de 32,8% en 2025, contra 17-26% de los grupos educativos de B3."),
    "A23": "Caja y disciplina de capital",
    "B23": ("Caja operativa de R$1.532M en 2025 (antes de intereses); deuda neta sin arrendamientos de 0,8x el EBITDA "
            "ajustado; dividendo de R$3,45 por acción (40% de la utilidad) y recompras de 3% de las acciones en el H1."),
    "A24": "Fusión con Yduqs",
    "B24": ("Crea el lider nacional (~5.900 plazas, ~17% del país) con sinergias estimadas de R$2.000-2.200M de valor "
            "presente; Gibbon sería el CEO de la empresa combinada."),
    "B27": "Riesgo",
    "A28": "Exceso de oferta de plazas",
    "B28": ("El MEC autorizó 77 cursos nuevos (4.412 plazas) entre 2024 y 2025 y hubo ~5.400 plazas abiertas por vía "
            "judicial: el país supero las 50.000 plazas anuales. Presiona la cuota real y la ocupación."),
    "A29": "Regulación de calidad (ENAMED) y fiscal",
    "B29": ("Algunos programás de Afya sacaron nota 2 en el primer ENAMED y quedaron bajo supervisión del MEC (mar-2026). "
            "El Pilar Dos (mínimo de 15%) sube el impuesto: R$133M corrientes en 2025 contra R$24M en 2024."),
    "A30": "Canje fijo con Yduqs",
    "B30": ("6,408347 acciones YDUQ3 por acción: el accionista queda expuesto a Yduqs, al real y al CADE. JPMorgan e "
            "Itaú BBA ven la relación favorable a Yduqs; el estadounidense no calificado recibe efectivo, no acciones."),
    "A32": SOURCES,
    "A35": "Período del Reporte: 13 de agosto de 2026 – 25 de septiembre de 2026",
    "B38": "Titular",
    "A39": "Resultados",
    "B39": "2T26: ingresos +5,7%, EBITDA ajustado +1,4% (margen −180pb) y utilidad neta +14%",
    "D39": "H1 2026: ingresos R$1.985M (+7,0%), EBITDA ajustado R$918M (46,2%), utilidad R$463M; R$448M devueltos al accionista.",
    "A40": "Guía",
    "B40": "Guía 2026 reafirmada",
    "D40": "Ingresos R$3.950-4.100M, EBITDA ajustado R$1.700-1.800M y capex R$340-380M; supone una buena captación en el 2S26.",
    "A41": "M&A",
    "B41": "Acuerdo vinculante de fusión con Yduqs (23-sep-2026)",
    "D41": "Afya 69,0% / Yduqs 31,0%; Bertelsmann 47,4% de la combinada; salida de Nasdaq; cierre a más tardar el 31-mar-2028.",
    "A42": "Regulación",
    "B42": "MEC: +17 plazas en Cruzeiro do Sul; supervisión por ENAMED",
    "D42": "3.785 plazas aprobadas (18-sep-2026). Las medidas cautelares por ENAMED no afectan 2026 según la empresa.",
    "A43": "Mercado / Wall St.",
    "B43": "El canje favorece a Yduqs según JPMorgan e Itaú BBA",
    "D43": "JPMorgan: canje justo 6,08 (paridad US$12,76 por AFYA). La acción cerró en US$13,00 el 25-sep (−5,3%), cerca del mínimo de 52 semanas.",
    "B46": "Análisis e impacto en la valoración",
    "A47": "Valor standalone contra valor del canje",
    "B47": ("El modelo valúa el negocio de Afya solo (DCF + múltiplos). Desde el 23-sep la acción sigue a la relación de "
            "canje (6,408347 x YDUQ3 / R$ por US$): la Tesis compara ambos valores con fórmulas vivas."),
    "A48": "Moneda y riesgo país",
    "B48": ("Todo en US$: cada año convertido a su tipo de cambio (flujos al promedio, saldos al cierre). El crecimiento "
            "en US$ descuenta ~1,5pp de diferencial de inflación; el costo de capital suma la prima país de Brasil (3,24%)."),
    "A49": "Impuestos",
    "B49": ("PROUNI deja la tasa efectiva en ~11%; el modelo la lleva al 15% del Pilar Dos (Afya es parte del grupo "
            "Bertelsmann), no a la corporativa de 34%."),
    "A50": "Múltiplos deprimidos",
    "B50": ("P/E de 25,8x en 2023 contra 10,4x en 2025 y 7,9x LTM: el ancla Base (mínimo positivo de 4 cierres) ya es el "
            "múltiplo post-derrumbe del sector, no el de la euforia post-IPO."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 9395,
    "B12": "='Income Statement'!L30", "B13": "='Income Statement'!L13",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "='Eficiencia de capital'!L5", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12",
    "E13": "=IFERROR('Input sheet'!D1/'Financials Multiples'!E72;\"\")", "E14": "—",
    "E15": "=IFERROR('Trailing Valuation'!L6/'Financials Multiples'!E43;\"\")",
    "E16": "=IFERROR('Trailing Valuation'!L6/'Financials Multiples'!E57;\"\")",
    "E20": "='Balance Sheet'!L5", "E21": "='Input sheet'!B16-'Input sheet'!B19",
    "E22": "='Input sheet'!B16/'Input sheet'!B15", "E23": "='Income Statement'!L12/'Income Statement'!L16",
    "H4": "=('Income Statement'!K3/'Income Statement'!H3)^(1/3)-1",
    "H5": "=('Income Statement'!K3/'Income Statement'!F3)^(1/5)-1",
    "H6": "=('Income Statement'!K3/'Income Statement'!E3)^(1/6)-1",   # 6 años (sale a bolsa en 2019)
    "H7": "=('Income Statement'!K24/'Income Statement'!H24)^(1/3)-1",
    "H8": "=('Income Statement'!K24/'Income Statement'!F24)^(1/5)-1",
    "H9": "=('Income Statement'!K24/'Income Statement'!E24)^(1/6)-1",
    "H10": "=('Cash Flow Statement'!K36/'Cash Flow Statement'!F36)^(1/5)-1",
    "H11": "=('Income Statement'!K26/'Income Statement'!F26)^(1/5)-1",
    "H12": "=(4025/3697,3)-1",   # punto medio de la guía 2026 contra 2025 (R$M), 1 año
    "H13": "=(1750/1680,3)-1",   # EBITDA ajustado: guía 2026 contra 2025 (R$M), 1 año
    "H14": "—", "H15": "—",
    "H18": "=IFERROR(Dividendos!L4/'Input sheet'!D1;\"\")", "H19": "=Dividendos!L5", "H20": "=Dividendos!L4",
    "H21": "—", "H22": "—", "H23": "—", "H24": "—",   # dividendos solo desde 2025
}

STORIES = {
    "A3": "Afya: el dueño de las plazas de medicina de Brasil, en la antesala de su fusión con Yduqs",
    "A4": ("Afya compró durante una década escuelas de medicina en el interior de Brasil y hoy tiene 3.785 plazas con "
           "ocupación cercana a 100%, cuotas que suben con la inflación y un margen operativo de 33%. El problema es que "
           "el Estado abrió más de 5.000 plazas en dos años y empezó a medir la calidad con el ENAMED, y la empresa entra "
           "en una etapa de crecimiento de un dígito medio con un ciclo de inversión digital que todavía no rinde. El "
           "23-sep-2026 acordó fusionarse con Yduqs: el modelo valúa el negocio standalone en US$ y lo compara con el "
           "valor de la relación de canje."),
    "G10": "Guía 2026 R$3.950-4.100M (+7% a +11%) y H1 +7% -> ~7,5% en R$; −1,5pp de diferencial de inflación -> Año 1 6% en US$. Años 2-5: ticket ~inflación + maduracion de plazas -> 5%.",
    "G11": "Año 1 31,5% (LTM 32,6% menos el ciclo de inversión: EBITDA ajustado −190pb en el H1 2026). Converge a 33% en 5 años (FY2025 32,8%).",
    "G12": "Tasa efectiva LTM 10,6% (PROUNI) que converge al 15% del Pilar Dos.",
    "G13": "1,5x (años 1-5): crecimiento orgánico con poco capital nuevo; con 1,5x el FCFF del Año 1 (~US$190M) queda en linea con el FCFF real LTM. 1,2x (años 6-10): el crecimiento vuelve a requerir plazas nuevas.",
    "G14": "ROIC actual ~15% (EBIT después de impuestos sobre capital con los intangibles de las compras); converge al costo de capital después del año 10.",
    "G15": "11,2%: rf 5,18% (UST) + beta 1,20 (Education global 0,74 reapalancada con D/E de mercado 72%) x ERP 7,33% (4,09% maduro + 3,24% Brasil) = Ke 14%; Kd 8,7% en US$. Terminal 11% (se mantiene el riesgo país).",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": 0.06, "D6": "Guía 2026: ingresos R$3.950-4.100M (+7% a +11%); H1 +7,0%. En US$ se resta ~1,5pp de diferencial de inflación Brasil-EE.UU.",
    "C7": 0.315, "D7": "Margen EBIT LTM 32,6% menos el ciclo de inversión 2026 (EBITDA ajustado −190pb en el H1).",
    "C8": 0.05, "D8": "Cuota neta de medicina ~inflación (+3,9% en el H1) + maduracion de plazas + salud +13%; sin compras. ~6,5% en R$ -> 5% en US$.",
    "C9": 0.33, "D9": "FY2025 32,8% y H1 2026 34,8% (estacional). Sin expansion adicional: la oferta de plazas nuevas limita la cuota real.",
    "C10": 5, "D10": "La mejora de margen ya esta en los numeros: 5 años.",
    "C11": 1.5, "D11": "Crecimiento orgánico (guía sin compras): con 1,5x el FCFF del Año 1 (~US$190M) coincide con el FCFF real LTM. El marginal histórico (0,7x) incluye R$4.400M de compras.",
    "C12": 1.2, "D12": "Despues del año 5 el crecimiento requiere plazas nuevas (compradas o construidas).",
}

MULTIPLOS_EVALUACION = (
    "Evaluación AFYA: P/E, EV/EBITDA, EV/FCFF, P/OCF y P/FCFE fueron positivos todos los años, así que el mecanismo nativo "
    "funciona: el ancla Base es el mínimo positivo de los cierres dic-22 a dic-25, que cae en dic-2025 (P/E 10,4x, EV/EBITDA "
    "6,5x). Son los múltiplos del sector educativo brasileño después del derrumbe, no los de 2019-2020 (P/E 40-53x). Los "
    "múltiplos en US$ se calcularon con el tipo de cambio de cada año (el real pasó de 3,94 a 6,18). Para comparar: los pares "
    "de B3 (Yduqs, Cogna, Ser, Cruzeiro do Sul, Ânima) cotizan a EV/EBITDA de 4,5-5,2x."
)

VO, INP, COC, RES = "'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'"

HISTORIA = (
    "Afya compró durante una década escuelas de medicina en ciudades medianas de Brasil y hoy es el mayor grupo del país por "
    "plazas (3.785), con ocupación cercana a 100%, cuotas que acompañan la inflación y un margen operativo de 33%. La acción "
    "cayó de US$27 (2019) a US$13 porque el sector educativo brasileño se desvalorizó, las tasas subieron (CDI ~15%) y el "
    "Estado abrió más de 5.000 plazas de medicina en dos años. El 23-sep-2026 Afya firmó su fusión con Yduqs a un canje fijo. "
    "El modelo valúa el negocio standalone en US$ (cada año a su tipo de cambio) y lo compara con el valor del canje."
)

BULL = [
    "Activo regulado y escaso: 3.785 plazas con ocupación ~100%; margen EBIT de 32,8% en 2025, el doble que los grupos diversificados de B3.",
    "Caja operativa de R$1.532M (2025) y deuda neta sin arrendamientos de 0,8x el EBITDA: financia dividendos (40% de la utilidad) y recompras.",
    "Siete años seguidos cumpliendo la guía; la de 2026 (R$3.950-4.100M de ingresos) fue reafirmada en agosto.",
    "~8x la utilidad LTM y ~5x EV/EBITDA: el precio descuenta crecimiento cero y el castigo al sector.",
]
BEAR = [
    "El MEC y los tribunales abrieron >5.000 plazas en 2024-25 (el país supera las 50.000 por año): la escasez se diluye.",
    "Primer ENAMED: programás de Afya con nota 2 y bajo supervisión; el Pilar Dos sube el impuesto (R$133M corrientes en 2025).",
    "Margen EBITDA ajustado −190pb en el H1 2026 y ecosistema digital estáncado (usuarios −7,9%).",
    "Canje fijo con Yduqs: el accionista queda atado a YDUQ3, al real y al CADE; JPMorgan e Itaú BBA lo ven favorable a Yduqs.",
]

LOG = [
    ["Hoja del modelo", "Copia de la valoración de LULU con el nombre AFYA", "Contenido de la plantilla maestra auditada (26-sep-2026)", "Respaldo de la copia anterior en reference/backups/afya_pre_reset.json.gz."],
    ["Loader SEC", "Solo lee us-gaap: AFYA (20-F, IFRS) no tiene datos", "Serie armada desde ifrs-full en scripts/run_afya.py (FY2019-FY2025)", "Emisor extranjero; sale a bolsa en jul-2019 (columnas B-D vacías)."],
    ["Moneda", "Estados en R$", "US$ al tipo de cambio de cada período: flujos al promedio del año, saldos al cierre", "El real pasó de 3,94 a 6,18 por dólar: a un solo spot, los múltiplos históricos quedaban distorsionados."],
    ["Columna LTM", "Sin 10-Q", "FY2025 + H1 2026 − H1 2025 (6-K del 13-ago-2026); balance al 30-jun-2026", "Flujos LTM a R$5,29 por US$; balance a R$5,18."],
    ["Flujo operativo (Cash Flow fila 13)", "OCF reportado antes de intereses (Afya los clasifica en financiamiento)", "OCF − intereses pagados de deuda, vendedores y arrendamientos", "2025: R$1.532M − R$445M. Para que P/OCF y P/FCFE midan caja del accionista."],
    ["Deuda (Balance filas 20/25 y 21/26)", "Solo préstamos", "Préstamos + cuentas por pagar a vendedores + arrendamientos IFRS 16", "Afya incluye a los vendedores en su deuda neta; B18 = No."],
    ["Income Statement fila 16", "Ingreso + gasto financiero sumados", "Gasto financiero bruto", "Mismo bug que ADSK."],
    ["Input sheet!B21 / B25", "0 / 25%", "US$7,8M / 15%", "Participaciones no controladoras; tasa de largo plazo = mínimo del Pilar Dos (PROUNI exime la mayor parte del IRPJ/CSLL)."],
    ["Input sheet!B46:B47", "Terminal = rf + ERP maduro (9,3%)", "11%", "Se mantiene el riesgo país de Brasil en perpetuidad."],
    ["Cost of capital worksheet", "Beta directa · A1/A+ · ERP enero", "Education global (0,74) · Kd directo 8,7% (rf + 2,13% Brasil + 1,38% Ba1) · ERP Brasil 7,33%", "Damodaran, sep-2026; UST 5,18% al 25-sep-2026."],
    ["Valuation output!C45 / C47", "=B6 / =B30 + 5pp", "29% / =B30 + 3pp (36%)", "Conservador: presión de la oferta de plazas. Optimista: 38% superaría a cualquier par."],
    ["Sector fila 2 (AFYA)", "yfinance mezcla precio en US$ con estados en R$", "Fórmulas contra las cifras LTM del libro", "Mismo caso que NVO."],
    ["Resumen de Valoración!C25 / G3", "—", "US$13,00 (cierre del 25-sep-2026) / Madura", "DCF 40%, EV/EBITDA 20%, P/E 20%, EV/FCFF 10%, P/FCFE 5%, P/OCF 5%."],
]


def tesis_rows() -> tuple[list[list], dict]:
    canje = '=6,408347*GOOGLEFINANCE("BVMF:YDUQ3";"price")/GOOGLEFINANCE("CURRENCY:USDBRL")'
    rows: list[list] = [
        ["AFYA (Afya Limited) — Tesis de Inversión: De la Historia a los Números"],
        [f'="Metodología Damodaran (NYU Stern) | Precio al día del análisis: US$"&TEXT({RES}!C25;"0.00")&" (25-sep-2026, Nasdaq) | WACC: "&TEXT({COC}!B14;"0.00%")&" | Cifras en US$ (R$ al tipo de cambio de cada período)"'],
        [],
        ["1. LA HISTORIA"],
        [HISTORIA],
        [],
        ["Caso alcista (Bull)", "", "", "Caso bajista (Bear)"],
    ]
    idx: dict = {"bull_start": len(rows) + 1}
    rows += [[b, "", "", s] for b, s in zip(BULL, BEAR)]
    idx["bull_end"] = len(rows)
    rows += [[], ["2. DE LA HISTORIA A LOS NÚMEROS — LOS TRES ESCENARIOS (fórmulas vivas del modelo)"]]
    rows.append(["Supuesto", "Conservador", "Base", "Optimista", "Justificación y fuente (dato real)"])
    idx["head2"] = len(rows)
    rows += [
        ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={INP}!B27", f"={VO}!C106",
         "Base 6% en US$: guía 2026 R$3.950-4.100M (+7% a +11% en R$) y H1 +7,0% -> ~7,5% en R$ menos ~1,5pp de diferencial de inflación Brasil-EE.UU. Conservador y Optimista: regla de la plantilla (mín −1,5pp / máx +1pp)."],
        ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={INP}!B29", f"={VO}!D106",
         "Base 5%: cuota neta de medicina ~inflación (+3,9% en el H1), maduración de plazas y salud +13%, sin compras (~6,5% en R$). Desde el año 6 convergen a la tasa libre de riesgo."],
        ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
         "31,5%: margen LTM de 32,6% menos el ciclo de inversión de 2026 (EBITDA ajustado −190pb en el H1 por nómina y marketing en Continuing Education y Medical Practice Solutions)."],
        ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
         "Base 33% (FY2025 32,8%): sin expansión adicional porque la oferta de plazas nuevas limita la cuota real; Laureate 36%, pares de B3 17-26%. Conservador 29%: presión de precios y ocupación. Optimista 36%: sinergias y regulación de calidad que favorece a los grandes."],
        ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31",
         "5 años: la mejora de margen ya está en los números; el riesgo es de baja, no de subida lenta."],
        ["Sales-to-Capital (años 1-5 / 6-10)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
         "1,5x (años 1-5): crecimiento orgánico con poco capital nuevo; con 1,5x el FCFF del Año 1 (~US$190M) coincide con el FCFF real LTM. El marginal histórico (0,7x) incluye R$4.400M de compras. 1,2x en los años 6-10."],
        ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
         "rf 5,18% (UST 10 años, 25-sep-2026) + beta 1,20 (Damodaran Education global desapalancada 0,74, D/E 72% a mercado) x ERP 7,33% (4,09% maduro + 3,24% de prima país de Brasil) = Ke 14,0%. Kd 8,7% en US$ (rf 5,18% + 2,13% soberano + 1,38% Ba1). D/(D+E) 42%. Terminal 11%."],
        ["Referencia: margen base (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
         "EBIT LTM a jun-2026: R$1.246,8M sobre ingresos de R$3.826,3M (32,6%)."],
    ]
    idx["assump_end"] = len(rows)
    rows += [[], ["3. RESULTADO POR ESCENARIO Y VALOR DE LA RELACIÓN DE CANJE CON YDUQS"]]
    rows.append(["Escenario", "Valor DCF hoy / acción", "Precio objetivo ponderado (3 años)", "DCF vs. precio del análisis", "Ponderado vs. precio del análisis"])
    idx["head3"] = len(rows)
    r0 = len(rows) + 1
    price = f"{RES}!$C$25"
    rows += [
        ["Conservador", f"={VO}!B86", f"={RES}!C12", f"=B{r0}/{price}-1", f"=C{r0}/{price}-1"],
        ["Base", f"={VO}!B35", f"={RES}!D12", f"=B{r0 + 1}/{price}-1", f"=C{r0 + 1}/{price}-1"],
        ["Optimista", f"={VO}!B137", f"={RES}!E12", f"=B{r0 + 2}/{price}-1", f"=C{r0 + 2}/{price}-1"],
        ["Valor de la relación de canje hoy (6,408347 × YDUQ3 ÷ R$ por US$)", canje, "", f"=B{r0 + 3}/{price}-1", ""],
        [f'=IF(AND(B{r0}<B{r0 + 1};B{r0 + 1}<B{r0 + 2};C{r0}<C{r0 + 1};C{r0 + 1}<C{r0 + 2};{VO}!C55<{INP}!B27;{INP}!B27<{VO}!C106;{VO}!C45<{VO}!C46;{VO}!C46<{VO}!C47);"✔ Orden verificado: Conservador < Base < Optimista en crecimiento, margen objetivo, valor DCF y precio ponderado";"✖ REVISAR: el orden Conservador < Base < Optimista no se cumple")'],
        ["*El Precio Objetivo Ponderado combina el DCF llevado a 3 años (40%) con 5 múltiplos (EV/EBITDA 20%, P/E 20%, EV/FCFF 10%, P/FCFE 5%, P/OCF 5%) según la categoría 'Madura'. El valor de la relación de canje es lo que recibe hoy un accionista de Afya en acciones de Yduqs si la fusión se cierra; es lo que en la práctica sigue la cotización desde el 23-sep-2026."],
    ]
    idx["res_rows"] = (r0, r0 + 3)
    idx["check"] = len(rows) - 1
    rows += [[], ["4. LOG DE AJUSTES (backup de cada fórmula en reference/backups/afya_formula_backup.json del repo JMR-valuation)"]]
    rows.append(["#", "Celda / componente", "Antes", "Después", "Razón"])
    idx["head4"] = len(rows)
    idx["log_start"] = len(rows)
    rows += [[i + 1, *row] for i, row in enumerate(LOG)]
    idx["log_end"] = len(rows)
    rows += [[], ["5. CONCLUSIÓN"]]
    rows.append([f'="A US$"&TEXT({price};"0.00")&", Afya cotiza por debajo de su DCF standalone Base (US$"&TEXT({VO}!B35;"0.00")&", "&TEXT({VO}!B35/{price}-1;"+0%;-0%")&") y de su Conservador (US$"&TEXT({VO}!B86;"0.00")&"): el mercado paga ~5x EBITDA por un negocio que genera caja y crece con la inflación. Pero desde el 23-sep-2026 el precio sigue a la relación de canje con Yduqs (hoy US$"&TEXT({canje[1:]};"0.00")&"), no al valor standalone: la diferencia entre ambos es lo que el accionista cede en la fusión, salvo que las sinergias (R$2.000-2.200M de valor presente) y la prima de control del grupo combinado la compensen."'])
    idx["concl"] = len(rows)
    rows.append(["Variables clave a monitorear: la aprobación del CADE (y si exige vender campus de medicina), el precio de YDUQ3 y el real (valor del canje), la cuota neta de medicina contra la inflación y el segúndo ciclo de ENAMED. Si la fusión fracasa, vuelve a mandar el valor standalone; si se cierra, la inversión pasa a ser la empresa combinada."])
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
        merges=[], bold_rows=(), head_rows=(),
        formats=[
            {"range": f"B{a0}:D{a0 + 3}", "format": pct}, {"range": f"B{a1}:D{a1}", "format": pct},
            {"range": f"B{a0 + 4}:D{a0 + 4}", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0"}}},
            {"range": f"B{a0 + 5}:D{a0 + 5}", "format": {"numberFormat": {"type": "NUMBER", "pattern": "0.0\"x\""}}},
            {"range": f"B{a0 + 6}:D{a0 + 6}", "format": {"numberFormat": {"type": "PERCENT", "pattern": "0.00%"}}},
            {"range": f"B{r0}:C{r1}", "format": {"numberFormat": {"type": "CURRENCY", "pattern": "$0.00"}}},
            {"range": f"D{r0}:E{r1}", "format": {"numberFormat": {"type": "PERCENT", "pattern": "+0.0%;-0.0%"}}},
            {"range": f"A{i['check']}", "format": {"textFormat": {"bold": True}}},
        ])
