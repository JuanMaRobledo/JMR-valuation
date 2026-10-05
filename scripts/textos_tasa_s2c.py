#!/usr/bin/env python
"""Textos de tasa, ventas/capital y ventaja al día en las hojas (revisión del 5-oct-2026).

Varias hojas conservaban textos de versiones anteriores que ya no describían sus números (p. ej. «Beta 1,3 (Direct
Input)» con una beta de 0,98, «Strong competitive edges» en una empresa sin ventaja defendible, o el texto de ventas/capital
de otra empresa). Este script los reescribe con los valores vigentes de cada hoja:
  - 'Tesis de Inversión y Supuestos'!F21 (si tiene texto) y 'Stories to Numbers'!G15: costo de capital;
  - 'Stories to Numbers'!G13 y 'Supuestos Recomendados'!C11:D12: ventas/capital usado y por qué;
  - 'Stories to Numbers'!G14: ventaja competitiva y ROIC después del año 10 (reference/moat_2026-09-30.json).
Respaldo en reference/revision_dcf_2026-10-05/textos_respaldo_<T>.json.

Uso: PYTHONPATH=.:scripts python scripts/textos_tasa_s2c.py [--apply] TICKER ...
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402

OUT = _ROOT / "reference" / "revision_dcf_2026-10-05"
BETA = {
    "BSX": "bottom-up de Healthcare Products en EE.UU., reapalancada",
    "DUOL": "bottom-up de Software (Internet) en la tabla global (62% de las ventas fuera de Norteamérica), reapalancada",
    "EPAM": "bottom-up de Computer Services, reapalancada",
    "GOOG": "por ingresos: Advertising (~82%) y Software (~18%) en EE.UU., reapalancada",
    "PLTR": "bottom-up de Software (System & Application) en EE.UU., sin deuda",
    "PYPL": "beta del patrimonio de Financial Svcs. (Non-bank & Insurance) en EE.UU.",
    "ZTS": "bottom-up de Drugs (Pharmaceutical), reapalancada",
    "MSFT": "bottom-up de Software (System & Application) en EE.UU., reapalancada",
    "NVO": "bottom-up de Drugs (Pharmaceutical) en EE.UU., reapalancada",
    "INTU": "bottom-up de Software (System & Application) en EE.UU., reapalancada",
    "NVDA": "bottom-up de Semiconductor en EE.UU., sin deuda relevante",
}
S2C = {
    "BSX": ("entre el de hoy (0,60, con el crédito mercantil de las compras) y el del sector (1,48); la Base crece sin compras",
            "un poco menor: parte del crecimiento posterior puede venir de compras"),
    "DUOL": ("el marginal de tres años con I+D capitalizado y sin los impuestos diferidos activos (3,04): los clientes prepagan y "
             "financian el crecimiento", "el de hoy (2,45), camino al del sector (1,35)"),
    "EPAM": ("servicios profesionales con poco capital fijo: entre el de hoy (1,95) y el del sector (5,19)",
             "algo menor por compras pequeñas y plataformas de IA"),
    "GOOG": ("carga el pico de capex de IA (marginal 0,44-0,65)", "la capacidad ya está construida; cerca del sector (1,35)"),
    "PLTR": ("software liviano en capital: entre el de hoy (3,23) y el marginal (3,0-7,8)", "eficiencia algo mayor al madurar"),
    "PYPL": ("marginal 2020-2025 con I+D capitalizado (~2,6); el de hoy (1,38) incluye el crédito mercantil", "igual"),
    "ZTS": ("el del sector (1,11); el de hoy (0,89) incluye el crédito mercantil de las compras", "igual"),
    "MSFT": ("carga el capex de IA (marginal 0,48-0,53)", "la capacidad madura sin volver a un modelo liviano"),
    "NVO": ("carga el capex de capacidad y la compra de plantas", "la capacidad ya está construida: el del sector (1,11)"),
    "INTU": ("el del sector (1,54): la Base es orgánica y el de hoy (1,08) carga el crédito mercantil de Credit Karma y "
             "Mailchimp", "igual"),
    "NVDA": ("el de hoy sin impuestos diferidos ni inversiones financieras (2,89); diseño fabless",
             "algo menor: más capital en empaquetado, redes y acuerdos de suministro"),
}


# 5-oct-2026: el resto de la cartera, solo los textos de tasa (G15 y F21), con la prima de mercado de octubre
BETA.update({
    "ADBE": "bottom-up de Software (System & Application) en EE.UU., reapalancada",
    "AFYA": "bottom-up de Education en la tabla global, reapalancada",
    "CELH": "bottom-up de Beverage (Soft) en EE.UU., reapalancada",
    "CMG": "bottom-up de Restaurant/Dining en EE.UU., reapalancada con los alquileres",
    "DPZ": "bottom-up de Restaurant/Dining en EE.UU., reapalancada con su D/E alta",
    "LULU": "bottom-up de Apparel en EE.UU., reapalancada",
    "NKE": "bottom-up de Shoe en la tabla global, reapalancada",
    "ONON": "bottom-up de Shoe en EE.UU., reapalancada",
    "PAGS": "patrimonio de Financial Svcs. en la tabla global",
    "SHAK": "bottom-up de Restaurant/Dining en EE.UU., reapalancada con los alquileres",
    "UBER": "regresión de Uber; «Transportation» no describe la plataforma",
})


def es(x: float, nd: int = 2) -> str:
    return f"{x:.{nd}f}".replace(".", ",")


def pct(x: float, nd: int = 1) -> str:
    return es(x * 100, nd) + "%"


def main(argv: list[str]) -> int:
    apply = "--apply" in argv
    moat = json.loads((_ROOT / "reference" / "moat_2026-09-30.json").read_text())
    moat = moat.get("empresas", moat)
    for tk in [a for a in argv if not a.startswith("--")]:
        for intento in range(4):  # cuota de lecturas de Google (60 por minuto)
            try:
                _uno(tk, apply, moat)
                break
            except Exception as e:
                if intento == 3:
                    raise
                print(f"  {tk}: {type(e).__name__}; reintento en 70 s")
                time.sleep(70)
        time.sleep(3)
    return 0


def _uno(tk: str, apply: bool, moat: dict) -> None:
    if True:
        sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())["sheet_id"]
        sh = ms.open_sheet(sid)
        rg = ["'Input sheet'!B35", "'Cost of capital worksheet'!C58", "'Cost of capital worksheet'!B28",
              "'Cost of capital worksheet'!B63:C63", "'Cost of capital worksheet'!B62", "'Input sheet'!B36",
              "'Input sheet'!B32:B33", "'Tesis de Inversión y Supuestos'!F21", "'Valuation output'!M14", "'Valuation output'!M42"]
        v = [x.get("values") for x in sh.values_batch_get(rg, params={"valueRenderOption": "UNFORMATTED_VALUE"})["valueRanges"]]
        rf, beta, erp = v[0][0][0], v[1][0][-1], v[2][0][0]
        ke, kd = v[3][0][0], v[3][0][1]
        we, w0 = v[4][0][0], v[5][0][0]
        s1, s2 = v[6][0][0], v[6][1][0]
        f21 = (v[7] or [[""]])[0][0] if v[7] else ""
        wt, roict = v[8][0][0], v[9][0][0]
        m = moat.get(tk, {})
        tasa = (f"rf {pct(rf, 2)} (UST 10 años, 30-sep-2026) + beta {es(beta)} ({BETA[tk]}) × ERP {pct(erp, 2)} (Damodaran, "
                f"oct-2026: 3,70% madura + riesgo país por regiones) = Ke {pct(ke)}; Kd después de impuestos {pct(kd)}; peso del "
                f"patrimonio {pct(we, 0)}; WACC inicial {pct(w0)} y terminal {pct(wt)}.")
        if tk == "PAGS":  # financiera: se descuenta el FCFE al costo del patrimonio
            fin = sh.values_get("'DCF FCFE financiero'!B4", params={"valueRenderOption": "UNFORMATTED_VALUE"})["values"][0][0]
            tasa = (f"rf {pct(rf, 2)} (UST 10 años, 30-sep-2026) + beta {es(beta)} ({BETA[tk]}) × ERP {pct(erp, 2)} (Damodaran, "
                    f"oct-2026: 3,70% madura + 3,24% de Brasil) = Ke {pct(ke)}, que converge a {pct(fin)} en el año 10; sin deuda "
                    f"financiera (fondeo operativo).")
        if tk not in S2C:  # solo los textos de tasa
            upd = {"Stories to Numbers": {"G15": tasa}}
            if isinstance(f21, str) and f21.strip():
                upd["Tesis de Inversión y Supuestos"] = {"F21": tasa}
            print(f"##### {tk}\n  G15 {tasa}")
            if apply:
                for hoja, celdas in upd.items():
                    ms.write_with_backup(sh, hoja, celdas, f"Texto de tasa al día ({tk}, 5-oct-2026)",
                                         OUT / f"textos_respaldo_{tk}.json")
            return
        r1, r2 = S2C[tk]
        g13 = (f"Ventas/capital {es(s1)} en los años 1-5: {r1}. " +
               (f"{es(s2)} en los años 6-10: {r2}." if r2 != "igual" else f"Igual en los años 6-10."))
        g14 = (f"{(m.get('ventaja') or 'sin dato').capitalize()}: ROIC después del año 10 de {pct(roict)} "
               f"(ROIC actual {pct(m['roic_actual'])}; industria {pct(m['roic_industria'])})."
               if m.get("roic_actual") is not None and m.get("roic_industria") is not None else
               f"{(m.get('ventaja') or 'sin dato').capitalize()}: ROIC después del año 10 de {pct(roict)}.")
        upd = {"Stories to Numbers": {"G13": g13, "G14": g14, "G15": tasa},
               "Supuestos Recomendados": {"C11": s1, "D11": f"{es(s1)}x: {r1}.", "C12": s2,
                                          "D12": f"{es(s2)}x: " + (r2 if r2 != "igual" else r1) + "."}}
        if isinstance(f21, str) and f21.strip():
            upd["Tesis de Inversión y Supuestos"] = {"F21": tasa}
        print(f"##### {tk}\n  G13 {g13}\n  G14 {g14}\n  G15 {tasa}")
        if apply:
            for hoja, celdas in upd.items():
                ms.write_with_backup(sh, hoja, celdas, f"Textos de tasa, ventas/capital y ventaja al día ({tk}, 5-oct-2026)",
                                     OUT / f"textos_respaldo_{tk}.json")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
