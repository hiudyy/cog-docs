import requests
import os

API_KEY = os.environ.get('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog.api.br/api/v1'

def get_gdrive_info():
    """Obter informações de arquivo do Google Drive"""
    try:
        url = 'https://drive.google.com/file/d/1ABC123xyz/view?usp=sharing'
        
        response = requests.get(
            f'{BASE_URL}/gdrive/info',
            params={'url': url},
            headers={'Authorization': f'Bearer {API_KEY}'}
        )
        response.raise_for_status()
        
        data = response.json()['data']
        print('📁 Google Drive File Info:')
        print(f"   Nome: {data['fileName']}")
        print(f"   Tamanho: {data['fileSize']}")
        print(f"   Tipo: {data['mimetype']}")
        print(f"   Link: {data['downloadUrl']}")
        
        return data
    except requests.exceptions.RequestException as e:
        print(f'❌ Erro: {e}')
        if hasattr(e, 'response') and e.response:
            print(f'   Detalhes: {e.response.json()}')

def download_gdrive():
    """Obter link de download do Google Drive"""
    try:
        url = 'https://drive.google.com/file/d/1ABC123xyz/view?usp=sharing'
        
        response = requests.get(
            f'{BASE_URL}/gdrive/download',
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

def download_file_to_disk(gdrive_url: str, output_path: str):
    """Baixar arquivo diretamente para o disco"""
    try:
        # Primeiro, obter o link de download
        response = requests.get(
            f'{BASE_URL}/gdrive/download',
            params={'url': gdrive_url},
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
    print('=== Google Drive API Examples ===\n')
    get_gdrive_info()

