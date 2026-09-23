"""Complementa 'companyfacts' de SEC EDGAR con hechos leidos directamente de
las instancias XBRL de 10-K/10-Q individuales.

Dos huecos reales de 'companyfacts' que este modulo cubre (ambos confirmados
con PYPL):

1. **Lag de la API**: 'companyfacts' puede tardar semanas en incorporar el
   ultimo 10-Q ya presentado (PYPL: el 10-Q de Q2 2026, presentado el
   2026-07-28, seguia sin aparecer en septiembre) -- el LTM quedaba un
   trimestre atrasado. Cualquier 10-K/10-Q presentado despues del ultimo
   'filed' que ya tiene companyfacts se lee de su instancia y se agrega.

2. **Tags propios de la empresa**: 'companyfacts' solo expone namespaces
   estandar (us-gaap, dei, srt...), nunca el namespace propio de la empresa.
   PYPL reporta su I+D como 'pypl:TechnologyAndDevelopmentExpense' desde
   2019 -- sin esto, R&D quedaba en 0 para 2019-2025 y la capitalizacion de
   I+D del modelo (Input sheet!B17) no tenia datos. `custom_tag_map` mapea el
   tag propio a su equivalente us-gaap y se leen los 10-K necesarios para
   cubrir el historico (cada 10-K trae 3 ejercicios comparativos).

Solo se toman hechos SIN dimensiones XBRL (contextos sin <segment>), igual
que companyfacts -- los desgloses por segmento/clase quedan afuera.
"""
from __future__ import annotations

import hashlib
import logging
import json
import re
import tempfile
import time
import xml.etree.ElementTree as ET
from pathlib import Path

import requests

from jmr_valuation.io.sec_edgar_client import SecEdgarClient

_ARCHIVES = "https://www.sec.gov/Archives/edgar/data"
_XBRLI = "{http://www.xbrl.org/2003/instance}"
_LINKBASE_SUFFIXES = ("_cal.xml", "_def.xml", "_lab.xml", "_pre.xml")
logger = logging.getLogger(__name__)
_CACHE_DIR = Path(tempfile.gettempdir()) / "jmr_sec_xbrl_cache"


def _instance_filename(items: list[dict]) -> str | None:
    names = [i["name"] for i in items]
    inline = [n for n in names if n.endswith("_htm.xml")]
    if inline:
        return inline[0]
    plain = [n for n in names if n.endswith(".xml") and not n.endswith(_LINKBASE_SUFFIXES)
             and n != "FilingSummary.xml" and not n.startswith("0")]
    return plain[0] if plain else None


def parse_instance(xml_bytes: bytes, *, accn: str, form: str, filed: str) -> dict[str, dict[str, list[dict]]]:
    """Devuelve {namespace_prefix: {tag: [filas estilo companyfacts]}}, con
    la unidad como clave intermedia igual que companyfacts:
    {'us-gaap': {'Revenues': {'units': {'USD': [...]}}}}."""
    root = ET.fromstring(xml_bytes)
    ns_uri_to_prefix = {}
    for prefix, uri in re.findall(rb'xmlns:([\w-]+)="([^"]+)"', xml_bytes[:20000]):
        ns_uri_to_prefix[uri.decode()] = prefix.decode()

    contexts: dict[str, dict] = {}
    for ctx in root.iter(f"{_XBRLI}context"):
        if ctx.find(f"{_XBRLI}entity/{_XBRLI}segment") is not None:
            continue
        period = ctx.find(f"{_XBRLI}period")
        instant = period.find(f"{_XBRLI}instant")
        if instant is not None:
            contexts[ctx.get("id")] = {"end": instant.text.strip()}
        else:
            contexts[ctx.get("id")] = {
                "start": period.find(f"{_XBRLI}startDate").text.strip(),
                "end": period.find(f"{_XBRLI}endDate").text.strip(),
            }

    units: dict[str, str] = {}
    for unit in root.iter(f"{_XBRLI}unit"):
        measures = [m.text.split(":")[-1] for m in unit.iter(f"{_XBRLI}measure")]
        divide = unit.find(f"{_XBRLI}divide")
        units[unit.get("id")] = "/".join(measures) if divide is not None else (measures[0] if measures else "")
    # companyfacts escribe USD/shares como "USD/shares" -- mismo formato.

    fy = fp = None
    out: dict[str, dict[str, dict]] = {}
    for el in root:
        if not isinstance(el.tag, str) or not el.tag.startswith("{"):
            continue
        uri, tag = el.tag[1:].split("}", 1)
        prefix = ns_uri_to_prefix.get(uri, uri)
        if prefix == "dei" and tag == "DocumentFiscalYearFocus":
            fy = int(el.text.strip())
        if prefix == "dei" and tag == "DocumentFiscalPeriodFocus":
            fp = el.text.strip()
        ctx = contexts.get(el.get("contextRef", ""))
        unit = units.get(el.get("unitRef", ""))
        if ctx is None or unit is None or el.text is None:
            continue
        try:
            val = float(el.text.strip())
        except ValueError:
            continue
        if val.is_integer():
            val = int(val)
        row = {**ctx, "val": val, "accn": accn, "form": form, "filed": filed}
        out.setdefault(prefix, {}).setdefault(tag, {"units": {}})["units"].setdefault(unit, []).append(row)

    for tags in out.values():
        for node in tags.values():
            for rows in node["units"].values():
                for r in rows:
                    r["fy"], r["fp"] = fy, fp
    return out


