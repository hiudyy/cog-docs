"""
Cognima API - Facebook Download Examples (Python)

This file demonstrates how to use the Facebook download endpoints
to download videos with multiple quality options.
"""

import requests
from typing import List, Dict, Optional

# API Configuration
BASE_URL = 'https://cog.api.br/api/v1'
API_KEY = 'YOUR_API_KEY_HERE'

# Configure headers
headers = {
    'apikey': API_KEY
}

def download_facebook_video(url: str) -> List[Dict]:
    """
    Download Facebook video (all quality options)
    
    Args:
        url: Facebook video URL
    
    Returns:
        List of video quality options
    """
    print('\n=== Downloading Facebook Video (All Qualities) ===\n')
    print(f'URL: {url}\n')
    
    params = {'url': url}
    
    response = requests.get(f'{BASE_URL}/facebook/download', params=params, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    
    if data['success']:
        videos = data['videos']
        print('✅ Download URLs Ready!\n')
        print(f"Found {len(videos)} quality options:\n")
        
        for i, video in enumerate(videos, 1):
            print(f"{i}. Resolution: {video['resolution']}")
            print(f"   URL: {video['url']}")
            print(f"   Thumbnail: {video['thumbnail']}")
            print(f"   Should Render: {'Yes' if video['shouldRender'] else 'No'}")
            print()
        
        return videos
    
    return []

def download_facebook_video_hd(url: str) -> Dict:
    """
    Download Facebook video in best quality (HD preferred)
    
    Args:
        url: Facebook video URL
    
    Returns:
        Best quality video information
    """
    print('\n=== Downloading Facebook Video (Best Quality) ===\n')
    print(f'URL: {url}\n')
    
    params = {'url': url}
    
    response = requests.get(f'{BASE_URL}/facebook/download-hd', params=params, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    
    if data['success']:
        video = data['video']
        all_qualities = data['allQualities']
        
        print('✅ Best Quality Download Ready!\n')
        print('🎬 Selected Quality:')
        print(f"   Resolution: {video['resolution']}")
        print(f"   URL: {video['url']}")
        print(f"   Thumbnail: {video['thumbnail']}")
        print(f"   Should Render: {'Yes' if video['shouldRender'] else 'No'}")
        print(f"\n📊 Available Qualities: {len(all_qualities)}")
        
        for i, q in enumerate(all_qualities, 1):
            print(f"   {i}. {q['resolution']}")
        
        return video
    
    return {}

def download_multiple_videos(urls: List[str]) -> List[Dict]:
    """
    Download multiple Facebook videos
    
    Args:
        urls: List of Facebook video URLs
    
    Returns:
        List of download results
    """
    print('\n=== Downloading Multiple Facebook Videos ===\n')
    
    results = []
    
    for url in urls:
        try:
            params = {'url': url}
            response = requests.get(f'{BASE_URL}/facebook/download-hd', params=params, headers=headers)
            response.raise_for_status()
            
            data = response.json()
            
            results.append({
                'url': url,
                'success': True,
                'video': data['video']
            })
            
            print(f"✅ Downloaded: {data['video']['resolution']}")
        except Exception as e:
            results.append({
                'url': url,
                'success': False,
                'error': str(e)
            })
            
            print(f"❌ Failed: {url}")
    
    successful = len([r for r in results if r['success']])
    print(f"\n📋 Downloaded {successful}/{len(urls)} videos")
    
    return results

def download_specific_quality(url: str, preferred_resolution: str) -> Dict:
    """
    Get specific quality from Facebook video
    
    Args:
        url: Facebook video URL
        preferred_resolution: Preferred resolution (e.g., "720p", "1080p")
    
    Returns:
        Video information for preferred quality
    """
    print(f'\n=== Downloading Facebook Video ({preferred_resolution}) ===\n')
    print(f'URL: {url}\n')
    
    params = {'url': url}
    
    response = requests.get(f'{BASE_URL}/facebook/download', params=params, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    
    if data['success']:
        videos = data['videos']
        
        # Find preferred quality
        video = next(
            (v for v in videos if preferred_resolution.lower() in v['resolution'].lower()),
            videos[0]
        )
        
        print('✅ Download URL Ready!\n')
        print(f"Resolution: {video['resolution']}")
        print(f"URL: {video['url']}")
        print(f"Thumbnail: {video['thumbnail']}")
        
        return video
    
    return {}

def get_video_info(url: str) -> Dict:
    """
    Get video information without downloading
    
    Args:
        url: Facebook video URL
    
    Returns:
        Dictionary with video information
    """
    print('\n=== Getting Facebook Video Info ===\n')
    print(f'URL: {url}\n')
    
    params = {'url': url}
    
    response = requests.get(f'{BASE_URL}/facebook/download', params=params, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    
    if data['success']:
        videos = data['videos']
        
        print('📊 Video Information:\n')
        print(f"Available Qualities: {len(videos)}")
        
        for i, video in enumerate(videos, 1):
            print(f"\n{i}. {video['resolution']}")
            print(f"   Has Thumbnail: {'Yes' if video['thumbnail'] else 'No'}")
            print(f"   Needs Rendering: {'Yes' if video['shouldRender'] else 'No'}")
        
        # Find best quality
        best_quality = (
            next((v for v in videos if '1080p' in v['resolution']), None) or
            next((v for v in videos if '720p' in v['resolution']), None) or
            videos[0]
        )
        
        print(f"\n🏆 Best Quality: {best_quality['resolution']}")
        
        return {
            'totalQualities': len(videos),
            'qualities': [v['resolution'] for v in videos],
            'bestQuality': best_quality['resolution']
        }
    
    return {}

def compare_qualities(url: str) -> List[Dict]:
    """
    Download and compare qualities
    
    Args:
        url: Facebook video URL
    
    Returns:
        List of quality comparisons
    """
    print('\n=== Comparing Video Qualities ===\n')
    print(f'URL: {url}\n')
    
    params = {'url': url}
    
    response = requests.get(f'{BASE_URL}/facebook/download', params=params, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    
    if data['success']:
        videos = data['videos']
        
        print('📊 Quality Comparison:\n')
        
        comparison = []
        for video in videos:
            comp = {
                'resolution': video['resolution'],
                'hasThumbnail': bool(video['thumbnail']),
                'needsRender': video['shouldRender'],
                'isDirectLink': not video['shouldRender']
            }
            comparison.append(comp)
            
            print(f"Resolution: {comp['resolution']}")
            print(f"  Thumbnail: {'Yes' if comp['hasThumbnail'] else 'No'}")
            print(f"  Needs Render: {'Yes' if comp['needsRender'] else 'No'}")
            print(f"  Direct Link: {'Yes' if comp['isDirectLink'] else 'No'}")
            print()
        
        return comparison
    
    return []

def download_best_from_multiple_sources(urls: List[str]) -> List[Dict]:
    """
    Download best quality from multiple Facebook video URLs
    
    Args:
        urls: List of Facebook video URLs
    
    Returns:
        List of best quality videos
    """
    print('\n=== Downloading Best Quality from Multiple Sources ===\n')
    
    best_videos = []
    
    for i, url in enumerate(urls, 1):
        print(f'Processing {i}/{len(urls)}...')
        
        try:
            video = download_facebook_video_hd(url)
            best_videos.append({
                'url': url,
                'video': video,
                'success': True
            })
        except Exception as e:
            print(f'❌ Error: {str(e)}')
            best_videos.append({
                'url': url,
                'error': str(e),
                'success': False
            })
        
        print()
    
    successful = len([v for v in best_videos if v['success']])
    print(f'✅ Successfully downloaded {successful}/{len(urls)} videos')
    
    return best_videos

def filter_by_resolution(url: str, min_resolution: str = '720p') -> List[Dict]:
    """
    Filter video qualities by minimum resolution
    
    Args:
        url: Facebook video URL
        min_resolution: Minimum resolution required
    
    Returns:
        List of filtered video qualities
    """
    print(f'\n=== Filtering by Minimum Resolution ({min_resolution}) ===\n')
    print(f'URL: {url}\n')
    
    params = {'url': url}
    
    response = requests.get(f'{BASE_URL}/facebook/download', params=params, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    
    if data['success']:
        videos = data['videos']
        
        # Simple resolution filtering
        resolution_order = {'1080p': 3, '720p': 2, '480p': 1, '360p': 0}
        min_value = resolution_order.get(min_resolution, 1)
        
        filtered = [
            v for v in videos
            if any(res in v['resolution'] for res in resolution_order.keys()
                   if resolution_order[res] >= min_value)
        ]
        
        print(f'Found {len(filtered)} qualities >= {min_resolution}:\n')
        for video in filtered:
            print(f"  - {video['resolution']}")
        
        return filtered
    
    return []

# ===================
# EXAMPLES
# ===================

def main():
    try:
        test_url = 'https://www.facebook.com/share/r/14RStacRcih/'
        
        # Example 1: Download all quality options
        download_facebook_video(test_url)
        
        # Example 2: Download best quality (HD preferred)
        download_facebook_video_hd(test_url)
        
        # Example 3: Download specific quality
        download_specific_quality(test_url, '720p')
        
        # Example 4: Get video information
        get_video_info(test_url)
        
        # Example 5: Compare qualities
        compare_qualities(test_url)
        
        # Example 6: Download multiple videos
        urls = [
            'https://www.facebook.com/share/r/14RStacRcih/',
            'https://fb.watch/example123/'
        ]
        download_multiple_videos(urls)
        
        # Example 7: Download best from multiple sources
        download_best_from_multiple_sources(urls)
        
        # Example 8: Filter by resolution
        filter_by_resolution(test_url, '720p')
        
    except Exception as e:
        print(f'Error: {str(e)}')
        exit(1)

if __name__ == '__main__':
    main()
