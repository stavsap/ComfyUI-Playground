curl -o run.sh https://raw.githubusercontent.com/stavsap/ComfyUI-Playground/main/run.sh
chmod +x run.sh
git clone https://github.com/comfyanonymous/ComfyUI.git

cd ComfyUI
python3 -m venv venv
source venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121

python -m pip install huggingface_hub opencv-python insightface onnxruntime onnxruntime-gpu simpleeval

git clone https://github.com/ltdrdata/ComfyUI-Manager.git custom_nodes/ComfyUI-Manager
git clone https://github.com/pythongosssss/ComfyUI-Custom-Scripts.git custom_nodes/ComfyUI-Custom-Scripts
git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus.git custom_nodes/ComfyUI_IPAdapter_plus
git clone https://github.com/cubiq/ComfyUI_InstantID.git custom_nodes/ComfyUI_InstantID
git clone https://github.com/cubiq/ComfyUI_essentials.git custom_nodes/ComfyUI_essentials
git clone https://github.com/Ttl/ComfyUi_NNLatentUpscale.git custom_nodes/ComfyUi_NNLatentUpscale
git clone https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git custom_nodes/ComfyUI-AnimateDiff-Evolved
git clone https://github.com/rgthree/rgthree-comfy.git custom_nodes/rgthree-comfy
git clone https://github.com/LEv145/images-grid-comfy-plugin.git custom_nodes/images-grid-comfy-plugin

git clone https://github.com/jags111/efficiency-nodes-comfyui.git custom_nodes/efficiency-nodes-comfyui
python -m pip install -r custom_nodes/efficiency-nodes-comfyui/requirements.txt

git clone https://github.com/giriss/comfy-image-saver.git custom_nodes/comfy-image-saver
python -m pip install -r custom_nodes/comfy-image-saver/requirements.txt

git clone https://github.com/kijai/ComfyUI-SUPIR.git custom_nodes/ComfyUI-SUPIR
python -m pip install -r custom_nodes/ComfyUI-SUPIR/requirements.txt

git clone https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git custom_nodes/ComfyUI-Advanced-ControlNet
python -m pip install -r custom_nodes/ComfyUI-Advanced-ControlNet/requirements.txt

git clone https://github.com/Gourieff/comfyui-reactor-node.git custom_nodes/comfyui-reactor-node
cd custom_nodes/comfyui-reactor-node
python install.py
cd ../..

git clone https://github.com/stavsap/comfyui-ollama.git custom_nodes/comfyui-ollama
python -m pip install -r custom_nodes/comfyui-ollama/requirements.txt

curl -s https://raw.githubusercontent.com/stavsap/ComfyUI-Playground/main/download-models.py | python

cd models/insightface/models
unzip antelopev2.zip
rm antelopev2.zip
cd ../../..

curl -s https://raw.githubusercontent.com/stavsap/ComfyUI-Playground/main/download-checkpoints.py | python

python main.py --listen
