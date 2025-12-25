import requests

API_BASE = 'https://cog.api.br/api/v1'

def download_bandcamp(url: str) -> dict:
    """
    Download track/album from Bandcamp
    
    Args:
        url: Bandcamp track or album URL
        
    Returns:
        dict: Download data or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/bandcamp/download', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Bandcamp Track Downloaded Successfully!')
            print(f"Title: {data['data']['title']}")
            print(f"Artist: {data['data']['artist']}")
            print(f"Album: {data['data']['album']}")
            print(f"Genre: {data['data']['genre']}")
            print(f"Track Number: {data['data']['trackNumber']}")
            print(f"Download URL: {data['data']['downloadUrl']}")
            print(f"Duration: {data['data']['duration']} seconds")
            print(f"Release Date: {data['data']['releaseDate']}")
            print(f"Format: {data['data']['ext']}")
            
            return data['data']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

def get_bandcamp_formats(url: str) -> list:
    """
    Get available formats for Bandcamp track
    
    Args:
        url: Bandcamp track URL
        
    Returns:
        list: Available formats or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/bandcamp/formats', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Available Formats:')
            for index, format_info in enumerate(data['formats'], 1):
                print(f'\nFormat {index}:')
                print(f"  ID: {format_info['formatId']}")
                print(f"  Extension: {format_info['ext']}")
                print(f"  Size: {format_info['filesize'] / 1024 / 1024:.2f} MB")
            
            return data['formats']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

def get_bandcamp_info(url: str) -> dict:
    """
    Get information about Bandcamp track/album
    
    Args:
        url: Bandcamp track or album URL
        
    Returns:
        dict: Track information or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/bandcamp/info', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Bandcamp Track Information:')
            print(f"Title: {data['info']['title']}")
            print(f"Artist: {data['info']['artist']}")
            print(f"Album: {data['info']['album']}")
            print(f"Genre: {data['info']['genre']}")
            print(f"Duration: {data['info']['duration']} seconds")
            print(f"Description: {data['info']['description']}")
            print(f"Release Date: {data['info']['releaseDate']}")
            
            return data['info']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

if __name__ == '__main__':
    print('=== Bandcamp Download Example ===\n')
    
    # Example 1: Download Bandcamp track
    bandcamp_url = 'https://artist.bandcamp.com/track/example'
    print(f'Downloading from Bandcamp: {bandcamp_url}')
    download_bandcamp(bandcamp_url)
    
    print('\n=== Bandcamp Formats Example ===\n')
    
    # Example 2: Get available formats
    print(f'Getting formats for: {bandcamp_url}')
    get_bandcamp_formats(bandcamp_url)
    
    print('\n=== Bandcamp Info Example ===\n')
    
    # Example 3: Get track info
    print(f'Getting track info: {bandcamp_url}')
    get_bandcamp_info(bandcamp_url)
