"""Valoracion de Zoetis Inc. (ZTS) -- posicion IBKR sin valoracion previa en Modelo JMR.
Motor: scripts/posiciones_ibkr.py. Hoja: Drive > Análisis > ZTS > Modelo JMR - ZTS
(copia nueva de la plantilla maestra auditada)."""
from __future__ import annotations

SHEET_ID = "1MYnJJfv2G9R5u4roWPYb855tFs3K0Mqt2vxCPNkXKPE"
TICKER = "ZTS"
COMPANY = "Zoetis Inc."
SHORT = "Zoetis"
INDUSTRY = "Drugs (Pharmaceutical)"
PEERS = ['ELAN', 'IDXX', 'MRK', 'PAHC']
# Zoetis no reporta 'OperatingIncomeLoss' en XBRL (EBIT quedaba en 0): EBIT = utilidad antes de
# impuestos + gasto por intereses. Dividendos en 'PaymentsOfOrdinaryDividends' (el loader busca
# 'PaymentsOfDividendsCommonStock' / 'PaymentsOfDividends').
EBIT_FROM_PRETAX = True
DEBT_TAGS = {"dividends_paid": "PaymentsOfOrdinaryDividends"}

CATEGORY = "Madura"
EMPLOYEES = 13800  # aproximado (10-K 2025); sin dato exacto verificado en esta hoja
DIVIDEND = True
MULT_ANCHOR = "LTM"  # accion de ~US$244 (2021) y ~US$126 (dic-2025) a ~US$71: los cierres historicos (P/E 21-57x) ya no son el multiplo pagado

Q2 = "https://www.sec.gov/Archives/edgar/data/1555280/000155528026000040/zts-20260630.htm"
K10 = "https://www.sec.gov/Archives/edgar/data/1555280/000155528026000011/zts-20251231.htm"
SOURCES = (
    "Fuentes: estados financieros del modelo (SEC EDGAR, XBRL, CIK 0001555280: 10-K 2025 presentado el 12-feb-2026, "
    f"{K10}; 10-Q del 2T 2026 presentado el 06-ago-2026, {Q2}); ingresos por segmento y especie, competencia en "
    "dermatología y parasiticidas, genéricos de Cerenia y Convenia y demanda colectiva del mismo 10-Q. EBIT "
    "reconstruido como utilidad antes de impuestos + intereses (Zoetis no reporta 'Operating income' en XBRL). "
    "Damodaran Online (industria 'Drugs (Pharmaceutical)'); UST 10 años y precio de ZTS vía yfinance (cierre del "
    "25-sep-2026)."
)

BASE = dict(g1=0.02, m1=0.36, g25=0.05, mt=0.36, conv=5, s2c1=2.0, s2c2=2.0, tax=0.20, wacc_term=0.09)
SCEN = dict(g1_cons=-0.01, g1_opt=0.06, mt_cons=0.33, mt_opt=0.38)
COC = {
    "B22": "Direct Input", "B23": 0.90,   # beta observado ~0,9
    "B26": "Country of Incorporation",
    "B33": 8, "B34": "Actual rating", "B36": "Baa2/BBB",  # calificacion real Baa1/BBB (Moody's/S&P); el cuadro no tiene Baa1
}

