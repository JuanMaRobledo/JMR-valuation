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

Uso: PYTHONPATH=.:scripts python scripts/lease_quarter_update.py TICKER ... [--apply]
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
import time
from pathlib import Path

from jmr_valuation.io.sheets_auth import get_gspread_client

_ROOT = Path(__file__).resolve().parents[1]
OUT = _ROOT / "reference" / "revision_dcf_2026-09-30"
REF = _ROOT / "reference" / "damodaran"
DATOS = _ROOT.parent / "Modelo-JMR-datos" / "valoraciones"
IS, OL = "Input sheet", "Operating lease converter"
CORTE = "2026-09-30"  # fecha de corte de la información (no se usan presentaciones posteriores)
P = "LesseeOperatingLeaseLiabilityPayments"
GASTO = ("OperatingLeaseCost", "OperatingLeasePayments")


def facts(tk: str) -> dict:
    import audit_statements_sec as sec
    return sec.facts(tk, sec.cik_map()[tk])


def vals(f: dict, tag: str) -> list[dict]:
    return [x for x in f.get(tag, {}).get("units", {}).get("USD", [])
            if x.get("form") in ("10-K", "10-Q") and x.get("filed", "") <= CORTE]


def inst(f, tag, end):
    return next((x["val"] / 1e6 for x in vals(f, tag) if x["end"] == end and "start" not in x), None)


def _d(s):
    return dt.date.fromisoformat(s)


def gasto_ltm(f, q, fy, fy_start):
    """Gasto de arrendamiento de los últimos doce meses: ejercicio + acumulado − acumulado del año anterior."""
    for tag in GASTO:
        xs = vals(f, tag)
        anual = next((x["val"] for x in xs if x["end"] == fy and x.get("start") == fy_start), None)
        if q == fy:
            if anual is not None:
                return anual / 1e6, f"{tag} del ejercicio"
            continue
        ytd = [x for x in xs if x["end"] == q and "start" in x]
        if not ytd or anual is None:
            continue
        y = max(ytd, key=lambda x: (_d(q) - _d(x["start"])).days)
        dias = (_d(q) - _d(y["start"])).days
        prev = next((x["val"] for x in xs if "start" in x and abs((_d(x["end"]) - _d(q)).days + 364) <= 10
                     and abs((_d(x["end"]) - _d(x["start"])).days - dias) <= 10), None)
        if prev is not None:
            return (anual + y["val"] - prev) / 1e6, f"{tag}: ejercicio + acumulado − acumulado del año anterior"
        if anual is not None:
            return anual / 1e6, f"{tag} del ejercicio (sin acumulado comparable)"
    return None, "sin dato"


