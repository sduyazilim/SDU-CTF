__author__ = 'sduyazilim'

import requests

url = "http://sdeveci.com/sductf/"
headers = {'user-agent': 'SD-Browser'}
r = requests.get(url, headers=headers)

print(r.text)
