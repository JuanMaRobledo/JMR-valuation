"""Valoracion de On Holding AG (ONON) -- posicion IBKR sin valoracion previa en Modelo JMR.
Motor: scripts/posiciones_ibkr.py. Hoja: Drive > Análisis > ONON > Modelo JMR - ONON
(copia nueva de la plantilla maestra auditada)."""
from __future__ import annotations

SHEET_ID = "17E_Rd-MD-u5i8Vez7sYwcWIdVYvDdjNhOu-6NWAzGnQ"
TICKER = "ONON"
COMPANY = "On Holding AG"
SHORT = "On"
INDUSTRY = "Shoe"
PEERS = ['NKE', 'DECK', 'BIRK', 'SKX']

# --- Emisor extranjero (20-F, IFRS, CHF): serie armada en scripts/ifrs_builder.py ---------------
H1_URL = "https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/onholdingag-20260630_htm.xml"
IFRS = dict(
    TICKER="ONON", FACTS_TICKER="ONON", YF_TICKER="ONON", COMPANY="On Holding AG", UNIT="CHF",
    COUNTRY="Switzerland", INDUSTRY="Shoe", MARGINAL_TAX=0.20,
    YEARS=["2021", "2022", "2023", "2024", "2025"],
    # CHF por US$ (yfinance CHF=X): promedio del año (flujos) y cierre (saldos).
    FX_AVG={"2021": 0.9141, "2022": 0.9548, "2023": 0.8986, "2024": 0.8803, "2025": 0.8309},
    FX_YE={"2021": 0.9137, "2022": 0.9229, "2023": 0.8434, "2024": 0.9032, "2025": 0.7917},
    FX_LTM_AVG=0.7934, FX_H1_END=0.8087,   # promedio jul-2025 a jun-2026; cierre del 30-jun-2026
    H1=H1_URL, H1_START="2026-01-01", H1_END="2026-06-30", H1_PREV_START="2025-01-01", H1_PREV_END="2025-06-30",
    TAGS=dict(
        revenue="RevenueFromContractsWithCustomers", cogs="CostOfSales", ebit="ProfitLossFromOperatingActivities",
        pretax="ProfitLossBeforeTax", tax="IncomeTaxExpenseContinuingOperations", ni="ProfitLossAttributableToOwnersOfParent",
        da="AdjustmentsForDepreciationAndAmortisationExpense", sbc="AdjustmentsForSharebasedPayments",
        ocf="CashFlowsFromUsedInOperatingActivities",
        capex_ppe="PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities",
        capex_int="PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities",
        buyback="PurchaseOfTreasuryShares", icf="CashFlowsFromUsedInInvestingActivities",
        fcf="CashFlowsFromUsedInFinancingActivities", fin_exp="FinanceCosts", fin_inc="FinanceIncome",
        rd="ResearchAndDevelopmentExpense", sga="SellingGeneralAndAdministrativeExpense",
        cash="CashAndCashEquivalents", lease_c="CurrentLeaseLiabilities", lease_nc="NoncurrentLeaseLiabilities",
        ca="CurrentAssets", cl="CurrentLiabilities", assets="Assets", equity="Equity", recv="CurrentTradeReceivables",
        ppe="PropertyPlantAndEquipment", intang="IntangibleAssetsAndGoodwill",
        ap="TradeAndOtherCurrentPayablesToTradeSuppliers", retained="RetainedEarnings",
    ),
    # Base economica en acciones Clase A equivalentes (1 Clase B = 1/10 de Clase A en derechos
    # economicos): Clase A de la portada del 20-F + ~34,5M de equivalentes de Clase B (33,4M tras la
    # conversion de may-2025). Promedio diluido = utilidad neta / EPS diluido reportado.
    SHARES_YE=[311.4, 316.5, 318.7, 323.8, 330.3],
    DILUTED_AVG=[300.0, 320.0, 320.0, 327.0, 334.0],
    SHARES_LTM=331.0,
)


def CUSTOM_REFRESH():
    import ifrs_builder as ib
    ib.IfrsCompany(IFRS).run(SHEET_ID, PEERS)

CATEGORY = "Crecimiento"
EMPLOYEES = 3200  # aproximado (20-F 2025); sin dato exacto verificado en esta hoja
DIVIDEND = False
MULT_ANCHOR = "LTM"  # accion de ~US$55 (dic-2024) a ~US$30; los cierres 2022-2025 (P/E 64-96x) ya no son el multiplo pagado

F20 = "https://www.sec.gov/Archives/edgar/data/1858985/000185898526000008/onholdingag-20251231.htm"
PR2 = "https://www.sec.gov/Archives/edgar/data/1858985/000185898526000018/a26q2-ex993xpressrelease.htm"
IDAY = "https://www.sec.gov/Archives/edgar/data/1858985/000185898526000021/exhibit991oninvestorday202.htm"
SOURCES = (
    "Fuentes: estados financieros del modelo armados desde XBRL IFRS de SEC EDGAR (CIK 0001858985): 20-F 2025 "
    f"presentado el 03-mar-2026 ({F20}) y 6-K del 1S 2026 del 11-ago-2026 (LTM = 2025 + 1S 2026 - 1S 2025); CHF "
    "convertidos a US$ al tipo promedio de cada año (flujos) y de cierre (saldos), yfinance CHF=X. Guía 2026 y "
    f"resultados del 2T 2026 del comunicado del 11-ago-2026 ({PR2}); metas 2029 y recompra de US$1.000M del Investor "
    f"Day del 22-sep-2026 ({IDAY}). Acciones en base Clase A equivalente (1 Clase B = 1/10). Damodaran Online "
    "(industria 'Shoe'); UST 10 años y precio de ONON vía yfinance (cierre del 25-sep-2026)."
)

