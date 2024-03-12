@echo off

cd ComfyUI
python -m venv venv
python main.py --windows-standalone-build --listen
