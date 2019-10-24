import os
import threading

import pandas as pd
from pydub import AudioSegment
from pydub.playback import play

from classical_influence.modulos.predict import predict
from classical_influence.modulos.audio import split_music
from classical_influence.modulos.grafico import create_graph
from classical_influence.servicos.youtube import download_music

def tocar_musica(music, start, duration):
    play(AudioSegment.from_wav(music)[start*1000:(start+duration)*1000])

musicas = pd.read_csv('musicas/musicas.csv')
for row in musicas.iterrows():
    nome = row[1]['nome'] + ".wav"
    if nome not in os.listdir('musicas'):
        download_music(row[1]['link'], row[1]['nome'])

    predition = list()
    slices = split_music(f'musicas/{nome}', row[1]['inicio'], row[1]['duracao'])
    thread1 = threading.Thread(target = tocar_musica, args = (f'musicas/{nome}', row[1]['inicio'], row[1]['duracao']))
    thread1.start()
    for index, music_slice in enumerate(slices):
        print(f"predição da fatia {index}")
        pred = predict(music_slice)
        predition.append(pred)
    create_graph(row[1]['nome'], predition)