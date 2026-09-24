#!/usr/bin/env python
"""Valoracion de Novo Nordisk A/S (NYSE: NVO) sobre una copia de la plantilla
maestra, con el mismo proceso que NKE/PYPL (scripts/model_steps.py).

Particularidades de Novo que este script resuelve:
  - Emisor extranjero (20-F, IFRS, DKK): el loader SEC del repo solo lee
    us-gaap, asi que la serie anual se arma aca desde el namespace
    'ifrs-full' de companyfacts (FY2019-FY2025; antes de 2019 no hay XBRL).
  - Moneda: el libro trabaja en US$ (precio del ADR NVO, 1 ADR = 1 accion B,
    UST como tasa libre de riesgo). Todo el historico se convierte al MISMO
    tipo de cambio spot (DKK/USD del dia de valoracion) -- conserva
    crecimientos y margenes tal como se reportan en DKK.
  - LTM a jun-2026 = FY2025 + H1 2026 - H1 2025 (6-K del 4-ago-2026; H1 no
    tiene XBRL).
  - Base normalizada (Input!B12/B13): "adjusted" de la propia empresa --
    excluye la reversion NO recurrente y sin caja de la provision 340B
    (DKK 26.760M en Q1 2026) y los deterioros de pipeline de Q2 2026
    (DKK 6.328M, monlunabant y otros).
  - Split 2:1 de sep-2023: acciones 2019-2020 duplicadas.
  - Prestamos ('Borrowings') ya incluyen arrendamientos (IFRS 16) -> B18=No.

Pasos: refresh | assumptions | content  (--step all corre todos)
Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts python scripts/run_nvo.py --step all
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

SHEET_ID = "1_w85o-Cv_4GzFB4nq5fGqrMSVoYf-Ltafuol3ir5TMw"
TICKER = "NVO"
COMPANY = "Novo Nordisk A/S"
INDUSTRY = "Drugs (Pharmaceutical)"
# Grupo de pares que la propia Novo uso en el Capital Markets Day (21-sep-2026).
PEER_TICKERS = ["LLY", "AZN", "NVS", "SNY", "MRK", "AMGN"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "nvo_formula_backup.json"
VALUATION_DATE = date(2026, 9, 23)

DKK_PER_USD = 6.5297       # cierre DKK=X 23-sep-2026 (yfinance)
UST_10Y = 0.0511           # ^TNX 23-sep-2026
MATURE_ERP = 0.0409        # Damodaran, 1-sep-2026 (mismo dato que NKE)
FY = [str(y) for y in range(2019, 2026)]

# Acciones A+B en circulacion (sin tesoreria) al 3-ago-2026: 4.465M emitidas
# - 44,25M en tesoreria (6-K H1 2026, "2026 share repurchase programme").
SHARES_OUT_M = 4465.0 - 44.249480

# --- H1 2026 / H1 2025 (6-K 4-ago-2026, Appendix 1-3), DKK millones ---
H1_26 = dict(revenue=175_311, cogs=30_698, sga=27_074 + 2_449, rd=28_071, ebit=86_679,
             pretax=89_047, tax=19_501, ni=69_546, ocf=79_283, capex=23_986, div=35_312,
             buyback=5_899, icf=-24_476, fcf_fin=-36_565, interest=2_759, fin_income=7_367,
             da_ex_imp=3_536 + (10_304 - 6_328), sbc=443)
H1_25 = dict(revenue=154_944, cogs=25_736, sga=32_425 + 2_536, rd=21_998, ebit=72_240,
             pretax=70_838, tax=15_301, ni=55_537, ocf=66_504, capex=28_083, div=35_100,
             buyback=1_388, icf=-20_097, fcf_fin=-42_731, interest=1_952, fin_income=8_739,
             sbc=None)
# One-offs para la base "adjusted" (definicion de la empresa, Appendix 7).
REVERSAL_340B_Q1_26 = 26_760
IMPAIRMENT_Q2_26 = 6_328

# Balance al 30-jun-2026 (Appendix 3), DKK millones.
BAL_JUN26 = dict(cash=44_482, sti=500, receivables=88_949, current_assets=208_696, ppe=231_758,
                 intangibles=102_167, goodwill=19_890, lt_investments=2_123 + 207, total_assets=594_941,
                 payables=14_591, current_debt=18_333, current_liabilities=239_083, lt_debt=121_794,
                 total_liabilities=373_664, equity=221_277, retained=224_164, other_reserves=-3_329)


def usd(dkk_m: float) -> float:
    """DKK millones -> US$ crudos (AnnualSeries espera $ crudos, ver refresh_native_model._M)."""
    return dkk_m / DKK_PER_USD * 1e6


# ---------------------------------------------------------------------------
# Serie anual desde ifrs-full (companyfacts)
# ---------------------------------------------------------------------------

def _facts() -> dict:
    return SecEdgarClient().company_facts(TICKER)["facts"]["ifrs-full"]


def _annual(ifrs: dict, tag: str, *, instant: bool = False, unit: str = "DKK") -> dict[str, float]:
    """{año: valor} de 20-F; si hay re-expresiones, gana la del 20-F mas nuevo."""
    rows = ifrs.get(tag, {}).get("units", {}).get(unit, [])
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


def _series(ifrs: dict, tag: str, **kw) -> list[float]:
    d = _annual(ifrs, tag, **kw)
    return [d.get(y, 0.0) / 1e6 for y in FY]  # DKK millones


def build_series(ifrs: dict) -> tuple[AnnualSeries, dict]:
    s = {k: _series(ifrs, t) for k, t in {
        "revenue": "Revenue", "ebit": "ProfitLossFromOperatingActivities", "cogs": "CostOfSales",
        "rd": "ResearchAndDevelopmentExpense", "admin": "AdministrativeExpense",
        "pretax": "ProfitLossBeforeTax", "tax": "IncomeTaxExpenseContinuingOperations", "ni": "ProfitLoss",
        "ocf": "CashFlowsFromUsedInOperatingActivities",
        "capex": "PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities",
        "div": "DividendsPaidClassifiedAsFinancingActivities", "buyback": "PaymentsToAcquireOrRedeemEntitysShares",
        "icf": "CashFlowsFromUsedInInvestingActivities", "fin": "CashFlowsFromUsedInFinancingActivities",
        "interest": "InterestExpense", "sbc": "AdjustmentsForSharebasedPayments",
        "da_imp": "AdjustmentsForDepreciationAndAmortisationExpenseAndImpairmentLossReversalOfImpairmentLossRecognisedInProfitOrLoss",
        "imp": "ImpairmentLossRecognisedInProfitOrLossIntangibleAssetsOtherThanGoodwill",
        "acq": "CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities",
    }.items()}
    b = {k: _series(ifrs, t, instant=True) for k, t in {
        "cash": "CashAndCashEquivalents", "sti": "CurrentFinancialAssetsAtFairValueThroughProfitOrLoss",
        "borrow": "Borrowings", "st_borrow": "ShorttermBorrowings", "lt_borrow": "LongtermBorrowings",
        "assets": "Assets", "liab": "Liabilities", "equity": "Equity", "ca": "CurrentAssets",
        "cl": "CurrentLiabilities", "recv": "CurrentTradeReceivables", "ppe": "PropertyPlantAndEquipmentIncludingRightofuseAssets",
        "intang": "IntangibleAssetsOtherThanGoodwill", "gw": "Goodwill", "ap": "TradeAndOtherCurrentPayablesToTradeSuppliers",
        "ofa": "OtherNoncurrentFinancialAssets", "assoc": "InvestmentsInAssociatesAccountedForUsingEquityMethod",
        "retained": "RetainedEarnings", "reserves": "OtherReserves",
    }.items()}
    sh_out = _series(ifrs, "NumberOfSharesOutstanding", instant=True, unit="shares")
    dil = _series(ifrs, "AdjustedWeightedAverageShares", unit="shares")
    basic = _series(ifrs, "WeightedAverageShares", unit="shares")
    # Split 2:1 (sep-2023): los 20-F de 2019-2020 no fueron re-expresados.
    for arr in (sh_out, dil, basic):
        for i, y in enumerate(FY):
            if y in ("2019", "2020") and arr[i] and arr[i] < 3_000:
                arr[i] *= 2
    # 2019 no tiene el desglose corto/largo plazo de deuda: todo a largo plazo.
    b["lt_borrow"] = [lt or (tot - st) for lt, st, tot in zip(b["lt_borrow"], b["st_borrow"], b["borrow"])]
    # D&A sin deterioros: DepreciationAndAmortisationExpense desde 2022; antes,
    # D&A+deterioros menos el deterioro de intangibles (el de PP&E no esta taggeado).
    da_tag = _annual(ifrs, "DepreciationAndAmortisationExpense")
    da = [da_tag[y] / 1e6 if y in da_tag else di - im for y, di, im in zip(FY, s["da_imp"], s["imp"])]
    # Tags que cambiaron de nombre entre 20-F.
    ppe_old = _series(ifrs, "PropertyPlantAndEquipment", instant=True)
    b["ppe"] = [n or o for n, o in zip(b["ppe"], ppe_old)]
    afs = _series(ifrs, "FinancialAssetsAvailableforsale", instant=True)
    b["sti"] = [n or o for n, o in zip(b["sti"], afs)]
    # Gastos de venta y distribucion no estan taggeados: = bruto - I+D - admin - otros - EBIT.
    other_op = _series(ifrs, "OtherOperatingIncomeExpense")
    selling = [r - c - rd - ad + oo - e for r, c, rd, ad, oo, e in
               zip(s["revenue"], s["cogs"], s["rd"], s["admin"], other_op, s["ebit"])]
    sga = [sl + ad for sl, ad in zip(selling, s["admin"])]

    def ltm(key: str, fy_last: float) -> float:
        return fy_last + H1_26[key] - H1_25[key]

    fy25 = {k: v[-1] for k, v in s.items()}
    ltm_vals = dict(
        revenue=ltm("revenue", fy25["revenue"]), cogs=ltm("cogs", fy25["cogs"]), rd=ltm("rd", fy25["rd"]),
        sga=ltm("sga", sga[-1]), ebit=ltm("ebit", fy25["ebit"]), pretax=ltm("pretax", fy25["pretax"]),
        tax=ltm("tax", fy25["tax"]), ni=ltm("ni", fy25["ni"]), ocf=ltm("ocf", fy25["ocf"]),
        capex=ltm("capex", fy25["capex"]), div=ltm("div", fy25["div"]), buyback=ltm("buyback", fy25["buyback"]),
        icf=ltm("icf", fy25["icf"]), fin=fy25["fin"] + H1_26["fcf_fin"] - H1_25["fcf_fin"],
        interest=ltm("interest", fy25["interest"]),
        # D&A sin deterioros: H1 2026 de los trimestrales (Q2 menos el deterioro
        # de DKK 6.328M); H1 2025 aproximado como la mitad del FY2025.
        da=da[-1] + H1_26["da_ex_imp"] - da[-1] / 2,
        sbc=fy25["sbc"],
    )

    series = AnnualSeries(
        ticker=TICKER, company_name=COMPANY, fiscal_year_ends=[f"{y}-12-31" for y in FY],
        revenue=[usd(v) for v in s["revenue"]], ebit=[usd(v) for v in s["ebit"]], da=[usd(v) for v in da],
        shares_outstanding=sh_out and [v * 1e6 for v in sh_out],
        long_term_debt=[usd(v) for v in b["lt_borrow"]], current_debt=[usd(v) for v in b["st_borrow"]],
        cash=[usd(v) for v in b["cash"]],
        ltm_revenue=usd(ltm_vals["revenue"]), ltm_ebit=usd(ltm_vals["ebit"]), ltm_da=usd(ltm_vals["da"]),
        tax_expense=[usd(v) for v in s["tax"]], net_income=[usd(v) for v in s["ni"]],
        diluted_shares_avg=[v * 1e6 for v in dil], basic_shares_avg=[v * 1e6 for v in basic],
        operating_cash_flow=[usd(v) for v in s["ocf"]], capex=[usd(v) for v in s["capex"]],
        buybacks=[usd(v) for v in s["buyback"]], dividends_paid=[usd(v) for v in s["div"]],
        cogs=[usd(v) for v in s["cogs"]],
        current_assets=[usd(v) for v in b["ca"]], current_liabilities=[usd(v) for v in b["cl"]],
        ltm_tax_expense=usd(ltm_vals["tax"]), ltm_net_income=usd(ltm_vals["ni"]),
        ltm_diluted_shares_avg=4_436e6, ltm_basic_shares_avg=4_428e6,  # Q2 2026 (promedio del trimestre)
        ltm_operating_cash_flow=usd(ltm_vals["ocf"]), ltm_capex=usd(ltm_vals["capex"]),
        ltm_buybacks=usd(ltm_vals["buyback"]), ltm_dividends_paid=usd(ltm_vals["div"]),
        ltm_cogs=usd(ltm_vals["cogs"]),
        rd=[usd(v) for v in s["rd"]], sga=[usd(v) for v in sga], pretax_income=[usd(v) for v in s["pretax"]],
        total_assets=[usd(v) for v in b["assets"]], total_liabilities=[usd(v) for v in b["liab"]],
        equity=[usd(v) for v in b["equity"]], share_based_comp=[usd(v) for v in s["sbc"]],
        investing_cash_flow=[usd(v) for v in s["icf"]], financing_cash_flow=[usd(v) for v in s["fin"]],
        receivables=[usd(v) for v in b["recv"]], ppe_net=[usd(v) for v in b["ppe"]],
        goodwill=[usd(v) for v in b["gw"]], accounts_payable=[usd(v) for v in b["ap"]],
        retained_earnings=[usd(v) for v in b["retained"]], aoci=[usd(v) for v in b["reserves"]],
        intangibles_net=[usd(v) for v in b["intang"]],
        long_term_investments=[usd(o + a) for o, a in zip(b["ofa"], b["assoc"])],
        short_term_investments=[usd(v) for v in b["sti"]],
        ltm_rd=usd(ltm_vals["rd"]), ltm_sga=usd(ltm_vals["sga"]), ltm_pretax_income=usd(ltm_vals["pretax"]),
        ltm_share_based_comp=usd(ltm_vals["sbc"]), ltm_investing_cash_flow=usd(ltm_vals["icf"]),
        ltm_financing_cash_flow=usd(ltm_vals["fin"]),
        interest_expense=[usd(v) for v in s["interest"]], ltm_interest_expense=usd(ltm_vals["interest"]),
        business_acquisitions=[usd(v) for v in s["acq"]],
    )
    return series, {"fy": s, "bal": b, "ltm": ltm_vals, "da": da, "sga": sga}


def build_company_inputs(raw: dict, price: float) -> CompanyInputs:
    fy, bal, lt = raw["fy"], raw["bal"], raw["ltm"]
    m = lambda v: v / DKK_PER_USD  # noqa: E731  DKK millones -> US$ millones
    margins = [e / r for e, r in zip(fy["ebit"], fy["revenue"])]
    return CompanyInputs(
        ticker=TICKER, company_name=COMPANY, country_of_incorporation="Denmark",
        industry_us=INDUSTRY, industry_global=INDUSTRY,
        revenue_ltm=m(lt["revenue"]), revenue_prior_10k=m(fy["revenue"][-1]),
        years_since_last_10k=0.5, ebit_ltm=m(lt["ebit"]), ebit_prior_10k=m(fy["ebit"][-1]),
        interest_expense_ltm=m(lt["interest"]), interest_expense_prior_10k=m(fy["interest"][-1]),
        book_value_equity_ltm=m(BAL_JUN26["equity"]), book_value_equity_prior_10k=m(bal["equity"][-1]),
        book_value_debt_ltm=m(BAL_JUN26["current_debt"] + BAL_JUN26["lt_debt"]),
        book_value_debt_prior_10k=m(bal["borrow"][-1]),
        cash_ltm=m(BAL_JUN26["cash"]), cash_prior_10k=m(bal["cash"][-1]),
        cross_holdings_ltm=m(BAL_JUN26["lt_investments"]),
        shares_outstanding=SHARES_OUT_M, current_price=price,
        effective_tax_rate=lt["tax"] / lt["pretax"], marginal_tax_rate=0.22,
        capitalize_rd=True, has_operating_leases=False, has_employee_options=False,
        ebit_margin_ltm=lt["ebit"] / lt["revenue"], ebit_margin_avg_3y=sum(margins[-3:]) / 3,
        ebit_margin_avg_5y=sum(margins[-5:]) / 5, ebit_margin_avg_10y=sum(margins) / len(margins),
        riskfree_rate=UST_10Y, initial_cost_of_capital=0.09,
    )


def _balance_ltm_column(sh) -> None:
    """Columna L (LTM) de 'Balance Sheet' al 30-jun-2026 -- refresh_balance_sheet
    repite el cierre de FY2025 como LTM para los items de balance."""
    b = {k: round(v / DKK_PER_USD, 1) for k, v in BAL_JUN26.items()}
    other_ca = round(b["current_assets"] - b["cash"] - b["sti"] - b["receivables"], 1)
    other_lta = round(b["total_assets"] - b["current_assets"] - b["ppe"] - b["goodwill"] - b["lt_investments"]
                      - b["intangibles"], 1)
    other_cl = round(b["current_liabilities"] - b["payables"] - b["current_debt"], 1)
    lt_liab = round(b["total_liabilities"] - b["current_liabilities"], 1)
    rnm._apply(sh.worksheet("Balance Sheet"), [(c, [[v]]) for c, v in {
        "L3": b["cash"], "L4": b["sti"], "L5": round(b["cash"] + b["sti"], 1), "L6": b["receivables"],
        "L8": b["receivables"], "L9": other_ca, "L10": b["current_assets"], "L11": b["ppe"],
        "L12": b["intangibles"], "L13": b["goodwill"], "L14": b["lt_investments"], "L15": other_lta,
        "L16": b["total_assets"], "L18": b["payables"], "L20": b["current_debt"], "L21": 0,
        "L23": other_cl, "L24": b["current_liabilities"], "L25": b["lt_debt"], "L26": 0,
        "L27": round(lt_liab - b["lt_debt"], 1), "L28": lt_liab, "L29": b["total_liabilities"],
        "L32": b["other_reserves"], "L33": b["retained"], "L34": b["equity"], "L35": b["equity"],
        "L36": b["total_assets"],
    }.items()])


def step_refresh() -> None:
    ifrs = _facts()
    series, raw = build_series(ifrs)
    market_raw = get_market_snapshot(TICKER)
    market = replace(market_raw, shares_outstanding=SHARES_OUT_M * 1e6,
                     market_cap=SHARES_OUT_M * 1e6 * market_raw.current_price, exchange="NYSE")
    ci = build_company_inputs(raw, market.current_price)
    sh = ms.open_sheet(SHEET_ID)

    print("[1/5] Input sheet + estados financieros (US$ al spot DKK/USD %.4f)..." % DKK_PER_USD)
    rnm.refresh_input_sheet(sh, TICKER, ci, INDUSTRY, INDUSTRY, market)
    rnm.refresh_income_statement(sh, series, ci)
    rnm.refresh_cash_flow_statement(sh, series)
    rnm.refresh_balance_sheet(sh, series, ci)
    _balance_ltm_column(sh)
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
    print("[5/5] listo:", sh.url)


def _fx(dkk_m: float) -> str:
    """DKK millones -> literal US$ millones para formulas (coma decimal, locale del libro)."""
    return f"{dkk_m / DKK_PER_USD:.1f}".replace(".", ",")


def _fix_sector_own_row(sh) -> None:
    """yfinance mezcla EV/precio en US$ con EBITDA/OCF en DKK para NVO (daba
    EV/EBITDA 1,5x y P/OCF 1,3x). Se recalculan los multiplos de la fila
    propia con las cifras LTM del libro (ya en US$)."""
    rnm._apply(sh.worksheet("Sector"), [("E2:J2", [[
        11.29,  # Forward P/E de yfinance (precio y EPS estimado ambos en US$)
        "='Trailing Valuation'!L13",
        "=('Input sheet'!B22*'Input sheet'!B23+'Input sheet'!B16-'Input sheet'!B19)/'Cash Flow Statement'!L36",
        "='Input sheet'!B22*'Input sheet'!B23/'Cash Flow Statement'!L36",
        "=('Input sheet'!B22*'Input sheet'!B23+'Input sheet'!B16-'Input sheet'!B19)/'Income Statement'!L28",
        "='Input sheet'!B22*'Input sheet'!B23/'Cash Flow Statement'!L13",
    ]])])


def step_assumptions() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.fix_template_bugs(sh, bk)
    ms.fix_nwc_projection(sh, bk)
    _fix_sector_own_row(sh)

    ms.write_with_backup(sh, "Input sheet", {
        "B4": ms.serial(VALUATION_DATE),
        # Base normalizada = "adjusted" de Novo: sin la reversion 340B (Q1 2026,
        # no recurrente y sin caja) y sin los deterioros de pipeline de Q2 2026.
        "B12": f"='Income Statement'!L3-{_fx(REVERSAL_340B_Q1_26)}",
        "B13": f"='Income Statement'!L12-{_fx(REVERSAL_340B_Q1_26)}+{_fx(IMPAIRMENT_Q2_26)}",
        "B17": "Yes",      # I+D capitalizado (farma: ~17% de ventas)
        "B18": "No",       # 'Borrowings' ya incluye arrendamientos IFRS 16
        "B25": 0.22,       # tasa corporativa de Dinamarca
        "B27": -0.03,      # Año 1 (jul-26/jun-27): guia 2026 0% a -6% CER (~-1pp FX) y recorte de WAC en EE.UU. desde ene-2027
        "B28": "='Valuation output'!B6-0,015",  # mismo basis ajustado por I+D; 2S26 con mas I+D/promocion (guia) y precios mas bajos en 2027
        "B29": 0.045,      # CMD 21-sep-2026: CAGR 2026-30 "en linea con pares" (~5-6%), con descuento por erosion de semaglutida
        "B30": 0.40,       # margen LP (basis ajustado por I+D): premium sobre big pharma madura tras la expiracion de semaglutida (2031-32)
        "B31": 7,          # convergencia hacia 2032-33 (patente de semaglutida en EE.UU.)
        "B32": 0.7,        # marginal 2020-25: +DKK 182 mil M de ventas con +~DKK 250 mil M de capital (capex pico)
        "B33": 1.1,        # capex en baja segun la empresa; ~promedio de la industria (1,07)
        "B35": UST_10Y,
        "B68": "Yes", "B69": 0.035,  # g perpetuo 3,5% < rf 5,1%: cliff de patentes de GLP-1 despues de 2032
    }, "Supuestos NVO (ver hoja Tesis de Inversión y Supuestos)", bk)

    ms.write_with_backup(sh, "R& D converter", {
        "F7": 5,           # vida util de 5 años (hay 7 años de I+D en XBRL)
        "F8": f"='Income Statement'!L10-{_fx(IMPAIRMENT_Q2_26)}",  # I+D LTM sin el deterioro (ya sumado en B13)
        "B15": "='Income Statement'!H10", "B16": "='Income Statement'!G10",
    }, "I+D NVO: 5 años de amortizacion, LTM sin deterioros", bk)

    ms.write_with_backup(sh, "Country equity risk premiums", {
        "B2": MATURE_ERP, "C2": "Updated September 1, 2026",
    }, "ERP de mercado maduro (Damodaran, 1-sep-2026)", bk)

    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Single Business(Global)",  # beta desapalancada global de Drugs (Pharmaceutical) = 1,00
        "B33": 7,                          # vencimiento promedio de los bonos EUR/USD/DKK
        "B34": "Actual rating",
        "B36": "Aa2/AA",                   # S&P AA (may-2025) / Moody's Aa3 (ene-2025)
    }, "Cost of capital NVO", bk)

    ms.write_with_backup(sh, "Valuation output", {
        # Conservador: margen de big pharma madura (NVS/AMGN ~35% GAAP) en el basis ajustado.
        "C45": 0.35,
        # Optimista: el margen "ampliamente estable" del CMD se sostiene (~basis actual).
        "C47": "='Input sheet'!B30+0,05",
        # Conservador: piso de la guia 2026 (-6% CER, -1pp FX = -7%) y luego +1%
        # anual (erosion de semaglutida + perdida de cuota frente a Lilly).
        "C55": "='Input sheet'!B27-0,04", "D55": 0.01,
        # Optimista: techo de la guia (0% CER, -1pp FX) y luego ~7% (pares con
        # Lilly; CagriSema, Wegovy pill/HD y zenagamtide cumplen).
        "C106": "='Input sheet'!B27+0,02", "D106": 0.07,
    }, "Escenarios NVO: orden Conservador < Base < Optimista", bk)

    # Bug #14 (plantilla): 'Financials Multiples' proyecta el EBIT contable con
    # el margen de 'Valuation output', que con B17="Yes" esta en el basis
    # AJUSTADO por I+D capitalizado (~5,6pp mas alto para NVO). Eso inflaba la
    # utilidad neta, el EBITDA y el OCF proyectados -- y por ende los precios
    # de P/E, EV/EBITDA, P/OCF y P/FCFE. Se resta el ajuste de I+D como % de
    # ventas para volver al basis contable (sin efecto si B17="No").
    rd_adj = "IF('Input sheet'!$B$17=\"Yes\";'R& D converter'!$D$40/'Input sheet'!$B$12;0)"
    fm_updates = {}
    for row, vo_row in ((8, 57), (47, 6), (87, 108)):
        for c, vo_col in zip("EFGH", "CDEF"):
            fm_updates[f"{c}{row}"] = (f'=IFERROR(IF({chr(ord(c) + 5)}{row}<>"";{chr(ord(c) + 5)}{row};'
                                       f"'Valuation output'!{vo_col}{vo_row}-{rd_adj});\"\")")
    ms.write_with_backup(sh, "Financials Multiples", fm_updates,
                         "Bug #14: margen proyectado en basis contable (sin el ajuste de I+D capitalizado)", bk)

    # Dividendos: la hoja venia vacia -> DPS proyectado = 0 en los 5 multiplos.
    # Dividendos pagados (caja) / acciones promedio, en US$ al mismo spot.
    raw = build_series(_facts())[1]
    fy, ltm_v = raw["fy"], raw["ltm"]
    ni = fy["ni"] + [ltm_v["ni"]]
    div = fy["div"] + [ltm_v["div"]]
    shares = [4757.4, 4680.0, 4606.2, 4544.6, 4494.8, 4463.0, 4447.7, 4436.0]
    pad = ["", "", ""]
    rnm._apply(sh.worksheet("Dividendos"), [
        ("B2:L2", [pad + [round(d / DKK_PER_USD, 1) for d in div]]),
        ("B4:L4", [pad + [round(d / DKK_PER_USD / s, 3) for d, s in zip(div, shares)]]),
        ("B5:L5", [pad + [round(d / n, 4) for d, n in zip(div, ni)]]),
        ("L3", [["=L4/'Input sheet'!B23"]]),
    ])

    # Paso 6: EV/FCFF historico (29,8x) refleja un FCFF deprimido por el capex
    # record (17% de ventas vs D&A 4,5%) y la burbuja 2022-24 -> se usa el
    # multiplo IMPLICITO del DCF de cada escenario (EV DCF / FCFF FY+1).
    ms.write_with_backup(sh, "EVFCFF", {
        "J8": "='Valuation output'!B77/'Financials Multiples'!E24",
        "J19": "='Valuation output'!B26/'Financials Multiples'!E63",
        "J30": "='Valuation output'!B128/'Financials Multiples'!E103",
    }, "EV/FCFF objetivo implicito del DCF (FCFF deprimido por capex record)", bk)

    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": "Madura"}, "Tipo de empresa NVO", bk)
    market = get_market_snapshot(TICKER)
    try:
        rnm.refresh_resumen_valoracion(sh, TICKER, market)
    except Exception:  # yfinance devuelve NaN para el cierre del 23-sep (aun sin consolidar)
        # Cierre real del 23-sep-2026: US$38,17 (-3,12% vs 39,40 del 22-sep).
        rnm._apply(sh.worksheet("Resumen de Valoración"), [("C25", [[round(market.current_price, 2)]])])


def _fix_errors(sh, bk) -> None:
    """Paso 8: errores reales (no de Industry Averages, que son preexistentes)."""
    ms.write_with_backup(sh, "Income Statement", {f"{c}30": f'=IFERROR({c}28/{c}3;"")' for c in "BCD"},
                         "#DIV/0! del margen EBITDA en años sin dato (B-D)", bk)
    ms.write_with_backup(sh, "Valuation output", {
        "B52": "=IFERROR(('Income Statement'!K3/'Income Statement'!B3)^(1/10)-1;\"\")",
    }, "#DIV/0! del CAGR 10Y (historico de 7 años)", bk)


def step_content() -> None:
    import nvo_content as nc

    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    _fix_errors(sh, bk)
    ms.write_with_backup(sh, "Cualitativo", nc.CUALITATIVO, "Contenido cualitativo NVO", bk)
    ms.write_with_backup(sh, "Estadísticas", nc.ESTADISTICAS, "Estadisticas NVO (formulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", nc.STORIES, "Historia NVO", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", nc.SUPUESTOS_RECOMENDADOS, "Recomendaciones NVO", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": nc.MULTIPLOS_EVALUACION}, "Evaluacion de multiplos NVO", bk)
    nc.format_estadisticas(sh)
    nc.write_tesis(sh, bk)


STEPS = {"refresh": step_refresh, "assumptions": step_assumptions, "content": step_content}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--step", choices=[*STEPS, "all", "dry"], default="all")
    args = parser.parse_args(argv)
    if args.step == "dry":
        series, raw = build_series(_facts())
        for k in ("revenue", "ebit", "rd", "ni", "ocf", "capex", "interest", "da_imp", "imp"):
            print(k, [round(v) for v in raw["fy"][k]])
        print("da", [round(v) for v in raw["da"]], "sga", [round(v) for v in raw["sga"]])
        for k, v in raw["bal"].items():
            print(k, [round(x) for x in v])
        print("shares", [round(x / 1e6) for x in series.shares_outstanding], [round(x / 1e6) for x in series.diluted_shares_avg])
        print("LTM", {k: round(v) for k, v in raw["ltm"].items()})
        return 0
    for name, fn in STEPS.items():
        if args.step in (name, "all"):
            fn()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
