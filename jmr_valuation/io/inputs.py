"""Carga los inputs de una empresa desde un CSV simple (field,value).

Mismos campos que hoy se llenan a mano en 'Input sheet' del Excel -- pensado
para que cualquier empresa nueva sea un archivo CSV nuevo, no una copia del
workbook completo. Ver data/example_adbe.csv para el formato esperado.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass, fields
from pathlib import Path


def _parse_value(raw: str):
    raw = raw.strip()
    if raw == "":
        return None
    low = raw.lower()
    if low in ("yes", "si", "sí", "true"):
        return True
    if low in ("no", "false"):
        return False
    try:
        return float(raw) if ("." in raw or "e" in low) else int(raw)
    except ValueError:
        return raw


@dataclass
class CompanyInputs:
    ticker: str
    company_name: str
    country_of_incorporation: str
    industry_us: str
    industry_global: str

    # Numeros del ultimo periodo reportado ('Input sheet' filas 12-25)
    revenue_ltm: float
    revenue_prior_10k: float
    years_since_last_10k: float
    ebit_ltm: float
    ebit_prior_10k: float
    interest_expense_ltm: float
    interest_expense_prior_10k: float
    book_value_equity_ltm: float
    book_value_equity_prior_10k: float
    book_value_debt_ltm: float
    book_value_debt_prior_10k: float
    cash_ltm: float
    cash_prior_10k: float
    cross_holdings_ltm: float = 0.0
    cross_holdings_prior_10k: float = 0.0
    minority_interests: float = 0.0
    shares_outstanding: float = 0.0
    current_price: float = 0.0
    effective_tax_rate: float = 0.0
    marginal_tax_rate: float = 0.25

    # Flags cualitativos
    capitalize_rd: bool = False
    has_operating_leases: bool = False
    has_employee_options: bool = False

    # Supuestos de crecimiento/margen ('Input sheet' filas 27-33)
    revenue_growth_next_year: float = 0.0
    revenue_growth_years_2_to_5: float = 0.0
    target_ebit_margin: float = 0.0  # fallback si no hay margenes historicos (ver abajo)
    year_of_margin_convergence: int = 5
    sales_to_capital_years_1_5: float = 2.0
    sales_to_capital_years_6_10: float = 2.0

    # Margen operativo historico -- 'Valuation output' arma el margen objetivo de
    # cada escenario a partir de ESTOS 4 numeros (Base=LTM, Conservador=MIN de
    # los 4, Optimista=MAX de los 4 y del margen actual), no de un delta fijo.
    # Si se dejan en 0, se usa target_ebit_margin +/- los deltas como fallback.
    ebit_margin_ltm: float = 0.0
    ebit_margin_avg_3y: float = 0.0
    ebit_margin_avg_5y: float = 0.0
    ebit_margin_avg_10y: float = 0.0

    # Mercado / macro
    riskfree_rate: float = 0.0
    initial_cost_of_capital: float = 0.0

    # Opciones para empleados (si has_employee_options)
    n_options_outstanding: float = 0.0
    avg_strike_price: float = 0.0
    avg_option_maturity: float = 0.0
    stdev_stock_price: float = 0.0

    nol_carryforward: float = 0.0

    # Deltas de escenario Conservador/Optimista sobre Base (por defecto: +/-2 pp
    # de crecimiento y margen -- ver docstring de `valuation.run_valuation`
    # para como se usan). Ajustar si se tiene una vision mas informada.
    conservative_growth_delta: float = -0.02
    optimistic_growth_delta: float = 0.02
    conservative_margin_delta: float = -0.02
    optimistic_margin_delta: float = 0.02

    # Ratios historicos promedio para proyectar FCFF/OCF/FCFE/EBITDA
    # (ver models.financials_multiples.historical_ratios_from_actuals para
    # calcularlos desde los estados financieros linea por linea).
    hist_interest_pct_of_ebit: float = 0.0
    hist_da_pct_of_revenue: float = 0.0
    hist_capex_pct_of_revenue: float = 0.0
    hist_nwc_pct_of_revenue_growth: float = 0.0
    hist_net_borrowing_pct_of_revenue: float = 0.0
    hist_shares_growth_rate: float = 0.0
    hist_dividend_growth_rate: float = 0.0
    dividend_per_share_ltm: float = 0.0

    # Multiplos "ancla" para la valoracion relativa. Por defecto se usa la
    # mediana de los ultimos 3 anios (hist_multiple_*_y1/y2/y3, el anio -1
    # primero, tal como quedan en el Excel al cargarlo con excel_loader) --
    # igual que 'EVFCFF'!F19 = MEDIAN(...). Activando la casilla
    # override_<metrica> se pisa la mediana con multiple_<metrica>, igual que
    # escribir algo en la celda J19 del Excel.
    hist_multiple_ev_fcff_y1: float = 0.0
    hist_multiple_ev_fcff_y2: float = 0.0
    hist_multiple_ev_fcff_y3: float = 0.0
    hist_multiple_p_ocf_y1: float = 0.0
    hist_multiple_p_ocf_y2: float = 0.0
    hist_multiple_p_ocf_y3: float = 0.0
    hist_multiple_pe_y1: float = 0.0
    hist_multiple_pe_y2: float = 0.0
    hist_multiple_pe_y3: float = 0.0
    hist_multiple_p_fcfe_y1: float = 0.0
    hist_multiple_p_fcfe_y2: float = 0.0
    hist_multiple_p_fcfe_y3: float = 0.0
    hist_multiple_ev_ebitda_y1: float = 0.0
    hist_multiple_ev_ebitda_y2: float = 0.0
    hist_multiple_ev_ebitda_y3: float = 0.0

    override_ev_fcff: bool = False
    override_p_ocf: bool = False
    override_pe: bool = False
    override_p_fcfe: bool = False
    override_ev_ebitda: bool = False

    multiple_ev_fcff: float = 0.0
    multiple_p_ocf: float = 0.0
    multiple_pe: float = 0.0
    multiple_p_fcfe: float = 0.0
    multiple_ev_ebitda: float = 0.0

    # Solo necesarios si has_operating_leases = Yes (ver models.converters)
    lease_expense_current_year: float = 0.0
    lease_commitment_y1: float = 0.0
    lease_commitment_y2: float = 0.0
    lease_commitment_y3: float = 0.0
    lease_commitment_y4: float = 0.0
    lease_commitment_y5: float = 0.0
    lease_commitment_y6_plus: float = 0.0

    # Solo necesarios si capitalize_rd = Yes (ver models.converters). El Excel
    # amortiza usando los `rd_amortization_years` anios anteriores (hasta 9,
    # limite de la hoja real) -- si tu periodo de amortizacion es corto, dejar
    # los campos que no usas en 0 no afecta el resultado.
    rd_amortization_years: int = 3
    rd_expense_current_year: float = 0.0
    rd_expense_year_minus_1: float = 0.0
    rd_expense_year_minus_2: float = 0.0
    rd_expense_year_minus_3: float = 0.0
    rd_expense_year_minus_4: float = 0.0
    rd_expense_year_minus_5: float = 0.0
    rd_expense_year_minus_6: float = 0.0
    rd_expense_year_minus_7: float = 0.0
    rd_expense_year_minus_8: float = 0.0
    rd_expense_year_minus_9: float = 0.0

    # Para el precio objetivo ponderado (ver models.blend) -- uno de
    # models.blend.COMPANY_TYPES: Crecimiento, Madura, Generico, Defensiva,
    # Ciclica/Commodity, Intensiva en Capital, Financiera, Infraestructura,
    # REIT/Inmobiliaria, Software.
    company_type: str = "Generico"
    margin_of_safety: float = 0.35

    # Incluir/excluir cada metodo del precio objetivo ponderado (ver models.blend).
    # Al excluir uno, su peso se reparte proporcionalmente entre los que quedan
    # activos -- no se pierde, ni queda el resto sumando menos de 100%.
    include_dcf: bool = True
    include_ev_ebitda: bool = True
    include_ev_fcff: bool = True
    include_pe: bool = True
    include_p_fcfe: bool = True
    include_p_ocf: bool = True

    company_description: str = ""  # en espanol, la llena el usuario (no viene de ningun API)


def load_company_inputs(csv_source) -> CompanyInputs:
    """csv_source: ruta a un archivo, o un objeto tipo archivo ya abierto (p.ej. io.StringIO)."""
    values: dict[str, object] = {}

    def _read_rows(f):
        for row in csv.reader(f):
            if not row or row[0].strip().startswith("#"):
                continue
            if len(row) < 2:
                continue
            # si el valor tenia comas sin comillas (ej. una descripcion escrita
            # a mano), csv.reader lo separa en mas columnas -- las reunimos en
            # vez de truncar en silencio.
            key, raw_value = row[0].strip(), ",".join(row[1:])
            values[key] = _parse_value(raw_value)

    if hasattr(csv_source, "read"):
        _read_rows(csv_source)
    else:
        with open(csv_source, newline="", encoding="utf-8") as f:
            _read_rows(f)

    csv_path = csv_source if not hasattr(csv_source, "read") else "<archivo subido>"
    valid_fields = {f.name for f in fields(CompanyInputs)}
    unknown = set(values) - valid_fields
    if unknown:
        raise ValueError(f"Campos desconocidos en {csv_path}: {sorted(unknown)}")

    required_no_default = {
        "ticker", "company_name", "country_of_incorporation", "industry_us", "industry_global",
        "revenue_ltm", "revenue_prior_10k", "years_since_last_10k", "ebit_ltm", "ebit_prior_10k",
        "interest_expense_ltm", "interest_expense_prior_10k", "book_value_equity_ltm",
        "book_value_equity_prior_10k", "book_value_debt_ltm", "book_value_debt_prior_10k",
        "cash_ltm", "cash_prior_10k",
    }
    missing = required_no_default - set(values)
    if missing:
        raise ValueError(f"Faltan campos obligatorios en {csv_path}: {sorted(missing)}")

    return CompanyInputs(**values)


def _format_value(value: object) -> str:
    if isinstance(value, bool):
        return "Yes" if value else "No"
    return str(value)


def save_company_inputs(inputs: CompanyInputs, csv_target) -> None:
    """Escribe un CompanyInputs a CSV field,value. csv_target: ruta, o archivo/buffer ya abierto para escritura."""
    def _write_rows(f):
        writer = csv.writer(f)
        for field in fields(CompanyInputs):
            writer.writerow([field.name, _format_value(getattr(inputs, field.name))])

    if hasattr(csv_target, "write"):
        _write_rows(csv_target)
    else:
        with open(csv_target, "w", newline="", encoding="utf-8") as f:
            _write_rows(f)
