import requests
import numpy as np
import matplotlib.pyplot as plt

def create_graph(music_name, pred):
    fsize = 20
    barroco, classico, renasc, romant = list(), list(), list(), list()
    for music_slice in pred:
        barroco.append(int(round(music_slice['baroque']*100)))
        classico.append(int(round(music_slice['classical']*100)))
        renasc.append(int(round(music_slice['renaissance']*100)))
        romant.append(int(round(music_slice['romantic']*100)))

    qtd = len(pred)
    plt.figure()
    plt.tick_params(labelsize=fsize)
    plt_b = plt.bar(range(qtd), barroco, width = 0.50)
    plt_c = plt.bar(range(qtd), classico, width = 0.50, bottom=barroco)
    y_init = [ a+b for a, b in zip(classico, barroco) ]
    plt_re = plt.bar(range(qtd), renasc, width = 0.50, bottom=y_init)
    y_init = [ a+b for a, b in zip(renasc, y_init) ]
    plt_rb = plt.bar(range(qtd), romant, width = 0.50, bottom=y_init)
    plt.ylabel('Confiança', fontsize=fsize)
    plt.xlabel('Fatias', fontsize=fsize)
    plt.title(music_name.title())
    plt.xticks(np.arange(0, qtd, 5))
    plt.yticks(np.arange(0, 111, 10))
    plt.legend((plt_b, plt_c, plt_re, plt_rb), 
        ('Barroco', 'Classico', 'Renascentista', 'Romantico'))        
    plt.show()  