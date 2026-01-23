import os
import requests

API_KEY = os.getenv('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog.api.br/api/v1'


def remove_background():
    url = f'{BASE_URL}/image/remove-bg'
    headers = {
        'X-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    payload = {
        'url': 'https://files.catbox.moe/ldsyfx.jpg'
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print('Remove BG Response:')
        print(data)
        if data.get('result', {}).get('download'):
            print(f"\nDownload: {data['result']['download']}")
    else:
        print(f"Error {response.status_code}: {response.text}")


if __name__ == '__main__':
    remove_background()
