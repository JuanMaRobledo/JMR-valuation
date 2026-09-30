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
