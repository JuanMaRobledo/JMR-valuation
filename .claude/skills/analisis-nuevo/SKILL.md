---
name: analisis-nuevo
description: Hace una valoración nueva del Modelo JMR (criterio Damodaran) de una empresa, o la rehace desde cero, con los datos más recientes: último 10-Q/10-K y todos los 8-K/6-K, corte de mercado vigente (precio, Treasury y prima de Damodaran de la misma fecha), plantilla maestra, cuatro historias, múltiplos con tres anclas, research, valoración, app, Drive y posición de la cartera. Úsala cuando el usuario pida "analiza X", "valora X", "haz el análisis de X" o "rehaz X desde cero".
---

# Análisis nuevo (Modelo JMR, criterio Damodaran)

Prompts que mandan: `Modelo-JMR/docs/prompts/valoracion-modelo-jmr-v4.md` (pasos 1-11) y
`research-fundamental-jmr-v5.md`. Léelos completos antes de empezar. Este archivo dice de dónde salen los datos más
recientes y qué scripts usar; el contenido y los criterios están en los prompts. Ejemplo completo y probado:
`scripts/run_celh_cero.py` (+ `celh_cero_spec.py`, `celh_cero_content.py`).

## 1. Datos más recientes (antes de abrir la hoja)
1. Corte de mercado: `python3 scripts/datos_mercado.py`. Si el corte que devuelve es más nuevo que
   `reference/corte_vigente.json`, pregunta al usuario si quiere actualizar la cartera (habilidad actualizar-cartera,
   modo B) para que el análisis nuevo sea comparable con el resto; si no, usa el corte vigente. Precio de la empresa:
   cierre del día del corte (Yahoo Finance, `auto_adjust=False`).
2. SEC: `python3 scripts/novedades_sec.py --desde <hace 15 meses> <T>`. Último 10-K y 10-Q (o 20-F/6-K), y lee TODOS
   los 8-K/6-K hasta hoy: los posteriores al corte se mencionan como hechos posteriores y, si son materiales, entran en
   las historias.
3. Noticias, guía y consenso (WebSearch), peers con sus múltiplos (yfinance) y datos de Damodaran del sector (betas,
   márgenes, ROIC, ventas/capital: la tabla de EE.UU. si la mayoría de las ventas está en Norteamérica, global si no).

## 2. Hoja desde la plantilla maestra
1. `python3 scripts/reset_from_master.py --new "Modelo JMR - <T>"`. Si la cuenta de servicio no puede crear archivos, pide
   al usuario «Archivo > Hacer una copia» de la plantilla maestra (19PRUFiYsNavUcN6WwHBVlp-VRMozp3rNSE2R1zt7N-g), que la
   comparta como editor con jmr-valuation-bot@jmr-valuation-508617.iam.gserviceaccount.com, y corre
   `reset_from_master.py --sheet-id <id>`.
2. Estados de la SEC: `python3 scripts/refresh_native_model.py <T> --sheet-id <id> --industry-us ... --industry-global ...
   --peers ...`, luego `python3 scripts/auditar_estados_sec.py <T>` y las correcciones con nota (splits, balance LTM al
   último 10-Q, partidas de una vez, preferentes, arrendamientos).
3. Corte: agrega la empresa a `reference/corte_vigente.json` (cierre) y corre `python3 scripts/aplicar_corte.py --apply <T>`
   (D1, B4, B23 = D1, tasa, prima, terminal). Registra la empresa en `reference/cartera_drive.json` y
   `reference/multiplos_v3/<T>_anclas.json` (sheet_id, peers).

## 3. Valoración (prompt v4)
- Costo de capital: beta bottom-up del sector sin primas por riesgos diversificables; Kd real; prima por regiones.
- Historia y visión externa (paso 3B) antes de mirar el precio; cuatro historias en `reference/damodaran/<T>.json`
  (crecimiento por segmento, margen, ventas/capital dentro del rango empresa / marginal / sector con capital de trabajo y
  sin impuestos diferidos de una liberación de reserva, ROIC terminal con la regla de `reference/moat_2026-09-30.json`).
- Tipo de empresa por ciclo de vida y sector: `reference/ciclo_de_vida/` y `scripts/ciclo_de_vida.py` (agrega la empresa a C).
- `bash scripts/regenerar_una.sh <T>`: historias → hoja → múltiplos (tres anclas) → app → sección Damodaran.
- Posición: si el usuario la tiene en cartera, habilidad actualizar-cartera, modo A.

## 4. Documentos, controles y entrega
- Research v5 y valoración v4 en `data/<T>_*_<fecha>.md` (las cifras salen de la hoja: `scripts/valores_hoja.py`),
  insertados en la app (`insert_damodaran_section.py`, `insert_scenarios_table.py`, `insert_research_horizons_app.py`).
- Controles: `consistencia_app.py <T>` 16/16, `integridad_hojas.py <T>` 0 hallazgos, `apply_canonical_formulas.py` en seco
  0 celdas, motor = hoja.
- `python3 scripts/subir_drive.py`, commit/PR/fusión en JMR-valuation y Modelo-JMR-datos, y la página de lectura
  (`scripts/pagina_cartera.py`).
- Informe al usuario: DCF Base (valor intrínseco), esperado, rango, precio con MOS, qué espera el precio (DCF inverso),
  juicios tomados y fuentes con fecha.
