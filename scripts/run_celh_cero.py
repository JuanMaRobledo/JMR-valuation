#!/usr/bin/env python
"""Valoración de Celsius Holdings, Inc. (CELH) DESDE CERO por segunda vez (5-oct-2026), sobre una copia nueva de la
plantilla maestra, con el prompt de valoración v4 y el de research v5 vigentes (fórmula única, tasas comunes, prima por
regiones, ventas/capital coherente con el ROIC y ambos horizontes). Reemplaza a la valoración del 1-oct-2026 (hoja
1E_s_A35yIAZRGatTIElusnMZs5NIvFJ9CUlGlqf7-j8, que queda sin cambios como referencia; sus fórmulas y las fichas anteriores
están en reference/backups/celh_anterior_2026-10-05/).

Fecha de corte: 30-sep-2026 (la de las tasas comunes de la cartera). Último reporte: 10-Q del 2T26 (6-ago-2026).

Particularidades de Celsius (todas como enlace + ajuste visible con nota, regla de la fórmula única):
  - EBIT normalizado: GAAP LTM + partidas de una vez SIN el acuerdo legal de 2026 (los costos legales se repiten:
    US$54,0M en 2024 y US$24,6M en 2026, con una investigación del fiscal de Texas y demandas abiertas).
  - Preferentes de PepsiCo a su valor de liquidación (Serie A US$550M + Serie B US$585M) y, en el capital invertido,
    a su valor contable (financiaron Rockstar y la capitanía).
  - Préstamo a plazo a valor nominal (US$694,75M); arrendamientos operativos por el conversor (US GAAP, Damodaran).
  - Split 3 por 1 del 15-nov-2023: acciones y BPA de 2016-2022 sin ajustar en el XBRL.
  - Balance LTM al 30-jun-2026 (el importador repetía el de dic-2025).

Pasos: refresh | split | balance | datos | costo | supuestos | presentacion | content   (--step all corre todos)
Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts python scripts/run_celh_cero.py --step datos
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

SHEET_ID = "1tHDLsh4yBF9NQkRLNqfTU6GPM5trOWsB5xIjpALLOIw"
TICKER = "CELH"
INDUSTRY = "Beverage (Soft)"  # Damodaran: MNST, KDP, KO, PEP, FIZZ, COCO, CELH
PEER_TICKERS = ["MNST", "KDP", "KO", "PEP", "FIZZ", "COCO"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "celh_desde_cero_2026-10-05.json"

VALUATION_DATE = date(2026, 9, 30)
PRICE_0930 = 27.35          # cierre del 30-sep-2026 (Nasdaq, yfinance)

# Partidas de una vez del EBIT GAAP de los últimos doce meses (jul-2025 a jun-2026), US$M, de las conciliaciones de los
# comunicados del 4T25 (26-feb-2026) y del 2T26 (6-ago-2026):
#   FY2025: terminación de distribuidores 327,461; compras e integración 59,524; step-up de inventario 22,448;
#           penalidades 0,710; reorganización 0,482.
#   1S26:   terminación 85,287; compras e integración 7,573.  (El acuerdo legal de 24,557 NO se suma: costo recurrente.)
#   1S25:   compras e integración 38,967; step-up 21,692; penalidades 0,710; reorganización 0,482.
ONE_OFFS_LTM = round((327.461 + 59.524 + 22.448 + 0.710 + 0.482) + (85.287 + 7.573)
                     - (38.967 + 21.692 + 0.710 + 0.482), 1)  # = 441,6

# Balance al 30-jun-2026 (10-Q 2T26, balance condensado), US$M.
BS_JUN26 = {
    "L3": 631.234, "L4": 0, "L5": 631.234, "L6": 735.336, "L8": 735.336,
    "L9": 390.602 + 67.422 + 49.472 + 1.895,           # inventarios + prepagos + costos diferidos + caja restringida
    "L10": 1875.961, "L11": 108.748, "L12": 99.529, "L13": 919.660,
    "L15": 1280.222 + 746.737 + 93.250 + 44.044,       # marcas + costos diferidos LP + impuesto diferido + otros
    "L16": 5168.151, "L18": 202.101, "L20": 7.000, "L22": 31.460,
    "L23": 264.558 + 40.821 + 8.761 + 453.043 + (42.891 - 7.000),  # devengados, impuestos, terminación, promociones, otros
    "L24": 1043.635, "L25": 667.850, "L26": 13.760,    # arrendamientos LP: último dato publicado (10-K 2025)
    "L27": 463.856 + 33.251 - 13.760, "L28": 1164.957, "L29": 2208.592,
    "L31": 1069.452, "L32": 0.335, "L33": 313.165, "L34": 1199.584, "L35": 1199.584, "L36": 5168.151,
}

# Split 3 por 1 del 15-nov-2023 (columnas Dec '16 .. Dec '22 del XBRL sin ajustar).
SPLIT_COLS = "BCDEFGH"
IS_SHARES_PRE = {25: [0, 0, 50.1, 60.8, 70.2, 73.8, 75.6], 26: [0, 0, 50.1, 64.2, 74.4, 77.7, 75.6],
                 27: [40, 45.7, 57, 68.9, 72.3, 74.9, 76.4]}
IS_EPS_PRE = {23: ["", "", -0.22, 0.16, 0.11, 0.05, -2.48], 24: ["", "", -0.22, 0.16, 0.11, 0.05, -2.48]}


def _dec(x: float) -> str:
    return str(x).replace(".", ",")


def step_refresh() -> None:
    ms.install_augmented_client(TICKER)
    rnm.run(TICKER, sheet_id=SHEET_ID, peer_tickers=PEER_TICKERS, industry_us=INDUSTRY, industry_global=INDUSTRY)


def step_split() -> None:
    sh = ms.open_sheet(SHEET_ID)
    cur = sh.worksheet("Income Statement").batch_get([f"B{r}:H{r}" for r in (25, 26, 27)], value_render_option="UNFORMATTED_VALUE")
    if cur and cur[2] and cur[2][0] and abs((cur[2][0][-1] or 0) - 76.4) > 0.5:
        print("split ya aplicado:", cur[2][0])
        return
    upd = {}
    for row, vals in IS_SHARES_PRE.items():
        upd.update({f"{c}{row}": round(v * 3, 1) for c, v in zip(SPLIT_COLS, vals)})
    for row, vals in IS_EPS_PRE.items():
        upd.update({f"{c}{row}": (round(v / 3, 3) if isinstance(v, (int, float)) else v) for c, v in zip(SPLIT_COLS, vals)})
    ms.write_with_backup(sh, "Income Statement", upd,
                         "Split 3x1 del 15-nov-2023: acciones x3 y BPA /3 en 2016-2022 (XBRL sin ajustar)", BACKUP_PATH)


def step_balance() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bs_f = sh.worksheet("Balance Sheet").batch_get(list(BS_JUN26), value_render_option="FORMULA")
    vals = {c: round(v, 3) for (c, v), f in zip(BS_JUN26.items(), bs_f)
            if not (f and f[0] and str(f[0][0]).startswith("="))}
    ms.write_with_backup(sh, "Balance Sheet", vals,
                         "LTM = balance al 30-jun-2026 (10-Q 2T26); el importador repetía el de dic-2025", BACKUP_PATH)


def step_datos() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    # Sin ms.fix_template_bugs / ms.fix_nwc_projection: la maestra ya trae esas correcciones con la fórmula única y
    # reescribirlas la desviaría (apply_canonical_formulas.py debe dar 0 celdas pendientes).
    inp = {
        "B4": ms.serial(VALUATION_DATE),
        "D1": PRICE_0930,
        "B13": f"='Income Statement'!L12+{_dec(ONE_OFFS_LTM)}",
        "B15": "='Balance Sheet'!L35+1759,975",
        "B16": "='Balance Sheet'!L20+'Balance Sheet'!L25+19,9",
        "B17": "No",
        "B18": "Yes",
        "B22": "='Income Statement'!L27+2,149",
        "B24": 0.201,
        "B38": "Yes", "B39": 2.313, "B40": 6.28, "B41": 3.96, "B42": 0.60,
        "A76": "Derechos preferentes separados (millones)",
        "B76": 1135,
        "A77": "Estado del tratamiento preferente",
        "B77": ("Valor de liquidación: Serie A US$550M + Serie B US$585M (10-Q 2T26). Conversión a US$25 (A) y US$51,75 (B) "
                "solo desde ago-2031 (automática, con requisito de participación) o ago-2032 (a opción de Celsius) y si la "
                "acción supera ese precio; redención desde 2032."),
    }
    ms.write_with_backup(sh, "Input sheet", inp, "Datos base CELH desde cero (10-Q 2T26, 10-K 2025, comunicados 4T25 y 2T26)", bk)
    notes = {
        "B13": (f"EBIT GAAP LTM (Income Statement L12) + {_dec(ONE_OFFS_LTM)} de partidas de una vez: terminación de "
                "distribuidores de Alani Nu (412,7; reembolsada en su mayoría por PepsiCo), compras e integración (28,1), "
                "step-up de inventario (0,8) y penalidades/reorganización. El acuerdo legal de 24,6 (1T26) NO se suma: Celsius "
                "registró 54,0 en 2024 y tiene litigios abiertos, así que se trata como costo recurrente. Fuentes: comunicados "
                "del 4T25 (26-feb-2026) y del 2T26 (6-ago-2026). Análisis desde cero del 5-oct-2026."),
        "B15": ("Patrimonio contable (Balance Sheet L35) + 1.759,975 del preferente en mezzanine (Serie A 852,355 + Serie B "
                "907,620; 10-Q 2T26): financió Rockstar y la capitanía de PepsiCo, así que forma parte del capital invertido."),
        "B16": ("Préstamo a plazo a valor nominal: corriente (L20, 7,0) + largo plazo neto (L25, 667,85) + 19,9 de descuento y "
                "costos de emisión = 694,75 (10-Q 2T26, nota 10; valor razonable ≈ principal). Arrendamientos por el conversor."),
        "B22": ("Acciones en circulación (Income Statement L27) + 2,149 millones de RSU/PSU sin consolidar al 30-jun-2026 "
                "(10-Q 2T26). Cobertura del 10-Q: 253.035.047 acciones al 31-jul-2026."),
        "B24": "Tasa efectiva del 1S26: 41,674 / 207,066 = 20,1% (10-Q 2T26). La LTM (8,8%) está distorsionada por las partidas de una vez.",
        "B76": "Preferentes de PepsiCo a valor de liquidación (550 + 585), no al contable (1.760): ver B77.",
    }
    sh.worksheet("Input sheet").update_notes(notes)
    ms.write_with_backup(sh, "Operating lease converter", {
        "E5": 5.7, "B8": 5.012, "B9": 5.189, "B10": 4.008, "B11": 3.699, "B12": 0.680, "B13": 2.018,
    }, "Arrendamientos operativos: gasto 2025 y compromisos al 31-dic-2025 (10-K 2025, nota de arrendamientos)", bk)


def step_costo() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Single Business(US)",  # bottom-up Beverage (Soft) 0,58 → 0,62 reapalancada (revisión del 5-oct-2026)
        "B26": "Operating regions",
        "H22": "", "H23": 13.0, "H24": "", "H25": "", "H26": "", "H27": "", "H28": "",
        "H29": 2422.5, "H30": 72.5, "H31": "", "H32": 7.3,   # ventas 2025 por región (10-K 2025)
        "B33": 5.75,          # préstamo a plazo con vencimiento en 2032
        "B34": "Direct Input",
        "B35": 0.065,         # SOFR + 2,25% tras la enmienda del 15-jul-2026; intereses del 2T26 anualizados ≈ 6,7%
    }, "Costo de capital CELH desde cero: beta bottom-up, prima por regiones, Kd real", BACKUP_PATH)
    sh.worksheet("Cost of capital worksheet").update_notes({
        "B23": "No se usa: la beta sale de «Single Business(US)» (ver nota de B22). Hasta el 5-oct-2026 se usaba 1,0 escrita a mano.",
        "B35": "SOFR + 2,25% (segunda enmienda del crédito, 8-K del 15-jul-2026). Intereses del 2T26: 11,566 / 694,75 × 4 ≈ 6,7%.",
    })


def step_supuestos() -> None:
    """Caso Base de la hoja = historia Base (los cuatro escenarios están en reference/damodaran/CELH.json)."""
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Input sheet", {
        "B27": 0.059,   # año 1 de la historia Base (suma de marcas: CELSIUS −3%, Alani Nu +12%, Rockstar con un año completo)
        "B28": 0.196,   # margen normalizado del 2T26 (19,6%) + 0,09 pp de arrendamientos ≈ 19,6%
        "B29": 0.045,   # CAGR años 2-5 de la historia Base (5,2%, 5,0%, 4,1%, 3,7%)
        "B30": 0.201,   # 20% en base reportada + 0,09 pp del ajuste de arrendamientos
        "B31": 5,
        "B32": 1.8,     # rendimiento sobre el capital nuevo 20% × 75% × 1,8 = 27%, bajo el de la industria (29%)
        "B33": 1.6,     # 24% sobre el capital nuevo en los años 6-10; industria Beverage (Soft) 1,54-1,68
        "B49": "No",    # sin ventaja defendible: ROIC terminal = costo de capital
    }, "Supuestos Base CELH desde cero (5-oct-2026) = historia Base", BACKUP_PATH)
    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": "Crecimiento"}, "Tipo de empresa CELH", BACKUP_PATH)
    # Otros ingresos / EBIT proyectado (supuesto escrito a mano, prompt v4): el promedio de 2023-2025 de la maestra (+8%)
    # supone ingresos financieros netos, pero desde el préstamo de abr-2025 Celsius paga intereses netos. LTM (2025 + 1S26 −
    # 1S25): ingresos por intereses 15,9 − gasto por intereses 54,3 + otros 19,8 = −18,6, −3,1% del EBIT normalizado.
    ms.write_with_backup(sh, "Financials Multiples", {"E11": -0.03, "E50": -0.03, "E90": -0.03},
                         "Otros ingresos / EBIT proyectado = −3% (costo financiero neto LTM)", BACKUP_PATH)
    sh.worksheet("Financials Multiples").update_notes({c: (
        "Supuesto escrito a mano (5-oct-2026): −3% del EBIT. LTM jun-2026: ingresos por intereses 15,9 − gasto por intereses "
        "54,3 + otros 19,8 = −18,6 sobre EBIT normalizado 601,9 (comunicados del 4T25 y del 2T26). El promedio de 3 años de "
        "la plantilla (+8%) venía de cuando Celsius tenía caja neta sin deuda.") for c in ("E11", "E50", "E90")})


def step_presentacion() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Descuento de múltiplos", {
        "A38": "DCF activo hoy · escenarios de las historias",
        "C38": "='Escenarios e historias'!H6", "D38": "='Escenarios e historias'!H5", "E38": "='Escenarios e historias'!H8",
        "A43": "Precio con MOS sobre el valor esperado", "C43": "", "D43": "='Escenarios e historias'!H14", "E43": "",
    }, "DCF activo = historias; MOS sobre el esperado (presentación vigente)", BACKUP_PATH)


def step_content() -> None:
    import celh_cero_content as cc

    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", cc.CUALITATIVO, "Contenido cualitativo CELH desde cero (5-oct-2026)", bk)
    ms.write_with_backup(sh, "Estadísticas", cc.ESTADISTICAS, "Estadísticas CELH (fórmulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", cc.STORIES, "Historia CELH", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", cc.SUPUESTOS_RECOMENDADOS, "Recomendaciones CELH", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": cc.MULTIPLOS_EVALUACION}, "Evaluación de múltiplos CELH", bk)
    cc.format_estadisticas(sh)
    cc.write_tesis(sh, bk)  # después hay que volver a correr apply_multiples_v3 --apply (agrega el origen de los múltiplos)


STEPS = {"refresh": step_refresh, "split": step_split, "balance": step_balance, "datos": step_datos, "costo": step_costo,
         "supuestos": step_supuestos, "presentacion": step_presentacion, "content": step_content}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--step", choices=[*STEPS, "all"], nargs="+", default=["all"])
    args = parser.parse_args(argv)
    for name, fn in STEPS.items():
        if name in args.step or "all" in args.step:
            print(f"== {name}")
            fn()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
