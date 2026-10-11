#!/usr/bin/env python
"""Tipo de empresa según el ciclo de vida de Damodaran y el sector (5-oct-2026).

Cada empresa se ubica en una etapa de Damodaran (crecimiento joven, alto, maduro, madura estable o declive) con las cuatro
variables de su cuadro (crecimiento de ventas, margen operativo, reinversión y flujo libre: SEC, tres últimos ejercicios, y
la historia Base de la hoja) y se le asigna el tipo de empresa de 'Resumen de Valoración'!G3 que corresponde a cómo
Damodaran pone precio en esa etapa y en ese sector. Fuentes y mapeo: reference/ciclo_de_vida/clasificacion_2026-10-05.json.
El tipo solo cambia los pesos del precio relativo (ponderado DCF + múltiplos); el DCF no cambia.
Respaldo en reference/revision_dcf_2026-10-05/ciclo_respaldo_<T>.json.

Uso: PYTHONPATH=.:scripts python scripts/ciclo_de_vida.py [--apply] [TICKER ...]
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402

OUT = _ROOT / "reference" / "revision_dcf_2026-10-05"
# ticker: (etapa de Damodaran, sector de Damodaran, tipo, evidencia)
C = {
    "ADSK": ("Crecimiento maduro", "Software (System & Application)", "Madura",
             "Ventas +12%, +12%, +18% en FY2024-FY2026 (+16% en el 2T FY27 con ~2 pp del nuevo modelo de transacción y ~2 pp "
             "de moneda); Base ~10%; margen GAAP 20-22% en FY2024-FY2026 y 26% LTM, en expansión moderada hacia ~31%; flujo "
             "libre de 33% de las ventas en FY2026; recompras de ~50% del flujo libre: utilidades positivas y estables, se "
             "valora por P/E futuro y EV/EBITDA (7-oct-2026)."),
    "ADBE": ("Madura estable (final del crecimiento maduro)", "Software (System & Application)", "Madura",
             "Ventas +10-11% en FY2023-FY2025 y 8,1% en la Base; margen operativo estable (31-37%, objetivo 40%); flujo libre "
             "estable (36-42% de las ventas); devuelve 37-47% de las ventas en recompras."),
    "AFYA": ("Madura estable", "Education", "Madura",
             "Ventas +23%, +15%, +12% y ~7% en el 1S26 (5,8% en la Base, en reales); margen estable (31-33%); flujo libre "
             "~37% de las ventas; plazas reguladas."),
    "BSX": ("Crecimiento maduro, cerca de madura estable", "Healthcare Products", "Madura",
            "Ventas orgánicas ~7% en el 2T26 y 5-6% de guía; Base 6,1%; margen GAAP en alza por la amortización de compras "
            "pasadas (ajustado estable ~28%); flujo libre de 7% a 18% de las ventas con menos compras; utilidades positivas y "
            "estables: se valora por P/E futuro y EV/EBITDA."),
    "CELH": ("Crecimiento maduro (marcas jóvenes que ya crecen poco)", "Beverage (Soft)", "Madura",
             "Crecimiento comprado (Alani Nu, Rockstar) y orgánico bajo: Base 4,8%; margen normalizado estable (19,6% → 20,1%); "
             "flujo libre positivo (9-18% de las ventas). Las utilidades GAAP fueron volátiles por cargos de una vez, pero los "
             "múltiplos se aplican a las utilidades proyectadas FY+1 a FY+3, ya normalizadas (Damodaran: P/E normalizado)."),
    "CMG": ("Madura estable (crecimiento por aperturas)", "Restaurant/Dining", "Madura",
            "Ventas +14%, +15% y +5% (2025); Base 7,2% (~8% por aperturas y comparables bajas); margen estable (15-17%); flujo "
            "libre estable (10-13%); recompras de 20% de las ventas en 2025."),
    "DPZ": ("Madura estable", "Restaurant/Dining", "Madura",
            "Ventas −1%, +5%, +5%; Base 4,5%; margen estable (18-20%); flujo libre estable; recompras con deuda titulizada."),
    "DUOL": ("Transición de crecimiento alto a crecimiento maduro", "Software (Internet)", "Crecimiento",
             "Ventas +44%, +41%, +39% y +18% en el 2T26; margen operativo GAAP recién positivo (−2% en 2023, 13% en 2025) y en "
             "expansión (20% → 27% en la Base); flujo libre de 13% a 36% de las ventas; utilidad de 2025 inflada por la "
             "liberación de la reserva fiscal: aún no se valora por P/E estable."),
    "EPAM": ("Madura estable (con riesgo de declive por la IA)", "Computer Services", "Madura",
             "Ventas −3%, +1%, +15% (con compras) y ~6% en el 1S26; Base 5,5%; margen estable (10-12%); flujo libre ~11%; "
             "recompras."),
    "GOOG": ("Crecimiento maduro", "Software (Internet)", "Madura",
             "Ventas +9-15%; Base 11,7%; margen estable en ~32-34%; reinversión en alza por la IA; utilidades positivas, "
             "estables y enormes: se valora por P/E futuro y EV/EBITDA."),
    "INTU": ("Crecimiento maduro", "Software (System & Application)", "Madura",
             "Ventas +13-16%; Base 9,8%; margen 22% → 27% histórico y estable en la Base (32%); flujo libre 29-40%; "
             "recompras crecientes: utilidades estables (antes «Software», que pesa como Crecimiento)."),
    "LULU": ("Madura estable con rasgos de declive", "Apparel", "Madura",
             "Ventas +19%, +10%, +5% y caída en Américas; Base 1,7% (−6,5% el primer año); margen en baja (24% → ~13%) con "
             "recuperación a 18,7%; flujo libre positivo; recompras. Damodaran pone precio al declive con valor en libros o "
             "de liquidación, que el modelo no tiene; mientras haya utilidades, Madura."),
    "MSFT": ("Crecimiento maduro", "Software (System & Application)", "Madura",
             "Ventas +15-18%; Base 13%; margen estable (45-47%); reinversión en alza por el capex de IA; utilidades positivas, "
             "estables y enormes: se valora por P/E futuro y EV/EBITDA (antes «Software», que pesa como Crecimiento)."),
    "NKE": ("Declive (reestructuración)", "Shoe", "Madura",
            "Ventas 0%, −10%, 0%; Base 1,3% (−6,6% el primer año); margen en baja (de ~13% a ~6%) con recuperación a 11,6%; "
            "flujo libre de 13% a 5% de las ventas. Igual que LULU: Madura mientras haya utilidades."),
    "NVDA": ("Crecimiento alto (rentable)", "Semiconductor", "Crecimiento",
             "Ventas +126%, +114%, +65%; Base 17,1% (46,7% el primer año); margen de 16% (2023, fondo del ciclo) a ~60%; "
             "semiconductores es manufactura cíclica (Damodaran: P/E normalizado), así que las utilidades de hoy no son una base "
             "estable: más peso al DCF (antes «Madura»)."),
    "NU": ("Crecimiento alto que pasa a crecimiento maduro (banco digital)", "Financial Svcs. (Non-bank & Insurance)",
           "Financiera",
           "Ingresos +68%, +43%, +37% (2023-2025, NIIF en dólares); Base ~15% anual cinco años; utilidad positiva y en alza "
           "(ROE 21% → 38% sobre el patrimonio de inicio); balance de banco (depósitos US$45.300 M, CET1 11,9%): Damodaran "
           "pone precio a los bancos con P/BV y flujo al accionista, no con múltiplos de EV."),
    "NVO": ("Transición a declive (patentes y precio)", "Drugs (Pharmaceutical)", "Biotech/Farma",
            "Ventas +31%, +25%, +6% y +2% en el 1S26; Base 0,8% (−3,4% el primer año); margen en baja (44% → 40%); flujo libre "
            "de 38% a 19% de las ventas; genéricos de semaglutida fuera de EE.UU. desde 2026: utilidades en cambio que dependen "
            "de patentes y del portafolio (antes «Madura»)."),
    "ONON": ("Crecimiento alto que pasa a crecimiento maduro", "Shoe", "Crecimiento",
             "Ventas +47%, +29%, +30%; Base 14,7%; margen en expansión (10% → 16,5%); flujo libre positivo; aún sin "
             "utilidades en su nivel estable."),
    "PAGS": ("Madura estable (banco digital; adquirencia en declive)", "Financial Svcs. (Non-bank & Insurance)", "Financiera",
             "Servicios financieros con balance de banco (depósitos, crédito, Basilea): Damodaran usa P/BV y flujo al "
             "accionista."),
    "PLTR": ("Crecimiento alto", "Software (System & Application)", "Crecimiento",
             "Ventas +17%, +29%, +56%; Base 35,3%; margen de −8% (2022) a 32% (2025) y 48% LTM; utilidades aún en expansión."),
    "PYPL": ("Madura estable (con riesgo de declive en el botón de pago)", "Financial Svcs. (Non-bank & Insurance)", "Madura",
             "Ventas +8%, +7%, +4%; Base 4,9%; margen estable (17-19%); flujo libre estable; recompras de ~19% de las ventas. Se "
             "valora como empresa no financiera (flujo a la firma), no como banco: Madura y no Financiera."),
    "SHAK": ("Crecimiento alto", "Restaurant/Dining", "Crecimiento",
             "Ventas +21%, +15%, +15%; Base 11%; margen cerca de cero (−3% → 4%) en expansión a 9,5%; flujo libre cerca de cero "
             "porque las aperturas consumen el flujo operativo."),
    "UBER": ("Transición de crecimiento alto a crecimiento maduro", "Transportation", "Crecimiento",
             "Ventas +17-18%; Base 10,9%; margen recién positivo (−6% en 2022, 12% LTM) y en expansión a 22%; flujo libre de 1% "
             "a 19% de las ventas; utilidad neta inflada por impuestos diferidos y revaluación de inversiones: aún no se "
             "valora por P/E estable (antes «Madura»)."),
    "ZTS": ("Madura estable", "Drugs (Pharmaceutical)", "Madura",
            "Ventas +6%, +8%, +2% y −0,2% en el 2T26; Base 4,5%; margen estable (~37%); flujo libre estable; recompras de 34% "
            "de las ventas en 2025. Farmacéutica, pero con utilidades estables y franquicias crónicas: Madura."),
}


def main(argv: list[str]) -> int:
    solo = [a.upper() for a in argv if not a.startswith("--")]
    for tk, (etapa, sector, tipo, ev) in C.items():
        if solo and tk not in solo:
            continue
        sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
        for i in range(4):
            try:
                sh = ms.open_sheet(sid)
                antes = sh.values_get("'Resumen de Valoración'!G3").get("values", [[None]])[0][0]
                break
            except Exception:
                time.sleep(70)
        marca = "" if antes == tipo else "  <- cambia"
        print(f"{tk:5s} {antes:12s} -> {tipo:13s} | {etapa}{marca}")
        if "--apply" in argv and antes != tipo:
            ms.write_with_backup(sh, "Resumen de Valoración", {"G3": tipo}, f"Tipo por ciclo de vida ({tk}, 5-oct-2026)",
                                 OUT / f"ciclo_respaldo_{tk}.json")
        if "--apply" in argv:
            sh.worksheet("Resumen de Valoración").update_notes({"G3": (
                f"Tipo «{tipo}» (5-oct-2026). Etapa del ciclo de vida de Damodaran: {etapa}. Sector: {sector}. {ev} "
                f"Mapeo y fuentes: reference/ciclo_de_vida/clasificacion_2026-10-05.json. Antes: «{antes}».")})
        time.sleep(1.5)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
