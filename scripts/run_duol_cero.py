#!/usr/bin/env python
"""Valoración de Duolingo, Inc. (DUOL) DESDE CERO (7-oct-2026), sobre una copia nueva de la plantilla maestra
(hoja 1eqWEqHU6TeIr8frOUt1vS54_YifnbBSCNvvIXhWbdC4, «Modelo JMR - DUOL (desde cero 2026-10-07)»), con el prompt de
valoración v4 y el de research v5 vigentes. La hoja anterior «DUOL análisis maestro» (1k-ms7Yt…, 30-sep-2026) queda
sin cambios como referencia.

Fecha de corte: 30-sep-2026 (la de las tasas comunes de la cartera). Último reporte: 10-Q del 2T26 (6-ago-2026, trimestre
al 30-jun-2026). Hechos posteriores al balance: nueva consejera (8-K del 10-ago-2026) y la pantalla con el crecimiento
de DAU de agosto (+27,4% el 17-ago, 8-K del 18-ago-2026; la empresa no cambió la guía).

Pasos: refresh | balance | fix | id | datos | costo | supuestos | presentacion | content   (--step all corre todos)
Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts python scripts/run_duol_cero.py --step datos
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402
import refresh_native_model as rnm  # noqa: E402

SHEET_ID = "1eqWEqHU6TeIr8frOUt1vS54_YifnbBSCNvvIXhWbdC4"
TICKER = "DUOL"
INDUSTRY = "Software (Internet)"  # clasificación de Damodaran de Duolingo (la misma de la valoración anterior)
PEER_TICKERS = ["SPOT", "NFLX", "RDDT", "PINS", "MTCH", "COUR"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "duol_desde_cero_2026-10-07.json"

VALUATION_DATE = date(2026, 9, 30)
PRICE_0930 = 142.40          # cierre del 30-sep-2026 (Nasdaq, yfinance auto_adjust=False; reference/corte_vigente.json)

# Balance al 30-jun-2026 (10-Q del 2T26), US$M. El importador repetía el cierre del 31-dic-2025 y dejaba en 0 las
# inversiones de corto plazo (bonos mantenidos al vencimiento: DebtSecuritiesHeldToMaturity...Current), que iban dentro
# de «otros activos corrientes».
BS_JUN26 = {
    "L3": 1180.887, "L4": 132.979, "L5": 1313.866,
    "L6": 130.979, "L8": 130.979,
    "L9": 102.689 + 2.707 + 20.873,                # costo de ingresos diferido + impuesto por cobrar + prepagos
    "L10": 1571.114,
    "L11": 42.619, "L12": 27.598, "L13": 35.335,
    "L14": 102.693,                                # inversiones de largo plazo (bonos al vencimiento): no operativas
    "L15": 74.830 + 2.735 + 206.039 + 10.990,      # derecho de uso + caja restringida + impuestos diferidos + otros
    "L16": 2073.953,
    "L18": 16.196, "L20": 0, "L22": 505.102,
    "L23": 1.106 + 55.429,                         # impuesto por pagar + gastos devengados (incluye arrendamientos corrientes)
    "L24": 577.833, "L25": 0, "L26": 0,
    "L27": 86.136 + 0.242,                         # arrendamientos operativos de largo plazo + impuestos diferidos pasivos
    "L28": 86.378, "L29": 664.211,
    "L31": 1046.326 - 1.425,                       # capital pagado − acciones en tesorería (1,4)
    "L32": 0, "L33": 364.836, "L34": 1409.742, "L35": 1409.742, "L36": 2073.953,
}
# Inversiones de corto plazo de los cierres anuales (10-K 2025): el importador las dejaba en «otros activos corrientes».
BS_STI = {"J4": 91.854, "J5": 785.8 + 91.854, "J9": 186.9 - 91.854,
          "K4": 104.078, "K5": 1036.4 + 104.078, "K9": 237.4 - 104.078}

# Estado de resultados LTM (jul-2025 a jun-2026 = 2025 + 1S26 − 1S25), US$M: el importador repetía el SG&A anual y
# ponía la diferencia en «otros gastos operativos».
#   SG&A = (125,677 + 181,887) − (56,225 + 89,435) + (79,256 + 96,939) = 338,099. Otros = −D&A (15,799), como en los
#   cierres anuales: el EBIT LTM no cambia (157,085 = 135,570 − 56,957 + 78,472).
IS_LTM = {
    "L8": 338.099, "L11": -15.799,
    # Acciones: el importador dejó en 0 el promedio básico de 2023-2025 y repitió el diluido de 2025 en el LTM.
    "I25": 41.451, "J25": 43.504, "K25": 45.773, "L25": 46.744,
    "I23": 0.39, "J23": 2.04, "K23": 9.05,
    "L23": 9.05 - 1.76 + 1.64, "L24": 8.57 - 1.64 + 1.53,  # BPA LTM = anual + 1S26 − 1S25
    "L26": 50.080,                                          # diluido promedio del 1S26
    "L27": 40.325 + 6.399,                                  # acciones A + B en circulación al 30-jun-2026
}
RSU = 2.8                    # RSU sin consolidar al 30-jun-2026 (carta del 2T26, tabla de títulos dilutivos)
OPCIONES, STRIKE = 0.6, 21.09  # opciones vivas y precio de ejercicio promedio ponderado (carta del 2T26)
NOL_FEDERAL = 111.199        # pérdidas fiscales federales de 2025 sin vencimiento (10-K 2025, nota de impuestos)


def _dec(x: float) -> str:
    return str(x).replace(".", ",")


def step_refresh() -> None:
    ms.install_augmented_client(TICKER)
    rnm.run(TICKER, sheet_id=SHEET_ID, peer_tickers=PEER_TICKERS, industry_us=INDUSTRY, industry_global=INDUSTRY)


def step_balance() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Balance Sheet", {k: round(v, 3) for k, v in {**BS_JUN26, **BS_STI}.items()},
                         "LTM = balance al 30-jun-2026 (10-Q 2T26); inversiones de corto plazo separadas de otros activos "
                         "corrientes (10-K 2025)", BACKUP_PATH)
    sh.worksheet("Balance Sheet").update_notes({
        "L4": "Bonos mantenidos al vencimiento de corto plazo al 30-jun-2026: 132,979 (10-Q 2T26). El importador los dejaba en 0.",
        "J4": "Inversiones de corto plazo al 31-dic-2024: 91,854 (10-K 2025, XBRL DebtSecuritiesHeldToMaturity...Current); salen de «otros activos corrientes».",
        "K4": "Inversiones de corto plazo al 31-dic-2025: 104,078 (10-K 2025); salen de «otros activos corrientes».",
        "L15": "Derecho de uso 74,830 + caja restringida 2,735 + impuestos diferidos 206,039 (liberación de la reserva de valuación del 3T25) + otros 10,990 (10-Q 2T26).",
        "L31": "Capital pagado 1.046,326 − acciones en tesorería 1,425 (recompras del 2T26 aún no retiradas), 10-Q 2T26.",
        "L27": "Arrendamientos operativos de largo plazo 86,136 (van por el conversor, no como deuda) + impuestos diferidos pasivos 0,242.",
    })


def step_fix() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Income Statement", {k: round(v, 3) for k, v in IS_LTM.items()},
                         "LTM jun-2026: SG&A de los 12 meses, otros = −D&A (EBIT sin cambio) y acciones/BPA reales",
                         BACKUP_PATH)
    sh.worksheet("Income Statement").update_notes({
        "L8": "LTM jul-2025 a jun-2026: ventas y marketing 148,708 + generales y administrativos 189,391 (10-K 2025 + 1S26 − 1S25) = 338,099.",
        "L11": "−D&A LTM (14,391 − 7,030 + 8,438 = 15,799): la D&A está dentro de los gastos funcionales y la fila 9 la muestra aparte. EBIT LTM 157,085 sin cambio.",
        "L27": "Acciones Clase A (40,325) + Clase B (6,399) en circulación al 30-jun-2026 (balance del 10-Q 2T26).",
        "K25": "Promedio básico 2025: 45,773 millones (10-K 2025); el importador lo dejaba en 0.",
        "L23": "BPA básico LTM = 9,05 (2025) − 1,76 (1S25) + 1,64 (1S26). Incluye el beneficio fiscal único de 2025 (US$256,7M).",
    })


def step_id() -> None:
    """Conversor de I+D alineado al LTM (criterio de la auditoría del 1-oct-2026): el año en curso es el LTM a jun-2026
    (F8 = 'Income Statement'!L10) y los años previos deben ser los 12 meses a junio, no los ejercicios calendario, que se
    solapan seis meses con el LTM. I+D semestral del XBRL (10-Q de cada 2T)."""
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "R& D converter", {
        "B12": "='Income Statement'!J10+144,06-106,025",   # 12 meses a jun-2025 = 2024 + 1S25 − 1S24
        "B13": "='Income Statement'!I10+106,025-93,791",   # 12 meses a jun-2024 = 2023 + 1S24 − 1S23
        "B14": "='Income Statement'!H10+93,791-63,998",    # 12 meses a jun-2023 = 2022 + 1S23 − 1S22
    }, "Conversor de I+D alineado al LTM (12 meses a junio)", BACKUP_PATH)
    sh.worksheet("R& D converter").update_notes({
        "B12": "I+D de los 12 meses a jun-2025 = 2024 (235,3) + 1S25 (144,06) − 1S24 (106,025) = 273,3 (10-Q 2T25 y 2T24). Antes el ejercicio 2025, que se solapa con el LTM.",
        "B13": "12 meses a jun-2024 = 2023 (194,4) + 1S24 (106,025) − 1S23 (93,791) = 206,6 (10-Q). Antes el ejercicio 2024.",
        "B14": "12 meses a jun-2023 = 2022 (150,0) + 1S23 (93,791) − 1S22 (63,998) = 179,8 (10-Q). Antes el ejercicio 2023.",
    })


def step_datos() -> None:
    sh = ms.open_sheet(SHEET_ID)
    inp = {
        "B4": ms.serial(VALUATION_DATE),
        "D1": PRICE_0930,
        "B16": "='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25",
        "B17": "Yes",
        "B19": "='Balance Sheet'!L5",
        "B20": "='Balance Sheet'!L14",
        "B22": f"='Income Statement'!L27+{_dec(RSU)}",
        "B24": 0.24,
        "B38": "Yes", "B39": OPCIONES, "B40": STRIKE, "B41": 3, "B42": 0.55,
        "B62": "Yes", "B63": f"={_dec(NOL_FEDERAL)}",
    }
    ms.write_with_backup(sh, "Input sheet", inp, "Datos base DUOL desde cero (10-Q 2T26, 10-K 2025, carta del 2T26)",
                         BACKUP_PATH)
    sh.worksheet("Input sheet").update_notes({
        "B4": "Fecha de corte de la cartera: 30-sep-2026 (Treasury 5,29% y prima de Damodaran de octubre de 2026, 3,70%).",
        "D1": "Cierre del 30-sep-2026 (Nasdaq): US$142,40. Fijo; no se usa GOOGLEFINANCE.",
        "B12": ("Ventas LTM jul-2025 a jun-2026: 1.037,589 (2025) − 483,008 (1S25) + 590,421 (1S26) = 1.145,0 (10-K 2025 y "
                "10-Q 2T26). Suscripciones 980,7; publicidad 82,9; Duolingo English Test 41,4; compras en la app y otros 40,0."),
        "B13": ("EBIT GAAP LTM 157,085 (135,570 − 56,957 + 78,472). No se ajusta: el deterioro de software capitalizado (0,6) y "
                "los costos de compras (0,3 en el 2T26) son inmateriales. Incluye la compensación en acciones (US$145M LTM, "
                "12,7% de las ventas), que es un costo económico."),
        "B16": "Duolingo no tiene deuda financiera. Los arrendamientos operativos (US$93M de pasivo) van por el conversor (B18 = Yes).",
        "B19": "Caja 1.180,887 + inversiones de corto plazo 132,979 al 30-jun-2026 (10-Q 2T26) = 1.313,9.",
        "B20": "Inversiones de largo plazo (bonos al vencimiento) 102,693 al 30-jun-2026: activo no operativo separable.",
        "B22": ("Acciones A + B al 30-jun-2026 (46,724 millones) + 2,8 millones de RSU sin consolidar (carta del 2T26). Las 0,6 "
                "millones de unidades del fundador sujetas a metas de precio no cumplidas no se cuentan; las 0,6 millones de "
                "opciones van por el valor de las opciones (B38)."),
        "B24": ("Tasa efectiva del año 1: 24% (guía de 23-25% para 2026, carta del 2T26; 24,1% en el 1S26). La LTM (−103%) "
                "incluye la liberación de la reserva de valuación de 2025 (US$256,7M de beneficio único)."),
        "B38": "0,6 millones de opciones a US$21,09 promedio (carta del 2T26); vida restante estimada 3 años; volatilidad 55% (acción muy volátil en 2025-2026).",
        "B63": ("Pérdidas fiscales federales generadas en 2025 sin vencimiento: US$111,2M (10-K 2025). Las estatales (US$72,4M) "
                "no se suman. El resto de los impuestos diferidos (diferencias temporales: I+D capitalizado, acciones) no se "
                "agrega como valor: estimación prudente."),
    })


def step_costo() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Single Business(Global)",   # 62% de las ventas fuera de EE.UU.: tabla global de Damodaran
        "B26": "Operating regions",
        "H22": "", "H23": "", "H24": "", "H25": "", "H26": "", "H27": "", "H28": "",
        "H29": 392.214, "H30": "", "H31": "",
        "G32": "Fuera de EE.UU. sin desglose", "H32": 645.375, "I32": "='Country equity risk premiums'!$B$2+0,018",
        "B33": 5,              # vencimiento promedio de los arrendamientos (la única deuda)
        "B34": "Direct Input",
        "B35": 0.0569,         # tasa libre de riesgo 5,29% + 0,40% (calificación sintética AAA: cobertura infinita)
    }, "Costo de capital DUOL desde cero: beta bottom-up global, prima por regiones, Kd sintético", BACKUP_PATH)
    sh.worksheet("Cost of capital worksheet").update_notes({
        "B22": ("Beta bottom-up: Software (Internet) de Damodaran, tabla global (enero de 2026; desapalancada 1,34), "
                "reapalancada con la D/E de mercado de Duolingo (solo arrendamientos). Se usa la global porque el 62% de las "
                "ventas de 2025 está fuera de EE.UU. (10-K 2025: EE.UU. 392,2 de 1.037,6); la de EE.UU. (1,59) se informa "
                "como sensibilidad."),
        "H29": "Ventas de 2025 en EE.UU.: 392,214 (10-K 2025, ubicación del usuario). Sin prima país (Treasury sin ajustar).",
        "H32": ("Resto del mundo 645,375 (10-K 2025): Duolingo no publica más desglose. Prima país 1,80% = la global de "
                "Damodaran sin el peso de EE.UU. (convención de scripts/erp_por_regiones.py)."),
        "B35": ("Costo de la deuda antes de impuestos = 5,29% + 0,40% (calificación sintética AAA de la hoja: Duolingo no "
                "tiene deuda ni gasto de intereses). Solo afecta a los arrendamientos (~US$90M)."),
    })


def _base_growth() -> list[float]:
    """Crecimiento agregado de la historia Base (suma de las fuentes de ingresos de scripts/duol_cero_spec.py)."""
    import duol_cero_spec as spec

    seg = dict(spec.SPEC["segmentos"])
    base = next(h for h in spec.SPEC["historias"] if h["id"] == "A")
    out = []
    for y in range(5):
        antes = sum(seg.values())
        for k in seg:
            seg[k] *= 1 + base["crec"][k][y]
        out.append(sum(seg.values()) / antes - 1)
    return out


LEASE_PP = 0.00037250955577619816   # ajuste del EBIT por arrendamientos / ventas (conversor)
LEASE_K = 0.09175658430369107       # VP de arrendamientos / ventas


def step_supuestos() -> None:
    """Caso Base de la hoja = historia Base (los cuatro escenarios están en reference/damodaran/DUOL.json)."""
    sh = ms.open_sheet(SHEET_ID)
    g = _base_growth()
    cagr25 = ((1 + g[1]) * (1 + g[2]) * (1 + g[3]) * (1 + g[4])) ** 0.25 - 1
    ms.write_with_backup(sh, "Input sheet", {
        "B27": round(g[0], 4),                 # año 1 de la historia Base (suma de las fuentes de ingresos)
        "B28": round(0.185 + LEASE_PP, 4),     # ~9,5% GAAP en 2026-27 + ~9 pp de I+D capitalizado (base del modelo)
        "B29": round(cagr25, 4),               # CAGR años 2-5 de la historia Base
        "B30": round(0.28 + LEASE_PP, 4),      # 28% en la base del modelo (~24% GAAP) + arrendamientos
        "B31": 5,
        "B32": 2.25,                           # cerca del de hoy con el capital arrendado (tabla_ventas_capital.py: 2,38)
        "B33": 2.0,
        "B46": "No",
        "B49": "No",                           # sin ventaja defendible: ROIC terminal = costo de capital
    }, "Supuestos Base DUOL desde cero (7-oct-2026) = historia Base", BACKUP_PATH)
    pre1, pre2 = 1 / (1 / 2.25 - LEASE_K), 1 / (1 / 2.0 - LEASE_K)
    sh.worksheet("Input sheet").update_notes({
        "B27": (f"Año 1 (jul-2026 a jun-2027) de la historia Base (reference/damodaran/DUOL.json): suscripciones +13%, "
                f"publicidad +4%, Duolingo English Test 0%, compras en la app y otros −10% = {g[0]*100:.2f}%. Converge a las "
                "reservas (+10,9% guía 2026; +8,9% guía 3T26, carta del 2T26), no al ingreso reportado (+16,3% en 2026)."),
        "B28": ("Margen del año 1: 18,5% en la base del modelo ≈ 9,5% GAAP (guía de EBITDA ajustado 2026 de 26,5% menos "
                "compensación en acciones ~15% de las ventas y ~1,5% de depreciación, carta del 2T26) + ~9 pp de I+D "
                "capitalizado a 3 años (10,2 pp en el LTM: 'Valuation output'!B6 = 24,0% frente a 13,7% GAAP; baja porque el I+D "
                "crece más lento). + 0,04 pp de arrendamientos."),
        "B29": (f"CAGR de los años 2-5 de la historia Base: {', '.join(f'{x*100:.1f}%' for x in g[1:])} ({cagr25*100:.2f}%). "
                "Suscripciones 13%, 12%, 11%, 10%; publicidad 12% a 9%; English Test 2%; compras en la app 4-5%."),
        "B30": ("Margen objetivo de la Base: 28% en la base del modelo (~24% GAAP: extremo bajo de Match Group, 25-29% GAAP, con "
                "el doble de I+D; supone compensación en acciones de ~10% de las ventas) + 0,04 pp de arrendamientos."),
        "B31": "Convergencia en 5 años: 2026 es un año de inversión deliberada (carta del 4T25); el margen vuelve en 2027-2030.",
        "B32": (f"Ventas/capital 2,25 con el capital arrendado ({pre1:.2f} sin él): el de hoy es 2,38 (con I+D alineado al LTM, sin los impuestos "
                "diferidos de la liberación de la reserva); marginal 7,6 (1 año) y 14,6 (3 años) inflados por los prepagos; "
                "sector 1,35 (Software (Internet)). Capital nuevo rinde 28% × 75% × 2,25 ≈ 47% (ROIC actual 43%)."),
        "B33": (f"Ventas/capital 2,0 en los años 6-10 ({pre2:.2f} sin arrendamientos): los prepagos dejan de crecer más que las "
                "ventas y el rendimiento del capital nuevo baja a ~42%, camino del costo de capital después del año 10."),
        "B49": ("Sin ventaja defendible (reference/moat_2026-09-30.json): gana sobre su costo de capital desde 2024, pero la "
                "marca (14 años) y el hábito de las rachas no son una ventaja estructural en el criterio de Damodaran: costos "
                "de cambio bajos y sin efectos de red. ROIC después del año 10 = costo de capital."),
    })
    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": "Crecimiento"}, "Tipo de empresa DUOL (ciclo de vida)",
                         BACKUP_PATH)
    sh.worksheet("Resumen de Valoración").update_notes({"G3": (
        "Ciclo de vida (Damodaran): transición de crecimiento alto a crecimiento maduro; sector Software (Internet). Ventas "
        "+44%, +41%, +39% en 2023-2025 y ~+11% de reservas en 2026; margen GAAP recién positivo (2024) y en expansión "
        "hacia ~24%: las utilidades aún no están en su nivel estable → «Crecimiento» (reference/ciclo_de_vida).")})
    # Otros ingresos / EBIT proyectado (supuesto escrito a mano, prompt v4): intereses de ~US$46M al año sobre US$1.417M de
    # caja e inversiones al ~3,5%, frente a un EBIT proyectado de ~US$250-350M en la base del modelo: ~15%.
    ms.write_with_backup(sh, "Financials Multiples", {"E11": 0.15, "E50": 0.15, "E90": 0.15},
                         "Otros ingresos / EBIT proyectado = 15% (intereses de la caja)", BACKUP_PATH)
    sh.worksheet("Financials Multiples").update_notes({c: (
        "Supuesto escrito a mano (7-oct-2026): 15% del EBIT. Intereses LTM US$45M (caja e inversiones de US$1.417M al ~3,5%; "
        "10-Q 2T26) frente a un EBIT proyectado de ~US$250-350M en FY+1 a FY+3; baja a medida que crece el EBIT y si la "
        "caja se usa en recompras. El promedio de 3 años de la plantilla mezcla años con EBIT casi nulo.") for c in ("E11", "E50", "E90")})


def step_presentacion() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Descuento de múltiplos", {
        "A38": "DCF activo hoy · escenarios de las historias",
        "C38": "='Escenarios e historias'!H6", "D38": "='Escenarios e historias'!H5", "E38": "='Escenarios e historias'!H8",
        "A43": "Precio con MOS sobre el valor esperado", "C43": "", "D43": "='Escenarios e historias'!H14", "E43": "",
    }, "DCF activo = historias; MOS sobre el esperado (presentación vigente)", BACKUP_PATH)
    ms.write_with_backup(sh, "Resumen de Valoración", {"C25": PRICE_0930},
                         "Precio al día del análisis = cierre del 30-sep-2026", BACKUP_PATH)
    sh.worksheet("Resumen de Valoración").update_notes({"C25": "Cierre del 30-sep-2026 (Nasdaq): US$142,40, fecha de corte de la cartera."})
    tv = sh.worksheet("Trailing Valuation").get("L3", value_render_option="FORMULA")
    if tv and tv[0] and not str(tv[0][0]).startswith("="):
        ms.write_with_backup(sh, "Trailing Valuation", {"L3": "='Input sheet'!D1"}, "Precio LTM = precio de corte", BACKUP_PATH)


def step_content() -> None:
    import duol_cero_content as cc

    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", cc.CUALITATIVO, "Contenido cualitativo DUOL desde cero (7-oct-2026)", bk)
    ms.write_with_backup(sh, "Estadísticas", cc.ESTADISTICAS, "Estadísticas DUOL (fórmulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", cc.STORIES, "Historia DUOL", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", cc.SUPUESTOS_RECOMENDADOS, "Recomendaciones DUOL", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": cc.MULTIPLOS_EVALUACION}, "Evaluación de múltiplos DUOL", bk)
    cc.format_estadisticas(sh)
    cc.write_tesis(sh, bk)  # después hay que volver a correr apply_multiples_v3 --apply (agrega el origen de los múltiplos)


STEPS = {"refresh": step_refresh, "balance": step_balance, "fix": step_fix, "id": step_id, "datos": step_datos, "costo": step_costo,
         "supuestos": step_supuestos, "presentacion": step_presentacion, "content": step_content}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--step", choices=[*STEPS, "all"], nargs="+", default=["all"])
    args = parser.parse_args(argv)
    for name, fn in STEPS.items():
        if name in args.step or ("all" in args.step and name != "refresh"):
            print(f"== {name}")
            fn()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
