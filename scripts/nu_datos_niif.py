#!/usr/bin/env python
"""NU (Nu Holdings): estados NIIF de banco hacia la hoja nueva copiada de la plantilla maestra, 11-oct-2026.

El importador de la SEC (refresh_native_model.py) lee la taxonomía us-gaap de companyfacts. Nu Holdings presenta 20-F
en NIIF (ifrs-full, dólares) y la SEC aún no publica en companyfacts el XBRL del 20-F 2025; además sus etiquetas
cambian de signo entre años y los 6-K trimestrales no traen XBRL. Por eso este script NO baja XBRL: arma la serie
anual y el UDM desde reference/desde_cero/NU/estados_fuente_2026-10-11.json (cifras transcritas de los 20-F 2023 y
2025 y del 6-K de estados del 2T26, con fuente por bloque) y se las entrega al importador en lugar de las funciones
de EDGAR. El resto del importador (encabezados, Trailing/Forward Valuation, pestañas de razones, Sector y precio
congelado) corre igual que en cualquier empresa.

Mapeo de un banco a la plantilla industrial (declarado en las notas de las celdas):
  - Ingresos = ingresos totales NIIF (intereses y ganancias sobre instrumentos financieros + comisiones);
  - Costo de ventas = costo de los servicios financieros y transaccionales (gasto de intereses + gasto transaccional
    + pérdida de crédito esperada): en un banco el interés pagado es materia prima, no gasto financiero;
  - SG&A = soporte al cliente + generales y administrativos + marketing; «otros gastos netos» en Other Operating;
  - EBIT («Operating Profit») = utilidad bruta − gastos operativos = utilidad antes de impuestos sin asociadas;
  - Interest Expense (no operativo) = 0; la deuda de la Input sheet = préstamos y financiación (no depósitos);
  - UDM (columna L) = ejercicio 2025 + 1S26 − 1S25 (mismas normas y perímetro); saldos al 30-jun-2026.

Uso: PYTHONPATH=.:scripts python scripts/nu_datos_niif.py --sheet-id ID --peers ITUB BBD ... [--solo-estados]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import refresh_native_model as rnm
from jmr_valuation.io.inputs import CompanyInputs
from jmr_valuation.io.sec_edgar_loader import AnnualSeries

_ROOT = Path(__file__).resolve().parents[1]
FUENTE = _ROOT / "reference" / "desde_cero" / "NU" / "estados_fuente_2026-10-11.json"
M = 1_000_000.0
ANIOS = 5  # 2021-2025; columnas 6 y 7 de cada lista = 1S25 y 1S26


def _datos() -> dict:
    return json.loads(FUENTE.read_text())


def _ltm(v: list) -> float:
    return v[4] + v[6] - v[5]


def series_nu() -> AnnualSeries:
    d = _datos()
    r, f, b = d["resultados"], d["flujos"], d["balance"]
    a = lambda lst: [x * M for x in lst[:ANIOS]]  # noqa: E731
    l = lambda lst: _ltm(lst) * M  # noqa: E731
    sga = [r["soporte_clientes"][i] + r["gastos_generales"][i] + r["marketing"][i] for i in range(7)]
    ebit = [r["utilidad_bruta"][i] - r["gastos_operativos_total"][i] for i in range(7)]
    capex = [f["capex_ppe"][i] + f["capex_intangibles"][i] for i in range(7)]
    bal = lambda k: [(x or 0.0) * M for x in b[k][:ANIOS]]  # noqa: E731
    return AnnualSeries(
        ticker="NU", company_name="Nu Holdings Ltd.",
        fiscal_year_ends=[f"{y}-12-31" for y in range(2021, 2026)],
        revenue=a(r["ingresos_totales"]), ebit=a(ebit), da=a(f["dya"]),
        shares_outstanding=[x * M for x in b["acciones_en_circulacion_millones"][:ANIOS]],
        long_term_debt=bal("prestamos_financiacion"), current_debt=[0.0] * ANIOS, cash=bal("caja"),
        ltm_revenue=l(r["ingresos_totales"]), ltm_ebit=l(ebit), ltm_da=l(f["dya"]),
        tax_expense=a(r["impuestos"]), net_income=a(r["utilidad_neta"]),
        diluted_shares_avg=[x * M for x in r["acciones_diluidas_prom_millones"][:ANIOS]],
        operating_cash_flow=a(f["flujo_operativo"]), capex=a(capex), buybacks=a(f["recompras"]),
        dividends_paid=a(f["dividendos"]), cogs=a(r["costo_servicios_total"]),
        ltm_tax_expense=l(r["impuestos"]), ltm_net_income=l(r["utilidad_neta"]),
        ltm_diluted_shares_avg=r["acciones_diluidas_prom_millones"][6] * M,  # promedio diluido del 1S26
        ltm_operating_cash_flow=l(f["flujo_operativo"]), ltm_capex=l(capex), ltm_buybacks=l(f["recompras"]),
        ltm_dividends_paid=0.0, ltm_cogs=l(r["costo_servicios_total"]),
        rd=[0.0] * ANIOS, sga=a(sga), pretax_income=a(r["utilidad_antes_impuestos"]),
        total_assets=bal("activos_totales"), total_liabilities=bal("pasivos_totales"), equity=bal("patrimonio_total"),
        share_based_comp=a(f["pagos_en_acciones"]),
        receivables=[((b["tarjetas_credito"][i] or 0) + (b["prestamos"][i] or 0)) * M for i in range(ANIOS)],
        ppe_net=bal("ppe"), goodwill=bal("plusvalia"), intangibles_net=bal("intangibles"),
        apic=bal("prima_emision"), retained_earnings=bal("utilidades_retenidas"), aoci=bal("otro_resultado_integral"),
        ltm_rd=0.0, ltm_sga=l(sga), ltm_pretax_income=l(r["utilidad_antes_impuestos"]),
        ltm_share_based_comp=l(f["pagos_en_acciones"]),
        interest_expense=[0.0] * ANIOS, ltm_interest_expense=0.0,
        short_term_investments=bal("titulos"),
        basic_shares_avg=[x * M for x in r["acciones_basicas_prom_millones"][:ANIOS]],
        ltm_basic_shares_avg=r["acciones_basicas_prom_millones"][6] * M,
        business_acquisitions=a(f["adquisiciones"]), ltm_business_acquisitions=l(f["adquisiciones"]),
    )


def inputs_nu(*, current_price: float, riskfree_rate: float, initial_cost_of_capital: float, **_) -> CompanyInputs:
    d = _datos()
    r, b = d["resultados"], d["balance"]
    ebit = [r["utilidad_bruta"][i] - r["gastos_operativos_total"][i] for i in range(7)]
    rev_ltm = _ltm(r["ingresos_totales"])
    return CompanyInputs(
        ticker="NU", company_name="Nu Holdings Ltd.", country_of_incorporation="Brazil",
        industry_us="", industry_global="",
        revenue_ltm=rev_ltm * M, revenue_prior_10k=r["ingresos_totales"][4] * M, years_since_last_10k=0.5,
        ebit_ltm=_ltm(ebit) * M, ebit_prior_10k=ebit[4] * M,
        interest_expense_ltm=0.0, interest_expense_prior_10k=0.0,
        book_value_equity_ltm=b["patrimonio_total"][5] * M, book_value_equity_prior_10k=b["patrimonio_total"][4] * M,
        book_value_debt_ltm=b["prestamos_financiacion"][5] * M, book_value_debt_prior_10k=b["prestamos_financiacion"][4] * M,
        cash_ltm=b["caja"][5] * M, cash_prior_10k=b["caja"][4] * M,
        minority_interests=(b["patrimonio_total"][5] - b["patrimonio_controladora"][5]) * M,
        shares_outstanding=b["acciones_en_circulacion_millones"][5] * M, current_price=current_price,
        effective_tax_rate=_ltm(r["impuestos"]) / _ltm(r["utilidad_antes_impuestos"]),
        riskfree_rate=riskfree_rate, initial_cost_of_capital=initial_cost_of_capital,
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet-id", required=True)
    ap.add_argument("--peers", nargs="+", required=True)
    ap.add_argument("--industry-us", required=True)
    ap.add_argument("--industry-global", required=True)
    a = ap.parse_args()
    rnm.load_annual_series_from_sec_edgar = lambda tk, **k: series_nu() if tk.upper() == "NU" else _orig_series(tk, **k)
    rnm.load_company_inputs_from_sec_edgar = lambda tk, **k: inputs_nu(**k) if tk.upper() == "NU" else _orig_inputs(tk, **k)
    rnm.run("NU", sheet_id=a.sheet_id, peer_tickers=a.peers, industry_us=a.industry_us, industry_global=a.industry_global)
    return 0


_orig_series, _orig_inputs = rnm.load_annual_series_from_sec_edgar, rnm.load_company_inputs_from_sec_edgar

if __name__ == "__main__":
    raise SystemExit(main())
