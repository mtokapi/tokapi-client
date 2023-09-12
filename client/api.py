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

        return self.http_client.execute('GET', '/v1/category', params)

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

        return self.http_client.execute('GET', '/v1/feed/recommended', params=params, headers=headers)

    def get_hashtag_info_by_id(self, hashtag_id: str) -> Response:
        """
        :param hashtag_id: hashtag id
        :return: Response object
        """

        return self.http_client.execute('GET', f'/v1/hashtag/{hashtag_id}')

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

        return self.http_client.execute('GET', f'/v1/hashtag/posts/{hashtag_id}', params)

    def get_music_info_by_id(self, music_id: str) -> Response:
        """
        :param music_id: music id
        :return: Response object
        """

        return self.http_client.execute('GET', f'/v1/music/{music_id}')

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

        return self.http_client.execute('GET', f'/v1/music/posts/{music_id}', params)

    def get_video_info_by_id(self, video_id: str, region: str = 'GB') -> Response:
        """
        :param video_id: video id
        :param region: alpha-2 country code
        :return: Response object
        """

        params = {
            'region': region,
        }

        return self.http_client.execute('GET', f'/v1/post/{video_id}', params)

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

        return self.http_client.execute('GET', '/v1/post', params)

    def get_video_comments(self, video_id: str, count: int = 20, offset: int = 0) -> Response:
        """
        :param video_id: video id
        :param count: number of items, a maximum value is 20
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'count': count,
            'offset': offset,
        }

        return self.http_client.execute('GET', f'/v1/post/{video_id}/comments', params)

    def get_video_comment_replies(self, video_id: str, comment_id: str, count: int = 20, offset: int = 0) -> Response:
        """
        :param video_id: video id
        :param comment_id: comment id
        :param count: number of items, a maximum value is 20
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'count': count,
            'offset': offset,
        }

        return self.http_client.execute('GET', f'/v1/post/{video_id}/comment/{comment_id}/replies', params)

    def get_user_videos(self, user_id: str, region: str = 'GB', with_pinned_posts: int = 1, count: int = 20,
                        offset: int = 0) -> Response:
        """
        :param user_id: tiktok user id
        :param region: alpha-2 country code
        :param with_pinned_posts: add pinned posts in response
        :param count: number of items, a maximum value is 20
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'region': region,
            'with_pinned_posts': with_pinned_posts,
            'count': count,
            'offset': offset,
        }

        return self.http_client.execute('GET', f'/v1/post/user/{user_id}/posts', params)

    def get_user_videos_by_different_ids(self,
                                         user_id: str = None,
                                         sec_user_id: str = None,
                                         username: str = None,
                                         region: str = 'GB',
                                         with_pinned_posts: int = 1,
                                         count: int = 20,
                                         offset: int = 0) -> Response:
        """
        :param user_id: tiktok user id
        :param sec_user_id: tiktok sec user id
        :param username: tiktok user uniq id
        :param region: alpha-2 country code
        :param with_pinned_posts: add pinned posts in response
        :param count: number of items, a maximum value is 20
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'region': region,
            'with_pinned_posts': with_pinned_posts,
            'count': count,
            'offset': offset,
        }

        if user_id:
            params['user_id'] = user_id
        elif sec_user_id:
            params['sec_user_id'] = sec_user_id
        elif username:
            params['username'] = username

        return self.http_client.execute('GET', f'/v1/post/user/posts', params)

    def get_user_liked_videos(self, user_id: str, count: int = 20, offset: int = 0) -> Response:
        """
        :param user_id: tiktok user id
        :param count: number of items, a maximum value is 20
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'count': count,
            'offset': offset,
        }

        return self.http_client.execute('GET', f'/v1/post/user/{user_id}/liked_posts', params)

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

        return self.http_client.execute('GET', f'/v1/post/{video_id}/comments', params)

    def search_user_by_keyword(self,
                               keyword: str,
                               follower_count: str = None,
                               profile_type: str = None,
                               other_pref: str = None,
                               count: int = 10,
                               offset: int = 0) -> Response:
        """
        :param keyword: search text query
        :param follower_count: filter by followers count, can be empty or one of: ZERO_TO_ONE_K (0 to 1k), ONE_K_TO_TEN_K (1k to 10k), TEN_K_TO_ONE_H_K(10k to 100k), ONE_H_K_PLUS(100k+)
        :param profile_type: filter by user profile type, can be empty or one of: VERIFIED
        :param other_pref: filter by other preference, can be empty or one of: USERNAME (keyword usage in username)
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'follower_count': follower_count,
            'profile_type': profile_type,
            'other_pref': other_pref,
            'keyword': keyword,
            'count': count,
            'offset': offset,
        }

        return self.http_client.execute('GET', '/v1/search/user', params)

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

        return self.http_client.execute('GET', '/v1/search/hashtag', params)

    def search_music_by_keyword(self,
                                keyword: str,
                                filter_by: int = None,
                                sort_type: int = None,
                                count: int = 10,
                                offset: int = 0) -> Response:
        """
        :param keyword: search text query
        :param filter_by: filter by type, can be empty or one of: 0 - All, 1 - Title, 2 - Creators
        :param sort_type: sort type, can be empty or one of: 0 - Relevance, 1 - Most used, 2 - Most recent, 3 - Shortest, 4 - Longest
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'keyword': keyword,
            'filter_by': filter_by,
            'sort_type': sort_type,
            'count': count,
            'offset': offset,
        }

        return self.http_client.execute('GET', '/v1/search/music', params)

    def search_videos_by_keyword(self,
                                 keyword: str,
                                 sort_type: int = None,
                                 publish_time: int = None,
                                 count: int = 10,
                                 offset: int = 0) -> Response:
        """
        :param keyword: search text query
        :param sort_type: sort type, can be empty or one of: 1 - Most liked, 0 - Relevance
        :param publish_time: date posted filter, can be empty or one of: 0 - All time, 1 - Yesterday, 7 - This week, 30 - This month, 90 - Last 3 months, 180 - Last 6 months
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'keyword': keyword,
            'sort_type': sort_type,
            'publish_time': publish_time,
            'count': count,
            'offset': offset,
        }

        return self.http_client.execute('GET', '/v1/search/post', params)

    def search_live_streams_by_keyword(self,
                                       keyword: str,
                                       count: int = 10,
                                       offset: int = 0) -> Response:
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

        return self.http_client.execute('GET', '/v1/search/live', params)

    def search_locations_by_keyword(self,
                                    keyword: str,
                                    count: int = 10,
                                    offset: int = 0) -> Response:
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

        return self.http_client.execute('GET', '/v1/search/location', params)

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

        return self.http_client.execute('GET', f'/v1/sticker/posts/{effect_id}', params)

    def get_effect_info_by_id(self, effect_id: str) -> Response:
        """
        :param effect_id: effect id
        :return: Response object
        """

        return self.http_client.execute('GET', f'/v1/sticker/{effect_id}')

    def get_effect_info_by_ids(self, effect_ids: list) -> Response:
        """
        :param effect_ids: effect ids
        :return: Response object
        """

        params = {
            'sticker_ids': ','.join(effect_ids)
        }

        return self.http_client.execute('GET', '/v1/sticker', params)

    def get_user_info_by_id(self, user_id: str) -> Response:
        """
        :param user_id: user id
        :return: Response object
        """

        return self.http_client.execute('GET', f'/v1/user/{user_id}')

    def get_user_info_by_different_ids(self,
                                       user_id: str = None,
                                       sec_user_id: str = None,
                                       username: str = None) -> Response:
        """
        :param user_id: user id
        :param sec_user_id: sec user id
        :param username: user unique id
        :return: Response object
        """

        params = {}
        if user_id:
            params['user_id'] = user_id
        elif sec_user_id:
            params['sec_user_id'] = sec_user_id
        elif username:
            params['username'] = username

        return self.http_client.execute('GET', '/v1/user/', params=params)

    def get_user_identifiers(self, user_id: str) -> Response:
        """
        :param user_id: user id
        :return: Response object
        """

        return self.http_client.execute('GET', f'/v1/user/username/{user_id}')

    def get_user_followers(self, user_id: str, ids_only: int = 0, count: int = 20, offset: int = 0) -> Response:
        """
        :param user_id: user id
        :param ids_only: if 1 then return only follower identifiers
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'ids_only': ids_only,
            'count': count,
            'offset': offset
        }

        return self.http_client.execute('GET', f'/v1/user/{user_id}/followers', params)

    def get_user_followings(self, user_id: str, ids_only: int = 0, count: int = 20, offset: int = 0) -> Response:
        """
        :param user_id: user id
        :param ids_only: if 1 then return only follower identifiers
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'ids_only': ids_only,
            'count': count,
            'offset': offset,
        }

        return self.http_client.execute('GET', f'/v1/user/{user_id}/followings', params)

    def get_user_playlists(self, user_id: str, offset: int = 0) -> Response:
        """
        :param user_id: user id
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'offset': offset,
        }

        return self.http_client.execute('GET', f'/v1/user/{user_id}/playlist', params)

    def get_user_playlist_info(self, user_id: str, playlist_id: str) -> Response:
        """
        :param user_id: user id
        :param playlist_id: playlist id
        :return: Response object
        """

        return self.http_client.execute('GET', f'/v1/user/{user_id}/playlist/{playlist_id}')

    def get_user_playlist_videos(self, user_id: str, playlist_id: str, offset: int = 0) -> Response:
        """
        :param user_id: user id
        :param playlist_id: playlist id
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'offset': offset,
        }

        return self.http_client.execute('GET', f'/v1/user/{user_id}/playlist/{playlist_id}/videos', params=params)

    def get_user_qr_code(self, user_id: str) -> Response:
        """
        :param user_id: user id
        :return: Response object
        """

        return self.http_client.execute('GET', f'/v1/user/{user_id}/qr_code')

    def sign_request(self, url: str, headers: dict):
        """
        :param url: request url with query parameters
        :param headers: all request headers
        :return: Response object
        """

        body = {
            'url': url,
            'headers': headers,
        }

        return self.http_client.execute('POST', '/v1/service/sign', body_data=body)

    def generate_device(self, region: str, proxy: str = None):
        """
        :param region: alpha-2 country code
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        body = {
            'region': region,
        }

        headers = {
            'x-proxy': proxy
        }

        return self.http_client.execute('POST', '/v1/service/device/generate', headers=headers, body_data=body)

    def get_location_by_id(self, location_id: str) -> Response:
        """
        :param location_id: location id
        :return: Response object
        """

        return self.http_client.execute('GET', f'/v1/location/{location_id}')

    def get_videos_by_location_id(self, location_id: str, region: str = 'GB', count: int = 20,
                                  offset: int = 0) -> Response:
        """
        :param location_id: location id
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

        return self.http_client.execute('GET', f'/v1/location/posts/{location_id}', params=params)

    def get_shop_homepage(self, region: str) -> Response:
        """
        :param region: alpha-2 country code
        :return: Response object
        """

        params = {
            'region': region,
        }

        return self.http_client.execute('GET', f'/v1/shop/homepage', params=params)

    def get_shop_products_from_user_shop_tab(self, user_id: str, region: str, count: int = 20,
                                             offset: int = 0) -> Response:
        """
        :param user_id: user sec id
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

        return self.http_client.execute('GET', f'/v1/shop/products/{user_id}', params=params)

    def get_seller_available_tabs_on_detail_page(self, user_id: str, region: str) -> Response:
        """
        :param user_id: user sec id
        :param region: alpha-2 country code
        :return: Response object
        """

        params = {
            'region': region,
        }

        return self.http_client.execute('GET', f'/v1/shop/products/{user_id}/tab_list', params=params)

    def get_seller_detail_page(self, user_id: str, region: str, tab_id: int = 1, count: int = 20,
                               offset: int = 0) -> Response:
        """
        :param user_id: user sec id
        :param region: alpha-2 country code
        :param tab_id: you can get 'tab id' from '/v1/shop/products/{user id}/tab_list' response'
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'region': region,
            'tab_id': tab_id,
            'count': count,
            'offset': offset,
        }

        return self.http_client.execute('GET', f'/v1/shop/products/{user_id}/detail_page', params=params)

    def get_shop_product_info_by_id(self, product_id: str, region: str) -> Response:
        """
        :param product_id: product id
        :param region: alpha-2 country code
        :return: Response object
        """

        params = {
            'region': region,
        }

        return self.http_client.execute('GET', f'/v1/shop/product/{product_id}', params=params)

    def get_shop_product_reviews(self, product_id: str, region: str, sort_type: int = 1, filter_id: str = None,
                                 count: int = 20, offset: int = 0) -> Response:
        """
        :param product_id: product id
        :param region: alpha-2 country code
        :param sort_type: 1 - Sort by Relevance, 2 - Sort by Recent
        :param filter_id: value from data.review_filters[].filter_id
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'region': region,
            'sort_type': sort_type,
            'filter_id': filter_id,
            'count': count,
            'offset': offset,
        }

        return self.http_client.execute('GET', f'/v1/shop/product/{product_id}/reviews', params=params)

    def get_shop_recommended_products(self, region: str, exposure_item_list: list = None, tab_id: int = 0,
                                      session_id: str = None, count: int = 20, offset: int = 0) -> Response:
        """
        :param region: alpha-2 country code
        :param exposure_item_list: the list of viewed products, which will be excluded from feed list
        :param tab_id: you can get tab_id from 'homepage' request under 'data.feed_data.tabs'
        :param session_id: you can get session id from 'homepage' request under 'data.feed data.session id'
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        if exposure_item_list is None:
            exposure_item_list = []

        params = {
            'region': region,
            'count': count,
            'offset': offset,
        }

        body = {
            'exposure_item_list': exposure_item_list,
            'tab_id': tab_id,
            'session_id': session_id,
        }

        return self.http_client.execute('POST', '/v1/shop/recommended_products', params=params, body_data=body)

    def get_shop_new_user_exclusive_deals(self, region: str, session_id: str = None, main_tab_id: str = None,
                                          sub_tab_id: str = None,
                                          tab_type: str = None, count: int = 20, offset: int = 0) -> Response:
        """
        :param region: alpha-2 country code
        :param session_id: you can get 'session_id' from 'data.session_id'
        :param main_tab_id: you can get 'main_tab_id' from 'data.main_tab_list[].main_tab_id'
        :param sub_tab_id: you can get 'sub_tab_id' from 'data.main_tab_list[].tab_list[].sub_tab_id'
        :param tab_type: you can get 'tab_type' from 'data.main_tab_list[].tab_type'
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'region': region,
            'session_id': session_id,
            'main_tab_id': main_tab_id,
            'sub_tab_id': sub_tab_id,
            'tab_type': tab_type,
            'count': count,
            'offset': offset,
        }

        return self.http_client.execute('GET', '/v1/shop/new_user_exclusive_deal', params=params)

    def get_shop_flash_sale(self, region: str, session_id: str = None, event_id: str = None,
                            tab_id: str = None, count: int = 20, offset: int = 0) -> Response:
        """
        :param region: alpha-2 country code
        :param session_id: you can get 'session_id' from 'data.event_tab_list[].session_id'
        :param event_id: you can get 'event_id' from 'data.event_tab_list[].event_id'
        :param tab_id: you can get 'tab_id' from 'data.event_tab_list[].tab_list[].tab_id'
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """
        params = {
            'region': region,
            'session_id': session_id,
            'event_id': event_id,
            'tab_id': tab_id,
            'count': count,
            'offset': offset,
        }

        return self.http_client.execute('GET', '/v1/shop/flash_sale', params=params)

    def search_shop_products(self, keyword: str, region: str, sort_by: str = "PRICE_ASC", filters_data: str = "",
                             count: int = 20, offset: int = 0) -> Response:
        """
        :param keyword: query text
        :param region: alpha-2 country code
        :param sort_by: sort types, possible values: PRICE_ASC, PRICE_DESC, BEST_SELLERS, RELEVANCE
        :param filters_data: All available filters can be found under "filter_groups" field from response.
            The "filters_data" value must be JSON array in format: [{simple filter button},{range/multiple select},
            and more filters]. Example for {simple filter button} - {"type": 2, "value": "true"}.
            Example for {range/multiple select} - {"type":8, "value_list": ["1,1000"]}. Full example with filter by
            "price" and "4 Stars & Up": [{"type": 2, "value": "true"},{"type":8, "value_list": ["1,1000"]}]
        :param count: number of items
        :param offset: number of item which will be skipped from start
        :return: Response object
        """

        params = {
            'keyword': keyword,
            'region': region,
            'sort_by': sort_by,
            'filters_data': filters_data,
            'count': count,
            'offset': offset,
        }

        return self.http_client.execute('GET', '/v1/shop/search', params=params)

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

        return self.http_client.execute('POST', '/v1/passport/email/login', body_data=body, headers=headers)

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

        return self.http_client.execute('POST', '/v1/passport/email/login/check_code', headers=headers, body_data=body)

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

        return self.http_client.execute('POST', '/v1/passport/email/signup', body_data=body, headers=headers)

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

        return self.http_client.execute('POST', '/v1/passport/email/signup/check_code', headers=headers, body_data=body)

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

        return self.http_client.execute('POST', '/v1/mssdk/decode', body_data=body)

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

        return self.http_client.execute('POST', '/v1/mssdk/encode', body_data=body)

    def mssdk_get_token(self, device_config: str, cookie: str, proxy: str) -> Response:
        """
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }
        return self.http_client.execute('GET', '/v1/mssdk/get_token', headers=headers)

    def mssdk_send_ri_report(self, report_type: str, device_config: str, cookie: str, proxy: str) -> Response:
        """
        :param report_type: report type can be `install`, `cold_start` and `autoReport`
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        params = {
            "report_type": report_type
        }

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        return self.http_client.execute('POST', '/v1/mssdk/send_report', params=params, headers=headers)

    def like_video_by_id(self, video_id: str, device_config: str, cookie: str, proxy: str) -> Response:
        """
        :param video_id: video id
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        return self.http_client.execute('POST', f'/v1/post/like/{video_id}', headers=headers)

    def unlike_video_by_id(self, video_id: str, device_config: str, cookie: str, proxy: str) -> Response:
        """
        :param video_id: video id
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        return self.http_client.execute('POST', f'/v1/post/unlike/{video_id}', headers=headers)

    def follow_user_by_id(self, user_id: str, device_config: str, cookie: str, proxy: str) -> Response:
        """
        :param user_id: user id
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        return self.http_client.execute('POST', f'/v1/user/follow/{user_id}', headers=headers)

    def unfollow_user_by_id(self, user_id: str, device_config: str, cookie: str, proxy: str) -> Response:
        """
        :param user_id: user id
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        return self.http_client.execute('POST', f'/v1/user/unfollow/{user_id}', headers=headers)

    def update_user_profile(self, user_id: str, profile_fields: dict, device_config: str, cookie: str,
                            proxy: str) -> Response:
        """
        :param user_id: user id
        :param profile_fields: dictionary with user profile fields
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        body = {
            'profile': profile_fields
        }

        return self.http_client.execute('POST', f'/v1/user/{user_id}/profile', body_data=body, headers=headers)

    def update_username(self, user_id: str, username: str, device_config: str, cookie: str, proxy: str) -> Response:
        """
        :param user_id: user id
        :param username: user unique id
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        body = {
            'username': username
        }

        return self.http_client.execute('POST', f'/v1/user/{user_id}/username', body_data=body, headers=headers)

    def enable_business_account(self, category_id: str, category_name: str, device_config: str,
                                cookie: str, proxy: str) -> Response:
        """
        :param category_id: category id
        :param category_name: category name
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        body = {
            'settings': {
                'category_id': category_id,
                'category_name': category_name,
            }
        }

        return self.http_client.execute('POST', '/v1/user/business_account/enable', body_data=body, headers=headers)

    def disable_business_account(self, device_config: str, cookie: str, proxy: str) -> Response:
        """
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        return self.http_client.execute('POST', '/v1/user/business_account/disable', headers=headers)

    def get_logged_in_user_info(self, device_config: str, cookie: str, proxy: str) -> Response:
        """
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        return self.http_client.execute('GEt', '/v1/user/self', headers=headers)

    def login_token_beat(self, device_config: str, cookie: str, proxy: str) -> Response:
        """
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        return self.http_client.execute('GET', '/v1/passport/token/beat', headers=headers)

    def publish_comment(self, post_id: str, text: str, user_ids: dict, device_config: str,
                        cookie: str, proxy: str) -> Response:
        """
        :param post_id: post id
        :param text: comment text
        :param user_ids: if comment text contains user mentions then you should provide usernames to user ids mapping
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        body = {
            'text': text,
            'user_ids': user_ids,
        }

        return self.http_client.execute('POST', f'v1/comment/publish/{post_id}', body_data=body, headers=headers)

    def delete_comment(self, comment_id: str, device_config: str, cookie: str, proxy: str) -> Response:
        """
        :param comment_id: comment id
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        return self.http_client.execute('POST', f'v1/comment/delete/{comment_id}', headers=headers)

    def like_comment(self, post_id: str, comment_id: str, device_config: str,
                     cookie: str, proxy: str) -> Response:
        """
        :param post_id: post id
        :param comment_id: comment id
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        return self.http_client.execute('POST', f'v1/comment/like/{comment_id}/{post_id}', headers=headers)

    def unlike_comment(self, post_id: str, comment_id: str, device_config: str,
                       cookie: str, proxy: str) -> Response:
        """
        :param post_id: post id
        :param comment_id: comment id
        :param device_config: JSON string with device configuration
        :param cookie: cookie string
        :param proxy: http, https, socks4 or socks5 proxy
        :return: Response object
        """

        headers = {
            'x-device': device_config,
            'x-cookie': cookie,
            'x-proxy': proxy
        }

        return self.http_client.execute('POST', f'v1/comment/unlike/{comment_id}/{post_id}', headers=headers)
