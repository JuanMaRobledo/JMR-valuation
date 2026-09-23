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

from dataclasses import dataclass, field, replace
from datetime import date

from jmr_valuation.io.inputs import CompanyInputs
from jmr_valuation.io.sec_edgar_client import SecEdgarClient, SecEdgarError

# Tags XBRL candidatos por concepto, en orden de preferencia -- se usa el
# primero que la empresa haya reportado con datos.
_TAGS: dict[str, list[str]] = {
    "revenue": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
                "SalesRevenueNet", "SalesRevenueGoodsNet"],
    "ebit": ["OperatingIncomeLoss"],
    "interest_expense": ["InterestExpense", "InterestExpenseDebt", "InterestAndDebtExpense",
                         "InterestExpenseNonoperating"],
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
    # Promedio ponderado de acciones DILUIDAS del periodo (para EPS/FCFF per
    # share historico) -- concepto DISTINTO de 'shares_outstanding' arriba
    # (que es un instantaneo a una fecha de balance, para el bridge de valor
    # por accion). Mezclarlos no es intercambiable: el promedio ponderado
    # diluido es sistematicamente mas alto que las acciones en circulacion a
    # cierre cuando hay recompras activas durante el año.
    "diluted_shares_avg": ["WeightedAverageNumberOfDilutedSharesOutstanding"],
    "basic_shares_avg": ["WeightedAverageNumberOfSharesOutstandingBasic"],
    "net_income": ["NetIncomeLoss", "ProfitLoss"],
    "tax_expense": ["IncomeTaxExpenseBenefit"],
    "operating_cash_flow": ["NetCashProvidedByUsedInOperatingActivities",
                             "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
    "buybacks": ["PaymentsForRepurchaseOfCommonStock"],
    "dividends_paid": ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends"],
    "cogs": ["CostOfRevenue", "CostOfGoodsAndServicesSold", "CostOfServices", "CostOfGoodsSold"],
    # Totales de balance ya agregados por la propia empresa (no hace falta
    # sumar Cuentas por Cobrar + Otros Activos Corrientes a mano) -- se
    # necesitan para el Cambio en Capital de Trabajo de 'Financials
    # Multiples' (filas historicas de FCFF/FCFE), que referencia
    # 'Balance Sheet'!fila 10 (Total Current Assets) y fila 24 (Total
    # Current Liabilities) directamente.
    "current_assets": ["AssetsCurrent"],
    "current_liabilities": ["LiabilitiesCurrent"],
    "pretax_income": [
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
        "IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
        # 'IncomeLossFromContinuingOperationsBeforeIncomeTaxesDomestic' NO va
        # aca: es solo la parte DOMESTICA del resultado antes de impuestos
        # (PYPL: ~$1.000M de ~$5.400M en 2023-2025) -- usarla como total
        # disparaba la tasa efectiva a >100%. Ver _pretax_rows.
    ],
    "dividend_per_share": ["CommonStockDividendsPerShareDeclared", "CommonStockDividendsPerShareCashPaid"],
    "da": ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet",
           "DepreciationAndAmortization"],
    # Fallback si la empresa NO reporta ninguno de los tags combinados de
    # arriba (MSFT, por ejemplo, reporta 'Depreciation' y
    # 'AmortizationOfIntangibleAssets' como dos lineas separadas, igual que
    # el caso de SG&A -- ver _sum_two_series). Sin este fallback, "da"
    # quedaba en 0 para MSFT: EBITDA terminaba IGUAL a EBIT en todo el
    # modelo (Income Statement fila 28, 'Financials Multiples' fila 18-20,
    # EV/EBITDA), entendiendo mal el multiplo real y, mas grave, dejando
    # FCFF/FCFE sin el resello de D&A (~$39.000M/año) -- eso fue lo que
    # tumbo 'EV/FCFF'/'P/FCFE' a precios objetivo profundamente negativos.
    "da_depreciation": ["Depreciation"],
    "da_amortization": ["AmortizationOfIntangibleAssets", "AmortizationOfIntangibleAssetsAndOtherAssets"],
    "capex": ["PaymentsToAcquirePropertyPlantAndEquipment", "PaymentsForCapitalImprovements"],
    "rd": ["ResearchAndDevelopmentExpense",
           "ResearchAndDevelopmentExpenseSoftwareExcludingAcquiredInProcessCost",
           "ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost"],
    "long_term_debt": ["LongTermDebtNoncurrent", "LongTermDebt", "LongTermDebtAndCapitalLeaseObligations"],
    "current_debt": ["LongTermDebtCurrent", "DebtCurrent", "ShortTermBorrowings"],
    "proceeds_debt": ["ProceedsFromIssuanceOfLongTermDebt"],
    "repayments_debt": ["RepaymentsOfLongTermDebt"],
    "nol": ["DeferredTaxAssetsOperatingLossCarryforwards"],
    # --- Agregado para terminar de poblar Income Statement/Balance Sheet/
    # Cash Flow Statement fila por fila (antes solo se llenaban las filas
    # que alimentan la valoracion; el resto quedaba en blanco en la
    # plantilla -- ver refresh_native_model.py). ---
    "sga": ["SellingGeneralAndAdministrativeExpense"],
    # Fallback si la empresa NO reporta el tag combinado de arriba (MSFT,
    # por ejemplo, reporta 'GeneralAndAdministrativeExpense' y
    # 'SellingAndMarketingExpense' como dos lineas separadas) -- estas DOS
    # series se SUMAN (no se combinan como candidatos intercambiables, ver
    # _sga_from_parts) para reconstruir el equivalente de SG&A combinado.
    "sga_admin": ["GeneralAndAdministrativeExpense"],
    "sga_selling": ["SellingAndMarketingExpense", "MarketingExpense", "SellingExpense"],
    "total_assets": ["Assets"],
    "total_liabilities": ["Liabilities"],
    "share_based_comp": ["ShareBasedCompensation"],
    "investing_cash_flow": ["NetCashProvidedByUsedInInvestingActivities"],
    "financing_cash_flow": ["NetCashProvidedByUsedInFinancingActivities"],
    "receivables": ["AccountsReceivableNetCurrent", "ReceivablesNetCurrent"],
    "ppe_net": ["PropertyPlantAndEquipmentNet"],
    "goodwill": ["Goodwill"],
    "accounts_payable": ["AccountsPayableCurrent"],
    "apic": ["AdditionalPaidInCapital", "AdditionalPaidInCapitalCommonStock",
             "CommonStockIncludingAdditionalPaidInCapital", "CommonStocksIncludingAdditionalPaidInCapital"],
    "retained_earnings": ["RetainedEarningsAccumulatedDeficit"],
    "aoci": ["AccumulatedOtherComprehensiveIncomeLossNetOfTax"],
    # --- Tercera tanda: conceptos que MSFT (y otras empresas grandes) SI
    # taggean, pero con nombres que no habiamos probado todavia. ---
    "short_term_investments": ["ShortTermInvestments"],
    "intangibles_net": ["FiniteLivedIntangibleAssetsNet", "IntangibleAssetsNetExcludingGoodwill"],
    "long_term_investments": ["LongTermInvestments"],
    "lease_liability_noncurrent": ["OperatingLeaseLiabilityNoncurrent", "FinanceLeaseLiabilityNoncurrent"],
    "unearned_revenue_current": ["ContractWithCustomerLiabilityCurrent", "DeferredRevenueCurrent"],
    "interest_investment_income": ["InvestmentIncomeInterestAndDividend", "InvestmentIncomeInterest",
                                    "InvestmentIncomeNet"],
    "business_acquisitions": ["PaymentsToAcquireBusinessesNetOfCashAcquired"],
    "stock_issuance": ["ProceedsFromIssuanceOfCommonStock"],
    # --- Cuarta tanda: desglose linea por linea de capital de trabajo (Cash
    # Flow Statement filas 7-11) e inversiones (filas 17-18), que antes
    # quedaban en blanco absorbidas enteras dentro de un solo plug (Other
    # Adjustments/Other Investing Activities). Signo tal cual XBRL (positivo
    # = el activo/pasivo AUMENTO en el periodo) -- se ajusta el signo para
    # caja en refresh_cash_flow_statement, no aca. ---
    "cf_receivables_change": ["IncreaseDecreaseInAccountsReceivable"],
    "cf_payables_change": ["IncreaseDecreaseInAccountsPayable"],
    "cf_income_tax_payable_change": ["IncreaseDecreaseInAccruedIncomeTaxesPayable"],
    # OJO: 'IncreaseDecreaseInDeferredRevenue' existe tambien para MSFT pero
    # con magnitudes que no son comparables (parece taggear el SALDO, no el
    # cambio, en los anios viejos) -- no se agrega como fallback para no
    # arriesgar mezclar dos series no comparables bajo el mismo 'end'.
    "cf_unearned_revenue_change": ["IncreaseDecreaseInContractWithCustomerLiability"],
    "purchases_of_investments": ["PaymentsToAcquireInvestments"],
    # Idem: 'ProceedsFromSaleOfAvailableForSaleSecurities' tambien existe
    # para MSFT pero solo hasta 2018 (despues deja de reportarse separado de
    # 'maturities/calls') -- no se suma como fallback porque en los anios
    # donde coexisten ambas SON dos flujos de caja reales distintos, no un
    # cambio de tag (el merge estandar asume lo segundo).
    "proceeds_from_investments": ["ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities"],
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
    return _dedupe_by_period(combined) if combined else None


