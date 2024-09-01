#!/usr/bin/env python

import cv2
import os
import cgi
import cgitb
cgitb.enable()

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Replace with the path to your service account key file
SERVICE_ACCOUNT_KEY_FILE = 'C:/Users/pc/Downloads/service-account-key.json'

# Replace with your API key
API_KEY = 'AIzaSyAghKVzvRfY2uFsMzHJ8BkK3TECqN5Njvk'

# Replace with the ID of the album you want to upload the photo to
ALBUM_ID = 'AF1QipP1qEHN9j-Z8Cm2SVHnRppXuXXkUYlZ4FYcU2zu'

# Create credentials from service account key file
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_KEY_FILE)

# Create the Google Photos API client
service = build('photoslibrary', 'v1', credentials=creds, developerKey=API_KEY)

# Open the default camera
cap = cv2.VideoCapture(0)

# Capture a photo
ret, frame = cap.read()
if ret:
    # Save the photo to a temporary file
    cv2.imwrite('temp.jpg', frame)

    # Upload the photo to Google Photos
    media_file = MediaFileUpload('temp.jpg', mimetype='image/jpeg')
    response = service.mediaItems().insert(body={
        'newMediaItem': {
            'description': 'Uploaded from Live Camera',
            'filename': 'live_camera_photo.jpg',
            'contentType': 'image/jpeg',
        },
        'edia': media_file
    }).execute()

    print('Content-Type: text/plain')
    print('')
    print('Photo uploaded to Google Photos:', response)

    # Add the uploaded media item to the album
    service.mediaItems().batchAddMediaItemsToAlbum(ALBUM_ID, [response.data.id]).execute()

    print('Photo added to album:', ALBUM_ID)

else:
    print('Content-Type: text/plain')
    print('')
    print('Error capturing photo')
