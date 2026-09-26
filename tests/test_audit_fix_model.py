"""Catalogo de correcciones de la auditoria de la plantilla (sin red)."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import audit_fix_model as afm  # noqa: E402
import model_presentation as mp  # noqa: E402


def _balanced(f: str) -> bool:
    depth = 0
    for ch in re.sub(r'"[^"]*"', "", f):
        depth += ch == "("
        depth -= ch == ")"
        if depth < 0:
            return False
    return depth == 0


def test_cada_celda_se_corrige_una_sola_vez():
    keys = [(f.sheet, f.cell) for f in afm.all_fixes()]
    assert len(keys) == len(set(keys))


def test_formulas_nuevas_bien_formadas_y_con_separador_es():
    for f in afm.all_fixes():
        if not (f.new or "").startswith("="):
            continue
        assert _balanced(f.new), f
        # la plantilla esta en es_ES: argumentos con ';' (nunca ',' fuera de decimales/rangos)
        sin_textos = re.sub(r'"[^"]*"', "", f.new)
        assert not re.search(r",\s*[A-Za-z$'(]", sin_textos), f


def test_la_formula_nueva_nunca_es_una_de_las_viejas():
    for f in afm.all_fixes():
        assert afm._norm(f.new) not in {afm._norm(o) for o in f.old}, f


def test_puente_ev_resta_deuda_neta_y_suma_caja():
    f = next(x for x in afm.all_fixes() if (x.sheet, x.cell) == ("EVEBITDA", "H21"))
    assert f.new == ("=(H19*H20-('Input sheet'!$B$16-'Input sheet'!$B$19-'Input sheet'!$B$20+'Input sheet'!$B$21))"
                     "/MAX('Financials Multiples'!$E$70;'Financials Multiples'!G70)")


def test_dividendo_acumulado_suma_los_tres_años():
    f = next(x for x in afm.all_fixes() if (x.sheet, x.cell) == ("PE", "H22"))
    assert f.new == "=SUM('Financials Multiples'!E74:G74)"


def test_a10_multiplo_b_usa_la_misma_definicion_que_c_e():
    f = next(x for x in afm.all_fixes() if (x.sheet, x.cell) == ("POCF", "B8"))
    assert "IFERROR" in f.new and "Trailing Valuation" not in f.new


def test_a11_endeudamiento_neto_crece_con_las_ventas_no_como_pct():
    f = next(x for x in afm.all_fixes() if (x.sheet, x.cell) == ("Financials Multiples", "E28"))
    assert "AVERAGE" not in f.new
    assert "$B$16" in f.new


def test_a12_mediana_de_acciones_excluye_el_periodo_ltm():
    f = next(x for x in afm.all_fixes() if (x.sheet, x.cell) == ("Financials Multiples", "F32"))
    assert f.new == "=MEDIAN(B32:D32)"


def test_a13_conservador_y_optimista_convergen_desde_su_propio_año_1():
    cons = next(x for x in afm.all_fixes() if (x.sheet, x.cell) == ("Valuation output", "D57"))
    opt = next(x for x in afm.all_fixes() if (x.sheet, x.cell) == ("Valuation output", "D108"))
    assert "$C$45" in cons.new and "$C$6" not in cons.new
    assert "$C$47" in opt.new and "$C$6" not in opt.new


def test_a14_margen_ebitda_con_iferror():
    f = next(x for x in afm.all_fixes() if (x.sheet, x.cell) == ("Income Statement", "L30"))
    assert f.new.startswith("=IFERROR(")


def test_a17_sales_to_capital_terminal_es_roic_sobre_margen_neto():
    f = next(x for x in afm.all_fixes() if (x.sheet, x.cell) == ("Stories to Numbers", "F13"))
    assert "M42" in f.new and "M6" in f.new and "M8" in f.new


def test_hoja_origen_formulas_balanceadas():
    for kind, cells, _ in mp.origen_rows():
        for c in cells:
            if str(c).startswith("="):
                assert _balanced(c), c
            else:
                assert not str(c).startswith(("+", "-")), c


def test_alto_de_fila_crece_con_el_texto():
    assert mp._lines("x" * 10, 300) == 1
    assert mp._lines("x" * 400, 300) > 3
