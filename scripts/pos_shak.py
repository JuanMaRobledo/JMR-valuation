"""Valoracion de Shake Shack Inc. (SHAK) -- posicion IBKR sin valoracion previa en Modelo JMR.
Motor: scripts/posiciones_ibkr.py. Hoja: Drive > Análisis > SHAK > Modelo JMR - SHAK
(copia nueva de la plantilla maestra auditada)."""
from __future__ import annotations

SHEET_ID = "1RcwUptYoVjCfHvdqED5wXCsjteCds61g4HMKA_T8GCM"
TICKER = "SHAK"
COMPANY = "Shake Shack Inc."
SHORT = "Shake Shack"
INDUSTRY = "Restaurant/Dining"
PEERS = ['CMG', 'WING', 'CAVA', 'MCD']

CATEGORY = "Crecimiento"
EMPLOYEES = 12800  # aproximado (10-K 2025); sin dato exacto verificado en esta hoja
DIVIDEND = False

Q2 = "https://www.sec.gov/Archives/edgar/data/1620533/000162053326000034/shak-20260701.htm"
K10 = "https://www.sec.gov/Archives/edgar/data/1620533/000162053326000018/shak-20251231.htm"
SOURCES = (
    "Fuentes: estados financieros del modelo (SEC EDGAR, XBRL, CIK 0001620533: 10-K 2025 presentado el 26-feb-2026, "
    f"{K10}; 10-Q del 2T 2026 presentado el 05-ago-2026, {Q2}); ingresos, ventas same-Shack, aperturas, número de "
    "Shacks y notas convertibles del mismo 10-Q; Damodaran Online (industria 'Restaurant/Dining'); UST 10 años y "
    "precio de SHAK vía yfinance (cierre del 25-sep-2026)."
)

# Deuda financiera = notas convertibles 0% 2028 (US$250M; US$248M contable). Los arrendamientos
# (US$575M) NO se restan: el alquiler ya esta dentro del EBIT.
INPUT_EXTRA = {"B16": 248}
# Utilidad GAAP casi nula en 2021-2024 (P/E de -319x a 574x): ni la historia ni el LTM sirven de
# ancla. Base = multiplos de una cadena de fast-casual en crecimiento de doble digito, por debajo
# de CMG/CAVA y descontados por el margen operativo bajo.
MULT_OVERRIDE = {"PE": 35, "EVEBITDA": 15, "POCF": 12, "PFCFE": 30, "EVFCFF": 30}

# 'Financials Multiples' proyecta "Interest / Other" como % PROMEDIO del EBIT de 2023-2025; con
# EBIT casi nulo en 2023-2024 (US$5,9M y US$3,0M) ese promedio da 193% y la utilidad proyectada de
# los multiplos se infla (P/E daba US$1.000+/accion). Se usa solo el % de 2025 (16%: intereses
# sobre la caja), en los 3 escenarios.
SHEET_EXTRA = {"Financials Multiples": {"E11": "=D11", "E50": "=D50", "E90": "=D90"}}

BASE = dict(g1=0.13, m1=0.045, g25=0.11, mt=0.08, conv=5, s2c1=1.4, s2c2=1.6, tax=0.25, wacc_term=0.09)
SCEN = dict(g1_cons=0.09, g1_opt=0.16, mt_cons=0.06, mt_opt=0.10)
COC = {
    "B22": "Direct Input", "B23": 1.60,   # small cap volatil, beta observado ~1,6
    "B26": "Country of Incorporation",
    "B33": 2, "B34": "Actual rating", "B36": "Ba1/BB+",  # convertibles 0% sin calificacion publica verificada
}

