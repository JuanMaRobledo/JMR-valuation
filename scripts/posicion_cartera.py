#!/usr/bin/env python
"""Fecha del análisis real y bloque «Mi posición» en el Resumen (6-oct-2026).

La fecha y el precio del análisis (B4, C25) son los del corte y los escribe scripts/aplicar_corte.py; este script solo
escribe la posición. 'Resumen de Valoración'!A50:E60 («Mi posición en cartera»): acciones, costo promedio de compra y primera compra
   (el reference/cartera_compras_<fecha>.json más reciente, de scripts/posiciones_cartera.py: app Cartera o Drive) y la ganancia potencial sobre
   ese costo hasta el precio del análisis, el DCF Base, el DCF esperado y el precio con MOS (fórmulas vivas).
Respaldo en reference/revision_dcf_2026-10-05/posicion_respaldo_<T>.json.

Uso: PYTHONPATH=.:scripts python scripts/posicion_cartera.py [--apply] [TICKER ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402

OUT = _ROOT / "reference" / "revision_dcf_2026-10-05"
CORTE = {"LULU": (2026, 10, 1), "NKE": (2026, 10, 1), "ONON": (2026, 10, 1)}  # resto: 30-sep-2026
RS = "Resumen de Valoración"


HOY = ("=IFERROR(GOOGLEFINANCE(IFERROR(REGEXEXTRACT('Input sheet'!A1;\"\\(([^)]+)\\)\");'Input sheet'!A1);\"price\");\"\")")


def bloque(c: dict, fecha: str = "", fuente: str = "") -> dict:
    b = {f"{col}{r}": "" for r in range(50, 61) for col in "ABCDE"}
    b["A50"] = "MI POSICIÓN EN CARTERA"
    origen = "app Cartera" if fuente.startswith("app Cartera") else "«Seguimiento de cartera» (Google Drive)"
    b["B50"] = f"Fuente: {origen}, posiciones al {fecha}"
    if not c["en_cartera"]:
        b["A51"] = f"Sin posición en cartera ({c['nota']})."
        return b
    y, m, d = map(int, c["primera_compra"].split("-"))
    b.update({
        "A51": "Acciones", "B51": c["cantidad"],
        "A52": "Costo promedio de compra (US$)", "B52": c["costo_promedio"],
        "A53": "Primera compra", "B53": f"=DATE({y};{m};{d})", "C53": "Compras: " + ", ".join(c["compras"]),
        "A54": "Precio", "B54": "US$ por acción", "C54": "Ganancia sobre tu costo", "D54": "Posición (US$)",
        "A55": "Precio de hoy (GOOGLEFINANCE, en vivo)", "B55": HOY,
        "C55": '=IFERROR(B55/$B$52-1;"")', "D55": '=IFERROR((B55-$B$52)*$B$51;"")',
        "A56": "Precio del análisis (cierre del corte)", "B56": "='Input sheet'!D1",
        "C56": '=IFERROR(B56/$B$52-1;"")', "D56": '=IFERROR((B56-$B$52)*$B$51;"")',
        "A57": "Ganancia potencial hasta el valor", "B57": "Valor por acción", "C57": "Desde el precio de hoy",
        "D57": "Desde tu precio de compra", "E57": "Posición (US$, desde tu costo)",
    })
    for r, (lab, f) in enumerate([("DCF Base hoy (valor intrínseco)", "=D32"),
                                   ("DCF esperado de las historias", "=D38"),
                                   ("Ponderado DCF + múltiplos Base hoy (secundario)", "=D34")], start=58):
        b[f"A{r}"] = lab
        b[f"B{r}"] = f
        b[f"C{r}"] = f'=IFERROR(B{r}/$B$55-1;"")'
        b[f"D{r}"] = f'=IFERROR(B{r}/$B$52-1;"")'
        b[f"E{r}"] = f'=IFERROR((B{r}-$B$52)*$B$51;"")'
    return b


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    archivo = sorted((_ROOT / "reference").glob("cartera_compras_*.json"))[-1]  # el más reciente (posiciones_cartera.py)
    compras = json.loads(archivo.read_text())
    datos = compras["empresas"]
    for tk in [a for a in argv if not a.startswith("--")] or sorted(datos):
        sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
        sh = ms.open_sheet(sid)
        b = bloque(datos[tk], compras["fecha"], compras.get("fuente", ""))
        print(f"{tk:5s} posición: "
              + (f"{datos[tk]['cantidad']:g} acc. a US${datos[tk]['costo_promedio']}" if datos[tk]["en_cartera"] else "no"))
        if not apply:
            continue
        bk = OUT / f"posicion_respaldo_{tk}.json"
        ms.write_with_backup(sh, RS, b, f"Bloque «Mi posición» ({tk})", bk)
        ws = sh.worksheet(RS)
        ws.format("A50", {"textFormat": {"bold": True}})
        if datos[tk]["en_cartera"]:
            pct = {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}}
            usd = {"numberFormat": {"type": "CURRENCY", "pattern": "\"US$\"#,##0.00"}}
            for rg, f in (("C55:C56", pct), ("C58:D60", pct), ("B52", usd), ("B55:B56", usd), ("B58:B60", usd),
                          ("D55:D56", usd), ("E58:E60", usd)):
                ws.format(rg, f)
            ws.format("A54:E54", {"textFormat": {"bold": True}})
            ws.format("A57:E57", {"textFormat": {"bold": True}})
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
