__author__ = 'sduyazilim'

import requests

res  = requests.get("http://107.170.76.50/static/uploads/d1b184140edbf1fc354c2464d1d7d88e/sx.txt")
con = res.content
bad_character = "+:`#',@.; "
flag = ""
for char in con:
    if char not in bad_character:
        flag += char
print flag.split()
