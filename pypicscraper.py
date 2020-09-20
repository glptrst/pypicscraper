# take insta page url as input, print link to picture

import urllib.request
import re

user_input = input()

while True:
    try: 
        # make http request to get page content
        with urllib.request.urlopen(user_input) as response:
            html = response.read().decode('utf-8')
        # extract the link we want
        regex = re.compile(r'og:image.+content=".+').search(html).group()
        regex = re.compile(r'http.+\"').search(regex).group()
        print(regex[:len(regex)-1])
        break;
    except:
        user_input = input("Something's gone wrong...try again:\n")
        
