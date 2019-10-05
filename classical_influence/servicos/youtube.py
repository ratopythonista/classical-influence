from uuid import uuid4

from pytube import YouTube
from loguru import logger


def progress_function(stream, chunk, file_handle, bytes_remaining):
    size = stream.filesize
    percent = int((size-bytes_remaining)/size * 100)
    logger.info(f'{stream.title} @ {percent} %')


def download_music(link):
    youtube = YouTube(link, on_progress_callback=progress_function)
    stream = youtube.streams.filter(only_audio=True).first()
    filename = str(uuid4())
    stream.download(filename=filename)
    return filename + '.mp4'