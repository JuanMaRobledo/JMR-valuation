#!/usr/bin/env python
"""Beta bottom-up para toda la cartera (prompt de valoración v4, paso 2), 3-oct-2026.

Regla única:
  beta = beta desapalancada del sector de Damodaran (Betas by Sector US, ene-2026, corregida por caja)
         reapalancada con la D/E de mercado de la hoja (incluidos los arrendamientos capitalizados)
         + primas explícitas solo por riesgos propios que el prompt nombra:
             +0,10 una sola categoría o concepto (o distribuidor concentrado)
             +0,15 moda
             +0,15 empresa pequeña (capitalización < US$5.000 millones)
  La beta de regresión queda como referencia. El riesgo país va en la prima de mercado, no en la beta.
  Excepciones documentadas en la ficha de historias (reference/damodaran/<T>.json):
    - financieras y redes de pagos (PAGS, PYPL): la beta desapalancada de Financial Services no sirve; se parte de la
      beta del patrimonio del sector (0,97);
    - GOOG: mezcla de sectores por ingresos (Advertising + Software), 1,07;
    - CELH: 1,0 por categoría única y distribuidor que concentra >50% de las ventas.
  Las hojas con «Single Business(Global)» ya calculan la beta bottom-up del sector global y no se cambian.

Escribe 'Cost of capital worksheet'!B23 (con B22 = "Direct Input"), deja respaldo y nota en la celda y actualiza el
texto de riesgo de la ficha de historias. Después hay que regenerar cada empresa (damodaran_stories, build_story_sheet,
ancla C de múltiplos y regenerar_cartera.sh).

Uso: PYTHONPATH=.:scripts python scripts/aplicar_beta_bottom_up.py [--apply] [TICKER ...]
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
REF = _ROOT / "reference" / "damodaran"
DATOS = _ROOT.parent / "Modelo-JMR-datos" / "valoraciones"
OUT = _ROOT / "reference" / "revision_dcf_2026-10-03"
CC = "Cost of capital worksheet"

# ticker -> (primas [(motivo, valor)], beta de partida fija o None = bottom-up del sector, comentario)
REGLA = {
    "BSX": ([], None, ""),
    "CMG": ([("un solo concepto de restaurante", 0.10)], None, ""),
    "DPZ": ([("un solo concepto (pizza a domicilio)", 0.10)], None,
            "La D/E alta (recapitalización con deuda) explica que la beta reapalancada supere a la del sector."),
    "EPAM": ([], None, "El riesgo de la entrega desde Europa del Este va en la prima de mercado ponderada por operaciones, no en la beta."),
    "INTU": ([], None, ""),
    # 5-oct-2026 (scripts/revisar_beta_s2c.py): sin prima por moda, que ya está en las historias; la hoja usa
    # «Single Business(US)» y reapalanca sola la beta del sector corregida por caja.
    "LULU": ([], None, ""),
    "ONON": ([], None, ""),
    "PAGS": ([("empresa pequeña", 0.15)], 0.97,
             "Banco digital: se parte de la beta del patrimonio del sector financiero (0,97), no de la desapalancada; "
             "el riesgo de Brasil va en la prima de mercado."),
    "PYPL": ([], 0.97, "Red de pagos con saldos de clientes y crédito: se parte de la beta del patrimonio del sector (0,97)."),
    "ZTS": ([], None, ""),
    "NVDA": ([], None, ""),
    "PLTR": ([], None, ""),
    "SHAK": ([("un solo concepto", 0.10), ("empresa pequeña", 0.15)], None,
             "Se fijó 1,25 el 3-oct-2026 (la regla da 1,23; la diferencia cubre los márgenes finos)."),
}
FIJA = {"SHAK": 1.25}  # ya aplicada y regenerada


def es(x, nd=2):
    return f"{x:.{nd}f}".replace(".", ",")


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    pedidos = [a for a in argv if not a.startswith("--")] or list(REGLA)
    betas = json.loads((REF / "betas_us_2026-01.json").read_text())["industrias"]
    gc = get_gspread_client()
    OUT.mkdir(parents=True, exist_ok=True)
    resumen = {}
    for tk in pedidos:
        primas, fija, extra = REGLA[tk]
        sid = re.search(r"/d/([^/]+)", json.loads(next(DATOS.glob(f"{tk}-*.json")).read_text())["hojaGoogle"]).group(1)
        sh = gc.open_by_key(sid)
        r = sh.values_batch_get([f"'Input sheet'!B10", f"'Input sheet'!B25", f"'{CC}'!B22:B23", f"'{CC}'!B61:C61"],
                                params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
        ind, tax = r[0]["values"][0][0], r[1]["values"][0][0]
        enfoque, antes = r[2]["values"][0][0], r[2]["values"][1][0]
        e, d = r[3]["values"][0]
        u = betas[ind]["Unlevered beta corrected for cash"]
        bu = u * (1 + (1 - tax) * d / e)
        partida = fija if fija is not None else bu
        nueva = FIJA.get(tk, round(partida + sum(p for _, p in primas), 2))
        prim_txt = "".join(f" + {es(p)} por {m}" for m, p in primas)
        base_txt = (f"beta del patrimonio del sector ({es(fija)})" if fija is not None else
                    f"bottom-up de {ind} (Damodaran, ene-2026: {es(u)} desapalancada y corregida por caja) reapalancada con la "
                    f"D/E de mercado {es(d / e)} = {es(bu)}")
        motivo = (f"Beta de la cartera (prompt v4, paso 2): {base_txt}{prim_txt} = {es(nueva)}. La de regresión queda como "
                  f"referencia. {extra}").strip()
        resumen[tk] = {"sheet_id": sid, "industria": ind, "enfoque_antes": enfoque, "antes": antes, "despues": nueva,
                       "sector_u": u, "bottom_up": bu, "primas": primas, "motivo": motivo}
        print(f"{tk:5s} {ind:40s} {antes} -> {nueva}  (bottom-up {bu:.2f}{prim_txt})", flush=True)
        if apply and (abs(float(antes) - nueva) > 1e-9 or str(enfoque).lower() != "direct input"):
            sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": [
                {"range": f"'{CC}'!B22", "values": [["Direct Input"]]}, {"range": f"'{CC}'!B23", "values": [[nueva]]}]})
            sh.worksheet(CC).insert_note("B23", f"Revisión {dt.date.today():%d-%b-%Y}: antes {antes}, ahora {es(nueva)}. {motivo}")
            spec_p = REF / f"{tk}.json"
            spec = json.loads(spec_p.read_text())
            spec.setdefault("riesgo", {})
            spec["riesgo"]["texto"] = (f"La hoja usa una beta de {es(nueva)} (desde el 3-oct-2026; antes {es(float(antes))}). "
                                       + motivo.replace("Beta de la cartera (prompt v4, paso 2): ", "Regla de la cartera (prompt v4, paso 2): ")
                                       + " El efecto de cada beta en el DCF Base está en la tabla.")
            if spec["riesgo"].get("beta_propuesta") is not None:
                spec["riesgo"]["beta_propuesta"] = None
            spec_p.write_text(json.dumps(spec, ensure_ascii=False, indent=1))
            resumen[tk]["aplicada"] = True
        time.sleep(6)
    if apply:
        (OUT / "betas_cartera.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
