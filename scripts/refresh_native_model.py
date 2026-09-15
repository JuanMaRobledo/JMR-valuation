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
  - Income Statement: Revenue, EBIT, Operating Margin, EBITDA, Provision for
    Income Taxes, Net Income, EPS (basico/diluido), Acciones (puntuales y
    diluidas promedio) -- historico completo (10 años) + LTM.
  - Cash Flow Statement: D&A, Net Income, OCF, CapEx, Recompras, Dividendos,
    Free Cash Flow -- historico completo + LTM.
  - Balance Sheet: Caja y deuda (corto/largo plazo), historico completo + LTM.
  - Trailing Valuation / Forward Valuation: precio de cierre historico real
    (nuevo, yfinance), Market Cap, Enterprise Value, y los ~20 multiplos
    derivados (P/E, EV/EBITDA, P/OCF, EV/FCF, yields, etc.) -- estas dos
    hojas eran ENTERAMENTE valores pegados de ADBE, nunca refrescadas antes;
    son el default del multiplo de salida de los 3 escenarios en las 5
    hojas EV/FCFF, P/OCF, P/E, P/FCFE, EV/EBITDA (ver
    refresh_trailing_valuation). P/B (fila 18 de Trailing Valuation) queda
    sin tocar -- no hay serie de Book Value historico completa todavia.
  - Solo columna LTM (no hay serie de 10 años limpia todavia): Interest
    Expense, Tasa impositiva efectiva, Equity (Income Statement L15/L29,
    Balance Sheet L35).
  - Sector: la fila de la empresa + cada peer (multiplos, margenes, CAGR).

Que NO toca: ninguna formula, ni las hojas de calculo/proyeccion. Tampoco
reescribe rotulos de texto sueltos en otras pestañas (p.ej. el titulo de
'Cualitativo' o 'Motor de Supuestos v2' A1) -- esos quedan con el nombre de
la empresa anterior hasta que se editen a mano; no afecta ningun calculo,
son solo etiquetas visuales.

Cada hoja se escribe con UN solo batch_update (no una llamada de API por
fila) -- con 'Trailing Valuation'/'Forward Valuation' sumando ~35 filas mas,
escribir fila por fila pegaba contra el limite de "Write requests per minute
per user" de la API de Sheets (429) a mitad de una corrida."""
from __future__ import annotations

import argparse
import sys

from dataclasses import dataclass, replace

from jmr_valuation.io.comps_loader import load_comps_table
from jmr_valuation.io.sec_edgar_client import SecEdgarError
from jmr_valuation.io.sec_edgar_loader import (
    load_annual_series_from_sec_edgar,
    load_company_inputs_from_sec_edgar,
)
from jmr_valuation.io.sheets_auth import get_gspread_client, open_target_sheet
from jmr_valuation.io.yfinance_client import (
    PeerMultiples,
    get_historical_close_prices,
    get_market_snapshot,
    get_peer_multiples,
)

_M = 1_000_000  # SEC EDGAR devuelve $ crudos; este Sheet trabaja en millones


def _apply(ws, updates: list[tuple[str, list]]) -> None:
    """Aplica todas las escrituras de una hoja en UNA sola llamada a la API
    (ver docstring del modulo -- fila por fila se pegaba contra el limite de
    'Write requests per minute' con las ~35 filas nuevas de Trailing/Forward
    Valuation)."""
    ws.batch_update([{"range": r, "values": v} for r, v in updates])


def _history_row(values_raw: list[float], ltm_raw: float, *, scale: float = _M, decimals: int = 1) -> list[float]:
    """Arma B:L (10 años + LTM) a partir de una serie de hasta 10 años (la mas
    vieja primero) -- si hay menos de 10, se alinea a la derecha (terminando
    en K, el año mas reciente) y se dejan en blanco las columnas mas viejas
    que no tienen dato, en vez de desalinear el historico existente."""
    values = [round(v / scale, decimals) for v in values_raw]
    padded = [""] * (10 - len(values)) + values if len(values) < 10 else values[-10:]
    return padded + [round(ltm_raw / scale, decimals)]


