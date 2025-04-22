@echo off
cd %~dp0
if exist .venv (
	call .venv\Scripts\activate.bat
	start http://127.0.0.1:8000
	python manage.py runserver
	cmd /k
) else (
	py -3.12 -m venv .venv
	call .venv\Scripts\activate.bat
	pip install -r requirements.txt
	start http://127.0.0.1:8000
	python manage.py runserver
	cmd /k
)
