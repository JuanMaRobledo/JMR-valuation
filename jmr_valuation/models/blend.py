"""Combina el DCF y los 5 multiplos en un precio objetivo ponderado por tipo de empresa.

Replica la hoja 'Resumen de Valoracion' (filas 5-19): cada metodo pesa distinto
segun el tipo de negocio -- una financiera no se valora igual que un REIT o una
empresa de software -- y el resultado final tambien fija bandas de precio de
compra (Value / Deep Value / Valoracion historica) y un precio con margen de
seguridad.
"""
from __future__ import annotations

from dataclasses import dataclass

METHODS = ("DCF Damodaran", "EV/EBITDA", "EV/FCFF", "P/E", "P/FCFE", "P/OCF")

COMPANY_TYPES = ("Crecimiento", "Madura", "Generico", "Defensiva", "Ciclica/Commodity",
                  "Intensiva en Capital", "Financiera", "Infraestructura",
                  "REIT/Inmobiliaria", "Software")

# Filas I6:S11 de 'Resumen de Valoracion' -- pesos de cada metodo por tipo de
# empresa. Cada columna (tipo de empresa) suma 1.0.
_WEIGHTS: dict[str, dict[str, float]] = {
    "DCF Damodaran": {"Crecimiento": 0.60, "Madura": 0.40, "Generico": 0.50, "Defensiva": 0.30,
                        "Ciclica/Commodity": 0.45, "Intensiva en Capital": 0.20, "Financiera": 0.35,
                        "Infraestructura": 0.40, "REIT/Inmobiliaria": 0.25, "Software": 0.55},
    "EV/EBITDA":     {"Crecimiento": 0.10, "Madura": 0.20, "Generico": 0.10, "Defensiva": 0.20,
                        "Ciclica/Commodity": 0.20, "Intensiva en Capital": 0.40, "Financiera": 0.00,
                        "Infraestructura": 0.15, "REIT/Inmobiliaria": 0.30, "Software": 0.25},
    "EV/FCFF":       {"Crecimiento": 0.15, "Madura": 0.10, "Generico": 0.10, "Defensiva": 0.10,
                        "Ciclica/Commodity": 0.15, "Intensiva en Capital": 0.15, "Financiera": 0.00,
                        "Infraestructura": 0.25, "REIT/Inmobiliaria": 0.10, "Software": 0.05},
    "P/E":           {"Crecimiento": 0.05, "Madura": 0.20, "Generico": 0.10, "Defensiva": 0.25,
                        "Ciclica/Commodity": 0.05, "Intensiva en Capital": 0.05, "Financiera": 0.35,
                        "Infraestructura": 0.10, "REIT/Inmobiliaria": 0.05, "Software": 0.05},
    "P/FCFE":        {"Crecimiento": 0.10, "Madura": 0.05, "Generico": 0.10, "Defensiva": 0.10,
                        "Ciclica/Commodity": 0.10, "Intensiva en Capital": 0.05, "Financiera": 0.20,
                        "Infraestructura": 0.05, "REIT/Inmobiliaria": 0.20, "Software": 0.05},
    "P/OCF":         {"Crecimiento": 0.00, "Madura": 0.05, "Generico": 0.10, "Defensiva": 0.05,
                        "Ciclica/Commodity": 0.05, "Intensiva en Capital": 0.15, "Financiera": 0.10,
                        "Infraestructura": 0.05, "REIT/Inmobiliaria": 0.10, "Software": 0.05},
}


def weights_for_type(company_type: str) -> dict[str, float]:
    if company_type not in COMPANY_TYPES:
        raise ValueError(f"Tipo de empresa no reconocido: {company_type!r}. Opciones: {COMPANY_TYPES}")
    return {method: _WEIGHTS[method][company_type] for method in METHODS}


def renormalize_weights(
    weights: dict[str, float], included_methods: dict[str, bool] | None = None,
) -> dict[str, float]:
    """Pone en 0 el peso de los metodos excluidos y reescala el resto para que
    sigan sumando 1.0 -- ej. si excluis 'P/OCF', su peso se reparte proporcionalmente
    entre los 5 metodos restantes, no queda simplemente "perdido"."""
    if included_methods is None:
        return dict(weights)

    active = {m: w for m, w in weights.items() if included_methods.get(m, True)}
    total = sum(active.values())
    if total <= 0:
        raise ValueError(
            "No puede quedar ningun metodo activo en la ponderacion "
            "(todos estan excluidos, o los que quedan tienen peso 0 para este tipo de empresa)."
        )
    return {m: (active[m] / total if m in active else 0.0) for m in weights}


