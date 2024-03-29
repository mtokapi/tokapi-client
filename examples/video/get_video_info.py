from client.api import TokApi
from examples.constants import API_KEY, BASE_URL


def example_by_id(video_id: str):
    """
    Print video info by id
    """
    api = TokApi(API_KEY, BASE_URL)

    result = api.get_video_info_by_id(video_id, region='FR')
    data = result.json()

    watch_url = data['aweme_detail']['video']['play_addr']['url_list'][0]
    statistics = data['aweme_detail']['statistics']
    print('Likes: {}, views: {}, shares: {}, watch url: {}'.format(statistics['digg_count'],
                                                                   statistics['play_count'],
                                                                   statistics['share_count'],
                                                                   watch_url))


def example_by_link(video_web_link: str):
    """
    Print video info by web link
    """
    api = TokApi(API_KEY, BASE_URL)

    result = api.get_video_info_by_web_link(video_web_link, region='FR')
    data = result.json()

    watch_url = data['aweme_detail']['video']['play_addr']['url_list'][0]
    statistics = data['aweme_detail']['statistics']
    print('Likes: {}, views: {}, shares: {}, watch url: {}'.format(statistics['digg_count'],
                                                                   statistics['play_count'],
                                                                   statistics['share_count'],
                                                                   watch_url))


if __name__ == "__main__":
    example_by_id('6977747303692078337')
    example_by_link('https://www.tiktok.com/@adidas/video/7013447428070280454')
