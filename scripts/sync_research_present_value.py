"""Lleva los multiplos a valor presente en 1, 2 y 3 años (discount_multiples.py) a los
analisis fundamentales guardados (Modelo-JMR-datos/analisis/*.json).

Cada analisis tiene, dentro del bloque JMR-CURRENT-VALUATION, la tabla "DCF y múltiplos
descontados al presente" armada con el puente anterior (solo 3 años, dividendos
descontados aparte). Este script:

1. Rehace esa tabla y su parrafo con la valoracion vinculada ya actualizada
   (linkedValuation.descuentoMultiples v2): DCF hoy, cada multiplo consolidado hoy,
   multiplos consolidados y ponderado (lecturas secundarias; el valor intrinseco es el DCF).
2. En el resto del texto (html y valuationHtml) cambia cada cifra "US$x" que era un
   valor del puente anterior (ponderado hoy, multiplos hoy, cada metodo descontado y el
   precio con MOS de hoy) por la cifra nueva equivalente. Las demas cifras no se tocan.

Uso:
    python scripts/sync_research_present_value.py ../Modelo-JMR-datos [--dry-run]
    (compara contra la version de valoraciones/ en HEAD~N con --old-rev, por defecto HEAD)
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

SCEN = ("conservador", "base", "optimista")
H3 = "<h3>DCF y múltiplos descontados al presente</h3>"
START = "<!-- JMR-CURRENT-VALUATION-START -->"
END = "<!-- JMR-CURRENT-VALUATION-END -->"
LECTURA = "<p><strong>Lectura de la valoración vigente:</strong>"


def es_money(v: float) -> str:
    s = f"{v:,.2f}"  # 1,234.56
    return "US$" + s.replace(",", "X").replace(".", ",").replace("X", ".")


def _old_rows(block: str) -> dict[str, list[str]]:
    """Filas de la tabla vieja: metodo -> [peso, cons, base, opt] (texto)."""
    rows = {}
    for m in re.finditer(r'<th scope="row">([^<]+)</th>((?:<td>[^<]*</td>)+)', block):
        rows[m.group(1).strip()] = re.findall(r"<td>([^<]*)</td>", m.group(2))
    return rows


def new_block(lv: dict) -> str:
    dm = lv["descuentoMultiples"]
    pct = lambda w: f"{round(w * 100):.0f}%" if isinstance(w, (int, float)) else "—"  # noqa: E731
    tr = lambda label, w, vals, cls="": (  # noqa: E731
        f'<tr class="{cls}"><th scope="row">{label}</th><td>{pct(w)}</td>'
        + "".join(f"<td>{es_money(v) if isinstance(v, (int, float)) else '—'}</td>" for v in vals) + "</tr>")
    body = tr("DCF Damodaran", dm.get("pesoDcf"), [dm["dcfHoy"][k] for k in SCEN])
    for m in dm["metodos"]:
        body += tr(m["nombre"], m.get("peso"), [m[k]["consolidado"] for k in SCEN])
    body += tr("Múltiplos consolidados", dm.get("pesoMultiplos"), [dm["multiplesHoy"][k] for k in SCEN])
    body += tr("Valor intrínseco ponderado hoy", 1.0, [lv["valorPresentePonderado"][k] for k in SCEN], "total")
    ke = f"{dm['costoPatrimonio'] * 100:.2f}%".replace(".", ",")
    crit = "el promedio simple de los tres horizontes" if dm.get("criterio", "").startswith("Promedio") else "el valor a 3 años"
    return (f'{H3}\n<div style="overflow-x:auto"><table><thead><tr><th>Método</th><th>Peso</th><th>Conservador</th>'
            f"<th>Base</th><th>Optimista</th></tr></thead><tbody>{body}</tbody></table></div>\n"
            f"<p>El DCF ya es valor presente. Cada múltiplo da un precio al cierre de FY+1, FY+2 y FY+3; a cada uno se le "
            f"suman los dividendos por acción acumulados hasta ese año y el total se trae a hoy con un costo de patrimonio "
            f"de {ke}: VP = (precio FY+n + dividendos) ÷ (1 + Ke)^n. Cada método se consolida con {crit}; los múltiplos "
            f"consolidados son su promedio con los pesos de la categoría, y el valor intrínseco ponderado es DCF × peso DCF "
            f"+ múltiplos × peso de los múltiplos. Los objetivos FY+3 no se suman de nuevo a esa cifra.</p>")


def current_block(ticker: str, lv: dict, rec: dict) -> str:
    """Bloque «Valoración vigente» con criterio Damodaran: el DCF es el valor intrínseco y va primero;
    múltiplos y ponderado van aparte como lecturas secundarias."""
    dm = lv["descuentoMultiples"]
    money = lambda v: es_money(v) if isinstance(v, (int, float)) else "—"  # noqa: E731
    pct = lambda w: f"{round(w * 100):.0f}%" if isinstance(w, (int, float)) else "—"  # noqa: E731

    def tr(label, vals, cls="", w=None):
        wcell = f"<td>{pct(w)}</td>" if w is not None or cls == "w" else ""
        return (f'<tr class="{cls}"><th scope="row">{label}</th>{wcell}'
                + "".join(f"<td>{money(v)}</td>" for v in vals) + "</tr>")
    head = lambda cols: "<thead><tr>" + "".join(f"<th>{c}</th>" for c in cols) + "</tr></thead>"  # noqa: E731
    dcf_fy3 = next(({k: m.get(k) for k in SCEN} for m in lv.get("metodos") or [] if "DCF" in (m.get("nombre") or "")), None)
    mos = rec.get("mos")
    dcf = dm["dcfHoy"]
    rows = tr("Valor intrínseco hoy · DCF", [dcf[k] for k in SCEN], "total")
    if dcf_fy3:
        rows += tr("DCF llevado a FY+3 (× (1 + Ke)³)", [dcf_fy3[k] for k in SCEN])
    if isinstance(mos, (int, float)):
        rows += tr(f"Precio con MOS sobre el DCF ({round(mos * 100)}%)", [dcf[k] * (1 - mos) for k in SCEN])
    t1 = f'<div style="overflow-x:auto"><table>{head(["", "Conservador", "Base", "Optimista"])}<tbody>{rows}</tbody></table></div>'
    fy3 = {m["nombre"]: m for m in lv.get("metodos") or []}
    rows2 = ""
    for m in dm["metodos"]:
        f = fy3.get(m["nombre"], {})
        rows2 += (f'<tr><th scope="row">{m["nombre"]}</th><td>{pct(m.get("peso"))}</td>'
                  + "".join(f"<td>{money(m[k]['consolidado'])}</td>" for k in SCEN)
                  + "".join(f"<td>{money(f.get(k))}</td>" for k in SCEN) + "</tr>")
    op, vp = lv.get("objetivoPonderado") or {}, lv.get("valorPresentePonderado") or {}
    rows2 += (f'<tr><th scope="row">Múltiplos consolidados</th><td>{pct(dm.get("pesoMultiplos"))}</td>'
              + "".join(f"<td>{money(dm['multiplesHoy'][k])}</td>" for k in SCEN) + "<td>—</td>" * 3 + "</tr>")
    rows2 += (f'<tr class="total"><th scope="row">Ponderado DCF + múltiplos</th><td>100%</td>'
              + "".join(f"<td>{money(vp.get(k))}</td>" for k in SCEN) + "".join(f"<td>{money(op.get(k))}</td>" for k in SCEN) + "</tr>")
    t2 = ('<div style="overflow-x:auto"><table><thead><tr><th rowspan="2">Método</th><th rowspan="2">Peso</th>'
          '<th colspan="3">Hoy (valor presente)</th><th colspan="3">Al cierre FY+3</th></tr><tr><th>Cons.</th><th>Base</th>'
          f'<th>Opt.</th><th>Cons.</th><th>Base</th><th>Opt.</th></tr></thead><tbody>{rows2}</tbody></table></div>')
    ke = f"{dm['costoPatrimonio'] * 100:.2f}%".replace(".", ",")
    saved = (rec.get("savedAt") or lv.get("fecha") or "")[:10]
    link = f"https://github.com/JuanMaRobledo/Modelo-JMR-datos/blob/main/{lv.get('sourcePath', '')}"
    return (f'{START}\n<section class="jmr-valuation-current" style="margin:1.5rem 0;padding:1.25rem;border:1px solid #dfd2b6;'
            f'border-radius:14px;background:#fffaf0;color:#24332d">\n<h2>Valoración vigente · {ticker}</h2>\n'
            f'<p>Resultados de la valoración guardada el {saved}. Los importes son por acción. <a href="{link}">Consultar datos y '
            'supuestos</a>.</p>\n<h3>Valor intrínseco: DCF</h3>\n' + t1 +
            '\n<p>Con criterio Damodaran, el valor intrínseco es el DCF: lo que vale la acción según sus flujos de caja, '
            'crecimiento, reinversión y riesgo. El DCF ya está a valor presente; llevado a FY+3 se capitaliza con el costo del '
            f'patrimonio ({ke}).</p>\n<h3>Lecturas secundarias: múltiplos y ponderado</h3>\n' + t2 +
            '\n<p>Los múltiplos son precio relativo: lo que pagaría el mercado por empresas parecidas. Cada uno da un precio al '
            'cierre de FY+1, FY+2 y FY+3, más los dividendos acumulados, traído a hoy con el costo del patrimonio; se consolidan '
            'con los pesos del tipo de empresa. El ponderado mezcla el DCF con los múltiplos y es opcional: sirve como contraste, '
            'no reemplaza al DCF.</p>\n<p><strong>Contexto del informe:</strong> el análisis fundamental que sigue conserva sus '
            'fuentes, fecha y cálculos originales. Las tablas anteriores contienen las cifras vigentes; las referencias fechadas a '
            'versiones anteriores del modelo en el estudio de negocio son antecedentes históricos.</p>\n</section>\n' + END)


def lectura(lv: dict) -> str:
    dm = lv["descuentoMultiples"]
    d, mh, vp = dm["dcfHoy"], dm["multiplesHoy"], lv.get("valorPresentePonderado") or {}
    return (f"{LECTURA} el valor intrínseco Base (DCF) hoy es {es_money(d['base'])}, con un rango de {es_money(d['conservador'])} "
            f"(Conservador) a {es_money(d['optimista'])} (Optimista). Los múltiplos ({es_money(mh['base'])} hoy) y el ponderado "
            f"({es_money(vp.get('base'))}) son lecturas secundarias. La comparación con el precio va al final de la sección "
            "«Valor con criterio Damodaran».</p>")


def replace_block(h: str, ticker: str, lv: dict, rec: dict) -> str:
    s, e = h.index(START), h.index(END) + len(END)
    h = h[:s] + current_block(ticker, lv, rec) + h[e:]
    i = h.find(LECTURA)
    if i != -1:
        j = h.index("</p>", i) + len("</p>")
        h = h[:i] + lectura(lv) + h[j:]
    return h


def mapping(old_rec: dict, new_lv: dict, old_rows: dict[str, list[str]]) -> dict[str, str]:
    """Cifra vieja (texto US$) -> cifra nueva, solo para valores del puente anterior."""
    dm = new_lv["descuentoMultiples"]
    out: dict[str, str] = {}

    def add(old, new):
        if isinstance(old, (int, float)) and isinstance(new, (int, float)):
            out[es_money(old)] = es_money(new)

    for k in SCEN:
        add(old_rec["valorPresentePonderado"][k], new_lv["valorPresentePonderado"][k])
        add(old_rec["descuentoMultiples"]["multiplesHoy"][k], dm["multiplesHoy"][k])
        add((old_rec.get("precioMOSHoy") or {}).get(k), (new_lv.get("precioMOSHoy") or {}).get(k))
    for m in dm["metodos"]:
        old = old_rows.get(m["nombre"])
        if old and len(old) >= 4:
            for i, k in enumerate(SCEN):
                if old[i + 1].startswith("US$"):
                    out[old[i + 1]] = es_money(m[k]["consolidado"])
    # un valor que no cambio (ej. el DCF) no debe entrar en el mapa
    return {a: b for a, b in out.items() if a != b}


def fy3_mapping(old_rec: dict, new_rec: dict) -> dict[str, str]:
    """Cifras FY+3: precio por método y escenario, ponderado, zonas y precio con MOS."""
    out: dict[str, str] = {}

    def add(o, n):
        if isinstance(o, (int, float)) and isinstance(n, (int, float)) and es_money(o) != es_money(n):
            out[es_money(o)] = es_money(n)

    nm = {m["nombre"]: m for m in new_rec.get("metodos") or []}
    for m in old_rec.get("metodos") or []:
        for k in SCEN:
            add(m.get(k), (nm.get(m["nombre"]) or {}).get(k))
    for k in SCEN:
        add(old_rec["objetivoPonderado"][k], new_rec["objetivoPonderado"][k])
    for z in ("value", "deepValue", "historica", "conMOS"):
        for b in ("max", "min"):
            add(((old_rec.get("zonas") or {}).get(z) or {}).get(b), ((new_rec.get("zonas") or {}).get(z) or {}).get(b))
    add(old_rec.get("precioMOS"), new_rec.get("precioMOS"))
    add(old_rec.get("precioMOSMax"), new_rec.get("precioMOSMax"))
    return out


def _pct_es(v: float) -> str:
    return f"{v * 100:.1f}".replace(".", ",")


def derived_percentages(text: str, old_rec: dict, new_rec: dict) -> tuple[str, int]:
    """Porcentajes que dependen de las cifras cambiadas: CAGR citado y diferencia valor hoy vs precio."""
    n = 0
    for k in SCEN:
        o, w = (old_rec.get("cagr") or {}).get(k), (new_rec.get("cagr") or {}).get(k)
        if isinstance(o, (int, float)) and isinstance(w, (int, float)) and _pct_es(o) != _pct_es(w):
            pat = re.compile(r"(CAGR[^.%<]{0,80}?)" + re.escape(_pct_es(o)) + "%")
            text, c = pat.subn(lambda m: m.group(1) + _pct_es(w) + "%", text)
            n += c

    def diff(m):
        nonlocal n
        val = float(m.group(1).replace(".", "").replace(",", "."))
        ref = float(m.group(2).replace(".", "").replace(",", "."))
        n += 1
        return m.group(0)[: m.start(3) - m.start(0)] + _pct_es(val / ref - 1) + "%"
    text = re.sub(r"valor presente ponderado de US\$([\d.,]+) por acción frente a US\$([\d.,]+) de referencia, una diferencia de (−?-?\d+,\d)%",
                  diff, text)
    return text, n


def substitute(text: str, table: dict[str, str]) -> tuple[str, int]:
    if not table:
        return text, 0
    pat = re.compile("|".join(re.escape(k) for k in sorted(table, key=len, reverse=True)) + r"(?![\d,])")
    n = 0

    def rep(m):
        nonlocal n
        n += 1
        return table[m.group(0)]
    return pat.sub(rep, text), n


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("datos")
    ap.add_argument("--old-rev", default="HEAD", help="revision de git con las valoraciones anteriores")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--tickers", nargs="*", help="solo estos tickers")
    ap.add_argument("--incluir-fy3", action="store_true",
                    help="también reemplaza las cifras FY+3 (precio por método y ponderado), p. ej. tras cambiar múltiplos")
    args = ap.parse_args()
    root = Path(args.datos)
    for f in sorted((root / "analisis").glob("*.json")):
        d = json.loads(f.read_text())
        lv = d.get("linkedValuation") or {}
        dm = lv.get("descuentoMultiples") or {}
        if dm.get("version") != 2 or START not in (d.get("html") or ""):
            print(f"{f.name}: se omite (sin valoración v2 vinculada o sin el bloque de valoración vigente)")
            continue
        if args.tickers and d.get("ticker") not in args.tickers:
            continue
        old_rec = json.loads(subprocess.check_output(["git", "-C", str(root), "show", f"{args.old_rev}:{lv['sourcePath']}"]))
        new_rec = json.loads((root / lv["sourcePath"]).read_text())
        for k in ("metodos", "objetivoPonderado", "zonas", "cagr", "precioMOS", "precioMOSMax", "valorPresentePonderado",
                  "descuentoMultiples", "precioMOSHoy"):
            if k in new_rec:
                lv[k] = new_rec[k]
        if (old_rec.get("descuentoMultiples") or {}).get("version") == 2 and not args.incluir_fy3:
            print(f"{f.name}: la revisión {args.old_rev} ya tiene v2; se omite")
            continue
        h = d["html"]
        old_rows = {}
        if H3 in h:
            s = h.index(H3)
            e = h.index("</p>", h.index("</table>", s)) + len("</p>")
            old_rows = _old_rows(h[s:e])
        if (old_rec.get("descuentoMultiples") or {}).get("version") == 2:
            old_rows = {m["nombre"]: ["", *(es_money(m[k]["consolidado"]) for k in SCEN)] for m in old_rec["descuentoMultiples"]["metodos"]}
        table = mapping(old_rec, lv, old_rows)
        if args.incluir_fy3:
            table.update(fy3_mapping(old_rec, new_rec))
        # el texto fuera del bloque se actualiza por sustitución; el bloque se rehace entero (DCF primero)
        h, n1 = substitute(h, table)
        h = replace_block(h, d.get("ticker") or "", lv, new_rec)
        if args.incluir_fy3:
            h, n3 = derived_percentages(h, old_rec, new_rec)
            n1 += n3
        vh, n2 = substitute(d.get("valuationHtml") or "", table)
        print(f"{d.get('ticker', f.name):5s} tabla rehecha, {n1 + n2} cifras del puente anterior reemplazadas en el texto")
        if not args.dry_run:
            d["html"] = h
            if d.get("valuationHtml"):
                d["valuationHtml"] = vh
            f.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
