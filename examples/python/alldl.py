import requests

API_BASE = 'https://cog.api.br/api/v1'

def download_all_media(url: str) -> dict:
    """
    Download all available media from any URL
    
    Args:
        url: Any URL supported by yt-dlp
        
    Returns:
        dict: All media data or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/alldl', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            result = data['data']
            metadata = result['metadata']
            media = result['media']
            
            print('=== METADATA ===')
            print(f"Title: {metadata['title']}")
            print(f"Platform: {metadata['platform']}")
            print(f"Duration: {metadata['duration']} seconds")
            print(f"Views: {metadata.get('views', 'N/A')}")
            print(f"Uploader: {metadata.get('uploader', 'N/A')}")
            
            print('\n=== SUMMARY ===')
            print(f"Total Items: {result['totalItems']}")
            print(f"Videos: {result['videoCount']}")
            print(f"Audio: {result['audioCount']}")
            print(f"Images: {result['imageCount']}")
            
            print('\n=== ALL MEDIA ===')
            for index, item in enumerate(media, 1):
                print(f"\n[{index}] {item['type'].upper()}")
                print(f"  URL: {item['url'][:60]}...")
                print(f"  Quality: {item['quality']}")
                print(f"  Format: {item['format']}")
                if item.get('filesize'):
                    print(f"  Size: {item['filesize'] / 1024 / 1024:.2f} MB")
                if item.get('isBest'):
                    print("  ⭐ BEST QUALITY")
            
            return result
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

def download_by_type(url: str, media_type: str) -> dict:
    """
    Download media filtered by type
    
    Args:
        url: Any URL supported by yt-dlp
        media_type: Media type - 'video', 'audio', or 'image'
        
    Returns:
        dict: Filtered media data or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/alldl/type', params={'url': url, 'type': media_type})
        data = response.json()
        
        if data.get('success'):
            result = data['data']
            metadata = result['metadata']
            media = result['media']
            
            print('=== METADATA ===')
            print(f"Title: {metadata['title']}")
            print(f"Platform: {metadata['platform']}")
            
            print(f"\n=== {media_type.upper()} ONLY ({result['totalItems']} items) ===")
            for index, item in enumerate(media, 1):
                print(f"\n[{index}] {item['type'].upper()}")
                print(f"  URL: {item['url'][:60]}...")
                print(f"  Quality: {item['quality']}")
                print(f"  Format: {item['format']}")
                
                if media_type == 'video' and item.get('resolution'):
                    print(f"  Resolution: {item['resolution']}")
                    print(f"  FPS: {item.get('fps')}")
                    print(f"  Codec: {item.get('vcodec')}")
                
                if media_type == 'audio':
                    print(f"  Codec: {item.get('acodec')}")
                    print(f"  Bitrate: {item.get('abr')} kbps")
                    print(f"  Sample Rate: {item.get('asr')} Hz")
                
                if media_type == 'image' and item.get('width'):
                    print(f"  Resolution: {item['width']}x{item['height']}")
                
                if item.get('filesize'):
                    print(f"  Size: {item['filesize'] / 1024 / 1024:.2f} MB")
            
            return result
        else:
            print(f"Error: {data.get('error')}")
            return None
            
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

def get_best_quality(url: str) -> dict:
    """
    Get only the best quality video
    
    Args:
        url: Any URL supported by yt-dlp
        
    Returns:
        dict: Best quality media or None if error
    """
    try:
        response = requests.get(f'{API_BASE}/alldl', params={'url': url})
        data = response.json()
        
        if data.get('success'):
            media = data['data']['media']
            best = next((m for m in media if m.get('isBest')), None)
            
            if best:
                print('=== BEST QUALITY ===')
                print(f"Type: {best['type']}")
                print(f"Quality: {best['quality']}")
                print(f"Format: {best['format']}")
                print(f"Download URL: {best['url']}")
                
                return best
        return None
    except Exception as e:
        print(f'Request Error: {str(e)}')
        return None

if __name__ == '__main__':
    # Example 1: Download all media
    print('=== EXAMPLE 1: ALL MEDIA ===\n')
    youtube_url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    download_all_media(youtube_url)
    
    print('\n\n=== EXAMPLE 2: AUDIO ONLY ===\n')
    download_by_type(youtube_url, 'audio')
    
    print('\n\n=== EXAMPLE 3: IMAGES ONLY ===\n')
    download_by_type(youtube_url, 'image')
    
    print('\n\n=== EXAMPLE 4: BEST QUALITY ===\n')
    get_best_quality(youtube_url)
    
    print('\n\n=== EXAMPLE 5: OTHER PLATFORMS ===\n')
    
    # TikTok
    print('\n--- TikTok ---')
    download_all_media('https://www.tiktok.com/@user/video/123456789')
    
    # Vimeo
    print('\n--- Vimeo ---')
    download_all_media('https://vimeo.com/123456789')
    
    # SoundCloud
    print('\n--- SoundCloud ---')
    download_by_type('https://soundcloud.com/artist/track', 'audio')
