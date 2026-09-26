#!/usr/bin/env python
"""Reinicia una hoja de valoracion desde la plantilla maestra auditada,
hoja por hoja (formulas, no solo valores). Uso obligatorio al empezar
CUALQUIER empresa nueva: nunca dupliques en Drive la hoja de otra
empresa ya llena, porque las hojas de texto (Cualitativo, Stories to
Numbers, Supuestos Recomendados, Tesis, Supuestos de los Multiplos) no
se regeneran solas y quedan con el contenido de la empresa anterior (ver
modelo/METODOLOGIA.md, seccion Auditoria, para el historial de casos
reales: PYPL con Cualitativo de Adobe, MSFT y PLTR con el perfil
cruzado de Palantir/Apple/LULU).

Generalizacion de 'step_reset' de run_afya.py (que se uso una vez para
esa empresa) para que cualquier valoracion nueva pueda arrancar limpia
desde el primer commit, sin escribir un script a medida cada vez.

El contenido ANTERIOR de la hoja destino se respalda completo (todas
las hojas, formulas) antes de borrarlo, para poder recuperarlo si la
hoja destino no era en realidad una hoja nueva sino que ya tenia una
valoracion real.

Uso:
    PYTHONPATH=.:scripts python scripts/reset_from_master.py --sheet-id ID [--dry-run]

    # o para una hoja que todavia no existe (crea una copia de la plantilla
    # maestra en Drive con ese nombre y la deja lista para --step reset+refresh):
    PYTHONPATH=.:scripts python scripts/reset_from_master.py --new "Modelo JMR - TICKER" [--dry-run]
"""
from __future__ import annotations

import argparse
import gzip
import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from gspread.exceptions import APIError  # noqa: E402

import model_steps as ms  # noqa: E402
from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

# Plantilla maestra auditada (misma que usa run_afya.py; ver auditoria
# A1-A18 en reference/auditoria_2026-09-26_informe.json). Si algun dia se
# vuelve a auditar la plantilla, actualizar este ID a la copia mas nueva.
MASTER_ID = "19PRUFiYsNavUcN6WwHBVlp-VRMozp3rNSE2R1zt7N-g"

BACKUP_DIR = _ROOT / "reference" / "backups" / "reset_from_master"


def _retry(fn, tries: int = 6):
    for i in range(tries):
        try:
            return fn()
        except APIError as exc:
            if "429" not in str(exc) or i == tries - 1:
                raise
            time.sleep(30 * (i + 1))


def reset(client, sheet_id: str, *, dry_run: bool) -> None:
    sh = client.open_by_key(sheet_id)
    master = client.open_by_key(MASTER_ID)
    titles = [w.title for w in sh.worksheets()]
    m_titles = [w.title for w in master.worksheets()]
    rng = lambda ts: [f"'{t}'" for t in ts]  # noqa: E731

    old = _retry(lambda: sh.values_batch_get(rng(titles), params={"valueRenderOption": "FORMULA"}))
    backup_path = BACKUP_DIR / f"{sheet_id}_pre_reset.json.gz"
    if not dry_run:
        backup_path.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(backup_path, "wt", encoding="utf-8") as fh:
            json.dump({"title": sh.title, "sheets": {t: v.get("values", []) for t, v in zip(titles, old["valueRanges"])}}, fh,
                      ensure_ascii=False)

    new = _retry(lambda: master.values_batch_get(rng(m_titles), params={"valueRenderOption": "FORMULA"}))["valueRanges"]
    n_new_sheets = sum(1 for t in m_titles if t not in titles)
    print(f"{sh.title}: {len(m_titles)} hojas en la plantilla, {n_new_sheets} no existian aun en el destino, "
          f"respaldo en {backup_path}")
    if dry_run:
        return

    for t in m_titles:
        if t not in titles:
            _retry(lambda: sh.add_worksheet(t, rows=200, cols=26))
    common = [t for t in m_titles]
    _retry(lambda: sh.values_batch_clear(body={"ranges": rng(common)}))
    data = [{"range": f"'{t}'!A1", "values": v.get("values", [])} for t, v in zip(m_titles, new) if v.get("values")]
    for i in range(0, len(data), 8):
        _retry(lambda: sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": data[i:i + 8]}))
    print("reset: contenido de la plantilla maestra copiado en", sh.title)


def new_copy(client, title: str, *, dry_run: bool) -> str:
    """Crea una copia de la plantilla maestra en Drive con el nombre dado
    (mas simple que reset() para una hoja que todavia no existe: Drive ya
    copia formulas y formato tal cual, sin pasar por la API de valores).

    La cuenta de servicio de este repo tiene cuota de almacenamiento 0 (no
    puede ser DUEÑA de archivos nuevos en Drive), asi que esto casi
    seguro falla con un 403/storageQuotaExceeded. Si pasa, la alternativa
    es que una persona haga "Archivo > Hacer una copia" de la plantilla
    maestra a mano en Drive (queda ya limpia, sin necesidad de --sheet-id
    despues) y comparta el resultado con la cuenta de servicio."""
    if dry_run:
        print(f"(dry-run) crearia una copia de la plantilla maestra llamada {title!r}")
        return ""
    try:
        new_sh = client.copy(MASTER_ID, title=title)
    except Exception as exc:  # noqa: BLE001
        print(f"No se pudo crear el archivo ({exc}). Copia la plantilla a mano en Drive "
              f"('Archivo > Hacer una copia' de {MASTER_ID}) y compartila con la cuenta de servicio.")
        raise
    print(f"creada: {title} -> {new_sh.url}")
    return new_sh.id


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--sheet-id", help="ID de una hoja EXISTENTE (posiblemente duplicada de otra empresa) a reiniciar")
    g.add_argument("--new", metavar="TITULO", help="Crea una copia nueva de la plantilla maestra con este titulo")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    client = get_gspread_client()
    if args.new:
        new_copy(client, args.new, dry_run=args.dry_run)
    else:
        reset(client, args.sheet_id, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
