#!/usr/bin/env python
"""Valoracion de Alphabet Inc., clase C sin voto (GOOG), sobre la
plantilla maestra (copia limpia hecha a mano en Drive, ver
scripts/reset_from_master.py), con el mismo proceso generico de NKE/PYPL
(refresh_native_model.run) mas supuestos y contenido a medida.

Particularidades de Alphabet que este script resuelve:
  - Clase de acciones: Alphabet cotiza en tres clases (A con voto, B con
    10 votos -no listada-, C sin voto). El ticker de esta valoracion es
    GOOG (clase C). Los datos contables de SEC EDGAR (CIK 0001652044) son
    los mismos para cualquier ticker de la empresa; el precio de mercado
    (Input sheet!D1, Trailing Valuation) es el propio de GOOG via
    yfinance. Las acciones en circulacion (`CommonStockSharesOutstanding`,
    ~12.230M) ya vienen combinadas de las 3 clases: como A/B/C tienen los
    mismos derechos economicos (solo difieren en el voto), el valor por
    accion del DCF y los multiplos aplica igual a las 3 clases, y dividir
    por el total combinado es lo correcto (no hay que prorratear).
  - Alphabet empezo a pagar dividendo recien en 2024 (historia corta).
  - Sin deuda financiera relevante (rating AA+/Aa2): Cost of capital casi
    100% equity.

Pasos: refresh | assumptions | content  (--step all corre todos)
Uso:
    SEC_EDGAR_USER_AGENT="JMR Valuation <email>" PYTHONPATH=.:scripts python scripts/run_google.py --step all
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

SHEET_ID = "1yt2zqdGz1JWEqV3SYqqL-nHarO7C1Oud1lvR3pY9i0U"
TICKER = "GOOG"
INDUSTRY = "Software (Internet)"
PEER_TICKERS = ["META", "MSFT", "AMZN"]
BACKUP_PATH = _ROOT / "reference" / "backups" / "google_formula_backup.json"


def step_refresh() -> None:
    ms.install_augmented_client(TICKER)
    rnm.run(TICKER, sheet_id=SHEET_ID, peer_tickers=PEER_TICKERS, industry_us=INDUSTRY, industry_global=INDUSTRY)


def step_assumptions() -> None:
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Input sheet", {
        "B17": "No",   # sin I+D separado (ya se activa como intangible en la contabilidad de Alphabet)
        "B18": "No",   # arrendamientos ya incluidos en la deuda reportada
        # Supuestos Base: LTM +10,7% (Cloud/IA compensan la madurez de Search y YouTube);
        # margen objetivo con expansion moderada sobre el operativo LTM real (32,6%->33,5%),
        # no el 36% que sale del promedio historico (incluye capex de IA muy por delante
        # del ingreso que genera todavia).
        "B27": 0.11,   # Año 1: en linea con el crecimiento LTM real (10,7%)
        "B28": 0.325,  # margen Año 1: LTM 33,1% menos algo de presion por depreciacion de capex de IA
        "B29": 0.07,   # años 2-5: converge hacia el crecimiento nominal de EE.UU. + prima de IA/Cloud
        "B30": 0.335,  # margen objetivo Base: expansion moderada (no el 36% del promedio historico)
        "B31": 5,
        "B32": 2.5,    # sales-to-capital: negocio de software/servicios, poco capital por dolar de ventas nuevas
        "B33": 2.0,
        "B25": 0.16,   # tasa marginal de impuestos de largo plazo (corporativa de EE.UU. 21% + estatal/exterior neto)
        "B46": "Yes",
        "B47": 0.09,   # WACC terminal: mantiene una prima moderada, no cae al ERP maduro puro
    }, "Supuestos GOOG Base (ver hoja Tesis de Inversión y Supuestos)", bk)
    ms.write_with_backup(sh, "Cost of capital worksheet", {
        # Beta de industria (Software/Internet, Damodaran) sale en 1,34 desapalancada: sobreestima
        # el riesgo de Alphabet (esa canasta la dominan empresas mucho mas chicas y de un solo
        # producto -Snap, Pinterest, Match-; Alphabet diversifica en Cloud, YouTube y Otras Apuestas
        # y tiene un beta regresivo real bastante mas bajo). Direct Input con beta observado ~1,05.
        "B22": "Direct Input", "B23": 1.05,
        "B26": "Country of Incorporation",  # EE.UU.: sin prima de riesgo pais
        # Costo de deuda: calificacion real Aa2/AA (S&P/Moody's), no el A1/A+ generico de la
        # plantilla. Vencimiento promedio ~10 años (bonos largos emitidos en 2020/2025 para IA).
        "B33": 10, "B36": "Aa2/AA",
    }, "Costo de capital GOOG (beta observado, sin deuda financiera material, calificacion real)", bk)
    ms.write_with_backup(sh, "Valuation output", {
        # Conservador: sin mas expansion de margen (se queda en el LTM real); Optimista: el
        # apalancamiento operativo de la nube compensa el capex de IA.
        "C45": 0.325, "C46": 0.335, "C47": 0.37,
        "C55": 0.06, "C106": 0.16,
    }, "Escenarios GOOG: orden Conservador < Base < Optimista", bk)


def step_content() -> None:
    import google_content as gc
    sh = ms.open_sheet(SHEET_ID)
    bk = BACKUP_PATH
    ms.write_with_backup(sh, "Cualitativo", gc.CUALITATIVO, "Contenido cualitativo GOOG", bk)
    ms.write_with_backup(sh, "Estadísticas", gc.ESTADISTICAS, "Estadisticas GOOG (formulas vivas)", bk)
    ms.write_with_backup(sh, "Stories to Numbers", gc.STORIES, "Historia GOOG", bk)
    ms.write_with_backup(sh, "Supuestos Recomendados", gc.SUPUESTOS_RECOMENDADOS, "Recomendaciones GOOG", bk)
    ms.write_with_backup(sh, "Supuestos de los Múltiplos", {"A12": gc.MULTIPLOS_EVALUACION}, "Evaluacion de multiplos GOOG", bk)
    gc.format_estadisticas(sh)
    gc.write_tesis(sh, bk)


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
