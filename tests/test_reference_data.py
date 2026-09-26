from jmr_valuation.io.reference_data import COUNTRY_ERP_AS_OF, country_risk_premiums, get_country_erp


def test_country_erp_snapshot_matches_published_january_table():
    table = country_risk_premiums()
    assert COUNTRY_ERP_AS_OF == "2026-01"
    assert len(table) == 178
    assert table["Canada"].total_erp == 0.0423
    assert table["Colombia"].default_spread == 0.0187
    assert table["Colombia"].total_erp == 0.0708
    assert table["United States"].total_erp == 0.0446
    assert get_country_erp("Turkey").total_erp == 0.0889
    assert get_country_erp("Yemen").total_erp == 0.1977
