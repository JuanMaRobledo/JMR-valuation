"""Inserta (o reemplaza) el bloque de las dos tablas de horizontes en el HTML del research de la app, antes de la sección 13."""
import json, re, sys, glob, subprocess, time
sys.path.insert(0, 'scripts'); sys.path.insert(0, '.')
import horizon_tables as ht
from jmr_valuation.io.sheets_auth import get_gspread_client
S = sys.argv.pop(1) if len(sys.argv) > 1 and sys.argv[1].endswith('/') else 'scratchpad/'
c = get_gspread_client()
for tk, sid in json.load(open(S + 'sheets22.json')):
    if sys.argv[1:] and tk not in sys.argv[1:]:
        continue
    rec = json.load(open([p for p in glob.glob(f'../Modelo-JMR-datos/valoraciones/{tk}-*.json') if 'regen' not in p][0]))
    for i in range(4):
        try:
            d = ht.build(ht.grid_cell(ht.read_grid(c.open_by_key(sid))), rec); break
        except ValueError:
            raise
        except Exception:
            time.sleep(45)
    md = ht.markdown(d, 'US$', rec.get('fecha') if re.match(r'\d{4}-\d\d-\d\d', str(rec.get('fecha'))) else '2026-10-02', '###')
    html = subprocess.check_output(['node', '-e', f"""const fs=require('fs'),vm=require('vm');const x={{}};vm.createContext(x);vm.runInContext(fs.readFileSync('{S}marked.min.js','utf8'),x);process.stdout.write(x.marked.parse(fs.readFileSync(0,'utf8'),{{gfm:true,breaks:false}}));"""], input=md.encode()).decode()
    blk = f'<div id="{tk.lower()}-horizontes-20261002">\n{html}</div>\n'
    ps = glob.glob(f'../Modelo-JMR-datos/analisis/{tk}-research-*.json')
    if not ps:
        print(tk, 'sin research en la app'); continue
    p = ps[0]; j = json.load(open(p)); h = j['html']
    pat = re.compile(rf'<div id="{tk.lower()}-horizontes-20261002">.*?</div>\n', re.S)
    if pat.search(h):
        h = pat.sub(lambda m: blk, h)
    else:
        m = re.search(r'<h2[^>]*>\s*13\. ', h)
        if not m:  # sin sección 13: al final de la sección 12 (antes del h2 siguiente)
            m12 = re.search(r'<h2[^>]*>\s*12\. ', h)
            m = re.compile(r'<h2[^>]*>').search(h, m12.end()) if m12 else None
        if not m:
            print(tk, 'SIN sección 12/13'); continue
        h = h[:m.start()] + blk + h[m.start():]
    j['html'] = h
    open(p, 'w').write(json.dumps(j, ensure_ascii=False, indent=2) + '\n')
    print(tk, 'ok', round(d['hoy']['base']['pond'], 2), round(d['fy3']['base']['pond'], 2))
    time.sleep(2)
