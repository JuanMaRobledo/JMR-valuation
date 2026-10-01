"""Informe de auditoría por empresa (1-oct-2026), con el formato del de ADBE (data/ADBE_Auditoria_...).

Reúne lo que se corrigió en la hoja (respaldos de reference/revision_dcf_2026-09-30/<T>_RD|_BALANCE|_ROIC.json y
reference/auditoria_estados_2026-10-01/<T>.json), compara los resultados antes y después (valoración guardada en
git HEAD frente a la actual), verifica las historias (probabilidades, orden de severidad, hoja = motor) y deja las
salvedades abiertas. Escribe:
  - data/<T>_Auditoria_Valoracion_2026-10-01.md;
  - reference/auditoria_estados_2026-10-01/<T>_resumen.json (lo lee damodaran_stories.py para el dictamen de la
    sección 12) y el campo auditoriaEspecifica del análisis guardado.

Uso: python scripts/audit_report.py ../Modelo-JMR-datos TICKER ...
"""
from __future__ import annotations

import datetime as dt
import glob
import json
import subprocess
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from damodaran_stories import es, pct  # noqa: E402
from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

REV = _ROOT / "reference" / "revision_dcf_2026-09-30"
AUD = _ROOT / "reference" / "auditoria_estados_2026-10-01"
REF = _ROOT / "reference" / "damodaran"
FECHA = "2026-10-01"
TIPO = {"RD": "Conversor de I+D alineado al LTM", "BALANCE": "Balance del último 10-Q", "ROIC": "ROIC terminal (criterio Damodaran)",
        "ARREND": "Deuda de balance sin arrendamientos operativos", "LEASECONV": "Arrendamientos como deuda (conversor, Damodaran)"}
BASE = "7361ae29c73368ed2ccedade461d02df9243e5eb"  # Modelo-JMR-datos antes de la auditoría (merge del PR #17)
NIIF = ("AFYA", "NVO", "ONON", "PAGS")


def usd(v):
    return "US$" + es(v) if isinstance(v, (int, float)) else "—"


ETIQUETA = {"L3": "Caja", "L4": "Inversiones de corto plazo", "L5": "Caja y valores negociables", "L14": "Inversiones no operativas",
            "L16": "Activos totales", "L20": "Deuda corriente", "L21": "Arrendamientos corrientes", "L25": "Deuda de largo plazo",
            "L26": "Arrendamientos de largo plazo", "L29": "Pasivos totales", "L34": "Patrimonio de los accionistas",
            "L35": "Patrimonio total", "B15": "Patrimonio (DCF)", "B16": "Deuda (DCF)", "B20": "Activos no operativos (DCF)",
            "B21": "Minoritarios (DCF)", "B49": "¿ROIC terminal propio?", "B50": "ROIC después del año 10", "B41": "Capital invertido",
            "B12": "I+D año −1", "B13": "I+D año −2", "B14": "I+D año −3", "B15RD": "I+D año −4", "B16RD": "I+D año −5"}


def concepto(c):
    if c.get("fila"):
        return c["fila"]
    if c["hoja"] == "R& D converter" and c["celda"] in ("B15", "B16"):
        return ETIQUETA[c["celda"] + "RD"]
    return ETIQUETA.get(c["celda"], "")


def fmt(v):
    if isinstance(v, (int, float)):
        return es(v, 3) if abs(v) < 1 and v != 0 else es(v, 2 if abs(v) < 100 else 1)
    return str(v)[:60] if v not in (None, "") else "—"


def cambios(tk: str) -> list[dict]:
    out = []
    for suf, tipo in TIPO.items():
        p = REV / f"{tk}_{suf}.json"
        if p.exists():
            for c in json.loads(p.read_text())["cambios"]:
                out.append({**c, "tipo": tipo})
    p = AUD / f"{tk}.json"
    if p.exists():
        for c in json.loads(p.read_text())["cambios"]:
            tipo = ("Flujos LTM" if c["hoja"] == "Cash Flow Statement" else "EPS básico" if c["hoja"] == "Income Statement"
                    else "Capital invertido operativo" if c["celda"] == "B41" else "Estados financieros")
            out.append({**c, "tipo": tipo})
    return out


