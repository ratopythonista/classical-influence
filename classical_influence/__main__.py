from loguru import logger

from modulos.predict import predict
from modulos.audio import split_music
from modulos.grafico import create_graph
from servicos.youtube import download_music

logger.add("classical_influence.log", rotation="500 MB")

predition = list()
slices = split_music(music, 5, 10)
for music_slice in slices:
    pred = predict(music_slice)
    print(pred)
    predition.append(pred)
create_graph(music_name, predition)
