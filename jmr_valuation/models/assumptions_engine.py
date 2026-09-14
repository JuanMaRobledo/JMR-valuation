"""Puerto 1:1 de la hoja 'Motor de Supuestos v2' del Excel: combina el
crecimiento historico real (LTM, CAGR 3/5/Ny) con el crecimiento de industria,
y el margen EBIT actual/mediana historica con el margen de industria, cada uno
ponderado segun el escenario (Conservador/Base/Optimista). El resultado
alimenta directamente a `models.dcf.run_dcf` (mismo motor de proyeccion a 10
anios que ya usa 'Valuation output' -- esta hoja no reinventa el DCF, solo
resuelve mejor los supuestos de entrada).

Los pesos de la Seccion 0 (A6:E18 del Excel) son calibracion del propio
modelo del usuario, no datos de una empresa/industria particular -- se portan
tal cual, no son un dato que haya que "no inventar".
"""
from __future__ import annotations

import statistics
from dataclasses import dataclass

from jmr_valuation.io import reference_data as ref
from jmr_valuation.io.sec_edgar_loader import AnnualSeries
from jmr_valuation.models.dcf import GrowthAndMarginPath, TerminalAssumptions

SCENARIOS = ("Conservador", "Base", "Optimista")


@dataclass(frozen=True)
class ScenarioWeights:
    """Fila 8-18 de 'Motor de Supuestos v2', columna del escenario."""

    weight_ltm: float
    weight_cagr3: float
    weight_cagr5: float
    weight_cagr_long: float
    industry_growth_weight: float     # peso a industria en crecimiento Año 1 (fila 13)
    growth_convergence_years: int     # fila 14
    industry_margin_weight: float     # peso a industria en margen objetivo (fila 15)
    margin_convergence_years: int     # fila 16


# Valores por defecto del Excel (filas 8-16, columnas B/C/D). Calibracion del
# modelo, igual para cualquier empresa -- no depende del ticker.
SCENARIO_WEIGHTS: dict[str, ScenarioWeights] = {
    "Conservador": ScenarioWeights(0.10, 0.20, 0.30, 0.40, 0.50, 5, 0.60, 7),
    "Base": ScenarioWeights(0.25, 0.25, 0.25, 0.25, 0.30, 7, 0.40, 5),
    "Optimista": ScenarioWeights(0.40, 0.30, 0.20, 0.10, 0.15, 10, 0.20, 3),
}


def _cagr(first: float, last: float, years: int) -> float:
    if years < 1 or first <= 0:
        return 0.0
    return (last / first) ** (1 / years) - 1


@dataclass(frozen=True)
class GrowthEngineResult:
    ltm_growth: float
    cagr_3y: float
    cagr_5y: float
    cagr_long: float
    cagr_long_years: int          # N intervalos usados (fila 34: "9 años" si hay 10 FY)
    industry_growth_us: float
    industry_growth_global: float
    combined_historical: float    # fila 37
    growth_year1: float           # fila 38: alimenta GrowthAndMarginPath.year1_growth


def run_growth_engine(
    series: AnnualSeries, weights: ScenarioWeights, *, industry_us: str, industry_global: str,
) -> GrowthEngineResult:
    revenue = series.revenue
    if len(revenue) < 2:
        raise ValueError("Se necesitan al menos 2 anios de historico de revenue para el motor de crecimiento")

    ltm_growth = series.ltm_revenue / revenue[-1] - 1

    n3 = min(3, len(revenue) - 1)
    cagr_3y = _cagr(revenue[-1 - n3], revenue[-1], n3)
    n5 = min(5, len(revenue) - 1)
    cagr_5y = _cagr(revenue[-1 - n5], revenue[-1], n5)
    n_long = len(revenue) - 1
    cagr_long = _cagr(revenue[0], revenue[-1], n_long)

    industry_growth_us = ref.get_industry_average(industry_us, global_=False).revenue_growth_5y
    industry_growth_global = ref.get_industry_average(industry_global, global_=True).revenue_growth_5y

    combined_historical = (
        ltm_growth * weights.weight_ltm
        + cagr_3y * weights.weight_cagr3
        + cagr_5y * weights.weight_cagr5
        + cagr_long * weights.weight_cagr_long
    )
    industry_avg = (industry_growth_us + industry_growth_global) / 2
    growth_year1 = (
        combined_historical * (1 - weights.industry_growth_weight)
        + industry_avg * weights.industry_growth_weight
    )

    return GrowthEngineResult(
        ltm_growth=ltm_growth, cagr_3y=cagr_3y, cagr_5y=cagr_5y, cagr_long=cagr_long,
        cagr_long_years=n_long, industry_growth_us=industry_growth_us,
        industry_growth_global=industry_growth_global, combined_historical=combined_historical,
        growth_year1=growth_year1,
    )


@dataclass(frozen=True)
class MarginEngineResult:
    ebit_margin_actual: float
    ebit_margin_median_5y: float     # fila 44
    industry_margin_us: float
    industry_margin_global: float
    target_ebit_margin: float        # fila 47: alimenta GrowthAndMarginPath.target_ebit_margin


