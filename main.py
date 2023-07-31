import requests

""" The parser for cite 'https://wttr.in/san%20francisco?nTqu&lang=en' """

payload = {'san%20francisco?nTqu&lang': 'en'}
url = 'https://wttr.in'
response = requests.get(url, params=payload)
response.raise_for_status()

print(response.text)