@dataclass(frozen=True)
class MethodValues:
    """Precio/valor por accion que da cada metodo, para un escenario (Conservador/Base/Optimista)."""
    dcf_damodaran: float
    ev_ebitda: float
    ev_fcff: float
    pe: float
    p_fcfe: float
    p_ocf: float

    def as_dict(self) -> dict[str, float]:
        return {
            "DCF Damodaran": self.dcf_damodaran, "EV/EBITDA": self.ev_ebitda,
            "EV/FCFF": self.ev_fcff, "P/E": self.pe, "P/FCFE": self.p_fcfe, "P/OCF": self.p_ocf,
        }


@dataclass(frozen=True)
class BuyPriceTiers:
    value_max: float
    value_min: float
    deep_value_max: float
    deep_value_min: float
    historical_valuation_max: float
    historical_valuation_min: float


@dataclass(frozen=True)
class BlendResult:
    company_type: str
    weights: dict[str, float]
    weighted_price_by_scenario: dict[str, float]   # Conservador / Base / Optimista
    cagr_3y_by_scenario: dict[str, float]
    mos_price: float                                # precio ponderado Base con margen de seguridad
    buy_price_tiers: BuyPriceTiers                   # basadas en el ponderado Base (D12 en el Excel)


def weighted_target_price(
    company_type: str, values: MethodValues, included_methods: dict[str, bool] | None = None,
) -> float:
    """B12/C12/D12/E12: SUMPRODUCT(pesos, valor por metodo) para un escenario."""
    weights = renormalize_weights(weights_for_type(company_type), included_methods)
    method_values = values.as_dict()
    return sum(weights[method] * method_values[method] for method in METHODS)


def cagr_3y(target_price: float, current_price: float) -> float:
    """Fila 13: CAGR implicito a 3 anios entre el precio actual y el objetivo ponderado."""
    if current_price <= 0:
        return 0.0
    return (target_price / current_price) ** (1 / 3) - 1


def buy_price_tiers(weighted_base_price: float) -> BuyPriceTiers:
    """Filas 16-18: bandas de precio de compra como % del ponderado Base."""
    return BuyPriceTiers(
        value_max=weighted_base_price * 0.70, value_min=weighted_base_price * 0.65,
        deep_value_max=weighted_base_price * 0.60, deep_value_min=weighted_base_price * 0.55,
        historical_valuation_max=weighted_base_price * 0.50, historical_valuation_min=weighted_base_price * 0.45,
    )


def margin_of_safety_price(weighted_base_price: float, margin_of_safety: float = 0.35) -> float:
    """Fila 19: precio de entrada objetivo, aplicando el margen de seguridad (35% por defecto) al ponderado Base."""
    return weighted_base_price * (1 - margin_of_safety)


def run_blend(
    company_type: str,
    current_price: float,
    values_by_scenario: dict[str, MethodValues],   # {"Conservador": ..., "Base": ..., "Optimista": ...}
    margin_of_safety: float = 0.35,
    included_methods: dict[str, bool] | None = None,  # metodo -> True/False; None = todos incluidos
) -> BlendResult:
    weights = renormalize_weights(weights_for_type(company_type), included_methods)
    weighted_by_scenario = {
        scenario: weighted_target_price(company_type, values, included_methods)
        for scenario, values in values_by_scenario.items()
    }
    cagr_by_scenario = {
        scenario: cagr_3y(price, current_price) for scenario, price in weighted_by_scenario.items()
    }
    base_price = weighted_by_scenario["Base"]

    return BlendResult(
        company_type=company_type, weights=weights, weighted_price_by_scenario=weighted_by_scenario,
        cagr_3y_by_scenario=cagr_by_scenario, mos_price=margin_of_safety_price(base_price, margin_of_safety),
        buy_price_tiers=buy_price_tiers(base_price),
    )