def _raw_rows(gaap: dict, key: str) -> list[dict]:
    out: list[dict] = []
    for tag in _TAGS[key]:
        out.extend(gaap.get(tag, {}).get("units", {}).get("USD", []))
    return out


def _period_key(r: dict) -> tuple:
    return (r.get("start"), r["end"], r.get("accn"))


def _ebit_rows(gaap: dict) -> list[dict] | None:
    """Resultado operativo. Si la empresa no taggea OperatingIncomeLoss
    (Nike no lo reporta nunca: su estado de resultados va de Gross Profit a
    Income Before Taxes sin subtotal operativo), se completa con
    Gross Profit - SG&A - I+D (I+D solo si la empresa lo reporta aparte en
    ese mismo periodo), emparejando periodo y presentacion como _pretax_rows.
    Sin esto el EBIT quedaba en 0 y el margen/DCF de NKE no tenian sentido.
    'Other (income) expense' queda afuera a proposito: es no operativo."""
    reported = _concept_rows(gaap, "ebit") or []
    sga_by_key = {_period_key(r): r["val"] for r in _raw_rows(gaap, "sga") if "start" in r}
    rd_by_key = {_period_key(r): r["val"] for r in _raw_rows(gaap, "rd") if "start" in r}
    synthesized = [
        {**r, "val": r["val"] - sga_by_key[_period_key(r)] - rd_by_key.get(_period_key(r), 0)}
        for r in gaap.get("GrossProfit", {}).get("units", {}).get("USD", [])
        if "start" in r and _period_key(r) in sga_by_key
    ]
    reported_periods = {(r.get("start"), r["end"]) for r in reported}
    combined = reported + [r for r in synthesized if (r["start"], r["end"]) not in reported_periods]
    return _dedupe_by_period(combined) if combined else None