def _ratio_row(values: list[float | None], ltm: float | None, *, scale: float = 1, decimals: int = 2) -> list:
    """Como _history_row, pero tolera None (un año sin dato -- p.ej. la
    empresa aun no cotizaba en bolsa en ese cierre de ejercicio, o el
    denominador de un ratio dio cero) escribiendolo en blanco en vez de
    reventar. Usado para 'Trailing Valuation'/'Forward Valuation' (precio
    historico y los multiplos que se arman con el)."""
    def _fmt(v: float | None) -> float | str:
        return "" if v is None else round(v / scale, decimals)

    formatted = [_fmt(v) for v in values]
    padded = ([""] * (10 - len(formatted)) + formatted) if len(formatted) < 10 else formatted[-10:]
    return padded + [_fmt(ltm)]


def _safe_div(a: float | None, b: float | None) -> float | None:
    return a / b if (a is not None and b) else None


def refresh_input_sheet(sh, ticker: str, company_inputs, industry_us: str, industry_global: str) -> None:
    ws = sh.worksheet("Input sheet")
    _apply(ws, [
        ("A1", [[ticker]]),
        ("B5", [[company_inputs.company_name]]),
        ("B8", [[company_inputs.country_of_incorporation]]),
        ("B9", [[industry_us]]),
        ("B10", [[industry_global]]),
    ])


def refresh_resumen_valoracion(sh, market) -> None:
    """'Resumen de Valoración'!C25 ('Precio al Día del Análisis') es un VALOR
    ESTATICO a proposito, no una formula -- 'Precio de Hoy' (B24) ya esta
    siempre vivo via GOOGLEFINANCE ('Input sheet'!D1), asi que si esta celda
    tambien fuera una formula ambas mostrarian siempre el mismo numero. Al
    quedar congelada con el precio de mercado del momento exacto en que se
    corre este script, el usuario puede volver dias despues y comparar el
    precio de HOY contra el que habia cuando se hizo el analisis."""
    ws = sh.worksheet("Resumen de Valoración")
    _apply(ws, [("C25", [[round(market.current_price, 2)]])])


