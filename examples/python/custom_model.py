import requests
import os

API_KEY = os.getenv('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog.api.br/api/v1'

def create_custom_model():
    url = f'{BASE_URL}/custom'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'name': 'python-mentor',
        'display_name': 'Python Programming Mentor',
        'description': 'Expert Python programming assistant',
        'personality_summary': 'You are an expert Python programmer with years of experience. You explain concepts clearly, provide practical examples, and follow best practices.',
        'base_model': 'microsoft/phi-3-medium-128k-instruct'
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 201:
        result = response.json()
        print('Custom model created!')
        print(f"Name: {result['data']['full_name']}")
        print(f"ID: {result['data']['id']}")
    else:
        print(f"Error {response.status_code}: {response.json()}")

def use_custom_model():
    url = f'{BASE_URL}/completion'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    data = {
        'model': '@cognima/python-mentor',
        'messages': [
            {'role': 'user', 'content': 'Explain Python decorators with an example'}
        ]
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print('\nUsing custom model:')
        print(result['data']['choices'][0]['message']['content'])
    else:
        print(f"Error {response.status_code}: {response.json()}")

if __name__ == '__main__':
    # create_custom_model()
    use_custom_model()
