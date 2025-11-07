import requests
import os

API_KEY = os.getenv('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog2.cognima.com.br/api/v1'

def get_status():
    url = f'{BASE_URL}/status'
    headers = {
        'X-API-Key': API_KEY
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        data = result['data']
        
        print('=== API Key Status ===')
        print(f"Name: {data['api_key']['name']}")
        print(f"Active: {data['api_key']['is_active']}")
        
        print('\n=== Limits ===')
        print(f"Hourly: {data['limits']['hourly']['remaining']}/{data['limits']['hourly']['limit']}")
        print(f"Daily Requests: {data['limits']['daily']['requests']['remaining']}/{data['limits']['daily']['requests']['limit']}")
        print(f"Daily Tokens: {data['limits']['daily']['tokens']['remaining']}/{data['limits']['daily']['tokens']['limit']}")
        
        print('\n=== Usage Today ===')
        print(f"Requests: {data['usage']['today']['requests']}")
        print(f"Tokens: {data['usage']['today']['total_tokens']:,}")
        print(f"Cost: ${data['usage']['today']['estimated_cost']:.6f}")
        
        print('\n=== Last 30 Days ===')
        print(f"Requests: {data['usage']['last_30_days']['requests']:,}")
        print(f"Tokens: {data['usage']['last_30_days']['total_tokens']:,}")
        print(f"Cost: ${data['usage']['last_30_days']['estimated_cost']:.4f}")
        print(f"Success Rate: {data['usage']['last_30_days']['success_rate']}%")
    else:
        print(f"Error {response.status_code}: {response.json()}")

def get_models_stats():
    url = f'{BASE_URL}/status/models?days=7'
    headers = {
        'X-API-Key': API_KEY
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        print('\n=== Models Statistics ===')
        print(f"Total Models: {result['data']['summary']['total_models']}")
        print(f"Total Requests: {result['data']['summary']['total_requests']:,}")
        print(f"Total Tokens: {result['data']['summary']['total_tokens']:,}")
    else:
        print(f"Error {response.status_code}: {response.json()}")

if __name__ == '__main__':
    get_status()
    get_models_stats()
