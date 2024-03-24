@echo off

curl -o run.bat https://raw.githubusercontent.com/stavsap/ComfyUI-Playground/main/run.bat
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
python -m pip install simpleeval

cd custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager.git
git clone https://github.com/pythongosssss/ComfyUI-Custom-Scripts.git
git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus.git
git clone https://github.com/cubiq/ComfyUI_InstantID.git
git clone https://github.com/cubiq/ComfyUI_essentials.git
git clone https://github.com/Ttl/ComfyUi_NNLatentUpscale.git
git clone https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git
git clone https://github.com/rgthree/rgthree-comfy.git
git clone https://github.com/LEv145/images-grid-comfy-plugin.git

git clone https://github.com/jags111/efficiency-nodes-comfyui.git
cd efficiency-nodes-comfyui
python -m pip install -r requirements.txt
cd ..

git clone https://github.com/giriss/comfy-image-saver.git
cd comfy-image-saver
python -m pip install -r requirements.txt
cd ..

git clone https://github.com/kijai/ComfyUI-SUPIR.git
cd ComfyUI-SUPIR
python -m pip install -r requirements.txt
cd ..

git clone https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git
cd ComfyUI-Advanced-ControlNet
python -m pip install -r requirements.txt
cd ..

git clone https://github.com/Gourieff/comfyui-reactor-node.git
cd comfyui-reactor-node
python install.py
cd ..

git clone https://github.com/stavsap/comfyui-ollama.git
cd comfyui-ollama
python -m pip install -r requirements.txt
cd ../..

curl -s https://raw.githubusercontent.com/stavsap/ComfyUI-Playground/main/download-models.py | python

cd models\insightface\models
tar -xf antelopev2.zip
del antelopev2.zip
cd ../../..

curl -s https://raw.githubusercontent.com/stavsap/ComfyUI-Playground/main/download-checkpoints.py | python

python main.py --windows-standalone-build --listen
