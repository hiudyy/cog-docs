import requests

API_BASE = 'https://cog.api.br/api/v1'

def download_vimeo(url: str) -> dict:
    """
    Download video from Vimeo
    
    Args:
        url: Vimeo video URL
        
    Returns:
        dict: Download data or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/vimeo/download', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Vimeo Video Downloaded Successfully!')
            print(f"Title: {data['data']['title']}")
            print(f"Author: {data['data']['author']}")
            print(f"Quality: {data['data']['quality']}")
            print(f"Views: {data['data']['views']}")
            print(f"Likes: {data['data']['likes']}")
            print(f"Download URL: {data['data']['downloadUrl']}")
            print(f"Duration: {data['data']['duration']} seconds")
            print(f"Resolution: {data['data']['width']}x{data['data']['height']}")
            
            return data['data']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

def get_vimeo_formats(url: str) -> list:
    """
    Get available formats for Vimeo video
    
    Args:
        url: Vimeo video URL
        
    Returns:
        list: Available formats or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/vimeo/formats', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Available Formats:')
            for index, format_info in enumerate(data['formats'], 1):
                print(f'\nFormat {index}:')
                print(f"  ID: {format_info['formatId']}")
                print(f"  Quality: {format_info['quality']}")
                print(f"  Extension: {format_info['ext']}")
                print(f"  Size: {format_info['filesize'] / 1024 / 1024:.2f} MB")
            
            return data['formats']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

def get_vimeo_info(url: str) -> dict:
    """
    Get information about Vimeo video
    
    Args:
        url: Vimeo video URL
        
    Returns:
        dict: Video information or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/vimeo/info', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Vimeo Video Information:')
            print(f"Title: {data['info']['title']}")
            print(f"Author: {data['info']['author']}")
            print(f"Views: {data['info']['views']}")
            print(f"Likes: {data['info']['likes']}")
            print(f"Duration: {data['info']['duration']} seconds")
            print(f"Description: {data['info']['description']}")
            print(f"Resolution: {data['info']['width']}x{data['info']['height']}")
            
            return data['info']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

if __name__ == '__main__':
    print('=== Vimeo Download Example ===\n')
    
    # Example 1: Download Vimeo video
    vimeo_url = 'https://vimeo.com/123456789'
    print(f'Downloading from Vimeo: {vimeo_url}')
    download_vimeo(vimeo_url)
    
    print('\n=== Vimeo Formats Example ===\n')
    
    # Example 2: Get available formats
    print(f'Getting formats for: {vimeo_url}')
    get_vimeo_formats(vimeo_url)
    
    print('\n=== Vimeo Info Example ===\n')
    
    # Example 3: Get video info
    print(f'Getting video info: {vimeo_url}')
    get_vimeo_info(vimeo_url)
