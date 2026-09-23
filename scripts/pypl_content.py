"""Contenido cualitativo de la valoracion de PYPL (pasos 3 y 9 del proceso).
Todo dato citado sale de una fuente real (ver SOURCES); ninguna cifra de
resultado del modelo esta escrita a mano en la tabla de resultados de la
Tesis -- son formulas vivas contra 'Valuation output'/'Resumen de Valoración'.
"""
from __future__ import annotations

SOURCES = (
    "Fuentes: 10-K 2025 y 10-Q Q2 2026 (SEC EDGAR, XBRL); comunicado de resultados Q2 2026 (8-K, 28-jul-2026); "
    "comunicados de PayPal del 3-feb-2026 (nuevo CEO) y 29-abr-2026 (reorganización); Bloomberg, Axios, Fortune, "
    "Yahoo Finance y TipRanks (jun-sep 2026); Damodaran Online (indname.xls ene-2026, ERPbymonth sep-2026); "
    "UST 10 años al 22-sep-2026 (CNBC/Trading Economics); consenso de analistas vía yfinance (22-sep-2026)."
)

CUALITATIVO = {
    "B5": "PayPal Holdings, Inc.",
    "B6": "Enrique Lores (desde el 1-mar-2026; reemplazó a Alex Chriss). Presidente independiente del directorio: David W. Dorman.",
    "B7": "Servicios financieros no bancarios / pagos digitales (Damodaran: Financial Svcs. (Non-bank & Insurance))",
    "B8": "https://www.paypal.com  |  IR: https://investor.pypl.com",
    "B11": "Descripción",
    "B12": ("Red de pagos digitales de dos lados: 439 millones de cuentas activas (Q2 2026) y millones de comercios. "
            "Ingresos LTM de US$34.128M, TPV de US$486.400M en el Q2 2026 (+9% sin efecto cambiario) y take rate de "
            "transacción de 1,61%. Desde el 2-jun-2026 opera en tres negocios."),
    "A13": "Checkout Solutions & PayPal",
    "B13": ("Checkout de marca (botón PayPal), PayPal wallet y soluciones para comercios del ecosistema propio. Es el "
            "negocio de mayor margen, pero crece solo +2% sin efecto cambiario (Q2 2026), presionado por Apple Pay, "
            "Shop Pay y la competencia en Europa. Lo dirige Frank Keller."),
    "A14": "Consumer Financial Services & Venmo",
    "B14": ("Venmo (TPV +14% interanual en el Q2 2026; las cuentas activas mensuales de la tarjeta de débito Venmo "
            "crecen más de 50%), BNPL y crédito al consumidor. Es la apuesta de crecimiento: convertir Venmo en una "
            "plataforma financiera completa. Líder interina: Alexis Sowa."),
    "A15": "Payment Services & Crypto",
    "B15": ("Procesamiento no de marca (Braintree, con TPV creciendo en torno al 15%), procesamiento para PyMEs, "
            "servicios de valor agregado y cripto (stablecoin PYUSD). Tiene alto volumen y bajo margen: es lo que "
            "diluye el take rate. Líder interino: Jeff Pomeroy."),
    "A16": "Estrategia de Distribución\ny Comercialización",
    "B16": ("Efecto red: consumidores y comercios se atraen mutuamente, sin sucursales físicas. El plan de Lores "
            "apunta a acercarse al consumidor, simplificar la organización, generar al menos US$1.500M de ahorro "
            "bruto en 2-3 años (reinvertido en su mayoría en producto) y dar metas de ingresos por negocio."),
    "B21": "Argumento",
    "A22": "Escala y generación de caja",
    "B22": ("FCF ajustado de al menos US$6.000M en 2026 (guía) sobre una capitalización de ~US$45.000M (~13% de FCF "
            "yield). Recompró US$6.053M de acciones en los últimos 12 meses: las acciones bajaron de 1.172M (2020) a "
            "855M."),
    "A23": "Valor estratégico confirmado",
    "B23": ("Stripe y Advent ofrecieron US$60,50 por acción (15-jul-2026, más de US$53.000M, financiamiento "
            "comprometido de ~US$50.000M) y el directorio lo rechazó por bajo: pedía cerca de US$70. Un comprador "
            "estratégico le puso un piso de valor muy por encima del precio actual."),
    "A24": "Palancas de crecimiento fuera del checkout",
    "B24": ("Venmo (TPV +14%), Braintree (~15%) y BNPL crecen a doble dígito, y el TPV total crece 9% sin efecto "
            "cambiario. El directorio y el nuevo CEO apuntan a crecimiento de EPS de doble dígito en el tiempo."),
    "B27": "Riesgo",
    "A28": "Erosión del checkout de marca",
    "B28": ("El negocio más rentable crece solo 2% sin efecto cambiario y el take rate cayó 7pb interanual, a 1,61%. "
            "Los transaction margin dollars crecen ~1% (guía 2026: ~US$15.600M vs US$15.500M en 2025) mientras los "
            "ingresos crecen ~4-5%."),
    "A29": "Compresión de márgenes por reinversión",
    "B29": ("Margen operativo GAAP del Q2 2026 de 16,4% (−171pb) y non-GAAP de 17,4% (−248pb); guía de EPS GAAP 2026 "
            "con caída de un dígito medio. Si los ahorros se reinvierten sin retorno, el margen no vuelve al 18% de "
            "2025."),
    "A30": "Ejecución e incertidumbre corporativa",
    "B30": ("Tercer CEO en 3 años, una reorganización en curso, despidos (~600 personas en sep-2026) y una oferta "
            "de compra caída el 27-ago-2026. El consenso es Mantener (36 de 46 analistas), con precio objetivo "
            "promedio de US$56 (18-sep-2026)."),
    "A32": SOURCES,
    "A35": "Periodo del Reporte: 28 de julio de 2026 – 22 de septiembre de 2026 (con contexto desde febrero de 2026)",
    "B38": "Titular",
    "A39": "M&A / Estratégico",
    "B39": "Stripe y Advent abandonan la oferta de US$60,50 por acción",
    "D39": "Oferta del 15-jul, rechazada por el directorio (pedía ~US$70); el consorcio se retiró el 27-ago-2026.",
    "A40": "Resultados",
    "B40": "Q2 2026 supera expectativas y sube la guía anual",
    "D40": "Ingresos de US$8.680M (+5%) y EPS non-GAAP de US$1,38 (vs US$1,28 esperado); guía de EPS 2026 ~US$5,38 y TM$ ~US$15.600M.",
    "A41": "Gestión / Gobierno",
    "B41": "Enrique Lores (ex CEO de HP) asume como CEO el 1-mar-2026",
    "D41": "Reemplaza a Alex Chriss porque el directorio pedía ejecución más rápida; David Dorman pasa a presidente independiente.",
    "A42": "Reestructuración",
    "B42": "Reorganización en 3 negocios, cierre de PayPal Ventures y despidos",
    "D42": "Nuevo modelo operativo desde el 2-jun; PayPal Ventures cerrada en jun-2026; ~600 despidos en sep-2026 (164 en Irlanda).",
    "A43": "Análisis de Wall St.",
    "B43": "Consenso Mantener, precio objetivo promedio de ~US$56",
    "D43": "RBC sube a US$70 (Outperform); Truist baja a US$53; Piper Sandler a US$59; Cantor a US$60; Morgan Stanley en US$45.",
    "B46": "Análisis e impacto en la valoración",
    "A47": "Oferta de Stripe / Advent",
    "B47": ("El 15-jul-2026 Stripe y Advent International ofrecieron US$60,50 por acción (28% de prima), más de "
            "US$53.000M, con ~US$50.000M de financiamiento comprometido por JPMorgan y Morgan Stanley. El directorio "
            "la consideró baja y pidió cerca de US$70. El consorcio se retiró el 27-ago porque su precio se basaba "
            "en el valor previo a los rumores. Impacto: la acción volvió a ~US$52, pero el rango US$60-70 funciona "
            "como referencia de valor de control, coherente con el DCF Conservador de este modelo."),
    "A48": "Resultados Q2 2026 (28-jul-2026)",
    "B48": ("Ingresos de US$8.700M (+5%, +3% sin efecto cambiario), TPV de US$486.400M (+10%), TM$ +1% (+3% sin "
            "intereses sobre saldos) y EPS GAAP de US$1,25 (−3%). Margen operativo GAAP de 16,4% (−171pb). FCF de "
            "US$1.800M y recompras por US$1.500M (33 millones de acciones). Guía 2026: EPS non-GAAP ~US$5,38 (antes: "
            "de leve caída a leve suba), EPS GAAP con caída de un dígito medio y FCF ajustado de al menos US$6.000M. "
            "Es el ancla del margen del Año 1 (B28)."),
    "A49": "Nuevo CEO y reorganización",
    "B49": ("Lores (en el directorio desde 2021 y presidente desde jul-2024) llegó el 1-mar-2026 para acelerar la "
            "ejecución. Reorganizó la empresa en tres negocios (Checkout Solutions & PayPal; Consumer Financial "
            "Services & Venmo; Payment Services & Crypto), va a reportar metas de ingresos por negocio y busca al "
            "menos US$1.500M de ahorro bruto en 2-3 años, reinvertido en su mayoría. Es el ancla de la diferencia "
            "de margen entre Base y Optimista."),
    "A50": "Recortes y foco",
    "B50": ("PayPal cerró su brazo de venture capital (PayPal Ventures, jun-2026) y en sep-2026 despidió a ~600 "
            "personas en varias geografías (12% de la plantilla en Irlanda). La plantilla era de ~23.800 empleados "
            "a dic-2025. Refuerza la tesis de disciplina de costos, pero con riesgo de ejecución durante la "
            "transición."),
}

