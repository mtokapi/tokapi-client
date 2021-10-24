from client.api import TokApi


def example_by_id(effect_id: str):
    """
    Print effect info by id
    """
    api = TokApi('YOUR_RAPID_API_KEY')

    result = api.get_effect_info_by_id(effect_id)
    data = result.json()

    info = data['sticker_infos'][0]
    print('Name: {}, user count: {}, views: {}'.format(info['name'],
                                                       info['user_count'],
                                                       info['vv_count']))


def example_by_ids(ids: list):
    """
    Print effect infos by ids
    """
    api = TokApi('YOUR_RAPID_API_KEY')

    result = api.get_effect_info_by_ids(ids)
    data = result.json()

    for sticker in data['sticker_infos']:
        print('Name: {}, user count: {}, views: {}'.format(sticker['name'],
                                                           sticker['user_count'],
                                                           sticker['vv_count']))


if __name__ == "__main__":
    example_by_id('1108584')
    example_by_ids(['1108584', '1108584'])
