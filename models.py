import numpy as np
from sklearn.metrics import accuracy_score
from glob import glob
from sklearn.model_selection import KFold

from keras.utils.np_utils import to_categorical
from keras.layers import (
    Input,
    Conv1D,
    MaxPool1D,
    Flatten,
    Dense,
    Dropout,
    Embedding,
    Activation,
    BatchNormalization,
    Concatenate,
    SimpleRNN
)
from keras.models import Model
#from keras.callbacks import ModelCheckpoint
#from keras.metrics import top_k_categorical_accuracy as tkacc

def stf_rnn(nb_points, emb_size1, tm_length, emb_size2, window_size, rnn_size):

    s_input = Input((window_size, ), dtype='int32', name='S')
    t_input = Input((window_size, ), dtype='int32', name='T')

    emb1 = Embedding(nb_points + 1, emb_size1)
    emb2 = Embedding(tm_length + 1, emb_size2)

    xe = emb1(s_input) 
    he = emb2(t_input) 

    x = Concatenate()([xe, he])
    x = SimpleRNN(rnn_size)(x)
    y = Dense(nb_points, activation='softmax')(x) 

    model = Model([s_input, t_input], y)

    model.compile('adadelta', 'categorical_crossentropy', metrics=['accuracy'])

    return model


