"""Proyecta FCFF, OCF, FCFE, EBITDA, EPS y DPS para alimentar `models.relative`.

Replica la hoja 'Financials Multiples' (743 formulas en el Excel, repetidas 3
veces -- Conservador/Base/Optimista -- con la misma mecanica). A diferencia del
Excel, esta funcion no re-deriva crecimiento/margen/tax rate: los toma
directamente de los `YearProjection` que ya devolvio `models.dcf.run_dcf`, que
es exactamente de donde 'Financials Multiples' los leia (E44='Valuation
output'!C4, E47='Valuation output'!C6, etc.) -- asi las dos piezas quedan
consistentes por construccion, no por casualidad.

Los ratios historicos (interes/EBIT, D&A/ingresos, capex/ingresos, etc.) se
promedian de los ultimos anios disponibles, igual que el Excel (AVERAGE de 3
anios). `historical_ratios_from_actuals` hace ese promedio si se tienen los
datos linea por linea; si no, se le pueden pasar los ratios ya calculados --
mas adaptable a una empresa con menos historia disponible.
"""
from __future__ import annotations

from dataclasses import dataclass

from jmr_valuation.models.dcf import YearProjection


@dataclass(frozen=True)
class HistoricalRatios:
    interest_pct_of_ebit: float
    da_pct_of_revenue: float
    capex_pct_of_revenue: float
    nwc_change_pct_of_revenue_growth: float
    net_borrowing_pct_of_revenue: float
    shares_growth_rate: float
    dividend_growth_rate: float


def historical_ratios_from_actuals(
    revenues: list[float],       # ultimos N anios, el mas antiguo primero
    prior_year_revenue: float,   # un anio antes del primero de `revenues` (solo para calcular su crecimiento)
    ebit: list[float],
    interest_other: list[float],
    da: list[float],
    capex: list[float],          # magnitud positiva del gasto de capital (no el signo de flujo de caja)
    nwc_change: list[float],
    net_borrowing: list[float],
    shares_diluted: list[float],
    prior_year_shares_diluted: float,
    dividends_per_share_oldest_and_newest: tuple[float, float] | None = None,
    years_between_dividends: int = 9,
) -> HistoricalRatios:
    """Promedia los ratios historicos igual que las filas 11/20/21/22/28/32 del Excel."""
    n = len(revenues)
    if not (len(ebit) == len(interest_other) == len(da) == len(capex)
            == len(nwc_change) == len(net_borrowing) == len(shares_diluted) == n):
        raise ValueError("Todas las listas historicas deben tener la misma longitud")
    if n < 1:
        raise ValueError("Se necesita al menos 1 anio de historia")

    revenues_with_prior = [prior_year_revenue] + revenues
    revenue_growth = [revenues_with_prior[i + 1] - revenues_with_prior[i] for i in range(n)]
    shares_with_prior = [prior_year_shares_diluted] + shares_diluted
    shares_growth = [(shares_with_prior[i + 1] / shares_with_prior[i]) - 1 for i in range(n)]

    interest_pct = sum(interest_other[i] / ebit[i] for i in range(n)) / n
    da_pct = sum(da[i] / revenues[i] for i in range(n)) / n
    capex_pct = sum(capex[i] / revenues[i] for i in range(n)) / n
    net_borrowing_pct = sum(net_borrowing[i] / revenues[i] for i in range(n)) / n
    nwc_pct = sum(
        nwc_change[i] / revenue_growth[i] for i in range(n) if revenue_growth[i] != 0
    ) / n
    shares_growth_rate = sorted(shares_growth)[len(shares_growth) // 2]  # mediana

    if dividends_per_share_oldest_and_newest is not None:
        dps_old, dps_new = dividends_per_share_oldest_and_newest
        dividend_growth_rate = (dps_new / dps_old) ** (1 / years_between_dividends) - 1 if dps_old else 0.0
    else:
        dividend_growth_rate = 0.0

    return HistoricalRatios(
        interest_pct_of_ebit=interest_pct, da_pct_of_revenue=da_pct, capex_pct_of_revenue=capex_pct,
        nwc_change_pct_of_revenue_growth=nwc_pct, net_borrowing_pct_of_revenue=net_borrowing_pct,
        shares_growth_rate=shares_growth_rate, dividend_growth_rate=dividend_growth_rate,
    )


@dataclass(frozen=True)
class MultiplesYear:
    year_label: str
    revenue: float
    ebit: float
    ebt: float
    net_income: float
    ebitda: float
    fcff: float
    fcff_per_share: float
    ocf: float
    ocf_per_share: float
    fcfe: float
    fcfe_per_share: float
    shares_diluted: float
    eps: float
    dividend_per_share: float
    cumulative_dividends_per_share: float


def project_financials_multiples(
    base_year_revenue: float,
    base_year_shares_diluted: float,
    base_year_dividend_per_share: float,
    year_projections: list[YearProjection],  # FY+1..FY+n, de dcf.run_dcf (usa .revenue_growth, .ebit_margin, .tax_rate)
    ratios: HistoricalRatios,
) -> list[MultiplesYear]:
    """Replica las filas 4-37 (bloque de un escenario) de 'Financials Multiples'."""
    results = []
    revenue_prev = base_year_revenue
    shares_prev = base_year_shares_diluted
    dividend_prev = base_year_dividend_per_share
    cumulative_dividends = 0.0

    for i, yp in enumerate(year_projections, start=1):
        revenue = revenue_prev * (1 + yp.revenue_growth)
        ebit = revenue * yp.ebit_margin
        interest_other = ebit * ratios.interest_pct_of_ebit
        ebt = ebit + interest_other
        taxes = ebt * yp.tax_rate
        net_income = ebt - taxes
        da = ratios.da_pct_of_revenue * revenue
        capex = ratios.capex_pct_of_revenue * revenue
        nwc_change = ratios.nwc_change_pct_of_revenue_growth * (revenue - revenue_prev)
        net_borrowing = ratios.net_borrowing_pct_of_revenue * revenue
        ebitda = ebit + da

        fcff = ebit * (1 - yp.tax_rate) + da - capex - nwc_change
        ocf = net_income + da - nwc_change
        fcfe = net_income + da - capex - nwc_change + net_borrowing

        shares = shares_prev * (1 + ratios.shares_growth_rate)
        dividend = dividend_prev * (1 + ratios.dividend_growth_rate)
        cumulative_dividends += dividend

        results.append(MultiplesYear(
            year_label=f"FY+{i}", revenue=revenue, ebit=ebit, ebt=ebt, net_income=net_income,
            ebitda=ebitda, fcff=fcff, fcff_per_share=fcff / shares, ocf=ocf,
            ocf_per_share=ocf / shares, fcfe=fcfe, fcfe_per_share=fcfe / shares,
            shares_diluted=shares, eps=net_income / shares, dividend_per_share=dividend,
            cumulative_dividends_per_share=cumulative_dividends,
        ))

        revenue_prev, shares_prev, dividend_prev = revenue, shares, dividend

    return results
