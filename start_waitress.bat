@echo off
REM STCH LIS - Waitress service launcher (supervised).
REM
REM Why this is a loop and not a single run:
REM  * Task Scheduler's "restart on failure" does NOT fire when a process is
REM    killed externally (crash / OOM / manual kill) - the task is recorded as
REM    "terminated" (0xFFFFFFFF) and nothing brings the server back up.
REM  * The old ExecutionTimeLimit of PT72H also let Windows kill the task after
REM    3 days with no restart. Both are now fixed in the task settings, but the
REM    loop is what actually guarantees recovery from an unexpected exit.
REM
REM Port 8000 is freed before each start: a zombie waitress from a previous
REM session would otherwise make the new process die instantly with
REM "address already in use" while the window gave no visible clue.
REM All output is teed to logs\startup.log so failures are diagnosable.

cd /d "%~dp0"
set DJANGO_SETTINGS_MODULE=pcs_project.settings
set DJANGO_DEBUG=False
set DATA_UPLOAD_MAX_NUMBER_FILES=10000

if not exist "%~dp0logs" mkdir "%~dp0logs"
set LOG=%~dp0logs\startup.log

REM If a healthy waitress already owns port 8000, do not start a second
REM supervisor (this is what happens if someone double-clicks this file while
REM the scheduled task is already running) - report and exit cleanly.
netstat -ano | findstr ":8000" | findstr "LISTENING" >nul
if not errorlevel 1 (
    echo [%date% %time%] port 8000 already in use - waitress already running; exiting.>> "%LOG%"
    exit /b 0
)

:run
echo [%date% %time%] === waitress service starting ===>> "%LOG%"

REM Free port 8000 if anything is still bound to it.
for /f "tokens=5" %%P in ('netstat -ano ^| findstr ":8000" ^| findstr "LISTENING"') do (
    echo [%date% %time%] port 8000 held by PID %%P - stopping it>> "%LOG%"
    taskkill /F /PID %%P >> "%LOG%" 2>&1
    timeout /t 2 /nobreak >nul
)

REM Interpreter: set PYTHON before running this file to override; otherwise a
REM local virtualenv is used when present, falling back to python on PATH.
if not defined PYTHON (
    if exist "%~dp0.venv\Scripts\python.exe" (
        set PYTHON=%~dp0.venv\Scripts\python.exe
    ) else if exist "%~dp0venv\Scripts\python.exe" (
        set PYTHON=%~dp0venv\Scripts\python.exe
    ) else (
        set PYTHON=python
    )
)

"%PYTHON%" run_waitress.py >> "%LOG%" 2>&1

echo [%date% %time%] === waitress exited with code %errorlevel% - restarting in 10s ===>> "%LOG%"
timeout /t 10 /nobreak >nul
goto run