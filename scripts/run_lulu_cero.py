#!/usr/bin/env python
"""Valoración de lululemon athletica inc. (LULU) DESDE CERO sobre una copia nueva de la plantilla maestra (2-oct-2026),
con el prompt de valoración v4 y el de research v5. Reemplaza a la valoración anterior (hoja
1Skav94fUb3IYvhsucWI1MQAcN6LH-VQ87Z_7KCImu3g, que queda sin cambios como referencia).

Pasos: refresh | assumptions | supuestos | presentacion | content
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

SHEET_ID = "1wuEhOhrjlL5t-oSO9sRd7Py0Vw-47rv_4AAwaS8-ZJw"
TICKER = "LULU"
INDUSTRY = "Apparel"  # Damodaran indname de lululemon
PEER_TICKERS = ["NKE", "ADDYY", "ONON", "DECK", "UAA", "BIRK", "GAP"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "lulu_desde_cero_2026-10-02.json"


def step_refresh() -> None:
    ms.install_augmented_client(TICKER)
    rnm.run(TICKER, sheet_id=SHEET_ID, peer_tickers=PEER_TICKERS, industry_us=INDUSTRY, industry_global=INDUSTRY)


VALUATION_DATE = date(2026, 10, 1)
PRICE_1001 = 95.86          # cierre del 1-oct-2026 (Nasdaq)
RF_1001 = 0.0524            # UST 10 años, cierre del 1-oct-2026 (^TNX 5,237)
ERP_SEP26 = 0.0409          # Damodaran, 1-sep-2026

# EBIT normalizado (US$M) de los últimos doce meses (ago-2025 a jul-2026 = FY2025 − 1S25 + 1S26):
#   − devolución de aranceles IEEPA del 2T26 (costo de ventas, una vez): 134,5
#   + costos de la disputa por poderes con Chip Wilson (1T26 11,4 + 2T26 13,4): 24,8
#   + costos de transición del CEO de FY2025 (10-K): 15,2
TARIFF_REFUND = 134.5
PROXY_COSTS = 11.4 + 13.4
CEO_TRANSITION = 15.2

# Balance al 2-ago-2026 (comunicado y 10-Q del 2T26), US$M. Arrendamientos corrientes y tarjetas de regalo separados.
BS_AUG26 = {
    "L3": 1389.737, "L4": 0, "L5": 1389.737, "L6": 171.164, "L8": 171.164,
    "L9": 1711.450 + 479.948 + 364.452 - 171.164, "L10": 3945.587,
    "L11": 2046.363, "L12": 188.370 - 184.9, "L13": 184.9, "L14": 0, "L15": 1947.077 + 357.181, "L16": 8484.578,
    "L18": 346.717, "L20": 0, "L21": 366.649, "L22": 277.318, "L23": 584.912 + 122.747 + 67.375 + 35.933,
    "L24": 1801.651, "L25": 0, "L26": 1774.478, "L27": 56.987 + 60.288, "L28": 1774.478 + 56.987 + 60.288,
    "L29": 1801.651 + 1774.478 + 56.987 + 60.288,
    "L31": 669.4, "L32": -230.7, "L33": 4791.174 - 669.4 + 230.7, "L34": 4791.174, "L35": 4791.174, "L36": 8484.578,
    # 1-feb-2026 (10-K FY2025): arrendamientos corrientes y tarjetas de regalo fuera de "otros pasivos corrientes"
    "K21": 298.724, "K22": 316.632, "K23": 1556.1 - 298.724 - 316.632,
}


def step_assumptions() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.fix_template_bugs(sh, bk)
    ms.fix_nwc_projection(sh, bk)
    ms.write_with_backup(sh, "Balance Sheet", BS_AUG26, "LTM = balance al 2-ago-2026 (10-Q del 2T26)", bk)
    ms.write_with_backup(sh, "Income Statement", {"L27": 105.594 + 5.116},
                         "Acciones al 28-ago-2026: 105,594M comunes + 5,116M intercambiables (portada del 10-Q)", bk)

    ms.write_with_backup(sh, "Input sheet", {
        "B4": ms.serial(VALUATION_DATE),
        "D1": PRICE_1001,
        "B13": f"='Income Statement'!L12-{str(TARIFF_REFUND).replace('.', ',')}+{round(PROXY_COSTS + CEO_TRANSITION)}",
        "B14": "='Income Statement'!L15",  # sin deuda financiera: 0; el gasto por arrendamientos entra por el conversor
        "B16": "='Balance Sheet'!L20+'Balance Sheet'!L25", "C16": "='Balance Sheet'!K20+'Balance Sheet'!K25",
        "B17": "No",       # lululemon no informa I+D por separado
        "B18": "Yes",      # arrendamientos operativos como deuda (Damodaran)
        "B20": 0,
        # Acciones: comunes + intercambiables (110,71M) + 0,759M RSU + 0,288M PSU sin consolidar (10-Q 2T26)
        "B22": "='Income Statement'!L27+0,759+0,288",
        "B24": 0.30,       # tasa efectiva 29,5% (FY2025) y guía de ~30% para 2026
        "B35": RF_1001,
        "B38": "Yes", "B39": 1.525, "B40": 258.81, "B41": 4.0, "B42": 0.437,  # opciones 10-Q 2T26; vol. 43,7%
        "B60": "Yes",      # la tasa efectiva (~30%) se mantiene: lululemon tributa en Canadá y EE.UU. por encima del 25%
    }, "Datos base LULU desde cero (10-Q 2T26, 10-K FY2025, comunicado del 3-sep-2026)", bk)

    ms.write_with_backup(sh, "Operating lease converter", {
        "E5": 405.987, "B8": 370.705, "B9": 391.976, "B10": 334.124, "B11": 287.375, "B12": 182.005, "B13": 537.635,
    }, "Arrendamientos operativos: gasto FY2025 y compromisos al 1-feb-2026 (10-K FY2025, nota de arrendamientos)", bk)

    ms.write_with_backup(sh, "Country equity risk premiums", {
        "B2": ERP_SEP26, "C2": "Damodaran, implied ERP September 1, 2026",
    }, "ERP de mercado maduro (Damodaran, 1-sep-2026)", bk)

    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Single Business(Global)",  # beta de la industria Apparel global; regresión 1,13 (2a) / 1,20 (5a)
        "B26": "Will Input",
        "B27": ERP_SEP26,
        "B33": 5,
        "B34": "Direct Input",
        "B35": 0.059,      # sin deuda calificada: tasa incremental de los arrendamientos ≈ UST + ~0,7 pp
    }, "Costo de capital LULU: beta de industria, ERP sep-2026, Kd de arrendamientos", bk)

    ms.write_with_backup(sh, "Valuation output", {
        "B33": "=B31-B32-N('Input sheet'!$B$76)",
        "B84": "=B82-B83-N('Input sheet'!$B$76)",
        "B135": "=B133-B134-N('Input sheet'!$B$76)",
    }, "Fórmula estándar con preferentes (B76 vacío en LULU)", bk)


def step_supuestos() -> None:
    """Supuestos del caso Base de la hoja = historia Base (paso 4 del prompt v4); las cuatro historias están en
    reference/damodaran/LULUN.json."""
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Direct Input",
        "B23": 1.15,   # regresión semanal 1,13 (2 años) y 1,20 (5 años); Apparel global reapalancada 0,79 (ver texto)
    }, "Beta LULU: marca única de moda deportiva discrecional; la de Apparel (0,79) mezcla fabricantes diversificados", BACKUP_PATH)
    ms.write_with_backup(sh, "Input sheet", {
        "B27": -0.065,  # año 1 de la historia Base: guía 2026 (ventas −5% a −7%; 3T −10% a −11%) y Américas −11%
        "B28": 0.125,   # guía 2026 sin la devolución de aranceles: BPA ~US$8,7 -> margen ~13% en 2026; 1S27 débil
        "B29": 0.039,   # CAGR años 2-5 de la historia Base (Américas se estabiliza; China y resto del mundo 6-8%)
        "B30": 0.1845,  # 17% en base reportada + 1,45 pp del ajuste de arrendamientos
        "B31": 5,
        "B32": 1.8,     # entre la industria (1,5) y la rotación propia (~2,0 con arrendamientos)
        "B33": 1.8,
        # Criterio de ventaja (reference/moat_2026-09-30.json, LULUN): marca de 28 años que gana muy por encima de su costo de
        # capital pero se desvanece (comparables de Américas −12%, rebajas) -> punto medio entre el costo de capital
        # terminal y el ROIC de la industria (menor que el actual).
        "B49": "Yes", "B50": 0.126,
    }, "Supuestos Base LULU desde cero = historia Base (ver reference/damodaran/LULUN.json)", BACKUP_PATH)
    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": "Madura"}, "Tipo de empresa LULU", BACKUP_PATH)
    rnm.refresh_resumen_valoracion(sh, TICKER, rnm.get_market_snapshot(TICKER))


def step_presentacion() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Descuento de múltiplos", {
        "A38": "DCF activo hoy · escenarios de las historias",
        "C38": "='Escenarios e historias'!H6", "D38": "='Escenarios e historias'!H5", "E38": "='Escenarios e historias'!H8",
        "A43": "Precio con MOS sobre el valor esperado", "C43": "", "D43": "='Escenarios e historias'!H14", "E43": "",
    }, "DCF activo = historias; MOS sobre el esperado (presentación vigente 1-oct-2026)", BACKUP_PATH)


def step_content() -> None:
    import lulu_cero_content as lc

    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", lc.CUALITATIVO, "Contenido cualitativo LULU desde cero", bk)
    ms.write_with_backup(sh, "Estadísticas", lc.ESTADISTICAS, "Estadísticas LULU (fórmulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", lc.STORIES, "Historia LULU", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", lc.SUPUESTOS_RECOMENDADOS, "Recomendaciones LULU", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": lc.MULTIPLOS_EVALUACION}, "Evaluación de múltiplos LULU", bk)
    lc.format_estadisticas(sh)
    lc.write_tesis(sh, bk)  # después hay que volver a correr apply_multiples_v3 --apply (agrega el origen de los múltiplos)


STEPS = {"refresh": step_refresh, "assumptions": step_assumptions, "supuestos": step_supuestos,
         "presentacion": step_presentacion, "content": step_content}


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
