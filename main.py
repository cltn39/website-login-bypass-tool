import hashlib
from pprint import pprint

import requests
from bs4 import BeautifulSoup

from config import username, password, targetUrl

def get_md5(s):
    return hashlib.md5(bytes(s, encoding='utf8')).hexdigest()

def main():
    url = targetUrl
    
    with requests.session() as session:
        response = session.get(url)
        
        md5_pass = get_md5(password) + ':'
        email = username + ':'

        soup = BeautifulSoup(response.text, 'lxml')
        challenge = soup.find('input', id='challange').get('value')

        result = email + md5_pass + challenge
        response = get_md5(result)

        data = {'username': username,
                'password': '',
                'challenge': '',
                'response': response
        }

        r_post = session.post(url, data=data)
        pprint(r_post.text)


        with open('index.html', 'w') as f:
            f.write(r_post.text)



if __name__ == '__main__':
    main()