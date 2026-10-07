#!/usr/bin/env python
"""Carga un análisis fundamental en Markdown (prompt de research v5) en la app (6-oct-2026, aprendido con MCD).

Hace lo mismo que research.html al subir un .md: quita los metadatos, convierte el cuerpo con marked 12.0.2 (gfm) y
vincula la valoración guardada de la empresa (linkedValuation, mismos campos que research.js). Si la empresa ya tiene
un análisis en la app, reemplaza su html y fuente y conserva id, ruta y demás campos; si no, crea uno nuevo
(Modelo-JMR-datos/analisis/<T>-research-<ms>-<5>.json). Después corre la cadena de la app (regenerar_cartera.sh <T>:
sección Damodaran, tabla de escenarios, horizontes y consistencia).

Uso: MARKED_PATH=.cache/js/marked.min.js python scripts/research_md_a_app.py TICKER data/<T>_Research_...md
"""
from __future__ import annotations

import datetime as dt
import glob
import json
import os
import random
import string
import subprocess
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
DATOS = _ROOT.parent / "Modelo-JMR-datos"
CAMPOS = ("precio", "fecha", "zonas", "objetivoPonderado", "valorPresentePonderado", "descuentoMultiples", "metodos",
          "hojas", "cagr", "mos", "hojaGoogle", "valorEsperado", "multiplesHistoricos")


def md_a_html(md: str) -> str:
    marked = os.environ.get("MARKED_PATH") or str(_ROOT / ".cache" / "js" / "marked.min.js")
    body = md.split("\n---\n", 1)[1] if md.startswith("---\n") else md
    js = ("const m=require(process.argv[1]);let s='';process.stdin.on('data',d=>s+=d);"
          "process.stdin.on('end',()=>process.stdout.write(m.parse(s,{gfm:true,breaks:false})));")
    return subprocess.run(["node", "-e", js, marked], input=body, capture_output=True, text=True, check=True).stdout


def main(argv: list[str]) -> int:
    tk, md_path = argv[0].upper(), Path(argv[1])
    md = md_path.read_text()
    meta = {}
    if md.startswith("---\n"):
        for line in md.split("\n---\n", 1)[0].splitlines()[1:]:
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
    vals = [p for p in glob.glob(str(DATOS / "valoraciones" / f"{tk}-*.json")) if "regen" not in p]
    rec = json.loads(Path(vals[0]).read_text()) if vals else {}
    linked = {k: rec.get(k) for k in CAMPOS}
    if vals:
        linked["sourcePath"] = "valoraciones/" + Path(vals[0]).name
    prev = glob.glob(str(DATOS / "analisis" / f"{tk}-research-*.json"))
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    if prev:
        out = json.loads(Path(prev[0]).read_text())
        path = Path(prev[0])
    else:
        rid = f"research-{int(time.time() * 1000)}-" + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
        path = DATOS / "analisis" / f"{tk}-{rid}.json"
        out = {"id": rid, "ticker": tk, "logo": f"https://images.financialmodelingprep.com/symbol/{tk}.png",
               "valuationHtml": "", "news": "", "remotePath": f"analisis/{path.name}"}
    out.update({"title": meta.get("title") or out.get("title") or tk, "company": meta.get("company") or out.get("company") or tk,
                "date": meta.get("analysis_date") or out.get("date"), "html": md_a_html(md), "sourceName": md_path.name,
                "price": str(rec.get("precio") or out.get("price") or ""), "linkedValuation": linked,
                "linkedValuationAtResearch": linked, "updatedAt": now})
    out.setdefault("priceFetchedAt", (meta.get("information_cutoff") or now[:10]) + "T20:00:00+00:00")
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    print("guardado", path.relative_to(DATOS), len(out["html"]), "caracteres de html")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
