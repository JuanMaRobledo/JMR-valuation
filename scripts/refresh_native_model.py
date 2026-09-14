#!/usr/bin/env python
"""Repuebla el modelo nativo del usuario (Income Statement/Balance Sheet/Cash
Flow Statement/Sector/Input sheet) con los datos REALES de la empresa que se
pida, sin tocar ninguna formula ni pestaña de calculo (Motor de Supuestos v2,
DCF v2, Valuation output, Crecimiento y Márgenes, EV/FCFF, etc.) -- esas
siguen leyendo de las celdas que este script actualiza, exactamente como ya
lo hacian con los datos pegados a mano de ADBE.

Uso:
    python scripts/refresh_native_model.py MSFT --sheet-id <id> \
        --industry-us "Software (System & Application)" \
        --industry-global "Software (System & Application)" \
        --peers ADBE ORCL CRM SAP GOOGL

Que SI toca (repuebla, no solo refresca LTM -- pensado para cambiar de
empresa, no solo actualizar la misma):
  - Input sheet: ticker (A1), nombre, pais, industria US/Global.
  - Income Statement: Revenue y EBIT, historico completo (10 años) + LTM.
  - Cash Flow Statement: D&A, historico completo + LTM.
  - Balance Sheet: Caja y deuda (corto/largo plazo), historico completo + LTM.
  - Solo columna LTM (no hay serie de 10 años limpia todavia): Interest
    Expense, Tasa impositiva efectiva, Equity (Income Statement L15/L29,
    Balance Sheet L35).
  - Sector: la fila de la empresa + cada peer (multiplos, margenes, CAGR).

Que NO toca: ninguna formula, ni las hojas de calculo/proyeccion. Tampoco
reescribe rotulos de texto sueltos en otras pestañas (p.ej. el titulo de
'Cualitativo' o 'Motor de Supuestos v2' A1) -- esos quedan con el nombre de
la empresa anterior hasta que se editen a mano; no afecta ningun calculo,
son solo etiquetas visuales.
"""
from __future__ import annotations

import argparse
import sys

from dataclasses import replace

from jmr_valuation.io.comps_loader import load_comps_table
from jmr_valuation.io.sec_edgar_client import SecEdgarError
from jmr_valuation.io.sec_edgar_loader import (
    load_annual_series_from_sec_edgar,
    load_company_inputs_from_sec_edgar,
)
from jmr_valuation.io.sheets_auth import get_gspread_client, open_target_sheet
from jmr_valuation.io.yfinance_client import PeerMultiples, get_market_snapshot, get_peer_multiples

_M = 1_000_000  # SEC EDGAR devuelve $ crudos; este Sheet trabaja en millones


def _history_row(values_raw: list[float], ltm_raw: float, *, scale: float = _M, decimals: int = 1) -> list[float]:
    """Arma B:L (10 años + LTM) a partir de una serie de hasta 10 años (la mas
    vieja primero) -- si hay menos de 10, se alinea a la derecha (terminando
    en K, el año mas reciente) y se dejan en blanco las columnas mas viejas
    que no tienen dato, en vez de desalinear el historico existente."""
    values = [round(v / scale, decimals) for v in values_raw]
    padded = [""] * (10 - len(values)) + values if len(values) < 10 else values[-10:]
    return padded + [round(ltm_raw / scale, decimals)]


def refresh_input_sheet(sh, ticker: str, company_inputs, industry_us: str, industry_global: str) -> None:
    ws = sh.worksheet("Input sheet")
    ws.update(values=[[ticker]], range_name="A1")
    ws.update(values=[[company_inputs.company_name]], range_name="B5")
    ws.update(values=[[company_inputs.country_of_incorporation]], range_name="B8")
    ws.update(values=[[industry_us]], range_name="B9")
    ws.update(values=[[industry_global]], range_name="B10")


