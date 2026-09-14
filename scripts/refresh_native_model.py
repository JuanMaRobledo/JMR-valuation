#!/usr/bin/env python
"""Refresca los datos EN VIVO del modelo nativo del usuario (Income Statement/
Balance Sheet/Cash Flow Statement columna LTM + pestaña Sector) sin tocar
ninguna formula ni pestaña de calculo (Motor de Supuestos v2, DCF v2,
Valuation output, EV/FCFF, etc.) -- esas siguen leyendo de las celdas que este
script actualiza, exactamente como ya lo hacian con los datos pegados a mano.

Uso:
    python scripts/refresh_native_model.py ADBE --sheet-id <id> \
        --peers INTU MSFT ORCL ADSK CRM SAP NOW

Que SI toca (todo columna 'LTM', la que cambia cada vez que corre):
  - Income Statement: Revenue, EBIT, Interest Expense, Net Income, Shares
    Outstanding, Effective Tax Rate.
  - Cash Flow Statement: D&A, CapEx.
  - Balance Sheet: Cash, Deuda corto/largo plazo, Equity.
  - Sector: la fila de la empresa + cada peer (multiplos, margenes, CAGR).

Que NO toca: el historico anual (columnas B:K, ya cargado con datos reales),
cualquier formula, y todas las hojas de calculo/proyeccion.
"""
from __future__ import annotations

import argparse
import sys

from jmr_valuation.io.comps_loader import load_comps_table
from jmr_valuation.io.sec_edgar_loader import (
    load_annual_series_from_sec_edgar,
    load_company_inputs_from_sec_edgar,
)
from jmr_valuation.io.sheets_auth import get_gspread_client, open_target_sheet
from jmr_valuation.io.yfinance_client import get_market_snapshot, get_peer_multiples

_M = 1_000_000  # SEC EDGAR devuelve $ crudos; este Sheet trabaja en millones


def refresh_income_statement(sh, series, company_inputs) -> None:
    ws = sh.worksheet("Income Statement")
    ws.update(values=[[
        round(series.ltm_revenue / _M, 1)],
    ], range_name="L3")
    ws.update(values=[[round(series.ltm_ebit / _M, 1)]], range_name="L12")
    # Interest Expense en esta hoja se guarda en NEGATIVO (fila 15, ver B15:K15).
    ws.update(values=[[-round(company_inputs.interest_expense_ltm, 1)]], range_name="L15")
    ws.update(values=[[round(company_inputs.effective_tax_rate, 4)]], range_name="L29")


def refresh_cash_flow_statement(sh, series) -> None:
    ws = sh.worksheet("Cash Flow Statement")
    ws.update(values=[[round(series.ltm_da / _M, 1)]], range_name="L4")


def refresh_balance_sheet(sh, series, company_inputs) -> None:
    ws = sh.worksheet("Balance Sheet")
    ws.update(values=[[round(company_inputs.cash_ltm, 1)]], range_name="L5")
    ws.update(values=[[round(series.current_debt[-1] / _M, 1)]], range_name="L20")
    ws.update(values=[[round(series.long_term_debt[-1] / _M, 1)]], range_name="L25")
    ws.update(values=[[round(company_inputs.book_value_equity_ltm, 1)]], range_name="L35")


def refresh_sector(sh, ticker: str, peer_tickers: list[str]) -> None:
    ws = sh.worksheet("Sector")
    own = get_peer_multiples(ticker)
    comps = load_comps_table(peer_tickers)

    def _row(p) -> list:
        return [
            p.company_name, p.ticker,
            round((p.market_cap or 0) / _M, 2), p.gross_margin, p.forward_pe, p.pe,
            p.ev_fcf, p.p_fcf, p.ev_ebitda, p.p_ocf, p.operating_margin,
            p.revenue_cagr_3y, p.revenue_cagr_5y, p.revenue_cagr_10y,
        ]

    rows = [_row(own)] + [_row(p) for p in comps.peers]
    ws.update(values=rows, range_name="A2")


def run(ticker: str, *, sheet_id: str, peer_tickers: list[str]) -> None:
    print(f"[1/4] Descargando historico + LTM de {ticker} desde SEC EDGAR...")
    series = load_annual_series_from_sec_edgar(ticker)
    market = get_market_snapshot(ticker)
    company_inputs = load_company_inputs_from_sec_edgar(
        ticker, current_price=market.current_price, riskfree_rate=0.04, initial_cost_of_capital=0.09,
    )

    client = get_gspread_client()
    sh = open_target_sheet(client, sheet_id)

    print("[2/4] Refrescando columna LTM de Income Statement / Cash Flow Statement / Balance Sheet...")
    refresh_income_statement(sh, series, company_inputs)
    refresh_cash_flow_statement(sh, series)
    refresh_balance_sheet(sh, series, company_inputs)

    print(f"[3/4] Refrescando pestaña Sector ({ticker} + {', '.join(peer_tickers)})...")
    refresh_sector(sh, ticker, peer_tickers)

    print(f"[4/4] Listo: {sh.url}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ticker")
    parser.add_argument("--sheet-id", required=True)
    parser.add_argument("--peers", nargs="+", required=True)
    args = parser.parse_args(argv)
    run(args.ticker.upper(), sheet_id=args.sheet_id, peer_tickers=args.peers)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