def refresh_income_statement(sh, series, company_inputs) -> None:
    """OJO: 'Operating Margin' (fila 13) y 'EBITDA' (fila 28) de esta hoja NO
    son formulas -- son valores pegados de cuando se cargo ADBE. Si no se
    reescriben aca, 'Crecimiento y Márgenes' (que lee la mediana de la fila
    13) queda mostrando el margen de la empresa VIEJA aunque Revenue/EBIT ya
    se hayan actualizado -- confirmado corriendo esto con MSFT antes de este
    fix (el margen 'actual' recalculaba bien via 'Valuation output', pero el
    'mediano historico' seguia en el numero de ADBE)."""
    ws = sh.worksheet("Income Statement")
    updates: list[tuple[str, list]] = []
    updates.append(("B3", [_history_row(series.revenue, series.ltm_revenue)]))
    updates.append(("B12", [_history_row(series.ebit, series.ltm_ebit)]))

    margins = [e / r for e, r in zip(series.ebit, series.revenue) if r]
    ltm_margin = series.ltm_ebit / series.ltm_revenue if series.ltm_revenue else margins[-1]
    updates.append(("B13", [_history_row(margins, ltm_margin, scale=1, decimals=4)]))

    # Total Revenues %Chg (fila 4) -- MISMO bug que Operating Margin/EBITDA:
    # valor pegado de ADBE, nunca refrescado. 'Input sheet'!B27 (crecimiento
    # para el proximo año, el driver #1 del escenario Base) y 'Valuation
    # output' (filas 49/100/151, candidatos de crecimiento Conservador/
    # Optimista) leen esta fila directo -- en blanco, ambos quedan en 0 o en
    # #DIV/0!, degenerando los 3 escenarios (confirmado con MSFT: el precio
    # objetivo Conservador salia MAS ALTO que el Base).
    growth = [r2 / r1 - 1 for r1, r2 in zip(series.revenue, series.revenue[1:]) if r1]
    ltm_growth = series.ltm_revenue / series.revenue[-1] - 1 if series.revenue[-1] else 0.0
    updates.append(("B4", [_history_row(growth, ltm_growth, scale=1, decimals=4)]))

    ebitda = [e + d for e, d in zip(series.ebit, series.da)]
    updates.append(("B28", [_history_row(ebitda, series.ltm_ebit + series.ltm_da)]))

    # Interest Expense en esta hoja se guarda en NEGATIVO (fila 15, ver B15:K15) -- solo LTM, sin serie de 10y limpia.
    updates.append(("L15", [[-round(company_inputs.interest_expense_ltm, 1)]]))
    updates.append(("L29", [[round(company_inputs.effective_tax_rate, 4)]]))

    # Shares Outstanding puntuales (fila 27, a cierre de cada ejercicio) --
    # 'Input sheet'!B22 y de ahi todo el bridge de equity (incluido DCF
    # v2!B32) leen la columna LTM de esta fila. Sin esto, el valor por
    # accion queda dividido por las acciones de la empresa ANTERIOR --
    # confirmado corriendo esto con MSFT.
    updates.append(("B27", [_history_row(series.shares_outstanding, company_inputs.shares_outstanding * _M)]))

    # Provision for Income Taxes / Net Income (filas 20-22) y Acciones
    # Diluidas Promedio (fila 26) -- MISMO bug que Operating Margin/EBITDA de
    # arriba: eran valores pegados de ADBE, nunca refrescados. Esto alimenta
    # 'Financials Multiples'!fila 13 (Taxes historicos) y fila 31 (Diluted
    # Shares Outstanding, la base de TODOS los "per share": FCFF/OCF/FCFE/EPS
    # por accion, tanto historico como proyectado). Confirmado con MSFT: sin
    # este fix, 'Financials Multiples' dividia el FCFF/OCF/Net Income REAL de
    # MSFT por las ~427-459M acciones de ADBE en vez de sus ~7.450-7.830M
    # reales (17x mas chicas) -- inflando cada "per share"/EPS en ese mismo
    # orden y arruinando los multiplos de las 5 hojas EV/FCFF, P/OCF, P/E,
    # P/FCFE y EV/EBITDA (P/E terminaba en 0,9x en vez de ~30x).
    updates.append(("B20", [_history_row(series.tax_expense, series.ltm_tax_expense)]))
    updates.append(("B21", [_history_row(series.net_income, series.ltm_net_income)]))
    updates.append(("B22", [_history_row(series.net_income, series.ltm_net_income)]))
    updates.append(("B26", [_history_row(series.diluted_shares_avg, series.ltm_diluted_shares_avg)]))

    # Basic/Diluted EPS (filas 23-24): se computan (Net Income / acciones
    # diluidas promedio) en vez de pegarse -- no hay un tag XBRL de "acciones
    # basicas promedio" confiable en todas las empresas para separar EPS
    # basico del diluido, asi que ambas filas usan el mismo EPS diluido
    # (aproximacion razonable: la diferencia basico/diluido rara vez supera
    # el 1-2% para empresas grandes).
    eps = [ni / shares for ni, shares in zip(series.net_income, series.diluted_shares_avg) if shares]
    ltm_eps = (
        series.ltm_net_income / series.ltm_diluted_shares_avg
        if series.ltm_diluted_shares_avg else (eps[-1] if eps else 0.0)
    )
    updates.append(("B23", [_history_row(eps, ltm_eps, scale=1, decimals=2)]))
    updates.append(("B24", [_history_row(eps, ltm_eps, scale=1, decimals=2)]))

    _apply(ws, updates)


