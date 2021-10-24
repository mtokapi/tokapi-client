import concurrent.futures
import os

import httpx
from httpx import Response

from client.api import TokApi


def example(user_id: str, dest_folder: str):
    """
    Download all user videos to folder
    """
    api = TokApi('YOUR_RAPID_API_KEY')

    dest_folder = os.path.join(dest_folder, user_id)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    offset = 0
    has_more = 1
    print('========== START DOWNLOADING VIDEOS FOR USER: {} ========== '.format(user_id))

    videos = []
    while has_more == 1:
        result: Response = api.get_user_videos(user_id, offset=offset)

        data = result.json()
        videos.extend(data['aweme_list'])

        has_more = data['has_more']
        offset = data['max_cursor']

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for video_info in videos:
            executor.submit(download_video, dest_folder, video_info)


def download_video(dest_folder: str, video_info: dict):
    filename = '{}.mp4'.format(video_info['aweme_id'])
    file_path = os.path.join(dest_folder, filename)

    with httpx.stream("GET", video_info['video']['play_addr']['url_list'][0]) as response:
        print("Saving to", os.path.abspath(file_path))
        with open(file_path, 'wb') as f:
            for chunk in response.iter_bytes(chunk_size=1024 * 8):
                f.write(chunk)


if __name__ == "__main__":
    example('6784563164518679557', os.path.dirname(os.path.abspath(__file__)))
