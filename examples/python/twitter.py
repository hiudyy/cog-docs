import requests
import os

API_KEY = os.environ.get('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog.api.br/api/v1'

def get_tweet_info():
    """Obter informações completas de um tweet"""
    try:
        url = 'https://twitter.com/elonmusk/status/1234567890123456789'
        # Também funciona com x.com:
        # url = 'https://x.com/elonmusk/status/1234567890123456789'
        
        response = requests.get(
            f'{BASE_URL}/twitter/info',
            params={'url': url},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        data = response.json()['data']
        print('🐦 Tweet Info:')
        print(f"   ID: {data['id']}")
        print(f"   Texto: {data['text'][:100]}...")
        print(f"   Data: {data['createdAt']}")
        
        print('\n👤 Autor:')
        print(f"   Nome: {data['author']['name']}")
        print(f"   Username: @{data['author']['username']}")
        print(f"   Avatar: {data['author']['avatarUrl']}")
        
        print('\n📊 Estatísticas:')
        print(f"   Likes: {data['stats']['likes']:,}")
        print(f"   Retweets: {data['stats']['retweets']:,}")
        print(f"   Respostas: {data['stats']['replies']:,}")
        
        print(f"\n📎 Tipo de Mídia: {data['type']}")
        print(f"   Tem Mídia: {'Sim' if data['hasMedia'] else 'Não'}")
        
        if data.get('media'):
            print('\n🎬 Mídias:')
            for i, media in enumerate(data['media'], 1):
                print(f"   {i}. Tipo: {media['type']}")
                if media['type'] == 'video':
                    print(f"      Duração: {media.get('duration', 'N/A')}ms")
                    if media.get('bestQuality'):
                        print(f"      Melhor qualidade: {media['bestQuality'].get('resolution', 'N/A')}")
                        print(f"      URL: {media['bestQuality'].get('url', media.get('url', 'N/A'))}")
                else:
                    print(f"      URL: {media.get('url', 'N/A')}")
        
        return data
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')
        if hasattr(e, 'response') and e.response:
            print(f'   Detalhes: {e.response.json()}')

def download_twitter_media():
    """Obter links de download direto"""
    try:
        url = 'https://twitter.com/user/status/1234567890123456789'
        
        response = requests.get(
            f'{BASE_URL}/twitter/download',
            params={'url': url},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        data = response.json()['data']
        print('✅ Downloads disponíveis:')
        print(f"   Tweet ID: {data['tweetId']}")
        print(f"   Autor: @{data['author']}")
        print(f"   Tipo: {data['type']}")
        
        print('\n📥 Links de Download:')
        for i, download in enumerate(data['downloads'], 1):
            print(f"   {i}. Tipo: {download['type']}")
            if download.get('resolution'):
                print(f"      Resolução: {download['resolution']}")
            if download.get('duration'):
                print(f"      Duração: {download['duration']}ms")
            print(f"      URL: {download['url']}")
        
        return data
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')

def download_video_to_disk(tweet_url: str, output_path: str):
    """Baixar vídeo do tweet para o disco"""
    try:
        # Primeiro, obter os links de download
        response = requests.get(
            f'{BASE_URL}/twitter/download',
            params={'url': tweet_url},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        data = response.json()['data']
        
        if not data['downloads']:
            print('❌ Nenhuma mídia encontrada no tweet')
            return
        
        # Pegar o primeiro download (melhor qualidade)
        download_url = data['downloads'][0]['url']
        media_type = data['downloads'][0]['type']
        
        print(f'⬇️  Baixando {media_type}...')
        file_response = requests.get(download_url, stream=True)
        file_response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in file_response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f'✅ Arquivo salvo em: {output_path}')
        
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')

def example_types():
    """Mostrar tipos suportados"""
    print('📋 Tipos de mídia suportados:')
    print('   • Vídeos (várias resoluções)')
    print('   • Fotos (qualidade original)')
    print('   • GIFs')
    print('\n🔗 Formatos de URL suportados:')
    print('   • https://twitter.com/user/status/ID')
    print('   • https://x.com/user/status/ID')
    print('   • https://twitter.com/i/status/ID')

if __name__ == '__main__':
    print('=== Twitter/X API Examples ===\n')
    get_tweet_info()

