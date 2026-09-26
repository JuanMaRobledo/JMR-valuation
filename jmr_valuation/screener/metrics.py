"""Metricas de calidad de negocio para el screener de "empresas maravillosas".

Todo se calcula a partir de un `AnnualSeries` (historico anual de SEC EDGAR,
el mas viejo primero, hasta 10 FY + LTM) -- ver sec_edgar_loader.py. Este
modulo es puro (sin red): recibe la serie y devuelve numeros, para poder
testearlo con series armadas a mano.

Las metricas siguen el Paso 3 de modelo/METODOLOGIA.md (Modelo-JMR): deuda
neta/EBITDA, caja operativa y FCF, margenes y su tendencia, ROE vs ROIC
(actual y promedio 5 anios) y uso del capital (recompras/dilucion). Se suman
las que usa el enfoque Buffett/Munger para "negocio maravilloso": ROIC alto
Y sostenido, margen bruto alto y estable (proxy de poder de precio),
utilidades que se convierten en caja, y crecimiento del FCF por accion.

Convencion sobre faltantes: el loader deja en 0.0 los anios en que un tag no
se reporto. Para conceptos que nunca son 0 en una empresa real (ingresos,
patrimonio, costo de ventas, acciones) el 0.0 se trata como "sin dato"; para
la deuda, 0.0 es un valor legitimo (empresa sin deuda).
"""
from __future__ import annotations

import statistics
from dataclasses import asdict, dataclass

from jmr_valuation.io.sec_edgar_loader import AnnualSeries

DEFAULT_TAX_RATE = 0.21
WINDOW = 5  # "promedio 5 anios" de la metodologia


@dataclass(frozen=True)
class QualityMetrics:
    years: int
    last_fiscal_year_end: str
    ltm_revenue: float
    roic_observations_5y: int
    fcf_observations_5y: int
    # Rentabilidad sobre el capital
    roic_last: float | None
    roic_median_5y: float | None
    roic_min_5y: float | None
    roic_median_10y: float | None
    roe_median_5y: float | None
    # Margenes (poder de precio / moat)
    gross_margin_median_5y: float | None
    gross_margin_std_5y: float | None
    operating_margin_ltm: float | None
    operating_margin_median_5y: float | None
    # Caja
    fcf_ltm: float | None
    fcf_margin_median_5y: float | None
    fcf_positive_ratio: float | None      # anios con FCF > 0 / anios con dato (hasta 10)
    fcf_positive_last_5y: int | None      # cuantos de los ultimos 5 FY tuvieron FCF > 0
    fcf_conversion_5y: float | None       # suma FCF / suma utilidad neta, ultimos 5 FY
    # Crecimiento
    revenue_cagr_5y: float | None
    revenue_cagr_10y: float | None        # la ventana mas larga disponible (hasta 9 intervalos)
    revenue_growth_consistency: float | None  # % de anios con crecimiento positivo
    fcf_per_share_cagr_5y: float | None
    eps_cagr_5y: float | None
    # Balance
    net_debt_to_ebitda: float | None      # negativo = caja neta
    interest_coverage: float | None       # EBIT LTM / gasto financiero LTM
    negative_equity: bool
    # Uso del capital
    shares_cagr_5y: float | None          # negativo = recompras netas
    sbc_pct_revenue: float | None

    def as_dict(self) -> dict:
        return asdict(self)


def _nz(x: float | None) -> float | None:
    """0.0 del loader = sin dato (solo para conceptos que nunca son 0)."""
    return None if x is None or x == 0 else x


def _at(values: list[float], i: int) -> float | None:
    return values[i] if 0 <= i < len(values) else None


def _cagr(start: float | None, end: float | None, years: int) -> float | None:
    if start is None or end is None or years <= 0 or start <= 0 or end <= 0:
        return None
    return (end / start) ** (1 / years) - 1


def _median(values: list[float | None]) -> float | None:
    clean = [v for v in values if v is not None]
    return statistics.median(clean) if clean else None


def _tax_rate(tax: float | None, pretax: float | None) -> float:
    if tax is None or pretax is None or pretax <= 0:
        return DEFAULT_TAX_RATE
    rate = tax / pretax
    return rate if 0.0 <= rate <= 0.5 else DEFAULT_TAX_RATE


def _invested_capital(s: AnnualSeries, i: int) -> float | None:
    """Capital invertido operativo = patrimonio + deuda financiera - caja e
    inversiones de corto plazo. Si da <= 0 (patrimonio negativo por
    recompras, caso MCD/AAPL/HD), se usa capital empleado = activos totales
    - pasivos corrientes - caja: no depende del patrimonio contable y sigue
    midiendo el capital que el negocio realmente necesita para operar."""
    debt = (_at(s.long_term_debt, i) or 0.0) + (_at(s.current_debt, i) or 0.0)
    cash = (_at(s.cash, i) or 0.0) + (_at(s.short_term_investments, i) or 0.0)
    equity = _nz(_at(s.equity, i))
    if equity is not None:
        ic = equity + debt - cash
        if ic > 0:
            return ic
    assets = _nz(_at(s.total_assets, i))
    cur_liab = _at(s.current_liabilities, i) or 0.0
    if assets is not None:
        ce = assets - cur_liab - cash
        if ce > 0:
            return ce
    return None


