"""Vitrina interactiva -- reemplaza 'Presentacion' y 'Resumen de Valoracion' del Excel.

Correr con:
    streamlit run jmr_valuation/report/dashboard.py
"""
from __future__ import annotations

import io
import sys
from dataclasses import fields
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

import pandas as pd
import streamlit as st

from jmr_valuation.io.company_store import list_saved_companies, load_saved_company, save_company
from jmr_valuation.io.description_fetch import fetch_company_description_es
from jmr_valuation.io.excel_loader import load_company_inputs_from_excel
from jmr_valuation.io.inputs import CompanyInputs, load_company_inputs, save_company_inputs
from jmr_valuation.io.sec_edgar_client import SecEdgarError
from jmr_valuation.io.sec_edgar_loader import load_company_inputs_from_sec_edgar
from jmr_valuation.io.sec_xbrl_instance import AugmentedSecEdgarClient
from jmr_valuation.models.blend import COMPANY_TYPES
from jmr_valuation.models.relative import SENSITIVITY_DELTAS, resolve_anchor_multiple
from jmr_valuation.valuation import RELATIVE_METRICS, SCENARIOS, run_valuation

# Campos que son una fraccion (0.045 = 4.5%) y se muestran/editan como
# porcentaje con 2 decimales en vez de la fraccion con 6 decimales.
PERCENT_FIELDS = {
    "revenue_growth_next_year", "revenue_growth_years_2_to_5", "target_ebit_margin",
    "riskfree_rate", "initial_cost_of_capital", "effective_tax_rate", "marginal_tax_rate",
    "conservative_growth_delta", "optimistic_growth_delta", "conservative_margin_delta",
    "optimistic_margin_delta", "hist_interest_pct_of_ebit", "hist_da_pct_of_revenue",
    "hist_capex_pct_of_revenue", "hist_nwc_pct_of_revenue_growth", "hist_net_borrowing_pct_of_revenue",
    "hist_shares_growth_rate", "hist_dividend_growth_rate", "margin_of_safety", "stdev_stock_price",
    "ebit_margin_ltm", "ebit_margin_avg_3y", "ebit_margin_avg_5y", "ebit_margin_avg_10y",
}

# metrica -> prefijo de campo (hist_multiple_<prefijo>_yN, override_<prefijo>, multiple_<prefijo>)
MULTIPLE_FIELD_PREFIX = {
    "EV/FCFF": "ev_fcff", "P/OCF": "p_ocf", "P/E": "pe", "P/FCFE": "p_fcfe", "EV/EBITDA": "ev_ebitda",
}

DATA_DIR = _PROJECT_ROOT / "data"

QUALITATIVE_TEXT_FIELDS = {
    "qual_business_model", "qual_competitive_advantages", "qual_key_risks",
    "qual_management_quality", "qual_growth_catalysts",
}

