#!/usr/bin/env python
"""Auditoria de la plantilla maestra del Modelo JMR (sep-2026): corrige
errores estructurales en la plantilla y en TODAS las valoraciones hechas
sobre ella, sin pisar ajustes manuales.

Cada correccion declara la formula ORIGINAL de la plantilla (y las variantes
conocidas). Una celda se reescribe solo si todavia tiene una de esas
formulas; si ya tiene la formula corregida se deja igual, y si tiene
cualquier otra cosa (un ajuste propio de esa valoracion) NO se toca y queda
listada en el informe como "personalizada". La formula anterior de cada
celda escrita se guarda en reference/backups/auditoria_2026-09-26/.

Correcciones (ver modelo/METODOLOGIA.md de Modelo-JMR, seccion Auditoria):
  A1  EV/EBITDA y EV/FCFF: el precio implicito era EV/accion (faltaba restar
      la deuda neta). Ahora (multiplo x metrica - deuda + caja + activos no
      operativos - minoritarios) / acciones.
  A2  Dividendos: la hoja 'Dividendos' estaba vacia y 'Financials Multiples'
      la leia corrida una columna; el DPS proyectado SUMABA la tasa de
      crecimiento en vez de multiplicar; y "Cumulative Dividends/Share"
      tomaba solo el dividendo de un año. Ahora DPS vivo desde el Cash Flow,
      DPS FY+1 = DPS LTM x (1+g), g = CAGR 5 años del DPS acotado a 0-15%, y
      el acumulado suma FY+1..FY+3.
  A3  Horizonte: el Resumen mezclaba el DCF (valor HOY) con los multiplos
      (precio al cierre FY+3 + dividendos) y calculaba un "CAGR a 3 años"
      sobre ambos. El DCF se lleva a 3 años al costo del equity:
      valor x (1+Ke)^3 (equivale a precio + dividendos reinvertidos).
  A4  CAGR con exponente equivocado: 'Crecimiento y Márgenes' C7:C9 y
      'Valuation output' B50:B52 dividian 2 intervalos por 3 años, 4 por 5
      y 9 por 10.
  A5  'Crecimiento y Márgenes' E7:E9 ("Margen EBITDA") promediaba la fila
      del margen EBIT (fila 13, y hasta la columna M).
  A6  Estadisticas de industria: rangos inconsistentes (L2:L7, K2:K11...)
      que incluian a la propia empresa (fila 2) y dejaban fuera peers de
      las filas 8-11. Ahora solo peers, filas 3-11, con minimo de 3 datos.
      La columna "Margen EBITDA" de industria era en realidad el CAGR 10Y.
  A7  Multiplo Base = MIN de los ultimos 4 cierres: con un año negativo
      (FCFE < 0) el minimo es negativo y el precio objetivo absurdo. Ahora
      el minimo de los multiplos POSITIVOS (si no hay, la mediana 5Y).
  A8  'Forward Valuation' M2:N13: valores de PYPL pegados en la plantilla
      (FY2027/FY2028), no referenciados. Se borran.
  A9  Etiquetas: "NTM ... Multiple" eran multiplos trailing al cierre
      fiscal; 'Crecimiento y Márgenes' B6 decia LTM y era el ultimo año
      fiscal.

Uso:
    PYTHONPATH=.:scripts python scripts/audit_fix_model.py --sheet-id ID [--dry-run]
    PYTHONPATH=.:scripts python scripts/audit_fix_model.py --all [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from gspread.exceptions import APIError  # noqa: E402

from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

BACKUP_DIR = _ROOT / "reference" / "backups" / "auditoria_2026-09-26"

FM = "'Financials Multiples'"
COLS_HIST = "BCDEFGHIJKL"  # FY-9 .. LTM, alineado con Income Statement


@dataclass
class Fix:
    code: str
    sheet: str
    cell: str
    new: str | None                 # None = borrar la celda
    old: tuple[str, ...] = ()       # formulas de plantilla que se reemplazan
    also_ok: tuple[str, ...] = ()   # variantes ya corregidas a mano (no tocar)


@dataclass
class Report:
    applied: list[tuple[str, str, str, str, str]] = field(default_factory=list)
    already: list[str] = field(default_factory=list)
    custom: list[tuple[str, str, str]] = field(default_factory=list)


def _norm(v) -> str:
    s = str(v if v is not None else "")
    return re.sub(r"\s+", "", s)


# ---------------------------------------------------------------------------
# Catalogo de correcciones
# ---------------------------------------------------------------------------

# bloques de las hojas de multiplos: (fila multiplo, fila metrica, fila precio,
# fila dividendos, fila acciones en FM, fila DPS en FM)
_BLOCKS = ((8, 9, 10, 11, 31, 35), (19, 20, 21, 22, 70, 74), (30, 31, 32, 33, 110, 114))
_FY = {"F": "E", "G": "F", "H": "G"}  # columna FY+n en la hoja de multiplo -> columna en FM
_MULT_SHEETS = {"EVEBITDA": "EV/EBITDA", "EVFCFF": "EV/FCFF", "PE": "P/E", "PFCFE": "P/FCFE", "POCF": "P/OCF"}

_NET_DEBT = "'Input sheet'!$B$16-'Input sheet'!$B$19-'Input sheet'!$B$20"


def _fixes_multiples() -> list[Fix]:
    out: list[Fix] = []
    for sheet in ("EVEBITDA", "EVFCFF"):
        for m, met, price, _div, shares, _dps in _BLOCKS:
            for c, fc in _FY.items():
                out.append(Fix(
                    "A1", sheet, f"{c}{price}",
                    f"=({c}{m}*{c}{met}-({_NET_DEBT}+'Input sheet'!$B$21))/{FM}!{fc}{shares}",
                    old=(f"={c}{m}*({c}{met}/{FM}!{fc}{shares})",
                         # primera version de este script (signo de la caja invertido)
                         f"=({c}{m}*{c}{met}-{_NET_DEBT}-'Input sheet'!$B$21)/{FM}!{fc}{shares}",
                         # variante manual (NVO) sin minoritarios
                         f"=({c}{m}*{c}{met}-({_NET_DEBT}))/{FM}!{fc}{shares}"),
                ))
    for sheet, label in _MULT_SHEETS.items():
        for m, _met, _price, div, _shares, dps in _BLOCKS:
            out.append(Fix("A2", sheet, f"G{div}", f"=SUM({FM}!E{dps}:F{dps})", old=(f"={FM}!F{dps}",)))
            out.append(Fix("A2", sheet, f"H{div}", f"=SUM({FM}!E{dps}:G{dps})", old=(f"={FM}!G{dps}",)))
        # A7: multiplo Base = minimo de los ultimos 4 cierres POSITIVOS
        out.append(Fix("A7", sheet, "J19", '=IF(COUNTIF(B19:E19;">0")=0;"";MINIFS(B19:E19;B19:E19;">0"))',
                       old=("=MIN(B19:E19)",)))
        # A9: etiquetas
        for m, *_ in _BLOCKS:
            out.append(Fix("A9", sheet, f"A{m}", f"Múltiplo {label} (histórico al cierre fiscal · objetivo FY+1..FY+3)",
                           old=(f"NTM {label} Multiple",)))
    return out


def _fixes_dividends() -> list[Fix]:
    out: list[Fix] = []
    for dps, g in ((35, 36), (74, 75), (114, 115)):
        # historicos alineados: FM B/C/D = Income Statement I/J/K = Dividendos I/J/K
        for c, (old_col, new_col, prev_old, prev_new) in zip("BCD", (("H", "I", "G", "H"), ("I", "J", "H", "I"), ("J", "K", "I", "J"))):
            out.append(Fix("A2", "Financials Multiples", f"{c}{dps}", f"=Dividendos!{new_col}$4", old=(f"=Dividendos!{old_col}$4",)))
            out.append(Fix("A2", "Financials Multiples", f"{c}{g}", f'=IFERROR({c}{dps}/Dividendos!{prev_new}4-1;"")',
                           old=(f'=IFERROR(({c}{dps}/ Dividendos!{prev_old}4)-1;"")',
                                f'=IFERROR(({c}{dps}/ Dividendos!{prev_old}4)-1;"0")')))
        out.append(Fix("A2", "Financials Multiples", f"E{dps}", f"=N(Dividendos!$L$4)*(1+E{g})", old=("=Dividendos!K$4",)))
        out.append(Fix("A2", "Financials Multiples", f"E{g}",
                       "=IFERROR(MIN(MAX((Dividendos!$K$4/Dividendos!$F$4)^(1/5)-1;0);0,15);0)",
                       old=(f'=IFERROR((E{dps}/ Dividendos!J4)-1;"0")', f'=IFERROR((E{dps}/ Dividendos!J4)-1;"")',
                            f"=(E{dps}/ Dividendos!J4)-1")))
        for c, p in (("F", "E"), ("G", "F"), ("H", "G")):
            out.append(Fix("A2", "Financials Multiples", f"{c}{dps}", f"={p}{dps}*(1+{c}{g})", old=(f"={p}{dps}+{c}{g}",)))
            out.append(Fix("A2", "Financials Multiples", f"{c}{g}", f"=$E${g}",
                           old=('=IFERROR((Dividendos!J4/Dividendos!B4)^(1/9)-1;"0")',)))
    return out


def _fixes_resumen() -> list[Fix]:
    roll = "*(1+IFERROR('Cost of capital worksheet'!$B$63;'Input sheet'!$B$36))^3"
    return [Fix("A3", "Resumen de Valoración", cell, f"='Valuation output'!{src}{roll}", old=(f"='Valuation output'!{src}",))
            for cell, src in (("C6", "B86"), ("D6", "B35"), ("E6", "B137"))]


def _fixes_growth() -> list[Fix]:
    IS = "'Income Statement'"
    out = [
        Fix("A4", "Crecimiento y Márgenes", "C7", f'=IFERROR(({IS}!K3/{IS}!H3)^(1/3)-1;"")',
            old=(f'=IFERROR(({IS}!K3 / {IS}!I3)^(1/3) - 1;"")', f"=({IS}!K3 / {IS}!I3)^(1/3) - 1")),
        Fix("A4", "Crecimiento y Márgenes", "C8", f'=IFERROR(({IS}!K3/{IS}!F3)^(1/5)-1;"")',
            old=(f'=IFERROR(({IS}!K3 / {IS}!G3)^(1/5) - 1;"")', f"=({IS}!K3 / {IS}!G3)^(1/5) - 1")),
        Fix("A4", "Crecimiento y Márgenes", "C9", f'=IFERROR(({IS}!K3/{IS}!B3)^(1/9)-1;"")',
            old=(f'=IFERROR(({IS}!K3 / {IS}!B3)^(1/10) - 1;"")', f"=({IS}!K3 / {IS}!B3)^(1/10) - 1")),
        Fix("A5", "Crecimiento y Márgenes", "E7", f"=AVERAGE({IS}!I30:K30)", old=(f"=AVERAGE({IS}!I13:M13)",)),
        Fix("A5", "Crecimiento y Márgenes", "E8", f"=AVERAGE({IS}!G30:K30)", old=(f"=AVERAGE({IS}!G13:M13)",)),
        Fix("A5", "Crecimiento y Márgenes", "E9", f"=AVERAGE({IS}!B30:K30)", old=(f"=AVERAGE({IS}!B13:M13)",)),
        Fix("A9", "Crecimiento y Márgenes", "B6", "Último año fiscal", old=("LTM",)),
        Fix("A6", "Crecimiento y Márgenes", "F14", "CAGR 10Y", old=("Margen EBITDA",)),
        Fix("A4", "Valuation output", "B50", f'=IFERROR(({IS}!K3/{IS}!H3)^(1/3)-1;"")',
            old=(f"=({IS}!K3/{IS}!I3)^(1/3)-1",), also_ok=(f"=({IS}!K3/{IS}!H3)^(1/3)-1",)),
        Fix("A4", "Valuation output", "B51", f'=IFERROR(({IS}!K3/{IS}!F3)^(1/5)-1;"")',
            old=(f"=({IS}!K3/{IS}!G3)^(1/5)-1",), also_ok=(f"=({IS}!K3/{IS}!F3)^(1/5)-1",)),
        Fix("A4", "Valuation output", "B52", f'=IFERROR(({IS}!K3/{IS}!B3)^(1/9)-1;"")',
            old=(f'=IFERROR(({IS}!K3/{IS}!B3)^(1/10)-1;"")', f"=({IS}!K3/{IS}!B3)^(1/10)-1"),
            also_ok=(f"=({IS}!K3/{IS}!B3)^(1/9)-1",)),
    ]
    # industria: solo peers (filas 3-11), con al menos 3 datos
    stats = (("15", "MIN({r})", "=MIN({o})"), ("16", "QUARTILE({r};1)", "=QUARTILE({o};1)"),
             ("17", "QUARTILE({r};2)", "=QUARTILE({o};2)"), ("18", "QUARTILE({r};3)", "=QUARTILE({o};3)"),
             ("19", "QUARTILE({r};4)", "=QUARTILE({o};4)"), ("20", "AVERAGE({r})", "=AVERAGE({o})"))
    for col, sec, olds in (("C", "L", ("L2:L7",)), ("D", "M", ("M2:M7",)), ("E", "K", ("K2:K11",)), ("F", "N", ("N2:N7",))):
        r = f"Sector!{sec}3:{sec}11"
        for row, new_t, old_t in stats:
            olds_f = [old_t.format(o=f"Sector!{o}") for o in olds]
            olds_f += [f'=IF(COUNT(Sector!{o})>=3;{new_t.format(r="Sector!" + o)};"N/D")' for o in olds]
            if col == "F" and row in ("15", "20"):
                olds_f.append("")  # la plantilla dejaba F15/F20 vacias
            out.append(Fix("A6", "Crecimiento y Márgenes", f"{col}{row}",
                           f'=IF(COUNT({r})>=3;{new_t.format(r=r)};"N/D")', old=tuple(olds_f)))
    # Sector: Promedio / Mediana solo de peers
    for c in "CDEFGHIJKLMN":
        for row, fn in (("13", "AVERAGE"), ("14", "MEDIAN")):
            olds = (f"={fn}({c}2:{c}7)", f"={fn}({c}2:{c}11)") + (("",) if (c, row) == ("C", "14") else ())
            out.append(Fix("A6", "Sector", f"{c}{row}", f'=IFERROR({fn}({c}3:{c}11);"")', old=olds))
    # Supuestos de los Multiplos: columnas de industria
    for row, sec in ((6, "G"), (7, "J"), (8, "F"), (9, "H"), (10, "I")):
        for c, fn in (("L", "AVERAGE"), ("M", "MEDIAN")):
            out.append(Fix("A6", "Supuestos de los Múltiplos", f"{c}{row}", f'=IFERROR({fn}(Sector!{sec}3:{sec}11);"")',
                           old=(f"={fn}(Sector!{sec}2:{sec}7)",)))
    return out


_FWD_STALE = {"M3": "3", "N3": "2.8", "M4": "7.9", "N4": "7"}


def all_fixes() -> list[Fix]:
    return _fixes_multiples() + _fixes_dividends() + _fixes_resumen() + _fixes_growth()


# ---------------------------------------------------------------------------
# Aplicacion
# ---------------------------------------------------------------------------

def _a1(sheet: str, cell: str) -> str:
    return f"'{sheet}'!{cell}"


def _dividendos_live(sh, titles: set[str]) -> dict[str, str]:
    """Formulas vivas para 'Dividendos' (filas 2-5, columnas B..L alineadas
    con Income Statement), solo si la fila DPS esta vacia (si alguien la
    lleno a mano, se respeta)."""
    if "Dividendos" not in titles:
        return {}
    got = sh.values_batch_get(["'Dividendos'!A2:L5"], params={"valueRenderOption": "FORMULA"})["valueRanges"][0].get("values", [])
    row4 = got[2] if len(got) > 2 else []
    if any(str(v).strip() for v in row4[1:]):
        return {}
    cf, is_ = "'Cash Flow Statement'", "'Income Statement'"
    out = {"A2": "Dividendos pagados", "A3": "Rendimiento (DPS / precio al cierre)", "A4": "DPS",
           "A5": "Payout (dividendos / utilidad neta)"}
    for c in COLS_HIST:
        out[f"{c}2"] = f'=IFERROR(-{cf}!{c}$32;"")'
        out[f"{c}3"] = f"=IFERROR({c}4/'Trailing Valuation'!{c}$3;\"\")"
        out[f"{c}4"] = f"=IFERROR(-{cf}!{c}$32/{is_}!{c}$27;0)"
        out[f"{c}5"] = f'=IFERROR(-{cf}!{c}$32/{is_}!{c}$22;"")'
    return out


def audit_sheet(client, sheet_id: str, *, dry_run: bool) -> tuple[Report, dict]:
    sh = client.open_by_key(sheet_id)
    titles = {w.title for w in sh.worksheets()}
    fixes = [f for f in all_fixes() if f.sheet in titles]
    # Precondicion de A1/A3: el Resumen debe tomar los multiplos tal cual de
    # sus hojas. Si una valoracion ya resolvio el horizonte por su cuenta
    # (p.ej. ADSK: multiplos traidos a valor presente y deuda neta restada
    # en el Resumen), aplicar A1/A3 encima duplicaria la correccion.
    res = sh.values_batch_get(["'Resumen de Valoración'!C7:E11"], params={"valueRenderOption": "FORMULA"})["valueRanges"][0].get("values", [])
    plain = all(re.fullmatch(r"=(EVEBITDA|EVFCFF|PE|PFCFE|POCF)!\$?H\$?(12|23|34)", _norm(v)) for row in res for v in row)
    skipped_pre: list[Fix] = []
    if not plain:
        skipped_pre = [f for f in fixes if f.code in ("A1", "A3")]
        fixes = [f for f in fixes if f.code not in ("A1", "A3")]
    rngs = [_a1(f.sheet, f.cell) for f in fixes]
    fwd = [_a1("Forward Valuation", c) for c in _FWD_STALE] if "Forward Valuation" in titles else []
    got = sh.values_batch_get(rngs + fwd, params={"valueRenderOption": "FORMULA"})["valueRanges"]
    cur = [(g.get("values") or [[""]])[0][0] for g in got]

    rep = Report()
    updates: dict[str, str] = {}
    for f, v in zip(fixes, cur[: len(fixes)]):
        nv = _norm(v)
        if f.new is not None and nv == _norm(f.new) or nv in {_norm(x) for x in f.also_ok}:
            rep.already.append(f"{f.sheet}!{f.cell}")
        elif nv in {_norm(x) for x in f.old}:
            updates[_a1(f.sheet, f.cell)] = f.new
            rep.applied.append((f.code, f.sheet, f.cell, str(v), f.new))
        else:
            rep.custom.append((f.code, f"{f.sheet}!{f.cell}", str(v)))

    if skipped_pre:
        rep.custom.append(("A1/A3", "Resumen de Valoración!C7:E11",
                           "horizonte ya resuelto a mano en el Resumen (múltiplos a valor presente): A1 y A3 no se aplican"))
    clears: list[str] = []
    if fwd and all(_norm(v) == _FWD_STALE[c] for c, v in zip(_FWD_STALE, cur[len(fixes):])):
        clears.append("'Forward Valuation'!M2:N13")
        rep.applied.append(("A8", "Forward Valuation", "M2:N13", "valores de PYPL", "(vacío)"))

    for cell, formula in _dividendos_live(sh, titles).items():
        updates[_a1("Dividendos", cell)] = formula
    if any(k.startswith("'Dividendos'") for k in updates):
        rep.applied.append(("A2", "Dividendos", "A2:L5", "(vacío)", "DPS/dividendos/rendimiento/payout vivos"))

    backup = {"sheet_id": sheet_id, "title": sh.title,
              "cells": {f"{s}!{c}": {"before": b, "after": a, "fix": code} for code, s, c, b, a in rep.applied}}
    if not dry_run and (updates or clears):
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        path = BACKUP_DIR / f"{sheet_id}.json"
        prev = json.loads(path.read_text())["cells"] if path.exists() else {}
        for key, cell in backup["cells"].items():
            if key in prev:  # conservar el 'before' ORIGINAL de la primera corrida
                cell["before"] = prev[key]["before"]
        backup["cells"] = {**prev, **backup["cells"]}
        path.write_text(json.dumps(backup, ensure_ascii=False, indent=1))
        if clears:
            sh.values_batch_clear(body={"ranges": clears})
        if updates:
            sh.values_batch_update({"valueInputOption": "USER_ENTERED",
                                    "data": [{"range": r, "values": [[v]]} for r, v in updates.items()]})
    return rep, backup


def snapshot(client, sheet_id: str) -> dict:
    """Precios objetivo del Resumen (para medir el impacto de la auditoria)."""
    sh = client.open_by_key(sheet_id)
    v = sh.values_batch_get(["'Resumen de Valoración'!A6:E13"], params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"][0].get("values", [])
    return {row[0]: row[2:5] for row in v if row}


def _retry(fn, tries: int = 6):
    """La API de Sheets limita a 60 lecturas/minuto: ante un 429 se espera
    y se reintenta (las correcciones son idempotentes)."""
    for i in range(tries):
        try:
            return fn()
        except APIError as exc:
            if "429" not in str(exc) or i == tries - 1:
                raise
            time.sleep(30 * (i + 1))


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--sheet-id", action="append")
    g.add_argument("--targets-json", help="JSON con [[id, nombre], ...]")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", default=str(_ROOT / "reference" / "auditoria_2026-09-26_informe.json"))
    args = ap.parse_args(argv)

    targets = [(s, s) for s in args.sheet_id] if args.sheet_id else [tuple(t[:2]) for t in json.loads(Path(args.targets_json).read_text())]
    client = get_gspread_client()
    report = json.loads(Path(args.report).read_text()) if Path(args.report).exists() else {}
    for sid, name in targets:
        before = _retry(lambda: snapshot(client, sid))
        rep, _ = _retry(lambda: audit_sheet(client, sid, dry_run=args.dry_run))
        after = before if args.dry_run else _retry(lambda: snapshot(client, sid))
        codes = sorted({a[0] for a in rep.applied})
        print(f"{name[:60]:60s} aplicadas={len(rep.applied):3d} ya_ok={len(rep.already):3d} "
              f"personalizadas={len(rep.custom):3d} {','.join(codes)}")
        for code, cell, v in rep.custom:
            print(f"    [{code}] {cell}: {v[:110]}")
        if not args.dry_run:
            report[sid] = {"nombre": name, "aplicadas": len(rep.applied), "ya_ok": len(rep.already),
                           "personalizadas": [list(x) for x in rep.custom], "antes": before, "despues": after}
    if not args.dry_run:
        Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=1, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
