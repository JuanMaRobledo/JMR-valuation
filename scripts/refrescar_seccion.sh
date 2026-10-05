#!/bin/bash
# refresh_sec.sh T...: rehace la sección Damodaran (sin tocar la hoja) e inserta en la app; consistencia
cd "$(dirname "$0")/.."
export PYTHONPATH=.:scripts MARKED_PATH=$PWD/.cache/js/marked.min.js SEC_EDGAR_USER_AGENT="JMR Valuation juan0804@gmail.com"
for T in "$@"; do
  echo "== $T"
  python3 scripts/damodaran_stories.py $T 2>&1 | tail -1
  for s in insert_damodaran_section insert_scenarios_table; do python3 scripts/$s.py ../Modelo-JMR-datos $T | tail -1; done
  python3 scripts/consistencia_app.py $T | tail -1
done