def datos(tk: str) -> dict:
    f = facts(tk)
    tot = vals(f, f"{P}Due")
    q = max(x["end"] for x in tot)
    forma = next(x["form"] for x in tot if x["end"] == q)
    fy = max(x["end"] for x in tot if x["form"] == "10-K")
    fy_start = next((x["start"] for t in GASTO for x in vals(f, t) if x["end"] == fy and x["form"] == "10-K"
                     and 350 <= (_d(fy) - _d(x["start"])).days <= 380), None)
    gasto, gasto_def = gasto_ltm(f, q, fy, fy_start)
    total = inst(f, f"{P}Due", q)
    g = lambda t: inst(f, f"{P}{t}", q)  # noqa: E731
    r = g("RemainderOfFiscalYear")
    if r is None:  # 10-K o tabla en años móviles: se usa tal cual
        anios = [g("DueNextTwelveMonths") or g("DueNextRollingTwelveMonths") or 0.0,
                 g("DueYearTwo") or g("DueInRollingYearTwo") or 0.0, g("DueYearThree") or g("DueInRollingYearThree") or 0.0,
                 g("DueYearFour") or g("DueInRollingYearFour") or 0.0, g("DueYearFive") or g("DueInRollingYearFive") or 0.0]
        resto = total - sum(anios)
        frac, cal, supuesto = 0.0, None, False
    else:
        c = [g("DueNextTwelveMonths") or 0.0, g("DueYearTwo") or 0.0, g("DueYearThree") or 0.0, g("DueYearFour") or 0.0]
        c5 = g("DueYearFive")
        despues = total - r - sum(c) - (c5 or 0.0)
        supuesto = c5 is None
        if supuesto:  # el quinto año calendario no se publica: igual al cuarto (sin superar «después»)
            c5 = min(c[3], despues)
        ytd_start = min(x["start"] for t in GASTO for x in vals(f, t) if x["end"] == q and "start" in x) if any(
            x["end"] == q and "start" in x for t in GASTO for x in vals(f, t)) else None
        fy_ini = ytd_start or (_d(q) - dt.timedelta(days=182)).isoformat()
        frac = min(max((_d(q) - _d(fy_ini)).days / 365, 0.0), 1.0)  # fracción del ejercicio transcurrida
        cs = c + [c5]
        # año móvil 1 = lo que queda del ejercicio + la fracción ya transcurrida del ejercicio siguiente
        anios = [r + frac * cs[0]] + [(1 - frac) * cs[i] + frac * cs[i + 1] for i in range(4)]
        resto = (despues - frac * c5) if supuesto else (despues + (1 - frac) * c5)
        cal = {"resto_ejercicio": r, "anios": cs, "despues": despues, "quinto_supuesto": supuesto}
    defs = (("OperatingLeaseLiability",), ("OperatingLeaseLiabilityNoncurrent", "OperatingLeaseLiabilityCurrent"),
            ("OperatingLeaseLiabilityNoncurrent",))

    def pas(e, tags):
        v = [inst(f, t, e) for t in tags]
        return None if any(x is None for x in v) else sum(v)

    pasivo = next((pas(q, t) for t in defs if pas(q, t) is not None), None)
    escala = None
    # La mayoría de los 10-Q no repite la tabla de vencimientos: si hay un balance posterior a la última tabla, los
    # compromisos y el gasto se escalan con el pasivo de ese trimestre, medido con la misma definición en las dos fechas.
    fechas = sorted({x["end"] for t in ("OperatingLeaseLiability", "OperatingLeaseLiabilityNoncurrent")
                     for x in vals(f, t) if "start" not in x})
    qb = fechas[-1] if fechas else q
    par = next(((pas(qb, t), pas(q, t)) for t in defs if pas(qb, t) and pas(q, t)), None)
    if qb > q and par:
        escala = par[0] / par[1]
        anios, resto, total = [a * escala for a in anios], resto * escala, total * escala
        g2, d2 = gasto_ltm(f, qb, fy, fy_start)
        if g2 is None or "sin acumulado" in d2:
            g2, d2 = (gasto * escala, f"gasto del ejercicio × {escala:.3f} (el 10-Q no publica el gasto acumulado)") if gasto else (None, d2)
        gasto, gasto_def = g2, d2
        forma, pasivo, q_tabla, q = "10-Q", par[0], q, qb
    else:
        q_tabla = q
    return {"trimestre": q, "forma": forma, "cierre_10k": fy, "tabla_al": q_tabla, "escala": escala, "gasto_ltm": gasto,
            "gasto_def": gasto_def, "calendario": cal, "fraccion": frac, "anios": anios, "despues": resto, "total": total,
            "pasivo_balance": pasivo}


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    for tk in [a for a in argv if not a.startswith("--")]:
        d = datos(tk)
        print(tk, json.dumps(d, default=lambda x: round(x, 3)))
        arr0 = json.loads((REF / f"{tk}.json").read_text()).get("arrendamientos")
        if not arr0:
            print(f"{tk}: sin conversor de arrendamientos (NIIF 16 o sin arrendamientos); no se toca")
            continue
        if str(arr0.get("cierre")) == d["trimestre"] and "--forzar" not in argv:
            print(f"{tk}: el conversor ya usa el {d['forma']} al {d['trimestre']}; sin cambios")
            continue
        if d["gasto_ltm"] is None or not d["total"]:
            print(f"{tk}: faltan datos de la SEC ({d['gasto_def']}); no se toca")
            continue
        if not apply:
            continue
        sid = re.search(r"/d/([^/]+)", json.loads(next(DATOS.glob(f"{tk}-*.json")).read_text())["hojaGoogle"]).group(1)
        sh = get_gspread_client().open_by_key(sid)
        rng = [f"'{OL}'!E5", f"'{OL}'!B8:B13", f"'{OL}'!C29", f"'{OL}'!F33", f"'{IS}'!B12"]
        cur = sh.values_batch_get(rng, params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
        v = [x.get("values", [[None]]) for x in cur]
        pv0, adj0, rev = v[2][0][0], v[3][0][0], v[4][0][0]
        fm = sh.values_batch_get([f"'{IS}'!B28", f"'{IS}'!B30"], params={"valueRenderOption": "FORMULA"})["valueRanges"]
        b28, b30 = ((x.get("values") or [[None]])[0][0] for x in fm)
        nuevos = [round(d["gasto_ltm"], 3)] + [round(x, 3) for x in d["anios"]] + [round(d["despues"], 3)]
        celdas = ["E5", "B8", "B9", "B10", "B11", "B12", "B13"]
        antes = [v[0][0][0]] + [r[0] for r in v[1]]
        cal = d["calendario"]
        motivo = (f"Arrendamientos al último informe ({d['forma']} al {d['trimestre']}, SEC XBRL): gasto de arrendamiento "
                  f"de los últimos doce meses ({d['gasto_def']}) y compromisos "
                  + (f"por año calendario pasados a años móviles (fracción del ejercicio transcurrida {d['fraccion']:.2f}"
                     + ("; el quinto año calendario, no publicado, igual al cuarto" if cal["quinto_supuesto"] else "") + ")."
                     if cal else "en años móviles tal como se publican.")
                  + (f" La tabla de vencimientos más reciente es del {d['tabla_al']}: se escaló por {d['escala']:.3f} = pasivo de "
                     f"arrendamientos al {d['trimestre']} / pasivo al {d['tabla_al']}." if d.get("escala") else ""))
        sh.values_batch_update({"valueInputOption": "USER_ENTERED",
                                "data": [{"range": f"'{OL}'!{c}", "values": [[n]]} for c, n in zip(celdas, nuevos)]})
        time.sleep(3)
        o = sh.values_batch_get([f"'{OL}'!C29", f"'{OL}'!F33"], params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
        pv, adj = (x["values"][0][0] for x in o)
        import apply_lease_conversion as alc
        spec_p = REF / f"{tk}.json"
        spec = json.loads(spec_p.read_text())
        dm_new = adj / rev
        delta = dm_new - arr0["margen_pp"]
        b28n, b30n = alc.ajusta(b28, delta), alc.ajusta(b30, delta)
        data = [{"range": f"'{IS}'!{c}", "values": [[n]]} for c, n in (("B28", b28n), ("B30", b30n)) if n is not None]
        if data:
            sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": data})
        cambios = [{"hoja": OL, "celda": c, "antes": a, "despues": n, "motivo": motivo} for c, a, n in zip(celdas, antes, nuevos)]
        mm = (f"Margen en base ajustada por arrendamientos: ajuste del EBIT {adj:.1f} / ventas {rev:.1f} = {dm_new * 100:.2f} pp "
              f"(antes {arr0['margen_pp'] * 100:.2f} pp al {arr0.get('cierre')}); diferencia {delta * 100:+.2f} pp.")
        cambios += [{"hoja": IS, "celda": c, "antes": a, "despues": n, "motivo": mm}
                    for c, a, n in (("B28", b28, b28n), ("B30", b30, b30n)) if n is not None]
        spec["arrendamientos"] = {**arr0, "vp": pv, "ajuste_ebit": adj, "margen_pp": dm_new, "capital_ventas": pv / rev,
                                  "cierre": d["trimestre"], "informe": d["forma"],
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