def _roic(s: AnnualSeries, i: int) -> float | None:
    ebit = _at(s.ebit, i)
    if ebit is None or _nz(_at(s.revenue, i)) is None:
        return None
    ic_now = _invested_capital(s, i)
    ic_prev = _invested_capital(s, i - 1) if i > 0 else None
    # Capital promedio del anio cuando hay dato del cierre anterior -- evita
    # que una adquisicion grande al cierre hunda el ROIC de ese anio.
    ic = (ic_now + ic_prev) / 2 if ic_now and ic_prev else ic_now
    if not ic:
        return None
    nopat = ebit * (1 - _tax_rate(_nz(_at(s.tax_expense, i)), _nz(_at(s.pretax_income, i))))
    return nopat / ic


def _fcf(s: AnnualSeries, i: int) -> float | None:
    ocf = _nz(_at(s.operating_cash_flow, i))
    if ocf is None:
        return None
    return ocf - (_at(s.capex, i) or 0.0)


_SPLIT_FACTORS = (1.5, 2, 3, 4, 5, 6, 7, 8, 10, 15, 20, 25, 30, 40, 50)


def _split_factor(ratio: float) -> float | None:
    """Si el salto de acciones entre dos FY se parece a un split (o
    contrasplit) tipico, devuelve el factor exacto; si no, None."""
    for k in _SPLIT_FACTORS:
        for f in (k, 1 / k):
            if abs(ratio / f - 1) <= 0.06:
                return f
    return None


def share_counts(s: AnnualSeries) -> tuple[list[float | None], float | None]:
    """Acciones diluidas promedio por FY (y las de hoy, LTM), llevadas a la
    base de acciones del ultimo dato reportado.

    Dos problemas reales del XBRL que esto corrige:
    - Splits: el loader deja cada FY como se reporto en su momento, asi que
      un split (TSLA 5:1 en 2020 y 3:1 en 2022) aparece como una "dilucion"
      de +400% y arruina el CAGR de acciones, de EPS y de FCF por accion. Se
      recorre la serie de atras hacia adelante y, si el salto contra el anio
      siguiente se parece a un factor tipico de split (+-6%), se reescala.
    - Unidades: algunos FY vienen taggeados en miles (GRMN: 191.900 en vez de
      191.900.000; MCD: 716.400 en vez de 716 millones). Un valor por debajo
      de 500 mil acciones, o ~1000 veces menor que la mediana de la propia
      serie, se lleva a unidades.

    Un salto que no es ni split ni unidad (x50 o /50) se descarta."""
    n = len(s.revenue)
    raw = [
        _nz(_at(s.diluted_shares_avg, i)) or _nz(_at(s.basic_shares_avg, i)) or _nz(_at(s.shares_outstanding, i))
        for i in range(n)
    ]
    ltm = _nz(s.ltm_diluted_shares_avg) or _nz(s.ltm_basic_shares_avg)
    valid = [v for v in raw + [ltm] if v is not None and v > 0]
    typical = statistics.median(valid) if valid else 0.0
    series: list[float | None] = []
    for v in raw + [ltm]:
        if v is None or v <= 0:
            series.append(None)
            continue
        # En miles: absurdamente chico en absoluto, o ~1000x menor que la
        # mediana de la propia serie (MCD taggea 2023-2025 en miles).
        while v < 5e5 or (typical and v * 500 < typical):
            v *= 1000
        series.append(v)

    later: float | None = None
    for i in range(len(series) - 1, -1, -1):
        v = series[i]
        if v is None:
            continue
        if later is not None:
            ratio = later / v
            for unit in (1000.0, 0.001):  # FY en miles (o al reves) vs el anio siguiente
                if abs(ratio / unit - 1) < 0.1:
                    v *= unit
                    ratio /= unit
            if abs(ratio - 1) > 0.4:
                f = _split_factor(ratio)
                if f is not None:
                    v *= f
                elif ratio > 50 or ratio < 1 / 50:
                    series[i] = None
                    continue
            series[i] = v
        later = v
    current = series[-1] or next((x for x in reversed(series[:-1]) if x is not None), None)
    return series[:-1], current


