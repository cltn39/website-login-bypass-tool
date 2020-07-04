import requests
import pprint

from config import username, password, targetUrl


def main():
    url = targetUrl
    
    with requests.session() as session:
        response = session.post(url, auth=(username, password))
        
        pprint(response.text)

        with open('index.html', 'w') as f:
            f.write(response.text)



if __name__ == '__main__':
    main()