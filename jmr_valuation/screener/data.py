"""Acceso a datos del screener: universo de tickers, SEC EDGAR con cache en
disco y precios semanales.

- Universo: las listas del S&P 500 / 400 / 600 de Wikipedia (traen sector
  GICS), o una lista de tickers propia.
- SEC EDGAR: se reusa `SecEdgarClient` (y por lo tanto todo el mapeo de tags
  de sec_edgar_loader.py), agregando cache en disco (companyfacts pesa varios
  MB por empresa; re-correr el screen el mismo dia no deberia volver a bajar
  500 archivos) y un limitador de ritmo global -- la SEC corta a quien pasa
  de 10 pedidos/segundo.
- Precios: endpoint publico de graficos de Yahoo (el mismo que usa yfinance
  por dentro) pedido directo con requests. yfinance.download en lote
  devuelve YFRateLimitError con facilidad desde IPs de nube; un pedido
  liviano por ticker, con reintentos, es mas robusto.
"""
from __future__ import annotations

import hashlib
import io
import json
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import requests

from jmr_valuation.io.sec_edgar_client import SecEdgarClient

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_CACHE_DIR = PROJECT_ROOT / "data" / "screener_cache"

WIKI_UNIVERSES = {
    "sp500": "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
    "sp400": "https://en.wikipedia.org/wiki/List_of_S%26P_400_companies",
    "sp600": "https://en.wikipedia.org/wiki/List_of_S%26P_600_companies",
}
_BROWSER_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"


class RateLimiter:
    def __init__(self, per_second: float):
        self._interval = 1.0 / per_second
        self._lock = threading.Lock()
        self._next = 0.0

    def wait(self) -> None:
        with self._lock:
            now = time.monotonic()
            delay = self._next - now
            self._next = max(now, self._next) + self._interval
        if delay > 0:
            time.sleep(delay)


class CachedSecEdgarClient(SecEdgarClient):
    """SecEdgarClient + cache JSON en disco (vence a los `max_age_days`)."""

    def __init__(self, user_agent: str | None = None, cache_dir: Path = DEFAULT_CACHE_DIR,
                 max_age_days: float = 7, per_second: float = 8):
        super().__init__(user_agent)
        self.cache_dir = Path(cache_dir) / "sec"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.max_age = max_age_days * 86400
        self._limiter = RateLimiter(per_second)

    def _get(self, url: str, params: dict | None = None) -> dict:
        key = hashlib.sha1((url + json.dumps(params or {}, sort_keys=True)).encode()).hexdigest()
        path = self.cache_dir / f"{key}.json"
        if path.exists() and time.time() - path.stat().st_mtime < self.max_age:
            return json.loads(path.read_text(encoding="utf-8"))
        self._limiter.wait()
        data = super()._get(url, params)
        path.write_text(json.dumps(data), encoding="utf-8")
        return data


def load_universe(name: str) -> list[dict]:
    """[{ticker, name, sector, industry}] de una lista S&P de Wikipedia.
    Los tickers se normalizan al formato de SEC/Yahoo (BRK.B -> BRK-B)."""
    import pandas as pd

    url = WIKI_UNIVERSES[name]
    html = requests.get(url, headers={"User-Agent": _BROWSER_UA}, timeout=30).text
    table = next(t for t in pd.read_html(io.StringIO(html))
                 if any(str(c).lower() in ("symbol", "ticker symbol", "ticker") for c in t.columns))
    cols = {str(c).lower(): c for c in table.columns}
    sym = cols.get("symbol") or cols.get("ticker symbol") or cols.get("ticker")
    name_col = cols.get("security") or cols.get("company")
    sector = cols.get("gics sector")
    industry = cols.get("gics sub-industry") or cols.get("gics sub-industry[3]")
    out = []
    for _, row in table.iterrows():
        out.append({
            "ticker": str(row[sym]).strip().replace(".", "-").upper(),
            "name": str(row[name_col]) if name_col is not None else "",
            "sector": str(row[sector]) if sector is not None else "",
            "industry": str(row[industry]) if industry is not None else "",
        })
    return out


_price_limiter = RateLimiter(4)


@dataclass(frozen=True)
class PriceHistory:
    prices: list[tuple[str, float]]   # (fecha ISO, cierre), el mas viejo primero; el ultimo = precio actual
    splits: list[tuple[str, float]]   # (fecha ISO, factor) -- 25.0 = split 25:1


def fetch_price_history(ticker: str, years: int = 11, retries: int = 5) -> PriceHistory | None:
    """Cierres semanales ajustados por splits pero no por dividendos (el
    'close' del endpoint de graficos de Yahoo) + los splits del periodo.
    None si Yahoo no tiene el ticker o no respondio."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    params = {"range": f"{years}y", "interval": "1wk", "includeAdjustedClose": "false", "events": "split"}
    for attempt in range(retries):
        _price_limiter.wait()
        try:
            # Con un User-Agent de navegador completo Yahoo responde 429 desde
            # varias IPs; el generico "Mozilla/5.0" pasa.
            resp = requests.get(url, params=params, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
        except requests.RequestException:
            resp = None
        if resp is not None and resp.status_code == 200:
            result = (resp.json().get("chart", {}).get("result") or [None])[0]
            if not result or not result.get("timestamp"):
                return None
            closes = result["indicators"]["quote"][0].get("close") or []
            prices = [
                (_iso(ts), float(c)) for ts, c in zip(result["timestamp"], closes) if c is not None
            ]
            live = result.get("meta", {}).get("regularMarketPrice")
            if live and prices:
                prices[-1] = (prices[-1][0], float(live))
            splits = sorted(
                (_iso(sp["date"]), sp["numerator"] / sp["denominator"])
                for sp in (result.get("events", {}).get("splits") or {}).values()
                if sp.get("denominator")
            )
            return PriceHistory(prices=prices, splits=splits) if prices else None
        if resp is not None and resp.status_code == 404:
            return None
        time.sleep(2 ** attempt)
    return None


def _iso(ts: int) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).date().isoformat()
