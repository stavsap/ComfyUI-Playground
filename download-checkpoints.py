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

    ("https://huggingface.co/camenduru/SUPIR/resolve/main/SUPIR-v0F.ckpt?download=true",  "SUPIR-v0F.ckpt", './models/checkpoints/supir/'),
    ("https://huggingface.co/camenduru/SUPIR/resolve/main/SUPIR-v0Q.ckpt?download=true",  "SUPIR-v0Q.ckpt", './models/checkpoints/supir/'),

    ("https://huggingface.co/SG161222/RealVisXL_V3.0_Turbo/resolve/main/RealVisXL_V3.0_Turbo.safetensors?download=true",  "RealVisXL_V3.0_Turbo.safetensors", './models/checkpoints/sdxl/'),
    ("https://huggingface.co/SG161222/RealVisXL_V4.0_Lightning/resolve/main/RealVisXL_V4.0_Lightning.safetensors?download=true",  "RealVisXL_V4.0_Lightning.safetensors", './models/checkpoints/sdxl/'),

    ("https://huggingface.co/Lykon/dreamshaper-xl-v2-turbo/resolve/main/DreamShaperXL_Turbo_v2_1.safetensors?download=true",  "DreamShaperXL_Turbo_v2_1.safetensors", './models/checkpoints/sdxl/'),
    ("https://huggingface.co/Lykon/dreamshaper-xl-lightning/resolve/main/DreamShaperXL_Lightning.safetensors?download=true",  "DreamShaperXL_Lightning.safetensors", './models/checkpoints/sdxl/'),

    ("https://huggingface.co/RunDiffusion/Juggernaut-XL-v9/resolve/main/Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors?download=true",  "Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors", './models/checkpoints/sdxl/'),
    ("https://huggingface.co/latent-consistency/lcm-lora-sdxl/resolve/main/pytorch_lora_weights.safetensors?download=true",  "LCM-lora-weights.safetensors", './models/loras/'),
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

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder: '{folder_path}', created.")

for url, file_name, path in downloads:
    create_folder_if_not_exists(path)

with ThreadPoolExecutor(max_workers=4) as executor:
    future_to_download = {executor.submit(download_file, url, file_name, path): file_name for url, file_name, path in downloads}
    for future in as_completed(future_to_download):
        file_name = future_to_download[future]
