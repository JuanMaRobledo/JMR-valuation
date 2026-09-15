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

    # Cost of Sales / Gross Profit / Gross Margin (filas 5-7), SG&A (fila 8),
    # D&A dentro de opex (fila 9) y R&D (fila 10) -- filas que quedaban
    # completamente en blanco en la plantilla (nunca se tocaban, solo se
    # rellenaban las filas que alimentan la valoracion). COGS/SG&A/R&D vienen
    # de SEC EDGAR real; la fila de D&A "dentro de opex" reusa el mismo D&A
    # total de la fila 4 de Cash Flow Statement (no hay un tag XBRL separado
    # para "D&A que vive en el estado de resultados" vs. "D&A total del cash
    # flow" -- son el mismo numero real, no un valor inventado).
    updates.append(("B5", [_history_row(series.cogs, series.ltm_cogs)]))
    gross_profit = [r - c for r, c in zip(series.revenue, series.cogs)]
    ltm_gross_profit = series.ltm_revenue - series.ltm_cogs
    updates.append(("B6", [_history_row(gross_profit, ltm_gross_profit)]))
    gross_margin = [g / r for g, r in zip(gross_profit, series.revenue) if r]
    ltm_gross_margin = ltm_gross_profit / series.ltm_revenue if series.ltm_revenue else gross_margin[-1]
    updates.append(("B7", [_history_row(gross_margin, ltm_gross_margin, scale=1, decimals=4)]))
    updates.append(("B8", [_history_row(series.sga, series.ltm_sga)]))
    updates.append(("B9", [_history_row(series.da, series.ltm_da)]))
    updates.append(("B10", [_history_row(series.rd, series.ltm_rd)]))

    # Other Operating Expenses (fila 11) -- no hay un tag XBRL limpio para
    # "otros gastos operativos" (es tipicamente un residuo, no una linea que
    # las empresas taggeen aparte). Se calcula como el remanente para que
    # Revenue - COGS - SG&A - D&A - R&D - Other Opex = EBIT REAL (el EBIT de
    # 'OperatingIncomeLoss', ya validado), en vez de dejar la identidad
    # contable rota o inventar un numero.
    other_opex = [
        r - c - s - d - rd - e
        for r, c, s, d, rd, e in zip(series.revenue, series.cogs, series.sga, series.da, series.rd, series.ebit)
    ]
    ltm_other_opex = (
        series.ltm_revenue - series.ltm_cogs - series.ltm_sga - series.ltm_da - series.ltm_rd - series.ltm_ebit
    )
    updates.append(("B11", [_history_row(other_opex, ltm_other_opex)]))

    # Interest Expense (fila 15, se guarda en NEGATIVO) e Interest and
    # Investment Income (fila 14) -- antes solo se escribia la columna LTM
    # de la primera, y la segunda quedaba en 0 por no tener tag. Ahora se
    # usa 'InvestmentIncomeNet'/'InvestmentIncomeInterestAndDividend' real.
    interest_expense_negated = [-v for v in series.interest_expense]
    updates.append(("B15", [_history_row(interest_expense_negated, -series.ltm_interest_expense)]))
    updates.append(("B14", [_history_row(series.interest_investment_income, series.ltm_interest_investment_income)]))

    # Income Before Provision for Income Taxes (fila 19) = pretax_income REAL
    # de SEC EDGAR. Total Non-Operating Income (fila 18) = pretax real -
    # EBIT (la brecha REAL entre resultado operativo y pretax, sea cual sea
    # su causa). Non-Operating Income (fila 17) resta el efecto de intereses
    # (ya capturado en las filas 14-16) para no duplicarlo -- lo que queda
    # es "todo lo demas" (ganancias/perdidas de inversiones, FX, etc.), sin
    # inventar un desglose que EDGAR no da linea por linea.
    updates.append(("B19", [_history_row(series.pretax_income, series.ltm_pretax_income)]))
    total_non_operating = [p - e for p, e in zip(series.pretax_income, series.ebit)]
    ltm_total_non_operating = series.ltm_pretax_income - series.ltm_ebit
    non_operating = [
        tno - ii + ie
        for tno, ii, ie in zip(total_non_operating, series.interest_investment_income, series.interest_expense)
    ]
    ltm_non_operating = ltm_total_non_operating - series.ltm_interest_investment_income + series.ltm_interest_expense
    updates.append(("B17", [_history_row(non_operating, ltm_non_operating)]))
    updates.append(("B18", [_history_row(total_non_operating, ltm_total_non_operating)]))

    # Effective Tax Rate (fila 29) -- ahora con serie completa (antes solo
    # LTM) porque ya tenemos tax_expense y pretax_income año a año.
    tax_rates = [t / p for t, p in zip(series.tax_expense, series.pretax_income) if p]
    ltm_tax_rate = (
        series.ltm_tax_expense / series.ltm_pretax_income
        if series.ltm_pretax_income else company_inputs.effective_tax_rate
    )
    updates.append(("B29", [_history_row(tax_rates, ltm_tax_rate, scale=1, decimals=4)]))

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
    if series.basic_shares_avg:
        updates.append(("B25", [_history_row(series.basic_shares_avg, series.ltm_basic_shares_avg)]))

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

    # Share-Based Compensation (fila 5) -- dato real de SEC EDGAR, antes en blanco.
    updates.append(("B5", [_history_row(series.share_based_comp, series.ltm_share_based_comp)]))

    # Other Adjustments (fila 6) -- plug para que Operating Activities sume
    # al OCF REAL: no tenemos desglosados los cambios de capital de trabajo
    # linea por linea (filas 7-12, quedan en blanco -- no se inventan), asi
    # que esta fila absorbe TODOS esos cambios juntos con la comp. en
    # acciones y cualquier otro ajuste no-monetario.
    other_adj = [
        ocf - ni - da - sbc
        for ocf, ni, da, sbc in zip(
            series.operating_cash_flow, series.net_income, series.da, series.share_based_comp,
        )
    ]
    ltm_other_adj = (
        series.ltm_operating_cash_flow - series.ltm_net_income - series.ltm_da - series.ltm_share_based_comp
    )
    updates.append(("B6", [_history_row(other_adj, ltm_other_adj)]))

    # Cash from Investing Activities (fila 22) = total REAL de SEC EDGAR.
    # Other Investing Activities (fila 21) absorbe todo lo que no es CapEx
    # (compra/venta de inversiones, adquisiciones, etc. -- no desglosadas
    # linea por linea, filas 16-20 quedan en blanco) como plug contra ese
    # total, para no inventar un desglose que EDGAR no da de forma limpia.
    updates.append(("B22", [_history_row(series.investing_cash_flow, series.ltm_investing_cash_flow)]))
    other_investing = [icf + cpx for icf, cpx in zip(series.investing_cash_flow, series.capex)]
    ltm_other_investing = series.ltm_investing_cash_flow + series.ltm_capex
    updates.append(("B21", [_history_row(other_investing, ltm_other_investing)]))

    # Cash from Financing Activities (fila 34) = total REAL. Net Issuance/
    # (Repayments) of Long-Term Debt (fila 28) = cambio interanual del saldo
    # de deuda de largo plazo (aproximacion estandar del efecto de caja,
    # ignora ajustes no-monetarios como FX -- no hay series de emision/pago
    # bruto por separado). Issuance of Common Shares (fila 29) = dato real
    # de SEC EDGAR ('ProceedsFromIssuanceOfCommonStock') donde esta
    # disponible; Net Issuance/(Repurchases) of Common Shares (fila 31) =
    # esa emision menos Recompras (antes solo -Recompras, ignorando
    # emisiones por stock comp). Other Financing Activities (fila 33)
    # absorbe el resto contra el total real.
    net_lt_debt = [0.0] + [d2 - d1 for d1, d2 in zip(series.long_term_debt, series.long_term_debt[1:])]
    updates.append(("B28", [_history_row(net_lt_debt, net_lt_debt[-1] if net_lt_debt else 0.0)]))
    if series.stock_issuance:
        updates.append(("B29", [_history_row(series.stock_issuance, series.ltm_stock_issuance)]))
    stock_issuance = series.stock_issuance or [0.0] * len(series.revenue)
    ltm_stock_issuance = series.ltm_stock_issuance
    net_share_issuance = [iss - buy for iss, buy in zip(stock_issuance, series.buybacks)]
    ltm_net_share_issuance = ltm_stock_issuance - series.ltm_buybacks
    updates.append(("B31", [_history_row(net_share_issuance, ltm_net_share_issuance)]))
    updates.append(("B34", [_history_row(series.financing_cash_flow, series.ltm_financing_cash_flow)]))
    other_financing = [
        fcf_total - lt - sh - div
        for fcf_total, lt, sh, div in zip(series.financing_cash_flow, net_lt_debt, net_share_issuance, dividends_negated)
    ]
    ltm_other_financing = (
        series.ltm_financing_cash_flow - (net_lt_debt[-1] if net_lt_debt else 0.0) - ltm_net_share_issuance
        - (-series.ltm_dividends_paid)
    )
    updates.append(("B33", [_history_row(other_financing, ltm_other_financing)]))

    # NOPAT (fila 37) = EBIT * (1 - tasa efectiva real). Levered/Unlevered
    # Free Cash Flow (filas 38-39) -- definiciones estandar a partir de
    # datos ya reales (Net Income/NOPAT + D&A - CapEx); no incluyen el
    # cambio en capital de trabajo (no tenemos esa serie limpia) asi que son
    # una aproximacion, no identicas al FCFF de 'Valuation output'.
    nopat = [
        e * (1 - t / p) if p else e
        for e, t, p in zip(series.ebit, series.tax_expense, series.pretax_income)
    ]
    ltm_nopat = (
        series.ltm_ebit * (1 - series.ltm_tax_expense / series.ltm_pretax_income)
        if series.ltm_pretax_income else series.ltm_ebit
    )
    updates.append(("B37", [_history_row(nopat, ltm_nopat)]))
    levered_fcf = [
        ni + da - cpx for ni, da, cpx in zip(series.net_income, series.da, series.capex)
    ]
    ltm_levered_fcf = series.ltm_net_income + series.ltm_da - series.ltm_capex
    updates.append(("B38", [_history_row(levered_fcf, ltm_levered_fcf)]))
    unlevered_fcf = [n + da - cpx for n, da, cpx in zip(nopat, series.da, series.capex)]
    ltm_unlevered_fcf = ltm_nopat + series.ltm_da - series.ltm_capex
    updates.append(("B39", [_history_row(unlevered_fcf, ltm_unlevered_fcf)]))

    _apply(ws, updates)