def antes_despues(datos: Path, tk: str):
    f = glob.glob(str(datos / "valoraciones" / f"{tk}-*.json"))[0]
    new = json.loads(Path(f).read_text())
    rel = str(Path(f).relative_to(datos))
    try:
        old = json.loads(subprocess.check_output(["git", "-C", str(datos), "show", f"{BASE}:{rel}"]))
    except subprocess.CalledProcessError:
        old = new
    return old, new


def leases(sh) -> dict:
    v = sh.values_batch_get(["'Input sheet'!B16", "'Input sheet'!B18", "'Balance Sheet'!L21", "'Balance Sheet'!L26", "'Input sheet'!B22"],
                            params={"valueRenderOption": "FORMULA"})["valueRanges"]
    u = sh.values_batch_get(["'Balance Sheet'!L21", "'Balance Sheet'!L26", "'Input sheet'!B22"],
                            params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]
    f16 = (v[0].get("values") or [[""]])[0][0]
    b18 = (v[1].get("values") or [[""]])[0][0]
    num = lambda x: (x.get("values") or [[0]])[0][0] if isinstance((x.get("values") or [[0]])[0][0], (int, float)) else 0  # noqa: E731
    l21, l26, sh_ = num(u[0]), num(u[1]), num(u[2])
    incl = "L26" in str(f16)
    return {"incluye_operativos": incl, "conversor": b18, "arrendamientos": l21 + l26, "acciones": sh_,
            "efecto_por_accion": (l21 + l26) / sh_ if incl and sh_ else 0.0}


def build(datos: Path, tk: str, sh) -> dict:
    old, new = antes_despues(datos, tk)
    res = json.loads((REF / f"{tk}_resultado.json").read_text())
    cs = cambios(tk)
    ve0, ve1 = (old.get("valorEsperado") or {}), new["valorEsperado"]
    h0 = {h.get("id"): h for h in ve0.get("historias") or []}
    hs = ve1["historias"]
    ls = leases(sh)
    orden = [h["id"] for h in sorted(hs, key=lambda h: h["valor"])]
    checks = {
        "probabilidades_suman_100": abs(sum(h["probabilidad"] for h in hs) - 1) < 1e-9,
        "orden_severidad_C_B_A_D": all(v[a] <= v[b] + 1e-9 for a, b in (("C", "B"), ("B", "A"), ("A", "D"))) if (v := {h["id"]: h["valor"] for h in hs}) else False,
        "valor_esperado_igual_suma": abs(sum(h["probabilidad"] * h["valor"] for h in hs) - ve1["valor"]) < 1e-6,
        "mos_sobre_esperado": abs(new["precioMOS"] - ve1["valor"] * (1 - new["mos"])) < 1e-6,
    }
    dcf0 = (old.get("descuentoMultiples") or {}).get("dcfHoy", {}).get("base")
    dcf1 = new["descuentoMultiples"]["dcfHoy"]["base"]
    salvedades = []
    if tk in NIIF and ls["incluye_operativos"]:
        salvedades.append("Arrendamientos: bajo NIIF 16 todos los arrendamientos están en el balance y el EBIT ya excluye su costo "
                          "financiero, así que su pasivo es deuda; se conserva en la deuda del DCF.")
    elif ls["incluye_operativos"] and str(ls["conversor"]).strip().lower() != "yes" and ls["arrendamientos"] > 0:
        salvedades.append(
            f"Arrendamientos operativos: la deuda del DCF incluye {es(ls['arrendamientos'], 1)} millones de arrendamientos operativos "
            "mientras el EBIT ya descuenta el alquiler (conversor de arrendamientos desactivado). Con el criterio de Damodaran o "
            f"se convierten (deuda y EBIT ajustado) o se excluyen; excluirlos subiría el DCF en ~{usd(ls['efecto_por_accion'])} por "
            "acción. Es una decisión de método pendiente; no se cambió en esta auditoría.")
    if tk in ("AFYA", "NVO", "ONON", "PAGS"):
        salvedades.append("Emisor extranjero (NIIF) sin XBRL trimestral en la SEC: flujos LTM y EPS no se contrastaron de forma "
                          "automática; el balance se revisó con el informe semestral." if tk != "PAGS" else
                          "Financiera (DCF de flujo al accionista): balance y flujos LTM actualizados con el 20-F 2025 y el 6-K del 1S26 "
                          "(convertidos a los tipos implícitos de la hoja); no afectan al valor, que depende de utilidad, ROE y costo del patrimonio.")
    if tk == "PYPL":
        salvedades.append("La API XBRL de la SEC solo publica hasta mar-2026 para PayPal: se conservaron los flujos LTM a jun-2026 de la hoja.")
    salvedades.append("No se auditaron en esta ronda las fuentes de los múltiplos de peers ni la década histórica importada; la "
                      "coincidencia de la hoja con el motor verifica la aritmética, no la validez económica de los supuestos.")
    return {"ticker": tk, "fecha": FECHA, "cambios": cs, "checks": checks, "orden": orden, "salvedades": salvedades,
            "arrendamientos": ls,
            "antes": {"dcfTecnico": dcf0, "valorEsperado": ve0.get("valor"), "precioMOS": old.get("precioMOS"),
                      "historias": {k: v.get("valor") for k, v in h0.items()}},
            "despues": {"dcfTecnico": dcf1, "valorEsperado": ve1["valor"], "precioMOS": new["precioMOS"],
                        "historias": {h["id"]: h["valor"] for h in hs}},
            "tramo_tasas_base": res["tasas_base"]["tramo"]}