ESTADISTICAS = {
    "B4": "='Trailing Valuation'!L5", "B5": "='Trailing Valuation'!L6", "B6": "='Input sheet'!B22",
    "B7": "='Income Statement'!L3", "B8": 23800,
    "B12": "='Income Statement'!L30", "B13": "='Income Statement'!L13",
    "B14": "='Income Statement'!L19/'Income Statement'!L3", "B15": "='Income Statement'!L22/'Income Statement'!L3",
    "B16": "='Márgenes'!L9",
    "B21": "='Eficiencia de capital'!L5", "B23": "='Eficiencia de capital'!L3",
    "E4": "='Trailing Valuation'!L13", "E5": "='Trailing Valuation'!L18", "E6": "='Trailing Valuation'!L19",
    "E7": "='Trailing Valuation'!L21", "E8": "='Trailing Valuation'!L16", "E9": "='Trailing Valuation'!L20",
    "E12": "='Resumen de Valoración'!D12",
    # Consenso EPS non-GAAP (yfinance, 22-sep-2026): FY2026 US$5,39 / FY2027 US$5,79 -> NTM ~US$5,69
    "E13": "='Input sheet'!D1/5,69", "E14": "=E13/7,3",
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
    "H12": "=(36210/33172)^(1/2)-1",   # consenso ingresos FY2027 vs FY2025
    "H13": "=('Financials Multiples'!F57/'Income Statement'!K28)^(1/2)-1",  # EBITDA FY+2 del caso Base
    "H14": "=(5,79/5,31)^(1/2)-1",      # consenso EPS non-GAAP FY2027 vs FY2025
    "H15": 0.073,                        # consenso de crecimiento de EPS FY2027
    "H18": "=0,56/'Input sheet'!D1", "H19": "=0,56/'Income Statement'!L24", "H20": 0.56,
    "H21": "—", "H22": "—", "H23": "—", "H24": "— (dividendo iniciado a fines de 2025)",
}

