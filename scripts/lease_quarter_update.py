#!/usr/bin/env python
"""Arrendamientos operativos al último trimestre (3-oct-2026).

apply_lease_conversion.py carga el conversor con el 10-K (gasto del ejercicio y compromisos de los años 1-5 y
posteriores). El prompt v4 pide el puente al patrimonio con saldos del último trimestre: este script recarga el
conversor con el último 10-Q.

  - Gasto: costo de arrendamiento operativo de los últimos doce meses (ejercicio + acumulado del año − acumulado del
    año anterior), igual que el EBIT LTM.
  - Compromisos: el 10-Q los da por año calendario (resto del ejercicio, cuatro años y «después»). Se pasan a años
    móviles desde la fecha del trimestre: año 1 = resto del ejercicio + (1 − f) × primer año completo; año k =
    f × año k−1 + (1 − f) × año k, con f = fracción del ejercicio ya transcurrida. El quinto año calendario no se
    publica: se supone igual al cuarto y se descuenta de «después» (el total no cambia).
  - Margen: el ajuste del EBIT cambia; la diferencia en puntos de ventas se suma a los márgenes del año 1 y objetivo
    de 'Input sheet' (B28, B30) y a spec["arrendamientos"] de la ficha de historias (damodaran_stories.py la aplica a
    las cuatro historias). El ventas/capital no se toca: B32/B33 se fijaron el 1-oct-2026 con la historia y la industria
    incluyendo el capital arrendado.
Respaldo y nota en cada celda; registro en reference/revision_dcf_2026-09-30/<T>_LEASEQ.json.

Uso: PYTHONPATH=.:scripts python scripts/lease_quarter_update.py SHAK [--apply]
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

from jmr_valuation.io.sheets_auth import get_gspread_client

_ROOT = Path(__file__).resolve().parents[1]
OUT = _ROOT / "reference" / "revision_dcf_2026-09-30"
REF = _ROOT / "reference" / "damodaran"
DATOS = _ROOT.parent / "Modelo-JMR-datos" / "valoraciones"
IS, OL = "Input sheet", "Operating lease converter"
UA = {"User-Agent": "JMR research juan0804@gmail.com"}
CIK = {"SHAK": "0001620533"}
P = "LesseeOperatingLeaseLiabilityPayments"


def facts(tk: str) -> dict:
    req = urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK[tk]}.json", headers=UA)
    return json.load(urllib.request.urlopen(req))["facts"]["us-gaap"]


def vals(f: dict, tag: str) -> list[dict]:
    return [x for x in f.get(tag, {}).get("units", {}).get("USD", []) if x.get("form") in ("10-K", "10-Q")]


def inst(f, tag, end):
    return next((x["val"] / 1e6 for x in vals(f, tag) if x["end"] == end and "start" not in x), None)


def dur(f, tag, start, end):
    return next((x["val"] / 1e6 for x in vals(f, tag) if x["end"] == end and x.get("start") == start), None)


def datos(tk: str) -> dict:
    f = facts(tk)
    q = max(x["end"] for x in vals(f, f"{P}Due") if x["form"] == "10-Q")
    fy = max(x["end"] for x in vals(f, f"{P}Due") if x["form"] == "10-K")
    fy_start = next(x["start"] for x in vals(f, "OperatingLeaseCost") if x["end"] == fy and x["form"] == "10-K")
    ytd_start = min(x["start"] for x in vals(f, "OperatingLeaseCost") if x["end"] == q)
    ytd = dur(f, "OperatingLeaseCost", ytd_start, q)
    # acumulado comparable del año anterior: termina ~1 año antes del trimestre y empieza al inicio de ese ejercicio
    prev = next(x["val"] / 1e6 for x in vals(f, "OperatingLeaseCost")
                if x.get("start") == fy_start and abs((dt.date.fromisoformat(x["end"]) - dt.date.fromisoformat(q)).days + 365) <= 7)
    gasto = dur(f, "OperatingLeaseCost", fy_start, fy) + ytd - prev
    r = inst(f, f"{P}RemainderOfFiscalYear", q)
    c = [inst(f, f"{P}{t}", q) for t in ("DueNextTwelveMonths", "DueYearTwo", "DueYearThree", "DueYearFour")]
    total = inst(f, f"{P}Due", q)
    resto_cal = total - r - sum(c)
    fy_end = dt.date.fromisoformat(fy).replace(year=dt.date.fromisoformat(q).year)
    frac = 1 - (fy_end - dt.date.fromisoformat(q)).days / 365  # fracción del ejercicio transcurrida
    c5 = min(c[3], resto_cal)  # quinto año calendario: no publicado, igual al cuarto
    anios = [r + (1 - frac) * c[0], frac * c[0] + (1 - frac) * c[1], frac * c[1] + (1 - frac) * c[2],
             frac * c[2] + (1 - frac) * c[3], frac * c[3] + (1 - frac) * c5]
    resto = resto_cal - (1 - frac) * c5
    pasivo = inst(f, "OperatingLeaseLiability", q) or ((inst(f, "OperatingLeaseLiabilityNoncurrent", q) or 0)
                                                       + (inst(f, "OperatingLeaseLiabilityCurrent", q) or 0))
    return {"trimestre": q, "cierre_10k": fy, "gasto_ltm": gasto, "calendario": {"resto_ejercicio": r, "anios": c,
            "despues": resto_cal, "total": total}, "fraccion": frac, "anios": anios, "despues": resto, "pasivo_balance": pasivo}


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    for tk in [a for a in argv if not a.startswith("--")]:
        d = datos(tk)
        print(tk, json.dumps(d, default=lambda x: round(x, 3)))
        if not apply:
            continue
        sid = re.search(r"/d/([^/]+)", json.loads(next(DATOS.glob(f"{tk}-*.json")).read_text())["hojaGoogle"]).group(1)
        sh = get_gspread_client().open_by_key(sid)
        rng = [f"'{OL}'!E5", f"'{OL}'!B8:B13", f"'{OL}'!C29", f"'{OL}'!F33", f"'{IS}'!B12", f"'{IS}'!B28", f"'{IS}'!B30"]
        cur = sh.values_batch_get(rng, params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
        v = [x.get("values", [[None]]) for x in cur]
        pv0, adj0, rev = v[2][0][0], v[3][0][0], v[4][0][0]
        b28, b30 = v[5][0][0], v[6][0][0]
        nuevos = [round(d["gasto_ltm"], 3)] + [round(x, 3) for x in d["anios"]] + [round(d["despues"], 3)]
        celdas = ["E5", "B8", "B9", "B10", "B11", "B12", "B13"]
        antes = [v[0][0][0]] + [r[0] for r in v[1]]
        motivo = (f"Arrendamientos al último trimestre ({d['trimestre']}, 10-Q, SEC XBRL): gasto LTM y compromisos por año "
                  f"calendario pasados a años móviles (f = {d['fraccion']:.2f}; el quinto año calendario, no publicado, igual al cuarto).")
        sh.values_batch_update({"valueInputOption": "USER_ENTERED",
                                "data": [{"range": f"'{OL}'!{c}", "values": [[n]]} for c, n in zip(celdas, nuevos)]})
        time.sleep(3)
        o = sh.values_batch_get([f"'{OL}'!C29", f"'{OL}'!F33"], params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
        pv, adj = (x["values"][0][0] for x in o)
        spec_p = REF / f"{tk}.json"
        spec = json.loads(spec_p.read_text())
        arr0 = spec["arrendamientos"]
        dm_new = adj / rev
        delta = dm_new - arr0["margen_pp"]
        b28n, b30n = round(b28 + delta, 6), round(b30 + delta, 6)
        sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": [
            {"range": f"'{IS}'!B28", "values": [[b28n]]}, {"range": f"'{IS}'!B30", "values": [[b30n]]}]})
        cambios = [{"hoja": OL, "celda": c, "antes": a, "despues": n, "motivo": motivo} for c, a, n in zip(celdas, antes, nuevos)]
        mm = (f"Margen en base ajustada por arrendamientos: ajuste del EBIT {adj:.1f} / ventas {rev:.1f} = {dm_new * 100:.2f} pp "
              f"(antes {arr0['margen_pp'] * 100:.2f} pp con el 10-K); diferencia {delta * 100:+.2f} pp.")
        cambios += [{"hoja": IS, "celda": "B28", "antes": b28, "despues": b28n, "motivo": mm},
                    {"hoja": IS, "celda": "B30", "antes": b30, "despues": b30n, "motivo": mm}]
        spec["arrendamientos"] = {**arr0, "vp": pv, "ajuste_ebit": adj, "margen_pp": dm_new, "capital_ventas": pv / rev,
                                  "cierre": d["trimestre"],
                                  "criterio": arr0.get("criterio", "") + f"; compromisos y gasto LTM del 10-Q al {d['trimestre']}"}
        spec_p.write_text(json.dumps(spec, ensure_ascii=False, indent=1))
        (OUT / f"{tk}_LEASEQ.json").write_text(json.dumps(
            {"ticker": tk, "sheet_id": sid, "fecha": dt.date.today().isoformat(), "sec": d, "vp_antes": pv0, "vp": pv,
             "ajuste_ebit_antes": adj0, "ajuste_ebit": adj, "margen_pp_antes": arr0["margen_pp"], "margen_pp": dm_new,
             "cambios": cambios}, ensure_ascii=False, indent=1))
        for c in cambios:
            sh.worksheet(c["hoja"]).insert_note(c["celda"], f"Revisión {dt.date.today():%d-%b-%Y}: antes {c['antes']}, ahora {c['despues']}. {c['motivo']}")
            time.sleep(1)
        print(f"{tk}: VP {pv0:.1f} -> {pv:.1f} (pasivo del balance {d['pasivo_balance']:.1f}); ajuste EBIT {adj0:.1f} -> {adj:.1f}; "
              f"margen {delta * 100:+.2f} pp")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
