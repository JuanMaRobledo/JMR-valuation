#!/usr/bin/env python
"""Lleva el corte vigente (reference/corte_vigente.json, de scripts/datos_mercado.py) a las hojas, 6-oct-2026.

Por hoja (respaldo en reference/cortes/<fecha>/respaldo_<T>.json; nota en las celdas que cambian):
  - precio y fecha: 'Input sheet'!D1 = cierre del corte, B4 = fecha del corte, B23 = D1 (precio de mercado del modelo:
    peso del patrimonio, opciones, precio/valor), 'Trailing Valuation'!L3 = D1 si era un número suelto,
    'Resumen de Valoración'!C25 = cierre y B3 = C25;
  - tasas: 'Input sheet'!B35 = Treasury a 10 años del corte; 'Country equity risk premiums'!B2 = prima madura de
    Damodaran del mismo corte; 'Cost of capital worksheet'!B27 = prima madura si tenía la anterior;
  - Brasil: AFYA 'Input sheet'!B47 y PAGS B47 y 'DCF FCFE financiero'!B4 = tasa + prima + diferencial país;
  - ROIC terminal: se recalcula con el costo de capital terminal nuevo según reference/moat_2026-09-30.json (ventaja
    durable: la referencia sin bajar del costo terminal; que se desvanece: punto medio entre el costo terminal y la
    referencia); si B49 = "No" queda el costo de capital.
También actualiza reference/moat_2026-09-30.json (costo_capital_terminal y roic_terminal).
No toca supuestos de las historias: los resultados nuevos se revisan aparte (novedades_sec.py y la historia de cada
empresa).

Uso: PYTHONPATH=.:scripts python scripts/aplicar_corte.py [--apply] [TICKER ...]
"""
from __future__ import annotations

import datetime as dt
import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402

MOAT = _ROOT / "reference" / "moat_2026-09-30.json"


def leer(sh, rangos):
    for i in range(4):
        try:
            return [(x.get("values") or [[None]])[0][0] for x in
                    sh.values_batch_get(rangos, params={"valueRenderOption": "FORMULA"})["valueRanges"]]
        except Exception:
            time.sleep(70)
    raise RuntimeError("cuota de Google")


def roic_regla(m: dict, terminal: float):
    if m.get("roic_terminal") is None:
        return None
    ref = m.get("referencia")
    if m["ventaja"] == "ventaja durable":
        return round(max(ref, terminal), 4)
    if m["ventaja"] == "ventaja que se desvanece":
        return round((terminal + ref) / 2, 3)
    return m["roic_terminal"]


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    c = json.loads((_ROOT / "reference" / "corte_vigente.json").read_text())
    f = dt.date.fromisoformat(c["fecha_corte"])
    out = _ROOT / "reference" / "cortes" / c["fecha_corte"]
    moat_all = json.loads(MOAT.read_text())
    moat = moat_all["empresas"]
    tks = [a for a in argv if not a.startswith("--")] or sorted(c["cierres"])
    nota = (f"Corte {c['fecha_corte_es']}: cierre de Yahoo Finance; Treasury 10 años {c['rf']*100:.2f}% ({c['rf_fuente']}); "
            f"prima madura de Damodaran de {c['erp_mes']} {c['erp_madura']*100:.2f}% ({c['erp_archivo']}), calculada con "
            f"la misma tasa. scripts/aplicar_corte.py.")
    for tk in tks:
        sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
        sh = ms.open_sheet(sid)
        d1, b4, b23, b35, b49, b50, l3, c25, b3, b2, b27 = leer(sh, [
            "'Input sheet'!D1", "'Input sheet'!B4", "'Input sheet'!B23", "'Input sheet'!B35", "'Input sheet'!B49",
            "'Input sheet'!B50", "'Trailing Valuation'!L3", "'Resumen de Valoración'!C25", "'Resumen de Valoración'!B3",
            "'Country equity risk premiums'!B2", "'Cost of capital worksheet'!B27"])
        cierre = c["cierres"][tk]
        term = c["terminal_brasil"].get(tk, c["costo_capital_terminal"])
        cambios = {"Input sheet": {"D1": cierre, "B4": f"=DATE({f.year};{f.month};{f.day})", "B35": c["rf"]},
                   "Resumen de Valoración": {"C25": cierre},
                   "Country equity risk premiums": {"B2": c["erp_madura"]}}
        if str(b23).replace("'Input sheet'!", "") != "=D1":
            cambios["Input sheet"]["B23"] = "=D1"
        if b3 != "=C25":
            cambios["Resumen de Valoración"]["B3"] = "=C25"
        if isinstance(l3, (int, float)):
            cambios["Trailing Valuation"] = {"L3": "='Input sheet'!D1"}
        if isinstance(b27, (int, float)) and isinstance(b2, (int, float)) and abs(b27 - b2) < 1e-6:
            cambios["Cost of capital worksheet"] = {"B27": c["erp_madura"]}
        if tk in c["terminal_brasil"]:
            cambios["Input sheet"]["B47"] = term
            if tk == "PAGS":
                cambios["DCF FCFE financiero"] = {"B4": term}
        m = moat.get(tk, {})
        nuevo_roic = roic_regla(m, term) if m else None
        if str(b49) == "Yes" and nuevo_roic is not None and isinstance(b50, (int, float)) and abs(b50 - nuevo_roic) > 0.001:
            cambios["Input sheet"]["B50"] = nuevo_roic
        if m:
            m["costo_capital_terminal"] = term
            if nuevo_roic is not None:
                m["roic_terminal"] = nuevo_roic
        print(f"{tk:5s} precio {d1} -> {cierre} | rf {b35} -> {c['rf']} | prima {b2} -> {c['erp_madura']} | terminal {term}"
              + (f" | ROIC terminal {b50} -> {cambios['Input sheet']['B50']}" if "B50" in cambios["Input sheet"] else ""))
        if not apply:
            continue
        bk = out / f"respaldo_{tk}.json"
        for hoja, celdas in cambios.items():
            ms.write_with_backup(sh, hoja, celdas, f"Corte {c['fecha_corte']} ({tk})", bk)
        sh.worksheet("Input sheet").update_notes({"D1": nota, "B35": nota})
        sh.worksheet("Country equity risk premiums").update_notes({"B2": nota})
        time.sleep(3)
    if apply:
        moat_all["corte"] = c["fecha_corte"]
        MOAT.write_text(json.dumps(moat_all, ensure_ascii=False, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
