"""Valoracion de Domino's Pizza, Inc. (DPZ) -- posicion IBKR sin valoracion previa en Modelo JMR.
Motor: scripts/posiciones_ibkr.py. Hoja: Drive > Análisis > DPZ > Modelo JMR - DPZ
(copia nueva de la plantilla maestra auditada)."""
from __future__ import annotations

SHEET_ID = "1voP-krWxuq4RtJDX4WYP6FEG_rRoqjMjgVXF5vPywSo"
TICKER = "DPZ"
COMPANY = "Domino's Pizza, Inc."
SHORT = "Domino's"
INDUSTRY = "Restaurant/Dining"
PEERS = ['MCD', 'YUM', 'PZZA', 'QSR']
# Deuda: el loader toma 'LongTermDebt' (US$15M, un tramo residual) en 2024-2025; la deuda
# titulizada esta en 'LongTermDebtAndCapitalLeaseObligations' (+ su porcion corriente).
DEBT_TAGS = {"long_term_debt": "LongTermDebtAndCapitalLeaseObligations",
             "current_debt": "LongTermDebtAndCapitalLeaseObligationsCurrent"}
DEBT_LTM = 4810.683 + 6.131  # US$M al 28-dic-2025 (10-K 2025; la columna LTM del modelo = ejercicio 2025)

CATEGORY = "Madura"
EMPLOYEES = 6500  # aproximado, empleados corporativos, de cadena de suministro y tiendas propias (10-K); sin dato exacto verificado
DIVIDEND = True
MULT_ANCHOR = "LTM"  # la accion cayo de ~US$426 (dic-2025) a ~US$292; los cierres 2021-2025 (P/E 24-42x) ya no son el multiplo pagado

Q2 = "https://www.sec.gov/Archives/edgar/data/1286681/000128668126000035/dpz-20260614.htm"
K10 = "https://www.sec.gov/Archives/edgar/data/1286681/000119312526062321/dpz-20251228.htm"
SOURCES = (
    "Fuentes: estados financieros del modelo (SEC EDGAR, XBRL, CIK 0001286681: 10-K 2025 presentado el 23-feb-2026, "
    f"{K10}; 10-Q del 2T 2026 presentado el 20-jul-2026, {Q2}); ventas globales, ventas mismas tiendas, deuda "
    "titulizada, recompras y dividendo del mismo 10-Q. La columna LTM del modelo corresponde al ejercicio 2025 (el "
    "1S 2026 sumó +3,9% de ingresos). Damodaran Online (industria 'Restaurant/Dining'); UST 10 años y precio de DPZ "
    "vía yfinance (cierre del 25-sep-2026)."
)

# Arrendamientos (~US$240M) como gasto operativo, no como deuda.
INPUT_EXTRA = {"B16": 4816.8}

BASE = dict(g1=0.04, m1=0.19, g25=0.045, mt=0.20, conv=5, s2c1=3.0, s2c2=3.0, tax=0.23, wacc_term=0.09)
SCEN = dict(g1_cons=0.02, g1_opt=0.065, mt_cons=0.18, mt_opt=0.22)
COC = {
    "B22": "Direct Input", "B23": 0.90,   # beta observado ~0,9
    "B26": "Country of Incorporation",
    # Notas titulizadas (whole business securitization) con calificacion grado de inversion baja.
    "B33": 5, "B34": "Actual rating", "B36": "Baa2/BBB",
}

