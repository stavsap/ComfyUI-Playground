@echo off

git clone https://github.com/comfyanonymous/ComfyUI.git

cd ComfyUI
python -m venv venv
call venv\Scripts\activate.bat

python -m pip install --upgrade pip
python -m pip install huggingface_hub
python -m pip install -r requirements.txt
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121

cd custom_nodes

git clone https://github.com/ltdrdata/ComfyUI-Manager.git
git clone https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git

cd ../models/controlnet

curl -s https://raw.githubusercontent.com/stavsap/CompfyUI-Playground/main/download-controlnet-models.py | python

cd ../..

python main.py --windows-standalone-build --listen
