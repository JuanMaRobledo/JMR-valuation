import pytest

from jmr_valuation.models.relative import resolve_anchor_multiple


def test_resolve_anchor_multiple_uses_median_of_3_years():
    assert resolve_anchor_multiple([30, 26, 28]) == 28  # mediana de [26,28,30]


def test_resolve_anchor_multiple_override_wins_when_active():
    assert resolve_anchor_multiple([30, 26, 28], override_value=15.5) == 15.5


def test_resolve_anchor_multiple_requires_exactly_3_years():
    with pytest.raises(ValueError):
        resolve_anchor_multiple([30, 26])


def test_resolve_anchor_multiple_override_of_zero_is_respected():
    # override_value=0.0 (casilla activada con 0 cargado) NO es lo mismo que
    # "no hay override" -- eso ahora se expresa con None, no con 0.
    assert resolve_anchor_multiple([10, 12, 14], override_value=0.0) == 0.0


def test_resolve_anchor_multiple_none_override_falls_back_to_median():
    assert resolve_anchor_multiple([10, 12, 14], override_value=None) == 12
