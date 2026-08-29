"""Arma un CompanyInputs a partir de datos de fiscal.ai -- TODAVIA NO TERMINADO.

Por que esta a medio hacer: mapear cada campo de CompanyInputs a un campo del
JSON de fiscal.ai requiere ver una respuesta real primero (los nombres exactos
de los campos no estan en la documentacion publica que pude revisar). Corre
`python scripts/inspect_fiscal_ai.py <TICKER> income-statement` (y los otros
endpoints) con tu API key, y con esa respuesta real se completa el mapeo de
abajo -- no tiene sentido adivinar nombres de campos y arriesgarse a que
carguen numeros mal etiquetados en el modelo.

Lo que si esta listo: la conexion (`FiscalAIClient`), y el esqueleto de esta
funcion con todos los campos que hay que llenar, marcados con TODO.
"""
from __future__ import annotations

from jmr_valuation.io.fiscal_ai_client import FiscalAIClient
from jmr_valuation.io.inputs import CompanyInputs


def load_company_inputs_from_fiscal_ai(ticker: str, client: FiscalAIClient | None = None) -> CompanyInputs:
    client = client or FiscalAIClient()

    income = client.income_statement(ticker)
    balance = client.balance_sheet(ticker)
    cash_flow = client.cash_flow_statement(ticker)
    ratios = client.ratios(ticker)
    prices = client.stock_prices(ticker)
    shares = client.shares_outstanding(ticker)
    profile = client.company_profile(ticker)

    raise NotImplementedError(
        "El mapeo de campos todavia no esta escrito -- ver el docstring del modulo. "
        "Los datos ya se pueden pedir (arriba); falta solo saber en que llave de "
        "cada respuesta vive cada numero. Las variables income/balance/cash_flow/"
        "ratios/prices/shares/profile ya tienen el JSON crudo de fiscal.ai; "
        "imprimilas (o corre scripts/inspect_fiscal_ai.py) para ver su forma real."
    )

    # TODO una vez que se vea la forma real de cada respuesta, completar asi:
    # return CompanyInputs(
    #     ticker=ticker,
    #     company_name=profile["..."],
    #     country_of_incorporation=profile["..."],
    #     industry_us=profile["..."],
    #     industry_global=profile["..."],
    #     revenue_ltm=income["..."],
    #     revenue_prior_10k=income["..."],
    #     ebit_ltm=income["..."],
    #     ebit_prior_10k=income["..."],
    #     interest_expense_ltm=income["..."],
    #     interest_expense_prior_10k=income["..."],
    #     book_value_equity_ltm=balance["..."],
    #     book_value_equity_prior_10k=balance["..."],
    #     book_value_debt_ltm=balance["..."],
    #     book_value_debt_prior_10k=balance["..."],
    #     cash_ltm=balance["..."],
    #     cash_prior_10k=balance["..."],
    #     shares_outstanding=shares["..."],
    #     current_price=prices["..."],
    #     hist_multiple_pe_y1=ratios["..."], hist_multiple_pe_y2=ratios["..."], hist_multiple_pe_y3=ratios["..."],
    #     # ... y el resto de los campos de CompanyInputs.
    # )
