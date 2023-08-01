import requests

""" The parser for site 'https://wttr.in/san%20francisco?nTqu&lang=en' """

payload = {'n': '', 'T': '', 'q': '', 'M': '', 'lang': 'ru'}
url_tmp = 'https://wttr.in/{}'
url = url_tmp.format('SVO')
# url = url_tmp.format('london':cherepovets:SVO')

response = requests.get(url, params=payload)
response.raise_for_status()

print(response.text)