STORIES = {
    "A3": "PayPal: una red de pagos madura, con caja abundante, que el mercado valúa como si se estuviera achicando",
    "A4": ("PayPal ya no es una historia de crecimiento: los ingresos crecen ~4-5%, el checkout de marca +2% y el take rate "
           "cae. Pero es una red de 439M de cuentas que genera ~US$6.000M de FCF por año y recompra ~13% de su "
           "capitalización. A US$52,5 cotiza a ~9x utilidades futuras, como si los márgenes fueran a erosionarse para "
           "siempre. El nuevo CEO reinvierte los ahorros en 2026 (el margen baja) para relanzar Venmo, BNPL y Braintree. "
           "La tesis Base: crecimiento de un dígito medio, margen que vuelve a ~19,5% y costo de capital de 9,2%."),
    "G10": "TPV +10%, pero el take rate baja (1,61%, −7pb): ingresos +4% en el Año 1 (consenso 2026: +4,8%) y 3,5% en los años 2-5.",
    "G11": "Baja a 17,3% en el Año 1 por la reinversión (margen GAAP del Q2 de 16,4%) y sube a 19,5% en 6 años con escala en Venmo/BNPL.",
    "G12": "Tasa efectiva LTM de 16,4% que converge a la marginal de 25%.",
    "G13": "2,6x: relación marginal real 2020-2025 (ΔIngresos / ΔCapital invertido, con I+D capitalizado). CapEx ~2,6% de ingresos, por debajo de D&A.",
    "G14": "ROIC actual ~18% (con US$10.900M de goodwill); la red de dos lados sostiene retornos sobre el WACC hasta el año 10.",
    "G15": "9,2%: beta 1,29 (entre las redes V/MA ~0,7 y el fintech ~1,7-2,7), rating A3/A-, ERP de 4,09% (sep-2026).",
}

