from client.api import TokApi
from examples.constants import API_KEY, BASE_URL


def example(user_id: str):
    """
    Print user info
    """
    api = TokApi(API_KEY, BASE_URL)

    result = api.get_user_info_by_id(user_id)
    data = result.json()

    info = data['user']
    print('Nickname: {}, video count: {}, followers: {}'.format(info['nickname'],
                                                                info['aweme_count'],
                                                                info['follower_count']))


def example_qr_code(user_id: str):
    """
    Print user info
    """
    api = TokApi(API_KEY, BASE_URL)

    result = api.get_user_qr_code(user_id)
    data = result.json()

    print('QR code link: {}'.format(data['qrcode_url']['url_list'][1]))


if __name__ == "__main__":
    example('6784563164518679557')
    example('MS4wLjABAAAA0nDSqs_RbIwdxHKDTT3Il0MsEo1pvx4-fG6czO7rtP_3rWk1OzqViPk6ACM4hhv1')
    example_qr_code('6784563164518679557')
