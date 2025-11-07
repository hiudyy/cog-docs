import requests
import os

API_KEY = os.getenv('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog2.cognima.com.br/api/v1'

def search_pinterest():
    url = f'{BASE_URL}/pinterest/search'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'query': 'modern interior design'
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print(f"Found {result['data']['count']} results")
        for i, item in enumerate(result['data']['results'][:5], 1):
            print(f"\n{i}. {item['title']}")
            print(f"   URL: {item['link']}")
    else:
        print(f"Error {response.status_code}: {response.json()}")

def download_pinterest():
    url = f'{BASE_URL}/pinterest/download'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'url': 'https://pinterest.com/pin/123456789/'
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print('Download info:')
        print(f"Title: {result['data']['title']}")
        for url_info in result['data']['urls']:
            print(f"{url_info['quality']}: {url_info['url']}")
    else:
        print(f"Error {response.status_code}: {response.json()}")

if __name__ == '__main__':
    search_pinterest()