def _pretax_rows(gaap: dict) -> list[dict] | None:
    """Resultado antes de impuestos. Si la empresa dejo de taggear el total
    (PYPL desde 2023 solo taggea el desglose Domestic/Foreign), se completa
    con la identidad Net Income + Income Tax Expense, emparejando filas del
    MISMO periodo (start/end) y la MISMA presentacion (accn) antes de
    deduplicar -- asi no se mezcla un trimestre de un concepto con un
    acumulado del otro que comparta fecha de cierre."""
    reported = _concept_rows(gaap, "pretax_income") or []

    def _raw(key: str) -> list[dict]:
        out: list[dict] = []
        for tag in _TAGS[key]:
            out.extend(gaap.get(tag, {}).get("units", {}).get("USD", []))
        return out

    tax_by_key = {(r.get("start"), r["end"], r.get("accn")): r["val"] for r in _raw("tax_expense") if "start" in r}
    synthesized = [
        {**r, "val": r["val"] + tax_by_key[(r["start"], r["end"], r.get("accn"))]}
        for r in _raw("net_income")
        if "start" in r and (r["start"], r["end"], r.get("accn")) in tax_by_key
    ]
    reported_ends = {(r.get("start"), r["end"]) for r in reported}
    combined = reported + [r for r in synthesized if (r["start"], r["end"]) not in reported_ends]
    return _dedupe_by_period(combined) if combined else None


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


def _dedupe_by_period(rows: list[dict]) -> list[dict]:
    """Como _dedupe_by_end, pero la clave es el PERIODO completo (start, end)
    y no solo la fecha de cierre. Un 10-Q de Q3 trae dos hechos que cierran
    el mismo dia -- el trimestre (jul-sep) y el acumulado de 9 meses
    (ene-sep); deduplicar solo por 'end' se quedaba con uno cualquiera y, si
    sobrevivia el trimestral, _derive_discrete_quarters ya no podia sacar
    Q4 = anual - 9M acumulado (PYPL: el LTM de I+D, SG&A y D&A caia al
    ultimo 10-K). Los filtros posteriores (_annual_rows, _quarterly_rows,
    _instant_rows) siguen deduplicando por 'end' despues de filtrar por
    duracion, asi que para ellos no cambia nada."""
    by_period: dict[tuple, dict] = {}
    for row in rows:
        key = (row.get("start"), row["end"])
        prev = by_period.get(key)
        if prev is None or row["filed"] < prev["filed"]:
            by_period[key] = row
    return sorted(by_period.values(), key=lambda r: (r["end"], r.get("start") or ""))


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
    duration_rows = _dedupe_by_period([r for r in rows if "start" in r])
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
    # Un mismo trimestre puede salir dos veces (reportado discreto Y derivado
    # de restar acumulados, ver _dedupe_by_period) -- uno por cierre.
    return _dedupe_by_end(discrete)


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


