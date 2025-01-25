# ComfyUI Playground

<a href="https://www.buymeacoffee.com/stavsapq" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="40" width="174"></a>

# Windows Install

The installation will set up ComfyUI on the host, and download custom nodes and relevant models. Pre-requisites are:

- [python 3.10+](https://www.python.org/downloads/)
- [git](https://git-scm.com/downloads)
- [cmake](https://cmake.org/download/)

Current Install Size: ~170GB

open cmd in desired path, copy past this command and run:

```shell
curl -o install.bat https://raw.githubusercontent.com/stavsap/ComfyUI-Playground/main/install.bat && cmd /c install.bat
```

# Ubuntu Install

- [python 3.10+](https://www.python.org/downloads/), python3-venv and python3-dev.
- [git](https://git-scm.com/downloads)
- unzip
- make
- cmake
- g++

```shell
curl -sLS https://raw.githubusercontent.com/stavsap/ComfyUI-Playground/main/ubuntu_install.sh | bash
```

# Additional Custom nodes Installed

- [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
- [ComfyUI-Ollama](https://github.com/stavsap/comfyui-ollama)
- [ComfyUI-Kokoro](https://github.com/stavsap/comfyui-kokoro)
- [ComfyUI-Essentials](https://github.com/cubiq/ComfyUI_essentials)
- [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)
- [ComfyUI-Crystools](https://github.com/crystian/ComfyUI-Crystools)
- [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git)
- [ComfyUI-IPAdapter-plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus.git)
- [ComfyUI-InstantID](https://github.com/cubiq/ComfyUI_InstantID.git)
- [ComfyUI-Reactor](https://github.com/Gourieff/ComfyUI-ReActor)
- [ComfyUI-NN-Latent-Upscale](https://github.com/Ttl/ComfyUi_NNLatentUpscale)
- [ComfyUI-AnimateDiff-Evolved](https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved)
- [ComfyUI-SUPIR](https://github.com/kijai/ComfyUI-SUPIR)
- [ComfyUI-RG3](https://github.com/rgthree/rgthree-comfy)
- [ComfyUI-Image-Saver](https://github.com/giriss/comfy-image-saver)
- [ComfyUI-Images-Grid](https://github.com/LEv145/images-grid-comfy-plugin)
- [ComfyUI-Efficiency-Nodes](https://github.com/jags111/efficiency-nodes-comfyui)
- [ComfyUI-Florence2](https://github.com/kijai/ComfyUI-Florence2)

# Models:

- Stable Diffusion XL 1.0 [base](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) and [refiner](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0).
- Stable Diffusion [Cascade](https://huggingface.co/stabilityai/stable-cascade).
- Stable Diffusion XL [Turbo](https://huggingface.co/stabilityai/sdxl-turbo).
- [Juggernaut-XL-v9](https://huggingface.co/RunDiffusion/Juggernaut-XL-v9)
- [dreamshaper-xl-v2-turbo](https://huggingface.co/Lykon/dreamshaper-xl-v2-turbo).
- [dreamshaper-xl-lightning](https://huggingface.co/Lykon/dreamshaper-xl-lightning)
- [RealVisXL V3 Turbo](https://huggingface.co/SG161222/RealVisXL_V3.0_Turbo).
- [RealVisXL V4.0 Lightning](https://huggingface.co/SG161222/RealVisXL_V4.0_Lightning)
- get more at: [https://civitai.com](https://civitai.com/)

# Upscalers

- [Open Model DB](https://openmodeldb.info/)
- https://huggingface.co/uwg/upscaler


# Blogs and Workflows:

[SD 3.5 Comfy blog](https://blog.comfy.org/p/sd-35-medium)
[ControlNet Models for Stable Diffusion 3.5 Large](https://blog.comfy.org/p/sd3-5-large-controlnet)