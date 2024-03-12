import requests
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

downloads = [
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p.pth", "control_v11e_sd15_ip2p.pth", "./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11e_sd15_ip2p.yaml","control_v11e_sd15_ip2p.yaml","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle.pth","control_v11e_sd15_shuffle.pth","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11e_sd15_shuffle.yaml","control_v11e_sd15_shuffle.yaml","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile.pth","control_v11f1e_sd15_tile.pth","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile.yaml","control_v11f1e_sd15_tile.yaml","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth.pth","control_v11f1p_sd15_depth.pth","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1p_sd15_depth.yaml","control_v11f1p_sd15_depth.yaml","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny.pth","control_v11p_sd15_canny.pth","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_canny.yaml","control_v11p_sd15_canny.yaml","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint.pth","control_v11p_sd15_inpaint.pth","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_inpaint.yaml","control_v11p_sd15_inpaint.yaml","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart.pth","control_v11p_sd15_lineart.pth","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart.yaml","control_v11p_sd15_lineart.yaml","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_mlsd.pth","control_v11p_sd15_mlsd.pth","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_mlsd.yaml","control_v11p_sd15_mlsd.yaml","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_normalbae.pth","control_v11p_sd15_normalbae.pth","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_normalbae.yaml","control_v11p_sd15_normalbae.yaml","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose.pth","control_v11p_sd15_openpose.pth","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose.yaml","control_v11p_sd15_openpose.yaml","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_scribble.pth","control_v11p_sd15_scribble.pth","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_scribble.yaml","control_v11p_sd15_scribble.yaml","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_seg.pth", "control_v11p_sd15_seg.pth","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_seg.yaml", "control_v11p_sd15_seg.yaml","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge.pth", "control_v11p_sd15_softedge.pth","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_softedge.yaml", "control_v11p_sd15_softedge.yaml","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15s2_lineart_anime.pth", "control_v11p_sd15s2_lineart_anime.pth","./models/controlnet/"),
        ("https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15s2_lineart_anime.yaml", "control_v11p_sd15s2_lineart_anime.yaml","./models/controlnet/"),
        ("https://huggingface.co/MonsterMMORPG/tools/resolve/main/antelopev2.zip?download=true", "antelopev2.zip", "./models/insightface/models/"),
        ("https://huggingface.co/InstantX/InstantID/resolve/main/ip-adapter.bin?download=true", "ip-adapter.bin", './models/instantid/'),
        ("https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true", "diffusion_pytorch_model.safetensors", './models/controlnet/'),
        ("https://huggingface.co/h94/IP-Adapter/resolve/main/models/image_encoder/model.safetensors?download=true", "model.safetensors", './models/clip_vision/'),
        ("https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/image_encoder/model.safetensors?download=true", "sdxl_model.safetensors", './models/clip_vision/'),

        ("https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter_sd15.safetensors?download=true", "ip-adapter_sd15.safetensors", './models/ipadapter/'),
        ("https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter_sd15_light.safetensors?download=true", "ip-adapter_sd15_light.safetensors", './models/ipadapter/'),
        ("https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter-plus_sd15.safetensors?download=true", "ip-adapter-plus_sd15.safetensors", './models/ipadapter/'),
        ("https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter-plus-face_sd15.safetensors?download=true", "ip-adapter-plus-face_sd15.safetensors", './models/ipadapter/'),
        ("https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter-full-face_sd15.safetensors?download=true", "ip-adapter-full-face_sd15.safetensors", './models/ipadapter/'),
        ("https://huggingface.co/h94/IP-Adapter/resolve/main/models/ip-adapter_sd15_vit-G.safetensors?download=true", "ip-adapter_sd15_vit-G.safetensors", './models/ipadapter/'),
        ("https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter_sdxl.safetensors?download=true", "ip-adapter_sdxl.safetensors", './models/ipadapter/'),
        ("https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter_sdxl_vit-h.safetensors?download=true", "ip-adapter_sdxl_vit-h.safetensors", './models/ipadapter/'),
        ("https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter-plus_sdxl_vit-h.safetensors?download=true", "ip-adapter-plus_sdxl_vit-h.safetensors", './models/ipadapter/'),
        ("https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter-plus-face_sdxl_vit-h.safetensors?download=true", "ip-adapter-plus-face_sdxl_vit-h.safetensors", './models/ipadapter/'),

        ("https://huggingface.co/AIBrainBox/inswapper_128.onnx/resolve/main/inswapper_128.onnx?download=true", "inswapper_128.onnx", './models/insightface/models/'),

        ("https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid_sd15.bin?download=true", "ip-adapter-faceid_sd15.bin", './models/loras/'),
        ("https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-plus_sd15.bin?download=true", "ip-adapter-faceid-plus_sd15.bin", './models/loras/'),
        ("https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-plusv2_sd15.bin?download=true", "ip-adapter-faceid-plusv2_sd15.bin", './models/loras/'),
        ("https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-portrait_sd15.bin?download=true", "ip-adapter-faceid-portrait_sd15.bin", './models/loras/'),
        ("https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid_sdxl.bin?download=true", "ip-adapter-faceid_sdxl.bin", './models/loras/'),
        ("https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-plusv2_sdxl.bin?download=true", "ip-adapter-plusv2_sdxl.bin", './models/loras/'),

        ("https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/codeformer.pth",  "codeformer.pth", './models/facerestore_models/'),
        ("https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth",  "GFPGANv1.4.pth", './models/facerestore_models/'),

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