CUALI = dict(
    ceo="Kristin Peck — CEO desde enero de 2020.",
    sector="Salud animal: medicamentos, vacunas y diagnósticos veterinarios (Damodaran: Drugs (Pharmaceutical))",
    web="https://www.zoetis.com  |  IR: https://investor.zoetis.com",
    overview=("Zoetis es la mayor compañía de salud animal del mundo: vende medicamentos, vacunas y diagnósticos para "
              "mascotas (perros y gatos) y animales de producción (ganado, aves, cerdos, peces) en más de 100 países. "
              "Ingresos LTM de US$9.517M (2T 2026: US$2.468M, -0,2%), margen operativo de ~37% y flujo de caja libre de "
              "US$2.366M LTM, destinado a recompras (US$3.644M LTM) y dividendos (US$889M en 2025)."),
    segments=[
        ("Mascotas (Companion animal)",
         "~68% de los ingresos: parasiticidas (Simparica Trio), dermatología (Apoquel, Cytopoint), dolor "
         "osteoartrítico (Librela, Solensia). En el 2T 2026 cayó 4,6% (US$1.708M) y 11% en EE.UU. por demanda más "
         "débil, competencia en dermatología y parasiticidas, genéricos de Cerenia y Convenia y menores ventas de "
         "Librela."),
        ("Animales de producción (Livestock)",
         "US$731M en el 2T 2026 (+12%): vacunas y medicamentos para ganado bovino (demanda elevada por el brote del "
         "gusano barrenador del Nuevo Mundo), cerdos, aves y peces."),
        ("Segmento EE.UU.",
         "US$1.266M en el 2T 2026 (-7%): mascotas -US$132M, producción +US$42M; ganancia del segmento -10%."),
        ("Segmento Internacional",
         "US$1.173M en el 2T 2026 (+8%; +5% operativo) por parasiticidas para mascotas y ganado."),
    ],
    bulls=[
        ("Líder global con marcas veterinarias y relación directa con veterinarios",
         "Escala en I+D (US$722M LTM), fabricación y fuerza de ventas veterinaria; márgenes operativos de ~37% y "
         "brutos de ~72%."),
        ("Tendencia estructural de gasto en mascotas",
         "Más mascotas, que viven más y reciben más tratamientos; el gasto veterinario es menos sensible al ciclo "
         "que otros consumos."),
        ("Retorno al accionista a precios deprimidos",
         "Recompras de US$3.644M LTM (acciones de 448M a fines de 2024 a 413M) y dividendo creciente."),
    ],
    bears=[
        ("Competencia en sus franquicias clave",
         "Dermatología (Apoquel/Cytopoint) y Simparica Trio enfrentan competidores nuevos y sensibilidad de precio; "
         "Librela cae tras reportes de eventos adversos."),
        ("Genéricos y concentración en mascotas de EE.UU.",
         "Cerenia y Convenia ya tienen competencia genérica; el segmento EE.UU. de mascotas cayó 11% en el 2T 2026."),
        ("Más deuda para recomprar",
         "Deuda de US$9.042M (US$6.570M en 2024) y demanda colectiva de accionistas sobre las declaraciones de "
         "desempeño y competencia de sus productos de mascotas."),
    ],
)

STORY = dict(
    title="Zoetis: el líder de la salud animal pierde crecimiento en mascotas de EE.UU. y el mercado lo re-valúa a la mitad",
    text=("Zoetis creció 8% anual durante una década con márgenes de ~37%, y el mercado le pagaba 30-57x utilidad. En "
          "2025-2026 la competencia en dermatología y parasiticidas, los genéricos y la debilidad de Librela frenaron "
          "el crecimiento (LTM +0,5%) y la acción cayó a ~US$71 (P/E ~12x). El caso Base asume un año de estancamiento "
          "(2%) y recuperación a 5% en los años 2-5 por nuevos productos y crecimiento internacional, con margen estable "
          "de 36%."),
    g="Año 1 2% (LTM +0,5%; 2T -0,2%), años 2-5 5%: estabilización de mascotas en EE.UU. y crecimiento internacional.",
    m="Margen operativo 36% (LTM 36,9%), estable.",
    tax="Tasa marginal 20% (efectiva ~20%).",
    s2c="2,0x: capex neto de depreciación bajo; I+D va como gasto.",
    roic="ROIC alto (>20%) incluso con goodwill.",
    wacc="Beta 0,9 (Direct Input), ERP maduro, deuda Baa2/BBB a 8 años.",
)

