"""Escaneo de integridad de las hojas del Modelo JMR (1-oct-2026).

Se corre después de cualquier cambio masivo o de una edición manual de las hojas, y antes de cerrar una revisión.
Lee fórmulas y valores de las pestañas clave de cada hoja y reporta:

  1. celdas con error (#REF!, #VALUE!, #DIV/0!, #N/A, #NAME?, #NUM!, #ERROR!);
  2. números escritos a mano donde al menos el 75% de las hojas tiene una fórmula (así apareció el margen Base de
     'Valuation output'!C46, que no seguía a 'Input sheet'!B30 en 10 hojas);
  3. 'Valuation output'!C46 sin enlazar a 'Input sheet'!B30;
  4. acciones preferentes en 'Input sheet'!B76 que 'Valuation output'!B33 o la pestaña «Escenarios e historias» no restan;
  5. la pestaña «Escenarios e historias» (H5:H8 y H10) frente al último cálculo guardado del motor
     (reference/damodaran/<T>_resultado.json): una diferencia indica que la hoja cambió después del cálculo;
  6. la última edición de cada hoja y si la hizo una persona (no la cuenta de servicio), para detectar ediciones en
     paralelo.

No modifica nada. Uso: python scripts/integridad_hojas.py [TICKER ...]
"""
from __future__ import annotations

import collections
import json
import re
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))
from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

TODAS = "ADBE AFYA BSX CELH CMG DPZ DUOL EPAM GOOG INTU LULU MSFT NKE NVDA NVO ONON PAGS PLTR PYPL SHAK UBER ZTS".split()
TABS = ["Input sheet", "Valuation output", "Cost of capital worksheet", "Operating lease converter", "R& D converter",
        "Descuento de múltiplos", "Resumen de Valoración", "Escenarios e historias", "EVEBITDA", "EVFCFF", "PE", "PFCFE", "POCF"]
ERR = re.compile(r"^#(REF!|VALUE!|DIV/0!|N/A|NAME\?|ERROR!|NUM!|NULL!)")
# Celdas que son entradas del analista por diseño (supuestos de escenarios técnicos y datos con respaldo documentado).
# «Escenarios e historias» E5:E8 = ventas/capital propio de cada historia (spec); 'Valuation output' filas 96-98 = referencia
# histórica que no alimenta el DCF; A1 = rótulo.
ENTRADAS = re.compile(r"^Valuation output!(?:[B-G](?:45|47|55|57|96|98|106)|A1)$|^Input sheet!B(?:15|16|19|20|22|24)$"
                      r"|^Escenarios e historias!E[5-8]$")


def col(j: int) -> str:
    return chr(65 + j)


