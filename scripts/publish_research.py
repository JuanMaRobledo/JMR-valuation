"""Publica un research fundamental v4 (Markdown) en Modelo-JMR-datos/analisis/
con el mismo formato que guarda docs/research.js: HTML del documento (sin el
bloque de metadatos), vinculado a la valoracion mas reciente del ticker en
valoraciones/ (sin recalcular nada).

Uso: python scripts/publish_research.py TICKER ruta.md [ruta_render.md]
Si el .md tiene marcadores {{TABLA_*}}, antes se rellenan con research_tables."""
import json
import random
import re
import string
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(ROOT), str(ROOT / "scripts")]
DATOS = ROOT.parent / "Modelo-JMR-datos"


def main(ticker: str, md_path: str) -> Path:
    text = Path(md_path).read_text(encoding="utf-8")
    if "{{TABLA_" in text:
        import research_tables as rt
        text = rt.render(ticker, text)
        Path(md_path).write_text(text, encoding="utf-8")
    meta = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip().strip('"')
        text = text[m.end():]
    text = re.sub(r"\n  (\d+\. )", r"\n    \1", text)  # listas anidadas: python-markdown exige 4 espacios
    html = markdown.markdown(text, extensions=["tables", "sane_lists"])
    vals = sorted((DATOS / "valoraciones").glob(f"{ticker}-*.json"))
    rec = json.loads(vals[-1].read_text())
    now_ms = int(time.time() * 1000)
    rid = f"research-{now_ms}-" + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
    iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    out = {
        "id": rid, "title": meta.get("title", f"Análisis fundamental de {ticker}"), "ticker": ticker,
        "company": meta.get("company", ticker), "date": meta.get("analysis_date", iso[:10]),
        "logo": f"https://images.financialmodelingprep.com/symbol/{ticker}.png",
        "price": rec.get("precio"), "priceFetchedAt": iso, "html": html,
        "sourceName": Path(md_path).name, "valuationHtml": "",
        "linkedValuation": {"precio": rec.get("precio"), "fecha": rec.get("fecha"), "zonas": rec.get("zonas"),
                            "objetivoPonderado": rec.get("objetivoPonderado"), "cagr": rec.get("cagr"),
                            "sourcePath": f"valoraciones/{vals[-1].name}"},
        "news": "", "remotePath": f"analisis/{ticker}-{rid}.json", "updatedAt": iso,
    }
    dest = DATOS / out["remotePath"]
    dest.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print(ticker, dest.name, "html", len(html), "vinculado a", vals[-1].name)
    return dest


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
