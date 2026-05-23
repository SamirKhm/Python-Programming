# modules and pip

import math # built-in module
import random # built-in module
import mymodule # user-defined module
import requests # external module (needs to be installed with pip)

print(math.sqrt(16))
print(random.randint(1,10))
print(mymodule.hello())

print(requests.get("https://httpbin.org/get"))