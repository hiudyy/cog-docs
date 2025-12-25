import requests

API_BASE = 'https://cog.api.br/api/v1'

def download_likee(url: str) -> dict:
    """
    Download video from Likee
    
    Args:
        url: Likee video URL
        
    Returns:
        dict: Download data or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/likee/download', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Likee Video Downloaded Successfully!')
            print(f"Title: {data['data']['title']}")
            print(f"Author: {data['data']['author']}")
            print(f"Views: {data['data']['views']}")
            print(f"Likes: {data['data']['likes']}")
            print(f"Comments: {data['data']['comments']}")
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

def get_likee_info(url: str) -> dict:
    """
    Get information about Likee video
    
    Args:
        url: Likee video URL
        
    Returns:
        dict: Video information or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/likee/info', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Likee Video Information:')
            print(f"Title: {data['info']['title']}")
            print(f"Author: {data['info']['author']}")
            print(f"Views: {data['info']['views']}")
            print(f"Likes: {data['info']['likes']}")
            print(f"Comments: {data['info']['comments']}")
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
    print('=== Likee Download Example ===\n')
    
    # Example 1: Download Likee video
    likee_url = 'https://likee.video/@username/video/123456'
    print(f'Downloading from Likee: {likee_url}')
    download_likee(likee_url)
    
    print('\n=== Likee Info Example ===\n')
    
    # Example 2: Get video info
    print(f'Getting video info: {likee_url}')
    get_likee_info(likee_url)
