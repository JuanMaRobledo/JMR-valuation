"""Actualiza en la valoración v4 las partes mecánicas que dependen de los múltiplos (tabla de anclas §6, tabla de
resultados §7, línea de múltiplos ±20% en §9 y crecimiento implícito en §11) desde los archivos vigentes."""
import json, re, sys, glob
sys.path.insert(0, 'scripts')
from horizon_tables import es
tk, doc_p = sys.argv[1], sys.argv[2]
doc = open(doc_p).read()
V = json.load(open([p for p in glob.glob(f'../Modelo-JMR-datos/valoraciones/{tk}-*.json') if 'regen' not in p][0]))
DR = json.load(open(f'reference/multiplos_v3/{tk}_decision_resultado.json'))['resultado']
CI = json.load(open(f'reference/multiplos_v3/{tk}_crecimiento.json'))
rep = open(f'data/{tk}_Valoracion_Modelo_JMR_2026-09-30.md').read()
dm = V['descuentoMultiples']
# §6 tabla de anclas: columnas C (justificado), Conservador, Base, Optimista y peers ajustados
def fix(line):
    m = re.match(r"\| (EV/EBITDA|EV/FCFF|P/E|P/FCFE|P/OCF) \|", line)
    if not m or line.count('|') != 9:
        return line
    x = DR[m.group(1)]; c = line.split('|')
    c[5] = f" {es(x['C']['Base'],1)}× "; c[6] = f" {es(x['conservador'],1)}× "; c[7] = f" {es(x['base'],1)}× "; c[8] = f" {es(x['optimista'],1)}× "
    if x.get('B_mediana') is not None:
        c[4] = re.sub(r"[\d,]+× → [\d,]+×", f"{es(x['B_mediana'],1)}× → {es(x['B_ajustada'],1)}×", c[4], count=1)
        c[4] = re.sub(r"^ Mediana [\d,]+×", f" Mediana {es(x['B_mediana'],1)}×", c[4]) if '→' not in c[4] else c[4]
    return '|'.join(c)
s6a = doc.index('## 6. '); s6b = doc.index('## 7. ')
doc = doc[:s6a] + '\n'.join(fix(l) for l in doc[s6a:s6b].split('\n')) + doc[s6b:]
# §7 tabla de detalle Base
rows = [f"| {x['nombre']} | " + " | ".join(es(v) for v in x['base']['fy']) + " | " + " | ".join(es(v) for v in x['base']['vp']) + f" | {es(x['base']['consolidado'])} |" for x in dm['metodos']]
cb = dm['consolidado']['base']
tbl = "\n".join(rows) + "\n| **Consolidado** | " + " | ".join(es(v) for v in cb['fy']) + " | " + " | ".join(es(v) for v in cb['vp']) + f" | **{es(cb['consolidado'])}** |\n"
doc = re.sub(r"(\| Método \(Base\) \| Precio \+ dividendos FY\+1[^\n]*\n\|[^\n]*\n)(?:\|[^\n]*\n){6}", lambda q: q.group(1) + tbl, doc, count=1)
doc = re.sub(r"Chequeo VP a 3 años < FY\+3 sin descontar: OK en los tres casos \(Base [\d,]+ < [\d,]+\)",
             f"Chequeo VP a 3 años < FY+3 sin descontar: OK en los tres casos (Base {es(dm['chequeo']['multiplosVP3']['base'])} < {es(dm['chequeo']['multiplosFY3SinDescontar']['base'])})", doc)
# §9 múltiplos ±20% (ponderado DCF + múltiplos Base hoy, del informe de la app)
lo = re.search(r'\| Múltiplos Base −20% \| (US\$[\d.,]+)', rep).group(1)
hi = re.search(r'\| Múltiplos Base \+20% \| (US\$[\d.,]+)', rep).group(1)
new9 = "| Múltiplos ±20% (ponderado DCF + múltiplos Base hoy) | " + lo + " | " + hi + " |"
doc = re.sub(r"\| Múltiplos ±20% \([^)]*\) \| US\$[\d.,]+ \| US\$[\d.,]+ \|", lambda q: new9, doc)
# §11 crecimiento implícito de los múltiplos
pc = lambda x: es(x*100, 1) + '%'
ig = {x['metodo']: x for x in CI['multiplos']}
txt = "Crecimiento implícito de los múltiplos Base frente al del DCF en FY+3: " + "; ".join(f"{k} {pc(ig[k]['gImplicito'])} frente a {pc(ig[k]['gDcf'])}" for k in ('EV/EBITDA','EV/FCFF','P/E','P/FCFE','P/OCF') if ig.get(k) and ig[k].get('gImplicito') is not None and ig[k].get('gDcf') is not None) + "."
doc = re.sub(r"Crecimiento implícito de los múltiplos Base frente al del DCF en FY\+3: [^.]*(?:\.\d[^.]*)*?\.(?= )", lambda q: txt, doc, count=1)
open(doc_p, 'w').write(doc)
print(tk, 'ok', {k: round(DR[k]['base'], 1) for k in DR}, 'mult hoy', round(dm['multiplesHoy']['base'], 2))
