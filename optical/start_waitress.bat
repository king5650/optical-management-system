@echo off
REM =====================================
REM Start Django backend with Waitress
REM =====================================

REM Move to this file's directory (optical/)
cd /d "%~dp0"

REM Activate the CORRECT venv (relative path)
call ..\venv\Scripts\activate.bat

REM Environment variables (NO COMMENTS ON SAME LINE!)
set PYTHONUNBUFFERED=1
set DJANGO_SETTINGS_MODULE=optical.settings

REM Debug info (logged)
python --version
where python

REM Start server (blocking)
python waitress_server.py >> ..\logs\backend.log 2>&1

