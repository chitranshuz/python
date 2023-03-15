import requests
import hashlib
import sys


def request_api_data(first5):
    url = 'https://api.pwnedpasswords.com/range/' + first5
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, please check the url')

    return res


def get_password_leak_count(response, tail):
    response = (line.split(':') for line in response.text.splitlines())
    for res, count in response:
        if res == tail:
            return count

    return 0


def pwned_api_check(input_pass):
    sha1password = hashlib.sha1(input_pass.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5)
    return get_password_leak_count(response, tail)


def main(args):
    for input_pass in args:
        count = pwned_api_check(input_pass)
        if count:
            print(f'{input_pass} was found {count} times, change it...')
        else:
            print(f'{input_pass} is good...:)')


if __name__ == '__main__':
    main(sys.argv[1:])
