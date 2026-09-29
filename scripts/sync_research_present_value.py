"""Lleva los multiplos a valor presente en 1, 2 y 3 años (discount_multiples.py) a los
analisis fundamentales guardados (Modelo-JMR-datos/analisis/*.json).

Cada analisis tiene, dentro del bloque JMR-CURRENT-VALUATION, la tabla "DCF y múltiplos
descontados al presente" armada con el puente anterior (solo 3 años, dividendos
descontados aparte). Este script:

1. Rehace esa tabla y su parrafo con la valoracion vinculada ya actualizada
   (linkedValuation.descuentoMultiples v2): DCF hoy, cada multiplo consolidado hoy,
   multiplos consolidados y valor intrinseco ponderado.
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
        if dm.get("version") != 2 or H3 not in (d.get("html") or ""):
            print(f"{f.name}: se omite (sin valoración v2 vinculada o sin la tabla)")
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
        s = h.index(H3)
        e = h.index("</p>", h.index("</table>", s)) + len("</p>")
        old_rows = _old_rows(h[s:e])
        if (old_rec.get("descuentoMultiples") or {}).get("version") == 2:
            old_rows = {m["nombre"]: ["", *(es_money(m[k]["consolidado"]) for k in SCEN)] for m in old_rec["descuentoMultiples"]["metodos"]}
        table = mapping(old_rec, lv, old_rows)
        if args.incluir_fy3:
            table.update(fy3_mapping(old_rec, new_rec))
        h = h[:s] + new_block(lv) + h[e:]
        h, n1 = substitute(h, table)
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
