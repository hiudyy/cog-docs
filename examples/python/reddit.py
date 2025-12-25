import requests

API_BASE = 'https://cog.api.br/api/v1'

def download_reddit(url: str) -> dict:
    """
    Download media from a Reddit post
    
    Args:
        url: Reddit post URL
        
    Returns:
        dict: Download data or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/reddit/download', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Reddit Media Downloaded Successfully!')
            print(f"Title: {data['data']['title']}")
            print(f"Author: {data['data']['author']}")
            print(f"Subreddit: {data['data']['subreddit']}")
            print(f"Upvotes: {data['data']['upvotes']}")
            print(f"Comments: {data['data']['comments']}")
            print(f"Download URL: {data['data']['downloadUrl']}")
            print(f"Is Video: {data['data']['isVideo']}")
            print(f"Duration: {data['data']['duration']} seconds")
            
            return data['data']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

def get_reddit_info(url: str) -> dict:
    """
    Get information about a Reddit post
    
    Args:
        url: Reddit post URL
        
    Returns:
        dict: Post information or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/reddit/info', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            print('Reddit Post Information:')
            print(f"Title: {data['info']['title']}")
            print(f"Author: {data['info']['author']}")
            print(f"Subreddit: {data['info']['subreddit']}")
            print(f"Upvotes: {data['info']['upvotes']}")
            print(f"Comments: {data['info']['comments']}")
            print(f"Is Video: {data['info']['isVideo']}")
            print(f"Description: {data['info']['description']}")
            print(f"URL: {data['info']['url']}")
            
            return data['info']
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

if __name__ == '__main__':
    print('=== Reddit Download Example ===\n')
    
    # Example 1: Download Reddit video
    reddit_url = 'https://www.reddit.com/r/videos/comments/example'
    print(f'Downloading from Reddit: {reddit_url}')
    download_reddit(reddit_url)
    
    print('\n=== Reddit Info Example ===\n')
    
    # Example 2: Get post info
    print(f'Getting post info: {reddit_url}')
    get_reddit_info(reddit_url)
