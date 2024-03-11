git clone https://github.com/comfyanonymous/ComfyUI.git
cd CompfyUI
python -m venv venv
venv\Scripts\activate.bat
python -m pip install -r requirements.txt
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121
python main.py --windows-standalone-build --listen
