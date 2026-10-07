"""European local listings, isolated from SEC loaders and company valuations.

A curated, versioned selection, NOT an index replica. Yahoo's annual time
series normally covers four FY. Never label this shorter window as five years
or award a JMR quality score without the required six fiscal closes.
Monetary ratios use one reporting currency and one fiscal date. London prices
are normalized from GBp to GBP. Cross-currency ratios remain unavailable.
"""
from __future__ import annotations

import json
import math
import time
from datetime import datetime, timezone
from urllib.parse import urlencode, quote
from urllib.request import Request, urlopen

# ticker | company | listing country | sector. Native listings, no ADR duplication.
_LIST = """ASML.AS|ASML|Países Bajos|Information Technology
ADYEN.AS|Adyen|Países Bajos|Financials
HEIA.AS|Heineken|Países Bajos|Consumer Staples
WKL.AS|Wolters Kluwer|Países Bajos|Industrials
AD.AS|Ahold Delhaize|Países Bajos|Consumer Staples
INGA.AS|ING|Países Bajos|Financials
MC.PA|LVMH|Francia|Consumer Discretionary
OR.PA|L’Oréal|Francia|Consumer Staples
RMS.PA|Hermès|Francia|Consumer Discretionary
SU.PA|Schneider Electric|Francia|Industrials
AI.PA|Air Liquide|Francia|Materials
SAN.PA|Sanofi|Francia|Health Care
TTE.PA|TotalEnergies|Francia|Energy
SAF.PA|Safran|Francia|Industrials
AIR.PA|Airbus|Francia|Industrials
BN.PA|Danone|Francia|Consumer Staples
DG.PA|Vinci|Francia|Industrials
BNP.PA|BNP Paribas|Francia|Financials
SAP.DE|SAP|Alemania|Information Technology
SIE.DE|Siemens|Alemania|Industrials
ALV.DE|Allianz|Alemania|Financials
DTE.DE|Deutsche Telekom|Alemania|Communication Services
DHL.DE|DHL Group|Alemania|Industrials
IFX.DE|Infineon|Alemania|Information Technology
ADS.DE|Adidas|Alemania|Consumer Discretionary
BMW.DE|BMW|Alemania|Consumer Discretionary
MBG.DE|Mercedes-Benz|Alemania|Consumer Discretionary
BAS.DE|BASF|Alemania|Materials
AZN.L|AstraZeneca|Reino Unido|Health Care
SHEL.L|Shell|Reino Unido|Energy
ULVR.L|Unilever|Reino Unido|Consumer Staples
REL.L|RELX|Reino Unido|Industrials
DGE.L|Diageo|Reino Unido|Consumer Staples
GSK.L|GSK|Reino Unido|Health Care
LSEG.L|London Stock Exchange Group|Reino Unido|Financials
HSBA.L|HSBC|Reino Unido|Financials
NESN.SW|Nestlé|Suiza|Consumer Staples
NOVN.SW|Novartis|Suiza|Health Care
ROP.SW|Roche|Suiza|Health Care
ABBN.SW|ABB|Suiza|Industrials
CFR.SW|Richemont|Suiza|Consumer Discretionary
ZURN.SW|Zurich Insurance|Suiza|Financials
NOVO-B.CO|Novo Nordisk|Dinamarca|Health Care
DSV.CO|DSV|Dinamarca|Industrials
COLO-B.CO|Coloplast|Dinamarca|Health Care
VWS.CO|Vestas|Dinamarca|Industrials
ITX.MC|Inditex|España|Consumer Discretionary
IBE.MC|Iberdrola|España|Utilities
FER.MC|Ferrovial|España|Industrials
SAN.MC|Banco Santander|España|Financials
ENEL.MI|Enel|Italia|Utilities
ENI.MI|Eni|Italia|Energy
RACE.MI|Ferrari|Italia|Consumer Discretionary
PRY.MI|Prysmian|Italia|Industrials
ATCO-A.ST|Atlas Copco|Suecia|Industrials
VOLV-B.ST|Volvo Group|Suecia|Industrials
ASSA-B.ST|Assa Abloy|Suecia|Industrials
EQNR.OL|Equinor|Noruega|Energy
KNEBV.HE|Kone|Finlandia|Industrials
NOKIA.HE|Nokia|Finlandia|Information Technology"""
EUROPE = [dict(zip(("ticker", "name", "country", "sector"), line.split("|")), region="Europa")
          for line in _LIST.splitlines()]
