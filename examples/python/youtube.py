import requests
import os
import base64

API_KEY = os.getenv('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog2.cognima.com.br/api/v1'

def search_youtube():
    url = f'{BASE_URL}/youtube/search'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'query': 'python programming tutorial'
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print(f"Found {result['data']['count']} results\n")
        for i, video in enumerate(result['data']['results'][:5], 1):
            print(f"{i}. {video['title']}")
            print(f"   Channel: {video['channel']['name']}")
            print(f"   Views: {video['views']:,}")
            print(f"   URL: {video['url']}\n")
    else:
        print(f"Error {response.status_code}: {response.json()}")

def download_mp3():
    url = f'{BASE_URL}/youtube/mp3'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print('Audio downloaded!')
        print(f"Title: {result['data']['title']}")
        print(f"Duration: {result['data']['duration']}s")
        print(f"Filename: {result['data']['filename']}")
        
        # Save file
        audio_data = base64.b64decode(result['data']['buffer'])
        with open(result['data']['filename'], 'wb') as f:
            f.write(audio_data)
        print(f"Saved to {result['data']['filename']}")
    else:
        print(f"Error {response.status_code}: {response.json()}")

def download_mp4():
    url = f'{BASE_URL}/youtube/mp4'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
        'quality': '720p'
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print('Video downloaded!')
        print(f"Title: {result['data']['title']}")
        print(f"Quality: {result['data']['quality']}")
    else:
        print(f"Error {response.status_code}: {response.json()}")

if __name__ == '__main__':
    search_youtube()
