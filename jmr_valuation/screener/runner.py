"""Orquesta el screen: universo -> SEC EDGAR -> metricas -> puntaje ->
precio vs historia -> ranking. Escribe CSV, JSON (lo consume la pagina
screener.html de Modelo-JMR) y un resumen en Markdown."""
from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Callable

from jmr_valuation.io.sec_edgar_client import SecEdgarError, _ticker_to_cik
from jmr_valuation.io.sec_edgar_loader import load_annual_series_from_sec_edgar
from jmr_valuation.screener import scoring
from jmr_valuation.screener.data import CachedSecEdgarClient, fetch_price_history
from jmr_valuation.screener.metrics import compute_metrics
from jmr_valuation.screener.valuation import value_snapshot

# Bancos, aseguradoras, REITs y demas financieras (SIC 6000-6799): el ROIC y
# el FCF no tienen lectura para ellas -- la metodologia las valora con P/VL y
# ROE (Paso 4), asi que se reportan aparte en vez de puntuarlas mal.
FINANCIAL_SIC = range(6000, 6800)
EXCLUDED = "Excluida (financiera)"
ERROR = "Sin datos"


@dataclass
class ScreenResult:
    ticker: str
    name: str
    sector: str = ""
    industry: str = ""
    sic: str = ""
    tier: str = ERROR
    score: float | None = None
    error: str | None = None
    metrics: dict = field(default_factory=dict)
    quality: dict = field(default_factory=dict)
    valuation: dict | None = None
    series: object = field(default=None, repr=False)  # AnnualSeries, solo en memoria

    def as_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if k != "series"}


def screen_one(company: dict, client: CachedSecEdgarClient, with_prices: bool = True) -> ScreenResult:
    ticker = company["ticker"]
    res = ScreenResult(ticker=ticker, name=company.get("name", ""),
                       sector=company.get("sector", ""), industry=company.get("industry", ""))
    try:
        submissions = client.company_submissions(ticker)
        res.sic = str(submissions.get("sic") or "")
        res.name = res.name or submissions.get("name", "")
        if not res.industry:
            res.industry = submissions.get("sicDescription", "")
        if res.sic.isdigit() and int(res.sic) in FINANCIAL_SIC:
            res.tier = EXCLUDED
            return res
        series = load_annual_series_from_sec_edgar(ticker, client=client)
    except (SecEdgarError, KeyError, ValueError, ZeroDivisionError) as exc:
        res.error = str(exc)[:200]
        return res
    except Exception as exc:  # una empresa rara no debe tumbar un screen de 500
        res.error = f"{type(exc).__name__}: {str(exc)[:180]}"
        return res

    res.series = series
    metrics = compute_metrics(series)
    quality = scoring.score_metrics(metrics)
    res.metrics = metrics.as_dict()
    res.quality = {k: v for k, v in quality.__dict__.items() if k not in ("score", "tier")}
    res.score, res.tier = quality.score, quality.tier

    if with_prices:
        attach_valuation(res, series)
    return res


def attach_valuation(res: ScreenResult, series) -> None:
    history = fetch_price_history(res.ticker)
    if history is None:
        return
    snap = value_snapshot(series, history.prices, history.splits,
                          eps_growth=res.metrics.get("eps_cagr_5y"))
    res.valuation = snap.as_dict() if snap else None


def run_screen(companies: list[dict], *, client: CachedSecEdgarClient | None = None,
               with_prices: bool = True, workers: int = 6,
               progress: Callable[[int, int, ScreenResult], None] | None = None) -> list[ScreenResult]:
    client = client or CachedSecEdgarClient()
    _ticker_to_cik(client.user_agent)  # listado ticker->CIK una sola vez, antes de abrir los hilos
    results: list[ScreenResult] = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(screen_one, c, client, with_prices) for c in companies]
        for i, fut in enumerate(as_completed(futures), 1):
            r = fut.result()
            results.append(r)
            if progress:
                progress(i, len(companies), r)
    if with_prices:
        # Segunda pasada, secuencial, para los que Yahoo corto por ritmo.
        for r in results:
            if r.series is not None and r.valuation is None:
                attach_valuation(r, r.series)
    tier_rank = {label: i for i, (_, label) in enumerate(scoring.TIERS)}
    tier_rank.update({scoring.NOT_PASSING: 10, EXCLUDED: 11, ERROR: 12})
    results.sort(key=lambda r: (tier_rank.get(r.tier, 99), -(r.score or 0)))
    return results


