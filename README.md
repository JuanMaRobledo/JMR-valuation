# JMR-valuation
Valoración de empresas

## Screener de empresas maravillosas

`scripts/run_screener.py` recorre un universo de acciones (S&P 500 por
defecto) y las ordena por calidad de negocio y por precio vs su propia
historia. Es el primer filtro antes de aplicar el checklist de 8 pasos de
`Modelo-JMR/modelo/METODOLOGIA.md`.

```bash
pip install -r requirements.txt
# .env: SEC_EDGAR_USER_AGENT="JMR Valuation tu_email@ejemplo.com"
python scripts/run_screener.py                          # S&P 500
python scripts/run_screener.py --universe sp400         # mid caps (también sp600)
python scripts/run_screener.py --tickers AAPL MSFT V MA
python scripts/run_screener.py --json-out ../Modelo-JMR/docs/screener/resultados.json
```

Genera `data/screener/resultados.{json,csv}` y `resumen.md`. El JSON se ve
en la página **Screener** de Modelo-JMR (se puede publicar ahí o abrirlo con
"Abrir JSON local"). La primera corrida del S&P 500 baja ~1.000 archivos de
SEC EDGAR (unos minutos); durante 7 días se reusan desde
`data/screener_cache/`.

Cómo decide (`jmr_valuation/screener/`):

1. **Filtros duros** (`scoring.py`): ≥ 5 años de 10-K, ROIC mediano 5 años
   ≥ 12%, FCF positivo en ≥ 4 de los últimos 5 años, deuda neta/EBITDA ≤ 3x
   (el *red flag* del Paso 3) y ventas que no caen en 5 años. Bancos,
   aseguradoras y REITs (SIC 6000-6799) se excluyen: van por P/VL y ROE.
2. **Puntaje 0-100**: ROIC (nivel y mínimo 5a), margen bruto (nivel y
   estabilidad), margen operativo, margen FCF, años con FCF positivo,
   conversión FCF/utilidad, crecimiento de ventas y de FCF por acción,
   deuda, cobertura de intereses, recompras vs dilución y SBC. Cada métrica
   es una rampa lineal entre un umbral "malo" y uno "excelente" (todos en
   `CRITERIA`, para ajustarlos). Clases: Maravillosa ≥ 82, Muy buena ≥ 68,
   Aceptable ≥ 52.
3. **Alertas** que no descalifican pero hay que mirar: ROE inflado vs ROIC,
   patrimonio negativo, márgenes comprimiéndose, dilución, SBC alto,
   utilidades que no se convierten en caja.
4. **Precio vs historia** (`valuation.py`): P/FCF de hoy vs la mediana del
   P/FCF de cada cierre fiscal (~10 años); P/E de respaldo. "Barata" = 20%
   o más por debajo de su mediana.

Datos: SEC EDGAR (vía `sec_edgar_loader.load_annual_series_from_sec_edgar`)
y cierres semanales de Yahoo Finance. Se corrigen splits y acciones
taggeadas en miles, pero el XBRL tiene errores: todo lo que salga arriba se
verifica a mano antes de invertir.

## Auditoría de la plantilla del modelo (26-sep-2026)

Dos scripts dejan la plantilla maestra de Google Sheets y todas sus copias de valoración
corregidas y explicadas:

```bash
PYTHONPATH=.:scripts python scripts/audit_fix_model.py --sheet-id <ID> [--dry-run]
PYTHONPATH=.:scripts python scripts/model_presentation.py --sheet-id <ID>
```

- `audit_fix_model.py` corrige 9 errores estructurales (A1-A9: deuda neta en los múltiplos EV,
  dividendos, horizonte DCF vs múltiplos, CAGR, margen EBITDA, estadísticas de industria, múltiplo
  Base negativo, datos ajenos pegados y rótulos). Solo reescribe una celda si todavía tiene la
  fórmula original de la plantilla: los ajustes manuales de cada valoración se respetan y se
  listan como «personalizadas». La fórmula anterior queda en
  `reference/backups/auditoria_2026-09-26/<id>.json`, y el impacto en precios objetivo, en
  `reference/auditoria_2026-09-26_informe.json`.
