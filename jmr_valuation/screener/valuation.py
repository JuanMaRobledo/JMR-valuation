"""Precio de hoy vs la propia historia de la empresa (Paso 4 de la metodologia).

"Rara vez se juzga barato en terminos absolutos -- casi siempre es
barato/caro RELATIVO a su propia historia." Por eso, ademas del FCF yield y
el P/E actuales, se reconstruye el P/FCF y el P/E de cada cierre de
ejercicio (precio de cierre de esa fecha x acciones diluidas promedio de ese
FY / FCF o utilidad neta del FY) y se compara el multiplo de hoy contra la
mediana de esa historia.

Modulo puro: recibe la serie SEC y los precios ya descargados.
"""
from __future__ import annotations

import statistics
from dataclasses import asdict, dataclass, field
from datetime import date

from jmr_valuation.io.sec_edgar_loader import AnnualSeries
from jmr_valuation.screener.metrics import share_counts


# Multiplos del Modelo JMR (EV/EBITDA, EV/FCFF, P/E, P/FCFE, P/OCF -- ver
# models/relative.py) + P/FCF (el "favorito transversal" de la metodologia,
# base del FCF yield) + EV/EBIT. Cada uno: (numerador, denominador).
MULTIPLES: dict[str, tuple[str, str]] = {
    "pe": ("mcap", "net_income"),
    "p_fcf": ("mcap", "fcf"),
    "p_fcfe": ("mcap", "fcfe"),
    "p_ocf": ("mcap", "ocf"),
    "ev_ebitda": ("ev", "ebitda"),
    "ev_fcff": ("ev", "fcff"),
    "ev_ebit": ("ev", "ebit"),
}


@dataclass(frozen=True)
class MultipleSnapshot:
    current: float | None
    median_hist: float | None
    vs_hist: float | None   # -0.25 = 25% por debajo de su mediana historica
    hist_years: int


@dataclass(frozen=True)
class ValuationSnapshot:
    price: float
    market_cap: float
    fcf_yield: float | None
    pe: float | None
    ev_ebit: float | None
    p_fcf: float | None
    p_fcf_median_hist: float | None
    pe_median_hist: float | None
    p_fcf_vs_hist: float | None   # -0.25 = 25% mas barata que su mediana historica
    pe_vs_hist: float | None
    hist_years: int
    label: str
    peg: float | None = None      # P/E / (crecimiento anual del EPS en %)
    multiples: dict[str, MultipleSnapshot] = field(default_factory=dict)
    # Lo necesario para que la pagina recalcule todo con el precio del dia
    # (screener.html + api/quotes.js de Modelo-JMR) sin volver a la SEC:
    # market cap = precio x shares; EV = market cap + net_debt; cada multiplo
    # = numerador / ltm[denominador] (ver MULTIPLES).
    shares: float | None = None
    net_debt: float | None = None
    ltm: dict[str, float | None] = field(default_factory=dict)
    eps_growth: float | None = None

    def as_dict(self) -> dict:
        return asdict(self)


def _close_on_or_before(prices: list[tuple[str, float]], iso_date: str) -> float | None:
    """`prices` ordenado por fecha (Yahoo: cierre ajustado por split, no por
    dividendos -- consistente con share_counts). Tolera hasta 21 dias de hueco (series
    semanales, feriados) antes de devolver None."""
    target = date.fromisoformat(iso_date)
    best: float | None = None
    best_day: date | None = None
    for day_iso, close in prices:
        day = date.fromisoformat(day_iso)
        if day > target:
            break
        best, best_day = close, day
    if best_day is None or (target - best_day).days > 21:
        return None
    return best


def _label(vs_hist: float | None) -> str:
    if vs_hist is None:
        return "Sin historia"
    if vs_hist <= -0.20:
        return "Barata vs su historia"
    if vs_hist <= -0.05:
        return "Algo bajo su historia"
    if vs_hist <= 0.10:
        return "En linea con su historia"
    return "Cara vs su historia"


def _pending_split_factor(s: AnnualSeries, splits: list[tuple[str, float]]) -> float:
    """Factor de los splits posteriores al ultimo 10-K que las acciones de la
    SEC todavia no reflejan (BKNG: split 25:1 en abril 2026, despues del 10-K
    2025). Si las acciones LTM (10-Q) ya saltaron en ese factor contra el
    ultimo FY, el split ya esta incorporado y share_counts ya reescalo la
    historia -- no se aplica dos veces."""
    if not splits or not s.fiscal_year_ends:
        return 1.0
    factor = 1.0
    for day, ratio in splits:
        if day > s.fiscal_year_ends[-1]:
            factor *= ratio
    if factor == 1.0:
        return 1.0
    last_fy = s.diluted_shares_avg[-1] if s.diluted_shares_avg else 0.0
    if last_fy and s.ltm_diluted_shares_avg and abs(s.ltm_diluted_shares_avg / last_fy / factor - 1) < 0.1:
        return 1.0
    return factor


def _at(values: list[float], i: int) -> float:
    return values[i] if -len(values) <= i < len(values) else 0.0


def _tax_rate(tax: float, pretax: float) -> float:
    rate = tax / pretax if pretax > 0 else 0.21
    return rate if 0.0 <= rate <= 0.5 else 0.21