# --- Salidas ---------------------------------------------------------------

def criteria_meta() -> dict:
    return {
        "hard_filters": {
            "min_years": scoring.MIN_YEARS,
            "min_roic_median_5y": scoring.MIN_ROIC_MEDIAN_5Y,
            "min_fcf_positive_last_5y": scoring.MIN_FCF_POSITIVE_LAST_5Y,
            "max_net_debt_to_ebitda": scoring.MAX_NET_DEBT_TO_EBITDA,
            "min_revenue_cagr_5y": scoring.MIN_REVENUE_CAGR_5Y,
        },
        "weights": [
            {"metric": m, "weight": w, "bad": b, "good": g, "group": grp}
            for m, w, b, g, grp in scoring.CRITERIA
        ],
        "tiers": [{"min_score": t, "label": label} for t, label in scoring.TIERS],
    }


def write_json(results: list[ScreenResult], path: Path, universe: str) -> None:
    payload = {
        "generated": date.today().isoformat(),
        "universe": universe,
        "source": "SEC EDGAR (companyfacts, 10-K) + precios semanales de Yahoo Finance",
        "criteria": criteria_meta(),
        "results": [r.as_dict() for r in results],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=1, default=float), encoding="utf-8")


def to_flat_rows(results: list[ScreenResult]) -> list[dict]:
    rows = []
    for r in results:
        row = {"ticker": r.ticker, "name": r.name, "sector": r.sector, "tier": r.tier, "score": r.score}
        row.update({k: v for k, v in r.metrics.items()})
        for k, v in (r.valuation or {}).items():
            if k == "multiples":
                for name, snap in v.items():
                    row[f"{name}"] = snap["current"]
                    row[f"{name}_hist"] = snap["median_hist"]
                    row[f"{name}_vs_hist"] = snap["vs_hist"]
            else:
                row[f"val_{k}"] = v
        row["failed_filters"] = " | ".join(r.quality.get("failed_filters", []))
        row["flags"] = " | ".join(r.quality.get("flags", []))
        row["error"] = r.error or ""
        rows.append(row)
    return rows


def write_csv(results: list[ScreenResult], path: Path) -> None:
    import pandas as pd

    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(to_flat_rows(results)).to_csv(path, index=False)


def _pct(x: float | None) -> str:
    return "-" if x is None else f"{x:.0%}"


def _x(x: float | None) -> str:
    return "-" if x is None else f"{x:.1f}x"


def markdown_summary(results: list[ScreenResult], universe: str, top: int = 40) -> str:
    counts: dict[str, int] = {}
    for r in results:
        counts[r.tier] = counts.get(r.tier, 0) + 1
    lines = [
        f"# Screener de empresas maravillosas -- {universe} ({date.today().isoformat()})",
        "",
        " · ".join(f"**{k}**: {v}" for k, v in counts.items()),
        "",
        "| # | Ticker | Empresa | Clase | Puntaje | ROIC 5a | Margen bruto | Margen FCF | Crec. ventas 5a | DN/EBITDA | FCF yield | P/FCF vs historia |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    shown = [r for r in results if r.quality.get("passes_filters")][:top]
    for i, r in enumerate(shown, 1):
        m, v = r.metrics, r.valuation or {}
        vs = v.get("p_fcf_vs_hist")
        lines.append(
            f"| {i} | {r.ticker} | {r.name[:28]} | {r.tier} | {r.score:.0f} | {_pct(m.get('roic_median_5y'))} | "
            f"{_pct(m.get('gross_margin_median_5y'))} | {_pct(m.get('fcf_margin_median_5y'))} | "
            f"{_pct(m.get('revenue_cagr_5y'))} | {_x(m.get('net_debt_to_ebitda'))} | {_pct(v.get('fcf_yield'))} | "
            f"{'-' if vs is None else f'{vs:+.0%}'} |"
        )
    return "\n".join(lines) + "\n"