- `model_presentation.py` agrega la hoja «Origen de los Supuestos» (de dónde sale cada supuesto
  de crecimiento, margen, costo de capital y múltiplo objetivo, con fórmulas vivas) y da un
  formato uniforme a las hojas de texto. El contenido previo de esas hojas queda en
  `reference/backups/auditoria_2026-09-26/<id>_textos.json`.

Detalle de las reglas y de cada corrección: `Modelo-JMR/modelo/METODOLOGIA.md`, anexo
«Modelo en Google Sheets».
- `discount_multiples.py` (29-sep-2026) reconstruye en la plantilla maestra y en cada valoración la
  hoja «Descuento de múltiplos»: cada múltiplo a valor presente en 1, 2 y 3 años,
  `(precio FY+n + dividendos acumulados) ÷ (1 + Ke)^n`, consolidado por método (promedio de los 3
  horizontes o solo 3 años) y ponderado con el DCF hoy; el Resumen (filas 30-47) muestra DCF,
  múltiplos consolidados y ponderado por separado. Respaldo en
  `reference/backups/descuento_multiples_2026-09-29/`, resultados y chequeo VP3 < FY+3 en
  `reference/descuento_multiples_2026-09-29_informe.json`. `--check-only` solo verifica.
  `patch_saved_present_value.py` lleva esos valores a las valoraciones guardadas del visor sin tocar
  el resto del registro, y `sync_research_present_value.py` rehace la tabla de valor presente y las
  cifras citadas en los análisis fundamentales guardados. El script detecta la estructura de cada hoja
  (nombres 'EVEBITDA' / 'EV/EBITDA' / 'EV∕EBITDA', filas, Ke, MOS, separador ',' o ';'), así que
  también cubre las versiones de julio-agosto (V3-V6, ONON, NFLX, Motor v2) y los respaldos;
  `reference/descuento_multiples_targets*.json` lista todas las hojas procesadas.
- `regen_saved_valuations.py` vuelve a generar una valoración guardada del visor web
  (`Modelo-JMR-datos/valoraciones/*.json`) desde la hoja corregida: carga el xlsx en
  `docs/visor.html` con Playwright e intercepta el guardado. Conserva el análisis fundamental
  y el Cualitativo que se hayan editado en el visor.

## Regenerar la cartera completa (3-oct-2026)

Cuando cambian las hojas (supuestos, fórmulas o datos), un solo comando rehace las valoraciones de la app, los informes,
la sección 12 del research de la app y las tablas de horizontes, y luego verifica todo:

```bash
scripts/regenerar_cartera.sh [--drive] [TICKER ...]   # sin tickers: las 22 de reference/cartera_drive.json
```

Requisitos: `Modelo-JMR` y `Modelo-JMR-datos` clonados junto a este repo, `GOOGLE_SERVICE_ACCOUNT_JSON_CONTENT`, Node,
Playwright con Chromium. El script descarga a `.cache/js/` las dos librerías que usa (SheetJS 0.18.5 y marked 12.0.2).

Por empresa: `regen_valoracion_app.py` (valoración de la app desde la hoja) → `implied_growth.py` →
`sync_saved_after_dcf.py` → `sync_valor_esperado.py` → `normalize_saved_mos.py` → `audit_report.py` →
`insert_damodaran_section.py` → `insert_scenarios_table.py` → `valuation_report_v3.py`. Para todas al final:
`insert_research_horizons_app.py`, `consistencia_app.py` (16 controles entre motor, valoración, research y auditoría) e
`integridad_hojas.py`. Con `--drive`, `subir_drive.py` reemplaza en Drive los archivos listados en
`reference/cartera_drive.json` y verifica el md5 de cada uno. Cada paso con llamadas a Google se reintenta (cuota de 60
lecturas por minuto); al final el script lista las empresas o pasos que fallaron.

Si cambian las historias (`reference/damodaran/<T>.json`), antes se corre
`PYTHONPATH=.:scripts python scripts/damodaran_stories.py <T>`, que recalcula las historias desde la hoja y reescribe
`data/<T>_Analisis_Damodaran_*.md`. Desde el 2-oct-2026 los bloques Base, Conservador, Optimista y Disrupción de
'Valuation output' calculan las cuatro historias, así que el DCF de la hoja (B35) es el DCF Base y ya no hay un caso
técnico aparte (salvo las financieras, como PAGS, que usan 'DCF FCFE financiero').

