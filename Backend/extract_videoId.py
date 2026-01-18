import re

def extract_id(url):

    # Case 1: youtube.com
    if 'youtube.com' in url:
        match = re.search(r"v=([A-Za-z0-9_-]{11})", url)
        if match:
            return match.group(1)

    # Case 2: youtu.be
    if 'youtu.be' in url:
        match = re.search(r"youtu\.be/([A-Za-z0-9_-]{11})", url)
        if match:
            return match.group(1)
        
    return None

