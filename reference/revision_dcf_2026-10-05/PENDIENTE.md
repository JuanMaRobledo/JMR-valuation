# Revisión Damodaran de la cartera (5-oct-2026): estado

Rama de trabajo: `ccr-45889b63-8puxn5` en `JuanMaRobledo/JMR-valuation` y `JuanMaRobledo/Modelo-JMR-datos`.

## Criterio aplicado
- Beta: bottom-up del sector, sin primas por riesgos diversificables (concepto único, distribuidor, tamaño, moda: van en las
  historias). Tabla de EE.UU. si la mayoría de las ventas está en Norteamérica; global si no. Regresión solo como referencia,
  salvo que el sector no describa el negocio (UBER: 1,20 por regresión).
- Ventas/capital: dentro del rango de la empresa hoy, el marginal y el sector; el rendimiento del capital nuevo (margen
  objetivo × (1 − t) × ventas/capital) debe ser creíble. Se quitó el tope de la auditoría del 4-oct (ROIC actual con
  crédito mercantil). Capital sin impuestos diferidos ni inversiones financieras (`AJUSTES` en `scripts/tabla_ventas_capital.py`).
- Precio y fecha de corte fijos: cierre del 30-sep-2026 (`scripts/fijar_precio_corte.py`), ya aplicado en las 18 hojas
  que leían el precio en vivo. CELH, LULU, NKE y ONON ya tenían precio fijo.

## Cambios ya hechos en las hojas (respaldo en esta carpeta)
UBER (beta 1,20; ventas/capital 2,2/2,0; NOL 14.024), PAGS (beta 0,82), AFYA (1,5/1,2), INTU (1,54), BSX (1,26/1,17),
EPAM (3,27/2,83), PYPL (2,48), GOOG (años 6-10 1,43), MSFT (tabla EE.UU.; años 6-10 0,94), NVO (tabla EE.UU.; años 6-10 1,10),
ZTS (1,11). Notas y textos al día (`scripts/revisar_beta_s2c.py`, `scripts/textos_tasa_s2c.py`). Sin cambios de supuestos:
NVDA, PLTR, DUOL.

## Estado: terminada (5-oct-2026)
Las 22 empresas regeneradas: consistencia 16/16, integridad 0 hallazgos, fórmula única 0 celdas pendientes; nota de
actualización en el research; informes subidos a Drive (52/52). Para regenerar una empresa: `bash scripts/regenerar_una.sh <T>`.

Requisitos: `GOOGLE_SERVICE_ACCOUNT_JSON_CONTENT`, `SEC_EDGAR_USER_AGENT`, Chromium (Playwright) y los repos hermanos
`Modelo-JMR` y `Modelo-JMR-datos` junto a `JMR-valuation`.
