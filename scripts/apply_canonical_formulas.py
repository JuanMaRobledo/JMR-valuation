#!/usr/bin/env python
"""Una sola fórmula para todas las hojas del Modelo JMR (2-oct-2026): plantilla maestra + contrato ADBE.

Conjunto canónico = fórmulas de la plantilla maestra en las pestañas de cálculo, más el contrato de escenarios
(30-sep-2026, aplicado a 18 hojas): los múltiplos de cada escenario se proyectan con la historia correspondiente
('Escenarios e historias': Conservadora filas 52-60, Base 28-36, Optimista 100-108), la deuda de los múltiplos EV
sale de 'Valuation output', se
restan preferentes (Input B76), acciones constantes sin referencia circular y zonas de compra sobre el valor de hoy.
También: Resumen C6:E6 = DCF de las historias × (1 + Ke)^3 (prompts del 2-oct-2026).

Se respetan supuestos y datos: 'Input sheet' (incluida la deuda B16, que depende de si los arrendamientos entran por el
conversor), múltiplos objetivo J8/J19/J30, parámetros de escenario
de referencia histórica en 'Valuation output' (filas 96-98), el % de EBIT de otros
ingresos proyectado en 'Financials Multiples' (E11/E50/E90; el promedio de 3 años de la maestra falla con EBIT histórico
casi nulo, p. ej. SHAK), precio fijado (Resumen B3/C25) y el
bloque del Resumen desde la fila 28. PAGS (banco, DCF FCFE financiero) conserva su bloque de múltiplos.

Uso:
    PYTHONPATH=.:scripts python scripts/apply_canonical_formulas.py --targets sheets.json [--master] [--apply]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import time
from pathlib import Path

from jmr_valuation.io.sheets_auth import get_gspread_client
from audit_master_formulas import MASTER_ID, TABS, grid_of, cells, norm

_ROOT = Path(__file__).resolve().parent.parent
EH = "'Escenarios e historias'"
COLS = "EFGH"  # FY+0..FY+3 en 'Financials Multiples' <-> C..F en la pestaña de historias
# bloque de 'Financials Multiples' -> fila de ingresos en la pestaña de historias
FM_BLOCKS = {4: 52, 43: 28, 83: 100}  # Conservador / Base / Optimista
VO_ASSUMPTION_ROWS = {96, 97, 98}  # referencia histórica; desde el 2-oct-2026 los bloques leen sus historias
EV_ROWS = (10, 21, 32)
CAP = "*(1+'Descuento de múltiplos'!$B$5)^3"


def contract(ev_formulas: dict[str, dict[str, str]], vo_b41: str, zones: dict[str, str]) -> dict[tuple[str, str], str]:
    c: dict[tuple[str, str], str] = {}
    fm = "Financials Multiples"
    import link_vo_to_stories as lv  # 2-oct-2026: cada escenario de múltiplos desde su bloque Damodaran
    for d in lv.fm_links():
        t, a = d["range"].split("!")
        c[(t.strip("'"), a)] = d["values"][0][0]
    for r_rev in FM_BLOCKS:
        r_sh, r_shg = r_rev + 27, r_rev + 28
        for i, col in enumerate(COLS[1:], start=1):
            prev = COLS[i - 1]
            c[(fm, f"{col}{r_sh}")] = f"={prev}{r_sh}"
            c[(fm, f"{col}{r_shg}")] = f'=IFERROR({col}{r_sh}/{prev}{r_sh}-1;"")'
    for tab, d in ev_formulas.items():
        c.update({(tab, a): f for a, f in d.items()})
    # Rentabilidad anualizada de cada múltiplo: «No interpretable» si el precio objetivo o el de hoy no es positivo
    # (2-oct-2026; la potencia de un negativo da #NUM!, p. ej. SHAK)
    for tab in ("EVEBITDA", "EVFCFF", "PE", "PFCFE", "POCF"):
        for r_irr, r_tot in ((14, 12), (25, 23), (36, 34)):
            for k, col in enumerate("FGH", start=1):
                c[(tab, f"{col}{r_irr}")] = (f'=IF(AND({col}{r_tot}>0;B3>0);({col}{r_tot}/B3) ^ (1 / {k}) - 1;'
                                             f'"No interpretable: precio no positivo")')
    c[("Valuation output", "B41")] = vo_b41
    for a, b, r in (("B33", "B31-B32", 33), ("B84", "B82-B83", 84), ("B135", "B133-B134", 135)):
        c[("Valuation output", a)] = f"={b}-N('Input sheet'!$B$76)"
    c.update({("Resumen de Valoración", a): f for a, f in zones.items()})
    c[("Resumen de Valoración", "A6")] = "DCF capitalizado FY+3"
    for a, h in (("C6", 6), ("D6", 5), ("E6", 8)):
        c[("Resumen de Valoración", a)] = f"={EH}!H{h}{CAP}"
    return c


def keep(tab: str, addr: str, cur, tk: str) -> bool:
    row = int(re.sub(r"[A-Z]", "", addr))
    is_formula = isinstance(cur, str) and cur.startswith("=")
    if tab == "Input sheet":
        return True
    if tab in ("EVEBITDA", "EVFCFF", "PE", "PFCFE", "POCF") and addr in ("J8", "J19", "J30"):
        return True
    if tab == "Valuation output" and row in VO_ASSUMPTION_ROWS and not is_formula:
        return True
    if tab == "Resumen de Valoración" and (row >= 28 or addr in ("B3", "C25")):
        return True
    if tab == "Financials Multiples" and addr in ("E11", "E50", "E90"):
        return True  # % de EBIT proyectado de otros ingresos/intereses: supuesto con valor por defecto (promedio 3 años)
    if tk == "PAGS" and tab in ("Financials Multiples", "Valuation output"):
        return True
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--targets", required=True)
    ap.add_argument("--master", action="store_true", help="Escribe también el contrato en la plantilla maestra")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only")
    a = ap.parse_args()
    client = get_gspread_client()
    msh = client.open_by_key(MASTER_ID)
    master = grid_of(msh, TABS)
    adbe = client.open_by_key("19WcSOKymo4gR6lnKiLB1gAitYFFwfI3xl08E4BDzLDw")
    rng = [f"{t}!F{r}:H{r}" for t in ("EVEBITDA", "EVFCFF") for r in EV_ROWS] + ["'Valuation output'!B41", "'Resumen de Valoración'!B16:E19"]
    vr = adbe.values_batch_get(rng, params={"valueRenderOption": "FORMULA"})["valueRanges"]
    ev = {"EVEBITDA": {}, "EVFCFF": {}}
    for (t, r), v in zip([(t, r) for t in ("EVEBITDA", "EVFCFF") for r in EV_ROWS], vr[:6]):
        for col, f in zip("FGH", v["values"][0]):
            ev[t][f"{col}{r}"] = f
    vo_b41 = vr[6]["values"][0][0]
    zones = {}
    for i, row in enumerate(vr[7]["values"]):
        for j, f in enumerate(row):
            zones[f"{'BCDE'[j]}{16 + i}"] = f
    C = contract(ev, vo_b41, zones)
    canon: dict[tuple[str, str], str] = {}
    for t in TABS:
        for addr, mv in cells(master[t]):
            if isinstance(mv, str) and mv.startswith("="):
                canon[(t, addr)] = mv
    canon.update(C)
    stamp = dt.date.today().isoformat()
    bdir = _ROOT / "reference" / "backups" / f"formula_unica_{stamp}"
    bdir.mkdir(parents=True, exist_ok=True)
    targets = json.loads(Path(a.targets).read_text())
    if a.master:
        targets = [["MAESTRA", MASTER_ID]] + targets
    summary = {}
    for tk, sid in targets:
        if a.only and tk not in a.only.split(","):
            continue
        sh = msh if tk == "MAESTRA" else client.open_by_key(sid)
        titles = {w.title for w in sh.worksheets()}
        g = master if tk == "MAESTRA" else grid_of(sh, {t: r for t, r in TABS.items() if t in titles})
        cur = {(t, addr): v for t in g for addr, v in cells(g[t])}
        data, backup = [], {}
        for (t, addr), f in canon.items():
            if t not in g:
                continue
            if tk == "MAESTRA" and (t, addr) not in C:
                continue
            v = cur.get((t, addr), "")
            if norm(v) == norm(f) or (tk != "MAESTRA" and keep(t, addr, v, tk)):
                continue
            q = "'" + t.replace("'", "''") + "'"
            data.append({"range": f"{q}!{addr}", "values": [[f]]})
            backup.setdefault(t, {})[addr] = v
        by_tab = {t: len(v) for t, v in backup.items()}
        summary[tk] = by_tab
        print(f"{tk:8s} {sum(by_tab.values()):4d} celdas", by_tab)
        if a.apply and data:
            (bdir / f"{tk}_{sid}.json").write_text(json.dumps(backup, ensure_ascii=False, indent=1, default=str))
            if tk == "MAESTRA" and "Escenarios e historias" not in titles:
                sh.add_worksheet("Escenarios e historias", rows=130, cols=14)
            for i in range(0, len(data), 400):
                sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": data[i:i + 400]})
        time.sleep(3)
    (bdir / ("resumen_apply.json" if a.apply else "resumen_dry.json")).write_text(json.dumps(summary, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
