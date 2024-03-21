import sys

print(sys.path)

import re

text = "Mi numero de telefono es 6644759728, el codigo del pais es 52 mi numero de la suerte es 3"

result = re.findall('[0-9]+',text)
print(result)

import time

timestamp = time.time()
print(timestamp)
local = time.localtime()
result = time.asctime(local)

print(result)


import collections

numbers = [1,1,1,2,3,3,4,4,4,4,5]

counter = collections.Counter(numbers)

print(counter)
