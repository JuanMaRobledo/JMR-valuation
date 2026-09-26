"""Regenera una valoracion guardada del visor (Modelo-JMR-datos) desde la
hoja corregida: exporta el xlsx, lo carga en docs/visor.html (Playwright),
pulsa "Guardar" e intercepta el PUT a GitHub para quedarse con el JSON."""
import sys, json, base64, threading, http.server, functools, os, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import requests, google.auth.transport.requests as tr
from jmr_valuation.io.sheets_auth import get_gspread_client
from playwright.sync_api import sync_playwright

DOCS = os.environ.get('MODELO_JMR_DOCS', str(Path(__file__).resolve().parents[2] / 'Modelo-JMR' / 'docs'))
SHEETJS = os.environ.get('SHEETJS_PATH', 'xlsx.full.min.js')  # copia local de cdnjs xlsx 0.18.5
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
def serve():
    h = functools.partial(Quiet, directory=DOCS)
    s = http.server.ThreadingHTTPServer(('127.0.0.1', 8765), h)
    threading.Thread(target=s.serve_forever, daemon=True).start()
    return s

def export_xlsx(sid, path):
    c = get_gspread_client(); cr = c.http_client.auth; cr.refresh(tr.Request())
    r = requests.get(f"https://docs.google.com/spreadsheets/d/{sid}/export?format=xlsx", headers={"Authorization": "Bearer " + cr.token})
    r.raise_for_status(); open(path, 'wb').write(r.content)

def regen(sid, xlsx, page):
    captured = {}
    def gh(route):
        req = route.request
        if req.method == 'PUT':
            captured['body'] = json.loads(req.post_data)
            route.fulfill(status=201, content_type='application/json', body='{"content":{}}')
        else:
            route.fulfill(status=200, content_type='application/json', body='[]')
    page.route("**/api.github.com/**", gh)
    page.route("**/xlsx.full.min.js", lambda r: r.fulfill(path=SHEETJS, content_type='application/javascript'))
    page.goto('http://127.0.0.1:8765/visor.html')
    page.set_input_files('#fileInput', xlsx)
    page.wait_for_selector('#saveValBtn', state='attached', timeout=60000)
    page.wait_for_timeout(1500)
    page.click('#saveValBtn')
    page.wait_for_function("document.getElementById('saveStatus') && /Guardada|Error/.test(document.getElementById('saveStatus').textContent)", timeout=60000)
    status = page.eval_on_selector('#saveStatus', 'e => e.textContent')
    body = captured['body']
    rec = json.loads(base64.b64decode(body['content']).decode('utf-8'))
    return rec, status

if __name__ == '__main__':
    # Uso: python scripts/regen_saved_valuations.py '[["<sheet_id>", "../Modelo-JMR-datos/valoraciones/X.json"], ...]'
    # Deja X.regen.json al lado; revisar y reemplazar a mano (se conservan analisisFundamental y Cualitativo).
    pairs = json.loads(sys.argv[1])
    srv = serve()
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get('CHROMIUM_PATH') or None)
        for sid, saved in pairs:
            xlsx = os.path.join(tempfile.gettempdir(), f'{sid}.xlsx')
            export_xlsx(sid, xlsx)
            ctx = b.new_context()
            ctx.add_init_script("localStorage.setItem('jmr-auth-ok-v1','1');localStorage.setItem('jmr-gh-datastore-token','x');")
            page = ctx.new_page()
            rec, status = regen(sid, xlsx, page)
            old = json.load(open(saved))
            # se conservan el analisis fundamental y la fecha/precio del analisis original
            for k in ('analisisFundamental',):
                if old.get(k) is not None:
                    rec[k] = old[k]
            # el Cualitativo guardado puede tener ediciones hechas en el visor: se conserva
            oc = (old.get('hojas') or {}).get('analisis', {}).get('Cualitativo')
            if oc and rec.get('hojas'):
                rec['hojas'].setdefault('analisis', {})['Cualitativo'] = oc
            rec['auditoria'] = {'fecha': '2026-09-26', 'guardadaOriginal': old.get('savedAt'),
                                'nota': 'Regenerada desde la hoja corregida (auditoria de la plantilla, ver METODOLOGIA.md de Modelo-JMR).'}
            out = saved.replace('.json', '.regen.json')
            json.dump(rec, open(out, 'w'), ensure_ascii=False, indent=2)
            print(sid, status, 'base', old['objetivoPonderado']['base'], '->', rec['objetivoPonderado']['base'], flush=True)
            ctx.close()
        b.close()
    srv.shutdown()
