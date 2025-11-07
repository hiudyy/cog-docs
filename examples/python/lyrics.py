import requests
import os

API_KEY = os.getenv('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog2.cognima.com.br/api/v1'

def search_lyrics():
    url = f'{BASE_URL}/lyrics/search'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'query': 'bohemian rhapsody queen'
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print(f"Song: {result['data']['title']}")
        print(f"Artist: {result['data']['artist']}")
        print(f"Album: {result['data']['album']}")
        print(f"Year: {result['data']['year']}")
        print(f"\nLyrics:\n{result['data']['lyrics'][:500]}...")
    else:
        print(f"Error {response.status_code}: {response.json()}")

if __name__ == '__main__':
    search_lyrics()
