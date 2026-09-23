"""Arma la tabla de comparables (hoja 'Sector' del Excel): multiplos de un
set de empresas peer + estadisticas agregadas (promedio, mediana). El set de
peers lo define quien corre el pipeline (parametro `peer_tickers`) -- este
modulo no elige ni inventa comparables."""
from __future__ import annotations

import statistics
from dataclasses import dataclass

from jmr_valuation.io.yfinance_client import PeerMultiples, get_peer_multiples

_NUMERIC_FIELDS = (
    "market_cap", "gross_margin", "forward_pe", "pe", "ev_fcf", "p_fcf",
    "ev_ebitda", "p_ocf", "operating_margin", "revenue_cagr_3y", "revenue_cagr_5y", "revenue_cagr_10y",
)


@dataclass(frozen=True)
class CompsTable:
    peers: list[PeerMultiples]
    average: dict[str, float | None]
    median: dict[str, float | None]
    q1: dict[str, float | None]   # primer cuartil -- ver assumptions_engine.run_growth_engine (escenario Conservador)
    q3: dict[str, float | None]   # tercer cuartil -- escenario Optimista


def _agg(peers: list[PeerMultiples], field: str, fn) -> float | None:
    values = [v for p in peers if (v := getattr(p, field)) is not None]
    return fn(values) if values else None


def _quartile(values: list[float], which: int) -> float:
    """QUARTILE.INC de Excel (metodo 'inclusive') -- mismo criterio que usa
    'Crecimiento y Márgenes'!C13:C15 (=QUARTILE(Sector!...,1/2/3)) para los
    cuartiles de industria basados en los peers reales, no en una tabla
    agregada de Damodaran."""
    if len(values) == 1:
        return values[0]
    return statistics.quantiles(sorted(values), n=4, method="inclusive")[which - 1]


def load_comps_table(peer_tickers: list[str]) -> CompsTable:
    if not peer_tickers:
        raise ValueError("Se necesita al menos un ticker peer para armar la tabla de comps")

    peers = [get_peer_multiples(ticker) for ticker in peer_tickers]
    average = {field: _agg(peers, field, lambda vs: sum(vs) / len(vs)) for field in _NUMERIC_FIELDS}
    median = {field: _agg(peers, field, statistics.median) for field in _NUMERIC_FIELDS}
    q1 = {field: _agg(peers, field, lambda vs: _quartile(vs, 1)) for field in _NUMERIC_FIELDS}
    q3 = {field: _agg(peers, field, lambda vs: _quartile(vs, 3)) for field in _NUMERIC_FIELDS}

    return CompsTable(peers=peers, average=average, median=median, q1=q1, q3=q3)
