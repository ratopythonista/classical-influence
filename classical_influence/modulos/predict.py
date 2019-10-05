import tensorflow as tf 
from keras.models import load_model
from keras.backend.tensorflow_backend import set_session

# solving problem with cuDNN
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)
set_session(session)

class CNNModel:
    model = load_model(f'classical_influence/modelos/relu_64_100.h5')
    GENRE_LIST = ['baroque', 'classical', 'renaissance', 'romantic']

    def predict(self, music_slice):
        result = self.model.predict(music_slice)
        return {self.GENRE_LIST[index]:value for index, value in enumerate(result[0])}