from moviepy.editor import VideoFileClip
from pytube import YouTube
import os
import re

#File directory for storing the .mp3 file
music_store_dir = r'C:\Users\dadax\OneDrive\Desktop\Editing Resource\Viral Music'
curr_working_dir = os.getcwd()

#Extract Audio from video
def extract_audio(name):
    audio_clip = VideoFileClip(f'{name}.mp4').audio
    audio_clip.write_audiofile(f'{name}.mp3')

    audio_clip.close()

#Download and return the name of the download video
def download_video(link):
    video = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    name = re.sub(r'[^\w\-_\. ]', '_', video.title)

    toDownload = video.streams.get_highest_resolution()
    toDownload.download(curr_working_dir, filename = f'{name}.mp4')
    
    return name

#Delete the video and put audio into right directory
def clean_files(name):
    new_dir = os.path.join(music_store_dir, f'{name}.mp3')

    os.remove(os.path.join(curr_working_dir, f'{name}.mp4'))
    os.replace(os.path.join(curr_working_dir, f'{name}.mp3'), new_dir)


with open('link.txt') as videos:
    for video in videos:
        name = download_video(video)

        extract_audio(name)
        clean_files(name)


print('Info: Finished Downloading!')