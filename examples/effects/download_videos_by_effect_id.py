import concurrent.futures
import os

import requests

from client.api import TokApi
from examples.contants import API_KEY, BASE_URL


def example(effect_id: str, dest_folder: str):
    """
    Download videos with effect to folder
    """
    api = TokApi(API_KEY, BASE_URL)

    dest_folder = os.path.join(dest_folder, effect_id)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    print('========== START DOWNLOADING VIDEOS BY EFFECT: {} ========== '.format(effect_id))

    offset = 0
    videos = []
    for i in range(0, 3):
        result = api.get_videos_by_effect_id(effect_id, offset=offset)

        data = result.json()
        videos.extend(data['aweme_list'])

        offset = data['cursor']

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
    example('1108584', os.path.dirname(os.path.abspath(__file__)))
