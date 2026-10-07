#!/bin/bash
# Regenera la cartera completa desde las hojas de cálculo (3-oct-2026).
#
#   scripts/regenerar_cartera.sh [--drive] [TICKER ...]     (sin tickers: las 22 de reference/cartera_drive.json)
#
# Orden por empresa: valoración de la app desde la hoja -> crecimiento implícito -> sincronización tras el DCF ->
# valor esperado -> MOS -> auditoría -> sección Damodaran -> tabla de escenarios -> informe v3. Después, para todas:
# tablas de horizontes en el research de la app, consistencia (16 controles) e integridad de las hojas.
# Con --drive sube al final los informes a Drive (scripts/subir_drive.py). Se corre desde cualquier carpeta; espera
# Modelo-JMR y Modelo-JMR-datos junto a JMR-valuation. Las llamadas a Google se reintentan (cuota de 60 lecturas/min).
# Un paso del modelo que falle detiene esa empresa en ese paso y sigue con la siguiente; el resumen final lo indica.
set -u -o pipefail
cd "$(dirname "$0")/.."
DRIVE=0; [ "${1:-}" = "--drive" ] && { DRIVE=1; shift; }
TICKERS=${*:-$(python3 -c "import json;print(' '.join(sorted(json.load(open('reference/cartera_drive.json'))['empresas'])))")}
D=../Modelo-JMR-datos
mkdir -p .cache/js
[ -s .cache/js/xlsx.full.min.js ] || curl -fsS -o .cache/js/xlsx.full.min.js https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js
[ -s .cache/js/marked.min.js ] || curl -fsS -o .cache/js/marked.min.js https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js
export PYTHONPATH=.:scripts SHEETJS_PATH=$PWD/.cache/js/xlsx.full.min.js MARKED_PATH=$PWD/.cache/js/marked.min.js
export JMR_FECHA=${JMR_FECHA:-$(python3 -c "import json;print(json.load(open('reference/corte_vigente.json'))['fecha_corte'])")}
[ -z "${CHROMIUM_PATH:-}" ] && CHROMIUM_PATH=$(ls -d /opt/pw-browsers/chromium-*/chrome-linux/chrome 2>/dev/null | head -1) && export CHROMIUM_PATH

reintentar() {  # reintentar <segundos> <comando...>: hasta 3 intentos con 60 s de espera
  local t=$1; shift
  for i in 1 2 3; do timeout "$t" "$@" && return 0; echo "  reintento $i: $*" >&2; python3 -c "import time;time.sleep(60)"; done
  return 1
}

FALLAS=()
for T in $TICKERS; do
  echo "===== $T $(date +%H:%M:%S)"
  V=$(ls $D/valoraciones/$T-*.json | grep -v regen | head -1)
  ok=1
  reintentar 900 python3 scripts/regen_valoracion_app.py $T | tail -1 || ok=0
  [ $ok = 1 ] && { reintentar 600 python3 scripts/implied_growth.py $T | tail -1 | cut -c1-110 || ok=0; }
  [ $ok = 1 ] && { timeout 900 python3 scripts/sync_saved_after_dcf.py $V | grep -i "guardada\|error\|trace" | cut -c1-160; }
  if [ $ok = 1 ]; then
    for s in sync_valor_esperado normalize_saved_mos audit_report insert_damodaran_section insert_scenarios_table; do
      python3 scripts/$s.py $D $T | tail -1 || { ok=0; break; }
    done
  fi
  [ $ok = 1 ] && { reintentar 600 python3 scripts/valuation_report_v3.py --ticker $T --saved $V --out data/ | tail -1 | cut -c1-120 || ok=0; }
  # Módulo aditivo: solo se recalcula si el ticker ya optó por múltiplos históricos normalizados.
  # No modifica DCF, escenarios, múltiplos vigentes ni ponderaciones.
  if [ $ok = 1 ] && [ -s "reference/historical_multiples/$T.json" ]; then
    reintentar 600 python3 scripts/historical_multiples.py "$T" --write-sheet --patch-app | tail -1 || ok=0
  fi
  [ $ok = 1 ] || FALLAS+=("$T")
  python3 -c "import time;time.sleep(20)"
done

echo "===== tablas de horizontes en el research de la app"
reintentar 1800 python3 scripts/insert_research_horizons_app.py $TICKERS || FALLAS+=("horizontes")
echo "===== consistencia"
python3 scripts/consistencia_app.py $TICKERS | tail -3 || FALLAS+=("consistencia")
echo "===== integridad de las hojas"
python3 scripts/integridad_hojas.py $TICKERS | grep -v "^\s*$" || FALLAS+=("integridad")
if [ $DRIVE = 1 ]; then
  echo "===== Drive"; python3 scripts/subir_drive.py $TICKERS | tail -1 || FALLAS+=("drive")
fi
[ ${#FALLAS[@]} = 0 ] && echo "FIN: sin fallas" || { echo "FIN con fallas: ${FALLAS[*]}"; exit 1; }