BASE = dict(g1=0.18, m1=0.14, g25=0.14, mt=0.17, conv=5, s2c1=2.5, s2c2=2.2, tax=0.20, wacc_term=0.09)
SCEN = dict(g1_cons=0.10, g1_opt=0.22, mt_cons=0.13, mt_opt=0.20)
COC = {
    "B22": "Direct Input", "B23": 1.50,   # beta observado ~1,5 (marca de consumo en hipercrecimiento)
    "B26": "Country of Incorporation",
    # Sin prestamos bancarios: la deuda son arrendamientos IFRS 16 (US$659M).
    "B33": 5, "B34": "Actual rating", "B36": "A2/A",
}

CUALI = dict(
    ceo="Martin Hoffmann — CEO y CFO; los cofundadores David Allemann y Caspar Coppetti son co-presidentes ejecutivos.",
    sector="Calzado y ropa deportiva premium (Damodaran: Shoe)",
    web="https://www.on.com  |  IR: https://investors.on-running.com",
    overview=("On es una marca suiza de calzado y ropa deportiva premium (running, outdoor, tenis y lifestyle), "
              "fundada en 2010. Facturó CHF 3.014M en 2025 (+30%) y CHF 850,3M en el 2T 2026 (+13,5% en CHF, +21,6% a "
              "tipo de cambio constante), con margen bruto de 65,4% y margen EBITDA ajustado de 19,8%. El canal directo "
              "(tiendas propias y e-commerce) ya es 45,7% de las ventas."),
    segments=[
        ("Calzado (running, outdoor, lifestyle)",
         "CHF 2.804M en 2025 (93% de las ventas): franquicias Cloudmonster, Cloudsurfer, Cloudtilt y tecnologías "
         "propias (CloudTec, Helion, LightSpray)."),
        ("Ropa y accesorios",
         "CHF 170M de ropa y CHF 40M de accesorios en 2025; la ropa creció 47,7% (56,2% a tipo constante) en el 2T 2026."),
        ("Canales: mayorista y directo",
         "Mayorista CHF 1.753M y directo CHF 1.261M en 2025; en el 2T 2026 el canal directo creció 26% (34,3% a tipo "
         "constante) y llegó a 45,7% de las ventas."),
        ("Regiones",
         "Américas CHF 1.740M, EMEA CHF 763M y Asia-Pacífico CHF 511M en 2025 (Asia casi se duplicó; más de 20% de las "
         "ventas en el 2T 2026)."),
    ],
    bulls=[
        ("Marca premium con disciplina de precio",
         "Margen bruto de 65,4% en el 2T 2026 (+3,9 pp) absorbiendo aranceles de EE.UU., sin descuentos: señal de poder "
         "de marca."),
        ("Pista de crecimiento larga",
         "Meta de crecimiento 'high-teens' a tipo constante hasta 2029, entrada en fútbol y golf, ropa y Asia creciendo "
         "mucho más rápido que el total (Investor Day 22-sep-2026)."),
        ("Caja y primera recompra",
         "Caja de CHF 1.206M sin deuda financiera y una recompra inaugural de hasta US$1.000M hasta 2029."),
    ],
    bears=[
        ("Moda y ciclo de consumo",
         "El calzado deportivo es propenso a ciclos de moda; Nike, Adidas, Hoka (Deckers) y otras marcas compiten por el "
         "mismo cliente premium."),
        ("Divisa y aranceles",
         "Reporta en CHF pero vende mayormente en US$ y otras monedas: el franco fuerte restó ~8 pp de crecimiento en el "
         "2T 2026; aranceles de EE.UU. a la fabricación en Vietnam e Indonesia."),
        ("Valuación y gobierno",
         "Estructura de dos clases (Clase B con voto de los fundadores) y dependencia de pocos proveedores asiáticos."),
    ],
)

