import requests
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

downloads = [

        # ControlNet
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
        ("https://huggingface.co/InstantX/InstantID/resolve/main/ControlNetModel/diffusion_pytorch_model.safetensors?download=true", "diffusion_pytorch_model.safetensors", './models/controlnet/'),

        ("https://huggingface.co/MonsterMMORPG/tools/resolve/main/antelopev2.zip?download=true", "antelopev2.zip", "./models/insightface/models/"),
        ("https://huggingface.co/InstantX/InstantID/resolve/main/ip-adapter.bin?download=true", "ip-adapter.bin", './models/instantid/'),
        ("https://huggingface.co/h94/IP-Adapter/resolve/main/models/image_encoder/model.safetensors?download=true", "CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors", './models/clip_vision/'),
        ("https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/image_encoder/model.safetensors?download=true", "CLIP-ViT-bigG-14-laion2B-39B-b160k.safetensors", './models/clip_vision/'),

        # IP-Adapter
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

        # IP-Adapter-FaceID
        ("https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid_sd15.bin?download=true", "ip-adapter-faceid_sd15.bin", './models/loras/'),
        ("https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-plus_sd15.bin?download=true", "ip-adapter-faceid-plus_sd15.bin", './models/loras/'),
        ("https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-plusv2_sd15.bin?download=true", "ip-adapter-faceid-plusv2_sd15.bin", './models/loras/'),
        ("https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-portrait_sd15.bin?download=true", "ip-adapter-faceid-portrait_sd15.bin", './models/loras/'),
        ("https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid_sdxl.bin?download=true", "ip-adapter-faceid_sdxl.bin", './models/loras/'),
        ("https://huggingface.co/h94/IP-Adapter-FaceID/resolve/main/ip-adapter-faceid-plusv2_sdxl.bin?download=true", "ip-adapter-plusv2_sdxl.bin", './models/loras/'),

        ("https://github.com/sczhou/CodeFormer/releases/download/v0.1.0/codeformer.pth",  "codeformer.pth", './models/facerestore_models/'),
        ("https://github.com/TencentARC/GFPGAN/releases/download/v1.3.4/GFPGANv1.4.pth",  "GFPGANv1.4.pth", './models/facerestore_models/'),

        ("https://huggingface.co/uwg/upscaler/resolve/main/ESRGAN/4x-UltraSharp.pth?download=true",  "4x-UltraSharp.pth", './models/upscale_models/'),

        # AnimatedDiff
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/mm_sd_v14.ckpt?download=true",  "mm_sd_v14.ckpt", './models/animatediff_models/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/mm_sd_v15.ckpt?download=true",  "mm_sd_v15.ckpt", './models/animatediff_models/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/mm_sd_v15_v2.ckpt?download=true",  "mm_sd_v15_v2.ckpt", './models/animatediff_models/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/mm_sdxl_v10_beta.ckpt?download=true",  "mm_sdxl_v10_beta.ckpt", './models/animatediff_models/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/v2_lora_PanLeft.ckpt?download=true",  "v2_lora_PanLeft.ckpt", './models/animatediff_motion_lora/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/v2_lora_PanRight.ckpt?download=true",  "v2_lora_PanRight.ckpt", './models/animatediff_motion_lora/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/v2_lora_RollingAnticlockwise.ckpt?download=true",  "v2_lora_RollingAnticlockwise.ckpt", './models/animatediff_motion_lora/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/v2_lora_RollingClockwise.ckpt?download=true",  "v2_lora_RollingClockwise.ckpt", './models/animatediff_motion_lora/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/v2_lora_TiltDown.ckpt?download=true",  "v2_lora_TiltDown.ckpt", './models/animatediff_motion_lora/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/v2_lora_TiltUp.ckpt?download=true",  "v2_lora_TiltUp.ckpt", './models/animatediff_motion_lora/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/v2_lora_ZoomIn.ckpt?download=true",  "v2_lora_ZoomIn.ckpt", './models/animatediff_motion_lora/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/v2_lora_ZoomOut.ckpt?download=true",  "v2_lora_ZoomOut.ckpt", './models/animatediff_motion_lora/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/v3_sd15_adapter.ckpt?download=true",  "v3_sd15_adapter.ckpt", './models/animatediff_models/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/v3_sd15_mm.ckpt?download=true",  "v3_sd15_mm.ckpt", './models/animatediff_models/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/v3_sd15_sparsectrl_rgb.ckpt?download=true",  "v3_sd15_sparsectrl_rgb.ckpt", './models/animatediff_models/'),
        ("https://huggingface.co/guoyww/animatediff/resolve/cd71ae134a27ec6008b968d6419952b0c0494cf2/v3_sd15_sparsectrl_scribble.ckpt?download=true",  "v3_sd15_sparsectrl_scribble.ckpt", './models/animatediff_models/'),

        # Flux clips
        ("https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true",  "t5xxl_fp16.safetensors", './models/clip/'),
        ("https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true",  "clip_l.safetensors", './models/clip/'),
        ("https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors?download=true",  "t5xxl_fp8_e4m3fn.safetensors", './models/clip/'),

        # Flux vae
        ("https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/ae.safetensors?download=true", "ae.safetensors", './models/vae/'),

        # Flux unet schnell (~24 GB)
        ("https://huggingface.co/black-forest-labs/FLUX.1-schnell/resolve/main/flux1-schnell.safetensors?download=true", "flux1-schnell.safetensors", './models/unet/'),

        # Flux unet Dev (~24 GB)
        ("https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux1-dev.safetensors?download=true", "flux1-dev.safetensors", './models/unet/'),

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
