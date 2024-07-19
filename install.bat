call python -m venv .venv
pause
call %cd%\.venv\Scripts\activate.bat
pause
call pip install -r requirements.txt
pause