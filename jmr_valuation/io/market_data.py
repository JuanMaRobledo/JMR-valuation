"""Datos de mercado que no son de una empresa en particular: la tasa libre de
riesgo (proxy: rendimiento del bono del Tesoro a 10 años, ticker '^TNX' en
Yahoo Finance). Separado de yfinance_client.py porque no toma un ticker de
empresa."""
from __future__ import annotations

import yfinance as yf

_TREASURY_10Y_TICKER = "^TNX"


class MarketDataError(RuntimeError):
    pass


def current_riskfree_rate() -> float:
    """Rendimiento mas reciente del Treasury a 10 años, como decimal (ej.
    0.0462, no 4.62). Mismo proxy que ya usaba el Excel (Input sheet B35)."""
    history = yf.Ticker(_TREASURY_10Y_TICKER).history(period="5d")
    if history.empty:
        raise MarketDataError(
            "yfinance no devolvio historico para ^TNX (Treasury 10y) -- "
            "pasa --riskfree-rate manualmente."
        )
    return float(history["Close"].iloc[-1]) / 100
