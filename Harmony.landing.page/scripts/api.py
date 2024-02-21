import requests

def fetch_recommended_songs():
    # Make a request to the external API to fetch recommended songs
    response = requests.get('https://api.spotify.com/v1/recommendations')
    if response.status_code == 200:
        return response.json()
    else:
        return None
