#!/usr/bin/env python
"""Valoracion de NIKE, Inc. (NKE) sobre la plantilla maestra, con el mismo
proceso de 9 pasos que PYPL (ver scripts/run_pypl.py) y los pasos
genericos de scripts/model_steps.py.

Particularidades de Nike que este script resuelve:
  - Año fiscal a mayo: el ultimo dato es el 10-K de FY2026 (31-may-2026);
    el 10-Q de Q1 FY2027 recien sale el 1-oct-2026, asi que LTM = FY2026.
  - El EBIT de FY2026 (US$3.797M) incluye un reembolso UNICO de aranceles
    IEEPA de ~US$986M (Q4, +900pb de margen bruto). Se normaliza el EBIT
    base (Input!B13) a US$2.811M (6,1%) y los US$684M todavia no cobrados
    (cuenta por cobrar al 31-may) se suman como activo no operativo.
  - Intereses: Nike reporta ingreso por intereses (US$278M) y el neto
    (US$50M a favor); el gasto bruto (US$228M) no esta taggeado -> filas
    15/16 del Income Statement se recalculan como ingreso - neto.
  - Sin I+D separado (B17 = No).

Pasos: refresh | assumptions | content  (--step all corre todos)
Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts python scripts/run_nke.py --step all
"""
from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402
import refresh_native_model as rnm  # noqa: E402