def refresh_income_statement(sh, series, company_inputs) -> None:
    """OJO: 'Operating Margin' (fila 13) y 'EBITDA' (fila 28) de esta hoja NO
    son formulas -- son valores pegados de cuando se cargo ADBE. Si no se
    reescriben aca, 'Crecimiento y Márgenes' (que lee la mediana de la fila
    13) queda mostrando el margen de la empresa VIEJA aunque Revenue/EBIT ya
    se hayan actualizado -- confirmado corriendo esto con MSFT antes de este
    fix (el margen 'actual' recalculaba bien via 'Valuation output', pero el
    'mediano historico' seguia en el numero de ADBE)."""
    ws = sh.worksheet("Income Statement")
    ws.update(values=[_history_row(series.revenue, series.ltm_revenue)], range_name="B3")
    ws.update(values=[_history_row(series.ebit, series.ltm_ebit)], range_name="B12")

    margins = [e / r for e, r in zip(series.ebit, series.revenue) if r]
    ltm_margin = series.ltm_ebit / series.ltm_revenue if series.ltm_revenue else margins[-1]
    ws.update(values=[_history_row(margins, ltm_margin, scale=1, decimals=4)], range_name="B13")

    ebitda = [e + d for e, d in zip(series.ebit, series.da)]
    ws.update(values=[_history_row(ebitda, series.ltm_ebit + series.ltm_da)], range_name="B28")

    # Interest Expense en esta hoja se guarda en NEGATIVO (fila 15, ver B15:K15) -- solo LTM, sin serie de 10y limpia.
    ws.update(values=[[-round(company_inputs.interest_expense_ltm, 1)]], range_name="L15")
    ws.update(values=[[round(company_inputs.effective_tax_rate, 4)]], range_name="L29")
    # Shares Outstanding LTM (fila 27) -- 'Input sheet'!B22 y de ahi todo el bridge de equity
    # (incluido DCF v2!B32) leen de esta celda. Sin esto, el valor por accion queda dividido
    # por las acciones de la empresa ANTERIOR -- confirmado corriendo esto con MSFT.
    ws.update(values=[[round(company_inputs.shares_outstanding, 1)]], range_name="L27")


def refresh_cash_flow_statement(sh, series) -> None:
    ws = sh.worksheet("Cash Flow Statement")
    ws.update(values=[_history_row(series.da, series.ltm_da)], range_name="B4")


def refresh_balance_sheet(sh, series, company_inputs) -> None:
    ws = sh.worksheet("Balance Sheet")
    ws.update(values=[_history_row(series.cash, company_inputs.cash_ltm * _M)], range_name="B5")
    ws.update(values=[_history_row(series.current_debt, series.current_debt[-1])], range_name="B20")
    ws.update(values=[_history_row(series.long_term_debt, series.long_term_debt[-1])], range_name="B25")
    ws.update(values=[[round(company_inputs.book_value_equity_ltm, 1)]], range_name="L35")


_SECTOR_MAX_ROWS = 10  # filas 2-11: el rango mas ancho que usan Promedio/Mediana (p.ej. C2:C11)


def _fill_revenue_cagr_gaps_from_edgar(p: PeerMultiples) -> PeerMultiples:
    """yfinance solo trae ~4 años de historico anual -- alcanza para CAGR 3y,
    no para 5y/10y (quedan en None, ver yfinance_client.py). Si se dejan en
    blanco, 'Sector'!Promedio/Mediana (AVERAGE/MEDIAN sobre TODA la columna)
    da #DIV/0!/#NUM! cuando TODOS los peers los tienen en blanco -- lo que
    a su vez rompe los cuartiles de industria de 'Crecimiento y Márgenes'.
    SEC EDGAR si tiene 10 años reales para cualquier ticker (ya lo usamos
    para la empresa principal) -- se completa el hueco con eso, no se
    inventa nada."""
    if p.revenue_cagr_5y is not None and p.revenue_cagr_10y is not None:
        return p
    try:
        series = load_annual_series_from_sec_edgar(p.ticker)
    except SecEdgarError:
        return p  # sin historico de EDGAR (p.ej. ADR que no presenta 10-K) -- queda en blanco, no se inventa

    revenue = series.revenue
    def _cagr(n: int) -> float | None:
        n = min(n, len(revenue) - 1)
        if n < 1 or revenue[-1 - n] <= 0:
            return None
        return (revenue[-1] / revenue[-1 - n]) ** (1 / n) - 1

    return replace(
        p,
        revenue_cagr_5y=p.revenue_cagr_5y if p.revenue_cagr_5y is not None else _cagr(5),
        revenue_cagr_10y=p.revenue_cagr_10y if p.revenue_cagr_10y is not None else _cagr(len(revenue) - 1),
    )