SUPUESTOS_RECOMENDADOS = {
    "C6": 0.04, "D6": "Entre el crecimiento del Q2 2026 (+5% nominal, +3% sin efecto cambiario) y el consenso FY2026 (+4,8%); la empresa no da guía de ingresos, solo de TM$ (+~1%).",
    "C7": "='Input sheet'!B28", "D7": "Base ajustada por I+D ('Valuation output'!B6 = 18,1%) menos 0,8pp: el margen GAAP del Q2 2026 fue 16,4% (−171pb) y la guía de EPS GAAP 2026 es de caída de un dígito medio.",
    "C8": 0.035, "D8": "Desacelera: consenso FY2027 +4,2% y TM$ creciendo ~1%. Categoría madura con take rate en baja.",
    "C9": 0.195, "D9": "Algo por encima del máximo GAAP de 10 años de PYPL (18,3% en 2025, ~19% ajustado por I+D) y de la mediana de comparables (16,5%: GPN 16,1%, AFRM 12,6%, XYZ 7,0%). No V/MA (61-66%): son redes puras sin costo de transacción.",
    "C10": 6, "D10": "Reinversión deliberada en 2026: el ahorro de US$1.500M se ejecuta en 2-3 años y el margen tarda en recuperarse.",
    "C11": 2.6, "D11": "Bottom-up: ΔIngresos 2020-25 (+US$11.718M) / ΔCapital invertido con I+D capitalizado (~+US$4.550M).",
    "C12": 2.6, "D12": "Mismo modelo asset-light; el CapEx (~2,6% de ingresos) no escala más rápido que los ingresos.",
}

MULTIPLOS_EVALUACION = (
    "Evaluación PYPL: la utilidad neta, el EBITDA y el FCF fueron POSITIVOS los 10 años (no hay cambio de signo), "
    "así que el mecanismo nativo (Base = MIN de los últimos 4 años) funciona sin reemplazos. Además es el ancla correcta: "
    "PayPal pasó de P/E de 50-66x (2017-2021) a ~10-11x (2025-LTM) y el mínimo de 4 años captura el múltiplo "
    "de hoy, no el de la burbuja de 2021. Resultado: P/E Base ~10,3x, EV/EBITDA ~7,7x y EV/FCFF ~10,5x. Contraste: "
    "V/MA cotizan a ~22x EV/EBITDA y Adyen a ~13x, por eso el rango x0,9 / x1,1 es conservador."
)


