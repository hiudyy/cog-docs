import requests

API_BASE = 'https://cog.api.br/api/v1'

def download_dailymotion(url: str) -> dict:
    """
    Download video from Dailymotion
    
    Args:
        url: Dailymotion video URL
        
    Returns:
        dict: Download data or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/dailymotion/download', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Dailymotion Video Downloaded Successfully!')
            print(f"Title: {data['data']['title']}")
            print(f"Author: {data['data']['author']}")
            print(f"Quality: {data['data']['quality']}")
            print(f"Views: {data['data']['views']}")
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

def get_dailymotion_formats(url: str) -> list:
    """
    Get available formats for Dailymotion video
    
    Args:
        url: Dailymotion video URL
        
    Returns:
        list: Available formats or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/dailymotion/formats', params={'url': url})
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

def get_dailymotion_info(url: str) -> dict:
    """
    Get information about Dailymotion video
    
    Args:
        url: Dailymotion video URL
        
    Returns:
        dict: Video information or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/dailymotion/info', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Dailymotion Video Information:')
            print(f"Title: {data['info']['title']}")
            print(f"Author: {data['info']['author']}")
            print(f"Views: {data['info']['views']}")
            print(f"Duration: {data['info']['duration']} seconds")
            print(f"Description: {data['info']['description']}")
            print(f"Quality: {data['info']['quality']}")
            
            return data['info']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

if __name__ == '__main__':
    print('=== Dailymotion Download Example ===\n')
    
    # Example 1: Download Dailymotion video
    dailymotion_url = 'https://www.dailymotion.com/video/x8example'
    print(f'Downloading from Dailymotion: {dailymotion_url}')
    download_dailymotion(dailymotion_url)
    
    print('\n=== Dailymotion Formats Example ===\n')
    
    # Example 2: Get available formats
    print(f'Getting formats for: {dailymotion_url}')
    get_dailymotion_formats(dailymotion_url)
    
    print('\n=== Dailymotion Info Example ===\n')
    
    # Example 3: Get video info
    print(f'Getting video info: {dailymotion_url}')
    get_dailymotion_info(dailymotion_url)
