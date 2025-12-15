import requests
import os

API_KEY = os.environ.get('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog.api.br/api/v1'

def search_web(query: str, max_results: int = 10):
    """Pesquisa web geral usando DuckDuckGo"""
    try:
        response = requests.get(
            f'{BASE_URL}/search',
            params={'q': query, 'max': max_results},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        data = response.json()['data']
        print(f'🔍 Pesquisa Web: "{data["query"]}"')
        print(f'   Total de resultados: {data["totalResults"]}\n')
        
        for i, result in enumerate(data['results'], 1):
            print(f'{i}. {result["title"]}')
            print(f'   URL: {result["url"]}')
            print(f'   {result["description"][:100]}...')
            print('')
        
        return data
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')
        if hasattr(e, 'response') and e.response:
            print(f'   Detalhes: {e.response.json()}')

def search_news(query: str, max_results: int = 10):
    """Pesquisa de notícias"""
    try:
        response = requests.get(
            f'{BASE_URL}/search/news',
            params={'q': query, 'max': max_results},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        data = response.json()['data']
        print(f'📰 Pesquisa de Notícias: "{data["query"]}"')
        print(f'   Total de resultados: {data["totalResults"]}\n')
        
        for i, result in enumerate(data['results'], 1):
            print(f'{i}. {result["title"]}')
            print(f'   Fonte: {result["displayUrl"]}')
            print(f'   {result["description"][:100]}...')
            print('')
        
        return data
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')

def multi_search(queries: list):
    """Pesquisa múltipla"""
    print('🔎 Pesquisa Múltipla:\n')
    
    results = {}
    for query in queries:
        try:
            response = requests.get(
                f'{BASE_URL}/search',
                params={'q': query, 'max': 3},
                headers={'Authorization': f'Bearer {API_KEY}'}
            )
            response.raise_for_status()
            
            data = response.json()['data']
            results[query] = data['results']
            
            print(f'Query: "{query}"')
            for r in data['results']:
                print(f'  • {r["title"]}')
            print('')
            
        except Exception as e:
            print(f'Erro em "{query}": {e}')
            results[query] = []
    
    return results

if __name__ == '__main__':
    print('=== Search API Examples ===\n')
    search_web('inteligência artificial')

