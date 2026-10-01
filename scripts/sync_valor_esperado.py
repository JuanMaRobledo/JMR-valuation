"""Lleva el valor esperado de las historias (reference/damodaran/<T>_resultado.json, damodaran_stories.py) a la
valoración guardada (Modelo-JMR-datos/valoraciones/<T>-*.json, campo valorEsperado) y a la copia vinculada del
análisis fundamental (analisis/<T>-research-*.json, linkedValuation.valorEsperado). La app lo muestra junto al DCF.

Valor esperado = suma de probabilidad × valor por acción de cada historia; cada historia es un DCF completo con los
insumos de la hoja (misma tasa de descuento, beta de la hoja) y su propio crecimiento, margen, reinversión, crecimiento
terminal y ROIC después del año 10. Contrato del 30-sep-2026: las historias A-D son los escenarios DCF activos
(escenariosUnificados), A es la central (valorCentral, dcfBase) y el antiguo Base de la hoja queda como
dcfBaseTecnicoAnterior; escenariosDCF documenta la convención en la valoración y en el análisis. ADBE se omite por
defecto: su bloque se construyó a mano y es la referencia.

Uso: python scripts/sync_valor_esperado.py ../Modelo-JMR-datos [TICKER ...]
"""
from __future__ import annotations

import datetime as dt
import glob
import json
import sys
from pathlib import Path

REF = Path(__file__).resolve().parents[1] / "reference" / "damodaran"
METODO = "Escenarios = historias; cada historia es un DCF completo. Valor principal = suma de DCF × probabilidad."


def valor_esperado(r: dict) -> dict:
    """Contrato del 30-sep-2026 (implementado primero en ADBE): las historias A-D son los escenarios DCF activos; el
    valor principal es el esperado, la historia A es la central y el antiguo Base de la hoja queda como referencia."""
    hs = r["historias"]
    a = next(h for h in hs if h.get("id") == "A")
    vals = [h["valor_beta_hoja"] for h in hs]
    now = dt.datetime.now(dt.timezone.utc).isoformat()

    def historia(h):
        out = {"nombre": h["nombre"], "probabilidad": h["prob"], "valor": h["valor_beta_hoja"],
               "valorBetaPropuesta": h.get("valor_beta_prop"), "margen": h.get("margen"), "crecimiento": h.get("cagr"),
               "roicTerminal": "costo_capital" if h.get("roic_terminal") == "costo_capital" else "hoja",
               "id": h["id"], "central": h["id"] == "A", "crecimientoPorGrupo": h.get("crec"),
               "salesToCapital": h.get("s2c") or r.get("s2c"), "salesToCapital2": (h.get("detalle") or {}).get("s2c2"),
               "crecimientoAnios": h.get("anios"), "terminalGrowth": h.get("terminal_growth")}
        if h.get("descripcion"):
            out["descripcion"] = h["descripcion"]
        if h.get("terminal_propio"):
            out["crecimientoAnios6a10"] = h.get("anios6a10")
            out["criterioTerminal"] = (f"Estabilización del negocio residual, sin recuperación: g = {h['terminal_growth'] * 100:.2f}% "
                                       "(crecimiento del año 5, sin superar el terminal de la hoja y con piso de 0%). Hipótesis del "
                                       "analista, no guía de la empresa.")
        return out

    return {
        "fecha": r.get("fecha"),
        "valor": r["valor_esperado_beta_hoja"],
        "valorBetaPropuesta": r.get("valor_esperado_beta_prop"),
        "betaHoja": r.get("beta_hoja"), "betaPropuesta": r.get("beta_prop"),
        "dcfBase": a["valor_beta_hoja"],
        "metodo": METODO,
        "escenariosUnificados": True,
        "historiaCentralId": "A",
        "valorCentral": a["valor_beta_hoja"],
        "rango": {"min": min(vals), "max": max(vals)},
        "dcfBaseTecnicoAnterior": r.get("dcf_base"),
        "updatedAt": now,
        "historias": [historia(h) for h in hs],
    }


def escenarios_dcf(rec: dict) -> dict:
    dh = (rec.get("descuentoMultiples") or {}).get("dcfHoy") or {}
    return {"version": 1, "fuente": "valorEsperado.historias", "principal": "valorEsperado.valor", "central": "A",
            "fecha": dt.datetime.now(dt.timezone.utc).isoformat(),
            "baseAnterior": {k: dh.get(k) for k in ("conservador", "base", "optimista")},
            "nota": "Los tres casos de la hoja original se conservan como calibración y supuestos auxiliares de múltiplos; "
                    "no son los escenarios DCF activos."}


def main(argv: list[str]) -> int:
    datos = Path(argv[0])
    tickers = argv[1:] or sorted(p.name.split("_")[0] for p in REF.glob("*_resultado.json") if not p.name.startswith("ADBE"))
    for t in tickers:
        r = json.loads((REF / f"{t}_resultado.json").read_text())
        ve = valor_esperado(r)
        vf = glob.glob(str(datos / f"valoraciones/{t}-*.json"))
        esc = escenarios_dcf(json.loads(Path(vf[0]).read_text())) if vf else None
        for pat, key in ((f"valoraciones/{t}-*.json", None), (f"analisis/{t}-research-*.json", "linkedValuation")):
            for f in glob.glob(str(datos / pat)):
                rec = json.loads(Path(f).read_text())
                tgt = rec.get(key) if key else rec
                if key and not isinstance(tgt, dict):
                    continue
                tgt["valorEsperado"] = ve
                rec["escenariosDCF"] = esc
                if key:  # el análisis también lleva el valor esperado en la raíz (lo lee la app)
                    rec["valorEsperado"] = ve
                Path(f).write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n")
        print(f"{t:5s} valor esperado {ve['valor']:.2f} (A {ve['valorCentral']:.2f}; técnico anterior {ve['dcfBaseTecnicoAnterior']:.2f})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