def _ltm_average_value(rows: list[dict] | None) -> float | None:
    """Como _ltm_value, pero PROMEDIA (no suma) los ultimos 4 trimestres --
    para un promedio ponderado por periodo (acciones diluidas promedio),
    sumar 4 trimestres da ~4x el valor real en vez de un LTM comparable.

    OJO: a diferencia de _ltm_value, esto usa _quarterly_rows (duracion
    propia de ~90 dias tal cual reportada) y NO _derive_discrete_quarters.
    _derive_discrete_quarters resta 'acumulado - acumulado anterior', que
    solo tiene sentido para un FLUJO que se acumula desde el inicio del
    ejercicio (ingresos, EBIT). El promedio ponderado de acciones diluidas
    NUNCA se reporta acumulado -- cada trimestre ya es su propio promedio
    independiente -- asi que restarlos como si fueran acumulados da un
    numero sin sentido (confirmado con MSFT: daba ~1.860M en vez de ~7.450M
    acciones)."""
    quarters = _quarterly_rows(rows)
    if len(quarters) >= 4:
        last_four = quarters[-4:]
        if _quarters_are_contiguous(last_four):
            return sum(r["val"] for r in last_four) / 4
    annual = _annual_rows(rows)
    return annual[-1]["val"] if annual else None


def _latest_instant(rows: list[dict] | None) -> float | None:
    instants = _instant_rows(rows)
    return instants[-1]["val"] if instants else None


def _instant_as_of(rows: list[dict] | None, as_of_date: str) -> float | None:
    instants = [r for r in _instant_rows(rows) if r["end"] == as_of_date]
    return instants[-1]["val"] if instants else None


def _latest_shares_outstanding(shares_rows: list[dict] | None, diluted_rows: list[dict] | None) -> float | None:
    """Como _latest_instant, pero con fallback al promedio diluido del año
    mas reciente cuando ese dato es MAS NUEVO que el ultimo instantaneo de
    acciones (empresas de clase dual que dejan de taggear el conteo puntual
    combinado -- ver docstring de _shares_outstanding_by_end). Usa
    _instant_rows (CUALQUIER fecha, no solo cierres de ejercicio) para no
    perder un 10-Q reciente frente a un 10-K viejo."""
    instants = _instant_rows(shares_rows)
    diluted_annual = _annual_rows(diluted_rows)
    if not instants:
        return diluted_annual[-1]["val"] if diluted_annual else None
    if diluted_annual and diluted_annual[-1]["end"] > instants[-1]["end"]:
        return diluted_annual[-1]["val"]
    return instants[-1]["val"]


def _shares_outstanding_by_end(shares_rows: list[dict] | None, diluted_rows: list[dict] | None) -> dict[str, float]:
    """Acciones en circulacion PUNTUALES (CommonStockSharesOutstanding /
    EntityCommonStockSharesOutstanding), con fallback al promedio ponderado
    diluido de ESE año para los cierres donde el conteo puntual no esta
    disponible. Empresas con clases duales de accion (DUOL confirmado:
    Class A/Class B) a veces dejan de taggear el conteo puntual combinado
    despues del IPO -- el dato pasa a reportarse solo en el cover page
    (dei:EntityCommonStockSharesOutstanding) desglosado POR CLASE, que la
    API de companyfacts no expone sin dimensiones XBRL que este loader no
    parsea. El promedio diluido del año es la mejor aproximacion real
    disponible al conteo actual (no una invencion), y sigue reportandose
    todos los años aunque el conteo puntual haya dejado de aparecer."""
    by_end = {r["end"]: r["val"] for r in _annual_instant_rows(shares_rows)}
    for r in _annual_rows(diluted_rows):
        by_end.setdefault(r["end"], r["val"])
    return by_end


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


def _da_rows(rows) -> list[dict] | None:
    """D&A con fallback: si la empresa no reporta un tag combinado de D&A,
    suma Depreciation + AmortizationOfIntangibleAssets (MSFT es el caso que
    motivo este fallback -- reporta ambos por separado, nunca un tag
    combinado, asi que 'da' quedaba vacio y EBITDA terminaba IGUAL a EBIT
    en todo el modelo). `rows` es la clausura local `rows(key, units)` de
    cada funcion que arma un AnnualSeries/CompanyInputs."""
    return rows("da") or _sum_two_series(_annual_rows(rows("da_depreciation")), _annual_rows(rows("da_amortization")))


