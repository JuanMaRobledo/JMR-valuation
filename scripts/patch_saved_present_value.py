"""Actualiza las valoraciones guardadas del visor (Modelo-JMR-datos/valoraciones)
con los multiplos a valor presente en 1, 2 y 3 años (discount_multiples.py).

A diferencia de regen_saved_valuations.py, NO reemplaza el registro entero:
exporta la hoja, la carga en docs/visor.html con Playwright, intercepta el
guardado y copia SOLO lo que depende del descuento de multiplos:

  descuentoMultiples, valorPresentePonderado y precioMOSHoy; y rehace los
  resumenes compactos 'Resumen de Valoración' y 'Descuento de múltiplos' de
  hojas.valoracion (mismo formato rv-wrap que ya tenian).

Todo lo demas (fecha, precios, analisis fundamental, Cualitativo editado,
notas de auditoria, hojas propias) queda como estaba. Si el precio FY+3 de
algun metodo difiere del guardado, la hoja cambio despues de guardar: se
avisa y el registro no se toca (hay que regenerarlo completo a proposito).

Uso:
    python scripts/patch_saved_present_value.py ../Modelo-JMR-datos/valoraciones/*.json
    (SHEETJS_PATH=<copia local de xlsx.full.min.js 0.18.5>, CHROMIUM_PATH opcional)
"""
from __future__ import annotations

import json
import os
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from playwright.sync_api import sync_playwright  # noqa: E402

from regen_saved_valuations import export_xlsx, regen, serve  # noqa: E402

FIELDS = ("descuentoMultiples", "valorPresentePonderado", "precioMOSHoy")
SCEN = ("conservador", "base", "optimista")


def _money(v, cur: str) -> str:
    return f"{cur} {v:,.2f}" if isinstance(v, (int, float)) else "—"


def _pct(v) -> str:
    return f"{v * 100:.0f}%" if isinstance(v, (int, float)) else "—"


