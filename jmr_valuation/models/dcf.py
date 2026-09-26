"""Motor de valoracion por flujo de caja descontado (DCF).

Replica la hoja 'Valuation output' (el motor de valoracion "Ginzu" de Damodaran):
10 anios explicitos + valor terminal, con convergencia de crecimiento, margen,
costo de capital y ROIC hacia supuestos de estado estable.

Cada uno de los tres escenarios del Excel (Base / Conservador / Optimista) usa
exactamente esta misma mecanica -- solo cambian los supuestos de crecimiento y
margen que se le pasan. Por eso aca hay una sola funcion (`run_dcf`) en vez de
tres copias.

Lo que NO esta portado todavia (fuera del alcance de esta primera etapa):
  - Probabilidad de fracaso / valor de liquidacion (Input sheet filas 51-55).
  - Ajuste por NOL mas alla del escudo fiscal basico en el flujo (fila 12/63/114).
  - Efectivo atrapado en el extranjero (filas 70-73).
  - Valor de opciones para empleados (ver models/options.py, separado).
Estos se restan/suman en 'Valuation output' filas 24-33 y quedan como
siguiente paso; `run_dcf` devuelve el valor de los activos operativos y deja
el puente a valor de equity como responsabilidad del llamador (ver ejemplo en
tests/test_dcf.py) para que sea explicito que` fracaso/NOL/opciones no estan
incluidos todavia.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from jmr_valuation.io import reference_data as ref

N_EXPLICIT_YEARS = 10


@dataclass(frozen=True)
class GrowthAndMarginPath:
    """Supuestos de crecimiento/margen de un escenario (Base/Conservador/Optimista)."""

    year1_growth: float          # B4/B55/B106
    years_2_to_5_growth: float   # D4/D55/D106 (constante desde el anio 2 al 5)
    target_ebit_margin: float    # C46/C45/C47: margen al que converge en year_of_convergence
    year_of_margin_convergence: int = 5  # 'Input sheet'!B31


@dataclass(frozen=True)
class TerminalAssumptions:
    """Resuelve M4 (crecimiento terminal), M14 (WACC terminal) y M42 (ROIC terminal).

    Por defecto replica el comportamiento de 'Input sheet' cuando ninguna de las
    3 casillas "Do you want to override" esta en 'Yes' (el caso mas comun):
      - crecimiento terminal = riskfree_rate
      - WACC terminal = riskfree_rate + prima de riesgo de mercado madura
      - ROIC terminal = costo de capital del ultimo anio explicito (no gana renta economica)
    Pasar cualquiera de los *_override para replicar las hojas B46/B65/B68/B49 en 'Yes'.
    """

    riskfree_rate: float
    terminal_growth_override: float | None = None       # 'Input sheet'!B69 si B68='Yes'
    riskfree_rate_after_year10_override: float | None = None  # B66 si B65='Yes'
    terminal_wacc_override: float | None = None          # B47 si B46='Yes'
    terminal_roic_override: float | None = None          # B50 si B49='Yes'

    def terminal_growth(self) -> float:
        if self.terminal_growth_override is not None:
            return self.terminal_growth_override
        if self.riskfree_rate_after_year10_override is not None:
            return self.riskfree_rate_after_year10_override
        return self.riskfree_rate

    def terminal_wacc(self) -> float:
        if self.terminal_wacc_override is not None:
            return self.terminal_wacc_override
        rf_after_10 = self.riskfree_rate_after_year10_override
        if rf_after_10 is not None:
            return rf_after_10 + ref.mature_market_erp()
        return self.riskfree_rate + ref.mature_market_erp()

    def terminal_roic(self, last_explicit_year_wacc: float) -> float:
        if self.terminal_roic_override is not None:
            return self.terminal_roic_override
        return last_explicit_year_wacc


@dataclass(frozen=True)
class YearProjection:
    year: int
    revenue_growth: float
    revenue: float
    ebit_margin: float
    ebit: float
    tax_rate: float
    ebit_after_tax: float
    reinvestment: float
    fcff: float
    cost_of_capital: float
    cumulative_discount_factor: float
    pv_fcff: float
    sales_to_capital: float
    invested_capital: float
    roic: float


@dataclass(frozen=True)
class DcfResult:
    years: list[YearProjection]
    terminal_year: YearProjection
    terminal_value: float
    pv_terminal_value: float
    pv_explicit_years: float
    value_of_operating_assets: float


def _converge_linear(start: float, end: float, n_steps: int, step: int) -> float:
    """Replica el patron '=G4-((G4-$M$4)/5)*k' usado para converger margen/crecimiento/WACC."""
    return start - ((start - end) / n_steps) * step


def run_dcf(
    base_revenue: float,
    base_ebit: float,  # ya incluye ajustes de leasing/I+D (ver models/converters.py)
    growth_path: GrowthAndMarginPath,
    initial_ebit_margin: float,   # C6/C57/C108: margen del ultimo anio reportado
    initial_cost_of_capital: float,
    terminal: TerminalAssumptions,
    initial_tax_rate: float,
    marginal_tax_rate: float,
    tax_rate_converges_to_marginal: bool,
    sales_to_capital_years_1_5: float,
    sales_to_capital_years_6_10: float,
    invested_capital_base: float,  # ya incluye ajustes de leasing/I+D
    nol_carryforward: float = 0.0,
    growth_convergence_years: int | None = None,
) -> DcfResult:
    """Proyecta 10 anios + terminal y descuenta a valor presente (filas 3-42 de 'Valuation output').

    growth_convergence_years=None (default): comportamiento original de
    'Valuation output' -- Año1 explicito, Años2-5 planos, Años6-10 convergen
    linealmente a crecimiento estable en exactamente 5 años. No lo usa
    valuation.py (motor original), no cambia nada para ese caller.

    growth_convergence_years=N: crecimiento converge linealmente desde
    year1_growth hacia crecimiento estable a lo largo de N años (empieza a
    converger desde el Año1, no recien en el Año6), igual que ya hace el
    margen EBIT con year_of_margin_convergence -- una curva continua en vez
    de "plano 4 años + caida brusca", mas parecido a como una empresa real
    desacelera. Es la formula de 'Motor de Supuestos v2' (fila 67 del Excel),
    usada por assumptions_engine.py con el N propio de cada escenario
    (Conservador=5, Base=7, Optimista=10 años -- mas años de crecimiento
    elevado en el caso optimista, consistente con la historia que cuenta ese
    escenario, no solo con un numero mas alto)."""

    terminal_growth = terminal.terminal_growth()
    terminal_wacc = terminal.terminal_wacc()
    if terminal_wacc <= terminal_growth:
        raise ValueError(
            f"WACC terminal ({terminal_wacc:.2%}) debe superar el crecimiento estable "
            f"({terminal_growth:.2%}); revisa moneda, tasa libre de riesgo y supuestos."
        )
    if sales_to_capital_years_1_5 <= 0 or sales_to_capital_years_6_10 <= 0:
        raise ValueError("Sales-to-capital debe ser positivo en ambos periodos")

    years: list[YearProjection] = []

    revenue_prev = base_revenue
    ebit_margin_prev = initial_ebit_margin
    invested_capital_prev = invested_capital_base
    nol_prev = nol_carryforward
    ebit_after_tax_prev = None  # para el escudo de NOL (fila 9: "IF(C7<B12,...)")
    cost_of_capital_prev = initial_cost_of_capital
    cum_discount_prev = 1.0

    final_tax_rate = marginal_tax_rate if tax_rate_converges_to_marginal else initial_tax_rate

    for year in range(1, N_EXPLICIT_YEARS + 1):
        # --- crecimiento de ingresos (fila 4) ---
        if growth_convergence_years is not None:
            if year <= growth_convergence_years:
                growth = _converge_linear(
                    growth_path.year1_growth, terminal_growth,
                    max(growth_convergence_years - 1, 1), year - 1,
                )
            else:
                growth = terminal_growth
        elif year == 1:
            growth = growth_path.year1_growth
        elif 2 <= year <= 5:
            growth = growth_path.years_2_to_5_growth
        else:
            growth = _converge_linear(growth_path.years_2_to_5_growth, terminal_growth, 5, year - 5)
        revenue = revenue_prev * (1 + growth)

        # --- margen EBIT (fila 6) ---
        conv_year = growth_path.year_of_margin_convergence
        if year > conv_year:
            ebit_margin = growth_path.target_ebit_margin
        else:
            ebit_margin = growth_path.target_ebit_margin - (
                (growth_path.target_ebit_margin - initial_ebit_margin) / conv_year
            ) * (conv_year - year)
        ebit = ebit_margin * revenue

        # --- tasa impositiva (fila 8): converge linealmente desde el anio 6 ---
        if year <= 5:
            tax_rate = initial_tax_rate
        else:
            tax_rate = initial_tax_rate + (final_tax_rate - initial_tax_rate) / 5 * (year - 5)

        # --- EBIT(1-t) con escudo de NOL (fila 9) ---
        if ebit > 0:
            if ebit < nol_prev:
                ebit_after_tax = ebit  # NOL absorbe todo, no paga impuestos
            else:
                ebit_after_tax = ebit - (ebit - nol_prev) * tax_rate
        else:
            ebit_after_tax = ebit

        # NOL remanente (fila 12), usado por el anio siguiente
        if ebit < 0:
            nol_next = nol_prev - ebit
        elif nol_prev > ebit:
            nol_next = nol_prev - ebit
        else:
            nol_next = 0.0

        # --- costo de capital (fila 14): converge linealmente desde el anio 6 ---
        if year <= 5:
            cost_of_capital = initial_cost_of_capital
        else:
            cost_of_capital = cost_of_capital_prev - (initial_cost_of_capital - terminal_wacc) / 5

        # --- sales-to-capital ratio (fila 40) ---
        sales_to_capital = sales_to_capital_years_1_5 if year <= 5 else sales_to_capital_years_6_10

        # --- reinversion (fila 10): (ingresos del anio siguiente - actuales) / sales-to-capital ---
        # Nota: usa el ingreso del anio siguiente, que todavia no calculamos aca;
        # se resuelve con una segunda pasada mas abajo (ver bucle principal).
        years.append(YearProjection(
            year=year, revenue_growth=growth, revenue=revenue, ebit_margin=ebit_margin,
            ebit=ebit, tax_rate=tax_rate, ebit_after_tax=ebit_after_tax,
            reinvestment=0.0, fcff=0.0, cost_of_capital=cost_of_capital,
            cumulative_discount_factor=0.0, pv_fcff=0.0,
            sales_to_capital=sales_to_capital, invested_capital=0.0, roic=0.0,
        ))

        revenue_prev = revenue
        ebit_margin_prev = ebit_margin
        nol_prev = nol_next
        cost_of_capital_prev = cost_of_capital

    # --- anio terminal ---
    terminal_revenue = years[-1].revenue * (1 + terminal_growth)
    terminal_ebit_margin = years[-1].ebit_margin
    terminal_ebit = terminal_ebit_margin * terminal_revenue
    terminal_tax_rate = final_tax_rate
    terminal_ebit_after_tax = terminal_ebit * (1 - terminal_tax_rate)

    # segunda pasada: reinversion (necesita el ingreso del anio siguiente) e invested capital
    invested_capital_prev = invested_capital_base
    revenues_extended = [base_revenue] + [y.revenue for y in years] + [terminal_revenue]
    final_years = []
    for i, y in enumerate(years):
        next_revenue = revenues_extended[i + 2]
        this_revenue = revenues_extended[i + 1]
        reinvestment = (next_revenue - this_revenue) / y.sales_to_capital
        fcff = y.ebit_after_tax - reinvestment
        invested_capital = invested_capital_prev + reinvestment
        roic = y.ebit_after_tax / invested_capital_prev if invested_capital_prev else 0.0

        cum_discount = cum_discount_prev * (1 / (1 + y.cost_of_capital))
        pv_fcff = fcff * cum_discount

        final_years.append(YearProjection(
            year=y.year, revenue_growth=y.revenue_growth, revenue=y.revenue,
            ebit_margin=y.ebit_margin, ebit=y.ebit, tax_rate=y.tax_rate,
            ebit_after_tax=y.ebit_after_tax, reinvestment=reinvestment, fcff=fcff,
            cost_of_capital=y.cost_of_capital, cumulative_discount_factor=cum_discount,
            pv_fcff=pv_fcff, sales_to_capital=y.sales_to_capital,
            invested_capital=invested_capital, roic=roic,
        ))
        invested_capital_prev = invested_capital
        cum_discount_prev = cum_discount

    terminal_roic = terminal.terminal_roic(final_years[-1].cost_of_capital)
    if terminal_roic <= 0:
        raise ValueError("ROIC terminal debe ser positivo para justificar el crecimiento estable")
    terminal_reinvestment = terminal_ebit_after_tax * (terminal_growth / terminal_roic)
    terminal_fcff = terminal_ebit_after_tax - terminal_reinvestment

    terminal_year = YearProjection(
        year=N_EXPLICIT_YEARS + 1, revenue_growth=terminal_growth, revenue=terminal_revenue,
        ebit_margin=terminal_ebit_margin, ebit=terminal_ebit, tax_rate=terminal_tax_rate,
        ebit_after_tax=terminal_ebit_after_tax, reinvestment=terminal_reinvestment,
        fcff=terminal_fcff, cost_of_capital=terminal_wacc,
        cumulative_discount_factor=final_years[-1].cumulative_discount_factor,
        pv_fcff=0.0, sales_to_capital=sales_to_capital_years_6_10,
        invested_capital=final_years[-1].invested_capital, roic=terminal_roic,
    )

    terminal_value = terminal_fcff / (terminal_wacc - terminal_growth)
    pv_terminal_value = terminal_value * final_years[-1].cumulative_discount_factor
    pv_explicit_years = sum(y.pv_fcff for y in final_years)
    value_of_operating_assets = pv_terminal_value + pv_explicit_years

    return DcfResult(
        years=final_years, terminal_year=terminal_year, terminal_value=terminal_value,
        pv_terminal_value=pv_terminal_value, pv_explicit_years=pv_explicit_years,
        value_of_operating_assets=value_of_operating_assets,
    )


@dataclass(frozen=True)
class EquityBridgeResult:
    value_of_operating_assets: float
    less_debt: float
    less_minority_interests: float
    plus_cash: float
    plus_non_operating_assets: float
    value_of_equity: float
    less_value_of_options: float
    value_of_equity_in_common_stock: float
    value_per_share: float
    price_as_pct_of_value: float | None


def equity_value_bridge(
    dcf_result: DcfResult,
    book_value_debt: float,
    minority_interests: float,
    cash: float,
    non_operating_assets: float,
    shares_outstanding: float,
    value_of_options: float = 0.0,
    current_price: float | None = None,
) -> EquityBridgeResult:
    """Filas 26-37 de 'Valuation output': del valor operativo al valor por accion.

    No incluye todavia el ajuste por probabilidad de fracaso (filas 24-26) ni por
    efectivo atrapado en el extranjero (filas 70-73) -- ver docstring del modulo.
    """
    value_of_equity = (
        dcf_result.value_of_operating_assets - book_value_debt - minority_interests
        + cash + non_operating_assets
    )
    value_of_equity_in_common_stock = value_of_equity - value_of_options
    value_per_share = value_of_equity_in_common_stock / shares_outstanding

    return EquityBridgeResult(
        value_of_operating_assets=dcf_result.value_of_operating_assets,
        less_debt=book_value_debt,
        less_minority_interests=minority_interests,
        plus_cash=cash,
        plus_non_operating_assets=non_operating_assets,
        value_of_equity=value_of_equity,
        less_value_of_options=value_of_options,
        value_of_equity_in_common_stock=value_of_equity_in_common_stock,
        value_per_share=value_per_share,
        price_as_pct_of_value=(current_price / value_per_share) if current_price else None,
    )
