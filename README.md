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
