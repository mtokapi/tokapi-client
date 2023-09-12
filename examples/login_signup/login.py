import json

from client.api import TokApi


def example(login: str, password: str, region: str, proxy: str):
    client = TokApi('YOUR_API_KEY', base_url="https://api.tokapi.online")

    initial_login_response = client.email_login(login, password, region, proxy)

    if initial_login_response.status_code == 403:
        initial_login_result = initial_login_response.json()
        print('Need additional verification:\n{}'.format(initial_login_result))

        print('\n Please enter a verification code from email: ')
        verification_code = input()

        login_response = client.email_login_check_code(login,
                                                       password,
                                                       initial_login_result['verify_ticket'],
                                                       verification_code,
                                                       json.dumps(initial_login_result['device']),
                                                       initial_login_result['cookie'],
                                                       proxy)

        if login_response.status_code == 200:
            login_data = login_response.json()

            print('Successful login')
            print()
            print('Please save cookie string:\n{}'.format(login_data['cookie']))
            print()
            print('Please save device config:\n{}'.format(json.dumps(login_data['device'])))
            print()
            print("You can use cookie string and device config in requests which have 'x-cookie' and 'x-device' headers :)")

        else:
            print('Ooops, something wrong while login: {}'.format(initial_login_response.text))

    elif initial_login_response.status_code == 200:
        login_data = initial_login_response.json()

        print('Successful login')
        print()
        print('Please save cookie string:\n {}'.format(login_data['cookie']))
        print()
        print('Please save device config:\n{}'.format(json.dumps(login_data['device'])))
        print()
        print("You can use cookie string and device config in requests which have 'x-cookie' and 'x-device' headers :)")
    else:
        print('Ooops, something wrong: {}'.format(initial_login_response.text))


if __name__ == "__main__":
    example("username or email", "password_here", "GB or other country code", "proxy_string_here")
