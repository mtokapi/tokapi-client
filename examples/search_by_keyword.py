from client.api import TokApi


def search_user(keyword: str):
    """
    Print results of user search
    """
    api = TokApi('YOUR_RAPID_API_KEY')

    offset = 0
    for i in range(0, 3):
        result = api.search_user_by_keyword(keyword, offset=offset)
        data = result.json()

        for user in data['user_list']:
            info = user['user_info']
            print('Nickname: {}, region: {}'.format(info['nickname'],
                                                    info['region']))

        offset = data['cursor']


def search_hashtag(keyword: str):
    """
    Print results of hashtag search
    """
    api = TokApi('YOUR_RAPID_API_KEY')

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
    api = TokApi('YOUR_RAPID_API_KEY')

    offset = 0
    for i in range(0, 3):
        result = api.search_music_by_keyword(keyword, offset=offset)
        data = result.json()

        for music in data['music']:
            print('Name: {}, user count: {}, listen url: {}'.format(music['title'],
                                                                    music['user_count'],
                                                                    music['play_url']['url_list'][0]))

        offset = data['cursor']


if __name__ == "__main__":
    print('==== User Search ====')
    search_user('nike')
    print('==== Hashtag Search ====')
    search_hashtag('work')
    print('==== Music Search ====')
    search_music('happy new year')
