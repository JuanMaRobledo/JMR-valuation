"""Carga las tablas de referencia de Damodaran (ERP por pais, promedios por industria).

Los CSV viven en reference/. Las primas por país son la tabla publicada por
Damodaran en enero de 2026 y los promedios sectoriales se heredaron del Excel;
sus fechas y límites están documentados en reference/SOURCES.md. La prima
implícita de mercado tiene un corte posterior (septiembre de 2026).
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

REFERENCE_DIR = Path(__file__).resolve().parent.parent.parent / "reference"
COUNTRY_ERP_AS_OF = "2026-01"
COUNTRY_ALIASES = {
    "Turkey": "Turkey (updated February 2026)",
    "Yemen": "Yemen, Republic",
    "Trinidad & Tobago": "Trinidad and Tobago",
}


@dataclass(frozen=True)
class CountryRiskPremium:
    country: str
    rating: str
    default_spread: float
    total_erp: float  # ERP total publicada en enero de 2026, incluye prima de riesgo país


@dataclass(frozen=True)
class IndustryAverage:
    industry: str
    num_firms: float
    revenue_growth_5y: float
    pretax_operating_margin: float
    aftertax_roc: float
    effective_tax_rate: float
    unlevered_beta: float
    levered_beta: float
    cost_of_equity: float
    stdev_stock_price: float
    pretax_cost_of_debt: float
    market_debt_to_capital: float
    cost_of_capital: float
    sales_to_capital: float
    ev_to_sales: float
    ev_to_ebitda: float
    ev_to_ebit: float
    price_to_book: float
    trailing_pe: float
    noncash_wc_pct_revenue: float


def _to_float(v: str):
    if v in (None, ""):
        return None
    try:
        return float(v)
    except ValueError:
        return v


@lru_cache(maxsize=1)
def mature_market_erp() -> float:
    return float((REFERENCE_DIR / "mature_market_erp.txt").read_text().strip())


@lru_cache(maxsize=1)
def country_risk_premiums() -> dict[str, CountryRiskPremium]:
    out = {}
    with open(REFERENCE_DIR / "country_risk_premiums.csv", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["total_erp"].startswith("="):
                raise ValueError(
                    "country_risk_premiums.csv contiene formulas de Excel sin evaluar; "
                    "exporta valores numericos y registra la fecha de la tabla."
                )
            out[row["country"]] = CountryRiskPremium(
                country=row["country"],
                rating=row["rating"],
                default_spread=float(row["default_spread"]) if row["default_spread"] else 0.0,
                total_erp=float(row["total_erp"]),
            )
    return out


def _load_industry_averages(filename: str) -> dict[str, IndustryAverage]:
    out = {}
    with open(REFERENCE_DIR / filename, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            values = {k: _to_float(v) for k, v in row.items() if k != "industry"}
            out[row["industry"]] = IndustryAverage(industry=row["industry"], **values)
    return out


@lru_cache(maxsize=1)
def industry_averages_us() -> dict[str, IndustryAverage]:
    return _load_industry_averages("industry_averages_us.csv")


@lru_cache(maxsize=1)
def industry_averages_global() -> dict[str, IndustryAverage]:
    return _load_industry_averages("industry_averages_global.csv")


def get_country_erp(country: str) -> CountryRiskPremium:
    table = country_risk_premiums()
    canonical = COUNTRY_ALIASES.get(country, country)
    if canonical not in table:
        raise KeyError(f"Pais no encontrado en la tabla de riesgo-pais: {country!r}")
    return table[canonical]


def get_industry_average(industry: str, *, global_: bool = False) -> IndustryAverage:
    table = industry_averages_global() if global_ else industry_averages_us()
    if industry not in table:
        scope = "Industry Averages (Global)" if global_ else "Industry Averages(US)"
        raise KeyError(f"Industria no encontrada en {scope}: {industry!r}")
    return table[industry]
