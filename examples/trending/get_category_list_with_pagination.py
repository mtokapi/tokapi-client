from client.api import TokApi
from examples.constants import API_KEY, BASE_URL


def example():
    """
    Load trending categories for default US region
    """
    api = TokApi(API_KEY, BASE_URL)

    offset = 0
    for i in range(0, 3):
        result = api.get_categories(offset=offset)
        data = result.json()

        print('========== START PAGE ========== items count: {}'.format(len(data['category_list'])))
        for category in data['category_list']:
            print('Category type: {}'.format(category['desc']))
            if category['category_type'] == 3:
                print_effect_info(category)
            elif category['category_type'] == 1:
                print_music_info(category)
            elif category['category_type'] == 0:
                print_challenge_info(category)
        print('=========== END PAGE ===========\n')

        # If we have more results then use cursor param from response
        if data['has_more'] == 1:
            offset = data['cursor']
        else:
            break


def print_effect_info(category: dict):
    print('Effect name : {}, user count: {}'.format(category['effect_info']['name'],
                                                    category['effect_info']['user_count']))


def print_music_info(category: dict):
    print('Music name : {}, user count: {}'.format(category['music_info']['title'],
                                                   category['music_info']['user_count']))


def print_challenge_info(category: dict):
    print('Challenge name : {}, user count: {}, view count: {}'.format(category['challenge_info']['cha_name'],
                                                                       category['challenge_info']['user_count'],
                                                                       category['challenge_info']['view_count']))


if __name__ == "__main__":
    example()
