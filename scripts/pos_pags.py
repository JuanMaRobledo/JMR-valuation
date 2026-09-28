"""Valoracion de PagSeguro Digital Ltd. (PAGS) -- posicion IBKR sin valoracion previa en Modelo JMR.
Motor: scripts/posiciones_ibkr.py. Hoja: Drive > Análisis > PAGS > Modelo JMR - PAGS
(copia nueva de la plantilla maestra auditada)."""
from __future__ import annotations

SHEET_ID = "1Q17gaT8w8fGx-3uRn7eCS_HsF0q-HZucEtgXGtVEIQY"
TICKER = "PAGS"
COMPANY = "PagSeguro Digital Ltd."
SHORT = "PagBank"
INDUSTRY = "Financial Svcs. (Non-bank & Insurance)"
PEERS = ['STNE', 'NU', 'MELI']

# --- Emisor extranjero (20-F, IFRS, R$) y financiero: serie armada en scripts/ifrs_builder.py ------
# Tratamiento de institucion financiera (enfoque de flujo al accionista dentro del DCF del modelo):
#   - EBIT = utilidad antes de impuestos: el costo financiero (fondeo de la anticipacion de cobros y
#     de los depositos de PagBank) es un costo OPERATIVO de un banco, no financiamiento corporativo.
#   - Deuda financiera = 0 (prestamos, CDB y depositos son fondeo operativo); caja = 0 (la caja de un
#     banco es operativa/regulatoria). Solo quedan los arrendamientos como deuda.
#   - La reinversion se mide contra el patrimonio (Sales-to-Capital ~ ingresos / patrimonio), que es el
#     capital regulatorio que exige crecer la cartera.
_F20 = "https://www.sec.gov/Archives/edgar/data/1712807/000155485526000826/pags-20251231_htm.xml"
_Y25 = {  # 20-F 2025 (instancia XBRL; companyfacts todavia no la incluye), R$
    "revenue": 20410.5e6, "ebit": 2549.4e6, "pretax": 2549.4e6, "tax": 431.1e6, "ni": 2118.4e6,
    "da": 1807.5e6, "sbc": 112.1e6, "ocf": 7562.4e6, "capex_ppe": 1040.0e6, "capex_int": 1236.8e6,
    "buyback": 1330.2e6, "div": 617.1e6, "equity": 14639.6e6, "assets": 74409.5e6, "ca": 64933.1e6,
    "cl": 47783.1e6, "lease_c": 19.1e6, "lease_nc": 59.7e6, "intang": 3172.4e6, "cogs": 0.0,
}
IFRS = dict(
    TICKER="PAGS", FACTS_TICKER="PAGS", YF_TICKER="PAGS", COMPANY="PagSeguro Digital Ltd.", UNIT="BRL",
    COUNTRY="Brazil", INDUSTRY="Financial Svcs. (Non-bank & Insurance)", MARGINAL_TAX=0.34,
    YEARS=["2021", "2022", "2023", "2024", "2025"],
    FX_AVG={"2021": 5.3939, "2022": 5.1620, "2023": 4.9942, "2024": 5.3826, "2025": 5.5878},
    FX_YE={"2021": 5.5702, "2022": 5.2846, "2023": 4.8502, "2024": 6.1779, "2025": 5.4762},
    FX_LTM_AVG=5.2905, FX_H1_END=5.1747,
    H1=None, H1_START="2026-01-01", H1_END="2026-06-30", H1_PREV_START="2025-01-01", H1_PREV_END="2025-06-30",
    # 1S 2026 / 1S 2025 (estados interinos del 6-K del 11-ago-2026), R$
    H1_MANUAL={"revenue": (10085.85e6, 9908.326e6), "ebit": (1247.81e6, 1196.154e6),
               "pretax": (1247.81e6, 1196.154e6), "tax": (153.209e6, 134.303e6), "ni": (1094.601e6, 1061.851e6)},
    H1_BAL_MANUAL={"equity": 15015.865e6, "cash": 0.0, "sti": 0.0, "loans_c": 0.0, "loans_nc": 0.0,
                   "lease_c": 19.1e6, "lease_nc": 59.7e6},
    TAGS=dict(
        revenue="Revenue", ebit="ProfitLossBeforeTax", pretax="ProfitLossBeforeTax",
        tax="IncomeTaxExpenseContinuingOperations", ni="ProfitLossAttributableToOwnersOfParent",
        da="AdjustmentsForDepreciationAndAmortisationExpense", sbc="AdjustmentsForSharebasedPayments",
        ocf="CashFlowsFromUsedInOperatingActivities",
        capex_ppe="PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities",
        capex_int="PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities",
        buyback="PurchaseOfTreasuryShares", div="DividendsPaidClassifiedAsFinancingActivities",
        icf="CashFlowsFromUsedInInvestingActivities", fcf="CashFlowsFromUsedInFinancingActivities",
        lease_c="CurrentLeaseLiabilities", lease_nc="NoncurrentLeaseLiabilities",
        ca="CurrentAssets", cl="CurrentLiabilities", assets="Assets", equity="Equity",
        intang="IntangibleAssetsAndGoodwill", retained="RetainedEarnings",
    ),
    OVERRIDES={k: {"2025": v} for k, v in _Y25.items()},
    # Acciones (millones): promedio diluido del 20-F (2024: 319,5; 2025: 297,9); al cierre, aprox.
    # emitidas - tesoreria. 1S 2026: utilidad / EPS basico => ~278M promedio; ~276M en circulacion.
    SHARES_YE=[329.0, 325.0, 322.0, 317.6, 290.0],
    DILUTED_AVG=[330.0, 326.0, 323.0, 319.5, 297.9],
    SHARES_LTM=276.0,
)