CUALI = dict(
    ceo="Rob Lynch — CEO desde mayo de 2024 (antes CEO de Papa John's).",
    sector="Restaurantes 'fine casual' de hamburguesas (Damodaran: Restaurant/Dining)",
    web="https://www.shakeshack.com  |  IR: https://investor.shakeshack.com",
    overview=("Shake Shack opera hamburgueserías 'fine casual': al 1-jul-2026 tenía 703 Shacks, 406 propios y 297 "
              "licenciados (aeropuertos, estadios y socios internacionales). Ingresos LTM US$1.552M; en el 2T 2026 "
              "facturó US$417,6M (+17,2%) con ventas same-Shack +3,5% y 61 Shacks propios nuevos en 12 meses. El margen "
              "operativo GAAP es bajo (3,6% LTM) por preaperturas y gastos generales."),
    segments=[
        ("Shacks propios (Company-operated)",
         "~97% de los ingresos: US$757,5M de ventas en el 1S 2026 (+16,0%). El crecimiento viene de aperturas (61 "
         "nuevas en 12 meses, US$47,2M de aporte) y de ventas same-Shack (+3,5%)."),
        ("Licencias",
         "297 Shacks operados por licenciatarios en EE.UU. (aeropuertos, estadios, rutas) y en el exterior (Asia, "
         "Medio Oriente, Europa); Shake Shack cobra un % de sus ventas: US$25,7M en el 1S 2026, casi todo margen."),
        ("Canales digitales y drive-thru",
         "Pedidos por app/kiosco y formatos con drive-thru para acercarse a la conveniencia de la comida rápida "
         "tradicional."),
        ("Financiamiento",
         "Notas convertibles de US$250M al 0% con vencimiento el 1-mar-2028 y ~US$308M de caja; sin dividendos ni "
         "recompras."),
    ],
    bulls=[
        ("Crecimiento de unidades de doble dígito",
         "~15% de crecimiento anual de Shacks propios con una marca premium reconocida; los ingresos crecieron "
         "15-21% por año desde 2022."),
        ("Apalancamiento operativo en marcha",
         "Margen operativo GAAP de 0,2% (2024) a 4,3% (2025) bajo la nueva gerencia: más eficiencia laboral y menos "
         "gasto general por Shack."),
        ("Regalías de licencias con capital ajeno",
         "Casi 300 Shacks licenciados aportan ingresos de alto margen sin capex propio."),
    ],
    bears=[
        ("Rentabilidad todavía baja",
         "Margen operativo GAAP de 3,6% LTM y flujo de caja libre negativo LTM (capex de US$203M vs flujo operativo de "
         "US$192M): el crecimiento consume toda la caja."),
        ("Precio premium frente a un consumidor presionado",
         "Ticket alto frente a la comida rápida tradicional; una recesión golpearía el tráfico."),
        ("Escala y dilución potencial",
         "Empresa chica frente a los líderes; las convertibles 2028 pueden diluir o requerir refinanciamiento."),
    ],
)

STORY = dict(
    title="Shake Shack: marca premium con crecimiento de unidades de doble dígito que recién empieza a ganar margen",
    text=("Shake Shack crece 15-17% por año abriendo Shacks propios y licenciados, pero durante años su margen operativo "
          "GAAP fue casi nulo. Desde 2024 la nueva gerencia lo llevó a 4,3% (2025). El caso Base asume crecimiento de 13% "
          "el Año 1 y 11% en los años 2-5 (aperturas + same-Shack de un dígito bajo) y que el margen operativo GAAP "
          "converge a 8% a medida que el gasto general se diluye y maduran los Shacks nuevos."),
    g="Año 1 13% (2T 2026 +17,2%), años 2-5 11%: aperturas de ~12-14% anual + same-Shack de un dígito bajo.",
    m="Margen GAAP Año 1 4,5% (LTM 3,6%; 2025 4,3%); objetivo 8% por dilución de gastos generales y preaperturas.",
    tax="Tasa marginal 25% (federal + estatal).",
    s2c="1,4x / 1,6x: cada Shack nuevo requiere capex propio (US$203M LTM); el alquiler va como gasto operativo.",
    roic="ROIC bajo hoy (margen chico), creciente si el margen converge.",
    wacc="Beta 1,6 (Direct Input), ERP maduro, convertibles como deuda (Ba1/BB+).",
)

