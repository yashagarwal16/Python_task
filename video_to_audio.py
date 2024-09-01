#!/usr/bin/env python3
import cgi
import cgitb
import os
from moviepy.editor import VideoFileClip

cgitb.enable(display=1, logdir="/tmp/cgi-bin-logs")

UPLOAD_DIR = "/tmp/uploads"
OUTPUT_DIR = "/tmp/outputs"

# Create directories if they don't exist
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Content-Type: text/html\r\n\r\n")

def convert_video_to_audio(video_path, output_path):
    try:
        video_clip = VideoFileClip(video_path)
        if video_clip.audio is None:
            return False, "Error: The video file does not contain an audio track."
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_path)
        return True, "Conversion successful"
    except Exception as e:
        return False, f"Error: {str(e)}"

try:
    form = cgi.FieldStorage()
    file_item = form['file']

    if file_item.filename:
        file_path = os.path.join(UPLOAD_DIR, file_item.filename)
        
        with open(file_path, 'wb') as f:
            f.write(file_item.file.read())
        
        output_audio_path = os.path.join(OUTPUT_DIR, os.path.splitext(file_item.filename)[0] + ".mp3")
        success, message = convert_video_to_audio(file_path, output_audio_path)
        
        if success:
            print(f"<p>{message}</p>")
            print(f'<a href="/downloads/{os.path.basename(output_audio_path)}">Download Audio</a>')
        else:
            print(f"<p>{message}</p>")
    else:
        print("<p>No file uploaded</p>")
except Exception as e:
    print(f"<p>Error: {str(e)}</p>")

