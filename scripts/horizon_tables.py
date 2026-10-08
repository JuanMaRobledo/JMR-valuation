#!/usr/bin/env python
"""Dos tablas de horizontes del valor por acción (prompts del 2-oct-2026).

Los prompts de research v5 y valoración v4 exigen, para cualquier empresa:
1. Valor por acción descontado al presente: cada múltiplo por separado, ponderado de
   múltiplos solos (pesos reescalados al 100% entre los múltiplos) y ponderado DCF + múltiplos.
2. Valor por acción a 3 años sin descontar (FY+3): lo mismo, con el DCF capitalizado a FY+3
   (DCF hoy × (1 + Ke)^3, antes de distribuciones) y los dividendos separados.
El DCF Base al presente va primero; múltiplos y ponderados son lecturas secundarias.

Todas las cifras se leen de la hoja (no se recalculan): 'Descuento de múltiplos' (VP por
método, pesos, filas 38-40, 47 y 50), las hojas de múltiplos (múltiplo aplicado F8/F19/F30 y
dividendos acumulados F:H de las filas 11/22/33) y 'Resumen de Valoración' (DCF capitalizado
C6:E6, categoría G3). La Disrupción sale del valor esperado guardado (solo existe en el DCF).

Uso:
    PYTHONPATH=.:scripts python scripts/horizon_tables.py --sheet-id ID --saved ../Modelo-JMR-datos/valoraciones/T-*.json
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

SHEET = "Descuento de múltiplos"
RES = "Resumen de Valoración"
TABS = {"EV/EBITDA": "EVEBITDA", "EV/FCFF": "EVFCFF", "P/E": "PE", "P/FCFE": "PFCFE", "P/OCF": "POCF"}
# escenario -> (primera fila de métodos en 'Descuento de múltiplos', fila del múltiplo aplicado,
#               fila de dividendos acumulados en las hojas de múltiplos, columna del resumen)
SCEN = {"base": (20, 19, 22, "D"), "conservador": (11, 8, 11, "C"), "optimista": (29, 30, 33, "E")}
ORDER = ("base", "conservador", "optimista")  # Base primero
RANGES = [f"'{SHEET}'!A1:K50", f"'{RES}'!A1:U20"] + [f"{t}!A1:J34" for t in TABS.values()]


def es(v, nd=2):
    return f"{v:,.{nd}f}".replace(",", "X").replace(".", ",").replace("X", ".") if isinstance(v, (int, float)) else "—"


def pct(v, nd=0):
    return es(v * 100, nd) + "%" if isinstance(v, (int, float)) else "—"


def xm(v, nd=1):
    return es(v, nd) + "×" if isinstance(v, (int, float)) else "—"


def grid_cell(grid: dict):
    def cell(sheet, addr):
        col, row = ord(addr[0]) - 65, int(addr[1:]) - 1
        g = grid.get(sheet, [])
        return g[row][col] if row < len(g) and col < len(g[row]) else None
    return cell


def read_grid(sh) -> dict:
    vr = sh.values_batch_get(RANGES, params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
    return {r.split("!")[0].strip("'"): v.get("values", []) for r, v in zip(RANGES, vr)}


def _num(v):
    return v if isinstance(v, (int, float)) and not isinstance(v, bool) else None


def build(cell, rec: dict) -> dict:
    """Cifras de las dos tablas, leídas de la hoja. Lanza ValueError si la hoja no cuadra con lo guardado."""
    d = {"ke": _num(cell(SHEET, "B5")), "criterio": cell(SHEET, "B6") or "Promedio 1-3 años",
         "tipo": cell(RES, "G3"), "peso_dcf": _num(cell(SHEET, "B38")), "peso_mult": _num(cell(SHEET, "B39")),
         "metodos": [], "hoy": {}, "fy3": {}, "div": {}}
    for i in range(5):
        r = SCEN["base"][0] + i
        name = cell(SHEET, f"A{r}")
        tab = TABS.get(name)
        m = {"nombre": name, "peso": _num(cell(SHEET, f"B{r}")), "peso_mult": _num(cell(SHEET, f"C{r}")),
             "multiplo": {}, "hoy": {}, "fy3": {}}
        for s, (first, mrow, _drow, _c) in SCEN.items():
            m["multiplo"][s] = _num(cell(tab, f"F{mrow}")) if tab else None
            m["hoy"][s] = _num(cell(SHEET, f"J{first + i}"))
            m["fy3"][s] = _num(cell(SHEET, f"F{first + i}"))
        d["metodos"].append(m)
    for s, (first, _mrow, drow, c) in SCEN.items():
        d["hoy"][s] = {"dcf": _num(cell(SHEET, f"{c}38")), "mult": _num(cell(SHEET, f"{c}39")),
                       "pond": _num(cell(SHEET, f"{c}40"))}
        d["fy3"][s] = {"dcf": _num(cell(RES, f"{c}6")), "mult": _num(cell(SHEET, f"{c}47")),
                       "pond": _num(cell(SHEET, f"{c}50"))}
        d["div"][s] = _num(cell("EVEBITDA", f"H{drow}")) or 0.0
    ve = rec.get("valorEsperado") or {}
    dis = next((h for h in ve.get("historias", []) if str(h.get("id", "")).upper() == "C" or "disrup" in str(h.get("nombre", "")).lower()), None)
    d["disrupcion"] = dis.get("valor") if dis else None
    d["esperado"] = ve.get("valor")
    # control de cierre: la hoja y la valoración guardada (app) deben coincidir
    errs = []
    for s in ORDER:
        for key, saved in (("hoy", (rec.get("valorPresentePonderado") or {}).get(s)),
                           ("fy3", (rec.get("objetivoPonderado") or {}).get(s))):
            v = d[key][s]["pond"]
            if isinstance(saved, (int, float)) and isinstance(v, (int, float)) and abs(v - saved) > 0.005:
                errs.append(f"{s} {key}: hoja {v:.4f} != guardada {saved:.4f}")
    if errs:
        raise ValueError("La hoja no coincide con la valoración guardada: " + "; ".join(errs))
    return d


def markdown(d: dict, cur: str = "US$", fecha: str | None = None, heading: str = "###") -> str:
    money = lambda v: f"{cur}{es(v)}" if isinstance(v, (int, float)) else "pendiente"  # noqa: E731
    fecha = fecha or os.environ.get("JMR_FECHA") or ""
    tri = lambda f: " | ".join(money(f(s)) for s in ORDER)  # noqa: E731
    mult_txt = lambda m: " / ".join(xm(m["multiplo"][s]) for s in ORDER)  # noqa: E731
    act = [m for m in d["metodos"] if (m["peso"] or 0) > 0]
    off = [m["nombre"] for m in d["metodos"] if not (m["peso"] or 0) > 0]
    crit = ("solo el VP a 3 años" if d["criterio"] == "Solo 3 años"
            else "el promedio simple de los VP a 1, 2 y 3 años")
    has_div = any(d["div"][s] > 1e-9 for s in ORDER)
    L: list[str] = []
    w = L.append
    w(f"{heading} Valor por acción en dos horizontes")
    w("")
    w(f"Moneda: {cur} por acción. Fecha de valoración: {fecha}. Escenarios en orden Base, Conservador y Optimista. "
      f"Categoría de empresa «{d['tipo']}»: DCF {pct(d['peso_dcf'])} y múltiplos {pct(d['peso_mult'])} "
      f"({', '.join(m['nombre'] + ' ' + pct(m['peso']) for m in act)}). "
      + (f"Sin peso (no aplica): {', '.join(off)}. " if off else "")
      + f"Costo del patrimonio (Ke) {pct(d['ke'], 2)}. Los múltiplos tienen solo tres escenarios auxiliares; la Disrupción "
      f"existe solo en el DCF ({money(d['disrupcion'])}) y no se inventa para ellos.")
    w("")
    w(f"**Valor intrínseco principal: DCF Base al presente, {money(d['hoy']['base']['dcf'])} por acción.** Complemento: "
      f"DCF esperado por probabilidades {money(d['esperado'])}. Múltiplos y ponderados son lecturas secundarias.")
    w("")
    w(f"**Tabla 1 · Valor por acción descontado al presente ({fecha}).** Cada método usa {crit} (criterio vigente "
      "de la hoja); cada dividendo se descuenta en su año de pago.")
    w("")
    w("| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |")
    w("|---|---|---:|---:|---:|---:|---:|")
    w(f"| DCF de las historias al presente | — | {pct(d['peso_dcf'])} | — | {tri(lambda s: d['hoy'][s]['dcf'])} |")
    for m in d["metodos"]:
        w(f"| {m['nombre']} | {mult_txt(m)} | {pct(m['peso'])} | {pct(m['peso_mult'])} | {tri(lambda s: m['hoy'][s])} |")
    w(f"| **Ponderado de múltiplos solos al presente** | — | {pct(d['peso_mult'])} | 100% | "
      f"{tri(lambda s: d['hoy'][s]['mult'])} |")
    w(f"| **Ponderado DCF + múltiplos al presente** | — | 100% | — | {tri(lambda s: d['hoy'][s]['pond'])} |")
    w("")
    w("**Tabla 2 · Valor por acción a 3 años sin descontar (FY+3).** Precio al cierre de FY+3 "
      + ("más los dividendos por acción de FY+1 a FY+3." if has_div else "(la hoja no proyecta dividendos: precio "
         "objetivo exdividendo = total)."))
    w("")
    w("| Método | Múltiplo aplicado (× Base / Cons. / Opt.) | Peso original | Peso entre múltiplos | Base | Conservador | Optimista |")
    w("|---|---|---:|---:|---:|---:|---:|")
    w(f"| DCF capitalizado a FY+3 antes de distribuciones | — | {pct(d['peso_dcf'])} | — | "
      f"{tri(lambda s: d['fy3'][s]['dcf'])} |")
    for m in d["metodos"]:
        w(f"| {m['nombre']}{' (total con dividendos)' if has_div else ''} | {mult_txt(m)} | {pct(m['peso'])} | "
          f"{pct(m['peso_mult'])} | {tri(lambda s: m['fy3'][s])} |")
    w(f"| **Ponderado de múltiplos solos a 3 años sin descontar**{' (total)' if has_div else ''} | — | "
      f"{pct(d['peso_mult'])} | 100% | {tri(lambda s: d['fy3'][s]['mult'])} |")
    if has_div:
        w(f"| Dividendos acumulados FY+1 a FY+3 (incluidos en cada múltiplo) | — | — | — | {tri(lambda s: d['div'][s])} |")
        w(f"| Ponderado de múltiplos solos: precio objetivo exdividendo | — | — | 100% | "
          f"{tri(lambda s: d['fy3'][s]['mult'] - d['div'][s] if isinstance(d['fy3'][s]['mult'], (int, float)) else None)} |")
    w(f"| **Ponderado DCF + múltiplos a 3 años sin descontar** | — | 100% | — | {tri(lambda s: d['fy3'][s]['pond'])} |")
    w("")
    w("Fórmulas. Peso entre múltiplos = peso del método ÷ suma de los pesos de los múltiplos aplicables; ponderado de "
      "múltiplos solos = suma(peso entre múltiplos × valor del método); ponderado DCF + múltiplos = peso DCF × DCF + "
      "suma(peso original × valor del método), con pesos que suman 100%. Estos pesos son de métodos y no son las "
      "probabilidades de las cuatro historias. Al presente: VP_n = Precio FY+n ÷ (1 + Ke)^n + suma(Dividendo FY+t ÷ "
      "(1 + Ke)^t), t = 1..n. En FY+3 el DCF es el DCF de las historias de hoy × (1 + Ke)^3: riqueza capitalizada antes de "
      "distribuciones, no un nuevo DCF ni un precio exdividendo; no se mezcla DCF presente con múltiplos futuros. "
      "Mostrar ambas lecturas no cambia las anclas de los múltiplos ni la política de MOS (sobre el DCF esperado).")
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sheet-id", required=True)
    ap.add_argument("--saved", required=True)
    ap.add_argument("--json", action="store_true", help="Imprime las cifras en JSON en vez del markdown")
    a = ap.parse_args()
    from jmr_valuation.io.sheets_auth import get_gspread_client
    rec = json.loads(Path(a.saved).read_text())
    d = build(grid_cell(read_grid(get_gspread_client().open_by_key(a.sheet_id))), rec)
    print(json.dumps(d, ensure_ascii=False, indent=1) if a.json else markdown(d))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
