<!-- markdownlint-disable MD013 -->
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/mtokapi/tokapi-client/issues)
<!-- markdownlint-enable MD013 -->

The simple http client for [TokApi](https://rapidapi.com/Sonjik/api/tokapi-mobile-version) tiktok mobile API

## Installation

```shell
pip install tokapi-client
```

## Usage

```shell
# For RapidAPI
api = TokApi('YOUR_RAPID_API_KEY')

# For api.tokapi.online
api = TokApi('YOUR_API_KEY_FROM_DASHBOARD', base_url="https://api.tokapi.online")

# Let's find some users by search query with pagination
keyword = 'nike'
offset = 0
for i in range(0, 3):
    result = api.search_user_by_keyword(keyword, offset=offset)
    data = result.json()

    for user in data['user_list']:
        info = user['user_info']
        print('Nickname: {}, region: {}'.format(info['nickname'],
                                                info['region']))

    offset = data['cursor']
```

## Examples

You can find more complex usage examples in [examples](examples) folder

## Legal

This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by TikTok
or any of its affiliates or subsidiaries. This is an independent and unofficial API. Use at your own risk.