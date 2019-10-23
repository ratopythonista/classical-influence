import os
from uuid import uuid4

from pytube import YouTube
from loguru import logger


def progress_function(stream, chunk, file_handle, bytes_remaining):
    size = stream.filesize
    percent = int((size-bytes_remaining)/size * 100)
    logger.info(f'{stream.title} @ {percent} %')


def download_music(link, filename):
    youtube = YouTube(link, on_progress_callback=progress_function)
    stream = youtube.streams.filter(only_audio=True).first()
    stream.download(filename=filename)
    os.system(f'ffmpeg -i "{filename}.mp4" "musicas/{filename}.wav"')
    os.remove(f'{filename}.mp4')
    return filename + '.wav'