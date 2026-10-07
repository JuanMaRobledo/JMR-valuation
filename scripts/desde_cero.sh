#!/bin/bash
# Valoración DESDE CERO de una empresa nueva con el Modelo JMR (prompt de valoración v4 + research v5), 6-oct-2026.
# Ordena los pasos automáticos que se usaron con CELH, NKE, LULU, ONON y MCD. Lo que exige juicio del analista va en un
# script propio de la empresa (scripts/run_<t>_cero.py: datos, costo, supuestos, presentacion, content) y en su ficha
# de historias (scripts/<t>_cero_spec.py -> reference/damodaran/<T>.json); este script se detiene en esos puntos.
#
#   scripts/desde_cero.sh datos     TICKER SHEET_ID "PEER1 PEER2 ..." "Industria Damodaran"
#   scripts/desde_cero.sh historias TICKER "PEER1 PEER2 ..."
#   scripts/desde_cero.sh app       TICKER data/<T>_Research_Fundamental_Modelo_JMR_<fecha>.md
#
# Antes de «datos»: copiar la plantilla maestra (Modelo_JMR_Plantilla_Maestra, 19PRUFiYsNavUcN6WwHBVlp-VRMozp3rNSE2R1zt7N-g)
# con el conector de Drive en la carpeta de la empresa (la cuenta de servicio no puede crear archivos). No usar la
# «Plantilla maestra reutilizable (vigente)» de la carpeta NVIDIA: es la hoja de NVDA. Nunca sobrescribir la hoja de
# otra empresa ni una copia anterior de la misma empresa: queda como referencia.
set -u -o pipefail
cd "$(dirname "$0")/.."
export PYTHONPATH=.:scripts SEC_EDGAR_USER_AGENT="${SEC_EDGAR_USER_AGENT:-JMR Valuation juan0804@gmail.com}"
FASE=$1; T=$(echo "$2" | tr a-z A-Z)

case "$FASE" in
datos)
  SID=$3; PEERS=$4; IND=$5
  echo "== 1. Estados de la SEC (importador corregido: D&A total, acciones en millones, arrendamientos financieros, deuda corriente)"
  python3 - "$T" "$SID" "$PEERS" "$IND" <<'EOF' || exit 1
import sys, refresh_native_model as rnm, model_steps as ms
t, sid, peers, ind = sys.argv[1], sys.argv[2], sys.argv[3].split(), sys.argv[4]
ms.install_augmented_client(t)
rnm.run(t, sheet_id=sid, peer_tickers=peers, industry_us=ind, industry_global=ind)
EOF
  echo "== 2. Arranque de empresa nueva (anclas, pestaña de historias semilla, registro en la app)"
  python3 scripts/nueva_empresa.py "$T" "$SID" || exit 1
  echo "== 3. Auditoría de estados contra la SEC (BPA básico, cambio de caja, balance LTM, D&A, SG&A en 0)"
  python3 scripts/auditar_estados_sec.py "$T" || exit 1
  python3 scripts/aplicar_cambios_celdas.py "$T" "reference/auditoria_estados_2026-10-03/${T}_cambios.json" --apply || exit 1
  echo "== 4. Arrendamientos operativos con el conversor (solo US GAAP; si falta el gasto: --gasto=${T}:<US\$M>)"
  python3 scripts/apply_lease_conversion.py --dry-run "$T"
  cat <<EOF

PAUSA (juicio del analista), en este orden:
  - revisar lo que la auditoría solo «informa» y corregir a mano con nota y respaldo (scripts/run_${T,,}_cero.py, paso fix):
    reexpresiones, partidas no etiquetadas, balance del último 10-Q, deuda corriente, arrendamientos por año;
  - apply_lease_conversion.py sin --dry-run (US GAAP) o B18 = No (NIIF 16);
  - datos de la Input sheet como enlace + ajuste con nota (B13, B15, B16, B22, B24, opciones, B76), D1 y B4 al corte,
    'Resumen de Valoración'!C25 al mismo precio, prima madura 'Country equity risk premiums'!B2 = la vigente;
  - costo de capital: beta bottom-up (tabla global si >50% de ventas fuera de EE.UU.), prima por regiones, Kd real;
  - ficha de historias (scripts/${T,,}_cero_spec.py) y supuestos Base en la Input sheet = historia Base.
Luego: scripts/desde_cero.sh historias $T "$PEERS"
EOF
  ;;
historias)
  PEERS=$3
  A=reference/multiplos_v3/${T}_anclas.json; D=reference/multiplos_v3/${T}_decision.json
  SID=$(python3 -c "import json;print(json.load(open('$A'))['sheet_id'])")
  echo "== 5. Historias con el motor y pestaña «Escenarios e historias» por fórmulas"
  python3 scripts/damodaran_stories.py "$T" || exit 1
  python3 scripts/build_story_sheet.py "$T" || exit 1
  python3 scripts/link_vo_to_stories.py --sheet-id "$SID" --check | tail -3
  echo "== 6. Anclas de los múltiplos (historia, peers, justificado)"
  python3 scripts/multiples_anchors.py --sheet-id "$SID" --peers $PEERS --out "$A" || exit 1
  if [ ! -s "$D" ]; then
    echo "PAUSA: escribir $D (etapa, peers excluidos, ajuste, λ, no aplica, evaluación) y volver a correr esta fase."; exit 0
  fi
  python3 scripts/apply_multiples_v3.py --anclas "$A" --decision "$D" --apply || exit 1
  echo "== 7. Crecimiento implícito y recálculo de las historias"
  python3 scripts/implied_growth.py "$T" || exit 1
  python3 scripts/damodaran_stories.py "$T" || exit 1
  echo "== 7b. Múltiplos históricos normalizados (lectura independiente; no afecta DCF ni ponderado)"
  python3 scripts/historical_multiples.py "$T" --sheet-id "$SID" --write-sheet || exit 1
  echo "== 8. Controles: fórmula única (0 pendientes) e integridad"
  echo "[[\"$T\",\"$SID\"]]" > /tmp/${T}_targets.json
  python3 scripts/apply_canonical_formulas.py --targets /tmp/${T}_targets.json
  python3 scripts/integridad_hojas.py "$T"
  cat <<EOF

PAUSA: textos de la hoja (paso content del script de la empresa) y apply_multiples_v3.py --apply otra vez (agrega el
origen de los múltiplos a la Tesis); redactar data/${T}_Valoracion_Modelo_JMR_<fecha>.md (14 secciones, prompt v4) y
data/${T}_Research_Fundamental_Modelo_JMR_<fecha>.md (18 secciones, research v5; la sección 12 sale de
data/${T}_Analisis_Damodaran_*.md). Luego: scripts/desde_cero.sh app $T <research.md>
EOF
  ;;
app)
  MD=$3
  echo "== 9. Valoración y research en la app; secciones, horizontes y consistencia"
  mkdir -p .cache/js
  [ -s .cache/js/marked.min.js ] || curl -fsS -o .cache/js/marked.min.js https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js
  bash scripts/regenerar_cartera.sh "$T" | tail -4
  MARKED_PATH=$PWD/.cache/js/marked.min.js python3 scripts/research_md_a_app.py "$T" "$MD" || exit 1
  bash scripts/regenerar_cartera.sh "$T" | tail -8
  cat <<EOF

Último paso: crear los .md vacíos en Drive (AAA Finanzas › Análisis › <empresa>) con el conector de Drive, anotar sus
ids en reference/cartera_drive.json y correr: python3 scripts/subir_drive.py $T (verifica el md5).
EOF
  ;;
*)
  sed -n 2,16p "$0"; exit 1 ;;
esac
