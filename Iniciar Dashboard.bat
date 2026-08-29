@echo off
cd /d "%~dp0"
echo ============================================
echo   Modelo JMR -- Vitrina de valoracion
echo ============================================
echo Iniciando el dashboard... se va a abrir solo en tu navegador.
echo NO cierres esta ventana mientras uses el dashboard (la podes minimizar).
echo Para cerrar el dashboard, cerra esta ventana o apreta Ctrl+C.
echo.
python -m streamlit run "jmr_valuation\report\dashboard.py"
pause