RECO = dict(
    g1="LTM +0,5%; 2T 2026 -0,2% (mascotas -4,6%, producción +12%).",
    m1="Margen operativo LTM 36,9% (EBIT reconstruido).",
    g25="5%: mercado de salud animal de un dígito medio; Zoetis pierde algo de participación en dermatología.",
    mt="36%: se mantiene; la presión de precio compensa el apalancamiento operativo.",
    s2c1="2,0x: capex de US$521M LTM con D&A de ~US$480M.",
    s2c2="2,0x.",
)

MULTIPLOS_EVALUACION = (
    "Evaluación ZTS: tras reconstruir el EBIT (antes era 0), los cierres 2021-2025 dan P/E de 21-57x y EV/EBITDA de "
    "15-38x. Con la acción en ~US$71 (P/E LTM ~12x, EV/EBITDA ~9x) se activó el override manual del bloque Base "
    "(columna J) = múltiplo LTM vivo: supone que el mercado no vuelve a pagar la prima de 'compounder defensivo' "
    "mientras no se estabilice el negocio de mascotas en EE.UU."
)

TESIS = dict(
    historia=("Zoetis se separó de Pfizer en 2013 y durante una década fue un 'compounder' defensivo: crecimiento de "
              "8% anual, márgenes de ~37% y marcas veterinarias líderes (Apoquel, Simparica Trio, Librela). En 2025-2026 "
              "esa historia se quebró en su mercado más rentable, mascotas en EE.UU.: competidores nuevos en "
              "dermatología y parasiticidas, genéricos de productos maduros, dudas de seguridad sobre Librela y un "
              "cliente más sensible al precio. Las ventas LTM crecieron 0,5% y la acción cayó a ~US$71. La tesis Base "
              "asume un año más de estancamiento y una recuperación a 5% (producción animal, internacional y nuevos "
              "lanzamientos) sin pérdida de margen; el Conservador asume caída de 1% anual y margen de 33%."),
    bull_bear=[
        ("Líder mundial en salud animal con márgenes de ~37% y FCF de US$2.366M LTM.",
         "Mascotas en EE.UU. -11% en el 2T 2026: competencia en dermatología y parasiticidas."),
        ("Producción animal +12% (2T 2026) y crecimiento internacional +8%.",
         "Genéricos de Cerenia y Convenia; menores ventas de Librela."),
        ("Recompras agresivas (US$3.644M LTM) y dividendo creciente.",
         "Deuda subió a US$9.042M para financiar recompras."),
        ("P/E LTM ~12x: el más bajo desde su salida a bolsa.",
         "Demanda colectiva de accionistas por declaraciones sobre productos de mascotas."),
    ],
    j_g1="Base 2%; Conservador -1% (erosión continúa); Optimista 6% (estabilización rápida y lanzamientos).",
    j_g25="Base 5%: mercado de salud animal de un dígito medio.",
    j_m1="Margen operativo LTM 36,9% (EBIT = utilidad antes de impuestos + intereses).",
    j_mt="Base 36%; Conservador 33% (presión de precio); Optimista 38%.",
    j_s2c="2,0x (1-5 y 6-10).",
    j_wacc="Beta 0,9 (Direct Input), ERP maduro, deuda Baa2/BBB a 8 años (US$9.042M).",
    j_mbase="Margen operativo LTM (US$3.510M / US$9.517M).",
    nota_multiplos="Múltiplos anclados al LTM (override) tras la re-valuación de 2025-2026.",
    conclusion=("El precio actual descuenta un estancamiento prolongado; el caso Base solo exige que las ventas vuelvan "
                "a crecer a un dígito medio sin perder margen."),
    monitor=("Variables a monitorear: ventas de mascotas en EE.UU. (dermatología, Simparica Trio, Librela), "
             "competencia y precios, crecimiento de producción animal, deuda neta/EBITDA y evolución de la demanda "
             "colectiva."),
)