def compute_metrics(s: AnnualSeries) -> QualityMetrics:
    n = len(s.revenue)
    last = n - 1
    idx_5y = list(range(max(0, n - WINDOW), n))

    revenue = [_nz(v) for v in s.revenue]
    roic = [_roic(s, i) for i in range(n)]
    roe = [
        (s.net_income[i] / s.equity[i]) if _at(s.equity, i) and s.equity[i] > 0 and _at(s.net_income, i) is not None else None
        for i in range(n)
    ]
    gross = [
        (revenue[i] - s.cogs[i]) / revenue[i] if revenue[i] and _nz(_at(s.cogs, i)) is not None else None
        for i in range(n)
    ]
    op_margin = [(s.ebit[i] / revenue[i]) if revenue[i] and _at(s.ebit, i) is not None else None for i in range(n)]
    fcf = [_fcf(s, i) for i in range(n)]
    fcf_margin = [(fcf[i] / revenue[i]) if fcf[i] is not None and revenue[i] else None for i in range(n)]

    gross_5y = [gross[i] for i in idx_5y if gross[i] is not None]
    fcf_known = [v for v in fcf if v is not None]
    fcf_5y = [fcf[i] for i in idx_5y]

    ni_5y = [_at(s.net_income, i) for i in idx_5y]
    fcf_conversion = None
    if all(v is not None for v in fcf_5y) and all(v is not None for v in ni_5y) and sum(ni_5y) > 0:
        fcf_conversion = sum(fcf_5y) / sum(ni_5y)

    growth_flags = [
        revenue[i] > revenue[i - 1] for i in range(1, n) if revenue[i] and revenue[i - 1]
    ]

    start_5y = n - 1 - WINDOW  # indice del FY de hace 5 anios
    shares, _ = share_counts(s)
    fcf_ps = [(fcf[i] / shares[i]) if fcf[i] is not None and shares[i] else None for i in range(n)]
    eps = [(s.net_income[i] / shares[i]) if _at(s.net_income, i) and shares[i] else None for i in range(n)]

    def cagr_5y(series: list[float | None]) -> float | None:
        if start_5y < 0:
            return None
        return _cagr(series[start_5y], series[last], WINDOW)

    # El D&A LTM del loader a veces sale incompleto (TSLA: 1.2B LTM vs 5.0B
    # del ultimo 10-K) -- si es menos del 60% del ultimo anual, se usa el anual.
    last_da = _at(s.da, last) or 0.0
    ltm_da = s.ltm_da if s.ltm_da >= 0.6 * last_da else last_da
    ltm_ebitda = s.ltm_ebit + ltm_da
    net_debt = (
        (_at(s.long_term_debt, last) or 0.0) + (_at(s.current_debt, last) or 0.0)
        - (_at(s.cash, last) or 0.0) - (_at(s.short_term_investments, last) or 0.0)
    )
    # Con EBITDA <= 0 el ratio no tiene lectura (ni "sano" ni "en alerta").
    nd_ebitda = net_debt / ltm_ebitda if ltm_ebitda > 0 else None

    ltm_revenue = s.ltm_revenue or (revenue[last] or 0.0)
    ltm_fcf = (s.ltm_operating_cash_flow - s.ltm_capex) if s.ltm_operating_cash_flow else fcf[last]

    return QualityMetrics(
        years=n,
        last_fiscal_year_end=s.fiscal_year_ends[last] if s.fiscal_year_ends else "",
        ltm_revenue=ltm_revenue,
        roic_observations_5y=sum(roic[i] is not None for i in idx_5y),
        fcf_observations_5y=sum(fcf[i] is not None for i in idx_5y),
        roic_last=roic[last],
        roic_median_5y=_median([roic[i] for i in idx_5y]),
        roic_min_5y=min((roic[i] for i in idx_5y if roic[i] is not None), default=None),
        roic_median_10y=_median(roic),
        roe_median_5y=_median([roe[i] for i in idx_5y]),
        gross_margin_median_5y=_median(gross_5y),
        gross_margin_std_5y=statistics.pstdev(gross_5y) if len(gross_5y) >= 3 else None,
        operating_margin_ltm=(s.ltm_ebit / ltm_revenue) if ltm_revenue else None,
        operating_margin_median_5y=_median([op_margin[i] for i in idx_5y]),
        fcf_ltm=ltm_fcf,
        fcf_margin_median_5y=_median([fcf_margin[i] for i in idx_5y]),
        fcf_positive_ratio=(sum(v > 0 for v in fcf_known) / len(fcf_known)) if fcf_known else None,
        fcf_positive_last_5y=sum(1 for v in fcf_5y if v is not None and v > 0) if any(v is not None for v in fcf_5y) else None,
        fcf_conversion_5y=fcf_conversion,
        revenue_cagr_5y=cagr_5y(revenue),
        revenue_cagr_10y=_cagr(revenue[0], revenue[last], last) if n >= 2 else None,
        revenue_growth_consistency=(sum(growth_flags) / len(growth_flags)) if growth_flags else None,
        fcf_per_share_cagr_5y=cagr_5y(fcf_ps),
        eps_cagr_5y=cagr_5y(eps),
        net_debt_to_ebitda=nd_ebitda,
        interest_coverage=(s.ltm_ebit / s.ltm_interest_expense) if s.ltm_interest_expense > 0 else None,
        negative_equity=bool(_at(s.equity, last) is not None and s.equity[last] < 0),
        shares_cagr_5y=cagr_5y(shares),
        sbc_pct_revenue=(s.ltm_share_based_comp / ltm_revenue) if ltm_revenue and s.ltm_share_based_comp else None,
    )
