#!/usr/bin/env python3
import cgi

# Print necessary headers
print("Content-Type: text/html")
print()

# Get user input from HTML form
form = cgi.FieldStorage()
song_name = form.getvalue('songName')

# Function to get Spotify URI based on song name (hardcoded for demonstration)
def get_spotify_uri(song_name):
    # Replace with actual implementation or Spotify API integration
    if song_name.lower() == 'despacito':
        return 'spotify:track:6habFhsOp2NvshLv26DqMb'  # Example Spotify URI for 'Despacito'
    # Add more songs and their Spotify URIs as needed
    return None  # Return None if song not found

# Redirect to Spotify URI or show error message
def redirect_to_spotify(song_name):
    spotify_uri = get_spotify_uri(song_name)
    if spotify_uri:
        print(f'<script>window.location.href = "{spotify_uri}";</script>')
    else:
        print('<p>Song not found.</p>')

# HTML content to display (optional, depending on use case)
print('<!DOCTYPE html>')
print('<html lang="en">')
print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<title>Redirecting to Spotify...</title>')
print('</head>')
print('<body>')
redirect_to_spotify(song_name)
print('</body>')
print('</html>')

