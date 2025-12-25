import requests

API_BASE = 'https://cog.api.br/api/v1'

def download_streamable(url: str) -> dict:
    """
    Download video from Streamable
    
    Args:
        url: Streamable video URL
        
    Returns:
        dict: Download data or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/streamable/download', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Streamable Video Downloaded Successfully!')
            print(f"Title: {data['data']['title']}")
            print(f"Quality: {data['data']['quality']}")
            print(f"Download URL: {data['data']['downloadUrl']}")
            print(f"Duration: {data['data']['duration']} seconds")
            print(f"Resolution: {data['data']['width']}x{data['data']['height']}")
            print(f"Filesize: {data['data']['filesize'] / 1024 / 1024:.2f} MB")
            
            return data['data']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

def get_streamable_formats(url: str) -> list:
    """
    Get available formats for Streamable video
    
    Args:
        url: Streamable video URL
        
    Returns:
        list: Available formats or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/streamable/formats', params={'url': url})
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

def get_streamable_info(url: str) -> dict:
    """
    Get information about Streamable video
    
    Args:
        url: Streamable video URL
        
    Returns:
        dict: Video information or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/streamable/info', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Streamable Video Information:')
            print(f"Title: {data['info']['title']}")
            print(f"Duration: {data['info']['duration']} seconds")
            print(f"Description: {data['info']['description']}")
            print(f"Quality: {data['info']['quality']}")
            print(f"Filesize: {data['info']['filesize'] / 1024 / 1024:.2f} MB")
            
            return data['info']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

if __name__ == '__main__':
    print('=== Streamable Download Example ===\n')
    
    # Example 1: Download Streamable video
    streamable_url = 'https://streamable.com/example'
    print(f'Downloading from Streamable: {streamable_url}')
    download_streamable(streamable_url)
    
    print('\n=== Streamable Formats Example ===\n')
    
    # Example 2: Get available formats
    print(f'Getting formats for: {streamable_url}')
    get_streamable_formats(streamable_url)
    
    print('\n=== Streamable Info Example ===\n')
    
    # Example 3: Get video info
    print(f'Getting video info: {streamable_url}')
    get_streamable_info(streamable_url)
