# ComfyUI Playground

# Windows Install

The installation will set up ComfyUI on the host, and download custom nodes and relevant models. Pre-requisites are:

- [python 3.10+](https://www.python.org/downloads/)
- [git](https://git-scm.com/downloads)
- Install [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) (it is required for some custom nodes to build c compiled python packages) OR only [VS C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) and select "Desktop Development with C++" under "Workloads -> Desktop & Mobile". Make sure the "cmake" is set in you cli PATH.

Current Install Size: ~100GB

open cmd, copy past this command and run:

```shell
curl -o install.bat https://raw.githubusercontent.com/stavsap/ComfyUI-Playground/main/install.bat && cmd /c install.bat
```

# Ubuntu Install

- [python 3.10+](https://www.python.org/downloads/)
- [git](https://git-scm.com/downloads)
- unzip
- make

```shell
curl -sLS https://raw.githubusercontent.com/stavsap/ComfyUI-Playground/main/ubuntu_install.sh | bash
```

# Additional Custom nodes Installed

- [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
- [ComfyUI-Advanced-ControlNet](https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet.git)
- [ComfyUI-IPAdapter-plus](https://github.com/cubiq/ComfyUI_IPAdapter_plus.git)
- [ComfyUI-InstantID](https://github.com/cubiq/ComfyUI_InstantID.git)
- [ComfyUI-Essentials](https://github.com/cubiq/ComfyUI_essentials)
- [ComfyUI-Reactor](https://github.com/Gourieff/comfyui-reactor-node.git)
- [ComfyUI-Ollama](https://github.com/stavsap/comfyui-ollama.git)
- [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)
- [ComfyUI-NN-Latent-Upscale](https://github.com/Ttl/ComfyUi_NNLatentUpscale)
- [ComfyUI-AnimateDiff-Evolved](https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved)
- [ComfyUI-SUPIR](https://github.com/kijai/ComfyUI-SUPIR)
- [ComfyUI-RG3](https://github.com/rgthree/rgthree-comfy)
- [ComfyUI-Image-Saver](https://github.com/giriss/comfy-image-saver)

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
