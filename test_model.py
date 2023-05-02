# Test the model and highlight the results

import tensorflow as tf
model = tf.keras.models.load_model("model.h5")
import os
import numpy as np
import matplotlib.pyplot as plt
test_dir = os.getcwd() + "/data/validation/"
test_data = tf.keras.preprocessing.image_dataset_from_directory(test_dir, image_size=(224, 224), batch_size=12)
class_names = test_data.class_names

image_count = 100

# Create a dictionary of paths to images and the class
images = {}
for class_name in class_names:
    images[test_dir + class_name] = os.listdir(test_dir + class_name)

success_count = 0

for i in range(image_count):
    # Pick random class and image
    class_name = np.random.choice(class_names)
    image_name = np.random.choice(images[test_dir + class_name])
    # Image path
    image_path = test_dir + class_name + "/" + image_name
    # Load the image
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
    # Convert the image to a numpy array
    img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0
    # Add a dimension to the image (since Keras expects batches of images)
    img_array = tf.expand_dims(img_array, 0)
    # Predict the class of the image
    predictions = model.predict(img_array)
    # Get the predicted class name
    predicted_class = class_names[np.argmax(predictions[0])]
    print("Actual class: " + class_name + " | Predicted class: " + predicted_class)
    if class_name == predicted_class:
        print(u"\u001b[32;1mPass! \u001b[0m")
        success_count += 1
    else:
        print(u"\u001b[31;1mFail! \u001b[0m")

percentage = str(round(success_count / image_count * 100, 2)) + "%"
if round(success_count/image_count, 2) >= 0.75:
    color = "\u001b[32;1m"
    rating = "Accurate"
elif round(success_count/image_count, 2) >= 0.5:
    color = "\u001b[33;1m"
    rating = "Average"
else:
    color = "\u001b[31;1m"
    rating = "Inaccurate"

print(f"Rating: {color} {rating} at {percentage} success. \u001b[0m")
