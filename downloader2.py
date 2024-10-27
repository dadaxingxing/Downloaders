import os
import yt_dlp

music_dir = music_store_dir = r'C:\Users\dadax\OneDrive\Desktop\Editing\Viral Music'

def download_audio(url):
    ydl_opts = {
        'formats': 'bestaudio/best',
        'outtmpl': os.path.join(music_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',    # Use ffmpeg to extract audio
            'preferredcodec': 'mp3',        # Convert to mp3
            'preferredquality': '192',      # Set bitrate to 192kbps
        }],
    }

    #download audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f'Downloading audio... link: {url}')
        ydl.download([url])

with open('link.txt') as videos:
    for video in videos:
        download_audio(video)
    print('Download Complete!')


