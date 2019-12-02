import cv2
import os

for file in os.listdir("source"):
    image = cv2.imread("source/" + file, 1)
    resized = cv2.resize(image, (100, 100))
    cv2.imwrite("resized/100_100_" + file, resized)
