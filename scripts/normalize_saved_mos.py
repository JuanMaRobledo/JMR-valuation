"""Deja las valoraciones guardadas con la convención vigente del MOS (auditoría del 30-sep-2026).

El visor recalcula desde la hoja, que no conoce el valor esperado de las historias, y por eso
sync_saved_after_dcf.py vuelve a escribir el MOS sobre el DCF. Este paso se corre después:
  - baseMOS = "valorEsperado"; precio con MOS = valor esperado × (1 − MOS), una sola cifra;
  - precioMOS, precioMOSMax, precioMOSHoy y zonas.conMOS usan esa cifra;
  - valorEsperado: ROIC terminal numérico en las historias que conservan el de la hoja;
  - copia esos campos al linkedValuation del análisis vinculado;
  - crecimientoImplicito: agrega dcfHoy, dcfFy3 y metodo si faltan (parametros se conserva de la revisión anterior).

Uso: python scripts/normalize_saved_mos.py ../Modelo-JMR-datos [TICKER ...]
"""
from __future__ import annotations

import glob
import json
import subprocess
import sys
from pathlib import Path

LINKED = ("valorEsperado", "escenariosDCF", "precioMOS", "precioMOSMax", "precioMOSHoy", "zonas", "baseMOS", "precioMOSValorEsperado")
ZONAS_DESC = ("Value, Deep Value e histórica son bandas heredadas del objetivo FY+3; no son umbrales de valor "
              "intrínseco presente. MOS vigente: valor esperado.")


def normalize(r: dict, old: dict | None, roic_hoja: float | None) -> dict:
    ve = r["valorEsperado"]
    pm = ve["valor"] * (1 - float(r.get("mos") or 0))
    r["baseMOS"] = "valorEsperado"
    r["precioMOSValorEsperado"] = r["precioMOS"] = r["precioMOSMax"] = pm
    r["precioMOSHoy"] = {k: pm for k in ("conservador", "base", "optimista")}
    r["zonas"]["conMOS"] = {"min": pm, "max": pm, "base": "valor esperado; una cifra, sin escenarios"}
    r["zonas"]["descripcion"] = ZONAS_DESC
    ve["metodo"] = ("Escenarios = historias; cada historia es un DCF completo. Valor principal = suma de DCF × probabilidad."
                    if ve.get("escenariosUnificados") else "Promedio de DCF completos ponderado por probabilidades del analista.")
    for h in ve["historias"]:
        if h.get("roicTerminal") == "hoja":
            h["roicTerminal"] = roic_hoja if roic_hoja else "costo_capital"
    ci = r.get("crecimientoImplicito") or {}
    ci["dcfHoy"] = r["descuentoMultiples"]["dcfHoy"]["base"]
    ci["dcfFy3"] = r["metodos"][0]["base"]
    ci["metodo"] = "DCF inverso completo sin calibración; múltiplos frente al DCF capitalizado FY+3"
    if "parametros" not in ci and old and "parametros" in (old.get("crecimientoImplicito") or {}):
        ci["parametros"] = old["crecimientoImplicito"]["parametros"]
    r["crecimientoImplicito"] = ci
    r["metodos"][0].setdefault("horizonte", "FY+3; capitalizado desde el DCF presente")
    return r


def main(argv: list[str]) -> int:
    root = Path(argv[0])
    tickers = argv[1:]
    moat = json.loads((Path(__file__).resolve().parents[1] / "reference" / "moat_2026-09-30.json").read_text())["empresas"]
    for f in sorted(glob.glob(str(root / "valoraciones" / "*.json"))):
        r = json.loads(Path(f).read_text())
        t = r.get("ticker")
        if tickers and t not in tickers or not r.get("valorEsperado"):
            continue
        rel = str(Path(f).relative_to(root))
        try:
            old = json.loads(subprocess.check_output(["git", "-C", str(root), "show", f"HEAD:{rel}"]))
        except subprocess.CalledProcessError:
            old = None
        normalize(r, old, (moat.get(t) or {}).get("roic_terminal"))
        Path(f).write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n")
        for af in glob.glob(str(root / "analisis" / f"{t}-research-*.json")):
            a = json.loads(Path(af).read_text())
            lv = a.get("linkedValuation") or {}
            if lv.get("sourcePath") == rel:
                for k in LINKED:
                    if k in r:
                        lv[k] = r[k]
                Path(af).write_text(json.dumps(a, ensure_ascii=False, indent=2) + "\n")
        print(f"{t:5s} MOS sobre el valor esperado: {r['precioMOS']:.2f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
