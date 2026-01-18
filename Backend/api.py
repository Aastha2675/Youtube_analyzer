from dotenv import load_dotenv
import os
import requests

load_dotenv()

api = os.getenv("API_KEY")

url = "https://www.googleapis.com/youtube/v3/videos"

params = {
  "part": "snippet,statistics",
  "id": "dQw4w9WgXcQ",
  'key' : api
}

response = requests.get(url,params=params)

print(response.status_code)
print(response.json())