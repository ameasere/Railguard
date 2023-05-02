import tensorflow as tf
import os
import cv2
import numpy as np
model = tf.keras.models.load_model("model.h5")
image_path = os.getcwd() + "/signal_maps/img_10.png"
test_dir = os.getcwd() + "/data/validation/"
test_data = tf.keras.preprocessing.image_dataset_from_directory(test_dir, image_size=(224, 224), batch_size=12)
class_names = test_data.class_names
img_rgb = cv2.imread(image_path)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

signal_to_compare = os.getcwd() + "/templates/original.png"
signal_to_compare_90_clockwise = os.getcwd() + "/templates/rotate_right.png"
signal_to_compare_180_clockwise = os.getcwd() + "/templates/rotate_180.png"
signal_to_compare_270_clockwise = os.getcwd() + "/templates/rotate_left.png"

PC = os.getcwd() + "/templates/PC_original.png"
PC_90_clockwise = os.getcwd() + "/templates/PC_rotate_right.png"
PC_180_clockwise = os.getcwd() + "/templates/PC_rotate_180.png"
PC_270_clockwise = os.getcwd() + "/templates/PC_rotate_left.png"

# Initialize the list of templates and their corresponding labels
templates = []
labels = []

# Load the 4 templates and their labels
template_paths = [signal_to_compare, signal_to_compare_90_clockwise, signal_to_compare_180_clockwise, signal_to_compare_270_clockwise
                  , PC, PC_90_clockwise, PC_180_clockwise, PC_270_clockwise]
template_labels = ["normal", "rotated 90 clockwise", "rotated 180 clockwise", "rotated 270 clockwise", "PC", "PC rotated 90 clockwise", "PC rotated 180 clockwise", "PC rotated 270 clockwise"]
for template_path, template_label in zip(template_paths, template_labels):
    template = cv2.cvtColor(cv2.imread(template_path), cv2.COLOR_BGR2GRAY)
    templates.append(template)
    labels.append(template_label)

# Set the threshold for matching
threshold = 0.8

# Initialize the count of detected signals
count = 0

# Initialize the mask for marking already detected regions
mask = np.zeros(img_rgb.shape[:2], np.uint8)

# Loop over each template and match it with the image
for template, label in zip(templates, labels):
    # Get the shape of the template
    w, h = template.shape[::-1]
    # Match the template with the image
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    # Get the locations where the template matches the image with a confidence above the threshold
    loc = np.where(res >= threshold)
    # Loop over each location and draw a rectangle around the matched region
    for pt in zip(*loc[::-1]):
        # Check if the region has already been detected
        if mask[pt[1] + int(round(h / 2)), pt[0] + int(round(w / 2))] != 255:
            # Mark the region as detected
            mask[pt[1]:pt[1] + h, pt[0]:pt[0] + w] = 255
            # Resize the matched region to 224x224 pixels
            resized = cv2.resize(img_rgb[pt[1]:pt[1] + h, pt[0]:pt[0] + w], (224, 224))
            # Check if the resized region has the correct dimensions
            if resized.shape[0] != 224 or resized.shape[1] != 224:
                continue
            # Draw a rectangle around the matched region on the original image
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
            # Save the resized image to a file
            random = np.random.randint(0, 100000)
            cv2.imwrite('Detected' + str(random) + '.png', resized)
            # Load the image file and convert it to a numpy array
            img = tf.keras.preprocessing.image.load_img(os.getcwd() + "/Detected" + str(random) + ".png", target_size=(224, 224))
            img_array = tf.keras.preprocessing.image.img_to_array(img) / 255.0
            img_array = tf.expand_dims(img_array, 0)
            # Predict the class of the image
            predictions = model.predict(img_array)
            # Get the predicted class name
            predicted_class = class_names[np.argmax(predictions[0])]
            # Map the predicted class name to a shorthand label
            match predicted_class:
                case "danger":
                    label = "D"
                case "preliminary_caution":
                    label = "PC"
                case "caution":
                    label = "C"
                case "proceed":
                    label = "P"
            # Label it on the image
            cv2.putText(img_rgb, label, (pt[0], pt[1] - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (0, 255, 255), 2)
            count += 1
            os.remove(os.getcwd() + "/Detected" + str(random) + ".png")
        else:
            continue
print(str(count) + " signals have been detected.")
# Show the final image with the matched area.
cv2.imwrite('Detected.png', img_rgb)
