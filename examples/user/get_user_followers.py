from client.api import TokApi
from examples.constants import API_KEY, BASE_URL


def example(user_id: str):
    """
    Print user followers info
    """
    api = TokApi(API_KEY, BASE_URL)

    max_time = 0
    for i in range(0, 3):
        result = api.get_user_followers(user_id, offset=max_time)
        data = result.json()

        for follower in data['followers']:
            print('Nickname: {}, region: {}'.format(follower['nickname'],
                                                    follower['region']))
        if data['has_more']:
            max_time = data['min_time']
        else:
            break


if __name__ == "__main__":
    example('6784563164518679557')
