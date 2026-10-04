#!/usr/bin/env python
"""Rellena «Cost of Sales» y «Selling, General & Admin» en el estado de resultados con lo que reporta la SEC (4-oct-2026).

El importador dejó esas filas en 0 en CMG, INTU, PYPL, SHAK (costo de ventas) y CMG, DPZ, SHAK (SG&A); la pestaña de
márgenes mostraba entonces un margen bruto de 100%. No tocan el DCF ni los múltiplos (usan ingresos, EBIT, D&A e I+D),
pero el análisis sí los lee. Fuente: el estado de resultados renderizado de cada 10-K / 10-Q (R*.htm de EDGAR), porque
varias líneas (comida y papel de SHAK, costo de ingresos de INTU, gasto de transacción de PYPL) solo vienen con
dimensiones o etiquetas propias y no aparecen en companyfacts.

Definiciones (las líneas del propio estado de la empresa):
  CMG  costo de ventas = comida, bebida y empaque + mano de obra + ocupación + otros costos operativos (sin D&A);
       SG&A = gastos generales y de administración.
  SHAK costo de ventas = comida y papel + mano de obra + otros gastos operativos + ocupación (sin D&A); SG&A = G&A.
  DPZ  SG&A = gastos generales y de administración (el costo de ventas ya estaba).
  INTU costo de ventas = costo de ingresos (producto + servicio) + amortización de tecnología adquirida (= costos y
       gastos totales − ventas y mercadeo − I+D − G&A − amortización de otros intangibles − reestructuración).
  PYPL costo de ventas = gasto de transacción + pérdidas de transacciones y crédito (margen de transacción de PayPal).
La utilidad operativa no cambia: «Other Operating Expenses» absorbe la diferencia (Other nuevo = Other − Δcosto − ΔSG&A),
y se recalculan «Gross Profit» y su margen. LTM = año fiscal + acumulado del último 10-Q − acumulado del año anterior.
Cada columna se valida contra los ingresos y la utilidad operativa de la hoja; si no cuadran, no se toca.

Salida: reference/revision_dcf_2026-10-04/<TK>_costos_sga.json, para scripts/aplicar_cambios_celdas.py.
Uso: PYTHONPATH=.:scripts python scripts/rellenar_costos_sga.py CMG DPZ INTU PYPL SHAK
"""
from __future__ import annotations

import datetime as dt
import html
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import audit_statements_sec as sec
from jmr_valuation.io.sheets_auth import get_gspread_client

_ROOT = Path(__file__).resolve().parents[1]
DATOS = _ROOT.parent / "Modelo-JMR-datos" / "valoraciones"
OUT = _ROOT / "reference" / "revision_dcf_2026-10-04"
CACHE = Path("/tmp/jmr_sec_r")
CORTE = "2026-09-30"
UA = sec.UA
IS = "Income Statement"
MESES = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}

# patrones (regex, minúsculas) de las líneas que se suman; «todas» = también las repetidas por segmento (#2, #3…)
DEF = {
    "CMG": {"cogs": [r"^food, beverage and packaging", r"^labor$", r"^occupancy$", r"^other operating costs"],
            "sga": [r"^general and administrative"]},
    "SHAK": {"cogs": [r"^food and paper", r"^labor and related", r"^other operating expenses", r"^occupancy and related"],
             "sga": [r"^general and administrative"]},
    "DPZ": {"sga": [r"^general and administrative$"]},
    # INTU solo etiqueta el costo de ingresos por segmento (y cambia el nombre entre años): se toma como el resto de
    # «total costs and expenses» menos los gastos operativos, que equivale a producto + servicio + tecnología adquirida
    "INTU": {"cogs": "residuo", "total": [r"^total costs and expenses"],
             "menos": [r"^selling and marketing", r"^research and development", r"^general and administrative",
                       r"^amortization of other acquired intangible", r"^restructuring"]},
    "PYPL": {"cogs": [r"^transaction expense", r"^transaction and (credit|loan) losses"]},
}
FILA = {"rev": 3, "cogs": 5, "gp": 6, "gpm": 7, "sga": 8, "other": 11, "ebit": 12}


