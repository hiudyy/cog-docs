import requests
import os

API_KEY = os.getenv('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog2.cognima.com.br/api/v1'

def download_tiktok():
    url = f'{BASE_URL}/tiktok/download'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'url': 'https://www.tiktok.com/@user/video/1234567890'
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print('TikTok Video Info:')
        print(f"Title: {result['data']['title']}")
        print(f"Author: {result['data']['author']['username']}")
        print(f"Views: {result['data']['stats']['views']:,}")
        print(f"Likes: {result['data']['stats']['likes']:,}")
        print(f"\nDownload URLs:")
        for video in result['data']['urls']:
            print(f"{video['quality']}: {video['url']}")
    else:
        print(f"Error {response.status_code}: {response.json()}")

def search_tiktok():
    url = f'{BASE_URL}/tiktok/search'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'query': 'cooking recipes'
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print('Search results:')
        print(result['data'])
    else:
        print(f"Error {response.status_code}: {response.json()}")

if __name__ == '__main__':
    download_tiktok()
