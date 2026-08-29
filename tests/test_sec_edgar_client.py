import pytest

from jmr_valuation.io.sec_edgar_client import SecEdgarClient, SecEdgarError, _ticker_to_cik


def test_client_raises_clear_error_without_user_agent(monkeypatch):
    monkeypatch.delenv("SEC_EDGAR_USER_AGENT", raising=False)
    monkeypatch.setattr("jmr_valuation.io.sec_edgar_client.load_dotenv", lambda: None)
    with pytest.raises(SecEdgarError, match="Falta SEC_EDGAR_USER_AGENT"):
        SecEdgarClient()


def test_client_accepts_explicit_user_agent():
    client = SecEdgarClient(user_agent="Test test@example.com")
    assert client.user_agent == "Test test@example.com"


class _FakeResponse:
    def __init__(self, status_code=200, json_data=None, text=""):
        self.status_code = status_code
        self.ok = status_code < 400
        self._json_data = json_data
        self.text = text

    def json(self):
        return self._json_data


def test_cik_for_ticker_resolves_from_sec_listing(monkeypatch):
    _ticker_to_cik.cache_clear()

    def fake_get(url, headers=None, params=None, timeout=None):
        assert "company_tickers.json" in url
        assert headers["User-Agent"] == "Test test@example.com"
        return _FakeResponse(json_data={"0": {"cik_str": 796343, "ticker": "ADBE", "title": "ADOBE INC."}})

    monkeypatch.setattr("jmr_valuation.io.sec_edgar_client.requests.get", fake_get)
    client = SecEdgarClient(user_agent="Test test@example.com")
    assert client.cik_for_ticker("adbe") == "0000796343"
    _ticker_to_cik.cache_clear()


def test_cik_for_unknown_ticker_raises_clear_error(monkeypatch):
    _ticker_to_cik.cache_clear()

    def fake_get(url, headers=None, params=None, timeout=None):
        return _FakeResponse(json_data={"0": {"cik_str": 796343, "ticker": "ADBE", "title": "ADOBE INC."}})

    monkeypatch.setattr("jmr_valuation.io.sec_edgar_client.requests.get", fake_get)
    client = SecEdgarClient(user_agent="Test test@example.com")
    with pytest.raises(SecEdgarError, match="No se encontro el ticker"):
        client.cik_for_ticker("NOPE")
    _ticker_to_cik.cache_clear()


def test_company_facts_uses_cik_directly_without_lookup(monkeypatch):
    calls = []

    def fake_get(url, headers=None, params=None, timeout=None):
        calls.append(url)
        return _FakeResponse(json_data={"cik": 796343, "facts": {}})

    monkeypatch.setattr("jmr_valuation.io.sec_edgar_client.requests.get", fake_get)
    client = SecEdgarClient(user_agent="Test test@example.com")
    client.company_facts("0000796343")
    assert calls == ["https://data.sec.gov/api/xbrl/companyfacts/CIK0000796343.json"]


def test_get_raises_on_error_status(monkeypatch):
    def fake_get(url, headers=None, params=None, timeout=None):
        return _FakeResponse(status_code=403, text="forbidden")

    monkeypatch.setattr("jmr_valuation.io.sec_edgar_client.requests.get", fake_get)
    client = SecEdgarClient(user_agent="Test test@example.com")
    with pytest.raises(SecEdgarError, match="403"):
        client.company_facts("0000796343")
