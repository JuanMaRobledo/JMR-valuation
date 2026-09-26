"""Valoracion relativa por multiplos (EV/FCFF, P/OCF, P/E, P/FCFE, EV/EBITDA).

Reemplaza las 5 hojas EVFCFF/POCF/PE/PFCFE/EVEBITDA del Excel -- que eran
estructuralmente identicas (79% de las celdas byte-a-byte iguales; ver el
reporte de auditoria) y solo diferian en que metrica alimentaban -- por una
sola funcion parametrizada por el nombre de la metrica.

Requiere como insumo la metrica ya proyectada (FCFF, OCF, utilidad neta, FCFE o
EBITDA) para los proximos 3 anios fiscales bajo cada escenario -- eso lo arma
`models.financials_multiples`.

El "multiplo ancla" (de que parte la valoracion) se resuelve igual que en el
Excel (p.ej. 'EVFCFF'!F19 = IFERROR(IF(J19<>"",J19,MEDIAN(...)),"")): mediana
de los ultimos 3 anios por defecto, o un valor manual si se lo da (ver
`resolve_anchor_multiple`).
"""
from __future__ import annotations

import statistics
from dataclasses import dataclass

# Ajustes de escenario sobre el multiplo mediano historico (F8/F19/F30 del Excel:
# Conservador = mediana*0.9, Base = mediana, Optimista = mediana*1.1)
SCENARIO_MULTIPLE_ADJUSTMENT = {"Conservador": 0.9, "Base": 1.0, "Optimista": 1.1}

# Deltas de la matriz de sensibilidad (filas/columnas A46:F51 del Excel)
SENSITIVITY_DELTAS = (0.9, 0.95, 1.0, 1.05, 1.1)


def resolve_anchor_multiple(historical_last_3_years: list[float], override_value: float | None = None) -> float:
    """Mediana de los ultimos 3 anios, salvo que el override este activo (override_value no sea None), que la pisa.

    Replica 'EVFCFF'!F19 = IFERROR(IF(J19<>"",J19,MEDIAN('Trailing Valuation'!G24:K24)),""),
    con la casilla de override explicita en vez de "0 = no hay override" (asi un
    override deliberado de 0 tampoco se confunde con "no cargado").
    """
    if override_value is not None:
        return override_value
    if len(historical_last_3_years) != 3:
        raise ValueError("Se esperan exactamente 3 anios de multiplo historico")
    return statistics.median(historical_last_3_years)


@dataclass(frozen=True)
class ScenarioMultipleInputs:
    scenario: str                    # "Conservador" | "Base" | "Optimista"
    historical_median_multiple: float  # mediana de los ultimos 5 anios (fila 19/8, columna F)
    metric_fy1: float                # metrica proyectada (FCFF/OCF/NI/FCFE/EBITDA) FY+1
    metric_fy2: float
    metric_fy3: float
    shares_or_ev_divisor: float      # acciones en circulacion (P/E, P/OCF, P/FCFE) o 1.0 si la metrica ya esta en EV total
    cumulative_dividends_fy1: float = 0.0
    cumulative_dividends_fy2: float = 0.0
    cumulative_dividends_fy3: float = 0.0
    manual_multiple_override: float | None = None  # celda J del Excel, si el usuario fija el multiplo a mano
    projected_shares: tuple[float, float, float] | None = None
    # Para EV/FCFF y EV/EBITDA: deuda + minoritarios + opciones - caja - inversiones.
    # El múltiplo produce valor de EMPRESA; hay que convertirlo a equity.
    ev_to_equity_adjustment: float = 0.0


@dataclass(frozen=True)
class YearTarget:
    year_label: str
    multiple: float
    metric: float
    implied_target_price: float
    cumulative_dividends: float
    total_target_price: float
    total_return: float
    annualized_return: float


@dataclass(frozen=True)
class RelativeValuationResult:
    metric_name: str
    scenario: str
    multiple_fy1: float
    years: list[YearTarget]


def project_target_prices(
    metric_name: str,
    current_price: float,
    inputs: ScenarioMultipleInputs,
) -> RelativeValuationResult:
    """Replica filas 5-14 (o 16-25, 27-36) de EVFCFF/POCF/PE/PFCFE/EVEBITDA."""
    if inputs.manual_multiple_override is not None:
        multiple_fy1 = inputs.manual_multiple_override
    else:
        adjustment = SCENARIO_MULTIPLE_ADJUSTMENT[inputs.scenario]
        multiple_fy1 = inputs.historical_median_multiple * adjustment

    metrics = [inputs.metric_fy1, inputs.metric_fy2, inputs.metric_fy3]
    dividends = [inputs.cumulative_dividends_fy1, inputs.cumulative_dividends_fy2, inputs.cumulative_dividends_fy3]
    labels = ["FY+1", "FY+2", "FY+3"]

    if current_price <= 0 or inputs.shares_or_ev_divisor <= 0:
        raise ValueError("Precio y acciones deben ser positivos")
    if inputs.projected_shares is not None and any(s <= 0 for s in inputs.projected_shares):
        raise ValueError("Las acciones proyectadas deben ser positivas")

    years = []
    for n, (label, metric, div) in enumerate(zip(labels, metrics, dividends), start=1):
        shares = inputs.projected_shares[n - 1] if inputs.projected_shares else inputs.shares_or_ev_divisor
        enterprise_value = multiple_fy1 * metric
        equity_value = (enterprise_value - inputs.ev_to_equity_adjustment
                        if metric_name.startswith("EV/") else enterprise_value)
        implied_price = equity_value / shares
        total_target = implied_price + div
        total_return = (total_target - current_price) / current_price
        annualized_return = (total_target / current_price) ** (1 / n) - 1
        years.append(YearTarget(
            year_label=label, multiple=multiple_fy1, metric=metric,
            implied_target_price=implied_price, cumulative_dividends=div,
            total_target_price=total_target, total_return=total_return,
            annualized_return=annualized_return,
        ))

    return RelativeValuationResult(
        metric_name=metric_name, scenario=inputs.scenario,
        multiple_fy1=multiple_fy1, years=years,
    )


def sensitivity_matrix(
    base_multiple_fy3: float,
    base_metric_fy3: float,
    shares_or_ev_divisor: float,
    ev_to_equity_adjustment: float = 0.0,
) -> list[list[float]]:
    """Replica la matriz A46:F51: precio objetivo FY+3 variando multiplo x metrica +/-10%."""
    multiples = [base_multiple_fy3 * d for d in SENSITIVITY_DELTAS]
    metrics = [base_metric_fy3 * d for d in SENSITIVITY_DELTAS]
    return [
        [(m * metric - ev_to_equity_adjustment) / shares_or_ev_divisor for metric in metrics]
        for m in multiples
    ]