def CUSTOM_REFRESH():
    import ifrs_builder as ib
    ib.IfrsCompany(IFRS).run(SHEET_ID, PEERS)

CATEGORY = "Financiera"
EMPLOYEES = 8000  # aproximado (20-F 2025); sin dato exacto verificado en esta hoja
DIVIDEND = True
MULT_ANCHOR = "LTM"

F20_HTM = "https://www.sec.gov/Archives/edgar/data/1712807/000155485526000826/pags-20251231.htm"
Q2_FS = "https://www.sec.gov/Archives/edgar/data/1712807/000155485526001791/MainDocument.htm"
Q2_PR = "https://www.sec.gov/Archives/edgar/data/1712807/000155485526001793/MainDocument.htm"
DIV_BB = "https://www.sec.gov/Archives/edgar/data/1712807/000155485526001939/MainDocument.htm"
SOURCES = (
    f"Fuentes: 20-F 2025 de PagSeguro Digital (presentado el 29-abr-2026, {F20_HTM}; instancia XBRL IFRS), estados "
    f"interinos del 1S 2026 (6-K del 11-ago-2026, {Q2_FS}) y comunicado de resultados del 2T 2026 ({Q2_PR}); metas "
    f"de dividendos 2027-2028 y recompra de US$150M (6-K del 01-sep-2026, {DIV_BB}). R$ convertidos a US$ al promedio "
    "de cada año (flujos) y al cierre (saldos), yfinance BRL=X. Damodaran Online (ERP de Brasil 7,47%); UST 10 años "
    "y precio de PAGS vía yfinance (cierre del 25-sep-2026). Tratamiento de banco: EBIT = utilidad antes de "
    "impuestos, sin deuda financiera ni caja excedente (ver pos_pags.py)."
)

BASE = dict(g1=0.05, m1=0.125, g25=0.06, mt=0.14, conv=5, s2c1=1.4, s2c2=1.4, tax=0.25, wacc_term=0.12)
SCEN = dict(g1_cons=0.02, g1_opt=0.09, mt_cons=0.11, mt_opt=0.16)
COC = {
    "B22": "Direct Input", "B23": 1.30,   # beta observado ~1,3 contra el mercado de EE.UU.
    "B26": "Country of Incorporation",    # Input sheet!B8 = Brazil -> ERP 7,47% (4,23% maduro + 3,24% pais)
    "B33": 3, "B34": "Actual rating", "B36": "Ba1/BB+",
}

