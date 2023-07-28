from moviepy.editor import *

NAME_NEW_VID = f'{}.mp4'
PATH_RAW_VID = ''

video = VideoFileClip(PATH_RAW_VID).without_audio()
clipe = video.subclip(60, 120)
clipe.write_videofile(NAME_NEW_VID)
