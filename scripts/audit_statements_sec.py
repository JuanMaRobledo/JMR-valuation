"""Auditoría de los estados financieros de la hoja contra la SEC (XBRL, companyfacts), 1-oct-2026.

Replica en las demás empresas las correcciones contables verificadas en ADBE (data/ADBE_Auditoria_...):
  - balance de la columna LTM ('Balance Sheet'!L): debe ser el del último 10-Q, no repetir el cierre anual;
  - flujos LTM ('Cash Flow Statement'!L): operación, inversión, financiación y cambio de caja con la identidad
    LTM = ejercicio + acumulado del año − acumulado del año anterior (solo flujos, nunca saldos);
  - EPS básico de los tres últimos ejercicios ('Income Statement'!I23:K23), que el importador copiaba del diluido.

Cada fila se calibra con el último ejercicio (columna K): se busca la etiqueta XBRL (o la suma de etiquetas) que
reproduce el valor de la hoja al cierre fiscal y se aplica la misma definición a la fecha del LTM. Si ninguna
reproduce la hoja, la fila queda «sin calibrar» y no se toca. No modifica supuestos.

Sin --apply solo informa. Con --apply escribe los valores, guarda el respaldo en
reference/auditoria_estados_2026-10-01/<T>.json y deja una nota en cada celda.

Uso: python scripts/audit_statements_sec.py [--apply] [--saldos] TICKER ...
(--saldos también propone saldos calibrados; por defecto solo flujos LTM y EPS básico)
"""
from __future__ import annotations

import datetime as dt
import itertools
import json
import sys
import time
import urllib.request
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))
from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

OUT = _ROOT / "reference" / "auditoria_estados_2026-10-01"
CACHE = Path("/tmp/jmr_sec_facts")
UA = {"User-Agent": "JMR research juan0804@gmail.com"}
CORTE = "2026-09-30"
SALDOS = "--saldos" in sys.argv  # los saldos se corrigieron con una tabla revisada a mano (revise_dcf_inputs, *_BALANCE)

