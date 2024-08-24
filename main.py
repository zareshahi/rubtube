from pytube import YouTube

def download_youtube_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()
        video.download()  # You can specify a path if needed: video.download('/path/to/save')
        print("Download completed!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
video_url = "https://www.youtube.com/watch?v=example"
download_youtube_video(video_url)
