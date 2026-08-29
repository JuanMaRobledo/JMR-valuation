"""Valoracion de opciones sobre acciones para empleados (hoja 'Option value').

El Excel original resuelve esto con una referencia circular deliberada (el precio
ajustado por dilucion depende del valor de la opcion, que depende del precio
ajustado) y pide activar "calculo iterativo" en Excel/Sheets para que converja.
Aca se resuelve la misma circularidad con iteracion de punto fijo.
"""
from __future__ import annotations

import math
from dataclasses import dataclass


def _norm_cdf(x: float) -> float:
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


@dataclass(frozen=True)
class OptionValueResult:
    value_per_option: float
    total_value: float
    adjusted_stock_price: float
    iterations: int


def dilution_adjusted_black_scholes(
    stock_price: float,
    strike_price: float,
    expiration_years: float,
    volatility: float,
    dividend_yield: float,
    riskfree_rate: float,
    n_options: float,
    n_shares: float,
    max_iterations: int = 100,
    tolerance: float = 0.001,
) -> OptionValueResult:
    """Replica B16:B30 de 'Option value'.

    Formulas (con S = precio ajustado, que se resuelve por iteracion):
        d1 = (ln(S/K) + (r - q + var/2) * T) / sqrt(var * T)
        d2 = d1 - sqrt(var * T)
        valor_opcion = S * exp(-q*T) * N(d1) - K * exp(-r*T) * N(d2)
        S_ajustado = (precio*acciones + valor_opcion*opciones) / (acciones + opciones)
    """
    if n_shares <= 0:
        raise ValueError("n_shares debe ser > 0")

    variance = volatility ** 2
    adjusted_s = stock_price  # arranca igual que el precio de mercado (B18 inicial)

    value_per_option = 0.0
    for i in range(1, max_iterations + 1):
        d1 = (
            math.log(adjusted_s / strike_price)
            + (riskfree_rate - dividend_yield + variance / 2) * expiration_years
        ) / math.sqrt(variance * expiration_years)
        d2 = d1 - math.sqrt(variance * expiration_years)

        new_value_per_option = (
            math.exp(-dividend_yield * expiration_years) * adjusted_s * _norm_cdf(d1)
            - strike_price * math.exp(-riskfree_rate * expiration_years) * _norm_cdf(d2)
        )

        new_adjusted_s = (
            stock_price * n_shares + new_value_per_option * n_options
        ) / (n_shares + n_options)

        converged = abs(new_adjusted_s - adjusted_s) < tolerance and abs(
            new_value_per_option - value_per_option
        ) < tolerance
        adjusted_s = new_adjusted_s
        value_per_option = new_value_per_option
        if converged:
            break

    return OptionValueResult(
        value_per_option=value_per_option,
        total_value=value_per_option * n_options,
        adjusted_stock_price=adjusted_s,
        iterations=i,
    )