FIELDS = ("TotalRevenue", "OperatingIncome", "GrossProfit", "NetIncome", "TaxProvision",
          "PretaxIncome", "OperatingCashFlow", "CapitalExpenditure", "TotalDebt",
          "CashCashEquivalentsAndShortTermInvestments", "StockholdersEquity",
          "EBITDA", "OrdinarySharesNumber")


def get_json(url):
    for attempt in range(3):
        try:
            with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as r:
                return json.load(r)
        except Exception:
            if attempt == 2:
                raise
            time.sleep(0.5 * 2 ** attempt)


def fetch_annual(ticker):
    params = {"type": ",".join("annual" + f for f in FIELDS), "period1": 1420070400,
              "period2": int(time.time())}
    return get_json("https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/"
                    + quote(ticker, safe="") + "?" + urlencode(params))


def fetch_chart(ticker):
    return get_json("https://query1.finance.yahoo.com/v8/finance/chart/" + quote(ticker, safe="")
                    + "?range=5y&interval=1mo&events=splits")


def number(value):
    return float(value) if isinstance(value, (int, float)) and math.isfinite(value) else None


def ratio(a, b):
    return a / b if a is not None and b is not None and b > 0 else None


def parse_annual(payload):
    """Retain dates and currencies; never turn absent data into zero."""
    result = {}
    for block in payload.get("timeseries", {}).get("result") or []:
        for field in FIELDS:
            for row in block.get("annual" + field, []):
                value = number(row.get("reportedValue", {}).get("raw"))
                if value is not None and row.get("asOfDate"):
                    result.setdefault(field, {})[row["asOfDate"]] = (value, row.get("currencyCode"))
    return result