def refresh_sector(sh, ticker: str, peer_tickers: list[str]) -> None:
    ws = sh.worksheet("Sector")
    own = _fill_revenue_cagr_gaps_from_edgar(get_peer_multiples(ticker))
    comps = load_comps_table(peer_tickers)
    peers = [_fill_revenue_cagr_gaps_from_edgar(p) for p in comps.peers]

    def _row(p) -> list:
        return [
            p.company_name, p.ticker,
            round((p.market_cap or 0) / _M, 2), p.gross_margin, p.forward_pe, p.pe,
            p.ev_fcf, p.p_fcf, p.ev_ebitda, p.p_ocf, p.operating_margin,
            p.revenue_cagr_3y, p.revenue_cagr_5y, p.revenue_cagr_10y,
        ]

    rows = [_row(own)] + [_row(p) for p in peers]
    if len(rows) > _SECTOR_MAX_ROWS:
        raise ValueError(
            f"Se pasaron {len(rows) - 1} peers + la empresa -- el rango de 'Promedio'/'Mediana' "
            f"de esta hoja solo cubre {_SECTOR_MAX_ROWS} filas (2-{1 + _SECTOR_MAX_ROWS}). Reduci la lista de peers."
        )

    # Limpia TODO el rango de filas antes de escribir (solo VALORES, con
    # batch_clear -- no pisa el formato de porcentaje/numero de las celdas,
    # a diferencia de escribir strings vacios con update()). Si la corrida
    # anterior tenia mas peers que esta (p.ej. veniamos de 8 filas y ahora
    # son 6), las filas sobrantes quedaban con datos VIEJOS y contaminaban
    # Promedio/Mediana (confirmado: quedo un SAP duplicado y un NOW que ya
    # no eran peers de la empresa nueva, mezclados en los promedios).
    ws.batch_clear([f"A2:N{1 + _SECTOR_MAX_ROWS}"])
    ws.update(values=rows, range_name="A2")


def run(
    ticker: str, *, sheet_id: str, peer_tickers: list[str], industry_us: str, industry_global: str,
) -> None:
    print(f"[1/5] Descargando historico de 10y de {ticker} desde SEC EDGAR...")
    series = load_annual_series_from_sec_edgar(ticker)
    market = get_market_snapshot(ticker)
    company_inputs = load_company_inputs_from_sec_edgar(
        ticker, current_price=market.current_price, riskfree_rate=0.04, initial_cost_of_capital=0.09,
    )

    client = get_gspread_client()
    sh = open_target_sheet(client, sheet_id)

    print(f"[2/5] Actualizando Input sheet (ticker={ticker}, industria={industry_us})...")
    refresh_input_sheet(sh, ticker, company_inputs, industry_us, industry_global)

    print("[3/5] Repoblando historico completo de Income Statement / Cash Flow Statement / Balance Sheet...")
    refresh_income_statement(sh, series, company_inputs)
    refresh_cash_flow_statement(sh, series)
    refresh_balance_sheet(sh, series, company_inputs)

    print(f"[4/5] Refrescando pestaña Sector ({ticker} + {', '.join(peer_tickers)})...")
    refresh_sector(sh, ticker, peer_tickers)

    print(f"[5/5] Listo: {sh.url}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ticker")
    parser.add_argument("--sheet-id", required=True)
    parser.add_argument("--peers", nargs="+", required=True)
    parser.add_argument("--industry-us", required=True)
    parser.add_argument("--industry-global", required=True)
    args = parser.parse_args(argv)
    run(
        args.ticker.upper(), sheet_id=args.sheet_id, peer_tickers=args.peers,
        industry_us=args.industry_us, industry_global=args.industry_global,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
