"""Consistencia de la app con el motor (3-oct-2026): 16 controles por empresa entre el último cálculo de las historias
(reference/damodaran/<T>_resultado.json), la valoración guardada, el research de la app y la auditoría de estados.

Se corre al final de scripts/regenerar_cartera.sh. Uso: python scripts/consistencia_app.py [TICKER ...]
Sale con 1 si algún control falla.
"""
import glob
import json
import re
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
R = str(_ROOT / "reference") + "/"
D = str(_ROOT.parent / "Modelo-JMR-datos") + "/"
es = lambda v: f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")  # noqa: E731
T = sys.argv[1:] or sorted(json.load(open(R + "cartera_drive.json"))["empresas"])
fallos = 0
for t in T:
    r=json.load(open(R+f"damodaran/{t}_resultado.json")); hs={h["id"]:h for h in r["historias"]}
    v=json.load(open(glob.glob(D+f"valoraciones/{t}-*.json")[0])); ve=v["valorEsperado"]
    a=json.load(open(glob.glob(D+f"analisis/{t}-research-*.json")[0])); h=a["html"]; lv=a["linkedValuation"]
    aud=json.load(open(R+f"auditoria_estados_2026-10-01/{t}_resumen.json"))
    A=hs["A"]["valor_beta_hoja"]; E=r["valor_esperado_beta_hoja"]; mos=v["mos"]
    c={
     "ve=resultado": abs(ve["valor"]-E)<1e-6,
     "central=A": abs(ve["valorCentral"]-A)<1e-6,
     "probs=100": abs(sum(x["probabilidad"] for x in ve["historias"])-1)<1e-9,
     "ve=suma": abs(sum(x["probabilidad"]*x["valor"] for x in ve["historias"])-ve["valor"])<1e-6,
     "principal=valorCentral": v["escenariosDCF"]["principal"]=="valorEsperado.valorCentral",
     "MOS sobre esperado": abs(v["precioMOS"]-E*(1-mos))<1e-6,
     "metodo Base": ve["metodo"].startswith("DCF Base"),
     "nombres sin letra": all(not re.match(r"^[A-D] ·",x["nombre"]) for x in ve["historias"]),
     "link=valoracion": abs(lv["valorEsperado"]["valor"]-E)<1e-6 and abs(lv["valorEsperado"]["valorCentral"]-A)<1e-6,
     "bloque Base primero": f"Valor intrínseco principal · DCF Base hoy: US${es(A)}" in h and h.find("Valor intrínseco principal · DCF Base hoy")<h.find("DCF esperado por probabilidades"),
     "seccion12 Base primero": h.count(f"Valor intrínseco principal · DCF Base hoy: US${es(A)} por acción")>=2,
     "justificacion": f'id="{t.lower()}-justificacion"' in h and "Sensibilidad del DCF Base" in h,
     "tabla multiplos": "<th>Base · múltiplo</th><th>Base · US$/acción hoy</th><th>Conservadora · múltiplo</th>" in h,
     "sin control pendiente": "Control pendiente:" not in h,
     "seccion10": "El DCF Base es el valor intrínseco principal" in h,
     "auditoria=resultado": abs(aud["despues"]["valorEsperado"]-E)<0.005 and abs(aud["despues"]["historias"]["A"]-A)<0.005,
    }
    bad=[k for k,x in c.items() if not x]; fallos+=len(bad)
    print(f"{t:5s} {len(c)-len(bad)}/{len(c)}", bad or "")
print("FALLOS", fallos)
sys.exit(1 if fallos else 0)
