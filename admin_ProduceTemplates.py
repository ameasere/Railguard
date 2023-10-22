import cv2
import os

normal = os.getcwd() + "/templates/original.png"

PC = os.getcwd() + "/templates/PC_original.png"

angles = [45, 135, 225, 315]

for angle in angles:
    image = cv2.imread(PC)

    # Calculate the rotation matrix
    M = cv2.getRotationMatrix2D((image.shape[1] / 2, image.shape[0] / 2), angle, 1)

    # Perform the rotation
    rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    # Save the rotated image
    cv2.imwrite(f"pc_rotated_{angle}_degrees.jpg", rotated)
print("Done!")
