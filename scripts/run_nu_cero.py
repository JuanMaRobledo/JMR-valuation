#!/usr/bin/env python
"""Valoración de Nu Holdings Ltd. (NU) DESDE CERO (11-oct-2026) sobre una copia nueva de la plantilla maestra
(«Modelo JMR - NU (desde cero 2026-10-11)», 1FIghcohETa7UiyRciIKiDCmFeEjN7XwlaN4TBCeWO6Q, carpeta Análisis › NU), con el
prompt de valoración v4 y el de research v5 vigentes. No hay valoración anterior de NU: nada se hereda de otra empresa.

Identidad: Nu Holdings Ltd. (Islas Caimán), acciones clase A en NYSE (NU), CIK 0001691493; estados NIIF consolidados en
dólares; 20-F 2025 (8-abr-2026) y 6-K de estados del 2T26 (13-ago-2026). Corte común de la cartera: 30-sep-2026
(cierre US$12,66; Treasury 5,29%; prima madura de Damodaran 3,70%).

Rama financiera (prompt v4, «Bancos / aseguradoras»): NU es un banco (depósitos US$45.300 M, cartera de crédito y
capital regulatorio en Brasil, México y Colombia), así que el valor sale del FCFE con utilidad = ROE × patrimonio
contable descontado al costo del patrimonio (pestaña «DCF FCFE financiero», el motor de la app y la pestaña de
historias), no del FCFF industrial: los depósitos y la liquidez son materia prima del negocio y no se restan ni se suman
como deuda y caja. 'Valuation output' queda como referencia técnica.

Pasos: fix | input | fcfe | multiplos | content   (--step all corre todos). Las celdas que cambian llevan respaldo
(reference/backups/nu_desde_cero_2026-10-11.json) y nota con la fuente.
Uso: PYTHONPATH=.:scripts python scripts/run_nu_cero.py --step all
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402

SHEET_ID = "1FIghcohETa7UiyRciIKiDCmFeEjN7XwlaN4TBCeWO6Q"
TICKER = "NU"
BACKUP = _ROOT / "reference" / "backups" / "nu_desde_cero_2026-10-11.json"
FUENTE = _ROOT / "reference" / "desde_cero" / "NU" / "estados_fuente_2026-10-11.json"
F6K = "6-K estados 2T26 (nufs2q26_6k.htm, 13-ago-2026)"
F20 = "20-F 2025 (8-abr-2026)"


def d() -> dict:
    return json.loads(FUENTE.read_text())


def notas(sh, tab: str, notes: dict[str, str]) -> None:
    ws = sh.worksheet(tab)
    ws.insert_notes(notes)


def step_fix() -> None:
    """Correcciones del importador con los datos curados (balance UDM al 30-jun-2026, utilidad de la controladora,
    acciones en millones, arrendamientos NIIF 16 y cambio de caja)."""
    sh = ms.open_sheet(SHEET_ID)
    x = d()
    b, r = x["balance"], x["resultados"]
    j = 5  # 30-jun-2026
    tarjetas_prest = b["tarjetas_credito"][j] + b["prestamos"][j]
    bs = {
        "L3": b["caja"][j], "L4": b["titulos"][j], "L5": b["caja"][j] + b["titulos"][j],
        "L6": tarjetas_prest, "L8": tarjetas_prest, "L11": b["ppe"][j], "L12": b["intangibles"][j],
        "L13": b["plusvalia"][j], "L16": b["activos_totales"][j], "L20": 0, "L25": b["prestamos_financiacion"][j],
        "L29": b["pasivos_totales"][j], "L31": b["prima_emision"][j], "L32": b["otro_resultado_integral"][j],
        "L33": b["utilidades_retenidas"][j], "L34": b["patrimonio_controladora"][j], "L35": b["patrimonio_total"][j],
        "L36": b["activos_totales"][j], "G4": "",
    }
    # Arrendamientos NIIF 16 (pasivo por arrendamiento): ya son deuda bajo NIIF 16 (B18 = No). 2021 sin dato.
    for c, v in zip("HIJKL", b["arrendamientos"][1:]):
        bs[f"{c}26"] = v
    # Patrimonio de la controladora en la fila 34 (la 35 es el total con minoritarios).
    for c, v in zip("GHIJK", b["patrimonio_controladora"][:5]):
        bs[f"{c}34"] = v
    ms.write_with_backup(sh, "Balance Sheet", bs, "NU: balance UDM al 30-jun-2026 y patrimonio de la controladora", BACKUP)
    inc = {"L27": b["acciones_en_circulacion_millones"][j]}
    for c, v in zip("GHIJK", r["utilidad_controladora"][:5]):
        inc[f"{c}22"] = v
    inc["L22"] = r["utilidad_controladora"][4] + r["utilidad_controladora"][6] - r["utilidad_controladora"][5]
    ms.write_with_backup(sh, "Income Statement", inc, "NU: utilidad de la controladora y acciones en millones", BACKUP)
    # Cambio de caja: la plantilla trae una serie de relleno; con dato solo 2023-2025 y UDM (20-F 2025 y 6-K 2T26).
    cf = {f"{c}40": "" for c in "BCDEFGH"}
    cf.update({"I40": 1514.401, "J40": 2796.158, "K40": 5448.386, "L40": round(5448.386 - 1769.613 - 3752.422, 3)})
    ms.write_with_backup(sh, "Cash Flow Statement", cf, "NU: cambio de caja de los 20-F y del 6-K (sin relleno)", BACKUP)
    notas(sh, "Balance Sheet", {
        "L3": f"Saldos al 30-jun-2026: {F6K}, estado de situación financiera. Títulos (L4) = VR con cambios en resultados "
              "+ VR con cambios en ORI + costo amortizado, sin derivados. Cuentas por cobrar (L6) = tarjetas de crédito + "
              "préstamos a clientes. Deuda (L25) = préstamos y financiación (no incluye depósitos: en un banco son materia "
              "prima y el FCFE no los resta).",
        "L34": "Patrimonio atribuible a los accionistas de la controladora (la fila 35 incluye minoritarios: US$2,1 M). "
               f"G:K de {F20} y 20-F 2023; L del {F6K}.",
        "H26": "Pasivo por arrendamiento NIIF 16 (ya es deuda: 'Input sheet'!B18 = No).",
    })
    notas(sh, "Income Statement", {
        "L22": "Utilidad atribuible a la controladora; UDM = 2025 + 1S26 − 1S25 (20-F 2025 y 6-K 2T26).",
        "L27": "Acciones clase A + B en circulación al 30-jun-2026 (4.830.688.659; netas de 40,7 M en tesorería por la "
               "recompra). Nota 31 del 6-K 2T26.",
        "L12": "Banco: 'Operating Profit' = utilidad bruta − gastos operativos (utilidad antes de impuestos sin asociadas). "
               "El gasto de intereses y la pérdida de crédito esperada están en el costo de los servicios (fila 5).",
    })
    print("fix: balance UDM, utilidad controladora, acciones, arrendamientos y cambio de caja")


# Exposición por país: ingresos de clientes del 1S26 (nota 34 del 6-K 2T26): Brasil 7.576,852; México 603,629;
# otros países (Colombia y EE.UU.) 152,785; total 8.333,266 (excluye el rendimiento de tesorería).
W_BR, W_MX, W_OT = 7576.852 / 8333.266, 603.629 / 8333.266, 152.785 / 8333.266


def step_input() -> None:
    sh = ms.open_sheet(SHEET_ID)
    CE = "'Country equity risk premiums'"
    ms.write_with_backup(sh, "Input sheet", {
        "B17": "No", "B18": "No", "B38": "No",
        "B21": "='Balance Sheet'!L35-'Balance Sheet'!L34",
        "B22": "='Income Statement'!L27+52,178",
        "B30": "='Income Statement'!L13",
        "D12": "=IF('Income Statement'!L3='Income Statement'!K3;1;0,5)",
    }, "NU: banco (sin I+D capitalizable, NIIF 16, minoritarios, acciones diluidas, margen técnico)", BACKUP)
    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Direct Input", "B23": 0.82,
        "B26": "Will Input",
        "B27": f"={CE}!D31*{W_BR:.6f}+{CE}!D120*{W_MX:.6f}+{CE}!D44*{W_OT:.6f}".replace(".", ","),
        "B34": "Direct Input", "B35": f"='Input sheet'!B35+{CE}!C31",
    }, "NU: beta del patrimonio de Financial Svcs. (global), prima por países, Kd", BACKUP)
    notas(sh, "Input sheet", {
        "B21": "Participaciones no controladoras al 30-jun-2026 (US$2,1 M): patrimonio total − controladora.",
        "B22": "Acciones diluidas = 4.830,689 M en circulación al 30-jun-2026 + 52,178 M de dilución de RSU y opciones por "
               "el método de la acción en tesorería (promedio diluido 4.908,841 M − básico 4.856,663 M del 1S26, nota 9 "
               "del 6-K 2T26). Las RSU no se valoran aparte (B38 = No) para no contarlas dos veces.",
        "B30": "Referencia técnica: margen antes de impuestos UDM. En NU (banco) el valor sale del FCFE de la pestaña "
               "«DCF FCFE financiero» (ROE × patrimonio); 'Valuation output' (FCFF) no es el DCF del banco.",
        "D12": "Años desde el último cierre anual: dic-2025 → UDM a jun-2026 (6-K 2T26).",
        "B17": "Sin I+D separado en los estados NIIF de NU: no se capitaliza.",
        "B18": "NIIF 16: los arrendamientos ya están en el balance (pasivo US$66,4 M) y fuera del EBIT.",
    })
    notas(sh, "Cost of capital worksheet", {
        "B23": "Beta bottom-up (Damodaran, ene-2026, tabla global porque >50% de las ventas está fuera de EE.UU.): beta del "
               "patrimonio de Financial Svcs. (Non-bank & Insurance) = 0,82, sin desapalancar ni reapalancar: en un banco la "
               "deuda (depósitos) es materia prima y la razón D/E no mide riesgo financiero. Bank (Money Center) global da "
               "0,70 y la regresión de NU (Yahoo, 5 años mensual) 0,955: sensibilidades. Sin primas por riesgos propios: "
               "van en las historias.",
        "B27": "Prima por países (Damodaran: exposición por dónde opera, no por dónde cotiza): ingresos de clientes del 1S26, "
               f"nota 34 del 6-K 2T26: Brasil {W_BR:.2%}, México {W_MX:.2%}, otros (Colombia y EE.UU.) {W_OT:.2%} con la "
               "prima de Colombia. Cada prima = madura (B2) + riesgo país de la tabla.",
        "B35": "Costo de la deuda antes de impuestos = Treasury + diferencial de default de Brasil (Ba1). Solo pesa en el "
               "WACC técnico: el DCF del banco descuenta el FCFE al costo del patrimonio.",
    })
    print("input: listo")


def fcfe_tab_rows() -> list[dict]:
    T = "'DCF FCFE financiero'"
    data = [
        {"range": f"{T}!A1:E12", "values": [
            ["DCF FCFE financiero", "", "", "", ""],
            ["Nu Holdings · utilidad = ROE × patrimonio contable, reinversión patrimonial y costo del patrimonio · US$ millones",
             "", "Conservadora", "Base", "Optimista"],
            ["Utilidad neta UDM (controladora)", "='Income Statement'!L22", "", "", ""],
            ["Ke terminal (= Ke inicial: el riesgo país de Brasil es estructural)", "=B6", "", "", ""],
            ["g estable US$ / ROE años 1-5 por escenario", "='Valuation output'!M4",
             "='Escenarios e historias'!D6", "='Escenarios e historias'!D5", "='Escenarios e historias'!D8"],
            ["Ke inicial", "='Cost of capital worksheet'!B63", "", "", ""],
            ["Acciones diluidas (millones)", "='Input sheet'!B22", "", "", ""],
            ["WACC referencia", "='Input sheet'!B36", "", "", ""],
            ["Peso del patrimonio", "='Cost of capital worksheet'!B62", "", "", ""],
            ["ROE actual: utilidad UDM / patrimonio medio (dic-25 y jun-26)",
             "=B3/AVERAGE('Balance Sheet'!K34;'Balance Sheet'!L34)", "", "", ""],
            ["ROE después del año 10 (ventaja durable: ROE de la industria, Damodaran)",
             "=MAX(B4;MIN(VLOOKUP('Input sheet'!B10;'Industry Averages (Global)'!A3:X96;24;FALSE);B10))", "", "", ""],
            ["Patrimonio contable de la controladora al 30-jun-2026", "='Balance Sheet'!L34", "", "", ""],
        ]},
    ]
    blocks = (("Conservadora", 13, "'Valuation output'!{c}55", "$C$5", "$B$4"),
              ("Base", 29, "'Valuation output'!{c}4", "$D$5", "$B$11"),
              ("Optimista", 45, "'Valuation output'!{c}106", "$E$5", "$B$11"))
    for name, top, gref, roe, rt in blocks:
        rows = [[f"Año · {name}", "Crecimiento (negocio y patrimonio)", "Utilidad neta", "ROE", "Reinversión patrimonial",
                 "FCFE", "Ke", "Factor de descuento", "VP FCFE", "Patrimonio contable al cierre"]]
        for k in range(10):
            y, r = k + 1, top + 1 + k
            prev = "$B$12" if k == 0 else f"J{r - 1}"
            g = ("=" + gref.format(c="CDEFG"[k])) if y <= 5 else f"=B{r - 1}-(B{top + 5}-$B$5)/5"
            roe_f = f"={roe}" if y <= 5 else f"={roe}+({rt}-{roe})*(A{r}-5)/5"
            ke_f = "=$B$6" if y <= 5 else f"=$B$6+($B$4-$B$6)*(A{r}-5)/5"
            disc = f"=1/(1+G{r})" if k == 0 else f"=H{r - 1}/(1+G{r})"
            rows.append([y, g, f"=D{r}*{prev}", roe_f, f"={prev}*MAX(0;B{r})", f"=C{r}-E{r}", ke_f, disc, f"=F{r}*H{r}",
                         f"={prev}+E{r}"])
        last = top + 10
        rows.append(["Valor terminal al año 10: patrimonio₁₀ × (ROE terminal − g) / (Ke − g)",
                     f"=J{last}*({rt}-$B$5)/($B$4-$B$5)"] + [""] * 8)
        rows.append(["Valor del patrimonio hoy (FCFE: no se resta deuda)", f"=SUM(I{top + 1}:I{last})+B{last + 1}*H{last}"] + [""] * 8)
        rows.append(["Valor intrínseco por acción", f"=B{last + 2}/$B$7"] + [""] * 8)
        data.append({"range": f"{T}!A{top}:J{top + 13}", "values": rows})
    return data


def step_fcfe() -> None:
    sh = ms.open_sheet(SHEET_ID)
    if "DCF FCFE financiero" not in [w.title for w in sh.worksheets()]:
        sh.add_worksheet("DCF FCFE financiero", rows=70, cols=12, index=3)
    sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": fcfe_tab_rows()})
    notas(sh, "DCF FCFE financiero", {
        "A1": "Rama financiera del prompt v4 (bancos): utilidad = ROE × patrimonio contable del año anterior; crecer exige "
              "aumentar el patrimonio al mismo ritmo (reinversión patrimonial = patrimonio × crecimiento); FCFE = utilidad − "
              "reinversión, descontado al Ke. Igual al modelo de rendimientos en exceso: patrimonio de hoy + VP de (ROE − Ke) × "
              "patrimonio. Depósitos, caja y títulos no se suman ni restan: ya están en la utilidad.",
        "B11": "Criterio de ventaja (reference/moat_2026-09-30.json): ROE sobre el Ke por 3 años (2023-2026), ventaja "
               "identificable (costo de servir ~US$1 por cliente activo al mes, escala de 118 M de clientes en Brasil, datos "
               "propios de crédito y relación bancaria principal) y sin erosión visible → ventaja durable: ROE de la industria "
               "(Damodaran ene-2026, global, Financial Svcs. 18,8%), sin superar el ROE actual ni bajar del Ke. Las historias "
               "Conservadora y Disrupción usan ROE terminal = Ke.",
        "B4": "El Ke terminal conserva la prima de Brasil, México y Colombia (riesgo soberano estructural, prompt v4).",
        "B5": "Crecimiento estable en dólares = el de la hoja ('Valuation output'!M4 = Treasury a 10 años, sin superarlo).",
        "B12": "Patrimonio de la controladora al 30-jun-2026 (6-K 2T26). Conciliación con capital regulatorio: CET1 del "
               "conglomerado prudencial de Brasil US$4.262,9 M (11,9% de APR US$35.710,1 M), México US$427,6 M (14,9%), "
               "Colombia US$179,7 M (15,3%); la diferencia con el patrimonio consolidado son activos por impuestos diferidos "
               "(US$3.649 M), intangibles y plusvalía (US$1.156 M) y capital fuera de las entidades reguladas.",
    })
    print("fcfe: pestaña creada")


def step_multiplos() -> None:
    """Los múltiplos de utilidad y FCFE se proyectan con la utilidad y el FCFE de cada historia (ROE × patrimonio), no
    con el margen EBIT de 'Valuation output' (FCFF industrial, referencia técnica en un banco). Excepción financiera
    registrada en scripts/financieras.py."""
    sh = ms.open_sheet(SHEET_ID)
    EH = "'Escenarios e historias'"
    fm, vo = {}, {}
    # bloque de 'Financials Multiples' -> (fila de la utilidad, fila del FCFE) en la pestaña de historias
    for ni_row, fcfe_row, eh_ni, eh_fcfe in ((15, 29, 54, 57), (54, 68, 30, 33), (94, 108, 102, 105)):
        for k, c in enumerate("EFGH"):
            fm[f"{c}{ni_row}"] = f"={EH}!{'CDEF'[k]}{eh_ni}"
            fm[f"{c}{fcfe_row}"] = f"={EH}!{'CDEF'[k]}{eh_fcfe}"
    for c in ("C45", "C46", "C47", "C48"):
        vo[c] = "='Input sheet'!B30"
    # DCF de hoy de cada escenario = el FCFE de su historia (como PAGS), no el FCFF técnico de 'Valuation output'.
    dm = {"C38": f"={EH}!H6", "D38": f"={EH}!H5", "E38": f"={EH}!H8"}
    ms.write_with_backup(sh, "Descuento de múltiplos", dm, "NU (banco): DCF de hoy = FCFE de las historias", BACKUP)
    ms.write_with_backup(sh, "Financials Multiples", fm, "NU (banco): utilidad y FCFE de las historias FCFE", BACKUP)
    ms.write_with_backup(sh, "Valuation output", vo, "NU (banco): margen técnico del FCFF de referencia (no es el ROE)", BACKUP)
    notas(sh, "Financials Multiples", {
        "E54": "Banco (NU): utilidad neta de la historia Base (ROE × patrimonio del año anterior, pestaña «Escenarios e "
               "historias»), no EBIT × (1 − t). Igual en los bloques Conservador (fila 15 ← historia Conservadora) y "
               "Optimista (fila 94 ← historia Optimista).",
        "E68": "Banco (NU): FCFE de la historia Base = utilidad − aumento del patrimonio.",
    })
    notas(sh, "Valuation output", {
        "C46": "NU es un banco: el DCF es el FCFE de «Escenarios e historias» / «DCF FCFE financiero». Este bloque FCFF usa "
               "el margen antes de impuestos UDM como referencia técnica y no gobierna ningún resultado.",
    })
    print("multiplos: utilidad y FCFE de las historias en 'Financials Multiples'")


def step_content() -> None:
    """Pasos 3 y 10 del prompt v4: textos de la empresa en las pestañas que la maestra trae con ejemplos de otras."""
    import nu_cero_content as cc

    sh = ms.open_sheet(SHEET_ID)
    ms.write_with_backup(sh, "Cualitativo", cc.CUALITATIVO, "Contenido cualitativo NU desde cero (11-oct-2026)", BACKUP)
    ms.write_with_backup(sh, "Estadísticas", cc.ESTADISTICAS, "Estadísticas NU (fórmulas vivas; sin números de ejemplo)", BACKUP)
    sh.worksheet("Estadísticas").insert_notes(cc.ESTADISTICAS_NOTAS)
    ms.write_with_backup(sh, "Stories to Numbers", cc.STORIES, "Historia NU", BACKUP)
    ms.write_with_backup(sh, "Supuestos Recomendados", cc.SUPUESTOS_RECOMENDADOS, "Recomendaciones NU (banco)", BACKUP)
    cc.format_estadisticas(sh)
    cc.write_tesis(sh, BACKUP)  # después: apply_multiples_v3 --apply (agrega el origen de los múltiplos)
    print("content: pestañas de texto de NU")


STEPS = {"fix": step_fix, "input": step_input, "fcfe": step_fcfe, "multiplos": step_multiplos, "content": step_content}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--step", required=True, choices=list(STEPS) + ["all"])
    a = ap.parse_args()
    for name, fn in STEPS.items():
        if a.step in (name, "all"):
            fn()
