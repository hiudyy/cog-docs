import requests

API_BASE = 'https://cog.api.br/api/v1'

def download_twitch(url: str) -> dict:
    """
    Download Twitch clip or VOD
    
    Args:
        url: Twitch clip or VOD URL
        
    Returns:
        dict: Download data or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/twitch/download', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Twitch Video Downloaded Successfully!')
            print(f"Title: {data['data']['title']}")
            print(f"Streamer: {data['data']['streamer']}")
            print(f"Type: {data['data']['type']}")
            print(f"Game: {data['data']['game']}")
            print(f"Views: {data['data']['views']}")
            print(f"Download URL: {data['data']['downloadUrl']}")
            print(f"Duration: {data['data']['duration']} seconds")
            
            return data['data']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

def get_twitch_formats(url: str) -> list:
    """
    Get available formats for Twitch video
    
    Args:
        url: Twitch clip or VOD URL
        
    Returns:
        list: Available formats or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/twitch/formats', params={'url': url})
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

def get_twitch_info(url: str) -> dict:
    """
    Get information about Twitch clip or VOD
    
    Args:
        url: Twitch clip or VOD URL
        
    Returns:
        dict: Video information or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/twitch/info', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Twitch Video Information:')
            print(f"Title: {data['info']['title']}")
            print(f"Streamer: {data['info']['streamer']}")
            print(f"Type: {data['info']['type']}")
            print(f"Game: {data['info']['game']}")
            print(f"Views: {data['info']['views']}")
            print(f"Duration: {data['info']['duration']} seconds")
            print(f"Description: {data['info']['description']}")
            
            return data['info']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

if __name__ == '__main__':
    print('=== Twitch Download Example ===\n')
    
    # Example 1: Download Twitch clip
    clip_url = 'https://clips.twitch.tv/example'
    print(f'Downloading Twitch clip: {clip_url}')
    download_twitch(clip_url)
    
    print('\n=== Twitch Formats Example ===\n')
    
    # Example 2: Get available formats
    vod_url = 'https://www.twitch.tv/videos/123456789'
    print(f'Getting formats for: {vod_url}')
    get_twitch_formats(vod_url)
    
    print('\n=== Twitch Info Example ===\n')
    
    # Example 3: Get video info
    print(f'Getting video info: {clip_url}')
    get_twitch_info(clip_url)
