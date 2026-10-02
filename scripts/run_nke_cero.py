#!/usr/bin/env python
"""Valoración de NIKE, Inc. (NKE) DESDE CERO sobre una copia nueva de la plantilla maestra (2-oct-2026), con el
prompt de valoración v4 y el de research v5. Reemplaza a la valoración anterior (hoja
1BAuhp8QPzXQx1osCIBHA4QoFC91DStgSr3h4SjFkAL4, que queda sin cambios como referencia).

Fuentes: 10-K FY2026 (31-may-2026, 15-jul-2026) y comunicado del 1T FY2027 (31-ago-2026, publicado el 1-oct-2026).
El 10-Q del 1T FY2027 todavía no está en la SEC: el LTM (sep-2025 a ago-2026) se arma con el comunicado.

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

SHEET_ID = "1OITWNynG7R3PKC1sITOOazW9jzXgFWFda6qNbbOnYZI"
TICKER = "NKE"
INDUSTRY = "Shoe"  # Damodaran: NKE, DECK, ONON, CROX, BIRK
PEER_TICKERS = ["ADDYY", "DECK", "ONON", "LULU", "UAA", "CROX"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "nke_desde_cero_2026-10-02.json"


def step_refresh() -> None:
    ms.install_augmented_client(TICKER)
    rnm.run(TICKER, sheet_id=SHEET_ID, peer_tickers=PEER_TICKERS, industry_us=INDUSTRY, industry_global=INDUSTRY)


VALUATION_DATE = date(2026, 10, 1)
PRICE_1001 = 35.15          # cierre del 1-oct-2026 (el comunicado del 1T salió después del cierre)
RF_1001 = 0.0524            # UST 10 años, cierre del 1-oct-2026 (^TNX 5,237)
ERP_SEP26 = 0.0409          # Damodaran, 1-sep-2026 (reference/mature_market_erp.txt)

# EBIT normalizado (US$M): el LTM (sep-2025 a ago-2026) incluye el reembolso ÚNICO de aranceles IEEPA reconocido en el
# 4T FY26 (US$986M en el costo de ventas; 10-K FY26, "Other matters") y la indemnización por despidos de FY26 (US$385M).
TARIFF_REFUND = 986
SEVERANCE_FY26 = 385

# Gasto bruto por intereses = ingreso por intereses - neto (10-K). FY17-FY21 sin ingreso taggeado: el neto es todo
# gasto. Columnas B..K = FY17..FY26, L = LTM (el 1T no publica el bruto: se mantiene el de FY26).
INTEREST_EXPENSE = [59, 54, 49, 89, 262, 299, 291, 269, 297, 228, 228]

# LTM = FY26 - 1T FY26 + 1T FY27 (comunicado del 1-oct-2026; el 10-Q todavía no está en la SEC).
IS_LTM = {
    "L3": 46398 - 11720 + 11213, "L4": round((46398 - 11720 + 11213) / 46398 - 1, 4),
    "L5": 26487 - 6777 + 6415, "L6": 19911 - 4943 + 4798, "L7": round((19911 - 4943 + 4798) / 45891, 4),
    "L8": 16114 - 4016 + 3910, "L12": 3797 - 927 + 888, "L13": round(3758 / 45891, 4),
    "L14": 228 + 50 - 18 + 14,                      # ingreso por intereses = bruto + neto LTM (46)
    "L17": 3899 - 3758 - 46,                         # otros ingresos (gastos) netos
    "L18": 3899 - 3758, "L19": 3900 - 922 + 921, "L20": 792 - 195 + 209,
    "L21": 3108 - 727 + 712, "L22": 3108 - 727 + 712, "L23": 2.09, "L24": 2.09,
    "L25": 1483.6, "L26": 1484.2, "L27": 1483.5,    # acciones: portada del 10-K (8-jul-2026)
    "L28": 3758 + 747, "L29": round((792 - 195 + 209) / (3900 - 922 + 921), 4),
}

# Balance al 31-ago-2026 (comunicado 1T FY27). Arrendamientos corrientes separados de "otros pasivos corrientes".
BS_AUG26 = {
    "L3": 6903, "L4": 1465, "L5": 6903 + 1465, "L6": 5242, "L8": 5242, "L9": 7846 + 2217, "L10": 23673,
    "L11": 4887, "L12": 259, "L13": 240, "L14": 0, "L15": 2947 + 5788, "L16": 37794,
    "L18": 3420, "L20": 2000, "L21": 473, "L22": 0, "L23": 5338 + 178, "L24": 11409,
    "L25": 5893, "L26": 2706, "L27": 2566, "L28": 5893 + 2706 + 2566, "L29": 11409 + 11165,
    "L31": 15158, "L32": -141, "L33": 15220 - 15158 + 141, "L34": 15220, "L35": 15220, "L36": 37794,
    # 31-may-2026 y 31-may-2025 (10-K FY26): porción corriente de arrendamientos fuera de "otros pasivos corrientes"
    "K21": 478, "K23": 6092 + 377, "J21": 502, "J23": 5916 + 669,
}


def step_assumptions() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.fix_template_bugs(sh, bk)
    ms.fix_nwc_projection(sh, bk)

    cols = "BCDEFGHIJKL"
    ws = sh.worksheet("Income Statement")
    r14, r18 = (ws.get(r, value_render_option="UNFORMATTED_VALUE")[0] for r in ("B14:K14", "B18:K18"))
    num = lambda x: float(x or 0)  # noqa: E731
    upd = {f"{c}15": v for c, v in zip(cols, INTEREST_EXPENSE)}
    # Otros ingresos = total no operativo - (ingreso - gasto por intereses): el pipeline metía el gasto ahí.
    upd.update({f"{c}17": round(num(t) - (num(i) - v), 1)
                for c, i, t, v in zip(cols[:-1], r14, r18, INTEREST_EXPENSE)})
    upd.update(IS_LTM)
    ms.write_with_backup(sh, "Income Statement", upd,
                         "Intereses brutos (el pipeline ponía el ingreso como gasto) y LTM a ago-2026 (1T FY27)", bk)
    ms.write_with_backup(sh, "Balance Sheet", BS_AUG26, "LTM = balance al 31-ago-2026 (comunicado 1T FY27)", bk)

    ms.write_with_backup(sh, "Input sheet", {
        "B4": ms.serial(VALUATION_DATE),
        "D1": PRICE_1001,
        "B13": f"='Income Statement'!L12-{TARIFF_REFUND}+{SEVERANCE_FY26}",
        "B14": "='Income Statement'!L15", "C14": "='Income Statement'!K15",
        # Deuda financiera a valor nominal (2.000 corriente + 5.893 LP); los arrendamientos entran por el conversor.
        "B16": "='Balance Sheet'!L20+'Balance Sheet'!L25",
        "C16": "='Balance Sheet'!K20+'Balance Sheet'!K25",
        "B17": "No",      # Nike no reporta I+D por separado
        "B18": "Yes",     # arrendamientos operativos como deuda (Damodaran)
        "B20": 0,         # el reembolso de aranceles por cobrar (US$684M al 31-may) ya se cobró en buena parte: está en caja
        # Acciones: 1.483,5M (portada del 10-K, 8-jul-2026) + 12,5M RSU sin consolidar (10-K FY26).
        "B22": "='Income Statement'!L27+12,5",
        "B24": 0.25,      # guía FY27 ~25% (corrección del 2-oct-2026); LTM 20,7% solo como dato histórico
        "B35": RF_1001,
        "B38": "Yes", "B39": 76.8, "B40": 96.44, "B41": 5.1, "B42": 0.331,  # 10-K FY26: opciones y volatilidad
    }, "Datos base NKE desde cero (10-K FY26, comunicado 1T FY27)", bk)

    ms.write_with_backup(sh, "Operating lease converter", {
        "E5": 693, "B8": 564, "B9": 553, "B10": 512, "B11": 456, "B12": 361, "B13": 1146,
    }, "Arrendamientos operativos: costo FY26 y compromisos al 31-may-2026 (10-K FY26)", bk)

    ms.write_with_backup(sh, "Country equity risk premiums", {
        "B2": ERP_SEP26, "C2": "Damodaran, implied ERP September 1, 2026",
    }, "ERP de mercado maduro (Damodaran, 1-sep-2026)", bk)

    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Single Business(Global)",  # beta desapalancada Shoe global 0,894; regresión 0,98 (2a) / 1,04 (5a)
        "B26": "Will Input",
        "B27": ERP_SEP26,
        "B33": 9,                          # vencimiento promedio ponderado de la deuda (10-K FY26)
        "B34": "Actual rating",
        "B36": "A2/A",                     # Moody's A2 / S&P A+ (rebajada en 2025)
    }, "Costo de capital NKE: beta de industria Shoe, ERP sep-2026, rating real", bk)

    ms.write_with_backup(sh, "Valuation output", {
        "B33": "=B31-B32-N('Input sheet'!$B$76)",
        "B84": "=B82-B83-N('Input sheet'!$B$76)",
        "B135": "=B133-B134-N('Input sheet'!$B$76)",
    }, "Fórmula estándar con preferentes (B76 vacío en NKE)", bk)


def step_supuestos() -> None:
    """Supuestos del caso Base de la hoja = historia Base (paso 4 del prompt v4). Las cuatro historias están en
    reference/damodaran/NKEN.json; aquí solo se fija el Base técnico de la plantilla."""
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Input sheet", {
        "B27": -0.066,  # año 1 de la historia Base: guía FY27 "caída de un dígito alto" (1T −4%; China, Converse y NSW a la baja)
        "B28": 0.06,    # guía FY27: BPA ajustado US$1,15-1,35 + ~US$0,15 de Pace -> EBIT ~6% de ventas ~8% menores
        "B29": 0.034,   # CAGR años 2-5 de la historia Base (Norteamérica 4%, China se estabiliza, Converse plano)
        "B30": 0.116,   # 11% en base reportada + ~0,6 pp del ajuste de arrendamientos
        "B31": 6,       # los ahorros de Pace (US$2.500M) se completan en FY2031
        "B32": 2.1,     # industria Shoe global (2,12); Nike rota su capital ~2,6 veces
        "B33": 2.1,
        # Criterio de ventaja (reference/moat_2026-09-30.json, NKEN): marca probada de más de 40 años que gana sobre su costo
        # de capital, pero que se desvanece (ROIC de 47% a ~15%, ventas cayendo) -> punto medio entre el costo de capital
        # terminal (9,3%) y el ROIC actual (15,2%, menor que el de la industria).
        "B49": "Yes", "B50": 0.123,
    }, "Supuestos Base NKE desde cero = historia Base (ver reference/damodaran/NKEN.json)", BACKUP_PATH)
    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": "Madura"}, "Tipo de empresa NKE", BACKUP_PATH)
    rnm.refresh_resumen_valoracion(sh, TICKER, rnm.get_market_snapshot(TICKER))


def step_presentacion() -> None:
    """Fila 38 de 'Descuento de múltiplos' = DCF de las historias; fila 43 = precio con MOS sobre el esperado."""
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Descuento de múltiplos", {
        "A38": "DCF activo hoy · escenarios de las historias",
        "C38": "='Escenarios e historias'!H6", "D38": "='Escenarios e historias'!H5", "E38": "='Escenarios e historias'!H8",
        "A43": "Precio con MOS sobre el valor esperado", "C43": "", "D43": "='Escenarios e historias'!H14", "E43": "",
    }, "DCF activo = historias; MOS sobre el esperado (presentación vigente 1-oct-2026)", BACKUP_PATH)


def step_content() -> None:
    import nke_cero_content as nc

    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", nc.CUALITATIVO, "Contenido cualitativo NKE desde cero", bk)
    ms.write_with_backup(sh, "Estadísticas", nc.ESTADISTICAS, "Estadísticas NKE (fórmulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", nc.STORIES, "Historia NKE", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", nc.SUPUESTOS_RECOMENDADOS, "Recomendaciones NKE", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": nc.MULTIPLOS_EVALUACION}, "Evaluación de múltiplos NKE", bk)
    nc.format_estadisticas(sh)
    nc.write_tesis(sh, bk)  # después hay que volver a correr apply_multiples_v3 --apply (agrega el origen de los múltiplos)


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