CUALI = dict(
    ceo="Alexandre Magnani — CEO de PagBank; el fundador Luis Frias dejó la presidencia del Directorio el 21-ago-2026.",
    sector="Pagos y banca digital para micro y pequeños comercios en Brasil (Damodaran: Financial Svcs. (Non-bank & Insurance))",
    web="https://www.pagbank.com.br  |  IR: https://investors.pagbank.com",
    overview=("PagSeguro (marca PagBank) procesa pagos con tarjeta para micro, pequeños y medianos comercios en Brasil "
              "y opera un banco digital con depósitos, crédito y servicios financieros. Ingresos y rendimientos de R$20.411M "
              "en 2025 (+8,5%), utilidad neta de R$2.118M, patrimonio de R$15.016M (jun-2026), ROAE de 15,6% y un índice "
              "de Basilea de 22,5% en el 2T 2026."),
    segments=[
        ("Pagos (adquirencia)",
         "Terminales POS, tap-on-phone y pagos en línea para comercios chicos; ingresos por tasa de descuento y por "
         "anticipación de cobros (el comercio cobra antes a cambio de un costo financiero)."),
        ("Banca digital (PagBank)",
         "Cuentas, tarjetas, inversiones y crédito para comercios y personas; depósitos de clientes de R$28.428M a fin "
         "de 2025 que fondean la operación a menor costo que la deuda mayorista."),
        ("Crédito",
         "Cartera en expansión disciplinada (préstamos con garantía de cobros, consignado, tarjetas); el gasto por "
         "pérdidas crediticias subió a R$129,6M en el 1S 2026 (R$48,9M un año antes)."),
        ("Capital y retorno al accionista",
         "Basilea 22,5% (rango objetivo 18-22%): dividendos (US$0,28/acción en sep-2026; meta de R$1.000M/año en "
         "2027-2028) y recompras (R$1.330M en 2025; nuevo programa de US$150M)."),
    ],
    bulls=[
        ("Ecosistema de pagos + banco con fondeo propio",
         "Los depósitos de clientes abaratan el fondeo de la anticipación de cobros: el costo financiero bajó en el 2T "
         "2026 y el beneficio bruto creció 3%."),
        ("Retorno de capital muy alto frente a la valuación",
         "Dividendos, recompras (acciones promedio de 319,5M en 2024 a ~278M en el 1S 2026) y un P/E LTM de ~6x con "
         "P/VL ~0,9x."),
        ("Capital holgado",
         "Basilea 22,5%, por encima del rango objetivo: margen para crecer el crédito y seguir distribuyendo."),
    ],
    bears=[
        ("Competencia feroz en adquirencia y banca digital",
         "Stone, Nubank, Mercado Pago, Cielo, Rede y el PIX (pagos instantáneos gratuitos del Banco Central) presionan "
         "las tasas de descuento; los ingresos por transacciones cayeron de R$9.183M (2024) a R$8.159M (2025)."),
        ("Riesgo macro y de tasas en Brasil",
         "Tasas altas encarecen el fondeo y elevan la morosidad; el real volátil afecta el valor en US$."),
        ("Riesgo de crédito y de gobierno",
         "Crédito en expansión en un ciclo difícil y salida del fundador y accionista controlador indirecto de la "
         "presidencia del Directorio (ago-2026)."),
    ],
)

STORY = dict(
    title="PagBank: un banco digital de pagos rentable, con crecimiento bajo y valuado como si no creciera",
    text=("PagSeguro gana ~R$2.100M por año con ROAE de ~15-16% y devuelve casi todo al accionista, pero su negocio "
          "original de adquirencia se achica por la competencia y el PIX, mientras el banco y el crédito crecen. La acción "
          "cotiza a ~US$9 (P/E ~6x, P/VL ~0,9x). El caso Base asume crecimiento de 5-6% (en US$) y un margen antes de "
          "impuestos de 14% sobre ingresos, con costo de capital de mercado brasileño."),
    g="Año 1 5%, años 2-5 6%: banca y crédito compensan la caída de ingresos de adquirencia.",
    m="Margen antes de impuestos 12,5% (LTM 12,6%); objetivo 14% con fondeo más barato vía depósitos.",
    tax="Tasa marginal 25% (efectiva LTM 17,3% por incentivos; nominal Brasil 34%).",
    s2c="1,4x: ingresos / patrimonio; crecer exige retener capital regulatorio (Basilea 18-22%).",
    roic="ROAE ~15,6% (2T 2026), cercano al costo del capital propio en Brasil.",
    wacc="Costo del capital propio: beta 1,3 x ERP de Brasil 7,47% + UST; sin deuda financiera (fondeo operativo).",
)

