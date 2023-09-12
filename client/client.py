import requests


class TokApiClient(object):
    def __init__(self, api_key: str, base_url: str, proxy: str = None):
        self.base_url = base_url
        self.default_headers = {
            'x-rapidapi-host': base_url.replace('http://', '').replace('https://', ''),
            'x-rapidapi-key': api_key,
            'x-api-key': api_key,
            'x-project-name': 'tokapi',
        }

        self.http_client = requests.Session()
        if proxy:
            self.http_client.proxies.update({
                'http': proxy,
                'https': proxy
            })

    def execute(self, method: str, path: str, params: dict = None, headers: dict = None, body_data: dict = None):
        if headers is None:
            headers = {}

        headers.update(self.default_headers)

        return self.http_client.request(url=f'{self.base_url}{path}',
                                        method=method,
                                        params=params,
                                        headers=headers,
                                        json=body_data)
