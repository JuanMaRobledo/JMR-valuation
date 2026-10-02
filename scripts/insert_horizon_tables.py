"""Inserta las dos tablas de horizontes (prompts del 2-oct-2026) en la valoración v4 y el research de una empresa.

Uso (desde la raíz del repo, con PYTHONPATH=.:scripts):
    python scripts/insert_horizon_tables.py TICKER SHEET_ID FECHA data/T_Valoracion_...md data/T_Research_...md

Reemplaza la línea «Precio relativo (secundario...» del resumen y la tabla «Valores presentes por método ...
Ponderado opcional» de Resultados; en el research inserta el bloque antes de la sección 13. Es idempotente
(marcadores JMR-HORIZONTES-20261002). Las cifras salen de la hoja (scripts/horizon_tables.py) y se
contrastan con la valoración guardada en ../Modelo-JMR-datos.
"""
import sys, re, json, glob
sys.path.insert(0, 'scripts'); sys.path.insert(0, '.')
import horizon_tables as ht
from jmr_valuation.io.sheets_auth import get_gspread_client

tk, sid, fecha = sys.argv[1], sys.argv[2], sys.argv[3]
val_doc = sys.argv[4] if len(sys.argv) > 4 else None
res_doc = sys.argv[5] if len(sys.argv) > 5 else None
saved = [p for p in glob.glob(f'../Modelo-JMR-datos/valoraciones/{tk}-*.json') if 'regen' not in p][0]
rec = json.load(open(saved))
d = ht.build(ht.grid_cell(ht.read_grid(get_gspread_client().open_by_key(sid))), rec)
MARK = '<!-- JMR-HORIZONTES-20261002 -->'
END = '<!-- /JMR-HORIZONTES-20261002 -->'
E = ht.es
tri = lambda f: ' / '.join(f'US${E(f(s))}' for s in ht.ORDER)


def block(heading):
    return f'{MARK}\n{ht.markdown(d, "US$", fecha, heading)}{END}\n'


def put_block(s, new, before_heading=None, replace_re=None):
    if MARK in s:
        return re.sub(re.escape(MARK) + r'.*?' + re.escape(END) + r'\n', lambda m: new, s, flags=re.S)
    if replace_re:
        s2, n = re.subn(replace_re, lambda m: new, s, count=1, flags=re.S | re.M)
        if n:
            return s2
    i = s.index(before_heading)
    return s[:i] + new + '\n' + s[i:]


summary = (f"Precio relativo (secundario; Base / Conservador / Optimista): múltiplos solos al presente {tri(lambda s: d['hoy'][s]['mult'])} "
           f"y a 3 años sin descontar {tri(lambda s: d['fy3'][s]['mult'])}; ponderado DCF + múltiplos "
           f"({ht.pct(d['peso_dcf'])}/{ht.pct(d['peso_mult'])}, categoría «{d['tipo']}») al presente {tri(lambda s: d['hoy'][s]['pond'])} "
           f"y a 3 años sin descontar {tri(lambda s: d['fy3'][s]['pond'])}, con el DCF capitalizado a FY+3 "
           f"({tri(lambda s: d['fy3'][s]['dcf'])}). Ninguno es valor intrínseco; las dos tablas completas están en «Resultados».")

if val_doc:
    s = open(val_doc).read()
    s, n = re.subn(r'^Precio relativo \(secundario[^\n]*$', lambda m: summary, s, count=1, flags=re.M)
    assert n == 1, 'línea de precio relativo'
    s = put_block(s, block('###'), replace_re=r'^\| Valores presentes por método \|.*?^\| Ponderado opcional[^\n]*\n')
    s = re.sub(r'^Ke de descuento de los múltiplos: ([\d,]+%)\.', r'Ke de descuento de los múltiplos: \1 (cada dividendo descontado en su año de pago).', s, count=1, flags=re.M)
    open(val_doc, 'w').write(s)
    print(val_doc, 'ok', 'opcional' in s)
if res_doc:
    s = open(res_doc).read()
    s = put_block(s, block('###'), before_heading='\n## 13. ')
    open(res_doc, 'w').write(s)
    print(res_doc, 'ok')
print(json.dumps({k: d[k] for k in ('hoy', 'fy3')}, default=str)[:400])