VO, INP, COC, RES = "'Valuation output'", "'Input sheet'", "'Cost of capital worksheet'", "'Resumen de Valoración'"

TESIS_ROWS: list[list] = [
    ["PYPL (PayPal Holdings, Inc.) — Tesis de Inversión: De la Historia a los Números"],
    [f'="Metodología Damodaran (NYU Stern) | Precio al día del análisis: US$"&TEXT({RES}!C25;"0.00")&" (22-sep-2026) | WACC: "&TEXT({COC}!B14;"0.00%")'],
    [],
    ["1. LA HISTORIA"],
    ["PayPal dejó de ser una acción de crecimiento y el mercado la castiga como si fuera un negocio en retirada: a US$52,5 "
     "cotiza a ~9x la utilidad esperada y ~7x EV/EBITDA, con un FCF yield de ~13%. Los datos muestran una red enorme "
     "(439M de cuentas, TPV +10%) que monetiza cada vez menos por transacción: el take rate cae y el checkout de marca "
     "crece solo 2%. La tensión central es si el nuevo CEO (Enrique Lores, desde mar-2026) puede convertir los US$1.500M "
     "de ahorro y el impulso de Venmo, BNPL y Braintree en márgenes estables, o si la erosión del checkout de marca se "
     "come la reinversión. El DCF dice que ni siquiera hace falta el escenario optimista: con crecimiento de 2% y el "
     "margen deprimido de 2026 como permanente, la acción vale más que hoy. Lo confirma la oferta de Stripe/Advent a "
     "US$60,50, que el directorio rechazó por baja."],
    [],
    ["Caso alcista (Bull)", "Caso bajista (Bear)"],
    ["FCF ajustado de al menos US$6.000M en 2026 (guía Q2) sobre una capitalización de ~US$45.000M; recompras de US$6.053M en los últimos 12 meses (−27% de acciones desde 2020).",
     "Checkout de marca +2% sin efecto cambiario y take rate de 1,61% (−7pb interanual) en el Q2 2026: el negocio de mayor margen pierde terreno frente a Apple Pay y Shop Pay."],
    ["Valor de control validado: Stripe/Advent ofrecieron US$60,50 (15-jul-2026) y el directorio pidió ~US$70.",
     "TM$ creciendo solo ~1% (guía 2026: US$15.600M vs US$15.500M) contra ingresos de +4-5%: el crecimiento viene de volumen de bajo margen (Braintree)."],
    ["Venmo con TPV +14% y tarjeta de débito con MAUs de más de +50%; Braintree ~+15%; TPV total +9% sin efecto cambiario (Q2 2026).",
     "Margen operativo GAAP del Q2 de 16,4% (−171pb) y guía de EPS GAAP 2026 con caída de un dígito medio: la reinversión puede no tener retorno."],
    ["US$1.500M de ahorro bruto en 2-3 años (~4,4pp de margen si no se reinvirtiera); objetivo de EPS de doble dígito.",
     "Tercer CEO en 3 años, reorganización y despidos en curso; el consenso es Mantener (36 de 46) con precio objetivo de ~US$56."],
    [],
    ["2. DE LA HISTORIA A LOS NÚMEROS — LOS TRES ESCENARIOS (fórmulas vivas del modelo)"],
    ["Supuesto", "Conservador", "Base", "Optimista", "Justificación y fuente (dato real)"],
    ["Crecimiento de ingresos — Año 1", f"={VO}!C55", f"={INP}!B27", f"={VO}!C106",
     "Base: entre el Q2 2026 (+5% nominal / +3% sin efecto cambiario) y el consenso FY2026 (+4,8%). Conservador: Base −1,5pp, en línea con el crecimiento de TM$ de la guía (~+1%) y el checkout de marca (+2%). Optimista: Base x1,3, apalancado en TPV +9-10%."],
    ["Crecimiento de ingresos — Años 2-5", f"={VO}!D55", f"={INP}!B29", f"={VO}!D106",
     "Base desacelera a 3,5% (consenso FY2027 +4,2%, take rate en baja, categoría madura). Desde el año 6, los tres escenarios convergen a la tasa libre de riesgo (regla de Damodaran)."],
    ["Margen operativo — Año 1", f"={VO}!C57", f"={VO}!C6", f"={VO}!C108",
     "Base ajustada por I+D = 18,1% ('Valuation output'!B6) menos 0,8pp. La caída es real: margen GAAP del Q2 2026 de 16,4% (−171pb) y guía de EPS GAAP 2026 con caída de un dígito medio por reinversión."],
    ["Margen objetivo (convergencia)", f"={VO}!C45", f"={VO}!C46", f"={VO}!C47",
     "Base 19,5%: algo por encima del máximo de 10 años de PYPL (18,3% GAAP en 2025) y de la mediana de comparables (16,5%). Conservador: la compresión de 2026 se vuelve permanente (=Año 1). Optimista: los US$1.500M de ahorro caen enteros a margen (+1.500/ingresos LTM = +4,4pp)."],
    ["Años de convergencia de margen", f"={INP}!B31", f"={INP}!B31", f"={INP}!B31",
     "6 años: la empresa reinvierte a propósito en 2026 y el plan de ahorro dura 2-3 años. La recuperación todavía no está demostrada en los resultados."],
    ["Sales-to-Capital (años 1-5 / 6-10)", f"={INP}!B32", f"={INP}!B32", f"={INP}!B32",
     "2,6x bottom-up: ΔIngresos 2020-2025 (+US$11.718M) / ΔCapital invertido con I+D capitalizado (~+US$4.550M). CapEx de 2,6% de ingresos, por debajo de D&A (modelo asset-light). No se usa la mediana de la industria de Damodaran (0,09x), distorsionada por prestamistas."],
    ["Costo de capital (WACC)", f"={COC}!B14", f"={COC}!B14", f"={COC}!B14",
     "Tasa libre de riesgo 4,96% (UST 10 años, 22-sep-2026) + beta 1,29 (regresión de 5 años; beta desapalancada implícita 1,07, entre redes V/MA ~0,7 y fintech XYZ/AFRM/Adyen ~1,7-2,7) x ERP 4,32% (Damodaran, 1-sep-2026) = Ke 10,5%. Kd 5,85% (rating A3/A-). D/(D+E) 22%."],
    ["Referencia: margen base ajustado (B6)", f"={VO}!B6", f"={VO}!B6", f"={VO}!B6",
     "Con I+D capitalizado a 3 años (Technology & development LTM US$3.247M): +US$229M de EBIT vs GAAP (17,4%)."],
    [],
    ["3. RESULTADO DEL DCF POR ESCENARIO"],
    ["Escenario", "Valor DCF / acción", "Precio Objetivo Ponderado*", "DCF vs. precio actual", "Ponderado vs. precio actual"],
    ["Conservador", f"={VO}!B86", f"={RES}!C12", f"=B26/{INP}!$B$23-1", f"=C26/{INP}!$B$23-1"],
    ["Base", f"={VO}!B35", f"={RES}!D12", f"=B27/{INP}!$B$23-1", f"=C27/{INP}!$B$23-1"],
    ["Optimista", f"={VO}!B137", f"={RES}!E12", f"=B28/{INP}!$B$23-1", f"=C28/{INP}!$B$23-1"],
    ["Precio actual (GOOGLEFINANCE)", f"={INP}!B23", "Precio al día del análisis", f"={RES}!C25"],
    [f'=IF(AND(B26<B27;B27<B28;C26<C27;C27<C28;{VO}!C55<{INP}!B27;{INP}!B27<{VO}!C106;{VO}!C45<{VO}!C46;{VO}!C46<{VO}!C47);"✔ Orden verificado: Conservador < Base < Optimista en crecimiento, margen objetivo, valor DCF y precio ponderado";"✖ REVISAR: el orden Conservador < Base < Optimista no se cumple")'],
    ["*El Precio Objetivo Ponderado combina el DCF (40%) con 5 múltiplos (EV/EBITDA 20%, P/E 20%, EV/FCFF 10%, P/FCFE 5%, P/OCF 5%) según la categoría 'Madura' de 'Resumen de Valoración'!G3. PYPL tiene utilidades, EBITDA y FCF positivos y estables los 10 años, así que P/E y EV/EBITDA son confiables y no hace falta cargar todo en el DCF. Los múltiplos Base son el MIN de los últimos 4 años (el de-rating 2022-2025), no la burbuja de 2021."],
    [],
    ["4. LOG DE CORRECCIONES ESTRUCTURALES Y AJUSTES (backup de cada fórmula en reference/backups/pypl_formula_backup.json del repo JMR-valuation)"],
    ["#", "Celda / componente", "Antes", "Después", "Razón"],
    [1, "Loader SEC: resultado antes de impuestos", "Tag '...BeforeIncomeTaxesDomestic' (solo doméstico, ~US$1.000M) -> tasa efectiva 2023-2025 de 117%/125%/73%", "Neto + impuesto (identidad) cuando falta el total: US$5.411M / 5.329M / 6.292M -> 21,5% / 22,2% / 16,8%", "PYPL dejó de taggear el total en 2023; el tag doméstico se usaba como si fuera el total."],
    [2, "Loader SEC: I+D (fila 10 del Income Statement)", "0 en 2019-2025; LTM 1.071 (dato de 2018)", "2.085 … 3.103; LTM 3.247", "PYPL reporta 'pypl:TechnologyAndDevelopmentExpense' (namespace propio, que companyfacts no expone). Se lee de las instancias XBRL de los 10-K/10-Q. Input!B17 = Yes capitaliza I+D."],
    [3, "Loader SEC: período LTM", "LTM al Q1 2026 (companyfacts sin el 10-Q del Q2, presentado el 28-jul)", "LTM al Q2 2026: ingresos 33.734 -> 34.128", "Lag de la API companyfacts; se complementa con la instancia XBRL del último 10-Q."],
    [4, "Loader SEC: deduplicación de trimestres", "Por fecha de cierre: el Q3 y el acumulado de 9M se pisaban y no se podía derivar el Q4", "Por período (inicio + cierre)", "El LTM de I+D/SG&A/D&A caía al último 10-K."],
    [5, "Balance Sheet, columna L (LTM)", "= FY2025 (deuda corriente 0, patrimonio 20.256)", "Balance real al 30-jun-2026: deuda 2.505 + 10.895 + arrendamientos 810; caja + inversiones de corto plazo 11.256; patrimonio 19.820", "refresh_balance_sheet usa el último 10-K como proxy de LTM."],
    [6, "Input sheet!B20 (activos no operativos)", "=L14+L15 -> 7.642", "=L14 -> 4.009", "L15 (otros activos de largo plazo: impuestos diferidos, derecho de uso) es operativo; inflaba el equity en ~US$4/acción."],
    [7, "Input sheet!B24 (tasa efectiva)", "='Income Statement'!I29 (Dec '23, 21,5%)", "='Income Statement'!L29 (LTM, 16,4%)", "La referencia estaba fija en una columna histórica."],
    [8, "Input sheet!B1", "(vacío)", "=A1", "Bug #6 del apéndice: no estaba aplicado en esta copia (TICKER vacío en Stories to Numbers y otras hojas)."],
    [9, "Valuation output!C55 (crecimiento Conservador)", "=PROMEDIO(B27;riskfree) -> 3,9% (MAYOR que el Base)", "=MIN(B27;B29)−1,5pp -> 2,0%", "Bug #10 del apéndice: no estaba aplicado. Con riskfree 4,96% por encima del crecimiento de PYPL, el 'conservador' crecía más."],
    [10, "Valuation output!C45 (margen Conservador)", "=B6 (18,1%)", "=Input!B28 (17,3%)", "El bear case real de PYPL es que la compresión de 2026 sea permanente, no que el margen se estanque en el nivel previo."],
    [11, "Valuation output!C47 (margen Optimista)", "=B30+5% fijo", "=B30+1.500/ingresos LTM (+4,4pp)", "Ancla en un dato real: el ahorro bruto anunciado."],
    [12, "Input sheet!B27-B33 (supuestos Base)", "B27=LTM 2,9% · B28=B6−2pp · B29=B27 · B30=MAX(ind.; B28; cuartiles de Sector)=36,6% · B31=5 · B32/33=0,09x (industria)", "4,0% · B6−0,8pp · 3,5% · 19,5% · 6 · 2,6x / 2,6x", "B30 tomaba cuartiles de margen contaminados por V/MA (60%+) y B32 la relación ventas/capital de prestamistas: sin sentido para PYPL."],
    [13, "Cost of capital worksheet", "Beta 'Single Business(Global)' 0,30 (industria de prestamistas/aseguradoras) · rating A1/A+ · rf 4,99% · ERP maduro 4,23% (ene-2026) · vencimiento 3 · WACC 6,11%", "Beta Direct Input 1,29 · A3/A- · rf 4,96% · ERP 4,09% (sep-2026; EE.UU. 4,32%) · vencimiento 6 · WACC 9,20%", "La industria de Damodaran de PYPL (Financial Svcs. Non-bank) está dominada por financieras apalancadas con betas bajas, que no representan a una plataforma de pagos."],
    [14, "Cost of capital worksheet!B24 / K65 / L65", "#DIV/0! (Direct Input caía a la tabla multibusiness vacía)", "B24 = beta desapalancada implícita (1,07); IFERROR en K65/L65", "Barrido de errores (paso 8)."],
    [15, "Option value!B18-B30", "#DIV/0! (sin opciones)", "IFERROR(…;0)", "Bug #5 del apéndice: no estaba aplicado en esta copia."],
    [16, "Financials Multiples!B36:E36, B75:E75, B115:E115", "#DIV/0! (crecimiento del dividendo sin año base)", "IFERROR(…;\"\")", "PYPL empezó a pagar dividendo a fines de 2025."],
    [17, "Resumen de Valoración!G3", "Genérico", "Madura", "Utilidades estables y positivas; empresa de crecimiento de un dígito medio."],
    [18, "Hojas de texto", "Contenido heredado (Adobe en Cualitativo, Amazon en Stories to Numbers, CAGRs de otra empresa como valores en Estadísticas)", "Contenido de PYPL; Estadísticas con fórmulas vivas", "Paso 3: no dejar el contenido de la empresa anterior."],
    [f'="Impacto total: DCF Base antes de los ajustes US$49,38 (Conservador −US$58,11, Optimista US$55,48, con WACC 6,11%) -> después US$"&TEXT({VO}!B35;"0.00")&" (Conservador US$"&TEXT({VO}!B86;"0.00")&", Optimista US$"&TEXT({VO}!B137;"0.00")&")."'],
    [],
    ["5. CONCLUSIÓN"],
    [f'="A US$"&TEXT({INP}!B23;"0.00")&", el modelo sugiere que el mercado descuenta un escenario PEOR que el Conservador (crecimiento de 2% y margen deprimido para siempre): el DCF Conservador da US$"&TEXT({VO}!B86;"0.00")&" ("&TEXT({VO}!B86/{INP}!B23-1;"+0%;-0%")&"), el Base US$"&TEXT({VO}!B35;"0.00")&" ("&TEXT({VO}!B35/{INP}!B23-1;"+0%;-0%")&") y el precio ponderado Base US$"&TEXT({RES}!D12;"0.00")&". El margen de seguridad es amplio, pero la historia necesita que la erosión del checkout de marca se frene. Es consistente con la oferta de US$60,50 que el directorio rechazó."'],
    ["Variable clave a monitorear: el crecimiento de los transaction margin dollars (TM$) frente al de los ingresos. Si los TM$ vuelven a crecer al ritmo de los ingresos (~4%), el margen converge al 19,5% del Base; si siguen en ~1% mientras los ingresos crecen 4-5%, la historia se mueve al Conservador (margen de ~17% permanente). Métrica secundaria: el crecimiento del checkout de marca (hoy +2% sin efecto cambiario)."],
    [],
    [SOURCES],
]
