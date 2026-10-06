---
name: actualizar-cartera
description: Actualiza las valoraciones de la cartera del Modelo JMR con los datos más recientes cuando el usuario lo pide ("actualiza", "pon al día", "compré", "vendí", "salieron resultados de X", "nuevo corte"). Cubre precios, tasa libre, prima de Damodaran, posiciones de la cartera, resultados y 8-K nuevos, regeneración de la app, Drive, controles y PR.
---

# Actualizar la cartera (Modelo JMR, criterio Damodaran)

Repositorios (rama de la sesión en los tres): JMR-valuation (scripts, hojas, documentos), Modelo-JMR-datos (lo que lee la
app) y Modelo-JMR (app y prompts). Variables: `export PYTHONPATH=.:scripts SEC_EDGAR_USER_AGENT="JMR Valuation juan0804@gmail.com"`.
Las hojas son la fuente: toda cifra de un texto sale de la hoja (`scripts/valores_hoja.py`). Criterios vigentes: prompts
`Modelo-JMR/docs/prompts/valoracion-modelo-jmr-v4.md` y `research-fundamental-jmr-v5.md`, `reference/criterios_damodaran_2026-10-04.md`,
`reference/moat_2026-09-30.json` (regla de ROIC terminal) y `reference/ciclo_de_vida/` (tipo de empresa).

Primero pregunta solo lo indispensable y elige el modo según lo que pidió el usuario. Si pide "actualiza todo", corre
A, B y C en ese orden.

## A. Posiciones (compras y ventas)
1. Descarga la hoja «Seguimiento de cartera» (Drive, id `1P3yzgr-RXJU6fFGuVPw0_JLQMwh_khGWuAZsZmft7kM`) como .xlsx con el
   conector de Google Drive (`download_file_content`, exportMimeType xlsx) y guárdala en el scratchpad. Si la cuenta de
   servicio ya tiene acceso de lector, omite la descarga.
2. `python3 scripts/posiciones_cartera.py --xlsx <archivo>` → `reference/cartera_compras_<hoy>.json`. Revisa la lista
   (empresas sin posición, cantidades).
3. `python3 scripts/posicion_cartera.py --apply <tickers>` (bloque «Mi posición», 'Resumen de Valoración'!A50:E60).
4. `bash scripts/regenerar_cartera.sh <tickers>` (la app guarda el campo `posicion`).
Si el usuario compró una empresa que no está en las 22, avísale y ofrece un análisis nuevo (habilidad analisis-nuevo).

## B. Corte nuevo (datos de mercado)
Regla Damodaran: tasa libre y prima de la MISMA fecha. Damodaran publica cada mes la prima calculada con el Treasury y los
precios del último día hábil del mes anterior; ese día es el corte.
1. `python3 scripts/datos_mercado.py` y revisa los avisos (FRED ≠ tasa del archivo de Damodaran, cierres faltantes).
   Si todo cuadra: `python3 scripts/datos_mercado.py --escribir` → `reference/corte_vigente.json`.
2. `python3 scripts/aplicar_corte.py` (en seco) y luego `--apply`: precio, fecha, B23 = D1, tasa, prima, Brasil y ROIC
   terminal de punto medio. Se corre una empresa a la vez con reintentos si Google responde 429.
3. `python3 scripts/textos_tasa_s2c.py --apply <22 tickers>` (textos de tasa de las hojas).
4. Por empresa: `bash scripts/regenerar_una.sh <T>` (historias → hoja → múltiplos → app → sección). Revisa cada línea
   "FIN: sin fallas 16/16 0 hallazgos". Corre en segundo plano y en orden (la cuota es 60 lecturas por minuto).
5. `python3 scripts/auditoria_research_al_dia.py --apply` y `python3 scripts/nota_revision_research.py` (tablas y nota
   de actualización del research de la app).
6. Controles: `python3 scripts/apply_canonical_formulas.py --targets <json con [ticker, sheet_id]>` en seco (0 celdas),
   hoja = app = resultado (valores_hoja frente a valoraciones/<T>-*.json y reference/damodaran/<T>_resultado.json).
7. Tabla antes/después de DCF Base y esperado frente a origin/main; `python3 scripts/subir_drive.py`.

## C. Resultados y hechos nuevos (por empresa)
1. `python3 scripts/novedades_sec.py --desde <fecha del último análisis>`: 10-Q/10-K/20-F nuevos y TODOS los 8-K/6-K.
   Lee cada 8-K/6-K material (2.02 resultados y guía, 1.05 ciberataque, 2.05 reestructuración, 1.01/2.01 compras).
2. Con 10-Q/10-K nuevo: actualiza los estados. `refresh_native_model.py <T> --sheet-id <id> --industry-us/--industry-global
   <industria de reference/damodaran/<T>.json> --peers <de reference/multiplos_v3/<T>_anclas.json>` repuebla Income
   Statement, Balance y Cash Flow: ANTES respalda la hoja y anota los ajustes documentados en las notas de la Input sheet
   (EBIT normalizado, preferentes, arrendamientos, balance LTM), y DESPUÉS vuelve a aplicarlos y corre
   `scripts/auditar_estados_sec.py <T>` (+ `aplicar_cambios_celdas.py`) hasta cuadrar con la SEC.
3. Ajusta la historia en `reference/damodaran/<T>.json` con la evidencia nueva (año 1 con la guía; probabilidades 5-10 pp
   por trimestre según los indicadores). Es juicio: muéstrale al usuario el cambio y su efecto antes de cerrarlo cuando
   mueva el DCF Base más de 5%.
4. `bash scripts/regenerar_una.sh <T>`.

## Cierre (siempre)
- Página de lectura: `python3 scripts/pagina_cartera.py` (antes de fusionar, para que «DCF Base anterior» sea el de
  origin/main) y publícala con la herramienta Artifact en la URL de «Cartera Modelo JMR»
  (https://claude.ai/artifact/FNfmJ4i6tozPLEo9r7qshN; si la sesión no la publicó, léela primero con action "read").
- Commit en las ramas de la sesión de JMR-valuation y Modelo-JMR-datos (y Modelo-JMR si cambió la app o un prompt), PR y
  fusión. Mensajes y PR en español, con la atribución de la sesión.
- Informe al usuario: qué cambió (tabla antes/después), avisos de datos, juicios que tomaste y controles.

## Errores conocidos
- 429 de Google: reintenta tras 70 s; nunca lances dos regeneraciones a la vez.
- Precios con GOOGLEFINANCE en vivo cambian el DCF: D1 y B23 deben ser números fijos del corte.
- Impuestos diferidos de una liberación de reserva inflan el capital invertido: AJUSTES en `scripts/tabla_ventas_capital.py`.
- Si cambia la prima, se recalculan el costo terminal y los ROIC de punto medio (aplicar_corte.py lo hace).
