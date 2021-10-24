import httpx
from httpx import Response

from client.client import TokApiClient


class TokApi(object):
    def __init__(self, api_key: str, rapid_host: str = 'https://tokapi-mobile-version.p.rapidapi.com',
                 proxy: httpx.Proxy = None):
        self.http_client = TokApiClient(api_key=api_key, rapid_host=rapid_host, proxy=proxy)

    def get_categories(self, count: int = 10, offset: int = 0, region: str = 'US') -> Response:
        """
        :param count: number of items, a maximum value is 50 (maybe changed by tiktok in future)
        :param offset: number of item which will be skipped from start
        :param region: region
        :return: Response object
        """
        params = {
            'count': count,
            'offset': offset,
            'region': region,
        }

        response = self.http_client.execute('GET', '/v1/category', params)

        return response

    def get_trending_feed(self, pull_type: int = 0, region: str = 'US', device_config: str = '',
                          cookie: str = '') -> Response:
        """
        :param pull_type: type of loading feed (0 - Initial loading, 2 - Load more, 8 - Reload)
        :param region: region
        :param device_config: device configuration
        :param cookie: cookie
        :return: Response object
        """
        params = {
            'pull_type': pull_type,
            'region': region
        }

        headers = {'x-device': device_config, 'x-cookie': cookie} if device_config and cookie else None
        response = self.http_client.execute('GET', '/v1/feed/recommended', params=params, headers=headers)

        return response

    def get_hashtag_info_by_id(self, hashtag_id: str) -> Response:
        """
        :param hashtag_id: hashtag id
        :return: Response object
        """

        response = self.http_client.execute('GET', '/v1/hashtag/{}'.format(hashtag_id))

        return response

    def get_videos_by_hashtag_id(self, hashtag_id: str, count: int = 20, offset: int = 0) -> Response:
        """
        :param hashtag_id: hashtag id
        :param count: number of items, a maximum value is 20 (can be changed by tiktok in future)
        :param offset: number of item which will be skipped from start
        :return: Response object
        """
        params = {
            'count': count,
            'offset': offset,
        }

        response = self.http_client.execute('GET', '/v1/hashtag/posts/{}'.format(hashtag_id), params)

        return response

    def get_music_info_by_id(self, music_id: str) -> Response:
        """
        :param music_id: music id
        :return: Response object
        """

        response = self.http_client.execute('GET', '/v1/music/{}'.format(music_id))

        return response

    def get_videos_by_music_id(self, music_id: str, count: int = 20, offset: int = 0) -> Response:
        """
        :param music_id: music id
        :param count: number of items, a maximum value is 20 (can be changed by tiktok in future)
        :param offset: number of item which will be skipped from start
        :return: Response object
        """
        params = {
            'count': count,
            'offset': offset,
        }

        response = self.http_client.execute('GET', '/v1/music/posts/{}'.format(music_id), params)

        return response

    def get_video_info_by_id(self, video_id: str) -> Response:
        """
        :param video_id: video id
        :return: Response object
        """

        response = self.http_client.execute('GET', '/v1/post/{}'.format(video_id))

        return response

    def get_video_info_by_web_link(self, video_web_link: str) -> Response:
        """
        :param video_web_link: video web link
        :return: Response object
        """

        params = {
            'video_url': video_web_link
        }

        response = self.http_client.execute('GET', '/v1/post', params)

        return response

    def get_user_videos(self, user_id: str, count: int = 20, offset: int = 0) -> Response:
        """
        :param user_id: tiktok user id
        :param count: number of items, a maximum value is 50 (can be changed by tiktok in future)
        :param offset: number of item which will be skipped from start
        :return: Response object
        """
        params = {
            'count': count,
            'offset': offset,
        }

        response = self.http_client.execute('GET', '/v1/post/user/{}/posts'.format(user_id), params)

        return response

    def get_comments_by_video_id(self, video_id: str, count: int = 20, offset: int = 0) -> Response:
        """
        :param video_id: video id
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """
        params = {
            'count': count,
            'offset': offset,
        }

        response = self.http_client.execute('GET', '/v1/post/{}/comments'.format(video_id), params)

        return response

    def search_user_by_keyword(self, keyword: str, count: int = 10, offset: int = 0) -> Response:
        """
        :param keyword: search text query
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """
        params = {
            'keyword': keyword,
            'count': count,
            'offset': offset,
        }

        response = self.http_client.execute('GET', '/v1/search/user', params)

        return response

    def search_hashtags_by_keyword(self, keyword: str, count: int = 10, offset: int = 0) -> Response:
        """
        :param keyword: search text query
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """
        params = {
            'keyword': keyword,
            'count': count,
            'offset': offset,
        }

        response = self.http_client.execute('GET', '/v1/search/hashtag', params)

        return response

    def search_music_by_keyword(self, keyword: str, count: int = 10, offset: int = 0) -> Response:
        """
        :param keyword: search text query
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """
        params = {
            'keyword': keyword,
            'count': count,
            'offset': offset,
        }

        response = self.http_client.execute('GET', '/v1/search/music', params)

        return response

    def get_videos_by_effect_id(self, effect_id: str, count: int = 20, offset: int = 0) -> Response:
        """
        :param effect_id: effect id
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """
        params = {
            'count': count,
            'offset': offset,
        }

        response = self.http_client.execute('GET', '/v1/sticker/posts/1108584'.format(effect_id), params)

        return response

    def get_effect_info_by_id(self, effect_id: str) -> Response:
        """
        :param effect_id: effect id
        :return: Response object
        """

        response = self.http_client.execute('GET', '/v1/sticker/{}'.format(effect_id))

        return response

    def get_effect_info_by_ids(self, effect_ids: list) -> Response:
        """
        :param effect_ids: effect ids
        :return: Response object
        """

        params = {
            'sticker_ids': ','.join(effect_ids)
        }

        response = self.http_client.execute('GET', '/v1/sticker', params)

        return response

    def get_user_info_by_id(self, user_id: str) -> Response:
        """
        :param user_id: user id
        :return: Response object
        """

        response = self.http_client.execute('GET', '/v1/user/{}'.format(user_id))

        return response

    def get_user_followers(self, user_id: str, count: int = 20, offset: int = 0) -> Response:
        """
        :param user_id: user id
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'count': count,
            'offset': offset
        }

        response = self.http_client.execute('GET', '/v1/user/{}/followers'.format(user_id), params)

        return response

    def get_user_followings(self, user_id: str, count: int = 20, offset: int = 0) -> Response:
        """
        :param user_id: user id
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'count': count,
            'offset': offset,
        }

        response = self.http_client.execute('GET', '/v1/user/{}/followings'.format(user_id), params)

        return response

    def get_user_qr_code(self, user_id: str) -> Response:
        """
        :param user_id: user id
        :return: Response object
        """

        response = self.http_client.execute('GET', '/v1/user/{}/qr_code'.format(user_id))

        return response
