#!/usr/bin/env python
"""Valoracion de Autodesk, Inc. (ADSK) en una COPIA NUEVA de la plantilla
maestra (Drive: AAA Finanzas > Análisis > ADSK > Modelo_JMR_ADSK), con el
mismo proceso de 9 pasos que NKE/PYPL y los pasos genericos de
scripts/model_steps.py.

Particularidades de Autodesk que este script resuelve:
  - Año fiscal a enero: el ultimo dato es el 10-Q de Q2 FY2027 (31-jul-2026,
    presentado 28-ago-2026); LTM = ago-2025 a jul-2026.
  - El pipeline deja el balance LTM (columna L) con el cierre de FY2026
    (31-ene-2026) salvo la caja -> se reemplaza por el balance real al
    31-jul-2026 (10-Q Q2 FY2027).
  - MaintainX: comprada el 3-ago-2026 (despues del cierre del Q2) por
    US$3.530M en efectivo, neto de la caja adquirida. El balance al 31-jul
    ya tiene el prestamo puente (US$994M) pero todavia no el pago -> la caja
    del modelo se ajusta pro forma (Input!B19 = caja - 3.530). La emision de
    notas de sep-2026 (US$1.000M) solo refinancia el prestamo: neutra.
  - SG&A LTM quedaba igual al de FY2026 y el gasto por intereses (fila 16)
    sumaba ingreso + gasto -> se recalculan.

Pasos: refresh | assumptions | content  (--step all corre todos)
Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts python scripts/run_adsk.py --step all
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

SHEET_ID = "17eku40NKWd72OBZEQ85diKEaNNSH1zuJrnhG6ucmJok"  # Análisis/ADSK/Modelo_JMR_ADSK
TICKER = "ADSK"
INDUSTRY = "Software (System & Application)"  # Damodaran indname.xls: ADSK, PTC, BSY, CDNS, SNPS, ADBE
PEER_TICKERS = ["PTC", "BSY", "CDNS", "SNPS", "ADBE", "INTU"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "adsk_formula_backup.json"
VALUATION_DATE = date(2026, 9, 25)

MAINTAINX_CASH_PAID = 3530  # US$M, neto de caja adquirida (cierre 3-ago-2026)

# Gasto bruto por intereses. FY2023-FY2026: tag InterestExpense (10-K).
# FY2017-FY2022 no esta taggeado -> intereses pagados (InterestPaidNet) como
# proxy. LTM = FY2026 (80) - H1 FY2026 (37) + H1 FY2027 (Q1 21 + Q2 ~22
# estimado: el 10-Q de Q2 solo taggea el neto). Columnas B..K = FY17..FY26, L = LTM.
INTEREST_EXPENSE = [47.6, 54.6, 59, 67.8, 63, 58, 83, 71, 71, 80, 86]

# Balance al 31-jul-2026 (10-Q Q2 FY2027), US$M.
BALANCE_JUL2026 = {
    "L3": 4098, "L4": 57, "L5": 4098 + 57,
    "L6": 684, "L8": 684, "L9": 831, "L10": 5670,
    "L11": 124, "L12": 423, "L13": 4331,
    "L14": 202 + 392,  # titulos negociables LP + inversiones estrategicas (sin valor razonable facil)
    "L15": 12983 - 5670 - 124 - 423 - 4331 - 594, "L16": 12983,
    "L18": 457, "L20": 994 + 499,  # prestamo puente MaintainX + notas 3,5% jun-2027
    "L21": 52, "L22": 4036, "L23": 6628 - 457 - 1493 - 52 - 4036, "L24": 6628,
    "L25": 1985, "L26": 175, "L27": (12983 - 3383 - 6628) - 1985 - 175, "L28": 12983 - 3383 - 6628,
    "L29": 12983 - 3383,
    "L31": 4846, "L32": -233, "L33": -1230, "L34": 3383, "L35": 3383, "L36": 12983,
}


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
        # SG&A LTM = FY2026 (3.066) + H1 FY2027 (1.209 + 341) - H1 FY2026 (1.125 + 330)
        "L8": 3161,
        # Otros gastos operativos (plug): Bruto - SG&A - D&A - I+D - EBIT
        "L11": 7108 - 3161 - 201 - 1721 - 2041,
    }, "Intereses brutos (fila 16 sumaba ingreso+gasto) y SG&A LTM (quedaba igual a FY2026)", bk)
    ms.write_with_backup(sh, "Balance Sheet", {**BALANCE_JUL2026, "K21": 52},
                        "Balance LTM real al 31-jul-2026 (el pipeline dejaba el de ene-2026)", bk)

    ms.write_with_backup(sh, "Input sheet", {
        "B4": ms.serial(VALUATION_DATE),
        # Caja pro forma: ya se pagaron US$3.530M por MaintainX (3-ago-2026).
        "B19": f"='Balance Sheet'!L5-{MAINTAINX_CASH_PAID}",
        "B20": "='Balance Sheet'!L14",
        "B17": "Yes",     # I+D = 22% de los ingresos: se capitaliza (3 años)
        "B18": "No",      # arrendamientos ya incluidos en la deuda (filas 21/26)
        "B27": 0.13,      # Crecimiento Año 1 (Base)
        "B28": 0.295,     # Margen Año 1 (Base, basis ajustado por I+D)
        "B29": 0.10,      # CAGR años 2-5 (Base)
        "B30": 0.335,     # Margen objetivo (Base, basis ajustado por I+D)
        "B31": 5,         # Años de convergencia
        "B32": 1.5,       # Sales to capital años 1-5
        "B33": 1.5,       # Sales to capital años 6-10
        "B35": 0.0517,    # UST 10 años al 25-sep-2026
        # ROIC en crecimiento estable: 15% en vez de ROIC = WACC (9,3%). Foso
        # de estandar (AutoCAD/DWG, Revit); ROIC actual ~36%. Sin el override
        # el DCF Base da US$152 (ver log de la Tesis).
        "B49": "Yes",
        "B50": 0.15,
    }, "Supuestos ADSK (ver hoja Tesis de Inversión y Supuestos)", bk)

    ms.write_with_backup(sh, "Country equity risk premiums", {
        "B2": 0.0409, "C2": "Updated September 1, 2026",
    }, "ERP de mercado maduro (Damodaran, 1-sep-2026)", bk)

    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Single Business(Global)",  # beta desapalancada Software (System & Application) global
        "B33": 5,                          # vencimiento promedio ponderado de las notas tras la emision de sep-2026
        "B34": "Direct Input",
        # Rating partido A3 (Moody's) / BBB+ (S&P): spread 1,0% entre A3/A- (0,89%) y Baa2/BBB (1,11%).
        # Las notas a 2033 salieron al 5,65% (sep-2026), consistente.
        "B35": "='Input sheet'!B35+0,01",
    }, "Cost of capital ADSK", bk)

    ms.write_with_backup(sh, "Valuation output", {
        # Conservador: el margen se estanca en el actual (mismo basis ajustado por I+D).
        "C45": "=MIN('Valuation output'!B6;'Input sheet'!B28)",
        # Optimista: margen tipo Adobe/Cadence (+3pp sobre el Base).
        "C47": "='Input sheet'!B30+0,03",
    }, "Escenarios ADSK: orden Conservador < Base < Optimista", bk)

    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": "Software"}, "Tipo de empresa ADSK", bk)
    rnm.refresh_resumen_valoracion(sh, TICKER, rnm.get_market_snapshot(TICKER))


def step_content() -> None:
    import adsk_content as ac

    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", ac.CUALITATIVO, "Contenido cualitativo ADSK", bk)
    ms.write_with_backup(sh, "Estadísticas", ac.ESTADISTICAS, "Estadisticas ADSK (formulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", ac.STORIES, "Historia ADSK", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", ac.SUPUESTOS_RECOMENDADOS, "Recomendaciones ADSK", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": ac.MULTIPLOS_EVALUACION}, "Evaluacion de multiplos ADSK", bk)
    ac.format_estadisticas(sh)
    ac.write_tesis(sh, bk)


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
