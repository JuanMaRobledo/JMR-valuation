#!/usr/bin/env python
"""Nota de actualización en el research de la app tras la revisión de betas y ventas/capital (5-oct-2026).

Las tablas de auditoría y de supuestos del research son la instantánea de la hoja a la fecha del informe; después de la
revisión con criterio Damodaran (scripts/revisar_beta_s2c.py) pueden mostrar una beta, un WACC o un ventas/capital
anteriores. Esta nota, al inicio del informe (antes de la primera sección), deja las cifras vigentes y remite a la sección
de historias Damodaran y a la valoración, que el flujo de regeneración sí mantiene al día. Es idempotente: reemplaza la
nota si ya está. Las cifras se leen de la hoja de cálculo (scripts/valores_hoja.py). Escribe el HTML del research en Modelo-JMR-datos/analisis y, si existe, el .md de origen en data/.

Uso: PYTHONPATH=.:scripts python scripts/nota_revision_research.py [TICKER ...]
"""
from __future__ import annotations

import datetime as dt
import glob
import json
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
DATOS = _ROOT.parent / "Modelo-JMR-datos"
INI, FIN = "<!-- JMR-NOTA-REVISION-2026-10-05 -->", "<!-- /JMR-NOTA-REVISION-2026-10-05 -->"

# ticker -> (beta antes, ventas/capital antes o None si no cambió, texto de la beta)
ANTES = {
    "ADBE": (1.39, None, "bottom-up de Software en EE.UU."),
    "LULU": (1.03, None, "bottom-up de Apparel en EE.UU., sin la prima por moda"),
    "NKE": (None, (2.1, 2.1), "bottom-up de Shoe global, sin cambio"),
    "ONON": (1.20, None, "bottom-up de Shoe en EE.UU., sin la prima por moda"),
    "CMG": (0.95, None, "bottom-up de Restaurant/Dining en EE.UU., sin la prima por un solo concepto"),
    "DPZ": (1.17, (2.6415, 2.6415), "bottom-up de Restaurant/Dining en EE.UU. reapalancada con su D/E alta, sin la prima "
                                    "por un solo concepto"),
    "UBER": (0.80, (1.11, 1.11), "regresión de Uber; la de Transportation es de logística con activos y no describe a la "
                                 "plataforma; pérdidas fiscales reconocidas"),
    "PAGS": (1.12, None, "patrimonio de Financial Svcs. en la tabla global porque vende 100% en Brasil, sin la prima por "
                         "tamaño; el riesgo de Brasil va en la prima de mercado"),
    "AFYA": (None, (0.75, 0.75), "bottom-up de Education global, sin cambio"),
    "MSFT": (1.36, (0.6246, 0.70), "bottom-up de Software (System & Application) en EE.UU., porque vende 51% allí"),
    "NVO": (1.09, (0.57, 0.76), "bottom-up de Drugs (Pharmaceutical) en EE.UU., porque vende 56% en Norteamérica"),
    "INTU": (None, (1.18, 1.18), "bottom-up de Software (System & Application) en EE.UU., sin cambio"),
    "BSX": (None, (0.86, 0.86), "bottom-up de Healthcare Products en EE.UU., sin cambio"),
    "EPAM": (None, (2.65, 2.65), "bottom-up de Computer Services, sin cambio"),
    "PYPL": (None, (1.42, 1.42), "patrimonio de Financial Svcs. en EE.UU., sin cambio"),
    "GOOG": (None, (1.1537, 1.12), "por ingresos (Advertising y Software), sin cambio"),
    "ZTS": (None, (0.91, 0.91), "bottom-up de Drugs (Pharmaceutical), sin cambio"),
    "CELH": (None, None, "bottom-up de Beverage (Soft) en EE.UU."),
    "NVDA": (None, None, "bottom-up de Semiconductor en EE.UU., sin cambio"),
    "PLTR": (None, None, "bottom-up de Software (System & Application) en EE.UU., sin cambio"),
    "DUOL": (None, None, "bottom-up de Software (Internet) en la tabla global, sin cambio"),
    "SHAK": (1.25, (1.51, 1.51), "bottom-up de Restaurant/Dining en EE.UU. reapalancada con los arrendamientos, sin primas "
                                 "por tamaño, concepto ni márgenes finos"),
}


def es(x: float, nd: int = 2) -> str:
    return f"{x:,.{nd}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(x: float) -> str:
    return es(x * 100) + "%"


def nota(tk: str) -> str:
    import valores_hoja  # cifras leídas de la hoja de cálculo, no de copias intermedias

    v = valores_hoja.leer(tk)
    b0, s0, txt = ANTES[tk]
    beta = f"beta {es(v['beta'])} ({txt}" + (f"; antes {es(b0)})" if b0 is not None else ")")
    s2c = f"ventas/capital {es(v['s1'], 1)} en los años 1-5 y {es(v['s2'], 1)} en los 6-10"
    if s0:
        s2c += f" (antes {es(s0[0])})" if s0[0] == s0[1] else f" (antes {es(s0[0])} y {es(s0[1])})"
    tasa = "costo del patrimonio" if v["fin"] else "costo de capital"
    return (f"<strong>Actualización del 5 de octubre de 2026.</strong> Las tablas de auditoría y de supuestos de este informe "
            f"se actualizaron con la hoja de cálculo; las demás tablas y el texto conservan la fecha del informe. Tras la "
            f"revisión con criterio Damodaran (beta del negocio sin primas por riesgos diversificables, que ya están en las "
            f"historias; ventas/capital contrastado con el de la empresa, el marginal y el del sector), la hoja usa {beta}, "
            f"{tasa} inicial {pct(v['w0'])} y terminal {pct(v['wT'])} con la prima de mercado madura de Damodaran de octubre de "
            f"2026 (3,70%, calculada con la tasa del 30-sep; antes 4,09%), y {s2c}. DCF Base US${es(v['base'])} por acción y DCF "
            f"esperado US${es(v['ve'])} ('Escenarios e historias' H11 y H10), con un precio de referencia de "
            f"US${es(v['precio'])} ('Input sheet' D1). Las cifras vigentes están en la sección de historias Damodaran y en la "
            f"valoración.")


def con_nota_html(h: str, n: str) -> str:
    h = re.sub(re.escape(INI) + r".*?" + re.escape(FIN) + r"\n?", "", h, flags=re.S)
    i = h.index("<h2")
    return h[:i] + f"{INI}\n<blockquote>\n<p>{n}</p>\n</blockquote>\n{FIN}\n" + h[i:]


def con_nota_md(m: str, n: str) -> str:
    m = re.sub(re.escape(INI) + r".*?" + re.escape(FIN) + r"\n\n?", "", m, flags=re.S)
    i = re.search(r"^## ", m, flags=re.M).start()
    md = re.sub(r"</?strong>", "**", n)
    return m[:i] + f"{INI}\n> {md}\n{FIN}\n\n" + m[i:]


def main(argv: list[str]) -> int:
    for tk in [a for a in argv if not a.startswith("--")] or list(ANTES):
        n = nota(tk)
        p = Path(glob.glob(str(DATOS / "analisis" / f"{tk}-research-*.json"))[0])
        j = json.loads(p.read_text())
        j["html"] = con_nota_html(j["html"], n)
        j["updatedAt"] = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
        p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + "\n")
        md = _ROOT / "data" / str(j.get("sourceName") or "")
        if j.get("sourceName") and md.is_file():
            md.write_text(con_nota_md(md.read_text(), n))
        print(f"{tk}: nota en {p.name}" + (f" y {md.name}" if j.get("sourceName") and md.is_file() else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
