import requests


def main():
    """ The parser for site 'https://wttr.in/san%20francisco?nTqu&lang=en' """

    payload = {'n': '', 'T': '', 'q': '', 'M': '', 'lang': 'ru'}
    tmp_url = 'https://wttr.in/{}'
    cities = ['london', 'cherepovets', 'SVO']

    for city in cities:
        url = tmp_url.format(city)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()