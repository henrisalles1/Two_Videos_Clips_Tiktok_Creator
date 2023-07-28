from moviepy.editor import *
from moviepy.video.fx.crop import *
import os

DIR_CONTENT_VIDEOS = ''
PATH_RANDOM_VIDEO = ''

def cortes(video_conteudo, video_bosta, corte_inicio=5, corte_fim=5):
    raw_video_ale = VideoFileClip(video_bosta).without_audio()
    video_ale = raw_video_ale.resize((1080, 1320)).subclip(0, 60)

    raw_full_video = VideoFileClip(video_conteudo)
    video = crop(raw_full_video, x1=40, x2=1000)
    full_video = video.resize((1080, 600))

    # Cortando Video

    # Definindo Total De Cortes
    total_de_cortes = round(((full_video.duration - (corte_inicio + corte_fim))//60))
    if total_de_cortes >= 12:
        total_de_cortes += 1
        if total_de_cortes >= 25:
            total_de_cortes += 1

    # Criando Clipes
    start = 0
    final = 0
    for i in range(total_de_cortes):
        if i == 0:
            start = corte_inicio
            final = 60 + corte_inicio
        else:
            start += 55
            final += 55
        if os.path.isfile(f'C:\workspace\Criador de Videos\Cortador De Videos\Corte{i}.mp4'):
           print(f'Corte{i} já exitente, pulando Corte')
        else:
            clipe = full_video.subclip(start, final)
            if clipe.duration != 60:
                input(f'Corte{i} com {clipe.duration} segundos')
            video_final = clips_array([[clipe],
                                      [video_ale]])
            print(video_final.size)
            video_final.write_videofile(f'Corte{i}.mp4')


def main():
    directory = DIR_CONTENT_VIDEO
    video_ale = PATH_RANDOM_VIDEO
    for filename in os.listdir(directory):
        video = os.path.join(directory, filename)
        if os.path.isfile(video):
            cortes(video, video_ale)


main()
