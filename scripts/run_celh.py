#!/usr/bin/env python
"""Valoracion de Celsius Holdings, Inc. (CELH) DESDE CERO sobre una copia nueva
de la plantilla maestra (1-oct-2026), con el prompt de valoracion v4 y el de
research v5 (Modelo-JMR/docs/prompts). No toca la hoja anterior de CELH
(1pl_6BeI9gl_ciaSY5wDqyjRF9GS-ZhjXXK4wGVuBC4o): sirve solo para comparar al final.

Particularidades de Celsius que este script resuelve (ver step_assumptions):
  - Preferentes convertibles de PepsiCo (Serie A US$550M, Serie B US$585M de
    valor de liquidacion; 10-Q 2T26). Se restan por su valor economico, no por
    el contable en mezzanine.
  - Partidas de una vez en el EBIT LTM (terminacion de distribuidores, acuerdo
    legal) que deprimen el margen GAAP.
  - Compras de Alani Nu (abr-2025) y Rockstar (ago-2025): crecimiento comprado.

Pasos: refresh | assumptions | content  (--step all corre todos)
Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts python scripts/run_celh.py --step refresh
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

SHEET_ID = "1E_s_A35yIAZRGatTIElusnMZs5NIvFJ9CUlGlqf7-j8"
TICKER = "CELH"
INDUSTRY = "Beverage (Soft)"  # Damodaran indname: MNST, KDP, KO, PEP, FIZZ, COCO, CELH
PEER_TICKERS = ["MNST", "KDP", "KO", "PEP", "FIZZ", "COCO"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "celh_desde_cero_2026-10-01.json"


def step_refresh() -> None:
    ms.install_augmented_client(TICKER)
    rnm.run(TICKER, sheet_id=SHEET_ID, peer_tickers=PEER_TICKERS, industry_us=INDUSTRY, industry_global=INDUSTRY)


VALUATION_DATE = date(2026, 9, 30)
PRICE_0930 = 27.35          # cierre del 30-sep-2026 (Nasdaq, vía yfinance)
RF_0930 = 0.0529            # UST 10 años, cierre del 30-sep-2026 (^TNX 5,293)
ERP_SEP26 = 0.0409          # Damodaran, ERPSept26.xlsx C45 (reference/mature_market_erp.txt)

# Partidas de una vez en el EBIT GAAP de los últimos doce meses (jul-2025 a jun-2026), en US$M.
# FY2025 (comunicado 4T25, 26-feb-2026): terminación de distribuidores 327,461; compras e integración 59,524;
#   step-up de inventario 22,448; penalidades 0,710; reorganización 0,482.
# 1S26 (comunicado 2T26, 6-ago-2026): terminación 85,287; compras e integración 7,573; acuerdo legal 24,557.
# 1S25 (mismo comunicado): compras e integración 38,967; step-up 21,692; penalidades 0,710; reorganización 0,482.
ONE_OFFS_LTM = round((327.461 + 59.524 + 22.448 + 0.710 + 0.482) + (85.287 + 7.573 + 24.557)
                     - (38.967 + 21.692 + 0.710 + 0.482), 1)  # = 466,2

# Balance al 30-jun-2026 (10-Q 2T26, balance condensado), US$M. La columna L traía el de dic-2025.
BS_JUN26 = {
    "L3": 631.234, "L4": 0, "L6": 735.336, "L8": 735.336,
    "L9": 390.602 + 67.422 + 49.472 + 1.895,           # inventarios + prepagos + costos diferidos + caja restringida
    "L10": 1875.961, "L11": 108.748, "L12": 99.529, "L13": 919.660,
    "L15": 1280.222 + 746.737 + 93.250 + 44.044,       # marcas + costos diferidos LP + impuesto diferido + otros
    "L16": 5168.151, "L18": 202.101, "L20": 7.000, "L22": 31.460,
    "L23": 264.558 + 40.821 + 8.761 + 453.043 + (42.891 - 7.000),  # devengados, impuestos, terminación, promociones, otros
    "L24": 1043.635, "L25": 667.850, "L26": 13.760,    # arrendamientos LP: último dato publicado (10-K, dic-2025)
    "L27": 463.856 + 33.251 - 13.760, "L28": 1164.957, "L29": 2208.592,
    "L31": 1069.452, "L32": 0.335, "L33": 313.165, "L34": 1199.584, "L35": 1199.584, "L36": 5168.151,
}


def step_assumptions() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.fix_template_bugs(sh, bk)
    ms.fix_nwc_projection(sh, bk)

    bs_f = sh.worksheet("Balance Sheet").batch_get(list(BS_JUN26), value_render_option="FORMULA")
    vals = {c: round(v, 3) for (c, v), f in zip(BS_JUN26.items(), bs_f)
            if not (f and f[0] and str(f[0][0]).startswith("="))}
    ms.write_with_backup(sh, "Balance Sheet", vals,
                         "LTM = balance al 30-jun-2026 (10-Q 2T26); el pipeline repetía dic-2025 salvo la caja", bk)

    ms.write_with_backup(sh, "Input sheet", {
        "B4": ms.serial(VALUATION_DATE),
        "D1": PRICE_0930,
        # EBIT normalizado: GAAP LTM + partidas de una vez (ver ONE_OFFS_LTM). La compensación en acciones y la
        # amortización de intangibles comprados se quedan como costo.
        "B13": f"='Income Statement'!L12+{str(ONE_OFFS_LTM).replace('.', ',')}",
        # Capital invertido con el capital preferente (mezzanine contable 852,355 + 907,620; 10-Q 2T26), que financió
        # Rockstar y el pago implícito a PepsiCo: sin él, el ROIC actual se ve en 39% en vez de ~16,5%.
        "B15": "='Balance Sheet'!L35+1759,975",
        # Deuda a valor nominal: préstamo a plazo US$694,75M (10-Q 2T26; valor razonable ≈ principal). Los
        # arrendamientos entran por el conversor (B18), no por el balance.
        "B16": 694.75,
        "B17": "No",      # I+D de ~US$1-2M al año: inmaterial
        "B18": "Yes",     # arrendamientos operativos como deuda (Damodaran)
        # Acciones: 253,035M en circulación al 31-jul-2026 (portada del 10-Q) + 2,149M RSU sin consolidar.
        "B22": "='Income Statement'!L27+2,149",
        "B24": 0.201,     # tasa efectiva 1S26 (10-Q 2T26); la LTM (8,8%) está distorsionada por las partidas de una vez
        "B35": RF_0930,
        "B38": "Yes", "B39": 2.313, "B40": 6.28, "B41": 3.96, "B42": 0.60,  # opciones 10-K 2025; vol. 60% (10-Q)
        "A76": "Derechos preferentes separados (millones)",
        "B76": 1135,
        "A77": "Estado del tratamiento preferente",
        "B77": ("Valor de liquidación: Serie A US$550M + Serie B US$585M (10-Q 2T26). Conversión a US$25 (A) y "
                "US$51,75 (B) solo a opción de Celsius o automática; redención exigible por PepsiCo desde 2032."),
    }, "Datos base CELH desde cero (10-Q 2T26, 10-K 2025, comunicados 4T25 y 2T26)", bk)

    ms.write_with_backup(sh, "Operating lease converter", {
        "E5": 5.7, "B8": 5.012, "B9": 5.189, "B10": 4.008, "B11": 3.699, "B12": 0.680, "B13": 2.018,
    }, "Arrendamientos operativos: gasto 2025 y compromisos al 31-dic-2025 (10-K 2025, nota 7)", bk)

    ms.write_with_backup(sh, "Valuation output", {
        "B33": "=B31-B32-N('Input sheet'!$B$76)",
        "B84": "=B82-B83-N('Input sheet'!$B$76)",    # caso técnico Conservador
        "B135": "=B133-B134-N('Input sheet'!$B$76)",  # caso técnico Optimista
    }, "Resta las preferentes de PepsiCo (Input sheet B76) en los tres casos técnicos", bk)

    ms.write_with_backup(sh, "Country equity risk premiums", {
        "B2": ERP_SEP26, "C2": "Damodaran, implied ERP September 1, 2026",
    }, "ERP de mercado maduro (Damodaran, 1-sep-2026)", bk)

    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Direct Input",
        "B23": 1.0,
        "B26": "Will Input",
        "B27": ERP_SEP26,
        "B33": 5.75,             # préstamo a plazo con vencimiento abr-2032
        "B34": "Direct Input",
        "B35": 0.065,            # SOFR + 2,25% tras la enmienda del 15-jul-2026; intereses 2T26 anualizados ≈ 6,6%
    }, "Costo de capital CELH: beta 1,0 (bottom-up 0,58 ajustada por riesgo propio), ERP sep-2026, Kd real", bk)


def step_supuestos() -> None:
    """Supuestos del caso Base de la hoja = historia Base (paso 4 del prompt v4). Los cuatro escenarios activos
    están en reference/damodaran/CELHN.json; aquí solo se fija el Base técnico de la plantilla."""
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Input sheet", {
        "B27": 0.078,   # año 1 de la historia Base: 2S26 ≈ 2T26 (guía: 3T similar al 2T) + 1S27 con la categoría
        "B28": 0.20,    # margen normalizado del 2T26 (EBITDA ajustado 22,5% − D&A 1,2% − compensación en acciones 1,3%)
        "B29": 0.055,   # CAGR años 2-5 de la historia Base (categoría ~6-7%, Celsius y Rockstar ceden participación)
        "B30": 0.211,   # 21% en base reportada + 0,09 pp del ajuste de arrendamientos
        "B31": 5,
        "B32": 2.0,     # entre la industria (1,54-1,68) y la intensidad orgánica (capex ≈ D&A, capital de trabajo ~8%)
        "B33": 1.7,     # industria Beverage (Soft) global, 1,68
    }, "Supuestos Base CELH desde cero = historia Base (ver reference/damodaran/CELHN.json)", BACKUP_PATH)
    # Tipo de empresa (paso 8): utilidades y EBITDA GAAP volátiles por partidas de una vez -> más peso al DCF (60%)
    # y a los múltiplos de flujo, como en la categoría Crecimiento.
    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": "Crecimiento"}, "Tipo de empresa CELH", BACKUP_PATH)
    rnm.refresh_resumen_valoracion(sh, TICKER, rnm.get_market_snapshot(TICKER))  # congela el cierre del 30-sep-2026


def step_presentacion() -> None:
    """Fila 38 de 'Descuento de múltiplos' = DCF de las historias (Conservadora/Base/Optimista), como en las demás
    hojas desde el 1-oct-2026; fila 43 = precio con MOS sobre el DCF esperado de las historias."""
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Descuento de múltiplos", {
        "A38": "DCF activo hoy · escenarios de las historias",
        "C38": "='Escenarios e historias'!H6", "D38": "='Escenarios e historias'!H5", "E38": "='Escenarios e historias'!H8",
        "A43": "Precio con MOS sobre el valor esperado", "C43": "", "D43": "='Escenarios e historias'!H14", "E43": "",
    }, "DCF activo = historias; MOS sobre el esperado (presentación vigente 1-oct-2026)", BACKUP_PATH)


def step_content() -> None:
    import celh_content as cc

    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", cc.CUALITATIVO, "Contenido cualitativo CELH desde cero", bk)
    ms.write_with_backup(sh, "Estadísticas", cc.ESTADISTICAS, "Estadísticas CELH (fórmulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", cc.STORIES, "Historia CELH", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", cc.SUPUESTOS_RECOMENDADOS, "Recomendaciones CELH", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": cc.MULTIPLOS_EVALUACION}, "Evaluación de múltiplos CELH", bk)
    cc.format_estadisticas(sh)
    cc.write_tesis(sh, bk)  # después hay que volver a correr apply_multiples_v3 --apply (agrega el origen de los múltiplos)


STEPS = {"refresh": step_refresh, "assumptions": step_assumptions, "supuestos": step_supuestos, "presentacion": step_presentacion, "content": step_content}


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
