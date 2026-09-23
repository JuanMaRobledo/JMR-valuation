import pandas as pd
import pytest

from jmr_valuation.io.yfinance_client import (
    YFinanceError,
    get_historical_close_prices,
    get_market_snapshot,
    get_peer_multiples,
)


class _FakeTicker:
    def __init__(self, info, financials=None, history_df=None):
        self.info = info
        self.financials = financials if financials is not None else pd.DataFrame()
        self._history_df = history_df if history_df is not None else pd.DataFrame()

    def history(self, start=None, end=None, auto_adjust=None):
        return self._history_df


def test_get_market_snapshot_reads_price_and_market_cap(monkeypatch):
    fake = _FakeTicker({
        "currentPrice": 263.5, "marketCap": 104_741_249_024, "sharesOutstanding": 397_500_000,
        "enterpriseValue": 100_360_921_088, "totalDebt": 7_077_000_192, "totalCash": 5_625_999_872,
        "beta": 1.417,
    })
    monkeypatch.setattr("jmr_valuation.io.yfinance_client.yf.Ticker", lambda ticker: fake)

    snap = get_market_snapshot("ADBE")
    assert snap.ticker == "ADBE"
    assert snap.beta == pytest.approx(1.417)
    assert snap.current_price == pytest.approx(263.5)
    assert snap.market_cap == pytest.approx(104_741_249_024)
    assert snap.shares_outstanding == pytest.approx(397_500_000)


def test_get_market_snapshot_raises_clear_error_without_price(monkeypatch):
    fake = _FakeTicker({"marketCap": 100.0})
    monkeypatch.setattr("jmr_valuation.io.yfinance_client.yf.Ticker", lambda ticker: fake)
    with pytest.raises(YFinanceError, match="no devolvio precio"):
        get_market_snapshot("NOPE")


def test_get_peer_multiples_computes_ratios_from_market_cap_and_ev(monkeypatch):
    info = {
        "shortName": "Adobe Inc.", "marketCap": 1000.0, "enterpriseValue": 950.0,
        "ebitda": 100.0, "freeCashflow": 80.0, "operatingCashflow": 90.0,
        "grossMargins": 0.9, "forwardPE": 10.0, "trailingPE": 12.0, "operatingMargins": 0.35,
    }
    financials = pd.DataFrame(
        {pd.Timestamp("2025-01-01"): [280.0], pd.Timestamp("2024-01-01"): [240.0],
         pd.Timestamp("2023-01-01"): [200.0], pd.Timestamp("2022-01-01"): [160.0]},
        index=["Total Revenue"],
    )
    fake = _FakeTicker(info, financials)
    monkeypatch.setattr("jmr_valuation.io.yfinance_client.yf.Ticker", lambda ticker: fake)

    result = get_peer_multiples("ADBE")
    assert result.company_name == "Adobe Inc."
    assert result.ev_ebitda == pytest.approx(950.0 / 100.0)
    assert result.ev_fcf == pytest.approx(950.0 / 80.0)
    assert result.p_fcf == pytest.approx(1000.0 / 80.0)
    assert result.p_ocf == pytest.approx(1000.0 / 90.0)
    assert result.revenue_cagr_3y == pytest.approx((280.0 / 160.0) ** (1 / 3) - 1)
    assert result.revenue_cagr_5y is None  # solo 4 anios de historia -- no se inventa
    assert result.revenue_cagr_10y is None


def test_get_peer_multiples_handles_missing_financials_gracefully(monkeypatch):
    fake = _FakeTicker({"shortName": "X"})  # financials queda como DataFrame vacio
    monkeypatch.setattr("jmr_valuation.io.yfinance_client.yf.Ticker", lambda ticker: fake)
    result = get_peer_multiples("X")
    assert result.revenue_cagr_3y is None
    assert result.ev_ebitda is None


def _history_df(rows: dict[str, float]) -> pd.DataFrame:
    """rows: {'YYYY-MM-DD': close} -- dias HABILES simulados (no todos los
    dias del calendario, igual que el historico real de yfinance)."""
    index = pd.to_datetime(list(rows.keys()))
    return pd.DataFrame({"Close": list(rows.values())}, index=index)


def test_get_historical_close_prices_picks_last_trading_day_on_or_before_target(monkeypatch):
    """Un fin de ejercicio fiscal (p.ej. 30/6, sabado en algunos años) casi
    nunca cae en un dia habil de bolsa exacto -- se usa el cierre del ultimo
    dia habil ANTERIOR, nunca uno posterior (no se inventa un precio que el
    mercado todavia no habia fijado a esa fecha)."""
    fake = _FakeTicker({}, history_df=_history_df({
        "2024-06-27": 445.0, "2024-06-28": 447.0,  # 6/29-30 son fin de semana
        "2024-07-01": 450.0,
    }))
    monkeypatch.setattr("jmr_valuation.io.yfinance_client.yf.Ticker", lambda ticker: fake)

    prices = get_historical_close_prices("MSFT", ["2024-06-30"])
    assert prices == pytest.approx([447.0])


def test_get_historical_close_prices_returns_none_before_earliest_available_data(monkeypatch):
    """Una fecha anterior a la primera cotizacion disponible (empresa recien
    salida a bolsa, o ticker sin ese historico) queda en None -- no se
    extrapola hacia atras."""
    fake = _FakeTicker({}, history_df=_history_df({"2020-01-02": 50.0, "2020-01-03": 51.0}))
    monkeypatch.setattr("jmr_valuation.io.yfinance_client.yf.Ticker", lambda ticker: fake)

    prices = get_historical_close_prices("MSFT", ["2019-06-30", "2020-01-03"])
    assert prices == [None, pytest.approx(51.0)]


def test_get_historical_close_prices_returns_all_none_when_history_is_empty(monkeypatch):
    fake = _FakeTicker({}, history_df=pd.DataFrame())
    monkeypatch.setattr("jmr_valuation.io.yfinance_client.yf.Ticker", lambda ticker: fake)

    assert get_historical_close_prices("MSFT", ["2020-01-01", "2021-01-01"]) == [None, None]


def test_get_historical_close_prices_returns_empty_list_for_no_dates(monkeypatch):
    monkeypatch.setattr("jmr_valuation.io.yfinance_client.yf.Ticker", lambda ticker: _FakeTicker({}))
    assert get_historical_close_prices("MSFT", []) == []
