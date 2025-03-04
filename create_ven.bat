@echo off

REM Setting the variables
title Virtual environment creation

REM Setting the virtual environmrnt
python -m venv env && call env\Scripts\activate && pip install -r requirements.txt && echo All good !!
pause
