import cv2
import os

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

print(os.getcwd())
for file in os.listdir("faces"):
    image = cv2.imread("faces/" + file)
    grayscaled = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grayscaled, scaleFactor=1.1, minNeighbors=5)

    for x, y, w, h in faces:
        image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Detected " + file, image)
    cv2.waitKey(0)
    cv2.destroyWindow("Detected " + file)
