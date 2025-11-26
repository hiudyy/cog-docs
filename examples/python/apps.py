import requests
import os

API_KEY = os.environ.get('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog2.cognima.com.br/api/v1'

def search_all_stores(query: str, num: int = 10, country: str = 'br'):
    """Pesquisar apps em ambas as lojas (Google Play + App Store)"""
    try:
        response = requests.get(
            f'{BASE_URL}/apps/search',
            params={'q': query, 'num': num, 'country': country},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        data = response.json()['data']
        print(f'📱 Pesquisa de Apps: "{data["query"]}"\n')
        
        print('=== Google Play Store ===')
        for i, app in enumerate(data['playStore'], 1):
            print(f'{i}. {app["title"]}')
            print(f'   Developer: {app["developer"]}')
            print(f'   Score: {app["score"]} | {app["price"]}')
            print(f'   ID: {app["appId"]}')
            print('')
        
        print('=== Apple App Store ===')
        for i, app in enumerate(data['appStore'], 1):
            print(f'{i}. {app["title"]}')
            print(f'   Developer: {app["developer"]}')
            price = 'Free' if app.get('free') else app.get('price', 'N/A')
            print(f'   Score: {app["score"]} | {price}')
            print(f'   ID: {app["appId"]}')
            print('')
        
        return data
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')

def search_playstore(query: str, num: int = 10, country: str = 'br', lang: str = 'pt'):
    """Pesquisar apenas na Google Play Store"""
    try:
        response = requests.get(
            f'{BASE_URL}/apps/playstore',
            params={'q': query, 'num': num, 'country': country, 'lang': lang},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        data = response.json()['data']
        print(f'🤖 Google Play Store: "{data["query"]}"\n')
        
        for i, app in enumerate(data['results'], 1):
            print(f'{i}. {app["title"]}')
            print(f'   {app["developer"]} | ⭐ {app["score"]} | {app["price"]}')
            summary = app.get('summary', '')[:60] if app.get('summary') else ''
            print(f'   {summary}...')
            print('')
        
        return data
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')

def search_appstore(query: str, num: int = 10, country: str = 'br'):
    """Pesquisar apenas na Apple App Store"""
    try:
        response = requests.get(
            f'{BASE_URL}/apps/appstore',
            params={'q': query, 'num': num, 'country': country},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        data = response.json()['data']
        print(f'🍎 Apple App Store: "{data["query"]}"\n')
        
        for i, app in enumerate(data['results'], 1):
            print(f'{i}. {app["title"]}')
            price = 'Free' if app.get('free') else app.get('price', 'N/A')
            print(f'   {app["developer"]} | ⭐ {app["score"]} | {price}')
            genres = ', '.join(app.get('genres', [])) if app.get('genres') else 'N/A'
            print(f'   Genres: {genres}')
            print('')
        
        return data
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')

def get_app_details(app_id: str, store: str = 'playStore', country: str = 'br'):
    """Obter detalhes de um app específico"""
    try:
        response = requests.get(
            f'{BASE_URL}/apps/details',
            params={'appId': app_id, 'store': store, 'country': country},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        app = response.json()['data']
        print(f'📋 Detalhes do App: {app["title"]}\n')
        print(f'   Developer: {app["developer"]}')
        print(f'   Score: ⭐ {app["score"]} ({app.get("ratings", "N/A")} avaliações)')
        print(f'   Installs: {app.get("installs", "N/A")}')
        print(f'   Version: {app.get("version", "N/A")}')
        print(f'   Size: {app.get("size", "N/A")}')
        print(f'   Updated: {app.get("updated", "N/A")}')
        print(f'   {app.get("summary", "")}')
        
        return app
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')

def get_similar_apps(app_id: str, store: str = 'playStore', num: int = 10):
    """Obter apps similares"""
    try:
        response = requests.get(
            f'{BASE_URL}/apps/similar',
            params={'appId': app_id, 'store': store, 'num': num},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        data = response.json()['data']
        print(f'🔗 Apps Similares a "{data["appId"]}":\n')
        
        for i, app in enumerate(data['results'], 1):
            print(f'{i}. {app["title"]}')
            print(f'   {app["developer"]} | ⭐ {app["score"]}')
            print('')
        
        return data
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')

if __name__ == '__main__':
    print('=== Apps Search API Examples ===\n')
    search_all_stores('whatsapp', num=3)

