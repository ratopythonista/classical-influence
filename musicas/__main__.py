import os

import pandas as pd

from classical_influence.modulos.predict import predict
from classical_influence.modulos.audio import split_music
from classical_influence.modulos.grafico import create_graph
from classical_influence.servicos.youtube import download_music


musicas = pd.read_csv('musicas/musicas.csv')
for row in musicas.iterrows():
    nome = row[1]['nome'] + ".wav"
    if nome not in os.listdir('musicas'):
        download_music(row[1]['link'], row[1]['nome'])

    predition = list()
    slices = split_music(f'musicas/{nome}', row[1]['inicio'], row[1]['duracao'])
    for index, music_slice in enumerate(slices):
        print(f"predição da fatia {index}")
        pred = predict(music_slice)
        predition.append(pred)
    create_graph(row[1]['nome'], predition)