"""Valoracion de Chipotle Mexican Grill, Inc. (CMG) -- posicion IBKR sin valoracion previa en Modelo JMR.
Motor: scripts/posiciones_ibkr.py. Hoja: Drive > Análisis > CMG > Modelo JMR - CMG
(copia nueva de la plantilla maestra auditada)."""
from __future__ import annotations

SHEET_ID = "1VUVN1cCm3Hj8bLrmsCZFYBCDIq3DncxHGHH_jbW8ZtU"
TICKER = "CMG"
COMPANY = "Chipotle Mexican Grill, Inc."
SHORT = "Chipotle"
INDUSTRY = "Restaurant/Dining"
PEERS = ['MCD', 'SBUX', 'CAVA', 'DRI']
SPLITS = [("2024-06-26", 50)]  # split 50:1 efectivo el 26-jun-2024 (acciones pre-2024 reescaladas)

CATEGORY = "Crecimiento"
EMPLOYEES = 130000  # aproximado (10-K 2025); sin dato exacto verificado en esta hoja
DIVIDEND = False
MULT_ANCHOR = "LTM"  # la accion cayo de ~US$60 (dic-2024) a ~US$31: los cierres 2021-2024 (P/E 50x+) ya no son el multiplo pagado

Q2 = "https://www.sec.gov/Archives/edgar/data/1058090/000105809026000066/cmg-20260630.htm"
K10 = "https://www.sec.gov/Archives/edgar/data/1058090/000105809026000009/cmg-20251231.htm"
SOURCES = (
    "Fuentes: estados financieros del modelo (SEC EDGAR, XBRL, CIK 0001058090: 10-K 2025 presentado el 04-feb-2026, "
    f"{K10}; 10-Q del 2T 2026 presentado el 31-jul-2026, {Q2}); ventas comparables, restaurantes, ventas digitales y "
    "recompras del mismo 10-Q. Acciones anteriores a 2024 reescaladas por el split 50:1 de jun-2024. Damodaran Online "
    "(industria 'Restaurant/Dining'); UST 10 años y precio de CMG vía yfinance (cierre del 25-sep-2026)."
)

# Arrendamientos: el gasto de alquiler ya esta dentro del EBIT (US$1.820M LTM), asi que el pasivo
# por arrendamiento operativo (US$4.773M) NO se resta como deuda (evita contarlo dos veces).
# Deuda financiera de Chipotle = 0.
INPUT_EXTRA = {"B16": 0}

BASE = dict(g1=0.08, m1=0.15, g25=0.08, mt=0.17, conv=5, s2c1=2.6, s2c2=2.2, tax=0.245, wacc_term=0.09)
SCEN = dict(g1_cons=0.05, g1_opt=0.11, mt_cons=0.14, mt_opt=0.20)
COC = {
    "B22": "Direct Input", "B23": 1.10,   # beta observado ~1,1
    "B26": "Country of Incorporation",
    # Sin deuda financiera (arrendamientos tratados como gasto operativo, ver INPUT_EXTRA).
    "B33": 10, "B34": "Actual rating", "B36": "A2/A",
}

