from client.api import TokApi
from examples.contants import API_KEY, BASE_URL


def example(music_id: str):
    """
    Print hashtag info
    """
    api = TokApi(API_KEY, BASE_URL)

    result = api.get_music_info_by_id(music_id)
    data = result.json()

    info = data['music_info']
    print('Music name: {}, user count: {}, listen url: {}'.format(info['title'],
                                                                  info['user_count'],
                                                                  info['play_url']['url_list'][0]))


if __name__ == "__main__":
    example('6928004115846924290')
