"""Migra las fichas de historias (reference/damodaran/<T>.json) al contrato de escenarios del 30-sep-2026
(prompt de valoración v4 y de research v5, implementado primero en ADBE): las cuatro historias son los
escenarios DCF activos y siguen el orden A · Base, B · Conservadora, C · Disrupción, D · Optimista.

Por ficha:
  - si la historia optimista está en C y la de deterioro en D, las intercambia y cambia las letras en los
    textos (probabilidades, tasas base, reinversión, riesgo, precio, evidencia en contra);
  - nombra C «C · Tesis de disrupción · Deterioro de los fundamentales» y guarda el nombre propio de la
    empresa en «descripcion»;
  - C usa ROIC terminal = costo de capital (la ventaja se pierde) y crecimiento terminal propio
    («terminal": "estabilizacion"): el del año 5 de la historia, sin superar el terminal de la hoja y con piso
    de 0% si el año 5 es negativo. No hay recuperación por defecto (damodaran_stories.py lo calcula);
  - agrega el identificador de cada historia («id») y el tipo de tesis («tesis»).

Es idempotente. Uso: python scripts/unify_story_specs.py [TICKER ...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REF = Path(__file__).resolve().parents[1] / "reference" / "damodaran"
NOMBRE_C = "C · Tesis de disrupción · Deterioro de los fundamentales"
TESIS = {"A": "base", "B": "conservadora", "C": "disrupción", "D": "optimista"}
LETRA = re.compile(r"(?<![\w+/.-])([CD])(?![\w+/-])")
TEXTOS = ("prob_texto", "tasas_base_nota", "contra", "precio_lectura")
BLOQUES = ("reinversion", "riesgo", "crecimiento", "margenes")


def swap_letters(s: str) -> str:
    return LETRA.sub(lambda m: "D" if m.group(1) == "C" else "C", s)


def swap_prob_sentences(s: str) -> str:
    """Tras cambiar las letras, «D (20%) … C (5%) …» vuelve al orden «C (5%) … D (20%) …»."""
    parts = re.split(r"(?<=\.)\s+(?=[A-D] \(\d)", s)
    i = next((k for k, x in enumerate(parts) if x.startswith("C (")), None)
    j = next((k for k, x in enumerate(parts) if x.startswith("D (")), None)
    if i is not None and j is not None and j < i:
        parts[i], parts[j] = parts[j], parts[i]
    return " ".join(parts)


def erosion_sentence(spec: dict) -> None:
    letras = [h["id"] for h in spec["historias"] if h.get("roic_terminal") == "costo_capital"]
    if not letras:
        return
    lista = letras[0] if len(letras) == 1 else ", ".join(letras[:-1]) + " y " + letras[-1]
    frase = f"En las historias de erosión ({lista}) el ROIC después del año 10 es el costo de capital."
    t = re.sub(r"\s*En las historias de erosión \([^)]*\) el ROIC después del año 10 es el costo de capital\.", "", spec["prob_texto"])
    spec["prob_texto"] = t.rstrip() + " " + frase


def migrate(spec: dict) -> str:
    hs = spec["historias"]
    if hs[2]["nombre"].startswith(NOMBRE_C):
        return "ya migrada"
    # La historia de deterioro es la de menor margen objetivo; si está en D, se intercambia con C.
    swapped = len(hs) == 4 and hs[3]["margen"] < hs[2]["margen"]
    if swapped:
        hs[2], hs[3] = hs[3], hs[2]
        for k in TEXTOS:
            if spec.get(k):
                spec[k] = swap_letters(spec[k])
        for k in BLOQUES:
            if (spec.get(k) or {}).get("texto"):
                spec[k]["texto"] = swap_letters(spec[k]["texto"])
        spec["prob_texto"] = swap_prob_sentences(spec["prob_texto"])
    for letra, h in zip("ABCD", hs):
        desc = h["nombre"].split(" · ", 1)[1] if " · " in h["nombre"] else h["nombre"]
        h["id"], h["tesis"] = letra, TESIS[letra]
        if letra == "C":
            h["descripcion"] = desc
            h["nombre"] = NOMBRE_C
            h["roic_terminal"] = "costo_capital"
            h["terminal"] = "estabilizacion"
        else:
            h["nombre"] = f"{letra} · {desc}"
    erosion_sentence(spec)
    return "C↔D intercambiadas" if swapped else "orden ya correcto"


def main(argv: list[str]) -> int:
    tickers = argv or sorted(p.stem for p in REF.glob("*.json") if "_" not in p.stem and p.stem.isupper())
    for t in tickers:
        if t == "ADBE":  # caso de referencia: sección escrita a mano, no se regenera
            continue
        f = REF / f"{t}.json"
        spec = json.loads(f.read_text())
        estado = migrate(spec)
        f.write_text(json.dumps(spec, ensure_ascii=False, indent=1))
        print(f"{t:5s} {estado}: " + " | ".join(f"{h['id']} {h['prob']:.0%} {h.get('descripcion', h['nombre'])[:40]}" for h in spec["historias"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
