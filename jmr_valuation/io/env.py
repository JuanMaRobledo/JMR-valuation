"""Carga variables desde un archivo .env a os.environ, sin depender de librerias externas.

Busca ".env" en la raiz del proyecto. No pisa una variable que ya este definida
en el entorno (por ejemplo, si la seteaste vos mismo en la terminal).
"""
from __future__ import annotations

import os
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def load_dotenv(path: str | Path | None = None) -> None:
    env_path = Path(path) if path is not None else _PROJECT_ROOT / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)
