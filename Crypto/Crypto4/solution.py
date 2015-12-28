__author__ = 'sduyazilim'

import base64

file = open("C:\Users\\arch\Downloads\\base", "r")

oku = file.read()
data = "sduyazilim_{"
num = 0
while (oku.startswith(data) != True):
    oku = base64.b64decode(oku)
    num = num + 1

print(oku)
print(num)