# fila de la hoja -> etiquetas candidatas (se prueban solas y en sumas de hasta tres)
BS = {
    "Cash and Cash Equivalents": ["CashAndCashEquivalentsAtCarryingValue", "Cash", "CashAndDueFromBanks"],
    "Short-Term Investments": ["ShortTermInvestments", "MarketableSecuritiesCurrent", "AvailableForSaleSecuritiesDebtSecuritiesCurrent",
                               "HeldToMaturitySecuritiesCurrent", "OtherShortTermInvestments", "CashCashEquivalentsAndShortTermInvestments"],
    "Total Cash and Cash Equivalents": ["CashAndCashEquivalentsAtCarryingValue", "ShortTermInvestments", "MarketableSecuritiesCurrent",
                                        "AvailableForSaleSecuritiesDebtSecuritiesCurrent", "CashCashEquivalentsAndShortTermInvestments",
                                        "HeldToMaturitySecuritiesCurrent", "OtherShortTermInvestments"],
    "Long-Term Investments": ["LongTermInvestments", "MarketableSecuritiesNoncurrent", "AvailableForSaleSecuritiesDebtSecuritiesNoncurrent",
                              "EquitySecuritiesFvNi", "NonmarketableEquitySecurities", "OtherLongTermInvestments", "HeldToMaturitySecuritiesNoncurrent"],
    "Short-Term Debt": ["LongTermDebtCurrent", "DebtCurrent", "ShortTermBorrowings", "CommercialPaper", "LongTermDebtAndCapitalLeaseObligationsCurrent",
                        "ConvertibleNotesPayableCurrent"],
    "Long-Term Debt": ["LongTermDebtNoncurrent", "LongTermDebtAndCapitalLeaseObligations", "ConvertibleNotesPayable", "LongTermDebt",
                       "ConvertibleLongTermNotesPayable", "SeniorNotes"],
    "Leases": ["OperatingLeaseLiabilityNoncurrent", "FinanceLeaseLiabilityNoncurrent"],
    "Total Assets": ["Assets"],
    "Total Liabilities": ["Liabilities"],
    "Total Common Shareholders' Equity": ["StockholdersEquity"],
    "Total Shareholders' Equity": ["StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
}
CF = {
    "Cash from Operating Activities": ["NetCashProvidedByUsedInOperatingActivities"],
    "Cash from Investing Activities": ["NetCashProvidedByUsedInInvestingActivities"],
    "Cash from Financing Activities": ["NetCashProvidedByUsedInFinancingActivities"],
    "Net Change in Cash": ["CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect",
                           "CashAndCashEquivalentsPeriodIncreaseDecrease",
                           "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseExcludingExchangeRateEffect"],
}


def facts(tk: str, cik: int) -> dict:
    CACHE.mkdir(exist_ok=True)
    p = CACHE / f"{tk}.json"
    if not p.exists():
        req = urllib.request.Request(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json", headers=UA)
        p.write_bytes(urllib.request.urlopen(req, timeout=60).read())
        time.sleep(0.3)
    return json.loads(p.read_text())["facts"].get("us-gaap", {})


def cik_map() -> dict:
    p = CACHE / "tickers.json"
    CACHE.mkdir(exist_ok=True)
    if not p.exists():
        req = urllib.request.Request("https://www.sec.gov/files/company_tickers.json", headers=UA)
        p.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    return {v["ticker"]: v["cik_str"] for v in json.loads(p.read_text()).values()}


def units(f: dict, tag: str, unit="USD") -> list:
    return [x for x in (f.get(tag, {}).get("units", {}).get(unit) or []) if x.get("filed", "") <= CORTE]


def instant(f, tag, end):
    v = [x for x in units(f, tag) if x["end"] == end and "start" not in x]
    return (sorted(v, key=lambda x: x["filed"])[-1]["val"] / 1e6) if v else None


def duration(f, tag, start, end, unit="USD", scale=1e6):
    v = [x for x in units(f, tag, unit) if x.get("start") == start and x["end"] == end]
    return (sorted(v, key=lambda x: x["filed"])[-1]["val"] / scale) if v else None


def periods(f):
    """Cierre del último ejercicio (10-K) y del último trimestre (10-Q o 10-K) hasta el corte, desde el patrimonio."""
    eq = units(f, "StockholdersEquity") or units(f, "Assets")
    k = [x for x in eq if x.get("form") == "10-K" and "start" not in x]
    q = [x for x in eq if x.get("form") in ("10-Q", "10-K") and "start" not in x]
    fy_end = max(x["end"] for x in k if x.get("fp") == "FY" and x["end"] == max(y["end"] for y in k if y.get("fp") == "FY"))
    ltm_end = max(x["end"] for x in q)
    return fy_end, ltm_end


def fy_start(f, fy_end):
    for x in units(f, "NetCashProvidedByUsedInOperatingActivities"):
        if x["end"] == fy_end and x.get("start"):
            d = (dt.date.fromisoformat(fy_end) - dt.date.fromisoformat(x["start"])).days
            if 350 < d < 380:
                return x["start"]
    return None


def ytd(f, tag, end, fy_end):
    """Acumulado del ejercicio en curso hasta `end` (inicio = día siguiente al cierre fiscal)."""
    start = (dt.date.fromisoformat(fy_end) + dt.timedelta(days=1)).isoformat()
    cands = [x for x in units(f, tag) if x["end"] == end and x.get("start")]
    best = None
    for x in cands:
        if abs((dt.date.fromisoformat(x["start"]) - dt.date.fromisoformat(start)).days) <= 7:
            best = x["val"] / 1e6
    return best


def prior_ytd(f, tag, end, fy_end):
    """Mismo acumulado un año antes."""
    e = dt.date.fromisoformat(end)
    pend = e.replace(year=e.year - 1)
    pfy = dt.date.fromisoformat(fy_end).replace(year=dt.date.fromisoformat(fy_end).year - 1)
    for de in range(-7, 8):
        v = ytd(f, tag, (pend + dt.timedelta(days=de)).isoformat(), pfy.isoformat())
        if v is not None:
            return v
        for dfy in range(-7, 8):
            v = ytd(f, tag, (pend + dt.timedelta(days=de)).isoformat(), (pfy + dt.timedelta(days=dfy)).isoformat())
            if v is not None:
                return v
    return None


def calibrate(target, fn, tags):
    """Combinación de etiquetas (1 a 3) cuya suma reproduce `target` al cierre fiscal."""
    if target is None or not isinstance(target, (int, float)):
        return None
    vals = {t: fn(t) for t in tags}
    vals = {t: v for t, v in vals.items() if v is not None}
    if abs(target) < 0.05:
        return () if not vals or all(abs(v) < 0.05 for v in vals.values()) else ()
    for n in (1, 2, 3):
        for combo in itertools.combinations(vals, n):
            s = sum(vals[c] for c in combo)
            if abs(s - target) <= max(0.6, abs(target) * 0.003):
                return combo
    return None


def find_row(grid, label):
    for i, r in enumerate(grid):
        if r and str(r[0]).strip() == label:
            return i + 1
    return None


def audit(tk: str, sh, f) -> dict:
    fy_end, ltm_end = periods(f)
    v = sh.values_batch_get(["'Balance Sheet'!A1:L40", "'Cash Flow Statement'!A1:L42", "'Income Statement'!A1:L30"],
                            params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
    bs, cf, inc = (x.get("values", []) for x in v)
    changes, notes = [], []
    same_period = fy_end == ltm_end

    def cellv(grid, r, c):
        row = grid[r - 1] if r - 1 < len(grid) else []
        return row[c] if c < len(row) else None

    for label, tags in (BS.items() if SALDOS else ()):
        r = find_row(bs, label)
        if not r:
            continue
        k, l_ = cellv(bs, r, 10), cellv(bs, r, 11)
        combo = calibrate(k, lambda t: instant(f, t, fy_end), tags)
        if combo is None:
            notes.append(f"Balance «{label}»: sin calibrar (hoja {k} al cierre {fy_end})")
            continue
        new = round(sum(instant(f, t, ltm_end) or 0 for t in combo), 1) if combo else 0.0
        if combo and all(instant(f, t, ltm_end) is None for t in combo):
            notes.append(f"Balance «{label}»: sin dato al {ltm_end}")
            continue
        if not isinstance(l_, (int, float)) or abs(new - l_) > max(0.6, abs(new) * 0.003):
            changes.append({"hoja": "Balance Sheet", "celda": f"L{r}", "fila": label, "antes": l_, "despues": new,
                            "motivo": f"Saldo al {ltm_end} (10-Q): {' + '.join(combo) or 'sin saldo'}. Antes {l_}"
                                      f"{', el cierre anual' if l_ == k and not same_period else ''}."})
    fs = fy_start(f, fy_end)
    for label, tags in CF.items():
        r = find_row(cf, label)
        if not r:
            continue
        k, l_ = cellv(cf, r, 10), cellv(cf, r, 11)
        combo = calibrate(k, lambda t: duration(f, t, fs, fy_end), tags) if fs else None
        if not combo:
            # El cambio de caja del importador suele ser un relleno: se usa la etiqueta más completa disponible.
            combo = next(((t,) for t in tags if duration(f, t, fs, fy_end) is not None), None) if label == "Net Change in Cash" and fs else None
        if not combo:
            notes.append(f"Flujo «{label}»: sin calibrar (hoja {k})")
            continue
        t = combo[0]
        if same_period:
            new = duration(f, t, fs, fy_end)
            how = f"ejercicio cerrado el {fy_end}"
        else:
            a, b, c = duration(f, t, fs, fy_end), ytd(f, t, ltm_end, fy_end), prior_ytd(f, t, ltm_end, fy_end)
            if None in (a, b, c):
                notes.append(f"Flujo «{label}»: falta acumulado ({a}, {b}, {c})")
                continue
            new = a + b - c
            how = f"ejercicio {round(a, 1)} + acumulado al {ltm_end} {round(b, 1)} − acumulado del año anterior {round(c, 1)}"
        new = round(new, 1)
        if not isinstance(l_, (int, float)) or abs(new - l_) > max(0.6, abs(new) * 0.003):
            changes.append({"hoja": "Cash Flow Statement", "celda": f"L{r}", "fila": label, "antes": l_, "despues": new,
                            "motivo": f"LTM = {how} ({t}). Antes {l_}."})
    # EPS básico de los tres últimos ejercicios (I, J, K)
    r = find_row(inc, "Basic EPS")
    if r:
        fys = sorted({x["end"] for x in units(f, "EarningsPerShareBasic", "USD/shares") if x.get("fp") == "FY" and x.get("form") == "10-K"
                      and x["end"] <= fy_end})[-3:]
        for c, end in zip((8, 9, 10), fys):
            vals = [x for x in units(f, "EarningsPerShareBasic", "USD/shares") if x["end"] == end and x.get("start")
                    and 350 < (dt.date.fromisoformat(end) - dt.date.fromisoformat(x["start"])).days < 380]
            if not vals:
                continue
            new = sorted(vals, key=lambda x: x["filed"])[-1]["val"]
            old = cellv(inc, r, c)
            # la hoja puede estar ajustada por splits: solo se corrige si el básico es igual al diluido de la hoja
            dil = cellv(inc, r + 1, c)
            if isinstance(old, (int, float)) and old == dil and abs(new - old) > 0.005:
                ratio = new / old if old else 0
                if 0.97 < ratio < 1.03:
                    changes.append({"hoja": "Income Statement", "celda": f"{'IJK'[c - 8]}{r}", "fila": f"Basic EPS {end}", "antes": old,
                                    "despues": round(new, 2), "motivo": f"EPS básico del 10-K ({end}); antes copiaba el diluido."})
    return {"ticker": tk, "cierre_fiscal": fy_end, "fecha_ltm": ltm_end, "cambios": changes, "notas": notes}


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    tickers = [a for a in argv if not a.startswith("--")]
    gc, cm = get_gspread_client(), cik_map()
    OUT.mkdir(parents=True, exist_ok=True)
    for tk in tickers:
        f = facts(tk, cm[tk])
        if not f:
            print(f"{tk}: sin XBRL us-gaap (emisor extranjero)")
            continue
        sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
        sh = gc.open_by_key(sid)
        res = audit(tk, sh, f)
        print(f"{tk}: cierre {res['cierre_fiscal']} · LTM {res['fecha_ltm']} · {len(res['cambios'])} cambios")
        for c in res["cambios"]:
            print(f"   {c['hoja'][:14]:14s} {c['celda']:4s} {c['fila'][:34]:34s} {c['antes']!s:>12} -> {c['despues']}")
        for n in res["notas"]:
            print("   nota:", n)
        if apply and res["cambios"]:
            bk = OUT / f"{tk}.json"
            if bk.exists():  # el respaldo conserva el estado original
                prev = json.loads(bk.read_text())
                seen = {(c["hoja"], c["celda"]) for c in prev["cambios"]}
                prev["cambios"] += [c for c in res["cambios"] if (c["hoja"], c["celda"]) not in seen]
                prev["notas"] = res["notas"]
                res_bk = prev
            else:
                res_bk = res
            bk.write_text(json.dumps(res_bk, ensure_ascii=False, indent=1))
            sh.values_batch_update({"valueInputOption": "RAW", "data": [
                {"range": f"'{c['hoja']}'!{c['celda']}", "values": [[c["despues"]]]} for c in res["cambios"]]})
            for c in res["cambios"]:
                sh.worksheet(c["hoja"]).insert_note(c["celda"], f"Auditoría 1-oct-2026 (SEC XBRL): {c['motivo']}")
                time.sleep(0.5)
        time.sleep(3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
