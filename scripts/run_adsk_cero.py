#!/usr/bin/env python
"""Valoración de Autodesk, Inc. (ADSK) DESDE CERO (7-oct-2026), sobre una copia nueva de la plantilla maestra
(hoja 1m-od4YZ7pQNvcQ8oFi78cKv72vQCr2S9Ak3jNDSnNfs), con el prompt de valoración v4 y el de research v5 vigentes.
La hoja anterior «Modelo_JMR_ADSK» (17eku40N…, 26-sep-2026) queda sin cambios como referencia.

Fecha de corte: 30-sep-2026 (la de las tasas comunes de la cartera). Último reporte: 10-Q del 2T FY27 (28-ago-2026,
trimestre al 31-jul-2026). Hechos posteriores al balance: compra de MaintainX (3-ago-2026, US$3.530M netos de caja,
préstamo puente de US$1.000M) y bonos por US$1.000M (10-sep-2026) que refinancian ese préstamo.

Pasos: refresh | balance | datos | costo | supuestos | presentacion | content   (--step all corre todos)
Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts python scripts/run_adsk_cero.py --step datos
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

SHEET_ID = "1m-od4YZ7pQNvcQ8oFi78cKv72vQCr2S9Ak3jNDSnNfs"
TICKER = "ADSK"
INDUSTRY = "Software (System & Application)"  # Damodaran: ADSK, PTC, BSY, CDNS, SNPS, ADBE, INTU
PEER_TICKERS = ["PTC", "BSY", "DASTY", "CDNS", "SNPS", "TRMB"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "adsk_desde_cero_2026-10-07.json"

VALUATION_DATE = date(2026, 9, 30)
PRICE_0930 = 209.00         # cierre del 30-sep-2026 (Nasdaq, yfinance auto_adjust=False)

# Balance al 31-jul-2026 (10-Q del 2T FY27, balance condensado), US$M. El importador repetía partidas del 31-ene-2026.
BS_JUL26 = {
    "L3": 4098, "L4": 57, "L5": 4155, "L6": 684, "L8": 684, "L9": 831, "L10": 5670, "L11": 124, "L12": 423,
    "L13": 4331, "L14": 202,                         # valores negociables de largo plazo (inversión financiera)
    "L15": 145 + 808 + 1280,                         # derecho de uso + impuestos diferidos + otros activos LP
    "L16": 12983, "L18": 457,
    "L20": 994 + 499,                                # papel comercial (994) + bonos 3,50% jun-2027 ya corrientes (499)
    "L22": 4036,
    "L23": 354 + 63 + 52 + 173,                      # remuneraciones, impuestos, arrendamientos corrientes, otros devengados
    "L24": 6628, "L25": 1985, "L26": 0,
    "L27": 222 + 175 + 203 + 53 + 334,               # ingresos diferidos LP, arrendamientos LP, impuestos LP, diferidos, otros
    "L28": 1985 + 987, "L29": 6628 + 2972,
    "L31": 4846, "L32": -233, "L33": -1230, "L34": 3383, "L35": 3383, "L36": 12983,
}

# Estado de resultados LTM (ago-2025 a jul-2026 = FY26 + 1S FY27 − 1S FY26), US$M: el importador repetía el SG&A anual.
#   SG&A = M&S 2.373 + G&A 693 + (1.209 + 341) − (1.125 + 330) = 3.161.
#   Otros gastos operativos = amortización de intangibles comprados (53 + 25 − 27 = 51) + reestructuración
#   (216 + 29 − 111 = 134) − D&A total del flujo de caja que la hoja muestra aparte (201) = −16. EBIT LTM sin cambio (2.041).
IS_LTM = {"L8": 3161, "L11": -16}

# MaintainX (comprada el 3-ago-2026, después del balance): ajustes pro forma, todos estimaciones declaradas.
MX_PRECIO_NETO = 3530        # contraprestación preliminar neta de la caja adquirida (10-Q 2T FY27, nota 19)
MX_PRESTAMO = 1000           # préstamo a plazo del 3-ago-2026 (refinanciado con bonos 2029/2033 el 10-sep-2026)
MX_INGRESOS_LTM = 90         # estimación: ARR > US$135M a dic-2026 creciendo > 50% => ~US$90M en los 12 meses a jul-2026
MX_EBIT_LTM = -80            # estimación: pérdida operativa (dilución ~0,5 pp del margen FY27 sobre ~5 meses)
RSU = 5.413                  # RSU y PSU sin consolidar al 31-jul-2026 (10-Q 2T FY27, nota de acciones)


def _dec(x: float) -> str:
    return str(x).replace(".", ",")


def step_refresh() -> None:
    ms.install_augmented_client(TICKER)
    rnm.run(TICKER, sheet_id=SHEET_ID, peer_tickers=PEER_TICKERS, industry_us=INDUSTRY, industry_global=INDUSTRY)


def step_balance() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bs_f = sh.worksheet("Balance Sheet").batch_get(list(BS_JUL26), value_render_option="FORMULA")
    vals = {c: v for (c, v), f in zip(BS_JUL26.items(), bs_f) if not (f and f[0] and str(f[0][0]).startswith("="))}
    ms.write_with_backup(sh, "Balance Sheet", vals,
                         "LTM = balance al 31-jul-2026 (10-Q 2T FY27); el importador repetía partidas del 31-ene-2026", BACKUP_PATH)


def step_fix() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Income Statement", IS_LTM,
                         "LTM jul-2026: SG&A = M&S + G&A de los 12 meses (el importador repetía el anual); otros gastos "
                         "compensan para no mover el EBIT (2.041)", BACKUP_PATH)
    sh.worksheet("Income Statement").update_notes({
        "L8": "LTM ago-2025 a jul-2026: M&S 2.373 + G&A 693 (10-K FY26) + 1S FY27 (1.209 + 341) − 1S FY26 (1.125 + 330) = 3.161.",
        "L11": "Amortización de intangibles comprados 51 + reestructuración 134 − D&A total 201 (fila 9) = −16 (10-K FY26 y 10-Q 2T FY27).",
    })


def step_datos() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    inp = {
        "B4": ms.serial(VALUATION_DATE),
        "D1": PRICE_0930,
        "B12": f"='Income Statement'!L3+{MX_INGRESOS_LTM}",
        "B13": f"='Income Statement'!L12{MX_EBIT_LTM}",
        "B16": f"='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25+'Balance Sheet'!L26+{MX_PRESTAMO}+22",
        "B17": "Yes",
        "B19": f"='Balance Sheet'!L5-{MX_PRECIO_NETO}+{MX_PRESTAMO}",
        "B22": f"='Income Statement'!L27+{_dec(RSU)}",
        "B38": "No",
    }
    ms.write_with_backup(sh, "Input sheet", inp, "Datos base ADSK desde cero (10-Q 2T FY27, 10-K FY26, 8-K de MaintainX)", bk)
    sh.worksheet("Input sheet").update_notes({
        "B12": ("Ventas LTM a jul-2026 (Income Statement L3 = 7.790: FY26 7.206 + 1S FY27 3.980 − 1S FY26 3.396) + 90 de "
                "MaintainX pro forma (estimación propia: ARR > US$135M a dic-2026 con crecimiento > 50%, comunicado del "
                "28-may-2026; la gerencia espera ~US$60M de ingresos en ago-2026 a ene-2027, llamada del 27-ago-2026). "
                "MaintainX se compró el 3-ago-2026, después del balance: su precio sale de la caja (B19)."),
        "B13": ("EBIT GAAP LTM (Income Statement L12 = 2.041) − 80 de pérdida operativa estimada de MaintainX (no publicada; "
                "la gerencia dijo que «no era rentable» y que diluye el margen de FY27, que mantuvo en ~39% no GAAP pese a "
                "márgenes subyacentes mejores). La reestructuración (134 LTM; 15 en FY25, 216 en FY26 y 29 en el 1S FY27) NO se "
                "suma: se repite tres ejercicios seguidos y se trata como costo recurrente (Damodaran, Investment Valuation, cap. 9)."),
        "B16": ("Deuda a valor nominal pro forma: papel comercial 994 (L20, nominal 1.000) + bonos 3,50% 2027 499 + bonos LP "
                "1.985 (nominal 2.000) + 1.000 del préstamo de MaintainX (3-ago-2026), refinanciado el 10-sep-2026 con bonos "
                "5,050% 2029 y 5,650% 2033 por US$1.000M (8-K) + 22 de descuentos = 4.500. Arrendamientos por el conversor."),
        "B19": ("Caja y valores negociables de corto plazo al 31-jul-2026 (L5 = 4.098 + 57) − 3.530 pagados por MaintainX "
                "netos de la caja adquirida (10-Q 2T FY27, nota 19) + 1.000 del préstamo = 1.625 pro forma. Los valores "
                "negociables de largo plazo (202) van en B20."),
        "B22": ("Acciones (Income Statement L27 = 209; portada del 10-Q: 209 millones al 21-ago-2026) + 5,413 millones de RSU "
                "y PSU sin consolidar al 31-jul-2026 (10-Q 2T FY27). Autodesk no tiene opciones relevantes: B38 = No."),
        "B17": ("I+D como gasto de capital (Damodaran, cap. 9; vida de 3 años como en ADBE y MSFT): Autodesk invierte ~22% de "
                "sus ventas en I+D y ese gasto crea el activo que sostiene sus ingresos."),
    })


def step_costo() -> None:
    sh = ms.open_sheet(SHEET_ID)
    other_am = 648 / 2  # «Otras Américas» (Canadá + Latinoamérica) sin desglose: mitad y mitad (estimación declarada)
    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Single Business(Global)",   # 65% de las ventas fuera de EE.UU.: tabla global de Damodaran
        "B26": "Operating regions",
        "H22": "", "H23": 1324, "H24": "", "H25": "", "H26": round(other_am), "H27": "", "H28": "",
        "H29": 2761 + round(other_am), "H30": "", "H31": 3057, "H32": "",
        "B33": 3.7,            # vencimiento promedio ponderado de la deuda pro forma (bonos 2027-2035 y papel comercial)
        "B34": "Direct Input",
        "B35": 0.0565,         # bonos 5,650% a 2033 colocados el 8-sep-2026 (8-K del 10-sep-2026)
    }, "Costo de capital ADSK desde cero: beta bottom-up global, prima por regiones, Kd de mercado", BACKUP_PATH)
    sh.worksheet("Cost of capital worksheet").update_notes({
        "B22": ("Beta bottom-up: Software (System & Application) de Damodaran, tabla global (enero de 2026), desapalancada "
                "y reapalancada con la D/E de mercado de Autodesk. Se usa la global porque el 65% de las ventas LTM está fuera "
                "de EE.UU. (10-Q 2T FY27: EE.UU. 2.761 de 7.790); la de EE.UU. se informa como sensibilidad."),
        "H29": "Norteamérica = EE.UU. 2.761 + mitad de «Otras Américas» (324, Canadá; estimación). Ventas LTM a jul-2026.",
        "H26": "Mitad de «Otras Américas» (324) como Latinoamérica: el 10-Q no separa Canadá de Latinoamérica (estimación).",
        "H31": "EMEA LTM 3.057 (10-K FY26 2.794 + 1S FY27 1.565 − 1S FY26 1.302).",
        "H23": "Asia Pacífico LTM 1.324 (incluye Japón y Australia; se usa la prima de Asia).",
        "B35": ("Costo de la deuda antes de impuestos = rendimiento de los bonos 5,650% a 2033 colocados el 8-sep-2026 (8-K del "
                "10-sep-2026); los 5,050% a 2029 confirman un diferencial bajo, propio de una calificación A/BBB+."),
    })


def step_arrendamientos() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Operating lease converter", {
        "E5": 58.0, "B8": 60.0, "B9": 61.0, "B10": 56.0, "B11": 37.0, "B12": 30.0, "B13": 31.0,
    }, "Arrendamientos operativos: gasto FY26 y compromisos al 31-ene-2026 (10-K FY26, nota de arrendamientos; SEC XBRL)",
        BACKUP_PATH)
    ms.write_with_backup(sh, "Input sheet", {"B18": "Yes"}, "Arrendamientos operativos como deuda (conversor; US GAAP)",
                         BACKUP_PATH)
    sh.worksheet("Operating lease converter").update_notes({
        "E5": "Costo de arrendamientos operativos FY26: 58 (10-K FY26, nota de arrendamientos; costo variable 10 aparte).",
        "B8": "Pagos de arrendamientos operativos al 31-ene-2026 (10-K FY26): FY27 60; FY28 61; FY29 56; FY30 37; FY31 30; después 31.",
    })


LEASE_PP = 19.048 / 7880         # ajuste del EBIT por arrendamientos / ventas pro forma (conversor)
LEASE_K = 233.71 / 7880          # VP de arrendamientos / ventas


def step_supuestos() -> None:
    """Caso Base de la hoja = historia Base (los cuatro escenarios están en reference/damodaran/ADSK.json)."""
    sh = ms.open_sheet(SHEET_ID)
    s2c = round(1 / (1 / 1.25 + LEASE_K), 4)
    ms.write_with_backup(sh, "Input sheet", {
        "B27": 0.1107,                         # año 1 de la historia Base (suma de las familias de productos + MaintainX)
        "B28": round(0.28 + LEASE_PP, 4),      # guía FY27 (25-27% GAAP) en la base del modelo (I+D capitalizado) + arrendamientos
        "B29": 0.0877,                         # CAGR años 2-5 de la historia Base (10,3%, 9,3%, 8,3%, 7,3%)
        "B30": round(0.34 + LEASE_PP, 4),      # 34% en la base del modelo (~31% GAAP) + ajuste de arrendamientos
        "B31": 5,
        "B32": s2c,                            # 1,25 con el capital arrendado: 1/(1/1,25 + VP arrendamientos/ventas)
        "B33": s2c,
        "B49": "Yes",
        "B50": 0.179,                          # ventaja durable: ROIC de la industria (20,6%) topado en el ROIC actual (17,9%)
    }, "Supuestos Base ADSK desde cero (7-oct-2026) = historia Base", BACKUP_PATH)
    sh.worksheet("Input sheet").update_notes({
        "B27": "Año 1 de la historia Base (reference/damodaran/ADSK.json): AECO +12%, AutoCAD +9%, manufactura +10%, M&E y otros +7%, MaintainX +55% = 11,07%.",
        "B28": ("Margen del año 1: guía FY27 de 25-27% GAAP (comunicado del 2T FY27, 27-ago-2026) llevada a la base del modelo "
                "con el I+D capitalizado (LTM: 24,9% GAAP pro forma → 27,7% en 'Valuation output'!B6) = 28%, + 0,24 pp de arrendamientos."),
        "B29": "CAGR de los años 2-5 de la historia Base: 10,3%, 9,3%, 8,3% y 7,3% (8,77%).",
        "B30": ("Margen objetivo de la Base: 34% en la base del modelo (~31% GAAP: meta de 41% no GAAP en FY29 menos ~8 pp de "
                "compensación en acciones y ~2 pp de amortización de compras; llamada del 2T FY27) + 0,24 pp de arrendamientos."),
        "B32": ("Ventas/capital 1,25 (1,205 con el capital arrendado): rendimiento del capital nuevo 34% × 75% × 1,25 ≈ 32%, entre "
                "el ROIC actual pro forma (17,9%) y el orgánico; incluye compras recurrentes. Sector (Damodaran, global) 1,54."),
        "B50": ("Ventaja durable (reference/moat_2026-09-30.json): gana sobre su costo de capital desde FY2021, costos de cambio y "
                "estándares de archivo (DWG, Revit), sin erosión visible (retención neta en el extremo alto de 100-110%). ROIC de "
                "Software (System & Application) en la base del modelo (I+D a 3 años) 20,56%, topado en el ROIC actual pro forma "
                "17,9% ('Valuation output'!B42, con MaintainX)."),
    })
    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": "Madura"}, "Tipo de empresa ADSK (ciclo de vida)", BACKUP_PATH)
    # Otros ingresos / EBIT proyectado (supuesto escrito a mano, prompt v4): LTM interés y otros +64 sobre EBIT 2.041 (+3%),
    # pero la deuda pro forma (US$4.500M) y la caja menor (US$1.625M) lo vuelven negativo: intereses ~US$200M frente a
    # ingresos financieros ~US$70M => ~ −6% del EBIT.
    ms.write_with_backup(sh, "Financials Multiples", {"E11": -0.06, "E50": -0.06, "E90": -0.06},
                         "Otros ingresos / EBIT proyectado = −6% (costo financiero neto pro forma)", BACKUP_PATH)
    sh.worksheet("Financials Multiples").update_notes({c: (
        "Supuesto escrito a mano (7-oct-2026): −6% del EBIT. Deuda pro forma US$4.500M (papel comercial 4,17%, bonos 2,40-5,65%) "
        "=> intereses ~US$200M; caja pro forma US$1.625M + 202 de valores LP al ~4% => ~US$70M. Neto ≈ −US$130M sobre un EBIT "
        "GAAP ~US$2.100M. El promedio de 3 años de la plantilla suponía la caja de antes de la compra de MaintainX.") for c in ("E11", "E50", "E90")})


def step_presentacion() -> None:
    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Descuento de múltiplos", {
        "A38": "DCF activo hoy · escenarios de las historias",
        "C38": "='Escenarios e historias'!H6", "D38": "='Escenarios e historias'!H5", "E38": "='Escenarios e historias'!H8",
        "A43": "Precio con MOS sobre el valor esperado", "C43": "", "D43": "='Escenarios e historias'!H14", "E43": "",
    }, "DCF activo = historias; MOS sobre el esperado (presentación vigente)", BACKUP_PATH)
    ms.write_with_backup(sh, "Resumen de Valoración", {"C25": PRICE_0930},
                         "Precio al día del análisis = cierre del 30-sep-2026", BACKUP_PATH)
    sh.worksheet("Resumen de Valoración").update_notes({"C25": "Cierre del 30-sep-2026 (Nasdaq): US$209,00, fecha de corte de la cartera."})
    tv = sh.worksheet("Trailing Valuation").get("L3", value_render_option="FORMULA")
    if tv and tv[0] and not str(tv[0][0]).startswith("="):
        ms.write_with_backup(sh, "Trailing Valuation", {"L3": "='Input sheet'!D1"}, "Precio LTM = precio de corte", BACKUP_PATH)


def step_content() -> None:
    import adsk_cero_content as cc

    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", cc.CUALITATIVO, "Contenido cualitativo ADSK desde cero (7-oct-2026)", bk)
    ms.write_with_backup(sh, "Estadísticas", cc.ESTADISTICAS, "Estadísticas ADSK (fórmulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", cc.STORIES, "Historia ADSK", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", cc.SUPUESTOS_RECOMENDADOS, "Recomendaciones ADSK", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": cc.MULTIPLOS_EVALUACION}, "Evaluación de múltiplos ADSK", bk)
    cc.format_estadisticas(sh)
    cc.write_tesis(sh, bk)  # después hay que volver a correr apply_multiples_v3 --apply (agrega el origen de los múltiplos)


STEPS = {"refresh": step_refresh, "balance": step_balance, "fix": step_fix, "datos": step_datos, "costo": step_costo,
         "arrendamientos": step_arrendamientos,
         "supuestos": step_supuestos, "presentacion": step_presentacion,
         "content": step_content}


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
