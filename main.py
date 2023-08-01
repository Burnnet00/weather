import requests

""" The parser for site 'https://wttr.in/san%20francisco?nTqu&lang=en' """

payload = {'lang': 'en'} #'n': 'Tqu',
url_tmp = 'https://wttr.in/{}'
url = url_tmp.format('SVO')
# url_tmp = url.format('san%20francisco')
# url = url_tmp.format('london')
# url = url_tmp.format('cherepovets')
# url = url_tmp.format('SVO')
response = requests.get(url, params=payload)
response.raise_for_status()

print(response.text)

# https://wttr.in/san%20francisco?nTqu&lang=en
# https://wttr.in/san%20francisco?n=Tqu&lang=en 2=




