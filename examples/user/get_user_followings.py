from client.api import TokApi
from examples.contants import API_KEY, BASE_URL


def example(user_id: str):
    """
    Print user followings info
    """
    api = TokApi(API_KEY, BASE_URL)

    max_time = 0
    for i in range(0, 3):
        result = api.get_user_followings(user_id, offset=max_time)
        data = result.json()

        for follower in data['followings']:
            print('Nickname: {}, region: {}'.format(follower['nickname'],
                                                    follower['region']))
        if data['has_more']:
            max_time = data['min_time']
        else:
            break


if __name__ == "__main__":
    example('7018908209437377542')
