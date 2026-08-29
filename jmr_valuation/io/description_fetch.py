"""Busca una descripcion de la empresa en espanol, sin API key.

No existe una fuente publica y gratuita de "descripciones de empresas" en
espanol con cobertura amplia -- Wikipedia en espanol es la que mejor cubre
tanto grandes empresas cotizadas como companias mas chicas, y no exige
registrarse ni pagar. Si no encuentra nada usable, el llamador debe dejar que
el usuario complete el campo a mano (igual que ya se hacia antes de esto).
"""
from __future__ import annotations

import re

import requests

_SEARCH_URL = "https://es.wikipedia.org/w/api.php"
_SUMMARY_URL = "https://es.wikipedia.org/api/rest_v1/page/summary/{title}"
_USER_AGENT = "JMR-Valuation-Dashboard/1.0 (uso personal, sin fines comerciales)"
_TIMEOUT = 8


def fetch_company_description_es(company_name: str) -> str | None:
    """Busca `company_name` en Wikipedia en espanol y devuelve el resumen del
    articulo mas relevante, o None si no se encontro nada usable (sin resultados,
    o el resultado es una pagina de desambiguacion)."""
    if not company_name.strip():
        return None
    title = _search_best_title(company_name)
    if title is None:
        return None
    return _fetch_summary(title)


def _is_plausible_match(company_name: str, title: str) -> bool:
    """Guarda minima contra resultados sin relacion: al menos una palabra
    significativa (4+ letras) del nombre buscado tiene que aparecer en el
    titulo encontrado. La busqueda de texto libre de MediaWiki puede devolver
    articulos totalmente ajenos cuando la consulta es corta o ambigua (ej. un
    ticker de 4 letras coincidiendo por casualidad con otro termino)."""
    words = [w for w in re.findall(r"[^\W\d_]+", company_name.lower()) if len(w) >= 4]
    if not words:
        return True  # nombre muy corto para filtrar (ticker de 3 letras, etc.) -- se confia en Wikipedia
    title_lower = title.lower()
    return any(w in title_lower for w in words)


def _search_best_title(company_name: str) -> str | None:
    params = {"action": "query", "list": "search", "srsearch": company_name, "format": "json", "srlimit": 1}
    response = requests.get(_SEARCH_URL, params=params, headers={"User-Agent": _USER_AGENT}, timeout=_TIMEOUT)
    response.raise_for_status()
    results = response.json().get("query", {}).get("search", [])
    if not results:
        return None
    title = results[0]["title"]
    return title if _is_plausible_match(company_name, title) else None


def _fetch_summary(title: str) -> str | None:
    url = _SUMMARY_URL.format(title=requests.utils.quote(title, safe=""))
    response = requests.get(url, headers={"User-Agent": _USER_AGENT}, timeout=_TIMEOUT)
    if response.status_code == 404:
        return None
    response.raise_for_status()
    data = response.json()
    if data.get("type") == "disambiguation":
        return None
    extract = data.get("extract", "").strip()
    return extract or None