def refresh_cash_flow_statement(sh, series) -> None:
    ws = sh.worksheet("Cash Flow Statement")
    updates: list[tuple[str, list]] = [("B4", [_history_row(series.da, series.ltm_da)])]

    # Net Income / OCF / CapEx / Recompras / Dividendos (filas 3,13,15,30,32)
    # -- mismo bug que el resto: valores pegados de ADBE, nunca refrescados.
    # Alimentan 'Trailing Valuation' (Buyback/Dividend/Shareholder Yield y
    # los multiplos P/OCF, P/FCF historicos reales, ver refresh_trailing_valuation).
    # CapEx/Recompras/Dividendos se NIEGAN: XBRL los reporta en positivo (el
    # monto pagado), pero esta hoja los guarda en negativo como salida de
    # caja (ver CapEx=-203,8 pegado para ADBE, siempre negativo).
    updates.append(("B3", [_history_row(series.net_income, series.ltm_net_income)]))
    updates.append(("B13", [_history_row(series.operating_cash_flow, series.ltm_operating_cash_flow)]))
    capex_negated = [-v for v in series.capex]
    updates.append(("B15", [_history_row(capex_negated, -series.ltm_capex)]))
    buybacks_negated = [-v for v in series.buybacks]
    updates.append(("B30", [_history_row(buybacks_negated, -series.ltm_buybacks)]))
    dividends_negated = [-v for v in series.dividends_paid]
    updates.append(("B32", [_history_row(dividends_negated, -series.ltm_dividends_paid)]))

    # Free Cash Flow (fila 36) = OCF + CapEx (CapEx ya en negativo aca) --
    # misma formula que ya se usaba en los valores pegados de ADBE (se
    # verifico: 2199,7 OCF + (-203,8) CapEx = 1995,9 FCF, igual al pegado).
    fcf = [ocf + cpx for ocf, cpx in zip(series.operating_cash_flow, capex_negated)]
    ltm_fcf = series.ltm_operating_cash_flow + (-series.ltm_capex)
    updates.append(("B36", [_history_row(fcf, ltm_fcf)]))

    _apply(ws, updates)


def refresh_balance_sheet(sh, series, company_inputs) -> None:
    ws = sh.worksheet("Balance Sheet")
    updates: list[tuple[str, list]] = [
        ("B5", [_history_row(series.cash, company_inputs.cash_ltm * _M)]),
        ("B20", [_history_row(series.current_debt, series.current_debt[-1])]),
        ("B25", [_history_row(series.long_term_debt, series.long_term_debt[-1])]),
        ("L35", [[round(company_inputs.book_value_equity_ltm, 1)]]),
    ]
    # Total Current Assets / Total Current Liabilities (filas 10, 24) --
    # mismo bug que el resto: valores pegados de ADBE (~$5-11B), nunca
    # refrescados. 'Financials Multiples' los usa DIRECTAMENTE (sin pasar
    # por ninguna otra celda que ya hayamos arreglado) para el Cambio en
    # Capital de Trabajo de las filas historicas de FCFF/FCFE -- confirmado
    # con MSFT: con estas dos filas en ADBE, el FCFF/FCFE del año mas
    # reciente daba NEGATIVO (-$7.679M) por una ΔNWC completamente
    # inventada, arruinando 'EV/FCFF' y 'P/FCFE' (multiplo implicito de
    # -363x/-387x) aun con Revenue/EBIT/Net Income ya corregidos.
    if series.current_assets:
        updates.append(("B10", [_history_row(series.current_assets, series.current_assets[-1])]))
    if series.current_liabilities:
        updates.append(("B24", [_history_row(series.current_liabilities, series.current_liabilities[-1])]))
    _apply(ws, updates)


@dataclass
class _TrailingComputed:
    """Series intermedias de 'Trailing Valuation' que 'Forward Valuation'
    reutiliza (evita re-pedir precios historicos a yfinance dos veces)."""

    mktcap: list[float | None]
    tev: list[float | None]
    gross_profit: list[float]
    ebitda: list[float]
    fcf: list[float]
    ltm_mktcap: float
    ltm_tev: float
    ltm_gross_profit: float
    ltm_ebitda: float
    ltm_fcf: float


