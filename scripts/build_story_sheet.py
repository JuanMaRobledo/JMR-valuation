"""Crea o actualiza la pestaña «Escenarios e historias» de la hoja de Google de cada empresa (contrato de escenarios
del 30-sep-2026, prompt de valoración v4): las cuatro historias A-D son los escenarios DCF activos y cada una es un DCF
completo por fórmulas, con el mismo diseño que la pestaña construida para ADBE.

- Filas 5-8: probabilidad, CAGR de ingresos, margen objetivo (ROE en financieras), ventas/capital, ROIC terminal,
  crecimiento terminal, DCF por acción y aporte al esperado. H10 = DCF esperado (complemento); H11 = DCF Base (valor intrínseco principal);
  H12:H13 = rango; H14 = precio con MOS sobre el esperado; H16 = antiguo caso Base (referencia técnica).
- Un bloque de 24 filas por historia desde la fila 22 (A), 46 (B), 70 (C) y 94 (D): ingresos por segmento (cuatro
  filas), crecimiento (años 6-10 convergen al terminal de la historia), margen, impuesto, NOPAT con pérdidas fiscales
  acumuladas, reinversión, FCFF, WACC, descuento, valor terminal, activos operativos, patrimonio y valor por acción
  (fila inicial + 22: B44, B68, B92, B116). Para el DCF FCFE de financieras (PAGS) el bloque usa utilidad, ROE, Ke y
  reinversión patrimonial, igual que 'DCF FCFE financiero'.
- Las cifras de cada historia salen de reference/damodaran/<T>.json y <T>_resultado.json (damodaran_stories.py); el
  resto son referencias a 'Input sheet', 'Valuation output' y 'Cost of capital worksheet'.

Verifica que H5:H8 y H10 coincidan con el motor (diferencia < 0,005 por acción).

Uso: python scripts/build_story_sheet.py CMG [MSFT ...]
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))
from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

REF = _ROOT / "reference" / "damodaran"
TAB = "Escenarios e historias"
COLS = "BCDEFGHIJKLM"  # año 0 … 10 y terminal
VO, IS = "'Valuation output'", "'Input sheet'"
SLOTS = 4  # filas de segmento por bloque
STARTS = {"A": 22, "B": 46, "C": 70, "D": 94}  # bloques de 24 filas; valor por acción en la fila inicial + 22


def n(x: float) -> str:
    """Número para una fórmula en la configuración regional es_ES (coma decimal)."""
    s = repr(round(float(x), 10))
    return s.replace(".", ",") if "e" not in s else f"{x:.12f}".rstrip("0").replace(".", ",")


def col(y: int) -> str:
    return COLS[y]


def _propios_6a10(h: dict):
    """Años 6-10 fijados por la historia (vencimiento de patentes u otra trayectoria explícita); None = convergencia."""
    if not h.get("anios6a10_propios"):
        return None
    return [round(float(x), 6) for x in h["anios6a10"]]


def block_fcff(h: dict, i: int, r0: int, segs: dict, rev_ltm: float) -> list[list]:
    """Bloque FCFF de una historia; i = fila de resumen (5-8)."""
    rows = [[h["nombre"] + (f": {h['descripcion']}" if h.get("descripcion") else "")],
            ["Año"] + list(range(11)) + ["Terminal"]]
    seg_rows = []
    for k, (name, v) in enumerate(list(segs.items()) + [("", None)] * (SLOTS - len(segs))):
        rr = r0 + 2 + k
        if v is None:
            rows.append([""])
            continue
        seg_rows.append(rr)
        g = h["crec"].get(name, [0] * 5)
        rows.append([name, f"={n(v)}*{VO}!B5/{n(rev_ltm)}"] + [f"={col(y - 1)}{rr}*(1+{n(g[y - 1])})" for y in range(1, 6)])
    R = {nm: r0 + 2 + SLOTS + j for j, nm in enumerate(
        ("rev", "g", "m", "t", "ebit", "nol", "nopat", "s2c", "reinv", "fcff", "wacc", "disc", "pv", "tv", "ops", "eq", "ps"))}
    first, last = seg_rows[0], r0 + 2 + SLOTS - 1
    rev = ["Ingresos totales", f"={VO}!B5"] + [f"=SUM({col(y)}{first}:{col(y)}{last})" for y in range(1, 6)] + \
        [f"={col(y - 1)}{R['rev']}*(1+{col(y)}{R['g']})" for y in range(6, 12)]
    tg = (f"=MAX(0;MIN($G{R['g']};{VO}!$M$4))" if h.get("terminal_propio") else f"={VO}!M4")
    g = ["Crecimiento", ""] + [f"={col(y)}{R['rev']}/{col(y - 1)}{R['rev']}-1" for y in range(1, 6)] + \
        (_propios_6a10(h) or [f"=$G{R['g']}-($G{R['g']}-$M${R['g']})*({y}-5)/5" for y in range(6, 11)]) + [tg]
    m = ["Margen operativo", "", f"={VO}!C6"] + [
        f"=IF({y}>{IS}!$B$31;$D${i};$D${i}-($D${i}-{VO}!$C$6)/{IS}!$B$31*({IS}!$B$31-{y}))" for y in range(2, 11)] + \
        [f"=L{R['m']}"]
    t = ["Impuesto", ""] + [f"={VO}!C8"] * 5 + [f"={VO}!$C$8+({VO}!$M$8-{VO}!$C$8)*({y}-5)/5" for y in range(6, 11)] + [f"={VO}!M8"]
    ebit = ["EBIT", ""] + [f"={col(y)}{R['rev']}*{col(y)}{R['m']}" for y in range(1, 12)]
    nol = ["Pérdidas fiscales acumuladas (NOL)", f"={VO}!B12"] + [
        f"=IF({c}{R['ebit']}<0;{p}{R['nol']}-{c}{R['ebit']};IF({p}{R['nol']}>{c}{R['ebit']};{p}{R['nol']}-{c}{R['ebit']};0))"
        for c, p in ((col(y), col(y - 1)) for y in range(1, 11))]
    nopat = ["NOPAT", ""] + [
        f"=IF({c}{R['ebit']}>0;IF({c}{R['ebit']}<{p}{R['nol']};{c}{R['ebit']};{c}{R['ebit']}-({c}{R['ebit']}-{p}{R['nol']})*{c}{R['t']});{c}{R['ebit']})"
        for c, p in ((col(y), col(y - 1)) for y in range(1, 11))] + [f"=M{R['ebit']}*(1-M{R['t']})"]
    s2c = ["Ventas/capital", ""] + [f"=$E${i}"] * 5 + [f"=$F${i}"] * 5
    reinv = ["Reinversión", ""] + [
        f"=IF(AND({IS}!$B$57=\"Yes\";{IS}!$B$58=0);{col(y)}{R['rev']}-{col(y - 1)}{R['rev']};{col(y + 1)}{R['rev']}-{col(y)}{R['rev']})/{col(y)}{R['s2c']}"
        for y in range(1, 11)] + [f"=M{R['nopat']}*M{R['g']}/$G${i}"]
    fcff = ["FCFF", ""] + [f"={col(y)}{R['nopat']}-{col(y)}{R['reinv']}" for y in range(1, 12)]
    wacc = ["WACC", ""] + [f"={VO}!C14"] * 5 + [f"={VO}!$C$14-({VO}!$C$14-{VO}!$M$14)*({y}-5)/5" for y in range(6, 11)] + [f"={VO}!M14"]
    disc = ["Factor de descuento", "", f"=1/(1+C{R['wacc']})"] + [f"={col(y - 1)}{R['disc']}/(1+{col(y)}{R['wacc']})" for y in range(2, 11)]
    pv = ["VP FCFF", ""] + [f"={col(y)}{R['fcff']}*{col(y)}{R['disc']}" for y in range(1, 11)]
    tv = ["Valor terminal"] + [""] * 11 + [f"=M{R['fcff']}/(M{R['wacc']}-M{R['g']})"]
    ops = ["VP activos operativos", f"=SUM(C{R['pv']}:L{R['pv']})+M{R['tv']}*L{R['disc']}"]
    eq = ["Valor patrimonio", f"=B{R['ops']}*(1-{VO}!B24)+IF({IS}!B54=\"B\";{IS}!B15+{IS}!B16;B{R['ops']})*{IS}!B55*{VO}!B24"
          f"-{VO}!B27-{VO}!B28+{VO}!B29+{VO}!B30-{VO}!B32-N({IS}!$B$76)"]  # B76: acciones preferentes separadas
    ps = ["DCF por acción", f"=B{R['eq']}/{VO}!B34"]
    rows += [rev, g, m, t, ebit, nol, nopat, s2c, reinv, fcff, wacc, disc, pv, tv, ops, eq, ps]
    return rows, R


def block_fcfe(h: dict, i: int, r0: int, segs: dict, rev_ltm: float) -> list[list]:
    """Bloque FCFE (financieras): igual que el motor runFCFEDetalle y la pestaña 'DCF FCFE financiero'."""
    F = "'DCF FCFE financiero'"
    rows = [[h["nombre"] + (f": {h['descripcion']}" if h.get("descripcion") else "")],
            ["Año"] + list(range(11)) + ["Terminal"]]
    seg_rows = []
    for k, (name, v) in enumerate(list(segs.items()) + [("", None)] * (SLOTS - len(segs))):
        rr = r0 + 2 + k
        if v is None:
            rows.append([""])
            continue
        seg_rows.append(rr)
        g = h["crec"].get(name, [0] * 5)
        rows.append([name, f"={n(v)}*{VO}!B5/{n(rev_ltm)}"] + [f"={col(y - 1)}{rr}*(1+{n(g[y - 1])})" for y in range(1, 6)])
    R = {nm: r0 + 2 + SLOTS + j for j, nm in enumerate(
        ("rev", "g", "ni", "roe", "reinv", "fcfe", "ke", "disc", "pv", "tv", "x1", "x2", "x3", "x4", "ops", "eq", "ps"))}
    first, last = seg_rows[0], r0 + 2 + SLOTS - 1
    rev = ["Ingresos por segmento (motor del crecimiento)", f"={VO}!B5"] + [f"=SUM({col(y)}{first}:{col(y)}{last})" for y in range(1, 6)]
    tg = (f"=MAX(0;MIN($G{R['g']};{F}!$B$5))" if h.get("terminal_propio") else f"={F}!B5")
    g = ["Crecimiento", ""] + [f"={col(y)}{R['rev']}/{col(y - 1)}{R['rev']}-1" for y in range(1, 6)] + \
        (_propios_6a10(h) or [f"=$G{R['g']}-($G{R['g']}-$M${R['g']})*({y}-5)/5" for y in range(6, 11)]) + [tg]
    ni = ["Utilidad neta", f"={F}!B3"] + [f"={col(y - 1)}{R['ni']}*(1+{col(y)}{R['g']})" for y in range(1, 12)]
    roe = ["ROE", ""] + [f"=$D${i}"] * 5 + [f"=$D${i}+({F}!$B$4-$D${i})*({y}-5)/5" for y in range(6, 11)]
    reinv = ["Reinversión patrimonial", ""] + [f"={col(y)}{R['ni']}*MAX(0;{col(y)}{R['g']})/{col(y)}{R['roe']}" for y in range(1, 11)] + \
        [f"=M{R['ni']}*M{R['g']}/{F}!B4"]
    fcfe = ["FCFE", ""] + [f"={col(y)}{R['ni']}-{col(y)}{R['reinv']}" for y in range(1, 12)]
    ke = ["Costo del patrimonio", ""] + ["='Cost of capital worksheet'!B63"] * 5 + \
        [f"='Cost of capital worksheet'!$B$63-('Cost of capital worksheet'!$B$63-{F}!$B$4)*({y}-5)/5" for y in range(6, 11)] + [f"={F}!B4"]
    disc = ["Factor de descuento", "", f"=1/(1+C{R['ke']})"] + [f"={col(y - 1)}{R['disc']}/(1+{col(y)}{R['ke']})" for y in range(2, 11)]
    pv = ["VP FCFE", ""] + [f"={col(y)}{R['fcfe']}*{col(y)}{R['disc']}" for y in range(1, 11)]
    tv = ["Valor terminal"] + [""] * 11 + [f"=M{R['fcfe']}/(M{R['ke']}-M{R['g']})"]
    ops = ["VP de los flujos al accionista", f"=SUM(C{R['pv']}:L{R['pv']})+M{R['tv']}*L{R['disc']}"]
    eq = ["Valor patrimonio (FCFE: no se resta deuda)", f"=B{R['ops']}"]
    ps = ["DCF por acción", f"=B{R['eq']}/{VO}!B34"]
    rows += [rev, g, ni, roe, reinv, fcfe, ke, disc, pv, tv, [""], [""], [""], [""], ops, eq, ps]
    return rows, R


def build(tk: str, gc) -> None:
    spec = json.loads((REF / f"{tk}.json").read_text())
    res = json.loads((REF / f"{tk}_resultado.json").read_text())
    anc = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{tk}_anclas.json").read_text())
    fin = bool(res.get("financiero"))
    hs = res["historias"]
    segs = spec["segmentos"]
    rev_ltm = sum(segs.values())
    sh = gc.open_by_key(anc["sheet_id"])
    try:
        ws = sh.worksheet(TAB)
        ws.clear()
    except Exception:  # noqa: BLE001
        ws = sh.add_worksheet(TAB, rows=130, cols=14, index=2)
    grid = [[""] * 13 for _ in range(120)]

    def put(r, vals):
        for c, v in enumerate(vals):
            grid[r - 1][c] = v

    put(1, [f"{tk} · Escenarios = historias · DCF Base (principal) y DCF esperado (complemento)"])
    put(2, ["Cuatro DCF completos (Base, Conservadora, Disrupción y Optimista) con probabilidades del analista. "
            "Supuestos vinculados al modelo; crecimiento por segmento y probabilidades son entradas del analista."])
    put(4, ["Escenario / historia", "Probabilidad", "CAGR ingresos 1–5", "ROE objetivo" if fin else "Margen objetivo",
            "Ventas/capital 1–5", "Ventas/capital 6–10", "ROIC terminal", "DCF hoy por acción", "Aporte al esperado",
            "Crecimiento terminal"])
    blocks = []
    for k, h in enumerate(hs):
        i, r0 = 5 + k, STARTS[h["id"]]
        rows, R = (block_fcfe if fin else block_fcff)(h, i, r0, segs, rev_ltm)
        blocks.append((h, R))
        for j, row in enumerate(rows):
            put(r0 + j, row)
        roic = ("" if fin else (f"={VO}!M14" if h.get("roic_terminal") == "costo_capital" else
                                f"=IF({IS}!B49=\"Yes\";{IS}!B50;{VO}!M14)"))
        s2 = h.get("s2c")
        put(i, [h["nombre"] + (f": {h['descripcion']}" if h.get("descripcion") else ""), h["prob"],
                f"=(G{R['rev']}/B{R['rev']})^(1/5)-1", h["margen"],
                "" if fin else (s2 if s2 else f"={IS}!$B$32"), "" if fin else f"={IS}!$B$33", roic,
                f"=MAX(0;B{R['ps']})", f"=B{i}*H{i}", f"=M{R['g']}"])  # responsabilidad limitada: patrimonio ≥ 0
    put(10, ["DCF esperado por probabilidades · complemento", "=SUM(B5:B8)"] + [""] * 5 + ["=IF(ABS(B10-1)<0,00000001;SUMPRODUCT(B5:B8;H5:H8);NA())"])
    put(11, ["DCF Base · valor intrínseco principal"] + [""] * 6 + ["=H5"])
    put(12, ["Mínimo de las historias"] + [""] * 6 + ["=MIN(H5:H8)"])
    put(13, ["Máximo de las historias"] + [""] * 6 + ["=MAX(H5:H8)"])
    put(14, ["Margen de seguridad (precio con MOS sobre el esperado)", "='Resumen de Valoración'!G4"] + [""] * 5 + ["=H10*(1-B14)"])
    put(16, ["Antiguo caso Base · referencia técnica"] + [""] * 6 + [f"={VO}!B35"])
    put(17, ["Los casos técnicos Conservador/Base/Optimista anteriores calibran el motor y los múltiplos auxiliares; los cuatro escenarios activos son Base, Conservadora, Disrupción y Optimista."])
    put(18, ["Disrupción se estabiliza sin recuperación: crecimiento terminal = el del año 5, sin superar el de la hoja, con piso de 0%; "
             "ROIC terminal = costo de capital. Las demás conservan el terminal de la hoja."])
    put(19, ["Las fórmulas siguientes reproducen el motor DCF del Modelo JMR; millones de la moneda de la hoja salvo valor por acción."])
    if not fin:
        put(20, ["Control: pérdidas fiscales iniciales (NOL) incluidas en los bloques"] + [""] * 6 +
            [f"=IF({VO}!B12=0;\"Sin NOL\";\"NOL incluido\")"])
    ws.update(values=grid, range_name="A1:M120", value_input_option="USER_ENTERED")
    sid = ws.id
    pct_rows = [(5, 9, 1, 4), (5, 9, 6, 7), (5, 9, 9, 10)]
    fmt = []

    def rc(r1, r2, c1, c2, pattern, typ="NUMBER"):
        fmt.append({"repeatCell": {"range": {"sheetId": sid, "startRowIndex": r1 - 1, "endRowIndex": r2 - 1,
                                             "startColumnIndex": c1, "endColumnIndex": c2},
                                   "cell": {"userEnteredFormat": {"numberFormat": {"type": typ, "pattern": pattern}}},
                                   "fields": "userEnteredFormat.numberFormat"}})
    for r1, r2, c1, c2 in pct_rows:
        rc(r1, r2, c1, c2, "0.0%", "PERCENT")
    rc(5, 9, 4, 6, "0.00")
    rc(5, 17, 7, 9, "#,##0.00")
    rc(10, 11, 1, 2, "0%", "PERCENT")
    rc(14, 15, 1, 2, "0%", "PERCENT")
    for h, R in blocks:
        rc(STARTS[h["id"]] + 2, R["ps"], 1, 13, "#,##0.00")
        for key in ("g", "m", "t", "wacc", "roe", "ke"):
            if key in R:
                rc(R[key], R[key] + 1, 1, 13, "0.00%", "PERCENT")
        rc(R["disc"], R["disc"] + 1, 1, 13, "0.0000")
    fmt.append({"repeatCell": {"range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": 1},
                               "cell": {"userEnteredFormat": {"textFormat": {"bold": True, "fontSize": 13}}},
                               "fields": "userEnteredFormat.textFormat"}})
    for r in [4, 10] + [STARTS[h["id"]] for h, _ in blocks]:
        fmt.append({"repeatCell": {"range": {"sheetId": sid, "startRowIndex": r - 1, "endRowIndex": r},
                                   "cell": {"userEnteredFormat": {"textFormat": {"bold": True}}},
                                   "fields": "userEnteredFormat.textFormat"}})
    fmt.append({"updateDimensionProperties": {"range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": 0, "endIndex": 1},
                                              "properties": {"pixelSize": 330}, "fields": "pixelSize"}})
    sh.batch_update({"requests": fmt})

    vals = ws.get("H5:H14", value_render_option="UNFORMATTED_VALUE")
    got = [row[0] if row else None for row in vals]
    exp = [h["valor_beta_hoja"] for h in hs] + [None, res["valor_esperado_beta_hoja"]]
    ok = all(abs(g - e) < 0.005 for g, e in zip(got, exp) if e is not None and isinstance(g, (int, float)))
    ok = ok and all(isinstance(got[j], (int, float)) for j in (0, 1, 2, 3, 5))
    print(f"{tk:5s} hoja H5:H8 {[round(x, 2) if isinstance(x, (int, float)) else x for x in got[:4]]} esperado "
          f"{got[5] if not isinstance(got[5], float) else round(got[5], 2)} motor {res['valor_esperado_beta_hoja']:.2f} "
          f"{'OK' if ok else 'DIFERENCIA'}", flush=True)
    if not ok:
        raise SystemExit(f"{tk}: la pestaña no reproduce el motor")
    if not fin:
        # 2-oct-2026: las cuatro historias se calculan en 'Valuation output' con la estructura de Damodaran
        import link_vo_to_stories as lv
        sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": lv.plan(sh)})
        lv.format_block(sh)
        time.sleep(3)
        chk = lv.check(sh)
        bad = {k: v for k, v in chk.items() if not (isinstance(v["dif"], (int, float)) and abs(v["dif"]) < 0.005)}
        if bad:
            raise SystemExit(f"{tk}: 'Valuation output' no reproduce las historias: {bad}")
        lv.apply_phase2(sh)
        print(f"{tk:5s} historias calculadas en 'Valuation output' (Base, Conservador, Optimista, Disrupción): OK", flush=True)


def main(argv: list[str]) -> int:
    gc = get_gspread_client()
    for tk in argv:
        for attempt in range(5):
            try:
                build(tk, gc)
                break
            except Exception as e:  # noqa: BLE001
                if "429" in str(e) or "Quota" in str(e):
                    time.sleep(30 * (attempt + 1))
                    continue
                raise
        time.sleep(5)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
