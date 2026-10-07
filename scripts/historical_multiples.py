"""Múltiplos históricos normalizados como lectura independiente del Modelo JMR.

No modifica DCF, historias, múltiplos de salida vigentes ni ponderaciones. Usa la
historia ya depurada en reference/multiplos_v3/<T>_anclas.json, excluye LTM de
las estadísticas históricas y respeta los outliers/exclusiones ya documentados.

Genera:
  reference/historical_multiples/<T>.json
Opcionalmente:
  --write-sheet  crea/actualiza la pestaña "Múltiplos históricos" en la hoja.
  --patch-app    añade el campo multiplesHistoricos a la valoración/research guardados.

Uso:
  python scripts/historical_multiples.py SHAK --write-sheet --patch-app
"""
from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import statistics as st
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

METHODS = {
    "EV/EBITDA": {"metric": "G57", "kind": "ev"},
    "EV/FCFF": {"metric": "G63", "kind": "ev"},
    "P/E": {"metric": "G54", "kind": "equity"},
    "P/FCFE": {"metric": "G68", "kind": "equity"},
    "P/OCF": {"metric": "G65", "kind": "equity"},
}
STAT_KEYS = ("min", "p25", "mediana_5a", "promedio_5a", "mediana_10a")
STAT_LABELS = {
    "min": "Mínimo histórico válido",
    "p25": "Percentil 25",
    "mediana_5a": "Mediana 5 años",
    "promedio_5a": "Promedio 5 años",
    "mediana_10a": "Mediana histórica depurada",
}


def _pct(values: list[float], q: float) -> float | None:
    v = sorted(values)
    if not v:
        return None
    k = (len(v) - 1) * q
    f, c = int(k), min(int(k) + 1, len(v) - 1)
    return v[f] + (v[c] - v[f]) * (k - f)


def _n(v):
    return float(v) if isinstance(v, (int, float)) else None


def _annual_kept(hist: dict) -> list[tuple[str, float]]:
    excluded = {str(x[0]) for x in hist.get("excluidos", []) if x}
    out = []
    for lab, val in (hist.get("serie") or {}).items():
        if lab in excluded or str(lab).strip().upper() == "LTM":
            continue
        if not isinstance(val, (int, float)) or val <= 0.5:
            continue
        out.append((str(lab), float(val)))
    return out


def _stats(hist: dict) -> dict:
    kept = _annual_kept(hist)
    vals = [v for _, v in kept]
    if not vals:
        return {"n": 0}
    last5 = vals[-5:]
    return {
        "n": len(vals),
        "periodos_validos": [lab for lab, _ in kept],
        "min": min(vals),
        "p25": _pct(vals, 0.25),
        "mediana_5a": st.median(last5),
        "promedio_5a": st.mean(last5),
        "mediana_10a": st.median(vals),
        "max": max(vals),
    }


def _cell(sh, a1: str):
    return sh.values_get(a1, params={"valueRenderOption": "UNFORMATTED_VALUE"}).get("values", [[None]])[0][0]


