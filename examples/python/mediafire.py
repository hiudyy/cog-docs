import requests
import os

API_KEY = os.environ.get('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog2.cognima.com.br/api/v1'

def get_mediafire_info():
    """Obter informações de arquivo do MediaFire"""
    try:
        url = 'https://www.mediafire.com/file/abc123xyz/arquivo.zip/file'
        
        response = requests.get(
            f'{BASE_URL}/mediafire/info',
            params={'url': url},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        data = response.json()['data']
        print('📁 MediaFire File Info:')
        print(f"   Nome: {data['fileName']}")
        print(f"   Tamanho: {data['fileSize']}")
        print(f"   Data Upload: {data['uploadDate']}")
        print(f"   Tipo: {data['mimetype']}")
        print(f"   Extensão: {data['extension']}")
        print(f"   Link: {data['downloadUrl']}")
        
        return data
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')
        if hasattr(e, 'response') and e.response:
            print(f'   Detalhes: {e.response.json()}')

def download_mediafire():
    """Obter link de download do MediaFire"""
    try:
        url = 'https://www.mediafire.com/file/abc123xyz/arquivo.zip/file'
        
        response = requests.get(
            f'{BASE_URL}/mediafire/download',
            params={'url': url},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        data = response.json()['data']
        print('✅ Download disponível:')
        print(f"   Arquivo: {data['fileName']}")
        print(f"   URL: {data['downloadUrl']}")
        
        return data
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')

def download_file_to_disk(mediafire_url: str, output_path: str):
    """Baixar arquivo diretamente para o disco"""
    try:
        # Primeiro, obter o link de download
        response = requests.get(
            f'{BASE_URL}/mediafire/download',
            params={'url': mediafire_url},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        download_url = response.json()['data']['downloadUrl']
        file_name = response.json()['data']['fileName']
        
        # Depois, baixar o arquivo
        print(f'⬇️  Baixando {file_name}...')
        file_response = requests.get(download_url, stream=True)
        file_response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in file_response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f'✅ Arquivo salvo em: {output_path}')
        
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')

if __name__ == '__main__':
    print('=== MediaFire API Examples ===\n')
    get_mediafire_info()

