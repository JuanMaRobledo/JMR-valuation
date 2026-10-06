#!/usr/bin/env python
"""Posiciones de la cartera desde la hoja «Seguimiento de cartera» de Google Drive (6-oct-2026).

Lee las pestañas Transacciones y Posiciones (cuentas IBKR, Hapi y Bróker Colombia) y escribe
reference/cartera_compras_<hoy>.json con, por empresa valorada: si está en cartera, acciones, costo promedio (costo base
de la hoja ÷ acciones), primera compra de la posición vigente (la primera compra después de la última vez que la
cantidad llegó a cero) y su precio, y las fechas de compra. Lo usa scripts/posicion_cartera.py.

Fuente, en este orden: --xlsx <archivo> (descargado con el conector de Google Drive: hoja 1P3yzgr-RXJU6fFGuVPw0_JLQMwh_
khGWuAZsZmft7kM exportada a .xlsx) o lectura directa con la cuenta de servicio, si la hoja está compartida como lector con
jmr-valuation-bot@jmr-valuation-508617.iam.gserviceaccount.com.

Uso: PYTHONPATH=.:scripts python scripts/posiciones_cartera.py [--xlsx archivo.xlsx]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from collections import defaultdict
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

HOJA = "1P3yzgr-RXJU6fFGuVPw0_JLQMwh_khGWuAZsZmft7kM"
ALIAS = {"GOOG": {"GOOG", "GOOGL"}}


def filas(args) -> tuple[list, list, str]:
    if args.xlsx:
        import openpyxl
        wb = openpyxl.load_workbook(args.xlsx, data_only=True)
        return (list(wb["Transacciones"].iter_rows(values_only=True)), list(wb["Posiciones"].iter_rows(values_only=True)),
                f"«Seguimiento de cartera» (Drive, descargada {dt.date.today()})")
    import model_steps as ms
    sh = ms.open_sheet(HOJA)
    conv = lambda v: v  # noqa: E731
    tx = sh.worksheet("Transacciones").get_all_values(value_render_option="UNFORMATTED_VALUE")
    po = sh.worksheet("Posiciones").get_all_values(value_render_option="UNFORMATTED_VALUE")
    return [[conv(x) for x in r] for r in tx], [[conv(x) for x in r] for r in po], "«Seguimiento de cartera» (Drive, lectura directa)"


def fecha(v):
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    if isinstance(v, (int, float)):
        return dt.date(1899, 12, 30) + dt.timedelta(days=int(v))
    return dt.date.fromisoformat(str(v)[:10])


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--xlsx")
    a = ap.parse_args(argv)
    tx, po, fuente = filas(a)
    empresas = sorted(json.loads((_ROOT / "reference" / "cartera_drive.json").read_text())["empresas"])
    hdr = list(tx[0])
    i = {k: hdr.index(k) for k in ("Fecha", "Cuenta", "Símbolo", "Actividad", "Cantidad", "Precio USD")}
    mov = defaultdict(list)
    for r in tx[1:]:
        if r and r[i["Actividad"]] in ("Compra", "Venta") and r[i["Símbolo"]]:
            mov[r[i["Símbolo"]]].append((fecha(r[i["Fecha"]]), r[i["Cuenta"]], r[i["Actividad"]], float(r[i["Cantidad"]]),
                                         float(r[i["Precio USD"]] or 0)))
    ph = next(k for k, r in enumerate(po) if r and r[0] == "Cuenta")
    hp = list(po[ph])
    pos = defaultdict(lambda: [0.0, 0.0])
    for r in po[ph + 1:]:
        if r and r[1]:
            pos[r[1]][0] += float(r[hp.index("Cantidad")] or 0)
            pos[r[1]][1] += float(r[hp.index("Costo base USD")] or 0)
    out = {}
    for t in empresas:
        syms = ALIAS.get(t, {t})
        L = sorted((x for s in syms for x in mov.get(s, [])), key=lambda x: x[0])
        q = sum(pos[s][0] for s in syms if s in pos)
        c = sum(pos[s][1] for s in syms if s in pos)
        if q <= 1e-9 or not L:
            ult = f" (última operación {L[-1][0]} {L[-1][2].lower()})" if L else " (sin operaciones)"
            out[t] = {"en_cartera": False, "nota": f"sin posición al {dt.date.today()}{ult}"}
            continue
        run, ini = 0.0, None
        for d, acc, act, qq, p in L:
            if run <= 1e-9 and act == "Compra":
                ini = d
            run += qq
        dia = [(qq, p) for d, acc, act, qq, p in L if d == ini and act == "Compra"]
        out[t] = {"en_cartera": True, "primera_compra": str(ini),
                  "precio_primera_compra": round(sum(q_ * p for q_, p in dia) / sum(q_ for q_, p in dia), 4),
                  "cantidad": round(q, 5), "costo_promedio": round(c / q, 4),
                  "compras": sorted({str(d) for d, acc, act, qq, p in L if act == "Compra" and d >= ini}),
                  "cuentas": sorted({acc for d, acc, act, qq, p in L if d >= ini})}
    dest = _ROOT / "reference" / f"cartera_compras_{dt.date.today()}.json"
    dest.write_text(json.dumps({"fecha": str(dt.date.today()), "fuente": fuente, "empresas": out}, ensure_ascii=False,
                               indent=1) + "\n")
    for t, v in out.items():
        print(t, f"{v['cantidad']:g} acc. a {v['costo_promedio']}" if v["en_cartera"] else v["nota"])
    print("escrito", dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
