import pytest

from jmr_valuation.io.description_fetch import fetch_company_description_es


class _FakeResponse:
    def __init__(self, status_code=200, json_data=None):
        self.status_code = status_code
        self._json_data = json_data or {}

    def raise_for_status(self):
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")

    def json(self):
        return self._json_data


def test_fetch_returns_none_for_blank_company_name():
    assert fetch_company_description_es("   ") is None


def test_fetch_returns_extract_when_article_found(monkeypatch):
    def fake_get(url, params=None, headers=None, timeout=None):
        if "api.php" in url:
            return _FakeResponse(json_data={"query": {"search": [{"title": "Adobe Inc."}]}})
        assert "Adobe" in url
        return _FakeResponse(json_data={"type": "standard", "extract": "Adobe es una empresa de software."})

    monkeypatch.setattr("jmr_valuation.io.description_fetch.requests.get", fake_get)
    result = fetch_company_description_es("Adobe")
    assert result == "Adobe es una empresa de software."


def test_fetch_returns_none_when_no_search_results(monkeypatch):
    def fake_get(url, params=None, headers=None, timeout=None):
        return _FakeResponse(json_data={"query": {"search": []}})

    monkeypatch.setattr("jmr_valuation.io.description_fetch.requests.get", fake_get)
    assert fetch_company_description_es("EmpresaQueNoExiste123") is None


def test_fetch_returns_none_for_disambiguation_page(monkeypatch):
    def fake_get(url, params=None, headers=None, timeout=None):
        if "api.php" in url:
            return _FakeResponse(json_data={"query": {"search": [{"title": "Mercurio"}]}})
        return _FakeResponse(json_data={"type": "disambiguation", "extract": "Mercurio puede referirse a..."})

    monkeypatch.setattr("jmr_valuation.io.description_fetch.requests.get", fake_get)
    assert fetch_company_description_es("Mercurio") is None


def test_fetch_rejects_unrelated_result_for_ambiguous_short_query(monkeypatch):
    # caso real: buscar el ticker "ADBE" (sin nombre completo de empresa) puede
    # traer un articulo de Wikipedia totalmente ajeno via full-text search --
    # no debe devolverse como si fuera una descripcion valida.
    def fake_get(url, params=None, headers=None, timeout=None):
        assert "api.php" in url
        return _FakeResponse(json_data={"query": {"search": [{"title": "Adopcion homoparental"}]}})

    monkeypatch.setattr("jmr_valuation.io.description_fetch.requests.get", fake_get)
    assert fetch_company_description_es("ADBE") is None


def test_fetch_returns_none_on_404_summary(monkeypatch):
    def fake_get(url, params=None, headers=None, timeout=None):
        if "api.php" in url:
            return _FakeResponse(json_data={"query": {"search": [{"title": "Titulo Fantasma"}]}})
        return _FakeResponse(status_code=404)

    monkeypatch.setattr("jmr_valuation.io.description_fetch.requests.get", fake_get)
    assert fetch_company_description_es("Titulo Fantasma") is None
