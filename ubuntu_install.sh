curl -o run.sh https://raw.githubusercontent.com/stavsap/ComfyUI-Playground/main/run.sh
chmod +x run.sh
git clone https://github.com/comfyanonymous/ComfyUI.git

cd ComfyUI
python3 -m venv venv
source venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu126

python -m pip install huggingface_hub opencv-python insightface onnxruntime onnxruntime-gpu simpleeval xformers imageio-ffmpeg

git clone https://github.com/ltdrdata/ComfyUI-Manager.git custom_nodes/ComfyUI-Manager
git clone https://github.com/pythongosssss/ComfyUI-Custom-Scripts.git custom_nodes/ComfyUI-Custom-Scripts
git clone https://github.com/cubiq/ComfyUI_IPAdapter_plus.git custom_nodes/ComfyUI_IPAdapter_plus
git clone https://github.com/cubiq/ComfyUI_InstantID.git custom_nodes/ComfyUI_InstantID
git clone https://github.com/cubiq/ComfyUI_essentials.git custom_nodes/ComfyUI_essentials
git clone https://github.com/Ttl/ComfyUi_NNLatentUpscale.git custom_nodes/ComfyUi_NNLatentUpscale
git clone https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved.git custom_nodes/ComfyUI-AnimateDiff-Evolved
git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git custom_nodes/ComfyUI-VideoHelperSuite
git clone https://github.com/rgthree/rgthree-comfy.git custom_nodes/rgthree-comfy
git clone https://github.com/LEv145/images-grid-comfy-plugin.git custom_nodes/images-grid-comfy-plugin
git clone https://github.com/glowcone/comfyui-load-image-from-url.git custom_nodes/comfyui-load-image-from-url
git clone https://github.com/11cafe/comfyui-workspace-manager.git custom_nodes/comfyui-workspace-manager
git clone https://github.com/ssitu/ComfyUI_UltimateSDUpscale.git --recursive custom_nodes/ComfyUI_UltimateSDUpscale

git clone https://github.com/crystian/ComfyUI-Crystools.git custom_nodes/ComfyUI-Crystools
python -m pip install -r custom_nodes/ComfyUI-Crystools/requirements.txt

git clone https://github.com/jags111/efficiency-nodes-comfyui.git custom_nodes/efficiency-nodes-comfyui
python -m pip install -r custom_nodes/efficiency-nodes-comfyui/requirements.txt

git clone https://github.com/giriss/comfy-image-saver.git custom_nodes/comfy-image-saver
python -m pip install -r custom_nodes/comfy-image-saver/requirements.txt

git clone https://github.com/kijai/ComfyUI-SUPIR.git custom_nodes/ComfyUI-SUPIR
python -m pip install -r custom_nodes/ComfyUI-SUPIR/requirements.txt

git clone https://github.com/ltdrdata/ComfyUI-Inspire-Pack.git custom_nodes/ComfyUI-Inspire-Pack
python -m pip install -r custom_nodes/ComfyUI-Inspire-Pack/requirements.txt

git clone https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git custom_nodes/ComfyUI-Advanced-ControlNet

git clone https://github.com/kijai/ComfyUI-Florence2.git custom_nodes/ComfyUI-Florence2
python -m pip install -r custom_nodes/ComfyUI-Florence2/requirements.txt

git clone https://github.com/Gourieff/ComfyUI-ReActor.git custom_nodes/ComfyUI-ReActor
cd custom_nodes/ComfyUI-ReActor
python install.py
cd ../..

git clone https://github.com/stavsap/comfyui-ollama.git custom_nodes/comfyui-ollama
python -m pip install -r custom_nodes/comfyui-ollama/requirements.txt

git clone https://github.com/stavsap/comfyui-kokoro.git custom_nodes/comfyui-kokoro
python -m pip install -r custom_nodes/comfyui-kokoro/requirements.txt

curl -s https://raw.githubusercontent.com/stavsap/ComfyUI-Playground/main/download-models.py | python

cd models/insightface/models
unzip antelopev2.zip
rm antelopev2.zip
cd ../../..

python main.py --listen
