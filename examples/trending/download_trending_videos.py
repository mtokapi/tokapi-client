import concurrent.futures
import os

import requests

from client.api import TokApi
from examples.constants import API_KEY, BASE_URL


def example(dest_folder: str):
    """
    Download trending videos to folder
    """
    api = TokApi(API_KEY, BASE_URL)

    dest_folder = os.path.join(dest_folder, '')
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    print('========== START DOWNLOADING TRENDING VIDEOS ========== ')

    videos = []
    device = ''
    cookie = ''
    for i in range(0, 5):
        result = api.get_trending_feed(0 if i == 0 else 2, device_config=device, cookie=cookie)

        data = result.json()
        videos.extend(data['aweme_list'])
        device = result.headers.get('x-device')
        cookie = result.headers.get('x-cookie')

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for video_info in videos:
            executor.submit(download_video, dest_folder, video_info)


def download_video(dest_folder: str, video_info: dict):
    filename = '{}.mp4'.format(video_info['aweme_id'])
    file_path = os.path.join(dest_folder, filename)

    with requests.get(video_info['video']['play_addr']['url_list'][0], stream=True) as response:
        print("Saving to", os.path.abspath(file_path))

        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024 * 8):
                f.write(chunk)


if __name__ == "__main__":
    example(os.path.dirname(os.path.abspath(__file__)))