CUALI = dict(
    ceo="Russell Weiner — CEO desde mayo de 2022 (antes COO y presidente de Domino's USA).",
    sector="Franquiciador global de pizza a domicilio y para llevar (Damodaran: Restaurant/Dining)",
    web="https://www.dominos.com  |  IR: https://ir.dominos.com",
    overview=("Domino's es la mayor cadena de pizza del mundo por ventas: casi todas sus tiendas son de franquiciados, "
              "que le pagan regalías y le compran insumos a su cadena de suministro (supply chain) en EE.UU. Ingresos "
              "2025 de US$4.940M (+5,0%), margen operativo de 19,3% y flujo de caja libre de US$672M; opera con "
              "patrimonio negativo por su deuda titulizada (~US$4.900M) usada para recompras y dividendos."),
    segments=[
        ("Cadena de suministro en EE.UU.",
         "La mayor línea de ingresos (US$1.258M de costo de supply chain solo en el 1S 2026): vende masa, queso e "
         "insumos a las tiendas franquiciadas con un margen bajo pero estable."),
        ("Regalías y tarifas de franquicia (EE.UU. e internacional)",
         "Regalías sobre las ventas de ~21.000 tiendas en más de 90 mercados; es la parte de mayor margen del "
         "negocio y la que sostiene el valor."),
        ("Tiendas propias en EE.UU. y fondo de publicidad",
         "Una fracción pequeña de tiendas propias y el fondo de publicidad de los franquiciados (se registra como "
         "ingreso y gasto por igual, sin margen)."),
        ("Desempeño reciente",
         "2T 2026: ventas minoristas globales +3,0% sin efecto cambiario; ventas mismas tiendas +0,1% en EE.UU. y "
         "-0,1% internacional (10-Q)."),
    ],
    bulls=[
        ("Escala en delivery y cadena de suministro propia",
         "La densidad de tiendas y la logística propia le dan el menor costo por entrega del sector y protegen el "
         "margen de los franquiciados."),
        ("Modelo liviano en capital y alto retorno al accionista",
         "Capex de US$121M sobre US$4.940M de ingresos; en 2025 destinó US$358M a recompras y US$237M a dividendos "
         "(dividendo trimestral de US$1,99 por acción declarado en abr-2026)."),
        ("Crecimiento de tiendas internacional",
         "Los máster franquiciados siguen abriendo tiendas fuera de EE.UU., lo que agrega regalías sin capital propio."),
    ],
    bears=[
        ("Ventas mismas tiendas estancadas",
         "+0,1% en EE.UU. y -0,1% internacional en el 2T 2026: la competencia de agregadores (DoorDash, Uber Eats) y "
         "la debilidad del consumidor limitan el crecimiento orgánico."),
        ("Apalancamiento alto",
         "~US$4.900M de deuda titulizada con patrimonio negativo de US$3.982M; un refinanciamiento a tasas más altas "
         "presionaría el flujo disponible para recompras."),
        ("Dependencia de la salud de los franquiciados",
         "Salarios y costos de insumos comprimen la rentabilidad de las tiendas; si caen las aperturas, cae el motor "
         "de crecimiento de regalías."),
    ],
)

STORY = dict(
    title="Domino's: una máquina de regalías de bajo crecimiento, apalancada y re-valuada",
    text=("Domino's genera ~US$670M de flujo de caja libre sobre US$4.940M de ingresos con un modelo de franquicias y "
          "cadena de suministro propia, pero sus ventas mismas tiendas están estancadas (+0,1% en EE.UU. en el 2T 2026) "
          "y la acción cayó de ~US$426 a ~US$292. El caso Base asume crecimiento de 4-4,5% (tiendas nuevas, sobre todo "
          "internacionales) y un margen estable de ~20%."),
    g="Año 1 4%, años 2-5 4,5%: ventas globales +3% sin FX en el 2T 2026 más aperturas internacionales.",
    m="Margen operativo Año 1 19% (2025: 19,3%); objetivo 20%.",
    tax="Tasa marginal 23% (efectiva 2025: 21,9%).",
    s2c="3,0x: franquiciador liviano en capital; el crecimiento lo financian los franquiciados.",
    roic="ROIC muy alto (capital invertido bajo, patrimonio negativo por recompras con deuda).",
    wacc="Beta 0,9 (Direct Input), ERP maduro, deuda titulizada Baa2/BBB a 5 años.",
)