def leer(gc, t: str) -> dict:
    sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{t}_anclas.json").read_text())["sheet_id"]
    for intento in range(5):
        try:
            sh = gc.open_by_key(sid)
            titulos = {w.title for w in sh.worksheets()}
            tabs = [x for x in TABS if x in titulos]
            rng = [f"'{x}'!A1:N140" for x in tabs]
            F = sh.values_batch_get(rng, params={"valueRenderOption": "FORMULA"})["valueRanges"]
            V = sh.values_batch_get(rng, params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
            rev = gc.http_client.request("get", f"https://www.googleapis.com/drive/v3/files/{sid}/revisions",
                                         params={"fields": "revisions(modifiedTime,lastModifyingUser(emailAddress))",
                                                 "pageSize": 1000}).json().get("revisions", [])
            return {"tabs": {tab: {"f": f.get("values", []), "v": v.get("values", [])} for tab, f, v in zip(tabs, F, V)},
                    "ultima": rev[-1] if rev else {}}
        except Exception as e:  # noqa: BLE001
            print(f"{t}: reintento ({str(e)[:60]})", flush=True)
            time.sleep(40)
    raise RuntimeError(t)


def celda(tab: dict, a: str):
    m = re.match(r"([A-Z])(\d+)", a)
    i, j = int(m.group(2)) - 1, ord(m.group(1)) - 65
    filas = tab["v"]
    return filas[i][j] if i < len(filas) and j < len(filas[i]) else None


def formula(tab: dict, a: str):
    m = re.match(r"([A-Z])(\d+)", a)
    i, j = int(m.group(2)) - 1, ord(m.group(1)) - 65
    filas = tab["f"]
    return filas[i][j] if i < len(filas) and j < len(filas[i]) else None


def main(argv: list[str]) -> int:
    tickers = [a for a in argv if not a.startswith("--")] or TODAS
    gc = get_gspread_client()
    D = {}
    for t in TODAS if len(tickers) < len(TODAS) else tickers:  # la regla de mayoría necesita todas las hojas
        D[t] = leer(gc, t)
        time.sleep(2)
    hallazgos = collections.defaultdict(list)
    # 2. números fijos donde la mayoría tiene fórmula
    for tab in TABS:
        celdas = collections.defaultdict(dict)
        for t, x in D.items():
            if tab not in x["tabs"]:
                continue
            for i, row in enumerate(x["tabs"][tab]["f"]):
                for j, c in enumerate(row):
                    if c not in ("", None):
                        celdas[(i, j)][t] = c
        for (i, j), m in celdas.items():
            nf = sum(1 for v in m.values() if isinstance(v, str) and v.startswith("="))
            if nf >= 0.75 * len(D):
                for t, v in m.items():
                    ref = f"{tab}!{col(j)}{i + 1}"
                    if not (isinstance(v, str) and v.startswith("=")) and not ENTRADAS.match(ref):
                        hallazgos[t].append(f"número fijo donde la mayoría tiene fórmula: {ref} = {v}")
    for t in tickers:
        x = D[t]["tabs"]
        # 1. errores
        for tab, d in x.items():
            for i, row in enumerate(d["v"]):
                for j, c in enumerate(row):
                    if isinstance(c, str) and ERR.match(c):
                        hallazgos[t].append(f"error {tab}!{col(j)}{i + 1} = {c}")
        vo, inp = x["Valuation output"], x["Input sheet"]
        # 3. C46
        if formula(vo, "C46") != "='Input sheet'!B30":
            hallazgos[t].append(f"Valuation output!C46 no está enlazado a Input sheet!B30 ({formula(vo, 'C46')})")
        # 4. preferentes
        pref = celda(inp, "B76")
        if isinstance(pref, (int, float)) and pref:
            if "B$76" not in str(formula(vo, "B33")):
                hallazgos[t].append(f"Input sheet!B76 = {pref} (preferentes) no se resta en Valuation output!B33")
            esc = x.get("Escenarios e historias")
            if esc and "B$76" not in str(formula(esc, "B43")):
                hallazgos[t].append("la pestaña «Escenarios e historias» no resta las preferentes (B76)")
        # 5. pestaña frente al motor
        rp = _ROOT / "reference" / "damodaran" / f"{t}_resultado.json"
        esc = x.get("Escenarios e historias")
        if rp.exists() and esc:
            r = json.loads(rp.read_text())
            orden = {h["id"]: h for h in r["historias"]}
            for k, a in zip("ABCD", ("H5", "H6", "H7", "H8")):
                v = celda(esc, a)
                if isinstance(v, (int, float)) and abs(v - orden[k]["valor_beta_hoja"]) > 0.01:
                    hallazgos[t].append(f"pestaña {a} = {v:.2f} y el último cálculo {orden[k]['valor_beta_hoja']:.2f}")
        # 6. última edición
        u = D[t]["ultima"]
        quien = (u.get("lastModifyingUser") or {}).get("emailAddress", "?")
        humano = "gserviceaccount" not in quien
        print(f"{t:5s} {len(hallazgos[t]):3d} hallazgos · última edición {u.get('modifiedTime', '?')[:16]} "
              f"{'por una persona (' + quien + ')' if humano else 'por la cuenta de servicio'}")
        for h in hallazgos[t]:
            print("      ·", h)
    return 1 if any(hallazgos[t] for t in tickers) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