def run_margin_engine(
    series: AnnualSeries, weights: ScenarioWeights, *, industry_us: str, industry_global: str,
) -> MarginEngineResult:
    margins = [e / r for e, r in zip(series.ebit, series.revenue) if r]
    if not margins:
        raise ValueError("No hay margenes EBIT historicos (revenue/ebit vacios)")
    ebit_margin_actual = series.ltm_ebit / series.ltm_revenue if series.ltm_revenue else margins[-1]
    tail_5 = margins[-5:]
    ebit_margin_median_5y = statistics.median(tail_5)

    industry_margin_us = ref.get_industry_average(industry_us, global_=False).pretax_operating_margin
    industry_margin_global = ref.get_industry_average(industry_global, global_=True).pretax_operating_margin

    best_historical = max(ebit_margin_actual, ebit_margin_median_5y)
    industry_avg = (industry_margin_us + industry_margin_global) / 2
    target_ebit_margin = (
        best_historical * (1 - weights.industry_margin_weight)
        + industry_avg * weights.industry_margin_weight
    )

    return MarginEngineResult(
        ebit_margin_actual=ebit_margin_actual, ebit_margin_median_5y=ebit_margin_median_5y,
        industry_margin_us=industry_margin_us, industry_margin_global=industry_margin_global,
        target_ebit_margin=target_ebit_margin,
    )


@dataclass(frozen=True)
class SalesToCapital:
    """Fila 17-18: Sales-to-Capital por escenario. El Excel usa cuartiles de
    una distribucion de industria que no esta en nuestros CSV de referencia
    (solo tenemos el promedio) -- Base usa el promedio global de industria
    (coincide exacto con el Excel de referencia), y Conservador/Optimista
    quedan en ese mismo valor salvo que el usuario pase un override real
    (no se inventa un spread arbitrario, ver README/instrucciones del pipeline)."""

    conservative: float
    base: float
    optimistic: float

    def for_scenario(self, scenario: str) -> float:
        return {"Conservador": self.conservative, "Base": self.base, "Optimista": self.optimistic}[scenario]


def resolve_sales_to_capital(
    *, industry_global: str, overrides: dict[str, float] | None = None,
) -> SalesToCapital:
    base = ref.get_industry_average(industry_global, global_=True).sales_to_capital
    overrides = overrides or {}
    return SalesToCapital(
        conservative=overrides.get("Conservador", base),
        base=overrides.get("Base", base),
        optimistic=overrides.get("Optimista", base),
    )


@dataclass(frozen=True)
class AssumptionsEngineResult:
    scenario: str
    weights: ScenarioWeights
    growth: GrowthEngineResult
    margin: MarginEngineResult
    sales_to_capital_1_5: float
    sales_to_capital_6_10: float


def run_assumptions_engine(
    series: AnnualSeries,
    scenario: str,
    *,
    industry_us: str,
    industry_global: str,
    sales_to_capital: SalesToCapital,
) -> AssumptionsEngineResult:
    if scenario not in SCENARIO_WEIGHTS:
        raise ValueError(f"Escenario desconocido: {scenario!r}. Opciones: {SCENARIOS}")
    weights = SCENARIO_WEIGHTS[scenario]
    growth = run_growth_engine(series, weights, industry_us=industry_us, industry_global=industry_global)
    margin = run_margin_engine(series, weights, industry_us=industry_us, industry_global=industry_global)
    stc = sales_to_capital.for_scenario(scenario)

    return AssumptionsEngineResult(
        scenario=scenario, weights=weights, growth=growth, margin=margin,
        sales_to_capital_1_5=stc, sales_to_capital_6_10=stc,
    )


def growth_and_margin_path(result: AssumptionsEngineResult) -> GrowthAndMarginPath:
    """Arma el input que espera `dcf.run_dcf` (fila 67/69 del Excel: Año1 =
    growth_year1, Años2-5 tambien = growth_year1 -- 'Motor de Supuestos v2' no
    distingue Año1 de 2-5 como si hace 'Valuation output' original, converge
    directo desde Año1 hacia el crecimiento estable).

    Simplificacion consciente: el Excel converge linealmente desde Año1 hacia
    el crecimiento estable durante exactamente `weights.growth_convergence_years`
    (5/7/10 segun escenario). `dcf.run_dcf` (reusado tal cual, sin tocar, por
    ser el motor ya validado de 'Valuation output') tiene ese numero fijo en 5
    y siempre a partir del año 6 -- coincide exacto para Conservador (5 años) y
    difiere unos años para Base/Optimista (7/10). `weights.growth_convergence_years`
    igual se expone en `AssumptionsEngineResult` para mostrarlo en la hoja de
    supuestos, aunque no mueva el DCF -- si hace falta la convergencia exacta,
    es el proximo paso natural (parametrizar `run_dcf`)."""
    return GrowthAndMarginPath(
        year1_growth=result.growth.growth_year1,
        years_2_to_5_growth=result.growth.growth_year1,
        target_ebit_margin=result.margin.target_ebit_margin,
        year_of_margin_convergence=result.weights.margin_convergence_years,
    )


def terminal_assumptions(result: AssumptionsEngineResult, *, riskfree_rate: float, wacc_current: float) -> TerminalAssumptions:
    """Fila 39/55: crecimiento estable = riskfree rate (igual que el motor
    original); WACC estable = WACC actual por defecto (asi lo deja 'Input
    sheet'!B47 salvo override) -- a diferencia del motor original, que por
    defecto usa riskfree + prima madura. Es una diferencia real y documentada
    entre las dos hojas del Excel, no un error de puerto."""
    return TerminalAssumptions(riskfree_rate=riskfree_rate, terminal_wacc_override=wacc_current)
