"""
Cognima API - Exemplo de Filmes e Séries (XC IPTV)

Este exemplo demonstra como usar a API de filmes e séries
integrada com XC IPTV.
"""

import requests
from typing import Optional, List, Dict

# Configuração
API_BASE_URL = 'https://cog.api.br/api/v1'
API_KEY = 'sua-api-key-aqui'  # Substitua pela sua API key

# Headers
HEADERS = {
    'X-API-Key': API_KEY,
    'Content-Type': 'application/json'
}

# ===== EXEMPLOS DE FILMES =====

def listar_categorias_filmes() -> Optional[List[Dict]]:
    """Exemplo 1: Listar todas as categorias de filmes"""
    try:
        print('\n📁 Listando categorias de filmes...\n')
        
        response = requests.get(
            f'{API_BASE_URL}/filmes/categorias',
            headers=HEADERS
        )
        response.raise_for_status()
        
        categorias = response.json()['data']
        
        print(f'✅ {len(categorias)} categorias encontradas:')
        for cat in categorias[:5]:
            print(f"   - {cat['category_name']} (ID: {cat['category_id']})")
        
        return categorias
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')
        return None


def listar_filmes(category_id: Optional[str] = None) -> Optional[List[Dict]]:
    """Exemplo 2: Listar filmes (todos ou por categoria)"""
    try:
        print('\n🎬 Listando filmes...\n')
        
        params = {'category_id': category_id} if category_id else {}
        response = requests.get(
            f'{API_BASE_URL}/filmes',
            headers=HEADERS,
            params=params
        )
        response.raise_for_status()
        
        filmes = response.json()['data']
        
        print(f'✅ {len(filmes)} filmes encontrados:')
        for filme in filmes[:5]:
            print(f"   - {filme['name']}")
            print(f"     ID: {filme['stream_id']} | Rating: {filme.get('rating', 'N/A')}")
        
        return filmes
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')
        return None


def buscar_filmes(query: str) -> Optional[List[Dict]]:
    """Exemplo 3: Buscar filmes por nome"""
    try:
        print(f'\n🔍 Buscando filmes: "{query}"...\n')
        
        response = requests.get(
            f'{API_BASE_URL}/filmes/buscar',
            headers=HEADERS,
            params={'query': query}
        )
        response.raise_for_status()
        
        filmes = response.json()['data']
        
        print(f'✅ {len(filmes)} resultados encontrados:')
        for filme in filmes:
            print(f"   - {filme['name']}")
            print(f"     ID: {filme['stream_id']} | Rating: {filme.get('rating', 'N/A')}")
        
        return filmes
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')
        return None


def obter_detalhes_filme(stream_id: str) -> Optional[Dict]:
    """Exemplo 4: Obter detalhes completos de um filme"""
    try:
        print(f'\n📄 Obtendo detalhes do filme ID {stream_id}...\n')
        
        response = requests.get(
            f'{API_BASE_URL}/filmes/{stream_id}',
            headers=HEADERS
        )
        response.raise_for_status()
        
        dados = response.json()['data']
        info = dados['info']
        
        print('✅ Detalhes do filme:')
        print(f"   Nome: {info.get('name', 'N/A')}")
        print(f"   Gênero: {info.get('genre', 'N/A')}")
        print(f"   Rating: {info.get('rating', 'N/A')}")
        print(f"   Duração: {info.get('duration', 'N/A')}")
        print(f"   Diretor: {info.get('director', 'N/A')}")
        print(f"   Elenco: {info.get('cast', 'N/A')}")
        print(f"   Sinopse: {info.get('plot', 'N/A')}")
        print(f"   URL de Stream: {dados.get('streamUrl', 'N/A')}")
        
        return dados
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')
        return None


# ===== EXEMPLOS DE SÉRIES =====

def listar_categorias_series() -> Optional[List[Dict]]:
    """Exemplo 5: Listar categorias de séries"""
    try:
        print('\n📁 Listando categorias de séries...\n')
        
        response = requests.get(
            f'{API_BASE_URL}/series/categorias',
            headers=HEADERS
        )
        response.raise_for_status()
        
        categorias = response.json()['data']
        
        print(f'✅ {len(categorias)} categorias encontradas:')
        for cat in categorias[:5]:
            print(f"   - {cat['category_name']} (ID: {cat['category_id']})")
        
        return categorias
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')
        return None


