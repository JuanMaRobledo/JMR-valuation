#!/usr/bin/env python
"""Fecha y precio del análisis = primera compra de la posición vigente (6-oct-2026).

Fuente: reference/cartera_compras_2026-10-06.json (hoja «Seguimiento de cartera» de Google Drive: Transacciones y
Posiciones, cuentas IBKR y Hapi). Para cada empresa en cartera:
  - 'Input sheet'!B4 (fecha del análisis que muestra la app) = fecha de la primera compra de la posición vigente;
  - 'Resumen de Valoración'!C25 (precio al día del análisis) = precio promedio de las compras de ese día.
Las empresas sin posición (GOOG, NVDA, PLTR) conservan el corte del 30-sep-2026 con C25 = cierre de ese día (D1).
La valoración no cambia: tasas, precio de mercado (D1), estados y DCF siguen al 30-sep-2026; B4 y C25 solo alimentan
etiquetas, el crecimiento a 3 años y la comparación «desde el análisis» del Resumen y de la app. Por eso, donde una
fórmula usaba C25 como precio de mercado (Input B23 y los textos de 'Tesis de Inversión y Supuestos'), se apunta a D1.
Respaldo en reference/revision_dcf_2026-10-05/fecha_compra_respaldo_<T>.json.

Uso: PYTHONPATH=.:scripts python scripts/fecha_compra_cartera.py [--apply] [TICKER ...]
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
C25 = "'Resumen de Valoración'!C25"
D1 = "'Input sheet'!D1"


def es(x: float) -> str:
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    datos = json.loads((_ROOT / "reference" / "cartera_compras_2026-10-06.json").read_text())["empresas"]
    tks = [a for a in argv if not a.startswith("--")] or sorted(datos)
    for tk in tks:
        c = datos[tk]
        sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
        for i in range(4):
            try:
                sh = ms.open_sheet(sid)
                v = sh.values_batch_get(["'Input sheet'!B4", "'Input sheet'!B23", C25, D1, "'Tesis de Inversión y Supuestos'!A1:F60",
                                         "'Resumen de Valoración'!B3", "'Input sheet'!A1:H120"],
                                        params={"valueRenderOption": "FORMULA"})["valueRanges"]
                b23v = sh.values_get("'Input sheet'!B23", params={"valueRenderOption": "UNFORMATTED_VALUE"}).get("values", [[None]])[0][0]
                break
            except Exception:
                time.sleep(70)
        b4, b23, c25, d1 = [(x.get("values") or [[None]])[0][0] for x in v[:4]]
        tesis = v[4].get("values", [])
        bk = OUT / f"fecha_compra_respaldo_{tk}.json"
        # 1) fórmulas que usaban C25 como precio de mercado -> D1 (mismo valor hoy)
        cambios_tesis = {}
        for i, fila in enumerate(tesis, 1):
            for j, f in enumerate(fila):
                if isinstance(f, str) and f.startswith("=") and C25 in f:
                    cambios_tesis[f"{'ABCDEF'[j]}{i}"] = f.replace(C25, D1)
        # B23 es el precio de mercado del modelo (peso del patrimonio en el costo de capital, opciones, precio/valor):
        # debe ser el cierre fijo del corte (D1), no C25 ni un GOOGLEFINANCE a la fecha de B4.
        b23_nuevo = None if str(b23).replace("'Input sheet'!", "") == "=D1" else "=D1"
        b3 = (v[5].get("values") or [[None]])[0][0]
        b3_nuevo = None if b3 == "=C25" else "=C25"
        otros_b4 = [f"{'ABCDEFGH'[j]}{i}" for i, fila in enumerate(v[6].get("values", []), 1) for j, f in enumerate(fila)
                    if isinstance(f, str) and f.startswith("=") and "B4" in f.replace("$", "") and f"{'ABCDEFGH'[j]}{i}" != "B23"]
        # 2) fecha y precio del análisis
        if c["en_cartera"]:
            y, m, d = map(int, c["primera_compra"].split("-"))
            b4_nuevo, c25_nuevo = f"=DATE({y};{m};{d})", round(c["precio_primera_compra"], 4)
            otras = [x for x in c["compras"] if x != c["primera_compra"]]
            nota = (f"Fecha y precio del análisis = primera compra de la posición vigente ({c['primera_compra']}, US${es(c25_nuevo)}"
                    f", promedio de las órdenes de ese día; cuentas: {', '.join(c['cuentas'])}). Posición al 5-oct-2026: "
                    f"{c['cantidad']:g} acciones con costo promedio de US${es(c['costo_promedio'])}"
                    + (f"; otras compras: {', '.join(otras)}" if otras else "") +
                    ". Fuente: «Seguimiento de cartera» (Drive). La valoración sigue al 30-sep-2026 (precio de mercado en "
                    "'Input sheet'!D1, tasas y estados). Cambio del 6-oct-2026.")
        else:
            b4_nuevo, c25_nuevo = None, float(d1)
            nota = (f"Sin posición en cartera ({c['nota']}): fecha y precio del análisis = corte de la valoración "
                    f"(30-sep-2026, cierre US${es(float(d1))}). Cambio del 6-oct-2026.")
        print(f"{tk:5s} B4 {b4} -> {b4_nuevo or 'igual'} | C25 {c25} -> {c25_nuevo} | B23 {'-> =D1' if b23_nuevo else 'igual'}"
              f" | Tesis {len(cambios_tesis)} fórmulas | B3 {'-> =C25' if b3_nuevo else 'igual'} | B23 {b23v} vs D1 {d1}"
              + (f" | otras fórmulas con B4 en Input: {otros_b4}" if otros_b4 else ""))
        if not apply:
            continue
        if b23_nuevo:
            if not isinstance(b23v, (int, float)) or abs(float(b23v) - float(d1)) > 0.005:
                print(f"  {tk}: B23 ({b23v}) distinto de D1 ({d1}); se detiene esta empresa")
                continue
            ms.write_with_backup(sh, "Input sheet", {"B23": b23_nuevo}, f"Precio del modelo = D1 ({tk})", bk)
        if "C23" in otros_b4:  # etiqueta del cierre que usaba B4: queda con la fecha fija del corte
            ms.write_with_backup(sh, "Input sheet", {"A23": "Precio de mercado del corte (cierre del 30-sep-2026) =",
                                                     "C23": "=DATE(2026;9;30)"}, f"Etiqueta del precio del corte ({tk})", bk)
        if b3_nuevo:
            ms.write_with_backup(sh, "Resumen de Valoración", {"B3": b3_nuevo}, f"Precio del análisis = C25 ({tk})", bk)
        if cambios_tesis:
            ms.write_with_backup(sh, "Tesis de Inversión y Supuestos", cambios_tesis, f"Textos con el precio de mercado ({tk})", bk)
        if b4_nuevo:
            ms.write_with_backup(sh, "Input sheet", {"B4": b4_nuevo}, f"Fecha del análisis = primera compra ({tk})", bk)
            sh.worksheet("Input sheet").update_notes({"B4": nota})
        ms.write_with_backup(sh, "Resumen de Valoración", {"C25": c25_nuevo}, f"Precio del análisis ({tk})", bk)
        sh.worksheet("Resumen de Valoración").update_notes({"C25": nota})
        time.sleep(2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
