"""Wrapper delgado sobre yfinance: precio/market cap del ticker objetivo, y
multiplos de comparables (peers) -- lo que SEC EDGAR no tiene, porque es un
repositorio de estados contables, no de cotizaciones (ver docstring de
sec_edgar_loader.py). yfinance en cambio solo trae ~4 anios de historico
anual, por eso NO se usa para el historico largo (ver
sec_edgar_loader.load_annual_series_from_sec_edgar) -- yfinance.financials
alcanza para CAGR 3Y de un peer, pero no siempre para 5Y/10Y; cuando no
alcanza, se deja en None en vez de inventar un numero (ver comps_loader.py).
"""
from __future__ import annotations

from dataclasses import dataclass

import yfinance as yf


class YFinanceError(RuntimeError):
    pass


@dataclass(frozen=True)
class MarketSnapshot:
    ticker: str
    current_price: float
    market_cap: float
    shares_outstanding: float
    enterprise_value: float | None
    total_debt: float | None
    total_cash: float | None
    beta: float | None = None   # beta apalancado (regresion de Yahoo contra el mercado) -- para WACC automatico


def get_market_snapshot(ticker: str) -> MarketSnapshot:
    info = yf.Ticker(ticker).info
    price = info.get("currentPrice") or info.get("regularMarketPrice")
    if not price:
        raise YFinanceError(
            f"yfinance no devolvio precio actual para {ticker!r} -- revisa que el "
            "ticker sea correcto (o que Yahoo Finance lo tenga listado)."
        )
    return MarketSnapshot(
        ticker=ticker.upper(),
        current_price=float(price),
        market_cap=float(info.get("marketCap") or 0.0),
        shares_outstanding=float(info.get("sharesOutstanding") or 0.0),
        enterprise_value=info.get("enterpriseValue"),
        total_debt=info.get("totalDebt"),
        total_cash=info.get("totalCash"),
        beta=info.get("beta"),
    )


@dataclass(frozen=True)
class PeerMultiples:
    """Una fila de la hoja 'Sector' del Excel -- ver comps_loader.py para como
    se arma la tabla completa (peer set + estadisticas agregadas)."""

    ticker: str
    company_name: str
    market_cap: float | None
    gross_margin: float | None
    forward_pe: float | None
    pe: float | None
    ev_fcf: float | None
    p_fcf: float | None
    ev_ebitda: float | None
    p_ocf: float | None
    operating_margin: float | None
    revenue_cagr_3y: float | None
    revenue_cagr_5y: float | None
    revenue_cagr_10y: float | None


def _cagr_from_annual_series(values: list[float], years: int) -> float | None:
    """`values` viene de yfinance.financials, MAS RECIENTE PRIMERO (asi lo
    devuelve la libreria). None si no hay suficiente historia -- no se
    extrapola (ver docstring del modulo)."""
    if len(values) <= years:
        return None
    newest, oldest = values[0], values[years]
    if oldest <= 0:
        return None
    return (newest / oldest) ** (1 / years) - 1


def get_peer_multiples(ticker: str, company_name: str | None = None) -> PeerMultiples:
    t = yf.Ticker(ticker)
    info = t.info

    market_cap = info.get("marketCap")
    ev = info.get("enterpriseValue")
    ebitda = info.get("ebitda")
    free_cash_flow = info.get("freeCashflow")
    operating_cash_flow = info.get("operatingCashflow")

    ev_ebitda = (ev / ebitda) if ev and ebitda else None
    ev_fcf = (ev / free_cash_flow) if ev and free_cash_flow else None
    p_fcf = (market_cap / free_cash_flow) if market_cap and free_cash_flow else None
    p_ocf = (market_cap / operating_cash_flow) if market_cap and operating_cash_flow else None

    try:
        revenue_values = list(t.financials.loc["Total Revenue"])  # mas reciente primero
    except (KeyError, AttributeError):
        revenue_values = []

    return PeerMultiples(
        ticker=ticker.upper(),
        company_name=company_name or info.get("shortName") or ticker.upper(),
        market_cap=market_cap,
        gross_margin=info.get("grossMargins"),
        forward_pe=info.get("forwardPE"),
        pe=info.get("trailingPE"),
        ev_fcf=ev_fcf,
        p_fcf=p_fcf,
        ev_ebitda=ev_ebitda,
        p_ocf=p_ocf,
        operating_margin=info.get("operatingMargins"),
        revenue_cagr_3y=_cagr_from_annual_series(revenue_values, 3),
        revenue_cagr_5y=_cagr_from_annual_series(revenue_values, 5),
        revenue_cagr_10y=_cagr_from_annual_series(revenue_values, 10),
    )
