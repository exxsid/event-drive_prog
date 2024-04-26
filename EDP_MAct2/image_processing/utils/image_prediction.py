import tensorflow as tf
from keras.preprocessing import image
from keras.models import load_model
import numpy as np

def predict_upload_image(file_name):
    model = load_model("trained_model/flower_recognition.keras")

    # Load and preprocess the separate image
    img_path = f"image_processing/static/media/{file_name}"
    img = image.load_img(img_path, target_size=(150, 150))  # Adjust target_size if needed
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.

    # Make predictions
    predictions = model.predict(img_array)

    # Classify the predictions
    class_labels = ['rose', 'sunflower']  # Adjust based on your class labels
    predicted_class = np.argmax(predictions)

    return {
        "category": class_labels[predicted_class],
        "accuracy": predictions[0][predicted_class]
    }
