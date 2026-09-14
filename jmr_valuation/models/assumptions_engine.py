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
reales (ver mas abajo) como Conservador/Optimista, y Base sigue siendo la
mezcla ponderada de siempre. Una mezcla ponderada (pesos no negativos que
suman 1) de un conjunto de numeros SIEMPRE cae entre su minimo y su maximo --
por lo tanto Conservador <= Base <= Optimista queda garantizado
matematicamente, para cualquier empresa, sin calibrar nada caso por caso.
Mismo criterio para el margen EBIT objetivo (min/blend/max de margen actual,
mediana 5y, industria US, industria Global) -- y coincide con el patron que
ya usa `valuation._target_ebit_margin` (el motor original del repo) para el
mismo problema.

Criterios de crecimiento (Damodaran, "Estimating growth"): el propio
Damodaran advierte que el crecimiento historico es un mal predictor
justamente para empresas jovenes/de alto crecimiento -- la volatilidad de su
historia (ADBE desacelerando de 17% a 6% es un caso de manual) lo vuelve poco
confiable. Sin acceso a estimados de analistas (fuente que no tenemos), su
alternativa es el CRECIMIENTO FUNDAMENTAL: g = Reinvestment Rate x ROIC (la
misma formula que ya usamos para el crecimiento terminal, aca aplicada
tambien al crecimiento del negocio real). Por eso el conjunto de candidatos
para growth_year1 combina TRES fuentes, cada una un metodo valido segun
Damodaran, no una sola:
  1. Historico combinado (LTM/CAGR 3y/5y/largo plazo, pesos de siempre).
  2. Promedio de industria (US + Global).
  3. Crecimiento fundamental = Reinvestment Rate LTM x ROIC LTM, con
     Reinvestment Rate = Net CapEx (CapEx - D&A) / EBIT(1-t) y
     ROIC = EBIT(1-t) / Capital Invertido (equity + deuda - caja, book value).
     Sin datos confiables de capital de trabajo (mismo motivo que
     sec_edgar_loader deja hist_nwc_pct_of_revenue_growth en 0), el
     Reinvestment Rate excluye ΔNWC -- no se inventa. Para empresas que
     reportan I+D, este se capitaliza primero (Damodaran: I+D es una
     inversion, no un gasto del periodo) reusando `converters.capitalize_rd`
     -- sin este ajuste, una empresa de software con poco activo fijo (Net
     CapEx ~0 o negativo) puede dar un crecimiento fundamental negativo que
     no refleja que en realidad reinvierte fuerte, solo que lo hace via I+D
     y no via CapEx (ver `FundamentalGrowthInputs`).
