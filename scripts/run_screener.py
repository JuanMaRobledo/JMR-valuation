#!/usr/bin/env python
"""Screener de "empresas maravillosas": recorre un universo de acciones y
las ordena por calidad de negocio (ROIC alto y sostenido, margenes, caja,
crecimiento, balance, uso del capital) y por precio vs su propia historia.

Uso:
    python scripts/run_screener.py                      # S&P 1500
    python scripts/run_screener.py --universe sp400     # mid caps
    python scripts/run_screener.py --universe sp1500    # 500 + 400 + 600
    python scripts/run_screener.py --tickers AAPL MSFT V MA ADBE
    python scripts/run_screener.py --tickers-file mis_tickers.txt
    python scripts/run_screener.py --json-out ../Modelo-JMR/docs/screener/resultados.json

Requiere SEC_EDGAR_USER_AGENT en .env (ver .env.example). La primera corrida
del S&P 500 tarda unos minutos (baja ~1.000 archivos de la SEC); las
siguientes, dentro de 7 dias, salen del cache en data/screener_cache/.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from jmr_valuation.screener.data import DEFAULT_CACHE_DIR, UNIVERSES, CachedSecEdgarClient, load_universe  # noqa: E402
from jmr_valuation.screener.runner import markdown_summary, run_screen, write_csv, write_json  # noqa: E402

OUT_DIR = Path(__file__).resolve().parent.parent / "data" / "screener"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = p.add_mutually_exclusive_group()
    src.add_argument("--universe", choices=sorted(UNIVERSES), default="sp1500")
    src.add_argument("--tickers", nargs="+", help="lista de tickers (formato SEC/Yahoo: BRK-B)")
    src.add_argument("--tickers-file", type=Path, help="archivo con un ticker por linea")
    p.add_argument("--no-prices", action="store_true", help="solo calidad, sin precio vs historia")
    p.add_argument("--workers", type=int, default=6)
    p.add_argument("--max-cache-age-days", type=float, default=7)
    p.add_argument("--limit", type=int, help="procesar solo los primeros N (para probar)")
    p.add_argument("--json-out", type=Path, default=OUT_DIR / "resultados.json")
    p.add_argument("--csv-out", type=Path, default=OUT_DIR / "resultados.csv")
    p.add_argument("--md-out", type=Path, default=OUT_DIR / "resumen.md")
    args = p.parse_args(argv)

    if args.tickers or args.tickers_file:
        raw = args.tickers or [
            line.split("#")[0].strip() for line in args.tickers_file.read_text(encoding="utf-8").splitlines()
        ]
        companies = [{"ticker": t.upper().replace(".", "-")} for t in raw if t]
        universe_label = "lista propia"
    else:
        companies = load_universe(args.universe)
        universe_label = {"sp500": "S&P 500", "sp400": "S&P 400", "sp600": "S&P 600", "sp1500": "S&P 1500 (500 + 400 + 600)"}[args.universe]
    if args.limit:
        companies = companies[: args.limit]

    client = CachedSecEdgarClient(cache_dir=DEFAULT_CACHE_DIR, max_age_days=args.max_cache_age_days)

    def progress(i: int, n: int, r) -> None:
        detail = r.error or (f"{r.score:.0f}" if r.score is not None else "")
        print(f"[{i:>4}/{n}] {r.ticker:<7} {r.tier:<22} {detail}", flush=True)

    results = run_screen(companies, client=client, with_prices=not args.no_prices,
                         workers=args.workers, progress=progress)

    write_json(results, args.json_out, universe_label)
    write_csv(results, args.csv_out)
    summary = markdown_summary(results, universe_label)
    args.md_out.parent.mkdir(parents=True, exist_ok=True)
    args.md_out.write_text(summary, encoding="utf-8")
    print()
    print(summary)
    print(f"JSON: {args.json_out}\nCSV:  {args.csv_out}\nMD:   {args.md_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
