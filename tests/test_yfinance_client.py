import pandas as pd
import pytest

from jmr_valuation.io.yfinance_client import (
    YFinanceError,
    get_market_snapshot,
    get_peer_multiples,
)


class _FakeTicker:
    def __init__(self, info, financials=None):
        self.info = info
        self.financials = financials if financials is not None else pd.DataFrame()


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
