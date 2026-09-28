"""Valoracion de EPAM Systems, Inc. (EPAM) -- posicion IBKR sin valoracion previa en Modelo JMR.
Motor: scripts/posiciones_ibkr.py. Hoja: Drive > Análisis > EPAM > Modelo JMR - EPAM
(copia nueva de la plantilla maestra auditada)."""
from __future__ import annotations

SHEET_ID = "1txQTjdUuzsnCem_4O1szofY7uAp5xLc3uda3l_iIcR0"
TICKER = "EPAM"
COMPANY = "EPAM Systems, Inc."
SHORT = "EPAM"
INDUSTRY = "Computer Services"
PEERS = ['ACN', 'CTSH', 'GLOB', 'IT']

CATEGORY = "Madura"
EMPLOYEES = 61000  # aproximado (10-K 2025); sin dato exacto verificado en esta hoja
DIVIDEND = False
MULT_ANCHOR = "LTM"  # accion de ~US$205 (dic-2025) a ~US$108: los cierres 2021-2025 (P/E 30-82x) ya no son el multiplo pagado

Q2 = "https://www.sec.gov/Archives/edgar/data/1352010/000135201026000046/epam-20260630.htm"
K10 = "https://www.sec.gov/Archives/edgar/data/1352010/000135201026000015/epam-20251231.htm"
SOURCES = (
    "Fuentes: estados financieros del modelo (SEC EDGAR, XBRL, CIK 0001352010: 10-K 2025 presentado el 26-feb-2026, "
    f"{K10}; 10-Q del 2T 2026 presentado el 06-ago-2026, {Q2}); ingresos trimestrales, segmento Europa, programa de "
    "recompra de US$1.000M (oct-2025) y exposición a Ucrania del mismo 10-Q; Damodaran Online (industria 'Computer "
    "Services'); UST 10 años y precio de EPAM vía yfinance (cierre del 25-sep-2026)."
)

BASE = dict(g1=0.05, m1=0.105, g25=0.05, mt=0.125, conv=5, s2c1=3.5, s2c2=3.0, tax=0.24, wacc_term=0.09)
SCEN = dict(g1_cons=0.01, g1_opt=0.09, mt_cons=0.095, mt_opt=0.15)
COC = {
    "B22": "Direct Input", "B23": 1.30,   # beta observado ~1,3 (servicios de TI, alta sensibilidad al ciclo de gasto tecnologico)
    "B26": "Country of Incorporation",
    # Sin deuda financiera material (US$25M + arrendamientos): la calificacion casi no pesa.
    "B33": 5, "B34": "Actual rating", "B36": "A2/A",
}

CUALI = dict(
    ceo="Balazs Fejes — CEO y Presidente desde septiembre de 2025 (sucedió al fundador Arkadiy Dobkin).",
    sector="Servicios de ingeniería de software y consultoría digital (Damodaran: Computer Services)",
    web="https://www.epam.com  |  IR: https://investors.epam.com",
    overview=("EPAM presta servicios de ingeniería de software, nube, datos e IA a grandes empresas, con centros de "
              "entrega en Europa Central y del Este, Asia y América Latina. Ingresos LTM de US$5.617M (2T 2026: "
              "US$1.415M, +4,5%), margen operativo GAAP de 10,0% y caja neta: sin deuda financiera material y "
              "US$789M de caja."),
    segments=[
        ("Norteamérica",
         "Aproximadamente la mitad de los ingresos: servicios de ingeniería para software, servicios financieros, "
         "salud y retail. Fue la región más afectada por el recorte de proyectos discrecionales desde 2023."),
        ("Europa",
         "US$622,5M en el 2T 2026 (+10,0% i.a.; US$1.227M en el 1S, +12,5%), con aporte de adquisiciones y "
         "moneda más fuerte."),
        ("Mercados de crecimiento y entrega",
         "Centros de entrega fuera de Rusia/Bielorrusia tras 2022; Ucrania sigue siendo una base relevante de "
         "profesionales (10-Q: activos operativos y compromiso humanitario de US$100M)."),
        ("Adquisiciones recientes",
         "Goodwill de US$1.182M-1.211M tras las compras de 2024-2025 (NEORIS en América Latina, First Derivative en "
         "servicios financieros), que explican parte del +15,4% de 2025."),
    ],
    bulls=[
        ("Ingeniería de alto valor y demanda de IA aplicada",
         "EPAM se posiciona como integrador de IA generativa y agentes para grandes empresas; los proyectos de "
         "modernización de datos y nube son prerrequisito para usar IA."),
        ("Balance sin deuda y recompras",
         "Caja neta y un programa de recompra de US$1.000M (oct-2025): US$715M recomprados LTM, reduciendo las "
         "acciones de 57M (2024) a 52M."),
        ("Valuación comprimida",
         "P/E LTM ~15x y EV/EBITDA ~7x, frente a 30-80x de utilidad en los cierres de 2019-2025."),
    ],
    bears=[
        ("Deflación de horas facturables por IA",
         "Si la IA generativa reduce las horas de programación necesarias por proyecto, el modelo de facturación por "
         "tiempo y materiales pierde volumen y precio."),
        ("Márgenes en baja",
         "Margen bruto de 36,5% (2016) a 29,4% LTM y margen operativo GAAP de 14,4% (2021) a 10,0%: presión de "
         "precios y costos de reubicación de talento."),
        ("Riesgo geopolítico y de ejecución",
         "Exposición a Ucrania y a Europa del Este, y un nuevo CEO tras la salida del fundador en 2025."),
    ],
)

