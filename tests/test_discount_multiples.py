"""Formulas de la hoja 'Descuento de múltiplos' y del bloque de valor hoy del Resumen (sin red)."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import discount_multiples as dm  # noqa: E402


def _balanced(f: str) -> bool:
    depth = 0
    for ch in re.sub(r'"[^"]*"', "", f):
        depth += ch == "("
        depth -= ch == ")"
        if depth < 0:
            return False
    return depth == 0


def _cell(rows, addr):
    col, row = re.match(r"([A-Z])(\d+)", addr).groups()
    return rows[int(row) - 1][ord(col) - 65]


def test_every_formula_is_balanced_and_uses_semicolons():
    for rows in (dm.sheet_values(), dm.resumen_values()):
        for row in rows:
            for v in row:
                if v.startswith("="):
                    assert _balanced(v), v
                    assert not re.search(r"\w,\w", re.sub(r'"[^"]*"', "", v)), v  # separador de argumentos ';' (hoja en es)


def test_each_scenario_reads_its_own_row_of_the_multiple_sheets_and_discounts_by_n():
    rows = dm.sheet_values()
    for (name, src_row, _dcf, _col) in dm.SCENARIOS:
        first = dm.FIRST_ROW[name]
        for i, (sheet, _res_row) in enumerate(dm.METHODS):
            r = first + i
            assert _cell(rows, f"D{r}") == f"={sheet}!F{src_row}"
            assert _cell(rows, f"F{r}") == f"={sheet}!H{src_row}"
            assert "/(1+$B$5)" in _cell(rows, f"G{r}") and "^" not in _cell(rows, f"G{r}")
            # cada dividendo se descuenta en su año de pago (prompts del 2-oct-2026)
            div = dm.DEFAULT.div_rows[[s[0] for s in dm.SCENARIOS].index(name)]
            c1, c2 = f"N({sheet}!F{div})", f"N({sheet}!G{div})"
            assert _cell(rows, f"H{r}") == f'=IFERROR((E{r}-{c1})/(1+$B$5)^2+{c1}/(1+$B$5);"")'
            assert _cell(rows, f"I{r}") == (f'=IFERROR((F{r}-{c2})/(1+$B$5)^3+{c1}/(1+$B$5)'
                                            f'+({c2}-{c1})/(1+$B$5)^2;"")')
            assert f"AVERAGE(G{r}:I{r})" in _cell(rows, f"J{r}")


def test_vp_formulas_without_dividend_row_discount_the_total():
    assert dm._vp_formulas("PE", 20, None)[2] == '=IFERROR(F20/(1+$B$5)^3;"")'


def test_fy3_weighted_row_uses_capitalized_dcf_and_undiscounted_multiples():
    row = dm._fy3_weighted_row(dm.DEFAULT)
    assert row[0].startswith("Ponderado DCF capitalizado")
    assert row[3] == f"=IFERROR($B${dm.SUM_DCF}*'{dm.RES}'!D6+$B${dm.SUM_MULT}*D{dm.CHK_NOM};\"\")"


def test_resumen_keeps_the_cells_the_viewer_reads():
    rows = dm.resumen_values()
    at = lambda addr: rows[int(addr[1:]) - dm.RES_FIRST][ord(addr[0]) - 65]  # noqa: E731
    assert at("C32") == f"='{dm.SHEET}'!C{dm.SUM_DCF}"
    assert at("D33") == f"='{dm.SHEET}'!D{dm.SUM_MULT}"
    assert at("E34") == f"='{dm.SHEET}'!E{dm.SUM_W}"
    assert at("D36") == f"='{dm.SHEET}'!D{dm.SUM_MOS}"


def test_known_resumen_block_detection():
    assert dm._known_resumen_block([])
    assert dm._known_resumen_block([[""], ["VALOR POR ACCIÓN HOY | DCF + MÚLTIPLOS"]])
    assert not dm._known_resumen_block([[""], ["Notas propias del analista"]])
