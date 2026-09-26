#!/usr/bin/env python
"""Valoracion de Afya Limited (Nasdaq: AFYA) en la hoja 'Modelo JMR - AFYA'
(Drive: Análisis > AFYA), con el mismo proceso que NVO/ADSK
(scripts/model_steps.py) sobre la plantilla maestra auditada.

Particularidades de Afya que este script resuelve:
  - La hoja existente era una copia de la valoracion de LULU. El paso
    'reset' guarda su contenido (reference/backups/afya_pre_reset.json.gz)
    y copia encima el contenido de la plantilla maestra ya auditada.
  - Emisor extranjero (20-F, IFRS, R$): el loader SEC del repo solo lee
    us-gaap, asi que la serie anual se arma aca desde 'ifrs-full' de
    companyfacts (FY2019-FY2025; la empresa salio a bolsa en jul-2019) y
    las lineas mal taggeadas salen de los estados del 20-F 2025.
  - Moneda: el libro trabaja en US$ (precio en Nasdaq, UST como tasa libre
    de riesgo). A diferencia de NVO, el real se movio mucho (3,94 a 6,18
    por dolar), asi que cada año se convierte a SU tipo de cambio: flujos al
    promedio del año, saldos al cierre. Asi los multiplos historicos son los
    que pago de verdad un inversor en dolares.
  - LTM a jun-2026 = FY2025 + H1 2026 - H1 2025 (6-K del 13-ago-2026).
  - Flujo operativo: Afya clasifica los intereses pagados (deuda, pagos a
    vendedores de empresas compradas y arrendamientos) en financiamiento o
    inversion. Para que P/OCF y P/FCFE midan caja del accionista, el OCF
    del libro = OCF reportado - intereses pagados.
  - Deuda = prestamos + cuentas por pagar a vendedores (deuda de
    adquisiciones, la empresa la incluye en su deuda neta) + arrendamientos
    IFRS 16 (B18 = No: ya estan en el balance).
  - Fusion con Yduqs (acuerdo vinculante del 23-sep-2026): se valora el
    negocio standalone y la Tesis compara contra el valor de la relacion de
    canje (6,408347 acciones YDUQ3 por accion de Afya).

Pasos: reset | refresh | assumptions | content  (--step all corre todos)
Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts python scripts/run_afya.py --step all
"""
from __future__ import annotations

import argparse
import gzip
import json
import sys
import time
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