# --- Como se agrupan y etiquetan los campos de CompanyInputs en el formulario ---
LABELS: dict[str, str] = {
    "ticker": "Ticker", "company_name": "Nombre de la empresa",
    "company_description": "Descripcion de la empresa (en espanol)",
    "country_of_incorporation": "Pais de incorporacion", "industry_us": "Industria (US)",
    "industry_global": "Industria (Global)", "current_price": "Precio actual de mercado",
    "revenue_ltm": "Ingresos (LTM)", "revenue_prior_10k": "Ingresos (10-K anterior)",
    "years_since_last_10k": "Anios desde el ultimo 10-K", "ebit_ltm": "EBIT (LTM)",
    "ebit_prior_10k": "EBIT (10-K anterior)", "interest_expense_ltm": "Gasto en intereses (LTM)",
    "interest_expense_prior_10k": "Gasto en intereses (10-K anterior)",
    "book_value_equity_ltm": "Valor libro del equity (LTM)",
    "book_value_equity_prior_10k": "Valor libro del equity (10-K anterior)",
    "book_value_debt_ltm": "Valor libro de la deuda (LTM)",
    "book_value_debt_prior_10k": "Valor libro de la deuda (10-K anterior)",
    "cash_ltm": "Caja (LTM)", "cash_prior_10k": "Caja (10-K anterior)",
    "cross_holdings_ltm": "Otros activos no operativos (LTM)",
    "cross_holdings_prior_10k": "Otros activos no operativos (10-K anterior)",
    "minority_interests": "Interes minoritario", "shares_outstanding": "Acciones en circulacion",
    "effective_tax_rate": "Tasa impositiva efectiva", "marginal_tax_rate": "Tasa impositiva marginal",
    "nol_carryforward": "Perdidas fiscales acumuladas (NOL)", "dividend_per_share_ltm": "Dividendo por accion (LTM)",
    "revenue_growth_next_year": "Crecimiento de ingresos - anio 1",
    "revenue_growth_years_2_to_5": "Crecimiento de ingresos - anios 2 a 5",
    "target_ebit_margin": "Margen EBIT objetivo", "year_of_margin_convergence": "Anio de convergencia del margen",
    "sales_to_capital_years_1_5": "Ventas/Capital (anios 1-5)", "sales_to_capital_years_6_10": "Ventas/Capital (anios 6-10)",
    "riskfree_rate": "Tasa libre de riesgo", "initial_cost_of_capital": "Costo de capital inicial (WACC)",
    "conservative_growth_delta": "Ajuste de crecimiento -- Conservador",
    "optimistic_growth_delta": "Ajuste de crecimiento -- Optimista",
    "conservative_margin_delta": "Ajuste de margen -- Conservador",
    "optimistic_margin_delta": "Ajuste de margen -- Optimista",
    "capitalize_rd": "Capitalizar I+D", "has_operating_leases": "Tiene leasing operativo",
    "has_employee_options": "Tiene opciones para empleados",
    "n_options_outstanding": "Opciones en circulacion", "avg_strike_price": "Precio de ejercicio promedio",
    "avg_option_maturity": "Vencimiento promedio (anios)", "stdev_stock_price": "Desviacion estandar del precio",
    "hist_interest_pct_of_ebit": "Interes / EBIT (historico)", "hist_da_pct_of_revenue": "D&A / Ingresos (historico)",
    "hist_capex_pct_of_revenue": "CapEx / Ingresos (historico)",
    "hist_nwc_pct_of_revenue_growth": "Cambio en NWC / Crecimiento de ingresos (historico)",
    "hist_net_borrowing_pct_of_revenue": "Endeudamiento neto / Ingresos (historico)",
    "hist_shares_growth_rate": "Crecimiento de acciones en circulacion (historico)",
    "hist_dividend_growth_rate": "Crecimiento de dividendos (historico)",
    "hist_multiple_ev_fcff_y1": "EV/FCFF anio -1", "hist_multiple_ev_fcff_y2": "EV/FCFF anio -2",
    "hist_multiple_ev_fcff_y3": "EV/FCFF anio -3", "multiple_ev_fcff": "EV/FCFF -- override manual (0 = usar mediana)",
    "hist_multiple_p_ocf_y1": "P/OCF anio -1", "hist_multiple_p_ocf_y2": "P/OCF anio -2",
    "hist_multiple_p_ocf_y3": "P/OCF anio -3", "multiple_p_ocf": "P/OCF -- override manual (0 = usar mediana)",
    "hist_multiple_pe_y1": "P/E anio -1", "hist_multiple_pe_y2": "P/E anio -2",
    "hist_multiple_pe_y3": "P/E anio -3", "multiple_pe": "P/E -- override manual (0 = usar mediana)",
    "hist_multiple_p_fcfe_y1": "P/FCFE anio -1", "hist_multiple_p_fcfe_y2": "P/FCFE anio -2",
    "hist_multiple_p_fcfe_y3": "P/FCFE anio -3", "multiple_p_fcfe": "P/FCFE -- override manual (0 = usar mediana)",
    "hist_multiple_ev_ebitda_y1": "EV/EBITDA anio -1", "hist_multiple_ev_ebitda_y2": "EV/EBITDA anio -2",
    "hist_multiple_ev_ebitda_y3": "EV/EBITDA anio -3",
    "multiple_ev_ebitda": "EV/EBITDA -- override manual (0 = usar mediana)",
    "company_type": "Tipo de empresa (pesos del blend)", "margin_of_safety": "Margen de seguridad",
    "include_dcf": "Incluir DCF Damodaran", "include_ev_ebitda": "Incluir EV/EBITDA",
    "include_ev_fcff": "Incluir EV/FCFF", "include_pe": "Incluir P/E",
    "include_p_fcfe": "Incluir P/FCFE", "include_p_ocf": "Incluir P/OCF",
    "lease_expense_current_year": "Gasto de leasing (anio actual)",
    "lease_commitment_y1": "Compromiso de leasing - anio 1", "lease_commitment_y2": "Compromiso de leasing - anio 2",
    "lease_commitment_y3": "Compromiso de leasing - anio 3", "lease_commitment_y4": "Compromiso de leasing - anio 4",
    "lease_commitment_y5": "Compromiso de leasing - anio 5", "lease_commitment_y6_plus": "Compromiso de leasing - anio 6+",
    "rd_amortization_years": "Anios de amortizacion de I+D", "rd_expense_current_year": "Gasto en I+D (anio actual)",
    "rd_expense_year_minus_1": "Gasto en I+D (anio -1)", "rd_expense_year_minus_2": "Gasto en I+D (anio -2)",
    "rd_expense_year_minus_3": "Gasto en I+D (anio -3)", "rd_expense_year_minus_4": "Gasto en I+D (anio -4)",
    "rd_expense_year_minus_5": "Gasto en I+D (anio -5)", "rd_expense_year_minus_6": "Gasto en I+D (anio -6)",
    "rd_expense_year_minus_7": "Gasto en I+D (anio -7)", "rd_expense_year_minus_8": "Gasto en I+D (anio -8)",
    "rd_expense_year_minus_9": "Gasto en I+D (anio -9)",
    "ebit_margin_ltm": "Margen EBIT LTM (sin ajustar)", "ebit_margin_avg_3y": "Margen EBIT promedio 3 anios",
    "ebit_margin_avg_5y": "Margen EBIT promedio 5 anios", "ebit_margin_avg_10y": "Margen EBIT promedio 10 anios",
    "qual_business_model": "Modelo de negocio", "qual_competitive_advantages": "Ventajas competitivas (moat)",
    "qual_key_risks": "Riesgos principales", "qual_management_quality": "Equipo directivo y gobierno corporativo",
    "qual_growth_catalysts": "Catalizadores de crecimiento",
}

