import tensorflow as tf
import tensorflow_text as tf_text
import numpy as np
import os


def load_model(MODEL_PATH,model_type='EK'):
    print('loading model...')
    reloaded = tf.saved_model.load(MODEL_PATH)

    #warming up
    print('warming up...')

    if model_type == 'EK':
        test_input='how are you?'
    else:
        test_input='तूं कसो आसा?'

    test_output = reloaded(tf.constant(test_input)) #warmup
    print("testing...ignore this:",test_output.numpy().decode())
    del test_output

    print(f'Model {MODEL_PATH} loaded!')
    return reloaded

def translate_text(model, input_text):
    return model(tf.constant(input_text)).numpy().decode()