SHEET_ID = "1_CXhy_5n-V4rwfOSl8xI8455hywS5W92VBed_FCylvQ"   # Análisis/AFYA/Modelo JMR - AFYA
MASTER_ID = "19PRUFiYsNavUcN6WwHBVlp-VRMozp3rNSE2R1zt7N-g"  # plantilla maestra (auditada 26-sep-2026)
TICKER = "AFYA"
COMPANY = "Afya Limited"
INDUSTRY = "Education"  # Damodaran indname.xls (ene-2026)
# Educacion superior en Brasil (B3) + Laureate (LatAm). Yduqs es ademas la contraparte de la fusion.
PEER_TICKERS = ["YDUQ3.SA", "COGN3.SA", "SEER3.SA", "CSED3.SA", "ANIM3.SA", "LAUR"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "afya_formula_backup.json"
RESET_BACKUP = _ROOT / "reference" / "backups" / "afya_pre_reset.json.gz"
VALUATION_DATE = date(2026, 9, 25)
PRICE_AT_ANALYSIS = 13.00      # cierre AFYA del 25-sep-2026 (Nasdaq, yfinance)

UST_10Y = 0.0518               # ^TNX 25-sep-2026
MATURE_ERP = 0.0409            # Damodaran, 1-sep-2026 (mismo dato que NKE/NVO)
FY = [str(y) for y in range(2019, 2026)]

# R$ por US$ (yfinance BRL=X): promedio del año (flujos) y cierre (saldos).
FX_AVG = {"2019": 3.9415, "2020": 5.1485, "2021": 5.3939, "2022": 5.1620, "2023": 4.9942, "2024": 5.3826, "2025": 5.5878}
FX_YE = {"2019": 4.0157, "2020": 5.1908, "2021": 5.5702, "2022": 5.2846, "2023": 4.8502, "2024": 6.1779, "2025": 5.4762}
FX_LTM_AVG = 5.2915            # promedio jul-2025 a jun-2026
FX_JUN26 = 5.1818              # cierre del 30-jun-2026

# Acciones en circulacion al cierre (millones) = emitidas - tesoreria (20-F / notas).
SHARES_YE = [89.7, 93.1, 92.0, 89.9, 89.9, 90.3, 89.9]
# 30-jun-2026: 93.722.831 emitidas - 5.244.615 en tesoreria (nota 14 del 6-K) + 0,44M de
# dilucion de opciones/RSU (nota 15, Q2 2026).
SHARES_OUT_M = (93_722_831 - 5_244_615 + 442_124) / 1e6

# --- H1 2026 / H1 2025 (6-K del 13-ago-2026), R$ millones ---
H1_26 = dict(revenue=1984.809, cogs=688.036, sga=574.000, ebit=691.462, pretax=507.495, tax=44.438, ni=454.137,
             ni_total=463.057, da=183.645, sbc=19.241, ocf=797.839, capex=41.003 + 78.960, acq=81.675,
             int_paid=178.721 + 0 + 64.366, div=314.882, buyback=133.011, fin_exp=287.663, fin_inc=94.374,
             debt_in=0.0, debt_out=5.254, icf=-200.760, fcf=-713.605)
H1_25 = dict(revenue=1855.760, cogs=625.346, sga=541.318, ebit=657.755, pretax=475.828, tax=42.250, ni=424.331,
             ni_total=433.578, da=186.453, sbc=12.520, ocf=771.596, capex=81.617 + 103.455, acq=81.463,
             int_paid=110.399 + 14.536 + 58.793, div=138.479, buyback=0.0, fin_exp=274.281, fin_inc=84.478,
             debt_in=0.0, debt_out=1.543, icf=-272.268, fcf=-309.187)

# Balance al 30-jun-2026 (6-K 13-ago-2026), R$ millones.
BAL_JUN26 = dict(cash=1006.490, receivables=819.716, current_assets=1950.191, ppe=701.624, intangibles=5575.840,
                 associate=54.962, total_assets=9326.633, payables=145.985,
                 loans_c=126.364, sellers_c=55.780, lease_c=57.630, current_liabilities=885.868,
                 loans_nc=1921.531, sellers_nc=296.768, lease_nc=1012.662, total_liabilities=4397.813,
                 equity=4928.820, nci=40.234, retained=2781.312, apic=2295.632)

# Lineas que el XBRL no trae limpias (20-F 2025 / 2023 y tags alternativos), R$ millones.
INTANGIBLE_CAPEX = {"2023": 126.993, "2024": 255.691, "2025": 197.997}
# Intereses pagados (deuda + vendedores + arrendamientos). 2023-2025: estado de flujos
# del 20-F 2025. 2021-2022: tag InterestPaidClassifiedAsFinancingActivities (incluye
# arrendamientos; no incluye los pocos intereses clasificados en inversion). 2019-2020:
# no hay tag -> gasto financiero devengado como aproximacion.
INTEREST_PAID = {"2019": 72.4, "2020": 98.3, "2021": 118.0, "2022": 201.6,
                 "2023": 175.889 + 71.518 + 103.911, "2024": 177.192 + 78.931 + 111.605,
                 "2025": 309.337 + 14.536 + 121.475}
# Recompras (caja). 2021-2022 por variacion de la reserva de acciones en tesoreria.
BUYBACKS = {"2019": 0.0, "2020": 0.0, "2021": 152.6, "2022": 152.3, "2023": 12.369, "2024": 0.0, "2025": 77.002}
DEBT_PROCEEDS = {"2019": 7.4, "2020": 0.0, "2021": 809.5, "2022": 496.9, "2023": 5.288, "2024": 491.593, "2025": 1494.881}
DEBT_REPAID = {"2019": 75.1, "2020": 155.1, "2021": 107.8, "2022": 1.8, "2023": 112.630, "2024": 128.696, "2025": 1624.911}

# Relacion de canje de la fusion con Yduqs (6-K del 23-sep-2026).
EXCHANGE_RATIO = 6.408347


def usd_flow(y: str, brl_m: float) -> float:
    return brl_m / FX_AVG[y] * 1e6


def usd_bal(y: str, brl_m: float) -> float:
    return brl_m / FX_YE[y] * 1e6


# ---------------------------------------------------------------------------
# Serie anual desde ifrs-full (companyfacts)
# ---------------------------------------------------------------------------

def _facts() -> dict:
    return SecEdgarClient().company_facts(TICKER)["facts"]["ifrs-full"]


def _annual(ifrs: dict, tag: str, *, instant: bool = False, unit: str = "BRL") -> dict[str, float]:
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
    return [abs(d.get(y, 0.0)) / 1e6 for y in FY]  # R$ millones (algunos años vienen con signo invertido)


def build_raw(ifrs: dict) -> dict:
    g = lambda tag, **kw: _series(ifrs, tag, **kw)  # noqa: E731
    s = dict(
        revenue=g("Revenue"), cogs=g("CostOfSales"), sga=g("GeneralAndAdministrativeExpense"),
        ebit=g("ProfitLossFromOperatingActivities"), pretax=g("ProfitLossBeforeTax"),
        ni_total=g("ProfitLoss"), ni=g("ProfitLossAttributableToOwnersOfParent"),
        da=g("AdjustmentsForDepreciationAndAmortisationExpense"), sbc=g("AdjustmentsForSharebasedPayments"),
        ocf_rep=g("CashFlowsFromUsedInOperatingActivities"), fin_exp=g("FinanceCosts"), fin_inc=g("FinanceIncome"),
        capex_ppe=g("PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities"),
        capex_int=g("PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities"),
        acq=g("PurchaseOfOtherLongtermAssetsClassifiedAsInvestingActivities"),
        div=g("DividendsPaidClassifiedAsFinancingActivities"),
        icf=[-v for v in g("CashFlowsFromUsedInInvestingActivities")],
    )
    fin = _annual(ifrs, "CashFlowsFromUsedInFinancingActivities")
    s["fcf_fin"] = [fin.get(y, 0.0) / 1e6 for y in FY]
    s["tax"] = [p - n for p, n in zip(s["pretax"], s["ni_total"])]  # 2025 no trae el tag de impuesto total
    s["capex_int"] = [INTANGIBLE_CAPEX.get(y, v) for y, v in zip(FY, s["capex_int"])]
    s["capex"] = [a + b for a, b in zip(s["capex_ppe"], s["capex_int"])]
    s["int_paid"] = [INTEREST_PAID[y] for y in FY]
    s["ocf"] = [o - i for o, i in zip(s["ocf_rep"], s["int_paid"])]
    s["buyback"] = [BUYBACKS[y] for y in FY]
    b = {k: g(t, instant=True) for k, t in dict(
        cash="CashAndCashEquivalents", loans_c="ShorttermBorrowings", loans_nc="LongtermBorrowings",
        sellers_c="TradeAndOtherCurrentPayablesToRelatedParties", sellers_nc="NoncurrentPayablesToRelatedParties",
        lease_c="CurrentLeaseLiabilities", lease_nc="NoncurrentLeaseLiabilities",
        ca="CurrentAssets", cl="CurrentLiabilities", assets="Assets", liab="Liabilities", equity="Equity",
        recv="CurrentTradeReceivables", ppe="PropertyPlantAndEquipment", intang="IntangibleAssetsOtherThanGoodwill",
        ap="TradeAndOtherCurrentPayables", retained="RetainedEarnings", apic="AdditionalPaidinCapital",
        assoc="InvestmentsInSubsidiariesJointVenturesAndAssociates",
    ).items()}
    ltm = {k: s[k][-1] - H1_25[k] + H1_26[k] for k in
           ("revenue", "cogs", "sga", "ebit", "pretax", "tax", "ni", "ni_total", "da", "sbc", "capex", "acq",
            "int_paid", "div", "buyback", "fin_exp", "fin_inc", "icf")}
    ltm["ocf_rep"] = s["ocf_rep"][-1] - H1_25["ocf"] + H1_26["ocf"]
    ltm["ocf"] = ltm["ocf_rep"] - ltm["int_paid"]
    ltm["fcf_fin"] = s["fcf_fin"][-1] - H1_25["fcf"] + H1_26["fcf"]
    return {"fy": s, "bal": b, "ltm": ltm}


def build_series(raw: dict) -> AnnualSeries:
    s, b, lt = raw["fy"], raw["bal"], raw["ltm"]
    fl = lambda k: [usd_flow(y, v) for y, v in zip(FY, s[k])]  # noqa: E731
    bl = lambda k: [usd_bal(y, v) for y, v in zip(FY, b[k])]  # noqa: E731
    L = lambda k: lt[k] / FX_LTM_AVG * 1e6  # noqa: E731
    cur_debt = [c + v for c, v in zip(b["loans_c"], b["sellers_c"])]
    lt_debt = [c + v for c, v in zip(b["loans_nc"], b["sellers_nc"])]
    return AnnualSeries(
        ticker=TICKER, company_name=COMPANY, fiscal_year_ends=[f"{y}-12-31" for y in FY],
        revenue=fl("revenue"), ebit=fl("ebit"), da=fl("da"),
        shares_outstanding=[v * 1e6 for v in SHARES_YE],
        long_term_debt=[usd_bal(y, v) for y, v in zip(FY, lt_debt)],
        current_debt=[usd_bal(y, v) for y, v in zip(FY, cur_debt)],
        cash=bl("cash"), lease_liability_noncurrent=bl("lease_nc"),
        ltm_revenue=L("revenue"), ltm_ebit=L("ebit"), ltm_da=L("da"),
        tax_expense=fl("tax"), net_income=fl("ni"),
        diluted_shares_avg=[v * 1e6 for v in _series(_FACTS_CACHE, "AdjustedWeightedAverageShares", unit="shares")],
        basic_shares_avg=[v * 1e6 for v in _series(_FACTS_CACHE, "WeightedAverageShares", unit="shares")],
        operating_cash_flow=fl("ocf"), capex=fl("capex"), buybacks=fl("buyback"), dividends_paid=fl("div"),
        cogs=fl("cogs"), current_assets=bl("ca"), current_liabilities=bl("cl"),
        ltm_tax_expense=L("tax"), ltm_net_income=L("ni"),
        ltm_diluted_shares_avg=89.673e6, ltm_basic_shares_avg=89.113e6,  # H1 2026 (nota 15)
        ltm_operating_cash_flow=L("ocf"), ltm_capex=L("capex"), ltm_buybacks=L("buyback"),
        ltm_dividends_paid=L("div"), ltm_cogs=L("cogs"),
        rd=[0.0] * len(FY), sga=fl("sga"), pretax_income=fl("pretax"),
        total_assets=bl("assets"), total_liabilities=bl("liab"), equity=bl("equity"),
        share_based_comp=fl("sbc"), investing_cash_flow=fl("icf"), financing_cash_flow=fl("fcf_fin"),
        receivables=bl("recv"), ppe_net=bl("ppe"), goodwill=[0.0] * len(FY), accounts_payable=bl("ap"),
        retained_earnings=bl("retained"), apic=bl("apic"), intangibles_net=bl("intang"),
        long_term_investments=bl("assoc"), short_term_investments=[0.0] * len(FY),
        ltm_rd=0.0, ltm_sga=L("sga"), ltm_pretax_income=L("pretax"), ltm_share_based_comp=L("sbc"),
        ltm_investing_cash_flow=L("icf"), ltm_financing_cash_flow=L("fcf_fin"),
        interest_expense=fl("fin_exp"), ltm_interest_expense=L("fin_exp"),
        interest_investment_income=fl("fin_inc"), ltm_interest_investment_income=L("fin_inc"),
        business_acquisitions=fl("acq"), ltm_business_acquisitions=L("acq"),
    )


_FACTS_CACHE: dict = {}


def build_company_inputs(raw: dict, price: float) -> CompanyInputs:
    s, b, lt = raw["fy"], raw["bal"], raw["ltm"]
    j = BAL_JUN26
    m_ltm = lambda v: v / FX_LTM_AVG  # noqa: E731
    m_jun = lambda v: v / FX_JUN26  # noqa: E731
    m_ye = lambda v: v / FX_YE["2025"]  # noqa: E731
    margins = [e / r for e, r in zip(s["ebit"], s["revenue"])]
    debt_jun = j["loans_c"] + j["loans_nc"] + j["sellers_c"] + j["sellers_nc"] + j["lease_c"] + j["lease_nc"]
    debt_ye = b["loans_c"][-1] + b["loans_nc"][-1] + b["sellers_c"][-1] + b["sellers_nc"][-1] + b["lease_c"][-1] + b["lease_nc"][-1]
    return CompanyInputs(
        ticker=TICKER, company_name=COMPANY, country_of_incorporation="Brazil",
        industry_us=INDUSTRY, industry_global=INDUSTRY,
        revenue_ltm=m_ltm(lt["revenue"]), revenue_prior_10k=s["revenue"][-1] / FX_AVG["2025"],
        years_since_last_10k=0.5, ebit_ltm=m_ltm(lt["ebit"]), ebit_prior_10k=s["ebit"][-1] / FX_AVG["2025"],
        interest_expense_ltm=m_ltm(lt["fin_exp"]), interest_expense_prior_10k=s["fin_exp"][-1] / FX_AVG["2025"],
        book_value_equity_ltm=m_jun(j["equity"]), book_value_equity_prior_10k=m_ye(b["equity"][-1]),
        book_value_debt_ltm=m_jun(debt_jun), book_value_debt_prior_10k=m_ye(debt_ye),
        cash_ltm=m_jun(j["cash"]), cash_prior_10k=m_ye(b["cash"][-1]),
        cross_holdings_ltm=m_jun(j["associate"]),
        shares_outstanding=SHARES_OUT_M, current_price=price,
        effective_tax_rate=lt["tax"] / lt["pretax"], marginal_tax_rate=0.15,
        capitalize_rd=False, has_operating_leases=False, has_employee_options=False,
        ebit_margin_ltm=lt["ebit"] / lt["revenue"], ebit_margin_avg_3y=sum(margins[-3:]) / 3,
        ebit_margin_avg_5y=sum(margins[-5:]) / 5, ebit_margin_avg_10y=sum(margins) / len(margins),
        riskfree_rate=UST_10Y, initial_cost_of_capital=0.12,
    )


# ---------------------------------------------------------------------------
# Pasos
# ---------------------------------------------------------------------------

def _retry(fn, tries=6):
    for i in range(tries):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001 (429 de la API de Sheets)
            if "429" not in str(exc) or i == tries - 1:
                raise
            time.sleep(30 * (i + 1))


def step_reset() -> None:
    """La hoja 'Modelo JMR - AFYA' era una copia de la valoracion de LULU.
    Se respalda su contenido y se reemplaza por el de la plantilla maestra
    (auditada), hoja por hoja (misma estructura: 44 hojas + Origen)."""
    sh = ms.open_sheet(SHEET_ID)
    master = ms.open_sheet(MASTER_ID)
    titles = [w.title for w in sh.worksheets()]
    m_titles = [w.title for w in master.worksheets()]
    rng = lambda ts: [f"'{t}'" for t in ts]  # noqa: E731
    if not RESET_BACKUP.exists():
        old = _retry(lambda: sh.values_batch_get(rng(titles), params={"valueRenderOption": "FORMULA"}))
        RESET_BACKUP.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(RESET_BACKUP, "wt", encoding="utf-8") as fh:
            json.dump({"title": sh.title, "sheets": {t: v.get("values", []) for t, v in zip(titles, old["valueRanges"])}}, fh,
                      ensure_ascii=False)
    new = _retry(lambda: master.values_batch_get(rng(m_titles), params={"valueRenderOption": "FORMULA"}))["valueRanges"]
    for t, v in zip(m_titles, new):
        if t not in titles:
            _retry(lambda: sh.add_worksheet(t, rows=200, cols=26))
    common = [t for t in m_titles]
    _retry(lambda: sh.values_batch_clear(body={"ranges": rng(common)}))
    data = [{"range": f"'{t}'!A1", "values": v.get("values", [])} for t, v in zip(m_titles, new) if v.get("values")]
    for i in range(0, len(data), 8):
        _retry(lambda: sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": data[i:i + 8]}))
    print("reset: contenido de la plantilla maestra copiado en", sh.title)


def _balance_ltm_column(sh) -> None:
    """Columna L (LTM) de 'Balance Sheet' al 30-jun-2026 (R$ -> US$ al cierre de jun)."""
    b = {k: round(v / FX_JUN26, 1) for k, v in BAL_JUN26.items()}
    other_ca = round(b["current_assets"] - b["cash"] - b["receivables"], 1)
    other_lta = round(b["total_assets"] - b["current_assets"] - b["ppe"] - b["intangibles"] - b["associate"], 1)
    st_debt = round(b["loans_c"] + b["sellers_c"], 1)
    lt_debt = round(b["loans_nc"] + b["sellers_nc"], 1)
    other_cl = round(b["current_liabilities"] - b["payables"] - st_debt - b["lease_c"], 1)
    lt_liab = round(b["total_liabilities"] - b["current_liabilities"], 1)
    rnm._apply(sh.worksheet("Balance Sheet"), [(c, [[v]]) for c, v in {
        "L3": b["cash"], "L4": 0, "L5": b["cash"], "L6": b["receivables"], "L8": b["receivables"], "L9": other_ca,
        "L10": b["current_assets"], "L11": b["ppe"], "L12": b["intangibles"], "L13": 0, "L14": b["associate"],
        "L15": other_lta, "L16": b["total_assets"], "L18": b["payables"], "L20": st_debt, "L21": b["lease_c"],
        "L22": 0, "L23": other_cl, "L24": b["current_liabilities"], "L25": lt_debt, "L26": b["lease_nc"],
        "L27": round(lt_liab - lt_debt - b["lease_nc"], 1), "L28": lt_liab, "L29": b["total_liabilities"],
        "L31": b["apic"], "L33": b["retained"], "L34": round(b["equity"] - b["nci"], 1), "L35": b["equity"],
        "L36": b["total_assets"],
    }.items()])


def _balance_history_fixes(sh, raw: dict) -> None:
    """Porcion corriente de arrendamientos (fila 21) y deuda neta emitida
    (Cash Flow fila 28) por año: el pipeline no las trae de 'ifrs-full'."""
    cols = "EFGHIJK"  # FY2019..FY2025 (7 años -> columnas E..K)
    lease_c = raw["bal"]["lease_c"]
    net_borrow = [DEBT_PROCEEDS[y] - DEBT_REPAID[y] for y in FY]
    ltm_nb = net_borrow[-1] - (H1_25["debt_in"] - H1_25["debt_out"]) + (H1_26["debt_in"] - H1_26["debt_out"])
    rnm._apply(sh.worksheet("Balance Sheet"), [(f"{c}21", [[round(v / FX_YE[y], 1)]]) for c, y, v in zip(cols, FY, lease_c)])
    rnm._apply(sh.worksheet("Cash Flow Statement"),
               [(f"{c}28", [[round(v / FX_AVG[y], 1)]]) for c, y, v in zip(cols, FY, net_borrow)]
               + [("L28", [[round(ltm_nb / FX_LTM_AVG, 1)]])])


def _fix_sector_own_row(sh) -> None:
    """yfinance mezcla precio en US$ con estados en R$ para AFYA: los
    multiplos de la fila propia se recalculan con las cifras LTM del libro."""
    rnm._apply(sh.worksheet("Sector"), [("E2:K2", [[
        "", "='Trailing Valuation'!L13",
        "=('Input sheet'!B22*'Input sheet'!B23+'Input sheet'!B16-'Input sheet'!B19)/'Cash Flow Statement'!L36",
        "='Input sheet'!B22*'Input sheet'!B23/'Cash Flow Statement'!L36",
        "=('Input sheet'!B22*'Input sheet'!B23+'Input sheet'!B16-'Input sheet'!B19)/'Income Statement'!L28",
        "='Input sheet'!B22*'Input sheet'!B23/'Cash Flow Statement'!L13",
        "='Income Statement'!L13",
    ]])])


def step_refresh() -> None:
    ifrs = _facts()
    _FACTS_CACHE.clear()
    _FACTS_CACHE.update(ifrs)
    raw = build_raw(ifrs)
    series = build_series(raw)
    market_raw = get_market_snapshot(TICKER)
    market = replace(market_raw, shares_outstanding=SHARES_OUT_M * 1e6,
                     market_cap=SHARES_OUT_M * 1e6 * market_raw.current_price, exchange="NASDAQ")
    ci = build_company_inputs(raw, market.current_price)
    sh = ms.open_sheet(SHEET_ID)
    print("[1/5] Input sheet + estados financieros (US$ al tipo de cambio de cada periodo)...")
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


def dry() -> None:
    ifrs = _facts()
    _FACTS_CACHE.update(ifrs)
    raw = build_raw(ifrs)
    for k in ("revenue", "cogs", "sga", "ebit", "da", "pretax", "tax", "ni", "ocf_rep", "int_paid", "ocf", "capex", "acq", "div", "fin_exp"):
        print(f"{k:9s}", [round(v, 1) for v in raw["fy"][k]], "LTM", round(raw["ltm"].get(k, 0), 1))
    for k, v in raw["bal"].items():
        print(f"{k:10s}", [round(x, 1) for x in v])
    s = build_series(raw)
    print("rev US$M", [round(v / 1e6) for v in s.revenue], round(s.ltm_revenue / 1e6))
    print("shares", SHARES_OUT_M, "EBIT margin LTM", round(raw["ltm"]["ebit"] / raw["ltm"]["revenue"], 4),
          "tax LTM", round(raw["ltm"]["tax"] / raw["ltm"]["pretax"], 4))


STEPS = {"reset": step_reset, "refresh": step_refresh}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--step", choices=[*STEPS, "all", "dry", "assumptions", "content"], default="dry")
    args = parser.parse_args(argv)
    if args.step == "dry":
        dry()
        return 0
    extra = {}
    try:
        import afya_steps  # supuestos y contenido (se agregan cuando esten listos)
        extra = {"assumptions": afya_steps.step_assumptions, "content": afya_steps.step_content}
    except ImportError:
        pass
    for name, fn in {**STEPS, **extra}.items():
        if args.step in (name, "all"):
            fn()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
