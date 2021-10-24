import httpx


class TokApiClient(object):
    def __init__(self, api_key: str, rapid_host: str, proxy: httpx.Proxy = None):
        default_headers = {
            'x-rapidapi-host': rapid_host.replace('http://', '').replace('https://', ''),
            'x-rapidapi-key': api_key
        }
        self.http_client = httpx.Client(base_url=rapid_host, headers=default_headers, proxies=proxy)

    def execute(self, method: str, path: str, params: dict = None, headers: dict = None):
        return self.http_client.request(url=path, method=method, params=params, headers=headers)