def refresh_trailing_valuation(sh, series, company_inputs) -> _TrailingComputed:
    """'Trailing Valuation' (y 'Forward Valuation', ver refresh_forward_valuation)
    eran tablas ENTERAMENTE de valores pegados a mano de ADBE -- precio
    historico, acciones, Enterprise Value, y los ~20 multiplos derivados de
    esos tres numeros -- nunca una formula, nunca refrescadas por ninguna
    version anterior de este script.

    Esto es la causa raiz del bug de multiplos que el usuario reporto: 'EV
    /FCFF' (y las hojas hermanas P/OCF, P/E, P/FCFE, EV/EBITDA), fila 19,
    usan `MEDIAN('Trailing Valuation'!G24:K24)` como el multiplo de SALIDA
    por default del escenario Base (Conservador/Optimista = Base*0,9/1,1) --
    es decir, esta tabla es el driver principal del "Total Return" de CADA
    escenario en las 5 hojas de multiplos. Confirmado con MSFT antes de este
    fix: EV/EBITDA implicito de ~0,9x (debia ser ~15-30x) y Total Return de
    -19% a -37% en las 5 hojas, enteramente por precio/acciones/EV de ADBE
    de hace años en vez de MSFT actual.

    Se recalculan TODOS los multiplos en Python (no formulas -- la hoja ya
    era de valores pegados, este fix mantiene esa misma convencion) a partir
    de: precio de cierre real en cada fin de ejercicio fiscal (nuevo,
    yfinance .history()), acciones/deuda/caja/ingresos/EBIT ya refrescados
    (SEC EDGAR), y Net Income/OCF/CapEx/Buybacks/Dividendos/COGS (nuevos
    campos de AnnualSeries). Book Value historico (para P/B, fila 18) NO
    esta disponible como serie completa -- esa fila queda sin tocar."""
    ws = sh.worksheet("Trailing Valuation")

    prices = get_historical_close_prices(series.ticker, series.fiscal_year_ends)
    ltm_price = company_inputs.current_price

    shares = [s or None for s in series.shares_outstanding]
    ltm_shares = company_inputs.shares_outstanding * _M

    mktcap = [p * s if p is not None and s else None for p, s in zip(prices, shares)]
    ltm_mktcap = ltm_price * ltm_shares

    debt = [lt + cur for lt, cur in zip(series.long_term_debt, series.current_debt)]
    ltm_debt = company_inputs.book_value_debt_ltm * _M

    tev = [(mc + d - c) if mc is not None else None for mc, d, c in zip(mktcap, debt, series.cash)]
    ltm_tev = ltm_mktcap + ltm_debt - company_inputs.cash_ltm * _M

    gross_profit = [r - c for r, c in zip(series.revenue, series.cogs)]
    ltm_gross_profit = series.ltm_revenue - series.ltm_cogs
    ebitda = [e + d for e, d in zip(series.ebit, series.da)]
    ltm_ebitda = series.ltm_ebit + series.ltm_da
    fcf = [ocf - cpx for ocf, cpx in zip(series.operating_cash_flow, series.capex)]
    ltm_fcf = series.ltm_operating_cash_flow - series.ltm_capex

    updates: list[tuple[str, list]] = [
        ("B3", [_ratio_row(prices, ltm_price)]),
        ("B4", [_ratio_row(shares, ltm_shares, scale=_M, decimals=1)]),
        ("B5", [_ratio_row(mktcap, ltm_mktcap, scale=_M, decimals=1)]),
        ("B6", [_ratio_row(tev, ltm_tev, scale=_M, decimals=1)]),
    ]

    dividend_yield = [_safe_div(d, mc) for d, mc in zip(series.dividends_paid, mktcap)]
    ltm_dividend_yield = _safe_div(series.ltm_dividends_paid, ltm_mktcap)
    updates.append(("B7", [_ratio_row(dividend_yield, ltm_dividend_yield, decimals=4)]))

    buyback_yield = [_safe_div(b, mc) for b, mc in zip(series.buybacks, mktcap)]
    ltm_buyback_yield = _safe_div(series.ltm_buybacks, ltm_mktcap)
    updates.append(("B8", [_ratio_row(buyback_yield, ltm_buyback_yield, decimals=4)]))

    debt_paydown_yield: list[float | None] = [None]
    for i in range(1, len(debt)):
        debt_paydown_yield.append(_safe_div(debt[i - 1] - debt[i], mktcap[i]))
    ltm_debt_paydown_yield = _safe_div(debt[-1] - ltm_debt, ltm_mktcap) if debt else None
    updates.append(("B9", [_ratio_row(debt_paydown_yield, ltm_debt_paydown_yield, decimals=4)]))

    def _sum_optional(*vals: float | None) -> float | None:
        present = [v for v in vals if v is not None]
        return sum(present) if present else None

    shareholder_yield = [_sum_optional(dy, by, dp) for dy, by, dp in zip(dividend_yield, buyback_yield, debt_paydown_yield)]
    ltm_shareholder_yield = _sum_optional(ltm_dividend_yield, ltm_buyback_yield, ltm_debt_paydown_yield)
    updates.append(("B10", [_ratio_row(shareholder_yield, ltm_shareholder_yield, decimals=4)]))

    updates.append(("B11", [_ratio_row(
        [_safe_div(mc, r) for mc, r in zip(mktcap, series.revenue)], _safe_div(ltm_mktcap, series.ltm_revenue),
    )]))
    updates.append(("B12", [_ratio_row(
        [_safe_div(mc, g) for mc, g in zip(mktcap, gross_profit)], _safe_div(ltm_mktcap, ltm_gross_profit),
    )]))
    updates.append(("B13", [_ratio_row(
        [_safe_div(mc, ni) for mc, ni in zip(mktcap, series.net_income)], _safe_div(ltm_mktcap, series.ltm_net_income),
    )]))
    updates.append(("B14", [_ratio_row(
        [_safe_div(ni, mc) for ni, mc in zip(series.net_income, mktcap)],
        _safe_div(series.ltm_net_income, ltm_mktcap), decimals=4,
    )]))
    updates.append(("B15", [_ratio_row(
        [_safe_div(mc, o) for mc, o in zip(mktcap, series.operating_cash_flow)],
        _safe_div(ltm_mktcap, series.ltm_operating_cash_flow),
    )]))
    updates.append(("B16", [_ratio_row(
        [_safe_div(mc, f) for mc, f in zip(mktcap, fcf)], _safe_div(ltm_mktcap, ltm_fcf),
    )]))
    updates.append(("B17", [_ratio_row(
        [_safe_div(f, mc) for f, mc in zip(fcf, mktcap)], _safe_div(ltm_fcf, ltm_mktcap), decimals=4,
    )]))
    # B18 (P/B) queda sin tocar -- no hay serie de Book Value historico completa en AnnualSeries.
    updates.append(("B19", [_ratio_row(
        [_safe_div(t, r) for t, r in zip(tev, series.revenue)], _safe_div(ltm_tev, series.ltm_revenue),
    )]))
    updates.append(("B20", [_ratio_row(
        [_safe_div(t, g) for t, g in zip(tev, gross_profit)], _safe_div(ltm_tev, ltm_gross_profit),
    )]))
    updates.append(("B21", [_ratio_row(
        [_safe_div(t, e) for t, e in zip(tev, ebitda)], _safe_div(ltm_tev, ltm_ebitda),
    )]))
    updates.append(("B22", [_ratio_row(
        [_safe_div(t, e) for t, e in zip(tev, series.ebit)], _safe_div(ltm_tev, series.ltm_ebit),
    )]))
    updates.append(("B23", [_ratio_row(
        [_safe_div(t, o) for t, o in zip(tev, series.operating_cash_flow)],
        _safe_div(ltm_tev, series.ltm_operating_cash_flow),
    )]))
    updates.append(("B24", [_ratio_row(
        [_safe_div(t, f) for t, f in zip(tev, fcf)], _safe_div(ltm_tev, ltm_fcf),
    )]))

    _apply(ws, updates)

    return _TrailingComputed(
        mktcap=mktcap, tev=tev, gross_profit=gross_profit, ebitda=ebitda, fcf=fcf,
        ltm_mktcap=ltm_mktcap, ltm_tev=ltm_tev, ltm_gross_profit=ltm_gross_profit,
        ltm_ebitda=ltm_ebitda, ltm_fcf=ltm_fcf,
    )


