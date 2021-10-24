from client.api import TokApi


def example(video_id: str):
    """
    Print comments for video
    """
    api = TokApi('YOUR_RAPID_API_KEY')

    offset = 0
    for i in range(0, 3):
        result = api.get_comments_by_video_id(video_id, offset=offset)
        data = result.json()

        for comment in data['comments']:
            print('Comment: {}, likes: {}, author: {}, author region: {}'.format(comment['text'],
                                                                                 comment['digg_count'],
                                                                                 comment['user']['nickname'],
                                                                                 comment['user']['region']))
        offset = data['cursor']


if __name__ == "__main__":
    example('6977747303692078337')
