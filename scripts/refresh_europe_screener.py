#!/usr/bin/env python
"""Merge European snapshots into the published screener, preserving US rows.
Usage: python scripts/refresh_europe_screener.py --json-out path/resultados.json
"""
from __future__ import annotations
import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from jmr_valuation.screener.europe import EUROPE, screen_europe


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--json-out', type=Path, required=True)
    p.add_argument('--workers', type=int, default=3)
    args = p.parse_args()
    payload = json.loads(args.json_out.read_text(encoding='utf-8'))
    rows = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(screen_europe, c) for c in EUROPE]
        for fut in as_completed(futures):
            r = fut.result()
            rows.append(r)
            print(f"{len(rows)}/{len(EUROPE)} {r['ticker']} {r['tier']} {r.get('error') or ''}", flush=True)
    errors = sum(bool(r.get('error')) for r in rows)
    quoted = sum(bool((r.get('valuation') or {}).get('price')) for r in rows)
    # Never replace a healthy published screen during a provider outage.
    if errors > len(rows) * .2 or quoted < len(rows) * .8:
        raise RuntimeError(f'European provider incomplete: {errors} errors, {quoted}/{len(rows)} prices. Output unchanged.')
    us = [r for r in payload['results'] if r.get('region') != 'Europa']
    for r in us:
        r.setdefault('region', 'EE. UU.')
        r.setdefault('currency', 'USD')
        r.setdefault('fundamentals_as_of', payload.get('generated'))
    base = payload.get('us_universe') or payload.get('universe', 'S&P 500').split(' + Europa')[0]
    now = datetime.now(timezone.utc).date().isoformat()
    payload.update(us_universe=base, universe=base + f' + Europa (selección de {len(EUROPE)} valores)',
                   europe_generated=now,
                   source='EE. UU.: SEC EDGAR + Yahoo; Europa: Yahoo Finance, historia anual parcial',
                   europe_coverage=dict(selected=len(rows), with_prices=quoted, errors=errors,
                       countries=len({r['country'] for r in rows}), selection='Selección propia; no replica un índice'),
                   results=us + sorted(rows, key=lambda r: (bool(r.get('error')), r['country'], r['name'])))
    temp = args.json_out.with_suffix('.tmp')
    temp.write_text(json.dumps(payload, ensure_ascii=False, indent=1, allow_nan=False)+'\n', encoding='utf-8')
    temp.replace(args.json_out)
    print(json.dumps(payload['europe_coverage']))

if __name__ == '__main__':
    main()
