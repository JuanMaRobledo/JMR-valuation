"""Puntaje de calidad (0-100), filtros duros y alertas del screener.

Dos capas, a proposito separadas:

1. Filtros duros -- condiciones minimas SIN las cuales un negocio no puede
   ser "maravilloso", por buenos que sean el resto de los numeros. Salen del
   Paso 3 de la metodologia (deuda neta/EBITDA > 3x = red flag, caja
   operativa negativa = alarma seria) y del criterio Buffett de ROIC alto y
   sostenido.
2. Puntaje -- cada metrica se lleva a 0..1 con una rampa lineal entre un
   umbral "malo" y uno "excelente" y se pondera. Una metrica sin dato
   (p. ej. margen bruto en una empresa de software que no reporta costo de
   ventas) se saca del calculo y se renormaliza el resto; si falta mas del
   30% del peso, se marca como "datos incompletos".

Los umbrales viven en constantes (no enterrados en el codigo) para poder
ajustarlos -- son un punto de partida razonable, no una verdad.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from jmr_valuation.screener.metrics import QualityMetrics

# (metrica, peso, umbral malo, umbral excelente, grupo). Si "malo" > "excelente"
# la metrica es de "menos es mejor" (deuda, dilucion, SBC).
CRITERIA: list[tuple[str, float, float, float, str]] = [
    ("roic_median_5y",            15, 0.10, 0.30, "Rentabilidad"),
    ("roic_min_5y",               10, 0.06, 0.20, "Rentabilidad"),
    ("gross_margin_median_5y",     7, 0.25, 0.65, "Moat"),
    ("gross_margin_std_5y",        5, 0.08, 0.015, "Moat"),
    ("operating_margin_median_5y", 8, 0.08, 0.30, "Moat"),
    ("fcf_margin_median_5y",       8, 0.03, 0.25, "Caja"),
    ("fcf_positive_ratio",         6, 0.70, 1.00, "Caja"),
    ("fcf_conversion_5y",          6, 0.60, 1.10, "Caja"),
    ("revenue_cagr_5y",            8, 0.00, 0.15, "Crecimiento"),
    ("fcf_per_share_cagr_5y",      7, 0.00, 0.15, "Crecimiento"),
    ("revenue_growth_consistency", 3, 0.50, 0.90, "Crecimiento"),
    ("net_debt_to_ebitda",         8, 3.00, 0.50, "Balance"),
    ("interest_coverage",          3, 4.00, 15.0, "Balance"),
    ("shares_cagr_5y",             4, 0.03, -0.02, "Capital"),
    ("sbc_pct_revenue",            2, 0.10, 0.02, "Capital"),
]
MIN_WEIGHT_COVERAGE = 0.70

# Filtros duros
MIN_YEARS = 5
MIN_ROIC_MEDIAN_5Y = 0.12
MIN_FCF_POSITIVE_LAST_5Y = 4
MAX_NET_DEBT_TO_EBITDA = 3.0
MIN_REVENUE_CAGR_5Y = 0.0

# Clasificacion (solo para quienes pasan los filtros duros)
TIERS: list[tuple[float, str]] = [
    (82, "Maravillosa"),
    (68, "Muy buena"),
    (52, "Aceptable"),
    (0, "Mediocre"),
]
NOT_PASSING = "No pasa filtros"


@dataclass
class QualityScore:
    score: float                       # 0-100
    coverage: float                    # fraccion del peso con dato
    group_scores: dict[str, float]     # 0-100 por grupo
    passes_filters: bool
    failed_filters: list[str] = field(default_factory=list)
    flags: list[str] = field(default_factory=list)
    tier: str = NOT_PASSING


def _ramp(value: float, bad: float, good: float) -> float:
    if good == bad:
        return 1.0 if value >= good else 0.0
    t = (value - bad) / (good - bad)
    return max(0.0, min(1.0, t))


def _metric_value(m: QualityMetrics, name: str) -> float | None:
    value = getattr(m, name)
    # Sin gasto financiero y con caja neta no hay cobertura que medir: es el
    # mejor caso posible, no un faltante.
    if name == "interest_coverage" and value is None and m.net_debt_to_ebitda is not None and m.net_debt_to_ebitda <= 0:
        return float("inf")
    return value


def _hard_filters(m: QualityMetrics) -> list[str]:
    failed: list[str] = []
    if m.years < MIN_YEARS:
        failed.append(f"Historia insuficiente ({m.years} FY < {MIN_YEARS})")
    if m.roic_median_5y is None or m.roic_median_5y < MIN_ROIC_MEDIAN_5Y:
        shown = "s/d" if m.roic_median_5y is None else f"{m.roic_median_5y:.0%}"
        failed.append(f"ROIC mediano 5a {shown} < {MIN_ROIC_MEDIAN_5Y:.0%}")
    if m.fcf_positive_last_5y is None or m.fcf_positive_last_5y < MIN_FCF_POSITIVE_LAST_5Y:
        failed.append(f"FCF positivo en {m.fcf_positive_last_5y or 0} de los ultimos 5 FY")
    if m.net_debt_to_ebitda is None and (m.fcf_ltm is None or m.fcf_ltm <= 0):
        failed.append("EBITDA LTM <= 0")
    elif m.net_debt_to_ebitda is not None and m.net_debt_to_ebitda > MAX_NET_DEBT_TO_EBITDA:
        failed.append(f"Deuda neta/EBITDA {m.net_debt_to_ebitda:.1f}x > {MAX_NET_DEBT_TO_EBITDA:.0f}x")
    if m.revenue_cagr_5y is not None and m.revenue_cagr_5y < MIN_REVENUE_CAGR_5Y:
        failed.append(f"Ingresos cayendo (CAGR 5a {m.revenue_cagr_5y:.1%})")
    return failed


def _flags(m: QualityMetrics) -> list[str]:
    """Alertas (no descalifican solas): lo que la metodologia pide revisar a mano."""
    flags: list[str] = []
    nd = m.net_debt_to_ebitda
    if nd is not None and 2.0 < nd <= MAX_NET_DEBT_TO_EBITDA:
        flags.append(f"Deuda en el limite ({nd:.1f}x EBITDA)")
    if (m.roe_median_5y is not None and m.roic_median_5y is not None
            and m.roe_median_5y > 0.30 and m.roe_median_5y > 2 * m.roic_median_5y):
        flags.append("ROE inflado vs ROIC (apalancamiento/recompras)")
    if m.negative_equity:
        flags.append("Patrimonio negativo (recompras acumuladas)")
    if (m.operating_margin_ltm is not None and m.operating_margin_median_5y is not None
            and m.operating_margin_ltm < m.operating_margin_median_5y - 0.03):
        flags.append("Margen operativo comprimiendose vs 5a")
    if m.roic_last is not None and m.roic_median_5y is not None and m.roic_last < 0.7 * m.roic_median_5y:
        flags.append("ROIC del ultimo FY muy por debajo de su mediana")
    if m.fcf_conversion_5y is not None and m.fcf_conversion_5y < 0.7:
        flags.append("Utilidades que no se convierten en caja (FCF/NI < 70%)")
    if m.shares_cagr_5y is not None and m.shares_cagr_5y > 0.02:
        flags.append(f"Dilucion ({m.shares_cagr_5y:+.1%} acciones/anio)")
    if m.sbc_pct_revenue is not None and m.sbc_pct_revenue > 0.08:
        flags.append(f"SBC alto ({m.sbc_pct_revenue:.0%} de ingresos)")
    if m.fcf_ltm is not None and m.fcf_ltm <= 0:
        flags.append("FCF LTM negativo")
    return flags


def score_metrics(m: QualityMetrics) -> QualityScore:
    total_weight = sum(c[1] for c in CRITERIA)
    got = used = 0.0
    group_got: dict[str, float] = {}
    group_used: dict[str, float] = {}
    for name, weight, bad, good, group in CRITERIA:
        value = _metric_value(m, name)
        if value is None:
            continue
        points = weight * _ramp(value, bad, good)
        got += points
        used += weight
        group_got[group] = group_got.get(group, 0.0) + points
        group_used[group] = group_used.get(group, 0.0) + weight

    score = 100 * got / used if used else 0.0
    coverage = used / total_weight
    failed = _hard_filters(m)
    flags = _flags(m)
    if coverage < MIN_WEIGHT_COVERAGE:
        flags.append(f"Datos incompletos ({coverage:.0%} del puntaje con dato)")

    tier = NOT_PASSING
    if not failed:
        tier = next(label for threshold, label in TIERS if score >= threshold)
        if tier == "Maravillosa" and coverage < MIN_WEIGHT_COVERAGE:
            tier = "Muy buena"  # no se corona con datos a medias

    return QualityScore(
        score=round(score, 1),
        coverage=round(coverage, 2),
        group_scores={g: round(100 * group_got[g] / group_used[g], 1) for g in group_used},
        passes_filters=not failed,
        failed_filters=failed,
        flags=flags,
        tier=tier,
    )
