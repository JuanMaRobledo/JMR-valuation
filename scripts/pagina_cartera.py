#!/usr/bin/env python
"""Página de lectura «Cartera Modelo JMR» (HTML para el Artifact), 6-oct-2026.

Lee de cada hoja (scripts/valores_hoja.py) precio, DCF Base, esperado, rango de historias, beta y costo de capital; de la
valoración guardada (Modelo-JMR-datos) el precio con MOS, la hoja y la posición; de reference/cartera_drive.json los
enlaces de Drive; y del corte vigente (reference/corte_vigente.json) la tasa, la prima y el costo terminal. «Antes» = DCF
Base de reference/damodaran/<T>_resultado.json en --antes (una referencia de git; por defecto origin/main).
Escribe --out (por defecto reference/pagina/cartera.html), que se publica con la herramienta Artifact en la misma URL.

Uso: PYTHONPATH=.:scripts python scripts/pagina_cartera.py [--antes REF] [--out archivo.html]
"""
from __future__ import annotations

import argparse
import glob
import json
import subprocess
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import valores_hoja  # noqa: E402


def es(x, nd=2):
    return f"{x:,.{nd}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--antes", default="origin/main")
    ap.add_argument("--out", default=str(_ROOT / "reference" / "pagina" / "cartera.html"))
    a = ap.parse_args(argv)
    drive = json.loads((_ROOT / "reference" / "cartera_drive.json").read_text())["empresas"]
    corte = json.loads((_ROOT / "reference" / "corte_vigente.json").read_text())
    rows = []
    for t in sorted(drive):
        v = valores_hoja.leer(t)
        sp = json.loads((_ROOT / "reference" / "damodaran" / f"{t}.json").read_text())
        sv = json.loads(Path([p for p in glob.glob(str(_ROOT.parent / "Modelo-JMR-datos" / "valoraciones" / f"{t}-*.json"))
                              if "regen" not in p][0]).read_text())
        try:
            r0 = json.loads(subprocess.check_output(["git", "show", f"{a.antes}:reference/damodaran/{t}_resultado.json"],
                                                    cwd=_ROOT, stderr=subprocess.DEVNULL))
            antes = r0["historias"][0]["valor_beta_hoja"]
        except Exception:
            antes = v["base"]
        links = []
        for path, fid in drive[t].items():
            n = path.split("/")[-1]
            lab = ("Análisis Damodaran" if "Analisis_Damodaran" in n else "Research" if "Research" in n else
                   "Valoración" + (" v4" if "2026-10-0" in n and "09-30" not in n else "") if "Valoracion" in n else n)
            links.append({"lab": lab, "url": f"https://drive.google.com/file/d/{fid}/view"})
        orden = {"Análisis Damodaran": 0, "Valoración": 1, "Valoración v4": 2, "Research": 3}
        links.sort(key=lambda x: orden.get(x["lab"], 9))
        rows.append({"t": t, "nombre": sp.get("empresa") or t, "frase": sp.get("frase") or "", "precio": v["precio"],
                     "base": v["base"], "ve": v["ve"], "min": min(v["vA"], v["vB"], v["vC"], v["vD"]),
                     "max": max(v["vA"], v["vB"], v["vC"], v["vD"]),
                     "mos": sv.get("precioMOSValorEsperado") or sv.get("precioMOS"), "beta": v["beta"], "w0": v["w0"],
                     "wT": v["wT"], "fin": v["fin"], "hoja": sv.get("hojaGoogle"), "links": links,
                     "ind": sp.get("industria_damodaran") or "", "antes": antes, "pos": sv.get("posicion")})
        time.sleep(1.2)
    tpl = (_ROOT / "reference" / "pagina" / "cartera_tpl.html").read_text()
    for viejo, nuevo in (("30-sep-2026</b><span>Corte", f"{corte['fecha_corte_es']}</b><span>Corte"),
                         ("<b>5,29%</b>", f"<b>{es(corte['rf'] * 100)}%</b>"),
                         ("<b>3,70%</b><span>Prima madura, Damodaran oct-2026", f"<b>{es(corte['erp_madura'] * 100)}%</b><span>Prima madura, Damodaran {corte['erp_mes_corto']}"),
                         ("<b>8,99%</b>", f"<b>{es(corte['costo_capital_terminal'] * 100)}%</b>"),
                         ("Las 22 valoraciones", f"Las {len(rows)} valoraciones"),  # 7-oct-2026: MCD y ADSK suman 24
                         ('<b id="n-emp">22</b>', f'<b id="n-emp">{len(rows)}</b>')):
        tpl = tpl.replace(viejo, nuevo)
    Path(a.out).write_text(tpl.replace("/*DATA*/[]", json.dumps(rows, ensure_ascii=False)))
    print("escrito", a.out, len(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