## Valoración desde cero de una empresa nueva (6-oct-2026)

Flujo usado con CELH, NKE, LULU, ONON y MCD, ahora en un solo script por fases (`scripts/desde_cero.sh`):

1. Copiar la plantilla maestra `Modelo_JMR_Plantilla_Maestra` (`19PRUFiYsNavUcN6WwHBVlp-VRMozp3rNSE2R1zt7N-g`) con el
   conector de Drive en la carpeta de la empresa (la cuenta de servicio no puede crear archivos). La «Plantilla maestra
   reutilizable (vigente)» de la carpeta NVIDIA es la hoja de NVDA: no usarla como plantilla.
2. `desde_cero.sh datos T SHEET_ID "PEERS" "Industria"`: importador de la SEC, `nueva_empresa.py` (anclas, pestaña de
   historias semilla y registro en la app), `auditar_estados_sec.py` + `aplicar_cambios_celdas.py` y el conversor de
   arrendamientos (`apply_lease_conversion.py`, con `--gasto=T:US$M` si el gasto no está etiquetado).
3. Juicio del analista en `scripts/run_<t>_cero.py` (datos con enlace + ajuste, costo de capital, supuestos Base,
   textos) y en la ficha de historias `scripts/<t>_cero_spec.py`.
4. `desde_cero.sh historias T "PEERS"`: historias, pestaña «Escenarios e historias», anclas, decisión de múltiplos,
   crecimiento implícito, fórmula única e integridad. `damodaran_stories.py` avisa si una historia libera capital por
   caída de ingresos o si el capital nuevo rinde más del doble del ROIC terminal.
5. Informes (valoración v4 de 14 secciones y research v5 de 18) y `desde_cero.sh app T research.md`
   (`research_md_a_app.py` + `regenerar_cartera.sh`); subida a Drive con `subir_drive.py`.

Correcciones del 6-oct-2026 a partir de MCD: el importador toma la D&A total cuando conviven etiquetas de distinto
alcance, lleva a unidades las acciones etiquetadas en millones, deja en «Leases» solo los arrendamientos financieros y no
suma la deuda corriente que ya está dentro del largo plazo; `implied_growth.py` calibra el DCF inverso con la trayectoria
real de los años 1-5 (`--sin-escribir` para medir sin tocar nada; efecto en la cartera en
`reference/revision_dcf_2026-10-06/implied_growth_calibracion.json`); el cliente de Sheets reintenta solo ante el 429.

### Screener europeo (selección propia)

`python scripts/refresh_europe_screener.py --json-out ../Modelo-JMR/docs/screener/resultados.json`

Agrega 60 cotizaciones locales de 11 países europeos al JSON existente, conservando
los campos y resultados estadounidenses. No replica un índice ni cubre toda Europa.
La selección versionada está en `jmr_valuation/screener/europe.py`. Roche usa ROP.SW
tras el cambio de certificado de marzo de 2026:
https://www.roche.com/investors/updates/inv-update-2026-03-16

La fuente europea es Yahoo Finance (timeseries anual y chart). Su historia parcial
normalmente cubre cuatro FY: no se asigna puntaje JMR, CAGR 5a ni medianas históricas.
ROIC y márgenes son del último FY; los múltiplos usan sus resultados anuales y una
capitalización aproximada con acciones al cierre FY. No son ratios LTM. Los importes
se mantienen en moneda local, se normaliza GBp/GBX a GBP y se omiten múltiplos cuando
las monedas no coinciden, hay clases/certificados pendientes de validar o un split
posterior al último FY. Los faltantes no se sustituyen por cero. Financieras excluidas.

El refresco falla sin escribir el JSON si más del 20% de los símbolos da error o
menos del 80% tiene precio. El workflow del sitio ejecuta esta ampliación después
del screener estadounidense y antes de publicar. Pruebas aisladas sin dependencias:
`python -m unittest discover -s tests -p test_europe_screener.py -v`.
