import requests
import os

API_KEY = os.getenv('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog.api.br/api/v1'

def chat_completion():
    url = f'{BASE_URL}/completion'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'microsoft/phi-3-medium-128k-instruct',
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': 'What is artificial intelligence?'}
        ],
        'max_tokens': 500,
        'temperature': 0.7
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print('Success!')
        print(f"Model: {result['data']['model']}")
        print(f"Response: {result['data']['choices'][0]['message']['content']}")
        print(f"\nTokens used: {result['usage']['total_tokens']}")
        print(f"Cost: ${result['usage']['estimated_cost']:.6f}")
    else:
        print(f"Error {response.status_code}: {response.json()}")

if __name__ == '__main__':
    chat_completion()
