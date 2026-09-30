"""Inserta la sección «Valor con criterio Damodaran» en los análisis fundamentales
guardados (Modelo-JMR-datos/analisis/*.json), prompt de research v5 (30-sep-2026).

Toma reference/damodaran/<T>_seccion.html (damodaran_stories.py) y:
  - estructura v4 (17 secciones): la inserta como «12.» antes de «Filosofías de
    inversión», renumera 12-17 → 13-18 en los h2 y en la tabla de control de
    calidad y agrega su fila de control;
  - otras estructuras (DUOL): la agrega como sección siguiente a la última
    numerada, antes de «Fuentes y trazabilidad».
Si la sección ya existe, solo reemplaza su contenido (idempotente). No toca el
bloque de valoración vigente ni el resto del texto.

Uso: python scripts/insert_damodaran_section.py ../Modelo-JMR-datos CELH NVDA ...
"""
from __future__ import annotations

import datetime as dt
import glob
import json
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
TITLE = "Valor con criterio Damodaran"
QC_NOTE = "Historia, tasas base, piezas del valor, historias con probabilidades, pre-mortem, indicadores y precio al final"


def _renumber(html: str, first: int, last: int) -> str:
    for n in range(last, first - 1, -1):
        html = re.sub(rf"<h2>{n}\. ", f"<h2>{n + 1}. ", html)
        html = re.sub(rf"<td>{n}\. ", f"<td>{n + 1}. ", html)
    return html


def insert(html: str, section: str) -> tuple[str, str]:
    m = re.search(rf"<h2>(\d+)\. {TITLE}</h2>", html)
    if m:  # ya existe: reemplaza el cuerpo hasta el siguiente h2
        start = m.end()
        nxt = html.find("<h2", start)
        return html[:start] + "\n" + section + "\n" + html[nxt:], "actualizada"

    m = re.search(r"<h2>12\. Filosofías de inversión</h2>", html)
    if m:
        last = max(int(x) for x in re.findall(r"<h2>(\d+)\. ", html))
        html = _renumber(html, 12, last)
        pos = html.find("<h2>13. Filosofías de inversión</h2>")
        html = html[:pos] + f"<h2>12. {TITLE}</h2>\n{section}\n" + html[pos:]
        qc = html.find("<tr>\n<td>13. Filosofías de inversión</td>")
        if qc >= 0:
            html = html[:qc] + f"<tr>\n<td>12. {TITLE}</td>\n<td>Sí</td>\n<td>{QC_NOTE}</td>\n</tr>\n" + html[qc:]
        return html, "insertada (12)"

    nums = [int(x) for x in re.findall(r"<h2>(\d+)\. ", html)]
    n = (max(nums) + 1) if nums else 1
    pos = html.find("<h2>Fuentes")
    if pos < 0:
        pos = len(html)
    return html[:pos] + f"<h2>{n}. {TITLE}</h2>\n{section}\n" + html[pos:], f"insertada ({n})"


def main(argv: list[str]) -> int:
    datos, tickers = Path(argv[0]), argv[1:]
    for t in tickers:
        sec_path = _ROOT / "reference" / "damodaran" / f"{t}_seccion.html"
        files = glob.glob(str(datos / "analisis" / f"{t}-research-*.json"))
        if not sec_path.exists() or len(files) != 1:
            print(f"{t}: falta la sección ({sec_path.exists()}) o hay {len(files)} análisis")
            continue
        rec = json.loads(Path(files[0]).read_text())
        rec["html"], estado = insert(rec["html"], sec_path.read_text().strip())
        rec["updatedAt"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
        Path(files[0]).write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n")
        print(f"{t}: {estado}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
