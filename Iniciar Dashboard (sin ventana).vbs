' Version "silenciosa" del launcher: no muestra ninguna ventana de consola.
' Usar esta una vez que ya probaste "Iniciar Dashboard.bat" y confirmaste que funciona.
' Para cerrar el dashboard cuando lo abris asi: Administrador de tareas -> buscar "python" -> Finalizar tarea.

Dim objShell, scriptDir
Set objShell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
scriptDir = fso.GetParentFolderName(WScript.ScriptFullName)
objShell.CurrentDirectory = scriptDir
objShell.Run "cmd /c python -m streamlit run ""jmr_valuation\report\dashboard.py""", 0, False
