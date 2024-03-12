@echo off
curl -o run.bat https://raw.githubusercontent.com/stavsap/CompfyUI-Playground/main/run.bat
git clone https://github.com/comfyanonymous/ComfyUI.git

cd ComfyUI
python -m venv venv
call venv\Scripts\activate.bat

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121
python -m pip install huggingface_hub
python -m pip install opencv-python
python -m pip install insightface
python -m pip install onnxruntime
python -m pip install onnxruntime-gpu

cd custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager.git
git clone https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git
git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus.git
git clone https://github.com/cubiq/ComfyUI_InstantID.git
git clone https://github.com/Gourieff/comfyui-reactor-node.git
cd comfyui-reactor-node
python install.py
cd ..
cd ..

curl -s https://raw.githubusercontent.com/stavsap/CompfyUI-Playground/main/download-models.py | python

cd models\insightface\models
tar -xf antelopev2.zip
del antelopev2.zip
cd ../../..

python main.py --windows-standalone-build --listen
