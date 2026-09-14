import pandas as pd
import pytest

from jmr_valuation.io.market_data import MarketDataError, current_riskfree_rate


class _FakeTicker:
    def __init__(self, history_df):
        self._history_df = history_df

    def history(self, period=None):
        return self._history_df


def test_current_riskfree_rate_converts_percent_to_decimal(monkeypatch):
    history = pd.DataFrame({"Close": [4.90, 4.95, 4.979]})
    monkeypatch.setattr("jmr_valuation.io.market_data.yf.Ticker", lambda ticker: _FakeTicker(history))

    rate = current_riskfree_rate()
    assert rate == pytest.approx(0.04979)


def test_current_riskfree_rate_raises_clear_error_when_empty(monkeypatch):
    monkeypatch.setattr("jmr_valuation.io.market_data.yf.Ticker", lambda ticker: _FakeTicker(pd.DataFrame()))
    with pytest.raises(MarketDataError, match="no devolvio historico"):
        current_riskfree_rate()