def _merge(facts: dict, prefix: str, tag: str, node: dict) -> None:
    target = facts.setdefault("facts", {}).setdefault(prefix, {}).setdefault(tag, {"units": {}})
    for unit, rows in node["units"].items():
        existing = target["units"].setdefault(unit, [])
        seen = {(r.get("start"), r["end"], r.get("accn")) for r in existing}
        existing.extend(r for r in rows if (r.get("start"), r["end"], r.get("accn")) not in seen)


class AugmentedSecEdgarClient(SecEdgarClient):
    """SecEdgarClient cuyo company_facts() ya viene complementado (ver
    docstring del modulo). `custom_tag_map` = {tag_propio: tag_us_gaap}."""

    def __init__(self, user_agent: str | None = None, *, custom_tag_map: dict[str, str] | None = None,
                 history_10ks: int = 4, tickers: tuple[str, ...] | None = None):
        super().__init__(user_agent)
        # Si se pasa `tickers`, el complemento solo se aplica a esos (p.ej. la
        # empresa valorada, no los peers de la pestaña Sector).
        self.tickers = {t.upper() for t in tickers} if tickers else None
        self.custom_tag_map = custom_tag_map or {}
        self.history_10ks = history_10ks
        self._cache: dict[str, dict] = {}

    def _filing_instance(self, cik: int, accn: str) -> bytes | None:
        folder = f"{_ARCHIVES}/{cik}/{accn.replace('-', '')}"
        index = self._session_get_json(f"{folder}/index.json")
        name = _instance_filename(index["directory"]["item"])
        return self._session_get_bytes(f"{folder}/{name}") if name else None

    def _session_get_json(self, url: str) -> dict:
        return json.loads(self._session_get_bytes(url))

    def _session_get_bytes(self, url: str) -> bytes:
        """GET con cache en disco (las presentaciones archivadas no cambian) y
        reintentos con backoff: /Archives responde 503 ante rafagas de
        pedidos aunque se respete el limite publicado de 10 req/s."""
        cache = _CACHE_DIR / hashlib.sha1(url.encode()).hexdigest()
        if cache.exists():
            return cache.read_bytes()
        for attempt in range(6):
            time.sleep(0.3)
            resp = requests.get(url, headers={"User-Agent": self.user_agent}, timeout=60)
            if resp.status_code in (429, 503) and attempt < 5:
                time.sleep(2 ** attempt * 2)
                continue
            resp.raise_for_status()
            _CACHE_DIR.mkdir(parents=True, exist_ok=True)
            cache.write_bytes(resp.content)
            return resp.content
        raise RuntimeError(f"SEC EDGAR no respondio tras varios reintentos: {url}")

    def company_facts(self, ticker_or_cik: str) -> dict:
        key = str(ticker_or_cik).upper()
        if key in self._cache:
            return self._cache[key]
        facts = super().company_facts(ticker_or_cik)
        if self.tickers is not None and key not in self.tickers:
            return facts
        recent = self.company_submissions(ticker_or_cik)["filings"]["recent"]
        cik = int(facts["cik"])

        latest_filed = max(
            (r["filed"] for ns in facts.get("facts", {}).values() for node in ns.values()
             for rows in node.get("units", {}).values() for r in rows if r.get("form") in ("10-K", "10-Q")),
            default="",
        )
        periodic = [
            (recent["form"][i], recent["filingDate"][i], recent["accessionNumber"][i])
            for i in range(len(recent["form"])) if recent["form"][i] in ("10-K", "10-Q")
        ]
        wanted = [p for p in periodic if p[1] > latest_filed]
        if self.custom_tag_map:
            # 10-K cada 3 anios (3 ejercicios comparativos por 10-K) + los
            # 10-Q de los ultimos ~5 trimestres para poder armar el LTM.
            tenks = [p for p in periodic if p[0] == "10-K"]
            wanted += tenks[: 3 * self.history_10ks : 3]
            wanted += [p for p in periodic if p[0] == "10-Q"][:4]
        seen_accn: set[str] = set()
        for form, filed, accn in wanted:
            if accn in seen_accn:
                continue
            seen_accn.add(accn)
            # Best-effort: si una presentacion no se puede bajar o parsear
            # (503 persistente, instancia con formato raro), se sigue con lo
            # que ya trae companyfacts en vez de tumbar toda la carga.
            try:
                xml = self._filing_instance(cik, accn)
                if not xml:
                    continue
                parsed = parse_instance(xml, accn=accn, form=form, filed=filed)
            except Exception as exc:  # noqa: BLE001
                logger.warning("No se pudo leer la instancia XBRL %s (%s): %s", accn, form, exc)
                continue
            for prefix, tags in parsed.items():
                for tag, node in tags.items():
                    if filed > latest_filed and prefix in ("us-gaap", "dei"):
                        _merge(facts, prefix, tag, node)
                    if tag in self.custom_tag_map and prefix not in ("us-gaap", "dei"):
                        _merge(facts, "us-gaap", self.custom_tag_map[tag], node)
        self._cache[key] = facts
        return facts
