#!/usr/bin/env python
"""Valoracion de McDonald's Corporation (MCD) sobre la hoja provista por el
usuario (copia de la plantilla maestra vigente, carpeta de Drive 'MCD'),
siguiendo el prompt maestro de valoracion Damodaran v2 y el mismo proceso
generico de NKE/NVDA (refresh_native_model.run) mas supuestos y contenido a
medida (mcd_content.py).

Pasos: refresh | assumptions | content  (--step all corre todos)
Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts python scripts/run_mcd.py --step all
"""
from __future__ import annotations

import argparse
import sys
from dataclasses import replace
from datetime import date
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402
import refresh_native_model as rnm  # noqa: E402

SHEET_ID = "1USPRKTTdnXcWAEoAQoVq9CJXH1ENPLQkP1k_SW0Rnp8"
TICKER = "MCD"
INDUSTRY = "Restaurant/Dining"
PEER_TICKERS = ["YUM", "QSR", "DPZ", "CMG", "WEN", "SBUX"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "mcd_formula_backup.json"
VALUATION_DATE = date(2026, 9, 25)  # ultimo cierre disponible (viernes)

# D&A total real (tag us-gaap:DepreciationAndAmortization del estado de flujo
# de caja, 10-K). El loader toma primero DepreciationDepletionAndAmortization,
# que en MCD desde 2018 es solo una partida menor (US$300-466M): subestimaba
# el EBITDA ~US$1.800M/año desde 2020. LTM = FY2025 - 1S2025 + 1S2026.
DA_10K = [1516.5, 1363.4, 1482.0, 1617.9, 1751.4, 1868.1, 1871.0, 1978.0, 2097.0, 2199.0]
DA_LTM = 2199.0 - 1064.0 + 1131.0
# Desde 2023 MCD taggea las acciones promedio EN MILLONES (732,3 en vez de
# 732.300.000): el loader las tomaba como 0 y el EPS 2023-LTM salia en
# millones. Se reescalan; LTM diluido = promedio ponderado 1S2026 (10-Q).
LTM_DILUTED_SHARES = 712.3e6
LTM_BASIC_SHARES = 709.9e6


def _fix_series(series):
    fix = lambda xs: [x * 1e6 if 0 < x < 1e5 else x for x in xs]  # noqa: E731
    return replace(
        series,
        shares_outstanding=fix(series.shares_outstanding),
        diluted_shares_avg=fix(series.diluted_shares_avg),
        basic_shares_avg=fix(series.basic_shares_avg),
        ltm_diluted_shares_avg=LTM_DILUTED_SHARES,
        ltm_basic_shares_avg=LTM_BASIC_SHARES,
        da=[v * 1e6 for v in DA_10K],
        ltm_da=DA_LTM * 1e6,
    )


def step_refresh() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Input sheet", {"B4": ms.serial(VALUATION_DATE)}, "Fecha de valoracion MCD", BACKUP_PATH)
    ms.install_augmented_client(TICKER)
    loader = rnm.load_annual_series_from_sec_edgar
    rnm.load_annual_series_from_sec_edgar = lambda t, *a, **k: (
        _fix_series(loader(t, *a, **k)) if t == TICKER else loader(t, *a, **k))
    rnm.run(TICKER, sheet_id=SHEET_ID, peer_tickers=PEER_TICKERS, industry_us=INDUSTRY, industry_global=INDUSTRY)
    # La plantilla vigente ya calcula el precio del analisis con el cierre
    # historico de B4 (Input!B23 -> Resumen!B3 -> C25); refresh_resumen_valoracion
    # lo pisa con un valor fijo, asi que se restaura la formula.
    ms.write_with_backup(sh, "Resumen de Valoración", {"C25": "=$B$3"},
                         "Precio del analisis vivo desde el cierre historico de B4 (plantilla vigente)", BACKUP_PATH)


def step_assumptions() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Input sheet", {
        "B17": "No",      # MCD no reporta I+D
        "B18": "No",      # arrendamientos operativos (~US$14.700M) ya en balance (ASC 842); su costo esta en el EBIT
        # Base. Investor Day 23-sep-2026 (8-K): refranquiciar de ~95% a ~98% a fines
        # de 2028 (~60% de los US$9.690M de ventas de locales propios pasan a
        # renta+regalias), nuevas unidades ~2,5% del crecimiento de ventas del
        # sistema en 2027, margen operativo "low-to-mid 50%" en 2030.
        "B27": -0.02,     # Año 1: ventas del sistema +4-5% menos la baja contable del refranquiciamiento
        "B28": 0.475,     # margen Año 1: LTM 46,2%, guia 2026 "mid-to-high 40%", G&A empieza a bajar en 2027
        "B29": 0.02,      # años 2-5: 2028 todavia refranquicia (~-4%), 2029-30 ~+4,5% (unidades + comps)
        "B30": 0.53,      # margen objetivo: rango "low-to-mid 50%" 2030 menos amortizacion del apoyo a franquiciados
        "B31": 5,         # objetivo a 2030
        "B32": 1.0,       # sales-to-capital 1-5: capex ~US$3.000M/año + apoyo NEXT vs D&A ~US$2.300M
        "B33": 1.2,       # 6-10: fin del programa NEXT de capex extraordinario
        "B35": 0.0518,    # UST 10 años al 25-sep-2026 (^TNX)
        # Perpetuidad. Default de la plantilla: WACC terminal = rf + ERP (9,27%) y
        # ROIC = WACC desde el año 11 (DCF Base US$147). Para MCD (beta desapalancada
        # 0,66, rating Baa1/BBB+, ROIC actual ~25% por el modelo de franquicia +
        # dueño del inmueble) eso equivale a volverla una empresa promedio sin moat:
        "B46": "Yes", "B47": 0.0825,  # WACC terminal: WACC actual (7,9%) + 0,3pp de prudencia
        "B49": "Yes", "B50": 0.12,    # ROIC terminal: la mitad del actual, por encima del WACC (renta + regalias)
    }, "Supuestos MCD Base (ver hoja Tesis de Inversión y Supuestos)", bk)
    ms.write_with_backup(sh, "Country equity risk premiums", {
        "B2": 0.0409, "C2": "Updated September 1, 2026",
    }, "ERP de mercado maduro (Damodaran, 1-sep-2026)", bk)
    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Single Business(Global)",  # Restaurant/Dining global (~60% de ingresos fuera de EE.UU.)
        "B26": "Country of Incorporation",
        "B33": 10,                          # vencimiento promedio aproximado (bonos hasta 2050+)
        "B34": "Actual rating",
        "B36": "Baa1/BBB+",                 # Moody's Baa1 (jul-2025), S&P BBB+ (abr-2025), ambos estables
    }, "Costo de capital MCD (rating real Baa1/BBB+)", bk)
    ms.write_with_backup(sh, "Valuation output", {
        # Conservador: la regla MIN(Año1; 2-5)-1,5pp usaria el -2% del refranquiciamiento
        # para los 5 años (-3,5% anual, absurdo); se baja cada tramo 1,5pp por separado.
        "C55": "='Input sheet'!B27-0,015", "D55": "='Input sheet'!B29-0,015",
        # Conservador: el cambio de mezcla por refranquiciar sube el margen aun sin
        # eficiencias; "sin mejora operativa" = margen Año 1, no el Año 0.
        "C45": "='Input sheet'!B28",
        # Optimista: +1pp por tramo; margen objetivo Base +3pp (tope del rango "mid 50%").
        "C106": "='Input sheet'!B27+0,01", "D106": "='Input sheet'!B29+0,01",
        "C47": "='Input sheet'!B30+0,03",
    }, "Escenarios MCD: orden Conservador < Base < Optimista", bk)
    # Multiplo Base = 0,78 x mediana de los 4 cierres (regla de la Calculadora, Paso 5):
    # el minimo de 4 años (P/E 25,5x, EV/EBITDA 17,9x) exige volver a los multiplos
    # de 2022-2025, muy por encima de lo que el mercado paga hoy (19x / 14x) y de los peers.
    for sheet in ("PE", "EVEBITDA", "EVFCFF", "PFCFE", "POCF"):
        ms.write_with_backup(sh, sheet, {"J19": "=0,78*MEDIAN(B19:E19)"},
                             "Multiplo Base MCD: 0,78 x mediana 4 cierres (regla Calculadora)", bk)
    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": "Defensiva", "G4": 0.25},
                         "Tipo de empresa MCD; MOS 25% (hipotesis Estandar: moat claro, deuda investment grade)", bk)
    ms.write_with_backup(sh, "Control de valoración", {
        "E5": "Yahoo Finance / GOOGLEFINANCE (cierre NYSE 25-sep-2026)",
        "E6": "USD (millones; acciones en millones)",
        "E7": ms.serial(date(2026, 6, 30)),
        "E8": "SEC EDGAR: 10-K FY2025 y 10-Q 2T2026 (CIK 0000063908)",
    }, "Control de valoracion MCD", bk)


def step_content() -> None:
    import mcd_content as mc
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", mc.CUALITATIVO, "Contenido cualitativo MCD", bk)
    ms.write_with_backup(sh, "Estadísticas", mc.ESTADISTICAS, "Estadisticas MCD (formulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", mc.STORIES, "Historia MCD", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", mc.SUPUESTOS_RECOMENDADOS, "Recomendaciones MCD", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {
        "C5": "Base (0,78 × mediana 4 cierres, fijado a mano)", "A12": mc.MULTIPLOS_EVALUACION,
    }, "Evaluacion de multiplos MCD", bk)
    mc.format_estadisticas(sh)
    mc.write_tesis(sh, bk)


STEPS = {"refresh": step_refresh, "assumptions": step_assumptions, "content": step_content}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--step", choices=[*STEPS, "all"], default="all")
    args = ap.parse_args(argv)
    for name, fn in STEPS.items():
        if args.step in (name, "all"):
            fn()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
