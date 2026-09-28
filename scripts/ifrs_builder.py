"""Arma AnnualSeries/CompanyInputs de un emisor extranjero (20-F, IFRS) a partir
de companyfacts 'ifrs-full' + la instancia XBRL del ultimo 6-K semestral, y
corre los mismos pasos refresh_* de refresh_native_model.py (como
run_afya.py y run_pfgruposura.py, pero generico para las posiciones IBKR).

Moneda: el libro trabaja en US$. Cada ejercicio se convierte a SU tipo de
cambio: flujos al promedio del año, saldos al cierre (yfinance). Asi los
multiplos historicos son los que pago un inversor en dolares.

LTM = ultimo ejercicio + semestre actual - mismo semestre del año anterior
(flujos); saldos al cierre del semestre."""
from __future__ import annotations

from dataclasses import replace
from datetime import date

import requests
from lxml import etree

import refresh_native_model as rnm
from jmr_valuation.io.inputs import CompanyInputs
from jmr_valuation.io.sec_edgar_client import SecEdgarClient
from jmr_valuation.io.sec_edgar_loader import AnnualSeries
from jmr_valuation.io.sheets_auth import get_gspread_client, open_target_sheet
from jmr_valuation.io.yfinance_client import get_market_snapshot

_NS = {"xbrli": "http://www.xbrl.org/2003/instance"}


def annual(ifrs: dict, tag: str | tuple[str, ...], unit: str, *, instant: bool = False) -> dict[str, float]:
    """{año: valor} de 20-F (ejercicio calendario); si hay re-expresiones gana el 20-F mas nuevo.
    `tag` puede ser una tupla de alternativas (se toma la primera que tenga dato por año)."""
    tags = (tag,) if isinstance(tag, str) else tag
    out: dict[str, tuple[str, float]] = {}
    for t in tags:
        found: dict[str, tuple[str, float]] = {}
        for r in ifrs.get(t, {}).get("units", {}).get(unit, []):
            if not r.get("form", "").startswith("20-F") or not r["end"].endswith("-12-31"):
                continue
            if not instant and not (r.get("start", "").endswith("-01-01") and r["start"][:4] == r["end"][:4]):
                continue
            y = r["end"][:4]
            if y not in found or r["filed"] > found[y][0]:
                found[y] = (r["filed"], r["val"])
        for y, v in found.items():
            out.setdefault(y, v)  # la primera alternativa con dato para ese año gana
    return {y: v for y, (_, v) in out.items()}


def instance_values(url: str, user_agent: str) -> dict[str, dict[tuple, float]]:
    x = etree.fromstring(requests.get(url, headers={"User-Agent": user_agent}, timeout=60).content)
    ctx = {}
    for c in x.findall(".//xbrli:context", _NS):
        if c.find(".//xbrli:segment", _NS) is not None:
            continue
        p = c.find("xbrli:period", _NS)
        s = p.findtext("xbrli:startDate", namespaces=_NS)
        e = p.findtext("xbrli:endDate", namespaces=_NS) or p.findtext("xbrli:instant", namespaces=_NS)
        ctx[c.get("id")] = (s, e)
    out: dict[str, dict[tuple, float]] = {}
    for el in x:
        if not isinstance(el.tag, str) or el.get("contextRef") not in ctx or el.text is None:
            continue
        try:
            v = float(el.text)
        except ValueError:
            continue
        out.setdefault(el.tag.split("}")[1], {})[ctx[el.get("contextRef")]] = v
    return out