def refresh_balance_sheet(sh, series, company_inputs) -> None:
    ws = sh.worksheet("Balance Sheet")
    updates: list[tuple[str, list]] = [
        ("B3", [_history_row(series.cash, company_inputs.cash_ltm * _M)]),  # Cash and Cash Equivalents (solo caja)
        ("B20", [_history_row(series.current_debt, series.current_debt[-1])]),
        ("B25", [_history_row(series.long_term_debt, series.long_term_debt[-1])]),
    ]
    # Short-Term Investments (fila 4) -- 'ShortTermInvestments' de SEC EDGAR.
    # Total Cash and Cash Equivalents (fila 5) = Cash + Short-Term
    # Investments (antes fila 5 solo tenia el mismo numero que la fila 3,
    # subestimando el total cuando la empresa SI reporta inversiones de
    # corto plazo por separado -- MSFT tiene ~$55-64B en esa linea).
    if series.short_term_investments:
        updates.append(("B4", [_history_row(series.short_term_investments, series.short_term_investments[-1])]))
        total_cash = [c + s for c, s in zip(series.cash, series.short_term_investments)]
        ltm_total_cash = company_inputs.cash_ltm * _M + series.short_term_investments[-1]
        updates.append(("B5", [_history_row(total_cash, ltm_total_cash)]))
    else:
        updates.append(("B5", [_history_row(series.cash, company_inputs.cash_ltm * _M)]))
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

    # Receivables (filas 6, 8 -- no hay 'Other Receivables' separado, fila 7
    # queda en blanco), PP&E neto (11), Goodwill (13), Total Assets (16),
    # Accounts Payable (18), Total Liabilities (29), y los 3 componentes de
    # Equity + su total (31-35) -- todas filas que quedaban en blanco.
    if series.receivables:
        updates.append(("B6", [_history_row(series.receivables, series.receivables[-1])]))
        updates.append(("B8", [_history_row(series.receivables, series.receivables[-1])]))
    if series.ppe_net:
        updates.append(("B11", [_history_row(series.ppe_net, series.ppe_net[-1])]))
    if series.intangibles_net:
        updates.append(("B12", [_history_row(series.intangibles_net, series.intangibles_net[-1])]))
    if series.goodwill:
        updates.append(("B13", [_history_row(series.goodwill, series.goodwill[-1])]))
    if series.long_term_investments:
        updates.append(("B14", [_history_row(series.long_term_investments, series.long_term_investments[-1])]))
    if series.unearned_revenue_current:
        updates.append(("B22", [_history_row(series.unearned_revenue_current, series.unearned_revenue_current[-1])]))
    if series.lease_liability_noncurrent:
        updates.append(("B26", [_history_row(series.lease_liability_noncurrent, series.lease_liability_noncurrent[-1])]))
    if series.total_assets:
        updates.append(("B16", [_history_row(series.total_assets, series.total_assets[-1])]))
        updates.append(("B36", [_history_row(series.total_assets, series.total_assets[-1])]))  # Total L+E == Total Assets, por identidad contable
    if series.accounts_payable:
        updates.append(("B18", [_history_row(series.accounts_payable, series.accounts_payable[-1])]))
    if series.total_liabilities:
        updates.append(("B29", [_history_row(series.total_liabilities, series.total_liabilities[-1])]))
    if series.apic:
        updates.append(("B31", [_history_row(series.apic, series.apic[-1])]))
    if series.aoci:
        updates.append(("B32", [_history_row(series.aoci, series.aoci[-1])]))
    if series.retained_earnings:
        updates.append(("B33", [_history_row(series.retained_earnings, series.retained_earnings[-1])]))
    if series.equity:
        # 'Total Common Shareholders Equity' y 'Total Shareholders Equity'
        # -- se asume interes minoritario nulo/inmaterial (razonable para la
        # gran mayoria de empresas; si el ticker tiene uno grande, ambas
        # filas quedarian iguales en vez de diferir en ese monto).
        updates.append(("B34", [_history_row(series.equity, series.equity[-1])]))
        updates.append(("B35", [_history_row(series.equity, series.equity[-1])]))
    else:
        updates.append(("L35", [[round(company_inputs.book_value_equity_ltm, 1)]]))

    # Other Current Assets (9) / Other Long-Term Assets (15) / Other Current
    # Liabilities (23) / Other Long-Term Liabilities (27) -- se calculan
    # como el REMANENTE contra los totales reales (Total Current Assets,
    # Total Assets, Total Current Liabilities, Total Liabilities), no se
    # inventan: "Other" es, por definicion, todo lo que no cae en las lineas
    # ya identificadas (Cash/Receivables/PP&E/Goodwill para activos;
    # AP/Deuda de corto plazo para pasivos corrientes; Deuda de largo plazo
    # para pasivos de largo plazo).
    # Cada "Other" resta TODAS las lineas ya identificadas de ese mismo total
    # (mas lineas identificadas -> plug mas chico y preciso; con solo
    # Cash/Receivables antes, ahora tambien Short-Term Investments/LT
    # Investments/Intangibles/Unearned Revenue/Leases donde estan disponibles).
    if series.current_assets and series.receivables:
        sti = series.short_term_investments or [0.0] * len(series.revenue)
        other_ca = [
            ca - c - r - s for ca, c, r, s in zip(series.current_assets, series.cash, series.receivables, sti)
        ]
        updates.append(("B9", [_history_row(other_ca, other_ca[-1])]))
    if series.total_assets and series.ppe_net and series.goodwill and series.current_assets:
        lti = series.long_term_investments or [0.0] * len(series.revenue)
        intang = series.intangibles_net or [0.0] * len(series.revenue)
        other_lt_assets = [
            ta - ca - ppe - gw - lt - it
            for ta, ca, ppe, gw, lt, it in zip(
                series.total_assets, series.current_assets, series.ppe_net, series.goodwill, lti, intang,
            )
        ]
        updates.append(("B15", [_history_row(other_lt_assets, other_lt_assets[-1])]))
    if series.current_liabilities and series.accounts_payable:
        unearned = series.unearned_revenue_current or [0.0] * len(series.revenue)
        other_cl = [
            cl - ap - cd - u
            for cl, ap, cd, u in zip(series.current_liabilities, series.accounts_payable, series.current_debt, unearned)
        ]
        updates.append(("B23", [_history_row(other_cl, other_cl[-1])]))
    if series.total_liabilities and series.current_liabilities:
        leases_nc = series.lease_liability_noncurrent or [0.0] * len(series.revenue)
        other_lt_liab = [
            tl - cl - ltd - ln
            for tl, cl, ltd, ln in zip(series.total_liabilities, series.current_liabilities, series.long_term_debt, leases_nc)
        ]
        updates.append(("B27", [_history_row(other_lt_liab, other_lt_liab[-1])]))
        total_lt_liab = [ltd + ln + o for ltd, ln, o in zip(series.long_term_debt, leases_nc, other_lt_liab)]
        updates.append(("B28", [_history_row(total_lt_liab, total_lt_liab[-1])]))

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