def build(ticker: str, sheet_id: str | None = None) -> dict:
    ticker = ticker.upper()
    ap = _ROOT / "reference" / "multiplos_v3" / f"{ticker}_anclas.json"
    if not ap.exists():
        raise FileNotFoundError(f"No existe {ap}")
    anchors = json.loads(ap.read_text())
    sheet_id = sheet_id or anchors["sheet_id"]
    sh = get_gspread_client().open_by_key(sheet_id)

    ranges = [
        "'Input sheet'!D1", "'Input sheet'!B23",
        "'Income Statement'!L22", "'Income Statement'!L27", "'Income Statement'!L28",
        "'Cash Flow Statement'!L13",
        "'Balance Sheet'!L5", "'Balance Sheet'!L25", "'Balance Sheet'!L26",
        "'Input sheet'!B16", "'Input sheet'!B19", "'Input sheet'!B20", "'Input sheet'!B21",
        "'Operating lease converter'!C30",
        "'Financials Multiples'!G54", "'Financials Multiples'!G57",
        "'Financials Multiples'!G63", "'Financials Multiples'!G65",
        "'Financials Multiples'!G68", "'Financials Multiples'!G70",
        "'Financials Multiples'!E74:G74",
        "'Descuento de múltiplos'!B5",
        "'Resumen de Valoración'!A7:B11",
    ]
    vr = sh.values_batch_get(ranges, params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
    one = lambda i: (vr[i].get("values") or [[None]])[0][0]

    price_now = _n(one(0))
    price_analysis = _n(one(1))
    net_income_ltm = _n(one(2))
    shares_ltm = _n(one(3))
    ebitda_ltm = _n(one(4))
    ocf_ltm = _n(one(5))
    cash_book = _n(one(6)) or 0.0
    debt_book = _n(one(7)) or 0.0
    leases_book = _n(one(8)) or 0.0
    debt_model = _n(one(9)) or 0.0
    cash_model = _n(one(10)) or 0.0
    nonop = _n(one(11)) or 0.0
    minority = _n(one(12)) or 0.0
    leases_model = _n(one(13)) or 0.0
    fy3 = {
        "P/E": _n(one(14)), "EV/EBITDA": _n(one(15)), "EV/FCFF": _n(one(16)),
        "P/OCF": _n(one(17)), "P/FCFE": _n(one(18)),
    }
    shares_fy3 = _n(one(19))
    dps = ((vr[20].get("values") or [[]])[0] + [0, 0, 0])[:3]
    dps = [float(x) if isinstance(x, (int, float)) else 0.0 for x in dps]
    ke = _n(one(21))
    weight_rows = vr[22].get("values") or []
    weights = {str(r[0]).strip(): float(r[1]) for r in weight_rows if len(r) > 1 and isinstance(r[1], (int, float))}

    current = {}
    if price_now and shares_ltm:
        if ebitda_ltm and ebitda_ltm > 0:
            ev_now = price_now * shares_ltm + debt_book + leases_book - cash_book
            current["EV/EBITDA"] = ev_now / ebitda_ltm
        if net_income_ltm and net_income_ltm > 0:
            current["P/E"] = price_now / (net_income_ltm / shares_ltm)
        if ocf_ltm and ocf_ltm > 0:
            current["P/OCF"] = price_now / (ocf_ltm / shares_ltm)

    net_debt_model = debt_model + leases_model - cash_model - nonop + minority
    pv_div = sum(dps[t - 1] / ((1 + ke) ** t) for t in (1, 2, 3)) if ke is not None else 0.0
    cum_div = sum(dps)

    methods = []
    for name, cfg in METHODS.items():
        a = (anchors.get("metodos") or {}).get(name) or {}
        hist = a.get("historia") or {}
        stats = _stats(hist)
        w = float(weights.get(name, 0.0))
        metric = fy3.get(name)
        applies = bool(w > 0 and stats.get("n", 0) >= 3 and metric and metric > 0 and shares_fy3 and ke is not None)
        prices = {}
        if applies:
            for key in STAT_KEYS:
                mult = stats.get(key)
                if not isinstance(mult, (int, float)):
                    continue
                if cfg["kind"] == "ev":
                    p3 = (mult * metric - net_debt_model) / shares_fy3
                else:
                    p3 = mult * metric / shares_fy3
                nominal = p3 + cum_div
                vp = p3 / ((1 + ke) ** 3) + pv_div
                prices[key] = {"multiplo": mult, "fy3": nominal, "vp": vp}
        cur = current.get(name)
        med = stats.get("mediana_10a")
        percentile = None
        vals = [v for _, v in _annual_kept(hist)]
        if cur is not None and vals:
            percentile = sum(v <= cur for v in vals) / len(vals)
        methods.append({
            "nombre": name,
            "aplica": applies,
            "peso_original": w,
            "actual": cur,
            "estadisticas": stats,
            "descuento_vs_mediana": (cur / med - 1) if cur is not None and med else None,
            "percentil_actual": percentile,
            "precios": prices,
            "excluidos": hist.get("excluidos", []),
        })

    applicable = [m for m in methods if m["aplica"]]
    wsum = sum(m["peso_original"] for m in applicable)
    rel_weights = {m["nombre"]: (m["peso_original"] / wsum if wsum else 0.0) for m in applicable}
    consolidated = {}
    for key in STAT_KEYS:
        vals = [(rel_weights[m["nombre"]], m["precios"].get(key, {}).get("vp")) for m in applicable]
        vals = [(w, v) for w, v in vals if isinstance(v, (int, float))]
        consolidated[key] = sum(w * v for w, v in vals) / sum(w for w, _ in vals) if vals and sum(w for w, _ in vals) else None

    out = {
        "version": 1,
        "ticker": ticker,
        "fecha": dt.date.today().isoformat(),
        "sheet_id": sheet_id,
        "independiente": True,
        "afecta_dcf": False,
        "afecta_ponderado": False,
        "precio_actual": price_now,
        "precio_analisis": price_analysis,
        "ke": ke,
        "regla": {
            "historia": "Solo cierres fiscales positivos y válidos; LTM se excluye de las estadísticas históricas. Se respetan las exclusiones/outliers documentados por multiples_anchors.py.",
            "estadisticas": "Mínimo válido, P25, mediana 5A, promedio 5A y mediana histórica depurada.",
            "valoracion": "Cada ancla histórica se aplica a la métrica Base de FY+3 y luego se trae a valor presente con Ke. No entra al DCF ni al ponderado principal.",
        },
        "pesos_relativos": rel_weights,
        "metodos": methods,
        "consolidado_vp": consolidated,
        "nota": "Barato frente a su propia historia no equivale a infravalorado intrínsecamente. Esta capa es una lectura histórica independiente.",
    }
    return out


def write_sheet(out: dict) -> None:
    sh = get_gspread_client().open_by_key(out["sheet_id"])
    title = "Múltiplos históricos"
    try:
        ws = sh.worksheet(title)
        ws.clear()
    except Exception:
        ws = sh.add_worksheet(title=title, rows=80, cols=14)
    hdr = [
        ["MÚLTIPLOS HISTÓRICOS NORMALIZADOS — lectura independiente"],
        ["No modifica DCF, historias, múltiplos vigentes ni ponderaciones. Barato vs historia ≠ infravalorado intrínsecamente."],
        [],
        ["Método", "Actual", "Mínimo válido", "P25", "Mediana 5A", "Promedio 5A", "Mediana histórica", "Actual vs mediana", "Percentil actual", "N válido"],
    ]
    rows = list(hdr)
    for m in out["metodos"]:
        if not m["estadisticas"].get("n"):
            continue
        s = m["estadisticas"]
        rows.append([
            m["nombre"], m["actual"], s.get("min"), s.get("p25"), s.get("mediana_5a"), s.get("promedio_5a"),
            s.get("mediana_10a"), m.get("descuento_vs_mediana"), m.get("percentil_actual"), s.get("n"),
        ])
    rows += [
        [],
        ["VALOR PRESENTE IMPLÍCITO CON LA HISTORIA — secundario, NO ponderado principal"],
        ["Ancla", "Consolidado VP hoy"],
    ]
    for k in STAT_KEYS:
        rows.append([STAT_LABELS[k], out["consolidado_vp"].get(k)])
    rows += [[], ["Detalle por método"], ["Método", "Ancla", "Múltiplo", "FY+3", "VP hoy", "Peso relativo"]]
    for m in out["metodos"]:
        if not m["aplica"]:
            continue
        for k in STAT_KEYS:
            p = m["precios"].get(k)
            if p:
                rows.append([m["nombre"], STAT_LABELS[k], p["multiplo"], p["fy3"], p["vp"], out["pesos_relativos"].get(m["nombre"])])
    ws.update(range_name="A1", values=rows, value_input_option="USER_ENTERED")
    try:
        ws.freeze(rows=4)
        ws.format("A1:J1", {"textFormat": {"bold": True, "fontSize": 14}})
        ws.format("A4:J4", {"textFormat": {"bold": True}})
        ws.format("B5:I40", {"numberFormat": {"type": "NUMBER", "pattern": "0.00"}})
        ws.format("H5:I40", {"numberFormat": {"type": "PERCENT", "pattern": "0.0%"}})
    except Exception:
        pass


def patch_app(out: dict) -> None:
    data_root = _ROOT.parent / "Modelo-JMR-datos"
    vals = [p for p in glob.glob(str(data_root / "valoraciones" / f"{out['ticker']}-*.json")) if "regen" not in p]
    if vals:
        p = Path(vals[0])
        d = json.loads(p.read_text())
        d["multiplesHistoricos"] = out
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    for pth in glob.glob(str(data_root / "analisis" / f"{out['ticker']}-research-*.json")):
        p = Path(pth)
        d = json.loads(p.read_text())
        d["multiplesHistoricos"] = out
        if isinstance(d.get("linkedValuation"), dict):
            d["linkedValuation"]["multiplesHistoricos"] = out
        if isinstance(d.get("linkedValuationAtResearch"), dict):
            d["linkedValuationAtResearch"]["multiplesHistoricos"] = out
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("ticker")
    ap.add_argument("--sheet-id")
    ap.add_argument("--write-sheet", action="store_true")
    ap.add_argument("--patch-app", action="store_true")
    args = ap.parse_args(argv)
    out = build(args.ticker, args.sheet_id)
    dst = _ROOT / "reference" / "historical_multiples" / f"{args.ticker.upper()}.json"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    if args.write_sheet:
        write_sheet(out)
    if args.patch_app:
        patch_app(out)
    print(args.ticker.upper(), "múltiplos históricos:", out["consolidado_vp"], "->", dst)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
