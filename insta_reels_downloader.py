import instaloader

def download_reels(url, target_dir = 'downloaded_reels'):
    url = url.rstrip('/')
    loader = instaloader.Instaloader(
        download_comments=False,
        download_video_thumbnails=False,
        download_geotags=False,
        download_pictures=False,
        download_videos=True,
        save_metadata=False,
        post_metadata_txt_pattern='',
    )
    shortcode = url.split('/')[-1]

    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        loader.dirname_pattern = target_dir
        loader.download_post(post, target_dir)
        print('Download successful!')
    except Exception as e:
        print(f'Error: could not download... Reasons: {e}')

#set to your own custom file directory in pc
repost_dir = r'C:\Users\dadax\OneDrive\Desktop\Instagram repost'

with open('link.txt', 'r') as reels:
    for reel in reels:
        reel = reel.strip()

        download_reels(reel, target_dir = repost_dir)

    print('Download Complete.') 