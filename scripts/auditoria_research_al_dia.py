#!/usr/bin/env python
"""Tablas de auditoría del research al día con la revisión Damodaran del 5-oct-2026.

El research de cada empresa tiene tablas escritas a la fecha del informe que citan la beta, la prima de mercado, la tasa
libre de riesgo, el WACC y el ventas/capital de ese momento. Este script reescribe esas filas con los valores vigentes de
la valoración (reference/damodaran/<T>_resultado.json, que reproduce la hoja):
  - tabla de auditoría («Dato o supuesto | Valor del modelo y unidad | …»): valor, origen, celda y contraste de las filas
    de ventas/capital, beta, ERP, tasa libre de riesgo, WACC y WACC terminal;
  - tabla de supuestos activos («Supuesto activo y escenario | …»): el nombre de las filas de ventas/capital, beta y WACC
    y la columna de justificación;
  - tabla de escenarios («Variable JMR | Conservador | Base | Optimista | …»): la fila de ventas/capital.
Se aplica al HTML del research en Modelo-JMR-datos/analisis y, si existe, al .md de origen en data/. Es idempotente.

Uso: PYTHONPATH=.:scripts python scripts/auditoria_research_al_dia.py [--apply] [TICKER ...]
"""
from __future__ import annotations

import datetime as dt
import glob
import html
import json
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
DATOS = _ROOT.parent / "Modelo-JMR-datos"
REV = "Revisión del 5-oct-2026"

BETA = {
    "ADBE": "bottom-up de Software (System & Application) en EE.UU.", "AFYA": "bottom-up de Education, tabla global",
    "BSX": "bottom-up de Healthcare Products en EE.UU.", "CELH": "bottom-up de Beverage (Soft) en EE.UU.",
    "CMG": "bottom-up de Restaurant/Dining en EE.UU.", "DPZ": "bottom-up de Restaurant/Dining en EE.UU. (D/E alta)",
    "DUOL": "bottom-up de Software (Internet), tabla global", "EPAM": "bottom-up de Computer Services",
    "GOOG": "por ingresos: Advertising y Software en EE.UU.", "INTU": "bottom-up de Software (System & Application) en EE.UU.",
    "LULU": "bottom-up de Apparel en EE.UU.", "MSFT": "bottom-up de Software (System & Application) en EE.UU.",
    "NKE": "bottom-up de Shoe, tabla global", "NVDA": "bottom-up de Semiconductor en EE.UU.",
    "NVO": "bottom-up de Drugs (Pharmaceutical) en EE.UU.", "ONON": "bottom-up de Shoe en EE.UU.",
    "PAGS": "patrimonio de Financial Svcs., tabla global", "PLTR": "bottom-up de Software (System & Application) en EE.UU.",
    "PYPL": "patrimonio de Financial Svcs. en EE.UU.", "SHAK": "bottom-up de Restaurant/Dining en EE.UU. (con arrendamientos)",
    "UBER": "regresión de Uber; «Transportation» no describe la plataforma", "ZTS": "bottom-up de Drugs (Pharmaceutical)",
}
S2C = {
    "ADBE": "≈ el de hoy con I+D capitalizado (1,20)", "AFYA": "orgánico: con 1,5 el FCFF del año 1 coincide con el real",
    "BSX": "entre el de hoy (0,60, con crédito mercantil) y el del sector (1,48)", "CELH": "bajo el ROIC de la industria (29%)",
    "CMG": "el del sector; Chipotle no franquicia", "DPZ": "el propio (franquiciadora) y luego hacia el sector",
    "DUOL": "el de Duolingo con I+D capitalizado", "EPAM": "entre el de hoy (1,95) y el del sector (5,19)",
    "GOOG": "los años 1-5 cargan el capex de IA", "INTU": "el del sector: crecimiento orgánico",
    "LULU": "entre el del sector (1,77) y el de hoy (2,04)", "MSFT": "los años 1-5 cargan el capex de IA",
    "NKE": "el de Nike hoy (2,61) y el del sector en EE.UU. (2,62)", "NVDA": "el de hoy sin impuestos diferidos ni inversiones (2,89)",
    "NVO": "los años 1-5 cargan el capex de capacidad", "ONON": "cerca del de hoy (2,59)",
    "PAGS": "financiera: el valor sale del FCFE", "PLTR": "entre el de hoy (3,23) y el marginal",
    "PYPL": "marginal 2020-2025 con I+D capitalizado (~2,6)", "SHAK": "marginal del último año y luego hacia el sector",
    "UBER": "2,58 sin impuestos diferidos, menos las flotas autónomas", "ZTS": "el del sector; el de hoy incluye crédito mercantil",
}


