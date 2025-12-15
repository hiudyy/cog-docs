import os
import requests
import time
from typing import List, Dict, Optional

API_KEY = os.getenv('COGNIMA_API_KEY', 'ck_your_api_key')
BASE_URL = 'https://cog.api.br/api/v1'


def get_service_info() -> Dict:
    """Get Free Fire Likes service information"""
    print('=== Free Fire Likes - Service Info ===\n')
    
    try:
        response = requests.get(
            f'{BASE_URL}/freefire/info',
            headers={'X-API-Key': API_KEY}
        )
        response.raise_for_status()
        
        data = response.json()
        print(f"Service: {data['service']}")
        print(f"Description: {data['description']}")
        print(f"Endpoint: {data['endpoint']}")
        print(f"\nMin Likes Required: {data['rules']['minLikes']}")
        print(f"Rule: {data['rules']['minLikesDescription']}")
        
        return data
    except requests.exceptions.HTTPError as e:
        print(f'Error: {e.response.json() if e.response else str(e)}')
        raise
    except Exception as e:
        print(f'Error: {str(e)}')
        raise


def send_likes(player_id: str) -> Dict:
    """
    Send likes to a Free Fire player
    
    Args:
        player_id: Player UID (8-10 digits)
    
    Returns:
        Response data dictionary
    """
    print(f'\n=== Sending Likes to Player {player_id} ===\n')
    
    try:
        response = requests.get(
            f'{BASE_URL}/freefire/sendlikes',
            params={'playerId': player_id},
            headers={'X-API-Key': API_KEY}
        )
        response.raise_for_status()
        
        result = response.json()
        success = result.get('success', False)
        data = result.get('data', {})
        message = result.get('message', '')
        
        if success:
            print('✅ Success!')
            print(f"Player: {data['player']}")
            print(f"UID: {data['uid']}")
            print(f"Region: {data['region']}")
            print(f"Level: {data['level']}")
            print(f"\nInitial Likes: {data['initialLikes']:,}")
            print(f"Final Likes: {data['finalLikes']:,}")
            print(f"Likes Added: {data['likesAdded']}")
            print(f"\nUsage Counted: {'Yes' if data['usageCounted'] else 'No'}")
            print(f"Status: {data['usageStatus']}")
            print(f"Key Stats: {data['keystats']}")
        else:
            print('❌ Failed')
            print(f"Error: {result.get('error', 'Unknown')}")
            print(f"Message: {message}")
            
            if data:
                print(f"\nPlayer: {data.get('player', 'N/A')}")
                print(f"Likes Added: {data.get('likesAdded', 0)} (less than {data.get('minLikesRequired', 100)} required)")
                print(f"Status: {data.get('usageStatus', 'N/A')}")
        
        return result
        
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            print('\n❌ Access Denied!')
            print('This endpoint requires an API key with daily limit > 500 requests.')
            print('Please upgrade to Unlimited or Bot plan.')
        elif e.response.status_code == 400:
            print('\n❌ Invalid Request!')
            error_data = e.response.json()
            print(error_data.get('message', 'Bad request'))
        else:
            print(f'\n❌ Error: {e.response.json() if e.response else str(e)}')
        raise
    except Exception as e:
        print(f'\n❌ Error: {str(e)}')
        raise


def send_likes_to_multiple_players(player_ids: List[str]) -> Dict[str, List[str]]:
    """
    Send likes to multiple players
    
    Args:
        player_ids: List of player UIDs
    
    Returns:
        Dictionary with successful, failed, and not counted player IDs
    """
    print(f'\n=== Sending Likes to {len(player_ids)} Players ===\n')
    
    results = {
        'successful': [],
        'failed': [],
        'not_counted': []
    }
    
    for player_id in player_ids:
        try:
            result = send_likes(player_id)
            
            if result.get('success') and result.get('data', {}).get('usageCounted'):
                results['successful'].append(player_id)
            elif result.get('success') and not result.get('data', {}).get('usageCounted'):
                results['not_counted'].append(player_id)
            else:
                results['failed'].append(player_id)
            
            # Wait 2 seconds between requests to avoid rate limiting
            time.sleep(2)
        except Exception:
            results['failed'].append(player_id)
    
    print('\n=== Summary ===')
    print(f"✅ Successful (counted): {len(results['successful'])}")
    print(f"⚠️  Successful (not counted): {len(results['not_counted'])}")
    print(f"❌ Failed: {len(results['failed'])}")
    
    return results


def main():
    """Example usage"""
    try:
        # Get service info
        get_service_info()
        
        # Send likes to a single player
        test_player_id = '1033857091'  # Replace with actual player UID
        send_likes(test_player_id)
        
        # Uncomment to send likes to multiple players
        # player_ids = ['1033857091', '1234567890', '9876543210']
        # send_likes_to_multiple_players(player_ids)
        
    except Exception:
        # Error already logged
        pass


if __name__ == '__main__':
    main()
