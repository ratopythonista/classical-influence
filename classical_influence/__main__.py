from modulos.predict import CNNModel
from modulos.audio import split_music
from servicos.youtube import download_music

music = download_music('https://www.youtube.com/watch?v=L3wKzyIN1yk')
slices = split_music(music)
cnnmodel = CNNModel()
for music_slice in slices:
    pred = cnnmodel.predict(music_slice)
    print(pred)