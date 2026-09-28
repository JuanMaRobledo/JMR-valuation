"""Guarda en Modelo-JMR-datos/valoraciones/ una valoracion NUEVA desde su hoja
(mismo mecanismo que regen_saved_valuations.py: exporta el xlsx, lo carga en
docs/visor.html con Playwright, pulsa "Guardar valoración" e intercepta el PUT
a GitHub para quedarse con el JSON exacto que el visor habria guardado).

Uso: python scripts/save_new_valuations.py '[["<sheet_id>", "TICKER"], ...]'
Deja el archivo en ../Modelo-JMR-datos/valoraciones/<TICKER>-<ms>.json."""
import base64
import json
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import regen_saved_valuations as rsv  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

DATOS = Path(os.environ.get("MODELO_JMR_DATOS", Path(__file__).resolve().parents[2] / "Modelo-JMR-datos"))


def main(pairs):
    srv = rsv.serve()
    out = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=os.environ.get("CHROMIUM_PATH") or None)
        for sid, ticker in pairs:
            xlsx = os.path.join(tempfile.gettempdir(), f"{sid}.xlsx")
            rsv.export_xlsx(sid, xlsx)
            ctx = b.new_context()
            ctx.add_init_script("localStorage.setItem('jmr-auth-ok-v1','1');localStorage.setItem('jmr-gh-datastore-token','x');")
            page = ctx.new_page()
            captured = {}

            def gh(route):
                req = route.request
                if req.method == "PUT":
                    captured["url"] = req.url
                    captured["body"] = json.loads(req.post_data)
                    route.fulfill(status=201, content_type="application/json", body='{"content":{}}')
                else:
                    route.fulfill(status=200, content_type="application/json", body="[]")

            page.route("**/api.github.com/**", gh)
            page.route("**/xlsx.full.min.js", lambda r: r.fulfill(path=rsv.SHEETJS, content_type="application/javascript"))
            page.goto("http://127.0.0.1:8765/visor.html")
            page.set_input_files("#fileInput", xlsx)
            page.wait_for_selector("#saveValBtn", state="attached", timeout=90000)
            page.wait_for_timeout(2000)
            page.click("#saveValBtn")
            page.wait_for_function("document.getElementById('saveStatus') && /Guardada|Error/.test(document.getElementById('saveStatus').textContent)", timeout=90000)
            status = page.eval_on_selector("#saveStatus", "e => e.textContent")
            rec = json.loads(base64.b64decode(captured["body"]["content"]).decode("utf-8"))
            name = captured["url"].split("/contents/")[-1]
            dest = DATOS / name
            dest.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(ticker, status.strip(), dest.name, "| rec.ticker", rec.get("ticker"), "| base", rec.get("objetivoPonderado", {}).get("base"), flush=True)
            out.append(str(dest))
            ctx.close()
        b.close()
    srv.shutdown()
    return out


if __name__ == "__main__":
    main(json.loads(sys.argv[1]))
