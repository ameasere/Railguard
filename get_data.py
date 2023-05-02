# Detect the train data in the signal maps, and extract them to image
import random
import cv2
import os

training_folder = os.getcwd() + "/data/train/"
test_folder = os.getcwd() + "/data/validation/"

method = cv2.TM_SQDIFF_NORMED

signal_maps = os.listdir(os.getcwd() + "/signal_maps")
# Get file names in all subdirectories of the training folder
signals = []
for i in os.listdir(training_folder):
    if os.path.isdir(training_folder + "/" + i):
        for j in os.listdir(training_folder + "/" + i):
            signals.append(i + "/" + j)
    else:
        signals.append(i)
counter = 0
result_array = []
for signal_map in signal_maps:
    for i in signals:
        counter += 1
        if counter > 1:
            large_image = cv2.imread(result_array[0])
        else:
            large_image = cv2.imread(os.getcwd() + "/signal_maps/" + signal_map)
        # Read the images from the file
        small_image = cv2.imread(training_folder + "/" + i)
        result = cv2.matchTemplate(small_image, large_image, method)

        # We want the minimum squared difference
        mn, _, mnLoc, _ = cv2.minMaxLoc(result)

        # Draw the rectangle:
        # Extract the coordinates of our best match
        MPx, MPy = mnLoc

        # Step 2: Get the size of the template. This is the same size as the match.
        trows, tcols = small_image.shape[:2]

        # Step 3: Draw rectangle around the match.
        cv2.rectangle(large_image, (MPx, MPy), (MPx + tcols, MPy + trows), (0, 0, 255), 2)

        # Step 4: Save the area inside the rectangle as a new image, without the red portion
        cropped = large_image[MPy:MPy + trows, MPx:MPx + tcols]
        # Remove the red outer rectangle
        cropped[0:trows, 0:2] = [0, 0, 0]
        cropped[0:trows, tcols - 2:tcols] = [0, 0, 0]
        cropped[0:2, 0:tcols] = [0, 0, 0]
        cropped[trows - 2:trows, 0:tcols] = [0, 0, 0]
        cropped_image_name = "cropped_" + str(random.randint(0, 100000)) + ".png"
        cv2.imwrite(cropped_image_name, cropped)


        # Save to file
        result_file = "result_" + str(random.randint(0, 100000)) + ".png"
        result_array.append(result_file)
        cv2.imwrite(result_file, large_image)

        # The image is only displayed if we call this
        cv2.waitKey(0)
    result_array.clear()
    counter = 0
