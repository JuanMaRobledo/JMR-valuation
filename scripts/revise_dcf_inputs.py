"""Revisión de supuestos del DCF (30-sep-2026) para GOOG, DUOL, UBER, NVDA y PLTR
(aprobada por el usuario) y, en una segunda ronda, BSX, DPZ, MSFT y NKE (retorno
sobre el capital después del año 10, 'Input sheet'!B49/B50).

Cambia solo celdas de supuestos (no fórmulas): crecimiento y margen del escenario
Base ('Input sheet'), crecimiento fijo y margen objetivo de los escenarios
Conservador / Optimista ('Valuation output' C55, C45, C106, C47), sales-to-capital
y la beta de entrada directa ('Cost of capital worksheet'!B23).

Antes de escribir guarda el valor (o fórmula) vigente de cada celda en
reference/revision_dcf_2026-09-30/<T>.json, y deja una nota en cada celda con el
valor anterior y el motivo. Con --revert restaura el respaldo.

Uso: python scripts/revise_dcf_inputs.py [--dry-run | --revert] [TICKER ...]
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

_ROOT = Path(__file__).resolve().parents[1]
OUT = _ROOT / "reference" / "revision_dcf_2026-09-30"
IS, VO, COC = "Input sheet", "Valuation output", "Cost of capital worksheet"

# (hoja, celda, valor nuevo, motivo)
CHANGES: dict[str, list[tuple[str, str, float, str]]] = {
    "GOOG": [
        (IS, "B27", 0.18, "Ingresos +24% en el 2T26 (Cloud +82%); la hoja suponía 11%."),
        (IS, "B29", 0.11, "Desaceleración con la escala; antes 7%."),
        (IS, "B30", 0.35, "Margen operativo de 34% en el 2T26 con Cloud rentable; antes 33,5%."),
        (IS, "B32", 1.2, "Capex 2026 de US$195-205 mil M: la reinversión real es muy superior a la de un S/C de 2,5."),
        (IS, "B33", 1.5, "El capex se modera pero sigue alto en los años 6-10; antes 2."),
        (COC, "B23", 1.07, "Beta por ingresos: Advertising (1,01, ~82%) y Software (1,25, ~18%), reapalancada."),
        (VO, "C55", 0.09, "Conservador: crecimiento de 9% (antes 6%, por debajo de lo que ya muestra la empresa)."),
        (VO, "C45", 0.31, "Conservador: la depreciación del capex de IA baja el margen a 31% (antes 32,5%)."),
        (VO, "C47", 0.38, "Optimista: margen de 38% con Cloud a escala (antes 37%)."),
    ],
    "DUOL": [
        (IS, "B27", 0.12, "Reservas +8% en el 2T26 y guía de reservas 2026 de +10,9%; la hoja suponía 19%."),
        (IS, "B29", 0.11, "Crecimiento de los años 2-5 alineado con las reservas; antes 16%."),
        (IS, "B30", 0.27, "Margen objetivo 27% (antes 30%): SBC de ~15% de los ingresos y costos de IA."),
        (VO, "C55", 0.08, "Conservador: 8% anual (antes 15%, por encima de las reservas actuales)."),
        (VO, "C106", 0.16, "Optimista: 16% anual si la IA reacelera las reservas (antes 23%)."),
    ],
    "UBER": [
        (IS, "B30", 0.21, "Margen GAAP de 13% en el 2T26; 26% superaba incluso el margen de los mejores segmentos. Objetivo 21%."),
        (IS, "B32", 2.5, "Flotas autónomas y Delivery Hero hacen el crecimiento más intensivo en capital; antes 3."),
    ],
    "NVDA": [
        (COC, "B23", 1.51, "Beta bottom-up de Semiconductor (Damodaran, ene-2026) en lugar de la de regresión (1,90)."),
    ],
    "PLTR": [
        (IS, "B27", 0.68, "Próximos 12 meses: ~US$10.400 M con la guía 2026 de US$8.150 M (+82% en el año calendario); antes 82% sobre el LTM."),
        (IS, "B29", 0.35, "Años 2-5 al 35% (antes 40%): tasa base de <1% de las empresas a este ritmo."),
        (IS, "B30", 0.48, "Margen objetivo 48% (antes 50%) por la compensación en acciones."),
        (COC, "B23", 1.25, "Beta bottom-up de Software (System & Application) en lugar de la de regresión (1,62)."),
        (VO, "C55", 0.35, "Conservador: 35% anual (antes 60%)."),
        (VO, "C106", 0.60, "Optimista: 60% anual (antes 95%, que multiplicaba los ingresos por 28 en cinco años)."),
    ],
    # Segunda ronda: el DCF suponía que después del año 10 el ROIC iguala al costo de
    # capital (sin retornos excedentes). Damodaran lo acepta solo sin ventajas
    # duraderas; con marca, escala o red se fija el menor entre el ROIC actual y el
    # de la industria (Damodaran, ene-2026).
    "BSX": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: Boston Scientific tiene ventajas duraderas (patentes, relación con médicos)."),
        (IS, "B50", 0.111, "ROIC terminal 11,1%: el menor entre el actual (11,1%, recortado por las compras de empresas) y el de su industria según Damodaran (17,0%)."),
    ],
    "DPZ": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: franquicia con marca y logística propias, muy poco capital."),
        (IS, "B50", 0.184, "ROIC terminal 18,4%: el de su industria según Damodaran (el actual, 99%, refleja el modelo de franquicia y no se sostiene para siempre)."),
    ],
    "MSFT": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: efectos de red y costos de cambio en Office, Azure y Windows."),
        (IS, "B50", 0.259, "ROIC terminal 25,9%: el menor entre el actual (25,9%, que ya descuenta el capex de IA) y el de su industria según Damodaran (29,3%)."),
    ],
    "NKE": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: marca global con poder de precio."),
        (IS, "B50", 0.133, "ROIC terminal 13,3%: el menor entre el actual (13,3%, con el margen deprimido) y el de su industria según Damodaran (20,9%)."),
    ],
}


def main(argv: list[str]) -> int:
    dry, revert = "--dry-run" in argv, "--revert" in argv
    tickers = [a for a in argv if not a.startswith("--")] or list(CHANGES)
    OUT.mkdir(parents=True, exist_ok=True)
    client = get_gspread_client()
    for tk in tickers:
        sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
        sh = client.open_by_key(sid)
        bk_path = OUT / f"{tk}.json"
        if revert:
            bk = json.loads(bk_path.read_text())
            data = [{"range": f"'{c['hoja']}'!{c['celda']}", "values": [[c["antes"]]]} for c in bk["cambios"]]
            sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": data})
            print(f"{tk}: restauradas {len(data)} celdas")
            continue
        ranges = [f"'{h}'!{c}" for h, c, _, _ in CHANGES[tk]]
        cur = sh.values_batch_get(ranges, params={"valueRenderOption": "FORMULA"})["valueRanges"]
        cambios = []
        for (h, c, new, why), vr in zip(CHANGES[tk], cur):
            old = (vr.get("values") or [[None]])[0][0]
            cambios.append({"hoja": h, "celda": c, "antes": old, "despues": new, "motivo": why})
            print(f"{tk:5s} {h[:24]:24s} {c:4s} {old!s:>28} -> {new}")
        if dry:
            continue
        if not bk_path.exists():  # el respaldo guarda siempre el estado original
            bk_path.write_text(json.dumps({"ticker": tk, "sheet_id": sid, "fecha": "2026-09-30", "cambios": cambios}, ensure_ascii=False, indent=1))
        sh.values_batch_update({"valueInputOption": "RAW", "data": [{"range": f"'{c['hoja']}'!{c['celda']}", "values": [[c["despues"]]]} for c in cambios]})
        for c in cambios:
            sh.worksheet(c["hoja"]).insert_note(c["celda"], f"Revisión 30-sep-2026: antes {c['antes']}, ahora {c['despues']}. {c['motivo']}")
            time.sleep(0.4)
        time.sleep(3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
