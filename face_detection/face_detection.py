
# TODO ! $ pip3 install opencv-python

import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread("image.png", 0)

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (225, 0, 0), 2)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()
cv2.imwrite("face_detected.png")