def refresh_forward_valuation(sh, series, computed: _TrailingComputed) -> None:
    """Multiplos FORWARD = precio/EV del año T dividido por el resultado REAL
    del año T+1 (asi se define un multiplo forward reconstruido en
    retrospectiva -- 'cuanto pagaba el mercado en T por lo que la empresa
    efectivamente iba a ganar en T+1'). Para el ultimo año historico
    (T=fila mas reciente) se usa el LTM como proxy del "T+1" (el periodo
    completo mas reciente disponible). La columna NTM (la ultima, L) queda
    en blanco: un forward NTM real necesitaria una estimacion FY+1, que en
    este modelo depende del escenario (Conservador/Base/Optimista) elegido
    en 'Valuation output' -- esta tabla es unica (no tiene un bloque por
    escenario) asi que no hay un unico numero correcto para poner ahi sin
    inventar un supuesto adicional."""
    ws = sh.worksheet("Forward Valuation")

    n = len(series.revenue)
    def _forward(actual: list[float], ltm: float) -> list[float | None]:
        return [actual[i + 1] if i + 1 < n else ltm for i in range(n)]

    fwd_revenue = _forward(series.revenue, series.ltm_revenue)
    fwd_net_income = _forward(series.net_income, series.ltm_net_income)
    fwd_ocf = _forward(series.operating_cash_flow, series.ltm_operating_cash_flow)
    fwd_fcf = _forward(computed.fcf, computed.ltm_fcf)
    fwd_ebitda = _forward(computed.ebitda, computed.ltm_ebitda)
    fwd_ebit = _forward(series.ebit, series.ltm_ebit)

    mktcap, tev = computed.mktcap, computed.tev

    updates: list[tuple[str, list]] = [
        ("B3", [_ratio_row([_safe_div(mc, r) for mc, r in zip(mktcap, fwd_revenue)], None)]),
        ("B4", [_ratio_row([_safe_div(mc, ni) for mc, ni in zip(mktcap, fwd_net_income)], None)]),
        ("B5", [_ratio_row([_safe_div(ni, mc) for ni, mc in zip(fwd_net_income, mktcap)], None, decimals=4)]),
        ("B6", [_ratio_row([_safe_div(mc, o) for mc, o in zip(mktcap, fwd_ocf)], None)]),
        ("B7", [_ratio_row([_safe_div(mc, f) for mc, f in zip(mktcap, fwd_fcf)], None)]),
        ("B8", [_ratio_row([_safe_div(f, mc) for f, mc in zip(fwd_fcf, mktcap)], None, decimals=4)]),
        ("B9", [_ratio_row([_safe_div(t, r) for t, r in zip(tev, fwd_revenue)], None)]),
        ("B10", [_ratio_row([_safe_div(t, e) for t, e in zip(tev, fwd_ebitda)], None)]),
        ("B11", [_ratio_row([_safe_div(t, e) for t, e in zip(tev, fwd_ebit)], None)]),
        ("B12", [_ratio_row([_safe_div(t, o) for t, o in zip(tev, fwd_ocf)], None)]),
        ("B13", [_ratio_row([_safe_div(t, f) for t, f in zip(tev, fwd_fcf)], None)]),
    ]
    _apply(ws, updates)


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
    print(f"[1/6] Descargando historico de 10y de {ticker} desde SEC EDGAR...")
    series = load_annual_series_from_sec_edgar(ticker)
    market = get_market_snapshot(ticker)
    company_inputs = load_company_inputs_from_sec_edgar(
        ticker, current_price=market.current_price, riskfree_rate=0.04, initial_cost_of_capital=0.09,
    )

    client = get_gspread_client()
    sh = open_target_sheet(client, sheet_id)

    print(f"[2/7] Actualizando Input sheet (ticker={ticker}, industria={industry_us})...")
    refresh_input_sheet(sh, ticker, company_inputs, industry_us, industry_global)

    print("[3/7] Repoblando historico completo de Income Statement / Cash Flow Statement / Balance Sheet...")
    refresh_income_statement(sh, series, company_inputs)
    refresh_cash_flow_statement(sh, series)
    refresh_balance_sheet(sh, series, company_inputs)

    print("[4/7] Recalculando Trailing Valuation / Forward Valuation (precio historico real + multiplos)...")
    computed = refresh_trailing_valuation(sh, series, company_inputs)
    refresh_forward_valuation(sh, series, computed)

    print(f"[5/7] Refrescando pestaña Sector ({ticker} + {', '.join(peer_tickers)})...")
    refresh_sector(sh, ticker, peer_tickers)

    print("[6/7] Congelando precio del día del análisis en 'Resumen de Valoración'...")
    refresh_resumen_valoracion(sh, market)

    print(f"[7/7] Listo: {sh.url}")


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