def get(u: str) -> bytes:
    CACHE.mkdir(exist_ok=True)
    p = CACHE / re.sub(r"[^A-Za-z0-9]", "_", u)[-150:]
    if p.exists():
        return p.read_bytes()
    for i in range(5):
        try:
            b = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()
            break
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(2 ** i)
    else:
        raise err
    p.write_bytes(b)
    time.sleep(0.15)
    return b


def presentaciones(cik: int) -> list[tuple]:
    s = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    bloques = [s["filings"]["recent"]] + [json.loads(get("https://data.sec.gov/submissions/" + f["name"]))
                                          for f in s["filings"].get("files", [])]
    out = []
    for r in bloques:
        for i, f in enumerate(r["form"]):
            if f in ("10-K", "10-Q") and r["filingDate"][i] <= CORTE:
                out.append((f, r["filingDate"][i], r["accessionNumber"][i], r["reportDate"][i]))
    return out


def _txt(x: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", x)).strip()


def estado(cik: int, acc: str) -> dict:
    """{etiqueta: {(meses, fecha_fin): valor en millones}} del estado de resultados de la presentación."""
    base = f"https://www.sec.gov/Archives/edgar/data/{cik}/{acc.replace('-', '')}/"
    try:
        fs = get(base + "FilingSummary.xml").decode("utf-8", "ignore")
    except urllib.error.HTTPError:
        return {}
    cand = []
    for r in re.findall(r"<Report[^>]*>(.*?)</Report>", fs, re.S):
        sn = re.search(r"<ShortName>(.*?)</ShortName>", r, re.S).group(1).upper()
        hf, cat = re.search(r"<HtmlFileName>(.*?)</HtmlFileName>", r), re.search(r"<MenuCategory>(.*?)</MenuCategory>", r)
        if not hf or not cat or cat.group(1) != "Statements":
            continue
        if any(k in sn for k in ("OPERATIONS", "INCOME", "EARNINGS", "PROFIT OR LOSS")) and not any(
                k in sn for k in ("PARENTHETICAL", "BALANCE", "CASH", "EQUITY", "STOCKHOLDERS", "SHAREHOLDERS")):
            if "COMPREHENSIVE" not in sn or "AND COMPREHENSIVE" in sn:
                cand.append(("COMPREHENSIVE" in sn, hf.group(1)))
    if not cand:
        return {}
    t = get(base + sorted(cand)[0][1]).decode("utf-8", "ignore")
    head = _txt(re.search(r"<th[^>]*>(.*?)</th>", t, re.S).group(1))
    esc = 1e-3 if "Thousand" in head else 1e3 if "Billion" in head else 1.0 if "Million" in head else 1e-6
    filas = re.findall(r"<tr[^>]*>(.*?)</tr>", t, re.S)
    hdr = [[(_txt(c), int(re.search(r'colspan="?(\d+)', a).group(1)) if "colspan" in a else 1)
             for a, c in re.findall(r"<th([^>]*)>(.*?)</th>", r, re.S)] for r in filas if "<th" in r]
    if len(hdr) < 2:
        return {}
    top = []
    for lab, cs in hdr[0][1:]:
        top += [lab] * cs
    cols = []
    for a, b in zip(top, [x for x, _ in hdr[1]]):
        m = re.search(r"(\d+)\s+(Months|Weeks)", a)
        n = (int(m.group(1)) if m.group(2) == "Months" else round(int(m.group(1)) / 4.345)) if m else None
        f = re.search(r"([A-Z][a-z]{2})\.? (\d{1,2}), (\d{4})", b)
        cols.append((n, dt.date(int(f.group(3)), MESES[f.group(1)], int(f.group(2))) if f else None))
    out = {}
    for r in filas:
        if "<th" in r:
            continue
        tds = re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)
        if len(tds) < 2:
            continue
        lab, vals = _txt(tds[0]).lower(), {}
        for c, k in zip(tds[1:], cols):
            s = _txt(c).replace("$", "").replace(",", "").strip()
            neg = s.startswith("(")
            try:
                vals[k] = float(s.strip("()").strip()) * esc * (-1 if neg else 1)
            except ValueError:
                pass
        if vals:
            k, n = lab, 2
            while k in out:
                k, n = f"{lab}#{n}", n + 1
            out[k] = vals
    return out


