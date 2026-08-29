"""Guarda cada empresa cargada (Excel/CSV/SEC EDGAR) en disco, para poder
volver a abrirla despues desde el dashboard sin resubir el archivo original.

Nota sobre Streamlit Community Cloud: ahi el filesystem es efimero. Lo que se
guarda aca sobrevive mientras la app siga corriendo (entre pestanias, entre
recargas de pagina), pero se pierde si la app se reinicia (redeploy, o si se
"duerme" por inactividad). Para persistencia 100% confiable conviene correr el
dashboard localmente (ver 'Iniciar Dashboard.bat').
"""
from __future__ import annotations

import re
from pathlib import Path

from jmr_valuation.io.inputs import CompanyInputs, load_company_inputs, save_company_inputs

_PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SAVED_COMPANIES_DIR = _PROJECT_ROOT / "data" / "saved_companies"


def _safe_filename(inputs: CompanyInputs) -> str:
    base = inputs.ticker.strip() or inputs.company_name.strip() or "empresa"
    safe = re.sub(r"[^A-Za-z0-9_-]+", "_", base).strip("_") or "empresa"
    return f"{safe.upper()}.csv"


def save_company(inputs: CompanyInputs) -> Path:
    """Escribe/actualiza el CSV guardado de esta empresa (una por ticker) y devuelve su ruta."""
    SAVED_COMPANIES_DIR.mkdir(parents=True, exist_ok=True)
    path = SAVED_COMPANIES_DIR / _safe_filename(inputs)
    save_company_inputs(inputs, path)
    return path


def list_saved_companies() -> list[Path]:
    if not SAVED_COMPANIES_DIR.exists():
        return []
    return sorted(SAVED_COMPANIES_DIR.glob("*.csv"))


def load_saved_company(path: Path) -> CompanyInputs:
    return load_company_inputs(path)
