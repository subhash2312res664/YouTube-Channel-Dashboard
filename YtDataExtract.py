import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError # Import HttpError for API-specific errors

# Set up your API key and channel ID

api_key = 'AIzaSyBgOYRcSAFemrr7WYNhW2yjusVTDztkjqg'
# channel_id = 'UC0T6MVd3wQDB5ICAe45OxaQ'  # WsCube Tech
channel_id = 'UC_x5XG1OV2P6uZZ5FSM9Ttw'  # Google Developer

# channel_id = 'UCd1Vb8O95eyCFh-7zDyLhvA' # Ar Anil Official

# --- Initialization ---
try:
    youtube = build('youtube', 'v3', developerKey=api_key)
    print("YouTube API service initialized successfully.")
except Exception as e:
    print(f"Error initializing YouTube API: {e}")
    exit() # Exit if API cannot be built

# --- Get Uploads playlist ID ---
uploads_playlist_id = None
try:
    print(f"Fetching content details for channel ID: {channel_id}...")
    channel_response = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    ).execute()

    if channel_response['items']:
        uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        print(f"Found uploads playlist ID: {uploads_playlist_id}")
    else:
        print(f"No channel found with ID: {channel_id} or no content details available.")
        exit()
except HttpError as e:
    print(f"API error fetching channel details: {e}")
    print("Please check your API key and ensure the channel ID is correct and accessible.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred while getting playlist ID: {e}")
    exit()


# --- Get videos from uploads playlist ---
videos = []
next_page_token = None
video_count = 0
print(f"Fetching videos from playlist: {uploads_playlist_id}...")

while True:
    try:
        playlist_response = youtube.playlistItems().list(
            part='snippet',
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for item in playlist_response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            title = item['snippet']['title']
            upload_date = item['snippet']['publishedAt']
            videos.append({'VideoID': video_id, 'Title': title, 'UploadDate': upload_date})
            video_count += 1

        next_page_token = playlist_response.get('nextPageToken')
        if not next_page_token:
            break
        print(f"Fetched {video_count} videos so far, fetching next page...")

    except HttpError as e:
        print(f"API error fetching playlist items: {e}")
        print("This might be due to API quota limits or network issues. Stopping video list fetch.")
        break # Stop if there's an API error
    except Exception as e:
        print(f"An unexpected error occurred while getting playlist videos: {e}")
        break

print(f"Finished fetching {len(videos)} video details from playlist.")

# --- Get statistics for each video ---
# Batching requests to optimize API quota usage and speed
# The API allows up to 50 video IDs per 'videos.list' request
statistics_data = {}
video_ids_to_fetch = [v['VideoID'] for v in videos]
print(f"Fetching statistics for {len(video_ids_to_fetch)} videos...")

for i in range(0, len(video_ids_to_fetch), 50):
    batch_ids = video_ids_to_fetch[i:i+50]
    try:
        stats_response = youtube.videos().list(
            part='statistics',
            id=','.join(batch_ids)
        ).execute()

        for item in stats_response['items']:
            video_id = item['id']
            stats = item['statistics']
            statistics_data[video_id] = {
                'Views': int(stats.get('viewCount', 0)),
                'Likes': int(stats.get('likeCount', 0)),
                'Dislikes': 'N/A', # Dislike count is not publicly available anymore
                'Comments': int(stats.get('commentCount', 0))
            }
        print(f"Fetched statistics for {len(statistics_data)} videos...")

    except HttpError as e:
        print(f"API error fetching statistics for batch starting with {batch_ids[0]}: {e}")
        print("This might be due to API quota limits or network issues. Continuing with next batch (if any).")
    except Exception as e:
        print(f"An unexpected error occurred while getting video statistics: {e}")

# Merge video details with statistics
for video in videos:
    stats = statistics_data.get(video['VideoID'], {})
    video['Views'] = stats.get('Views')
    video['Likes'] = stats.get('Likes')
    video['Dislikes'] = 'N/A' # Ensure this is set even if stats not found
    video['Comments'] = stats.get('Comments')

# Convert UploadDate to datetime objects for easier sorting/plotting
df = pd.DataFrame(videos)
df['UploadDate'] = pd.to_datetime(df['UploadDate'])
df = df.sort_values(by='UploadDate').reset_index(drop=True)


# --- Save to CSV or print ---
if not df.empty:
    print("\n--- Channel Data (First 5 Videos) ---")
    print(df.head())
    output_filename = 'youtube_channel_dataar.csv'
    df.to_csv(output_filename, index=False)
    print(f"\nData saved to {output_filename}")
else:
    print("\nNo data was retrieved. The DataFrame is empty.")
