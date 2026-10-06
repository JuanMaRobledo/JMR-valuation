#!/usr/bin/env python
"""Valoración de McDonald's Corporation (MCD) DESDE CERO (6-oct-2026) sobre una copia nueva de la plantilla maestra, con
el prompt de valoración v4 y el de research v5 vigentes (fórmula única, tasas comunes, ambos horizontes). La hoja del
27-sep-2026 (1USPRKTTdnXcWAEoAQoVq9CJXH1ENPLQkP1k_SW0Rnp8, «Plantilla maestra reutilizable (vigente)» en la carpeta MCD)
queda sin cambios como referencia.

Fecha de corte: 30-sep-2026 (la de las tasas comunes de la cartera). Último reporte: 10-Q del 2T26.

Pasos: refresh | fix | datos | costo | supuestos | presentacion | content   (--step all corre todos)
Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts python scripts/run_mcd_cero.py --step refresh
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

import gspread  # noqa: E402

# Reintento con espera exponencial ante el límite de 60 lecturas por minuto de la API de Sheets.
_authorize = gspread.authorize
gspread.authorize = lambda creds, **kw: _authorize(creds, http_client=gspread.BackOffHTTPClient, **kw)

import model_steps as ms  # noqa: E402
import refresh_native_model as rnm  # noqa: E402

SHEET_ID = "1D44qNMrcbmbDbWuGO4EdFJdWdg9xE6cYg_pDCwLb30M"
TICKER = "MCD"
INDUSTRY = "Restaurant/Dining"  # Damodaran: MCD, YUM, QSR, DPZ, WEN, CMG, SBUX
PEER_TICKERS = ["YUM", "QSR", "DPZ", "WEN", "PZZA", "CMG"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "mcd_desde_cero_2026-10-06.json"

VALUATION_DATE = date(2026, 9, 30)


def _dec(x: float) -> str:
    return str(x).replace(".", ",")


def step_refresh() -> None:
    ms.install_augmented_client(TICKER)
    rnm.run(TICKER, sheet_id=SHEET_ID, peer_tickers=PEER_TICKERS, industry_us=INDUSTRY, industry_global=INDUSTRY)


# --- Correcciones de datos del importador (verificadas contra el XBRL de companyfacts y los 10-K/10-Q) -------------------
# Columnas: B=2016 ... K=2025, L=LTM (jul-2025 a jun-2026 = FY2025 − 1S25 + 1S26).
COLS = "DEFGHIJKL"  # 2018 .. LTM
REV = [21025.2, 21076.5, 19207.8, 23222.9, 23182.6, 25493.7, 25920, 26885, 27702]
EBIT = [8822.6, 9069.8, 7324, 10356, 9371, 11646.7, 11712, 12393, 12805]
# SG&A reportado (incluye la D&A corporativa); 2020-2021 no están etiquetados en el XBRL: 10-K 2021 (2.545,6 y 2.707,5).
SGA_TOTAL = [2200.2, 2229.4, 2545.6, 2707.5, 2863, 2817, 2858, 3039, 3232]
# D&A corporativa incluida en el SG&A (DepreciationDepletionAndAmortization); LTM = 457 − 213 + 222.
DA_CORP = [214.8, 262.5, 300.6, 329.7, 370.4, 381.7, 447, 457, 466]
# D&A total del flujo de caja (DepreciationAndAmortization); LTM = 2.199 − 1.064 + 1.131.
DA_TOTAL = [1482, 1617.9, 1751.4, 1868.1, 1871, 1978, 2097, 2199, 2266]
DA_OLD_CF = {"F": 300.6, "G": 329.7, "H": 370.4, "I": 381.7, "J": 447, "K": 457, "L": 466}

# Balance al 30-jun-2026 (10-Q 2T26, balance condensado), US$M. El importador repetía el de dic-2025.
BS_JUN26 = {
    "L3": 822, "L5": 822, "L9": 4345 - 822, "L10": 4345, "L11": 28479, "L13": 3347,
    "L15": 59920 - 4345 - 28479 - 3347,  # inversiones en afiliadas + misceláneos + derecho de uso de arrendamientos
    "L16": 59920, "L18": 1114, "L20": 0, "L23": 4018 - 1114, "L24": 4018,
    "L25": 39863,                        # incluye vencimientos corrientes y papel comercial (clasificados como largo plazo)
    "L26": 2329,                         # arrendamientos financieros no corrientes: último dato publicado (10-K 2025)
    "L27": 39863 + 14039 + 176 + 946 + 677 + 1222 - 39863 - 2329,
    "L28": 39863 + 14039 + 176 + 946 + 677 + 1222, "L29": 4018 + 39863 + 14039 + 176 + 946 + 677 + 1222,
    "L31": 9841, "L32": -2340, "L33": 71987, "L34": -1023, "L35": -1023, "L36": 59920,
}


def step_fix() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    inc, cfs = {}, {}
    for c, rev, ebit, sga, dac, dat in zip(COLS, REV, EBIT, SGA_TOTAL, DA_CORP, DA_TOTAL):
        sga_ex = round(sga - dac, 1)
        inc[f"{c}8"] = sga_ex
        inc[f"{c}9"] = dat
        inc[f"{c}11"] = round(rev - ebit - sga_ex - dat, 1)
        inc[f"{c}28"] = round(ebit + dat, 1)
    # BPA y acciones: desde 2023 MCD etiqueta las acciones en millones; el importador las dejó en 0 y el BPA en millones.
    inc.update({"I23": 11.63, "J23": 11.45, "K23": 12.00, "L23": 12.35,   # LTM = 12,00 − 5,77 + 6,12
                "I24": 11.56, "J24": 11.39, "K24": 11.95, "L24": 12.31,   # LTM = 11,95 − 5,74 + 6,10
                "I25": 727.9, "J25": 718.3, "K25": 713.4, "L25": 709.9,
                "I26": 732.3, "J26": 721.9, "K26": 716.4, "L26": 712.3,
                "I27": 732.3, "J27": 721.9, "K27": 716.4, "L27": 707.6})
    ms.write_with_backup(sh, "Income Statement", inc,
                         "D&A total (no solo la corporativa), SG&A sin su D&A, SG&A 2020-21, BPA y acciones 2023-LTM", bk)
    sh.worksheet("Income Statement").update_notes({
        "F8": "SG&A 2020 = 2.545,6 (10-K 2021, no etiquetado en XBRL) menos 300,6 de D&A corporativa incluida en esa línea.",
        "G8": "SG&A 2021 = 2.707,5 (10-K 2021, no etiquetado en XBRL) menos 329,7 de D&A corporativa incluida en esa línea.",
        "L9": ("D&A total del flujo de caja (DepreciationAndAmortization): 2.199 − 1.064 + 1.131 = 2.266. El importador usaba "
               "DepreciationDepletionAndAmortization, que en MCD es solo la D&A corporativa incluida en el SG&A (466)."),
        "L27": "Acciones en circulación al 30-jun-2026: 707.641.531 (portada del 10-Q 2T26). 2023-2025: diluidas promedio (XBRL en millones).",
        "L24": "BPA diluido LTM = 11,95 (FY25) − 5,74 (1S25) + 6,10 (1S26) = 12,31.",
    })
    for c in "FGHIJKL":
        new = DA_TOTAL[COLS.index(c)]
        d = round(new - DA_OLD_CF[c], 1)
        cur = sh.worksheet("Cash Flow Statement").batch_get([f"{c}6", f"{c}38", f"{c}39"], value_render_option="UNFORMATTED_VALUE")
        oth, lfcf, ufcf = (x[0][0] for x in cur)
        cfs.update({f"{c}4": new, f"{c}6": round(oth - d, 1), f"{c}38": round(lfcf + d, 1), f"{c}39": round(ufcf + d, 1)})
    ms.write_with_backup(sh, "Cash Flow Statement", cfs,
                         "D&A total en el flujo (2020-LTM); otros ajustes compensan para conservar el flujo operativo", bk)
    bs = dict(BS_JUN26)
    # Dic-2025: los 725 de vencimientos corrientes están DENTRO de la deuda de largo plazo (10-K 2025, nota de deuda).
    bs.update({"K20": 0, "K23": 2487 + 725})
    # Arrendamientos operativos 2019-2022 en la fila de «Leases» (2023+ solo financieros): se pasan a otros pasivos de LP
    # para que la deuda de los múltiplos históricos sea comparable. 2023: arrendamientos financieros 1.575,5 (XBRL).
    cur = sh.worksheet("Balance Sheet").batch_get(["E26:I26", "E27:I27"], value_render_option="UNFORMATTED_VALUE")
    for c, l26, l27 in zip("EFGHI", cur[0][0], cur[1][0]):
        if c == "I":
            bs.update({"I26": 1575.5, "I27": round(l27 - 1575.5, 1)})
        else:
            bs.update({f"{c}26": 0, f"{c}27": round(l27 + l26, 1)})
    ms.write_with_backup(sh, "Balance Sheet", bs,
                         "LTM = balance al 30-jun-2026 (10-Q 2T26); deuda corriente dentro del LP; arrendamientos comparables", bk)
    sh.worksheet("Balance Sheet").update_notes({
        "L25": ("Deuda de largo plazo al 30-jun-2026 (10-Q 2T26): 39.863. Incluye vencimientos corrientes y papel comercial, "
                "clasificados como largo plazo por la línea de crédito a 2028 (10-K 2025, nota de financiamiento)."),
        "L26": "Arrendamientos financieros no corrientes: 2.329 al 31-dic-2025 (10-K 2025, nota de arrendamientos); el 10-Q no los separa.",
        "H26": "2019-2022: el importador cargó aquí los arrendamientos OPERATIVOS; se pasaron a la fila 27 (sin dato de financieros).",
    })


PRICE_0930 = 230.94          # cierre del 30-sep-2026 (NYSE, yfinance)


def step_datos() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    # EBIT: GAAP sin normalizar. Los cargos de reestructuración de «Accelerating the Organization» se repiten desde 2023
    # (362, 291, 229 y 219 LTM): se tratan como costo recurrente, igual que los litigios de CELH.
    inp = {
        "B4": ms.serial(VALUATION_DATE),
        "D1": PRICE_0930,
        "B17": "No",                 # MCD no reporta I+D
        "B18": "Yes",                # arrendamientos operativos como deuda (conversor; US GAAP)
        "B20": 0,                    # afiliadas (China, Japón): su resultado ya está en el EBIT (otros ingresos operativos)
        "B22": "='Income Statement'!L27+1,164",
        "B24": 0.22,
        "B38": "Yes", "B39": 8.8, "B40": 228.19, "B41": 5.3, "B42": 0.18,
    }
    ms.write_with_backup(sh, "Input sheet", inp, "Datos base MCD desde cero (10-Q 2T26, 10-K 2025)", bk)
    sh.worksheet("Input sheet").update_notes({
        "B13": ("EBIT GAAP LTM (12.805). No se suman los cargos de reestructuración de Accelerating the Organization (219 LTM): "
                "se repiten desde 2023 (362, 291, 229), así que se tratan como costo recurrente (10-K 2025; comunicado del 2T26)."),
        "B16": ("Deuda de largo plazo 39.863 al 30-jun-2026 (incluye vencimientos corrientes y papel comercial) + arrendamientos "
                "financieros 2.329 (10-K 2025). Los arrendamientos operativos van por el conversor (B18 = Yes)."),
        "B20": ("0: las inversiones en afiliadas (2.896, China y Japón) no se suman porque su resultado (equity in earnings, 190 en "
                "2025) ya está dentro del EBIT como otro ingreso operativo; sumarlas contaría dos veces su valor."),
        "B22": ("Acciones en circulación al 30-jun-2026: 707,6 millones (portada del 10-Q 2T26) + 1,164 millones de RSU sin "
                "consolidar (10-K 2025, tabla de planes de compensación). Las opciones van por separado (B38-B42)."),
        "B24": "Guía de la empresa para 2026: tasa efectiva de 21%-23% (anexo 99.2 del 8-K del 4-ago-2026). LTM 21,4%.",
        "B39": "8,8 millones de opciones, precio de ejercicio promedio US$228,19, vida remanente 5,3 años (10-K 2025, nota de compensación en acciones).",
        "B42": "Volatilidad histórica de 3 años de la acción: 18,4% (cálculo propio con cierres diarios al 30-sep-2026).",
        "D1": "Cierre del 30-sep-2026 (fecha de corte de la cartera): US$230,94 (NYSE).",
    })
    ms.write_with_backup(sh, "Operating lease converter", {
        "E5": 1631, "B8": 1200, "B9": 1166, "B10": 1115, "B11": 1076, "B12": 1029, "B13": 10977,
    }, "Arrendamientos operativos: gasto de renta 2025 y compromisos al 31-dic-2025 (10-K 2025, nota de arrendamientos)", bk)
    sh.worksheet("Operating lease converter").update_notes({
        "E5": "Gasto total de renta 2025: 1.631 (restaurantes 1.573 + otros 58), 10-K 2025, nota de arrendamientos.",
        "B8": ("Pagos de arrendamientos OPERATIVOS al 31-dic-2025 (10-K 2025): 2026 1.200; 2027 1.166; 2028 1.115; 2029 1.076; "
               "2030 1.029; después 10.977 (incluye opciones razonablemente ciertas). Los financieros (2.352) ya están en la deuda."),
    })


def step_costo() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Country equity risk premiums", {"B2": 0.037},
                         "Prima madura de octubre de 2026 (3,70%), como el resto de la cartera", BACKUP_PATH)
    sh.worksheet("Country equity risk premiums").update_notes({"B2": (
        "Prima de mercado madura 3,70%: implícita de Damodaran del 1-oct-2026 (ERPOct26.xlsx), calculada con la tasa del UST a "
        "10 años del 30-sep-2026 (5,29%), la misma de la hoja. La maestra aún tenía 4,09% (septiembre).")})
    # Ventas por región (10-K 2025): EE.UU. 10.825; IOM 13.633 repartido por locales al 30-jun-2026 (Canadá 14%, Australia
    # 10%, Polonia 6%, resto de Europa 70%); IDL y corporativo 2.427 sin desglose (Japón, China, Latinoamérica, etc.).
    iom = 13633
    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Single Business(Global)",   # Restaurant/Dining global: 0,66 desapalancada; 60% de las ventas fuera de EE.UU.
        "B26": "Operating regions",
        "H22": "", "H23": "", "H24": round(iom * 1078 / 10918, 1), "H25": "", "H26": "",
        "H27": round(iom * 623 / 10918, 1), "H28": "",
        "H29": round(10825 + iom * 1523 / 10918, 1),
        "H30": round(iom * (10918 - 1078 - 623 - 1523) / 10918, 1),
        "H31": "", "H32": 2427,
        "B33": 12,
        "B34": "Actual rating", "B36": "Baa1/BBB+",
    }, "Costo de capital MCD desde cero: beta bottom-up global, prima por regiones, rating real", BACKUP_PATH)
    sh.worksheet("Cost of capital worksheet").update_notes({
        "B22": ("Beta bottom-up: Restaurant/Dining global de Damodaran (desapalancada 0,66), reapalancada con la D/E de mercado. "
                "Se usa la global porque ~60% de las ventas está fuera de EE.UU. (la de EE.UU., 0,78, se muestra como sensibilidad)."),
        "B33": "Vencimientos de 2026 a 2054 (10-K 2025, nota de financiamiento); 12 años es una estimación del plazo promedio.",
        "B36": "Calificación real: Baa1 (Moody's) y BBB+ (S&P), 10-K 2025.",
        "H24": "Australia: IOM (13.633, 10-K 2025) × 1.078/10.918 locales al 30-jun-2026 (anexo 99.2 del 2T26). Estimación por locales.",
        "H29": "EE.UU. 10.825 (10-K 2025) + Canadá: IOM × 1.523/10.918 locales. Estimación por locales.",
        "H30": "Resto de IOM (Francia, Reino Unido, Alemania, Italia, España y otros europeos) × locales; estimación.",
        "H32": "IDL y corporativo 2.427 (10-K 2025): Japón, China, Latinoamérica, Medio Oriente y otros, sin desglose por país.",
    })


def step_supuestos() -> None:
    """Caso Base de la hoja = historia Base (los cuatro escenarios están en reference/damodaran/MCD.json)."""
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Input sheet", {
        "B27": -0.0087,  # año 1 de la historia Base: franquicias +7%, restaurantes propios −15% (refranquiciamiento), otros +8%
        "B28": 0.497,    # margen LTM en base ajustada por arrendamientos ('Valuation output'!B6): continuidad
        "B29": 0.0146,   # CAGR años 2-5 de la historia Base (−4,7%, +1,6%, +4,6%, +4,6%)
        "B30": 0.5548,   # 52% en base reportada (guía «low-to-mid 50%» a 2030) + 3,48 pp del ajuste de arrendamientos
        "B31": 5,
        "B32": 0.5,      # rendimiento del capital nuevo 55,5% × 75% × 0,5 = 20,8% ≈ ROIC actual con arrendamientos (21,3%)
        "B33": 0.5,
        "B49": "Yes",    # ventaja durable: ROIC terminal = promedio de la industria
        "B50": 0.184,    # Restaurant/Dining (EE.UU., Damodaran ene-2026): 18,4%; actual 21,3%; costo de capital terminal 8,99%
    }, "Supuestos Base MCD desde cero (6-oct-2026) = historia Base", BACKUP_PATH)
    sh.worksheet("Input sheet").update_notes({
        "B28": ("Margen del año 1 = margen LTM en base ajustada por arrendamientos (12.805 + 963 de ajuste del conversor = 13.768 "
                "/ 27.702 = 49,7%). Sin caída artificial: la guía 2026 es «mid-to-high 40%» en base reportada (anexo 99.2 del 2T26)."),
        "B30": ("Margen objetivo de la historia Base: 52% reportado, dentro de la guía «low-to-mid 50%» a 2030 (8-K del 23-sep-2026), "
                "+3,48 pp del ajuste de arrendamientos = 55,5%. Se elige el tramo bajo-medio porque el apoyo a franquiciados (rentas) "
                "se amortiza contra el resultado ~10 años y el tráfico en EE.UU. es negativo en 2026."),
        "B32": ("Ventas/capital 0,5 (capital con arrendamientos): cada dólar de ventas nuevas pide US$2 de capital (inmuebles). "
                "Rendimiento del capital nuevo ≈ 55,5% × 75% × 0,5 = 20,8%, igual al ROIC actual (21,3%). En los años 1-2 el "
                "refranquiciamiento baja las ventas y libera capital (~US$2.600 M), del orden de lo que reciben por vender los "
                "restaurantes; el apoyo de capital a franquiciados (US$1.500-2.000 M 2027-2030) no se modela aparte."),
        "B50": ("Ventaja durable: (1) ROIC con arrendamientos ~21% > costo de capital 8,0-9,0% en cada uno de los últimos años; "
                "(2) marca probada de 70 años con ciclos y crisis superados, escala en compras, publicidad e inmuebles; (3) sin "
                "erosión visible del ROIC (el tráfico débil de EE.UU. en 2026 no baja el retorno). ROIC terminal = promedio de "
                "Restaurant/Dining (Damodaran, EE.UU., ene-2026) 18,4%, bajo el actual y sobre el costo de capital terminal (8,99%). "
                "Registro en reference/moat_2026-09-30.json."),
    })
    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": "Madura"}, "Tipo de empresa MCD (madura estable)", BACKUP_PATH)


def step_presentacion() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Descuento de múltiplos", {
        "A38": "DCF activo hoy · escenarios de las historias",
        "C38": "='Escenarios e historias'!H6", "D38": "='Escenarios e historias'!H5", "E38": "='Escenarios e historias'!H8",
        "A43": "Precio con MOS sobre el valor esperado", "C43": "", "D43": "='Escenarios e historias'!H14", "E43": "",
    }, "DCF activo = historias; MOS sobre el esperado (presentación vigente)", BACKUP_PATH)
    # El refresco congeló el cierre de la fecha que traía la maestra (14-sep-2026); se fija el del corte.
    ms.write_with_backup(sh, "Resumen de Valoración", {"C25": PRICE_0930},
                         "Precio al día del análisis = cierre del 30-sep-2026", BACKUP_PATH)
    sh.worksheet("Resumen de Valoración").update_notes({"C25": "Cierre del 30-sep-2026 (NYSE): US$230,94, fecha de corte de la cartera."})
    tv = sh.worksheet("Trailing Valuation").get("L3", value_render_option="FORMULA")
    if tv and tv[0] and not str(tv[0][0]).startswith("="):
        ms.write_with_backup(sh, "Trailing Valuation", {"L3": "='Input sheet'!D1"}, "Precio LTM = precio de corte", BACKUP_PATH)


def step_content() -> None:
    import mcd_cero_content as cc

    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", cc.CUALITATIVO, "Contenido cualitativo MCD desde cero (6-oct-2026)", bk)
    ms.write_with_backup(sh, "Estadísticas", cc.ESTADISTICAS, "Estadísticas MCD (fórmulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", cc.STORIES, "Historia MCD", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", cc.SUPUESTOS_RECOMENDADOS, "Recomendaciones MCD", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": cc.MULTIPLOS_EVALUACION}, "Evaluación de múltiplos MCD", bk)
    cc.format_estadisticas(sh)
    cc.write_tesis(sh, bk)  # después hay que volver a correr apply_multiples_v3 --apply (agrega el origen de los múltiplos)


STEPS = {"refresh": step_refresh, "fix": step_fix, "datos": step_datos, "costo": step_costo, "supuestos": step_supuestos,
         "presentacion": step_presentacion, "content": step_content}


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