def es(x: float, nd: int = 2) -> str:
    return f"{x:,.{nd}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def pct(x: float, nd: int = 2) -> str:
    return es(x * 100, nd) + "%"


def valores(tk: str) -> dict:
    r = json.loads((_ROOT / "reference" / "damodaran" / f"{tk}_resultado.json").read_text())
    a = r["historias"][0]
    d = a["detalle"]
    s1, s2 = d.get("s2c") or 0, d.get("s2c2") or d.get("s2c") or 0
    u = (a.get("margen") or 0) * (1 - (d.get("impuestoMarg") or 0))
    w0 = d["tasa"][1] if r.get("financiero") else d["wacc0"]
    return {"beta": r["beta_hoja"], "rf": r["rf"], "erp": r["erp"], "w0": w0, "wT": d["tasaTerminal"], "s1": s1, "s2": s2,
            "r1": u * s1, "r2": u * s2, "fin": bool(r.get("financiero"))}


def s2c_txt(v: dict) -> str:
    if abs(v["s1"] - v["s2"]) < 0.005:
        return f"{es(v['s1'])}x (años 1-10)"
    return f"{es(v['s1'])}x (años 1-5) / {es(v['s2'])}x (años 6-10)"


def transformar(tk: str, hdr: list[str], row: list[str], v: dict) -> list[str] | None:
    """Devuelve la fila nueva (texto plano por celda) o None si no cambia."""
    n = row[0].strip().lower()
    h0 = hdr[0].strip().lower() if hdr else ""
    out = list(row)
    if len(hdr) >= 5 and len(hdr) > 1 and "valor del modelo" in hdr[1].lower():
        if re.match(r"(sales[- ]to[- ]capital|ventas/capital)", n):
            out[0] = "Ventas/capital"
            out[1] = s2c_txt(v)
            out[2] = "Entrada manual con las referencias de Damodaran (empresa, marginal, sector); activo"
            out[3] = "Input sheet B32:B33"
            out[4] = (f"{REV}: {S2C[tk]}" + ("" if v["fin"] else f"; el capital nuevo rinde ~{pct(v['r1'], 0)}"
                      + ("" if abs(v['s1'] - v['s2']) < 0.005 else f" y ~{pct(v['r2'], 0)}")))
        elif n.startswith("beta"):
            out[0] = "Beta"
            out[1] = es(v["beta"])
            out[2] = "Bottom-up del sector; activo" if not tk == "UBER" else "Regresión; activo"
            out[3] = "Cost of capital worksheet B22:B24"
            out[4] = f"{REV}: {BETA[tk]}; sin primas por riesgos diversificables (van en las historias)"
        elif n.startswith("erp y tasa libre"):
            out[1] = f"{pct(v['erp'])} / {pct(v['rf'])}"
            out[4] = "Conciliado: Damodaran sep-2026 por regiones; UST 10 años al 30-sep-2026"
        elif n.startswith("tasa libre de riesgo y erp"):
            out[1] = f"{pct(v['rf'])} / {pct(v['erp'])}"
            out[4] = "Conciliado: UST 10 años al 30-sep-2026; Damodaran sep-2026 por regiones"
        elif n.startswith("tasa libre"):
            out[1] = pct(v["rf"])
        elif n == "erp":
            out[1] = pct(v["erp"])
        elif n.startswith("wacc terminal"):
            out[1] = pct(v["wT"])
            if v["fin"]:
                out[4] = f"{REV}: supuesto de Ke de una empresa madura en Brasil (rf + ERP con beta ~1 ≈ 12,6%)"
            else:
                out[2] = "Derivado: tasa libre de riesgo + prima de mercado madura; activo"
                out[3] = "Valuation output M14"
                out[4] = f"{REV}: recalculado por la hoja"
        elif re.match(r"(wacc|costo de capital \(wacc\))( inicial)?$", n):
            out[1] = pct(v["w0"]) + (f" (terminal {pct(v['wT'])})" if "terminal" in row[1] else "")
            out[2] = "Cálculo derivado; activo"
            out[3] = f"Cost of capital worksheet B14: beta {es(v['beta'])}, ERP {pct(v['erp'])}, rf {pct(v['rf'])}"
            out[4] = f"{REV}: recalculado por la hoja con la beta y el precio de corte (30-sep-2026)"
        else:
            return None
    elif h0.startswith("supuesto activo"):
        if re.match(r"(sales[- ]to[- ]capital|ventas/capital)", n):
            out[0] = f"Ventas/capital {s2c_txt(v)}"
        elif n.startswith("beta") or n.startswith("wacc"):
            out[0] = f"Beta {es(v['beta'])} y WACC {pct(v['w0'])} → {pct(v['wT'])}"
        else:
            return None
        if len(out) > 4:
            out[4] = f"{REV}: ver la nota al inicio del informe y la sección de historias Damodaran"
    elif h0.startswith("variable jmr") and re.match(r"(sales[- ]to[- ]capital|ventas/capital)", n):
        for i in (1, 2, 3):
            if i < len(out):
                out[i] = s2c_txt(v)
        if len(out) > 4:
            out[4] = f"{REV}: {S2C[tk]} (igual en los tres escenarios)"
    else:
        return None
    return out if out != row else None


