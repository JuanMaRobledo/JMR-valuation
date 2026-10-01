"""Verifica (y con --fix corrige) las cifras escritas a mano en las fichas de historias (reference/damodaran/<T>.json)
contra el resultado calculado (<T>_resultado.json) y el criterio de ventaja competitiva (moat_2026-09-30.json).

Cifras que se regeneran desde el cálculo, para que el texto no quede desactualizado cuando cambia el modelo:
  - tasas base: la frase «crecer X% anual (Base) lo logró ~Y%» y el tramo de tamaño (dólares de 2015);
  - riesgo: «el DCF Base sube/baja de US$a a US$b» (DCF con la beta de la hoja y con la bottom-up o la propuesta);
  - reinversión: «El ROIC después del año 10 es X%»;
  - probabilidades «Base (NN%)» del texto de probabilidades.
Informa además los importes en US$ de los demás textos que no coinciden con ningún valor calculado.

Uso: python scripts/verify_story_texts.py [--fix] TICKER ...
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from damodaran_stories import NOMBRE, REF, _ROOT, es  # noqa: E402

MOAT = json.loads((_ROOT / "reference" / "moat_2026-09-30.json").read_text())["empresas"]


def tramo_es(t: str) -> str:
    t = t.replace(" Mn", "")
    if t.startswith(">"):
        return "de más de US$" + t[2:].replace(",", ".") + " millones"
    lo, hi = t.strip("$").split("-")
    return f"de US${lo.replace(',', '.')}-{hi.replace(',', '.')} millones"


def frase_tasas(r: dict) -> str:
    br, hs = r["tasas_base"], {h["id"]: h for h in r["historias"]}
    a, d = hs["A"], hs["D"]
    return (f"En dólares de 2015 la empresa está en el tramo {tramo_es(br['tramo'])}: crecer {es(a['cagr'] * 100, 1)}% anual "
            f"cinco años (Base) lo logró ~{es(a['tasa_base'] * 100, 0)}% de las empresas de ese tamaño; "
            f"{es(d['cagr'] * 100, 1)}% (Optimista), ~{es(d['tasa_base'] * 100, 0)}%.")


_X = r"(?:[^.]|(?<=\d)\.(?=\d))"  # cualquier carácter salvo el punto final de una oración (admite «US$4.500»)
_H = r"\((?:historia )?(?:[A-D]|Base|Conservadora|Disrupción|Optimista)\)"
ORACION_TASAS = re.compile(rf"(?:Para|Entre las) empresas de {_X}*?(?:{_H}|mediana){_X}*\.(?:\s*Crecer {_X}*{_H}{_X}*\.)?")


def fix_tasas(spec, r, fixes):
    t = spec.get("tasas_base_nota", "")
    nueva = frase_tasas(r)
    if nueva in t:
        return
    def resto(m):
        """Conserva el comentario del analista que sigue a la cifra («…lo logró ~64%: la hoja es realista»)."""
        s_ = m.group(0)
        ult = list(re.finditer(r"~\d+%(?: de las empresas)?", s_))
        if not ult:
            return ""
        cola = s_[ult[-1].end():].lstrip()
        if cola[:1] in ":;":
            cola = cola[1:].strip()
            return " " + cola[:1].upper() + cola[1:] + " "
        return " "
    t2, n = ORACION_TASAS.subn(resto, t, count=1)
    t2 = re.sub(r"^En dólares de 2015 la empresa está en el tramo [^.]*\.[^.]*?\((?:historia D|Optimista)\), ~\d+%\.\s*", "", t2)
    spec["tasas_base_nota"] = re.sub(r"\s{2,}", " ", (nueva + " " + t2.strip()).strip())
    fixes.append(("tasas_base_nota", t[:120], spec["tasas_base_nota"][:160]))


def fix_riesgo(spec, r, fixes):
    t = spec.get("riesgo", {}).get("texto", "")
    b = r["betas"]
    if len(b) < 2:
        return
    v0, v1 = b[0]["dcf_base"], b[-1]["dcf_base"]
    verbo = "sube" if v1 > v0 else "baja"

    def rep(m):
        return f"el DCF Base {verbo} de US${es(v0)} a US${es(v1)}"
    t2 = re.sub(r"el DCF Base (?:sube|baja) de US\$\d[\d.]*,\d{2} a US\$\d[\d.]*,\d{2}", rep, t)
    t2 = re.sub(r"\(US\$\d[\d.]*,\d{2} frente a US\$\d[\d.]*,\d{2}\)", f"(US${es(v0)} frente a US${es(v1)})", t2)
    t2 = re.sub(r"\(US\$\d[\d.]*,\d{2} → US\$\d[\d.]*,\d{2}\)", f"(US${es(v0)} → US${es(v1)})", t2)
    if r.get("beta_bu"):  # beta bottom-up reapalancada (cambia con la deuda, incluidos los arrendamientos)
        t2 = re.sub(r"(reapalancada[^.]*? da )\d,\d\d", lambda m_: m_.group(1) + es(r["beta_bu"]), t2, count=1)
    if t2 != t:
        spec["riesgo"]["texto"] = t2
        fixes.append(("riesgo", re.findall(r"US\$[\d.,]+", t), re.findall(r"US\$[\d.,]+", t2)))


def fix_roic(spec, tk, fixes):
    m = MOAT.get(tk) or {}
    rt = m.get("roic_terminal")
    blk = spec.get("reinversion") or {}
    t = blk.get("texto", "")
    if rt is None or "ROIC después del año 10 es" not in t:
        return
    nuevo = es(rt * 100, 1) + "%"
    t2 = re.sub(r"(El ROIC después del año 10 es )[\d,]+%", lambda m_: m_.group(1) + nuevo, t)
    if t2 != t:
        blk["texto"] = t2
        fixes.append(("reinversion.ROIC", re.findall(r"año 10 es [\d,]+%", t), nuevo))


def check_probs(spec, r, issues):
    probs = {NOMBRE[h["id"]]: round(h["prob"] * 100) for h in r["historias"]}
    for letra, pct in re.findall(r"\b(Base|Conservadora|Disrupción|Optimista) (?:es la más probable )?\((\d+)%\)", spec.get("prob_texto", "")):
        if int(pct) != probs.get(letra):
            issues.append(f"prob_texto: {letra} dice {pct}% y la historia tiene {probs.get(letra)}%")


def check_importes(spec, r, issues):
    vals = {round(r["dcf_base"], 2), round(r["valor_esperado_beta_hoja"], 2), round(r["valor_esperado_beta_prop"], 2)}
    vals |= {round(h["valor_beta_hoja"], 2) for h in r["historias"]} | {round(h["valor_beta_prop"], 2) for h in r["historias"]}
    vals |= {round(b["dcf_base"], 2) for b in r["betas"]}
    for campo in ("precio_lectura", "contra", "prob_texto"):
        for m in re.finditer(r"(DCF[^.;]{0,40}?|historia (?:Base|Conservadora|Disrupción|Optimista)[^.;]{0,20}?)\(US\$([\d.]+,\d{2})\)", spec.get(campo, "")):
            v = float(m.group(2).replace(".", "").replace(",", "."))
            if v not in vals:
                issues.append(f"{campo}: «{m.group(0)[:70]}» no coincide con ningún valor calculado")


def main(argv):
    fix = "--fix" in argv
    for tk in [a for a in argv if not a.startswith("--")]:
        p = REF / f"{tk}.json"
        spec = json.loads(p.read_text())
        r = json.loads((REF / f"{tk}_resultado.json").read_text())
        fixes, issues = [], []
        fix_tasas(spec, r, fixes)
        fix_riesgo(spec, r, fixes)
        fix_roic(spec, tk, fixes)
        check_probs(spec, r, issues)
        check_importes(spec, r, issues)
        print(f"{tk}: {len(fixes)} cifras regeneradas, {len(issues)} avisos")
        for f in fixes:
            print("   ·", f)
        for i in issues:
            print("   !", i)
        if fix and fixes:
            p.write_text(json.dumps(spec, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