GROUPS: list[tuple[str, list[str]]] = [
    ("Identificacion", ["ticker", "company_name", "country_of_incorporation",
                         "industry_us", "industry_global", "current_price"]),
    ("Estados financieros", ["revenue_ltm", "revenue_prior_10k", "years_since_last_10k",
                              "ebit_ltm", "ebit_prior_10k", "interest_expense_ltm", "interest_expense_prior_10k",
                              "book_value_equity_ltm", "book_value_equity_prior_10k",
                              "book_value_debt_ltm", "book_value_debt_prior_10k", "cash_ltm", "cash_prior_10k",
                              "cross_holdings_ltm", "cross_holdings_prior_10k", "minority_interests",
                              "shares_outstanding", "effective_tax_rate", "marginal_tax_rate",
                              "nol_carryforward", "dividend_per_share_ltm"]),
    ("Supuestos de crecimiento y margen", ["revenue_growth_next_year", "revenue_growth_years_2_to_5",
                                            "year_of_margin_convergence",
                                            "sales_to_capital_years_1_5", "sales_to_capital_years_6_10",
                                            "conservative_growth_delta", "optimistic_growth_delta"]),
    ("Margen EBIT objetivo -- Base=LTM, Conservador=minimo, Optimista=maximo (o el fallback de abajo si estan en 0)",
     ["ebit_margin_ltm", "ebit_margin_avg_3y", "ebit_margin_avg_5y", "ebit_margin_avg_10y",
      "target_ebit_margin", "conservative_margin_delta", "optimistic_margin_delta"]),
    ("Costo de capital", ["riskfree_rate", "initial_cost_of_capital"]),
    ("Ratios historicos (para FCFF/OCF/FCFE/EBITDA proyectados)",
     ["hist_interest_pct_of_ebit", "hist_da_pct_of_revenue", "hist_capex_pct_of_revenue",
      "hist_nwc_pct_of_revenue_growth", "hist_net_borrowing_pct_of_revenue",
      "hist_shares_growth_rate", "hist_dividend_growth_rate"]),
    ("Precio objetivo ponderado", ["company_type", "margin_of_safety",
                                    "include_dcf", "include_ev_ebitda", "include_ev_fcff",
                                    "include_pe", "include_p_fcfe", "include_p_ocf"]),
    ("Ajustes -- I+D, leasing y opciones",
     ["capitalize_rd", "rd_amortization_years", "rd_expense_current_year",
      "rd_expense_year_minus_1", "rd_expense_year_minus_2", "rd_expense_year_minus_3",
      "rd_expense_year_minus_4", "rd_expense_year_minus_5", "rd_expense_year_minus_6",
      "rd_expense_year_minus_7", "rd_expense_year_minus_8", "rd_expense_year_minus_9",
      "has_operating_leases", "lease_expense_current_year", "lease_commitment_y1", "lease_commitment_y2",
      "lease_commitment_y3", "lease_commitment_y4", "lease_commitment_y5", "lease_commitment_y6_plus",
      "has_employee_options", "n_options_outstanding", "avg_strike_price", "avg_option_maturity",
      "stdev_stock_price"]),
]

FIELD_TYPES = {f.name: f.type for f in fields(CompanyInputs)}


def _save_and_notify(inputs: CompanyInputs) -> None:
    """Persiste la empresa recien cargada en data/saved_companies/ para poder
    volver a abrirla despues. No debe tumbar el dashboard si falla (ej. disco
    de solo lectura) -- en ese caso el usuario igual puede seguir trabajando
    y descargar el CSV a mano."""
    try:
        path = save_company(inputs)
    except OSError as exc:
        st.warning(f"No se pudo guardar la empresa en disco: {exc}")
        return
    st.toast(f"Guardado como '{path.stem}' -- vas a poder volver a abrirla en 'empresa guardada antes'.")


def _fetch_description_callback() -> None:
    """Callback de 'Buscar en Wikipedia' -- corre antes del rerun, asi el
    text_area de company_description ya arranca con el valor nuevo."""
    company_name = st.session_state.get("company_name", "")
    if not company_name.strip():
        st.session_state["_wikipedia_fetch_error"] = "Completa 'Nombre de la empresa' antes de buscar."
        return
    try:
        description = fetch_company_description_es(company_name)
    except Exception as exc:  # noqa: BLE001 -- se muestra al usuario, no se traga silenciosamente
        st.session_state["_wikipedia_fetch_error"] = f"No se pudo buscar en Wikipedia: {exc}"
        return
    if description:
        st.session_state["company_description"] = description
        st.session_state["_wikipedia_fetch_error"] = None
    else:
        st.session_state["_wikipedia_fetch_error"] = (
            f"No se encontro un articulo en Wikipedia en espanol para '{company_name}'. "
            "Proba con el nombre completo de la empresa, o escribi la descripcion a mano."
        )


def _init_session_state(inputs: CompanyInputs) -> None:
    for field in fields(CompanyInputs):
        value = getattr(inputs, field.name)
        if field.name in PERCENT_FIELDS:
            st.session_state[f"{field.name}__pct"] = round(value * 100, 2)
        else:
            st.session_state[field.name] = value


def _render_field(name: str) -> None:
    label = LABELS.get(name, name.replace("_", " ").capitalize())
    ftype = FIELD_TYPES[name]
    if name == "company_type":
        st.selectbox(label, COMPANY_TYPES, key=name)
    elif ftype == "bool":
        st.checkbox(label, key=name)
    elif name == "company_description":
        st.text_area(label, key=name, height=100,
                      help="Texto libre, en espanol. Se puede autocompletar desde Wikipedia con el "
                           "boton de al lado, o escribirlo a mano.")
    elif name in QUALITATIVE_TEXT_FIELDS:
        st.text_area(label, key=name, height=140,
                      help="Texto libre, con tu propio criterio -- no viene de ningun API.")
    elif ftype == "str":
        st.text_input(label, key=name)
    elif ftype == "int":
        st.number_input(label, key=name, step=1)
    elif name in PERCENT_FIELDS:
        st.number_input(f"{label} (%)", key=f"{name}__pct", format="%.2f", step=0.01)
    else:
        st.number_input(label, key=name, format="%.2f")


