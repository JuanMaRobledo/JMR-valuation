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
from dataclasses import asdict, dataclass
from datetime import date

from jmr_valuation.io.sec_edgar_loader import AnnualSeries
from jmr_valuation.screener.metrics import share_counts


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


def value_snapshot(s: AnnualSeries, prices: list[tuple[str, float]],
                   splits: list[tuple[str, float]] = ()) -> ValuationSnapshot | None:
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

    ltm_fcf = s.ltm_operating_cash_flow - s.ltm_capex
    ltm_ni = s.ltm_net_income
    debt = (s.long_term_debt[-1] if s.long_term_debt else 0.0) + (s.current_debt[-1] if s.current_debt else 0.0)
    cash = (s.cash[-1] if s.cash else 0.0) + (s.short_term_investments[-1] if s.short_term_investments else 0.0)
    ev = market_cap + debt - cash

    p_fcf = market_cap / ltm_fcf if ltm_fcf > 0 else None
    pe = market_cap / ltm_ni if ltm_ni > 0 else None

    hist_p_fcf: list[float] = []
    hist_pe: list[float] = []
    for i, end in enumerate(s.fiscal_year_ends):
        close = _close_on_or_before(prices, end)
        sh = hist_shares[i] if i < len(hist_shares) else None
        if close is None or not sh:
            continue
        mcap = close * sh
        ocf = s.operating_cash_flow[i] if i < len(s.operating_cash_flow) else 0.0
        fcf = ocf - (s.capex[i] if i < len(s.capex) else 0.0) if ocf else 0.0
        ni = s.net_income[i] if i < len(s.net_income) else 0.0
        if fcf > 0:
            hist_p_fcf.append(mcap / fcf)
        if ni > 0:
            hist_pe.append(mcap / ni)

    p_fcf_med = statistics.median(hist_p_fcf) if len(hist_p_fcf) >= 3 else None
    pe_med = statistics.median(hist_pe) if len(hist_pe) >= 3 else None
    p_fcf_vs = (p_fcf / p_fcf_med - 1) if p_fcf and p_fcf_med else None
    pe_vs = (pe / pe_med - 1) if pe and pe_med else None

    return ValuationSnapshot(
        price=round(price, 2),
        market_cap=market_cap,
        fcf_yield=(ltm_fcf / market_cap) if market_cap else None,
        pe=pe,
        ev_ebit=(ev / s.ltm_ebit) if s.ltm_ebit > 0 else None,
        p_fcf=p_fcf,
        p_fcf_median_hist=p_fcf_med,
        pe_median_hist=pe_med,
        p_fcf_vs_hist=p_fcf_vs,
        pe_vs_hist=pe_vs,
        hist_years=max(len(hist_p_fcf), len(hist_pe)),
        # FCF es el multiplo "favorito transversal" de la metodologia; P/E de respaldo.
        label=_label(p_fcf_vs if p_fcf_vs is not None else pe_vs),
    )