def _table(title: str, head: list[str], rows: list[list[str]]) -> str:
    th = "".join(f"<th>{h}</th>" for h in head)
    body = "".join("<tr><th>" + r[0] + "</th>" + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
    return f'<div class="rv-wrap"><h3>{title}</h3><table><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def summaries(rec: dict, cur: str) -> tuple[str, str]:
    """HTML compacto de 'Resumen de Valoración' y 'Descuento de múltiplos'."""
    dm, link = rec["descuentoMultiples"], rec.get("hojaGoogle") or ""
    trio = lambda t: [_money((t or {}).get(k), cur) for k in SCEN]  # noqa: E731
    fy3 = [[f"{m['nombre']} ({_pct(m.get('peso'))})"] + trio(m) for m in rec.get("metodos") or []]
    fy3.append(["Combinado FY+3"] + trio(rec.get("objetivoPonderado")))
    today = [[f"DCF hoy, valor presente ({_pct(dm.get('pesoDcf'))})"] + trio(dm["dcfHoy"])]
    today += [[f"&nbsp;&nbsp;{m['nombre']} · VP consolidado ({_pct(m.get('peso'))})"] + [_money(m[k]["consolidado"], cur) for k in SCEN]
              for m in dm.get("metodos") or []]
    today += [[f"Múltiplos consolidados hoy ({_pct(dm.get('pesoMultiplos'))})"] + trio(dm["multiplesHoy"]),
              ["Valor intrínseco ponderado hoy"] + trio(rec.get("valorPresentePonderado")),
              ["Precio de compra con MOS"] + trio(rec.get("precioMOSHoy"))]
    ke = dm.get("costoPatrimonio")
    a = f'<a href="{link}" target="_blank" rel="noopener noreferrer">Abrir hoja con fórmulas</a>' if link else ""
    note = (f"<p>Precio de referencia de la hoja: {_money(rec.get('precio'), cur)}. Tasa de descuento (Ke): "
            f"{ke * 100:.2f}%. Múltiplos: VP = (precio FY+n + dividendos acumulados) ÷ (1 + Ke)^n para n = 1, 2 y 3; "
            f"consolidado por método: {dm.get('criterio')}. {a}.</p>")
    resumen = _table(f"{rec.get('ticker')} · valoración FY+3 (sin descontar)", ["Método", "Conservador", "Base", "Optimista"], fy3) \
        + _table("Valor por acción hoy · DCF + múltiplos descontados", ["Método", "Conservador", "Base", "Optimista"], today) + note

    blocks = []
    for k in SCEN:
        rows = []
        for m in dm.get("metodos") or []:
            d = m[k]
            rows.append([m["nombre"], _money(d["fy"][2], cur)] + [_money(v, cur) for v in d["vp"]]
                        + [_money(d["consolidado"], cur), d.get("chequeo") or "—"])
        c = dm["consolidado"][k]
        rows.append(["Múltiplos consolidados", _money(c["fy"][2], cur)] + [_money(v, cur) for v in c["vp"]]
                    + [_money(c["consolidado"], cur), (dm["chequeo"]["resultado"] or {}).get(k) or "—"])
        blocks.append(_table(f"{k.capitalize()} · múltiplos a 1, 2 y 3 años traídos a hoy",
                             ["Método", "FY+3 sin descontar", "VP 1 año", "VP 2 años", "VP 3 años", "Consolidado hoy", "VP3 &lt; FY+3"], rows))
    descuento = "".join(blocks) + _table("Valor intrínseco hoy", ["Concepto", "Conservador", "Base", "Optimista"], today[:1] + today[-3:]) + note
    return resumen, descuento


def _same_fy3(old: dict, new: dict) -> list[str]:
    diffs = []
    for a, b in zip(old.get("metodos") or [], new.get("metodos") or []):
        for k in ("conservador", "base", "optimista"):
            x, y = a.get(k), b.get(k)
            if isinstance(x, (int, float)) and isinstance(y, (int, float)) and abs(x - y) > 1e-6 * max(1.0, abs(x)):
                diffs.append(f"{a.get('nombre')} {k}: {x:.4f} -> {y:.4f}")
    return diffs


def main(paths: list[str]) -> int:
    srv = serve()
    bad = 0
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
        for path in paths:
            old = json.loads(Path(path).read_text())
            sid = (old.get("hojaGoogle") or "").split("/d/")[-1].split("/")[0]
            if not sid:
                print(f"{path}: sin hojaGoogle, se omite")
                continue
            xlsx = os.path.join(tempfile.gettempdir(), f"{sid}.xlsx")
            export_xlsx(sid, xlsx)
            ctx = browser.new_context()
            ctx.add_init_script("localStorage.setItem('jmr-auth-ok-v1','1');localStorage.setItem('jmr-gh-datastore-token','x');")
            new, status = regen(sid, xlsx, ctx.new_page())
            ctx.close()
            diffs = _same_fy3(old, new)
            dm = new.get("descuentoMultiples") or {}
            if diffs or dm.get("version") != 2:
                bad += 1
                print(f"{old.get('ticker')}: NO se actualiza ({'version ' + str(dm.get('version')) if not diffs else ''}) {diffs[:3]}")
                continue
            for k in FIELDS:
                old[k] = new.get(k)
            m = re.search(r"<td>([^<\d-]+?)\s[\d-]", ((old.get("hojas") or {}).get("valoracion") or {}).get("Resumen de Valoración", ""))
            cur = m.group(1) if m else "US$"
            old_val = old.setdefault("hojas", {}).setdefault("valoracion", {})
            old_val["Resumen de Valoración"], old_val["Descuento de múltiplos"] = summaries(old, cur)
            old["descuentoMultiples"]["nota"] = (
                "29-sep-2026: cada múltiplo se trae a valor presente en 1, 2 y 3 años — VP = (precio FY+n + "
                "dividendos acumulados, nominales) ÷ (1 + Ke)^n — y se consolida por método con "
                f"«{dm.get('criterio')}». Ponderado = DCF × peso DCF + múltiplos consolidados × peso múltiplos.")
            Path(path).write_text(json.dumps(old, ensure_ascii=False, indent=2) + "\n")
            chk = (dm.get("chequeo") or {}).get("resultado") or {}
            print(f"{old.get('ticker'):5s} {status[:20]:20s} DCF {dm['dcfHoy']['base']:.2f}  múltiplos {dm['multiplesHoy']['base']:.2f}  "
                  f"ponderado {old['valorPresentePonderado']['base']:.2f}  chequeo {chk}", flush=True)
    srv.shutdown()
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