def buscar_series(query: str) -> Optional[List[Dict]]:
    """Exemplo 6: Buscar séries"""
    try:
        print(f'\n🔍 Buscando séries: "{query}"...\n')
        
        response = requests.get(
            f'{API_BASE_URL}/series/buscar',
            headers=HEADERS,
            params={'query': query}
        )
        response.raise_for_status()
        
        series = response.json()['data']
        
        print(f'✅ {len(series)} resultados encontrados:')
        for serie in series[:5]:
            print(f"   - {serie['name']}")
            print(f"     ID: {serie['series_id']} | Rating: {serie.get('rating', 'N/A')}")
        
        return series
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')
        return None


def obter_detalhes_serie(series_id: str) -> Optional[Dict]:
    """Exemplo 7: Obter detalhes completos de uma série (com temporadas e episódios)"""
    try:
        print(f'\n📄 Obtendo detalhes da série ID {series_id}...\n')
        
        response = requests.get(
            f'{API_BASE_URL}/series/{series_id}',
            headers=HEADERS
        )
        response.raise_for_status()
        
        dados = response.json()['data']
        info = dados['info']
        
        print('✅ Detalhes da série:')
        print(f"   Nome: {info.get('name', 'N/A')}")
        print(f"   Gênero: {info.get('genre', 'N/A')}")
        print(f"   Rating: {info.get('rating', 'N/A')}")
        print(f"   Temporadas: {len(dados.get('seasons', []))}")
        
        if 'episodes' in dados and dados['episodes']:
            total_episodes = sum(len(eps) for eps in dados['episodes'].values())
            print(f"   Total de Episódios: {total_episodes}")
            
            # Mostrar primeira temporada
            first_season = sorted(dados['episodes'].keys())[0]
            print(f"\n   📺 Temporada {first_season}:")
            for ep in dados['episodes'][first_season][:3]:
                print(f"      E{ep['episode_num']}: {ep.get('title', 'Sem título')}")
                print(f"      Stream URL: {ep.get('streamUrl', 'N/A')}")
        
        return dados
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')
        return None


def gerar_link_player(tipo: str, id: str, episode_id: Optional[str] = None) -> str:
    """Exemplo 8: Gerar link do player web"""
    BASE_URL = 'https://cog.api.br'
    
    if tipo == 'filme':
        link = f'{BASE_URL}/watch/{id}'
        print(f'\n🎬 Link do Player (Filme):\n   {link}\n')
        return link
    elif tipo == 'serie':
        if episode_id:
            link = f'{BASE_URL}/watch/series/{id}/{episode_id}'
        else:
            link = f'{BASE_URL}/watch/series/{id}'
        print(f'\n📺 Link do Player (Série):\n   {link}\n')
        return link


# ===== EXECUTAR EXEMPLOS =====

def executar_exemplos():
    """Executar todos os exemplos"""
    print('═══════════════════════════════════════════════════')
    print('   🎬 Cognima API - Exemplos de Filmes e Séries')
    print('═══════════════════════════════════════════════════')

    # Exemplos de filmes
    listar_categorias_filmes()
    listar_filmes()
    
    filmes_matrix = buscar_filmes('matrix')
    if filmes_matrix and len(filmes_matrix) > 0:
        obter_detalhes_filme(filmes_matrix[0]['stream_id'])
        gerar_link_player('filme', filmes_matrix[0]['stream_id'])

    # Exemplos de séries
    listar_categorias_series()
    
    series_breaking = buscar_series('breaking bad')
    if series_breaking and len(series_breaking) > 0:
        detalhes = obter_detalhes_serie(series_breaking[0]['series_id'])
        gerar_link_player('serie', series_breaking[0]['series_id'])
        
        # Link para episódio específico
        if detalhes and 'episodes' in detalhes and detalhes['episodes']:
            first_season = sorted(detalhes['episodes'].keys())[0]
            if detalhes['episodes'][first_season]:
                episode_id = detalhes['episodes'][first_season][0]['id']
                gerar_link_player('serie', series_breaking[0]['series_id'], episode_id)

    print('\n═══════════════════════════════════════════════════')
    print('   ✅ Exemplos concluídos!')
    print('═══════════════════════════════════════════════════\n')


if __name__ == '__main__':
    executar_exemplos()