class IfrsCompany:
    """cfg: dict con TICKER, COMPANY, YF_TICKER, UNIT (moneda), YEARS, FX_AVG, FX_YE, FX_LTM_AVG, FX_H1_END,
    H1 (url de la instancia del 6-K semestral o None), H1_END/H1_PREV (fechas ISO de cierre del semestre),
    TAGS (mapa campo -> tag o tupla de tags), SHARES_YE (millones por año), SHARES_LTM (millones),
    DILUTED_AVG (millones por año), COUNTRY, INDUSTRY, MARGINAL_TAX, OVERRIDES (campo -> {año: valor})."""

    def __init__(self, cfg: dict):
        self.c = cfg
        self.ifrs = SecEdgarClient().company_facts(cfg["FACTS_TICKER"])["facts"]["ifrs-full"]
        ua = SecEdgarClient().user_agent
        self.h1 = instance_values(cfg["H1"], ua) if cfg.get("H1") else {}

    # --- lectura -------------------------------------------------------------
    def fy(self, field: str, *, instant: bool = False, sign: float = 1.0) -> list[float]:
        tag = self.c["TAGS"].get(field)
        d = annual(self.ifrs, tag, self.c["UNIT"], instant=instant) if tag else {}
        d.update(self.c.get("OVERRIDES", {}).get(field, {}))
        return [sign * d.get(y, 0.0) for y in self.c["YEARS"]]

    def _h1(self, field: str, start: str, end: str) -> float | None:
        manual = self.c.get("H1_MANUAL", {}).get(field)
        if manual is not None:  # (semestre actual, mismo semestre del año anterior) en unidades crudas
            return manual[0] if start == self.c["H1_START"] else manual[1]
        tag = self.c["TAGS"].get(field)
        tags = (tag,) if isinstance(tag, str) else (tag or ())
        for t in tags:
            v = self.h1.get(t, {}).get((start, end))
            if v is not None:
                return v
        return None

    def ltm(self, field: str, sign: float = 1.0) -> float:
        last = self.fy(field, sign=sign)[-1]
        cur = self._h1(field, self.c["H1_START"], self.c["H1_END"])
        prev = self._h1(field, self.c["H1_PREV_START"], self.c["H1_PREV_END"])
        if cur is None or prev is None:
            return last
        return last + sign * (cur - prev)

    def bal_h1(self, field: str) -> float:
        if field in self.c.get("H1_BAL_MANUAL", {}):
            return self.c["H1_BAL_MANUAL"][field]
        tag = self.c["TAGS"].get(field)
        tags = (tag,) if isinstance(tag, str) else (tag or ())
        for t in tags:
            v = self.h1.get(t, {}).get((None, self.c["H1_END"]))
            if v is not None:
                return v
        return self.fy(field, instant=True)[-1]

    # --- conversion ----------------------------------------------------------
    def flow(self, field: str, sign: float = 1.0) -> list[float]:
        return [v / self.c["FX_AVG"][y] for v, y in zip(self.fy(field, sign=sign), self.c["YEARS"])]

    def bal(self, field: str) -> list[float]:
        return [v / self.c["FX_YE"][y] for v, y in zip(self.fy(field, instant=True), self.c["YEARS"])]

    def ltm_usd(self, field: str, sign: float = 1.0) -> float:
        return self.ltm(field, sign) / self.c["FX_LTM_AVG"]

    def bal_ltm_usd(self, field: str) -> float:
        return self.bal_h1(field) / self.c["FX_H1_END"]

    # --- objetos del pipeline -------------------------------------------------
    def series(self) -> AnnualSeries:
        c, Y = self.c, self.c["YEARS"]
        f, b, L = self.flow, self.bal, self.ltm_usd
        capex = [x + y for x, y in zip(f("capex_ppe"), f("capex_int"))]
        # 'Balance Sheet' tiene fila propia de arrendamientos (lease_liability_noncurrent) y el
        # Input sheet suma deuda CP + LP + arrendamientos: la deuda LP va SIN arrendamientos para no
        # contarlos dos veces. Bajo IFRS 16 el alquiler no esta en el EBIT, asi que si son deuda.
        debt_lt = b("loans_nc")
        debt_c = [x + y for x, y in zip(b("loans_c"), b("lease_c"))]
        tax = f("tax")
        return AnnualSeries(
            ticker=c["TICKER"], company_name=c["COMPANY"], fiscal_year_ends=[f"{y}-12-31" for y in Y],
            revenue=f("revenue"), ebit=f("ebit"), da=f("da"),
            shares_outstanding=[s * 1e6 for s in c["SHARES_YE"]],
            long_term_debt=debt_lt, current_debt=debt_c, cash=b("cash"), lease_liability_noncurrent=b("lease_nc"),
            ltm_revenue=L("revenue"), ltm_ebit=L("ebit"), ltm_da=L("da"),
            tax_expense=tax, net_income=f("ni"),
            diluted_shares_avg=[s * 1e6 for s in c["DILUTED_AVG"]], basic_shares_avg=[s * 1e6 for s in c["DILUTED_AVG"]],
            operating_cash_flow=f("ocf"), capex=capex, buybacks=f("buyback"), dividends_paid=f("div"),
            cogs=f("cogs"), current_assets=b("ca"), current_liabilities=b("cl"),
            ltm_tax_expense=L("tax"), ltm_net_income=L("ni"),
            ltm_diluted_shares_avg=c["SHARES_LTM"] * 1e6, ltm_basic_shares_avg=c["SHARES_LTM"] * 1e6,
            ltm_operating_cash_flow=L("ocf"), ltm_capex=L("capex_ppe") + L("capex_int"), ltm_buybacks=L("buyback"),
            ltm_dividends_paid=L("div"), ltm_cogs=L("cogs"),
            rd=f("rd"), sga=f("sga"), pretax_income=f("pretax"),
            total_assets=b("assets"), total_liabilities=[a - e for a, e in zip(b("assets"), b("equity"))], equity=b("equity"),
            share_based_comp=f("sbc"), investing_cash_flow=f("icf"), financing_cash_flow=f("fcf"),
            receivables=b("recv"), ppe_net=b("ppe"), goodwill=b("goodwill"), accounts_payable=b("ap"),
            retained_earnings=b("retained"), apic=[0.0] * len(Y), intangibles_net=b("intang"),
            long_term_investments=[0.0] * len(Y), short_term_investments=b("sti"),
            ltm_rd=L("rd"), ltm_sga=L("sga"), ltm_pretax_income=L("pretax"), ltm_share_based_comp=L("sbc"),
            ltm_investing_cash_flow=L("icf"), ltm_financing_cash_flow=L("fcf"),
            interest_expense=f("fin_exp"), ltm_interest_expense=L("fin_exp"),
            interest_investment_income=f("fin_inc"), ltm_interest_investment_income=L("fin_inc"),
            business_acquisitions=[0.0] * len(Y), ltm_business_acquisitions=0.0,
        )

    def inputs(self, s: AnnualSeries, price: float) -> CompanyInputs:
        c = self.c
        M = 1e6
        debt_ltm = sum(self.bal_ltm_usd(k) for k in ("loans_c", "loans_nc", "lease_c", "lease_nc"))
        debt_ye = s.long_term_debt[-1] + s.current_debt[-1]
        margins = [e / r for e, r in zip(s.ebit, s.revenue) if r]
        return CompanyInputs(
            ticker=c["TICKER"], company_name=c["COMPANY"], country_of_incorporation=c["COUNTRY"],
            industry_us=c["INDUSTRY"], industry_global=c["INDUSTRY"],
            revenue_ltm=s.ltm_revenue / M, revenue_prior_10k=s.revenue[-1] / M, years_since_last_10k=0.5,
            ebit_ltm=s.ltm_ebit / M, ebit_prior_10k=s.ebit[-1] / M,
            interest_expense_ltm=s.ltm_interest_expense / M, interest_expense_prior_10k=s.interest_expense[-1] / M,
            book_value_equity_ltm=self.bal_ltm_usd("equity") / M, book_value_equity_prior_10k=s.equity[-1] / M,
            book_value_debt_ltm=debt_ltm / M, book_value_debt_prior_10k=debt_ye / M,
            cash_ltm=(self.bal_ltm_usd("cash") + self.bal_ltm_usd("sti")) / M,
            cash_prior_10k=(s.cash[-1] + s.short_term_investments[-1]) / M,
            cross_holdings_ltm=0.0, shares_outstanding=c["SHARES_LTM"], current_price=price,
            effective_tax_rate=s.ltm_tax_expense / s.ltm_pretax_income if s.ltm_pretax_income else 0.2,
            marginal_tax_rate=c["MARGINAL_TAX"],
            capitalize_rd=False, has_operating_leases=False, has_employee_options=False,
            ebit_margin_ltm=s.ltm_ebit / s.ltm_revenue, ebit_margin_avg_3y=sum(margins[-3:]) / 3,
            ebit_margin_avg_5y=sum(margins[-5:]) / min(5, len(margins)),
            ebit_margin_avg_10y=sum(margins) / len(margins),
            riskfree_rate=0.04, initial_cost_of_capital=0.09,
        )

    def run(self, sheet_id: str, peers: list[str]) -> None:
        c = self.c
        s = self.series()
        market = get_market_snapshot(c["YF_TICKER"])
        # yfinance cuenta solo una clase de accion en algunos emisores: se fija la base economica.
        market = replace(market, shares_outstanding=c["SHARES_LTM"] * 1e6,
                         market_cap=c["SHARES_LTM"] * 1e6 * market.current_price)
        ci = self.inputs(s, market.current_price)
        sh = open_target_sheet(get_gspread_client(), sheet_id)
        print(f"[ifrs] {c['TICKER']}: ingresos LTM US${s.ltm_revenue/1e6:,.0f}M, EBIT LTM US${s.ltm_ebit/1e6:,.0f}M")
        rnm.refresh_input_sheet(sh, c["TICKER"], ci, c["INDUSTRY"], c["INDUSTRY"], market)
        rnm.refresh_income_statement(sh, s, ci)
        rnm.refresh_cash_flow_statement(sh, s)
        rnm.refresh_balance_sheet(sh, s, ci)
        rnm.refresh_period_headers(sh, s)
        computed = rnm.refresh_trailing_valuation(sh, s, ci)
        rnm.refresh_forward_valuation(sh, s, computed)
        rnm.refresh_eficiencia_capital(sh)
        rnm.refresh_margenes(sh)
        rnm.refresh_salud_financiera(sh)
        rnm.refresh_por_accion(sh)
        rnm.refresh_sector(sh, c["YF_TICKER"], peers)
        rnm.refresh_resumen_valoracion(sh, c["YF_TICKER"], market)
        print(f"[ifrs] listo: {sh.url}")


def today() -> date:
    return date.today()
