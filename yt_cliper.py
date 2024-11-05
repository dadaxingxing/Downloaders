import subprocess
import yt_dlp
import re


def download_youtube_segment(url, start_time, end_time, output_path="output_segment.mp4"):
    # Step 1: Get the direct video URL using yt-dlp
    ydl_opts = {
        'format': 'best',  # Select the best video quality
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_url = info_dict.get("url", None)
        if not video_url:
            print("Error: Unable to retrieve video URL.")
            return

    # Step 2: Use FFmpeg to stream and clip the video segment
    start_time_str = f"{int(start_time // 3600):02}:{int((start_time % 3600) // 60):02}:{int(start_time % 60):02}"


    command = [
        "ffmpeg",
        "-ss", start_time_str,       # Start time
        "-i", video_url,              # Input URL (YouTube video stream)
        "-t", str(end_time - start_time),  # Duration to keep
        "-c:v", "libx264",            # Video codec
        "-c:a", "aac",                # Audio codec
        "-strict", "experimental",
        "-loglevel", "error",         # Minimize FFmpeg output
        output_path
    ]

    # Run the FFmpeg command
    subprocess.run(command)

    print(f"Segment saved as {output_path}")


def clean_url(url):
    # Define a regex pattern to extract the video ID after 'v=' in the URL
    match = re.search(r"(?:v=|/)([a-zA-Z0-9_-]{11})", url)
    if match:
        video_id = match.group(1)
        # Return the cleaned URL with just the video ID
        return f"https://www.youtube.com/watch?v={video_id}"
    else:
        return None  # Return None if no video ID is found

repost_dir = r'C:\Users\dadax\OneDrive\Desktop\Instagram repost'

with open('link.txt', 'r') as infos:
    for id, info in enumerate(infos):
        url, start, end = info.split()
        url = clean_url(url)
        if not url:
            continue
        
        download_youtube_segment(url, int(start), int(end), f'{repost_dir}\\{id}_{start}_{end}.mp4')

    print('Download Complete.') 