def _render_multiples_group() -> None:
    """Un bloque por metrica: 3 anios historicos (del Excel) + mediana calculada
    + casilla de override para pisarla con un valor manual."""
    for metric_name, prefix in MULTIPLE_FIELD_PREFIX.items():
        st.markdown(f"**{metric_name}**")
        y1, y2, y3 = (f"hist_multiple_{prefix}_y1", f"hist_multiple_{prefix}_y2", f"hist_multiple_{prefix}_y3")
        cols = st.columns(3)
        for col, field_name, year_label in zip(cols, (y3, y2, y1), ("Anio -3", "Anio -2", "Anio -1")):
            with col:
                st.number_input(year_label, key=field_name, format="%.2f", step=0.01)

        historical = [st.session_state[y1], st.session_state[y2], st.session_state[y3]]
        median = resolve_anchor_multiple(historical) if any(historical) else 0.0

        override_key = f"override_{prefix}"
        st.checkbox(f"Usar un valor manual en vez de la mediana ({median:.2f}x)", key=override_key)
        if st.session_state[override_key]:
            st.number_input("Multiplo manual", key=f"multiple_{prefix}", format="%.2f", step=0.01)
        st.divider()


def _inputs_from_session_state() -> CompanyInputs:
    kwargs = {}
    for field in fields(CompanyInputs):
        if field.name in PERCENT_FIELDS:
            kwargs[field.name] = st.session_state[f"{field.name}__pct"] / 100
        else:
            kwargs[field.name] = st.session_state[field.name]
    return CompanyInputs(**kwargs)


def _scenario_table(report) -> pd.DataFrame:
    rows = []
    for scenario in SCENARIOS:
        b = report.scenarios[scenario].equity_bridge
        rows.append({
            "Escenario": scenario,
            "Valor / accion": b.value_per_share,
            "Precio actual": report.inputs.current_price,
            "Precio / Valor": b.price_as_pct_of_value,
        })
    return pd.DataFrame(rows).set_index("Escenario")


def _relative_summary_table(report) -> pd.DataFrame:
    rows = []
    for metric_name in RELATIVE_METRICS:
        for scenario in SCENARIOS:
            result = report.relative[metric_name][scenario]
            fy3 = result.years[-1]
            rows.append({
                "Metrica": metric_name, "Escenario": scenario,
                "Ancla (mediana 3a)": report.anchor_multiples[metric_name],
                "Multiplo usado": result.multiple_fy1,
                "Target FY+3": fy3.total_target_price,
                "Retorno total": fy3.total_return,
                "TIR anualizada": fy3.annualized_return,
            })
    return pd.DataFrame(rows)


def _relative_full_table(report) -> pd.DataFrame:
    """Todos los anios (FY+1/+2/+3), todas las metricas, todos los escenarios -- para ver o graficar."""
    rows = []
    for metric_name in RELATIVE_METRICS:
        for scenario in SCENARIOS:
            result = report.relative[metric_name][scenario]
            for year in result.years:
                rows.append({
                    "Metrica": metric_name, "Escenario": scenario, "Anio": year.year_label,
                    "Multiplo": year.multiple, "Valor de la metrica": year.metric,
                    "Precio implicito": year.implied_target_price,
                    "Dividendos acumulados": year.cumulative_dividends,
                    "Precio objetivo total": year.total_target_price,
                    "Retorno total": year.total_return, "TIR anualizada": year.annualized_return,
                })
    return pd.DataFrame(rows)


def _relative_chart_data(report, scenario: str = "Base") -> pd.DataFrame:
    """Precio objetivo total por anio (FY+1/+2/+3), una columna por metrica, para graficar."""
    year_labels = [y.year_label for y in next(iter(report.relative.values()))[scenario].years]
    data = {
        metric_name: [y.total_target_price for y in report.relative[metric_name][scenario].years]
        for metric_name in RELATIVE_METRICS
    }
    data["Precio actual"] = [report.inputs.current_price] * len(year_labels)
    return pd.DataFrame(data, index=year_labels)


def _sensitivity_dataframe(matrix: list[list[float]]) -> pd.DataFrame:
    row_labels = [f"Multiplo {(d - 1):+.0%}" for d in SENSITIVITY_DELTAS]
    col_labels = [f"Metrica {(d - 1):+.0%}" for d in SENSITIVITY_DELTAS]
    return pd.DataFrame(matrix, index=row_labels, columns=col_labels)


