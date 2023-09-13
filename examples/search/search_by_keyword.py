from client.api import TokApi
from examples.constants import API_KEY, BASE_URL


def search_user(keyword: str):
    """
    Print results of user search
    """
    api = TokApi(API_KEY, BASE_URL)

    offset = 0
    for i in range(0, 3):
        result = api.search_user_by_keyword(keyword, offset=offset)
        data = result.json()

        for user in data['user_list']:
            info = user['user_info']
            print('Nickname: {}, region: {}'.format(info['nickname'],
                                                    info.get('region')))

        offset = data['cursor']


def search_hashtag(keyword: str):
    """
    Print results of hashtag search
    """
    api = TokApi(API_KEY, BASE_URL)

    offset = 0
    for i in range(0, 3):
        result = api.search_hashtags_by_keyword(keyword, offset=offset)
        data = result.json()

        for hashtag in data['challenge_list']:
            info = hashtag['challenge_info']
            print('Name: {}, user count: {}'.format(info['cha_name'],
                                                    info['user_count']))

        offset = data['cursor']


def search_music(keyword: str):
    """
    Print results of music search
    """
    api = TokApi(API_KEY, BASE_URL)

    offset = 0
    for i in range(0, 3):
        result = api.search_music_by_keyword(keyword, offset=offset)
        data = result.json()

        for music in data['music']:
            print('Name: {}, user count: {}, listen url: {}'.format(music['title'],
                                                                    music['user_count'],
                                                                    music['play_url']['url_list'][0]))

        offset = data['cursor']


def search_videos(keyword: str):
    """
    Print results of videos search
    """
    api = TokApi(API_KEY, BASE_URL)

    offset = 0
    for i in range(0, 3):
        result = api.search_videos_by_keyword(keyword, sort_type=1, publish_time=1, offset=offset)
        data = result.json()

        for video in data['aweme_list']:
            print('ID: {}, views count: {}, no watermark url: {}'.format(video['aweme_id'],
                                                                         video['statistics']['play_count'],
                                                                         video['video']['play_addr']['url_list'][0]))

        offset = data['cursor']


def search_live_streams(keyword: str):
    """
    Print results of live stream search
    """
    api = TokApi(API_KEY, BASE_URL)

    offset = 0
    for i in range(0, 3):
        result = api.search_live_streams_by_keyword(keyword, offset=offset)
        data = result.json()

        for live in data['data']:
            print('ID: {}, author nickname: {}'.format(live['lives']['aweme_id'], live['lives']['author']['unique_id']))

        offset = data['cursor']


def search_locations(keyword: str):
    """
    Print results of locations search
    """

    api = TokApi(API_KEY, BASE_URL)

    offset = 0
    for i in range(0, 3):
        result = api.search_locations_by_keyword(keyword, offset=offset)
        data = result.json()

        for poi in data['poi_info']['poi_info']:
            print('ID: {}, location: {}, type: {}'.format(poi['poi_id_str'],
                                                          poi['poi_location'],
                                                          poi['poi_type']))

        offset = data['cursor']


if __name__ == "__main__":
    print('==== User Search ====')
    search_user('nike')

    print('==== Hashtag Search ====')
    search_hashtag('work')

    print('==== Music Search ====')
    search_music('happy new year')

    print('==== Video Search ====')
    search_videos('happy new year')

    print('==== Location Live Streams ====')
    search_live_streams('nike')

    print('==== Location Search ====')
    search_locations('London')