RECO = dict(
    g1="2T 2026: ingresos +17,2%; same-Shack +3,5%; 61 aperturas propias en 12 meses.",
    m1="Margen operativo GAAP LTM 3,6%; 2025 4,3%.",
    g25="11%: aperturas de doble dígito bajo sobre una base más grande.",
    mt="8%: margen a nivel Shack ~20% menos gastos generales, preaperturas y D&A.",
    s2c1="1,4x: capex de construcción de Shacks nuevos.",
    s2c2="1,6x: mayor peso de licencias (sin capex propio).",
)

MULTIPLOS_EVALUACION = (
    "Evaluación SHAK: la utilidad GAAP fue negativa o casi nula entre 2020 y 2024, así que los múltiplos históricos "
    "(P/E de -319x a 574x, EV/FCFF > 200x) no tienen sentido como ancla; el mecanismo nativo daba precios de US$750-"
    "1.900 por acción. Se activó un override manual en el bloque Base (columna J): P/E 35x, EV/EBITDA 15x, P/OCF 12x, "
    "P/FCFE 30x, EV/FCFF 30x (múltiplos de una cadena de fast-casual en crecimiento de doble dígito, por debajo de "
    "CMG y descontados por el margen todavía bajo). Además, en 'Financials Multiples' el % de 'Interest / Other' "
    "sobre EBIT usa solo 2025 (16%) en vez del promedio 2023-2025 (193%, distorsionado por EBIT casi nulo)."
)

TESIS = dict(
    historia=("Shake Shack nació como un carrito de hamburguesas en Madison Square Park y se convirtió en una marca "
              "premium global con 703 locales. Su problema histórico fue la rentabilidad: crecía rápido pero el margen "
              "operativo GAAP rondaba cero por costos laborales, preaperturas y una estructura corporativa pensada para "
              "una empresa más grande. Desde la llegada de Rob Lynch (2024) el margen mejoró a 4,3% en 2025 y el "
              "crecimiento sigue en 15-17%. La tesis Base asume que esa mejora continúa hasta 8% de margen operativo con "
              "crecimiento de 11-13%; el Conservador asume que el consumidor presionado frena las ventas same-Shack y el "
              "margen se estanca en 6%."),
    bull_bear=[
        ("Crecimiento de unidades de doble dígito con una marca premium (703 Shacks).",
         "Margen operativo GAAP de solo 3,6% LTM y flujo de caja libre negativo."),
        ("Mejora de margen bajo la nueva gerencia (0,2% en 2024 a 4,3% en 2025).",
         "Ticket premium expuesto a un consumidor más cauto."),
        ("297 Shacks licenciados que aportan regalías de alto margen sin capital propio.",
         "Convertibles de US$250M con vencimiento en 2028."),
        ("Formatos con drive-thru y canal digital amplían la ocasión de consumo.",
         "Competencia intensa en hamburguesas (Five Guys, In-N-Out, comida rápida con ofertas de valor)."),
    ],
    j_g1="Base 13%; Conservador 9% (menos aperturas, same-Shack plano); Optimista 16% (ritmo actual).",
    j_g25="Base 11%: crecimiento de unidades de doble dígito bajo sobre una base mayor.",
    j_m1="Margen operativo GAAP LTM 3,6% (2025: 4,3%); Año 1 4,5%.",
    j_mt="Base 8%; Conservador 6%; Optimista 10% (margen de cadenas maduras de fast-casual).",
    j_s2c="1,4x (1-5) / 1,6x (6-10): capex de Shacks propios; más licencias a futuro.",
    j_wacc="Beta 1,6 (Direct Input), ERP maduro, deuda = convertibles de US$248M (el alquiler ya está en el EBIT).",
    j_mbase="Margen operativo GAAP LTM (US$55M / US$1.552M).",
    nota_multiplos="Múltiplos Base fijados a mano (override) porque la utilidad GAAP histórica fue casi nula.",
    conclusion=("Casi todo el valor está en que el margen operativo converja a niveles de una cadena madura; con margen "
                "estancado, el crecimiento no crea valor."),
    monitor=("Variables a monitorear: ventas same-Shack y tráfico, margen a nivel Shack, gastos generales como % de "
             "ventas, ritmo de aperturas y refinanciamiento de las convertibles 2028."),
)
