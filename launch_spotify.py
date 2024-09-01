#!/usr/bin/env python3
import cgi
import cgitb
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Enable debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: text/html")
print()

try:
    # Spotify API credentials (replace with your actual credentials)
    CLIENT_ID = 'ce1df751b86848d3a10dc5c54669b5a0'
    CLIENT_SECRET = '66dd0ef40bd741b38f71a3cea3ff0068'

    # Initialize Spotify API client
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

    # Get user input from HTML form
    form = cgi.FieldStorage()
    song_name = form.getvalue('songName')

    if not song_name:
        print("Error: No song name provided.")
        exit()

    # Function to get Spotify URI based on song name
    def get_spotify_uri(song_name):
        results = sp.search(q=song_name, type='track', limit=1)
        tracks = results.get('tracks', {}).get('items', [])
        if tracks:
            return tracks[0]['uri']  # Return the URI of the first search result
        return None  # Return None if no song found

    # Generate response
    spotify_uri = get_spotify_uri(song_name)
    if spotify_uri:
        print(spotify_uri)
    else:
        print('Song not found.')

except Exception as e:
    print(f"Error: {e}")

