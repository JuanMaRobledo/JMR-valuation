"""Tabla «Escenarios e historias» (Base, Conservadora, Disrupción y Optimista) de la sección 10 del análisis fundamental (prompt de research v5).

La tabla cualitativa de escenarios de la sección 10 tenía tres columnas, Conservador / Base / Optimista: los casos
técnicos antiguos de la hoja. Con el contrato del 30-sep-2026 los escenarios activos son las cuatro historias A-D,
así que la tabla pasa a tener una columna por historia con las filas del prompt v5 (crecimiento y participación,
poder de precios y retención, margen, reinversión y retorno, moat y sustitución) más la tesis y la probabilidad.

- Las filas cuantitativas salen de las historias (reference/damodaran/<T>.json y <T>_resultado.json).
- Las cualitativas (precios, moat) conservan el texto del analista de la tabla anterior para A (antes Base),
  B (antes Conservador) y D (antes Optimista); la columna C se escribe con la tesis de disrupción de la ficha.
- La columna de evidencia se conserva.

Reemplaza «Escenarios cualitativos de largo plazo» (o la tabla de una ejecución anterior, entre los marcadores
JMR-ESCENARIOS) en Modelo-JMR-datos/analisis/<T>-research-*.json. Sin tabla previa (DUOL), la agrega al final
de la sección de riesgos. No calcula valoración: remite a la sección 12.

Uso: python scripts/insert_scenarios_table.py ../Modelo-JMR-datos ADBE CMG ...
"""
from __future__ import annotations

import datetime as dt
import glob
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from damodaran_stories import REF, es, pct, prob_frase  # noqa: E402

START, END = "<!-- JMR-ESCENARIOS-START -->", "<!-- JMR-ESCENARIOS-END -->"
OLD_H3 = "<h3>Escenarios cualitativos de largo plazo</h3>"
FILAS = ["Crecimiento y participación", "Poder de precios y retención", "Margen bruto y operativo",
         "Reinversión y retorno sobre capital", "Moat y sustitución"]
COL_ANTIGUA = {"A": 2, "B": 1, "D": 3}  # columnas de la tabla anterior: 1 Conservador, 2 Base, 3 Optimista


def old_table(h: str) -> dict[str, list[str]]:
    i = h.find(OLD_H3)
    if i < 0:
        return {}
    t = h[h.find("<table", i):h.find("</table>", i)]
    rows = {}
    for tr in re.findall(r"<tr>(.*?)</tr>", t, re.S):
        cells = [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]
        if len(cells) >= 5 and cells[0] != "Variable":
            rows[html.unescape(cells[0])] = [html.unescape(c) for c in cells]
    return rows


def corta(t: str, n: int = 200) -> str:
    t = t.split("; ")[0]
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "…"


