"""Arma un CompanyInputs a partir de datos estructurados (XBRL) de SEC EDGAR.

Por que esto SI se puede automatizar de punta a punta (a diferencia de
fiscal_ai_loader.py, que sigue a medio hacer): 'company facts' de EDGAR expone
cada numero contable ya identificado por su tag XBRL estandar
(us-gaap:Revenues, us-gaap:OperatingIncomeLoss, etc.), no un JSON propietario
-- no hace falta adivinar en que llave vive cada dato, solo elegir, para cada
concepto, la primera etiqueta de una lista de candidatas conocidas que la
empresa efectivamente haya reportado (los nombres de tag varian bastante entre
empresas -- Adobe reporta I+D como
'ResearchAndDevelopmentExpenseSoftwareExcludingAcquiredInProcessCost' en vez
del generico 'ResearchAndDevelopmentExpense', por ejemplo -- de ahi las listas
de fallback en _TAGS).

Que NO se puede sacar de un 10-K/10-Q, y por que sigue siendo manual o queda
en su valor por defecto:
- Precio actual y multiplos historicos (hist_multiple_*): dependen de la
  cotizacion en cada fecha, y EDGAR es un repositorio de estados contables,
  no de precios de mercado. current_price se pide como parametro obligatorio;
  los multiplos historicos quedan en 0 (activa el override manual en el
  dashboard si los conoces de otra fuente).
- Supuestos de proyeccion puros (WACC, tasa libre de riesgo, sales-to-capital,
  company_type, margin_of_safety, deltas de escenario Conservador/Optimista):
  son juicio del analista sobre el futuro, no un hecho contable historico.
  riskfree_rate e initial_cost_of_capital se piden como parametros
  obligatorios (no tiene sentido adivinar un WACC); el resto usa los valores
  por defecto de CompanyInputs y se ajusta despues en el dashboard.
- Cronograma de compromisos de leasing y el detalle de stock options (numero
  de opciones, strike, vencimiento, volatilidad): estan en el 10-K, pero como
  tablas con dimensiones (breakdown por anio o por tranche) que la vista
  plana de 'company facts' no expone -- has_operating_leases y
  has_employee_options quedan en False a proposito, para no prender un ajuste
  a medio completar con commitments en cero. Activalos a mano si la empresa
  los tiene y completa los numeros del 10-K.
- hist_nwc_pct_of_revenue_growth: requiere el detalle linea por linea del
  capital de trabajo (que activos/pasivos corrientes se excluyen), que no
  vive en un tag XBRL unico y confiable -- se deja en 0 en vez de arriesgar
  un numero con el signo equivocado.

Uso tipico:
    from jmr_valuation.io.sec_edgar_loader import load_company_inputs_from_sec_edgar

    inputs = load_company_inputs_from_sec_edgar(
        "ADBE", current_price=276.27, riskfree_rate=0.0462, initial_cost_of_capital=0.0938,
    )
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import date

from jmr_valuation.io.inputs import CompanyInputs
from jmr_valuation.io.sec_edgar_client import SecEdgarClient, SecEdgarError

# Tags XBRL candidatos por concepto, en orden de preferencia -- se usa el
# primero que la empresa haya reportado con datos.
_TAGS: dict[str, list[str]] = {
    "revenue": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
                "SalesRevenueNet", "SalesRevenueGoodsNet"],
    "ebit": ["OperatingIncomeLoss"],
    "interest_expense": ["InterestExpense", "InterestExpenseDebt", "InterestAndDebtExpense"],
    "equity": ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
    "cash": ["CashAndCashEquivalentsAtCarryingValue",
             "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"],
    "minority_interest": ["MinorityInterest"],
    # Acciones en circulacion A UNA FECHA (balance/portada del 10-K), no el
    # promedio ponderado diluido del estado de resultados -- para el bridge de
    # valor por accion interesa cuantas acciones hay HOY, no cuantas hubo en
    # promedio durante el ejercicio.
    # 'EntityCommonStockSharesOutstanding' vive en el namespace 'dei', no
    # 'us-gaap' -- varias empresas (Boston Scientific incluida) dejaron de
    # taggear CommonStockSharesOutstanding en us-gaap alrededor de 2020 y
    # desde entonces solo reportan el dato de portada via dei. Se busca en
    # ambos namespaces (ver 'extra' en _concept_rows).
    #
    # OJO: 'CommonStockSharesIssued' NO es un candidato valido aca -- mide
    # acciones EMITIDAS (incluye las que estan en tesoreria), no acciones en
    # CIRCULACION. Para una empresa sin recompras son casi iguales, pero para
    # una con tesoreria material (Boston Scientific, por ejemplo) difieren en
    # cientos de millones de acciones -- mezclarlo con _concept_rows() (que
    # combina todos los candidatos) inflaria la serie con un numero mas alto
    # que no es el que corresponde.
    "shares_outstanding": ["CommonStockSharesOutstanding", "EntityCommonStockSharesOutstanding"],
    "tax_expense": ["IncomeTaxExpenseBenefit"],
    "pretax_income": [
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic",
    ],
    "dividend_per_share": ["CommonStockDividendsPerShareDeclared", "CommonStockDividendsPerShareCashPaid"],
    "da": ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
           "DepreciationAndAmortization"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsForCapitalImprovements"],
    "rd": ["ResearchAndDevelopmentExpense",
           "ResearchAndDevelopmentExpenseSoftwareExcludingAcquiredInProcessCost",
           "ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost"],
    "long_term_debt": ["LongTermDebtNoncurrent", "LongTermDebt", "LongTermDebtAndCapitalLeaseObligations"],
    "current_debt": ["LongTermDebtCurrent", "DebtCurrent", "ShortTermBorrowings"],
    "proceeds_debt": ["ProceedsFromIssuanceOfLongTermDebt"],
    "repayments_debt": ["RepaymentsOfLongTermDebt"],
    "nol": ["DeferredTaxAssetsOperatingLossCarryforwards"],
}


def _concept_rows(gaap: dict, key: str, units: tuple[str, ...] = ("USD",),
                   extra: dict | None = None) -> list[dict] | None:
    """Empresas distintas (y a veces la misma empresa a lo largo de los anios)
    usan tags XBRL distintos para el mismo concepto -- Adobe, por ejemplo, dejo
    de reportar 'LongTermDebtNoncurrent' en 2015 y desde entonces usa
    'LongTermDebt'; Boston Scientific reporta 'StockholdersEquity' recien
    desde 2021 (cuando empezo a tener interes minoritario) pero
    'StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest'
    desde 2008; y varias empresas (Boston Scientific incluida) dejaron de
    taggear 'CommonStockSharesOutstanding' en us-gaap alrededor de 2020,
    reportando desde entonces solo el equivalente de portada
    ('dei:EntityCommonStockSharesOutstanding', namespace distinto -- ver
    'extra' abajo).

    Elegir un unico tag "ganador" (el mas reciente, o el de mas historia en
    caso de empate) resuelve el problema de no traer un dato viejo, pero
    cuando una empresa cambia de tag a mitad de camino dos veces (un tag
    cubre 2008-2020, el reemplazo cubre 2021 en adelante) quedarse con un
    solo tag pierde los anios que solo el OTRO tiene. Por eso esta funcion
    combina ('merge') las filas de TODOS los tags candidatos (y del
    diccionario 'extra' si se paso) en una sola serie, deduplicando por fecha
    de cierre con el mismo criterio que _dedupe_by_end (ante dos filas para
    el mismo 'end', gana la reportada en la presentacion mas antigua)."""
    combined: list[dict] = []
    for source in (gaap, extra) if extra is not None else (gaap,):
        for tag in _TAGS[key]:
            node = source.get(tag)
            if not node:
                continue
            for unit in units:
                candidate_rows = node.get("units", {}).get(unit)
                if candidate_rows:
                    combined.extend(candidate_rows)
                    break
    return _dedupe_by_end(combined) if combined else None


def _duration_days(row: dict) -> int:
    return (date.fromisoformat(row["end"]) - date.fromisoformat(row["start"])).days


def _dedupe_by_end(rows: list[dict]) -> list[dict]:
    """Cuando el mismo periodo aparece en mas de una presentacion (p.ej. como
    comparativo del anio siguiente), nos quedamos con la version reportada en
    la presentacion mas antigua (la propia, no la comparativa posterior)."""
    by_end: dict[str, dict] = {}
    for row in rows:
        prev = by_end.get(row["end"])
        if prev is None or row["filed"] < prev["filed"]:
            by_end[row["end"]] = row
    return sorted(by_end.values(), key=lambda r: r["end"])


def _annual_rows(rows: list[dict] | None) -> list[dict]:
    """OJO: 'fp' == 'FY' NO significa que el hecho en si abarque un anio
    completo -- describe de que reporte periodico se extrajo el hecho (un
    10-K siempre tiene fp='FY' para TODOS sus hechos), no la duracion propia
    del hecho. Muchos 10-K (p.ej. Intuit) redivulgan cada trimestre fiscal en
    una nota de 'informacion financiera trimestral' usando el MISMO tag XBRL
    (Revenues), tambien con form='10-K'/fp='FY', pero con una duracion
    realmente trimestral (~90 dias, frame tipo 'CY2016Q3'). Sin el chequeo de
    duracion, esos trimestres se colaban como si fueran el dato anual y
    corrompian revenue_prior_10k/ebit_prior_10k y todos los ratios/margenes
    historicos derivados de esta funcion."""
    if not rows:
        return []
    annual = [r for r in rows if r.get("form") == "10-K" and r.get("fp") == "FY" and "start" in r
              and 350 <= _duration_days(r) <= 380]
    return _dedupe_by_end(annual)


def _annual_instant_rows(rows: list[dict] | None) -> list[dict]:
    """Como _annual_rows, pero para conceptos de balance (instantaneos, sin
    'start'): un valor por cierre de ejercicio, tomado de los 10-K.

    Nota sobre el bug de _annual_rows (form=10-K/fp=FY con duracion
    trimestral colandose como anual, ver docstring de _annual_rows): un hecho
    INSTANT no tiene 'start', por lo tanto no tiene duracion que chequear, asi
    que ese mismo filtro no se puede aplicar aqui. En teoria un 10-K podria
    tener una nota al pie con el conteo de acciones a un cierre trimestral
    (mismo riesgo conceptual), pero se reviso 'CommonStockSharesOutstanding'
    de INTU y todas las filas con form=10-K/fp=FY tienen 'end' en fechas de
    cierre de ejercicio anual (fin de julio), no de trimestre -- no se
    encontro evidencia real del problema para este tag, asi que no se agrega
    un chequeo especulativo sin caso que lo justifique."""
    if not rows:
        return []
    annual = [r for r in rows if r.get("form") == "10-K" and r.get("fp") == "FY" and "start" not in r]
    return _dedupe_by_end(annual)


def _quarterly_rows(rows: list[dict] | None) -> list[dict]:
    if not rows:
        return []
    quarterly = [r for r in rows if "start" in r and 80 <= _duration_days(r) <= 100]
    return _dedupe_by_end(quarterly)


def _derive_discrete_quarters(rows: list[dict] | None) -> list[dict]:
    """Muchas empresas (Boston Scientific incluida) taggean el primer
    trimestre fiscal como duracion propia (~90 dias) pero Q2 y Q3 como
    ACUMULADO desde el inicio del ejercicio (p.ej. 'del 1/1 al 30/6', no 'del
    1/4 al 30/6') -- _quarterly_rows() (que solo acepta duraciones de ~90
    dias) nunca los encuentra, asi que _ltm_value() siempre termina cayendo
    al ultimo 10-K aunque la empresa SI reporte con la frecuencia trimestral
    normal.

    Esta funcion agrupa los hechos de duracion por su fecha de INICIO (todos
    los puntos acumulados de un mismo ejercicio fiscal comparten el mismo
    'start'), los ordena por fecha de cierre, y resta cada punto menos el
    anterior del mismo grupo para obtener el trimestre discreto -- Q1 sale de
    restar cero (nada anterior), Q2 discreto = Q2 acumulado - Q1, Q3 discreto
    = Q3 acumulado - Q2 acumulado, y Q4 discreto = anual (10-K) - Q3
    acumulado, ya que el propio anual es "el ultimo punto acumulado del
    ejercicio". Para una empresa que YA taggea cada trimestre como duracion
    discreta (Adobe, por ejemplo), cada trimestre queda solo en su propio
    grupo (arrancan en fechas distintas) y el resultado es identico al
    trimestre tal cual estaba reportado -- no cambia nada para ese caso."""
    if not rows:
        return []
    duration_rows = _dedupe_by_end([r for r in rows if "start" in r])
    groups: dict[str, list[dict]] = {}
    for r in duration_rows:
        groups.setdefault(r["start"], []).append(r)

    discrete: list[dict] = []
    for start, group in groups.items():
        group_sorted = sorted(group, key=lambda r: r["end"])
        prev_val, prev_end = 0.0, start
        for r in group_sorted:
            gap_days = (date.fromisoformat(r["end"]) - date.fromisoformat(prev_end)).days
            if 55 <= gap_days <= 105:
                discrete.append({**r, "start": prev_end, "val": r["val"] - prev_val})
            prev_val, prev_end = r["val"], r["end"]
    return sorted(discrete, key=lambda r: r["end"])


def _instant_rows(rows: list[dict] | None) -> list[dict]:
    if not rows:
        return []
    return _dedupe_by_end([r for r in rows if "start" not in r])


def _quarters_are_contiguous(quarters: list[dict]) -> bool:
    """Muchas empresas (Intuit incluida) nunca taggean su ultimo trimestre
    fiscal como un hecho discreto propio -- se calcula como 'anio completo
    menos Q1/Q2/Q3' y no aparece nunca solo en 'company facts'. Si ese
    trimestre falta, tomar 'los ultimos 4 registros trimestrales por fecha de
    cierre' salta ese hueco y termina sumando ~15 meses no consecutivos (con
    un trimestre contado de mas) en vez de un LTM real de 12 meses. Antes de
    confiar en la suma, se verifica que cada trimestre arranque el dia
    siguiente al cierre del anterior (con un margen de +/-5 dias por
    calendarios fiscales de 52/53 semanas)."""
    for prev, curr in zip(quarters, quarters[1:]):
        gap_days = (date.fromisoformat(curr["start"]) - date.fromisoformat(prev["end"])).days
        if not (-5 <= gap_days <= 5):
            return False
    return True


def _ltm_value(rows: list[dict] | None) -> float | None:
    """Suma los ultimos 4 trimestres discretos SI son consecutivos (LTM real);
    si no hay 4 trimestres disponibles, o si hay un hueco entre ellos (ver
    _quarters_are_contiguous), cae al ultimo valor anual (10-K) cerrado en vez
    de sumar periodos no comparables. Los trimestres se derivan con
    _derive_discrete_quarters() (no _quarterly_rows() directo) para poder
    calcular Q2/Q3 discretos aunque la empresa solo los reporte acumulados
    desde el inicio del ejercicio (ver docstring de esa funcion)."""
    quarters = _derive_discrete_quarters(rows)
    if len(quarters) >= 4:
        last_four = quarters[-4:]
        if _quarters_are_contiguous(last_four):
            return sum(r["val"] for r in last_four)
    annual = _annual_rows(rows)
    return annual[-1]["val"] if annual else None


def _latest_instant(rows: list[dict] | None) -> float | None:
    instants = _instant_rows(rows)
    return instants[-1]["val"] if instants else None


def _instant_as_of(rows: list[dict] | None, as_of_date: str) -> float | None:
    instants = [r for r in _instant_rows(rows) if r["end"] == as_of_date]
    return instants[-1]["val"] if instants else None


def _avg_ratio(numerator_rows: list[dict] | None, denominator_annual: list[dict], n: int = 5) -> float:
    numerator_annual = _annual_rows(numerator_rows)
    if not numerator_annual or not denominator_annual:
        return 0.0
    denom_by_end = {r["end"]: r["val"] for r in denominator_annual}
    ratios = [r["val"] / denom_by_end[r["end"]] for r in numerator_annual
              if denom_by_end.get(r["end"])]
    tail = ratios[-n:]
    return sum(tail) / len(tail) if tail else 0.0


def _avg_net_ratio(pos_rows, neg_rows, denominator_annual: list[dict], n: int = 5) -> float:
    """Como _avg_ratio, pero para un numerador = pos - neg (p.ej. emision menos
    repago de deuda). Solo usa los anios donde estan disponibles los 3 datos."""
    pos_annual = {r["end"]: r["val"] for r in _annual_rows(pos_rows)}
    neg_annual = {r["end"]: r["val"] for r in _annual_rows(neg_rows)}
    denom_by_end = {r["end"]: r["val"] for r in denominator_annual}
    ends = sorted(set(pos_annual) & set(neg_annual) & set(denom_by_end))
    ratios = [(pos_annual[e] - neg_annual[e]) / denom_by_end[e] for e in ends if denom_by_end[e]]
    tail = ratios[-n:]
    return sum(tail) / len(tail) if tail else 0.0


def _cagr(values: list[float], years: int) -> float:
    years = min(years, len(values) - 1)
    if years < 1 or values[-1 - years] <= 0:
        return 0.0
    return (values[-1] / values[-1 - years]) ** (1 / years) - 1


def _avg_last_n(values: list[float], n: int) -> float:
    tail = values[-n:]
    return sum(tail) / len(tail) if tail else 0.0


def _to_millions(value: float | None) -> float:
    return (value or 0.0) / 1_000_000


def _resolve_country(submissions: dict) -> str:
    business = submissions.get("addresses", {}).get("business", {})
    if business.get("isForeignLocation"):
        return business.get("country") or business.get("stateOrCountryDescription") or "N/A"
    return "United States"


def load_company_inputs_from_sec_edgar(
    ticker: str,
    *,
    current_price: float,
    riskfree_rate: float,
    initial_cost_of_capital: float,
    client: SecEdgarClient | None = None,
    **overrides: object,
) -> CompanyInputs:
    """current_price, riskfree_rate e initial_cost_of_capital son obligatorios
    porque son datos de mercado/supuestos, no datos contables -- SEC EDGAR no
    los tiene. **overrides permite pisar cualquier otro campo de CompanyInputs
    (por ejemplo company_type='Software' o margin_of_safety=0.30)."""
    client = client or SecEdgarClient()
    ticker = ticker.upper()

    facts_json = client.company_facts(ticker)
    submissions = client.company_submissions(ticker)
    gaap = facts_json.get("facts", {}).get("us-gaap", {})
    dei = facts_json.get("facts", {}).get("dei", {})

    def rows(key: str, units: tuple[str, ...] = ("USD",)) -> list[dict] | None:
        return _concept_rows(gaap, key, units)

    revenue_rows = rows("revenue")
    revenue_annual = _annual_rows(revenue_rows)
    if not revenue_annual:
        raise SecEdgarError(
            f"No se encontraron ingresos anuales (10-K) para {ticker} en SEC EDGAR -- "
            "revisa que el ticker sea correcto y que la empresa presente 10-K (no aplica "
            "a ADRs que solo presentan 20-F, por ejemplo)."
        )
    last_10k_end = revenue_annual[-1]["end"]
    revenue_prior_10k = revenue_annual[-1]["val"]
    revenue_ltm = _ltm_value(revenue_rows) or revenue_prior_10k

    ebit_rows = rows("ebit")
    ebit_annual = _annual_rows(ebit_rows)
    ebit_prior_10k = ebit_annual[-1]["val"] if ebit_annual else 0.0
    ebit_ltm = _ltm_value(ebit_rows) or ebit_prior_10k

    interest_rows = rows("interest_expense")
    interest_annual = _annual_rows(interest_rows)
    interest_expense_prior_10k = interest_annual[-1]["val"] if interest_annual else 0.0
    interest_expense_ltm = _ltm_value(interest_rows) or interest_expense_prior_10k

    equity_rows = rows("equity")
    book_value_equity_ltm = _latest_instant(equity_rows) or 0.0
    book_value_equity_prior_10k = _instant_as_of(equity_rows, last_10k_end) or book_value_equity_ltm

    lt_debt_rows, cur_debt_rows = rows("long_term_debt"), rows("current_debt")

    def _debt_at(as_of: str | None) -> float:
        lt = _instant_as_of(lt_debt_rows, as_of) if as_of else _latest_instant(lt_debt_rows)
        cur = _instant_as_of(cur_debt_rows, as_of) if as_of else _latest_instant(cur_debt_rows)
        return (lt or 0.0) + (cur or 0.0)

    book_value_debt_ltm = _debt_at(None)
    book_value_debt_prior_10k = _debt_at(last_10k_end)

    cash_rows = rows("cash")
    cash_ltm = _latest_instant(cash_rows) or 0.0
    cash_prior_10k = _instant_as_of(cash_rows, last_10k_end) or cash_ltm

    minority_interests = _latest_instant(rows("minority_interest")) or 0.0

    shares_rows = _concept_rows(gaap, "shares_outstanding", units=("shares",), extra=dei)
    shares_outstanding = _to_millions(_latest_instant(shares_rows))
    shares_annual = _annual_instant_rows(shares_rows)

    tax_annual = _annual_rows(rows("tax_expense"))
    pretax_annual = _annual_rows(rows("pretax_income"))
    effective_tax_rate = 0.0
    if tax_annual and pretax_annual:
        pretax_by_end = {r["end"]: r["val"] for r in pretax_annual}
        pretax_last = pretax_by_end.get(tax_annual[-1]["end"])
        if pretax_last:
            effective_tax_rate = tax_annual[-1]["val"] / pretax_last

    dividend_annual = _annual_rows(rows("dividend_per_share", units=("USD/shares",)))
    dividend_per_share_ltm = dividend_annual[-1]["val"] if dividend_annual else 0.0

    nol_carryforward = _to_millions(_latest_instant(rows("nol")))

    # --- Margenes EBIT historicos: si estan poblados, 'run_valuation' arma el
    # margen objetivo Base/Conservador/Optimista a partir de ellos en vez de
    # target_ebit_margin +/- deltas (ver docstring de valuation._target_ebit_margin). ---
    ebit_margin_ltm = ebit_ltm / revenue_ltm if revenue_ltm else 0.0
    revenue_by_end = {r["end"]: r["val"] for r in revenue_annual}
    margins_by_year = [e["val"] / revenue_by_end[e["end"]] for e in ebit_annual
                        if revenue_by_end.get(e["end"])]
    ebit_margin_avg_3y = _avg_last_n(margins_by_year, 3)
    ebit_margin_avg_5y = _avg_last_n(margins_by_year, 5)
    ebit_margin_avg_10y = _avg_last_n(margins_by_year, 10)

    # --- Ratios historicos para proyectar FCFF/OCF/FCFE/EBITDA (promedio de
    # hasta 5 anios anuales -- mismo horizonte que financials_multiples). ---
    hist_interest_pct_of_ebit = _avg_ratio(interest_rows, ebit_annual)
    hist_da_pct_of_revenue = _avg_ratio(rows("da"), revenue_annual)
    hist_capex_pct_of_revenue = _avg_ratio(rows("capex"), revenue_annual)
    hist_net_borrowing_pct_of_revenue = _avg_net_ratio(
        rows("proceeds_debt"), rows("repayments_debt"), revenue_annual,
    )
    shares_values = [r["val"] for r in shares_annual]
    hist_shares_growth_rate = _cagr(shares_values, 3)
    dividend_values = [r["val"] for r in dividend_annual]
    hist_dividend_growth_rate = _cagr(dividend_values, 3)

    # --- I+D: si la empresa lo capitaliza, se completan hasta 9 anios hacia
    # atras (limite de CompanyInputs) para que converters.capitalize_rd amortice. ---
    rd_annual = _annual_rows(rows("rd"))
    capitalize_rd = bool(rd_annual and rd_annual[-1]["val"])
    rd_expense_current_year = rd_annual[-1]["val"] if rd_annual else 0.0
    rd_by_year_ago = {i: 0.0 for i in range(1, 10)}
    for i in range(1, 10):
        idx = len(rd_annual) - 1 - i
        if idx >= 0:
            rd_by_year_ago[i] = rd_annual[idx]["val"]

    revenue_values = [r["val"] for r in revenue_annual]
    naive_growth = _cagr(revenue_values, 3)

    submission_country = _resolve_country(submissions)
    industry = submissions.get("sicDescription") or ""
    years_since_last_10k = (date.today() - date.fromisoformat(last_10k_end)).days / 365.25

    inputs = CompanyInputs(
        ticker=ticker,
        company_name=submissions.get("name") or ticker,
        country_of_incorporation=submission_country,
        industry_us=industry,
        industry_global=industry,
        revenue_ltm=_to_millions(revenue_ltm),
        revenue_prior_10k=_to_millions(revenue_prior_10k),
        years_since_last_10k=years_since_last_10k,
        ebit_ltm=_to_millions(ebit_ltm),
        ebit_prior_10k=_to_millions(ebit_prior_10k),
        interest_expense_ltm=_to_millions(interest_expense_ltm),
        interest_expense_prior_10k=_to_millions(interest_expense_prior_10k),
        book_value_equity_ltm=_to_millions(book_value_equity_ltm),
        book_value_equity_prior_10k=_to_millions(book_value_equity_prior_10k),
        book_value_debt_ltm=_to_millions(book_value_debt_ltm),
        book_value_debt_prior_10k=_to_millions(book_value_debt_prior_10k),
        cash_ltm=_to_millions(cash_ltm),
        cash_prior_10k=_to_millions(cash_prior_10k),
        minority_interests=_to_millions(minority_interests),
        shares_outstanding=shares_outstanding,
        current_price=current_price,
        effective_tax_rate=effective_tax_rate,
        capitalize_rd=capitalize_rd,
        revenue_growth_next_year=naive_growth,
        revenue_growth_years_2_to_5=naive_growth,
        ebit_margin_ltm=ebit_margin_ltm,
        ebit_margin_avg_3y=ebit_margin_avg_3y,
        ebit_margin_avg_5y=ebit_margin_avg_5y,
        ebit_margin_avg_10y=ebit_margin_avg_10y,
        riskfree_rate=riskfree_rate,
        initial_cost_of_capital=initial_cost_of_capital,
        nol_carryforward=nol_carryforward,
        hist_interest_pct_of_ebit=hist_interest_pct_of_ebit,
        hist_da_pct_of_revenue=hist_da_pct_of_revenue,
        hist_capex_pct_of_revenue=hist_capex_pct_of_revenue,
        hist_net_borrowing_pct_of_revenue=hist_net_borrowing_pct_of_revenue,
        hist_shares_growth_rate=hist_shares_growth_rate,
        hist_dividend_growth_rate=hist_dividend_growth_rate,
        dividend_per_share_ltm=dividend_per_share_ltm,
        rd_expense_current_year=_to_millions(rd_expense_current_year),
        rd_expense_year_minus_1=_to_millions(rd_by_year_ago[1]),
        rd_expense_year_minus_2=_to_millions(rd_by_year_ago[2]),
        rd_expense_year_minus_3=_to_millions(rd_by_year_ago[3]),
        rd_expense_year_minus_4=_to_millions(rd_by_year_ago[4]),
        rd_expense_year_minus_5=_to_millions(rd_by_year_ago[5]),
        rd_expense_year_minus_6=_to_millions(rd_by_year_ago[6]),
        rd_expense_year_minus_7=_to_millions(rd_by_year_ago[7]),
        rd_expense_year_minus_8=_to_millions(rd_by_year_ago[8]),
        rd_expense_year_minus_9=_to_millions(rd_by_year_ago[9]),
    )

    if overrides:
        inputs = replace(inputs, **overrides)
    return inputs


@dataclass(frozen=True)
class AnnualSeries:
    """Historico anual (hasta 10 FY, el mas viejo primero) + LTM -- alimenta
    'Motor de Supuestos v2' (CAGR 3/5/Ny, mediana de margen, etc.), que
    necesita la SERIE completa y no solo LTM/prior_10k como
    `load_company_inputs_from_sec_edgar`."""

    ticker: str
    company_name: str
    fiscal_year_ends: list[str]      # ISO date, mas viejo primero, hasta 10
    revenue: list[float]             # $ (no millones -- se convierte al armar la hoja "Datos")
    ebit: list[float]
    da: list[float]
    shares_outstanding: list[float]
    long_term_debt: list[float]
    current_debt: list[float]
    cash: list[float]
    ltm_revenue: float
    ltm_ebit: float
    ltm_da: float


def load_annual_series_from_sec_edgar(
    ticker: str, *, years: int = 10, client: SecEdgarClient | None = None,
) -> AnnualSeries:
    """Arma hasta `years` FY de historico real desde SEC EDGAR (companyfacts),
    reusando el mismo mapeo de tags/dedupe que `load_company_inputs_from_sec_edgar`
    -- ver docstring de ese modulo para por que EDGAR (y no yfinance, que solo
    trae ~4-5 anios de anual) es la fuente para esta serie larga."""
    client = client or SecEdgarClient()
    ticker = ticker.upper()

    facts_json = client.company_facts(ticker)
    submissions = client.company_submissions(ticker)
    gaap = facts_json.get("facts", {}).get("us-gaap", {})
    dei = facts_json.get("facts", {}).get("dei", {})

    def rows(key: str, units: tuple[str, ...] = ("USD",)) -> list[dict] | None:
        return _concept_rows(gaap, key, units)

    revenue_rows = rows("revenue")
    revenue_annual = _annual_rows(revenue_rows)
    if not revenue_annual:
        raise SecEdgarError(
            f"No se encontraron ingresos anuales (10-K) para {ticker} en SEC EDGAR."
        )
    revenue_annual = revenue_annual[-years:]
    ends = [r["end"] for r in revenue_annual]

    ebit_by_end = {r["end"]: r["val"] for r in _annual_rows(rows("ebit"))}
    da_by_end = {r["end"]: r["val"] for r in _annual_rows(rows("da"))}

    shares_rows = _concept_rows(gaap, "shares_outstanding", units=("shares",), extra=dei)
    shares_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(shares_rows)}
    lt_debt_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("long_term_debt"))}
    cur_debt_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("current_debt"))}
    cash_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("cash"))}

    def _series_at(by_end: dict[str, float]) -> list[float]:
        return [by_end.get(end, 0.0) for end in ends]

    ltm_revenue = _ltm_value(revenue_rows) or revenue_annual[-1]["val"]
    ltm_ebit = _ltm_value(rows("ebit")) or ebit_by_end.get(ends[-1], 0.0)
    ltm_da = _ltm_value(rows("da")) or da_by_end.get(ends[-1], 0.0)

    return AnnualSeries(
        ticker=ticker,
        company_name=submissions.get("name") or ticker,
        fiscal_year_ends=ends,
        revenue=[r["val"] for r in revenue_annual],
        ebit=_series_at(ebit_by_end),
        da=_series_at(da_by_end),
        shares_outstanding=_series_at(shares_by_end),
        long_term_debt=_series_at(lt_debt_by_end),
        current_debt=_series_at(cur_debt_by_end),
        cash=_series_at(cash_by_end),
        ltm_revenue=ltm_revenue,
        ltm_ebit=ltm_ebit,
        ltm_da=ltm_da,
    )
