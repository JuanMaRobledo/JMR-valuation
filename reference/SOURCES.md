# Procedencia de los datos de referencia

| Archivo | Procedencia | Fecha verificable | Uso |
| --- | --- | --- | --- |
| `mature_market_erp.txt` | [ERPSept26.xlsx de Damodaran](https://pages.stern.nyu.edu/~adamodar/pc/implprem/ERPSept26.xlsx), hoja `Impl premium calculator`, celda C45 | Inicio de septiembre de 2026: 4,093700355 % sobre Treasury 10 años (C45); C44 = 4,313700355 % sobre tasa libre de riesgo ajustada por default | CAPM automático con Treasury sin ajuste; revisar mensualmente |
| `industry_averages_us.csv`, `industry_averages_global.csv` | Extraídos del Excel original del modelo; tablas de industria Damodaran | **No registrada en estos CSV** | Crecimiento y márgenes de industria, ventas/capital; verificar contra la publicación antes de asumir vigencia |
| `country_risk_premiums.csv` | Extraído del Excel original; columna `total_erp` conserva fórmulas Excel | **No registrada; archivo inutilizable en su estado actual** | Fallar explícitamente hasta volver a exportar valores numéricos y registrar fecha |

No combinar primas de distinta fecha sin registrar el corte usado. Esta cifra se usa con la tasa Treasury de mercado en USD sin sustraer el spread soberano estadounidense. El nombre interno `mature_market_erp` es histórico: C45 mide la ERP implícita estadounidense **sobre Treasury**; C44 corresponde a la tasa libre de riesgo ajustada por default. No combinar C44 con Treasury sin ajuste ni C45 con tasa ajustada.
