#!/bin/bash
# pipe.sh TICKER: historias -> hoja -> ancla C -> múltiplos -> historias -> regenerar_cartera -> refresco de la sección
set -u -o pipefail
cd "$(dirname "$0")/.."
export PYTHONPATH=.:scripts SEC_EDGAR_USER_AGENT="JMR Valuation juan0804@gmail.com"
S=$(mktemp -d)
T=$1
A=reference/multiplos_v3/${T}_anclas.json; D=reference/multiplos_v3/${T}_decision.json
r() {  # hasta 4 intentos con 70 s de espera (cuota de lecturas de Google: 60 por minuto)
  for i in 1 2 3 4; do "$@" > $S/_paso.log 2>&1 && { tail -3 $S/_paso.log; return 0; }; tail -2 $S/_paso.log; echo "  reintento $i: $*"; python3 -c "import time;time.sleep(70)"; done
  return 1
}
echo "##### $T $(date +%H:%M:%S)"
r python3 scripts/damodaran_stories.py $T || exit 1
r python3 scripts/build_story_sheet.py $T || exit 1
r python3 scripts/multiples_anchors.py --solo-justificado $A || exit 1
r python3 scripts/apply_multiples_v3.py --anclas $A --decision $D --apply || exit 1
r python3 scripts/damodaran_stories.py $T || exit 1
bash scripts/regenerar_cartera.sh $T 2>&1
echo "===== refresco de la sección con el precio guardado"
bash scripts/refrescar_seccion.sh $T 2>&1
echo "FIN $T $(date +%H:%M:%S)"
