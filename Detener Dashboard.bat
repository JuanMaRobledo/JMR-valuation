@echo off
echo Buscando el proceso del dashboard para cerrarlo...
powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.CommandLine -like '*streamlit*dashboard.py*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force; Write-Host ('Cerrado (PID ' + $_.ProcessId + ')') }"
echo Listo. Si no vio ningun mensaje de "Cerrado", es que ya estaba cerrado.
pause
