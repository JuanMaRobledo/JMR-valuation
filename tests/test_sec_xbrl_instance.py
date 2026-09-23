from jmr_valuation.io.sec_xbrl_instance import _instance_filename, _merge, parse_instance

_XML = b"""<?xml version="1.0"?>
<xbrli:xbrl xmlns:xbrli="http://www.xbrl.org/2003/instance" xmlns:us-gaap="http://fasb.org/us-gaap/2025"
  xmlns:dei="http://xbrl.sec.gov/dei/2025" xmlns:pypl="http://www.paypal.com/20260630"
  xmlns:xbrldi="http://xbrl.org/2006/xbrldi" xmlns:iso4217="http://www.xbrl.org/2003/iso4217">
  <xbrli:context id="q2"><xbrli:entity><xbrli:identifier scheme="x">1</xbrli:identifier></xbrli:entity>
    <xbrli:period><xbrli:startDate>2026-04-01</xbrli:startDate><xbrli:endDate>2026-06-30</xbrli:endDate></xbrli:period></xbrli:context>
  <xbrli:context id="i"><xbrli:entity><xbrli:identifier scheme="x">1</xbrli:identifier></xbrli:entity>
    <xbrli:period><xbrli:instant>2026-06-30</xbrli:instant></xbrli:period></xbrli:context>
  <xbrli:context id="seg"><xbrli:entity><xbrli:identifier scheme="x">1</xbrli:identifier>
    <xbrli:segment><xbrldi:explicitMember dimension="a">b</xbrldi:explicitMember></xbrli:segment></xbrli:entity>
    <xbrli:period><xbrli:instant>2026-06-30</xbrli:instant></xbrli:period></xbrli:context>
  <xbrli:unit id="usd"><xbrli:measure>iso4217:USD</xbrli:measure></xbrli:unit>
  <dei:DocumentFiscalYearFocus contextRef="q2">2026</dei:DocumentFiscalYearFocus>
  <dei:DocumentFiscalPeriodFocus contextRef="q2">Q2</dei:DocumentFiscalPeriodFocus>
  <pypl:TechnologyAndDevelopmentExpense contextRef="q2" unitRef="usd" decimals="-6">849000000</pypl:TechnologyAndDevelopmentExpense>
  <us-gaap:DebtCurrent contextRef="i" unitRef="usd" decimals="-6">2505000000</us-gaap:DebtCurrent>
  <us-gaap:DebtCurrent contextRef="seg" unitRef="usd" decimals="-6">1</us-gaap:DebtCurrent>
</xbrli:xbrl>"""


def test_parse_instance_reads_undimensioned_facts_in_companyfacts_shape():
    out = parse_instance(_XML, accn="0001", form="10-Q", filed="2026-07-28")

    td = out["pypl"]["TechnologyAndDevelopmentExpense"]["units"]["USD"]
    assert td == [{"start": "2026-04-01", "end": "2026-06-30", "val": 849000000, "accn": "0001",
                   "form": "10-Q", "filed": "2026-07-28", "fy": 2026, "fp": "Q2"}]
    debt = out["us-gaap"]["DebtCurrent"]["units"]["USD"]
    assert [r["val"] for r in debt] == [2505000000]  # el hecho con segmento queda afuera


def test_merge_maps_custom_tag_without_duplicating_rows():
    facts = {"facts": {"us-gaap": {}}}
    node = parse_instance(_XML, accn="0001", form="10-Q", filed="2026-07-28")["pypl"]["TechnologyAndDevelopmentExpense"]
    _merge(facts, "us-gaap", "ResearchAndDevelopmentExpense", node)
    _merge(facts, "us-gaap", "ResearchAndDevelopmentExpense", node)

    assert len(facts["facts"]["us-gaap"]["ResearchAndDevelopmentExpense"]["units"]["USD"]) == 1


def test_instance_filename_prefers_inline_extracted_instance():
    items = [{"name": n} for n in ("FilingSummary.xml", "pypl-20260630_cal.xml", "pypl-20260630_htm.xml", "pypl-20260630.xsd")]
    assert _instance_filename(items) == "pypl-20260630_htm.xml"
    legacy = [{"name": n} for n in ("FilingSummary.xml", "pypl-20181231.xml", "pypl-20181231_lab.xml")]
    assert _instance_filename(legacy) == "pypl-20181231.xml"


def test_company_facts_keeps_companyfacts_data_when_a_filing_cannot_be_fetched(monkeypatch):
    from jmr_valuation.io import sec_xbrl_instance as mod
    from jmr_valuation.io.sec_edgar_client import SecEdgarClient

    base = {"cik": 1, "facts": {"us-gaap": {"Revenues": {"units": {"USD": [
        {"start": "2025-01-01", "end": "2025-12-31", "val": 1, "form": "10-K", "filed": "2026-02-01"}]}}}}}
    monkeypatch.setattr(SecEdgarClient, "company_facts", lambda self, t: base)
    monkeypatch.setattr(SecEdgarClient, "company_submissions", lambda self, t: {"filings": {"recent": {
        "form": ["10-Q"], "filingDate": ["2026-05-01"], "accessionNumber": ["0001-26-000001"]}}})

    def boom(self, cik, accn):
        raise RuntimeError("503")

    monkeypatch.setattr(mod.AugmentedSecEdgarClient, "_filing_instance", boom)

    facts = mod.AugmentedSecEdgarClient(user_agent="test x@y.z").company_facts("ABC")

    assert facts["facts"]["us-gaap"]["Revenues"]["units"]["USD"][0]["val"] == 1
