"""Arrendamientos operativos como deuda, con el criterio de Damodaran (1-oct-2026).

Damodaran (Leases, Debt and Value; Dealing with Operating Leases in Valuation): los arrendamientos operativos son
deuda. Hay que capitalizarlos por completo:
  - deuda += valor presente de los compromisos (y entra en el peso de la deuda del WACC);
  - EBIT ajustado = EBIT + gasto de arrendamiento − depreciación del activo arrendado;
  - capital invertido += activo arrendado;
  - reinversión: el crecimiento del valor presente de los arrendamientos es capex.
La plantilla Ginzu lo hace con «Operating lease converter» al activar 'Input sheet'!B18 = Yes (VO B7 suma F33,
VO B27 y 'Cost of capital worksheet'!B46 suman C29, VO B41 suma F34). Este script, para cada empresa US GAAP:
  1. carga en el conversor el gasto del último ejercicio y los compromisos de los años 1-5 y posteriores (10-K, SEC
     XBRL) y activa B18;
  2. suma al margen del año 1, al objetivo y a los objetivos Conservador/Optimista el ajuste del EBIT en puntos de
     ventas (los márgenes del modelo pasan a estar en base ajustada);
  3. convierte el ventas/capital al capital que incluye los arrendamientos: 1/(1/s2c + VP arrendamientos/ventas)
     (cada dólar de ventas nuevas exige también activo arrendado);
  4. guarda el ajuste en la ficha de historias (spec["arrendamientos"]) para que damodaran_stories.py lo aplique a
     los márgenes y ventas/capital de cada historia.
Bajo NIIF 16 (AFYA, NVO, ONON, PAGS) el EBIT ya excluye el costo financiero de los arrendamientos y su pasivo es
deuda: no se cambian. Respaldo en reference/revision_dcf_2026-09-30/<T>_LEASECONV.json y nota en cada celda.

Uso: python scripts/apply_lease_conversion.py [--dry-run] [--gasto=TK:US$M] TICKER ...
"""
from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import audit_statements_sec as sec  # noqa: E402
from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

OUT = _ROOT / "reference" / "revision_dcf_2026-09-30"
REF = _ROOT / "reference" / "damodaran"
IS, VO, OL = "Input sheet", "Valuation output", "Operating lease converter"
GASTO = ["OperatingLeaseCost", "OperatingLeasePayments", "OperatingLeaseExpense", "LeaseAndRentalExpense"]
PAGOS = {"y1": ["LesseeOperatingLeaseLiabilityPaymentsDueNextTwelveMonths", "LesseeOperatingLeaseLiabilityPaymentsDueNextRollingTwelveMonths"],
         "y2": ["LesseeOperatingLeaseLiabilityPaymentsDueYearTwo", "LesseeOperatingLeaseLiabilityPaymentsDueInRollingYearTwo"],
         "y3": ["LesseeOperatingLeaseLiabilityPaymentsDueYearThree", "LesseeOperatingLeaseLiabilityPaymentsDueInRollingYearThree"],
         "y4": ["LesseeOperatingLeaseLiabilityPaymentsDueYearFour", "LesseeOperatingLeaseLiabilityPaymentsDueInRollingYearFour"],
         "y5": ["LesseeOperatingLeaseLiabilityPaymentsDueYearFive", "LesseeOperatingLeaseLiabilityPaymentsDueInRollingYearFive"],
         "resto": ["LesseeOperatingLeaseLiabilityPaymentsDueAfterYearFive", "LesseeOperatingLeaseLiabilityPaymentsDueAfterRollingYearFive"]}
AUTO = re.compile(r"'Input sheet'!\$?B\$?2[8-9]|'Input sheet'!\$?B\$?30|'Valuation output'!\$?B\$?6|Input sheet'!B28|Input sheet'!B30")


def datos(tk: str) -> dict:
    f = sec.facts(tk, sec.cik_map()[tk])
    fy, _ = sec.periods(f)
    fs = sec.fy_start(f, fy)
    g = next((sec.duration(f, t, fs, fy) for t in GASTO if sec.duration(f, t, fs, fy)), None)
    p = {k: next((sec.instant(f, t, fy) for t in ts if sec.instant(f, t, fy) is not None), 0.0) for k, ts in PAGOS.items()}
    return {"cierre": fy, "gasto": g, **p}


def num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def ajusta(old, delta, es_s2c=False, k=0.0):
    """Nuevo valor de una celda de margen (+delta) o de ventas/capital (transformado); None si se ajusta sola."""
    if es_s2c:
        if num(old) and old > 0:
            return round(1 / (1 / old + k), 4)
        return None
    if num(old):
        return round(old + delta, 6)
    s = str(old)
    if s.startswith("=") and (AUTO.search(s) or re.fullmatch(r"=\$?B\$?6", s)):
        return None  # depende de B28/B30/B6, que ya se ajustan
    if s.startswith("="):
        return f"=({s[1:]})+{str(round(delta, 6)).replace('.', ',')}"
    return None


