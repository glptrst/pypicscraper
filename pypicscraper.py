# take insta page url as input, print link to picture

import urllib.request
import re
#from bs4 import BeautifulSoup

# get input (url) from user
user_input = input()

print(user_input)

# check input

# make http request to get page content
with urllib.request.urlopen(user_input) as response:
    html = response.read().decode('utf-8')

# extract the link we want
regex = re.compile(r'og:image.+content=".+').search(html).group()
regex = re.compile(r'http.+\"').search(regex).group()

print(regex[:len(regex)-1])