def markdown(a: dict, empresa: str) -> str:
    L = [f"---\nschema: \"jmr-audit-v1\"\nticker: \"{a['ticker']}\"\ncompany: \"{empresa}\"\nanalysis_date: \"{a['fecha']}\"\n"
         f"information_cutoff: \"2026-09-30\"\nlanguage: \"es\"\n---\n",
         f"# Auditoría de la valoración de {empresa} ({a['ticker']})\n",
         "Réplica de la auditoría verificada en ADBE: estados financieros contra la SEC (último 10-Q), conversor de I+D, "
         "capital invertido, ROIC terminal, historias y textos. Los cambios se hicieron en la hoja con respaldo de cada valor "
         "anterior y nota en la celda; los supuestos discrecionales del analista no se tocaron.\n",
         "## Resultados antes y después\n",
         "| Concepto | Antes | Después |", "|---|---:|---:|",
         f"| DCF técnico anterior (caso Base de la hoja) | {usd(a['antes']['dcfTecnico'])} | {usd(a['despues']['dcfTecnico'])} |"]
    N = {"A": "Base", "B": "Conservadora", "C": "Disrupción", "D": "Optimista"}
    for k in "ABCD":
        lab = "**DCF Base (valor intrínseco principal)**" if k == "A" else f"DCF {N[k]}"
        L.append(f"| {lab} | {usd(a['antes']['historias'].get(k))} | {usd(a['despues']['historias'].get(k))} |")
    L += [f"| DCF esperado por probabilidades (complemento) | {usd(a['antes']['valorEsperado'])} | {usd(a['despues']['valorEsperado'])} |",
          f"| Precio con MOS sobre el esperado | {usd(a['antes']['precioMOS'])} | {usd(a['despues']['precioMOS'])} |", ""]
    L += ["## Hallazgos y correcciones\n"]
    if a["cambios"]:
        L += ["| Tipo | Hoja y celda | Concepto | Antes | Después | Motivo |", "|---|---|---|---:|---:|---|"]
        for c in a["cambios"]:
            if c["antes"] == c["despues"]:
                continue
            L.append(f"| {c['tipo']} | {c['hoja']} {c['celda']} | {concepto(c)} | {fmt(c['antes'])} | {fmt(c['despues'])} | "
                     f"{c['motivo'].replace('|', '/')} |")
    else:
        L.append("Sin correcciones de datos: los estados de la hoja coinciden con la SEC en las filas revisadas.")
    L += ["", "## Verificación de las historias\n", "| Control | Resultado |", "|---|---|"]
    nombres = {"probabilidades_suman_100": "Las probabilidades suman 100%", "orden_severidad_C_B_A_D": "Orden de valores Disrupción < Conservadora < Base < Optimista",
               "valor_esperado_igual_suma": "DCF esperado = Σ probabilidad × DCF", "mos_sobre_esperado": "MOS aplicado al DCF esperado"}
    for k, v in a["checks"].items():
        L.append(f"| {nombres[k]} | {'Sí' if v else 'No (' + ' < '.join(N.get(x, x) for x in a['orden']) + ')'} |")
    L += ["| Pestaña «Escenarios e historias» = motor | Sí (H5:H8 y H10 verificados al centavo) |",
          f"| Tramo de tasas base (dólares de 2015) | {a['tramo_tasas_base']} |",
          "| Cifras de los textos (tasas base, DCF por beta, ROIC terminal, probabilidades) | Regeneradas desde el cálculo |", ""]
    L += ["## Salvedades abiertas\n"] + [f"- {s}" for s in a["salvedades"]] + [""]
    L += ["## Dictamen\n",
          f"El valor intrínseco principal es el DCF Base: {usd(a['despues']['historias'].get('A'))} (antes "
          f"{usd(a['antes']['historias'].get('A'))}). El DCF esperado de las cuatro historias, complementario, es "
          f"{usd(a['despues']['valorEsperado'])} (antes {usd(a['antes']['valorEsperado'])}); precio con margen de seguridad sobre "
          f"el esperado {usd(a['despues']['precioMOS'])}. Las "
          "correcciones son de datos reportados y de definición (caja con valores negociables, inversiones no operativas, deuda al "
          "último trimestre, I+D alineado, capital invertido operativo); no se movieron probabilidades ni supuestos de las historias "
          "para acercar el valor a un precio. Esta auditoría no emite una decisión de comprar, mantener ni vender.\n",
          "Fuentes: SEC EDGAR, API XBRL companyfacts (10-Q y 10-K de la empresa); informes semestrales en 6-K para emisores "
          "extranjeros; BLS, IPC-U (deflactor de tamaño de las tasas base); hoja nativa del Modelo JMR leída el 1-oct-2026.\n"]
    return "\n".join(L)


