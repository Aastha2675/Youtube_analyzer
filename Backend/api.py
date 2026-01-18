from dotenv import load_dotenv
import os
import requests
from extract_videoId import extract_id

load_dotenv()

sample_url = "https://www.youtube.com/watch?v=-0oPVEYSIGk"
video_id = extract_id(sample_url)

if video_id is None:
  print("Invalid URL")
  exit()

api = os.getenv("API_KEY")
url = "https://www.googleapis.com/youtube/v3/videos"

params = {
  "part": "snippet,statistics",
  "id": video_id,
  'key' : api
}

response = requests.get(url,params=params)

print(response.status_code)
print(response.json())