import instaloader

def download_reels(url):
    url = url.rstrip('/')
    loader = instaloader.Instaloader()
    shortcode = url.split('/')[-1]

    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target='downloaded_reels')
        print('Download successful!')
    except Exception as e:
        print('Error: could not download...')

with open('link.txt') as reels:
    for reel in reels:
        download_reels(reel)
    print('Download Complete.')