Base mezcla las 3 fuentes; Conservador/Optimista toman el minimo/maximo del
conjunto completo (los 4 numeros historicos + industria + fundamental, ver
`run_growth_engine`).
"""
from __future__ import annotations

import statistics
from dataclasses import dataclass

from jmr_valuation.io import reference_data as ref
from jmr_valuation.io.sec_edgar_loader import AnnualSeries
from jmr_valuation.models.converters import capitalize_rd
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
    fundamental_growth_weight: float
    industry_margin_weight: float


# Pesos de la mezcla de Base. Calibracion del modelo, igual para cualquier
# empresa -- no depende del ticker. Ya no se usan para Conservador/Optimista
# (ver docstring del modulo). industry_growth_weight + fundamental_growth_weight
# reparten el 60% no-historico casi parejo (30/30): ni el promedio de
# industria ni el crecimiento fundamental deberian dominar solos sobre un
# historico real de 10 años.
BASE_BLEND_WEIGHTS = _BaseBlendWeights(
    weight_ltm=0.25, weight_cagr3=0.25, weight_cagr5=0.25, weight_cagr_long=0.25,
    industry_growth_weight=0.30, fundamental_growth_weight=0.30, industry_margin_weight=0.40,
)


def _cagr(first: float, last: float, years: int) -> float:
    if years < 1 or first <= 0:
        return 0.0
    return (last / first) ** (1 / years) - 1


@dataclass(frozen=True)
class FundamentalGrowthInputs:
    """Datos ya calculados por `sec_edgar_loader.load_company_inputs_from_sec_edgar`
    (no se vuelven a pedir a EDGAR aca) -- lo minimo necesario para
    g = Reinvestment Rate x ROIC sin inventar capital de trabajo.

    rd_*: si `capitalize_rd` es True, el I+D se capitaliza (Damodaran) antes de
    calcular EBIT(1-t)/ROIC/Reinvestment -- para una empresa de software, el
    Net CapEx (CapEx - D&A) tipicamente da negativo o cercano a 0 (poco activo
    fijo) y subestima brutalmente cuanto reinvierte realmente la empresa, que
    es sobre todo via I+D (gasto contable, no capex). Sin este ajuste, el
    crecimiento fundamental de una empresa de software puede salir negativo
    aunque la empresa este creciendo -- un artefacto contable, no la realidad
    del negocio (ver docstring del modulo)."""

    ebit_ltm: float
    effective_tax_rate: float
    revenue_ltm: float
    book_value_equity_ltm: float
    book_value_debt_ltm: float
    cash_ltm: float
    hist_capex_pct_of_revenue: float
    hist_da_pct_of_revenue: float
    capitalize_rd: bool = False
    rd_amortization_years: int = 3
    rd_expense_current_year: float = 0.0
    rd_expense_past_years: tuple[float, ...] = ()   # anio -1, -2, -3... (el mas reciente primero)


@dataclass(frozen=True)
class FundamentalGrowthResult:
    reinvestment_rate: float
    roic: float
    fundamental_growth: float
    rd_adjusted: bool   # True si se capitalizo I+D para este calculo


def fundamental_growth_rate(inputs: FundamentalGrowthInputs) -> FundamentalGrowthResult | None:
    """g = Reinvestment Rate x ROIC (formula de Damodaran para crecimiento
    sostenible). None si EBIT(1-t) o el capital invertido no son positivos --
    la formula no tiene sentido economico en ese caso, no se fuerza un numero."""
    ebit = inputs.ebit_ltm
    invested_capital = inputs.book_value_equity_ltm + inputs.book_value_debt_ltm - inputs.cash_ltm
    net_capex = (inputs.hist_capex_pct_of_revenue - inputs.hist_da_pct_of_revenue) * inputs.revenue_ltm

    rd_adjusted = inputs.capitalize_rd and inputs.rd_expense_current_year > 0
    if rd_adjusted:
        rd = capitalize_rd(
            amortization_years=inputs.rd_amortization_years,
            current_year_rd_expense=inputs.rd_expense_current_year,
            past_years_rd_expense=list(inputs.rd_expense_past_years),
            tax_rate=inputs.effective_tax_rate,
        )
        ebit = ebit + rd.ebit_adjustment          # I+D como si fuera un activo que se amortiza, no gasto del año
        invested_capital = invested_capital + rd.research_asset_value
        net_capex = net_capex + rd.ebit_adjustment  # reinversion neta en el activo de I+D

    ebit_after_tax = ebit * (1 - inputs.effective_tax_rate)
    if ebit_after_tax <= 0 or invested_capital <= 0:
        return None

    roic = ebit_after_tax / invested_capital
    reinvestment_rate = net_capex / ebit_after_tax
    return FundamentalGrowthResult(
        reinvestment_rate=reinvestment_rate, roic=roic, fundamental_growth=reinvestment_rate * roic,
        rd_adjusted=rd_adjusted,
    )


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
    fundamental: FundamentalGrowthResult | None   # None si no se pudo calcular (ver fundamental_growth_rate)
    growth_year1: float           # resultado para el escenario pedido: min/blend/max


def run_growth_engine(
    series: AnnualSeries, scenario: str, *, industry_us: str, industry_global: str,
    fundamental_inputs: FundamentalGrowthInputs | None = None,
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
    industry_avg = (industry_growth_us + industry_growth_global) / 2

    fundamental = fundamental_growth_rate(fundamental_inputs) if fundamental_inputs is not None else None

    w = BASE_BLEND_WEIGHTS
    combined_historical = (
        ltm_growth * w.weight_ltm + cagr_3y * w.weight_cagr3
        + cagr_5y * w.weight_cagr5 + cagr_long * w.weight_cagr_long
    )
    candidates = [ltm_growth, cagr_3y, cagr_5y, cagr_long, industry_avg]
    if fundamental is not None:
        candidates.append(fundamental.fundamental_growth)
        base_blend = (
            combined_historical * (1 - w.industry_growth_weight - w.fundamental_growth_weight)
            + industry_avg * w.industry_growth_weight
            + fundamental.fundamental_growth * w.fundamental_growth_weight
        )
    else:
        # Sin fundamental (EBIT(1-t) o capital invertido no positivos): se
        # reparte su peso proporcionalmente entre historico e industria, no
        # se inventa un tercer numero.
        total = (1 - w.fundamental_growth_weight)
        hist_share = (1 - w.industry_growth_weight - w.fundamental_growth_weight) / total
        industry_share = w.industry_growth_weight / total
        base_blend = combined_historical * hist_share + industry_avg * industry_share

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
        fundamental=fundamental, growth_year1=growth_year1,
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
    fundamental_inputs: FundamentalGrowthInputs | None = None,
) -> AssumptionsEngineResult:
    if scenario not in SCENARIO_WEIGHTS:
        raise ValueError(f"Escenario desconocido: {scenario!r}. Opciones: {SCENARIOS}")
    weights = SCENARIO_WEIGHTS[scenario]
    growth = run_growth_engine(
        series, scenario, industry_us=industry_us, industry_global=industry_global,
        fundamental_inputs=fundamental_inputs,
    )
    margin = run_margin_engine(series, scenario, industry_us=industry_us, industry_global=industry_global)
    stc = sales_to_capital.for_scenario(scenario)

    return AssumptionsEngineResult(
        scenario=scenario, weights=weights, growth=growth, margin=margin,
        sales_to_capital_1_5=stc, sales_to_capital_6_10=stc,
    )


def growth_and_margin_path(result: AssumptionsEngineResult) -> GrowthAndMarginPath:
    """Arma el input que espera `dcf.run_dcf`. `years_2_to_5_growth` queda
    igual a `year1_growth` -- es el valor que usaria `run_dcf` con
    `growth_convergence_years=None` (motor original), pero esta funcion se usa
    siempre junto con `run_dcf(..., growth_convergence_years=result.weights.growth_convergence_years)`
    (ver `run_pipeline.py`), que ignora `years_2_to_5_growth` y en cambio
    converge linealmente desde `year1_growth` hacia el crecimiento estable a
    lo largo de esos N años -- la curva continua de 'Motor de Supuestos v2',
    con el N propio de cada escenario (Conservador converge rapido en 5 años,
    Optimista se toma 10 -- la historia que cuenta cada escenario, no un
    ajuste cosmetico)."""
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