def build_result(company, annual_payload, chart_payload):
    today = datetime.now(timezone.utc).date().isoformat()
    r = dict(company, industry="", sic="", tier="Historia insuficiente", score=None,
             error=None, metrics={}, quality={}, valuation=None, source="Yahoo Finance · estados anuales",
             fundamentals_as_of=today, currency=None)
    blocks = chart_payload.get("chart", {}).get("result") or []
    chart = blocks[0] if blocks else {}
    meta = chart.get("meta", {})
    # London quote units are pence; monetary statements are pounds (or USD).
    quote_currency = meta.get("currency")
    scale = 0.01 if quote_currency in ("GBp", "GBX") else 1.0
    currency = "GBP" if scale == 0.01 else quote_currency
    price = number(meta.get("regularMarketPrice"))
    r.update(currency=currency, quote_scale=scale)
    if price and currency:
        r["valuation"] = dict(price=price * scale, price_as_of=datetime.fromtimestamp(
            meta["regularMarketTime"], timezone.utc).date().isoformat() if meta.get("regularMarketTime") else None,
            market_cap=None, fcf_yield=None, pe=None, p_fcf=None, ev_ebit=None, peg=None,
            label="Sin historia", hist_years=0, multiples={}, basis="Último FY", live_reprice=False)
    if company["sector"] == "Financials":
        r["tier"] = "Excluida (financiera)"
        r["quality"] = dict(passes_filters=False, failed_filters=["Analizar con metodología financiera"],
                             flags=[], group_scores={})
        return r
    data = parse_annual(annual_payload)
    dates = sorted(data.get("TotalRevenue", {}))
    if not dates:
        raise ValueError("No hay ingresos anuales disponibles")
    end = dates[-1]
    reporting_currency = data["TotalRevenue"][end][1]
    if not reporting_currency:
        raise ValueError("Moneda de los estados financieros no identificada")
    r["reporting_currency"] = reporting_currency

    def at(field, day=end):
        entry = data.get(field, {}).get(day)
        if not entry or (field != "OrdinarySharesNumber" and entry[1] != reporting_currency):
            return None
        return entry[0]

    rev, ebit, gross, ni, debt, cash, equity, ebitda, ocf, capex, tax, pretax = [at(f) for f in (
        "TotalRevenue", "OperatingIncome", "GrossProfit", "NetIncome", "TotalDebt",
        "CashCashEquivalentsAndShortTermInvestments", "StockholdersEquity", "EBITDA",
        "OperatingCashFlow", "CapitalExpenditure", "TaxProvision", "PretaxIncome")]
    fcf = ocf - abs(capex) if ocf is not None and capex is not None else None
    net_debt = debt - cash if debt is not None and cash is not None else None
    def invested(day):
        parts = [at(f, day) for f in ("StockholdersEquity", "TotalDebt", "CashCashEquivalentsAndShortTermInvestments")]
        return parts[0] + parts[1] - parts[2] if all(x is not None for x in parts) else None
    ic = invested(end)
    prev = invested(dates[-2]) if len(dates) > 1 else None
    if ic is not None and prev is not None and ic > 0 and prev > 0:
        ic = (ic + prev) / 2
    rate = ratio(tax, pretax)
    roic = ratio(ebit * (1-rate), ic) if ebit is not None and rate is not None and 0 <= rate <= .5 else None
    r["metrics"] = dict(years=len(dates), last_fiscal_year_end=end, roic_last=roic,
        operating_margin_fy=ratio(ebit, rev), gross_margin_fy=ratio(gross, rev),
        fcf_margin_fy=ratio(fcf, rev), net_debt_to_ebitda=ratio(net_debt, ebitda))
    flags = ["Serie europea parcial: sin puntaje JMR, CAGR 5a ni medianas 5a/10a.",
             "Métricas y múltiplos basados en el último ejercicio anual (FY), no LTM."]
    if (datetime.now(timezone.utc).date() - datetime.fromisoformat(end).date()).days > 550:
        flags.append("Último ejercicio de más de 18 meses: revisar vigencia de los datos.")
    r["quality"] = dict(passes_filters=False, failed_filters=[
        f"Historia no validada para el filtro JMR de seis cierres fiscales ({len(dates)} FY disponibles)"],
        flags=flags, group_scores={}, coverage=None)
    if currency != reporting_currency:
        flags.append(f"Precio en {currency}; estados en {reporting_currency}: múltiplos omitidos hasta validar conversión.")
        return r
    # Balance share counts cannot price a certificate/class or a post-FY split
    # without an explicitly validated share conversion.
    share_safe = company["ticker"] not in {"BMW.DE", "ROP.SW", "CFR.SW", "ATCO-A.ST", "VOLV-B.ST", "ASSA-B.ST", "NOVO-B.CO", "COLO-B.CO", "KNEBV.HE"}
    split_after_fy = any(datetime.fromtimestamp(x["date"], timezone.utc).date().isoformat() > end
                         for x in chart.get("events", {}).get("splits", {}).values())
    shares = at("OrdinarySharesNumber")
    if not share_safe or split_after_fy:
        flags.append("Múltiplos omitidos: validar clases de acciones, certificados o split posterior al FY.")
        return r
    v = r["valuation"]
    if v is None or shares is None or shares <= 0:
        flags.append("Sin precio o número de acciones verificable para calcular múltiplos.")
        return r
    mcap = v["price"] * shares
    ev = mcap + net_debt if net_debt is not None else None
    denominators = dict(net_income=ni, fcf=fcf, ocf=ocf, ebitda=ebitda, ebit=ebit)
    definitions = dict(pe=(mcap, ni), p_fcf=(mcap, fcf), p_ocf=(mcap, ocf),
                       ev_ebitda=(ev, ebitda), ev_ebit=(ev, ebit))
    v.update(market_cap=mcap, shares=shares, net_debt=net_debt,
             fcf_yield=ratio(fcf, mcap), annual=denominators, live_reprice=True)
    v["multiples"] = {k: dict(current=ratio(a, b) if a is not None and a > 0 else None,
                              median_hist=None, vs_hist=None, hist_years=0) for k, (a,b) in definitions.items()}
    v.update({k: v["multiples"][k]["current"] for k in ("pe", "p_fcf", "ev_ebit")})
    flags.append("Capitalización aproximada con acciones al cierre FY; verificar recompras/emisiones posteriores.")
    return r


def screen_europe(company):
    try:
        chart = fetch_chart(company["ticker"])
        annual = {} if company["sector"] == "Financials" else fetch_annual(company["ticker"])
        return build_result(company, annual, chart)
    except Exception as exc:
        return dict(company, tier="Sin datos", score=None, error=f"{type(exc).__name__}: {str(exc)[:180]}",
                    metrics={}, quality={}, valuation=None, source="Yahoo Finance")