SHEET_ID = "1BAuhp8QPzXQx1osCIBHA4QoFC91DStgSr3h4SjFkAL4"
TICKER = "NKE"
INDUSTRY = "Shoe"  # Damodaran indname.xls (ene-2026): NKE, DECK, ONON, CROX, BIRK, PUMA
PEER_TICKERS = ["DECK", "ONON", "CROX", "BIRK", "LULU", "UAA"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "nke_formula_backup.json"
VALUATION_DATE = date(2026, 9, 22)

TARIFF_REFUND = 986          # US$M, reconocido en Q4 FY2026 (comunicado 30-jun-2026)
TARIFF_REFUND_UNCOLLECTED = 986 - 302  # cobrado US$302M al 31-may-2026

# Gasto bruto por intereses = ingreso por intereses (InvestmentIncomeInterest)
# - neto (InterestIncomeExpenseNonoperatingNet); FY17-FY21 sin ingreso
# taggeado -> el neto es todo gasto. Columnas B..K = FY17..FY26, L = LTM.
INTEREST_EXPENSE = [59, 54, 49, 89, 262, 299, 291, 269, 297, 228, 228]


def step_refresh() -> None:
    ms.install_augmented_client(TICKER)
    rnm.run(TICKER, sheet_id=SHEET_ID, peer_tickers=PEER_TICKERS, industry_us=INDUSTRY, industry_global=INDUSTRY)


def step_assumptions() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.fix_template_bugs(sh, bk)
    ms.fix_nwc_projection(sh, bk)

    cols = "BCDEFGHIJKL"
    ms.write_with_backup(sh, "Income Statement", {
        **{f"{c}15": -v for c, v in zip(cols, INTEREST_EXPENSE)},
        **{f"{c}16": v for c, v in zip(cols, INTEREST_EXPENSE)},
    }, "Gasto por intereses bruto (ingreso por intereses - neto); el pipeline ponia el INGRESO como gasto", bk)
    ms.write_with_backup(sh, "Balance Sheet", {"K21": 502, "L21": 478},
                         "Porcion corriente de arrendamientos operativos (31-may-2026)", bk)

    ms.write_with_backup(sh, "Input sheet", {
        "B4": ms.serial(VALUATION_DATE),
        # EBIT base normalizado: sin el reembolso unico de aranceles.
        "B13": f"='Income Statement'!L12-{TARIFF_REFUND}",
        # Activos no operativos: inversiones LP (0) + reembolso de aranceles por cobrar.
        "B20": f"='Balance Sheet'!L14+{TARIFF_REFUND_UNCOLLECTED}",
        "B17": "No",      # Nike no reporta I+D por separado
        "B27": -0.02,     # Crecimiento Año 1 (Base)
        "B28": 0.065,     # Margen Año 1 (Base)
        "B29": 0.035,     # CAGR años 2-5 (Base)
        "B30": 0.11,      # Margen objetivo (Base)
        "B31": 7,         # Años de convergencia
        "B32": 2.1,       # Sales to capital años 1-5
        "B33": 2.1,       # Sales to capital años 6-10
        "B35": 0.0496,    # UST 10 años al 22-sep-2026
    }, "Supuestos NKE (ver hoja Tesis de Inversión y Supuestos)", bk)

    ms.write_with_backup(sh, "Country equity risk premiums", {
        "B2": 0.0409, "C2": "Updated September 1, 2026",
    }, "ERP de mercado maduro (Damodaran, 1-sep-2026)", bk)

    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Single Business(Global)",  # beta de industria Shoe (0,89) ~ mediana de comparables (1,06)
        "B33": 9,                          # vencimiento promedio ponderado de la deuda (10-K FY2026)
        "B34": "Actual rating",
        "B36": "A2/A",                     # Moody's A2 (nov-2025) / S&P A+
    }, "Cost of capital NKE", bk)

    ms.write_with_backup(sh, "Valuation output", {
        # Conservador: la recuperacion se estanca en el margen del Año 1.
        "C45": "='Input sheet'!B28",
        # Optimista: vuelve al margen promedio FY2021-FY2024 (pre-deterioro).
        "C47": "=AVERAGE('Income Statement'!F13:I13)",
        # Conservador: caida de un digito bajo-medio que persiste 5 años
        # (guia H1 FY27: caida de un digito bajo a medio). Antes =PROMEDIO(B27;rf).
        "C55": "='Input sheet'!B27-0,01",
        # Optimista: antes =B27*1,3 -> con B27 NEGATIVO daba un crecimiento
        # MENOR que el Base (bug #11). Ahora: recuperacion rapida, CAGR Base + 1pp.
        "C106": "='Input sheet'!B29+0,01",
    }, "Escenarios NKE: orden Conservador < Base < Optimista", bk)

    # Paso 6: el FCFE de FY2026 fue NEGATIVO (-US$734M) -> el MIN de 4 años
    # del P/FCFE da -93x. Multiplo objetivo = implicito del propio DCF de cada
    # escenario (valor del equity / FCFE FY+1 del mismo escenario).
    ms.write_with_backup(sh, "PFCFE", {
        "J8": "='Valuation output'!B84/'Financials Multiples'!E29",
        "J19": "='Valuation output'!B33/'Financials Multiples'!E68",
        "J30": "='Valuation output'!B135/'Financials Multiples'!E108",
    }, "P/FCFE objetivo implicito del DCF (FCFE FY2026 negativo)", bk)

    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": "Madura"}, "Tipo de empresa NKE", bk)
    rnm.refresh_resumen_valoracion(sh, TICKER, rnm.get_market_snapshot(TICKER))


def step_content() -> None:
    import nke_content as nc

    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", nc.CUALITATIVO, "Contenido cualitativo NKE", bk)
    ms.write_with_backup(sh, "Estadísticas", nc.ESTADISTICAS, "Estadisticas NKE (formulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", nc.STORIES, "Historia NKE", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", nc.SUPUESTOS_RECOMENDADOS, "Recomendaciones NKE", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": nc.MULTIPLOS_EVALUACION}, "Evaluacion de multiplos NKE", bk)
    nc.format_estadisticas(sh)
    nc.write_tesis(sh, bk)


STEPS = {"refresh": step_refresh, "assumptions": step_assumptions, "content": step_content}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--step", choices=[*STEPS, "all"], default="all")
    args = parser.parse_args(argv)
    for name, fn in STEPS.items():
        if args.step in (name, "all"):
            fn()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
