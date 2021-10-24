import concurrent.futures
import os

import httpx
from httpx import Response

from client.api import TokApi


def example(hashtag_id: str, dest_folder: str):
    """
    Download videos by specific hashtag to folder
    """
    api = TokApi('YOUR_RAPID_API_KEY')

    dest_folder = os.path.join(dest_folder, hashtag_id)
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    print('========== START DOWNLOADING VIDEOS BY HASHTAG: {} ========== '.format(hashtag_id))

    offset = 0
    videos = []
    for i in range(0, 3):
        result: Response = api.get_videos_by_hashtag_id(hashtag_id, offset=offset)

        data = result.json()
        videos.extend(data['aweme_list'])

        offset = data['cursor']

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
    example('2878999', os.path.dirname(os.path.abspath(__file__)))
