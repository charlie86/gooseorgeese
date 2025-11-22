import sys
import json
import urllib.request
import urllib.parse
import re
import random

if len(sys.argv) < 2:
    print("Please provide a YouTube API key as the first argument.")
    print("Usage: python3 fetch_songs.py <YOUR_API_KEY>")
    sys.exit(1)

API_KEY = sys.argv[1]
BANDS = [
    { 'name': 'Goose', 'query': 'Goose band official video' },
    { 'name': 'Geese', 'query': 'Geese band official video' }
]
MAX_RESULTS = 40 # Fetch more to allow for filtering

def parse_duration(duration_str):
    """Parses ISO 8601 duration (e.g., PT4M13S) into seconds."""
    match = re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', duration_str)
    if not match:
        return 0
    
    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)
    
    return hours * 3600 + minutes * 60 + seconds

def get_video_details(video_ids, api_key):
    """Fetches content details (duration) for a list of video IDs."""
    if not video_ids:
        return {}
        
    ids_str = ",".join(video_ids)
    url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id={ids_str}&key={api_key}"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            parsed = json.loads(data)
            
            details = {}
            for item in parsed.get('items', []):
                duration_sec = parse_duration(item['contentDetails']['duration'])
                details[item['id']] = duration_sec
            return details
    except Exception as e:
        print(f"Error fetching video details: {e}")
        return {}

def search_youtube(query, api_key):
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={encoded_query}&type=video&maxResults={MAX_RESULTS}&key={api_key}"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            parsed = json.loads(data)
            return parsed.get('items', [])
    except Exception as e:
        raise e

def main():
    all_songs = []
    
    for band in BANDS:
        print(f"Fetching songs for {band['name']}...")
        try:
            items = search_youtube(band['query'], API_KEY)
            
            # Filter out obvious live versions, interviews, and wrong band
            filtered_items = []
            other_band = 'Geese' if band['name'] == 'Goose' else 'Goose'
            
            for item in items:
                title = item['snippet']['title'].lower()
                if 'live' in title or 'session' in title or 'concert' in title:
                    continue
                if 'interview' in title or 'review' in title or 'reaction' in title:
                    continue
                if 'teaser' in title or 'trailer' in title or 'full album' in title:
                    continue
                if other_band.lower() in title: # Avoid cross-contamination
                    continue
                    
                filtered_items.append(item)
            
            # Get video IDs to fetch details
            video_ids = [item['id']['videoId'] for item in filtered_items]
            video_details = get_video_details(video_ids, API_KEY)
            
            songs_added = 0
            for item in filtered_items:
                video_id = item['id']['videoId']
                duration = video_details.get(video_id, 0)
                
                # Skip if duration is too short (e.g. < 30s) or missing
                if duration < 30:
                    continue
                    
                # Calculate random start time
                # Ensure we have at least 15s of play time
                max_start = max(0, duration - 20) 
                start_time = random.randint(0, max_start)
                
                song = {
                    'id': f"{band['name'].lower()}-{video_id}",
                    'artist': band['name'],
                    'title': item['snippet']['title'],
                    'youtubeId': video_id,
                    'startTime': start_time,
                    'duration': 15,
                    'totalDuration': duration
                }
                all_songs.append(song)
                songs_added += 1
                
                if songs_added >= 30: # Cap at 30 clean songs per band
                    break
            
            print(f"Found {songs_added} songs for {band['name']}")
        except Exception as e:
            print(f"Error fetching for {band['name']}: {e}")

    with open('new_songs.json', 'w') as f:
        json.dump(all_songs, f, indent=2)
    print('Saved songs to new_songs.json')

if __name__ == "__main__":
    main()
