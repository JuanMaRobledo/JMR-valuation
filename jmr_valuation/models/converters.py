"""Convierte partidas fuera de balance en deuda/activo de capital.

Replica 'Operating lease converter' y 'R& D converter' del Excel, formula por
formula (mismas referencias de celda en los comentarios).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OperatingLeaseResult:
    debt_value: float          # C29: Debt Value of leases
    ebit_adjustment: float     # F33: Adjustment to Operating Earnings (sumar al EBIT)
    debt_adjustment: float     # F34: Adjustment to Total Debt outstanding
    depreciation: float        # F32/F35: Depreciation on Operating Lease Asset


def capitalize_operating_leases(
    current_year_lease_expense: float,
    commitments_years_1_to_5: list[float],
    commitment_year_6_plus: float,
    pretax_cost_of_debt: float,
) -> OperatingLeaseResult:
    """Convierte compromisos de leasing operativo en deuda (hoja 'Operating lease converter').

    commitments_years_1_to_5: compromisos de los proximos 5 anios, en orden (anio 1 primero).
    commitment_year_6_plus: compromiso remanente a partir del anio 6 (suma total, no anual).
    """
    if len(commitments_years_1_to_5) != 5:
        raise ValueError("Se esperan exactamente 5 compromisos (anios 1 a 5)")

    r = pretax_cost_of_debt

    # D19: numero de anios de leasing embebidos en la estimacion del anio 6+
    avg_first_five = sum(commitments_years_1_to_5) / 5
    n_years_yr6 = round(commitment_year_6_plus / avg_first_five) if (
        commitment_year_6_plus > 0 and avg_first_five != 0
    ) else 0

    # C23:C27 - valor presente de los compromisos de los anios 1 a 5
    pv_years_1_5 = [
        commitments_years_1_to_5[i] / (1 + r) ** (i + 1) for i in range(5)
    ]

    # B28 / C28 - el remanente (anio 6+) convertido en anualidad
    if commitment_year_6_plus > 0:
        annual_yr6 = commitment_year_6_plus / n_years_yr6 if n_years_yr6 > 0 else commitment_year_6_plus
    else:
        annual_yr6 = 0.0

    if n_years_yr6 > 0:
        pv_year6_plus = (annual_yr6 * (1 - (1 + r) ** (-n_years_yr6)) / r) / (1 + r) ** 5
    else:
        pv_year6_plus = annual_yr6 / (1 + r) ** 6

    debt_value = sum(pv_years_1_5) + pv_year6_plus  # C29

    depreciation = debt_value / (5 + n_years_yr6)  # F32 / F35
    ebit_adjustment = current_year_lease_expense - depreciation  # F33

    return OperatingLeaseResult(
        debt_value=debt_value,
        ebit_adjustment=ebit_adjustment,
        debt_adjustment=debt_value,
        depreciation=depreciation,
    )


@dataclass(frozen=True)
class RDCapitalizationResult:
    research_asset_value: float   # D36: Value of Research Asset
    amortization_current_year: float  # D38/E36: Amortization of asset for current year
    ebit_adjustment: float        # D40: Adjustment to Operating Income
    tax_effect: float             # D41: Tax Effect of R&D Expensing


def capitalize_rd(
    amortization_years: int,
    current_year_rd_expense: float,
    past_years_rd_expense: list[float],
    tax_rate: float,
) -> RDCapitalizationResult:
    """Capitaliza gasto de I+D (hoja 'R& D converter').

    past_years_rd_expense: gasto de I+D de anios anteriores, el mas reciente primero
        (anio -1, -2, -3, ...). Se usan los primeros `amortization_years` valores
        (anio -1 hasta -amortization_years): para amortizacion a 3 anios, el ano -3
        todavia aporta su cuota de amortizacion de este ano aunque su valor de activo
        remanente ya sea 0 -- confirmado celda por celda contra 'R& D converter'
        (E26:E28 suman los 3 anios cuando F7=3, no solo los primeros 2).
    """
    if amortization_years < 1:
        raise ValueError("amortization_years debe ser >= 1")

    years_used = past_years_rd_expense[:amortization_years]

    value_current = current_year_rd_expense * 1.0  # D25 (C25=1, fraccion no amortizada = 100%)

    value_past = []
    amort_past = []
    for k, rd_expense in enumerate(years_used, start=1):
        fraction_unamortized = (amortization_years - k) / amortization_years  # C26=(F7+A26)/F7
        value_past.append(rd_expense * fraction_unamortized)               # D26
        amort_past.append(rd_expense / amortization_years)                  # E26

    research_asset_value = value_current + sum(value_past)      # D36
    amortization_current_year = sum(amort_past)                  # E36 / D38

    ebit_adjustment = current_year_rd_expense - amortization_current_year  # D40
    tax_effect = ebit_adjustment * tax_rate  # D41

    return RDCapitalizationResult(
        research_asset_value=research_asset_value,
        amortization_current_year=amortization_current_year,
        ebit_adjustment=ebit_adjustment,
        tax_effect=tax_effect,
    )