STORY = dict(
    title="On: la marca premium de más rápido crecimiento del calzado deportivo, con márgenes de lujo",
    text=("On creció de CHF 725M (2021) a CHF 3.014M (2025) y guía crecimiento de ~20% a tipo constante para 2026 y "
          "'high-teens' hasta 2029, con margen bruto de al menos 65% y EBITDA ajustado de al menos 22% en 2029. La acción "
          "cayó de ~US$55 a ~US$30 por la desaceleración en CHF y los aranceles. El caso Base asume 18% de crecimiento en "
          "US$ el Año 1 y 14% en los años 2-5, con margen operativo GAAP de 17% (EBITDA ajustado 22% menos D&A y "
          "compensación en acciones)."),
    g="Año 1 18% (guía 2026: 'low-20%' a tipo constante), años 2-5 14% (meta 'high-teens' hasta 2029 con desgaste).",
    m="Margen GAAP Año 1 14% (LTM 13,8%); objetivo 17% (meta de EBITDA ajustado ≥22% en 2029 menos D&A y SBC).",
    tax="Tasa marginal 20% (Suiza + mezcla internacional; la efectiva LTM, 8%, está deprimida por partidas diferidas).",
    s2c="2,5x / 2,2x: marca con fabricación tercerizada; el capital va a inventario, tiendas propias y cuentas por cobrar.",
    roic="ROIC alto y creciente (margen en expansión, capital liviano).",
    wacc="Beta 1,5 (Direct Input), ERP maduro; deuda = arrendamientos IFRS 16.",
)

RECO = dict(
    g1="2T 2026: +21,6% a tipo constante, +13,5% en CHF; guía 2026 'low-20%' a tipo constante.",
    m1="Margen operativo IFRS LTM 13,8%.",
    g25="14%: meta 'high-teens' a tipo constante hasta 2029, con algo de desgaste por escala.",
    mt="17%: EBITDA ajustado objetivo ≥22% (2029) menos D&A (~3,5%) y compensación en acciones (~2%).",
    s2c1="2,5x: capex de CHF 88M LTM; inventario y tiendas propias.",
    s2c2="2,2x: más tiendas propias y categorías nuevas.",
)

MULTIPLOS_EVALUACION = (
    "Evaluación ONON: serie armada desde XBRL IFRS (CHF → US$). Los cierres 2022-2025 dan P/E de 64-96x y EV/EBITDA "
    "de 25-48x, múltiplos de hipercrecimiento. Con la acción en ~US$30 el P/E LTM es ~20x (la utilidad LTM incluye "
    "ganancias cambiarias) y el EV/EBITDA ~13x. Se activó el override manual del bloque Base (columna J) = múltiplo "
    "LTM vivo: conservador para una marca que guía crecimiento de ~20%."
)

TESIS = dict(
    historia=("On pasó de ser una marca suiza de nicho para corredores a una marca global de ropa deportiva premium: "
              "CHF 725M de ventas en 2021, CHF 3.014M en 2025 y un margen bruto de 65% que supera al de Nike y Adidas, "
              "sin depender de descuentos. El canal directo, Asia y la ropa crecen más rápido que el total, y el "
              "Investor Day de sep-2026 fijó metas de crecimiento 'high-teens' hasta 2029 con EBITDA ajustado de al "
              "menos 22%. Aun así la acción cayó a ~US$30 por el franco fuerte, los aranceles y el temor a un ciclo de "
              "moda. La tesis Base asume que On cumple una versión algo más moderada de sus metas (14% en US$ en los "
              "años 2-5) con margen operativo de 17%; el Conservador asume que la marca madura antes (10%) y el margen "
              "se estanca en 13%."),
    bull_bear=[
        ("Margen bruto de 65,4% sin descuentos: poder de marca real.",
         "Ciclo de moda: las marcas de calzado 'de moda' pueden perder impulso rápido."),
        ("Canal directo 45,7% de las ventas y creciendo 34% a tipo constante.",
         "Franco suizo fuerte y aranceles de EE.UU. sobre fabricación asiática."),
        ("Caja de CHF 1.206M, sin deuda financiera y recompra de hasta US$1.000M.",
         "Competencia de Nike (en recuperación), Hoka, Adidas y Asics en running premium."),
        ("Asia-Pacífico, ropa, fútbol y golf como nuevas avenidas de crecimiento.",
         "Estructura de dos clases de acciones con control de los fundadores."),
    ],
    j_g1="Base 18% (US$); Conservador 10% (la marca madura); Optimista 22% (guía 2026 a tipo constante).",
    j_g25="Base 14%: meta 'high-teens' a tipo constante hasta 2029 con algo de desgaste.",
    j_m1="Margen operativo IFRS LTM 13,8% (US$560M / US$4.059M).",
    j_mt="Base 17%; Conservador 13%; Optimista 20% (meta de EBITDA ajustado ≥22% casi completa).",
    j_s2c="2,5x (1-5) / 2,2x (6-10): fabricación tercerizada; capital en inventario y tiendas.",
    j_wacc="Beta 1,5 (Direct Input), ERP maduro; deuda = arrendamientos IFRS 16 (US$659M); caja US$1.491M.",
    j_mbase="Margen operativo IFRS LTM (jul-2025 a jun-2026, en US$).",
    nota_multiplos="Múltiplos anclados al LTM (override) tras la caída de la acción.",
    conclusion=("El valor depende de que On sostenga crecimiento de doble dígito alto con márgenes crecientes, como "
                "guía la compañía hasta 2029."),
    monitor=("Variables a monitorear: crecimiento a tipo constante vs. guía, margen bruto y descuentos, peso del canal "
             "directo, ventas de ropa y Asia-Pacífico, efecto del franco y los aranceles, ejecución de la recompra."),
)