RECO = dict(
    g1="Ventas minoristas globales +3,0% sin FX (2T 2026); ingresos 1S 2026 +3,9%.",
    m1="Margen operativo 2025: 19,3%.",
    g25="4,5%: crecimiento de tiendas internacional y ventas mismas tiendas de un dígito bajo.",
    mt="20%: leve mejora por mezcla hacia regalías internacionales.",
    s2c1="3,0x: bajo capex (US$121M en 2025).",
    s2c2="3,0x: mismo modelo de franquicias.",
)

MULTIPLOS_EVALUACION = (
    "Evaluación DPZ: corrección previa de la deuda (el XBRL tomó un tramo residual de US$15M en 2024-2025; se usa "
    "'LongTermDebtAndCapitalLeaseObligations', ~US$4.800M) para que los múltiplos EV sean correctos. Los cierres "
    "2021-2025 dan P/E de 24-42x; con la acción en ~US$292 el P/E LTM es ~17x. Se activó el override manual del "
    "bloque Base (columna J) = múltiplo LTM vivo: supone que no vuelve la prima de 2021-2025 mientras las ventas "
    "mismas tiendas sigan planas."
)

TESIS = dict(
    historia=("Domino's construyó su ventaja en la logística: tiendas densas, entrega propia y una cadena de "
              "suministro que abastece a los franquiciados de EE.UU. y Canadá. Ese modelo generó durante una década "
              "crecimiento de ventas mismas tiendas y recompras financiadas con deuda titulizada, y el mercado le pagó "
              "25-40x utilidad. Hoy el crecimiento orgánico está estancado (ventas mismas tiendas ~0% en el 2T 2026) por "
              "la competencia de los agregadores de delivery y un consumidor más cauto, y la acción cayó ~31% en 2026. "
              "La tesis Base asume que Domino's sigue creciendo 4-4,5% por aperturas internacionales con margen estable, "
              "y que el retorno al accionista viene de dividendos y recompras más que de crecimiento."),
    bull_bear=[
        ("Costo por entrega más bajo del sector gracias a densidad de tiendas y logística propia.",
         "Ventas mismas tiendas planas en EE.UU. e internacional en el 2T 2026."),
        ("Flujo de caja libre de US$672M (2025) y bajo capex: dividendos crecientes y recompras.",
         "Deuda titulizada de ~US$4.900M y patrimonio negativo: sensibilidad a tasas de refinanciamiento."),
        ("Crecimiento de tiendas internacionales sin capital propio (máster franquiciados).",
         "Agregadores (DoorDash, Uber Eats) le quitan la ventaja exclusiva de delivery."),
        ("P/E LTM ~17x, el más bajo de 10 años.",
         "Rentabilidad de franquiciados presionada por salarios y costos de insumos."),
    ],
    j_g1="Base 4%; Conservador 2% (ventas mismas tiendas negativas); Optimista 6,5% (recuperación de ventas mismas tiendas a +3%).",
    j_g25="Base 4,5%: aperturas netas internacionales y EE.UU. de un dígito bajo.",
    j_m1="Margen operativo 2025: 19,3%.",
    j_mt="Base 20%; Conservador 18%; Optimista 22% (mayor mezcla de regalías).",
    j_s2c="3,0x: franquiciador, bajo capex.",
    j_wacc="Beta 0,9 (Direct Input), ERP maduro, deuda Baa2/BBB a 5 años (US$4.817M al cierre 2025).",
    j_mbase="Margen operativo GAAP 2025 (US$954M / US$4.940M).",
    nota_multiplos="Múltiplos anclados al LTM (override) tras la caída de 2026; deuda corregida antes de calcularlos.",
    conclusion=("Con crecimiento bajo, el valor depende del margen y del costo de la deuda; la acción ya no incorpora "
                "prima de crecimiento."),
    monitor=("Variables a monitorear: ventas mismas tiendas en EE.UU., aperturas netas internacionales, margen de la "
             "cadena de suministro, costo de refinanciamiento de las notas titulizadas y ritmo de recompras."),
)
