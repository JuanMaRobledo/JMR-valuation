#!/usr/bin/env python
"""Datos de mercado más recientes para un corte de la cartera (Damodaran), 6-oct-2026.

Regla: la tasa libre de riesgo y la prima de mercado tienen que ser de la MISMA fecha. Damodaran publica cada mes la prima
implícita calculada con el Treasury a 10 años y los precios del último día hábil del mes anterior (ERP<Mes><AA>.xlsx). Por
eso el corte por defecto es ese día: el último cierre de mes con prima publicada.

Busca y verifica:
  - la prima implícita más reciente (fila «Implied Equity Risk Premium (with US treasury rate as riskfree rate)») y la tasa
    con la que se calculó;
  - el Treasury a 10 años del corte (FRED DGS10), que debe coincidir con la del archivo de Damodaran;
  - el cierre sin ajustar de cada empresa en el corte (Yahoo Finance, «Close» con auto_adjust=False).
Escribe reference/corte_vigente.json (lo leen aplicar_corte.py, textos_tasa_s2c.py, damodaran_stories.py y
regenerar_cartera.sh). Con --fecha AAAA-MM-DD se fuerza otro corte (avisa si la prima no es de esa fecha).

Uso: PYTHONPATH=.:scripts python scripts/datos_mercado.py [--fecha AAAA-MM-DD] [--escribir]
"""
from __future__ import annotations

import argparse
import datetime as dt
import io
import json
import sys
from pathlib import Path

import requests

_ROOT = Path(__file__).resolve().parents[1]
OUT = _ROOT / "reference" / "corte_vigente.json"
H = {"User-Agent": "JMR Valuation juan0804@gmail.com"}
MESES = {1: ["Jan"], 2: ["Feb"], 3: ["Mar"], 4: ["Apr"], 5: ["May"], 6: ["June", "Jun"], 7: ["July", "Jul"], 8: ["Aug"],
         9: ["Sept", "Sep"], 10: ["Oct"], 11: ["Nov"], 12: ["Dec"]}
MES_ES = ["", "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
          "noviembre", "diciembre"]
ABR_ES = ["", "ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
# Diferencial terminal de Brasil sobre (tasa libre + prima madura): conserva la prima país en perpetuidad.
SPREAD_BRASIL = {"AFYA": 0.0173, "PAGS": 0.0292}


def fecha_es(d: dt.date) -> str:
    return f"{d.day}-{ABR_ES[d.month]}-{d.year}"


def prima_damodaran(hoy: dt.date) -> dict:
    """Prima implícita más reciente publicada (busca hasta 4 meses atrás)."""
    import openpyxl
    y, m = hoy.year, hoy.month
    for _ in range(5):
        for ab in MESES[m]:
            url = f"https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERP{ab}{str(y)[2:]}.xlsx"
            r = requests.get(url, headers=H, timeout=60)
            if r.status_code == 200 and r.content[:2] == b"PK":
                wb = openpyxl.load_workbook(io.BytesIO(r.content), data_only=True, read_only=True)
                ws = wb["Impl premium calculator"]
                for fila in ws.iter_rows(min_row=30, max_row=80):
                    a = str(fila[0].value or "")
                    if a.startswith("Implied Equity Risk Premium (with US treasury rate"):
                        erp = fila[2].value
                        rf = next((c.value for c in fila[4:] if isinstance(c.value, float)), None)
                        return {"erp": round(float(erp), 4), "rf_damodaran": rf, "url": url, "mes": m, "anio": y}
        m, y = (12, y - 1) if m == 1 else (m - 1, y)
    raise SystemExit("No encontré un archivo ERP<Mes><AA>.xlsx de Damodaran en los últimos 5 meses.")


def ultimo_habil_mes_anterior(anio: int, mes: int) -> dt.date:
    d = dt.date(anio, mes, 1) - dt.timedelta(days=1)
    while d.weekday() >= 5:
        d -= dt.timedelta(days=1)
    return d


def dgs10(fecha: dt.date) -> tuple[float, dt.date]:
    txt = requests.get("https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10", headers=H, timeout=60).text
    filas = [l.split(",") for l in txt.strip().splitlines()[1:]]
    val = [(dt.date.fromisoformat(d), float(v)) for d, v in filas if v not in (".", "") and dt.date.fromisoformat(d) <= fecha]
    d, v = val[-1]
    return round(v / 100, 4), d


def cierres(tickers: list[str], fecha: dt.date) -> dict:
    import yfinance as yf
    out = {}
    for t in tickers:
        h = yf.Ticker(t).history(start=fecha - dt.timedelta(days=7), end=fecha + dt.timedelta(days=1), auto_adjust=False)
        h = h[h.index.date <= fecha]
        out[t] = {"cierre": round(float(h["Close"].iloc[-1]), 2), "fecha": str(h.index[-1].date())}
    return out


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fecha")
    ap.add_argument("--escribir", action="store_true")
    a = ap.parse_args(argv)
    hoy = dt.date.today()
    p = prima_damodaran(hoy)
    corte_erp = ultimo_habil_mes_anterior(p["anio"], p["mes"])
    corte = dt.date.fromisoformat(a.fecha) if a.fecha else corte_erp
    rf, rf_fecha = dgs10(corte)
    tks = sorted(json.loads((_ROOT / "reference" / "cartera_drive.json").read_text())["empresas"])
    c = cierres(tks, corte)
    avisos = []
    if corte != corte_erp:
        avisos.append(f"La prima de {MES_ES[p['mes']]} se calculó con la tasa del {corte_erp}, no del {corte}.")
    if p["rf_damodaran"] and abs(p["rf_damodaran"] - rf) > 0.0005:
        avisos.append(f"Tasa de FRED {rf:.4f} distinta de la del archivo de Damodaran {p['rf_damodaran']:.4f}.")
    for t, v in c.items():
        if v["fecha"] != str(corte):
            avisos.append(f"{t}: último cierre disponible {v['fecha']} (no {corte}).")
    d = {"fecha_corte": str(corte), "fecha_corte_es": fecha_es(corte), "rf": rf, "rf_fecha": str(rf_fecha),
         "rf_fuente": "FRED DGS10 (Treasury a 10 años)", "erp_madura": p["erp"],
         "erp_mes": f"{MES_ES[p['mes']]} de {p['anio']}", "erp_mes_corto": f"{ABR_ES[p['mes']]}-{p['anio']}",
         "erp_archivo": p["url"], "erp_rf_damodaran": p["rf_damodaran"],
         "costo_capital_terminal": round(rf + p["erp"], 4),
         "terminal_brasil": {k: round(rf + p["erp"] + s, 4) for k, s in SPREAD_BRASIL.items()},
         "spread_brasil": SPREAD_BRASIL, "cierres": {t: v["cierre"] for t, v in c.items()},
         "obtenido": dt.datetime.now().isoformat(timespec="seconds"), "avisos": avisos}
    print(json.dumps({k: v for k, v in d.items() if k != "cierres"}, ensure_ascii=False, indent=1))
    print("cierres:", d["cierres"])
    if a.escribir:
        OUT.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n")
        print("escrito", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
