# arrancar entorno virtual
python -m venv .venv


# activar entorno (powershell)
.\.venv\Scripts\Activate.ps1

# o esto que me aparecio solo (en la terminal)
d:\0_python\ej_python_inf_av\.venv\Scripts\activate

# permitir comandos en sesion - luego ejecutar la activacion del env
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# instalacion pyside6 (dentro del env)
pip install pyside6

# abrir el diseñador (dentro del env)
pyside6-designer

# .ui to .py
pyside6-uic intro_gui.ui -o intro_gui.py
