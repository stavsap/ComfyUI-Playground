@echo off

cd ComfyUI
call venv\Scripts\activate.bat
python main.py --windows-standalone-build --listen