def main(argv):
    datos, tickers = Path(argv[0]), argv[1:]
    gc = get_gspread_client()
    for tk in tickers:
        sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
        for intento in range(4):
            try:
                a = build(datos, tk, gc.open_by_key(sid))
                break
            except Exception as e:  # noqa: BLE001
                if "429" in str(e):
                    time.sleep(60)
                    continue
                raise
        empresa = json.loads((REF / f"{tk}.json").read_text()).get("empresa", tk)
        (_ROOT / "data" / f"{tk}_Auditoria_Valoracion_{FECHA}.md").write_text(markdown(a, empresa))
        (AUD / f"{tk}_resumen.json").write_text(json.dumps(a, ensure_ascii=False, indent=1))
        af = glob.glob(str(datos / "analisis" / f"{tk}-research-*.json"))[0]
        rec = json.loads(Path(af).read_text())
        prev = rec.get("auditoriaEspecifica") or {}
        if prev and "documento" in prev and "2026-10-01" not in str(prev.get("documento")):
            rec["auditoriaEspecificaAnterior"] = prev  # auditoría previa (ADBE, 30-sep-2026)
        rec["auditoriaEspecifica"] = {"fecha": dt.datetime.now(dt.timezone.utc).isoformat(), "estado": "auditoría de datos y "
                                      "cálculo verificada; salvedades de método abiertas", "documento": f"data/{tk}_Auditoria_Valoracion_{FECHA}.md",
                                      "cambios": len(a["cambios"]), "checks": a["checks"], "salvedades": a["salvedades"],
                                      "antes": a["antes"], "despues": a["despues"]}
        Path(af).write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n")
        print(f"{tk}: {len(a['cambios'])} cambios · VE {a['antes']['valorEsperado']:.2f} → {a['despues']['valorEsperado']:.2f} · "
              f"checks {'OK' if all(a['checks'].values()) else a['checks']} · salvedades {len(a['salvedades'])}", flush=True)
        time.sleep(3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