def build(tk: str, h: str) -> str:
    spec = json.loads((REF / f"{tk}.json").read_text())
    res = json.loads((REF / f"{tk}_resultado.json").read_text())
    res["spec"] = spec
    hs = {x["id"]: x for x in res["historias"]}
    fin = res.get("financiero")
    old = old_table(h)
    ve = res["valor_esperado_beta_hoja"]
    vb = next(h for h in res["historias"] if h["id"] == "A")["valor_beta_hoja"]

    def cell(fila, letra, generado):
        o = old.get(fila)
        if o and letra in COL_ANTIGUA and o[COL_ANTIGUA[letra]] and o[COL_ANTIGUA[letra]] not in ("—", "-"):
            return o[COL_ANTIGUA[letra]]
        return generado

    def evid(fila, defecto):
        o = old.get(fila)
        return o[4] if o and len(o) > 4 and o[4] else defecto

    filas = []
    filas.append(["Tesis"] + [hs[x].get("descripcion") or hs[x]["nombre"].split(" · ", 1)[-1] for x in "ABCD"] +
                 ["Sección 12, «Las cuatro tesis»"])
    filas.append(["Probabilidad del analista"] + [pct(hs[x]["prob"], 0) for x in "ABCD"] +
                 ["Indicadores de la sección 12 (se mueven 5-10 pp por trimestre)"])
    for fila in FILAS:
        row = [fila]
        for x in "ABCD":
            s = hs[x]
            if fila == "Crecimiento y participación":
                v = (f"{'Beneficio' if fin else 'Ingresos'} +{es(s['cagr'] * 100, 1)}% anual en los años 1–5 "
                     f"(año 1 {pct(s['anios'][0])}, año 5 {pct(s['anios'][4])})").replace("+-", "−")
            elif fila == "Poder de precios y retención":
                desc = s.get("descripcion") or s["nombre"].split(" · ", 1)[-1]
                v = (f"Pierde poder de precio y retención: {desc[:1].lower() + desc[1:]}" if x == "C"
                     else cell(fila, x, corta(prob_frase(spec, x))))
            elif fila == "Margen bruto y operativo":
                v = f"{'ROE' if fin else 'Margen operativo'} objetivo {pct(s['margen'], 1)}"
            elif fila == "Reinversión y retorno sobre capital":
                if fin:
                    v = f"Reinversión = utilidad × crecimiento / ROE; crecimiento terminal {pct(s['terminal_growth'], 1)}"
                else:
                    roic = ("= costo de capital" if s.get("roic_terminal") == "costo_capital" or not s.get("roic_terminal_usado")
                            else pct(s["roic_terminal_usado"], 1))
                    v = (f"Ventas/capital {es(s.get('s2c') or res['s2c'], 1)}; ROIC después del año 10 {roic}; "
                         f"crecimiento terminal {pct(s['terminal_growth'], 1)}")
            else:  # Moat y sustitución
                v = cell(fila, x, {"A": "La ventaja se mantiene", "B": "La ventaja se erosiona de forma gradual",
                                   "C": "La ventaja se pierde", "D": "La ventaja se fortalece"}[x])
                if x == "C" and not fin:
                    v = "Deterioro estructural: la ventaja se pierde y el ROIC terminal baja al costo de capital"
            row.append(v)
        row.append(evid(fila, {"Crecimiento y participación": "Crecimiento trimestral frente a la guía",
                               "Poder de precios y retención": "Precio realizado y retención",
                               "Margen bruto y operativo": "Margen trimestral",
                               "Reinversión y retorno sobre capital": "Capex, adquisiciones y retorno incremental",
                               "Moat y sustitución": "Participación de mercado y sustitutos"}[fila]))
        filas.append(row)
    heads = ["Variable", "Base", "Conservadora", "Disrupción · Deterioro de los fundamentales", "Optimista", "Evidencia que movería de escenario"]
    t = ("<table>\n<thead>\n<tr>" + "".join(f"<th>{c}</th>" for c in heads) + "</tr>\n</thead>\n<tbody>" +
         "".join("<tr>" + "".join(f"<td>{html.escape(str(c))}</td>" for c in r) + "</tr>\n" for r in filas) + "</tbody></table>")
    nota_old = (" Las celdas de precios y moat de Base, Conservadora y Optimista conservan el criterio del analista de la tabla anterior (Base, "
                "Conservador y Optimista de la hoja)." if old else "")
    return (f"{START}\n<h3>Escenarios e historias: Base, Conservadora, Disrupción y Optimista</h3>\n<p>Los escenarios son "
            "las cuatro historias del análisis: Base (la trayectoria central), Conservadora (erosión gradual), Disrupción · "
            "Deterioro de los fundamentales (deterioro estructural; no presupone quiebra) y Optimista. Cada una se cuantifica "
            "en la sección 12 como un DCF completo, año por año. El DCF Base es el valor intrínseco principal "
            f"(US${es(vb)} por acción); el promedio ponderado por probabilidad es el DCF esperado, un complemento "
            f"(US${es(ve)} por acción). Los casos Conservador/Base/Optimista de la hoja quedan como calibración técnica, "
            f"no como escenarios.{nota_old}</p>\n{t}\n{END}")


def insert(h: str, block: str) -> tuple[str, str]:
    if START in h:
        return re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, h, flags=re.S), "actualizada"
    i = h.find(OLD_H3)
    if i >= 0:
        j = h.find("</table>", i) + len("</table>")
        return h[:i] + block + h[j:], "reemplazada"
    m = re.search(r"<h2[^>]*>\d+\. Valor con criterio Damodaran</h2>", h)
    if not m:
        return h, "sin lugar"
    return h[:m.start()] + block + "\n" + h[m.start():], "agregada antes de la sección 12"


def main(argv: list[str]) -> int:
    datos, tickers = Path(argv[0]), argv[1:]
    for t in tickers:
        f = glob.glob(str(datos / "analisis" / f"{t}-research-*.json"))[0]
        rec = json.loads(Path(f).read_text())
        rec["html"], estado = insert(rec["html"], build(t, rec["html"]))
        rec["updatedAt"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
        Path(f).write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n")
        print(f"{t}: {estado}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
