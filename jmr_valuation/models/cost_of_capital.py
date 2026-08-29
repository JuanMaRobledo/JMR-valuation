"""Costo de capital: costo de deuda, costo de equity y WACC.

Replica la hoja 'Cost of capital worksheet'. Por ahora cubre los dos enfoques mas
usados de esa hoja -- input directo y promedio de industria -- mas el calculo
detallado (equity/deuda/preferentes ponderados). Los enfoques de "distribucion
cross-seccional" (Approach 3) y "rating actual" completo quedan para una
siguiente pasada; se documentan como TODO explicito, no se simulan.
"""
from __future__ import annotations

from dataclasses import dataclass

from jmr_valuation.io import reference_data as ref

# Risk-free rate que Damodaran usaba como base al publicar los promedios de
# industria de este archivo (B35-4.58% en 'Cost of capital worksheet'!B68).
# Al actualizar los CSV de referencia, actualizar tambien esta constante segun
# la nota que acompanie los nuevos datos de Damodaran.
INDUSTRY_BASELINE_RISKFREE_RATE = 0.0458

# Tablas de rating sintetico (hoja 'Synthetic rating'), cada tupla es
# (limite_inferior_inclusive_del_ratio_de_cobertura, rating, spread)
_LARGE_MANUFACTURING_RATINGS = [
    (-100000, "D2/D", 0.19), (0.2, "C2/C", 0.16), (0.65, "Ca2/CC", 0.126101),
    (0.8, "Caa/CCC", 0.0885), (1.25, "B3/B-", 0.050899), (1.5, "B2/B", 0.032098),
    (1.75, "B1/B+", 0.027531), (2.0, "Ba2/BB", 0.018395), (2.25, "Ba1/BB+", 0.013828),
    (2.5, "Baa2/BBB", 0.011113), (3.0, "A3/A-", 0.008872), (4.25, "A2/A", 0.007751),
    (5.5, "A1/A+", 0.007003), (6.5, "Aa2/AA", 0.005506), (8.5, "Aaa/AAA", 0.004),
]
_SMALL_RISKIER_RATINGS = [
    (-100000, "D2/D", 0.19), (0.5, "C2/C", 0.16), (0.8, "Ca2/CC", 0.126101),
    (1.25, "Caa/CCC", 0.0885), (1.5, "B3/B-", 0.050899), (2.0, "B2/B", 0.032098),
    (2.5, "B1/B+", 0.027531), (3.0, "Ba2/BB", 0.018395), (3.5, "Ba1/BB+", 0.013828),
    (4.0, "Baa2/BBB", 0.011113), (4.5, "A3/A-", 0.008872), (6.0, "A2/A", 0.007751),
    (7.5, "A1/A+", 0.007003), (9.5, "Aa2/AA", 0.005506), (12.5, "Aaa/AAA", 0.004),
]
# Hoja 'Synthetic rating'!G43:H57 -- tabla de rating (texto) a spread, usada por
# el enfoque "Actual rating" ('Cost of capital worksheet'!B38, tercera rama).
RATING_TO_SPREAD = {
    "A1/A+": 0.007003, "A2/A": 0.007751, "A3/A-": 0.008872,
    "Aa2/AA": 0.005506, "Aaa/AAA": 0.004,
    "B1/B+": 0.027531, "B2/B": 0.032098, "B3/B-": 0.050899,
    "Ba1/BB+": 0.013828, "Ba2/BB": 0.018395, "Baa2/BBB": 0.011113,
    "C2/C": 0.16, "Ca2/CC": 0.126101, "Caa/CCC": 0.0885, "D2/D": 0.19,
}


def synthetic_rating_spread(interest_coverage_ratio: float, *, small_firm: bool = False):
    """D14/D15 de 'Synthetic rating': devuelve (rating, spread) por ratio de cobertura."""
    table = _SMALL_RISKIER_RATINGS if small_firm else _LARGE_MANUFACTURING_RATINGS
    best = table[0]
    for lower_bound, rating, spread in table:
        if interest_coverage_ratio >= lower_bound:
            best = (lower_bound, rating, spread)
        else:
            break
    return best[1], best[2]


