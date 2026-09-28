"""Valoracion de Celsius Holdings, Inc. (CELH) -- posicion IBKR sin valoracion previa en Modelo JMR.
Motor: scripts/posiciones_ibkr.py. Hoja: Drive > Análisis > CELH > Modelo JMR - CELH
(copia nueva de la plantilla maestra auditada)."""
from __future__ import annotations

SHEET_ID = "1pl_6BeI9gl_ciaSY5wDqyjRF9GS-ZhjXXK4wGVuBC4o"
TICKER = "CELH"
COMPANY = "Celsius Holdings, Inc."
SHORT = "Celsius"
INDUSTRY = "Beverage (Soft)"
PEERS = ['MNST', 'KDP', 'PEP', 'KO']

CATEGORY = "Crecimiento"
EMPLOYEES = 1300  # aproximado (10-K 2025 + integracion de Alani Nu y Rockstar); sin dato exacto verificado en esta hoja
DIVIDEND = False

Q2 = "https://www.sec.gov/Archives/edgar/data/1341766/000134176626000050/celh-20260630.htm"
K10 = "https://www.sec.gov/Archives/edgar/data/1341766/000134176626000024/celh-20251231.htm"
SOURCES = (
    "Fuentes: estados financieros del modelo (SEC EDGAR, XBRL, CIK 0001341766: 10-K 2025 presentado el 02-mar-2026, "
    f"{K10}; 10-Q del 2T 2026 presentado el 06-ago-2026, {Q2}); ingresos por marca, cargos por terminación de "
    "distribuidores, acciones preferentes convertibles de PepsiCo y acciones potencialmente dilutivas (~33,4 millones) "
    "del mismo 10-Q; Damodaran Online (industria 'Beverage (Soft)'); UST 10 años y precio de CELH vía yfinance "
    "(cierre del 25-sep-2026)."
)

# Acciones: 253,1M comunes + ~33,4M potencialmente dilutivas (preferentes Serie A y B de
# PepsiCo convertibles, en el dinero, y PSU) segun el 10-Q del 2T 2026 -> base "como convertida".
INPUT_EXTRA = {"B22": 286.5}

BASE = dict(g1=0.07, m1=0.12, g25=0.06, mt=0.17, conv=5, s2c1=2.5, s2c2=2.0, tax=0.24, wacc_term=0.09)
SCEN = dict(g1_cons=0.02, g1_opt=0.12, mt_cons=0.11, mt_opt=0.21)
COC = {
    # Beta observado alto (acción muy volatil, ~1,5); la canasta 'Beverage (Soft)' (0,54
    # desapalancada) corresponde a embotelladoras maduras, no a una marca en construccion.
    "B22": "Direct Input", "B23": 1.50,
    "B26": "Country of Incorporation",
    # Prestamo a plazo de ~US$680M (compra de Alani Nu) sin calificacion publica verificada: BB.
    "B33": 5, "B34": "Actual rating", "B36": "Ba2/BB",
}
# Utilidad GAAP deprimida por cargos de terminacion de distribuidores (US$85M en el 1S 2026)
# y amortizacion de intangibles: los multiplos historicos (P/E 43-109x) y el LTM (55x) no sirven
# de ancla. Base = multiplos de un fabricante de bebidas energeticas en crecimiento moderado
# (referencia: Monster ~30x P/E; Keurig Dr Pepper ~15x), descontados por concentracion en PepsiCo.
MULT_OVERRIDE = {"PE": 25, "EVEBITDA": 16, "POCF": 18, "PFCFE": 20, "EVFCFF": 20}

