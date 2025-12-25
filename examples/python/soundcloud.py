"""
Cognima API - SoundCloud Examples (Python)

This file demonstrates how to use the SoundCloud endpoints
to search and download tracks.
"""

import requests
import time
from typing import List, Dict

# API Configuration
BASE_URL = 'https://cog.api.br/api/v1'
API_KEY = 'YOUR_API_KEY_HERE'

# Configure headers
headers = {
    'apikey': API_KEY
}

def search_soundcloud(query: str, limit: int = 10) -> List[Dict]:
    """
    Search for tracks on SoundCloud
    
    Args:
        query: Track name or artist
        limit: Number of results
    
    Returns:
        List of tracks
    """
    print(f'\n=== Searching SoundCloud: "{query}" ===\n')
    
    params = {
        'q': query,
        'limit': limit
    }
    
    response = requests.get(f'{BASE_URL}/soundcloud/search', params=params, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    results = data['results']
    
    print(f"Found {data['total']} results:\n")
    
    for i, track in enumerate(results, 1):
        print(f"{i}. {track['title']}")
        print(f"   Artist ID: {track['artist']}")
        print(f"   Duration: {track['duration']}s")
        print(f"   Plays: {track['playback_count']:,}")
        print(f"   Likes: {track['likes_count']:,}")
        print(f"   URL: {track['permalink_url']}")
        print()
    
    return results

def search_one_track(query: str) -> Dict:
    """
    Search for a specific track (returns only the first result)
    
    Args:
        query: Track name or artist
    
    Returns:
        First track found
    """
    print(f'\n=== Searching One Track: "{query}" ===\n')
    
    params = {'q': query}
    
    response = requests.get(f'{BASE_URL}/soundcloud/search-one', params=params, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    track = data['result']
    
    print('✅ Track found:\n')
    print(f"Title: {track['title']}")
    print(f"Artist ID: {track['artist']}")
    print(f"Duration: {track['duration']}s")
    print(f"Plays: {track['playback_count']:,}")
    print(f"Likes: {track['likes_count']:,}")
    print(f"Genre: {track['genre']}")
    print(f"URL: {track['permalink_url']}")
    
    return track

def search_multiple_tracks(queries: List[str]) -> List[Dict]:
    """
    Search for multiple different tracks
    
    Args:
        queries: List of track names
    
    Returns:
        List of tracks found
    """
    print('\n=== Searching Multiple Tracks ===\n')
    
    all_results = []
    
    for query in queries:
        params = {'q': query}
        response = requests.get(f'{BASE_URL}/soundcloud/search-one', params=params, headers=headers)
        response.raise_for_status()
        
        result = response.json()['result']
        all_results.append(result)
        print(f"✅ Found: {result['title']}")
    
    print(f'\n📋 Total tracks found: {len(all_results)}')
    return all_results

def get_recommendations(query: str, count: int = 5) -> List[Dict]:
    """
    Get track recommendations based on a search
    
    Args:
        query: Track name or artist
        count: Number of recommendations
    
    Returns:
        List of recommended tracks
    """
    print(f'\n=== Getting {count} Recommendations for: "{query}" ===\n')
    
    params = {
        'q': query,
        'limit': count
    }
    
    response = requests.get(f'{BASE_URL}/soundcloud/search', params=params, headers=headers)
    response.raise_for_status()
    
    results = response.json()['results']
    
    print('🎵 Recommendations:\n')
    for i, track in enumerate(results, 1):
        print(f"{i}. {track['title']}")
        print(f"   Plays: {track['playback_count']:,} | Likes: {track['likes_count']:,}")
    
    return results

def download_track(url: str) -> Dict:
    """
    Download track from SoundCloud by URL
    
    Args:
        url: SoundCloud track URL
    
    Returns:
        Dictionary with download information
    """
    print('\n=== Downloading Track from SoundCloud ===\n')
    print(f'URL: {url}\n')
    
    params = {'url': url}
    
    response = requests.get(f'{BASE_URL}/soundcloud/download', params=params, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    
    if data['success']:
        download = data['data']
        print('✅ Download Ready!\n')
        print(f"Title: {download['title']}")
        print(f"Artist: {download['artist']}")
        print(f"Thumbnail: {download['thumbnail']}")
        print(f"\n📥 Download URL: {download['downloadUrl']}")
        
        return download
    
    return {}

def search_and_download(query: str) -> Dict:
    """
    Search and download track automatically
    
    Args:
        query: Track name or artist
    
    Returns:
        Dictionary with track and download information
    """
    print(f'\n=== Searching and Downloading: "{query}" ===\n')
    
    params = {'q': query}
    
    response = requests.get(f'{BASE_URL}/soundcloud/search-download', params=params, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    
    if data['success']:
        track = data['track']
        download = data['download']
        
        print('✅ Track Found and Download Ready!\n')
        print('🎵 Track Info:')
        print(f"   Title: {track['title']}")
        print(f"   Artist ID: {track['artist']}")
        print(f"   Duration: {track['duration']}s")
        print(f"   Plays: {track['playback_count']:,}")
        print(f"   Likes: {track['likes_count']:,}")
        print(f"   URL: {track['permalink_url']}")
        print('\n📥 Download Info:')
        print(f"   Title: {download['title']}")
        print(f"   Artist: {download['artist']}")
        print(f"   Thumbnail: {download['thumbnail']}")
        print(f"\n📥 Download URL: {download['downloadUrl']}")
        
        return {'track': track, 'download': download}
    
    return {}

def search_by_genre(genre: str, limit: int = 10) -> List[Dict]:
    """
    Search by genre and get top tracks
    
    Args:
        genre: Genre name
        limit: Number of results
    
    Returns:
        List of tracks from the genre
    """
    print(f'\n=== Searching {genre} tracks ===\n')
    
    params = {
        'q': genre,
        'limit': limit
    }
    
    response = requests.get(f'{BASE_URL}/soundcloud/search', params=params, headers=headers)
    response.raise_for_status()
    
    results = response.json()['results']
    
    print(f'🎵 Top {genre} Tracks:\n')
    for i, track in enumerate(results, 1):
        print(f"{i}. {track['title']}")
        print(f"   Genre: {track['genre']}")
        print(f"   Plays: {track['playback_count']:,}")
    
    return results

def get_trending_tracks(query: str, limit: int = 10) -> List[Dict]:
    """
    Get trending tracks based on play count
    
    Args:
        query: Search query
        limit: Number of results
    
    Returns:
        List of trending tracks
    """
    print(f'\n=== Getting Trending Tracks: "{query}" ===\n')
    
    params = {
        'q': query,
        'limit': limit
    }
    
    response = requests.get(f'{BASE_URL}/soundcloud/search', params=params, headers=headers)
    response.raise_for_status()
    
    results = response.json()['results']
    
    # Sort by playback count
    trending = sorted(results, key=lambda x: x['playback_count'], reverse=True)
    
    print('🔥 Trending Tracks:\n')
    for i, track in enumerate(trending, 1):
        print(f"{i}. {track['title']}")
        print(f"   Plays: {track['playback_count']:,}")
        print(f"   Likes: {track['likes_count']:,}")
    
    return trending

def download_multiple_tracks(queries: List[str]) -> List[Dict]:
    """
    Search and download multiple tracks
    
    Args:
        queries: List of track searches
    
    Returns:
        List of download results
    """
    print('\n=== Downloading Multiple Tracks ===\n')
    
    downloads = []
    
    for query in queries:
        try:
            result = search_and_download(query)
            downloads.append(result)
            print(f"✅ Downloaded: {result['download']['title']}")
            time.sleep(1)  # Delay to avoid rate limiting
        except Exception as e:
            print(f"❌ Failed to download: {query} - {str(e)}")
        
        print()
    
    print(f'\n📋 Downloaded {len(downloads)} tracks')
    return downloads

def create_playlist_from_searches(queries: List[str]) -> List[Dict]:
    """
    Create a playlist by searching for multiple tracks
    
    Args:
        queries: List of track searches
    
    Returns:
        List of tracks for the playlist
    """
    print('\n=== Creating Playlist ===\n')
    
    playlist = []
    
    for i, query in enumerate(queries, 1):
        print(f'Adding track {i}/{len(queries)}...')
        
        try:
            track = search_one_track(query)
            playlist.append(track)
            print(f'✅ Added: {track["title"]}\n')
        except Exception as e:
            print(f'❌ Failed to add: {query} - {str(e)}\n')
    
    print(f'\n📋 Playlist created with {len(playlist)} tracks')
    return playlist

# ===================
# EXAMPLES
# ===================

def main():
    try:
        # Example 1: Search for multiple tracks
        search_soundcloud('te vi de canto', 5)
        
        # Example 2: Search for a specific track
        search_one_track('te vi dançando')
        
        # Example 3: Search multiple different tracks
        queries = [
            'lofi hip hop',
            'deep house mix',
            'ambient music'
        ]
        search_multiple_tracks(queries)
        
        # Example 4: Get recommendations
        get_recommendations('electronic music', 5)
        
        # Example 5: Download track by URL
        download_track('https://soundcloud.com/jose-luiiz-ii/ro-rosa-te-vi-de-canto-prod')
        
        # Example 6: Search and download automatically (recommended!)
        search_and_download('te vi de canto')
        
        # Example 7: Search by genre
        search_by_genre('hip hop', 5)
        
        # Example 8: Get trending tracks
        get_trending_tracks('remix', 5)
        
        # Example 9: Create a playlist
        playlist_queries = [
            'lofi beats',
            'chill vibes',
            'study music'
        ]
        create_playlist_from_searches(playlist_queries)
        
        # Example 10: Download multiple tracks
        download_queries = [
            'te vi dançando',
            'electronic music',
            'hip hop beat'
        ]
        download_multiple_tracks(download_queries)
        
    except Exception as e:
        print(f'Error: {str(e)}')
        exit(1)

if __name__ == '__main__':
    main()
