"""Puerto de la hoja 'Motor de Supuestos v2' del Excel: combina el
crecimiento historico real (LTM, CAGR 3/5/Ny) con el crecimiento de industria,
y el margen EBIT actual/mediana historica con el margen de industria. El
resultado alimenta directamente a `models.dcf.run_dcf` (mismo motor de
proyeccion a 10 anios que ya usa 'Valuation output' -- esta hoja no reinventa
el DCF, solo resuelve mejor los supuestos de entrada).

Criterio de escenarios (Conservador/Base/Optimista), y por que no es el del
Excel original:

El Excel calculaba growth_year1/target_margin como una mezcla ponderada
historia+industria, con un vector de pesos DISTINTO por escenario (mas peso a
industria en Conservador, menos en Optimista). Eso no garantiza ningun orden
entre escenarios: dos mezclas ponderadas del mismo conjunto de numeros pueden
salir en cualquier orden entre si. Para una empresa desacelerando (ADBE en la
corrida de prueba), esa mezcla daba Conservador > Optimista -- invertido.

Este modulo usa en cambio el MINIMO y el MAXIMO del mismo conjunto de tasas
reales (LTM, CAGR 3y, CAGR 5y, CAGR largo plazo, promedio de industria) como
Conservador/Optimista, y Base sigue siendo la mezcla ponderada de siempre.
Una mezcla ponderada (pesos no negativos que suman 1) de un conjunto de
numeros SIEMPRE cae entre su minimo y su maximo -- por lo tanto
Conservador <= Base <= Optimista queda garantizado matematicamente, para
cualquier empresa, sin calibrar nada caso por caso. Mismo criterio para el
margen EBIT objetivo (min/blend/max de margen actual, mediana 5y, industria
US, industria Global) -- y coincide con el patron que ya usa
`valuation._target_ebit_margin` (el motor original del repo) para el mismo
problema.
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
    """Años de convergencia por escenario (fila 14/16 del Excel) -- lo unico
    que sigue variando por escenario. Los pesos de mezcla historia/industria
    (fila 8-13/15 del Excel) se usan una sola vez, solo para Base (ver
    BASE_BLEND_WEIGHTS) -- Conservador/Optimista ya no mezclan con pesos
    propios, toman el minimo/maximo del conjunto (ver docstring del modulo)."""

    growth_convergence_years: int     # fila 14
    margin_convergence_years: int     # fila 16


SCENARIO_WEIGHTS: dict[str, ScenarioWeights] = {
    "Conservador": ScenarioWeights(growth_convergence_years=5, margin_convergence_years=7),
    "Base": ScenarioWeights(growth_convergence_years=7, margin_convergence_years=5),
    "Optimista": ScenarioWeights(growth_convergence_years=10, margin_convergence_years=3),
}


@dataclass(frozen=True)
class _BaseBlendWeights:
    weight_ltm: float
    weight_cagr3: float
    weight_cagr5: float
    weight_cagr_long: float
    industry_growth_weight: float
    industry_margin_weight: float


# Pesos de la mezcla de Base (fila 8-15 del Excel, columna Base). Calibracion
# del modelo, igual para cualquier empresa -- no depende del ticker. Ya no se
# usan para Conservador/Optimista (ver docstring del modulo).
BASE_BLEND_WEIGHTS = _BaseBlendWeights(
    weight_ltm=0.25, weight_cagr3=0.25, weight_cagr5=0.25, weight_cagr_long=0.25,
    industry_growth_weight=0.30, industry_margin_weight=0.40,
)


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
    combined_historical: float    # mezcla de Base (LTM/CAGR3/CAGR5/CAGRlargo)
    growth_year1: float           # resultado para el escenario pedido: min/blend/max


def run_growth_engine(series: AnnualSeries, scenario: str, *, industry_us: str, industry_global: str) -> GrowthEngineResult:
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
    industry_avg = (industry_growth_us + industry_growth_global) / 2

    w = BASE_BLEND_WEIGHTS
    combined_historical = (
        ltm_growth * w.weight_ltm + cagr_3y * w.weight_cagr3
        + cagr_5y * w.weight_cagr5 + cagr_long * w.weight_cagr_long
    )
    base_blend = combined_historical * (1 - w.industry_growth_weight) + industry_avg * w.industry_growth_weight

    candidates = [ltm_growth, cagr_3y, cagr_5y, cagr_long, industry_avg]
    if scenario == "Conservador":
        growth_year1 = min(candidates)
    elif scenario == "Optimista":
        growth_year1 = max(candidates)
    else:
        growth_year1 = base_blend

    return GrowthEngineResult(
        ltm_growth=ltm_growth, cagr_3y=cagr_3y, cagr_5y=cagr_5y, cagr_long=cagr_long,
        cagr_long_years=n_long, industry_growth_us=industry_growth_us,
        industry_growth_global=industry_growth_global, combined_historical=combined_historical,
        growth_year1=growth_year1,
    )


@dataclass(frozen=True)
class MarginEngineResult:
    ebit_margin_actual: float
    ebit_margin_median_5y: float     # mediana ultimos 5 FY
    industry_margin_us: float
    industry_margin_global: float
    target_ebit_margin: float        # resultado para el escenario pedido: min/blend/max


def run_margin_engine(series: AnnualSeries, scenario: str, *, industry_us: str, industry_global: str) -> MarginEngineResult:
    margins = [e / r for e, r in zip(series.ebit, series.revenue) if r]
    if not margins:
        raise ValueError("No hay margenes EBIT historicos (revenue/ebit vacios)")
    ebit_margin_actual = series.ltm_ebit / series.ltm_revenue if series.ltm_revenue else margins[-1]
    tail_5 = margins[-5:]
    ebit_margin_median_5y = statistics.median(tail_5)

    industry_margin_us = ref.get_industry_average(industry_us, global_=False).pretax_operating_margin
    industry_margin_global = ref.get_industry_average(industry_global, global_=True).pretax_operating_margin
    industry_avg = (industry_margin_us + industry_margin_global) / 2

    w = BASE_BLEND_WEIGHTS
    best_historical = max(ebit_margin_actual, ebit_margin_median_5y)
    base_blend = best_historical * (1 - w.industry_margin_weight) + industry_avg * w.industry_margin_weight

    candidates = [ebit_margin_actual, ebit_margin_median_5y, industry_margin_us, industry_margin_global]
    if scenario == "Conservador":
        target_ebit_margin = min(candidates)
    elif scenario == "Optimista":
        target_ebit_margin = max(candidates)
    else:
        target_ebit_margin = base_blend

    return MarginEngineResult(
        ebit_margin_actual=ebit_margin_actual, ebit_margin_median_5y=ebit_margin_median_5y,
        industry_margin_us=industry_margin_us, industry_margin_global=industry_margin_global,
        target_ebit_margin=target_ebit_margin,
    )


@dataclass(frozen=True)
class SalesToCapital:
    """Sales-to-Capital por escenario. El Excel usa cuartiles de una
    distribucion de industria que no esta en nuestros CSV de referencia
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
    growth = run_growth_engine(series, scenario, industry_us=industry_us, industry_global=industry_global)
    margin = run_margin_engine(series, scenario, industry_us=industry_us, industry_global=industry_global)
    stc = sales_to_capital.for_scenario(scenario)

    return AssumptionsEngineResult(
        scenario=scenario, weights=weights, growth=growth, margin=margin,
        sales_to_capital_1_5=stc, sales_to_capital_6_10=stc,
    )


def growth_and_margin_path(result: AssumptionsEngineResult) -> GrowthAndMarginPath:
    """Arma el input que espera `dcf.run_dcf` (Año1 = growth_year1, Años2-5
    tambien = growth_year1 -- 'Motor de Supuestos v2' no distingue Año1 de 2-5
    como si hace 'Valuation output' original, converge directo desde Año1
    hacia el crecimiento estable).

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
    """Crecimiento estable = riskfree rate (igual que el motor original); WACC
    estable = WACC actual por defecto (asi lo deja 'Input sheet'!B47 salvo
    override) -- a diferencia del motor original, que por defecto usa
    riskfree + prima madura. Es una diferencia real y documentada entre las
    dos hojas del Excel, no un error de puerto."""
    return TerminalAssumptions(riskfree_rate=riskfree_rate, terminal_wacc_override=wacc_current)