CUALI = dict(
    ceo="John Fieldly — Presidente y CEO desde 2018 (CFO desde 2012).",
    sector="Bebidas energéticas funcionales (Damodaran: Beverage (Soft))",
    web="https://www.celsiusholdingsinc.com  |  IR: https://ir.celsiusholdingsinc.com",
    overview=("Celsius vende bebidas energéticas 'funcionales' bajo tres marcas: Celsius, Alani Nu (comprada el "
              "1-abr-2025) y Rockstar (derechos de EE.UU. y Canadá comprados a PepsiCo el 28-ago-2025). Terceriza la "
              "fabricación y distribuye principalmente a través del sistema de PepsiCo, que además es accionista con "
              "preferentes convertibles. Ingresos LTM de US$3.047M; en el 2T 2026 facturó US$818M (+10,6%)."),
    segments=[
        ("Marca Celsius",
         "US$387M en el 2T 2026 (-11,7% i.a.): más promociones como % de ingresos, ajuste de inventarios del "
         "distribuidor, debilidad en el canal club y menos lanzamientos. Es la marca original y la que más pierde "
         "impulso."),
        ("Alani Nu",
         "US$364M en el 2T 2026 (+21,0%): demanda fuerte, innovación y más distribución; orientada a consumidoras "
         "jóvenes. Ya es casi la mitad de los ingresos."),
        ("Rockstar",
         "US$66,5M en el 2T 2026 (sin comparable): marca madura comprada a PepsiCo, con menor margen; aporta escala en "
         "tiendas de conveniencia."),
        ("Distribución con PepsiCo",
         "PepsiCo distribuye las tres marcas en EE.UU. y Canadá; la transición de territorios de Alani Nu generó cargos "
         "por terminación de distribuidores (US$85M en el 1S 2026) que deprimen el margen GAAP."),
    ],
    bulls=[
        ("Portafolio multimarca en la categoría de mayor crecimiento de bebidas",
         "Con Celsius, Alani Nu y Rockstar la compañía es el tercer jugador de bebidas energéticas en EE.UU. y cubre "
         "segmentos distintos (fitness, consumidora joven, tradicional)."),
        ("Modelo liviano en capital",
         "Fabricación tercerizada: capex de US$46M LTM sobre US$3.047M de ingresos y flujo operativo de US$509M LTM."),
        ("Alineación con PepsiCo",
         "PepsiCo es socio de distribución y accionista (preferentes Serie A y B y dos asientos en el Directorio), lo "
         "que da acceso a la red de distribución más grande de EE.UU."),
    ],
    bears=[
        ("Desaceleración de la marca Celsius",
         "La marca original cayó 11,7% en el 2T 2026; el crecimiento consolidado depende de Alani Nu y de las compras."),
        ("Dependencia y dilución vinculadas a PepsiCo",
         "Concentración de la distribución en un solo socio y ~33,4 millones de acciones potencialmente dilutivas "
         "(preferentes convertibles y PSU) sobre ~253 millones de acciones comunes."),
        ("Competencia y promociones",
         "Monster, Red Bull y nuevas marcas compiten por espacio en góndola; más inversión promocional bajó el margen "
         "bruto de 51,5% a 48,1% en el 2T 2026."),
    ],
)

STORY = dict(
    title="Celsius: de marca de hipercrecimiento a plataforma multimarca de bebidas energéticas dependiente de PepsiCo",
    text=("Celsius pasó de US$1.356M de ingresos en 2024 a US$3.047M LTM gracias a las compras de Alani Nu y Rockstar, "
          "pero la marca Celsius cae (-11,7% en el 2T 2026) y el margen operativo GAAP es de apenas 5,3% LTM por "
          "cargos de transición de distribuidores y amortización. El caso Base asume crecimiento de 7% el Año 1 y 6% "
          "después (Alani Nu compensa a Celsius) y que, sin cargos no recurrentes, el margen converge a 17%, por debajo "
          "del ~20% que la empresa tuvo en 2023 como marca única."),
    g="Año 1 7%, años 2-5 6%: Alani Nu +21% compensa la caída de la marca Celsius; Rockstar aporta escala sin crecimiento.",
    m="Margen GAAP Año 1 12% (LTM 5,3% con cargos por terminación de distribuidores); objetivo 17%.",
    tax="Tasa marginal 24%: federal 21% + estatal.",
    s2c="2,5x / 2,0x: fabricación tercerizada; el capital invertido contable incluye goodwill e intangibles de las compras.",
    roic="ROIC operativo alto en el negocio de marcas; bajo sobre el capital total por las compras de 2025.",
    wacc="Beta 1,5 (Direct Input), ERP maduro, deuda BB a 5 años.",
)

RECO = dict(
    g1="Q2 2026: +10,6% reportado; sin Rockstar ~+1,7%. Año 1 7% supone que Alani Nu sigue creciendo y Celsius se estabiliza.",
    m1="12%: LTM 5,3% incluye US$85M de cargos por terminación de distribuidores en el 1S 2026 y amortización de intangibles.",
    g25="6%: categoría de energéticas creciendo a un dígito alto; Celsius pierde participación, Alani Nu gana.",
    mt="17%: margen bruto ~48% menos marketing y distribución; por debajo del ~20% de 2023 por mezcla (Rockstar) y promociones.",
    s2c1="2,5x: modelo de co-empacadores, bajo capex.",
    s2c2="2,0x: más capital de trabajo y marketing de marca a escala.",
)

