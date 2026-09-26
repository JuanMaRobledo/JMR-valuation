"""Supuestos y contenido de la valoracion de Afya (AFYA). Los numeros de
cada supuesto estan justificados en la hoja 'Tesis de Inversión y
Supuestos' y en data/AFYA_Research_Fundamental_Modelo_JMR_2026-09-26.md."""
from __future__ import annotations

import model_steps as ms
import refresh_native_model as rnm
import run_afya as ra


def step_assumptions() -> None:
    sh = ms.open_sheet(ra.SHEET_ID)
    bk = ra.BACKUP_PATH

    # Gasto financiero bruto: la fila 16 sumaba ingreso + gasto (mismo bug que ADSK).
    ms.write_with_backup(sh, "Income Statement", {f"{c}16": f"=-{c}15" for c in "EFGHIJKL"},
                         "Gasto financiero bruto (fila 16 = ingreso - (-gasto) sumaba ambos)", bk)

    ms.write_with_backup(sh, "Input sheet", {
        "B4": ms.serial(ra.VALUATION_DATE),
        "B17": "No",      # sin I+D separado (contenido y producto digital se activan como intangible)
        "B18": "No",      # arrendamientos IFRS 16 ya incluidos en la deuda (filas 21/26)
        "B21": round(ra.BAL_JUN26["nci"] / ra.FX_JUN26, 1),   # participaciones no controladoras (30-jun-2026)
        # Tasa marginal de largo plazo: PROUNI exime IRPJ/CSLL de la mayor parte del ingreso de grado;
        # como parte del grupo Bertelsmann, Afya queda bajo el minimo global de 15% (Pilar Dos,
        # vigente en Brasil desde 2025; 6-K del 13-ago-2026). La corporativa de Brasil (34%) no aplica.
        "B25": 0.15,
        # Supuestos Base (US$; crecimiento en reales menos ~1,5pp de diferencial de inflacion Brasil-EE.UU.)
        "B27": 0.06,      # Año 1 (jul-26/jun-27): guia 2026 R$3.950-4.100M (+7-11%), H1 +7% -> ~7,5% en R$
        "B28": 0.315,     # margen LTM 32,6% menos el ciclo de inversion guiado (EBITDA ajustado -190pb en el H1)
        "B29": 0.05,      # años 2-5: ~6,5% en R$ (ticket ~inflacion + maduracion de plazas) -> ~5% en US$
        "B30": 0.33,      # margen objetivo: FY2025 32,8%; sin expansion adicional por la competencia de plazas nuevas
        "B31": 5,
        "B32": 1.5,       # anclado al FCFF real (organico): con 1,5x el FCFF del Año 1 (~US$190M) ~ LTM
        "B33": 1.2,       # años 6-10: el crecimiento vuelve a requerir plazas nuevas (compradas o construidas)
        "B35": ra.UST_10Y,
        # Costo de capital en la etapa estable: se mantiene el riesgo pais de Brasil (el default de la
        # plantilla es rf + ERP maduro = 9,3%, que borraria el riesgo pais en perpetuidad).
        "B46": "Yes",
        "B47": 0.11,
    }, "Supuestos AFYA (ver hoja Tesis de Inversión y Supuestos)", bk)

    ms.write_with_backup(sh, "Country equity risk premiums", {
        "B2": ra.MATURE_ERP, "C2": "Updated September 1, 2026",
    }, "ERP de mercado maduro (Damodaran, 1-sep-2026)", bk)

    ms.write_with_backup(sh, "Cost of capital worksheet", {
        "B22": "Single Business(Global)",  # beta desapalancada global de Education (Damodaran) = 0,74
        "B26": "Country of Incorporation", # Brasil: ERP 4,09% + prima pais 3,24%
        "B33": 4,                          # duracion de la deuda: 3,7 años (6-K 2Q26)
        # Kd en US$ = rf + spread soberano de Brasil (2,13%) + spread de la empresa (Ba1/BB+, 1,38%)
        "B34": "Direct Input",
        "B35": round(ra.UST_10Y + 0.0213 + 0.0138, 4),
    }, "Cost of capital AFYA", bk)

    ms.write_with_backup(sh, "Valuation output", {
        # Conservador: la oferta de plazas nuevas (Mais Médicos, ENAMED) presiona ticket y ocupacion.
        "C45": 0.29,
        # Optimista: +3pp (la plantilla usa +5pp: 38% dejaria a Afya por encima de cualquier par).
        "C47": "='Input sheet'!B30+0,03",
    }, "Escenarios AFYA: orden Conservador < Base < Optimista", bk)

    ms.write_with_backup(sh, "Resumen de Valoración", {"G3": "Madura", "C25": ra.PRICE_AT_ANALYSIS},
                         "Tipo de empresa y precio del analisis (cierre 25-sep-2026)", bk)
    rnm._apply(sh.worksheet("Resumen de Valoración"), [("B3", [["=C25"]])])


def step_content() -> None:
    import afya_content as ac

    sh = ms.open_sheet(ra.SHEET_ID)
    bk = ra.BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", ac.CUALITATIVO, "Contenido cualitativo AFYA", bk)
    ms.write_with_backup(sh, "Estadísticas", ac.ESTADISTICAS, "Estadisticas AFYA (formulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", ac.STORIES, "Historia AFYA", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", ac.SUPUESTOS_RECOMENDADOS, "Recomendaciones AFYA", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": ac.MULTIPLOS_EVALUACION}, "Evaluacion de multiplos AFYA", bk)
    ac.write_tesis(sh, bk)