def _denominators(s: AnnualSeries, i: int | None) -> dict[str, float | None]:
    """Utilidad, flujos y EBITDA de un FY (i) o del LTM (i=None), con las
    mismas definiciones que 'Financials Multiples' del modelo:
    - FCFF = OCF - CapEx + intereses x (1 - t)  (equivale a EBIT(1-t) + D&A - CapEx - dNWC)
    - FCFE = OCF - CapEx + endeudamiento neto   (cambio de la deuda financiera en el anio)
    - OCF  = flujo de caja operativo reportado
    """
    last = len(s.revenue) - 1
    j = last if i is None else i
    debt_now = _at(s.long_term_debt, j) + _at(s.current_debt, j)
    debt_prev = _at(s.long_term_debt, j - 1) + _at(s.current_debt, j - 1) if j > 0 else None
    if i is None:
        ocf, capex, ebit = s.ltm_operating_cash_flow, s.ltm_capex, s.ltm_ebit
        ni, interest = s.ltm_net_income, s.ltm_interest_expense
        last_da = _at(s.da, last)
        da = s.ltm_da if s.ltm_da >= 0.6 * last_da else last_da  # ver metrics.compute_metrics
        t = _tax_rate(s.ltm_tax_expense, s.ltm_pretax_income)
    else:
        ocf, capex, ebit = _at(s.operating_cash_flow, i), _at(s.capex, i), _at(s.ebit, i)
        ni, interest, da = _at(s.net_income, i), _at(s.interest_expense, i), _at(s.da, i)
        t = _tax_rate(_at(s.tax_expense, i), _at(s.pretax_income, i))
    has_ocf = bool(ocf)
    fcf = ocf - capex if has_ocf else None
    return {
        "net_income": ni or None,
        "ocf": ocf if has_ocf else None,
        "fcf": fcf,
        "fcff": fcf + abs(interest) * (1 - t) if fcf is not None else None,
        "fcfe": fcf + (debt_now - debt_prev) if fcf is not None and debt_prev is not None else None,
        "ebit": ebit or None,
        "ebitda": (ebit + da) if ebit else None,
        "net_debt": debt_now - _at(s.cash, j) - _at(s.short_term_investments, j),
    }


def _multiple(kind: str, denom_key: str, mcap: float, d: dict[str, float | None]) -> float | None:
    denom = d[denom_key]
    if denom is None or denom <= 0:
        return None
    numerator = mcap if kind == "mcap" else mcap + (d["net_debt"] or 0.0)
    return numerator / denom if numerator > 0 else None


def value_snapshot(s: AnnualSeries, prices: list[tuple[str, float]],
                   splits: list[tuple[str, float]] = (),
                   eps_growth: float | None = None) -> ValuationSnapshot | None:
    """`eps_growth`: crecimiento anual del EPS (0.12 = 12%) para el PEG --
    el screener pasa el CAGR 5 anios de metrics.compute_metrics."""
    if not prices:
        return None
    price = prices[-1][1]
    hist_shares, shares = share_counts(s)
    pending = _pending_split_factor(s, list(splits))
    if pending != 1.0:
        hist_shares = [x * pending if x else x for x in hist_shares]
        shares = shares * pending if shares else shares
    if not shares or price <= 0:
        return None
    market_cap = price * shares

    ltm = _denominators(s, None)
    current = {k: _multiple(kind, den, market_cap, ltm) for k, (kind, den) in MULTIPLES.items()}

    history: dict[str, list[float]] = {k: [] for k in MULTIPLES}
    for i, end in enumerate(s.fiscal_year_ends):
        close = _close_on_or_before(prices, end)
        sh = hist_shares[i] if i < len(hist_shares) else None
        if close is None or not sh:
            continue
        d = _denominators(s, i)
        for k, (kind, den) in MULTIPLES.items():
            value = _multiple(kind, den, close * sh, d)
            if value is not None:
                history[k].append(value)

    multiples: dict[str, MultipleSnapshot] = {}
    for k in MULTIPLES:
        med = statistics.median(history[k]) if len(history[k]) >= 3 else None
        cur = current[k]
        multiples[k] = MultipleSnapshot(
            current=cur, median_hist=med,
            vs_hist=(cur / med - 1) if cur and med else None,
            hist_years=len(history[k]),
        )

    pe, p_fcf = multiples["pe"], multiples["p_fcf"]
    ltm_fcf = ltm["fcf"]
    return ValuationSnapshot(
        price=round(price, 2),
        market_cap=market_cap,
        fcf_yield=(ltm_fcf / market_cap) if ltm_fcf is not None else None,
        pe=pe.current,
        ev_ebit=multiples["ev_ebit"].current,
        p_fcf=p_fcf.current,
        p_fcf_median_hist=p_fcf.median_hist,
        pe_median_hist=pe.median_hist,
        p_fcf_vs_hist=p_fcf.vs_hist,
        pe_vs_hist=pe.vs_hist,
        hist_years=max(p_fcf.hist_years, pe.hist_years),
        # FCF es el multiplo "favorito transversal" de la metodologia; P/E de respaldo.
        label=_label(p_fcf.vs_hist if p_fcf.vs_hist is not None else pe.vs_hist),
        peg=(pe.current / (eps_growth * 100)) if pe.current and eps_growth and eps_growth > 0 else None,
        multiples=multiples,
        shares=shares,
        net_debt=ltm["net_debt"],
        ltm={k: v for k, v in ltm.items() if k != "net_debt"},
        eps_growth=eps_growth,
    )