def _sum_two_series(rows_a: list[dict] | None, rows_b: list[dict] | None) -> list[dict] | None:
    """Suma dos series de hechos DURATION por fecha de cierre -- para
    reconstruir un concepto combinado (p.ej. SG&A) cuando una empresa lo
    reporta como dos lineas separadas (MSFT: 'GeneralAndAdministrativeExpense'
    + 'SellingAndMarketingExpense') en vez del tag combinado estandar. Solo
    suma los años donde AMBAS series tienen dato -- un año con solo una de
    las dos no se incluye (evita subestimar el total)."""
    a_by_end = {r["end"]: r for r in (rows_a or [])}
    b_by_end = {r["end"]: r for r in (rows_b or [])}
    common_ends = set(a_by_end) & set(b_by_end)
    if not common_ends:
        return None
    return [{**a_by_end[end], "val": a_by_end[end]["val"] + b_by_end[end]["val"]} for end in common_ends]


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

    ebit_rows = _ebit_rows(gaap)
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
    diluted_rows_for_shares = rows("diluted_shares_avg", units=("shares",))
    shares_outstanding = _to_millions(_latest_shares_outstanding(shares_rows, diluted_rows_for_shares))
    shares_annual = _annual_instant_rows(shares_rows)

    tax_annual = _annual_rows(rows("tax_expense"))
    pretax_annual = _annual_rows(_pretax_rows(gaap))
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
    hist_da_pct_of_revenue = _avg_ratio(_da_rows(rows), revenue_annual)
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
    # --- Agregado para refrescar Income Statement (taxes/net income/EPS/
    # acciones diluidas), Cash Flow Statement (OCF/CapEx/buybacks/dividendos)
    # y Trailing/Forward Valuation (multiplos historicos reales) -- ver
    # docstring de refresh_native_model.py para el mapeo completo a celdas.
    # Con default (lista vacia/0.0) para no romper fixtures de test
    # existentes (test_assumptions_engine.py, test_sheets_writer.py) que
    # arman un AnnualSeries a mano sin estos campos, que no les interesan. ---
    tax_expense: list[float] = field(default_factory=list)
    net_income: list[float] = field(default_factory=list)
    diluted_shares_avg: list[float] = field(default_factory=list)  # promedio ponderado diluido, no instantaneo
    operating_cash_flow: list[float] = field(default_factory=list)
    capex: list[float] = field(default_factory=list)          # signo tal cual XBRL lo reporta (positivo = salida de caja)
    buybacks: list[float] = field(default_factory=list)       # idem, positivo = salida de caja
    dividends_paid: list[float] = field(default_factory=list)  # idem, positivo = salida de caja
    cogs: list[float] = field(default_factory=list)            # costo de ventas -- Gross Profit = revenue - cogs
    current_assets: list[float] = field(default_factory=list)       # AssetsCurrent, ya agregado por la empresa
    current_liabilities: list[float] = field(default_factory=list)  # LiabilitiesCurrent, idem
    ltm_tax_expense: float = 0.0
    ltm_net_income: float = 0.0
    ltm_diluted_shares_avg: float = 0.0
    ltm_operating_cash_flow: float = 0.0
    ltm_capex: float = 0.0
    ltm_buybacks: float = 0.0
    ltm_dividends_paid: float = 0.0
    ltm_cogs: float = 0.0
    # --- Segunda tanda: termina de poblar filas de Income Statement/Balance
    # Sheet/Cash Flow Statement que antes quedaban en blanco en la plantilla
    # (solo se llenaban las filas que alimentan la valoracion). ---
    rd: list[float] = field(default_factory=list)
    sga: list[float] = field(default_factory=list)
    pretax_income: list[float] = field(default_factory=list)
    total_assets: list[float] = field(default_factory=list)
    total_liabilities: list[float] = field(default_factory=list)
    equity: list[float] = field(default_factory=list)               # historico completo (distinto de company_inputs, que solo trae LTM/prior_10k)
    share_based_comp: list[float] = field(default_factory=list)
    investing_cash_flow: list[float] = field(default_factory=list)
    financing_cash_flow: list[float] = field(default_factory=list)
    receivables: list[float] = field(default_factory=list)
    ppe_net: list[float] = field(default_factory=list)
    goodwill: list[float] = field(default_factory=list)
    accounts_payable: list[float] = field(default_factory=list)
    apic: list[float] = field(default_factory=list)
    retained_earnings: list[float] = field(default_factory=list)
    aoci: list[float] = field(default_factory=list)
    ltm_rd: float = 0.0
    ltm_sga: float = 0.0
    ltm_pretax_income: float = 0.0
    ltm_share_based_comp: float = 0.0
    ltm_investing_cash_flow: float = 0.0
    ltm_financing_cash_flow: float = 0.0
    interest_expense: list[float] = field(default_factory=list)  # historico completo -- company_inputs solo trae LTM/prior_10k
    ltm_interest_expense: float = 0.0
    # --- Tercera tanda (ver _TAGS) ---
    short_term_investments: list[float] = field(default_factory=list)
    intangibles_net: list[float] = field(default_factory=list)
    long_term_investments: list[float] = field(default_factory=list)
    lease_liability_noncurrent: list[float] = field(default_factory=list)
    unearned_revenue_current: list[float] = field(default_factory=list)
    basic_shares_avg: list[float] = field(default_factory=list)  # promedio ponderado BASICO como serie propia (no solo fallback de diluido)
    interest_investment_income: list[float] = field(default_factory=list)
    business_acquisitions: list[float] = field(default_factory=list)
    stock_issuance: list[float] = field(default_factory=list)
    ltm_basic_shares_avg: float = 0.0
    ltm_interest_investment_income: float = 0.0
    ltm_business_acquisitions: float = 0.0
    ltm_stock_issuance: float = 0.0
    # --- Cuarta tanda (ver _TAGS) ---
    cf_receivables_change: list[float] = field(default_factory=list)
    cf_payables_change: list[float] = field(default_factory=list)
    cf_income_tax_payable_change: list[float] = field(default_factory=list)
    cf_unearned_revenue_change: list[float] = field(default_factory=list)
    purchases_of_investments: list[float] = field(default_factory=list)
    proceeds_from_investments: list[float] = field(default_factory=list)
    ltm_cf_receivables_change: float = 0.0
    ltm_cf_payables_change: float = 0.0
    ltm_cf_income_tax_payable_change: float = 0.0
    ltm_cf_unearned_revenue_change: float = 0.0
    ltm_purchases_of_investments: float = 0.0
    ltm_proceeds_from_investments: float = 0.0


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

    ebit_by_end = {r["end"]: r["val"] for r in _annual_rows(_ebit_rows(gaap))}
    da_rows = _da_rows(rows)
    da_by_end = {r["end"]: r["val"] for r in _annual_rows(da_rows)}

    shares_rows = _concept_rows(gaap, "shares_outstanding", units=("shares",), extra=dei)
    diluted_rows = rows("diluted_shares_avg", units=("shares",))
    shares_by_end = _shares_outstanding_by_end(shares_rows, diluted_rows)
    lt_debt_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("long_term_debt"))}
    cur_debt_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("current_debt"))}
    cash_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("cash"))}
    current_assets_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("current_assets"))}
    current_liabilities_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("current_liabilities"))}

    tax_rows, ni_rows = rows("tax_expense"), rows("net_income")
    ocf_rows, capex_rows = rows("operating_cash_flow"), rows("capex")
    buyback_rows, dividend_rows = rows("buybacks"), rows("dividends_paid")
    cogs_rows = rows("cogs")
    tax_by_end = {r["end"]: r["val"] for r in _annual_rows(tax_rows)}
    ni_by_end = {r["end"]: r["val"] for r in _annual_rows(ni_rows)}
    ocf_by_end = {r["end"]: r["val"] for r in _annual_rows(ocf_rows)}
    capex_by_end = {r["end"]: r["val"] for r in _annual_rows(capex_rows)}
    buyback_by_end = {r["end"]: r["val"] for r in _annual_rows(buyback_rows)}
    dividend_by_end = {r["end"]: r["val"] for r in _annual_rows(dividend_rows)}
    cogs_by_end = {r["end"]: r["val"] for r in _annual_rows(cogs_rows)}

    # Acciones diluidas promedio: si una empresa solo reporta el promedio
    # BASICO (no diluido) para algun anio, se completa con ese -- mejor
    # aproximacion real que dejar el anio en 0 (que arruinaria EPS/FCFF per
    # share de ese punto especifico en las hojas de multiplos).
    basic_rows = rows("basic_shares_avg", units=("shares",))
    diluted_by_end = {r["end"]: r["val"] for r in _annual_rows(diluted_rows)}
    basic_by_end = {r["end"]: r["val"] for r in _annual_rows(basic_rows)}
    diluted_shares_by_end = {**basic_by_end, **diluted_by_end}

    def _series_at(by_end: dict[str, float]) -> list[float]:
        return [by_end.get(end, 0.0) for end in ends]

    ltm_revenue = _ltm_value(revenue_rows) or revenue_annual[-1]["val"]
    ltm_ebit = _ltm_value(_ebit_rows(gaap)) or ebit_by_end.get(ends[-1], 0.0)
    ltm_da = _ltm_value(da_rows) or da_by_end.get(ends[-1], 0.0)
    ltm_tax_expense = _ltm_value(tax_rows) or tax_by_end.get(ends[-1], 0.0)
    ltm_net_income = _ltm_value(ni_rows) or ni_by_end.get(ends[-1], 0.0)
    ltm_operating_cash_flow = _ltm_value(ocf_rows) or ocf_by_end.get(ends[-1], 0.0)
    ltm_capex = _ltm_value(capex_rows) or capex_by_end.get(ends[-1], 0.0)
    ltm_buybacks = _ltm_value(buyback_rows) or buyback_by_end.get(ends[-1], 0.0)
    ltm_dividends_paid = _ltm_value(dividend_rows) or dividend_by_end.get(ends[-1], 0.0)
    ltm_cogs = _ltm_value(cogs_rows) or cogs_by_end.get(ends[-1], 0.0)
    ltm_diluted_shares_avg = (
        _ltm_average_value(diluted_rows) or _ltm_average_value(basic_rows)
        or diluted_shares_by_end.get(ends[-1], 0.0)
    )

    # --- Segunda tanda de conceptos (ver docstring de AnnualSeries) --
    # duration (flujo, se les aplica _annual_rows/_ltm_value) o instant
    # (balance, _annual_instant_rows, sin LTM propio -- se reusa el ultimo
    # anual, igual que ya se hace con current_assets/current_debt). ---
    rd_rows, pretax_rows = rows("rd"), _pretax_rows(gaap)
    # _sum_two_series recibe filas YA filtradas a anuales (_annual_rows) --
    # sumar filas crudas (sin filtrar duracion) arriesgaria sumar un hecho
    # anual de una serie con uno trimestral de la otra que comparta 'end'.
    sga_rows = rows("sga") or _sum_two_series(_annual_rows(rows("sga_admin")), _annual_rows(rows("sga_selling")))
    sbc_rows = rows("share_based_comp")
    icf_rows, fcf_rows = rows("investing_cash_flow"), rows("financing_cash_flow")
    rd_by_end = {r["end"]: r["val"] for r in _annual_rows(rd_rows)}
    sga_by_end = {r["end"]: r["val"] for r in _annual_rows(sga_rows)}
    pretax_by_end = {r["end"]: r["val"] for r in _annual_rows(pretax_rows)}
    sbc_by_end = {r["end"]: r["val"] for r in _annual_rows(sbc_rows)}
    icf_by_end = {r["end"]: r["val"] for r in _annual_rows(icf_rows)}
    fcf_by_end = {r["end"]: r["val"] for r in _annual_rows(fcf_rows)}

    total_assets_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("total_assets"))}
    total_liabilities_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("total_liabilities"))}
    equity_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("equity"))}
    receivables_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("receivables"))}
    ppe_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("ppe_net"))}
    goodwill_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("goodwill"))}
    ap_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("accounts_payable"))}
    apic_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("apic"))}
    re_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("retained_earnings"))}
    aoci_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("aoci"))}

    interest_rows = rows("interest_expense")
    interest_by_end = {r["end"]: r["val"] for r in _annual_rows(interest_rows)}
    ltm_interest_expense = _ltm_value(interest_rows) or interest_by_end.get(ends[-1], 0.0)

    # --- Tercera tanda (ver _TAGS) ---
    sti_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("short_term_investments"))}
    intangibles_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("intangibles_net"))}
    lti_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("long_term_investments"))}
    lease_nc_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("lease_liability_noncurrent"))}
    unearned_by_end = {r["end"]: r["val"] for r in _annual_instant_rows(rows("unearned_revenue_current"))}

    ii_rows = rows("interest_investment_income")
    acq_rows = rows("business_acquisitions")
    issuance_rows = rows("stock_issuance")
    ii_by_end = {r["end"]: r["val"] for r in _annual_rows(ii_rows)}
    acq_by_end = {r["end"]: r["val"] for r in _annual_rows(acq_rows)}
    issuance_by_end = {r["end"]: r["val"] for r in _annual_rows(issuance_rows)}
    ltm_interest_investment_income = _ltm_value(ii_rows) or ii_by_end.get(ends[-1], 0.0)
    ltm_business_acquisitions = _ltm_value(acq_rows) or acq_by_end.get(ends[-1], 0.0)
    ltm_stock_issuance = _ltm_value(issuance_rows) or issuance_by_end.get(ends[-1], 0.0)
    ltm_basic_shares_avg = _ltm_average_value(basic_rows) or basic_by_end.get(ends[-1], 0.0)

    ltm_rd = _ltm_value(rd_rows) or rd_by_end.get(ends[-1], 0.0)
    ltm_sga = _ltm_value(sga_rows) or sga_by_end.get(ends[-1], 0.0)
    ltm_pretax_income = _ltm_value(pretax_rows) or pretax_by_end.get(ends[-1], 0.0)
    ltm_share_based_comp = _ltm_value(sbc_rows) or sbc_by_end.get(ends[-1], 0.0)
    ltm_investing_cash_flow = _ltm_value(icf_rows) or icf_by_end.get(ends[-1], 0.0)
    ltm_financing_cash_flow = _ltm_value(fcf_rows) or fcf_by_end.get(ends[-1], 0.0)

    # --- Cuarta tanda (ver _TAGS) ---
    cf_recv_rows = rows("cf_receivables_change")
    cf_pay_rows = rows("cf_payables_change")
    cf_tax_rows = rows("cf_income_tax_payable_change")
    cf_unearned_rows = rows("cf_unearned_revenue_change")
    purch_inv_rows = rows("purchases_of_investments")
    proceeds_inv_rows = rows("proceeds_from_investments")
    cf_recv_by_end = {r["end"]: r["val"] for r in _annual_rows(cf_recv_rows)}
    cf_pay_by_end = {r["end"]: r["val"] for r in _annual_rows(cf_pay_rows)}
    cf_tax_by_end = {r["end"]: r["val"] for r in _annual_rows(cf_tax_rows)}
    cf_unearned_by_end = {r["end"]: r["val"] for r in _annual_rows(cf_unearned_rows)}
    purch_inv_by_end = {r["end"]: r["val"] for r in _annual_rows(purch_inv_rows)}
    proceeds_inv_by_end = {r["end"]: r["val"] for r in _annual_rows(proceeds_inv_rows)}
    ltm_cf_receivables_change = _ltm_value(cf_recv_rows) or cf_recv_by_end.get(ends[-1], 0.0)
    ltm_cf_payables_change = _ltm_value(cf_pay_rows) or cf_pay_by_end.get(ends[-1], 0.0)
    ltm_cf_income_tax_payable_change = _ltm_value(cf_tax_rows) or cf_tax_by_end.get(ends[-1], 0.0)
    ltm_cf_unearned_revenue_change = _ltm_value(cf_unearned_rows) or cf_unearned_by_end.get(ends[-1], 0.0)
    ltm_purchases_of_investments = _ltm_value(purch_inv_rows) or purch_inv_by_end.get(ends[-1], 0.0)
    ltm_proceeds_from_investments = _ltm_value(proceeds_inv_rows) or proceeds_inv_by_end.get(ends[-1], 0.0)

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
        tax_expense=_series_at(tax_by_end),
        net_income=_series_at(ni_by_end),
        diluted_shares_avg=_series_at(diluted_shares_by_end),
        operating_cash_flow=_series_at(ocf_by_end),
        capex=_series_at(capex_by_end),
        buybacks=_series_at(buyback_by_end),
        dividends_paid=_series_at(dividend_by_end),
        cogs=_series_at(cogs_by_end),
        current_assets=_series_at(current_assets_by_end),
        current_liabilities=_series_at(current_liabilities_by_end),
        ltm_tax_expense=ltm_tax_expense,
        ltm_net_income=ltm_net_income,
        ltm_diluted_shares_avg=ltm_diluted_shares_avg,
        ltm_operating_cash_flow=ltm_operating_cash_flow,
        ltm_capex=ltm_capex,
        ltm_buybacks=ltm_buybacks,
        ltm_dividends_paid=ltm_dividends_paid,
        ltm_cogs=ltm_cogs,
        rd=_series_at(rd_by_end),
        sga=_series_at(sga_by_end),
        pretax_income=_series_at(pretax_by_end),
        total_assets=_series_at(total_assets_by_end),
        total_liabilities=_series_at(total_liabilities_by_end),
        equity=_series_at(equity_by_end),
        share_based_comp=_series_at(sbc_by_end),
        investing_cash_flow=_series_at(icf_by_end),
        financing_cash_flow=_series_at(fcf_by_end),
        receivables=_series_at(receivables_by_end),
        ppe_net=_series_at(ppe_by_end),
        goodwill=_series_at(goodwill_by_end),
        accounts_payable=_series_at(ap_by_end),
        apic=_series_at(apic_by_end),
        retained_earnings=_series_at(re_by_end),
        aoci=_series_at(aoci_by_end),
        ltm_rd=ltm_rd,
        ltm_sga=ltm_sga,
        ltm_pretax_income=ltm_pretax_income,
        ltm_share_based_comp=ltm_share_based_comp,
        ltm_investing_cash_flow=ltm_investing_cash_flow,
        ltm_financing_cash_flow=ltm_financing_cash_flow,
        interest_expense=_series_at(interest_by_end),
        ltm_interest_expense=ltm_interest_expense,
        short_term_investments=_series_at(sti_by_end),
        intangibles_net=_series_at(intangibles_by_end),
        long_term_investments=_series_at(lti_by_end),
        lease_liability_noncurrent=_series_at(lease_nc_by_end),
        unearned_revenue_current=_series_at(unearned_by_end),
        basic_shares_avg=_series_at(basic_by_end),
        interest_investment_income=_series_at(ii_by_end),
        business_acquisitions=_series_at(acq_by_end),
        stock_issuance=_series_at(issuance_by_end),
        ltm_basic_shares_avg=ltm_basic_shares_avg,
        ltm_interest_investment_income=ltm_interest_investment_income,
        ltm_business_acquisitions=ltm_business_acquisitions,
        ltm_stock_issuance=ltm_stock_issuance,
        cf_receivables_change=_series_at(cf_recv_by_end),
        cf_payables_change=_series_at(cf_pay_by_end),
        cf_income_tax_payable_change=_series_at(cf_tax_by_end),
        cf_unearned_revenue_change=_series_at(cf_unearned_by_end),
        purchases_of_investments=_series_at(purch_inv_by_end),
        proceeds_from_investments=_series_at(proceeds_inv_by_end),
        ltm_cf_receivables_change=ltm_cf_receivables_change,
        ltm_cf_payables_change=ltm_cf_payables_change,
        ltm_cf_income_tax_payable_change=ltm_cf_income_tax_payable_change,
        ltm_cf_unearned_revenue_change=ltm_cf_unearned_revenue_change,
        ltm_purchases_of_investments=ltm_purchases_of_investments,
        ltm_proceeds_from_investments=ltm_proceeds_from_investments,
    )
