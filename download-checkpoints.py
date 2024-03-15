import requests
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

downloads = [
        ("https://civitai.com/api/download/models/357609",  "juggernautXL_v9Rdphoto2Lightning.safetensors", './models/checkpoints/sdxl/'),
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
