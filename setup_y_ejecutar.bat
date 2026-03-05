@echo off
echo ==========================================
echo  Setup automatico para el proyecto NLP
echo ==========================================

echo.
echo Comprobando Python 3.11...

py -3.11 --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python 3.11 no encontrado. Descargando...

    powershell -Command "Invoke-WebRequest https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe -OutFile python_installer.exe"

    echo Instalando Python 3.11...
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1

    echo Instalacion completada.
) ELSE (
    echo Python 3.11 ya esta instalado.
)

echo.
echo Creando entorno virtual...

py -3.11 -m venv venv

echo.
echo Activando entorno virtual...

call venv\Scripts\activate

echo.
echo Instalando dependencias...

pip install --upgrade pip
pip install -r requirements.txt

echo.
echo ==========================================
echo  Ejecutando la aplicacion
echo ==========================================

python app.py

pause