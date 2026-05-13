@echo off
SET CURRENT_DIR=%~dp0
SET PYTHON_EXE=%CURRENT_DIR%entornoPySide01\Scripts\pythonw.exe
SET SCRIPT_PATH=%CURRENT_DIR%main_ServidorTCP_IP.pyw

if exist "%PYTHON_EXE%" (
    start "" "%PYTHON_EXE%" "%SCRIPT_PATH%"
) else (
    echo Error: No se encontro el entorno virtual en %PYTHON_EXE%
    pause
)