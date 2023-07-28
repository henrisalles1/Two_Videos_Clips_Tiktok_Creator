from pytube import YouTube


def download_video(link: str, dir:str):
    yt = YouTube(link, allow_oauth_cache=True, use_oauth=True)
    yt.streams.get_by_resolution('720p').download(dir)
    print('Download Concluido')


def download_list_videos(list_videos: list, dir: str):
    for video in list_videos:
        download_video(video, dir)


LINK_OF_VIDEO_YT = ''
DIR_CONTENT_VIDEOS = ''

download_video(LINK_OF_VIDEO_YT, DIR_CONTENT_VIDEOS)