def main(argv):
    dry = "--dry-run" in argv
    gc = get_gspread_client()
    for tk in [a for a in argv if not a.startswith("--")]:
        d = datos(tk)
        # 6-oct-2026 (MCD): si el gasto del ejercicio no está etiquetado en el XBRL (MCD lo publica solo en la tabla de
        # «rent expense» del 10-K: US$1.631M en 2025) se pasa a mano con --gasto=TK:valor (US$ millones) y se cita.
        manual = dict(a.split("=", 1)[1].split(":") for a in argv if a.startswith("--gasto="))
        if manual.get(tk):
            d["gasto"] = float(manual[tk])  # US$ millones, como el resto de datos()
        if d["gasto"] is None:
            print(f"{tk}: gasto de arrendamientos operativos no etiquetado en el XBRL; páselo con --gasto={tk}:<US$ millones> "
                  "(tabla de gasto de arrendamientos o «rent expense» del 10-K)")
            continue
        sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
        sh = gc.open_by_key(sid)
        rng = [f"'{OL}'!E5", f"'{OL}'!B8:B13", f"'{IS}'!B18", f"'{IS}'!B28", f"'{IS}'!B30", f"'{IS}'!B32", f"'{IS}'!B33",
               f"'{VO}'!C45", f"'{VO}'!C47"]
        cur = sh.values_batch_get(rng, params={"valueRenderOption": "FORMULA"})["valueRanges"]
        val = lambda i: (cur[i].get("values") or [[None]])[0][0]  # noqa: E731
        old_ol = [val(0)] + [r[0] if r else None for r in (cur[1].get("values") or [])]
        conv = [(OL, "E5", round(d["gasto"], 1)), (OL, "B8", d["y1"]), (OL, "B9", d["y2"]), (OL, "B10", d["y3"]), (OL, "B11", d["y4"]),
                (OL, "B12", d["y5"]), (OL, "B13", d["resto"]), (IS, "B18", "Yes")]
        if dry:
            print(tk, d)
            continue
        cambios = [{"hoja": h, "celda": c, "antes": (old_ol[["E5", "B8", "B9", "B10", "B11", "B12", "B13"].index(c)] if h == OL else val(2)),
                    "despues": v, "motivo": f"Conversor de arrendamientos (Damodaran): gasto y compromisos del 10-K al {d['cierre']} (SEC XBRL)."}
                   for h, c, v in conv]
        sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": [{"range": f"'{h}'!{c}", "values": [[v]]} for h, c, v in conv]})
        time.sleep(2)
        o = sh.values_batch_get([f"'{OL}'!C29", f"'{OL}'!F33", f"'{IS}'!B12"], params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
        pv, adj, rev = (x["values"][0][0] for x in o)
        delta, k = adj / rev, pv / rev
        segundo = []
        for i, (h, c, s2c) in enumerate(((IS, "B28", False), (IS, "B30", False), (IS, "B32", True), (IS, "B33", True),
                                         (VO, "C45", False), (VO, "C47", False)), start=3):
            old = val(i)
            new = ajusta(old, delta, s2c, k)
            if new is None:
                continue
            why = (f"Ventas/capital con el capital arrendado: 1/(1/{old} + {round(k, 4)}), con VP de arrendamientos {round(pv, 1)} / ventas {round(rev, 1)}."
                   if s2c else f"Margen en base ajustada por arrendamientos: + {round(delta * 100, 2)} pp (ajuste del EBIT {round(adj, 1)} / ventas {round(rev, 1)}).")
            segundo.append((h, c, new))
            cambios.append({"hoja": h, "celda": c, "antes": old, "despues": new, "motivo": why})
        if segundo:
            sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": [{"range": f"'{h}'!{c}", "values": [[v]]} for h, c, v in segundo]})
        bk = {"ticker": f"{tk}_LEASECONV", "sheet_id": sid, "fecha": "2026-10-01", "cambios": cambios,
              "vp_arrendamientos": pv, "ajuste_ebit": adj, "ventas": rev, "margen_pp": delta, "capital_ventas": k, "datos_sec": d}
        (OUT / f"{tk}_LEASECONV.json").write_text(json.dumps(bk, ensure_ascii=False, indent=1))
        for c in cambios:
            try:
                sh.worksheet(c["hoja"]).insert_note(c["celda"], f"Revisión 1-oct-2026: antes {c['antes']}, ahora {c['despues']}. {c['motivo']}")
            except Exception:  # noqa: BLE001
                time.sleep(20)
            time.sleep(0.5)
        spec_p = REF / f"{tk}.json"
        spec = json.loads(spec_p.read_text())
        spec["arrendamientos"] = {"vp": pv, "ajuste_ebit": adj, "margen_pp": delta, "capital_ventas": k, "cierre": d["cierre"],
                                  "criterio": "Damodaran: arrendamientos operativos como deuda; EBIT + gasto − depreciación del activo"}
        spec_p.write_text(json.dumps(spec, ensure_ascii=False, indent=1))
        print(f"{tk}: VP arrendamientos {pv:,.1f} · ajuste EBIT {adj:,.1f} (+{delta * 100:.2f} pp) · capital/ventas +{k:.3f} · {len(cambios)} celdas", flush=True)
        time.sleep(4)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
