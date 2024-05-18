# 유튜브 동영상 다운

# from pytube import YouTube

# # URL of the YouTube video
# video_url = (
#     "https://www.youtube.com/watch?v=w7K_xPBbCIQ&ab_channel=%EC%A4%91%EA%B3%A0%EC%B0%A8%ED%8C%8C%EA%B4%B4%EC%9E%90"
# )

# # Create a YouTube object
# yt = YouTube(video_url)

# # Get the highest resolution stream available
# video_stream = yt.streams.get_highest_resolution()

# # Download the video
# video_stream.download(output_path=".", filename="downloaded_video.mp4")

# print("Video downloaded successfully")


# 네이버 라이브 커머스 다운
import requests
from bs4 import BeautifulSoup
import youtube_dl


def get_video_url(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.content, "html.parser")
    # 예시: 스크립트 태그 내에서 비디오 URL 찾기
    for script in soup.find_all("script"):
        if "videoUrl" in script.text:
            start = script.text.find("videoUrl") + len("videoUrl") + 3
            end = script.text.find('"', start)
            return script.text[start:end]
    return None


def download_video(video_url, output_path):
    ydl_opts = {"outtmpl": output_path, "format": "best"}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


page_url = "https://view.shoppinglive.naver.com/replays/46181?fm=shoppinglive&sn=home"
video_url = get_video_url(page_url)

if video_url:
    download_video(video_url, "downloaded_video.mp4")
    print("Video downloaded successfully.")
else:
    print("Failed to find video URL.")
