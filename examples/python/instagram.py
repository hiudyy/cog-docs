import requests
import os

API_KEY = os.getenv('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog2.cognima.com.br/api/v1'

def download_instagram():
    url = f'{BASE_URL}/instagram/download'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'url': 'https://www.instagram.com/p/ABC123xyz/'
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print('Instagram Post Info:')
        print(f"Type: {result['data']['type']}")
        print(f"Caption: {result['data']['caption']}")
        print(f"Author: {result['data']['author']['username']}")
        print(f"Likes: {result['data']['likes']:,}")
        print(f"\nMedia URLs:")
        for i, media in enumerate(result['data']['media'], 1):
            print(f"{i}. {media['type']}: {media['url']}")
    else:
        print(f"Error {response.status_code}: {response.json()}")

if __name__ == '__main__':
    download_instagram()
