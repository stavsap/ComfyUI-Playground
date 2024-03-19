import requests
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

downloads = [
    ("https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors?download=true", "sd_xl_base_1.0.safetensors", './models/checkpoints/sdxl/'),
    ("https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0/resolve/main/sd_xl_refiner_1.0.safetensors?download=true", "sd_xl_refiner_1.0.safetensors", './models/checkpoints/sdxl/'),
    ("https://huggingface.co/stabilityai/sdxl-vae/resolve/main/sdxl_vae.safetensors?download=true", "sdxl_vae.safetensors", './models/vae/'),

    ("https://huggingface.co/stabilityai/stable-cascade/resolve/main/comfyui_checkpoints/stable_cascade_stage_c.safetensors?download=true", "stable_cascade_stage_c.safetensors", './models/checkpoints/sd-cascade/'),
    ("https://huggingface.co/stabilityai/stable-cascade/resolve/main/comfyui_checkpoints/stable_cascade_stage_b.safetensors?download=true", "stable_cascade_stage_b.safetensors", './models/checkpoints/sd-cascade/'),
    ("https://huggingface.co/stabilityai/stable-cascade/resolve/main/stage_a.safetensors?download=true", "stable_cascade_stage_a.safetensors", './models/vae/'),

    ("https://huggingface.co/stabilityai/sdxl-turbo/resolve/main/sd_xl_turbo_1.0_fp16.safetensors?download=true",  "sd_xl_turbo_1.0_fp16.safetensors.safetensors", './models/checkpoints/sdxl/'),

    ("https://civitai.com/api/download/models/351306",  "dreamshaperXL_v21TurboDPMSDE.safetensors", './models/checkpoints/sdxl/'),

    ("https://huggingface.co/camenduru/SUPIR/resolve/main/SUPIR-v0F.ckpt?download=true",  "SUPIR-v0F.ckpt", './models/checkpoints/supir/'),
    ("https://huggingface.co/camenduru/SUPIR/resolve/main/SUPIR-v0Q.ckpt?download=true",  "SUPIR-v0Q.ckpt", './models/checkpoints/supir/'),

    ("https://huggingface.co/SG161222/RealVisXL_V3.0_Turbo/resolve/main/RealVisXL_V3.0_Turbo.safetensors?download=true",  "RealVisXL_V3.0_Turbo.safetensors", './models/checkpoints/sdxl/'),
    ("https://huggingface.co/SG161222/RealVisXL_V4.0_Lightning/resolve/main/RealVisXL_V4.0_Lightning.safetensors?download=true",  "RealVisXL_V4.0_Lightning.safetensors", './models/checkpoints/sdxl/'),

     ("https://huggingface.co/stavsap/my-comfy-models/resolve/main/juggernautXL_v9Rdphoto2Lightning.safetensors?download=true",  "juggernautXL_v9Rdphoto2Lightning.safetensors", './models/checkpoints/sdxl/'),
]

def download_file(url, file_name, path):
    if not os.path.exists(path):
        os.makedirs(path)
    with requests.get(url, stream=True, allow_redirects=True) as response:
        total_size = int(response.headers.get('content-length', 0))
        block_size = 4096  # 4KB blocks
        progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=file_name)
        with open(path+file_name, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)

        progress_bar.close()

with ThreadPoolExecutor(max_workers=4) as executor:
    future_to_download = {executor.submit(download_file, url, file_name, path): file_name for url, file_name, path in downloads}
    for future in as_completed(future_to_download):
        file_name = future_to_download[future]