STORY = dict(
    title="EPAM: ingeniería de software de primera línea frente a la deflación de horas por IA",
    text=("EPAM creció a más de 20% anual durante una década hasta 2022; desde entonces la salida de Rusia/Bielorrusia, "
          "el recorte de proyectos discrecionales y la llegada de la IA generativa bajaron su crecimiento a un dígito y "
          "su margen operativo GAAP a 10%. La acción cayó de US$668 (2021) a ~US$108. El caso Base asume crecimiento de "
          "5% y una leve recuperación del margen a 12,5%, con la IA como fuente de proyectos nuevos que compensa la "
          "menor intensidad de horas."),
    g="5% años 1-5: 1S 2026 +6% (con adquisiciones), 2T +4,5%.",
    m="Margen GAAP Año 1 10,5% (LTM 10,0%); objetivo 12,5% (sin volver al 14% de 2020-2021).",
    tax="Tasa marginal 24% (efectiva LTM 26,8%).",
    s2c="3,5x / 3,0x: servicios profesionales, poco capital fijo; el capital es talento y capital de trabajo.",
    roic="ROIC operativo alto (poco capital), menor con el goodwill de las compras recientes.",
    wacc="Beta 1,3 (Direct Input), ERP maduro; sin deuda financiera material.",
)

RECO = dict(
    g1="Ingresos 2T 2026 +4,5% i.a.; 1S +6,0% (US$2.815M).",
    m1="Margen operativo GAAP LTM 10,0%.",
    g25="5%: gasto en servicios de TI de un dígito medio, con la IA como fuente de proyectos y de deflación de horas.",
    mt="12,5%: recuperación parcial con utilización y precios estables; sin volver a 14%.",
    s2c1="3,5x: bajo capex (US$56M LTM).",
    s2c2="3,0x: más inversión en adquisiciones pequeñas y plataformas de IA.",
)

MULTIPLOS_EVALUACION = (
    "Evaluación EPAM: los cierres 2021-2025 dan P/E de 30-82x y EV/EBITDA de 15-59x, múltiplos de una empresa de "
    "crecimiento de 20%+. Con la acción en ~US$108 (P/E LTM ~15x, EV/EBITDA ~7x) se activó el override manual del "
    "bloque Base (columna J) = múltiplo LTM vivo: supone que el mercado sigue descontando el riesgo de la IA sobre "
    "el modelo de horas facturables."
)

TESIS = dict(
    historia=("EPAM fue durante una década el referente de la ingeniería de software tercerizada de alta calidad, con "
              "crecimiento de más de 20% anual y márgenes estables gracias a su base de talento en Europa del Este. La "
              "invasión de Ucrania (2022) la obligó a salir de Rusia y Bielorrusia y a reubicar miles de profesionales; "
              "después llegó el recorte de gasto discrecional en tecnología y, en 2025-2026, el temor a que la IA "
              "generativa reduzca las horas de programación que facturan las empresas de servicios. La acción cayó de "
              "US$668 a ~US$108. La tesis Base asume que EPAM crece 5% (la IA crea proyectos de datos y modernización "
              "que compensan la deflación de horas) con margen GAAP de 12,5%; el Conservador asume estancamiento (1%) "
              "y más compresión de margen."),
    bull_bear=[
        ("Ingeniería compleja y datos: la IA en grandes empresas requiere modernizar sistemas, un trabajo que EPAM sabe hacer.",
         "La IA generativa reduce horas de programación por proyecto: presión estructural sobre el modelo por tiempo y materiales."),
        ("Caja neta y recompras de US$715M LTM (acciones de 57M a 52M).",
         "Margen operativo GAAP de 10,0% LTM vs 14,4% en 2021."),
        ("P/E LTM ~15x: la acción descuenta un escenario de estancamiento.",
         "Exposición geopolítica a Ucrania y Europa del Este."),
        ("Europa +10% en el 2T 2026 con adquisiciones integradas.",
         "Cambio de CEO en 2025 tras la salida del fundador."),
    ],
    j_g1="Base 5%; Conservador 1% (la IA reduce volumen de horas); Optimista 9% (demanda de proyectos de IA).",
    j_g25="Base 5%: gasto global en servicios de TI de un dígito medio.",
    j_m1="Margen operativo GAAP LTM 10,0%.",
    j_mt="Base 12,5%; Conservador 9,5%; Optimista 15% (mejor utilización y mezcla de IA).",
    j_s2c="3,5x (1-5) / 3,0x (6-10): negocio de servicios, bajo capex.",
    j_wacc="Beta 1,3 (Direct Input), ERP maduro; caja neta de ~US$680M.",
    j_mbase="Margen operativo GAAP LTM (US$563M / US$5.617M).",
    nota_multiplos="Múltiplos anclados al LTM (override) tras la caída de 2025-2026.",
    conclusion=("La acción descuenta un crecimiento cercano a cero; el caso Base solo exige que EPAM crezca a un dígito "
                "medio sin más compresión de margen."),
    monitor=("Variables a monitorear: crecimiento orgánico en Norteamérica, facturación por proyectos de IA, "
             "utilización y precio por hora, margen operativo ajustado vs GAAP y ritmo de recompras."),
)
