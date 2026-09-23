import pytest

from jmr_valuation.io.comps_loader import load_comps_table
from jmr_valuation.io.yfinance_client import PeerMultiples


def _peer(ticker, pe, ev_ebitda, revenue_cagr_3y=None):
    return PeerMultiples(
        ticker=ticker, company_name=ticker, market_cap=100.0, gross_margin=0.8,
        forward_pe=pe - 1, pe=pe, ev_fcf=10.0, p_fcf=10.0, ev_ebitda=ev_ebitda,
        p_ocf=10.0, operating_margin=0.3, revenue_cagr_3y=revenue_cagr_3y,
        revenue_cagr_5y=None, revenue_cagr_10y=None,
    )


def test_load_comps_table_computes_average_and_median(monkeypatch):
    peers = {
        "AAA": _peer("AAA", pe=10.0, ev_ebitda=8.0, revenue_cagr_3y=0.1),
        "BBB": _peer("BBB", pe=20.0, ev_ebitda=12.0, revenue_cagr_3y=0.2),
        "CCC": _peer("CCC", pe=30.0, ev_ebitda=16.0),  # revenue_cagr_3y ausente -> no entra al promedio
    }
    monkeypatch.setattr(
        "jmr_valuation.io.comps_loader.get_peer_multiples", lambda ticker: peers[ticker],
    )

    table = load_comps_table(["AAA", "BBB", "CCC"])
    assert [p.ticker for p in table.peers] == ["AAA", "BBB", "CCC"]
    assert table.average["pe"] == pytest.approx(20.0)
    assert table.median["pe"] == pytest.approx(20.0)
    assert table.average["ev_ebitda"] == pytest.approx(12.0)
    assert table.average["revenue_cagr_3y"] == pytest.approx(0.15)  # solo AAA/BBB tienen dato


def test_load_comps_table_rejects_empty_peer_list():
    with pytest.raises(ValueError, match="al menos un ticker"):
        load_comps_table([])


def test_load_comps_table_computes_quartiles_excel_inclusive_method(monkeypatch):
    # QUARTILE.INC de Excel para [10,20,30,40,50,60] (6 peers): Q1=22.5, Q3=47.5
    peers = {t: _peer(t, pe=v, ev_ebitda=v) for t, v in
             zip("ABCDEF", [10.0, 20.0, 30.0, 40.0, 50.0, 60.0])}
    monkeypatch.setattr("jmr_valuation.io.comps_loader.get_peer_multiples", lambda ticker: peers[ticker])

    table = load_comps_table(list(peers))
    assert table.q1["pe"] == pytest.approx(22.5)
    assert table.median["pe"] == pytest.approx(35.0)
    assert table.q3["pe"] == pytest.approx(47.5)


def test_quartile_falls_back_to_the_single_value_with_one_peer(monkeypatch):
    peer = _peer("AAA", pe=15.0, ev_ebitda=8.0)
    monkeypatch.setattr("jmr_valuation.io.comps_loader.get_peer_multiples", lambda ticker: peer)
    table = load_comps_table(["AAA"])
    assert table.q1["pe"] == table.median["pe"] == table.q3["pe"] == pytest.approx(15.0)