def suma(est: dict, pats: list[str], todas: bool, per) -> float | None:
    tot, hay = 0.0, False
    for lab, v in est.items():
        base = lab.split("#")[0]
        if "#" in lab and not todas:
            continue
        if any(re.search(p, base) for p in pats) and per in v:
            tot += v[per]
            hay = True
    return round(tot, 3) if hay else None


def campo(est: dict, d: dict, c: str, per) -> float | None:
    if d.get(c) == "residuo":
        t = primera(est, d["total"], per)
        m = suma(est, d["menos"], False, per)
        return round(t - (m or 0), 3) if t is not None else None
    return suma(est, d[c], d.get("todas", False), per)


def primera(est: dict, pats: list[str], per):
    for lab, v in est.items():
        if "#" not in lab and any(re.search(p, lab) for p in pats) and per in v:
            return v[per]
    return None


REV = [r"^total (net )?revenues?:?$", r"^net revenues?:?$", r"^revenues?$", r"^total revenue"]
EBIT = [r"^operating income from continuing operations", r"^income \(loss\) from operations", r"^income from operations", r"^operating income", r"^income \(loss\) from operations"]


def main(argv: list[str]) -> int:
    gc = get_gspread_client()
    ciks = sec.cik_map()
    for tk in argv:
        d = DEF[tk]
        cik = ciks[tk]
        fl = presentaciones(cik)
        anual: dict = {}  # fecha_fin -> {campo: valor} (presentación más reciente gana)
        for f in sorted([x for x in fl if x[0] == "10-K" and x[3] >= "2015-06-01"], key=lambda x: x[1]):
            est = estado(cik, f[2])
            pers = {k for v in est.values() for k in v if k[0] and k[0] >= 12}
            for per in pers:
                rec = {"rev": primera(est, REV, per), "ebit": primera(est, EBIT, per), "src": f"10-K {f[3]} ({f[2]})"}
                for c in ("cogs", "sga"):
                    if c in d:
                        rec[c] = campo(est, d, c, per)
                anual.setdefault(per[1], []).append(rec)  # en orden de presentación
        ult_q = max([x for x in fl if x[0] == "10-Q"], key=lambda x: x[3])
        ult_k = max([x for x in fl if x[0] == "10-K"], key=lambda x: x[3])
        ltm = None
        if ult_q[3] <= ult_k[3]:  # el último informe es el 10-K: LTM = año fiscal
            ltm = {**anual[max(anual)][-1], "src": f"10-K {ult_k[3]} (último informe; LTM = año fiscal)"}
        else:
            est = estado(cik, ult_q[2])
            ytd = sorted({k for v in est.values() for k in v if k[0] and k[0] < 12}, key=lambda k: (-k[0], k[1]))
            n = ytd[0][0]
            prev, cur = sorted([k for k in ytd if k[0] == n], key=lambda k: k[1])
            fy = anual[max(anual)][-1]
            ltm = {"src": f"10-K {ult_k[3]} + 10-Q {ult_q[3]} ({n} meses) − mismo periodo del año anterior"}
            for c in ("rev", "ebit", "cogs", "sga"):
                if c in d or c in ("rev", "ebit"):
                    pats = REV if c == "rev" else EBIT
                    fn = (lambda p: primera(est, pats, p)) if c in ("rev", "ebit") else (lambda p, c=c: campo(est, d, c, p))
                    a, b = fn(cur), fn(prev)
                    ltm[c] = round(fy[c] + a - b, 3) if None not in (fy.get(c), a, b) else None
        sid = re.search(r"/d/([^/]+)", json.loads(next(DATOS.glob(f"{tk}-*.json")).read_text())["hojaGoogle"]).group(1)
        sh = gc.open_by_key(sid)
        g = sh.values_get(f"'{IS}'!A1:L13", params={"valueRenderOption": "UNFORMATTED_VALUE"})["values"]
        hdr = g[1]
        cambios, informe = [], []
        for j in range(1, 12):
            h = hdr[j] if j < len(hdr) else ""
            if h == "LTM":
                rec = ltm
            else:
                m = re.match(r"([A-Z][a-z]{2}) '(\d{2})", str(h))
                if not m:
                    continue
                mes, an = MESES[m.group(1)], 2000 + int(m.group(2))
                k = [x for x in anual if x.year == an and x.month == mes]
                recs = anual[k[0]] if k else []
                # la presentación más reciente cuyos ingresos coinciden con la hoja (la hoja puede no estar reexpresada)
                ok = [x for x in recs if x.get("rev") and isinstance(g[2][j], (int, float)) and abs(g[2][j] / x["rev"] - 1) < 0.01]
                rec = ok[-1] if ok else (recs[-1] if recs else None)
            col = chr(65 + j)
            v = {c: (g[r - 1][j] if j < len(g[r - 1]) else None) for c, r in FILA.items()}
            if not rec:
                informe.append(f"{h}: sin estado de la SEC")
                continue
            if not (isinstance(v["rev"], (int, float)) and rec.get("rev") and abs(v["rev"] / rec["rev"] - 1) < 0.01):
                informe.append(f"{h}: ingresos de la hoja {v['rev']} ≠ SEC {rec.get('rev')}; no se toca")
                continue
            if rec.get("ebit") is not None and isinstance(v["ebit"], (int, float)) and abs(v["ebit"] - rec["ebit"]) > max(1.0, abs(rec["ebit"]) * 0.02):
                informe.append(f"{h}: utilidad operativa de la hoja {v['ebit']} ≠ SEC {rec['ebit']} (se informa)")
            nuevo = {c: v[c] for c in ("cogs", "sga")}
            for c in ("cogs", "sga"):
                if c in d and rec.get(c) is not None:
                    nuevo[c] = round(rec[c], 2)
            dc = (nuevo["cogs"] or 0) - (v["cogs"] or 0)
            ds = (nuevo["sga"] or 0) - (v["sga"] or 0)
            if abs(dc) < 0.05 and abs(ds) < 0.05:
                continue
            src = f"SEC {rec['src']}"
            otro = round(v["other"] - dc - ds, 2)
            gp = round(v["rev"] - nuevo["cogs"], 2)
            if abs(dc) >= 0.05:
                cambios.append({"hoja": IS, "celda": f"{col}{FILA['cogs']}", "antes": v["cogs"], "despues": nuevo["cogs"],
                                "motivo": f"Costo de ventas {h}: {src}."})
                cambios.append({"hoja": IS, "celda": f"{col}{FILA['gp']}", "antes": v["gp"], "despues": gp,
                                "motivo": f"Utilidad bruta {h} = ingresos − costo de ventas."})
                cambios.append({"hoja": IS, "celda": f"{col}{FILA['gpm']}", "antes": v["gpm"], "despues": round(gp / v["rev"], 4),
                                "motivo": f"Margen bruto {h}."})
            if abs(ds) >= 0.05:
                cambios.append({"hoja": IS, "celda": f"{col}{FILA['sga']}", "antes": v["sga"], "despues": nuevo["sga"],
                                "motivo": f"SG&A {h}: {src}."})
            cambios.append({"hoja": IS, "celda": f"{col}{FILA['other']}", "antes": v["other"], "despues": otro,
                            "motivo": f"Otros gastos operativos {h}: se les resta lo que pasó a costo de ventas/SG&A; la utilidad operativa no cambia."})
            if otro < -0.5:
                informe.append(f"{h}: Other Operating Expenses queda en {otro} (las líneas de la SEC incluyen D&A, que la hoja resta aparte)")
        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / f"{tk}_costos_sga.json").write_text(json.dumps(cambios, ensure_ascii=False, indent=1))
        print(f"{tk}: {len(cambios)} cambios")
        for c in cambios:
            if c["celda"][1:] in ("5", "8", "11"):
                print(f"   {c['celda']:4s} {str(c['antes']):>10} -> {str(c['despues']):>10}  {c['motivo'][:70]}")
        for x in informe:
            print("   informa:", x)
        time.sleep(3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
