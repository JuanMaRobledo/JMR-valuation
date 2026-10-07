import unittest
from jmr_valuation.screener.europe import EUROPE, build_result, parse_annual


def fixture(currency='EUR', quote_currency='EUR', symbol='ASML.AS', missing=()):
    values = dict(TotalRevenue=1000, OperatingIncome=200, GrossProfit=400, NetIncome=150,
                  TaxProvision=50, PretaxIncome=250, OperatingCashFlow=300,
                  CapitalExpenditure=-100, TotalDebt=500, CashCashEquivalentsAndShortTermInvestments=100,
                  StockholdersEquity=600, EBITDA=250, OrdinarySharesNumber=10)
    blocks = [{ 'annual'+key: [dict(asOfDate=f'{year}-12-31', currencyCode=currency,
               reportedValue={'raw': value}) for year in range(2022, 2026)]}
              for key,value in values.items() if key not in missing]
    annual={'timeseries':{'result':blocks}}
    chart={'chart':{'result':[{'meta':{'currency':quote_currency,'regularMarketPrice':100,
                                       'regularMarketTime':1791331200}}]}}
    company=dict(ticker=symbol, name='Fixture', country='Países Bajos', region='Europa',sector='Industrials')
    return company, annual, chart


class EuropeanScreenTests(unittest.TestCase):
    def test_native_currency_ratios_and_fcf_sign(self):
        r=build_result(*fixture())
        self.assertEqual(r['valuation']['market_cap'],1000)
        self.assertEqual(r['valuation']['fcf_yield'],.2)
        self.assertEqual(r['valuation']['p_fcf'],5)
        self.assertEqual(r['valuation']['multiples']['ev_ebitda']['current'],5.6)
        self.assertAlmostEqual(r['metrics']['roic_last'],.16)
        self.assertNotIn('ltm',r['valuation'])

    def test_partial_history_never_scored_or_five_year(self):
        r=build_result(*fixture())
        self.assertIsNone(r['score'])
        self.assertFalse(r['quality']['passes_filters'])
        self.assertEqual(r['tier'],'Historia insuficiente')
        self.assertIsNone(r['metrics'].get('revenue_cagr_5y'))
        self.assertIsNone(r['metrics'].get('roic_median_5y'))
        self.assertIsNone(r['valuation']['multiples']['pe']['median_hist'])

    def test_pence_normalized_once(self):
        r=build_result(*fixture(currency='GBP',quote_currency='GBp',symbol='DGE.L'))
        self.assertEqual(r['currency'],'GBP')
        self.assertEqual(r['quote_scale'],.01)
        self.assertEqual(r['valuation']['price'],1)
        self.assertEqual(r['valuation']['market_cap'],10)

    def test_cross_currency_not_divided(self):
        r=build_result(*fixture(currency='USD',quote_currency='GBp',symbol='AZN.L'))
        self.assertIsNone(r['valuation']['pe'])
        self.assertIsNone(r['valuation']['market_cap'])
        self.assertFalse(r['valuation']['live_reprice'])

    def test_missing_capex_is_not_zero(self):
        r=build_result(*fixture(missing=('CapitalExpenditure',)))
        self.assertIsNone(r['valuation']['fcf_yield'])
        self.assertIsNone(r['valuation']['p_fcf'])

    def test_missing_debt_does_not_mean_debt_free(self):
        r=build_result(*fixture(missing=('TotalDebt',)))
        self.assertIsNone(r['metrics']['roic_last'])
        self.assertIsNone(r['metrics']['net_debt_to_ebitda'])
        self.assertIsNone(r['valuation']['multiples']['ev_ebit']['current'])

    def test_dual_classes_not_priced_as_whole_company(self):
        r=build_result(*fixture(symbol='NOVO-B.CO'))
        self.assertIsNone(r['valuation']['market_cap'])

    def test_post_fy_split_blocks_ratios(self):
        c,a,q=fixture()
        q['chart']['result'][0]['events']={'splits':{'x':{'date':1782864000,'numerator':2,'denominator':1}}}
        self.assertIsNone(build_result(c,a,q)['valuation']['pe'])

    def test_financials_excluded(self):
        c,a,q=fixture();c['sector']='Financials'
        r=build_result(c,{},q)
        self.assertEqual(r['tier'],'Excluida (financiera)')
        self.assertIsNone(r['score'])

    def test_bad_numbers_and_selection_unique(self):
        self.assertEqual(parse_annual({'timeseries':{'result':[{'annualTotalRevenue':[
            {'asOfDate':'2025-12-31','reportedValue':{'raw':float('nan')}}]}]}}),{})
        self.assertEqual(len(EUROPE),60)
        self.assertEqual(len({c['ticker'] for c in EUROPE}),60)
        self.assertEqual(len({c['country'] for c in EUROPE}),11)

if __name__=='__main__':unittest.main()
