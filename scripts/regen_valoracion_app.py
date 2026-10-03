"""Regenera la valoración guardada de la app desde la hoja de cálculo (3-oct-2026).

Exporta la hoja a .xlsx, la carga en la calculadora de la app (docs/ de Modelo-JMR, servida en local) con Chromium y
reemplaza Modelo-JMR-datos/valoraciones/<T>-*.json. Conserva los campos que no salen de la hoja (análisis vinculado,
enlace a la hoja, fuente del precio) y el historial de auditoría.

Uso: python scripts/regen_valoracion_app.py TICKER [SHEET_ID]
Variables: SHEETJS_PATH (xlsx.full.min.js 0.18.5), CHROMIUM_PATH (opcional). scripts/regenerar_cartera.sh las define.
"""
from __future__ import annotations

import glob
import json
import os
import sys
import tempfile
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT / "scripts"))
sys.path.insert(0, str(_ROOT))
import regen_saved_valuations as rg  # noqa: E402

DATOS = _ROOT.parent / "Modelo-JMR-datos"
CONSERVAR = ("analisisFundamental", "hojaGoogle", "precioReferenciaFuente", "precioReferenciaConsultadoAt")


def main(tk: str, sid: str | None = None) -> None:
    from playwright.sync_api import sync_playwright

    sid = sid or json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
    saved = [p for p in glob.glob(str(DATOS / "valoraciones" / f"{tk}-*.json")) if "regen" not in p][0]
    srv = rg.serve()
    try:
        with sync_playwright() as p:
            b = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
            x = os.path.join(tempfile.gettempdir(), f"{sid}.xlsx")
            rg.export_xlsx(sid, x)
            ctx = b.new_context()
            ctx.add_init_script("localStorage.setItem('jmr-auth-ok-v1','1');localStorage.setItem('jmr-gh-datastore-token','x');")
            rec, status = rg.regen(sid, x, ctx.new_page())
            b.close()
    finally:
        srv.shutdown()
    old = json.load(open(saved))
    for k in CONSERVAR:
        if old.get(k) is not None:
            rec[k] = old[k]
    if old.get("auditoria"):
        rec["auditoria"] = {**old["auditoria"], **(rec.get("auditoria") or {})}
    with open(saved, "w") as f:
        f.write(json.dumps(rec, ensure_ascii=False, indent=2) + "\n")
    print(status, tk, saved, "precio", rec.get("precio"), "pondFY3", rec["objetivoPonderado"]["base"],
          "pondHoy", rec["valorPresentePonderado"]["base"])


if __name__ == "__main__":
    main(*sys.argv[1:3])