MULTIPLOS_EVALUACION = (
    "Evaluación CELH: la utilidad GAAP está deprimida por cargos no recurrentes (terminación de distribuidores, "
    "amortización de intangibles de Alani Nu y Rockstar), así que los múltiplos históricos (P/E 43-109x en 2023-2025) "
    "y el LTM (P/E ~55x, EV/EBITDA ~36x) sobreestiman el múltiplo 'normal'. Se activó un override manual en el bloque "
    "Base (columna J): P/E 25x, EV/EBITDA 16x, P/OCF 18x, P/FCFE 20x, EV/FCFF 20x (entre Keurig Dr Pepper ~15x y "
    "Monster ~30x de P/E, descontado por la concentración en PepsiCo y la caída de la marca Celsius). OJO: las hojas de "
    "múltiplos dividen por las acciones comunes (~253M), no por la base como convertida (~286,5M) que usa el DCF; "
    "sus precios por acción quedan ~13% por encima del equivalente totalmente diluido."
)

TESIS = dict(
    historia=("Celsius fue la historia de hipercrecimiento de las bebidas energéticas entre 2021 y 2023, apoyada en su "
              "acuerdo de distribución con PepsiCo. En 2024 el crecimiento se frenó (+2,9%) y la compañía respondió con "
              "compras: Alani Nu (abr-2025) y los derechos de Rockstar en EE.UU. y Canadá (ago-2025), a cambio de más "
              "deuda (~US$680M) y más preferentes convertibles en manos de PepsiCo. Hoy es una plataforma de tres marcas "
              "con US$3.047M de ingresos LTM, en la que Alani Nu crece (+21%) y la marca Celsius se contrae (-11,7%). La "
              "tesis Base asume que el conjunto crece a un dígito medio-alto y que, una vez absorbidos los cargos de "
              "transición de distribución, el margen operativo converge a 17%; el Conservador asume que la erosión de "
              "Celsius se contagia y el crecimiento se estanca en 2%."),
    bull_bear=[
        ("Tres marcas en la categoría de bebidas de mayor crecimiento; Alani Nu +21% en el 2T 2026.",
         "La marca Celsius cayó 11,7% en el 2T 2026 por promociones, inventarios y canal club."),
        ("Distribución a través de PepsiCo, la red más grande de EE.UU.",
         "Dependencia de un solo distribuidor que además es accionista con preferentes convertibles."),
        ("Modelo de co-empacadores: capex de 1,5% de ventas y flujo operativo de US$509M LTM.",
         "Margen bruto en baja (48,1% vs 51,5%) por promociones y mezcla con Rockstar."),
        ("Cargos de transición no recurrentes: el margen GAAP de 5% subestima la rentabilidad normal.",
         "~33,4M de acciones potencialmente dilutivas (13% de la base) y deuda de ~US$680M."),
    ],
    j_g1="Base 7%; Conservador 2% (Celsius sigue cayendo); Optimista 12% (Alani Nu y distribución internacional).",
    j_g25="Base 6%: categoría energética a un dígito alto con pérdida de participación de la marca Celsius.",
    j_m1="LTM 5,3% con cargos no recurrentes; Año 1 12% sin la mayor parte de esos cargos.",
    j_mt="Base 17%; Conservador 11% (promociones persistentes); Optimista 21% (vuelta al margen de 2023).",
    j_s2c="2,5x (1-5) / 2,0x (6-10): fabricación tercerizada.",
    j_wacc="Beta 1,5 (Direct Input), ERP maduro, deuda Ba2/BB a 5 años.",
    j_mbase="Margen operativo GAAP LTM (US$160M / US$3.047M), deprimido por cargos de distribución.",
    nota_multiplos=("Múltiplos Base fijados a mano (override) por la distorsión de la utilidad GAAP; ver 'Supuestos "
                    "de los Múltiplos'. El DCF usa 286,5M de acciones (base como convertida)."),
    conclusion=("La valoración depende casi por completo de que el margen se normalice tras la transición de "
                "distribución y de que Alani Nu compense a la marca Celsius."),
    monitor=("Variables a monitorear: ingresos de la marca Celsius vs. Alani Nu, promociones como % de ingresos y margen "
             "bruto, fin de los cargos por terminación de distribuidores, conversión o recompra de las preferentes de "
             "PepsiCo."),
)
