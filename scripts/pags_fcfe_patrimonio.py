#!/usr/bin/env python
"""PAGS: DCF FCFE con utilidad = ROE × patrimonio contable (Damodaran, bancos), 4-oct-2026.

Antes la utilidad de cada escenario crecía con los ingresos y el ROE solo fijaba la retención; al bajar el ROE al Ke en
los años 6-10, la utilidad seguía como si el ROE fuera alto (ROE implícito > Ke a perpetuidad, contra el supuesto «sin
ventaja») y los escenarios de ROE bajo partían de la misma utilidad que la Base. Ahora, en 'DCF FCFE financiero':
  B12 = patrimonio contable del último cierre (Balance Sheet L35);
  columna J = patrimonio al cierre de cada año = anterior + retención;
  utilidad = ROE × patrimonio del año anterior; retención = patrimonio anterior × MAX(0; crecimiento);
  valor terminal = FCFE₁₁ / (Ke − g) con utilidad₁₁ = Ke terminal × patrimonio₁₀ (= patrimonio del año 10).
Respaldo de las fórmulas en reference/revision_dcf_2026-10-04/PAGS_FCFE_respaldo.json.
"""
import json, sys
from pathlib import Path
sys.path.insert(0, '.')
from jmr_valuation.io.sheets_auth import get_gspread_client

SID = '1Q17gaT8w8fGx-3uRn7eCS_HsF0q-HZucEtgXGtVEIQY'
T = "'DCF FCFE financiero'"
OUT = Path('reference/revision_dcf_2026-10-04/PAGS_FCFE_respaldo.json')
sh = get_gspread_client().open_by_key(SID)
antes = sh.values_get(f"{T}!A1:J60", params={"valueRenderOption": "FORMULA"}).get('values', [])
if not OUT.exists():
    OUT.write_text(json.dumps({"sheet_id": SID, "rango": "DCF FCFE financiero!A1:J60", "formulas": antes}, ensure_ascii=False, indent=1))
data = [
    {"range": f"{T}!A10", "values": [["ROE escenarios en C5:E5: 13% / 15,6% / 17%; convergen al Ke terminal en el año 10. "
                                      "Utilidad = ROE × patrimonio contable del año anterior (Damodaran, bancos)."]]},
    {"range": f"{T}!A12:B12", "values": [["Patrimonio contable último cierre", "='Balance Sheet'!L35"]]},
]
for top in (13, 29, 45):
    data.append({"range": f"{T}!B{top}", "values": [["Crecimiento (negocio y patrimonio)"]]})
    data.append({"range": f"{T}!J{top}", "values": [["Patrimonio contable al cierre"]]})
    for k in range(10):
        r = top + 1 + k
        prev = "$B$12" if k == 0 else f"J{r - 1}"
        data.append({"range": f"{T}!C{r}", "values": [[f"=D{r}*{prev}"]]})
        data.append({"range": f"{T}!E{r}", "values": [[f"={prev}*MAX(0;B{r})"]]})
        data.append({"range": f"{T}!J{r}", "values": [[f"={prev}+E{r}"]]})
    last = top + 10
    data.append({"range": f"{T}!B{top + 11}", "values": [[f"=$B$4*J{last}*(1-$B$5/$B$4)/($B$4-$B$5)"]]})
sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": data})
v = sh.values_get(f"{T}!B24:B58", params={"valueRenderOption": "UNFORMATTED_VALUE"}).get('values', [])
print("Conservador", v[2], "Base", v[18], "Optimista", v[34])
