import tensorflow as tf 
from keras.models import load_model
from keras.backend.tensorflow_backend import set_session

# solving problem with cuDNN
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
set_session(session)


def predict(music_slice):
    model = load_model(f'classical_influence/modelos/relu_64_100.h5')
    GENRE_LIST = ['baroque', 'classical', 'renaissance', 'romantic']
    result = model.predict(music_slice)
    return {GENRE_LIST[index]:value for index, value in enumerate(result[0])}