CUALI = dict(
    ceo="Scott Boatwright — CEO desde noviembre de 2024 (antes Director de Operaciones).",
    sector="Restaurantes de comida rápida casual (Damodaran: Restaurant/Dining)",
    web="https://www.chipotle.com  |  IR: https://ir.chipotle.com",
    overview=("Chipotle opera restaurantes propios (sin franquicias en EE.UU.) de comida mexicana rápida-casual: al "
              "30-jun-2026 tenía 4.186 restaurantes propios (4.074 en EE.UU. y 112 en el exterior) y 15 operados por "
              "socios internacionales. Ingresos LTM US$12.424M con margen operativo de 14,6%; en el 2T 2026 facturó "
              "US$3.300M (+9,3%) con ventas comparables de +2,2% (10-Q 2T 2026)."),
    segments=[
        ("Restaurantes propios en EE.UU.",
         "Prácticamente todos los ingresos: menú corto (burritos, bowls, tacos, ensaladas) preparado en línea a la vista, "
         "con alta rotación. Crecimiento = aperturas (~8% de unidades nuevas por año, mayoría con Chipotlane) + ventas "
         "comparables."),
        ("Canal digital y Chipotlanes",
         "Las ventas digitales fueron 38,3% de los ingresos de comida y bebida en el 2T 2026 (35,5% un año antes); las "
         "Chipotlanes (ventanilla para retirar pedidos digitales) mejoran la economía de los locales nuevos."),
        ("Internacional",
         "112 restaurantes propios (Canadá y Europa) y 15 de socios en Medio Oriente y Asia: opcionalidad de largo "
         "plazo, aún inmaterial en ingresos."),
        ("Asignación de capital",
         "Sin deuda financiera; recompras de US$1.332M en el 1S 2026 a un precio promedio de US$34,35 por acción y "
         "US$1.679M de autorización remanente al 30-jun-2026."),
    ],
    bulls=[
        ("Economía unitaria y crecimiento de unidades",
         "Modelo 100% propio con locales rentables: el crecimiento de ~8% anual en unidades no requiere franquiciados "
         "ni deuda y se financia con flujo operativo (US$2.328M LTM)."),
        ("Pista de crecimiento en EE.UU. y exterior",
         "La compañía apunta a duplicar su base de restaurantes en Norteamérica en el largo plazo; hoy tiene ~4.200."),
        ("Recompras a precios deprimidos",
         "US$2.783M de recompras LTM con la acción a la mitad de su máximo reduce la base de acciones (1.265M LTM vs "
         "1.377M a fin de 2024)."),
    ],
    bears=[
        ("Desaceleración del tráfico",
         "Ventas comparables de solo +2,2% en el 2T 2026 (tráfico +1,0%) tras un 2025 débil: el consumidor de ingresos "
         "medios gasta menos en restaurantes."),
        ("Presión de costos y márgenes",
         "Aranceles e inflación de alimentos, empaques y salarios: el margen operativo LTM (14,6%) está por debajo del "
         "16,9% de 2024."),
        ("Competencia en fast-casual",
         "Cadenas como CAVA, Sweetgreen y la oferta de valor de McDonald's y Taco Bell compiten por el mismo cliente."),
    ],
)

STORY = dict(
    title="Chipotle: crecimiento de unidades intacto, tráfico débil y una acción re-valuada a la mitad",
    text=("Chipotle sigue abriendo ~8% más restaurantes por año sin deuda y con flujo operativo de US$2.328M LTM, pero "
          "las ventas comparables se frenaron (+2,2% en el 2T 2026) y el margen operativo bajó a 14,6% LTM. La acción "
          "cayó de ~US$60 a ~US$31. El caso Base asume crecimiento de 8% (unidades + comparables bajos) y recuperación "
          "parcial del margen a 17%, cerca del máximo de 2024."),
    g="8% años 1-5: ~7-8% de restaurantes nuevos + ventas comparables de ~1-2%.",
    m="Margen Año 1 15% (LTM 14,6%); objetivo 17% (2024: 16,9%) con apalancamiento de ventas digitales y Chipotlanes.",
    tax="Tasa marginal 24,5% (efectiva LTM 24,1%).",
    s2c="2,6x / 2,2x: la reinversión neta (capex US$758M LTM menos D&A ~US$380M) financia ~US$1.000M de ingresos nuevos por año.",
    roic="ROIC alto (restaurantes propios rentables, sin goodwill).",
    wacc="Beta 1,1 (Direct Input), ERP maduro; sin deuda financiera (alquileres dentro del EBIT).",
)

RECO = dict(
    g1="Unidades nuevas ~8% + comparables +2,2% (2T 2026); ingresos 2T +9,3%.",
    m1="Margen operativo LTM 14,6%.",
    g25="8%: la compañía tiene pista para seguir abriendo unidades a ritmo similar.",
    mt="17%: vuelta al nivel de 2024 (16,9%) con algo de apalancamiento operativo.",
    s2c1="2,6x: capex neto de depreciación (~US$380M/año) frente a ~US$1.000M de ingresos incrementales.",
    s2c2="2,2x: mayor peso internacional y remodelaciones.",
)

