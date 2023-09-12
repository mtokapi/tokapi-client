import json

from client.api import TokApi


def example(email: str, password: str, birthday: str, region: str, proxy: str):
    client = TokApi('YOUR_API_KEY', base_url="https://api.tokapi.online")

    initial_signup_response = client.email_signup(email, password, birthday, region, proxy)

    if initial_signup_response.status_code == 403:
        initial_signup_result = initial_signup_response.json()
        print('Need additional verification:\n{}'.format(initial_signup_result))

        print('\n Please enter a verification code from email: ')
        verification_code = input()

        signup_response = client.email_signup_check_code(email,
                                                         birthday,
                                                         verification_code,
                                                         json.dumps(initial_signup_result['device']),
                                                         initial_signup_result['cookie'],
                                                         proxy)

        if signup_response.status_code == 200:
            signup_data = signup_response.json()

            print('Successful signup')
            print()
            print('Please save cookie string:\n{}'.format(signup_data['cookie']))
            print()
            print('Please save device config:\n{}'.format(json.dumps(signup_data['device'])))
            print()
            print(
                "You can use cookie string and device config in requests which have 'x-cookie' and 'x-device' headers :)")

        else:
            print('Ooops, something wrong: {}'.format(initial_signup_response.text))

    elif initial_signup_response.status_code == 200:
        signup_data = initial_signup_response.json()

        print('Successful signup')
        print()
        print('Please save cookie string:\n {}'.format(signup_data['cookie']))
        print()
        print('Please save device config:\n{}'.format(json.dumps(signup_data['device'])))
        print()
        print("You can use cookie string and device config in requests which have 'x-cookie' and 'x-device' headers :)")
    else:
        print('Ooops, something wrong: {}'.format(initial_signup_response.text))


if __name__ == "__main__":
    example("email", "password_here", "1983-10-16", "GB", "proxy_string_here")
