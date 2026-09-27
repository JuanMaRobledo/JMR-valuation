#!/usr/bin/env python
"""Valoracion de NVIDIA Corporation (NVDA) sobre la plantilla maestra
auditada (misma hoja que el usuario provisto, ya reiniciada con
scripts/reset_from_master.py para tener las correcciones vigentes),
con el mismo proceso generico de NKE/PYPL/GOOG (refresh_native_model.run)
mas supuestos y contenido a medida.

Particularidades de Nvidia que este script resuelve:
  - Crecimiento extremo pero desacelerando: FY2026 (cerrado ene-2026)
    ingresos +65% i.a. (US$215.900M); Data Center +117% i.a. en el 2T
    FY2027 (jul-2026). La compañia guio ~70% de crecimiento para FY2028
    ("supply-constrained"), pero eso no es sostenible como tasa de
    convergencia de largo plazo del DCF -- los 3 escenarios reflejan
    distintos grados de desaceleracion, no el ritmo actual.
  - Riesgo de sustitucion por ASICs a medida de los hiperescaladores
    (TPU de Google, Trainium de Amazon, Maia de Microsoft, MTIA de
    Meta): ~40% de los ingresos de Nvidia vienen de 4 clientes que
    estan construyendo chips propios. Esto castiga el margen objetivo
    y el crecimiento de largo plazo en el escenario Conservador.
  - Beta observado muy por encima del beta de industria de
    Damodaran (Semiconductor): la concentracion de la narrativa de IA
    en un solo nombre eleva el riesgo idiosincratico especifico de
    Nvidia por encima del promedio de la industria de semiconductores
    (dominada por jugadores mas diversificados). Direct Input con beta
    observado ~1,90.
  - Calificacion crediticia real muy solida (Aa1 Moody's / AA S&P,
    set-2026): se usa "Actual Rating" en vez del generico A1/A+ de la
    plantilla.

Pasos: refresh | assumptions | content  (--step all corre todos)
Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts python scripts/run_nvidia.py --step all
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
for p in (str(_ROOT), str(_ROOT / "scripts")):
    if p not in sys.path:
        sys.path.insert(0, p)

import model_steps as ms  # noqa: E402
import refresh_native_model as rnm  # noqa: E402

SHEET_ID = "1eEsuWSHXWQrBa2Dt5l_9Fbx24M4pug15Rx_Gj-CCkMg"
TICKER = "NVDA"
INDUSTRY = "Semiconductor"
PEER_TICKERS = ["AMD", "AVGO", "INTC"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "nvidia_formula_backup.json"


def step_refresh() -> None:
    ms.install_augmented_client(TICKER)
    rnm.run(TICKER, sheet_id=SHEET_ID, peer_tickers=PEER_TICKERS, industry_us=INDUSTRY, industry_global=INDUSTRY)


def step_assumptions() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Input sheet", {
        "B17": "No",  # I+D ya se capitaliza dentro de la contabilidad reportada de Nvidia (via ajuste generico del loader)
        "B18": "No",  # sin arrendamientos operativos materiales fuera de deuda ya reportada
        # Supuestos Base: Año 1 desacelera desde el ritmo actual (Data Center +117% i.a.
        # en el 2T FY2027) hacia la mitad de lo que Nvidia guio para FY2028 (~70%,
        # "supply-constrained", Jensen Huang) -- no tomamos la guia de la propia empresa
        # como caso central porque asume que la oferta (no la demanda) sigue siendo la
        # unica restriccion, sin ceder nada de cuota a los ASICs de los hiperescaladores.
        "B27": 0.50,   # Año 1 Base: desaceleracion desde 117% (Data Center 2T FY27) hacia la mitad de la guia FY28 de Nvidia (~70%)
        "B28": 0.60,   # margen operativo Año 1 Base: en linea con el margen GAAP real FY2026 (60,4%)
        "B29": 0.14,   # años 2-5 Base: la demanda de compute de IA se mantiene fuerte pero los ASICs propios de los hiperescaladores empiezan a restar crecimiento incremental
        "B30": 0.58,   # margen objetivo Base: leve compresion desde el 60,4% actual por presion de precio de los ASICs y mezcla hacia productos de menor margen relativo
        "B31": 5,
        "B32": 3.0,    # sales-to-capital: diseño de chips fabless, sin fabricas propias (TSMC fabrica), relativamente liviano en capital fijo
        "B33": 2.5,
        "B25": 0.16,   # tasa marginal de largo plazo: corporativa de EE.UU. (21%) neta de creditos fiscales/tasa efectiva historica mas baja de Nvidia
        "B46": "Yes",
        "B47": 0.09,   # WACC terminal: mantiene una prima sobre el ERP maduro puro, dado el perfil de crecimiento aun por encima del promedio de mercado
    }, "Supuestos NVDA Base (ver hoja Tesis de Inversión y Supuestos)", bk)
    ms.write_with_backup(sh, "Cost of capital worksheet", {
        # Beta de industria "Semiconductor" de Damodaran subestima el riesgo especifico
        # de Nvidia: esa canasta promedia decenas de fabricantes de chips mucho mas
        # diversificados y de menor crecimiento: el riesgo idiosincratico de Nvidia
        # (concentracion en la narrativa de IA, ~40% de ingresos de 4 clientes que
        # construyen ASICs propios) es sustancialmente mayor. Direct Input con beta
        # observado ~1,90 (fuentes de mercado citan 1,7-2,2 segun ventana/frecuencia).
        "B22": "Direct Input", "B23": 1.90,
        "B26": "Country of Incorporation",  # EE.UU.: sin prima de riesgo pais
        # Costo de deuda: calificacion real Aa1/AA (Moody's/S&P, set-2026), no el A1/A+
        # generico de la plantilla. Nvidia tiene muy poca deuda financiera frente a su
        # caja y generacion de flujo de caja.
        "B33": 10, "B36": "Aa1/AA",
    }, "Costo de capital NVDA (beta observado, calificacion real Aa1/AA)", bk)
    ms.write_with_backup(sh, "Valuation output", {
        # Conservador: los ASICs de los hiperescaladores erosionan margen y cuota mas
        # rapido de lo esperado; Optimista: la demanda de compute de IA sigue superando
        # a la oferta durante todo el horizonte de proyeccion, sin cesion de cuota.
        "C45": 0.50, "C46": 0.58, "C47": 0.65,
        "C55": 0.06, "C106": 0.22,
    }, "Escenarios NVDA: orden Conservador < Base < Optimista", bk)


def step_content() -> None:
    import nvidia_content as nc
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", nc.CUALITATIVO, "Contenido cualitativo NVDA", bk)
    ms.write_with_backup(sh, "Estadísticas", nc.ESTADISTICAS, "Estadisticas NVDA (formulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", nc.STORIES, "Historia NVDA", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", nc.SUPUESTOS_RECOMENDADOS, "Recomendaciones NVDA", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": nc.MULTIPLOS_EVALUACION}, "Evaluacion de multiplos NVDA", bk)
    nc.format_estadisticas(sh)
    nc.write_tesis(sh, bk)


STEPS = {"refresh": step_refresh, "assumptions": step_assumptions, "content": step_content}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--step", choices=[*STEPS, "all"], default="all")
    args = ap.parse_args(argv)
    for name, fn in STEPS.items():
        if args.step in (name, "all"):
            fn()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
