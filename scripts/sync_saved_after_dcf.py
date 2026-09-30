"""Lleva a la valoración guardada del visor (Modelo-JMR-datos/valoraciones/*.json) los
resultados de una hoja después de revisar los supuestos del DCF (revise_dcf_inputs.py,
30-sep-2026). Misma mecánica que sync_saved_after_multiples.py; además copia 'Valuation
output' y deja la revisión en auditoria.revisionDCF.

Carga la hoja en docs/visor.html (Playwright, igual que patch_saved_present_value.py) y
copia TODO lo que depende de los múltiplos: metodos, objetivoPonderado, cagr, zonas,
precioMOS, precioMOSMax, valorPresentePonderado, descuentoMultiples y precioMOSHoy;
rehace los resúmenes compactos 'Resumen de Valoración' y 'Descuento de múltiplos' y
reemplaza las hojas crudas de los múltiplos y la tesis. Conserva fecha, precios,
análisis fundamental, Cualitativo editado y notas. Anota el cambio en 'auditoria'.

Uso:
    python scripts/sync_saved_after_dcf.py ../Modelo-JMR-datos/valoraciones/GOOG-*.json
"""
from __future__ import annotations

import json
import os
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from playwright.sync_api import sync_playwright  # noqa: E402

from patch_saved_present_value import summaries  # noqa: E402
from regen_saved_valuations import export_xlsx, regen, serve  # noqa: E402

FIELDS = ("metodos", "objetivoPonderado", "cagr", "zonas", "precioMOS", "precioMOSMax",
          "valorPresentePonderado", "descuentoMultiples", "precioMOSHoy", "crecimientoImplicito")
RAW_SHEETS = ("Valuation output", "EVEBITDA", "EVFCFF", "PE", "PFCFE", "POCF", "Financials Multiples")


def main(paths: list[str]) -> int:
    srv = serve()
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
        for path in paths:
            old = json.loads(Path(path).read_text())
            sid = old["hojaGoogle"].split("/d/")[1].split("/")[0]
            xlsx = os.path.join(tempfile.gettempdir(), f"{sid}.xlsx")
            export_xlsx(sid, xlsx)
            ctx = browser.new_context()
            ctx.add_init_script("localStorage.setItem('jmr-auth-ok-v1','1');localStorage.setItem('jmr-gh-datastore-token','x');")
            new, status = regen(sid, xlsx, ctx.new_page())
            ctx.close()
            before = {k: old.get(k) for k in ("objetivoPonderado", "valorPresentePonderado")}
            for k in FIELDS:
                old[k] = new.get(k)
            val_old = old.setdefault("hojas", {}).setdefault("valoracion", {})
            val_new = (new.get("hojas") or {}).get("valoracion") or {}
            for name in RAW_SHEETS:
                if val_new.get(name):
                    val_old[name] = val_new[name]
            an_old = old["hojas"].setdefault("analisis", {})
            an_new = (new.get("hojas") or {}).get("analisis") or {}
            if an_new.get("Tesis de Inversión y Supuestos"):
                an_old["Tesis de Inversión y Supuestos"] = an_new["Tesis de Inversión y Supuestos"]
            m = re.search(r"<td>([^<\d-]+?)\s[\d-]", val_old.get("Resumen de Valoración", ""))
            val_old["Resumen de Valoración"], val_old["Descuento de múltiplos"] = summaries(old, m.group(1) if m else "US$")
            before["dcfHoy"] = ((json.loads(Path(path).read_text()).get("descuentoMultiples") or {}).get("dcfHoy"))
            aud = old.setdefault("auditoria", {})
            aud["revisionDCF"] = {"fecha": "2026-09-30", "antes": {"dcfHoy": before["dcfHoy"], "objetivoPonderado": before["objetivoPonderado"],
                                  "valorPresentePonderado": before["valorPresentePonderado"]},
                                  "detalle": "Supuestos del DCF revisados (crecimiento, margen, sales-to-capital, beta y/o ROIC después del año 10). Celdas, valores anteriores y motivos: "
                                             "reference/revision_dcf_2026-09-30/ en JMR-valuation; cada celda cambiada tiene una nota en la hoja."}
            Path(path).write_text(json.dumps(old, ensure_ascii=False, indent=2) + "\n")
            print(f"{old['ticker']:5s} {status[:18]} DCF hoy base {(before['dcfHoy'] or {}).get('base', 0):.2f} -> {old['descuentoMultiples']['dcfHoy']['base']:.2f} | FY+3 base {before['objetivoPonderado']['base']:.2f} -> {old['objetivoPonderado']['base']:.2f} | "
                  f"hoy base {before['valorPresentePonderado']['base']:.2f} -> {old['valorPresentePonderado']['base']:.2f}", flush=True)
    srv.shutdown()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
