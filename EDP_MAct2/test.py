import tensorflow as tf
from keras.preprocessing import image
from keras.models import load_model
import numpy as np

model = load_model('trained_model/flower_recognition.keras')