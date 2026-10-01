"""Revisión de supuestos del DCF (30-sep-2026) para GOOG, DUOL, UBER, NVDA y PLTR
(aprobada por el usuario) y, en una segunda ronda, BSX, DPZ, MSFT y NKE (retorno
sobre el capital después del año 10, 'Input sheet'!B49/B50).

Cambia solo celdas de supuestos (no fórmulas): crecimiento y margen del escenario
Base ('Input sheet'), crecimiento fijo y margen objetivo de los escenarios
Conservador / Optimista ('Valuation output' C55, C45, C106, C47), sales-to-capital
y la beta de entrada directa ('Cost of capital worksheet'!B23).

Antes de escribir guarda el valor (o fórmula) vigente de cada celda en
reference/revision_dcf_2026-09-30/<T>.json, y deja una nota en cada celda con el
valor anterior y el motivo. Con --revert restaura el respaldo.

Uso: python scripts/revise_dcf_inputs.py [--dry-run | --revert] [TICKER ...]
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from jmr_valuation.io.sheets_auth import get_gspread_client  # noqa: E402

_ROOT = Path(__file__).resolve().parents[1]
OUT = _ROOT / "reference" / "revision_dcf_2026-09-30"
IS, VO, COC, RD, BSH, CFH = "Input sheet", "Valuation output", "Cost of capital worksheet", "R& D converter", "Balance Sheet", "Cash Flow Statement"

ARREND = 'Deuda de balance sin arrendamientos operativos porque entran por el conversor de arrendamientos (B18 = Yes, criterio Damodaran: VP de los compromisos como deuda y EBIT + gasto − depreciación); así no se cuentan dos veces. Los arrendamientos financieros siguen en esta deuda.'

# (hoja, celda, valor nuevo, motivo)
CHANGES: dict[str, list[tuple[str, str, float, str]]] = {
    "GOOG": [
        (IS, "B27", 0.18, "Ingresos +24% en el 2T26 (Cloud +82%); la hoja suponía 11%."),
        (IS, "B29", 0.11, "Desaceleración con la escala; antes 7%."),
        (IS, "B30", 0.35, "Margen operativo de 34% en el 2T26 con Cloud rentable; antes 33,5%."),
        (IS, "B32", 1.2, "Capex 2026 de US$195-205 mil M: la reinversión real es muy superior a la de un S/C de 2,5."),
        (IS, "B33", 1.5, "El capex se modera pero sigue alto en los años 6-10; antes 2."),
        (COC, "B23", 1.07, "Beta por ingresos: Advertising (1,01, ~82%) y Software (1,25, ~18%), reapalancada."),
        (VO, "C55", 0.09, "Conservador: crecimiento de 9% (antes 6%, por debajo de lo que ya muestra la empresa)."),
        (VO, "C45", 0.31, "Conservador: la depreciación del capex de IA baja el margen a 31% (antes 32,5%)."),
        (VO, "C47", 0.38, "Optimista: margen de 38% con Cloud a escala (antes 37%)."),
    ],
    "DUOL": [
        (IS, "B27", 0.12, "Reservas +8% en el 2T26 y guía de reservas 2026 de +10,9%; la hoja suponía 19%."),
        (IS, "B29", 0.11, "Crecimiento de los años 2-5 alineado con las reservas; antes 16%."),
        (IS, "B30", 0.27, "Margen objetivo 27% (antes 30%): SBC de ~15% de los ingresos y costos de IA."),
        (VO, "C55", 0.08, "Conservador: 8% anual (antes 15%, por encima de las reservas actuales)."),
        (VO, "C106", 0.16, "Optimista: 16% anual si la IA reacelera las reservas (antes 23%)."),
    ],
    "UBER": [
        (IS, "B30", 0.21, "Margen GAAP de 13% en el 2T26; 26% superaba incluso el margen de los mejores segmentos. Objetivo 21%."),
        (IS, "B32", 2.5, "Flotas autónomas y Delivery Hero hacen el crecimiento más intensivo en capital; antes 3."),
    ],
    "NVDA": [
        (COC, "B23", 1.51, "Beta bottom-up de Semiconductor (Damodaran, ene-2026) en lugar de la de regresión (1,90)."),
    ],
    "PLTR": [
        (IS, "B27", 0.68, "Próximos 12 meses: ~US$10.400 M con la guía 2026 de US$8.150 M (+82% en el año calendario); antes 82% sobre el LTM."),
        (IS, "B29", 0.35, "Años 2-5 al 35% (antes 40%): tasa base de <1% de las empresas a este ritmo."),
        (IS, "B30", 0.48, "Margen objetivo 48% (antes 50%) por la compensación en acciones."),
        (COC, "B23", 1.25, "Beta bottom-up de Software (System & Application) en lugar de la de regresión (1,62)."),
        (VO, "C55", 0.35, "Conservador: 35% anual (antes 60%)."),
        (VO, "C106", 0.60, "Optimista: 60% anual (antes 95%, que multiplicaba los ingresos por 28 en cinco años)."),
    ],
    # Segunda ronda: el DCF suponía que después del año 10 el ROIC iguala al costo de
    # capital (sin retornos excedentes). Damodaran lo acepta solo sin ventajas
    # duraderas; con marca, escala o red se fija el menor entre el ROIC actual y el
    # de la industria (Damodaran, ene-2026).
    # BSX se revirtió el 30-sep-2026 (--revert BSX): no cumple la regla del prompt (ROIC sostenido por encima
    # del costo de capital); se conserva aquí como registro de lo que se aplicó y se deshizo.
    "BSX": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: Boston Scientific tiene ventajas duraderas (patentes, relación con médicos)."),
        (IS, "B50", 0.111, "ROIC terminal 11,1%: el menor entre el actual (11,1%, recortado por las compras de empresas) y el de su industria según Damodaran (17,0%)."),
    ],
    "DPZ": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: franquicia con marca y logística propias, muy poco capital."),
        (IS, "B50", 0.184, "ROIC terminal 18,4%: el de su industria según Damodaran (el actual, 99%, refleja el modelo de franquicia y no se sostiene para siempre)."),
    ],
    "MSFT": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: efectos de red y costos de cambio en Office, Azure y Windows."),
        (IS, "B50", 0.259, "ROIC terminal 25,9%: el menor entre el actual (25,9%, que ya descuenta el capex de IA) y el de su industria según Damodaran (29,3%)."),
    ],
    "NKE": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: marca global con poder de precio."),
        (IS, "B50", 0.133, "ROIC terminal 13,3%: el menor entre el actual (13,3%, con el margen deprimido) y el de su industria según Damodaran (20,9%)."),
    ],
    # Tercera ronda (regla del prompt de valoración v4): ventaja durable, ROIC sostenido por encima del
    # costo de capital y sin amenaza directa en la historia Base -> menor entre ROIC actual e industria.
    "ADBE": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: costos de cambio: Creative Cloud y Acrobat son el estándar de la industria creativa y documental."),
        (IS, "B50", 0.293, "ROIC terminal 29,3%: el menor entre el actual (36,3%) y el de Software (System & Application) según Damodaran (29,3%); costo de capital terminal 9,2%."),
    ],
    "AFYA": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: licencias reguladas: los cupos de medicina en Brasil los fija el gobierno y Afya tiene la red más grande."),
        (IS, "B50", 0.148, "ROIC terminal 14,8%: el menor entre el actual (14,8%) y el de Education según Damodaran (15,9%); costo de capital terminal 11,0%."),
    ],
    "CMG": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: marca y economía por local: 30 años de retornos altos sin franquiciar."),
        (IS, "B50", 0.184, "ROIC terminal 18,4%: el menor entre el actual (53,1%) y el de Restaurant/Dining según Damodaran (18,4%); costo de capital terminal 9,0%."),
    ],
    "GOOG": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: efectos de red y escala en búsqueda, YouTube y Android."),
        (IS, "B50", 0.286, "ROIC terminal 28,6%: el menor entre el actual (28,6%) y el de Software (System & Application) según Damodaran (29,3%); el de Software (Internet) (3,4%) no es representativo porque agrega muchas empresas con pérdidas; costo de capital terminal 9,0%."),
    ],
    "INTU": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: costos de cambio: TurboTax y QuickBooks guardan los datos contables y fiscales del cliente."),
        (IS, "B50", 0.222, "ROIC terminal 22,2%: el menor entre el actual (22,2%) y el de Software (System & Application) según Damodaran (29,3%); costo de capital terminal 9,0%."),
    ],
    "LULU": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: marca premium en ropa deportiva, con márgenes altos durante más de una década."),
        (IS, "B50", 0.158, "ROIC terminal 15,8%: el menor entre el actual (25,2%) y el de Apparel según Damodaran (15,8%); costo de capital terminal 9,0%."),
    ],
    "NVDA": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: ecosistema CUDA y escala en cómputo acelerado."),
        (IS, "B50", 0.272, "ROIC terminal 27,2%: el menor entre el actual (113,7%) y el de Semiconductor según Damodaran (27,2%); costo de capital terminal 9,0%."),
    ],
    "NVO": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: franquicia de I+D en diabetes y obesidad, con patentes que se renuevan con nuevas moléculas."),
        (IS, "B50", 0.169, "ROIC terminal 16,9%: el menor entre el actual (23,8%) y el de Drugs (Pharmaceutical) según Damodaran (16,9%); costo de capital terminal 9,2%."),
    ],
    "ZTS": [
        (IS, "B49", "Yes", "ROIC después del año 10 distinto del costo de capital: líder en salud animal: marcas, relación con veterinarios y cartera diversificada de patentes."),
        (IS, "B50", 0.169, "ROIC terminal 16,9%: el menor entre el actual (25,3%) y el de Drugs (Pharmaceutical) según Damodaran (16,9%); costo de capital terminal 9,0%."),
    ],
    # Cuarta ronda: tasa efectiva de los años 1-5 normalizada cuando la del LTM es atípica.
    "BSX_IMPUESTO": [
        (IS, "B24", 0.178, "Tasa efectiva de los años 1-5 = promedio 2023-2025 (19,8%, 19,1% y 14,6%). La del LTM (5%) refleja beneficios fiscales de una vez y no es sostenible."),
    ],
    # Sexta ronda (30-sep-2026, revaloración de CMG): saldos del balance al 30-jun-2026 (10-Q del 2T26).
    "CMG_CAJA": [
        (IS, "B19", 677.9, "Caja e inversiones negociables al 30-jun-2026 = efectivo US$228,2M + inversiones de corto plazo US$449,7M (10-Q 2T26). Antes solo el efectivo."),
        (IS, "B20", 97.1, "Inversiones de largo plazo al 30-jun-2026 (10-Q 2T26); antes US$197,1M, el saldo de dic-2025."),
        (IS, "B15", 2199.8, "Patrimonio al 30-jun-2026 (10-Q 2T26); antes US$2.830,6M, el saldo de dic-2025. Bajó por recompras de US$1.355M en el semestre."),
    ],
    # Séptima ronda (1-oct-2026): conversor de I+D con períodos alineados al LTM, como la corrección verificada de ADBE.
    # El año −1 del conversor debe ser los doce meses anteriores al LTM, no el último ejercicio fiscal (que se solapa
    # con el LTM): LTM a jun-2025 = ejercicio 2024 + 1S25 − 1S24, y así hacia atrás (10-Q de cada año, SEC EDGAR).
    "DUOL_RD": [
        (RD, "B12", "='Income Statement'!J10+144,06-106,025", "I+D de los 12 meses a jun-2025 = 2024 (235,3) + 1S25 (144,06) − 1S24 (106,025) = 273,3 (10-Q 2T25 y 2T24). Antes el ejercicio 2025, que se solapa con el LTM."),
        (RD, "B13", "='Income Statement'!I10+106,025-93,791", "12 meses a jun-2024 = 2023 + 1S24 − 1S23 (10-Q). Antes el ejercicio 2024."),
        (RD, "B14", "='Income Statement'!H10+93,791-63,998", "12 meses a jun-2023 = 2022 + 1S23 − 1S22 (10-Q). Antes el ejercicio 2023."),
    ],
    "PLTR_RD": [
        (RD, "B12", "='Income Statement'!J10+269,932-218,821", "I+D de los 12 meses a jun-2025 = 2024 (507,9) + 1S25 (269,9) − 1S24 (218,8) (10-Q). Antes el ejercicio 2025, que se solapa con el LTM."),
        (RD, "B13", "='Income Statement'!I10+218,821-189,633", "12 meses a jun-2024 = 2023 + 1S24 − 1S23 (10-Q). Antes el ejercicio 2024."),
        (RD, "B14", "='Income Statement'!H10+189,633-176,772", "12 meses a jun-2023 = 2022 + 1S23 − 1S22 (10-Q). Antes el ejercicio 2023."),
    ],
    "PYPL_RD": [
        (RD, "B12", "='Income Statement'!J10+1498-1460", "Tecnología y desarrollo de los 12 meses a jun-2025 = 2024 (2.979) + 1S25 (1.498) − 1S24 (1.460) (10-Q). Antes el ejercicio 2025, que se solapa con el LTM."),
        (RD, "B13", "='Income Statement'!I10+1460-1464", "12 meses a jun-2024 = 2023 + 1S24 − 1S23 (10-Q). Antes el ejercicio 2024."),
        (RD, "B14", "='Income Statement'!H10+1464-1630", "12 meses a jun-2023 = 2022 + 1S23 − 1S22 (10-Q). Antes el ejercicio 2023."),
    ],
    "UBER_RD": [
        (RD, "B12", "='Income Statement'!J10+1655-1550", "I+D de los 12 meses a jun-2025 = 2024 (3.109) + 1S25 (1.655) − 1S24 (1.550) (10-Q). Antes el ejercicio 2025, que se solapa con el LTM."),
        (RD, "B13", "='Income Statement'!I10+1550-1583", "12 meses a jun-2024 = 2023 + 1S24 − 1S23 (10-Q). Antes el ejercicio 2024."),
        (RD, "B14", "='Income Statement'!H10+1583-1291", "12 meses a jun-2023 = 2022 + 1S23 − 1S22 (10-Q). Antes el ejercicio 2023."),
    ],
    # MSFT cierra en junio: el LTM es el ejercicio 2026, así que el año −1 es el ejercicio 2025 (antes repetía el 2026).
    "MSFT_RD": [
        (RD, "B12", "='Income Statement'!J10", "Año −1 = ejercicio a jun-2025 (32.488). Antes repetía el ejercicio a jun-2026, que es el mismo LTM: el activo de I+D contaba dos veces el año actual."),
        (RD, "B13", "='Income Statement'!I10", "Año −2 = ejercicio a jun-2024. Antes el ejercicio a jun-2025."),
        (RD, "B14", "='Income Statement'!H10", "Año −3 = ejercicio a jun-2023. Antes el ejercicio a jun-2024."),
    ],
    # NVO (IFRS, coronas; la hoja convierte todos los años a 0,1531 USD/DKK): el año −k es el LTM a junio, escalando el
    # ejercicio anterior por la razón (ejercicio + 1S del año siguiente − 1S del año) / ejercicio, en coronas (6-K de Novo).
    "NVO_RD": [
        (RD, "B12", "='Income Statement'!J10*45288/48062", "12 meses a jun-2025 = 2024 (48.062) + 1S25 (21.998) − 1S24 (24.772) = 45.288 MDKK (6-K 2T25 y 4T24). Antes el ejercicio 2025, que se solapa con el LTM."),
        (RD, "B13", "='Income Statement'!I10*43360/32443", "12 meses a jun-2024 = 2023 (32.443) + 1S24 (24.772) − 1S23 (13.855) = 43.360 MDKK. Antes el ejercicio 2024."),
        (RD, "B14", "='Income Statement'!H10*27573/24047", "12 meses a jun-2023 = 2022 (24.047) + 1S23 (13.855) − 1S22 (10.329) = 27.573 MDKK. Antes el ejercicio 2023."),
        (RD, "B15", "='Income Statement'!G10*20213/17772", "12 meses a jun-2022 = 2021 (17.772) + 1S22 (10.329) − 1S21 (7.888) = 20.213 MDKK. Antes el ejercicio 2022."),
        (RD, "B16", "='Income Statement'!F10*16282/15462", "12 meses a jun-2021 = 2020 (15.462) + 1S21 (7.888) − 1S20 (7.068) = 16.282 MDKK. Antes el ejercicio 2021."),
    ],
    # Octava ronda (1-oct-2026): auditoría del balance LTM contra la SEC (XBRL del último 10-Q), como la de ADBE.
    # El importador dejaba en la columna LTM el cierre anual y omitía los valores negociables y las inversiones
    # no operativas. Solo se corrigen saldos reportados; la convención de arrendamientos de cada hoja se conserva.
    "BSX_BALANCE": [
        (BSH, "L20", 1709, "Deuda corriente al 30-jun-2026 (DebtCurrent, 10-Q 2T26); antes 299, el cierre de 2025."),
        (BSH, "L25", 10915, "Deuda de largo plazo al 30-jun-2026 (10-Q 2T26); antes 11.137, el cierre de 2025."),
        (BSH, "L14", 2245, "Inversiones al 30-jun-2026: método de participación 1.308 + sin valor de mercado 938 (10-Q). Antes 0: son activos no operativos."),
        (BSH, "L34", 24930, "Patrimonio de los accionistas al 30-jun-2026 (10-Q); antes 24.233, el cierre de 2025."),
        (BSH, "L35", 25172, "Patrimonio total con minoritarios al 30-jun-2026 (10-Q)."),
        (IS, "B21", 242, "Participaciones minoritarias al 30-jun-2026 (10-Q 2T26); antes 0."),
        (IS, "B15", "='Balance Sheet'!L34", "Patrimonio de los accionistas (sin minoritarios, que se restan aparte)."),
    ],
    "CELH_BALANCE": [
        (BSH, "L25", 668, "Deuda de largo plazo al 30-jun-2026 (10-Q 2T26); antes 669,9, el cierre de 2025."),
        (BSH, "L34", 1200, "Patrimonio al 30-jun-2026 (10-Q); antes 1.181,5, el cierre de 2025."),
        (BSH, "L35", 1200, "Patrimonio al 30-jun-2026 (10-Q); antes 1.181,5, el cierre de 2025."),
    ],
    "DPZ_BALANCE": [
        (BSH, "L20", 7, "Porción corriente de deuda y arrendamientos financieros al 14-jun-2026 (10-Q 2T26)."),
        (BSH, "L25", 4876, "Deuda de largo plazo con arrendamientos financieros al 14-jun-2026 (10-Q 2T26); antes 4.810,7, el cierre de 2025."),
        (BSH, "L14", 28, "Valores negociables de largo plazo al 14-jun-2026 (10-Q); antes 0."),
        (BSH, "L34", -3982, "Déficit patrimonial al 14-jun-2026 (10-Q); antes −3.901,1, el cierre de 2025."),
        (BSH, "L35", -3982, "Déficit patrimonial al 14-jun-2026 (10-Q); antes −3.901,1, el cierre de 2025."),
        (IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", "Deuda financiera al 14-jun-2026 (antes 4.816,8 fijo, del cierre de 2025). Sin arrendamientos operativos, como antes."),
    ],
    "DUOL_BALANCE": [
        (BSH, "L4", 133, "Inversiones mantenidas al vencimiento de corto plazo al 30-jun-2026 (10-Q 2T26); antes 0."),
        (BSH, "L5", 1313.9, "Caja 1.180,9 + inversiones de corto plazo 133 al 30-jun-2026 (10-Q)."),
        (BSH, "L14", 103, "Inversiones de largo plazo al 30-jun-2026 (10-Q); antes 135,1, el cierre de 2025."),
        (BSH, "L26", 86, "Arrendamientos de largo plazo al 30-jun-2026 (10-Q); antes 93,8."),
        (BSH, "L34", 1410, "Patrimonio al 30-jun-2026 (10-Q); antes 1.347, el cierre de 2025."),
        (BSH, "L35", 1410, "Patrimonio al 30-jun-2026 (10-Q); antes 1.347, el cierre de 2025."),
        (IS, "B20", "='Balance Sheet'!L14", "Activos no operativos = inversiones de largo plazo. Antes sumaba «Other Long-Term Assets» (320,8), que no son inversiones."),
    ],
    "EPAM_BALANCE": [
        (BSH, "L21", 39.3, "Porción corriente de arrendamientos al 30-jun-2026 (10-Q 2T26)."),
        (BSH, "L26", 88, "Arrendamientos de largo plazo al 30-jun-2026 (10-Q); antes 81,5."),
        (BSH, "L34", 3519, "Patrimonio al 30-jun-2026 (10-Q); antes 3.677,2, el cierre de 2025."),
        (BSH, "L35", 3519, "Patrimonio al 30-jun-2026 (10-Q); antes 3.677,2, el cierre de 2025."),
    ],
    "GOOG_BALANCE": [
        (BSH, "L4", 186563, "Valores negociables al 30-jun-2026 (10-Q 2T26); antes 0: la caja del DCF omitía los valores negociables."),
        (BSH, "L5", 242474, "Caja y valores negociables al 30-jun-2026 = 55.911 + 186.563 (10-Q)."),
        (BSH, "L14", 131461, "Valores no negociables y otras inversiones de largo plazo al 30-jun-2026 (10-Q); antes 0: son activos no operativos."),
        (BSH, "L20", 1999, "Porción corriente de la deuda al 30-jun-2026 (10-Q)."),
        (BSH, "L25", 98165, "Deuda de largo plazo al 30-jun-2026 (10-Q); antes 46.547, el cierre de 2025."),
        (BSH, "L21", 3446, "Arrendamientos operativos corrientes al 30-jun-2026 = 18.037 − 14.591 (10-Q)."),
        (BSH, "L26", 14591, "Arrendamientos operativos de largo plazo al 30-jun-2026 (10-Q); antes 12.744."),
        (BSH, "L34", 640480, "Patrimonio al 30-jun-2026 (10-Q); antes 415.265, el cierre de 2025."),
        (BSH, "L35", 640480, "Patrimonio al 30-jun-2026 (10-Q); antes 415.265, el cierre de 2025."),
    ],
    "NVDA_BALANCE": [
        (BSH, "L4", 34143, "Valores negociables (deuda) al 26-jul-2026 (10-Q 2T FY27); antes 0."),
        (BSH, "L5", 56586, "Caja 22.443 + valores negociables 34.143 al 26-jul-2026 (10-Q)."),
        (BSH, "L14", 90681, "Inversiones en acciones al 26-jul-2026: cotizadas 42.783 + no cotizadas 47.898 (10-Q); antes 0: son activos no operativos."),
        (BSH, "L20", 1000, "Porción corriente de la deuda al 26-jul-2026 (10-Q)."),
        (BSH, "L25", 32366, "Deuda de largo plazo al 26-jul-2026 (10-Q); antes 7.469, el cierre de enero de 2026."),
        (BSH, "L21", 509, "Arrendamientos operativos corrientes al 26-jul-2026 (10-Q)."),
        (BSH, "L26", 4985, "Arrendamientos operativos de largo plazo al 26-jul-2026 (10-Q); antes 2.572."),
        (BSH, "L34", 228984, "Patrimonio al 26-jul-2026 (10-Q); antes 157.293, el cierre de enero de 2026."),
        (BSH, "L35", 228984, "Patrimonio al 26-jul-2026 (10-Q); antes 157.293, el cierre de enero de 2026."),
    ],
    "ZTS_BALANCE": [
        (BSH, "L4", 200, "Inversiones de corto plazo al 30-jun-2026 (10-Q 2T26); antes 0."),
        (BSH, "L5", 1676, "Caja 1.476 + inversiones de corto plazo 200 al 30-jun-2026 (10-Q)."),
        (BSH, "L25", 9048, "Deuda de largo plazo al 30-jun-2026 (10-Q); antes 9.042."),
        (BSH, "L26", 190, "Arrendamientos de largo plazo al 30-jun-2026 (10-Q); antes 196."),
        (BSH, "L34", 3148, "Patrimonio al 30-jun-2026 (10-Q); antes 3.331, el cierre de 2025."),
        (BSH, "L35", 3148, "Patrimonio al 30-jun-2026 (10-Q); antes 3.331, el cierre de 2025."),
    ],
    "SHAK_BALANCE": [
        (BSH, "L26", 622, "Arrendamientos operativos de largo plazo al 1-jul-2026 (10-Q 2T26); antes 575,1."),
        (BSH, "L34", 544, "Patrimonio de los accionistas al 1-jul-2026 (10-Q); antes 525,3, el cierre de 2025."),
        (BSH, "L35", 572, "Patrimonio total con minoritarios al 1-jul-2026 (10-Q)."),
        (IS, "B15", "='Balance Sheet'!L34", "Patrimonio de los accionistas (sin minoritarios, que se restan aparte)."),
        (IS, "B21", 27, "Participaciones minoritarias al 1-jul-2026 (10-Q 2T26); antes 0."),
    ],
    # ONON (NIIF, francos; la hoja convierte a USD al tipo implícito de su caja LTM: 1.490,8 / 1.205,6 = 1,2366).
    "ONON_BALANCE": [
        (BSH, "L20", 108.7, "Arrendamientos corrientes al 30-jun-2026: 87,9 MCHF × 1,2366 (6-K 1S26). Antes 102,6, el cierre de 2025. Sin deuda bancaria dispuesta."),
        (BSH, "L26", 586.9, "Arrendamientos no corrientes al 30-jun-2026: 474,6 MCHF × 1,2366 (6-K 1S26). Antes 556,1."),
        (BSH, "L34", 2363.6, "Patrimonio al 30-jun-2026: 1.911,4 MCHF × 1,2366 (6-K 1S26). Antes 2.061,9, el cierre de 2025."),
        (BSH, "L35", 2363.6, "Patrimonio al 30-jun-2026: 1.911,4 MCHF × 1,2366 (6-K 1S26). Antes 2.061,9, el cierre de 2025."),
        (BSH, "L16", 4010.2, "Activos totales al 30-jun-2026: 3.242,9 MCHF × 1,2366 (6-K 1S26)."),
        (BSH, "L29", 1646.5, "Pasivos totales al 30-jun-2026: 1.331,5 MCHF × 1,2366 (6-K 1S26)."),
    ],
    # PAGS (NIIF, reales; la hoja convierte a USD: flujos a 5.5877 BRL/USD, el implícito en su flujo operativo de 2025;
    # balance a 5.4762, el implícito en su patrimonio de dic-2025). 20-F 2025 y 6-K 1S26 (estados intermedios).
    "PAGS_BALANCE": [
        (BSH, "L34", 2742.0, "Patrimonio al 30-jun-2026: R$15.015.865 mil / 5.4762 (6-K 1S26). Antes 2.673,3, el cierre de 2025."),
        (BSH, "L35", 2742.0, "Patrimonio al 30-jun-2026: R$15.015.865 mil / 5.4762 (6-K 1S26). Antes 2.673,3, el cierre de 2025."),
        (BSH, "L16", 13823.0, "Activos totales al 30-jun-2026: R$75.697.476 mil / 5.4762 (6-K 1S26)."),
        (BSH, "L29", 11080.9, "Pasivos totales al 30-jun-2026 = activos − patrimonio (6-K 1S26)."),
        (CFH, "K22", -411.6, "Flujo de inversión 2025: −R$2.299.796 mil / 5.5877 (20-F 2025). Antes 0 (no importado)."),
        (CFH, "K34", -775.4, "Flujo de financiación 2025: −R$4.332.796 mil / 5.5877 (20-F 2025). Antes 0 (no importado)."),
        (CFH, "L13", 1082.6, "Flujo operativo LTM = 2025 (7.562.431) + 1S26 (1.938.645) − 1S25 (3.451.822) = R$6.049.254 mil / 5.5877 (20-F y 6-K)."),
        (CFH, "L22", -431.9, "Flujo de inversión LTM = −2.299.796 − 1.215.583 + 1.101.798 = −R$2.413.581 mil / 5.5877 (20-F y 6-K). Antes 0."),
        (CFH, "L34", -740.9, "Flujo de financiación LTM = −4.332.796 − 1.956.893 + 2.149.485 = −R$4.140.204 mil / 5.5877 (20-F y 6-K). Antes 0."),
    ],
    "MSFT_BALANCE": [
        (IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L21+'Balance Sheet'!L25+'Balance Sheet'!L26+66594",
         "Se suman los arrendamientos financieros (66.594 al 30-jun-2026, 10-K FY26): son deuda (centros de datos) y su costo no está en el EBIT como alquiler. Antes se omitían."),
    ],
    # Novena ronda (1-oct-2026): la deuda de balance excluye los arrendamientos operativos, que entran por el conversor
    # (apply_lease_conversion.py, criterio Damodaran).
    "BSX_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "CELH_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "DUOL_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "EPAM_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "GOOG_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "INTU_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "LULU_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "NKE_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "NVDA_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "PYPL_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "UBER_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "ZTS_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "PLTR_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "ADBE_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25", ARREND)],
    "MSFT_ARREND": [(IS, "B16", "='Balance Sheet'!L20+'Balance Sheet'!L25+66594", ARREND + " MSFT: se conservan los 66.594 de arrendamientos financieros.")],
    # CELH_IMPUESTO se aplicó y se revirtió el 30-sep-2026: la hoja ya usa la tasa marginal (24%) desde el año 1
    # ('Valuation output'!C8 = 'Input sheet'!B25); B24 solo alimenta el año base y no cambia el valor.
    "CELH_IMPUESTO": [
        (IS, "B24", 0.205, "Tasa efectiva de los años 1-5 = promedio 2023-2025 (22,3%, 25,6% y 13,6%). La del LTM (8,8%) refleja beneficios fiscales de una vez y no es sostenible."),
    ],
}

# ROIC después del año 10 con el criterio Damodaran (reference/moat_2026-09-30.json, campo "regla"):
#   sin ventaja defendible -> costo de capital (B49 = "No");
#   ventaja durable -> promedio de la industria, entre el costo de capital terminal y el ROIC actual;
#   ventaja que se desvanece -> punto medio entre el costo de capital terminal y ese valor.
# Las rondas anteriores (<T>_MOAT) conservan su respaldo en reference/revision_dcf_2026-09-30/ y se revierten con
# --revert. La ronda vigente usa la clave <T>_ROIC solo para las hojas que cambian con este criterio.
_MOAT = json.loads((_ROOT / "reference" / "moat_2026-09-30.json").read_text())["empresas"]
_p = lambda x: f"{x * 100:.1f}".replace(".", ",") + "%"  # noqa: E731


def _roic_nota(m: dict) -> str:
    base = f"{m['ventaja'].capitalize()}: {m['fuentes']}. Evidencia: {m['evidencia']}."
    if m["roic_terminal"] is None:
        return base + " ROIC después del año 10 = costo de capital (supuesto por defecto de Damodaran)."
    ind = _p(m["roic_industria"]) if m["roic_industria"] else "sin dato"
    ref = (f"el promedio de la industria ({ind}), sin superar el ROIC actual ({_p(m['roic_actual'])}): {_p(m['referencia'])}")
    if m["ventaja"] == "ventaja durable":
        return base + f" ROIC después del año 10 = {ref} (Damodaran, Investment Valuation, cap. 12)."
    return base + (f" ROIC después del año 10 = {_p(m['roic_terminal'])}, punto medio entre el costo de capital terminal "
                   f"({_p(m['costo_capital_terminal'])}) y {ref}, porque la ventaja se desvanece.")


# MSFT (1-oct-2026): el ROIC actual sube a 26,5% al corregir el conversor de I+D y sigue bajo el de la industria.
# 1-oct-2026: ROIC actual con capital operativo y balance del último 10-Q (auditoría de estados).
for _t in ("CMG", "AFYA", "LULU", "EPAM", "MSFT", "GOOG", "INTU", "NKE", "PYPL", "ADBE"):
    _m = _MOAT[_t]
    CHANGES[f"{_t}_ROIC"] = [(IS, "B49", "Yes", _roic_nota(_m)), (IS, "B50", _m["roic_terminal"], _roic_nota(_m))]


def main(argv: list[str]) -> int:
    dry, revert = "--dry-run" in argv, "--revert" in argv
    tickers = [a for a in argv if not a.startswith("--")] or list(CHANGES)
    OUT.mkdir(parents=True, exist_ok=True)
    client = get_gspread_client()
    for tk in tickers:
        base_tk = tk.split("_")[0]  # "BSX_IMPUESTO" = otra ronda de cambios de BSX, con su propio respaldo
        sid = json.loads((_ROOT / "reference" / "multiplos_v3" / f"{base_tk}_anclas.json").read_text())["sheet_id"]
        sh = client.open_by_key(sid)
        bk_path = OUT / f"{tk}.json"
        if revert:
            bk = json.loads(bk_path.read_text())
            data = [{"range": f"'{c['hoja']}'!{c['celda']}", "values": [[c["antes"]]]} for c in bk["cambios"]]
            sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": data})
            print(f"{tk}: restauradas {len(data)} celdas")
            continue
        ranges = [f"'{h}'!{c}" for h, c, _, _ in CHANGES[tk]]
        cur = sh.values_batch_get(ranges, params={"valueRenderOption": "FORMULA"})["valueRanges"]
        cambios = []
        for (h, c, new, why), vr in zip(CHANGES[tk], cur):
            old = (vr.get("values") or [[None]])[0][0]
            cambios.append({"hoja": h, "celda": c, "antes": old, "despues": new, "motivo": why})
            print(f"{tk:5s} {h[:24]:24s} {c:4s} {old!s:>28} -> {new}")
        if dry:
            continue
        # El respaldo guarda siempre el estado original: en una ronda posterior solo se agregan las celdas nuevas.
        bk = json.loads(bk_path.read_text()) if bk_path.exists() else {"ticker": tk, "sheet_id": sid, "fecha": "2026-09-30", "cambios": []}
        vistas = {(c["hoja"], c["celda"]) for c in bk["cambios"]}
        bk["cambios"] += [c for c in cambios if (c["hoja"], c["celda"]) not in vistas]
        bk_path.write_text(json.dumps(bk, ensure_ascii=False, indent=1))
        # USER_ENTERED: los números entran como números y las fórmulas (conversor de I+D) como fórmulas.
        sh.values_batch_update({"valueInputOption": "USER_ENTERED", "data": [{"range": f"'{c['hoja']}'!{c['celda']}", "values": [[c["despues"]]]} for c in cambios]})
        for c in cambios:
            sh.worksheet(c["hoja"]).insert_note(c["celda"], f"Revisión 30-sep-2026: antes {c['antes']}, ahora {c['despues']}. {c['motivo']}")
            time.sleep(0.4)
        time.sleep(3)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
