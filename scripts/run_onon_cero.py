#!/usr/bin/env python
"""Valoración de On Holding AG (ONON) DESDE CERO sobre una copia nueva de la plantilla maestra (2-oct-2026), con el
prompt de valoración v4 y el de research v5. Reemplaza a la valoración anterior (hoja
17E_Rd-MD-u5i8Vez7sYwcWIdVYvDdjNhOu-6NWAzGnQ, que queda sin cambios como referencia).

Particularidades de On que este script resuelve (mismo enfoque que scripts/run_afya.py):
  - Emisor extranjero (20-F y 6-K, NIIF, francos suizos): el loader SEC del repo solo lee us-gaap, así que la serie anual
    se arma acá desde 'ifrs-full' de companyfacts (FY2021-FY2025; On salió a bolsa en septiembre de 2021).
  - Moneda: el libro trabaja en US$ (precio en la NYSE, UST como tasa libre de riesgo). Cada año se convierte a SU tipo de
    cambio (yfinance CHFUSD=X): flujos al promedio del año, saldos al cierre. LTM (jul-2025 a jun-2026) al promedio de esos
    doce meses y balance al cierre del 30-jun-2026.
  - LTM = FY2025 − 1S25 + 1S26 (6-K del 11-ago-2026).
  - NIIF 16: los arrendamientos ya están en el balance y el resultado operativo ya excluye su interés; la deuda del modelo
    son los pasivos por arrendamiento (B18 = No). No hay deuda bancaria.
  - Acciones: Clase A + Clase B / 10 (la Clase B tiene una décima parte de los derechos económicos; su BPA es 1/10 del de
    la Clase A).
  - Flujo operativo del libro = flujo operativo NIIF − intereses pagados (como en AFYA, para que P/OCF y P/FCFE midan caja
    del accionista); el pago de capital de arrendamientos queda en financiamiento.

Pasos: refresh | assumptions | supuestos | presentacion | content
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import replace
from datetime import date
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402
import refresh_native_model as rnm  # noqa: E402

from jmr_valuation.io.inputs import CompanyInputs  # noqa: E402
from jmr_valuation.io.sec_edgar_client import SecEdgarClient  # noqa: E402
from jmr_valuation.io.sec_edgar_loader import AnnualSeries  # noqa: E402
from jmr_valuation.io.yfinance_client import get_market_snapshot  # noqa: E402

SHEET_ID = "1nlN8qDy9BipM5IWwGE5Fgf6VKpyYQScLXIPvqtAE9Oo"
TICKER = "ONON"
COMPANY = "On Holding AG"
INDUSTRY = "Shoe"  # Damodaran: NKE, DECK, ONON, CROX, BIRK
PEER_TICKERS = ["DECK", "NKE", "LULU", "BIRK", "ADDYY", "CROX"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "onon_desde_cero_2026-10-02.json"
FY = [str(y) for y in range(2021, 2026)]

# US$ por franco suizo (yfinance CHFUSD=X): promedio del año (flujos) y cierre (saldos).
FX_AVG = {"2021": 1.0942, "2022": 1.0481, "2023": 1.1134, "2024": 1.1367, "2025": 1.2065}
FX_YE = {"2021": 1.0945, "2022": 1.0836, "2023": 1.1857, "2024": 1.1071, "2025": 1.2631}
FX_LTM_AVG = 1.2608            # promedio jul-2025 a jun-2026
FX_JUN26 = 1.2382              # cierre del 30-jun-2026

# Acciones económicas al cierre (millones) = Clase A en circulación (portada del 20-F) + Clase B / 10.
SHARES_YE = [276.864 + 34.5, 281.976 + 34.5, 284.215 + 34.5, 289.296 + 34.5, 296.873 + 34.124]
# 30-jun-2026 (nota 4.5 del 6-K): 301.715.535 Clase A + 324.991.680 Clase B / 10 + premios con efecto dilutivo
# (1.644.629 Clase A + 2.493.692 Clase B / 10).
SHARES_OUT_M = 301.715535 + 32.499168 + 1.644629 + 0.249369

# --- 1S26 / 1S25 (6-K del 11-ago-2026), CHF millones ---
H1_26 = dict(revenue=1682.2, cogs=592.2, sga=853.2, ebit=236.9, pretax=241.8, tax=33.5, ni=208.3, da=72.1, sbc=30.9,
             ocf_rep=255.0, int_paid=12.5, capex=41.9 + 5.3, icf=-47.2, fcf_fin=-43.3, fin_exp=16.3, fin_inc=18.3,
             buyback=0.1)
H1_25 = dict(revenue=1475.8, cogs=579.7, sga=726.3, ebit=169.8, pretax=16.6, tax=0.8, ni=15.8, da=60.7, sbc=25.2,
             ocf_rep=89.1, int_paid=9.9, capex=27.3 + 2.2, icf=-29.4, fcf_fin=-37.0, fin_exp=13.6, fin_inc=14.8,
             buyback=0.1)

# Balance al 30-jun-2026 (6-K del 11-ago-2026), CHF millones.
BAL_JUN26 = dict(cash=1205.6, receivables=374.0, inventories=472.9, other_ca=78.1 + 162.4, current_assets=2293.0,
                 ppe=175.5, rou=530.7, intangibles=55.8, dta=187.8, total_assets=3242.9, payables=211.0,
                 lease_c=87.9, other_cl=46.3 + 371.3 + 12.0 + 81.4, current_liabilities=810.0, lease_nc=474.6,
                 other_ncl=8.1 + 27.6 + 5.6 + 5.5, noncurrent_liabilities=521.5, equity=1911.4, retained=590.9,
                 capital_reserves=1324.7, other_reserves=-12.0)


def _facts() -> dict:
    return SecEdgarClient().company_facts(TICKER)["facts"]["ifrs-full"]


def _annual(ifrs: dict, tag: str, *, instant: bool = False) -> dict[str, float]:
    rows = ifrs.get(tag, {}).get("units", {}).get("CHF", [])
    out: dict[str, tuple[str, float]] = {}
    for r in rows:
        if r.get("form") != "20-F" or not r["end"].endswith("-12-31"):
            continue
        if not instant and not (r.get("start", "").endswith("-01-01") and r["start"][:4] == r["end"][:4]):
            continue
        y = r["end"][:4]
        if y not in out or r["filed"] > out[y][0]:
            out[y] = (r["filed"], r["val"])
    return {y: v for y, (_, v) in out.items()}


def _series(ifrs: dict, tag: str, *, signed: bool = False, **kw) -> list[float]:
    d = _annual(ifrs, tag, **kw)
    return [(d.get(y, 0.0) if signed else abs(d.get(y, 0.0))) / 1e6 for y in FY]


def build_raw(ifrs: dict) -> dict:
    g = lambda tag, **kw: _series(ifrs, tag, **kw)  # noqa: E731
    s = dict(
        revenue=g("RevenueFromContractsWithCustomers"), cogs=g("CostOfSales"), sga=g("SellingGeneralAndAdministrativeExpense"),
        ebit=g("ProfitLossFromOperatingActivities", signed=True), pretax=g("ProfitLossBeforeTax", signed=True),
        tax=g("IncomeTaxExpenseContinuingOperations", signed=True), ni=g("ProfitLossAttributableToOwnersOfParent", signed=True),
        da=g("AdjustmentsForDepreciationAndAmortisationExpense"), sbc=g("AdjustmentsForSharebasedPayments"),
        ocf_rep=g("CashFlowsFromUsedInOperatingActivities", signed=True), fin_exp=g("FinanceCosts"), fin_inc=g("FinanceIncome"),
        capex=[a + b for a, b in zip(g("PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"),
                                     g("PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities"))],
        icf=g("CashFlowsFromUsedInInvestingActivities", signed=True), fcf_fin=g("CashFlowsFromUsedInFinancingActivities", signed=True),
        int_paid=g("InterestPaidClassifiedAsFinancingActivities"), buyback=g("PurchaseOfTreasuryShares"),
    )
    if not any(s["revenue"]):
        gp = g("GrossProfit")
        s["revenue"] = [a + b for a, b in zip(gp, s["cogs"])]
    s["ocf"] = [o - i for o, i in zip(s["ocf_rep"], s["int_paid"])]
    b = {k: g(t, instant=True, signed=True) for k, t in dict(
        cash="CashAndCashEquivalents", recv="CurrentTradeReceivables", inv="Inventories", ca="CurrentAssets",
        cl="CurrentLiabilities", assets="Assets", equity="Equity", ppe="PropertyPlantAndEquipment", rou="RightofuseAssets",
        intang="IntangibleAssetsAndGoodwill", ap="TradeAndOtherCurrentPayablesToTradeSuppliers", retained="RetainedEarnings",
        lease_c="CurrentLeaseLiabilities", lease_nc="NoncurrentLeaseLiabilities", lease_t="LeaseLiabilities",
        apic="CapitalReserve",
    ).items()}
    # 2021: el XBRL no trae los pasivos por arrendamiento -> aproximación por el activo por derecho de uso (177,9)
    b["lease_nc"] = [nc if nc else (t - c if t else rou) for nc, t, c, rou in zip(b["lease_nc"], b["lease_t"], b["lease_c"], b["rou"])]
    b["liab"] = [a - e for a, e in zip(b["assets"], b["equity"])]
    ltm = {k: s[k][-1] - H1_25[k] + H1_26[k] for k in H1_26}
    ltm["ocf"] = ltm["ocf_rep"] - ltm["int_paid"]
    return {"fy": s, "bal": b, "ltm": ltm}


def build_series(raw: dict) -> AnnualSeries:
    s, b, lt = raw["fy"], raw["bal"], raw["ltm"]
    fl = lambda k: [v * FX_AVG[y] * 1e6 for y, v in zip(FY, s[k])]  # noqa: E731
    bl = lambda k: [v * FX_YE[y] * 1e6 for y, v in zip(FY, b[k])]  # noqa: E731
    L = lambda k: lt[k] * FX_LTM_AVG * 1e6  # noqa: E731
    econ_w = [n / e if e else 0 for n, e in zip(s["ni"], [0, 0.21, 0.25, 0.75, 0.62])]  # NI / BPA Clase A
    sh_avg = [SHARES_YE[0]] + [w for w in econ_w[1:]]
    return AnnualSeries(
        ticker=TICKER, company_name=COMPANY, fiscal_year_ends=[f"{y}-12-31" for y in FY],
        revenue=fl("revenue"), ebit=fl("ebit"), da=fl("da"),
        shares_outstanding=[v * 1e6 for v in SHARES_YE],
        long_term_debt=[0.0] * len(FY), current_debt=bl("lease_c"),
        cash=bl("cash"), lease_liability_noncurrent=bl("lease_nc"),
        ltm_revenue=L("revenue"), ltm_ebit=L("ebit"), ltm_da=L("da"),
        tax_expense=fl("tax"), net_income=fl("ni"),
        diluted_shares_avg=[v * 1e6 for v in sh_avg], basic_shares_avg=[v * 1e6 for v in sh_avg],
        operating_cash_flow=fl("ocf"), capex=fl("capex"), buybacks=fl("buyback"), dividends_paid=[0.0] * len(FY),
        cogs=fl("cogs"), current_assets=bl("ca"), current_liabilities=bl("cl"),
        ltm_tax_expense=L("tax"), ltm_net_income=L("ni"),
        ltm_diluted_shares_avg=(298.951784 + 33.8278973 + 2.97) * 1e6, ltm_basic_shares_avg=(298.951784 + 33.8278973) * 1e6,
        ltm_operating_cash_flow=L("ocf"), ltm_capex=L("capex"), ltm_buybacks=L("buyback"), ltm_dividends_paid=0.0,
        ltm_cogs=L("cogs"), rd=[0.0] * len(FY), sga=fl("sga"), pretax_income=fl("pretax"),
        total_assets=bl("assets"), total_liabilities=bl("liab"), equity=bl("equity"),
        share_based_comp=fl("sbc"), investing_cash_flow=fl("icf"), financing_cash_flow=fl("fcf_fin"),
        receivables=bl("recv"), ppe_net=bl("ppe"), goodwill=[0.0] * len(FY), accounts_payable=bl("ap"),
        retained_earnings=bl("retained"), apic=bl("apic"), intangibles_net=bl("intang"),
        long_term_investments=[0.0] * len(FY), short_term_investments=[0.0] * len(FY),
        ltm_rd=0.0, ltm_sga=L("sga"), ltm_pretax_income=L("pretax"), ltm_share_based_comp=L("sbc"),
        ltm_investing_cash_flow=L("icf"), ltm_financing_cash_flow=L("fcf_fin"),
        interest_expense=fl("fin_exp"), ltm_interest_expense=L("fin_exp"),
        interest_investment_income=fl("fin_inc"), ltm_interest_investment_income=L("fin_inc"),
    )


def build_company_inputs(raw: dict, price: float) -> CompanyInputs:
    s, b, lt = raw["fy"], raw["bal"], raw["ltm"]
    j = BAL_JUN26
    margins = [e / r for e, r in zip(s["ebit"], s["revenue"])]
    return CompanyInputs(
        ticker=TICKER, company_name=COMPANY, country_of_incorporation="Switzerland",
        industry_us=INDUSTRY, industry_global=INDUSTRY,
        revenue_ltm=lt["revenue"] * FX_LTM_AVG, revenue_prior_10k=s["revenue"][-1] * FX_AVG["2025"],
        years_since_last_10k=0.5, ebit_ltm=lt["ebit"] * FX_LTM_AVG, ebit_prior_10k=s["ebit"][-1] * FX_AVG["2025"],
        interest_expense_ltm=lt["fin_exp"] * FX_LTM_AVG, interest_expense_prior_10k=s["fin_exp"][-1] * FX_AVG["2025"],
        book_value_equity_ltm=j["equity"] * FX_JUN26, book_value_equity_prior_10k=b["equity"][-1] * FX_YE["2025"],
        book_value_debt_ltm=(j["lease_c"] + j["lease_nc"]) * FX_JUN26,
        book_value_debt_prior_10k=(b["lease_c"][-1] + b["lease_nc"][-1]) * FX_YE["2025"],
        cash_ltm=j["cash"] * FX_JUN26, cash_prior_10k=b["cash"][-1] * FX_YE["2025"],
        shares_outstanding=SHARES_OUT_M, current_price=price,
        effective_tax_rate=0.20, marginal_tax_rate=0.20,
        capitalize_rd=False, has_operating_leases=False, has_employee_options=False,
        ebit_margin_ltm=lt["ebit"] / lt["revenue"], ebit_margin_avg_3y=sum(margins[-3:]) / 3,
        ebit_margin_avg_5y=sum(margins[-5:]) / 5, ebit_margin_avg_10y=sum(margins) / len(margins),
        riskfree_rate=0.0524, initial_cost_of_capital=0.10,
    )


def _balance_ltm_column(sh) -> None:
    """Columna L (LTM) de 'Balance Sheet' al 30-jun-2026 (CHF -> US$ al cierre de junio)."""
    b = {k: round(v * FX_JUN26, 1) for k, v in BAL_JUN26.items()}
    other_ca = round(b["current_assets"] - b["cash"] - b["receivables"], 1)
    other_lta = round(b["total_assets"] - b["current_assets"] - b["ppe"] - b["intangibles"], 1)
    lt_liab = b["noncurrent_liabilities"]
    tl = round(b["current_liabilities"] + lt_liab, 1)
    rnm._apply(sh.worksheet("Balance Sheet"), [(c, [[v]]) for c, v in {
        "L3": b["cash"], "L4": 0, "L5": b["cash"], "L6": b["receivables"], "L8": b["receivables"], "L9": other_ca,
        "L10": b["current_assets"], "L11": b["ppe"], "L12": b["intangibles"], "L13": 0, "L14": 0,
        "L15": other_lta, "L16": b["total_assets"], "L18": b["payables"], "L20": 0, "L21": b["lease_c"],
        "L22": 0, "L23": round(b["current_liabilities"] - b["payables"] - b["lease_c"], 1), "L24": b["current_liabilities"],
        "L25": 0, "L26": b["lease_nc"], "L27": round(lt_liab - b["lease_nc"], 1), "L28": lt_liab, "L29": tl,
        "L31": b["capital_reserves"], "L32": b["other_reserves"], "L33": b["retained"], "L34": b["equity"],
        "L35": b["equity"], "L36": b["total_assets"],
    }.items()])


def _balance_history_fixes(sh, raw: dict) -> None:
    """Porción corriente de arrendamientos (fila 21) por año: el pipeline no la trae de 'ifrs-full'."""
    cols = "GHIJK"  # FY2021..FY2025
    rnm._apply(sh.worksheet("Balance Sheet"),
               [(f"{c}21", [[round(v * FX_YE[y], 1)]]) for c, y, v in zip(cols, FY, raw["bal"]["lease_c"])])


def _fix_sector_own_row(sh) -> None:
    """yfinance mezcla precio en US$ con estados en CHF para ONON: los múltiplos de la fila propia se recalculan con las
    cifras LTM del libro (en US$)."""
    rnm._apply(sh.worksheet("Sector"), [("E2:K2", [[
        "", "='Trailing Valuation'!L13",
        "=('Input sheet'!B22*'Input sheet'!B23+'Input sheet'!B16-'Input sheet'!B19)/'Cash Flow Statement'!L36",
        "='Input sheet'!B22*'Input sheet'!B23/'Cash Flow Statement'!L36",
        "=('Input sheet'!B22*'Input sheet'!B23+'Input sheet'!B16-'Input sheet'!B19)/'Income Statement'!L28",
        "='Input sheet'!B22*'Input sheet'!B23/'Cash Flow Statement'!L13",
        "='Income Statement'!L13",
    ]])])


def dry() -> None:
    raw = build_raw(_facts())
    for k in ("revenue", "cogs", "sga", "ebit", "da", "pretax", "tax", "ni", "ocf_rep", "int_paid", "ocf", "capex", "fin_exp",
              "buyback"):
        print(f"{k:9s}", [round(v, 1) for v in raw["fy"][k]], "LTM", round(raw["ltm"].get(k, 0), 1))
    for k, v in raw["bal"].items():
        print(f"{k:10s}", [round(x, 1) for x in v])


def step_refresh() -> None:
    raw = build_raw(_facts())
    series = build_series(raw)
    market_raw = get_market_snapshot(TICKER)
    market = replace(market_raw, shares_outstanding=SHARES_OUT_M * 1e6,
                     market_cap=SHARES_OUT_M * 1e6 * market_raw.current_price, exchange="NYSE")
    ci = build_company_inputs(raw, market.current_price)
    sh = ms.open_sheet(SHEET_ID)
    print("[1/5] Input sheet + estados (US$ al tipo de cambio de cada período)...")
    rnm.refresh_input_sheet(sh, TICKER, ci, INDUSTRY, INDUSTRY, market)
    rnm.refresh_income_statement(sh, series, ci)
    rnm.refresh_cash_flow_statement(sh, series)
    rnm.refresh_balance_sheet(sh, series, ci)
    _balance_ltm_column(sh)
    _balance_history_fixes(sh, raw)
    print("[2/5] Encabezados, Trailing/Forward Valuation...")
    rnm.refresh_period_headers(sh, series)
    computed = rnm.refresh_trailing_valuation(sh, series, ci)
    rnm.refresh_forward_valuation(sh, series, computed)
    print("[3/5] Hojas de ratios...")
    rnm.refresh_eficiencia_capital(sh)
    rnm.refresh_margenes(sh)
    rnm.refresh_salud_financiera(sh)
    rnm.refresh_por_accion(sh)
    print("[4/5] Sector...")
    rnm.refresh_sector(sh, TICKER, PEER_TICKERS)
    _fix_sector_own_row(sh)
    print("[5/5] listo:", sh.url)


VALUATION_DATE = date(2026, 10, 1)
PRICE_1001 = 30.20          # cierre del 1-oct-2026 (NYSE)
RF_1001 = 0.0524            # UST 10 años, cierre del 1-oct-2026
ERP_SEP26 = 0.0409          # Damodaran, 1-sep-2026


def step_assumptions() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.fix_template_bugs(sh, bk)
    ms.fix_nwc_projection(sh, bk)
    raw = build_raw(_facts())
    s, lt = raw["fy"], raw["ltm"]
    cols = "GHIJK"
    upd = {f"{c}15": round(v * FX_AVG[y], 1) for c, y, v in zip(cols, FY, s["fin_exp"])}
    upd["L15"] = round(lt["fin_exp"] * FX_LTM_AVG, 1)
    ms.write_with_backup(sh, "Income Statement", upd,
                         "Gasto financiero bruto en positivo (el pipeline lo restaba dos veces en la fila 16)", bk)
    ms.write_with_backup(sh, "Balance Sheet", {f"{c}20": 0 for c in cols},
                         "Sin deuda bancaria: el pipeline duplicaba los arrendamientos corrientes en la fila 20", bk)
    ms.write_with_backup(sh, "Input sheet", {
        "B4": ms.serial(VALUATION_DATE),
        "D1": PRICE_1001,
        "B14": "='Income Statement'!L15", "C14": "='Income Statement'!K15",
        "B17": "No",      # On no capitaliza I+D en el modelo: inmaterial frente a las ventas
        "B18": "No",      # NIIF 16: los arrendamientos ya están en el balance (B16) y el resultado operativo excluye su interés
        "B24": 0.20,      # tasa efectiva normalizada (LTM 7,9% por reconocimiento de impuestos diferidos; Suiza ~19,6%)
        "B25": 0.23,      # marginal: mezcla de Suiza, EE.UU. (55% de las ventas) y el resto
        "B35": RF_1001,
    }, "Datos base ONON desde cero (20-F 2025, 6-K del 1S26)", bk)
    ms.write_with_backup(sh, "Country equity risk premiums", {
        "B2": ERP_SEP26, "C2": "Damodaran, implied ERP September 1, 2026",
    }, "ERP de mercado maduro (Damodaran, 1-sep-2026)", bk)
    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Direct Input",
        "B23": 1.30,      # entre la bottom-up de Shoe reapalancada (~0,95) y la regresión (1,58 a 2 años; 1,80 desde la salida a bolsa)
        "B26": "Will Input",
        "B27": ERP_SEP26,
        "B33": 5,
        "B34": "Direct Input",
        "B35": 0.06,      # sin deuda bancaria: tasa de los arrendamientos en US$ ≈ UST + ~0,8 pp
    }, "Costo de capital ONON: beta 1,30, ERP sep-2026, Kd de arrendamientos", bk)
    ms.write_with_backup(sh, "Valuation output", {
        "B33": "=B31-B32-N('Input sheet'!$B$76)",
        "B84": "=B82-B83-N('Input sheet'!$B$76)",
        "B135": "=B133-B134-N('Input sheet'!$B$76)",
    }, "Fórmula estándar con preferentes (B76 vacío en ONON)", bk)


def step_supuestos() -> None:
    """Supuestos del caso Base de la hoja = historia Base; las cuatro historias están en reference/damodaran/ONONN.json."""
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Input sheet", {
        "B27": 0.175,   # año 1 de la historia Base: guía 2026 (moneda constante de ~20%) con mayoristas contenidos y DTC +30%
        "B28": 0.14,    # margen operativo NIIF del 1S26 (14,1%); guía de EBITDA ajustado 19,5-20% menos D&A y pagos en acciones
        "B29": 0.14,    # CAGR años 2-5 de la historia Base (mayoristas ~9%, DTC 14-24%)
        "B30": 0.165,   # meta de EBITDA ajustado ≥ 22% en 2029 menos D&A (~4,5%) y pagos en acciones (~2%), con algo más de escala
        "B31": 5,
        "B32": 2.3,     # rotación propia ~2,6 (con arrendamientos) e industria Shoe 2,1
        "B33": 2.1,
        "B49": "No",    # sin ventaja defendible (marca de 16 años): ROIC terminal = costo de capital
    }, "Supuestos Base ONON desde cero = historia Base (ver reference/damodaran/ONONN.json)", BACKUP_PATH)
    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": "Crecimiento"}, "Tipo de empresa ONON", BACKUP_PATH)
    rnm.refresh_resumen_valoracion(sh, TICKER, rnm.get_market_snapshot(TICKER))


def step_presentacion() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Descuento de múltiplos", {
        "A38": "DCF activo hoy · escenarios de las historias",
        "C38": "='Escenarios e historias'!H6", "D38": "='Escenarios e historias'!H5", "E38": "='Escenarios e historias'!H8",
        "A43": "Precio con MOS sobre el valor esperado", "C43": "", "D43": "='Escenarios e historias'!H14", "E43": "",
    }, "DCF activo = historias; MOS sobre el esperado (presentación vigente 1-oct-2026)", BACKUP_PATH)


def step_content() -> None:
    import onon_cero_content as oc

    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", oc.CUALITATIVO, "Contenido cualitativo ONON desde cero", bk)
    ms.write_with_backup(sh, "Estadísticas", oc.ESTADISTICAS, "Estadísticas ONON (fórmulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", oc.STORIES, "Historia ONON", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", oc.SUPUESTOS_RECOMENDADOS, "Recomendaciones ONON", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": oc.MULTIPLOS_EVALUACION}, "Evaluación de múltiplos ONON", bk)
    oc.format_estadisticas(sh)
    oc.write_tesis(sh, bk)  # después hay que volver a correr apply_multiples_v3 --apply (agrega el origen de los múltiplos)


STEPS = {"refresh": step_refresh, "assumptions": step_assumptions, "supuestos": step_supuestos,
         "presentacion": step_presentacion, "content": step_content}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--step", choices=[*STEPS, "all", "dry"], default="dry")
    args = parser.parse_args(argv)
    if args.step == "dry":
        dry()
        return 0
    for name, fn in STEPS.items():
        if args.step in (name, "all"):
            fn()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
