#!/usr/bin/env python
"""Corre el pipeline de refresh_native_model.py para Grupo de Inversiones
Suramericana S.A. (BVC: PFGRUPOSURA), pero SIN pasar por SEC EDGAR (Grupo
Sura no presenta 10-K/10-Q en EE.UU. -- reporta IFRS a la Superintendencia
Financiera de Colombia). En vez de eso, este script arma a mano los mismos
objetos que ese pipeline espera (AnnualSeries/CompanyInputs/MarketSnapshot)
con los datos primarios ya investigados (EEFF consolidados IFRS de Grupo Sura
IR 4T2025/4T2024/2T2026, BVC, yfinance para precio/historico), y reusa las
funciones refresh_* de refresh_native_model.py tal cual (ninguna formula del
libro se toca).

Despues corre una segunda tanda de escrituras puntuales -- decisiones
metodologicas que el pipeline generico no cubre porque son especificas de
esta valoracion (riskfree COP, beta de industria via 'Single Business
(Global)', ERP de mercado maduro sin doble conteo de riesgo pais, tipo de
empresa "Financiera" para el precio objetivo ponderado, los 3 escenarios de
crecimiento/margen, y un parche de IFERROR en Input sheet!D1 porque
GOOGLEFINANCE no cubre la BVC -- ver docstring de `_patch_googlefinance_bvc`).

Uso:
    PYTHONPATH=. python scripts/run_pfgruposura.py
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

import refresh_native_model as rnm  # noqa: E402 (scripts/ ya esta en sys.path[0])

from jmr_valuation.io.inputs import CompanyInputs  # noqa: E402
from jmr_valuation.io.sec_edgar_loader import AnnualSeries  # noqa: E402
from jmr_valuation.io.sheets_auth import get_gspread_client, open_target_sheet  # noqa: E402
from jmr_valuation.io.yfinance_client import get_market_snapshot  # noqa: E402

TICKER = "PFGRUPOSURA"          # ticker "logico" que usa el libro (Input sheet!A1, Sector, etc.)
YF_TICKER = "PFGRUPSURA.CL"     # ticker real de yfinance (BVC, accion preferencial)
PEER_TICKERS = ["CIB", "AVAL", "BAP", "ITUB", "BCH"]
INDUSTRY = "Financial Svcs. (Non-bank & Insurance)"

_M = 1_000_000.0


def cop_m(value_millones: float) -> float:
    """Convierte COP millones (las unidades en las que vienen los datos de
    los EEFF) a COP crudos -- AnnualSeries espera $ crudos, igual que SEC
    EDGAR, porque refresh_native_model.py divide por _M=1e6 al escribir
    "$mm" en el Sheet (ver docstring de ese modulo)."""
    return value_millones * _M


# ---------------------------------------------------------------------------
# 1. AnnualSeries -- FY2023 / FY2024 (restated) / FY2025 + LTM jun-2026.
# Fuente: EEFF consolidados IFRS de Grupo Sura (Doc A 4T2025, Doc B 4T2024,
# Doc C interinos 2T2026), via Superintendencia Financiera / Grupo Sura IR.
# ---------------------------------------------------------------------------

FISCAL_YEAR_ENDS = ["2023-12-31", "2024-12-31", "2025-12-31"]

# Acciones en circulacion: el dato primario solo da el TOTAL (ambas clases)
# para 2023/2024, y el desglose preferencial/ordinaria exacto solo para
# dic-2025/jun-2026 (161.871.882 pref. de 327.705.908 total = 49,40%). Para
# mantener consistencia de UNA sola clase de accion como denominador en TODO
# el modelo (ver decision metodologica mas abajo y en la Tesis), se estima el
# conteo preferencial historico aplicando esa misma proporcion 49,40% a los
# totales de 2023/2024 -- una aproximacion razonable (las recompras de
# 2023-2024 no distinguieron entre clases en las fuentes revisadas), no un
# dato primario exacto. 2025 SI es el numero primario exacto.
_PREF_SHARE_OF_TOTAL = 161_871_882 / 327_705_908
SHARES_TOTAL_BY_YEAR = [579_228_875, 395_128_602, 327_705_908]
SHARES_PREF_BY_YEAR = [579_228_875 * _PREF_SHARE_OF_TOTAL, 395_128_602 * _PREF_SHARE_OF_TOTAL, 161_871_882]
SHARES_PREF_LTM = 161_871_882.0

ZERO3 = [0.0, 0.0, 0.0]

series = AnnualSeries(
    ticker=YF_TICKER,  # refresh_trailing_valuation pide precios historicos reales via yfinance con ESTE ticker (no el logico "PFGRUPOSURA")
    company_name="Grupo de Inversiones Suramericana S.A.",
    fiscal_year_ends=FISCAL_YEAR_ENDS,
    revenue=[cop_m(v) for v in (35_310_885, 36_326_664, 28_706_719)],
    ebit=[cop_m(v) for v in (4_561_151, 8_444_350, 4_375_267)],
    da=[cop_m(v) for v in (598_406, 543_834, 570_383)],
    shares_outstanding=SHARES_PREF_BY_YEAR,
    long_term_debt=[cop_m(v) for v in (6_791_435, 11_704_798, 9_299_809)],
    current_debt=[cop_m(v) for v in (2_992_827, 672_087, 1_750_149)],
    cash=[cop_m(v) for v in (3_305_577, 2_975_302, 2_686_482)],
    ltm_revenue=cop_m(30_760_744),
    ltm_ebit=cop_m(4_981_975),
    ltm_da=cop_m(571_465),
    # --- segunda tanda ---
    tax_expense=[cop_m(v) for v in (1_540_340, 1_178_583, 1_174_215)],
    net_income=[cop_m(v) for v in (1_539_582, 6_073_978, 1_841_118)],  # atribuible a la CONTROLADORA (ver Tesis, ajuste metodologico)
    diluted_shares_avg=SHARES_PREF_BY_YEAR,  # proxy: no hay promedio ponderado primario separado, se usa el puntual (ver Tesis)
    operating_cash_flow=[cop_m(v) for v in (1_430_411, 4_907_758, 4_065_145)],
    capex=[cop_m(v) for v in (161_785, 128_862, 119_780)],
    buybacks=ZERO3,  # dato pendiente: no se consiguio la linea de "recompra de acciones" del EECF como flujo anual limpio (ver Tesis)
    dividends_paid=[cop_m(v) for v in (669_174, 675_285, 604_761)],
    cogs=ZERO3,  # Grupo Sura no reporta costo de ventas tipo empresa operativa -- ver Tesis, ajuste metodologico
    ltm_tax_expense=cop_m(1_318_098),
    ltm_net_income=cop_m(2_301_023),
    ltm_diluted_shares_avg=SHARES_PREF_LTM,
    ltm_operating_cash_flow=cop_m(3_063_508),
    ltm_capex=cop_m(99_184),
    ltm_buybacks=0.0,
    ltm_dividends_paid=cop_m(604_542),
    ltm_cogs=0.0,
    rd=ZERO3, sga=ZERO3,
    pretax_income=[cop_m(v) for v in (3_514_949, 6_808_068, 2_992_253)],
    total_assets=[cop_m(v) for v in (93_504_778, 96_295_907, 93_145_510)],
    total_liabilities=[cop_m(v) for v in (61_069_540, 67_699_721, 71_577_449)],
    equity=[cop_m(v) for v in (32_435_238, 28_596_186, 21_568_061)],  # patrimonio TOTAL (incl. no controlante) -- se corrige el minoritario en la col. LTM aparte
    share_based_comp=ZERO3,
    investing_cash_flow=ZERO3,   # sin desglose primario limpio de inversion/financiacion mas alla de CapEx/dividendos/deuda (ver Tesis)
    financing_cash_flow=ZERO3,
    ltm_rd=0.0, ltm_sga=0.0,
    ltm_pretax_income=cop_m(3_625_710),
    ltm_share_based_comp=0.0,
    ltm_investing_cash_flow=0.0,
    ltm_financing_cash_flow=0.0,
    interest_expense=[cop_m(v) for v in (1_127_641, 1_452_007, 1_348_764)],
    ltm_interest_expense=cop_m(1_408_725),
    interest_investment_income=ZERO3,
    ltm_interest_investment_income=0.0,
    cf_receivables_change=ZERO3, cf_payables_change=ZERO3,
    cf_income_tax_payable_change=ZERO3, cf_unearned_revenue_change=ZERO3,
    purchases_of_investments=ZERO3, proceeds_from_investments=ZERO3,
    ltm_cf_receivables_change=0.0, ltm_cf_payables_change=0.0,
    ltm_cf_income_tax_payable_change=0.0, ltm_cf_unearned_revenue_change=0.0,
    ltm_purchases_of_investments=0.0, ltm_proceeds_from_investments=0.0,
)

# Balance al cierre mas reciente (jun-2026), MAS actualizado que dic-2025 --
# refresh_balance_sheet no tiene un mecanismo generico para esto (usa el
# ultimo anio de la serie anual como columna "LTM" de balance, ver docstring
# de refresh_native_model.py), asi que se corrige aparte despues de llamar a
# esa funcion (ver _override_balance_sheet_ltm_column mas abajo).
BALANCE_JUN2026 = dict(
    cash=cop_m(2_959_035),
    current_debt=cop_m(730_868),
    long_term_debt=cop_m(9_882_299),
    total_debt=cop_m(10_613_167),
    total_assets=cop_m(94_574_189),
    total_liabilities=cop_m(73_461_561),
    equity_total=cop_m(21_112_628),
    equity_controladora=cop_m(19_026_523),
    minority_interest=cop_m(21_112_628 - 19_026_523),
)


# ---------------------------------------------------------------------------
# 2. CompanyInputs -- LTM y "10-K" previo (FY2025), tal como lo pide el
# dataclass (unidades: COP MILLONES directo, sin multiplicar por 1e6 --
# `_to_millions` de sec_edgar_loader.py hace exactamente esa conversion para
# empresas de EDGAR, y estos datos primarios YA vienen en millones).
# ---------------------------------------------------------------------------

def build_company_inputs(current_price: float) -> CompanyInputs:
    ebit_margin_2023 = 4_561_151 / 35_310_885
    ebit_margin_2024 = 8_444_350 / 36_326_664
    ebit_margin_2025 = 4_375_267 / 28_706_719
    ebit_margin_3y_avg = (ebit_margin_2023 + ebit_margin_2024 + ebit_margin_2025) / 3

    return CompanyInputs(
        ticker=TICKER,
        company_name="Grupo de Inversiones Suramericana S.A.",
        country_of_incorporation="Colombia",
        industry_us=INDUSTRY,
        industry_global=INDUSTRY,
        revenue_ltm=30_760_744, revenue_prior_10k=28_706_719,
        years_since_last_10k=(date(2026, 9, 22) - date(2025, 12, 31)).days / 365.25,
        ebit_ltm=4_981_975, ebit_prior_10k=4_375_267,
        interest_expense_ltm=1_408_725, interest_expense_prior_10k=1_348_764,
        book_value_equity_ltm=BALANCE_JUN2026["equity_total"] / _M,
        book_value_equity_prior_10k=21_568_061,
        book_value_debt_ltm=BALANCE_JUN2026["total_debt"] / _M,
        book_value_debt_prior_10k=11_049_958,
        cash_ltm=BALANCE_JUN2026["cash"] / _M,
        cash_prior_10k=2_686_482,
        minority_interests=BALANCE_JUN2026["minority_interest"] / _M,
        shares_outstanding=161.871882,  # MM de acciones PREFERENCIALES (ver Tesis, ajuste metodologico de la doble clase)
        current_price=current_price,
        effective_tax_rate=0.3635,
        marginal_tax_rate=0.35,
        capitalize_rd=False, has_operating_leases=False, has_employee_options=False,
        revenue_growth_next_year=0.08, revenue_growth_years_2_to_5=0.06,
        target_ebit_margin=0.17, year_of_margin_convergence=5,
        sales_to_capital_years_1_5=1.1, sales_to_capital_years_6_10=1.3,
        ebit_margin_ltm=4_981_975 / 30_760_744,
        ebit_margin_avg_3y=ebit_margin_3y_avg,
        ebit_margin_avg_5y=ebit_margin_3y_avg,   # solo 3 anios de historico limpio disponibles -- ver Tesis
        ebit_margin_avg_10y=ebit_margin_3y_avg,
        riskfree_rate=0.12785, initial_cost_of_capital=0.16,
        company_type="Financiera", margin_of_safety=0.30,
        dividend_per_share_ltm=2000.0,
    )


# ---------------------------------------------------------------------------
# 3. Overrides puntuales que el pipeline generico no cubre (ver docstring del
# modulo). Cada funcion documenta la celda y la razon.
# ---------------------------------------------------------------------------

def _date_serial(d: date) -> int:
    return (d - date(1899, 12, 30)).days


def _override_input_sheet_assumptions(sh, riskfree_rate: float) -> None:
    ws = sh.worksheet("Input sheet")
    rnm._apply(ws, [
        ("B4", [[_date_serial(date(2026, 9, 22))]]),  # Fecha de analisis -- estaba en una fecha vieja de LULU
        ("B21", [[round(BALANCE_JUN2026["minority_interest"] / _M, 1)]]),  # Minority interests (literal, sin formula propia)
        ("B24", [[0.3635]]),   # Effective tax rate
        ("B25", [[0.35]]),     # Marginal tax rate
        ("B27", [[0.08]]),     # Revenue growth next year (Base)
        ("B28", [[0.16]]),     # Operating margin next year (Base)
        ("B29", [[0.06]]),     # CAGR revenue years 2-5 (Base)
        ("B30", [[0.17]]),     # Target pre-tax operating margin (Base)
        ("B31", [[5]]),        # Year of convergence for margin (compartido por los 3 escenarios)
        ("B32", [[1.1]]),      # Sales to capital years 1-5
        ("B33", [[1.3]]),      # Sales to capital years 6-10
        ("B35", [[riskfree_rate]]),  # Riskfree rate (COP, TES 10y)
        ("B38", [["No"]]),     # Employee options -- eran datos de LULU (1,525M opciones a strike 258,81), irrelevantes/incorrectos para Grupo Sura
        ("B68", [["Yes"]]),    # Override growth rate en perpetuidad
        ("B69", [[0.06]]),     # Crecimiento terminal COP nominal ~6% (inflacion objetivo BanRep ~3% + crecimiento real potencial ~3%) en vez del 12,785% (riskfree COP, el tope teorico de Damodaran pero muy agresivo como "g" real) o del 3% heredado de LULU (calibrado en USD, muy bajo para COP nominal)
    ])


def _patch_googlefinance_bvc(sh, fallback_price: float) -> None:
    """GOOGLEFINANCE no cubre la Bolsa de Valores de Colombia -- confirmado
    en vivo: `=GOOGLEFINANCE("PFGRUPOSURA";"price")` devuelve
    '#N/A ... returned no data'. Sin este parche, Input sheet!D1 (y todo lo
    que depende de el: B23/B24 de esta misma hoja, 'Resumen de
    Valoración'!B3/B24 y las filas 13-14/16-19/26 que dependen de B3,
    'Valuation output'!B36/B87/B138 en los 3 escenarios, y 'Presentación')
    quedarian en #N/A -- rompiendo la mayor parte de la salida visible del
    modelo. Se cambia D1 a un IFERROR con fallback a una celda estatica
    (G1) que este script actualiza con el precio real de yfinance en cada
    corrida -- el UNICO cambio de formula de todo este trabajo, y solo
    porque sin el la mitad del libro queda inutilizable para un ticker BVC."""
    ws = sh.worksheet("Input sheet")
    rnm._apply(ws, [
        ("F1", [["Fallback BVC (GOOGLEFINANCE no cubre la Bolsa de Colombia):"]]),
        ("G1", [[round(fallback_price, 2)]]),
        ("D1", [['=IFERROR(GOOGLEFINANCE(REGEXEXTRACT(A1;"\\(.*?:(.*?)\\)");"price");G1)']]),
    ])


def _override_balance_sheet_ltm_column(sh) -> None:
    """Corrige la columna L (LTM) de 'Balance Sheet' al cierre real mas
    reciente (jun-2026, interinos 2T2026) en vez del cierre de FY2025 que
    refresh_balance_sheet usa por defecto como proxy de LTM para items de
    balance (ver docstring de refresh_native_model.py: esa funcion no tiene
    un campo `ltm_*` propio para deuda/equity/activos, a diferencia de
    Income Statement/Cash Flow Statement que si lo tienen). Tambien separa
    patrimonio controladora (fila 34) de patrimonio total incl. interes
    minoritario (fila 35) -- Grupo Sura SI tiene interes minoritario
    material (~$2,09 billones jun-2026, subsidiarias de seguros/AM no
    100% propias), a diferencia del supuesto de "minoritario nulo" que
    refresh_balance_sheet usa por defecto para la mayoria de empresas."""
    ws = sh.worksheet("Balance Sheet")
    b = BALANCE_JUN2026
    rnm._apply(ws, [
        ("L20", [[round(b["current_debt"] / _M, 1)]]),
        ("L25", [[round(b["long_term_debt"] / _M, 1)]]),
        ("L16", [[round(b["total_assets"] / _M, 1)]]),
        ("L36", [[round(b["total_assets"] / _M, 1)]]),
        ("L29", [[round(b["total_liabilities"] / _M, 1)]]),
        ("L34", [[round(b["equity_controladora"] / _M, 1)]]),
        ("L35", [[round(b["equity_total"] / _M, 1)]]),
    ])


def _override_cost_of_capital(sh, mature_erp: float) -> None:
    """Ver metodologia de WACC en la Tesis: beta de industria (no la beta de
    regresion directa de la accion, muy dispersa/distorsionada por eventos
    idiosincraticos 2024-2025), ERP de SOLO mercado maduro (la tasa libre de
    riesgo ya esta en COP, que ya incorpora el riesgo pais/inflacionario de
    Colombia -- sumar tambien el country risk premium seria contarlo dos
    veces), y costo de deuda pre-tax implicito real (Gastos financieros LTM
    / Deuda financiera total LTM) en vez del 6% heredado de LULU (una tasa
    en USD, muy por debajo de la tasa libre de riesgo en COP -- hubiera
    dejado el costo de deuda por debajo del activo libre de riesgo, un
    resultado sin sentido economico)."""
    ws = sh.worksheet("Cost of capital worksheet")
    implied_pretax_cost_of_debt = 1_408_725 / BALANCE_JUN2026["total_debt"] * _M  # gastos financieros LTM / deuda financiera total LTM
    rnm._apply(ws, [
        ("B22", [["Single Business(Global)"]]),  # Approach for estimating beta
        ("B26", [["Will Input"]]),                # ERP approach
        ("B27", [[mature_erp]]),                  # ERP de mercado maduro (reference/mature_market_erp.txt)
        ("B34", [["Direct Input"]]),               # Pre-tax cost of debt approach
        ("B35", [[round(implied_pretax_cost_of_debt, 4)]]),
    ])


def _clear_relative_valuation_multiple_overrides(sh) -> None:
    """PE/POCF/PFCFE/EVFCFF/EVEBITDA (celda J8/J19/J30 de cada una, para
    Conservador/Base/Optimista) traian multiplos de salida pegados a mano
    de lululemon (p.ej. P/E 10x/15x/20x, EV/EBITDA 6x/8x/11x) -- ajenos por
    completo al perfil de Grupo Sura. Se limpian (celda vacia) para que cada
    hoja caiga a su propio fallback ya presente en la formula
    (IF(J8<>"";J8;'Valuation output'!B82/F9) -- el multiplo IMPLICITO en el
    propio DCF de este modelo, aplicado hacia adelante), en vez de dejar un
    numero de otra empresa o inventar uno nuevo sin sustento. EV/EBITDA y
    EV/FCFF quedan con 0% de ponderacion en el precio objetivo para el tipo
    "Financiera" (ver Tesis), asi que este fix no cambia el resultado final
    para esas dos, pero se limpian igual por prolijidad."""
    for name in ("PE", "POCF", "PFCFE", "EVFCFF", "EVEBITDA"):
        ws = sh.worksheet(name)
        rnm._apply(ws, [("J8", [[""]]), ("J19", [[""]]), ("J30", [[""]])])


def _fix_optimista_equity_value_off_by_one(sh) -> None:
    """Bug pre-existente de la plantilla (no introducido por este script,
    y no especifico de Grupo Sura -- afecta a cualquier empresa que use el
    bloque Optimista de PE/PFCFE/POCF sin un multiplo J30 pegado a mano):
    la formula de respaldo del multiplo NTM del bloque OPTIMISTA
    (F30 = IF(J30<>"";J30;'Valuation output'!B132/F31)) apunta a
    'Valuation output'!B132 (" + Non-operating assets", que vale 0 en la
    inmensa mayoria de los casos -- Grupo Sura incluido, ver Tesis) en vez
    de B133 ("Value of equity in common stock"), la fila que SI usan los
    bloques Conservador (B82) y Base (B31) de forma consistente. Con
    B132=0 el multiplo por defecto daba 0, y todo el bloque Optimista de
    esas 3 hojas (Implied Target Price, Total Return, etc.) colapsaba a 0
    -- confirmado en vivo: sin este fix, el escenario "Optimista" del
    precio objetivo ponderado salia MAS BAJO que el Base, algo imposible.
    Se corrige la referencia en las 3 hojas donde la ponderacion
    "Financiera" SI usa este bloque (PE/PFCFE/POCF); EVFCFF/EVEBITDA usan
    la fila correcta (B128, "Value of operating assets") y no tienen el bug."""
    for name in ("PE", "PFCFE", "POCF"):
        ws = sh.worksheet(name)
        rnm._apply(ws, [("F30", [['=IF(J30<>"";J30;\'Valuation output\'!B133/F31)']])])


def _override_resumen_tipo_empresa(sh) -> None:
    ws = sh.worksheet("Resumen de Valoración")
    rnm._apply(ws, [("G3", [["Financiera"]])])


def _override_valuation_output_scenarios(sh) -> None:
    """'Valuation output' NO deriva Conservador/Optimista de deltas sobre el
    Base (a diferencia de lo que CompanyInputs.conservative_growth_delta
    sugeriria) -- son bloques de celdas LITERALES independientes (confirmado
    leyendo la hoja en vivo: traian los supuestos pegados a mano de LULU,
    p.ej. crecimiento -10%/0%/0%/0%/0% para el conservador). Se reemplazan
    esos literales por los supuestos de Grupo Sura (ver Tesis, seccion 2,
    para la justificacion dato-a-dato de cada numero)."""
    ws = sh.worksheet("Valuation output")
    rnm._apply(ws, [
        # Conservador: fila 55 (crecimiento), fila 57 (margen año 1), C45 (margen objetivo)
        ("C55", [[0.02]]), ("D55:G55", [[0.03, 0.03, 0.03, 0.03]]),
        ("C57", [[0.13]]), ("C45", [[0.14]]),
        # Optimista: fila 106 (crecimiento), fila 108 (margen año 1), C47 (margen objetivo)
        ("C106", [[0.12]]), ("D106:G106", [[0.08, 0.08, 0.08, 0.08]]),
        ("C108", [[0.18]]), ("C47", [[0.19]]),
    ])


def _fix_sector_own_market_cap(sh, market) -> None:
    """El 'marketCap' que devuelve yfinance para PFGRUPSURA.CL esta mal
    calculado (da ~2x lo que corresponde -- probablemente mezcla ambas
    clases de accion, ver investigacion previa) -- se corrige la fila propia
    (fila 2) de 'Sector' con el valor real (acciones preferenciales x
    precio). Los multiplos EV/FCF y EV/EBITDA de esa misma fila pueden
    arrastrar el mismo problema (enterpriseValue de yfinance tambien
    resulto no confiable para este ticker) pero no se corrigen: con
    'Resumen de Valoración'!G3="Financiera" ambos multiplos ya reciben 0%
    de ponderacion en el precio objetivo final, asi que no afectan el
    resultado -- son solo referencia visual en la tabla de comparables."""
    ws = sh.worksheet("Sector")
    rnm._apply(ws, [("C2", [[round(161_871_882 * market.current_price / _M, 2)]])])


def _patch_short_history_baseline(sh) -> None:
    """Grupo Sura solo tiene 3 años de historico limpio (2023-2025), no los
    10 que espera la plantilla -- refresh_period_headers ya maneja el
    RÓTULO de las columnas B-H vacias (las rellena con "—"), pero los
    VALORES de esas columnas en Income Statement quedan realmente en blanco
    (ver _history_row). 'Financials Multiples' (hoja de formulas, no
    tocada por ningun refresh_*) calcula el "% Change YoY" del PRIMER año
    disponible (columna I, 2023) contra la columna INMEDIATAMENTE anterior
    (H, "2022") -- con H en blanco, ese %change es 0/0 (#DIV/0!), y ese
    error se propagaba via MEDIAN() hacia la proyeccion de "Diluted Shares
    Outstanding" (fila 31) de las 5 hojas de multiplos relativos (PE, POCF,
    PFCFE, EVFCFF, EVEBITDA), y de ahi al precio objetivo ponderado
    ('Resumen de Valoración'!D12, que daba #DIV/0! antes de este fix).

    Se "rellena" la columna H de Income Statement (Revenue/EBIT/Net
    Income/EPS/Acciones diluidas, filas 3/12/21/24/26) con el valor de la
    columna I (2023) DESCONTADO a un 5% de crecimiento generico asumido
    (no el 0% mas "neutral" que parece obvio a primera vista -- se probo
    con H = I exacto y eso ROMPE 'Financials Multiples' fila 22 (Cambio en
    NWC proyectado), que divide entre "Revenue(2023) - Income
    Statement!H3": con H3 = I3 exacto ese denominador da CERO -- un
    #DIV/0! nuevo en vez del original. Con un 5% generico el denominador
    nunca es exactamente cero, sin inventar una tendencia real de un año
    (2022) del que no hay dato primario)."""
    ws = sh.worksheet("Income Statement")
    vals = ws.get("I3:I26", value_render_option="UNFORMATTED_VALUE")
    i3, i12, i21, i24, i26 = vals[0][0], vals[9][0], vals[18][0], vals[21][0], vals[23][0]
    g = 1.05
    rnm._apply(ws, [
        ("H3", [[i3 / g]]), ("H12", [[i12 / g]]), ("H21", [[i21 / g]]),
        ("H24", [[i24 / g]]), ("H26", [[i26 / g]]),
    ])


def write_tesis_sheet(sh, *, price: float, wacc: float, conservador: float, base: float, optimista: float) -> None:
    """Reemplaza todo el contenido de lululemon en 'Tesis de Inversión y
    Supuestos' por el analisis de Grupo Sura, siguiendo la MISMA estructura
    de la plantilla (5 secciones, bull/bear, tabla de supuestos por
    escenario, resultado del DCF, ajustes metodologicos, conclusion)."""
    ws = sh.worksheet("Tesis de Inversión y Supuestos")
    ws.batch_clear(["A1:H50"])  # limpia el contenido de lululemon antes de escribir el de Grupo Sura (mismo motivo que Cualitativo)
    up_cons = (conservador / price - 1) * 100
    up_base = (base / price - 1) * 100
    up_opt = (optimista / price - 1) * 100

    rows: list[tuple[str, list]] = [
        ("A1", [["GRUPO DE INVERSIONES SURAMERICANA S.A. (PFGRUPOSURA) — Tesis de Inversión: De la Historia a los Números"]]),
        ("A2", [[f"Metodología Damodaran (NYU Stern) | Precio al día del análisis: {price:,.0f} COP (22-sept-2026) | WACC: {wacc:.2%}"]]),
        ("A4", [["1. LA HISTORIA"]]),
        ("A5", [[
            "Grupo Sura es el mayor holding financiero de Colombia: controla Seguros Suramericana, tiene participación "
            "mayoritaria en SURA Asset Management (pensiones/ahorro en 6 países de LatAm) y sostiene la participación "
            "estratégica histórica del Grupo Empresarial Antioqueño en Bancolombia/Grupo Cibest, además de una "
            "participación cruzada en Grupo Argos. 2024-2025 fue el período de mayor reestructuración societaria de su "
            "historia: perdió el control de EPS Suramericana (salud) en jun-2024 (deconsolidación que explica la caída "
            "de ingresos consolidados de $36,3 billones en 2024 a $28,7 billones en 2025 — no es una contracción del "
            "negocio, es un cambio de perímetro contable), ejecutó una escisión de activos no corrientes hacia sus "
            "accionistas en 2025 (~$6,6 billones), recompró casi la mitad de sus acciones en circulación (de 579 "
            "millones en dic-2023 a 328 millones en dic-2025), y en mar-2026 eligió por primera vez en 40+ años una "
            "Junta Directiva sin representación de Grupo Argos (5 de 7 miembros independientes). El resultado: una "
            "holding más simple, más enfocada en seguros y gestión de activos, con ROE en máximos históricos (16,5% "
            "LTM vs. 7,9% hace 5 años) y utilidad neta controladora 1S2026 de $1,7 billones (+37,7% interanual, con un "
            "2T2026 aislado de $1,2 billones, +67%, récord trimestral). La tensión central: ¿el mercado todavía valora "
            "a Sura como el conglomerado opaco y sobre-apalancado de 2023-2024 (la acción cotiza a un P/E LTM de apenas "
            "~4x), o ya empezó a reconocer la simplificación societaria, el récord de rentabilidad y el plan explícito "
            "de desapalancamiento (reducir deuda neta individual ~20% en 2026, de $7,1 a ~$5,7 billones, usando ~$3 "
            "billones de dividendos de sus participadas)? Persisten riesgos reales: S&P bajó la calificación a 'BB' en "
            "mar-2025 citando lentitud en el desapalancamiento post-escisión de Argos, agravada por un pasivo "
            "tributario extraordinario de ~US$171M de la venta de Nutresa en 2024; Fitch, en cambio, reafirmó "
            "'BB+'/'AAA(col)' con perspectiva estable en mar-2026.",
        ]]),
        ("A7", [["Caso alcista (Bull)", "Caso bajista (Bear)"]]),
        ("A8", [[
            "ROE en máximo histórico (16,5% LTM vs. 7,9% hace 5 años) y guidance oficial de la compañía para 2026 de "
            "ROE ajustado 15-16% y utilidad neta $2,5-2,7 billones (vs. $1,84 billones en 2025) — la rentabilidad "
            "estructural del negocio ya mejoró, no es una promesa a futuro.",
            "Calificación crediticia bajo presión: S&P bajó a 'BB' en mar-2025 por lentitud en el desapalancamiento "
            "post-escisión de Argos, con un pasivo tributario extraordinario de ~US$171M (venta Nutresa 2024) como "
            "presión adicional de liquidez sobre la matriz individual.",
        ]]),
        ("A9", [[
            "Holding simplificado y más transparente: sin el lastre de EPS Suramericana (salud, deconsolidada 2024), "
            "con recompras que redujeron el conteo de acciones casi a la mitad (579M→328M) y, desde mar-2026, "
            "gobierno corporativo más independiente (Junta sin representación de Grupo Argos por primera vez en 40+ "
            "años) — menos descuento por complejidad/conflicto de interés de holding cruzado del GEA.",
            "Deuda financiera total se mantiene elevada en términos absolutos ($10,6 billones jun-2026, aunque bajando "
            "desde $12,4 billones en dic-2024) y depende de que los dividendos de las participadas (Bancolombia/"
            "Cibest, Suramericana, SURA AM — ~$3 billones esperados en 2026) efectivamente lleguen a la matriz "
            "individual para cumplir el plan de desapalancamiento; un recorte de dividendos de cualquiera de ellas "
            "retrasaría el plan.",
        ]]),
        ("A10", [[
            "Múltiplo de entrada muy bajo en términos históricos: P/E LTM implícito de ~4x (con ROE de 16,5%) sugiere "
            "que el mercado aún no ha re-tasado la acción tras la simplificación societaria — el spin-off de Argos, la "
            "venta de la participación en Banistmo por Grupo Cibest (~USD 1.400M, culminada en el semestre) y el pago "
            "de bonos internacionales por USD 300M en abr-2026 (reemplazados por deuda bancaria local a 5 años) son "
            "catalizadores recientes que el precio podría no reflejar todavía.",
            "El valor de Grupo Sura depende en gran medida de negocios que NO controla al 100% (Bancolombia/Cibest, "
            "Grupo Argos) y de un DCF de flujo de caja libre a la firma que tiene limitaciones conocidas para "
            "instituciones financieras (ver Sección 4) — el modelo pondera esto reduciendo el peso del DCF FCFF, pero "
            "sigue siendo una limitación real de cualquier valoración de un holding financiero con este método.",
        ]]),
        ("A11", [[
            "Dividendo 2026 aprobado de $2.000/acción (+33,3% vs. 2025, ambas clases), con dividend yield preferencial "
            "de ~3,5% al precio actual — señal de confianza de la administración en la generación de caja sostenible "
            "post-reestructuración.",
            "Concentración regulatoria/país: la totalidad del negocio de seguros y una porción mayoritaria de la "
            "gestión de activos están en Colombia y la región andina — expuesto a riesgo político/regulatorio local y "
            "a la volatilidad del peso colombiano, sin la diversificación geográfica de un múltiplo global.",
        ]]),
        ("A13", [["2. DE LA HISTORIA A LOS NÚMEROS — LOS TRES ESCENARIOS"]]),
        ("A14", [["Supuesto", "Conservador", "Base", "Optimista", "Justificación (dato real)"]]),
        ("A15", [[
            "Crecimiento Ingresos — Año 1", "2,0%", "8,0%", "12,0%",
            "Base = extrapola la recuperación YA REALIZADA (ingresos LTM jun-2026 de $30,76 billones ya crecen "
            "+7,1% vs. FY2025, $28,71 billones, con el negocio ya estabilizado post-deconsolidación de EPS "
            "Suramericana). Conservador = el desapalancamiento se estanca, los dividendos de participadas no llegan "
            "al ritmo esperado y el crecimiento orgánico de seguros/AM se frena. Optimista = la utilidad neta "
            "controladora 1S2026 (+37,7% interanual, 2T2026 aislado +67%) se sostiene y el ingreso consolidado "
            "acelera junto con ella.",
        ]]),
        ("A16", [[
            "Crecimiento Ingresos — Años 2-5", "3,0%", "6,0%", "8,0%",
            "Base converge a un crecimiento nominal COP de mediano plazo razonable para una holding de "
            "seguros/gestión de activos ya madura (por encima de la inflación objetivo de ~3% del Banco de la "
            "República, sin asumir una repetición del crecimiento de doble dígito excepcional de 1S2026).",
        ]]),
        ("A17", [[
            "Margen Operativo — Año 1", "13,0%", "16,0%", "18,0%",
            "Base ≈ margen operativo LTM real (16,20% = EBIT LTM $4.981.975M / Ingresos LTM $30.760.744M), ya "
            "recuperado del mínimo de 2025 (15,24%, año de la deconsolidación) pero por debajo del pico de 2024 "
            "restated (23,25%, inflado por una ganancia no recurrente de la venta/deconsolidación de EPS "
            "Suramericana — no representativo del margen operativo recurrente, ver Sección 4).",
        ]]),
        ("A18", [[
            "Margen Objetivo (convergencia)", "14,0%", "17,0%", "19,0%",
            "Base = modesta expansión sobre el margen LTM, consistente con el plan de reducir deuda neta individual "
            "~20% en 2026 (menor gasto financiero futuro) y el guidance oficial de ROE ajustado 15-16% para 2026. "
            "Conservador = el margen se estanca en el nivel más débil reciente (FY2025, 15,24%, redondeado). "
            "Optimista = mejora adicional si el desapalancamiento se completa antes de lo previsto.",
        ]]),
        ("A19", [[
            "Años de convergencia de margen", "5", "5", "5",
            "Horizonte estándar de Damodaran para una empresa que ya no está en una crisis aguda (a diferencia de "
            "una turnaround story) pero sí en transición activa de estructura de capital -- ni tan rápido como una "
            "empresa estable (3 años) ni tan lento como una crisis profunda (6+ años).",
        ]]),
        ("A20", [[
            "Sales-to-Capital (años 1-5 / 6-10)", "1,1x / 1,3x", "1,1x / 1,3x", "1,1x / 1,3x",
            "Calculado directo de los datos primarios: Ingresos LTM ($30.760.744M) / Capital Invertido ($21.112.628M "
            "patrimonio + $10.613.167M deuda financiera − $2.959.035M caja = $28.766.760M) ≈ 1,07x. Es un ratio "
            "conceptualmente limitado para una holding financiera (Damodaran lo diseñó para empresas industriales con "
            "CapEx físico real -- el CapEx LTM de Sura es de apenas $99.184M, 0,3% de los ingresos, porque el "
            "'capital' de un asegurador es principalmente reservas técnicas y capital regulatorio, no plantas ni "
            "equipos) -- se usa igual por consistencia con la plantilla, pero es la razón principal por la que el DCF "
            "FCFF recibe menos peso en el precio objetivo ponderado (ver Sección 4).",
        ]]),
        ("A21", [[
            "Costo de Capital (WACC)", f"{wacc:.2%}", f"{wacc:.2%}", f"{wacc:.2%}",
            "Tasa libre de riesgo TES 10 años Colombia (12,785%, en COP nominal) + beta de industria 'Financial Svcs. "
            "(Non-bank & Insurance)' (Single Business Global, β desapalancada 0,295, reapalancada a la estructura de "
            "capital real de Sura ≈0,38) × ERP de SOLO mercado maduro (4,23%) — ver Sección 4 para la justificación "
            "completa de por qué no se suma también el riesgo país de Colombia. Costo de deuda pre-tax = tasa "
            "implícita real (Gastos financieros LTM $1.408.725M / Deuda financiera total LTM $10.613.167M ≈ 13,27%).",
        ]]),
        ("A23", [["3. RESULTADO DEL DCF POR ESCENARIO (precio objetivo ponderado, no solo DCF puro)"]]),
        ("A24", [["Escenario", "Precio Objetivo Ponderado", f"vs. Precio Actual ({price:,.0f} COP)", "Potencial (%)"]]),
        ("A25", [["Conservador", f"{conservador:,.0f} COP", f"{conservador - price:,.0f} COP", f"{up_cons:.1f}%"]]),
        ("A26", [["Base", f"{base:,.0f} COP", f"{base - price:,.0f} COP", f"{up_base:.1f}%"]]),
        ("A27", [["Optimista", f"{optimista:,.0f} COP", f"{optimista - price:,.0f} COP", f"{up_opt:.1f}%"]]),
        ("A28", [[
            "*Precio Objetivo Ponderado (categoría 'Financiera'): DCF Damodaran 40%, P/E 35%, P/FCFE 20%, P/OCF 5%, "
            "EV/EBITDA 0%, EV/FCFF 0%. Los múltiplos NTM de salida de cada escenario (P/E, P/FCFE, P/OCF) NO usan un "
            "múltiplo de mercado externo fijo -- caen al múltiplo IMPLÍCITO en el propio DCF de este modelo aplicado "
            "hacia adelante (celdas J8/J19/J30 de cada hoja dejadas en blanco a propósito, ver Sección 4), lo que "
            "explica que el precio ponderado quede por encima del DCF puro (que ya de por sí sugiere una acción muy "
            "barata frente a su historia: P/E LTM implícito de solo ~4x con ROE de 16,5%).",
        ]]),
        ("A30", [["4. AJUSTES METODOLÓGICOS APLICADOS PARA GRUPO SURA"]]),
        ("A31", [["#", "Ajuste", "Razón"]]),
        ("A32", [[1,
            "Tasa libre de riesgo en COP (TES 10 años, 12,785%, Investing.com 21-sept-2026) + ERP de SOLO mercado "
            "maduro (4,23%), SIN sumar además el country risk premium completo de Colombia (7,08%, hoja 'Country "
            "equity risk premiums').",
            "Enfoque estándar de Damodaran para valoraciones en moneda local con tasa libre de riesgo local: la TES "
            "colombiana YA cotiza con una prima sobre el Treasury de EE.UU. que compensa el riesgo soberano/"
            "inflacionario de Colombia -- sumar también el country risk premium sobre el ERP contaría ese mismo "
            "riesgo DOS VECES.",
        ]]),
        ("A33", [[2,
            "Beta de industria 'Financial Svcs. (Non-bank & Insurance)' (Single Business Global, β desapalancada "
            "0,295) en vez de la beta de regresión directa de la acción.",
            "La beta de mercado de PFGRUPSURA resultó muy dispersa según la fuente consultada (entre -0,16 y 0,99) -- "
            "probablemente distorsionada por los eventos idiosincráticos de 2024-2025 (escisión de Grupo Argos, "
            "venta de la participación en Nutresa, recompras masivas) que desacoplaron temporalmente el precio del "
            "mercado general, no por un riesgo estructural genuinamente bajo. El beta de industria, reapalancado a la "
            "estructura de capital real de Sura, da una estimación mucho más estable y defendible.",
        ]]),
        ("A34", [[3,
            "Tipo de empresa = 'Financiera' en el precio objetivo ponderado (40% DCF, 35% P/E, 20% P/FCFE, 5% P/OCF, "
            "0% EV/EBITDA, 0% EV/FCFF).",
            "El propio Damodaran documenta que el DCF de flujo de caja libre a la firma (FCFF) tiene limitaciones "
            "conocidas para instituciones financieras: el CapEx y el 'sales-to-capital ratio' no capturan bien cómo "
            "una aseguradora/gestora de activos genera y reinvierte capital (ver Sección 2, supuesto de "
            "sales-to-capital); P/E y P/FCFE son más apropiados porque el apalancamiento es parte integral -- no "
            "accesoria -- del modelo de negocio financiero, y EV/EBITDA/EV/FCFF pierden sentido cuando gran parte del "
            "balance es reservas técnicas y no deuda operativa.",
        ]]),
        ("A35", [[4,
            "GOOGLEFINANCE no cubre la Bolsa de Valores de Colombia (confirmado en vivo: "
            "GOOGLEFINANCE('PFGRUPOSURA';'price') devuelve error 'returned no data') -- se agregó un IFERROR con "
            "respaldo a un precio estático (yfinance, actualizado en cada corrida) en 'Input sheet'!D1.",
            "Sin este parche, la mitad del libro (Resumen de Valoración, las 3 columnas de escenario de Valuation "
            "output, Presentación) hubiera quedado en #N/A -- es el único cambio de fórmula de toda esta adaptación, "
            "y solo porque Google Finance no tiene datos de la BVC.",
        ]]),
        ("A36", [[5,
            "Denominador de acciones = SOLO las acciones PREFERENCIALES en circulación (161.871.882, jun-2026) en "
            "TODO el modelo (Input sheet, Cost of Capital, Income Statement, DCF) -- no el total de ambas clases "
            "(327.705.908).",
            "Grupo Sura tiene doble clase de acciones (ordinaria con voto + preferencial sin voto) y este ticker "
            "(PFGRUPOSURA) es la preferencial. Ambas clases reciben el mismo dividendo ($2.000/acción en 2026), un "
            "supuesto razonable de valor económico equivalente por acción -- se eligió la preferencial como "
            "denominador único para que el precio objetivo resultante sea directamente comparable al precio de "
            "mercado de ESTE ticker. Consecuencia importante: el EPS y el FCFE por acción que muestra este modelo NO "
            "coinciden con el EPS oficialmente reportado por la compañía (que usa acciones promedio ponderadas de "
            "AMBAS clases, ~2 a 2,7x más acciones) -- son ~2x más altos aquí por construcción, no por un error de "
            "cálculo.",
        ]]),
        ("A37", [[6,
            "Reexpresión de 2024: los ingresos ($36,3 billones) y el margen operativo (23,25%) de FY2024 restated "
            "están inflados por la deconsolidación de EPS Suramericana (salud, jun-2024) y no se usan como año base "
            "ni como referencia de margen 'normal' en ningún supuesto del escenario Base/Conservador/Optimista.",
            "Usar el margen de 2024 como ancla hubiera sobreestimado sistemáticamente la rentabilidad recurrente de "
            "la nueva Sura (post-escisión de activos hacia accionistas en 2025 y salida de Grupo Argos de la Junta "
            "en 2026) -- el Año 1 y el margen objetivo de los 3 escenarios se anclan en cambio al margen LTM real "
            "(16,20%) y al guidance oficial de la compañía para 2026.",
        ]]),
        ("A38", [[7,
            "Costo de deuda pre-tax = tasa implícita real (Gastos financieros LTM / Deuda financiera total LTM ≈ "
            "13,27%) vía 'Direct Input', en vez del 6% heredado de la corrida anterior (lululemon, una tasa en USD).",
            "Con la tasa libre de riesgo en COP al 12,785%, dejar el costo de deuda pre-tax heredado en 6% hubiera "
            "puesto el costo de deuda POR DEBAJO del activo libre de riesgo -- un resultado sin sentido económico.",
        ]]),
        ("A39", [[8,
            "Crecimiento terminal en perpetuidad = 6% nominal COP (override manual en 'Input sheet'!B68/B69), en vez "
            "del 12,785% (la tasa libre de riesgo COP completa, el tope teórico de Damodaran pero muy agresivo como "
            "'g' real de largo plazo) o del 3% heredado de la corrida anterior (calibrado en USD, muy bajo para COP "
            "nominal).",
            "6% nominal COP ≈ inflación objetivo de largo plazo del Banco de la República (~3%) + crecimiento real "
            "potencial de la economía colombiana (~3%) -- un ancla más realista que cualquiera de los dos extremos "
            "disponibles por defecto en la plantilla.",
        ]]),
        ("A40", [[9,
            "Interés minoritario material: se corrigió 'Input sheet'!B21 (Minority interests, $2.086.105M jun-2026) "
            "y se diferenció el patrimonio atribuible a la controladora ($19.026.523M) del patrimonio total "
            "($21.112.628M) en 'Balance Sheet', en vez del supuesto por defecto de 'interés minoritario nulo' que "
            "usa la plantilla para la mayoría de empresas.",
            "Las subsidiarias de seguros y gestión de activos de Sura no son 100% propias -- ignorar el interés "
            "minoritario hubiera sobreestimado el valor de equity atribuible a los accionistas de Sura en el puente "
            "de Enterprise Value a Equity Value del DCF.",
        ]]),
        ("A41", [[10,
            "Limitaciones de datos documentadas y NO subsanadas por falta de una fuente primaria limpia: (a) "
            "recompra de acciones anual como línea de flujo de caja separada (se usó $0, aunque el conteo de "
            "acciones sí cayó de 579M a 328M entre 2023 y 2025 -- el efecto SÍ está reflejado en el denominador de "
            "acciones, no en la línea de 'Recompras' del Cash Flow Statement); (b) desglose de Flujo de "
            "Inversión/Financiación más allá de CapEx, dividendos y cambio en deuda de largo plazo; (c) Costo de "
            "Ventas/SG&A por función (Sura reporta primas, siniestros y comisiones de seguros, no un P&L de empresa "
            "operativa tradicional -- se usó COGS=SG&A=0 y 'Other Opex' absorbe la diferencia real contra el EBIT "
            "real); (d) acciones preferenciales históricas de 2023/2024 estimadas por proporción (49,4% del total), "
            "no dato primario exacto -- solo dic-2025/jun-2026 son cifras primarias.",
            "Documentado para transparencia -- ninguna de estas aproximaciones afecta el EBIT, Net Income, OCF, "
            "CapEx, dividendos ni el balance histórico REAL usados en el DCF (todos con fuente primaria exacta); "
            "afectan solo el desglose fino de líneas secundarias del Cash Flow Statement y la serie histórica de "
            "acciones de años que no son la base del WACC ni del año 1 de proyección.",
        ]]),
        ("A44", [["5. CONCLUSIÓN"]]),
        ("A45", [[
            f"Al precio de análisis de {price:,.0f} COP (PFGRUPOSURA, 22-sept-2026), el modelo arroja un precio "
            f"objetivo ponderado Base de {base:,.0f} COP (+{up_base:.0f}%), con un rango Conservador-Optimista de "
            f"{conservador:,.0f} a {optimista:,.0f} COP ({up_cons:+.0f}% a {up_opt:+.0f}%). El WACC de {wacc:.1%} "
            "sobre un P/E LTM implícito de apenas ~4x (con ROE de 16,5%) sugiere una acción significativamente "
            "barata frente a su propia historia de rentabilidad -- consistente con una compañía que atravesó una "
            "reestructuración societaria profunda (deconsolidación de EPS Suramericana, escisión de activos hacia "
            "accionistas, recompras masivas, salida de Grupo Argos de la Junta) cuyo mercado todavía puede no haber "
            "terminado de re-tasar. El resultado es sensible a supuestos genuinamente inciertos: el ritmo real del "
            "plan de desapalancamiento 2026 (~$3 billones de dividendos de participadas necesarios), la sostenibilidad "
            "del ROE récord (16,5% LTM) frente al guidance oficial más conservador (15-16% ROE ajustado), y el "
            "destino de la calificación crediticia (Fitch 'BB+' estable vs. S&P 'BB' con presión). El margen de "
            "seguridad (35%) y el peso relativamente bajo asignado al DCF FCFF puro (40%, con más peso en P/E y "
            "P/FCFE, ver Sección 4) buscan compensar -- no eliminar -- esa incertidumbre. Deben vigilarse: el "
            "cumplimiento del plan de desapalancamiento individual, los dividendos efectivamente recibidos de "
            "Bancolombia/Cibest y Grupo Argos, la evolución de la calificación crediticia, y el margen operativo "
            "reportado trimestre a trimestre contra el guidance 2026 ($2,5-2,7 billones de utilidad neta).",
        ]]),
        ("A46", [[
            "Fuentes principales: EEFF consolidados IFRS de Grupo Sura (4T2025, 4T2024, interinos 2T2026) vía "
            "Superintendencia Financiera de Colombia / Grupo Sura IR; gruposura.com/en/shares/ (acciones en "
            "circulación); BVC / La República (precio, 22-sept-2026); yfinance (PFGRUPSURA.CL, precio e histórico); "
            "Investing.com (TES 10 años Colombia, 21-sept-2026); NYU Stern/Damodaran (reference/mature_market_erp.txt, "
            "reference/industry_averages_*.csv, actualizados enero 2026); comunicados de prensa Grupo Sura (guidance "
            "2026, plan de desapalancamiento, Junta Directiva 2026-2028); Fitch Ratings (mar-2026) y S&P Global "
            "Ratings (mar-2025).",
        ]]),
    ]
    rnm._apply(ws, rows)


def write_cualitativo_sheet(sh, *, price: float, wacc: float) -> None:
    """Reemplaza el contenido mixto (PLTR/lululemon) de 'Cualitativo' por
    una ficha cualitativa limpia de Grupo Sura -- negocio, segmentos y
    hechos relevantes recientes. Complementa (no repite en detalle) la
    Tesis de Inversión, que ya tiene el analisis de escenarios completo."""
    ws = sh.worksheet("Cualitativo")
    ws.batch_clear(["A1:H60"])  # la hoja traia contenido MEZCLADO de PLTR/lululemon en columnas B-D de filas que este script no reescribe todas -- se limpia todo el bloque antes de escribir el contenido nuevo de Grupo Sura
    rows: list[tuple[str, list]] = [
        ("A1", [["GRUPO DE INVERSIONES SURAMERICANA S.A. — Análisis Cualitativo y Puente a la Valoración"]]),
        ("A2", [[f"Fecha: 22-sept-2026 | Precio: {price:,.0f} COP (PFGRUPOSURA) | WACC: {wacc:.2%}"]]),
        ("A4", [["1. NEGOCIO Y ESTRUCTURA"]]),
        ("A5", [["Nombre de la Empresa", "Grupo de Inversiones Suramericana S.A. (Grupo Sura)"]]),
        ("A6", [["Ticker / Bolsa", "PFGRUPOSURA (preferencial) / GRUPOSURA (ordinaria) — Bolsa de Valores de Colombia (BVC)"]]),
        ("A7", [["Sector", "Holding financiero: seguros, gestión de activos y participaciones estratégicas"]]),
        ("A8", [["Sitio Web Oficial", "www.gruposura.com"]]),
        ("A9", [["Visión General", (
            "Grupo Sura es el mayor holding financiero de Colombia y uno de los más grandes de América Latina. "
            "Opera a través de tres pilares: (1) Seguros Suramericana, controlada mayoritariamente; (2) SURA Asset "
            "Management, gestora de pensiones y ahorro con presencia en Chile, México, Perú, Uruguay, Colombia y El "
            "Salvador; y (3) participaciones estratégicas históricas en Bancolombia/Grupo Cibest y Grupo Argos, "
            "originadas en el Grupo Empresarial Antioqueño (GEA). Entre 2024 y 2026 la compañía atravesó su mayor "
            "reestructuración societaria: perdió el control de EPS Suramericana (salud) en jun-2024, ejecutó una "
            "escisión de activos no corrientes hacia sus accionistas en 2025 (~$6,6 billones), recompró cerca de la "
            "mitad de sus acciones en circulación, y en mar-2026 eligió por primera vez en 40+ años una Junta "
            "Directiva sin representación de Grupo Argos."
        )]]),
        ("A10", [["Seguros Suramericana", (
            "Aseguradora líder en Colombia (vida, generales, ARL) con operaciones regionales -- el pilar de mayor "
            "escala del holding en primas."
        )]]),
        ("A11", [["SURA Asset Management", (
            "Gestión de pensiones obligatorias/voluntarias y ahorro en 6 países de LatAm -- ingresos por comisiones, "
            "sensibles a los activos bajo administración (AUM) y a los mercados de capitales locales."
        )]]),
        ("A12", [["Participación en Bancolombia / Grupo Cibest", (
            "Participación estratégica de larga data en el mayor banco de Colombia -- Grupo Cibest culminó en el "
            "semestre la venta de su participación en Banistmo (~USD 1.400M), fortaleciendo su propio balance."
        )]]),
        ("A13", [["Participación cruzada en Grupo Argos", (
            "Participación histórica del GEA, ahora con gobierno corporativo más independiente entre ambos grupos "
            "tras la salida de Argos de la Junta Directiva de Sura en mar-2026."
        )]]),
        ("A15", [["2. HECHOS RELEVANTES RECIENTES (2025-2026)"]]),
        ("A16", [["Evento", "Detalle"]]),
        ("A17", [["Resultados 1S2026: utilidad récord", (
            "Utilidad neta controladora 1S2026 de $1,7 billones (+37,7% interanual); 2T2026 aislado $1,2 billones "
            "(+67%, récord trimestral); ROE LTM de 16,5%, máximo histórico (vs. 7,9% hace 5 años)."
        )]]),
        ("A18", [["Guidance oficial 2026", (
            "Utilidad neta $2,5-2,7 billones; ROE ajustado objetivo 15-16%."
        )]]),
        ("A19", [["Plan de desapalancamiento", (
            "Reducir la deuda neta individual (matriz, no consolidada) en ~20% durante 2026, de $7,1 a ~$5,7 "
            "billones, usando ~$3 billones de dividendos esperados de sus participadas."
        )]]),
        ("A20", [["Manejo de deuda internacional", (
            "Pago de bonos internacionales por USD 300M en abr-2026, reemplazados por deuda bancaria local de "
            "COP 900.000M a 5 años -- reduce el riesgo cambiario de la deuda de la matriz."
        )]]),
        ("A21", [["Venta de Banistmo (Grupo Cibest)", (
            "Culminada en el semestre, por ~USD 1.400M -- fortalece el balance de Bancolombia/Cibest, una de las "
            "principales participadas de Sura."
        )]]),
        ("A22", [["Junta Directiva 2026-2028", (
            "Elegida el 27-mar-2026, sin representación de Grupo Argos por primera vez en 40+ años -- 5 de 7 "
            "miembros independientes, señal de mayor gobierno corporativo."
        )]]),
        ("A23", [["Dividendo 2026", (
            "$2.000/acción aprobado (ambas clases), +33,3% vs. 2025, pagadero en 4 cuotas de $500 -- dividend yield "
            "preferencial ≈3,5% al precio actual."
        )]]),
        ("A24", [["Calificaciones crediticias", (
            "Fitch reafirmó 'BB+' (escala internacional) / 'AAA(col)' (escala local) con perspectiva estable en "
            "mar-2026. S&P Global Ratings había bajado a 'BB' en mar-2025, citando lentitud en el "
            "desapalancamiento post-escisión de Grupo Argos, agravada por un pasivo tributario extraordinario de "
            "~US$171M derivado de la venta de Nutresa en 2024."
        )]]),
        ("A26", [["3. DICTAMEN"]]),
        ("A27", [[(
            "Holding financiero en plena simplificación y re-calificación, cotizando a múltiplos históricamente "
            "bajos (P/E LTM implícito ~4x) frente a un ROE en máximos (16,5%). La tesis de inversión depende de que "
            "el plan de desapalancamiento 2026 se cumpla (los ~$3 billones de dividendos de participadas son la "
            "variable crítica) y de que el mercado reconozca gradualmente la nueva estructura societaria, más simple "
            "y con mejor gobierno corporativo, que el holding heredado de 2023. Ver 'Tesis de Inversión y Supuestos' "
            "para los 3 escenarios de valoración completos con su justificación dato a dato."
        )]]),
        ("A29", [["Fuentes: EEFF consolidados IFRS de Grupo Sura (4T2025, 4T2024, interinos 2T2026); gruposura.com/en/shares/; BVC/La República; comunicados de prensa de la compañía; Fitch Ratings; S&P Global Ratings. Datos al 22-sept-2026."]]),
    ]
    rnm._apply(ws, rows)


def run() -> None:
    import os
    from jmr_valuation.io.env import load_dotenv
    load_dotenv()
    sheet_id = os.environ["GOOGLE_SHEET_ID"]

    print("[1/6] Precio y snapshot de mercado real (yfinance, PFGRUPSURA.CL)...")
    market_raw = get_market_snapshot(YF_TICKER)
    from dataclasses import replace
    market = replace(
        market_raw,
        market_cap=161_871_882 * market_raw.current_price,
        shares_outstanding=161_871_882,
        total_debt=BALANCE_JUN2026["total_debt"],
        total_cash=BALANCE_JUN2026["cash"],
        beta=None,  # no se usa: WACC via beta de industria, ver _override_cost_of_capital
        exchange="BVC",
    )
    print(f"  Precio actual PFGRUPSURA.CL: {market.current_price:,.2f} COP")

    company_inputs = build_company_inputs(current_price=market.current_price)

    client = get_gspread_client()
    sh = open_target_sheet(client, sheet_id)

    print("[2/6] Input sheet (nombre/pais/industria)...")
    rnm.refresh_input_sheet(sh, TICKER, company_inputs, INDUSTRY, INDUSTRY, market)

    print("[3/6] Income Statement / Cash Flow Statement / Balance Sheet...")
    rnm.refresh_income_statement(sh, series, company_inputs)
    rnm.refresh_cash_flow_statement(sh, series)
    rnm.refresh_balance_sheet(sh, series, company_inputs)
    _override_balance_sheet_ltm_column(sh)
    _patch_short_history_baseline(sh)

    print("[4/6] Rotulos de columna / Trailing & Forward Valuation / hojas de formulas / Sector...")
    rnm.refresh_period_headers(sh, series)
    computed = rnm.refresh_trailing_valuation(sh, series, company_inputs)
    rnm.refresh_forward_valuation(sh, series, computed)
    rnm.refresh_eficiencia_capital(sh)
    rnm.refresh_margenes(sh)
    rnm.refresh_salud_financiera(sh)
    rnm.refresh_por_accion(sh)
    rnm.refresh_sector(sh, YF_TICKER, PEER_TICKERS)
    _fix_sector_own_market_cap(sh, market)
    rnm.refresh_resumen_valoracion(sh, YF_TICKER, market)

    print("[5/6] Overrides metodologicos (riskfree/tax/supuestos, beta industria, ERP, tipo empresa, escenarios, parche BVC)...")
    _override_input_sheet_assumptions(sh, riskfree_rate=0.12785)
    _patch_googlefinance_bvc(sh, fallback_price=market.current_price)
    with open(_ROOT / "reference" / "mature_market_erp.txt") as f:
        mature_erp = float(f.read().strip())
    _override_cost_of_capital(sh, mature_erp)
    _override_resumen_tipo_empresa(sh)
    _override_valuation_output_scenarios(sh)
    _clear_relative_valuation_multiple_overrides(sh)
    _fix_optimista_equity_value_off_by_one(sh)

    print("[6/6] Hojas narrativas (Tesis de Inversión y Supuestos / Cualitativo) con los resultados finales...")
    resumen_ws = sh.worksheet("Resumen de Valoración")
    coc_ws = sh.worksheet("Cost of capital worksheet")
    final_price = resumen_ws.acell("B3", value_render_option="UNFORMATTED_VALUE").value
    final_wacc = coc_ws.acell("B14", value_render_option="UNFORMATTED_VALUE").value
    conservador, base, optimista = resumen_ws.get("C12:E12", value_render_option="UNFORMATTED_VALUE")[0]
    write_tesis_sheet(sh, price=final_price, wacc=final_wacc, conservador=conservador, base=base, optimista=optimista)
    write_cualitativo_sheet(sh, price=final_price, wacc=final_wacc)

    print(f"Listo: {sh.url}")


if __name__ == "__main__":
    run()
