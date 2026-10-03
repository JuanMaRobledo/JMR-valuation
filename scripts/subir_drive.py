"""Sube a Drive los informes regenerados (3-oct-2026) y verifica el md5 de cada archivo.

Reemplaza el contenido de archivos que ya existen en Drive (no crea archivos nuevos). Los pares ruta -> id están en
reference/cartera_drive.json.

Uso: python scripts/subir_drive.py [TICKER ...]        (sin tickers: las 22)
     python scripts/subir_drive.py --id FILE_ID RUTA   (un archivo suelto)
Necesita GOOGLE_SERVICE_ACCOUNT_JSON_CONTENT.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]


def sesion():
    from google.auth.transport.requests import AuthorizedSession
    from google.oauth2 import service_account

    info = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT_JSON_CONTENT"])
    cr = service_account.Credentials.from_service_account_info(info, scopes=["https://www.googleapis.com/auth/drive"])
    return AuthorizedSession(cr)


def subir(s, fid: str, path: Path) -> bool:
    data = path.read_bytes()
    r = s.patch(f"https://www.googleapis.com/upload/drive/v3/files/{fid}?uploadType=media&supportsAllDrives=true",
                data=data, headers={"Content-Type": "text/markdown"})
    r.raise_for_status()
    m = s.get(f"https://www.googleapis.com/drive/v3/files/{fid}?fields=name,md5Checksum&supportsAllDrives=true").json()
    ok = m.get("md5Checksum") == hashlib.md5(data).hexdigest()
    print(f"{'OK ' if ok else 'MD5 DISTINTO'} {m.get('name')} <- {path.relative_to(_ROOT) if path.is_relative_to(_ROOT) else path}")
    return ok


def main(argv: list[str]) -> int:
    s = sesion()
    if argv[:1] == ["--id"]:
        return 0 if subir(s, argv[1], Path(argv[2]).resolve()) else 1
    emp = json.loads((_ROOT / "reference" / "cartera_drive.json").read_text())["empresas"]
    pares = [(fid, _ROOT / ruta) for t in (argv or sorted(emp)) for ruta, fid in emp[t].items()]
    faltan = [str(p) for _, p in pares if not p.exists()]
    if faltan:
        print("No existen:", *faltan, sep="\n  ")
        return 1
    malos = sum(not subir(s, fid, p) for fid, p in pares)
    print(f"{len(pares) - malos}/{len(pares)} archivos subidos y verificados")
    return 1 if malos else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
