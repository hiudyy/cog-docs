import requests
import time
from typing import List, Dict, Optional
from urllib.parse import quote

BASE_URL = 'https://cog.api.br/api/v1'

def search_spotify(query: str, limit: int = 10) -> Dict:
    """
    Search for tracks on Spotify
    
    Args:
        query: Track name or artist
        limit: Number of results (default: 10, max: 50)
    
    Returns:
        Dictionary with search results
    """
    print(f'\n=== Searching Spotify: "{query}" ===\n')
    
    params = {
        'q': query,
        'limit': limit
    }
    
    response = requests.get(f'{BASE_URL}/spotify/search', params=params)
    response.raise_for_status()
    
    data = response.json()
    
    if data['success']:
        print(f"✅ Found {data['total']} results on {data['platform']}\n")
        
        for track in data['results']:
            print(f"{track['index']}. {track['name']}")
            print(f"   Artist(s): {track['artists']}")
            print(f"   Link: {track['link']}")
            print()
        
        return data['results']
    
    return []

def search_one_track(query: str) -> Optional[Dict]:
    """
    Search for a specific track (returns first result)
    
    Args:
        query: Track name or artist
    
    Returns:
        Dictionary with track info or None
    """
    print(f'\n=== Searching One Track: "{query}" ===\n')
    
    params = {'q': query}
    
    response = requests.get(f'{BASE_URL}/spotify/search-one', params=params)
    response.raise_for_status()
    
    data = response.json()
    
    if data['success']:
        result = data['result']
        print(f"✅ Found on {data['platform']}\n")
        print(f"Track: {result['name']}")
        print(f"Artist(s): {result['artists']}")
        print(f"Link: {result['link']}")
        
        return result
    
    return None

def search_multiple_tracks(queries: List[str]) -> List[Dict]:
    """
    Search for multiple tracks from different artists
    
    Args:
        queries: List of search queries
    
    Returns:
        List of results
    """
    print('\n=== Searching Multiple Tracks ===\n')
    
    results = []
    
    for query in queries:
        try:
            result = search_one_track(query)
            results.append({'query': query, 'result': result})
            
            # Small delay to avoid rate limiting
            time.sleep(0.5)
        except Exception as e:
            print(f'Failed to search: {query} - {str(e)}')
            results.append({'query': query, 'error': str(e)})
    
    return results

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
    
    response = requests.get(f'{BASE_URL}/spotify/search', params=params)
    response.raise_for_status()
    
    data = response.json()
    results = data['results']
    
    print('🎵 Recommendations:\n')
    for index, track in enumerate(results, 1):
        print(f"{index}. {track['name']} - {track['artists']}")
    
    return results

def create_playlist_from_searches(queries: List[str]) -> List[Dict]:
    """
    Create a playlist by searching multiple tracks
    
    Args:
        queries: List of track searches
    
    Returns:
        List of tracks for playlist
    """
    print('\n=== Creating Playlist ===\n')
    
    playlist = []
    
    for query in queries:
        try:
            track = search_one_track(query)
            if track:
                playlist.append(track)
                print(f"✅ Added: {track['name']} - {track['artists']}")
        except Exception as e:
            print(f"❌ Could not add: {query} - {str(e)}")
        
        time.sleep(0.5)
    
    print(f'\n📋 Playlist created with {len(playlist)} tracks')
    return playlist

def search_by_artist(artist: str, limit: int = 10) -> List[Dict]:
    """
    Search tracks by artist name
    
    Args:
        artist: Artist name
        limit: Number of results
    
    Returns:
        List of tracks from the artist
    """
    print(f'\n=== Searching tracks by {artist} ===\n')
    
    results = search_spotify(artist, limit)
    
    # Filter results that actually contain the artist name
    filtered = [
        track for track in results 
        if artist.lower() in track['artists'].lower()
    ]
    
    print(f'\nFiltered to {len(filtered)} tracks by {artist}')
    return filtered

def download_track(url: str) -> Dict:
    """
    Download track from Spotify by URL
    
    Args:
        url: Spotify track URL
    
    Returns:
        Dictionary with download information
    """
    print('\n=== Downloading Track from Spotify ===\n')
    print(f'URL: {url}\n')
    
    params = {'url': url}
    
    response = requests.get(f'{BASE_URL}/spotify/download', params=params)
    response.raise_for_status()
    
    data = response.json()
    
    if data['success']:
        download = data['data']
        print('✅ Download Ready!\n')
        print(f"Title: {download['title']}")
        print(f"Artists: {', '.join(download['artists'])}")
        print(f"Album: {download['year']}")
        print(f"Duration: {download['duration']}")
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
    
    response = requests.get(f'{BASE_URL}/spotify/search-download', params=params)
    response.raise_for_status()
    
    data = response.json()
    
    if data['success']:
        track = data['track']
        download = data['download']
        
        print('✅ Track Found and Download Ready!\n')
        print('🎵 Track Info:')
        print(f"   Name: {track['name']}")
        print(f"   Artists: {track['artists']}")
        print(f"   Link: {track['link']}")
        print('\n📥 Download Info:')
        print(f"   Title: {download['title']}")
        print(f"   Artists: {', '.join(download['artists'])}")
        print(f"   Album Image: {download['albumImage']}")
        print(f"   Year: {download['year']}")
        print(f"   Duration: {download['duration']}")
        print(f"\n📥 Download URL: {download['downloadUrl']}")
        
        return {'track': track, 'download': download}
    
    return {}

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

# ===================
# EXAMPLES
# ===================

def main():
    try:
        # Example 1: Search for multiple tracks
        search_spotify('te vi dançando', 5)
        
        # Example 2: Search for a specific track
        search_one_track('Bohemian Rhapsody Queen')
        
        # Example 3: Search multiple different tracks
        queries = [
            'Blinding Lights',
            'Shape of You',
            'Someone Like You Adele'
        ]
        search_multiple_tracks(queries)
        
        # Example 4: Get recommendations
        get_recommendations('acoustic guitar', 5)
        
        # Example 5: Create a playlist
        playlist_queries = [
            'Hotel California Eagles',
            'Stairway to Heaven Led Zeppelin',
            'Imagine John Lennon'
        ]
        create_playlist_from_searches(playlist_queries)
        
        # Example 6: Search by artist
        search_by_artist('Queen', 10)
        
        # Example 7: Download track by URL
        download_track('https://open.spotify.com/track/4irM0ZydWatEXDDC7SflXS')
        
        # Example 8: Search and download automatically (recommended!)
        search_and_download('te vi de canto')
        
        # Example 9: Download multiple tracks
        download_queries = [
            'te vi dançando',
            'Bohemian Rhapsody',
            'Imagine'
        ]
        download_multiple_tracks(download_queries)
        
    except Exception as e:
        print(f'Error: {str(e)}')
        exit(1)

if __name__ == '__main__':
    main()
