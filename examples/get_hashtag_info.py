from client.api import TokApi


def example():
    """
    Print hashtag info
    """
    api = TokApi('YOUR_RAPID_API_KEY')

    result = api.get_hashtag_info_by_id('2878999')
    data = result.json()

    info = data['ch_info']
    print('Hashtag name: {}, user count: {}, views count: {}'.format(info['cha_name'],
                                                                     info['user_count'],
                                                                     info['view_count']))


if __name__ == "__main__":
    example()