RECO = dict(
    g1="Ingresos 1S 2026 +1,8% en R$; en US$ el real más fuerte suma crecimiento.",
    m1="Utilidad antes de impuestos / ingresos LTM 12,6%.",
    g25="6%: crecimiento nominal de Brasil con banca y crédito en expansión.",
    mt="14%: ROAE objetivo de ~16% con fondeo de depósitos.",
    s2c1="1,4x: ingresos por real de patrimonio (2025: R$20.411M / R$14.640M).",
    s2c2="1,4x.",
)

MULTIPLOS_EVALUACION = (
    "Evaluación PAGS (financiera): solo pesan P/E (35%), P/FCFE (20%) y P/OCF (5%) junto al DCF (40%); los múltiplos "
    "de EV no aplican a un banco. El flujo operativo de un banco incluye movimientos de depósitos y cartera (2024: "
    "-R$3.416M; 2025: +R$7.562M), así que P/OCF y P/FCFE son ruidosos. Se activó el override manual del bloque Base "
    "(columna J) = múltiplo LTM vivo (P/E ~6x), coherente con cómo el mercado valora hoy a las adquirentes brasileñas. OJO: P/FCFE da US$2,2-2,7 y se ordena al revés "
    "(Conservador > Optimista) porque el FCFE proyectado descuenta capex y capital de trabajo que en un banco son "
    "cartera; leerlo como no significativo (pesa 20% en el ponderado y lo sesga a la baja)."
)

TESIS = dict(
    historia=("PagSeguro nació como la adquirente de los microcomercios brasileños y se transformó en PagBank, un banco "
              "digital que capta depósitos, presta y procesa pagos. La adquirencia enfrenta tasas de descuento en caída "
              "por la competencia y por el PIX, pero el banco reduce el costo de fondeo y el crédito agrega ingresos. El "
              "resultado es una empresa que gana ~R$2.100M por año, con ROAE de ~15-16%, Basilea holgado y una política "
              "explícita de dividendos (R$1.000M/año en 2027-2028) y recompras. La tesis Base asume crecimiento de un "
              "dígito medio y margen antes de impuestos de 14%; el Conservador asume que la erosión de la adquirencia "
              "domina (2%) y el margen cae a 11% por morosidad."),
    bull_bear=[
        ("P/E ~6x y P/VL ~0,9x con ROAE de 15,6%.",
         "Ingresos por transacciones en caída (R$9.183M en 2024 a R$8.159M en 2025)."),
        ("Dividendos de R$1.000M/año comprometidos para 2027-2028 y recompras.",
         "Competencia de Nubank, Mercado Pago, Stone y del PIX."),
        ("Depósitos de R$28.428M abaratan el fondeo.",
         "Riesgo de crédito en expansión y tasas altas en Brasil."),
        ("Basilea 22,5%: capital para crecer y distribuir.",
         "Riesgo cambiario del real y salida del fundador de la presidencia del Directorio."),
    ],
    j_g1="Base 5% (US$); Conservador 2%; Optimista 9% (crédito y banca aceleran).",
    j_g25="Base 6%: crecimiento nominal de Brasil.",
    j_m1="Utilidad antes de impuestos / ingresos LTM (tratamiento de banco).",
    j_mt="Base 14%; Conservador 11% (morosidad); Optimista 16%.",
    j_s2c="1,4x: ingresos / patrimonio regulatorio.",
    j_wacc="Costo del capital propio (sin deuda financiera): beta 1,3, ERP de Brasil 7,47%, UST 10 años; WACC terminal 12%.",
    j_mbase="Utilidad antes de impuestos / ingresos LTM (US$).",
    nota_multiplos="Múltiplos anclados al LTM (override); los de EV no pesan en la categoría 'Financiera'.",
    conclusion=("El mercado valora a PagBank por debajo de su patrimonio: el caso Base solo exige que mantenga el ROAE "
                "y el crecimiento nominal."),
    monitor=("Variables a monitorear: TPV y tasa de descuento, crecimiento de depósitos y costo de fondeo, morosidad y "
             "pérdidas crediticias, índice de Basilea, cumplimiento de la meta de dividendos y ritmo de recompras."),
)
