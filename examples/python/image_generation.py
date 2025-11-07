import requests
import os

API_KEY = os.getenv('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog2.cognima.com.br/api/v1'

def generate_image():
    url = f'{BASE_URL}/generate'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'deepimg',
        'prompt': 'A beautiful sunset over mountains, highly detailed',
        'size': '1024x1024',
        'quality': 'hd'
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print('Image generated successfully!')
        print(f"URL: {result['data']['data'][0]['url']}")
        print(f"Cost: ${result['usage']['estimated_cost']:.6f}")
    else:
        print(f"Error {response.status_code}: {response.json()}")

if __name__ == '__main__':
    generate_image()
