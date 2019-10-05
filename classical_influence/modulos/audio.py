import os

import librosa
import numpy as np
import soundfile as sf

def split_music(music):
    signal, sample_rating = librosa.load(music)
    os.remove(music)
    window_size = 5*sample_rating
    qtd_windons = len(signal)//(window_size)
    for slice_count in range(qtd_windons):
        start_slice = int(slice_count*window_size)
        end_slice = int((slice_count+1)*window_size)
        music_slice = signal[start_slice:end_slice]
        music_slice = np.abs(librosa.stft(music_slice))
        music_slice = music_slice.reshape(1, 1025, 216, 1)
        yield music_slice