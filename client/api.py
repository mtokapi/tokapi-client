from requests import Response

from client.client import TokApiClient


class TokApi(object):
    def __init__(self, api_key: str, base_url: str = 'https://tokapi-mobile-version.p.rapidapi.com',
                 proxy: str = None):
        self.http_client = TokApiClient(api_key=api_key, base_url=base_url, proxy=proxy)

    def get_categories(self, count: int = 10, offset: int = 0, region: str = 'US') -> Response:
        """
        :param count: number of items, a maximum value is 50
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

        response = self.http_client.execute('GET', f'/v1/hashtag/{hashtag_id}')

        return response

    def get_videos_by_hashtag_id(self, hashtag_id: str, region: str = 'GB', count: int = 20,
                                 offset: int = 0) -> Response:
        """
        :param hashtag_id: hashtag id
        :param region: alpha-2 country code
        :param count: number of items, a maximum value is 20
        :param offset: number of item which will be skipped from start
        :return: Response object
        """
        params = {
            'region': region,
            'count': count,
            'offset': offset,
        }

        response = self.http_client.execute('GET', f'/v1/hashtag/posts/{hashtag_id}', params)

        return response

    def get_music_info_by_id(self, music_id: str) -> Response:
        """
        :param music_id: music id
        :return: Response object
        """

        response = self.http_client.execute('GET', f'/v1/music/{music_id}')

        return response

    def get_videos_by_music_id(self, music_id: str, region: str = 'GB', count: int = 20, offset: int = 0) -> Response:
        """
        :param music_id: music id
        :param region: alpha-2 country code
        :param count: number of items, a maximum value is 20
        :param offset: number of item which will be skipped from start
        :return: Response object
        """
        params = {
            'region': region,
            'count': count,
            'offset': offset,
        }

        response = self.http_client.execute('GET', f'/v1/music/posts/{music_id}', params)

        return response

    def get_video_info_by_id(self, video_id: str, region: str = 'GB') -> Response:
        """
        :param video_id: video id
        :param region: alpha-2 country code
        :return: Response object
        """

        params = {
            'region': region,
        }

        response = self.http_client.execute('GET', f'/v1/post/{video_id}', params)

        return response

    def get_video_info_by_web_link(self, video_web_link: str, region: str = 'GB') -> Response:
        """
        :param video_web_link: video web link
        :param region: alpha-2 country code
        :return: Response object
        """

        params = {
            'video_url': video_web_link,
            'region': region,
        }

        response = self.http_client.execute('GET', '/v1/post', params)

        return response

    def get_user_videos(self, user_id: str, region: str = 'GB', count: int = 20, offset: int = 0) -> Response:
        """
        :param user_id: tiktok user id
        :param region: alpha-2 country code
        :param count: number of items, a maximum value is 20
        :param offset: number of item which will be skipped from start
        :return: Response object
        """
        params = {
            'region': region,
            'count': count,
            'offset': offset,
        }

        response = self.http_client.execute('GET', f'/v1/post/user/{user_id}/posts', params)

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

        response = self.http_client.execute('GET', f'/v1/post/{video_id}/comments', params)

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

    def get_videos_by_effect_id(self, effect_id: str, region: str = 'GB', count: int = 20, offset: int = 0) -> Response:
        """
        :param effect_id: effect id
        :param region: alpha-2 country code
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """
        params = {
            'region': region,
            'count': count,
            'offset': offset,
        }

        response = self.http_client.execute('GET', f'/v1/sticker/posts/{effect_id}', params)

        return response

    def get_effect_info_by_id(self, effect_id: str) -> Response:
        """
        :param effect_id: effect id
        :return: Response object
        """

        response = self.http_client.execute('GET', f'/v1/sticker/{effect_id}')

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

        response = self.http_client.execute('GET', f'/v1/user/{user_id}')

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

        response = self.http_client.execute('GET', f'/v1/user/{user_id}/followers', params)

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

        response = self.http_client.execute('GET', f'/v1/user/{user_id}/followings', params)

        return response

    def get_user_qr_code(self, user_id: str) -> Response:
        """
        :param user_id: user id
        :return: Response object
        """

        response = self.http_client.execute('GET', f'/v1/user/{user_id}/qr_code')

        return response

    def email_login(self, login: str, password: str, region: str, proxy: str) -> Response:
        """
        :param login: email or username
        :param password: password
        :param region: alpha-2 country code
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        body = {
            "email": login,
            "password": password
        }

        headers = {
            'x-proxy': proxy,
            'x-region': region,
        }

        return self.http_client.execute('POST',
                                        '/v1/passport/email/login',
                                        body_data=body,
                                        headers=headers)

    def email_login_check_code(self, login: str, password: str, verify_ticket: str, code: str, device_config: str,
                               cookie: str, proxy: str) -> Response:
        """
        :param login: email or username
        :param password: password
        :param verify_ticket: value from 'email_login' response
        :param code: code from email message
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        body = {
            "email": login,
            "password": password,
            "verify_ticket": verify_ticket,
            "code": code,
        }

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        return self.http_client.execute('POST',
                                        '/v1/passport/email/login/check_code',
                                        headers=headers,
                                        body_data=body)

    def email_signup(self, email: str, password: str, birthday: str, region: str, proxy: str) -> Response:
        """
        :param email: email
        :param password: password
        :param birthday: birthday in format YYYY-MM-D, example: 1983-10-16
        :param region: alpha-2 country code
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        body = {
            "email": email,
            "password": password,
            "birthday": birthday,
        }

        headers = {
            'x-proxy': proxy,
            'x-region': region,
        }

        return self.http_client.execute('POST',
                                        '/v1/passport/email/signup',
                                        body_data=body,
                                        headers=headers)

    def email_signup_check_code(self, email: str, birthday: str, code: str, device_config: str, cookie: str,
                                proxy: str) -> Response:
        """
        :param email: email
        :param code: code from email message
        :param birthday: birthday in format YYYY-MM-D, example: 1983-10-16
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        body = {
            "email": email,
            "birthday": birthday,
            "code": code
        }

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        return self.http_client.execute('POST',
                                        '/v1/passport/email/signup/check_code',
                                        headers=headers,
                                        body_data=body)

    def mssdk_decode(self, payload: str, mode: str = 'full') -> Response:
        """
        :param payload: encoded bytes in hex format
        :param mode: decode mode, can be 'full' or 'raw'
        :return: Response object
        """

        body = {
            "payload": payload,
            "mode": mode
        }

        return self.http_client.execute('POST',
                                        '/v1/mssdk/decode',
                                        body_data=body)

    def mssdk_encode(self, payload: str, payload_type: str) -> Response:
        """
        :param payload: encoded bytes in hex format
        :param payload_type: type of protobuf message, can be:
            'sdi/get_token' - get token payload
            'ri/report' - report payload
            'ms/get_seed' - seed payload
            'raw' - use this one if you want to just encrypt without padding and zipping
        :return: Response object
        """

        body = {
            "payload": payload,
            "payload_type": payload_type
        }

        return self.http_client.execute('POST',
                                        '/v1/mssdk/encode',
                                        body_data=body)
