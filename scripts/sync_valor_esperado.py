"""Lleva el valor esperado de las historias (reference/damodaran/<T>_resultado.json, damodaran_stories.py) a la
valoración guardada (Modelo-JMR-datos/valoraciones/<T>-*.json, campo valorEsperado) y a la copia vinculada del
análisis fundamental (analisis/<T>-research-*.json, linkedValuation.valorEsperado). La app lo muestra junto al DCF.

Valor esperado = suma de probabilidad × valor por acción de cada historia; cada historia es un DCF completo con los
insumos de la hoja (misma tasa de descuento, beta de la hoja) y su propio crecimiento, margen, reinversión y ROIC
después del año 10.

Uso: python scripts/sync_valor_esperado.py ../Modelo-JMR-datos [TICKER ...]
"""
from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

REF = Path(__file__).resolve().parents[1] / "reference" / "damodaran"


def valor_esperado(r: dict) -> dict:
    return {
        "fecha": r.get("fecha"),
        "valor": r["valor_esperado_beta_hoja"],
        "valorBetaPropuesta": r.get("valor_esperado_beta_prop"),
        "betaHoja": r.get("beta_hoja"), "betaPropuesta": r.get("beta_prop"),
        "dcfBase": r.get("dcf_base"),
        "metodo": "Promedio de las historias ponderado por probabilidad; cada historia es un DCF completo con los insumos "
                  "de la hoja y la misma tasa de descuento (sección «Valor con criterio Damodaran»).",
        "historias": [{"nombre": h["nombre"], "probabilidad": h["prob"], "valor": h["valor_beta_hoja"],
                       "valorBetaPropuesta": h.get("valor_beta_prop"), "margen": h.get("margen"), "crecimiento": h.get("cagr"),
                       "roicTerminal": "costo_capital" if h.get("roic_terminal") == "costo_capital" else "hoja"}
                      for h in r["historias"]],
    }


def main(argv: list[str]) -> int:
    datos = Path(argv[0])
    tickers = argv[1:] or sorted(p.name.split("_")[0] for p in REF.glob("*_resultado.json"))
    for t in tickers:
        r = json.loads((REF / f"{t}_resultado.json").read_text())
        ve = valor_esperado(r)
        for pat, key in ((f"valoraciones/{t}-*.json", None), (f"analisis/{t}-research-*.json", "linkedValuation")):
            for f in glob.glob(str(datos / pat)):
                rec = json.loads(Path(f).read_text())
                tgt = rec.get(key) if key else rec
                if key and not isinstance(tgt, dict):
                    continue
                tgt["valorEsperado"] = ve
                Path(f).write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n")
        print(f"{t:5s} valor esperado {ve['valor']:.2f} (DCF {ve['dcfBase']:.2f})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