_CUSTOM_CSS = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
<style>
  html, body, [class*="css"] { font-family: 'Inter', -apple-system, sans-serif; }

  .jmr-hero {
    padding: 0.25rem 0 0.5rem 0;
  }
  .jmr-hero-title {
    font-size: 1.9rem;
    font-weight: 700;
    color: #1B2A4A;
    letter-spacing: -0.01em;
  }
  .jmr-ticker {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 1rem;
    font-weight: 500;
    color: #FFFFFF;
    background: #2F5E8C;
    padding: 0.15rem 0.55rem;
    border-radius: 6px;
    margin-left: 0.5rem;
    vertical-align: middle;
  }
  .jmr-hero-sub {
    color: #5C6670;
    font-size: 0.95rem;
    margin-top: 0.15rem;
  }
  .jmr-description {
    background: #F2F4F7;
    border-left: 3px solid #2F5E8C;
    border-radius: 6px;
    padding: 0.75rem 1rem;
    margin: 0.6rem 0 1.1rem 0;
    color: #33404A;
    font-size: 0.92rem;
    line-height: 1.5;
  }

  [data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #E3E7EC;
    border-radius: 10px;
    padding: 0.75rem 0.9rem 0.6rem 0.9rem;
    box-shadow: 0 1px 2px rgba(27,42,74,0.04);
  }
  [data-testid="stMetricLabel"] {
    font-size: 0.78rem;
    color: #5C6670;
  }
  [data-testid="stMetricValue"] {
    font-family: 'IBM Plex Mono', monospace;
    color: #1B2A4A;
  }

  h1, h2, h3, h4 { color: #1B2A4A; font-weight: 700; }

  [data-testid="stTabs"] button[role="tab"] {
    font-weight: 600;
  }

  section[data-testid="stSidebar"] {
    border-right: 1px solid #E3E7EC;
  }
</style>
"""


def _inject_custom_css() -> None:
    st.html(_CUSTOM_CSS)


def _render_company_snapshot(inputs: CompanyInputs) -> None:
    """Portada tipo 'company overview' de una terminal financiera (fiscal.ai,
    stockanalysis.com, Bloomberg): precio, tamano, multiplos trailing, margen,
    crecimiento y salud financiera de un vistazo -- armado con datos que ya
    tenemos localmente, sin depender de ninguna API paga."""

    def _x(value) -> str:
        return f"{value:.1f}x" if value else "—"

    market_cap = inputs.current_price * inputs.shares_outstanding
    net_debt = inputs.book_value_debt_ltm - inputs.cash_ltm
    enterprise_value = market_cap + net_debt
    ebit_margin_ltm = inputs.ebit_ltm / inputs.revenue_ltm if inputs.revenue_ltm else 0.0
    revenue_growth_ltm = (
        (inputs.revenue_ltm / inputs.revenue_prior_10k) - 1 if inputs.revenue_prior_10k else 0.0
    )
    dividend_yield = inputs.dividend_per_share_ltm / inputs.current_price if inputs.current_price else 0.0

    st.markdown(
        f"""<div class="jmr-hero">
            <div class="jmr-hero-title">{inputs.company_name} <span class="jmr-ticker">{inputs.ticker}</span></div>
            <div class="jmr-hero-sub">{inputs.industry_us} &middot; {inputs.country_of_incorporation}</div>
        </div>""",
        unsafe_allow_html=True,
    )
    if inputs.company_description:
        st.markdown(f'<div class="jmr-description">{inputs.company_description}</div>', unsafe_allow_html=True)
    else:
        st.caption("Sin descripcion cargada -- agregala en 'Identificacion' en la barra lateral.")

    row1 = st.columns(5)
    row1[0].metric("Precio", f"{inputs.current_price:,.2f}")
    row1[1].metric("Market Cap", f"{market_cap:,.0f}")
    row1[2].metric("Enterprise Value", f"{enterprise_value:,.0f}")
    row1[3].metric("Deuda neta", f"{net_debt:,.0f}")
    row1[4].metric("Dividend Yield", f"{dividend_yield:.2%}" if dividend_yield else "—")

    row2 = st.columns(5)
    row2[0].metric("P/E (TTM)", _x(inputs.hist_multiple_pe_y1))
    row2[1].metric("EV/EBITDA (TTM)", _x(inputs.hist_multiple_ev_ebitda_y1))
    row2[2].metric("EV/FCFF (TTM)", _x(inputs.hist_multiple_ev_fcff_y1))
    row2[3].metric("P/OCF (TTM)", _x(inputs.hist_multiple_p_ocf_y1))
    row2[4].metric("P/FCFE (TTM)", _x(inputs.hist_multiple_p_fcfe_y1))

    row3 = st.columns(5)
    row3[0].metric("Margen EBIT (LTM)", f"{ebit_margin_ltm:.1%}")
    row3[1].metric("Crecimiento ingresos (LTM)", f"{revenue_growth_ltm:+.1%}")
    row3[2].metric("Tasa impositiva efectiva", f"{inputs.effective_tax_rate:.1%}")
    row3[3].metric("Costo de capital (WACC)", f"{inputs.initial_cost_of_capital:.2%}")
    row3[4].metric("Tasa libre de riesgo", f"{inputs.riskfree_rate:.2%}")

    row4 = st.columns(5)
    row4[0].metric("Acciones en circulacion", f"{inputs.shares_outstanding:,.1f}M")
    row4[1].metric("Caja", f"{inputs.cash_ltm:,.0f}")
    row4[2].metric("Deuda (valor libro)", f"{inputs.book_value_debt_ltm:,.0f}")
    row4[3].metric("Valor libro del equity", f"{inputs.book_value_equity_ltm:,.0f}")
    if inputs.has_employee_options and inputs.n_options_outstanding:
        row4[4].metric("Opciones en circulacion", f"{inputs.n_options_outstanding:,.2f}M")
    elif inputs.nol_carryforward:
        row4[4].metric("NOL acumulado", f"{inputs.nol_carryforward:,.0f}")
    else:
        row4[4].metric("Tasa impositiva marginal", f"{inputs.marginal_tax_rate:.1%}")

    st.divider()


def _dcf_year_table(dcf_result) -> pd.DataFrame:
    rows = [{
        "Anio": y.year, "Crecimiento": y.revenue_growth, "Ingresos": y.revenue,
        "Margen EBIT": y.ebit_margin, "EBIT": y.ebit, "EBIT(1-t)": y.ebit_after_tax,
        "Reinversion": y.reinvestment, "FCFF": y.fcff, "WACC": y.cost_of_capital,
        "FD acumulado": y.cumulative_discount_factor, "PV(FCFF)": y.pv_fcff, "ROIC": y.roic,
    } for y in dcf_result.years]
    return pd.DataFrame(rows).set_index("Anio")


def main() -> None:
    st.set_page_config(page_title="JMR Valuation", layout="wide", page_icon="📊")
    _inject_custom_css()
    st.title("Modelo JMR -- Vitrina de valoracion")
    st.caption("Motor DCF (3 escenarios) + valoracion relativa (5 multiplos). "
               "Reemplaza 'Presentacion' y 'Resumen de Valoracion' del Excel.")

    with st.sidebar:
        st.header("Empresa")
        csv_files = sorted(DATA_DIR.glob("*.csv"))
        options = [f.name for f in csv_files]
        chosen = st.selectbox("Cargar desde data/", options) if options else None

        saved_paths = list_saved_companies()
        saved_options = [p.stem for p in saved_paths]
        saved_chosen = (
            st.selectbox("...o abrir una empresa guardada antes", saved_options,
                         help="Cada empresa que subis (Excel, CSV o SEC EDGAR) se guarda aca "
                              "automaticamente para poder volver a abrirla despues.")
            if saved_options else None
        )

        uploaded_excel = st.file_uploader(
            "...o subir el Excel del modelo (.xlsx)", type="xlsx",
            help="Tiene que estar recalculado y guardado en Excel al menos una vez -- "
                 "openpyxl lee los valores que Excel ya calculo, no calcula formulas.",
        )
        uploaded_csv = st.file_uploader("...o subir un CSV", type="csv")

        if "loaded_source" not in st.session_state:
            st.session_state.loaded_source = None

        if uploaded_excel is not None and st.session_state.loaded_source != f"xlsx:{uploaded_excel.name}":
            try:
                inputs = load_company_inputs_from_excel(io.BytesIO(uploaded_excel.getvalue()))
            except Exception as exc:  # noqa: BLE001 -- se muestra al usuario
                st.error(f"No se pudo leer el Excel: {exc}")
                st.stop()
            _init_session_state(inputs)
            st.session_state.loaded_source = f"xlsx:{uploaded_excel.name}"
            _save_and_notify(inputs)
        elif (uploaded_excel is None and uploaded_csv is not None
              and st.session_state.loaded_source != f"upload:{uploaded_csv.name}"):
            inputs = load_company_inputs(io.StringIO(uploaded_csv.getvalue().decode("utf-8")))
            _init_session_state(inputs)
            st.session_state.loaded_source = f"upload:{uploaded_csv.name}"
            _save_and_notify(inputs)
        elif (uploaded_excel is None and uploaded_csv is None and chosen
              and chosen != st.session_state.get("prev_chosen")):
            # 'chosen' nunca es None (el selectbox siempre tiene algo seleccionado),
            # asi que comparar contra loaded_source como en las otras dos ramas
            # reengancharia este bloque en cualquier rerun posterior a cargar por
            # SEC EDGAR (esa carga no toca 'chosen') y pisaria los datos de EDGAR
            # con el CSV de la lista otra vez -- por eso se compara contra el
            # valor anterior de 'chosen', no contra loaded_source.
            inputs = load_company_inputs(DATA_DIR / chosen)
            _init_session_state(inputs)
            st.session_state.loaded_source = f"file:{chosen}"
        elif (uploaded_excel is None and uploaded_csv is None and saved_chosen
              and saved_chosen != st.session_state.get("prev_saved_chosen")):
            # mismo motivo que con 'chosen': comparar contra el valor anterior de
            # este selectbox, no contra loaded_source, para no reengancharse en
            # reruns posteriores a otra fuente de carga.
            saved_path = next(p for p in saved_paths if p.stem == saved_chosen)
            inputs = load_saved_company(saved_path)
            _init_session_state(inputs)
            st.session_state.loaded_source = f"saved:{saved_chosen}"
        st.session_state.prev_chosen = chosen
        st.session_state.prev_saved_chosen = saved_chosen

        with st.expander("...o buscar una empresa en SEC EDGAR (solo EE.UU., 10-K/10-Q)"):
            st.caption(
                "Trae ingresos, EBIT, balance, I+D, dividendos y ratios historicos "
                "directo de los estados financieros presentados a la SEC. Lo que la SEC "
                "no tiene -- precio, WACC, tasa libre de riesgo, multiplos historicos -- "
                "hay que completarlo aca."
            )
            edgar_ticker = st.text_input("Ticker", key="edgar_ticker_input", placeholder="ADBE")
            e_col1, e_col2, e_col3 = st.columns(3)
            edgar_price = e_col1.number_input("Precio actual", key="edgar_price_input", format="%.2f")
            edgar_rf_pct = e_col2.number_input("Tasa libre de riesgo (%)", key="edgar_rf_input", format="%.2f")
            edgar_wacc_pct = e_col3.number_input("WACC inicial (%)", key="edgar_wacc_input", format="%.2f")
            if st.button("Buscar en SEC EDGAR", width="stretch"):
                if not edgar_ticker:
                    st.warning("Escribi un ticker primero.")
                else:
                    try:
                        # AugmentedSecEdgarClient: suma el ultimo 10-Q/10-K que la API
                        # companyfacts todavia no incorporo (puede tardar semanas), para
                        # que el LTM no quede un trimestre atrasado.
                        edgar_inputs = load_company_inputs_from_sec_edgar(
                            edgar_ticker, client=AugmentedSecEdgarClient(), current_price=edgar_price,
                            riskfree_rate=edgar_rf_pct / 100, initial_cost_of_capital=edgar_wacc_pct / 100,
                        )
                    except SecEdgarError as exc:
                        st.error(f"No se pudo cargar {edgar_ticker.upper()} desde SEC EDGAR: {exc}")
                        st.stop()
                    _init_session_state(edgar_inputs)
                    st.session_state.loaded_source = f"edgar:{edgar_ticker.upper()}"
                    _save_and_notify(edgar_inputs)
                    st.success(
                        f"Cargado {edgar_inputs.company_name} desde SEC EDGAR. Revisa 'Multiplos ancla' "
                        "(en 0 -- no vienen de EDGAR) y los supuestos de crecimiento/margen antes de "
                        "confiar en el resultado."
                    )

        if st.session_state.loaded_source is None:
            st.info("Elegi un CSV de data/, o subi tu Excel o un CSV, para empezar.")
            st.stop()

        st.divider()
        st.header("Supuestos")
        for group_title, field_names in GROUPS:
            with st.expander(group_title, expanded=(group_title == "Supuestos de crecimiento y margen")):
                for name in field_names:
                    _render_field(name)

        with st.expander("Multiplos ancla -- mediana de los ultimos 3 anios del Excel (u override manual)"):
            _render_multiples_group()

        st.divider()
        current_inputs = _inputs_from_session_state()
        save_col, download_col = st.columns(2)
        with save_col:
            if st.button("Guardar cambios", width="stretch",
                         help="Actualiza la version guardada de esta empresa con los valores actuales."):
                _save_and_notify(current_inputs)
        with download_col:
            buffer = io.StringIO()
            save_company_inputs(current_inputs, buffer)
            st.download_button("Descargar .csv", buffer.getvalue(),
                                file_name=f"{current_inputs.ticker or 'empresa'}.csv", mime="text/csv",
                                width="stretch")

    inputs = _inputs_from_session_state()
    try:
        report = run_valuation(inputs)
    except Exception as exc:  # noqa: BLE001 -- se muestra al usuario, no se traga silenciosamente
        st.error(f"No se pudo calcular la valoracion con estos inputs: {exc}")
        st.stop()

    _render_company_snapshot(inputs)

    st.markdown("#### Valoracion")
    base_bridge = report.scenarios["Base"].equity_bridge
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Precio actual", f"{inputs.current_price:,.2f}")
    col2.metric("Valor DCF -- Base", f"{base_bridge.value_per_share:,.2f}",
                delta=f"{(base_bridge.value_per_share - inputs.current_price):+,.2f}")
    col3.metric("Precio / Valor (Base)",
                f"{base_bridge.price_as_pct_of_value:.1%}" if base_bridge.price_as_pct_of_value else "—")
    col4.metric("Ajuste EBIT (leasing/I+D)", f"{report.ebit_adjustment:+,.1f}")

    st.markdown(f"#### Comparación exploratoria -- tipo *{report.blend.company_type}* "
                "(combina DCF de hoy y precios por múltiplos a 3 años; los pesos son criterios del modelo JMR)")
    blend = report.blend
    bcol1, bcol2, bcol3, bcol4 = st.columns(4)
    bcol1.metric("Ponderado -- Conservador", f"{blend.weighted_price_by_scenario['Conservador']:,.2f}",
                 delta=f"CAGR 3a {blend.cagr_3y_by_scenario['Conservador']:+.1%}")
    bcol2.metric("Ponderado -- Base", f"{blend.weighted_price_by_scenario['Base']:,.2f}",
                 delta=f"CAGR 3a {blend.cagr_3y_by_scenario['Base']:+.1%}")
    bcol3.metric("Ponderado -- Optimista", f"{blend.weighted_price_by_scenario['Optimista']:,.2f}",
                 delta=f"CAGR 3a {blend.cagr_3y_by_scenario['Optimista']:+.1%}")
    bcol4.metric(f"MOS sobre ponderado Base (horizontes mixtos) ({inputs.margin_of_safety:.0%})", f"{blend.mos_price:,.2f}")

    st.markdown("##### Análisis individual por método (escenario Base)")
    st.caption("El ponderado Base determina el umbral principal. El DCF es valor presente; "
               "los múltiplos son objetivos FY+3. Los márgenes individuales usan la cotización disponible.")
    per_method = [{
        "Método": "Ponderado Base (principal)", "Peso": 1.0,
        "Valor base": blend.weighted_price_by_scenario["Base"],
        "MOS vs precio actual": (1 - inputs.current_price / blend.weighted_price_by_scenario["Base"]
                                 if inputs.current_price > 0 else None),
        "Compra con MOS": blend.mos_price,
        "Horizonte": "Mixto",
    }]
    for method, value in blend.method_base_values.items():
        per_method.append({
            "Método": method, "Peso": blend.weights[method], "Valor base": value,
            "MOS vs precio actual": blend.method_mos_vs_current[method],
            "Compra con MOS": blend.method_mos_price[method],
            "Horizonte": "Presente" if method == "DCF Damodaran" else "FY+3",
        })
    individual_df = pd.DataFrame(per_method).set_index("Método")
    st.dataframe(individual_df.style.format({
        "Peso": "{:.0%}", "Valor base": "{:,.2f}",
        "MOS vs precio actual": "{:.1%}", "Compra con MOS": "{:,.2f}",
    }, na_rep="—"), width="stretch")

    with st.expander("Pesos usados y bandas de precio de compra"):
        st.caption("Si excluiste algun metodo (en 'Precio objetivo ponderado' de la barra lateral), "
                   "su peso queda en 0% y se reparte proporcionalmente entre los que quedan activos.")
        weights_df = pd.DataFrame([blend.weights], index=["Peso"]).T
        st.dataframe(weights_df.style.format({"Peso": "{:.0%}"}), width="stretch")
        tiers = blend.buy_price_tiers
        tiers_df = pd.DataFrame({
            "Banda": ["Value", "Deep Value", "Valoracion historica"],
            "Minimo": [tiers.value_min, tiers.deep_value_min, tiers.historical_valuation_min],
            "Maximo": [tiers.value_max, tiers.deep_value_max, tiers.historical_valuation_max],
        }).set_index("Banda")
        st.dataframe(tiers_df.style.format("{:,.2f}"), width="stretch")

    st.markdown("#### Valor por accion segun escenario (por metodo)")
    scenario_df = _scenario_table(report)
    chart_df = scenario_df[["Valor / accion"]].copy()
    chart_df.loc["Precio actual"] = [inputs.current_price]
    st.bar_chart(chart_df)
    st.dataframe(
        scenario_df.style.format({"Valor / accion": "{:,.2f}", "Precio actual": "{:,.2f}", "Precio / Valor": "{:.1%}"}),
        width="stretch",
    )

    tab_relativa, tab_detalle, tab_sensibilidad, tab_dcf, tab_cualitativo = st.tabs(
        ["Valoracion relativa", "Detalle completo (todos los anios)", "Sensibilidad", "Detalle del DCF (Base)",
         "Analisis cualitativo"]
    )

    with tab_relativa:
        st.markdown("Precio objetivo a 3 anios segun multiplo y escenario. "
                     "*Ancla* = mediana de los ultimos 3 anios del Excel, salvo que tengas activo el override.")
        rel_df = _relative_summary_table(report)
        st.dataframe(
            rel_df.style.format({"Ancla (mediana 3a)": "{:.2f}x", "Multiplo usado": "{:.2f}x",
                                  "Target FY+3": "{:,.2f}", "Retorno total": "{:+.1%}", "TIR anualizada": "{:+.1%}"}),
            width="stretch", hide_index=True,
        )
        st.markdown("##### Precio objetivo total por anio -- escenario Base")
        st.line_chart(_relative_chart_data(report, "Base"))

    with tab_detalle:
        st.markdown("Todas las filas de las 5 hojas de multiplos: FY+1, FY+2 y FY+3, "
                     "los 3 escenarios -- podes ordenar, filtrar y descargar como CSV desde la tabla.")
        full_df = _relative_full_table(report)
        st.dataframe(
            full_df.style.format({
                "Multiplo": "{:.2f}x", "Valor de la metrica": "{:,.2f}", "Precio implicito": "{:,.2f}",
                "Dividendos acumulados": "{:,.2f}", "Precio objetivo total": "{:,.2f}",
                "Retorno total": "{:+.1%}", "TIR anualizada": "{:+.1%}",
            }),
            width="stretch", hide_index=True,
        )
        scenario_for_chart = st.selectbox("Escenario a graficar", SCENARIOS, index=1, key="detalle_chart_scenario")
        st.line_chart(_relative_chart_data(report, scenario_for_chart))

    with tab_sensibilidad:
        st.markdown("Precio objetivo FY+3 (escenario Base) si el multiplo y la metrica se mueven "
                     "+/-10%/5% -- misma matriz que las filas 45-51 de cada hoja en el Excel.")
        metric_for_matrix = st.selectbox("Metrica", list(RELATIVE_METRICS), key="sensitivity_metric")
        matrix_df = _sensitivity_dataframe(report.sensitivity[metric_for_matrix])
        st.dataframe(matrix_df.style.format("{:,.2f}").background_gradient(cmap="RdYlGn", axis=None),
                     width="stretch")

    with tab_dcf:
        st.markdown("Proyeccion anio a anio del escenario Base (`models.dcf.run_dcf`).")
        dcf_df = _dcf_year_table(report.scenarios["Base"].dcf)
        st.dataframe(
            dcf_df.style.format({
                "Crecimiento": "{:.1%}", "Ingresos": "{:,.0f}", "Margen EBIT": "{:.1%}",
                "EBIT": "{:,.0f}", "EBIT(1-t)": "{:,.0f}", "Reinversion": "{:,.0f}", "FCFF": "{:,.0f}",
                "WACC": "{:.2%}", "FD acumulado": "{:.3f}", "PV(FCFF)": "{:,.0f}", "ROIC": "{:.1%}",
            }),
            width="stretch",
        )
        st.caption(
            f"Valor terminal: {report.scenarios['Base'].dcf.terminal_value:,.0f}  |  "
            f"PV(valor terminal): {report.scenarios['Base'].dcf.pv_terminal_value:,.0f}  |  "
            f"PV(10 anios explicitos): {report.scenarios['Base'].dcf.pv_explicit_years:,.0f}"
        )

    with tab_cualitativo:
        st.markdown("#### Descripcion del negocio")
        desc_col, btn_col = st.columns([5, 1])
        with desc_col:
            _render_field("company_description")
        with btn_col:
            st.write("")  # alinea el boton con el text_area
            st.button("Buscar en Wikipedia", key="fetch_wikipedia_btn", width="stretch",
                      on_click=_fetch_description_callback,
                      help="Busca el nombre de la empresa en Wikipedia en espanol y trae el resumen del articulo.")
        wiki_error = st.session_state.get("_wikipedia_fetch_error")
        if wiki_error:
            st.warning(wiki_error)

        st.divider()
        st.markdown("#### Marco cualitativo")
        st.caption("Texto libre, con tu propio criterio -- no viene de ningun API. Se guarda junto con la "
                     "empresa (Guardar cambios, en la barra lateral).")
        qual_col1, qual_col2 = st.columns(2)
        with qual_col1:
            _render_field("qual_business_model")
            _render_field("qual_competitive_advantages")
            _render_field("qual_management_quality")
        with qual_col2:
            _render_field("qual_key_risks")
            _render_field("qual_growth_catalysts")

        st.divider()
        st.markdown("#### Datos estructurales")
        struct_df = pd.DataFrame({
            "Campo": ["Tipo de empresa (pesos del blend)", "Industria (US)", "Industria (Global)",
                      "Pais de incorporacion", "Capitaliza I+D", "Tiene leasing operativo",
                      "Tiene opciones para empleados"],
            "Valor": [inputs.company_type, inputs.industry_us, inputs.industry_global,
                      inputs.country_of_incorporation, "Si" if inputs.capitalize_rd else "No",
                      "Si" if inputs.has_operating_leases else "No",
                      "Si" if inputs.has_employee_options else "No"],
        }).set_index("Campo")
        st.dataframe(struct_df, width="stretch")


if __name__ == "__main__":
    main()