def celdas_html(tr: str) -> list[str]:
    return [html.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]


def en_html(tk: str, h: str, v: dict) -> tuple[str, int]:
    n = 0

    def tabla(m):
        nonlocal n
        tb = m.group(0)
        trs = re.findall(r"<tr>.*?</tr>", tb, re.S)
        if not trs:
            return tb
        hdr = celdas_html(trs[0])
        for tr in trs[1:]:
            nueva = transformar(tk, hdr, celdas_html(tr), v)
            if nueva is None:
                continue
            tds = re.findall(r"(<td[^>]*>)(.*?)(</td>)", tr, re.S)
            vieja = celdas_html(tr)
            partes = [f"{a}{html.escape(x, quote=False) if x != y else c}{b}" for (a, c, b), x, y in zip(tds, nueva, vieja)]
            tb = tb.replace(tr, "<tr>\n" + "\n".join(partes) + "\n</tr>", 1)
            n += 1
        return tb

    return re.sub(r"<table>.*?</table>", tabla, h, flags=re.S), n


def en_md(tk: str, m: str, v: dict) -> tuple[str, int]:
    lines, n, hdr = m.split("\n"), 0, None
    for i, ln in enumerate(lines):
        if not ln.startswith("|"):
            hdr = None
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if hdr is None:
            hdr = cells
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        nueva = transformar(tk, hdr, cells, v)
        if nueva is not None:
            lines[i] = "| " + " | ".join(nueva) + " |"
            n += 1
    return "\n".join(lines), n


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    tks = [a for a in argv if not a.startswith("--")] or [t for t in sorted(BETA) if t != "CELH"]  # CELH: research del 5-oct
    for tk in tks:
        v = valores(tk)
        p = Path(glob.glob(str(DATOS / "analisis" / f"{tk}-research-*.json"))[0])
        j = json.loads(p.read_text())
        h, nh = en_html(tk, j["html"], v)
        md = _ROOT / "data" / str(j.get("sourceName") or "")
        nm = 0
        if j.get("sourceName") and md.is_file():
            m, nm = en_md(tk, md.read_text(), v)
        print(f"{tk:5s} filas: html {nh} · md {nm if md.is_file() else '—'}")
        if apply:
            if nh:
                j["html"] = h
                j["updatedAt"] = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
                p.write_text(json.dumps(j, ensure_ascii=False, indent=2) + "\n")
            if nm:
                md.write_text(m)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
