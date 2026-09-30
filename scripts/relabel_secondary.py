"""Rotula en las hojas el ponderado y los múltiplos como lecturas secundarias (30-sep-2026).

Criterio Damodaran: el valor intrínseco es el DCF. Solo reescribe textos de la
columna A de «Descuento de múltiplos» y «Resumen de Valoración» cuando el texto
vigente es el rótulo anterior; no toca fórmulas ni valores.

Uso: python scripts/relabel_secondary.py [--dry-run]
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from discount_multiples import RES, SHEET, _open, _retry, get_gspread_client  # noqa: E402

_ROOT = Path(__file__).resolve().parents[1]
REPORT = _ROOT / "reference" / "descuento_multiples_2026-09-29_informe.json"

CHANGES = {
    SHEET: {
        36: ("VALOR INTRÍNSECO HOY · DCF + MÚLTIPLOS DESCONTADOS", "VALOR HOY · DCF (VALOR INTRÍNSECO) + MÚLTIPLOS DESCONTADOS (SECUNDARIO)"),
        38: ("DCF (valor presente)", "DCF · valor intrínseco (valor presente)"),
        40: ("Valor intrínseco ponderado", "Ponderado DCF + múltiplos (secundario)"),
        43: ("Precio de compra con MOS", "Compra con MOS sobre el ponderado (secundario)"),
    },
    RES: {
        30: ("VALOR POR ACCIÓN HOY | DCF + MÚLTIPLOS DESCONTADOS", "VALOR POR ACCIÓN HOY | DCF = VALOR INTRÍNSECO · MÚLTIPLOS Y PONDERADO = SECUNDARIOS"),
        32: ("DCF hoy (valor presente)", "DCF hoy · valor intrínseco"),
        33: ("Múltiplos consolidados hoy", "Múltiplos consolidados hoy (secundario)"),
        34: ("Valor intrínseco ponderado hoy", "Ponderado hoy (secundario)"),
        36: ("Compra con MOS", "Compra con MOS sobre el ponderado"),
    },
}


def main(argv: list[str]) -> int:
    dry = "--dry-run" in argv
    client = get_gspread_client()
    rep = json.loads(REPORT.read_text())
    tabs = list(CHANGES)
    for sid, info in rep.items():
        if info.get("estado") != "aplicada":
            continue
        name = info.get("nombre", sid)[:50]
        try:
            sh = _retry(lambda: _open(client, sid))
            got = _retry(lambda: sh.values_batch_get([f"'{t}'!A1:A60" for t in tabs]))["valueRanges"]
        except Exception as e:  # noqa: BLE001
            print(f"{name:50s} sin acceso ({type(e).__name__})")
            continue
        data = []
        for tab, vr in zip(tabs, got):
            cur = [(row[0] if row else "") for row in vr.get("values", [])]
            data += [{"range": f"'{tab}'!A{r}", "values": [[new]]} for r, (old, new) in CHANGES[tab].items()
                     if r <= len(cur) and cur[r - 1].strip() == old]
        if data and not dry:
            _retry(lambda: sh.values_batch_update({"valueInputOption": "RAW", "data": data}))
        print(f"{name:50s} {len(data)} rótulos{' (simulado)' if dry else ''}", flush=True)
        time.sleep(4)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