def interest_coverage_ratio(ebit: float, interest_expense: float) -> float:
    """D13 de 'Synthetic rating'."""
    if interest_expense == 0:
        return 1_000_000.0
    if ebit < 0:
        return -100_000.0
    return ebit / interest_expense


def cost_of_debt_synthetic_rating(
    ebit: float, interest_expense: float, riskfree_rate: float,
    country_default_spread: float = 0.0, *, small_firm: bool = False,
) -> float:
    """D17 de 'Synthetic rating': riskfree + spread de rating + spread-pais."""
    coverage = interest_coverage_ratio(ebit, interest_expense)
    _, spread = synthetic_rating_spread(coverage, small_firm=small_firm)
    return riskfree_rate + spread + country_default_spread


def cost_of_debt_actual_rating(riskfree_rate: float, rating: str) -> float:
    """'Cost of capital worksheet'!B38, rama 'Actual rating': riskfree + spread(rating)."""
    if rating not in RATING_TO_SPREAD:
        raise KeyError(f"Rating no reconocido: {rating!r}. Opciones: {sorted(RATING_TO_SPREAD)}")
    return riskfree_rate + RATING_TO_SPREAD[rating]


def unlevered_to_levered_beta(unlevered_beta: float, tax_rate: float, debt_to_equity: float) -> float:
    """C58: beta_L = beta_U * (1 + (1 - t) * D/E)."""
    return unlevered_beta * (1 + (1 - tax_rate) * debt_to_equity)


def cost_of_equity(riskfree_rate: float, levered_beta: float, equity_risk_premium: float) -> float:
    """B63: Ke = Rf + beta_L * ERP."""
    return riskfree_rate + levered_beta * equity_risk_premium


def weighted_average_erp(country_revenue_weights: dict[str, float]) -> float:
    """K19/K33: ERP ponderado por ingresos entre paises/regiones (G6:K19).

    country_revenue_weights: {nombre_de_pais: ingresos_en_ese_pais}.
    """
    total_revenue = sum(country_revenue_weights.values())
    if total_revenue == 0:
        return 0.0
    weighted = 0.0
    for country, revenue in country_revenue_weights.items():
        if revenue <= 0:
            continue
        erp = ref.get_country_erp(country).total_erp
        weighted += erp * (revenue / total_revenue)
    return weighted


@dataclass(frozen=True)
class WaccResult:
    cost_of_equity: float
    cost_of_debt_pretax: float
    cost_of_debt_aftertax: float
    weight_equity: float
    weight_debt: float
    weight_preferred: float
    wacc: float


def wacc(
    market_value_equity: float,
    market_value_debt: float,
    cost_of_equity_: float,
    cost_of_debt_pretax: float,
    tax_rate: float,
    market_value_preferred: float = 0.0,
    cost_of_preferred: float = 0.0,
) -> WaccResult:
    """B61:E63: costo de capital ponderado por valor de mercado."""
    total = market_value_equity + market_value_debt + market_value_preferred
    if total <= 0:
        raise ValueError("El valor total de mercado (equity+deuda+preferentes) debe ser > 0")

    w_e = market_value_equity / total
    w_d = market_value_debt / total
    w_p = market_value_preferred / total
    cost_of_debt_aftertax = cost_of_debt_pretax * (1 - tax_rate)

    wacc_value = w_e * cost_of_equity_ + w_d * cost_of_debt_aftertax + w_p * cost_of_preferred

    return WaccResult(
        cost_of_equity=cost_of_equity_,
        cost_of_debt_pretax=cost_of_debt_pretax,
        cost_of_debt_aftertax=cost_of_debt_aftertax,
        weight_equity=w_e,
        weight_debt=w_d,
        weight_preferred=w_p,
        wacc=wacc_value,
    )


def industry_average_cost_of_capital(
    industry: str, riskfree_rate: float, *, global_: bool = False,
) -> float:
    """B68, ramas 'Single Business(US/Global)': costo de capital de la industria,
    ajustado por la diferencia entre el riskfree rate actual y el que Damodaran
    uso como base al publicar la tabla (ver INDUSTRY_BASELINE_RISKFREE_RATE)."""
    avg = ref.get_industry_average(industry, global_=global_)
    return avg.cost_of_capital + (riskfree_rate - INDUSTRY_BASELINE_RISKFREE_RATE)