MULTIPLOS_EVALUACION = (
    "Evaluación CMG: tras reescalar las acciones pre-2024 por el split 50:1, los múltiplos de los cierres 2021-2024 "
    "quedan en P/E ~50-60x y EV/EBITDA ~35-40x, propios de una acción que el mercado veía como compounder de "
    "crecimiento. Con la acción en ~US$31 (P/E LTM ~30x, EV/EBITDA ~20x) se activó el override manual del bloque Base "
    "(columna J) = múltiplo LTM vivo: supone que el mercado no vuelve a pagar los múltiplos de 2021-2024."
)

TESIS = dict(
    historia=("Chipotle es probablemente la cadena de restaurantes con mejor economía unitaria de EE.UU.: todos sus "
              "locales son propios, no tiene deuda financiera y financia su crecimiento de ~8% anual en unidades con "
              "flujo operativo. Entre 2021 y 2024 eso se tradujo en crecimiento de ingresos de 14-26% anual y en un "
              "múltiplo de 50-60x utilidad. Desde 2025 el tráfico se debilitó (comparables +2,2% en el 2T 2026) y el "
              "margen se comprimió por costos, y la acción cayó a la mitad. La tesis Base asume que el crecimiento de "
              "unidades se mantiene, que las comparables vuelven a un dígito bajo positivo y que el margen se recupera "
              "a 17%; el Conservador asume comparables planas (5% de crecimiento total) y margen de 14%."),
    bull_bear=[
        ("Economía unitaria excelente y crecimiento de ~8% en unidades financiado con caja propia.",
         "Tráfico débil: comparables +2,2% y transacciones +1,0% en el 2T 2026."),
        ("Sin deuda financiera; recompras de US$2.783M LTM a precios deprimidos.",
         "Margen operativo LTM 14,6% vs 16,9% en 2024 por costos de alimentos, aranceles y salarios."),
        ("Ventas digitales 38,3% y Chipotlanes mejoran la productividad de los locales nuevos.",
         "Competencia creciente en fast-casual (CAVA, Sweetgreen) y guerras de valor en comida rápida."),
        ("Opcionalidad internacional (112 propios + 15 de socios).",
         "Cambio de CEO en nov-2024 (salida de Brian Niccol): riesgo de ejecución."),
    ],
    j_g1="Base 8%; Conservador 5% (comparables planas, solo unidades); Optimista 11% (comparables de +3-4%).",
    j_g25="Base 8%: aperturas ~8% anual sostenidas.",
    j_m1="Margen operativo LTM 14,6%; Año 1 15%.",
    j_mt="Base 17% (≈ 2024); Conservador 14%; Optimista 20% (apalancamiento operativo pleno).",
    j_s2c="2,6x (1-5) / 2,2x (6-10): capex neto de D&A (~US$380M/año) frente a ~US$1.000M de ingresos nuevos por año.",
    j_wacc="Beta 1,1 (Direct Input), ERP maduro; sin deuda financiera: el alquiler ya está en el EBIT, así que el pasivo por arrendamiento (US$4.773M) no se resta como deuda.",
    j_mbase="Margen operativo GAAP LTM (US$1.820M / US$12.424M).",
    nota_multiplos="Múltiplos anclados al LTM (override) tras la re-valuación de 2025-2026.",
    conclusion=("El valor depende de que las comparables vuelvan a crecer y el margen se recupere; el crecimiento de "
                "unidades por sí solo sostiene un valor cercano al escenario Conservador."),
    monitor=("Variables a monitorear: ventas comparables y transacciones trimestrales, margen a nivel restaurante "
             "(costos de alimentos y aranceles), ritmo de aperturas con Chipotlane y precio promedio de las recompras."),
)
